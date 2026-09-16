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

    if "GOOGLE_API_KEY" in os.environ:

        return

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


    def tool_result_content(self, name, result):

        return self.types.Content(role="user", parts=[self.types.Part.from_function_response(name=name, response={"result": result})])


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


    def tool_result_content(self, name, result):

        kind = "client_reply" if name == "message_client" else ("wrote" if name == "write_file" else "tool")

        return {"kind": kind, "name": name, "text": str(result)}
