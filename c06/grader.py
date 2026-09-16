import json

from pathlib import Path


from . import mercor_prompts as mp

from .llm import extract_json

from .tools import read_as_text


FINAL_ONLY = "Final Answer Only (No Files)"

RETRIES = 3


def artifacts_block(workdir, writes):

    parts = []

    for rel in sorted(set(writes)):

        p = Path(workdir) / rel

        if not p.exists():

            continue

        text = read_as_text(p)

        if len(text) > 12000:

            text = text[:12000] + "\n(TRUNCATED)"

        parts.append(f'<ARTIFACT path="{rel}">\n{text}\n</ARTIFACT>')

    return "\n".join(parts)


def judge_one(model, output, criterion_text):

    system = mp.GRADING_SYSTEM_PROMPT_NO_REFERENCE

    user = mp.GRADING_BASE_USER_PROMPT_TEMPLATE.format(final_answer=output, criteria=criterion_text, answer_assertion_check="")

    last = ""

    for _ in range(RETRIES):

        turn, _raw = model.chat(system, [model.user_content(user)], json_mode=True)

        last = turn.text

        try:

            j = extract_json(turn.text)

            return bool(j.get("is_criteria_true")), j.get("rationale", ""), True

        except Exception:

            continue

    return None, f"UNRESOLVED after {RETRIES} attempts: {last[:300]}", False


def grade(model, final_answer, workdir, writes, criteria):

    final_only = all(c.get("expected_file_type", FINAL_ONLY) == FINAL_ONLY for c in criteria)

    arts = "" if final_only else artifacts_block(workdir, writes)

    output = final_answer + ("\n\n" + arts if arts else "")

    results = []

    for c in criteria:

        met, rationale, resolved = judge_one(model, output, c["description"])

        results.append({"id": c.get("id"), "linked": bool(c.get("linked_to_removed")), "met": met, "resolved": resolved, "rationale": rationale})

    resolved = [r for r in results if r["resolved"]]

    mean = sum(r["met"] for r in resolved) / max(1, len(resolved))

    return {"mean_score": mean, "n_unresolved": len(results) - len(resolved), "criteria": results}
