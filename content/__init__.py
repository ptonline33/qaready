"""Content authoring helpers for QAReady.

Everything the app teaches lives in Python modules in this package so it can be
written as readable multi-line Markdown (no JSON escaping), validated, and then
compiled into a single `data/content.js` by `build_content.py`.

An exercise is a dict. Five kinds are supported by the app (ported from the
DeskReady exercise engine): mcq, input, order, md, sql.
"""

# ---------------------------------------------------------------------------
# Shared sample database for the in-browser SQL exercises (QA themed).
# ---------------------------------------------------------------------------
QA_DB = [
    {
        "name": "testers",
        "columns": ["id", "name", "team", "active"],
        "rows": [
            [1, "Asha", "Web", 1],
            [2, "Ben", "API", 1],
            [3, "Cy", "Web", 0],
            [4, "Dee", "Mobile", 1],
            [5, "Eli", "API", 1],
        ],
    },
    {
        "name": "test_cases",
        "columns": ["id", "title", "module", "priority", "status", "owner_id"],
        "rows": [
            [101, "Login with valid credentials", "Auth", "High", "Passed", 1],
            [102, "Login with locked account", "Auth", "High", "Failed", 1],
            [103, "Reset password email", "Auth", "Medium", "Passed", 2],
            [104, "Cart total with discount", "Cart", "High", "Failed", 4],
            [105, "Cart with empty basket", "Cart", "Low", "Blocked", 4],
            [106, "Search by SKU", "Search", "Medium", "Passed", 3],
            [107, "Checkout as guest", "Checkout", "High", "Not Run", 5],
            [108, "Apply invalid coupon", "Cart", "Medium", "Failed", 2],
        ],
    },
    {
        "name": "defects",
        "columns": ["id", "test_case_id", "severity", "status", "assignee_id"],
        "rows": [
            [501, 102, "Critical", "Open", 1],
            [502, 104, "Major", "Open", 4],
            [503, 104, "Minor", "Fixed", 2],
            [504, 108, "Major", "Retest", 5],
            [505, 105, "Trivial", "Closed", 3],
            [506, 107, "Major", "Open", None],  # deliberately unassigned (NULL)
        ],
    },
]


# ---------------------------------------------------------------------------
# Exercise constructors
# ---------------------------------------------------------------------------
def mcq(prompt, options, answer, explain="", hint=""):
    """Multiple choice. `answer` is the index of the correct option."""
    ex = {"type": "mcq", "prompt": prompt, "options": list(options), "answer": answer}
    if explain:
        ex["explain"] = explain
    if hint:
        ex["hint"] = hint
    return ex


def inp(prompt, answers, explain="", hint="", case_sensitive=False):
    """Type-the-answer. Several accepted spellings can be supplied."""
    if isinstance(answers, str):
        answers = [answers]
    ex = {"type": "input", "prompt": prompt, "answers": list(answers)}
    if case_sensitive:
        ex["caseSensitive"] = True
    if explain:
        ex["explain"] = explain
    if hint:
        ex["hint"] = hint
    return ex


def order(prompt, items, explain="", hint=""):
    """Put the given items into the correct (listed) order."""
    ex = {"type": "order", "prompt": prompt, "items": list(items)}
    if explain:
        ex["explain"] = explain
    if hint:
        ex["hint"] = hint
    return ex


def mdex(prompt, patterns, solution, starter="", explain="", hint=""):
    """Write a Markdown/document artifact; each pattern is {re, m}."""
    ex = {"type": "md", "prompt": prompt, "patterns": list(patterns), "solution": solution}
    if starter:
        ex["starter"] = starter
    if explain:
        ex["explain"] = explain
    if hint:
        ex["hint"] = hint
    return ex


def sqlex(prompt, solution, expected, db=None, explain="", hint=""):
    """Runnable SQL against the in-browser mini database."""
    ex = {
        "type": "sql",
        "prompt": prompt,
        "db": db if db is not None else QA_DB,
        "solution": solution,
        "expected": expected,
    }
    if explain:
        ex["explain"] = explain
    if hint:
        ex["hint"] = hint
    return ex


def P(re, m):
    """A single markdown-exercise pattern."""
    return {"re": re, "m": m}


def table(columns, rows):
    """Build a Markdown table from a header list and row list."""
    head = "| " + " | ".join(str(c) for c in columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    body = ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join([head, sep] + body)


# ---------------------------------------------------------------------------
# Lesson / course constructors
# ---------------------------------------------------------------------------
def lesson(lid, title, minutes, intro, sections=(), desk=None, ex=(), takeaway=None):
    """Compose a lesson from structured parts.

    sections: iterable of (heading, markdown_body). A `> From the desk` callout
    is appended when supplied, plus an optional closing takeaway line.
    """
    parts = [intro.strip()]
    for heading, body in sections:
        parts.append("## " + heading.strip() + "\n\n" + str(body).strip())
    if desk:
        parts.append("> **From the desk:** " + str(desk).strip())
    if takeaway:
        parts.append("**Remember:** " + str(takeaway).strip())
    return {
        "id": lid,
        "title": title,
        "minutes": minutes,
        "body": "\n\n".join(parts),
        "exercises": list(ex),
    }


def course(cid, title, subtitle, description, color, phase, weeks, level, lessons, quiz=None):
    return {
        "id": cid,
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "color": color,
        "phase": phase,
        "weeks": weeks,
        "level": level,
        "lessons": list(lessons),
        "quizId": quiz or (cid + "-quiz"),
    }


def quiz(qid, course_id, title, questions):
    """questions: list of (question, [options], answer_index, explanation)."""
    return {
        "id": qid,
        "courseId": course_id,
        "title": title,
        "questions": [
            {"q": q, "options": list(o), "answer": a, "explain": e}
            for (q, o, a, e) in questions
        ],
    }
