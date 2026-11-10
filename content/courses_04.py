"""Phase 6 courses: ISTQB, portfolio, communication, career & interviews."""
from . import lesson, course, quiz, mcq, inp, order, mdex, P, table

# ---------------------------------------------------------------------------
# 17. ISTQB & certification
# ---------------------------------------------------------------------------
ISTQB = course(
    "istqb", "ISTQB & Certification", "Credential + vocabulary",
    "The certification landscape, a map of the ISTQB Certified Tester Foundation Level syllabus to what you have already learned, exam strategy, and a terminology drill. Optional but useful for career changers.",
    "#c084fc", "p6", "Week 23", "Exam prep",
    [
        lesson("istqb-01", "The certification landscape (honest take)", 10,
               "Certifications are neither magic nor useless. For a career changer with no QA job history, one well-chosen credential can get a resume past a keyword filter and prove the vocabulary. Here is the honest picture.",
               [
                 ("What's out there", """| Certification | Body | Level | Worth knowing |
|---|---|---|---|
| **ISTQB CTFL (Certified Tester Foundation Level)** | ISTQB / national boards | Foundation | The globally recognised one; ~40 multiple-choice questions, widely accepted. Best first pick. |
| **ISTQB CTFL-AT (Agile Tester)** | ISTQB | Foundation extension | Good follow-up if you're in Agile teams |
| **ISTQB CTAL-TA / TM / TAE** | ISTQB | Advanced | For experienced testers / leads, later in your career |
| **CSTE / CSTP** | QAI / others | Practitioner | Less common in the UK/EU market |
| **AWS / Azure / Postman / Playwright certificates** | Vendors | Tool-specific | Useful as *additions*, not substitutes |
| **Scrum: PSM I / CSM** | Scrum.org / ScrumAlliance | Process | Cheap, useful for Agile vocabulary |"""),
                 ("What a certificate does and doesn't do", """**Does:** prove you know the standard terminology; satisfy HR keyword filters; give a structured syllabus to study; signal commitment to a career change; give you confidence in interviews.

**Doesn't:** prove you can test a real product; replace a portfolio; guarantee a job. Hiring managers consistently rank **hands-on evidence and test thinking** above the certificate itself.

Recommendation for you: **CTFL is worth it** because it is cheap (exam fee varies by country), recognised, and its syllabus overlaps ~80% with this app's Phases 0-2. Treat it as a *vocabulary exam*, not a skills substitute. Pair it with your portfolio repos. If budget is tight, skip it initially and apply with the portfolio — you can sit the exam later while employed (many employers pay)."""),
                 ("Exam logistics", """- Typically **40 multiple-choice questions**, ~60 minutes, pass mark ~65% (26/40). Check your national board for current rules; some now offer online proctored exams.
- One mark per question; **no negative marking** — always answer everything.
- Questions are definition- and scenario-based and often hinge on one precise word ('verification' vs 'validation', 'severity' vs 'priority', 'retesting' vs 'regression').
- Read the official **syllabus** (free PDF) and do several timed mock exams. The syllabus is the exam's test basis — a delightfully QA-appropriate situation."""),
               ],
               desk="You already hold or have chased ITIL/CompTIA-style credentials. Same logic: a shared vocabulary that gets you past the filter, plus real evidence that proves you can do the work.",
               takeaway="CTFL = globally recognised, cheap, vocabulary-heavy, ~80% covered here. Worth it for career changers, but the portfolio matters more.",
               ex=[
                   mcq("What is the main value of ISTQB CTFL for a career changer?", [
                       "It guarantees a job", "It proves terminology and gets past keyword filters", "It replaces a portfolio", "It teaches Playwright"], 1),
                   mcq("CTFL exam format is typically:", [
                       "An essay", "40 multiple-choice questions, ~60 minutes", "A live coding test", "An oral defence"], 1),
                   mcq("The official syllabus is best described as the exam's:", [
                       "Marketing brochure", "Test basis — it defines what is examined", "Defect report", "Release note"], 1),
               ]),

        lesson("istqb-02", "Syllabus map: what you already know", 11,
               "The CTFL syllabus looks intimidating until you map it to the courses you've completed. This lesson does exactly that and flags the few topics that need extra attention.",
               [
                 ("The map", table(
                     ["CTFL chapter", "What it covers", "Where you learned it here"],
                     [["1. Fundamentals of Testing", "What is testing, 7 principles, test process, psychology of testing", "Foundations: principles / STLC / vocabulary"],
                      ["2. Testing Throughout the SDLC", "SDLC models, test levels, test types, maintenance testing", "Foundations: SDLC / V-Model / levels & types / retest vs regression"],
                      ["3. Static Testing", "Reviews, static analysis, review process, roles", "Foundations: verification, static vs dynamic, Three Amigos"],
                      ["4. Test Analysis and Design", "Black-box, white-box, experience-based techniques, coverage", "Test Design course (full): EP, BVA, decision tables, state transitions, exploratory"],
                      ["5. Managing the Test Activities", "Test plan, risk, estimation, monitoring, configuration, defect management", "Test Docs + Defects courses"],
                      ["6. Test Tools", "Tool categories, benefits/risks, tool selection", "Tools, Postman, Playwright, CI/CD courses"]])),
                 ("Gaps to fill before the exam", """1. **Exact ISTQB definitions** — the exam uses specific wording. Drill the Glossary/Flashcards until terms like *test condition, test case, test procedure, test basis, confirmation testing, incident, testware* are precise.
2. **Static testing / reviews in detail** — roles (manager, moderator, author, reviewer, scribe), review types (informal, walkthrough, technical, inspection), and the review process steps. This is the thinnest area in most self-study plans.
3. **Test process vs test activities** — ISTQB's *test process* (planning, analysis, design, implementation, execution, evaluating exit criteria, closure) and the distinction between **test analysis** ('what to test') and **test design** ('how to test').
4. **Psychology of testing** — independence, the tester-developer relationship, constructive communication, and why testers need a different mindset from developers. (Your service-desk diplomacy is a genuine advantage here.)
5. **Maintenance testing** — testing after a change/migration, impact analysis, regression and confirmation testing."""),
                 ("A 2-week revision plan", """- **Days 1-4:** read the official syllabus once, then re-read chapter by chapter alongside the matching course here.
- **Days 5-8:** 2 timed mock exams per day; for every wrong answer, write the correct definition in your own words.
- **Days 9-11:** drill the glossary flashcards twice daily; focus on static testing and exact definitions.
- **Day 12:** one final timed mock, then stop. Sleep.

Track your mock scores; consistently >80% before booking. Use the **Flashcards** view in this app for the terminology drill."""),
               ],
               desk="You've revised for certifications before. Same method: syllabus → gap analysis → timed mocks → error log. The only difference is the vocabulary.",
               takeaway="~80% of CTFL is already covered here; focus extra study on static testing/reviews, exact definitions, test psychology and maintenance testing.",
               ex=[
                   mcq("Test ANALYSIS answers which question?", [
                       "'How do we run the test?'", "'WHAT do we test?' (identifying test conditions)", "'When do we stop?'", "'Who writes code?'"], 1,
                       "Design = HOW; analysis = WHAT."),
                   mcq("Which CTFL chapter is usually the biggest gap for self-studiers?", [
                       "Test design techniques", "Static testing / reviews", "Test principles", "Test levels"], 1),
                   mcq("An ISTQB 'inspection' is:", [
                       "A type of automated test", "A formal, documented static review with defined roles", "A defect severity", "A performance test"], 1),
               ]),

        lesson("istqb-03", "Terminology precision drill", 11,
               "ISTQB questions turn on single words. This lesson drills the pairs people confuse most — use the Flashcards view afterwards to make them automatic.",
               [
                 ("The confusion pairs", """| Pair | Distinction |
|---|---|
| **Error / Fault / Failure** | Human mistake → defect in code → observable wrong behaviour |
| **Verification / Validation** | Building the product *right* (static/docs) vs building the *right* product (execution) |
| **Test condition / test case / test procedure** | An item to verify / one case with steps+expected / ordered sequence of cases |
| **Test basis / test oracle** | Source of expected behaviour / how you decide a result is correct |
| **Severity / Priority** | Technical impact (QA) / business order (PO) |
| **Confirmation testing / Regression testing** | Re-run the failed case / re-run other cases for side effects |
| **Retesting / Regression** | Same as above — ISTQB says 'confirmation testing' |
| **Smoke / Sanity** | Broad shallow build check / narrow check of a specific change |
| **Static / Dynamic** | Nothing executes / software executes |
| **Black-box / White-box** | Spec-based / code-structure-based |
| **Test plan / Test strategy** | Release-specific / organisation-level |
| **Incident / Defect** | An event that needs investigation / a confirmed flaw (ISTQB treats incidents as *may or may not* be defects) |
| **Testware / Test environment** | All artefacts produced for testing / the configured setup they run in |
| **Coverage / Traceability** | How much of the basis is exercised / the links requirement→test→defect |"""),
                 ("Scenario practice", """*'A tester re-runs TC-014 after a fix and it passes; she then re-runs the other 30 cart cases.'* → The first is **confirmation testing**; the second is **regression testing**.

*'A tester reads the requirements document and finds an ambiguous sentence before any code exists.'* → **Static testing / verification**, shifting left.

*'The team reviews the release and agrees that 3 minor cosmetic defects with workarounds will ship.'* → **Residual risk**, documented and accepted by the PO at **test closure**.

*'The tester writes down the exact values, preconditions and expected result for one condition.'* → A **test case** derived from a **test condition** in the **test basis**.

Learn to spot the verb in the question: 'reads/reviews' → static; 'executes/runs' → dynamic; 're-runs the failed' → confirmation; 're-runs others' → regression."""),
               ],
               desk="P1 vs severity, incident vs problem, change vs release — you already live in a world where one word changes the whole process. This is the same precision, new glossary.",
               takeaway="Drill the confusion pairs until automatic; in scenarios, the verb tells you which concept is being tested.",
               ex=[
                   mcq("'Error → Fault → Failure' is the order of:", [
                       "Test levels", "Human mistake → code defect → observable wrong behaviour", "Severity levels", "SDLC phases"], 1),
                   mcq("ISTQB's term for re-running the previously FAILED test case is:", [
                       "Regression testing", "Confirmation testing", "Smoke testing", "Exploratory testing"], 1),
                   mcq("An 'incident' in ISTQB terms:", [
                       "Is always a defect", "Is an event requiring investigation that may or may not be a defect", "Is a severity level", "Is a test case"], 1),
                   inp("What do we call the collection of all artefacts produced during testing (cases, scripts, data, reports)? (8 letters)", ["Testware", "testware"], hint="Test + ware."),
               ]),

        lesson("istqb-04", "Exam strategy and after the certificate", 10,
               "A short, practical lesson on sitting the exam and on what to do with the credential once you have it — including how to present it honestly as a career changer.",
               [
                 ("In the exam", """- **Answer every question** (no negative marking); flag uncertain ones and return.
- **Read the last sentence first** — it usually contains the actual question ('which principle is illustrated?').
- Watch for **absolutes**: 'always', 'never', 'all', 'only' are usually wrong in a discipline built on context-dependence.
- Watch for **near-miss definitions**: an option that swaps 'verification' for 'validation' or 'severity' for 'priority' is a trap.
- For scenario questions, identify the **one activity** described before choosing.
- Budget ~1 minute per question; leave 10 minutes to review flagged ones.
- Eliminate obviously wrong options first; with 4 options, removing 2 doubles your odds."""),
                 ("Putting it on your resume", """List it as a **Certifications** section, not as experience:

```
CERTIFICATIONS
ISTQB Certified Tester Foundation Level (CTFL), 2026  [or "In progress — exam booked"]
ITIL 4 Foundation, 2023
```

If it's in progress, say so honestly ('Exam scheduled Nov 2026'). Never imply a certificate you don't hold. Place certifications below **Projects / Skills** on a career-changer resume — the portfolio still does the heavy lifting."""),
                 ("After the exam", """Keep the momentum: add the credential to LinkedIn (the 'Licenses & Certifications' section, with the issuing body and date), mention it in the first line of your cover letter, and then **go back to building**. The next steps are CTFL-AT (Agile Tester) or a tool-specific badge — but only after you've landed the role or built the automation portfolio. A wall of beginner certificates with no hands-on evidence is a red flag; one certificate plus four solid repos is a strong profile."""),
               ],
               desk="You know how to present a certification alongside real experience without overselling it. Same rule: credential = vocabulary, repos = proof.",
               takeaway="Answer everything, watch absolutes and near-miss definitions, flag and review; list the credential honestly below your projects; keep building afterwards.",
               ex=[
                   mcq("Which word in an ISTQB option is usually a warning sign?", [
                       "usually", "typically", "always", "may"], 2,
                       "Absolutes rarely hold in a context-dependent discipline."),
                   mcq("Where should a career changer place certifications on the resume?", [
                       "Above everything, replacing experience", "In their own section, below projects/skills", "In the footer only", "Nowhere"], 1),
                   mcq("If the exam is booked but not yet passed, you should:", [
                       "List it as passed", "Say 'in progress / exam scheduled' honestly", "Omit it entirely and never mention it", "Claim a different grade"], 1),
               ]),
    ],
    quiz="istqb-quiz",
)

# ---------------------------------------------------------------------------
# 18. Portfolio
# ---------------------------------------------------------------------------
PORTFOLIO = course(
    "portfolio", "Build a Portfolio That Gets Interviews", "Replace 'no QA experience' with proof",
    "Five concrete projects with deliverables and checklists: a full manual test suite, a defect hunt, an API collection, an automation framework, and publishing it all. This is the most important course for a career changer.",
    "#3df2c0", "p6", "Week 23-24", "Capstone",
    [
        lesson("port-01", "Why a portfolio is your substitute for experience", 11,
               "Every junior QA job ad asks for experience you don't have yet. A portfolio replaces that requirement with **observable evidence**: artefacts a hiring manager can open in 60 seconds and conclude 'this person can do the work'.",
               [
                 ("What a portfolio proves", """| Artefact | Proves |
|---|---|
| Test plan + 25 test cases + RTM | You can design tests systematically and trace requirements |
| 5 professional defect reports | You can find, reproduce and document problems |
| A Postman collection with assertions running in CI | You can test APIs and automate checks |
| A Playwright framework in CI with an HTML report | You can code, structure, and operate a test suite |
| A clean README + study notes | You can document and communicate |

For a career changer, this is **the** lever. Two or three of these links in a resume beat any number of 'I'm passionate about quality' paragraphs. Hiring managers rarely read a whole repo — they check the README, the file structure, one test case, one test script, and the CI badge. Optimise for that 60-second skim."""),
                 ("Choose a target application", """Pick a **real, public, free app** with enough depth: a demo e-commerce site (e.g. `automationexercise.com`, `saucedemo.com`, `demo.opencart.com`), a todo app, or an open-source project you can run locally with Docker. Requirements:

- Multiple user journeys (login, search, cart, checkout, account).
- Some real bugs (or you can deliberately seed your own in a local fork).
- No terms-of-service or privacy problem with testing it.
- Prefer an app with a documented API too, so projects 3 and 4 can reuse it.

Use the **same app across all five projects**. A coherent portfolio ('I tested ShopDemo end to end: manual, API, and automated') reads far better than five unrelated fragments."""),
                 ("The one-page portfolio site (optional but powerful)", """A single GitHub Pages site (or even a well-structured GitHub profile README) with: your name + target role, a 2-sentence summary, 4 project cards with links and a one-line 'what this proves', a skills list, your certifications, and contact links. Keep it fast, accessible and mobile-friendly — it's itself a demonstration of the quality mindset you're selling."""),
               ],
               desk="A portfolio is a knowledge base of *your work*: structured, searchable, and readable by someone who wasn't there. You already know what good documentation looks like from the inside.",
               takeaway="Evidence beats claims. Use ONE target app across all projects, optimise for a 60-second skim, and lead with links on the resume.",
               ex=[
                   mcq("Why does a portfolio matter most for a career changer?", [
                       "It's prettier than a resume", "It supplies observable evidence in place of QA job history", "Employers require a website", "It replaces interviews"], 1),
                   mcq("Using one target app across all projects is better because:", [
                       "It's less work only", "It tells a coherent end-to-end story", "Free apps are rare", "CI requires it"], 1),
                   mcq("A hiring manager typically skims:", [
                       "Every line of code", "The README, structure, one test case, one script, CI status", "Only the commit count", "Nothing"], 1),
               ]),

        lesson("port-02", "Project 1 — Full manual test suite", 12,
               "Your first and most important artefact: a complete, professional manual test suite for one feature of your target app. This single repo demonstrates the entire Phase 1 skill set.",
               [
                 ("Deliverables", """```
qa-portfolio-manual/
├── README.md                 # what/why/how, target app, scope, how to review
├── docs/
│   ├── test-plan.md          # all 13 sections from the Test Docs course
│   ├── requirements.md       # the AC you derived (your test basis)
│   └── rtm.md                # requirement → test case → defect links
├── test-cases/
│   └── checkout.md           # 25+ cases in a consistent tabular format
├── defects/
│   ├── DEF-001.md ...        # 5 professional defect reports
│   └── evidence/             # redacted screenshots / logs
└── reports/
    └── test-summary.md       # execution summary, exit criteria, residual risk
```"""),
                 ("How to make it stand out", """- **Derive 20-30 cases using named techniques** and label them: `EP-1`, `BVA-4`, `DT-3`, `ST-2`, `EX-1`. Add a short section explaining why each technique was used. That one detail proves you understand test design, not just copying a template.
- Include **positive, negative, boundary, state-transition and exploratory** cases.
- Add a **decision table** for at least one business rule (discounts, shipping, permissions).
- Add an **RTM** showing coverage and one deliberate gap with a reasoned 'accepted risk' note.
- Write 5 defect reports in the full format from the Defects course, with **anonymised evidence** and a repro rate.
- End with a **test summary report**: pass/fail/blocked counts, exit criteria checked item by item, residual risk, and a go/no-go recommendation.
- Keep the README crisp: 'What I tested', 'Techniques used', 'What I found', 'How to review in 2 minutes'."""),
                 ("A 2-minute review path", """Tell the reader exactly where to look: *'Start with `docs/test-plan.md` for scope, then `test-cases/checkout.md` rows 1-8 for boundary design, then `defects/DEF-003.md` for report quality, then `reports/test-summary.md` for the release decision.'* Guiding the reviewer is a documentation skill in itself — and it respects their time, which is exactly what good QA does."""),
               ],
               desk="This is a full incident/change documentation pack, applied to a product that doesn't exist yet. Your instinct for 'what would an auditor ask for?' is exactly the right one.",
               takeaway="One repo: plan + AC + RTM + 25 technique-labelled cases + 5 defect reports + summary with a release decision. Guide the reviewer.",
               ex=[
                   mcq("Labelling cases with 'BVA-4' or 'DT-3' demonstrates:", [
                       "Nothing", "Deliberate test-design technique choice, not a copied template", "Automation", "A severity scale"], 1),
                   mcq("Which section turns the suite into a *decision* artefact?", [
                       "The README", "A test summary report with exit criteria, residual risk and a recommendation", "The screenshots folder", "The file names"], 1),
                   mcq("Evidence in a public portfolio must be:", [
                       "As detailed as possible", "Anonymised / redacted with no real PII or credentials", "From production", "Omitted"], 1),
               ]),

        lesson("port-03", "Project 2 — Bug hunt & defect reports", 10,
               "A focused, credible 'I found real bugs' artefact. This is often the most persuasive single item for a service-desk-to-QA candidate, because finding and documenting problems is already your strength.",
               [
                 ("The exercise", """Spend **90 minutes in a structured exploratory session** on your target app (or a deliberately seeded local fork), then publish 5-8 defect reports. Use **session-based test management**:

```
Charter: Explore checkout with focus on form validation, boundaries and
         error messages. 90 min, no interruptions.
Notes:   what I covered, what I found, what I'd explore next, questions.
```

Use several **tours** (money tour for revenue paths, saboteur tour to break it, back-alley tour for neglected features) and an **error-guessing checklist** (empty, long, special characters, double-submit, back/refresh, timezone, concurrent tabs)."""),
                 ("What makes the artefact credible", """- Each report uses the full template: ID, title, severity, priority, environment/build, preconditions, numbered steps, exact test data, actual vs expected with the requirement reference, evidence, repro rate, workaround.
- Include a **mix** of severities (not five typos, not five 'critical' claims) and justify each severity.
- Include at least one **intermittent** defect with a quantified repro rate and the method you used to isolate it.
- Include one **non-functional** finding (accessibility, usability, or a client/server validation mismatch).
- Add a short **'bugs I did NOT log'** section (duplicates, 'works as designed', enhancement requests) with reasons — that shows triage judgement, which juniors usually lack.
- End with a **5 Whys** on the most serious finding and the regression case you'd add."""),
                 ("Seeding your own bugs (if the app has none)", """Fork a small open-source app locally and deliberately introduce 3-4 defects (an off-by-one discount, a missing null check, a broken `aria-label`, a duplicate-submit), document them in a `SEEDED-BUGS.md` **after** your hunt, and compare your found list against the seeded list. That comparison is a miniature **defect-detection-effectiveness** study — unusually sophisticated for a junior portfolio, and completely honest as long as you label it."""),
               ],
               desk="This is literally your current job, pointed at software before release. Lean into it: reproducibility, severity judgement, and evidence are where you already outperform most bootcamp grads.",
               takeaway="90-min chartered session → 5-8 full-format reports with mixed severities, an intermittent bug, triage exclusions and a 5 Whys. Optionally seed bugs and measure detection.",
               ex=[
                   mcq("What does a 'bugs I did NOT log' section demonstrate?", [
                       "Laziness", "Triage judgement (duplicates, by-design, enhancements)", "A defect", "Nothing"], 1),
                   mcq("An intermittent defect report should include:", [
                       "'Happens sometimes'", "A quantified repro rate and the isolation method", "Only a screenshot", "A Critical severity by default"], 1),
                   inp("What structured exploratory approach uses a charter, time box, session notes and a debrief? (acronym)", ["SBTM", "Session-based test management"], hint="Four letters, or the full phrase."),
               ]),

        lesson("port-04", "Project 3 & 4 — API collection and automation framework", 12,
               "The two technical repos that prove you can automate. Both should be public, documented, and running in CI — a green badge is worth more than a paragraph of claims.",
               [
                 ("Project 3: API test collection", """Deliverables (from the Postman course):

```
qa-portfolio-api/
├── collections/shop-api.postman_collection.json
├── env/staging.postman_environment.json   # placeholders only, NO secrets
├── data/order-cases.csv                    # data-driven negative/boundary cases
├── docs/test-design.md                     # the 20-case matrix + techniques
├── .github/workflows/api-tests.yml         # Newman run
└── README.md
```

Include ≥15 requests with assertions on **status, shape, business value, side effects, headers and timing**; positive AND negative cases; a create→read→delete flow chained via variables; a data-driven boundary set; and a workflow that uploads an HTML report on failure. Write a short **'defects found'** section with the assertion that catches each."""),
                 ("Project 4: Playwright framework", """```
qa-portfolio-playwright/
├── playwright.config.js        # 3 browsers, baseURL from env, traces on retry
├── tests/                      # 15-25 specs: smoke, checkout, auth, negative
├── pages/                      # Page Objects
├── fixtures/                   # auth fixture, test data, sample upload
├── .github/workflows/pw.yml
└── README.md
```

Must include: resilient `getByRole`/`getByLabel` locators, web-first assertions, at least one **data-driven boundary loop**, a **Page Object Model**, a custom **logged-in fixture**, tags (`@smoke`, `@regression`), and a CI workflow with `npm ci`, secrets, and an uploaded report. Add a `docs/flaky-test-journal.md` documenting one flake you diagnosed and fixed — that single file demonstrates maturity most juniors can't show."""),
                 ("READMEs and CI badges", """Every repo README needs: a one-sentence purpose, the **target role/skill it demonstrates**, prerequisites, exact run commands, expected output, the test-approach summary, a screenshot or link to a green CI run, and a 'what I'd improve next' section. Add the workflow badge (`![tests](.../badge.svg)`) at the top. A green badge that goes red tells the truth — don't fake a static image.

Keep secrets out, keep `.gitignore` correct, and make small readable commits with real messages. Reviewers absolutely look at commit history."""),
               ],
               desk="A runnable script with a documented procedure and a green scheduled run is something you've built on the desk. These repos are that, plus test assertions and public documentation.",
               takeaway="Two public repos: an asserted Postman collection + Newman CI, and a Playwright POM framework + CI. Both with strong READMEs, no secrets, and honest green badges.",
               ex=[
                   mcq("Which file must NEVER contain real credentials in a public repo?", [
                       "README.md", "The Postman environment JSON / .env", "The test-design doc", "The workflow badge"], 1),
                   mcq("A 'flaky-test-journal.md' mainly demonstrates:", [
                       "That your tests are unreliable", "Diagnostic maturity — you found and fixed a root cause", "Extra typing", "A CI requirement"], 1),
                   mcq("What should a CI badge reflect?", [
                       "A static green image", "The real workflow status, even if it sometimes goes red", "The number of tests", "Your certification"], 1),
               ]),

        lesson("port-05", "Publish, present and keep it alive", 11,
               "A finished repo nobody can find is not a portfolio. This lesson covers publishing, the 60-second skim, and talking about your projects in an interview without rambling.",
               [
                 ("Publishing checklist", """- GitHub profile: real name, photo, a headline like *'Service Desk Technician → Software QA Analyst'*, location, and a **profile README** linking your 4 repos.
- Each repo: description, topics/tags (`qa`, `playwright`, `postman`, `testing`), a licence, and a pinned status on your profile.
- **GitHub Pages** (free) for a one-page portfolio site, or a simple `README.md` on a repo named after your username.
- Pin your **4 best** repos, not all 20 learning scratch repos. Archive or delete the messy ones.
- Optional: a short blog post ('How I tested a checkout flow from scratch') on dev.to / Medium / LinkedIn. Writing about your work multiplies its reach and demonstrates communication."""),
                 ("The 60-second interview walkthrough", """Prepare a **90-second** story for each repo using this shape:

> *'The problem: I had no QA job history, so I needed evidence. I picked a demo shop and wrote a test plan plus 28 cases — here's the decision table for the discount rules and the boundary set. I found 6 defects; this one is intermittent, so I quantified the repro rate and isolated it to a double-submit. Then I automated the API checks with Postman assertions running in Newman, and the top 12 UI journeys in Playwright with Page Objects and CI. Everything's in the README. The hardest part was X, and I'd add Y next.'*

Lead with the **decision/technique**, not the tool list. Be ready for 'why did you choose that technique?', 'what would you test next?', and 'what did you deliberately NOT test?' — all of which this app has prepared you for."""),
                 ("Keep it alive", """A stale portfolio decays. After you land the role, keep one repo updated with a new technique, refresh CI so the badge stays green, and add a 'what changed' note. Also: your **first 90 days on the job** will generate far better material than any demo app — with permission, anonymise and publish a sanitised test approach or a talk. The portfolio is a habit, not a one-off project."""),
               ],
               desk="A well-maintained knowledge base with clear ownership and a link people can actually find is the same discipline. Pin the good ones; archive the scratch.",
               takeaway="Publish and pin 4 repos, add a profile README or one-page site, prepare a 90-second story per project, and keep CI green after you're hired.",
               ex=[
                   mcq("In an interview, lead a project walkthrough with:", [
                       "A list of tools", "The problem, the test decisions/techniques, and what you found", "Your commit count", "The framework version"], 1),
                   mcq("How many repos should you PIN on GitHub?", [
                       "All of them", "Your 4 best, polished ones", "None", "Only forks"], 1),
                   mcq("A static fake green CI badge is:", [
                       "Fine", "Dishonest — link the real workflow status", "Required", "Better for performance"], 1),
               ]),
    ],
    quiz="portfolio-quiz",
)

# ---------------------------------------------------------------------------
# 19. Communication (placed late but relevant throughout)
# ---------------------------------------------------------------------------
COMMUNICATION = course(
    "communication", "Communication & Collaboration for QA", "The skill that gets you promoted",
    "Writing clearly, asking requirements questions, disagreeing about quality without friction, running defect triage and handoffs, and documenting for humans. Drawn directly from service desk strengths.",
    "#ff8a3d", "p1", "Weeks 5-6 (ongoing)", "Core",
    [
        lesson("comm-01", "Writing so engineers can act", 10,
               "QA produces a lot of writing: defect reports, test cases, summaries, questions, release notes. The measure of all of it is the same: can the reader act without coming back to you?",
               [
                 ("Principles", """1. **Lead with the conclusion.** 'Recommend no-go: DEF-1042 (Critical, payments) is still open.' Then the evidence. Engineers and managers read the first line.
2. **Be specific, not emphatic.** 'Total shows $96.00, expected $108.00' beats 'totally broken!!!'. Facts scale; exclamation marks don't.
3. **One idea per sentence, one issue per ticket.**
4. **Name the artefact**: build, URL, ID, version, environment. 'The staging build' is not an identifier.
5. **Separate observation from inference.** 'Response returned 96.00' (fact). 'Suspect the coupon listener fires twice' (clearly labelled hypothesis).
6. **State the ask.** 'Please clarify whether the 30-minute expiry is inclusive' — don't leave an implicit question.
7. ** Write for the reader's context**: a developer wants repro steps and logs; a PO wants impact and a decision; a future tester wants preconditions and cleanup."""),
                 ("Before/after examples", """| Before | After |
|---|---|
| *'Checkout is broken again, pls fix ASAP'* | *'[Cart] Discount applied twice with SAVE10 on orders over $100 — staging build 2026.04.7. Steps + actual/expected + HAR attached. Severity Major, blocks TC-022.'* |
| *'Testing done, looks fine'* | *'148/150 planned cases executed; 2 blocked by the staging data outage (low-risk). 0 open Critical. Recommend go, with DEF-512 deferred. Details in test-summary.md.'* |
| *'What about coupons?'* | *'AC-2 doesn't say what happens when two coupons are applied, or when one expires mid-checkout. Can we agree the rule before development starts?'* |"""),
                 ("Tone", """Write about **the system**, not the person: 'the total is recomputed twice', not 'the dev broke it again'. QA is often the bearer of bad news; being consistently calm, factual and solution-oriented is what earns you the influence to say 'not yet' and be listened to. Never use a defect report to score points."""),
               ],
               desk="You already write ticket updates for very different audiences (user, L2, manager, auditor). This is that skill with the QA artefacts as the output.",
               takeaway="Lead with the conclusion, be specific, name artefacts, separate fact from hypothesis, state the ask, write about the system.",
               ex=[
                   mcq("Which is the best opening line for a test summary?", [
                       "'Testing went well overall'", "'Recommend no-go: DEF-1042 (Critical, payments) remains open'", "'Please see below'", "'Lots of tests were run'"], 1),
                   mcq("'Suspect the coupon listener fires twice' should be labelled as:", [
                       "An observed fact", "A hypothesis, separate from the observed values", "A defect", "A requirement"], 1),
                   mcq("Why write about the system rather than the person?", [
                       "It's shorter", "It keeps the report factual and preserves working relationships", "It's required by Jira", "It raises severity"], 1),
               ]),

        lesson("comm-02", "Asking the awkward requirements question", 11,
               "The highest-value thing a QA Analyst does in refinement is ask the question nobody else thought of. This lesson gives you a repeatable question set — and the confidence to use it.",
               [
                 ("The question checklist", """For every story, work through:

- **Happy path**: what exactly should happen on success? what is the observable result?
- **Boundaries**: what are the min/max/empty values? is that inclusive?
- **Negative paths**: what happens for invalid input, expired links, missing records, no permission?
- **States**: what states can this object be in? which transitions are forbidden?
- **Combinations**: do these conditions interact (decision table)?
- **Data**: what test data exists? who creates it? any PII/masking?
- **Role/permission**: who is allowed? what about guest, suspended, admin?
- **Non-functional**: performance target, accessibility, error messages, logging, mobile?
- **Failure**: what if the third party is down / the request times out / the user double-clicks?
- **Oracle**: how will we know the result is right?
- **Out of scope**: what are we explicitly NOT doing?"""),
               ],
               desk="'What exactly did the user do before it broke? What state was their account in?' — you ask these on every ticket. Point them *forward* at a story instead of backward at an incident and you're doing shift-left requirements review.",
               takeaway="Use a fixed question set per story; ask before coding; frame unknowns as decisions to agree, not criticism.",
               ex=[
                   mcq("When should QA raise acceptance-criteria questions?", [
                       "After release", "During refinement / before development", "Only in the retrospective", "Never"], 1),
                   mcq("'How will we know the result is right?' is asking for the:", [
                       "Test environment", "Test oracle", "Severity", "Build number"], 1),
               ]),

        lesson("comm-03", "Disagreeing about quality without friction", 11,
               "You will sometimes have to say 'this shouldn't ship'. Doing that well is a career-defining skill — and it's mostly preparation, evidence and framing, not volume.",
               [
                 ("A framework for the hard conversation", """1. **Get the criteria agreed in advance.** Exit criteria in the test plan and the Definition of Done mean a no-go is a *measured* result, not your personal opinion. Most conflict disappears when the standard exists before the pressure.
2. **Lead with shared goals.** 'We both want a clean launch. Here's the risk I can see.'
3. **State facts and impact, not verdicts.** 'Payments fail for all users on build 2026.04.7, 5/5 repros, no workaround. Impact: 100% of revenue transactions.'
4. **Offer options, with trade-offs.** 'We can (a) hold the release 4 hours for the fix, (b) ship with the feature flag off, or (c) accept the risk with PO sign-off and a documented rollback.' Options turn you from a blocker into a decision partner.
5. **Escalate with evidence, not emotion.** If the decision goes against your recommendation, record the **accepted residual risk** in writing (PO sign-off in the ticket), and move on professionally. You have done your job.
6. **Never** say 'I told you so' afterwards. Do a blameless 5 Whys instead."""),
                 ("Phrases that help", """- *'Here's the evidence; what am I missing?'* — invites collaboration.
- *'What would we need to be true to feel safe shipping?'* — makes it a shared problem.
- *'I can't sign off on this criterion yet, but here's the smallest scope that unblocks us.'*
- *'Let's write down the accepted risk and who owns it.'*

Avoid: 'this is garbage', 'the devs always do this', 'I'm blocking the release', and any version of 'not my problem'."""),
               ],
               desk="Escalating a risky change up the chain with evidence, options and a rollback plan is exactly what you do on the desk. Same conversation, earlier in the lifecycle.",
               takeaway="Agree criteria in advance; lead with shared goals; state facts + impact; offer options; document accepted risk; stay blameless.",
               ex=[
                   mcq("What most reduces conflict when QA recommends 'no-go'?", [
                       "A louder email", "Exit criteria agreed in advance, so the decision is measured", "Escalating immediately", "Deferring silently"], 1),
                   mcq("If the PO ships over your objection, you should:", [
                       "Argue until they change their mind", "Record the accepted residual risk with PO sign-off and move on", "Delete your test report", "Say nothing ever"], 1),
                   mcq("The best framing for a risk conversation is:", [
                       "'I'm blocking the release'", "'We both want a clean launch; here's the risk and three options'", "'The devs did it again'", "'Not my problem'"], 1),
               ]),

        lesson("comm-04", "Triage, handoffs and documentation habits", 10,
               "The daily collaboration mechanics: running a triage meeting, handing a defect to a developer, and keeping documentation that survives you.",
               [
                 ("Running defect triage well", """Agenda for a 15-minute triage: **new** defects since last time (is it real? duplicate? severity? priority? owner? which release? does it block testing? workaround?), **stale** defects (nothing moved in N days), **reopened** defects (fix quality), **deferred** ones (still accepted?), and **escapes** (add a regression case). End by reading out the decisions and who owns each.

Rules: no defect sits in 'New' > 1 day; no rejection without a reason; no 'Fixed' without a build number; no silent priority changes. Keep the meeting short and the decisions in the tracker, not in the room."""),
                 ("The perfect handoff", """When a defect goes to a developer, include everything they need to reproduce without asking you: exact build, environment, role, data, minimal steps, actual vs expected, evidence, repro rate, and a labelled hypothesis. Then **be available**: offer to reproduce it together on a call. A 5-minute pairing session often saves a day of ping-pong — and it builds the relationship that makes the next hard conversation easier."""),
                 ("Documentation that survives you", """- Keep a **decision log**: '2026-04-07: PO agreed expired links are inclusive of the 30th minute.' Ambiguity resolved once, recorded forever.
- Keep a **known-issues / workarounds** list for the support team — you of all people know how much time that saves.
- Keep a **personal bug taxonomy** and a **runbook** for the environment ('how to seed staging data', 'how to get a fresh token').
- Write for the person who joins in six months: plain language, exact commands, no tribal knowledge.

> **From the desk:** you are the person who has *received* bad handoffs for years. Being the colleague who never sends one is an immediate, visible reputation win in your first QA role."""),
               ],
               desk="A good shift handover, a known-error database and a runbook are precisely these three habits. You already know the cost of a bad one.",
               takeaway="Short triage with explicit decisions; complete handoffs; decision logs, known-issues lists, bug taxonomy and runbooks.",
               ex=[
                   mcq("Which rule belongs in healthy defect triage?", [
                       "'Fixed' without a build number is fine", "No defect sits in 'New' for more than a day", "Rejections need no reason", "Priorities change silently"], 1),
                   mcq("A decision log mainly prevents:", [
                       "CI failures", "Re-litigating the same ambiguity months later", "Slow tests", "Browser bugs"], 1),
                   inp("What do we call the shared list of open issues and workarounds handed to support? (12 letters)", ["Known-issues", "Known issues", "known-issues list"], hint="'Known ...' list."),
               ]),
    ],
    quiz="communication-quiz",
)

# ---------------------------------------------------------------------------
# 20. Career & interviews
# ---------------------------------------------------------------------------
CAREER = course(
    "career", "Landing the QA Job", "From application to first 90 days",
    "Reposition your service desk experience, rewrite your resume section by section, prepare LinkedIn/GitHub, 40+ interview Q&As (manual, SQL, API, automation, behavioural), take-home exercises, job-search strategy, and your first 90 days.",
    "#ff5470", "p6", "Week 24", "Job search",
    [
        lesson("career-01", "Repositioning your experience", 12,
               "Your resume currently describes a service desk job. It needs to describe a *future QA Analyst with directly relevant evidence*. This lesson is the translation work that makes everything else land.",
               [
                 ("Before/after bullet rewrites", table(
                     ["Service desk bullet (before)", "QA-ready bullet (after)"],
                     [["Resolved 40+ tickets/day for application issues", "Investigated and reproduced 40+ reported application defects daily, isolating root conditions from logs and user steps"],
                      ["Escalated complex issues to L2/L3", "Produced structured, evidence-backed defect escalations with severity, repro steps and impact, enabling engineering resolution"],
                      ["Wrote knowledge base articles", "Authored reusable documentation of expected system behaviour and verification procedures"],
                      ["Ran SQL queries to check ticket data", "Validated back-end data integrity with SQL to confirm reported behaviour against persisted records"],
                      ["Managed P1-P4 incidents to SLA", "Triaged issues by business impact and urgency, communicating risk and workarounds to stakeholders"],
                      ["Handled password reset requests", "Supported authentication and access-control workflows; identified recurring failure patterns"],
                      ["Tested fixes before closing tickets", "Performed confirmation (retest) and regression checks on fixes before closure"]])),
                 ("The summary statement", """**Before:** *'Service Desk Technician with 4 years of IT support experience seeking a new challenge.'*

**After:** *'Service Desk Technician (4 yrs) transitioning to Software QA Analyst. Investigated and documented 3,000+ application defects; strong in structured reproduction, log/SQL-based verification, impact-based triage and clear technical writing. Built a QA portfolio: a 28-case manual test suite with RTM, a 20-case Postman API collection running in Newman CI, and a Playwright framework in GitHub Actions. ISTQB CTFL (in progress). Seeking a manual/API QA role where I can prevent defects before release.'*

Notice: **transferable evidence + new proof (portfolio) + clear target + honest status**. No apology, no 'no experience' framing."""),
                 ("Skills section that passes filters", """Group honestly by proficiency:

```
TESTING        Manual functional testing · Test design (EP, BVA, decision tables,
               state transitions) · Test plans & cases · RTM · Defect lifecycle ·
               Exploratory/SBTM · Regression & confirmation testing · UAT support
API & DATA     REST · Postman (pm.test assertions, environments, Newman) ·
               SQL (SELECT, JOIN, GROUP BY) · JSON/schema checks · Auth (401/403, IDOR)
AUTOMATION     Playwright (locators, fixtures, POM, data-driven, CI) · Git ·
               GitHub Actions · JavaScript (basics)
TOOLS          Jira/JQL · TestRail · Browser DevTools/HAR · VS Code · Linux CLI
NON-FUNCTIONAL Accessibility (WCAG AA, axe, keyboard) · Performance basics (k6) ·
               OWASP Top 10 awareness
```

Only list what you could defend for 5 minutes in an interview. Keyword filters matter, but an inflated skills list is a trap you'll walk into live."""),
               ],
               desk="You are not hiding your past — you are translating it. Every bullet above is something you genuinely did; the rewrite just uses the vocabulary of the job you're applying for.",
               takeaway="Translate tickets→defects, triage→severity/risk, KB→documentation, SQL→data verification. Lead with evidence + portfolio, never apologise for the switch.",
               ex=[
                   mcq("The best summary statement framing is:", [
                       "'No QA experience but willing to learn'", "'Escaping the helpdesk'", "'Transferable investigation experience + portfolio proof + clear target role'", "'Looking for any job'"], 2),
                   mcq("Why only list skills you can defend for 5 minutes?", [
                       "Resume space", "Inflated skills get exposed in live interviews", "ATS rules", "It's illegal"], 1),
                   mcq("'Tested fixes before closing tickets' maps to:", [
                       "Unit testing", "Confirmation (retest) and regression testing", "Load testing", "Static analysis"], 1),
               ]),

        lesson("career-02", "Resume, LinkedIn and GitHub makeover", 12,
               "A step-by-step makeover of the three surfaces a recruiter sees, with the ordering and keyword choices that matter for a career-change application.",
               [
                 ("Resume structure (one page, reverse-chronological)", """```
NAME  ·  Service Desk Technician → Software QA Analyst
[city] · [phone] · [email] · linkedin.com/in/... · github.com/...

SUMMARY           2-3 lines (from the previous lesson)

PROJECTS          ★ LEAD WITH THIS for a career changer
  QA Portfolio — Manual Test Suite (github.com/...)     [2 bullets]
  API Test Collection — Postman + Newman CI (...)       [2 bullets]
  Playwright Framework — POM + GitHub Actions (...)     [2 bullets]

SKILLS            grouped, keyword-rich, honest

EXPERIENCE
  Service Desk Technician | Company | 2022-present
    - 3-4 QA-translated bullets (impact + numbers)

CERTIFICATIONS    ISTQB CTFL (in progress) · ITIL 4 · ...

EDUCATION         degree / diplomas
```

Put **Projects above Experience** — that's the single biggest structural change for a career changer. Use numbers (tickets/day, defects documented, cases written, SLA %). Keep it to one page, PDF, with a plain filename (`Firstname_Lastname_QA_Analyst.pdf`). No photo, no tables that break ATS parsers, no 'References available on request'."""),
                 ("LinkedIn", """- **Headline:** `Service Desk Technician → Software QA Analyst | Manual & API testing | Playwright | ISTQB CTFL (in progress)` — not 'Seeking opportunities'.
- **About:** your 3-line summary + portfolio links + what role you want.
- **Featured section:** pin the 3 portfolio repos and a post about your journey.
- **Experience:** use the rewritten bullets; add a **Projects** section with links.
- **Skills:** add the top 15 QA skills; ask 2-3 colleagues to endorse the transferable ones (documentation, troubleshooting, SQL).
- **Activity:** post once a week about something you learned ('today I learned why 401 ≠ 403'). It's low-cost visibility and proves ongoing learning.
- Turn on **'Open to work'** for recruiters only if you're comfortable; set the title to 'QA Analyst / Software Tester'."""),
                 ("GitHub and the ATS", """GitHub: real name/photo, profile README, pinned 4 repos, green CI badges, topics/tags. For **ATS (Applicant Tracking Systems)**: mirror the exact phrases from the job ad ('manual testing', 'test cases', 'defect tracking', 'Agile/Scrum', 'SQL', 'API testing') where they're genuinely true; use standard section headings; avoid text-in-image; submit in the requested format. Then, because machines are imperfect, **find a human**: comment thoughtfully on a QA post, ask for a 15-minute chat, or apply via a referral."""),
               ],
               desk="You've filled in plenty of forms where the wording decides whether you get through. ATS keywords are the same game — with a human referral as the workaround.",
               takeaway="Projects above experience, one page, quantified bullets; rewrite LinkedIn headline/About/Featured; mirror real ATS keywords and find a human referral.",
               ex=[
                   mcq("For a career changer, what goes ABOVE work experience on the resume?", [
                       "Education", "Projects / portfolio", "References", "Hobbies"], 1),
                   mcq("Which LinkedIn headline is strongest?", [
                       "'Seeking opportunities'", "'Service Desk Technician'", "'Service Desk → Software QA Analyst | Manual & API testing | Playwright'", "'Hard worker'"], 2),
                   mcq("ATS keyword advice:", [
                       "Stuff in invisible keywords", "Mirror genuine phrases from the job ad in standard sections", "Use only images", "Avoid all technical terms"], 1),
               ]),

        lesson("career-03", "Job search strategy and the cover letter", 11,
               "Which roles to target, where to find them, how to apply without burning out, and a cover letter template that handles the career change in one confident paragraph.",
               [
                 ("Titles to search (and which to avoid at first)", """**Target:** QA Analyst · Software Tester · Manual QA Tester · Test Analyst · Functional Test Analyst · Junior QA Engineer · QA Specialist · UAT Analyst · Quality Assurance Analyst · Software QA Technician · Test Engineer (junior).

**Also worth it:** Application Support + Testing hybrid, QA with SQL/data focus, 'QA Analyst (manual, automation training provided)' — your support background is an advantage on these.

**Be cautious with:** 'SDET / Senior Automation Engineer / 3+ years Playwright' as a first application (aim at those after 12-18 months), and 'QA Lead/Manager'. Don't self-reject from a role requiring 1-2 years if your portfolio is strong — those ads are often flexible. Read the *responsibilities*, not just the years."""),
                 ("Where and how to apply", """Boards: LinkedIn Jobs, Indeed, Reed, CV-Library, Otta/Welcome to the Jungle, company career pages, and **recruiters specialising in QA/testing**. Also: local tech meetups, Ministry of Testing community, and LinkedIn posts from QA leads.

Volume with quality: aim for **5-8 tailored applications a week**, not 50 generic ones. For each, spend 10 minutes: mirror 3 keywords, add one line about their product/domain, and if you can find the hiring manager or a tester there, send a short, non-desperate note. Track everything in a spreadsheet: company, role, date, link, contact, status, follow-up date, notes. Follow up once after ~7-10 days.

**Referrals beat cold applications by a wide margin.** A 15-minute chat with someone on the team is worth more than ten portal submissions."""),
                 ("A cover letter template", """```
Dear [Hiring Manager name],

I'm applying for the [exact title] role at [Company]. I've spent four years as a
Service Desk Technician investigating and documenting application problems —
reproducing defects from user reports, isolating causes with logs and SQL, and
triaging by business impact. I want to move upstream and prevent those problems
before release, so I've built the skills and the evidence to do it.

Over the last six months I completed a structured QA curriculum and built a
portfolio: a 28-case test suite with a traceability matrix and 6 defect reports
for [app], a 20-case Postman API collection with automated assertions running in
CI, and a Playwright framework using Page Objects and GitHub Actions. [One line
about their product/domain and why it interests you.]

My support background means I bring something many junior testers don't: real
familiarity with how software fails for users, calm structured triage, and
documentation that engineers can act on. I'd welcome the chance to show you the
portfolio and talk through how I'd test [a specific feature of their product].

Kind regards, [Name] · [links]
```

The career change is handled in **one confident paragraph**, then immediately backed by proof. Never apologise for it."""),
               ],
               desk="Job hunting is a pipeline with stages and follow-ups — you manage those for a living. Track it like a queue: status, owner, next action, SLA.",
               takeaway="Target junior/manual/API QA titles; 5-8 tailored applications a week plus referrals; one-paragraph career-change cover letter backed by portfolio links.",
               ex=[
                   mcq("Which role is a sensible FIRST target?", [
                       "Senior SDET", "QA Lead", "Junior/Manual QA Analyst or UAT Analyst", "QA Manager"], 2),
                   mcq("What beats a cold portal application most reliably?", [
                       "More keywords", "A referral / short conversation with someone on the team", "A longer resume", "Applying twice"], 1),
                   mcq("How should the cover letter handle the career change?", [
                       "Apologise at length", "One confident paragraph, immediately backed by portfolio evidence", "Never mention it", "Blame the old employer"], 1),
               ]),

        lesson("career-04", "The interview loop and 15 essential manual QA Q&As", 14,
               "What the QA interview process actually looks like, then a drilled set of the questions that come up in almost every first-role interview — with model answers you can adapt.",
               [
                 ("The typical loop", """1. **Recruiter screen (20-30 min):** motivation for the switch, salary, notice period, right-to-work, basic terminology. Have your 30-second 'why QA' answer ready.
2. **Hiring manager / technical QA interview (45-60 min):** test design, defect lifecycle, STLC, tooling, scenarios, and your portfolio walkthrough.
3. **Practical exercise:** write test cases for a login page / a pen / an ATM, find bugs in a sample app, write SQL, or review a bug report. Sometimes take-home, sometimes live.
4. **Team / behavioural interview (30-45 min):** STAR stories, collaboration, conflict about quality.
5. **Offer.**

Anything called a 'live bug hunt' is testing your *process*: talk aloud, state your charter, note what you'd log and what you wouldn't, and prioritise."""),
                 ("Q&A drill — fundamentals & design", """**Q: What is the difference between QA and QC?**
A: QA is *process-focused* and preventive (standards, reviews, improving how we build); QC is *product-focused* and detective (actually checking the artefact). Testing is a QC activity within a QA mindset.

**Q: Explain severity vs priority with an example.**
A: Severity = technical impact (QA sets it); priority = business urgency (PO sets it). A misspelled logo before a launch demo is Trivial severity but P1 priority.

**Q: Retesting vs regression testing?**
A: Confirmation/retesting re-runs the failed case after a fix; regression re-runs other previously-passing cases to catch side effects.

**Q: What are the 7 testing principles?**
A: Testing shows presence of defects not absence; exhaustive testing impossible; early testing; defects cluster; pesticide paradox; testing is context dependent; absence-of-errors is a fallacy. (Name all 7, then briefly explain 2.)

**Q: How would you test a login page?**
A: Don't just list happy path. Structure it: valid credentials; invalid password/email; locked account; unknown email (no enumeration); empty fields; SQL/script injection strings; very long inputs; boundary on password length; remember-me/session; logout; password reset link; 2FA; concurrent sessions; keyboard-only and accessibility; error messages; network failure; brute-force rate limiting; SQL verification that no session row is created for a failed login.

**Q: Design test cases for a field accepting 1-100.**
A: Equivalence classes: below (0), in-range (50), above (101), plus non-numeric/empty/null. BVA adds 0,1,2,99,100,101. Mention both techniques by name.

**Q: What is STLC?**
A: Requirement analysis → test planning → test case development → environment setup → execution → cycle closure, with entry/exit criteria and deliverables each.

**Q: What makes a good bug report?**
A: Unique ID, clear title, severity/priority, environment+build, preconditions, minimal numbered steps, exact test data, actual vs expected (with AC reference), evidence, repro rate, workaround, one issue per ticket.

**Q: What is a test plan? What's in it?**
A: Release-specific scope (in AND out), approach, environment/tools, data, roles, schedule, risks+mitigations, defect management, entry/exit criteria, deliverables, approvals. Distinguish from a test strategy.

**Q: What is exploratory testing? Is it just random clicking?**
A: No — simultaneous learning, design and execution, structured with a charter, time box, session notes and a debrief (SBTM), using tours and an error-guessing checklist.

**Q: When would you NOT automate a test?**
A: One-off/changing features, subjective usability/visual checks, unclear expected results, or flaky uncontrolled dependencies. Automate stable, repetitive, high-risk checks with a clear oracle.

**Q: What is the test pyramid?**
A: Many fast unit tests, some API/integration tests, few E2E UI tests; pushing checks down reduces cost and flakiness.

**Q: How do you decide what to test when there isn't time?**
A: Risk-based: score likelihood × impact, allocate depth/technique/automation to high-risk areas, and explicitly record low-risk areas as accepted residual risk with PO agreement.

**Q: What is a traceability matrix?**
A: Links requirements → test cases → defects to prove coverage, spot gaps/orphans, and support impact analysis when a requirement changes.

**Q: A developer says 'works as designed' but you disagree. What do you do?**
A: Don't argue in the ticket. Check the AC/spec, take it to refinement, get the requirement clarified (or the AC updated), and record the decision. If it's genuinely user-impacting, raise it as a usability/requirements concern with evidence."""),
                 ("How to answer", """Use the **PREP** shape: **Point** (one-sentence answer), **Reason** (why), **Example** (a concrete one from your portfolio or desk), **Point** (restate). Interviewers are not grading poetry — they want to see structured thinking, correct vocabulary and self-awareness. If you don't know, say *'I haven't done that hands-on, but here's how I'd approach it...'* — honesty plus reasoning beats bluffing every time."""),
               ],
               desk="These are the same questions as 'walk me through how you'd troubleshoot X' — structured, methodical, and honest about what you'd check first. You've been answering them informally for years.",
               takeaway="Know the loop; drill the 15 core Q&As; structure answers as Point–Reason–Example–Point; never bluff, reason out loud.",
               ex=[
                   mcq("'Testing shows the presence of defects' implies:", [
                       "Bugs never exist", "Passing tests can't prove the software is defect-free", "Testing is unnecessary", "All tests must fail"], 1),
                   mcq("A good 'test a login page' answer:", [
                       "Lists only the happy path", "Structures positive, negative, boundary, security, session and accessibility cases", "Says 'I'd click around'", "Only mentions automation"], 1),
                   inp("What 4-letter structure means Point–Reason–Example–Point for interview answers?", ["PREP"], hint="A mnemonic for structured answers."),
               ]),

        lesson("career-05", "SQL, API and automation interview questions", 13,
               "Technical rounds for QA roles are usually *shallow but precise*: a few SQL queries, API status/auth questions, and automation concepts. Here are the ones that actually get asked, with model answers.",
               [
                 ("SQL questions", """**Q: Find all failed test cases.**
```sql
SELECT id, title FROM test_cases WHERE status = 'Failed';
```

**Q: Count test cases per status.**
```sql
SELECT status, COUNT(*) FROM test_cases GROUP BY status;
```

**Q: List testers with their test case titles.**
```sql
SELECT t.name, tc.title
FROM testers t
JOIN test_cases tc ON t.id = tc.owner_id;
```

**Q: Find test cases with NO defects.**
```sql
SELECT tc.id, tc.title
FROM test_cases tc
LEFT JOIN defects d ON tc.id = d.test_case_id
WHERE d.id IS NULL;
```

**Q: `= NULL` vs `IS NULL`?**
A: NULL is *unknown*, so `= NULL` never evaluates true; you must use `IS NULL` / `IS NOT NULL`. Also `COUNT(*)` counts rows while `COUNT(col)` skips NULLs.

**Q: WHERE vs HAVING?**
A: WHERE filters rows before grouping; HAVING filters groups after aggregation.

**Q: How would you verify a UI 'order created' message?**
A: Query the orders table for the exact reference; check exactly one row, the total, status, child order_items, and an audit/outbox record. Use an independent calculation as the oracle."""),
                 ("API questions", """**Q: 401 vs 403?** A: 401 = unauthenticated (missing/invalid token); 403 = authenticated but forbidden (wrong role/scope).

**Q: POST vs PUT?** A: POST creates (not idempotent — repeating can create duplicates); PUT replaces a whole resource and is idempotent; PATCH partially updates.

**Q: What would you test on `POST /orders`?** A: Valid → 201 + Location + correct body; missing/wrong-type fields → 400/422 with no partial write; boundary/extra fields; no auth → 401; wrong role → 403; duplicate POST → two orders unless an Idempotency-Key; injection strings; follow-up GET and DELETE→GET 404.

**Q: How do you test authentication?** A: The 8-row matrix: valid, missing, malformed, expired, insufficient role, cross-user/IDOR, post-logout, tampered signature.

**Q: What is a contract test?** A: Verifies the agreed request/response shape between consumer and provider, catching breaking changes before integration.

**Q: UI shows wrong data but the API response is correct — where's the bug?** A: Front-end rendering/state. Attach the response + screenshot. If the response itself is wrong, it's back-end."""),
                 ("Automation questions", """**Q: What is a flaky test and how do you fix one?** A: Passes/fails without a code change. Reproduce with repeats, read the call log, replace fixed sleeps with condition waits, make locators strict/unambiguous, remove ordering dependencies and shared data, stabilise the environment, then quarantine+fix or delete. Never just raise retries.

**Q: Why Page Object Model?** A: Selectors/actions live in one class, so a UI change is fixed once instead of in every test; tests read as business rules.

**Q: How do you choose locators?** A: Prefer `getByRole`/`getByLabel`/`getByText`/`data-testid`; avoid absolute XPath and positional nth-child; scope with `filter()`.

**Q: What is auto-waiting?** A: Playwright waits for elements to be visible/stable/enabled and retries web-first assertions, removing arbitrary sleeps.

**Q: How do tests run in CI?** A: GitHub Actions: checkout → setup-node → `npm ci` → install browsers → run tests with secrets → upload the HTML report `if: always()`; the job is a required status check for merges."""),
               ],
               desk="You've talked a user through a status code or a query result before. These answers are that explanation, formalised and tightened to 3 sentences.",
               takeaway="Drill the SQL query set, the 401/403 and POST/PUT distinctions, the 8-row auth matrix, and flake/POM/locator/auto-wait/CI explanations.",
               ex=[
                   mcq("Which query counts test cases per status?", [
                       "SELECT COUNT(*) FROM test_cases", "SELECT status, COUNT(*) FROM test_cases GROUP BY status", "SELECT DISTINCT status", "SELECT * ORDER BY status"], 1),
                   mcq("PUT is:", ["Not idempotent", "Idempotent — repeating it has the same effect", "Only for reads", "Always cached"], 1),
                   mcq("'The API response is right but the page is wrong' points to:", [
                       "A database defect", "A front-end defect", "DNS", "A 500 error"], 1),
               ]),

        lesson("career-06", "Behavioural questions with STAR (service-desk gold)", 12,
               "Behavioural interviews are where a career changer wins, because your stories are real. This lesson gives the STAR structure and six fully worked stories drawn from work you've actually done.",
               [
                 ("STAR, done properly", """- **S**ituation (1-2 sentences): context, scale, stakes.
- **T**ask (1 sentence): *your* responsibility — not the team's.
- **A**ction (3-5 sentences, the bulk): what *you* did, step by step, using 'I'.
- **R**esult (1-2 sentences): **quantified** outcome + what you learned.

Keep it to ~2 minutes. Prepare 6-8 stories in advance and write them down. Most people fail because their 'Action' is vague ('I worked with the team') — be concrete about your own decisions."""),
                 ("Six STAR stories you can adapt", """**1. A difficult/escalated problem.**
S: A critical app failed for ~40 users during month-end. T: I owned diagnosis and escalation. A: Reproduced with a clean account, compared logs by request ID, isolated it to a config change in the previous deploy, gathered evidence, briefed L3 with a minimal repro, and gave support a workaround while the fix was built. R: Restored in 90 minutes; wrote a runbook; the same class of issue was caught in pre-release checks afterwards.

**2. A time you found a pattern others missed.**
S: Repeated 'printer' tickets that were actually the same auth failure. T: Reduce the noise. A: Grouped 30 tickets, correlated timestamps with a token-expiry config, proved the common cause with logs, raised one problem record. R: Ticket volume for that issue dropped ~80%; added a KB article.

**3. Conflict / pushback.**
S: A change was due to go live despite an unresolved issue. T: Make the risk visible. A: Documented impact, repro and affected users; proposed three options (delay, feature-flag off, accept risk with rollback); escalated with evidence, not emotion. R: Manager chose the flag-off option; no customer impact; the decision was recorded.

**4. A mistake you made and learned from.**
S: I closed a ticket after a fix appeared to work. T: Own it. A: The issue recurred; I re-opened immediately, told the user and the team, traced my assumption (I'd tested the wrong account role), added a verification step to my checklist. R: No repeat; the checklist became team standard.

**5. Learning something new quickly.**
S: Our team adopted a new ticketing/reporting tool. T: Get productive and help others. A: Built a sandbox, wrote a one-page cheat sheet, ran a 20-minute walkthrough. R: 6 colleagues used it within a week; ramp-up complaints dropped.

**6. Going beyond the ticket (quality mindset).**
S: The same password-reset confusion appeared weekly. T: Stop the repeat. A: Analysed 50 tickets, drafted clearer UI copy and a KB article with the dev team. R: Related contacts fell by ~60%; the change shipped in the next release.

> **Bridge line for every story:** *'That's the same instinct I'd bring to QA — reproduce, isolate with evidence, document so it never costs the team a day again.'*"""),
                 ("Questions to ask THEM (prepare 4)", """- 'What does the current test process look like — is there a regression pack, and how much is automated?'
- 'How does QA get involved in refinement and acceptance criteria?'
- 'What's the biggest quality problem the team is trying to solve right now?'
- 'How do you decide a release is ready, and who signs off?'
- 'What would success look like for me in the first 90 days?'

These are genuinely useful to you *and* signal seniority. Never ask something the job ad answered."""),
               ],
               desk="These stories already happened to you. Anonymise them, quantify the result, and add the bridge line — done. This round should be your strongest.",
               takeaway="STAR with a quantified Result and concrete 'I' actions; prepare 6 stories + 4 questions; end each with the QA bridge line.",
               ex=[
                   mcq("In STAR, which part should be the LONGEST?", [
                       "Situation", "Task", "Action (your own concrete steps)", "Result"], 2),
                   mcq("A strong Result includes:", [
                       "A vague 'it went well'", "A quantified outcome and what you learned", "A list of teammates", "An apology"], 1),
                   mcq("Asking 'how does QA get involved in refinement?' mainly signals:", [
                       "Nothing", "Seniority and genuine interest in process", "That you didn't read the ad", "Impatience"], 1),
               ]),

        lesson("career-07", "Take-homes, first 90 days and growth paths", 12,
               "The last mile: practical exercises, what to do in your first three months, and where this career can go next — so the job is a starting point, not a finish line.",
               [
                 ("Common practical exercises", """| Exercise | What they're grading | How to approach |
|---|---|---|
| 'Write test cases for a login page / a pen / an ATM' | Structure and coverage, not volume | State assumptions, then positive/negative/boundary/state/security/usability/a11y, then prioritise; name the techniques |
| 'Find bugs in this sample app' | Repro + report quality | Talk aloud, use a charter, log 4-6 well-written defects with severity + repro rate; mention what you deliberately didn't log |
| 'Write SQL against this schema' | Core query fluency | SELECT/WHERE/JOIN/GROUP BY/NULL; say your assumptions |
| 'Review this bug report / test case' | Attention to detail | List what's missing (build, steps, expected, evidence) and rewrite a better version |
| 'Automate this flow' (junior) | Locators, waits, assertions | POM, resilient locators, web-first assertions, no sleeps; explain choices |
| 'Is it ready to release?' | Risk judgement | Ask for exit criteria, defect list and coverage; give a conditional recommendation with residual risk |

Always **state assumptions out loud** — that's the test-design mindset. Submit tidy, documented work with a short README even for a take-home."""),
                 ("Your first 90 days", """| Window | Focus | Concrete actions |
|---|---|---|
| **Days 1-30 — Learn** | Product, people, process | Read the test plan/RTM, run the existing suite, shadow triage, map the environments, ask 'what breaks most?', fix one small documentation gap. Don't try to revolutionise anything. |
| **Days 31-60 — Contribute** | Own a feature end to end | Write cases for one story, run the regression pack, log 5 good defects, add one missing test for an escaped bug, pair with a dev on a flaky test. |
| **Days 61-90 — Improve** | One visible, measurable improvement | Automate one high-value smoke flow, add a CI check, reduce suite flakiness, or publish a defect-pattern report. Write down the before/after numbers for your review. |

Habits that get noticed: never silently re-run a flaky test, always record build+environment, keep the decision log, and be the person whose handoffs never bounce back."""),
                 ("Where this career goes", """| Path | What it is | Typical next step |
|---|---|---|
| **Senior QA Analyst / QA Lead** | Deeper test strategy, mentoring, risk ownership, release sign-off | 2-4 years; ISTQB Advanced, coaching |
| **SDET / Test Automation Engineer** | Code-heavy framework and tooling work | Strengthen JS/TS, CI, API automation |
| **Quality Engineer / QE** | Whole-team quality, shift-left, process and tooling | Broader engineering + coaching |
| **Specialist** | Performance, security, accessibility, data/ETL testing, mobile | Deepen one non-functional area |
| **Adjacent** | Product Owner, BA, Release Manager, DevOps, Developer | Transferable emphasises domain + communication |

Your service desk background keeps paying off in **any** of these: you understand how software fails for real people better than most people who started in QA. Keep that perspective — it's a genuine differentiator, not something to leave behind."""),
               ],
               desk="You've onboarded into new environments and been the 'new person' before. The 30/60/90 plan is just a deliberate version of learning the queue, owning a shift, then improving one thing.",
               takeaway="State assumptions in practicals; learn → contribute → one measurable improvement in 90 days; multiple growth paths, all enhanced by your support perspective.",
               ex=[
                   mcq("In a 'write test cases for a login page' exercise, the FIRST thing to do is:", [
                       "Write 50 cases quickly", "State your assumptions and acceptance criteria", "Ask about salary", "Automate it"], 1),
                   mcq("A good first-90-days improvement is:", [
                       "Rewriting the whole framework in week 1", "One visible, measurable change with before/after numbers", "Changing nothing", "Only reading docs"], 1),
                   mcq("Which path is the coding-heavy evolution of a QA Analyst?", [
                       "QA Manager", "SDET / Test Automation Engineer", "Product Owner", "Service Desk"], 1),
               ]),
    ],
    quiz="career-quiz",
)

COURSES_04 = [ISTQB, PORTFOLIO, COMMUNICATION, CAREER]

QUIZZES_04 = [
    quiz("istqb-quiz", "istqb", "ISTQB checkpoint", [
        ("CTFL is typically:", ["An essay exam", "40 multiple-choice questions, ~60 min", "A coding test", "An interview"], 1, ""),
        ("Test ANALYSIS answers:", ["HOW to test", "WHAT to test (test conditions)", "WHEN to stop", "WHO codes"], 1, ""),
        ("ISTQB's term for re-running the failed case:", ["Regression", "Confirmation testing", "Smoke", "Exploratory"], 1, ""),
        ("An 'incident':", ["Is always a defect", "May or may not be a defect — needs investigation", "Is a severity", "Is a test case"], 1, ""),
        ("'Static testing' includes:", ["Running unit tests", "Reviews of documents and code without execution", "Load tests", "Exploratory sessions"], 1, ""),
        ("Which option word is usually a warning sign?", ["usually", "typically", "always", "may"], 2, ""),
    ]),
    quiz("portfolio-quiz", "portfolio", "Portfolio checkpoint", [
        ("A portfolio's main job for a career changer:", ["Decorate a CV", "Supply observable evidence in place of QA experience", "Replace interviews", "Show certificates"], 1, ""),
        ("Use ONE target app across projects because:", ["It's less work", "It tells a coherent end-to-end story", "CI requires it", "Free apps are rare"], 1, ""),
        ("A public repo must never contain:", ["A README", "Real credentials/PII", "Test cases", "A licence"], 1, ""),
        ("Lead a project walkthrough with:", ["Tool versions", "The problem, test decisions and what you found", "Commit count", "The framework name"], 1, ""),
        ("A CI badge should:", ["Be a static green image", "Reflect the real workflow status", "Show test count", "Be hidden"], 1, ""),
    ]),
    quiz("communication-quiz", "communication", "Communication checkpoint", [
        ("Best opening for a test summary:", ["'Testing went well'", "'Recommend no-go: DEF-1042 (Critical) remains open'", "'See below'", "'Lots of tests run'"], 1, ""),
        ("A hypothesis in a bug report should be:", ["Mixed with facts", "Clearly labelled and separate from observed values", "Omitted always", "Called a defect"], 1, ""),
        ("Most reduces conflict over a no-go decision:", ["A louder email", "Exit criteria agreed in advance", "Escalating immediately", "Silence"], 1, ""),
        ("If the PO ships over your objection:", ["Argue", "Record accepted residual risk with sign-off and move on", "Delete your report", "Say nothing"], 1, ""),
        ("A decision log prevents:", ["CI failures", "Re-litigating the same ambiguity later", "Browser bugs", "Slow tests"], 1, ""),
    ]),
    quiz("career-quiz", "career", "Career checkpoint", [
        ("For a career changer, resume order puts:", ["Education first", "Projects/portfolio above work experience", "References first", "Hobbies first"], 1, ""),
        ("Best framing of the switch:", ["'No experience but willing'", "'Move upstream and prevent defects before release'", "'Escaping the desk'", "'QA is easier'"], 1, ""),
        ("'Tested fixes before closing tickets' maps to:", ["Unit testing", "Confirmation/retest and regression", "Load testing", "Static analysis"], 1, ""),
        ("A sensible FIRST target role:", ["Senior SDET", "QA Lead", "Junior/Manual QA Analyst or UAT Analyst", "QA Manager"], 2, ""),
        ("In STAR, the longest part should be:", ["Situation", "Action — your own concrete steps", "Task", "Result"], 1, ""),
        ("In a 'test a login page' exercise, first:", ["Write 50 cases", "State assumptions and acceptance criteria", "Automate", "Ask about salary"], 1, ""),
        ("A good first-90-days improvement:", ["Rewrite everything in week 1", "One measurable change with before/after numbers", "Change nothing", "Only read"], 1, ""),
    ]),
]
