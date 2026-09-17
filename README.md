# C06 pilot

Pilot for a clarification track on APEX-Agents: one requirement is withheld from a public task, the agent gets a one-message client channel, its state is saved at first contact, and the continuation is branched across different client replies. Eight matched task pairs, three agent models, two prompt conditions.

## Results

| Asked on adapted / complete tasks | Gemini 3.8 Flash | Fable 5.1 | Qwen 3.8 Flash |
|---|---:|---:|---:|
| Asking permitted | 0/8 / 0/8 | 4/8 / 0/8 | 1/8 / 1/8 |
| Ask before assuming | 2/8 / 1/8 | not run | 3/8 / 3/8 |

Under the permissive prompt, average rubric scores on complete versus adapted tasks were 0.83 versus 0.42 for Gemini 3.8 Flash, 0.70 versus 0.54 for Fable 5.1, and 0.51 versus 0.33 for Qwen 3.8 Flash over the seven pairs with graded base runs, since one of its complete runs ended in contact (Flash judge; a second judge, Gemini 3.1 Pro, is recorded alongside). At one saved Qwen state, a simulator that withheld an unasked-for requirement produced scores of 0.5 in both continuations; replies supplying that requirement produced 1.0 in all four continuations.

`METHODS.md` has the design, per-task results for every run, the replay check, the practitioner reply, precision estimates from pilot variance, and the grading rules to pre-register. `results/` holds, per run, the results table, the agent's questions, the simulator replies, per-cell grades under both judges (rationales removed because they quote rubric text), and final answers:

| Folder | Model | Prompt |
|---|---|---|
| `pilot_default_20260915` | Gemini 3.8 Flash | permissive |
| `pilot_ask_20260916` | Gemini 3.8 Flash | directive |
| `replay_3m_20260916` | Gemini 3.8 Flash | directive; in-process versus save-and-restore continuations on one task |
| `subagent_fable_20260916` | Fable 5.1 | permissive |
| `qwen_default_20260916` | Qwen 3.8 Flash | permissive |
| `qwen_ask_20260917` | Qwen 3.8 Flash | directive |

One reply written by a finance practitioner (not the task author) was branched four times from a Gemini 3.8 Flash saved state on the 3M task: `pilot_ask_20260916/world223-smn-05-b00d08c1/adapted/practitioner_*`, with the reply text, results and grades under both judges alongside.

## Prompts and versions

- Agent: `c06/agent.py` (`SYSTEM`; `ASK_PROMPT` is the directive sentence).
- Simulated clients: `c06/client.py` (`SIM_CONFIGS`, plus the scripted reply from each adaptation). The Gemini runs used an earlier wording of `SIM_CONFIGS` that referred to a "requirement packet"; the Qwen runs used the current wording. Both texts, with the commit each run started from, are in `c06/prompts_used.md`.
- Grading: `c06/mercor_prompts.py`, Mercor's judge prompt strings from `Mercor-Intelligence/archipelago` at `79668ba`, applied in `c06/grader.py` with one judge call per positive criterion.
- Models: agents `gemini-3.8-flash`, `claude-fable-5-1`, `qwen/qwen3.8-flash`; simulators `gemini-3.8-flash`; judges `gemini-3.8-flash` and `gemini-3.1-pro-preview`.
- Fable 5.1 was run as a fresh agent instance per task with the same rules and task folders; its questions were answered with the scripted reply and continued once each, without simulators (`c06/subagent.py`).

## Setup

Python 3.12, `uv sync`. Keys go in `.env` or the environment, only for the models you run: `GOOGLE_API_KEY` for Gemini agents, simulators and judges (required, since the simulators and the run-time judge are Gemini); `OPENROUTER_API_KEY` for any model id containing a slash, such as `qwen/qwen3.8-flash` or `google/gemini-3.1-pro-preview`; `ANTHROPIC_API_KEY` for `claude-*` ids; `OPENAI_API_KEY` for `gpt-*` ids.

Task data is the gated dataset `mercor/apex-agents-v1.1` on Hugging Face: accept its terms, run `hf auth login`, and `c06/harbor.py` downloads what a run needs into `data/`. The adapted instructions are derived from that data and are not included; `adapts/build.py` shows how each one is produced.

## Run

```
MODEL=gemini-3.8-flash REPEATS=2 ./run_pilot.sh
ASK=1 MODEL=gemini-3.8-flash REPEATS=2 OUT=runs/pilot_ask ./run_pilot.sh
./.venv/bin/python -m c06.report runs/pilot/<stamp>
./.venv/bin/python -m c06.regrade runs/pilot/<stamp> --judge gemini-3.1-pro-preview
./.venv/bin/python -m c06.replay data/apex-agents-v1.1/tasks/<task> --ask-prompt --contacts 4
```

`run_pilot.sh` takes `MODEL` (agent), `JUDGE` (default `gemini-3.8-flash`), `REPEATS`, `OUT`, and `ASK=1` for the directive prompt.
