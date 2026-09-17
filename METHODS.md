# C06 pilot: methods and results

Design, results across three agent models and two prompt conditions, the replay check, one practitioner reply, precision estimates from pilot variance, and the grading rules to pre-register. Result files are under `results/`; prompts and versions are in `c06/prompts_used.md`.

## Task selection (eight matched pairs)

Screened the 240 public tasks and verified each pick against the world filesystem to confirm the removed fact does not also appear in any file the agent can read.

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

## Purpose

A small, faithful demonstration of the proposed experiment: it shows the study can run and that its assumptions deserve a larger test. It is not a scaled-down version of the study (no task author in the loop), and it is not the official APEX environment.

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

Allocation rule for the main study (methods note): development estimates determine how the expert budget is split between additional tasks and repeated continuations; the confirmatory sample and analysis are frozen before held-out outcomes are examined. If development precision is inadequate, the options are more independent tasks and authors, a narrower claim, or an explicitly inconclusive equivalence result, chosen and recorded before confirmatory data are seen. Contribution in one sentence: the study measures how replacing expert-authored client replies with simulated replies changes professional-work scores from identical agent states. Core commitment: the two-model author-reference study, reusable code, and the paper; broader leaderboard coverage follows as resources permit. Expert budget: the proposal requests expert support for task adaptation, reference replies and independent review without an hourly estimate, because task and reply counts do not establish hours; conversion, independent review, answering questions and adjudicating grades each need a measured rate, and the pilot measured my own implementation cost, not professional expert throughput. Development-stage estimates set the final task count within the agreed budget; if credible expert-time estimates arrive, the request becomes a range with stated assumptions.

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

## Four questions it answers

1. **Do agents ask when information is missing?** Report "contacted on X of eight adapted tasks" next to contact on the complete versions. An initial observation, not a population contact rate.
2. **Does the missing information matter?** Compare with the matched controls. Complete succeeds and adapted fails without asking: a potentially useful clarification challenge. Both succeed: inspect for inference, guessing, residual information or prior exposure. Both fail: the task may be too hard for this model to show the value of asking. Inspect the affected criteria before changing any task.
3. **Can the answer source change the final work?** Show the same question, the two replies and the resulting deliverables. A concrete difference on a relevant criterion illustrates why simulator validation matters; no difference is still reported. This is evidence of sensitivity, not a bound on human-reference distortion, since neither simulator is the human reference.
4. **Can the larger study be executed and afforded?** Measure task-conversion time, API usage, execution failures, and whether restoring state preserves the intended starting conditions. Replay checks verify restoration of conversation and tool state; identical replies can still produce different continuations.

## Reading the results

- Near-zero contact triggers inspection of tool visibility, task solvability and performance on the complete versions.
- Report the pilot as it comes out. Inconclusive results still establish implementation feasibility and identify changes needed before the main study.
- Contact rate is one useful measurement, not the number that validates the project.

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

## Protocol for one additional agent model (fixed before any paid call)

Purpose: does a different model use the client channel, and does the score gap between complete and adapted versions look the same. One model at a time; the Flash rows stay as the reference.

1. Same eight tasks and the same `adapts/` files; nothing about the adaptations changes, including the two known weak ones, so the rows stay comparable.
2. Both prompt conditions are predefined for the model, permissive and directive, each on all eight pairs; neither is added or dropped after seeing results.
3. Two repeats per branch when the agent asks; simulators use the current `c06/client.py` wording, which differs from the wording behind the Flash rows (recorded in `c06/prompts_used.md`); the new rows are labeled with that difference rather than presented as identical to the Flash experiment.
4. Judges: `gemini-3.8-flash` at run time under the repaired grader, then a `gemini-3.1-pro-preview` regrade; report both, as for Flash.
5. Cost is measured, not assumed: one task (complete and adapted, permissive prompt) runs first; its token counts, multiplied by eight tasks and two conditions, plus half again for branches, give the estimate; the full run proceeds only if that estimate is accepted. Scenario figures from price lists are not a cap.
6. The protocol commit hash is recorded before the first call; any code change after that is a new protocol version and is documented.
7. Backends: `c06/llm.py` (`AnthropicModel` with prompt caching, `OpenAIModel` with parallel tool calls disabled); the model id is passed with `--model`.

## Fable 5.1 (Sept 16; `results/subagent_fable_20260916`)

Model `claude-fable-5-1`: each run was a fresh agent instance with no conversation context; asking meant writing `CLIENT_QUESTION.md` and stopping, after which the same agent was resumed with the scripted reply (one continuation per contact, no simulators, no repeats). The task folders, adaptations, criteria and Flash judge were the pilot's; the wording of the rules matched the permissive prompt.

| Task | Complete | Adapted | Linked criteria, complete → adapted |
|---|---|---|---|
| SkyLink | 1.00 | 0.50, no ask (midpoint guess) | 6/6 → 3/6 |
| Brightpath pricing | 0.00 | asked (about method, not the user count), 0.00 | 0/4 → 0/4 |
| CompliSure share | 1.00 | asked the removed rule, 1.00 | 6/6 → 6/6 |
| Whitaker service date | 1.00 | asked the removed fact, 1.00 | 2/2 → 2/2 |
| WARN notice | 1.00 | 0.83, no ask | 1/1 → 0/1 |
| 3M buyback | 0.00 | 0.00, no ask (proportional split) | 0/4 → 0/4 |
| Golden Everest cap rate | 1.00 | asked the removed value, 1.00 | 2/2 → 2/2 |
| BBDC merger account | 0.60 | 0.00, no ask (default 2024 basis) | 3/5 → 0/5 |

Asked on 4 of 8 adapted tasks and 0 of 8 complete versions, against Flash's 0 of 8 and 0 of 8 under the same permissive wording. Mean 0.70 complete, 0.54 adapted (Flash judge; Pro regrade recorded alongside). Where it asked and the reply carried the fact, three of four adapted runs scored 1.0; the fourth, Brightpath, is the task both models fail either way. Where it did not ask, it made the same guesses Flash made (midpoint mapping, proportional paydown, model-default account). Where it asked and the reply carried the withheld fact, the continuation scored 1.0; where it did not ask, the loss landed on the linked criteria.

## Qwen 3.8 Flash, permissive prompt (Sept 16 17:13 to 21:05; `results/qwen_default_20260916`)

Model `qwen/qwen3.8-flash` through OpenRouter, in the pilot harness (sandbox, saved-state branching, the reworded simulators), protocol commit 4cd189b, two repeats per branch. All outputs were graded by `gemini-3.8-flash` after the run (27 of 28 cells identical to the run-time grades); those are the numbers reported.

| Task | Complete | Adapted | Linked criteria, complete → adapted |
|---|---|---|---|
| SkyLink | 0.33 | 0.17, no ask | 2/6 → 1/6 |
| Brightpath pricing | asked (method), six branches all 0.00 | 0.00, no ask | 0/4 → 0/4 |
| CompliSure share | 0.00 | 0.83, no ask | 0/6 → 5/6 |
| Whitaker service date | 1.00 | 0.33, no ask | 2/2 → 0/2 |
| WARN notice | 0.83 | 1.00, no ask | 1/1 → 1/1 |
| 3M buyback | 0.00 | asked; minimal 0.50, 0.50; scripted 1.00, 1.00; helpful 1.00, 1.00 | 0/4 → see branches |
| Golden Everest cap rate | 1.00 | 0.00, no ask | 2/2 → 0/2 |
| BBDC merger account | 0.40 | 0.00, no ask | 2/5 → 0/5 |

Asked on 1 of 8 adapted tasks and 1 of 8 complete versions. Base-run means over the seven pairs with two graded base runs (Brightpath's complete version ended in contact and has no base grade), so not the eight-task denominator of the Flash and Fable means: 0.51 complete, 0.33 adapted under the Flash judge; 0.49 and 0.24 under gemini-3.1-pro-preview (via OpenRouter), which agrees with Flash on 24 of 26 cells and differs on WARN complete (0.83 vs 0.67) and CompliSure adapted (0.83 vs 0.17, a forced closing answer listing several scenarios). The 3M branch scores are identical under both judges.

The 3M contact is an observed example of the effect the study is designed to measure, not a settled estimate. Qwen asked about the buyback price and the fee while stating a proportional debt-equity split as its own assumption. The minimal simulator answered only what was asked ("I have no further instruction on the tender premium or the transaction fee"), so the wrong split stood and both continuations scored 0.50; the scripted reply and the helpful simulator supplied the withheld 2.60x rule, and all four of those continuations scored 1.00. Two agreeing repeats per reply do not establish that continuation noise is absent, and no human reference was involved; it is one saved state, in the situation where the question misses the withheld fact and a simulator's disclosure policy decides the outcome.

## Qwen 3.8 Flash, directive prompt (Sept 16 21:47 to Sept 17 02:35; `results/qwen_ask_20260917`)

Same setup, judge `gemini-3.8-flash` at run time (launcher fixed), the directive sentence added. Asked on 3 of 8 adapted tasks (SkyLink, Brightpath, BBDC) and 3 of 8 complete versions (Brightpath, CompliSure, BBDC); the 3M adapted task, which produced the reply-source example under the permissive prompt, did not ask this time (0.00). Non-contact base means over five pairs: 0.80 complete, 0.27 adapted.

| Task | Complete | Adapted |
|---|---|---|
| SkyLink | 1.00 | asked; scripted 0.50, 1.00; minimal 0.67, 0.33; helpful 0.17, 0.33 |
| Brightpath pricing | asked; six branches 0.00 | asked; six branches 0.00 |
| CompliSure share | asked; six branches 0.00 | 0.33 (forced), no ask |
| Whitaker service date | 1.00 | 0.33, no ask |
| WARN notice | 1.00 | 0.67, no ask |
| 3M buyback | 0.00 | 0.00, no ask |
| Golden Everest cap rate | 1.00 | 0.00, no ask |
| BBDC merger account | asked; six branches 0.60 | asked; minimal 0.40, 0.40; scripted 0.40, 0.40; helpful 0.40, 0.20 |

Reading. Every reply on SkyLink and BBDC carried the withheld rule, so the spread on SkyLink (0.17 to 1.00 across six branches) is continuation variation with the reply held fixed, the counterpart of the 3M case under the permissive prompt. The directive wording raised Qwen's asking on complete versions (1 to 3 of 8) as well as on adapted ones (1 to 3 of 8). Across models under the permissive wording the observed contact counts are Fable 5.1 4 of 8, Qwen 3.8 Flash 1 of 8, Gemini 3.8 Flash 0 of 8; three models and one run each do not establish a relationship between capability and asking. Cost of both Qwen conditions together: under two dollars on OpenRouter (43M input tokens, 40M of them cache reads, 2.8M output), plus Flash judge calls.

## One practitioner reply (Sept 17; `results/pilot_ask_20260916/world223-smn-05-b00d08c1/adapted/practitioner_*`)

A finance practitioner with hedge fund experience, not the task author and not the adapter, answered the 3M question from the Gemini 3.8 Flash directive-run saved state (the state whose simulator branches scored scripted 0.75 and 0.00, minimal 1.00 and 0.00, helpful 0.00 and 0.50). He was given the original instruction, the withheld requirement and the agent's three questions, and wrote the reply in his own words (`practitioner_reply.txt`): pay down debt only to 2.60x and put the rest into buybacks; no instruction on fee timing, "use your standard judgment"; use the figure matching "3M Total Equity"; execute the buyback at the dropped market price with no 15 percent premium. The last point is a judgment neither simulator made and the packet did not contain. Four continuations were run from the saved state with his reply (`c06/human.py`, label `practitioner`), judged by `gemini-3.8-flash` and `gemini-3.1-pro-preview`.

All four continuations computed the same primary figures: 14.13 million shares, EV $86,793 million, 12.94x, 23.32x. Scores were 0.00, 1.00, 1.00, 1.00 under both judges. The rubric expects 14.30 million shares, $86,767 million, 12.93x and 23.31x, which is the same calculation on gross proceeds; the only difference is the 1 percent transaction fee (gross $2,630 million less a $448 million paydown gives $2,182 million and 14.30 million shares at $152.53; net of the fee, $2,156 million and 14.13 million). His reply left the fee to judgment, every continuation deducted it, and the three that scored 1.00 did so because they added "(14.30 million if transaction fees are not deducted)" and the judge credited the parenthetical; the one that scored 0.00 offered a different alternative. Reading: the human-reference workflow runs end to end (a human reply entering a saved state, repeated continuations, two-judge grading); the score outcome here turns on an assumption the task's rubric never states, which is the kind of item the proposed author approval of acceptable disclosures is meant to settle before grading. One reply from one practitioner; it says nothing about author-versus-simulator distortion.

## Precision from pilot variance (Sept 17)

Inputs measured in the pilot: pooled within-state SD of per-task Mean Score across repeated continuations from the same reply, 0.228 (34 reply groups, 36 degrees of freedom, Gemini 3.8 Flash and Qwen 3.8 Flash); between-task SD of base scores 0.42; SD of the paired complete-minus-adapted difference 0.37 over eight tasks (mean 0.41). The between-state SD of the true author-minus-simulator shift is unknown; the table takes 0, 0.10 and 0.20.

States per model for a 95 percent interval half-width of two points on that model's mean shift, with r repeats per reply (variance per state = s_b² + 2·0.228²/r):

| s_b | r = 1 | r = 2 | r = 4 |
|---|---:|---:|---:|
| 0.00 | 998 | 499 | 250 |
| 0.10 | 1,094 | 595 | 346 |
| 0.20 | 1,382 | 883 | 634 |

At the planned scale (up to 626 author replies across two models, about 300 states per model), the half-width at s_b = 0.10 is 2.8 points with two repeats and 2.1 with four. The interval for the difference between the two models' shifts is wider by about √2, so the three-interval criterion is unlikely to be met at this scale unless frontier-model continuation variance is below Flash's. Consequences already in the design: four runs per task; the development phase measures the actual within-state and between-state variances before the confirmatory sample is fixed; the allocation rule spends the expert budget on repeats or on states according to which variance dominates; and the reported fallback is the interval achieved rather than a claim of equivalence. Caveats: the within-state SD comes from two Flash-class models on tasks with two to six criteria; per-task scores are coarse, which the mean over states smooths; author and simulator continuations from one state share that state, which the s_b term absorbs.

## Grading rules to pre-register (from pilot findings)

1. Multi-scenario answers: a criterion is met only if the required value is the answer's stated primary result; values that appear only in a sensitivity, alternative or "if" clause do not count. The pilot's judges credited such clauses inconsistently (3M branches, both judges).
2. Unstated rubric assumptions: before grading, the task author lists the assumptions the reference answer relies on that the instruction does not state (for 3M, gross rather than fee-net proceeds); each is either added to the instruction, added to the approved disclosures, or accepted as a judgment call whose alternatives are graded as correct. The practitioner reply exposed this case.
3. Judge agreement is reported per task from two judges, and any criterion where they disagree is adjudicated by a person before the score enters the analysis.
