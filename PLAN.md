# C06 pilot: implementation and simulator-sensitivity demonstration

Pitch draft: `~/Downloads/mercor_C06_pitch_v5.md` (section 2b is the current one-pager; section 6 mirrors this plan).

## Status (2026-09-15, evening)

Built and passing on engineering examples and on one real world (stub agent): `c06/` holds the agent loop (`agent.py`), tools (`tools.py`: list_files, read_file, run_python, write_file, message_client), state save and restore with hash checks (`state.py`, APFS clone copies), two simulator configs (`client.py`), the grader with Mercor's pinned judge prompts (`grader.py`, `mercor_prompts.py`), the APEX task adapter (`harbor.py`) and the runner (`run.py`). `adapts/build.py` records every removal as an exact find-and-replace on the original `instruction.md` and emits `adapts/<task>.json` (adapted instruction, requirement packet, scripted reply, linked criteria).

Grading note: in the pinned harness `NEGATIVE_CRITERIA_ENABLED = False`, so each criterion is one judge call on the positive criterion text, scored 1 or 0; Mean Score is the plain average. Runs that hit the step limit without a final answer are graded as an empty answer.

Containment note: the first real-model smoke run (Sept 15, 22:46) is void. The agent's script called `os.listdir('..')`, learned the repository path from its working directory, then read the adaptation file (packet and scripted reply), the grader, the task's solution folder and the grading criteria before asking the client. Since then `run_python` executes under an audit-hook sandbox (`sandbox.py`: file access only inside the task folder and the interpreter's own install; no subprocess, socket, ctypes, or chdir out), and task folders are materialized under a neutral temporary path that reveals neither the repository nor the task id. Any run is void unless it was produced with both in place.

Agent capability note: the agent has a `run_python` tool (subprocess in the task folder, 180 s limit) because several banking tasks require reading formula workbooks and recomputing; without it a Flash-class model would fail both variants and the comparison would carry no signal. The official harness gives agents code execution and app servers too, so this is closer to it, not further.

## Task selection (eight matched pairs)

Screened 240 tasks (a subagent read 76 in detail); I verified each pick against the world filesystem to confirm the removed fact does not also appear in any file the agent can read.

| Task | Domain | Removed requirement (instruction only) | Linked criteria |
|---|---|---|---|
| 128-jr-1 | Consulting | use the worst case option when translating the v2 framework's qualitative ranges to ideal ratings | 6 of 6 |
| world-129-cy-task-3 | Consulting | use the midpoint of the Company Size range as the user count | 4 of 4 |
| world-134-rg-04 | Consulting | market share lost by TrainIQ is fully captured by CompliSure | 6 of 6 |
| lawworld433-anb-01 | Law | each Complaint was served ten days after filing (complaints carry no service dates) | 2 of 3 |
| lawworld417-ne-06 | Law | the group health plan's coverage-through-month-end and amendment terms (no plan document in the world) | 1 of 6 |
| world223-smn-05 | Banking | pay down debt to a 2.60x debt to equity ratio, remainder to buybacks (no 2.60 in the model) | 4 of 4 |
| world-225-je-01 | Banking | the cap rate value, 5.5% (kept "based on the REIT industry capitalization rate"; no cap rate cell in the workbook) | 2 of 2 |
| world-221-hy-05 | Banking | set the merger model to the 9M TTM 2025 account (the model's Financial Account input defaults to 2024) | 5 of 5 |

Rejected after inspection: world130-al (the normal scrap rate cancels out of the Adjusted Cost of Instability formula, so the removal would not change the answer), task-ncwq9a4b and world132-sf-task03 (removal leaves the task fully specified, so there is nothing to ask about), world-421-anb-02 (the removable sentence is a source restriction, not a requirement). Backup: world-131-mk-task-1 (world downloaded, not yet checked).

## Purpose

A small, faithful demonstration of the proposed experiment: it shows the study can run and that its assumptions deserve a larger test. It is not a scaled-down version of the study (no human author), and it is not the official APEX environment even where it reuses Mercor's open-source app servers.

## Design

| Component | Setup |
|---|---|
| Tasks | Eight public APEX-Agents 1.1 tasks across several worlds, covering law, consulting and banking where suitable |
| Adaptation | Remove one consequential requirement from every place the agent could find it; document each removal |
| Control | The fully specified version of the same task, run with the same client tool available (eight matched pairs) |
| Agent | One fixed Gemini Flash version and configuration. A Pro pass is optional, after Flash shows the runner and conversions work |
| Client comparison | Two prespecified simulator instructions, both given exactly the same requirement packet; no solution, no rubric |
| Branching | At first contact, save the conversation and tool state; obtain both replies; continue independently |
| Reference | Where useful, a prepared factual reply written from the packet, labeled scripted, never called an author reply |
| Repeats | A few repeated continuations from the same reply, to show how much continuation randomness alone moves scores |
| Scoring | The final deliverable under the task rubric, with the criteria affected by the removed requirement marked; inspect the small sample by hand |
| Protocol | Debug the runner on separate engineering examples, then freeze the eight-task protocol before collecting reported results. Record failures and unsuccessful tasks |

Definitions: "complete" means the requirement sits where it originally was (the matched control). "Disclosed at the question" means it arrives only in the client's reply at the saved state. These are different arms and are reported separately.

## Results (regraded Sept 16 with the repaired judge; two judges reported)

Every saved final answer of both conditions was regraded twice with the repaired grader: gemini-3.8-flash (the run-time judge, now with JSON repair and retries; no unresolved grades remained) and gemini-3.1-pro-preview. The two judges agree on 43 of the 47 scored outputs (16 in condition 1, 31 in condition 2; the Brightpath complete base run in condition 2 ended in contact and has no grade). Disagreements: WARN adapted (condition 1, an unlinked criterion, Flash 1.00 vs Pro 0.83), Whitaker complete (condition 2, one linked criterion, Flash 1.00 vs Pro 0.67), and two 3M branches (condition 2) where expected values appearing in a "Sensitivities / Alternative Model Cases" line are credited inconsistently by both judges (scripted#1 Flash 0.75 vs Pro 1.00; minimal#0 Flash 1.00 vs Pro 0.50, with Pro still crediting two of the four values from that line). Where the two judges differ the table shows Flash / Pro. Raw grades: `grade_gemini-3.8-flash.json` and `grade_gemini-3.1-pro-preview.json` in each run folder; `regrade_*.csv` at each run root; copies under `results/`.

### Condition 1: permissive prompt (Sept 15 23:50 to Sept 16 00:45; `results/pilot_default_20260915`)

The system prompt tells the agent it may message the client once when a requirement is missing. The agent never used the client tool: 0 of 8 adapted tasks, 0 of 8 complete versions. Mean Score 0.83 on complete versions (both judges) and 0.42 / 0.40 on adapted versions.

| Task | Complete | Adapted | Linked criteria met, complete → adapted (both judges) | Reading |
|---|---|---|---|---|
| SkyLink | 1.00 | 0.50 | 6/6 → 3/6 | saw the ranges, chose a "midpoint interpretation", never asked |
| Brightpath pricing | 0.00 | 0.00 | 0/4 → 0/4 | too hard for this model in both versions; uninformative |
| CompliSure share | 1.00 | 1.00 | 6/6 → 6/6 | guessed the intended rule from context; the removal was too inferable |
| Whitaker service date | 1.00 | 0.33 | 2/2 → 0/2 | wrote "the complaints do not state when the Original Complaint was served", then computed deadlines under assumed service dates instead of asking |
| WARN notice | 1.00 | 1.00 / 0.83 | 1/1 → 1/1 | the linked criterion was met without the plan terms; null pair |
| 3M buyback | 1.00 | 0.50 | 4/4 → 2/4 | assumed its own debt paydown split |
| Golden Everest cap rate | 1.00 | 0.00 | 2/2 → 0/2 | picked its own cap rate |
| BBDC merger account | 0.60 | 0.00 | 3/5 → 0/5 | used the model's default 2024 basis |

Across the six informative pairs (excluding Brightpath and CompliSure), linked criteria met fell from 18/20 to 6/20 under both judges, while unlinked criteria on the adapted versions stayed at 6/6 (Flash) or 5/6 (Pro). Cost: 832 calls, 33.9M prompt tokens of which 28.7M cached, 216k output; about $7 after caching, $26 at list price. Two runs hit the 80-step limit and answered through the forced closing turn.

### Condition 2: directive prompt (Sept 16 00:47 to 02:20; `results/pilot_ask_20260916`)

Same tasks and protocol; one sentence added telling the agent to ask before making an assumption (the permissive prompt already said it may ask; the difference is wording strength, not whether a client exists). Contact: 2 of 8 adapted tasks (CompliSure at step 71, 3M at step 33) and 1 of 8 complete versions (Brightpath at step 78, after the budget notice). Both adapted-version questions led with the removed requirement and added two or three questions the client notes did not cover.

| Task | Complete | Adapted | Branches from the adapted saved state (two repeats per reply; Flash / Pro where they differ) |
|---|---|---|---|
| SkyLink | 1.00 | 0.50, no contact | |
| Brightpath pricing | contacted; six branches all 0.00 | 0.00, no contact | |
| CompliSure share | 0.00 | contacted | scripted 1.00, 1.00; minimal 1.00, 1.00; helpful 1.00, 1.00 |
| Whitaker service date | 1.00 / 0.67 | 0.33, no contact | |
| WARN notice | 1.00 | 0.83, no contact | |
| 3M buyback | 0.50 | contacted | scripted 0.00, 0.75 / 1.00; minimal 1.00 / 0.50, 0.00; helpful 0.50, 0.00 |
| Golden Everest cap rate | 1.00 | 0.00, no contact | |
| BBDC merger account | 0.40 (forced) | 0.00, no contact | |

Reading. CompliSure: every reply carried the one fact that mattered and all six branches scored 1.0 under both judges, so the reply source made no difference there. 3M: the same reply produced opposite outcomes on two repeats (minimal simulator 1.00 / 0.50 then 0.00; scripted 0.00 then 0.75 / 1.00), so at two repeats per reply the within-reply spread is as large as the between-reply spread and nothing can be attributed to the reply. Two of those branch scores also depend on how the judge treats expected values that appear only in a sensitivity line, so this example shows differing outputs after identical replies, not a clean estimate of task-performance variability. File-state restoration checks (folder hash after restore) passed on all 12 branches; the conversation and model-content hashes are verified from commit 131f2fd on, and none of this is an uninterrupted-versus-restored replay comparison. Run-to-run variance on the complete versions is large (CompliSure 1.00 then 0.00; 3M 1.00 then 0.50), so single-run pair differences carry wide uncertainty. Cost: 996 calls, 43.4M prompt tokens of which 37.2M cached, 319k output; about $9 after caching, $34 at list. Both conditions together about $16 after caching; the four regrade passes about $2 more.

Limitations to state with the results: lite harness (file tools and a sandboxed Python instead of Mercor's nine app servers and Docker world); one model, one run per cell; the run-time judge is a Flash model rather than Mercor's judge, and both judges credit alternative-scenario values inconsistently; the CompliSure removal was guessable from context and the Brightpath task is beyond this model in both versions, so those two pairs are uninformative about asking; both simulator instructions referred to "the packet" in replies during these runs (reworded since); the directive prompt is a wording manipulation and its contact rate is not the default rate; the six-pair linked-criteria analysis is exploratory.

Changes before any further run: replace the CompliSure adaptation with one whose removed rule is not inferable from the task framing; drop or replace Brightpath; at least four repeats per reply; a judge instruction or post-check for answers that list several scenarios; a second model on the complete versions to see whether the variance is model-specific.

## Four questions it answers

1. **Do agents ask when information is missing?** Report "contacted on X of eight adapted tasks" next to contact on the complete versions. An initial observation, not a population contact rate.
2. **Does the missing information matter?** Compare with the matched controls. Complete succeeds and adapted fails without asking: a potentially useful clarification challenge. Both succeed: inspect for inference, guessing, residual information or prior exposure. Both fail: the task may be too hard for this model to show the value of asking. Inspect the affected criteria before changing any task.
3. **Can the answer source change the final work?** Show the same question, the two replies and the resulting deliverables. A concrete difference on a relevant criterion illustrates why simulator validation matters; no difference is still reported. This is evidence of sensitivity, not a bound on human-reference distortion, since neither simulator is the human reference.
4. **Can the larger study be executed and afforded?** Measure task-conversion time, API usage, execution failures, and whether restoring state preserves the intended starting conditions. Replay checks verify restoration of conversation and tool state; identical replies can still produce different continuations.

## Reading the results

- Near-zero contact triggers inspection of tool visibility, task solvability and performance on the complete versions.
- Report the pilot as it comes out. Inconclusive results still establish implementation feasibility and identify changes needed before the main study.
- Contact rate is one useful measurement, not the number that validates the project.

## Does not establish

Human-simulator equivalence, the two-point tolerance, model rankings, or that any confirmatory sample size is sufficient.

## Strongest upgrade

A few replies from a qualified expert who authored the adapted requirements. That exercises the human-reference workflow and starts measuring expert effort. Without that person, this stays an implementation and simulator-sensitivity demonstration.

## Evidence package for the application

A working runner, an eight-task results table, one inspectable example (question, two replies, two deliverables), and measured costs and limitations.

## Build order

1. Done: text files for all 240 tasks and task data downloaded; eight tasks picked; packets and removals in `adapts/`.
2. Plain file tools plus `run_python` over the unpacked world filesystems (`data/worlds/<slug>/fs`, fetched on demand by `harbor.py`); Mercor's app servers are not used.
3. Done: agent loop with `message_client`; state saved at first contact (conversation as JSON, task folder cloned and hashed); branches restored from the clone.
4. Smoke tests on 128-jr-1 with gemini-3.8-flash (sandboxed, Sept 15 23:00 and 23:05): complete version 1.0 both times (33 and 38 steps, no contact). Adapted version: first run explored for all 50 steps, never asked, no final answer (scored 0); second run, with a budget notice at 12 calls left, never asked, reported a "midpoint interpretation" with alternatives, 0.67 (two of six linked criteria unmet: Spin out 15.5 vs 15, Discontinue 21 vs 20). Cost per matched pair about $0.72 after Gemini's implicit caching (3.3M prompt tokens of which 2.8M cached, 31k output); $2.60 at list price. Protocol first frozen at commit bb2396d and the eight-pair run started 23:35; stopped after the second task's complete version hit the 60-step limit without answering (the budget notice was ignored). Protocol re-frozen with an 80-step limit and a forced closing turn (tools removed, "give your final answer now"; status `done_forced`), and the run restarted at 23:50 with two repeats per branch. The aborted run was discarded.
5. Check behavior against one official run if Docker is ever available; until then, label results as lite-harness.

## Run commands

```
./.venv/bin/python -m c06.run --stub --harbor data/apex-agents-v1.1/tasks/128-jr-1-f7f95d92 --repeats 1 --out runs/stub
./.venv/bin/python -m c06.run --harbor data/apex-agents-v1.1/tasks/<task> ... --repeats 2 --out runs/pilot
./.venv/bin/python -m c06.report runs/pilot/<stamp>
```

## Blockers (Jacob)

1. Google AI Studio billing funded before the eight-pair run (estimate: $1 to $3 per task run; whole pilot $50 to $150).
2. Rotate the Hugging Face token and the Gemini key after the pilot; both were pasted into chat.

## Human-check calculator findings (planning inputs, 8 models, 1,000 simulated runs per model)

- Savings depend on the correlation between author-branch and simulator-branch scores from the same saved state. At run SD 20 and a ±3 target: correlation 0.9 needs 38 author checks per model versus 171; 0.5 needs 134; 0.3 saves about 8%.
- Pinning leaderboard ranks is expensive: at correlation 0.8, 300 author checks per model still leave about 4 of 8 plausible rank positions.

## Human reply workflow (ready; needs a person)

The two adapted-version questions from condition 2 are in `human/*_question.md` with the original instruction and the withheld requirement for context. A person writes the client's reply into the matching `human/*_reply.txt`, then:

```
./.venv/bin/python -m c06.human runs/pilot_ask/20260916-003149/world223-smn-05-b00d08c1/adapted/state0 --reply-file human/3m_buyback_reply.txt --label adapter --repeats 4 --ask-prompt
./.venv/bin/python -m c06.human runs/pilot_ask/20260916-003149/world-134-rg-04-4498da8f/adapted/state0 --reply-file human/complisure_share_reply.txt --label adapter --repeats 4 --ask-prompt
```

Label the arm by who answered: `adapter` if the person who wrote the adaptation answers, `expert_finance` or similar if someone with domain training does. This exercises the human-reference workflow (a human reply entering a saved state, repeated continuations, grading) and nothing more; an adapter is not the task author and not a qualified expert.

## Replay check (uninterrupted versus restored)

`c06/replay.py` runs the adapted task to first contact and, from that one moment, continues twice with the identical scripted reply: once in-process on the live folder with the in-memory conversation, once through save, restore and the JSON round trip of the conversation. Paired outcomes (score, linked criteria, steps, tool mix) over several contacts test whether branching itself changes behavior. Run on 3M under the directive prompt on Sept 16 (`results/replay_3m_20260916`): four attempts, four contacts (steps 28, 34, 41, 38), four pairs.

| Contact | Uninterrupted: score, linked, steps after reply | Restored: score, linked, steps after reply | Hashes verified |
|---|---|---|---|
| 1 | 0.00, 0/4, 5 | 0.00, 0/4, 8 | folder, transcript, contents |
| 2 | 0.00, 0/4, 5 | 0.00, 0/4, 4 | folder, transcript, contents |
| 3 | 0.50, 2/4, 5 | 0.50, 2/4, 5 | folder, transcript, contents |
| 4 | 0.00, 0/4, 3 | 0.00, 0/4, 7 | folder, transcript, contents |

Paired score differences 0, 0, 0, 0; every post-reply call on both arms was `run_python`; the answers on both arms cite the same share counts (14.13 and 12.29 million in seven of eight, reflecting the same fee-and-premium choices). Reading: with four pairs this rules out a gross effect of save-and-restore on behavior, not a small one; step counts vary by up to four between arms, which is the same order as between repeats. Cost about $2 after caching (7.8M prompt tokens of which 6.2M cached, 73k output). Side observation: under the directive prompt the 3M task produced a client question on four of four attempts, so its contact behavior is stable even though its scores are not.
