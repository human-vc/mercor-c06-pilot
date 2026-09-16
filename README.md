# C06 pilot: a clarification track for APEX-Agents, lite harness

Code, prompts and results for a small pilot behind a Mercor Research Fellowship proposal: adapt public APEX-Agents 1.1 tasks by withholding one requirement, give the agent a one-message client channel, save its state at first contact, branch the continuation across different client replies, and grade with Mercor's pinned judge prompts. Eight matched task pairs, Gemini 3.8 Flash, two prompt conditions. It is an implementation and simulator-sensitivity demonstration, not a scaled-down version of the proposed study: there is no task author in the loop and this is not Mercor's official environment.

Full write-up, including task selection, results under two judges, grading corrections and limitations: [PLAN.md](PLAN.md). Exact source commit of the private working repository: [SOURCE_COMMIT](SOURCE_COMMIT).

## Results in brief

| Pilot condition | Asked: adapted tasks | Asked: complete tasks |
|---|---:|---:|
| Asking permitted | 0/8 | 0/8 |
| Ask before assuming | 2/8 | 1/8 |

Under the permissive prompt, average rubric scores were 0.83 on complete tasks versus 0.42 (Flash judge) or 0.40 (Pro judge) on adapted tasks. Exploratory, six informative pairs: criteria tied to the removed requirement went from 18/20 met to 6/20 under both judges; other criteria stayed at 6/6 or 5/6. A replay check on one task (four contacts) gave identical paired scores for in-process and save-and-restore continuations. Details, per-task tables, judge disagreements (43 of 47 scored outputs agree) and the grading repair are in PLAN.md.

## What is here

- `c06/agent.py`: agent loop and system prompt, including the permissive and directive prompt variants (`SYSTEM`, `ASK_PROMPT`), the step budget notice and the forced closing turn.
- `c06/tools.py`, `c06/sandbox.py`: file tools, a `run_python` tool under an audit-hook sandbox (file access confined to the task folder; no subprocess, socket, ctypes symbol lookup, or chdir out).
- `c06/client.py`: the two simulator instructions (`SIM_CONFIGS`) and the scripted reply. The runs in `results/` used an earlier wording that said "requirement packet"; the current wording says "what you know" and instructs the simulator not to mention notes or an experiment.
- `c06/grader.py`, `c06/mercor_prompts.py`: grading with Mercor's judge prompt strings copied verbatim from `Mercor-Intelligence/archipelago` at commit `79668ba` (`grading/runner/evals/output_llm/utils/prompts.py`; the file's comments are removed here, the prompt constants are unchanged). One judge call per positive criterion; negative criteria disabled, as in the pinned harness. JSON repair, three retries, unresolved grades kept separate from failures.
- `c06/state.py`: save and restore of the task folder (APFS clone copies), the transcript and the model-content JSON, each hashed and verified on restore.
- `c06/harbor.py`: adapter from an APEX-Agents task directory plus `adapts/<task>.json` to the runner.
- `c06/run.py`, `run_pilot.sh`: the matched-pair runner. `c06/replay.py`: uninterrupted-versus-restored continuation check. `c06/regrade.py`: regrade saved outputs with any judge. `c06/human.py`: continue a saved state with a reply written by a person. `c06/report.py`: REPORT.md from a run folder.
- `adapts/`: the eight adaptations. Packets (what the simulated client knows), scripted replies, paraphrased removals and linked-criteria indices are included; the verbatim instruction fragments and adapted instruction texts are redacted because the dataset is gated (see below). `adapts/build.py` shows the exact find-and-replace structure.
- `results/`: results CSVs, summaries, REPORT.md files, the agent's questions (`meta.json`), the simulator replies (`replies.json`), per-cell grades under both judges with rationales removed (they quote rubric text), and the replay check.
- `budget.py`: the prediction-powered-inference calculator used in the proposal's planning.

## Versions

- Agent and simulator model: `gemini-3.8-flash` (temperature 0.2). Judges: `gemini-3.8-flash` (run time and repaired regrade) and `gemini-3.1-pro-preview` (second regrade).
- Judge prompts: archipelago `79668ba`.
- Python 3.12; dependencies in `pyproject.toml` (`google-genai`, `openpyxl`, `python-docx`, `python-pptx`, `pypdf`, `pandas`, `huggingface_hub`). Install with `uv sync`.

## Running it

1. Accept the terms of the gated dataset `mercor/apex-agents-v1.1` on Hugging Face and run `hf auth login`. Task text files, task data and world filesystems are downloaded on demand into `data/` (gitignored) by `c06/harbor.py`; `c06/run.py` expects `data/apex-agents-v1.1/tasks/<task>/`.
2. Put `GOOGLE_API_KEY=...` in `.env` (gitignored) or the environment.
3. Rebuild the adaptations from the original instructions with your own copy of `adapts/build.py` find-and-replace strings (the redacted fields), then:

```
./.venv/bin/python -m c06.run --stub --harbor data/apex-agents-v1.1/tasks/<task> --repeats 1 --out runs/stub
REPEATS=2 ./run_pilot.sh                      # permissive prompt
ASK=1 REPEATS=2 OUT=runs/pilot_ask ./run_pilot.sh   # directive prompt
./.venv/bin/python -m c06.report runs/pilot/<stamp>
./.venv/bin/python -m c06.regrade runs/pilot/<stamp> --judge gemini-3.1-pro-preview
./.venv/bin/python -m c06.replay data/apex-agents-v1.1/tasks/<task> --ask-prompt --contacts 4
```
