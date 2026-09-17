import json

import os

import re

import time

from dataclasses import dataclass, field


@dataclass

class Usage:

    prompt_tokens: int = 0

    output_tokens: int = 0

    cached_tokens: int = 0

    calls: int = 0

    price_in_per_m: float = 0.0

    price_out_per_m: float = 0.0


    def add(self, p, o, c=0):

        self.prompt_tokens += p

        self.output_tokens += o

        self.cached_tokens += c

        self.calls += 1


    def cost(self):

        return self.prompt_tokens / 1e6 * self.price_in_per_m + self.output_tokens / 1e6 * self.price_out_per_m


@dataclass

class FunctionCall:

    name: str

    args: dict

    id: str = ""


@dataclass

class Turn:

    text: str = ""

    calls: list = field(default_factory=list)


def extract_json(text):

    m = re.search(r"\{.*\}", text, re.S)

    if not m:

        raise ValueError("no json in response")

    return json.loads(m.group(0), strict=False)


def load_env():

    env = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")

    if os.path.exists(env):

        for line in open(env):

            if "=" in line and not line.startswith("#"):

                k, v = line.strip().split("=", 1)

                os.environ.setdefault(k, v)


class GeminiModel:

    def __init__(self, model, usage=None, temperature=0.2, seed=None):

        from google import genai

        from google.genai import types

        load_env()

        self.types = types

        self.client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

        self.model = model

        self.usage = usage or Usage()

        self.temperature = temperature

        self.seed = seed


    def _config(self, system, tools, json_mode):

        kw = dict(temperature=self.temperature, system_instruction=system)

        if self.seed is not None:

            kw["seed"] = self.seed

        if tools:

            kw["tools"] = [self.types.Tool(function_declarations=tools)]

            kw["automatic_function_calling"] = self.types.AutomaticFunctionCallingConfig(disable=True)

        if json_mode:

            kw["response_mime_type"] = "application/json"

        return self.types.GenerateContentConfig(**kw)


    def chat(self, system, contents, tools=None, json_mode=False):

        for attempt in range(5):

            try:

                r = self.client.models.generate_content(model=self.model, contents=contents, config=self._config(system, tools, json_mode))

                break

            except Exception as e:

                if attempt == 4:

                    raise

                time.sleep(2 ** attempt)

        u = r.usage_metadata

        self.usage.add(u.prompt_token_count or 0, u.candidates_token_count or 0, getattr(u, 'cached_content_token_count', 0) or 0)

        turn = Turn()

        cand = r.candidates[0] if r.candidates else None

        if cand and cand.content and cand.content.parts:

            for part in cand.content.parts:

                if getattr(part, "function_call", None):

                    fc = part.function_call

                    turn.calls.append(FunctionCall(fc.name, dict(fc.args or {})))

                elif getattr(part, "text", None):

                    turn.text += part.text

        return turn, (cand.content if cand else None)


    def user_content(self, text):

        return self.types.Content(role="user", parts=[self.types.Part.from_text(text=text)])


    def tool_result_content(self, name, result, call_id=None):

        return self.types.Content(role="user", parts=[self.types.Part.from_function_response(name=name, response={"result": result})])


    def pending_call_id(self, contents, name):

        return None


class StubModel:

    def __init__(self, usage=None):

        self.usage = usage or Usage()

        self.model = "stub"


    def chat(self, system, contents, tools=None, json_mode=False):

        self.usage.add(100, 20)

        if json_mode:

            last = contents[-1]["text"]

            met = "8%" in last or "8.0%" in last

            return Turn(text=json.dumps({"rationale": "stub", "is_criteria_true": met})), None

        kinds = [c.get("kind") for c in contents if isinstance(c, dict)]

        texts = {c.get("kind"): c.get("text", "") for c in contents if isinstance(c, dict)}

        names = [c.get("name") for c in contents if isinstance(c, dict)]

        turn = Turn()

        can_ask = tools is not None and any(d["name"] == "message_client" for d in tools)

        if "list_files" not in names:

            turn.calls.append(FunctionCall("list_files", {}))

        elif "read_file" not in names:

            turn.calls.append(FunctionCall("read_file", {"path": "brief.md"}))

        elif "wrote" not in kinds:

            brief = next((c["text"] for c in contents if isinstance(c, dict) and c.get("name") == "read_file"), "")

            reply = texts.get("client_reply", "")

            src = reply or brief

            val = re.search(r"(\d+(?:\.\d+)?)\s*%", src)

            if not val and can_ask and "client_reply" not in kinds:

                turn.calls.append(FunctionCall("message_client", {"message": "What discount rate should I use?"}))

            else:

                rate = val.group(1) if val else "10"

                turn.calls.append(FunctionCall("write_file", {"path": "memo.md", "content": f"Discount rate used: {rate}%\n"}))

        else:

            rate = re.search(r"(\d+(?:\.\d+)?)%", texts.get("wrote", ""))

            turn.text = "Final: memo written; see memo.md."

        return turn, None


    def user_content(self, text):

        return {"kind": "user", "text": text}


    def tool_result_content(self, name, result, call_id=None):

        kind = "client_reply" if name == "message_client" else ("wrote" if name == "write_file" else "tool")

        return {"kind": kind, "name": name, "text": str(result)}


def _merge_user_runs(messages):

    merged = []

    for m in messages:

        if merged and m["role"] == "user" and merged[-1]["role"] == "user":

            merged[-1] = {"role": "user", "content": list(merged[-1]["content"]) + list(m["content"])}

        else:

            merged.append({"role": m["role"], "content": list(m["content"]) if isinstance(m["content"], list) else m["content"]})

    return merged


class AnthropicModel:

    def __init__(self, model, usage=None, temperature=0.2, max_tokens=8192):

        import anthropic

        load_env()

        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

        self.model = model

        self.usage = usage or Usage()

        self.temperature = temperature

        self.max_tokens = max_tokens

        self.last_tools = None


    def _tools(self, tools):

        return [{"name": d["name"], "description": d["description"], "input_schema": d["parameters"]} for d in tools]


    def chat(self, system, contents, tools=None, json_mode=False):

        messages = _merge_user_runs(contents)

        if messages and messages[-1]["role"] == "user" and isinstance(messages[-1]["content"], list) and messages[-1]["content"]:

            last = dict(messages[-1]["content"][-1])

            last["cache_control"] = {"type": "ephemeral"}

            messages[-1] = {"role": "user", "content": messages[-1]["content"][:-1] + [last]}

        kw = dict(model=self.model, max_tokens=self.max_tokens, temperature=self.temperature, system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}], messages=messages)

        if tools:

            kw["tools"] = self._tools(tools)

            self.last_tools = kw["tools"]

        elif self.last_tools and any(isinstance(m["content"], list) and any(b.get("type") in ("tool_use", "tool_result") for b in m["content"]) for m in messages):

            kw["tools"] = self.last_tools

            kw["tool_choice"] = {"type": "none"}

        if json_mode:

            kw["system"][0]["text"] += "\nRespond with a single JSON object and nothing else."

        for attempt in range(5):

            try:

                r = self.client.messages.create(**kw)

                break

            except Exception as e:

                if "tool_choice" in kw and "tool_choice" in str(e):

                    kw.pop("tool_choice")

                    continue

                if attempt == 4:

                    raise

                time.sleep(2 ** attempt)

        u = r.usage

        cached = getattr(u, "cache_read_input_tokens", 0) or 0

        created = getattr(u, "cache_creation_input_tokens", 0) or 0

        self.usage.add((u.input_tokens or 0) + cached + created, u.output_tokens or 0, cached)

        turn = Turn()

        blocks = []

        for b in r.content:

            d = b.model_dump(exclude_none=True)

            blocks.append(d)

            if d.get("type") == "text":

                turn.text += d.get("text", "")

            elif d.get("type") == "tool_use":

                turn.calls.append(FunctionCall(d["name"], dict(d.get("input") or {}), d["id"]))

        return turn, {"role": "assistant", "content": blocks}


    def user_content(self, text):

        return {"role": "user", "content": [{"type": "text", "text": text}]}


    def tool_result_content(self, name, result, call_id=None):

        return {"role": "user", "content": [{"type": "tool_result", "tool_use_id": call_id or "", "content": str(result)}]}


    def pending_call_id(self, contents, name):

        answered = {b["tool_use_id"] for m in contents if m["role"] == "user" and isinstance(m["content"], list) for b in m["content"] if b.get("type") == "tool_result"}

        for m in reversed(contents):

            if m["role"] == "assistant":

                for b in m["content"]:

                    if b.get("type") == "tool_use" and b["name"] == name and b["id"] not in answered:

                        return b["id"]

        return None


class OpenAIModel:

    def __init__(self, model, usage=None, temperature=0.2):

        import openai

        load_env()

        if "/" in model:

            self.client = openai.OpenAI(api_key=os.environ["OPENROUTER_API_KEY"], base_url="https://openrouter.ai/api/v1")

        else:

            self.client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

        self.model = model

        self.usage = usage or Usage()

        self.temperature = temperature

        self.use_temperature = True


    def _tools(self, tools):

        return [{"type": "function", "function": {"name": d["name"], "description": d["description"], "parameters": d["parameters"]}} for d in tools]


    def chat(self, system, contents, tools=None, json_mode=False):

        messages = [{"role": "system", "content": system}] + list(contents)

        kw = dict(model=self.model, messages=messages)

        if self.use_temperature:

            kw["temperature"] = self.temperature

        if tools:

            kw["tools"] = self._tools(tools)

            kw["parallel_tool_calls"] = False

        if json_mode:

            kw["response_format"] = {"type": "json_object"}

        for attempt in range(5):

            try:

                r = self.client.chat.completions.create(**kw)

                break

            except Exception as e:

                msg = str(e)

                if "temperature" in msg and self.use_temperature:

                    self.use_temperature = False

                    kw.pop("temperature", None)

                    continue

                if "parallel_tool_calls" in msg and "parallel_tool_calls" in kw:

                    kw.pop("parallel_tool_calls")

                    continue

                if attempt == 4:

                    raise

                time.sleep(2 ** attempt)

        u = r.usage

        cached = 0

        details = getattr(u, "prompt_tokens_details", None)

        if details is not None:

            cached = getattr(details, "cached_tokens", 0) or 0

        self.usage.add(u.prompt_tokens or 0, u.completion_tokens or 0, cached)

        m = r.choices[0].message

        turn = Turn(text=m.content or "")

        raw = {"role": "assistant", "content": m.content or ""}

        if m.tool_calls:

            raw["tool_calls"] = []

            for tc in m.tool_calls:

                try:

                    args = json.loads(tc.function.arguments or "{}")

                except Exception:

                    args = {}

                turn.calls.append(FunctionCall(tc.function.name, args, tc.id))

                raw["tool_calls"].append({"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments or "{}"}})

        return turn, raw


    def user_content(self, text):

        return {"role": "user", "content": text}


    def tool_result_content(self, name, result, call_id=None):

        return {"role": "tool", "tool_call_id": call_id or "", "content": str(result)}


    def pending_call_id(self, contents, name):

        answered = {m.get("tool_call_id") for m in contents if m.get("role") == "tool"}

        for m in reversed(contents):

            if m.get("role") == "assistant" and m.get("tool_calls"):

                for tc in m["tool_calls"]:

                    if tc["function"]["name"] == name and tc["id"] not in answered:

                        return tc["id"]

        return None


def make_model(name, usage=None, stub=False):

    if stub:

        return StubModel(usage=usage)

    low = name.lower()

    if low.startswith("claude"):

        return AnthropicModel(name, usage=usage)

    if low.startswith(("gpt", "o1", "o3", "o4", "chatgpt")) or "/" in low:

        return OpenAIModel(name, usage=usage)

    return GeminiModel(name, usage=usage)
