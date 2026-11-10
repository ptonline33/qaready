# QAReady

**Service Desk Technician → Software QA Analyst.** A complete, installable, offline-first PWA that teaches software quality assurance from scratch over a 24-week, part-time roadmap.

Built as a sister app to DeskReady, but deeper: a structured curriculum rather than a course library, plus a roadmap, quizzes, glossary/flashcards, portfolio projects, a resource toolkit, and a full career/interview kit.

## Run it

PWAs need to be served over `http://localhost` or HTTPS (the service worker won't register from `file://`).

```bash
cd qaready
npm start          # python3 -m http.server 8080
# or: python3 -m http.server 8080
```

Open <http://localhost:8080>. On Chrome/Edge you'll get an **Install app** button in the header (or use the browser menu → *Install app* / *Add to Home Screen*). After the first load everything works offline.

There is **no build step, no dependencies and no backend**. `index.html` loads plain scripts.

## What's inside

| | |
|---|---|
| **7 phases / 24 weeks** | Week-by-week roadmap with a focus, deliverable and checkpoint for every week |
| **20 courses** | From "What is QA?" to "Landing the job" |
| **110 lessons** | Detailed Markdown lessons written from zero, each with a *"From the desk"* callout connecting the topic to skills you already have |
| **358 interactive exercises** | Multiple choice, type-the-answer, ordering, Markdown/document writing, and a **runnable in-browser SQL engine** |
| **20 quizzes** | 134 questions, shuffled options, saved best scores |
| **132 glossary terms** | Searchable + a flashcard drill mode |
| **53 resources** | Free courses, certifications, tools, books, communities and practice apps |
| **5 portfolio projects** | Checklists + copyable artefact templates (test case, defect report, Postman assertions, Playwright POM) |
| **46 interview Q&As** | Plus resume rewrites, a cover-letter template, STAR stories, job-search and first-90-days plans |
| **2 long-form plans** | The 24-week schedule and the complete career guide |

Plus: 4 themes (night/sepia/light/high-contrast), 6 reading fonts, adjustable text size, per-lesson notes, bookmarks, full-text search (`Ctrl+K`), progress export/import, day streaks, and offline caching.

## The curriculum

| Phase | Weeks | Theme |
|---|---|---|
| 0 · Start here | 1 | Orientation, the QA role, your transferable skills |
| 1 · Manual QA craft | 2-6 | Test design (EP, BVA, decision tables, state transitions, exploratory, pairwise), test cases/plans/RTM, defect management, tools, communication |
| 2 · Technical foundations | 7-11 | Web/HTTP, SQL, CLI & Git, JavaScript from zero |
| 3 · API testing | 12-14 | REST, auth, Postman assertions, Newman CI |
| 4 · Automation & CI/CD | 15-20 | Strategy, Playwright, Page Objects, GitHub Actions, quality gates |
| 5 · Beyond functional | 21-22 | Performance, accessibility, security, usability, compatibility, localisation/privacy |
| 6 · Get hired | 23-24 | ISTQB CTFL, portfolio, resume, interviews, job search |

**Design principle:** manual test thinking comes first. Automation is *coding a check for behaviour you already understand* — if you can't design a good test case by hand, an automated test just asserts the wrong thing faster.

## Project layout

```
qaready/
├── index.html                 app shell
├── styles.css                 themes, fonts, all components
├── manifest.webmanifest       PWA manifest + shortcuts
├── sw.js                      offline cache
├── icons/                     generated PNG/SVG icons
├── fonts/                     6 reading fonts (woff2)
├── vendor/marked.js           Markdown renderer
├── js/
│   ├── sql-engine.js          mini SQL interpreter (offline, dependency-free)
│   ├── app.js                 routing, views, exercise engine, progress
│   └── content.js             GENERATED — do not edit
├── content/                   AUTHORING SOURCE (Python + Markdown)
│   ├── __init__.py            helpers & practice database
│   ├── courses_01.py … _04.py 20 courses / 110 lessons
│   └── extras.py              roadmap, glossary, toolkit, projects, career kit, plans
├── build_content.py           validates + compiles content → js/content.js
├── generate_icons.py          regenerates icons (stdlib only)
└── README.md
```

## Editing the content

All teaching material lives in `content/*.py` as readable multi-line Markdown — no JSON escaping. After changing anything:

```bash
python3 build_content.py     # validates ids/exercises/quizzes and rebuilds data/content.js
npm run check                # also syntax-checks the JS
```

The build script exits non-zero with a detailed report if any exercise is malformed, an answer index is out of range, a regex is invalid, or a cross-reference is broken. Bump `VERSION` in `sw.js` when you ship changes so installed copies refresh.

To regenerate icons: `python3 generate_icons.py` (uses only the standard library — no Pillow/ImageMagick).

## Data & privacy

Progress (completed lessons/exercises, quiz scores, notes, bookmarks, checklists, theme) is stored **only** in your browser's `localStorage`. No account, no server, no analytics, no network calls except optional external resource links you click. Use **Settings → Export JSON** to back up or move progress between devices.
