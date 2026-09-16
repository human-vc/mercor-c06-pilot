import json

from pathlib import Path


from .state import save_state

from .tools import Toolbox, declarations


SYSTEM = """You are an AI agent completing a professional task for a client. Work from the files in the task folder; nothing outside it is accessible. Use list_files and read_file to find and read documents, run_python for calculations and for reading spreadsheets precisely, and write_file for any file deliverables. When a requirement you need is missing and you cannot find it in the files, you may send the client one message with the message_client tool; the reply is final and you will not be able to ask again. Finish with a final text response that states your conclusions and lists any files you produced."""


MAX_STEPS = 80

WARN_AT = 15


ASK_PROMPT = " A client contact is available through the message_client tool. When a requirement you need is missing from the files, ask the client before making an assumption; you may ask once."


def run_agent(model, task_text, workdir, transcript=None, contents=None, client_reply=None, allow_contact=True, log=None, ask_prompt=False):

    system = SYSTEM + (ASK_PROMPT if ask_prompt else "")

    tb = Toolbox(workdir)

    tools = [d for d in declarations() if allow_contact or d["name"] != "message_client"]

    transcript = list(transcript or [])

    if contents is None:

        contents = [model.user_content(task_text)]

        transcript.append({"role": "user", "text": task_text})

    else:

        contents = list(contents)

    if client_reply is not None:

        contents.append(model.tool_result_content("message_client", client_reply))

        transcript.append({"role": "tool", "name": "message_client", "result": client_reply})

    final_text = ""

    step = 0

    for step in range(MAX_STEPS):

        turn, raw = model.chat(system, contents, tools=tools)

        if raw is not None:

            contents.append(raw)

        if turn.text and not turn.calls:

            final_text = turn.text

            transcript.append({"role": "assistant", "text": turn.text})

            break

        if not turn.calls:

            transcript.append({"role": "assistant", "text": ""})

            contents.append(model.user_content("Continue. If you are finished, reply with your final answer as text."))

            continue

        for call in turn.calls:

            transcript.append({"role": "assistant", "call": call.name, "args": call.args})

            if call.name == "message_client":

                message = call.args.get("message", "")

                return {"status": "contacted", "message": message, "transcript": transcript, "contents": contents, "writes": tb.changed_files(), "steps": step + 1}

            fn = getattr(tb, call.name, None) if call.name in {d["name"] for d in declarations()} else None

            try:

                result = fn(**call.args) if fn else f"ERROR: unknown tool {call.name}"

            except Exception as e:

                result = f"ERROR: {type(e).__name__}: {e}"

            transcript.append({"role": "tool", "name": call.name, "result": str(result)[:4000]})

            contents.append(model.tool_result_content(call.name, result))

            if log:

                log(f"  step {step+1}: {call.name}({', '.join(f'{k}={str(v)[:40]!r}' for k, v in call.args.items())})")

        remaining = MAX_STEPS - step - 1

        if remaining == WARN_AT:

            notice = f"Budget notice: {remaining} tool calls remain before this session ends. If a requirement you need is still missing, ask the client now if that tool is available; otherwise finish with your final answer."

            contents.append(model.user_content(notice))

            transcript.append({"role": "user", "text": notice})

    status = "done" if final_text else "no_final"

    if not final_text:

        closing = "The tool session has ended. Give your final answer now as plain text, with no further tool calls, based on the work you have done."

        contents.append(model.user_content(closing))

        transcript.append({"role": "user", "text": closing})

        turn, raw = model.chat(system, contents, tools=None)

        if raw is not None:

            contents.append(raw)

        if turn.text:

            final_text = turn.text

            status = "done_forced"

            transcript.append({"role": "assistant", "text": turn.text})

    return {"status": status, "final": final_text, "transcript": transcript, "contents": contents, "writes": tb.changed_files(), "steps": step + 1}
