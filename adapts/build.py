import json

from pathlib import Path


ROOT = Path(__file__).resolve().parent

TASKS = ROOT.parent / "data" / "apex-agents-v1.1" / "tasks"


SPECS = {

    "128-jr-1-f7f95d92": {

        "domain": "Management Consulting",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["use the worst case scenario when translating the updated framework to a quantitative value"],

        "packet": "You are the engagement lead who sent this request. The revised Business Unit Assessment Framework (v2) gives qualitative ranges for several criteria (for example 'Low to very low'), so more than one ideal rating is possible for those criteria. Your instruction: when translating the updated framework to a quantitative ideal rating, use the worst case option for each criterion. There are no changes to the formulas or calculations.",

        "scripted_reply": "Use the worst case scenario when translating the updated framework to a quantitative value. There are no changes to the formulas or calculations.",

        "linked_criteria": [0, 1, 2, 3, 4, 5],

    },

    "world-129-cy-task-3-2bcdc3db": {

        "domain": "Management Consulting",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["use the midpoint of the Company Size range as the user count"],

        "packet": "You commissioned this analysis. The revenue-by-segment data gives Company Size as employee ranges (10-50, 51-250, 251-500). Your instruction: use the midpoint of the Company Size range as the user count for each segment row.",

        "scripted_reply": "Use the midpoint of the Company Size range as the user count.",

        "linked_criteria": [0, 1, 2, 3],

    },

    "world-134-rg-04-4498da8f": {

        "domain": "Management Consulting",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["any market share lost by TrainIQ is fully captured by CompliSure, with no impact on other competitors"],

        "packet": "You commissioned this analysis. Your assumption: any market share lost by TrainIQ is fully captured by CompliSure, with no impact on other competitors. The overall 2025 market size does not change.",

        "scripted_reply": "Assume that any market share lost by TrainIQ is fully captured by CompliSure, with no impact on other competitors.",

        "linked_criteria": [0, 1, 2, 3, 4, 5],

    },

    "lawworld433-anb-01-5d12cf8d": {

        "domain": "Law",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["each Complaint was served on the defendant ten days after it was filed"],

        "packet": "You are the Assistant General Counsel who sent this request. Fact you know: each Complaint was served on the defendant ten days after it was filed. The complaints themselves do not state service dates.",

        "scripted_reply": "Each Complaint was served on the defendant ten days after it was filed.",

        "linked_criteria": [0, 2],

    },

    "lawworld417-ne-06-7d454c39": {

        "domain": "Law",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["the group health plan terms: coverage runs through the last day of the month in which employment ends; eligibility changes only through a formal plan amendment"],

        "packet": "You are the in-house lawyer who sent this request. Facts you know about Streams' group health plan: an active employee's coverage runs through the last day of the month in which employment ends, and any change to plan eligibility takes effect only through a formal plan amendment adopted under the plan's amendment procedure.",

        "scripted_reply": "Streams' group health plan provides that an active employee's coverage runs through the last day of the month in which employment ends, and any change to plan eligibility takes effect only through a formal plan amendment adopted under the plan's amendment procedure.",

        "linked_criteria": [4],

    },

    "world223-smn-05-b00d08c1": {

        "domain": "Investment Banking",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["pay down debt to bring the debt to equity ratio down to 2.60x"],

        "packet": "You are the client who sent this request. Your assumption: the proceeds from the sale of Solventum are used to pay down debt only as far as needed to bring 3M's debt to equity ratio down to 2.60x from its baseline. The remaining proceeds are used to repurchase shares.",

        "scripted_reply": "Use the proceeds to pay down debt until the debt to equity ratio comes down to 2.60x; the remaining proceeds go to share repurchases.",

        "linked_criteria": [0, 1, 2, 3],

    },

    "world-225-je-01-70449b2d": {

        "domain": "Investment Banking",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["the capitalization rate value, 5.5%"],

        "packet": "You are the client who sent this request. The REIT industry capitalization rate to use is 5.5%.",

        "scripted_reply": "Use a REIT industry capitalization rate of 5.5%.",

        "linked_criteria": [0, 1],

    },

    "world-221-hy-05-fa5120b0": {

        "domain": "Investment Banking",

        "find": "REDACTED: verbatim fragment of the gated task instruction",

        "replace": "REDACTED",

        "removed": ["set the merger model to the 9M TTM 2025 account"],

        "packet": "You are the client who sent this request. Your instruction: set the merger model to the 9M TTM 2025 account (the Financial Account input in the merger analysis), and take every figure on that basis.",

        "scripted_reply": "Set the merger model to the 9M TTM 2025 account.",

        "linked_criteria": [0, 1, 2, 3, 4],

    },

}


def build():

    for tid, s in SPECS.items():

        text = (TASKS / tid / "instruction.md").read_text()

        if text.count(s["find"]) != 1:

            raise SystemExit(f"{tid}: find string occurs {text.count(s['find'])} times")

        adapted = text.replace(s["find"], s["replace"])

        n_crit = len(json.loads((TASKS / tid / "tests" / "grading_config.json").read_text())["verifiers"])

        assert all(i < n_crit for i in s["linked_criteria"]), tid

        out = {

            "task": tid,

            "domain": s["domain"],

            "instruction_adapted": adapted,

            "removed": s["removed"],

            "packet": s["packet"],

            "scripted_reply": s["scripted_reply"],

            "linked_criteria": s["linked_criteria"],

            "edits": [],

        }

        (ROOT / f"{tid}.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))

        print(tid, "ok", f"{len(text.split())}->{len(adapted.split())} words", "linked", s["linked_criteria"], "/", n_crit)


if __name__ == "__main__":

    build()
