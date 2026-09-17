# C06 pilot

Pilot for a clarification track on APEX-Agents: one requirement is withheld from a public task, the agent gets a one-message client channel, its state is saved at first contact, and the continuation is branched across different client replies. Eight matched task pairs, Gemini 3.8 Flash, two prompt conditions.

## Results

| Asked on adapted / complete tasks | Gemini 3.8 Flash | Fable 5.1 | Qwen 3.8 Flash |
|---|---:|---:|---:|
| Asking permitted | 0/8 / 0/8 | 4/8 / 0/8 | 1/8 / 1/8 |
| Ask before assuming | 2/8 / 1/8 | not run | 3/8 / 3/8 |

Under the permissive prompt, average rubric scores on complete versus adapted tasks were 0.83 versus 0.42 for Gemini 3.8 Flash, 0.70 versus 0.54 for Fable 5.1, and 0.51 versus 0.33 for Qwen 3.8 Flash (Flash judge; a second judge, Gemini 3.1 Pro, is recorded alongside). Per-task scores, questions, simulator replies, grades under both judges and the replay check are in `results/`.

## Prompts

- Agent: `c06/agent.py` (`SYSTEM`; `ASK_PROMPT` is the directive variant).
- Simulated clients: `c06/client.py` (`SIM_CONFIGS`, scripted reply).
- Grading: `c06/mercor_prompts.py`, Mercor's judge prompt strings from `Mercor-Intelligence/archipelago` at `79668ba`; one judge call per positive criterion, applied in `c06/grader.py`.
- Models: `gemini-3.8-flash` (agent, simulators, first judge), `claude-fable-5-1` and `qwen/qwen3.8-flash` (agents), `gemini-3.1-pro-preview` (second judge).
- The prompt texts and commits behind the reported runs are in `c06/prompts_used.md`. The simulator wording in `c06/client.py` was revised after those runs and has not been used for any reported result.

## Setup

Python 3.12, `uv sync`. Put `GOOGLE_API_KEY` in `.env` or the environment.

Task data is the gated dataset `mercor/apex-agents-v1.1` on Hugging Face: accept its terms, run `hf auth login`, and `c06/harbor.py` downloads what a run needs into `data/`. The adapted instructions are derived from that data and are not included; `adapts/build.py` shows how each one is produced.

## Run

```
REPEATS=2 ./run_pilot.sh
ASK=1 REPEATS=2 OUT=runs/pilot_ask ./run_pilot.sh
./.venv/bin/python -m c06.report runs/pilot/<stamp>
./.venv/bin/python -m c06.regrade runs/pilot/<stamp> --judge gemini-3.1-pro-preview
./.venv/bin/python -m c06.replay data/apex-agents-v1.1/tasks/<task> --ask-prompt --contacts 4
```
