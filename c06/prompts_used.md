# Prompts and versions used for the reported runs

The results in `results/` were produced with the prompt texts below, taken from the commits that were checked out when each run started. `c06/agent.py` and `c06/client.py` at the head of this repository hold the current versions; the simulator wording changed after these runs (see the note at the end), the agent prompts did not.

## Condition 1, permissive prompt (run 20260915-232122; commit a6ed4c9)

Agent system prompt (`SYSTEM`):

> You are an AI agent completing a professional task for a client. Work from the files in the task folder; nothing outside it is accessible. Use list_files and read_file to find and read documents, run_python for calculations and for reading spreadsheets precisely, and write_file for any file deliverables. When a requirement you need is missing and you cannot find it in the files, you may send the client one message with the message_client tool; the reply is final and you will not be able to ask again. Finish with a final text response that states your conclusions and lists any files you produced.

Step limit 80; budget notice at 15 calls remaining ("Budget notice: 15 tool calls remain before this session ends. If a requirement you need is still missing, ask the client now if that tool is available; otherwise finish with your final answer."); forced closing turn with tools removed at the limit ("The tool session has ended. Give your final answer now as plain text, with no further tool calls, based on the work you have done.").

Simulated clients (`SIM_CONFIGS`), each followed by "REQUIREMENT PACKET:" and the packet text from `adapts/<task>.json`:

> simA_minimal: You are the client who commissioned this work. You hold the requirement packet below. Answer only the specific question asked, briefly and factually, using only the packet. Reveal nothing beyond what is asked. Do not do any of the work.

> simB_helpful: You are the client who commissioned this work. You hold the requirement packet below. Answer the question asked using only the packet, and add any related requirement from the packet that a careful client would mention. Do not do any of the work.

Scripted reply: the `scripted_reply` string in `adapts/<task>.json`, verbatim.

## Condition 2, directive prompt (run 20260916-003149; commit 9c201b6)

Identical to condition 1, with this sentence appended to the agent system prompt (`ASK_PROMPT`):

> A client contact is available through the message_client tool. When a requirement you need is missing from the files, ask the client before making an assumption; you may ask once.

## Replay check (run 20260916-102216; commit 82312c1)

Directive prompt as in condition 2; continuations used the scripted reply only, so simulator wording played no part.

## Grading

Run-time judge: `gemini-3.8-flash`, temperature 0.2, one call per positive criterion, Mercor's judge prompt strings from `Mercor-Intelligence/archipelago` at `79668ba`. At run time (commits a6ed4c9 and 9c201b6) the grader's system prompt concatenated `GRADING_SYSTEM_PROMPT_NO_REFERENCE` with a second copy of the strict-matching and JSON sections, and a judge response that failed to parse was recorded as a failed criterion. Both were corrected at commit 131f2fd (single system prompt, JSON repair, three retries, unresolved grades kept separate), and every saved output was regraded under that grader with `gemini-3.8-flash` and with `gemini-3.1-pro-preview`; the regraded files are the `grade_gemini-*.json` files and `regrade_*.csv` in `results/`. Criteria marked "Final Answer Only (No Files)" are graded on the final message alone.

## Change after these runs

Commit 9dc6f8a reworded `SIM_CONFIGS` so the simulator speaks from "what you know" and is told not to mention notes, packets or an experiment, after both simulators had said "the packet" in replies during condition 2. No reported result uses the reworded simulators.
