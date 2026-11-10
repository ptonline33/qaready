#!/usr/bin/env python3
"""Compile all QAReady content into data/content.js and validate it.

Usage (from the project folder):
    python3 build_content.py

Why a build step? All teaching material is authored as readable, multi-line
Markdown in Python modules (no JSON escaping, no build tooling needed in the
browser). This script assembles it into one file the app loads with a plain
<script> tag, so the whole course works offline with zero network requests.

It also validates the data: unique IDs, exercise shapes, quiz answer ranges,
regex patterns, and cross-references. It exits non-zero with a report on any
problem, so bad content never silently ships.
"""
import json
import re
import sys
from pathlib import Path

from content.courses_01 import COURSES_01, QUIZZES_01
from content.courses_02 import COURSES_02, QUIZZES_02
from content.courses_03 import COURSES_03, QUIZZES_03
from content.courses_04 import COURSES_04, QUIZZES_04
from content.extras import (
    PHASES, WEEKS, GLOSSARY, RESOURCES, PROJECTS, CAREER_KIT, INTERVIEW, PLANS,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "content.js"

COURSES = COURSES_01 + COURSES_02 + COURSES_03 + COURSES_04
QUIZZES = QUIZZES_01 + QUIZZES_02 + QUIZZES_03 + QUIZZES_04

EX_KINDS = {"mcq", "input", "order", "md", "sql"}


def validate_ex(ex, where, problems):
    if not isinstance(ex, dict):
        problems.append(f"{where}: exercise is not an object")
        return
    if not ex.get("prompt", "").strip():
        problems.append(f"{where}: missing prompt")
    kind = ex.get("type")
    if kind not in EX_KINDS:
        problems.append(f"{where}: unknown exercise type {kind!r}")
        return
    if kind == "mcq":
        opts = ex.get("options")
        if not isinstance(opts, list) or len(opts) < 2:
            problems.append(f"{where}: mcq needs >= 2 options")
        ans = ex.get("answer")
        if not isinstance(ans, int) or not isinstance(opts, list) or not (0 <= ans < len(opts)):
            problems.append(f"{where}: mcq answer index out of range")
    elif kind == "input":
        answers = ex.get("answers")
        if not isinstance(answers, list) or not answers or not all(isinstance(a, str) and a.strip() for a in answers):
            problems.append(f"{where}: input needs non-empty answers list")
    elif kind == "order":
        items = ex.get("items")
        if not isinstance(items, list) or len(items) < 2 or len(set(items)) != len(items):
            problems.append(f"{where}: order needs >= 2 unique items")
    elif kind == "md":
        pats, sol = ex.get("patterns"), ex.get("solution")
        if not isinstance(pats, list) or not pats or not all(
            isinstance(p, dict) and p.get("re") and p.get("m") for p in pats
        ):
            problems.append(f"{where}: md needs patterns with re + m")
        else:
            for i, p in enumerate(pats):
                try:
                    re.compile(p["re"], re.MULTILINE)
                except re.error as e:
                    problems.append(f"{where}: md pattern {i} invalid regex: {e}")
        if not isinstance(sol, str) or not sol.strip():
            problems.append(f"{where}: md needs a solution")
    elif kind == "sql":
        db = ex.get("db")
        if not isinstance(db, list) or not db:
            problems.append(f"{where}: sql needs a db")
        else:
            for t in db:
                cols, rows = t.get("columns"), t.get("rows")
                if not isinstance(cols, list) or not cols or not isinstance(rows, list):
                    problems.append(f"{where}: sql db table malformed")
                    break
                if any(not (isinstance(r, list) and len(r) == len(cols)) for r in rows):
                    problems.append(f"{where}: sql db row width mismatch")
                    break
        exp = ex.get("expected")
        if not isinstance(exp, dict) or not isinstance(exp.get("columns"), list) or not isinstance(exp.get("rows"), list):
            problems.append(f"{where}: sql needs expected columns/rows")
        elif any(not (isinstance(r, list) and len(r) == len(exp["columns"])) for r in exp["rows"]):
            problems.append(f"{where}: sql expected row width mismatch")
        if not isinstance(ex.get("solution"), str) or not ex["solution"].strip():
            problems.append(f"{where}: sql needs a solution")


def main():
    problems = []

    # ---- unique ids / cross references ----
    course_ids = [c["id"] for c in COURSES]
    if len(set(course_ids)) != len(course_ids):
        problems.append("duplicate course ids")

    phase_ids = {p["id"] for p in PHASES}
    for c in COURSES:
        if c["phase"] not in phase_ids:
            problems.append(f"course {c['id']}: unknown phase {c['phase']}")
    for p in PHASES:
        for cid in p["courses"]:
            if cid not in course_ids:
                problems.append(f"phase {p['id']}: references unknown course {cid}")
    for w in WEEKS:
        if w["phase"] not in phase_ids:
            problems.append(f"week {w['w']}: unknown phase {w['phase']}")
        for cid in w["courses"]:
            if cid not in course_ids:
                problems.append(f"week {w['w']}: references unknown course {cid}")

    quiz_ids = [q["id"] for q in QUIZZES]
    if len(set(quiz_ids)) != len(quiz_ids):
        problems.append("duplicate quiz ids")
    for c in COURSES:
        if c["quizId"] not in quiz_ids:
            problems.append(f"course {c['id']}: missing quiz {c['quizId']}")

    lesson_ids = []
    total_ex = 0
    for c in COURSES:
        if not c["lessons"]:
            problems.append(f"course {c['id']}: no lessons")
        for li, lesson in enumerate(c["lessons"]):
            where = f"{c['id']} lesson {li + 1} ({lesson.get('id')})"
            if not lesson.get("title", "").strip():
                problems.append(f"{where}: missing title")
            if not lesson.get("body", "").strip():
                problems.append(f"{where}: missing body")
            lesson_ids.append(lesson["id"])
            exs = lesson.get("exercises")
            if not isinstance(exs, list) or not exs:
                problems.append(f"{where}: no exercises")
                continue
            total_ex += len(exs)
            for ei, ex in enumerate(exs):
                validate_ex(ex, f"{where} exercise {ei + 1}", problems)
    if len(set(lesson_ids)) != len(lesson_ids):
        dupes = sorted({x for x in lesson_ids if lesson_ids.count(x) > 1})
        problems.append(f"duplicate lesson ids: {dupes}")

    for q in QUIZZES:
        where = f"quiz {q['id']}"
        if q["courseId"] not in course_ids:
            problems.append(f"{where}: unknown courseId {q['courseId']}")
        if not q["questions"]:
            problems.append(f"{where}: no questions")
        for qi, qq in enumerate(q["questions"]):
            if not qq.get("q", "").strip():
                problems.append(f"{where} q{qi + 1}: missing question")
            opts = qq.get("options")
            if not isinstance(opts, list) or len(opts) < 2:
                problems.append(f"{where} q{qi + 1}: needs >= 2 options")
            ans = qq.get("answer")
            if not isinstance(ans, int) or not isinstance(opts, list) or not (0 <= ans < len(opts)):
                problems.append(f"{where} q{qi + 1}: answer index out of range")

    if [w["w"] for w in WEEKS] != list(range(1, len(WEEKS) + 1)):
        problems.append("WEEKS must be numbered 1..N consecutively")

    if problems:
        print("VALIDATION FAILED:\n  " + "\n  ".join(problems), file=sys.stderr)
        sys.exit(1)

    # ---- assemble ----
    data = {
        "meta": {
            "title": "QAReady",
            "subtitle": "Service Desk → Software QA Analyst",
            "version": "1.0.0",
            "weeks": len(WEEKS),
            "hoursPerWeek": "8-10",
            "phases": len(PHASES),
            "courses": len(COURSES),
            "lessons": len(lesson_ids),
            "exercises": total_ex,
            "quizzes": len(QUIZZES),
            "quizQuestions": sum(len(q["questions"]) for q in QUIZZES),
            "glossaryTerms": len(GLOSSARY),
            "resources": len(RESOURCES),
            "projects": len(PROJECTS),
            "interviewQuestions": len(INTERVIEW),
            "plans": len(PLANS),
        },
        "phases": PHASES,
        "weeks": WEEKS,
        "courses": COURSES,
        "quizzes": QUIZZES,
        "glossary": GLOSSARY,
        "resources": RESOURCES,
        "projects": PROJECTS,
        "career": CAREER_KIT,
        "interview": INTERVIEW,
        "plans": PLANS,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, indent=1)
    OUT.write_text(
        "/* QAReady content — generated by build_content.py. Do not edit by hand. */\n"
        "window.QA_DATA = " + payload + ";\n",
        encoding="utf-8",
    )

    m = data["meta"]
    size_kb = OUT.stat().st_size / 1024
    print(f"QAReady content built -> {OUT.relative_to(ROOT)} ({size_kb:.0f} KB)")
    print(f"  {m['phases']} phases · {m['weeks']} weeks · {m['courses']} courses")
    print(f"  {m['lessons']} lessons · {m['exercises']} exercises · "
          f"{m['quizzes']} quizzes ({m['quizQuestions']} questions)")
    print(f"  {m['glossaryTerms']} glossary terms · {m['resources']} resources · "
          f"{m['projects']} projects · {m['interviewQuestions']} interview Q&As · "
          f"{m['plans']} study plans")


if __name__ == "__main__":
    main()
