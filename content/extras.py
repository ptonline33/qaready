"""Everything that isn't a lesson: roadmap, glossary, toolkit, projects, career kit, plans."""

# ---------------------------------------------------------------------------
# Phases (7) and the 24-week roadmap
# ---------------------------------------------------------------------------
PHASES = [
    {"id": "p0", "num": 0, "title": "Start here", "weeks": "Week 1", "color": "#7b5cff",
     "icon": "compass",
     "goal": "Understand the QA role, map your service desk experience onto it, and set up a study routine that survives shift work.",
     "deliverable": "A study journal, a GitHub account, and a written 'why I'm moving into QA' paragraph.",
     "checkpoint": "Explain what a QA Analyst does and name 5 transferable skills without notes.",
     "courses": ["orientation", "foundations"]},
    {"id": "p1", "num": 1, "title": "Manual QA craft", "weeks": "Weeks 2-6", "color": "#3ddc84",
     "icon": "clipboard",
     "goal": "Master the core job: test design techniques, test cases/plans/RTM, professional defect reports, tools and workflows, and QA communication.",
     "deliverable": "Portfolio Project 1 — a full manual test suite (plan + 25 cases + RTM + 5 defect reports + summary).",
     "checkpoint": "Design boundary + decision-table cases for an unseen feature, and write a defect report a developer can act on.",
     "courses": ["test-design", "test-docs", "defects", "tools", "communication"]},
    {"id": "p2", "num": 2, "title": "Technical foundations", "weeks": "Weeks 7-11", "color": "#4f8cff",
     "icon": "terminal",
     "goal": "Test below the UI: how the web works, SQL for verification, command line and Git, and JavaScript from zero.",
     "deliverable": "A SQL verification-queries file, a CLI cheat sheet, and your first GitHub repo with a real README.",
     "checkpoint": "Explain a 401 vs 403, write a JOIN + GROUP BY query, and read a short JS test script.",
     "courses": ["web", "sql", "cli-git", "javascript"]},
    {"id": "p3", "num": 3, "title": "API testing", "weeks": "Weeks 12-14", "color": "#3df2c0",
     "icon": "plug",
     "goal": "Understand REST, JSON, auth and status codes; build an asserted Postman collection and run it in CI with Newman.",
     "deliverable": "Portfolio Project 3 — a public API collection, 20-case test matrix, and a green Newman CI run.",
     "checkpoint": "Build an 8-row auth negative matrix and explain UI-vs-API defect triage.",
     "courses": ["api", "postman"]},
    {"id": "p4", "num": 4, "title": "Automation & CI/CD", "weeks": "Weeks 15-20", "color": "#a78bfa",
     "icon": "robot",
     "goal": "Learn automation strategy, build a maintainable Playwright framework with Page Objects and fixtures, and gate it in GitHub Actions.",
     "deliverable": "Portfolio Project 4 — Playwright framework (3 browsers, POM, data-driven tests, CI report badge).",
     "checkpoint": "Diagnose a flaky test, explain the pyramid, and describe a quality gate.",
     "courses": ["automation", "playwright", "cicd"]},
    {"id": "p5", "num": 5, "title": "Beyond functional", "weeks": "Weeks 21-22", "color": "#ff3d81",
     "icon": "shield",
     "goal": "Cover performance, accessibility, security awareness, usability, compatibility/mobile, localisation and privacy at a first-role depth.",
     "deliverable": "A non-functional test appendix added to your Project 1 test plan, with measurable acceptance criteria.",
     "checkpoint": "Run a keyboard/axe accessibility pass and write a WCAG-referenced finding.",
     "courses": ["nonfunctional"]},
    {"id": "p6", "num": 6, "title": "Get hired", "weeks": "Weeks 23-24", "color": "#ff5470",
     "icon": "briefcase",
     "goal": "ISTQB CTFL prep, finish and publish the portfolio, rewrite your resume/LinkedIn, drill interviews, and run a targeted job search.",
     "deliverable": "A tailored one-page resume, polished LinkedIn/GitHub, 4 pinned repos, and 20+ targeted applications.",
     "checkpoint": "Answer 15 core QA questions aloud and deliver a 90-second walkthrough of each portfolio repo.",
     "courses": ["istqb", "portfolio", "career"]},
]

WEEKS = [
    {"w": 1, "phase": "p0", "focus": "Orientation, the QA role, your transferable skills, study setup",
     "hours": 6, "deliverable": "Study journal + GitHub account + 'why QA' paragraph", "checkpoint": "Explain the role & 5 transferable skills", "courses": ["orientation", "foundations"]},
    {"w": 2, "phase": "p0", "focus": "SDLC/STLC, Agile & Scrum, 7 principles, levels & types, vocabulary",
     "hours": 9, "deliverable": "A one-page STLC/principles cheat sheet in your own words", "checkpoint": "Foundations quiz ≥ 80%", "courses": ["foundations"]},
    {"w": 3, "phase": "p1", "focus": "Test design: black/white box, EP, BVA, decision tables",
     "hours": 9, "deliverable": "Worked BVA + decision-table examples for your target app's checkout", "checkpoint": "Design cases for an unseen field unaided", "courses": ["test-design"]},
    {"w": 4, "phase": "p1", "focus": "State transitions, use cases, exploratory/SBTM, pairwise; start test docs",
     "hours": 9, "deliverable": "45-min chartered exploratory session notes on your target app", "checkpoint": "Test-design quiz ≥ 80%", "courses": ["test-design", "test-docs"]},
    {"w": 5, "phase": "p1", "focus": "Test cases, test data, RTM, test plans, risk-based testing, estimation",
     "hours": 10, "deliverable": "Draft test plan + RTM + first 15 test cases", "checkpoint": "Test-docs quiz ≥ 80%", "courses": ["test-docs"]},
    {"w": 6, "phase": "p1", "focus": "Defect reports, severity/priority, lifecycle, retest/regression, tools, communication",
     "hours": 10, "deliverable": "PROJECT 1 SHIPPED: plan + 25 cases + RTM + 5 defect reports + summary", "checkpoint": "Defects quiz ≥ 80%; repo README complete", "courses": ["defects", "tools", "communication"]},
    {"w": 7, "phase": "p2", "focus": "Client-server, DNS, HTTP methods/status/headers, HTML/CSS/JS basics",
     "hours": 8, "deliverable": "A labelled HTTP request/response diagram + status-code cheat sheet", "checkpoint": "Web quiz ≥ 80%", "courses": ["web"]},
    {"w": 8, "phase": "p2", "focus": "DevTools, Network panel, sessions/cookies/cache; SQL tables & SELECT/WHERE",
     "hours": 9, "deliverable": "One HAR file with a written UI-vs-API triage note", "checkpoint": "10 basic SQL queries unaided", "courses": ["web", "sql"]},
    {"w": 9, "phase": "p2", "focus": "SQL filtering (NULL/IN/LIKE/BETWEEN), aggregates, GROUP BY, HAVING, JOINs",
     "hours": 10, "deliverable": "`verification-queries.sql` — 15 commented queries against the practice DB", "checkpoint": "SQL quiz ≥ 80%", "courses": ["sql"]},
    {"w": 10, "phase": "p2", "focus": "Safe writes/transactions, CLI, files/permissions/processes/logs, Git basics",
     "hours": 9, "deliverable": "CLI cheat sheet + first GitHub repo with a real README", "checkpoint": "CLI/Git quiz ≥ 80%", "courses": ["sql", "cli-git"]},
    {"w": 11, "phase": "p2", "focus": "Branches/PRs, Markdown, JavaScript: variables, conditions, loops, functions",
     "hours": 10, "deliverable": "A small JS script that classifies test results + a PR to your own repo", "checkpoint": "JavaScript quiz ≥ 80%", "courses": ["cli-git", "javascript"]},
    {"w": 12, "phase": "p2", "focus": "JS arrays/objects, JSON, async/await, debugging; intro to API concepts",
     "hours": 9, "deliverable": "A script that fetches and validates a JSON response", "checkpoint": "Explain a Promise and an off-by-one", "courses": ["javascript", "api"]},
    {"w": 13, "phase": "p3", "focus": "REST, JSON schemas, auth (keys/JWT/OAuth), status/error matrix, idempotency",
     "hours": 9, "deliverable": "A 20-case API test matrix for POST /orders", "checkpoint": "API quiz ≥ 80%", "courses": ["api"]},
    {"w": 14, "phase": "p3", "focus": "Postman collections, environments, pm.test assertions, Runner, Newman CI",
     "hours": 10, "deliverable": "PROJECT 3 SHIPPED: public collection + Newman workflow + HTML report", "checkpoint": "Postman quiz ≥ 80%; CI badge green", "courses": ["postman"]},
    {"w": 15, "phase": "p4", "focus": "Automation strategy: pyramid, what to automate, ROI, tool choice, test anatomy",
     "hours": 8, "deliverable": "A written automation strategy for your target app (what/why/not)", "checkpoint": "Automation quiz ≥ 80%", "courses": ["automation"]},
    {"w": 16, "phase": "p4", "focus": "Playwright setup, first tests, locators, actions, web-first assertions",
     "hours": 10, "deliverable": "10 specs for your target app using getByRole/getByLabel only", "checkpoint": "All 10 pass in --ui mode", "courses": ["playwright"]},
    {"w": 17, "phase": "p4", "focus": "Waits, fixtures, hooks, config, storageState, environments, parallelism",
     "hours": 10, "deliverable": "A logged-in fixture + 3-browser config + a flake you diagnosed", "checkpoint": "Playwright quiz ≥ 80%", "courses": ["playwright"]},
    {"w": 18, "phase": "p4", "focus": "Page Object Model, data-driven boundary loops, traces, reports, flakiness",
     "hours": 10, "deliverable": "PROJECT 4 (part 1): POM framework + data-driven BVA loop + flaky-test journal", "checkpoint": "Suite green on Chromium + WebKit", "courses": ["playwright"]},
    {"w": 19, "phase": "p4", "focus": "CI/CD concepts, GitHub Actions pipeline, reports/artefacts, failure triage",
     "hours": 9, "deliverable": "PROJECT 4 (part 2): workflow with npm ci, secrets, uploaded report", "checkpoint": "CI/CD quiz ≥ 80%; badge live", "courses": ["cicd"]},
    {"w": 20, "phase": "p4", "focus": "Quality gates, Definition of Done, metrics, shift-left; polish all repos",
     "hours": 9, "deliverable": "A one-paragraph quality report for your portfolio app", "checkpoint": "4 repos with strong READMEs, no secrets", "courses": ["cicd"]},
    {"w": 21, "phase": "p5", "focus": "Performance (k6/JMeter), accessibility (WCAG/axe/keyboard), security (OWASP)",
     "hours": 9, "deliverable": "Non-functional appendix to the Project 1 test plan", "checkpoint": "Non-functional quiz ≥ 80%", "courses": ["nonfunctional"]},
    {"w": 22, "phase": "p5", "focus": "Usability, compatibility/mobile, localisation, privacy, gating NFRs",
     "hours": 8, "deliverable": "A keyboard/axe finding + a pairwise compatibility matrix", "checkpoint": "Write 3 measurable non-functional AC", "courses": ["nonfunctional"]},
    {"w": 23, "phase": "p6", "focus": "ISTQB CTFL syllabus map & mock exams; finish/publish portfolio; PhD of the README",
     "hours": 10, "deliverable": "4 pinned repos + optional one-page portfolio site + 2 timed mocks", "checkpoint": "ISTQB quiz ≥ 80%; 60-second skim works", "courses": ["istqb", "portfolio"]},
    {"w": 24, "phase": "p6", "focus": "Resume/LinkedIn rewrite, 40 Q&As, STAR stories, take-homes, job-search sprint",
     "hours": 10, "deliverable": "One-page QA resume + 20 tailored applications + 6 STAR stories", "checkpoint": "Career quiz ≥ 80%; 90-second walkthrough per repo", "courses": ["career"]},
]

# ---------------------------------------------------------------------------
# Glossary (~95 terms)
# ---------------------------------------------------------------------------
def G(term, definition, cat, aka=""):
    d = {"term": term, "def": definition, "cat": cat}
    if aka:
        d["aka"] = aka
    return d

GLOSSARY = [
    G("Acceptance criteria (AC)", "Concrete conditions a user story must satisfy to be accepted; effectively testable requirements.", "Fundamentals"),
    G("Acceptance testing", "Formal testing against business needs, usually by the customer/PO, to decide whether to accept the system.", "Fundamentals"),
    G("Accessibility testing", "Checking the product works for people with disabilities (WCAG POUR, keyboard, screen readers, contrast).", "Non-functional", "a11y"),
    G("Actual result", "What the system actually did when a test was executed; recorded against the expected result.", "Documentation"),
    G("Agile", "Iterative, incremental development with frequent delivery and inspection; Scrum is the common framework.", "Process"),
    G("Alpha testing", "Internal testing by the organisation before releasing to external users.", "Fundamentals"),
    G("API", "Application Programming Interface: a documented contract letting one program talk to another.", "API"),
    G("API key", "A secret token sent with requests to identify/authenticate a client.", "API"),
    G("Assertion", "A check in test code that fails when the actual result differs from the expected result.", "Automation"),
    G("Audit trail", "A chronological, tamper-evident record of actions; vital for regulated testing evidence.", "Process"),
    G("Automated test", "A test executed by tooling rather than a human, with an explicit assertion.", "Automation"),
    G("Backlog refinement", "Ceremony where the team clarifies stories and acceptance criteria before development; a key QA shift-left opportunity.", "Process", "grooming"),
    G("Beta testing", "Testing by a limited group of real external users before general release.", "Fundamentals"),
    G("Black-box testing", "Testing based on specifications with no knowledge of internal code structure.", "Design"),
    G("Blocked", "Test status: cannot be executed because of an environment/build/data issue — neither a pass nor a fail.", "Documentation"),
    G("Boundary value analysis (BVA)", "Black-box technique testing values at and just around the edges of an input range.", "Design", "BVA"),
    G("Branch", "A movable pointer to a line of Git commits, used to isolate work.", "Technical"),
    G("Bug / Defect / Fault", "A flaw in the software causing (or capable of causing) incorrect behaviour.", "Defects", "bug"),
    G("Build", "A numbered, deployable version of the software; must be recorded with every test result.", "Technical"),
    G("Build verification test (BVT)", "A short smoke suite run on a new build to decide whether it is worth testing.", "Technical", "BVT"),
    G("Capability Maturity Model (CMM)", "A process-improvement model (test process improvement: TMMi, TPI).", "Process"),
    G("Cause-effect graphing", "A black-box technique turning combinations of causes into a decision table.", "Design"),
    G("Checklist-based testing", "Experience-based testing driven by a checklist of items to verify or attack patterns.", "Design"),
    G("Code coverage", "The proportion of code (statements/branches/paths) exercised by tests; a white-box measure.", "Automation"),
    G("Compatibility testing", "Checking the product across browsers, OS, devices and versions.", "Non-functional"),
    G("Component / Unit testing", "Testing a single function/class/module in isolation, usually by developers.", "Fundamentals"),
    G("Confirmation testing", "ISTQB term for re-running a previously failed test after a fix.", "Defects", "retesting"),
    G("Contract testing", "Verifying an agreed request/response shape between an API consumer and provider.", "API"),
    G("Correlation / request ID", "An identifier attached to a request that lets you trace one transaction across many logs/services.", "Technical"),
    G("Coverage", "The degree to which a test basis has been exercised, expressed as a percentage — always state 'of what'.", "Fundamentals"),
    G("Cross-browser testing", "Running the same checks in multiple browser engines.", "Non-functional"),
    G("Data-driven testing", "Running one test definition against many rows of input/expected data.", "Automation"),
    G("Decision table", "A table enumerating combinations of conditions and their resulting actions; one column = one test case.", "Design"),
    G("Defect clustering", "The principle that a small number of modules contain most defects (Pareto 80/20).", "Fundamentals"),
    G("Defect density", "Defects per module or per thousand lines of code; helps focus risk-based testing.", "Defects"),
    G("Defect lifecycle", "The states a defect moves through (New → Assigned → Fixed → Retest → Closed/Reopened).", "Defects"),
    G("Defect triage", "A regular meeting to validate, prioritise, assign and disposition new defects.", "Defects"),
    G("Definition of Done (DoD)", "The team-wide checklist that must be satisfied before a story is considered complete.", "Process", "DoD"),
    G("Deliverable", "A tangible artefact produced by a phase (test plan, cases, report).", "Process"),
    G("Dynamic testing", "Testing that executes the software.", "Fundamentals"),
    G("Entry criteria", "Conditions that must be met before a test phase may begin.", "Process"),
    G("Equivalence partitioning (EP)", "Dividing inputs into classes expected to be treated identically and testing one representative per class.", "Design", "EP"),
    G("Error", "A human mistake that introduces a fault.", "Fundamentals"),
    G("Error guessing", "Experience-based technique aimed at known weak spots (nulls, long strings, double submits).", "Design"),
    G("Escaped defect", "A defect found after release — the most honest measure of test-design effectiveness.", "Defects"),
    G("Exit criteria", "Measurable conditions that must be met before a test cycle/release can close.", "Process"),
    G("Expected result", "The specific, observable outcome predicted by the test basis; the oracle for a test case.", "Documentation"),
    G("Exploratory testing", "Simultaneous learning, test design and execution; made rigorous with charters, time boxes and notes.", "Design"),
    G("Failure", "The observable deviation from expected behaviour when a fault executes.", "Fundamentals"),
    G("False negative", "A test that passes when a defect is actually present.", "Automation"),
    G("False positive", "A test that fails when there is no defect (often a flaky test).", "Automation"),
    G("Fixture", "A prepared resource (page, user, DB state) supplied to a test and cleaned up automatically.", "Automation"),
    G("Flaky test", "A test that sometimes passes and sometimes fails with no code change.", "Automation"),
    G("Functional testing", "Checking that the software does what the requirements say it should do.", "Fundamentals"),
    G("Given/When/Then", "Gherkin syntax for acceptance criteria / BDD scenarios: context, action, outcome.", "Process", "Gherkin"),
    G("HAR file", "HTTP Archive: a captured record of all network requests/responses, used as defect evidence.", "Technical"),
    G("HAVING", "SQL clause filtering groups after aggregation (unlike WHERE, which filters rows).", "Technical"),
    G("Heuristic", "A fallible but useful rule of thumb for test design or exploration.", "Design"),
    G("Idempotency", "Repeating an operation has the same effect as doing it once (PUT/DELETE yes, POST no).", "API"),
    G("Impact analysis", "Assessing what a change affects — used to select regression tests.", "Process"),
    G("Incident", "An event requiring investigation that may or may not turn out to be a defect.", "Defects"),
    G("Integration testing", "Testing that two or more components work together.", "Fundamentals"),
    G("ISTQB CTFL", "Certified Tester Foundation Level — the widely recognised entry-level testing certification.", "Career"),
    G("JIRA / JQL", "Issue tracker and its query language for finding and reporting work and defects.", "Technical"),
    G("JOIN", "SQL operation combining rows from two tables on a related column.", "Technical"),
    G("JSON", "JavaScript Object Notation: the standard text format for API payloads.", "API"),
    G("JWT", "JSON Web Token: a signed, self-contained bearer token (header.payload.signature).", "API"),
    G("Left join / anti-join", "LEFT JOIN keeps all left rows; adding WHERE right.id IS NULL finds missing relationships.", "Technical"),
    G("Load testing", "Non-functional testing under expected peak concurrent load.", "Non-functional"),
    G("Locator", "An expression identifying an element to interact with; prefer role/label/testid over XPath.", "Automation"),
    G("Maintenance testing", "Testing after a change, migration or fix — mainly confirmation + regression.", "Fundamentals"),
    G("Mock / Stub", "A test double returning controlled responses when a real dependency is unavailable.", "API"),
    G("Negative testing", "Verifying graceful handling of invalid input and failure conditions.", "Fundamentals"),
    G("Non-functional testing", "Testing how well the system behaves: performance, security, accessibility, usability, compatibility.", "Non-functional"),
    G("NULL", "SQL marker for an unknown/absent value; use IS NULL, never = NULL.", "Technical"),
    G("Oracle", "The source or mechanism used to decide whether an actual result is correct.", "Fundamentals", "test oracle"),
    G("Page Object Model (POM)", "Design pattern putting page selectors/actions in one class so tests stay readable and maintainable.", "Automation", "POM"),
    G("Pairwise testing", "Combinatorial technique covering every pair of parameter values in a small number of tests.", "Design", "all-pairs"),
    G("Pareto principle", "Roughly 80% of effects come from 20% of causes — the basis of defect clustering.", "Fundamentals"),
    G("Pesticide paradox", "Repeated identical tests stop finding new defects; suites must be reviewed and refreshed.", "Fundamentals"),
    G("Performance testing", "Measuring responsiveness/throughput/stability under load (load, stress, soak, spike).", "Non-functional"),
    G("Postcondition", "The required system state after a test, including cleanup.", "Documentation"),
    G("Precondition", "The system/data state that must exist before a test's first step.", "Documentation"),
    G("Priority", "The business order in which a defect should be fixed; owned by the Product Owner.", "Defects"),
    G("Regression testing", "Re-running previously passing tests after a change to detect side effects.", "Defects"),
    G("Regression pack", "A stable, risk-selected subset of the suite run after every change.", "Defects"),
    G("Requirements Traceability Matrix (RTM)", "A table linking requirements → test cases → defects to prove coverage and support impact analysis.", "Documentation", "RTM"),
    G("Residual risk", "Risk knowingly accepted at release; documented with PO sign-off.", "Process"),
    G("Retest / Retesting", "Re-running the failed test case after a fix (ISTQB: confirmation testing).", "Defects"),
    G("Review / Static testing", "Evaluating documents or code without executing them (walkthroughs, inspections, linting).", "Fundamentals"),
    G("Risk-based testing", "Prioritising depth and technique by likelihood × impact.", "Process"),
    G("Root cause analysis", "Finding the underlying reason a defect occurred (e.g. 5 Whys) to prevent recurrence.", "Defects", "RCA"),
    G("Sanity testing", "A narrow, quick check of a specific change after a build.", "Fundamentals"),
    G("SDET", "Software Development Engineer in Test: the coding-heavy automation role.", "Career"),
    G("SDLC", "Software Development Life Cycle: requirements → design → build → test → deploy → maintain.", "Process"),
    G("Severity", "The technical impact of a defect, set by QA (Critical/Major/Minor/Trivial).", "Defects"),
    G("Shift-left", "Moving testing activities earlier in the lifecycle to find defects sooner and cheaper.", "Process"),
    G("Smoke test", "A small, broad suite answering 'is this build testable at all?'.", "Fundamentals"),
    G("Soak / endurance test", "Moderate load sustained for hours to find leaks and degradation.", "Non-functional"),
    G("State transition testing", "Testing valid/invalid moves between states (e.g. order lifecycle).", "Design"),
    G("Static analysis", "Tool-based examination of code/artefacts without execution.", "Fundamentals"),
    G("Status code", "HTTP response number: 2xx success, 3xx redirect, 4xx client error, 5xx server error.", "API"),
    G("STLC", "Software Test Life Cycle: analyse → plan → design → setup → execute → close.", "Process"),
    G("Stress testing", "Increasing load beyond expected limits to find the breaking point.", "Non-functional"),
    G("System testing", "End-to-end testing of the whole integrated application — the QA Analyst's main level.", "Fundamentals"),
    G("Test automation pyramid", "Many unit, some API, few E2E UI tests; cheap checks early, expensive checks later.", "Automation"),
    G("Test basis", "All sources from which tests are derived: requirements, stories, designs, specs, regulations.", "Fundamentals"),
    G("Test case", "Preconditions + inputs/steps + expected result for one test condition.", "Documentation"),
    G("Test charter", "A short mission scoping an exploratory testing session.", "Design"),
    G("Test condition", "A single item or event of the test basis that could be verified.", "Documentation"),
    G("Test data", "Concrete values and records used during test execution.", "Documentation"),
    G("Test environment", "Configured hardware, software, data, network and accounts on which tests run.", "Technical"),
    G("Test level", "A scope/timing of testing: unit, integration, system, acceptance.", "Fundamentals"),
    G("Test oracle", "How you decide whether a result is correct (spec, reference system, calculation, expert).", "Fundamentals"),
    G("Test plan", "Release-specific document: scope, approach, resources, schedule, risks, entry/exit criteria.", "Documentation"),
    G("Test procedure / script", "The ordered sequence of steps for executing one or more test cases.", "Documentation"),
    G("Test run / execution", "One instance of running a test case against one build, with a recorded result.", "Documentation"),
    G("Test strategy", "High-level, often organisation-wide testing approach and standards.", "Documentation"),
    G("Test suite", "A collection of test cases grouped for one execution run.", "Documentation"),
    G("Test summary report", "Closure document: scope, results, coverage, defects, exit criteria, residual risk, recommendation.", "Documentation"),
    G("Test type", "A category of testing by attribute: functional, non-functional, static, dynamic, etc.", "Fundamentals"),
    G("Testware", "All artefacts produced during testing (cases, scripts, data, reports).", "Documentation"),
    G("Three Amigos", "BA + Developer + QA aligning on examples and expected behaviour before coding.", "Process"),
    G("Traceability", "The ability to link a requirement to its tests and defects (and vice versa).", "Documentation"),
    G("UAT", "User Acceptance Testing — business users validate the system against real needs.", "Fundamentals"),
    G("Usability testing", "Evaluating clarity, learnability, feedback and error recovery for real users.", "Non-functional"),
    G("Validation", "'Are we building the right product?' — evaluation against real user needs (dynamic).", "Fundamentals"),
    G("Verification", "'Are we building the product right?' — checks against specs, often static (reviews).", "Fundamentals"),
    G("V-Model", "SDLC model pairing each development stage with a corresponding test stage.", "Process"),
    G("WCAG", "Web Content Accessibility Guidelines; POUR principles, levels A/AA/AAA.", "Non-functional"),
    G("White-box testing", "Testing based on internal code structure, branches and paths.", "Design"),
    G("Workaround", "A temporary way to achieve the goal despite a defect; affects effective priority.", "Defects"),
]

# ---------------------------------------------------------------------------
# Toolkit / resources
# ---------------------------------------------------------------------------
def R(name, url, type_, desc, tag, free=True, note=""):
    d = {"name": name, "url": url, "type": type_, "desc": desc, "tag": tag, "free": free}
    if note:
        d["note"] = note
    return d

RESOURCES = [
    # Free courses
    R("Test Automation University", "https://testautomationu.applitools.com/", "free", "Free, high-quality video courses on testing, Postman, Playwright, Cypress, SQL and more. Start with 'Introduction to Testing'.", "Courses", True),
    R("Guru99 Software Testing Tutorial", "https://www.guru99.com/software-testing.html", "free", "A thorough free text tutorial covering manual testing concepts, SDLC/STLC and test design. Old-fashioned layout, solid content.", "Manual QA", True),
    R("freeCodeCamp", "https://www.freecodecamp.org/", "free", "Free full courses on JavaScript, APIs, SQL and web fundamentals — exactly the Phase 2 prerequisites.", "Programming", True),
    R("MDN Web Docs — HTTP", "https://developer.mozilla.org/en-US/docs/Web/HTTP", "free", "The authoritative reference for HTTP methods, status codes, headers and cookies.", "Web", True),
    R("Postman Academy / Learning Center", "https://learning.postman.com/", "free", "Official guided courses on requests, variables, tests, collections, Newman and API fundamentals.", "API", True),
    R("Playwright Docs & Tutorial", "https://playwright.dev/docs/intro", "free", "Official getting-started, locators, assertions, fixtures and CI guides. Best single source for Phase 4.", "Automation", True),
    R("SQLZoo", "https://sqlzoo.net/", "free", "Interactive SQL tutorials and exercises right in the browser.", "SQL", True),
    R("W3Schools SQL Tutorial", "https://www.w3schools.com/sql/", "free", "Simple, clickable SQL reference with 'try it yourself' examples.", "SQL", True),
    R("DataLemur SQL Interview Questions", "https://datalemur.com/questions", "free", "Real SQL interview questions with an in-browser editor — great for the technical round.", "SQL / Interviews", True),
    R("Learn Git Branching", "https://learngitbranching.js.org/", "free", "Interactive visual sandbox that teaches branching, merging, rebasing and remotes.", "Git", True),
    R("Pro Git (free book)", "https://git-scm.com/book/en/v2", "free", "The complete official Git book, free online.", "Git", True),
    R("The Linux Command Line (free book)", "http://linuxcommand.org/", "free", "A gentle, free book covering the shell from scratch.", "CLI", True),
    R("OverTheWire: Bandit", "https://overthewire.org/wargames/bandit/", "free", "A game that teaches the command line by solving progressively harder puzzles over SSH.", "CLI", True),
    R("PortSwigger Web Security Academy", "https://portswigger.net/web-security", "free", "Free, hands-on security labs with a deliberately vulnerable app — for OWASP awareness.", "Security", True),
    R("OWASP Juice Shop", "https://owasp.org/www-project-juice-shop/", "free", "An intentionally insecure app to practise finding security defects safely and locally.", "Security", True),
    R("Axe / Deque University", "https://www.deque.com/axe/devtools/", "free", "Free browser extension for automated accessibility scans plus learning resources.", "Accessibility", True),
    R("WebAIM Contrast Checker", "https://webaim.org/resources/contrastchecker/", "free", "Check colour contrast against WCAG AA/AAA thresholds.", "Accessibility", True),
    R("Lighthouse (Chrome DevTools)", "https://developer.chrome.com/docs/lighthouse/overview/", "free", "Built-in audits for performance, accessibility, SEO and best practices.", "Non-functional", True),
    # Paid / certifications
    R("ISTQB Official Site & Syllabus", "https://www.istqb.org/", "cert", "Free syllabus PDFs, glossary and exam-board links for the CTFL certification.", "Certification", True),
    R("ASTQB / ISTQB Exam Info", "https://www.astqb.org/", "cert", "Exam registration and free sample exams for ISTQB certifications.", "Certification", False),
    R("Coursera — Software Testing courses", "https://www.coursera.org/courses?query=software%20testing", "paid", "University- and vendor-led testing courses and specialisations; many are free to audit.", "Courses", False),
    R("Udemy — Software Testing", "https://www.udemy.com/courses/search/?q=software%20testing", "paid", "Low-cost, frequently discounted ISTQB/manual/Postman/Selenium courses. Check recent reviews before buying.", "Courses", False),
    R("Scrum.org — PSM I", "https://www.scrum.org/", "cert", "Free Scrum guide and optional Professional Scrum Master assessment; useful Agile vocabulary.", "Agile", False),
    R("edX — Software Testing", "https://www.edx.org/learn/software-testing", "paid", "University-style testing and quality courses, often free to audit.", "Courses", False),
    # Tools
    R("Postman", "https://www.postman.com/", "tool", "API client for building collections, environments, pm.test assertions and mock servers.", "API", True),
    R("Playwright", "https://playwright.dev/", "tool", "Modern cross-browser E2E framework with auto-waits, traces and an HTML reporter.", "Automation", True),
    R("Cypress", "https://docs.cypress.io/", "tool", "Developer-friendly JS E2E framework with time-travel debugging.", "Automation", True),
    R("Selenium WebDriver", "https://www.selenium.dev/documentation/", "tool", "The long-standing W3C-standard browser automation framework; common in enterprise.", "Automation", True),
    R("Newman", "https://learning.postman.com/docs/collections/using-newman-cli/command-line-integration-with-newman/", "tool", "Postman's CLI collection runner for CI pipelines.", "API / CI", True),
    R("Jira", "https://www.atlassian.com/software/jira", "tool", "The most common issue/defect tracker; learn JQL and workflow.", "Tools", False),
    R("TestRail", "https://www.gurock.com/testrail/", "tool", "Dedicated test-case management with runs, milestones and reports. Free trial.", "Tools", False),
    R("GitHub Actions", "https://docs.github.com/en/actions", "tool", "CI/CD built into GitHub — free for public repos. Runs your Newman and Playwright suites.", "CI/CD", True),
    R("VS Code", "https://code.visualstudio.com/", "tool", "Free editor with excellent JS, Markdown, Git and Playwright extensions.", "Tools", True),
    R("k6", "https://k6.io/docs/", "tool", "Open-source JS-based load-testing tool with pass/fail thresholds.", "Performance", True),
    R("Apache JMeter", "https://jmeter.apache.org/", "tool", "Classic open-source load and performance testing tool.", "Performance", True),
    R("httpbin", "https://httpbin.org/", "practice", "Echoes back your request — perfect for learning methods, headers and status codes.", "Practice API", True),
    R("JSONPlaceholder", "https://jsonplaceholder.typicode.com/", "practice", "Free fake REST API with users, posts and comments for safe practice.", "Practice API", True),
    R("ReqRes", "https://reqres.in/", "practice", "A simple hosted REST API with auth and error scenarios.", "Practice API", True),
    R("Swagger Petstore", "https://petstore.swagger.io/", "practice", "A documented sample API with an OpenAPI spec — good for contract-based practice.", "Practice API", True),
    R("SauceDemo", "https://www.saucedemo.com/", "practice", "A deliberately testable demo e-commerce site, ideal for portfolio projects.", "Practice app", True),
    R("Automation Exercise", "https://automationexercise.com/", "practice", "A full practice e-commerce site with many flows to test.", "Practice app", True),
    R("The Internet (Herokuapp)", "https://the-internet.herokuapp.com/", "practice", "A collection of tricky UI scenarios (dynamic loading, hovers, frames, file uploads).", "Practice app", True),
    # Books
    R("Lessons Learned in Software Testing", "", "book", "Kaner/Bach/Pettichord — 300+ short, wise essays about the craft and mindset of testing.", "Book", False, "Borrow or buy; no official free link."),
    R("Explore It!", "", "book", "Elisabeth Hendrickson — the best practical book on structured exploratory testing.", "Book", False, "Borrow or buy; no official free link."),
    R("Agile Testing", "", "book", "Lisa Crispin & Janet Gregory — how QA fits into Agile teams.", "Book", False, "Borrow or buy; no official free link."),
    R("The Art of Software Testing (3rd ed.)", "", "book", "Glenford Myers et al. — a classic on test design and psychology.", "Book", False, "Borrow or buy; no official free link."),
    R("A Practitioner's Guide to Software Test Design", "", "book", "Lee Copeland — deep, worked examples of every black-box technique.", "Book", False, "Borrow or buy; no official free link."),
    # Communities
    R("Ministry of Testing", "https://www.ministryoftesting.com/", "community", "The friendliest global QA community: articles, 30-day testing challenges, forums and events.", "Community", True),
    R("Software Testing Stack Exchange", "https://sqa.stackexchange.com/", "community", "Focused Q&A for testing questions; great for precise terminology debates.", "Community", True),
    R("r/softwaretesting", "https://www.reddit.com/r/softwaretesting/", "community", "Active community for career questions, tools and interview experiences.", "Community", True),
    R("TestGuild", "https://testguild.com/", "community", "Podcasts, articles and conferences on test automation and QA careers.", "Community", True),
    R("OWASP Top 10", "https://owasp.org/www-project-top-ten/", "community", "The standard, free list of the most critical web security risks.", "Security", True),
    R("W3C WCAG", "https://www.w3.org/WAI/standards-guidelines/wcag/", "community", "The official accessibility guidelines and quick-reference 'How to Meet WCAG'.", "Accessibility", True),
]

# ---------------------------------------------------------------------------
# Portfolio projects (with checkable checklists + sample artefacts)
# ---------------------------------------------------------------------------
PROJECTS = [
    {
        "id": "proj-manual", "title": "Project 1 — Full manual test suite", "color": "#3ddc84",
        "subtitle": "Plan + 25 cases + RTM + 5 defect reports + summary", "hours": "10-14 h", "phase": "Week 6",
        "why": "Proves you can design tests systematically and document them to a professional standard — the core of a first QA role.",
        "steps": [
            "Pick one public practice app and one feature (e.g. checkout).",
            "Write requirements.md with concrete acceptance criteria (your test basis).",
            "Write docs/test-plan.md with all 13 sections, including out-of-scope and entry/exit criteria.",
            "Write 25+ test cases labelled by technique (EP, BVA, DT, ST, EX).",
            "Add a decision table and a boundary-value table with worked values.",
            "Build rtm.md linking every requirement to case IDs and defects.",
            "Log 5 full-format defect reports with anonymised evidence and repro rates.",
            "Write reports/test-summary.md with pass/fail/blocked counts, exit criteria, residual risk and a go/no-go recommendation.",
            "Write a README with a 'review this in 2 minutes' guide and push to GitHub.",
        ],
        "deliverables": ["test-plan.md", "requirements.md", "rtm.md", "25+ test cases", "5 defect reports", "test-summary.md", "README.md"],
        "artifact": """## Sample test case (copy this format)

| Field | Value |
|---|---|
| **ID** | `TC_CART_014` |
| **Title** | Reject an expired coupon |
| **Requirement** | `REQ-14 / AC-4` |
| **Priority** | High |
| **Technique** | BVA / state transition (coupon expiry) |
| **Preconditions** | Basket contains SKU-88 ($50.00); user signed in as Member; coupon `EXPIRED` ended yesterday. |
| **Test data** | email `qa.user14@example.com`, coupon `EXPIRED` |
| **Steps** | 1. Open `/cart`. 2. Enter `EXPIRED` in the promo field. 3. Click **Apply**. 4. Observe the total. |
| **Expected** | Inline message "Coupon EXPIRED has expired"; total stays `$50.00`; no discount row; no order submitted. |
| **Postconditions** | Clear the promo field. |

## Sample defect report skeleton

```text
ID:            DEF-003
Title:         [Cart] Discount applied twice with SAVE10 on orders over $100
Severity:      Major        Priority: High
Environment:   staging build 2026.04.7 · Chrome 125 / Windows 11 · Member
Preconditions: SKU-88 priced $120.00; coupon SAVE10 (10%) active.
Steps:         1. Add SKU-88 to cart. 2. Apply SAVE10. 3. Observe summary.
               4. Click Place order.
Actual:        Summary and confirmation show $96.00 (two discounts).
Expected:      $108.00 per REQ-14 / AC-2.
Evidence:      cart-003.png, cart-003.har, request-id 8f3c
Repro rate:    5/5. First seen 2026.04.7 (2026.04.6 OK).
Workaround:    Remove and re-add the coupon — not reliable.
```""",
    },
    {
        "id": "proj-bugs", "title": "Project 2 — Bug hunt & defect reports", "color": "#ff5470",
        "subtitle": "A 90-minute chartered exploratory session", "hours": "4-6 h", "phase": "Week 6 (stretch)",
        "why": "Your strongest existing skill. Proves you can find, isolate and document real problems — the thing service desk work has trained you for.",
        "steps": [
            "Write a charter and time-box a 90-minute session (no interruptions).",
            "Use 3 tours: money (revenue path), saboteur (try to break it), back-alley (neglected features).",
            "Keep session notes: covered, found, questions, next charters.",
            "Apply an error-guessing checklist: empty, long, special chars, double-submit, back/refresh, timezone, concurrent tabs.",
            "Write 5-8 full-format defect reports with mixed, justified severities.",
            "Include one intermittent defect with a quantified repro rate and isolation method.",
            "Include one non-functional finding (a11y, usability, or client/server validation).",
            "Add a 'bugs I did NOT log' section (duplicates / by-design / enhancements) with reasons.",
            "Finish with a 5 Whys on the worst finding and the regression case you'd add.",
        ],
        "deliverables": ["session-notes.md", "5-8 defect reports", "evidence/ (redacted)", "triage-notes.md", "5-whys.md"],
        "artifact": """## Exploratory session charter (template)

```text
CHARTER:  Explore the checkout flow, focusing on form validation,
          boundary values and error messages.
TIMEBOX:  90 minutes, no interruptions.
TOURS:    money, saboteur, back-alley.
NOTES:    - what I covered: ...
          - what I found: ...
          - questions raised: ...
          - charters to run next: ...
DEBRIEF:  3 findings logged, 1 duplicate excluded, 1 'by design'.
```

## Error-guessing checklist (tick as you go)

- [ ] Empty / null / whitespace-only fields
- [ ] Very long strings (1k, 10k characters)
- [ ] Special characters: `'`, `<`, `&`, emoji, non-Latin names
- [ ] Double-click / rapid resubmit / Back / refresh
- [ ] Two tabs editing the same record
- [ ] Session timeout mid-flow
- [ ] Timezone / end-of-month / leap-day edge
- [ ] Role changes (guest → member → suspended → admin)
- [ ] Network throttling / offline mid-request""",
    },
    {
        "id": "proj-api", "title": "Project 3 — API test collection in CI", "color": "#3df2c0",
        "subtitle": "Postman + assertions + Newman + GitHub Actions", "hours": "8-12 h", "phase": "Week 14",
        "why": "Proves you can test below the UI, write automated assertions and operate a pipeline — the most hireable technical skill for a first QA role.",
        "steps": [
            "Choose a free practice API (or your target app's API) and read its spec.",
            "Create a 20-case test matrix: valid, missing/wrong-type fields, boundaries, auth, duplicate POST, injection strings.",
            "Build a collection with folders by resource and descriptions referencing the spec.",
            "Use environments + {{variables}}; chain create → read → delete via collectionVariables.",
            "Add pm.test assertions on status, shape, business value, side effects, headers and response time.",
            "Add a data-driven boundary set from a CSV file with the Collection Runner.",
            "Export collection + environment JSON with placeholder secrets only.",
            "Add a Newman GitHub Actions workflow that uploads an HTML report `if: always()`.",
            "Write a README and a 'defects found / assertion that catches each' section.",
        ],
        "deliverables": ["postman_collection.json", "staging_environment.json", "order-cases.csv", "test-design.md", "api-tests.yml", "README.md"],
        "artifact": """## Reusable assertion block

```js
pm.test("Status is 201 and the resource was created", () => {
  pm.response.to.have.status(201);
});
pm.test("Response has the documented shape", () => {
  const b = pm.response.json();
  pm.expect(b).to.have.property("id");
  pm.expect(b.total).to.be.a("number");
  pm.expect(b.status).to.be.oneOf(["NEW", "PAID", "CANCELLED"]);
});
pm.test("Total matches the 10% discount", () => {
  pm.expect(pm.response.json().total).to.eql(108.00);
});
pm.test("Location header points at the new order", () => {
  pm.response.to.have.header("Location", /\\/orders\\/\\d+/);
});
pm.collectionVariables.set("orderId", pm.response.json().id);
```

## Minimal Newman CI step

```yaml
- run: npm install -g newman newman-reporter-htmlextra
- run: newman run collections/shop.json -e env/staging.json \\
         --env-var "token=${{ secrets.QA_TOKEN }}" --reporters cli,htmlextra
- uses: actions/upload-artifact@v4
  if: always()
  with: { name: api-report, path: report.html }
```""",
    },
    {
        "id": "proj-pw", "title": "Project 4 — Playwright framework in CI", "color": "#a78bfa",
        "subtitle": "POM + fixtures + data-driven tests + 3 browsers", "hours": "14-20 h", "phase": "Week 18-19",
        "why": "Proves you can code, structure a maintainable suite and operate it in CI — turning 'manual tester' into 'QA Analyst with automation skills'.",
        "steps": [
            "Scaffold with `npm init playwright@latest`; add .gitignore and package scripts.",
            "Configure 3 browser projects, baseURL from env, traces/screenshots/videos on failure.",
            "Write 15-25 specs: smoke, auth, checkout, negative paths, tags (@smoke/@regression).",
            "Use only getByRole/getByLabel/getByTestId locators; no absolute XPath.",
            "Add web-first assertions including negative ones (URL did NOT change, error hidden).",
            "Build Page Objects in pages/ and a logged-in custom fixture in fixtures/.",
            "Add one data-driven loop over a boundary-value table.",
            "Diagnose one real flake and write docs/flaky-test-journal.md.",
            "Add a GitHub Actions workflow (npm ci, secrets, uploaded report) and a live badge.",
            "Write a README with exact run commands and a 'what I'd improve next' section.",
        ],
        "deliverables": ["playwright.config.js", "tests/", "pages/", "fixtures/", "flaky-test-journal.md", "pw.yml", "README.md", "CI badge"],
        "artifact": """## Data-driven boundary loop (example)

```js
const cases = [
  { qty: 0,    ok: false }, { qty: 1,   ok: true },
  { qty: 999,  ok: true },  { qty: 1000, ok: false },
  { qty: -1,   ok: false },
];
for (const { qty, ok } of cases) {
  test(`quantity ${qty} is ${ok ? "accepted" : "rejected"}`, async ({ page }) => {
    await page.goto('/cart');
    await page.getByLabel('Quantity').fill(String(qty));
    await page.getByRole('button', { name: 'Update' }).click();
    const err = page.getByText('Invalid quantity');
    if (ok) await expect(err).toBeHidden();
    else await expect(err).toBeVisible();
  });
}
```

## Page Object (example)

```js
export class CartPage {
  constructor(page) { this.page = page; }
  async goto()      { await this.page.goto('/cart'); }
  async apply(code) {
    await this.page.getByLabel('Promo code').fill(code);
    await this.page.getByRole('button', { name: 'Apply' }).click();
  }
  total() { return this.page.getByTestId('cart-total'); }
  error() { return this.page.getByTestId('promo-error'); }
}
```""",
    },
    {
        "id": "proj-publish", "title": "Project 5 — Publish & present", "color": "#ffb020",
        "subtitle": "GitHub profile, one-page site, 90-second walkthroughs", "hours": "3-5 h", "phase": "Week 23-24",
        "why": "An invisible portfolio doesn't exist. This turns four repos into links on a resume and a story you can tell in an interview.",
        "steps": [
            "Write a GitHub profile README with your headline and links to the 4 repos.",
            "Set a real name/photo; pin exactly the 4 polished repos; archive scratch repos.",
            "Add topics/tags, a licence and descriptions to every repo.",
            "Create a one-page GitHub Pages site (optional) with 4 project cards and contact links.",
            "Verify every README has: purpose, prerequisites, exact run commands, expected output, approach, CI badge.",
            "Write a 90-second walkthrough per repo and rehearse it aloud.",
            "Add portfolio links to your resume, LinkedIn Featured section and cover letter.",
            "Post one learning note on LinkedIn/dev.to to start visible activity.",
        ],
        "deliverables": ["Profile README", "4 pinned repos", "Optional portfolio site", "4 rehearsed walkthroughs", "Resume/LinkedIn links"],
        "artifact": """## 90-second walkthrough template

> *The problem:* I had no QA job history, so I needed observable evidence.
> *What I did:* I picked a demo shop and wrote a test plan plus 28 cases —
> here's the decision table for the discount rules and the boundary set.
> *What I found:* 6 defects; this one was intermittent, so I quantified the
> repro rate and isolated it to a double-submit.
> *Then:* I automated the API checks with Postman assertions in Newman, and
> the top 12 UI journeys in Playwright with Page Objects and CI.
> *Hardest part:* X. *What I'd add next:* Y.

Lead with the decision, not the tool list. Be ready for:
"why that technique?", "what would you test next?", "what did you NOT test?".""",
    },
]

# ---------------------------------------------------------------------------
# Career kit
# ---------------------------------------------------------------------------
CAREER_KIT = {
    "skills": [
        ["Reproducing a user's issue", "Reproducing a defect with minimal deterministic steps", "'Reproduced and isolated defects using minimal deterministic steps'"],
        ["Reading logs and error messages", "Gathering evidence / root-cause analysis", "'Analysed application logs to isolate failure conditions'"],
        ["Ticket documentation", "Defect reports and test evidence", "'Authored clear, actionable defect reports with severity and evidence'"],
        ["Priority / SLA triage (P1-P4)", "Severity vs priority assessment", "'Triaged defects by technical severity and business impact'"],
        ["Escalation to L2/L3", "Cross-team defect triage", "'Partnered with engineering to resolve and verify fixes'"],
        ["Knowledge base articles", "Test documentation / test cases", "'Maintained reusable documentation of expected behaviour'"],
        ["SQL queries on a support DB", "Back-end data verification", "'Validated data integrity with SQL against persisted records'"],
        ["ITIL incident/change process", "STLC / defect workflow / release gates", "'Worked within structured change and release processes'"],
        ["Testing fixes before closing tickets", "Confirmation (retest) + regression testing", "'Performed retest and regression checks before closure'"],
        ["Handling angry users", "Quality conversations / defect triage diplomacy", "'Communicated risk calmly with evidence and options'"],
    ],
    "resume": {
        "bullets": [
            ["Resolved 40+ tickets/day for application issues", "Investigated and reproduced 40+ reported application defects daily, isolating root conditions from logs and user steps"],
            ["Escalated complex issues to L2/L3", "Produced structured, evidence-backed defect escalations with severity, repro steps and impact, enabling engineering resolution"],
            ["Wrote knowledge base articles", "Authored reusable documentation of expected system behaviour and verification procedures"],
            ["Ran SQL queries to check ticket data", "Validated back-end data integrity with SQL to confirm reported behaviour against persisted records"],
            ["Managed P1-P4 incidents to SLA", "Triaged issues by business impact and urgency, communicating risk and workarounds to stakeholders"],
            ["Tested fixes before closing tickets", "Performed confirmation (retest) and regression checks on fixes before closure"],
        ],
        "outline": """```
NAME  ·  Service Desk Technician → Software QA Analyst
[city] · [phone] · [email] · linkedin.com/in/... · github.com/...

SUMMARY
  Service Desk Technician (4 yrs) transitioning to Software QA Analyst.
  Investigated and documented 3,000+ application defects; strong in structured
  reproduction, log/SQL-based verification, impact-based triage and clear
  technical writing. Built a QA portfolio: a 28-case manual test suite with
  RTM, a 20-case Postman API collection running in Newman CI, and a Playwright
  framework in GitHub Actions. ISTQB CTFL (in progress).

PROJECTS                      ← LEAD WITH THIS as a career changer
  QA Portfolio — Manual Test Suite (github.com/…)      [2 bullets]
  API Test Collection — Postman + Newman CI (…)        [2 bullets]
  Playwright Framework — POM + GitHub Actions (…)      [2 bullets]
  Bug Hunt — 6 defect reports + 5 Whys (…)             [1-2 bullets]

SKILLS
  TESTING        Manual functional testing · Test design (EP, BVA, decision
                 tables, state transitions) · Test plans & cases · RTM ·
                 Defect lifecycle · Exploratory/SBTM · Regression · UAT
  API & DATA     REST · Postman (pm.test, environments, Newman) · SQL
                 (SELECT, JOIN, GROUP BY) · JSON/schema · Auth (401/403, IDOR)
  AUTOMATION     Playwright (locators, fixtures, POM, data-driven, CI) ·
                 Git · GitHub Actions · JavaScript (basics)
  TOOLS          Jira/JQL · TestRail · DevTools/HAR · VS Code · Linux CLI
  NON-FUNCTIONAL WCAG AA / axe / keyboard · k6 basics · OWASP Top 10 awareness

EXPERIENCE
  Service Desk Technician | Company | 2022-present
    - 3-4 translated bullets with numbers (see the rewrite table)

CERTIFICATIONS
  ISTQB CTFL (in progress) · ITIL 4 Foundation · [others]

EDUCATION
  [degree / diplomas]
```

Rules: one page, PDF, plain filename, standard headings for ATS, no photo,
no text-in-image, no 'References available on request'. Projects ABOVE
experience. Only list skills you can defend for five minutes.""",
    },
    "coverLetter": """Dear [Hiring Manager name],

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

Kind regards,
[Name] · [LinkedIn] · [GitHub]""",
    "titles": [
        "QA Analyst", "Software Test Analyst", "Software Tester", "Manual QA Tester",
        "Test Analyst", "Functional Test Analyst", "Junior QA Engineer",
        "Quality Assurance Analyst", "QA Specialist", "UAT Analyst",
        "Software QA Technician", "Junior Test Engineer", "QA Analyst (manual, automation training provided)",
        "Application Support Analyst with testing responsibilities",
    ],
    "jobSearch": [
        "Set your LinkedIn headline and 'Open to work' (recruiters-only) to the QA target titles.",
        "Build a tracking spreadsheet: company, role, date, link, contact, status, follow-up date, notes.",
        "Aim for 5-8 tailored applications per week — mirror 3 genuine keywords from each ad.",
        "Add one line about the company's product/domain in each cover letter.",
        "Find a human: a 15-minute chat or referral beats ten portal submissions.",
        "Follow up once after 7-10 days; then close the loop in your tracker.",
        "Post one learning note per week on LinkedIn to build visible activity.",
        "Practise 15 core Q&As aloud twice a week; rehearse the 90-second repo walkthroughs.",
        "Do a mock interview with a peer or record yourself answering STAR stories.",
        "After each interview, write down every question you were asked and add it to your drill list.",
    ],
    "first90": [
        {"when": "Days 1-30", "focus": "Learn", "actions": [
            "Read the existing test plan, RTM and regression pack.",
            "Run the existing suite; note the build, environment and any blockers.",
            "Shadow defect triage and a release sign-off meeting.",
            "Map environments, feature flags, test data sources and CI jobs.",
            "Ask 'what breaks most often?' and read the last 20 escaped defects.",
            "Fix one small documentation gap (a runbook or known-issues note).",
        ]},
        {"when": "Days 31-60", "focus": "Contribute", "actions": [
            "Own test design and execution for one story end to end.",
            "Run the regression pack and report results with build + environment.",
            "Log 5 well-written defects and retest fixes properly.",
            "Add one missing regression case for a recently escaped defect.",
            "Pair with a developer on a flaky test; document the fix.",
        ]},
        {"when": "Days 61-90", "focus": "Improve", "actions": [
            "Automate one high-value smoke flow, or add a CI quality check.",
            "Measure a before/after number (suite time, flakiness rate, escaped defects).",
            "Publish a short defect-pattern or coverage report to the team.",
            "Write down your 90-day achievements for your review and resume.",
        ]},
    ],
    "paths": [
        {"title": "Senior QA Analyst / QA Lead", "desc": "Test strategy, risk ownership, mentoring, release sign-off.", "next": "2-4 years; ISTQB Advanced, coaching skills"},
        {"title": "SDET / Test Automation Engineer", "desc": "Code-heavy frameworks, tooling and CI architecture.", "next": "Deepen JS/TS, API automation and pipeline design"},
        {"title": "Quality Engineer (QE)", "desc": "Whole-team quality, shift-left practices, process improvement.", "next": "Broader engineering + facilitation"},
        {"title": "Specialist: performance / security / a11y", "desc": "Deep expertise in one non-functional area.", "next": "k6/JMeter, OWASP labs, WCAG/axe mastery"},
        {"title": "Specialist: data / ETL / mobile", "desc": "Testing data pipelines or mobile platforms.", "next": "Advanced SQL, dbt, real-device labs"},
        {"title": "Adjacent: PO / BA / Release Manager", "desc": "Uses domain knowledge, communication and process skills.", "next": "Your support background transfers strongly here"},
    ],
}

# ---------------------------------------------------------------------------
# Interview Q&A bank
# ---------------------------------------------------------------------------
def IQ(cat, q, a):
    return {"cat": cat, "q": q, "a": a}

INTERVIEW = [
    IQ("Fundamentals", "What is the difference between QA and QC?",
       "QA is process-focused and preventive — standards, reviews and improving how we build. QC is product-focused and detective — actually checking the artefact. Testing is a QC activity inside a QA mindset."),
    IQ("Fundamentals", "Explain verification vs validation.",
       "Verification asks 'are we building the product right?' (reviews, static checks, documents). Validation asks 'are we building the right product?' (executing against real user needs). A review is verification; running a UAT scenario is validation."),
    IQ("Fundamentals", "What are the seven testing principles?",
       "1) Testing shows presence of defects, not absence. 2) Exhaustive testing is impossible. 3) Early testing saves time/money. 4) Defects cluster. 5) Pesticide paradox. 6) Testing is context dependent. 7) Absence-of-errors is a fallacy. Name all seven, then explain two briefly."),
    IQ("Fundamentals", "What does 'all tests passed' actually tell you?",
       "Only that no defects were found by the tests we designed. It can never prove the software is defect-free — coverage is limited by test design. Always mention residual risk."),
    IQ("Fundamentals", "What are the four test levels?",
       "Unit/component (a single function, developers), integration (components talking), system (the whole app end to end — the QA Analyst's main level), acceptance (business/customer sign-off). Regression is an activity across levels, not a level."),
    IQ("Fundamentals", "What is the test automation pyramid?",
       "Many fast cheap unit tests, some API/integration tests, few slow brittle E2E UI tests. Pushing checks down reduces cost and flakiness; the inverted 'ice-cream cone' is the anti-pattern."),
    IQ("Test design", "How would you test a login page?",
       "Structure it, don't list happy path only: valid credentials; wrong password/email; locked account; unknown email with no account enumeration; empty fields; boundary on password length; injection strings; very long inputs; remember-me/session; logout; reset link; 2FA; concurrent sessions; brute-force rate limiting; keyboard-only/accessibility; clear error messages; network failure; plus a SQL check that no session row is created for a failed login. Then prioritise by risk."),
    IQ("Test design", "Design test cases for a field that accepts 1-100.",
       "Equivalence partitioning: below-range (e.g. 0), in-range (50), above-range (101), plus invalid types (abc, empty, null, decimal). Boundary value analysis adds 0, 1, 2, 99, 100, 101. Name both techniques — that's what they're grading."),
    IQ("Test design", "What is a decision table and when would you use one?",
       "A table of conditions vs rules with resulting actions; one column = one test case. Use it whenever a requirement contains if/unless/except/and/or — pricing, eligibility, permissions. Collapse impossible combinations with 'don't care' entries."),
    IQ("Test design", "What is pairwise testing?",
       "A combinatorial technique ensuring every PAIR of values from any two parameters appears together, replacing dozens of full combinations with ~10 tests. Based on the observation that most defects involve one input or a pair. Use a generator, then add explicit high-risk combinations."),
    IQ("Test design", "Is exploratory testing just random clicking?",
       "No. It's simultaneous learning, design and execution, made rigorous with session-based test management: a charter, a time box, session notes and a debrief, plus tours (money, landmark, saboteur, fedex) and an error-guessing checklist."),
    IQ("Test design", "What is a test oracle?",
       "The mechanism or source used to decide whether an actual result is correct: a spec, a reference system, an independent SQL calculation, a spreadsheet, or a domain expert. It must be independent of the logic under test."),
    IQ("Defects", "Severity vs priority — give an example where they disagree.",
       "Severity = technical impact, set by QA; priority = business urgency, set by the PO. A misspelled company logo the day before a launch demo is Trivial severity but P1 priority."),
    IQ("Defects", "Retesting vs regression testing?",
       "Confirmation/retesting re-runs the exact failed case after the fix. Regression re-runs other previously-passing tests to detect side effects of the change. ISTQB calls the first 'confirmation testing'."),
    IQ("Defects", "What makes a good bug report?",
       "A unique ID, a one-line title naming module+fault+condition, severity/priority, environment and build, preconditions, minimal numbered steps, exact test data, actual vs expected with the AC reference, evidence (screenshot/HAR/log), a repro rate, a workaround, and one issue per ticket."),
    IQ("Defects", "A developer closes your bug as 'works as designed'. What do you do?",
       "Don't argue in the ticket. Check the acceptance criteria/spec, take it to refinement, get the requirement clarified or the AC updated, and record the decision. If it's user-impacting, raise it as a usability/requirements concern with evidence."),
    IQ("Defects", "How would you handle an intermittent 'cannot reproduce' bug?",
       "Capture full context each time (build, role, data, time, browser, flags, sequence), find what differs between pass and fail, control one variable at a time, force the condition (slow network, concurrency, cache), quantify the repro rate, and attach logs/HAR/recording."),
    IQ("Process", "Walk me through the STLC.",
       "Requirement analysis (RTM skeleton) → test planning (plan/strategy) → test case development (cases + data) → environment setup (smoke) → test execution (results + defects) → test cycle closure (summary report, exit criteria, residual risk, sign-off). Each has entry/exit criteria."),
    IQ("Process", "What is in a test plan?",
       "ID/version, objectives, scope IN and OUT, approach/techniques, environment & tools, test data, roles, schedule, risks WITH mitigations, defect management, entry/exit criteria, deliverables and approvals. A test strategy is higher-level and organisation-wide."),
    IQ("Process", "There's no time to test everything. How do you prioritise?",
       "Risk-based testing: score likelihood × impact, give high-risk areas more technique/depth/automation and earlier testing, and explicitly record low-risk areas as accepted residual risk with PO agreement. Always report the denominator."),
    IQ("Process", "What is a traceability matrix used for?",
       "Links requirements → test cases → defects to prove coverage, expose gaps and orphan tests, and support impact analysis when a requirement changes ('which tests must I revisit?')."),
    IQ("Process", "How do you 'shift left'?",
       "Review acceptance criteria before coding, ask 'what should happen when...?' in refinement, join Three Amigos, write test charters early, add contract/unit tests in the PR gate, and give developers a fast local test command. The measurable outcome is a shorter feedback loop."),
    IQ("SQL", "Write a query to count test cases per status.",
       "SELECT status, COUNT(*) FROM test_cases GROUP BY status; — and explain that WHERE filters rows before grouping while HAVING filters groups after aggregation."),
    IQ("SQL", "Why doesn't `status = NULL` work?",
       "NULL means unknown, so any comparison with it evaluates to unknown, not true. Use IS NULL / IS NOT NULL. Also COUNT(*) counts rows while COUNT(column) skips NULLs."),
    IQ("SQL", "How would you find test cases that have no defects?",
       "A LEFT JOIN plus an IS NULL check on the right side: SELECT tc.id FROM test_cases tc LEFT JOIN defects d ON tc.id = d.test_case_id WHERE d.id IS NULL;"),
    IQ("SQL", "How do you verify a UI 'order created' success message?",
       "Query the DB for the exact reference: exactly one row, correct total/status, the expected child order_items, and an audit/outbox record. Use an independent calculation as the oracle, not the app's own logic."),
    IQ("API", "401 vs 403?",
       "401 Unauthenticated = we don't know who you are (missing/invalid/expired token). 403 Forbidden = we know who you are but you lack the role/scope. A valid token with the wrong role is 403."),
    IQ("API", "POST vs PUT vs PATCH?",
       "POST creates/submits and is NOT idempotent (repeating can duplicate). PUT replaces a whole resource and IS idempotent. PATCH partially updates. Safe methods (GET) don't change state."),
    IQ("API", "What would you test on POST /orders?",
       "Valid → 201 + Location + correct body; missing/wrong-type fields → 400/422 with no partial write; boundaries and extra fields; no auth → 401; wrong role → 403; duplicate POST → two orders unless an Idempotency-Key; injection strings; follow-up GET to confirm persistence; DELETE then GET → 404; error bodies must be consistent with no stack traces."),
    IQ("API", "The API returns the right data but the page shows the wrong value. Where's the bug?",
       "Front-end rendering/state. Attach the response body and a screenshot. If the response itself is wrong, it's a back-end defect. This 30-second triage is exactly what the Network panel gives you."),
    IQ("API", "What is a contract test?",
       "A test of the agreed request/response shape between a consumer and a provider (often consumer-driven, e.g. Pact), catching breaking changes — removed fields, type changes, new required fields — before integration."),
    IQ("Automation", "What is a flaky test and how do you fix one?",
       "A test that passes/fails with no code change. Reproduce with repeats, read the error/call log, replace fixed sleeps with condition waits, make locators strict and unambiguous, remove ordering dependencies and shared data, stabilise the environment, then quarantine and fix or delete. Never just raise retries."),
    IQ("Automation", "Why use the Page Object Model?",
       "Selectors and actions live in one class, so a UI change is fixed in one place instead of dozens of tests; tests read as business rules. Keep assertions in the tests, not the page objects."),
    IQ("Automation", "How do you choose locators?",
       "Prefer user-facing ones: getByRole, getByLabel, getByText, then data-testid. Avoid absolute XPath and positional nth-child. Scope repeated elements with filter()/chaining. getByRole also doubles as a partial accessibility check."),
    IQ("Automation", "What is auto-waiting, and why not use sleep(2000)?",
       "Playwright waits for elements to be visible/stable/enabled and retries web-first assertions until a timeout. Fixed sleeps are slow and flaky because they guess rather than observe the real condition."),
    IQ("Automation", "How do automated tests run in CI?",
       "GitHub Actions: checkout → setup-node → npm ci → install browsers → run tests with secrets from the secret store → upload the HTML report with if: always(). The job is a required status check so a red build blocks merging."),
    IQ("Automation", "What would you NOT automate?",
       "One-off/changing features, subjective usability and visual judgement, anything with an unclear expected result, and tests depending on flaky uncontrolled third parties. Automate stable, repetitive, high-risk checks with a clear oracle."),
    IQ("Career change", "Why are you moving from service desk to QA?",
       "'I've spent years being the last line of defence for users — reproducing problems, isolating causes with logs and SQL, and documenting them so engineers can act. I want to move upstream and prevent those problems before release, and I've built the testing skills plus a portfolio to do it.' One confident paragraph, then proof. Never frame it as escaping tickets."),
    IQ("Career change", "You have no QA experience. Why should we hire you?",
       "Three parts: (1) transferable evidence — thousands of defects investigated, triage by impact, documentation; (2) new proof — four portfolio repos with a test plan, API collection and Playwright CI framework; (3) perspective — I know how software actually fails for real users. Then offer to walk through a repo."),
    IQ("Career change", "Walk me through one of your portfolio projects.",
       "Use the 90-second shape: problem → what I tested → the technique/decision (show the decision table or boundary set) → what I found (one intermittent bug with a repro rate) → how I automated it → hardest part → what I'd add next. Lead with decisions, not tool names."),
    IQ("Behavioural", "Tell me about a difficult problem you solved.",
       "STAR: a critical app failed for ~40 users at month-end (S); I owned diagnosis/escalation (T); reproduced with a clean account, correlated logs by request ID, isolated it to a config change in the last deploy, briefed L3 with a minimal repro and gave support a workaround (A); restored in 90 minutes, wrote a runbook, and the check moved pre-release (R)."),
    IQ("Behavioural", "Tell me about a time you disagreed with someone about quality.",
       "STAR: a change was due to go live with an unresolved issue; I documented impact and repro, proposed three options (delay / feature-flag off / accept risk with rollback), escalated with evidence not emotion; the manager chose flag-off, no customer impact, and the decision was recorded."),
    IQ("Behavioural", "Tell me about a mistake you made.",
       "STAR: I closed a ticket after a fix appeared to work; it recurred; I re-opened immediately, told the user and team, traced my assumption (I'd tested the wrong account role), added a verification step to my checklist; no repeat, and the checklist became team standard."),
    IQ("Behavioural", "Tell me about a pattern you spotted that others missed.",
       "STAR: 30 recurring 'printer' tickets were actually the same auth/token-expiry failure; I grouped them, correlated timestamps with a config change, proved the common cause with logs, raised one problem record; volume dropped ~80% and a KB article prevented repeats."),
    IQ("Behavioural", "How do you handle pressure and competing priorities?",
       "Impact-based triage, explicit communication of what's blocked and why, a visible tracker, and a short daily re-prioritisation. Give a real example with an SLA and a number. End with the QA bridge: the same habit becomes risk-based test prioritisation."),
    IQ("Behavioural", "What questions do you have for us?",
       "Ask about the current regression pack and how much is automated; how QA is involved in refinement/AC; the biggest quality problem the team is solving; how release readiness is decided and who signs off; and what success looks like in the first 90 days."),
]

# ---------------------------------------------------------------------------
# Long-form study plans (rendered like DeskReady's plan view)
# ---------------------------------------------------------------------------
PLAN_SCHEDULE = """# The 24-Week QA Analyst Study Schedule

**Goal:** go from service desk technician to a *job-ready* Software QA Analyst,
part-time. **Assumes:** ~8-10 focused hours a week (≈45 min on 3-4 weekdays +
a 2-3 h weekend build session). **Companion:** the full *QA Career Guide* plan.

**Rhythm:** Mon-Thu = learn + exercises; Sat = build the deliverable; Sun =
checkpoint quiz + journal. **The rule:** ship something every week. If a week
slips, drop the stretch reading — never the deliverable.

---

## Setup once (before Week 1)
- Install **VS Code**, **Node.js LTS**, **Git**. Create a **GitHub** account.
- Start `journal.md`: one paragraph per study day — what you did, what confused you, what to revisit.
- Book recurring calendar blocks. Treat them like a shift you cannot swap.
- Pick a **practice app** for your portfolio (SauceDemo, Automation Exercise, or an open-source app run locally).
- Export your QAReady progress from Settings once a week as a backup.

---

# Phase 0 — Start here (Week 1)

## Week 1 — Orientation
- **Mon:** Courses `orientation` lessons 1-2. Write your 'why QA' paragraph.
- **Tue:** Lesson 3-4. Set up GitHub, VS Code, Node, Git, the journal.
- **Wed:** `foundations` lessons 1-2 (SDLC, Agile). Sketch the STLC on paper.
- **Thu:** Lessons 3-4 (7 principles). Write each principle in your own words.
- **Sat:** Lessons 5-6 (levels, types, vocabulary). Build a 1-page cheat sheet.
- **Sun:** Orientation + Foundations quizzes; 10 glossary flashcards.
- **Deliverable:** journal + GitHub account + STLC/principles cheat sheet.
- **Checkpoint:** explain the role + 5 transferable skills without notes.

## Week 2 — Foundations consolidation
- Re-read anything below 80% on the quizzes. Drill 20 glossary cards.
- Write 5 Given/When/Then acceptance criteria for your practice app's login.
- **Deliverable:** AC examples + corrected cheat sheet. **Checkpoint:** Foundations quiz ≥ 80%.

---

# Phase 1 — Manual QA craft (Weeks 2-6)

## Week 3 — Test design: partitioning & boundaries
- `test-design` lessons 1-3. Do every worked example on paper *before* checking.
- Build a BVA table for your app's quantity/price field (6 values + rounding question).
- **Deliverable:** worked EP + BVA examples. **Checkpoint:** design cases for an unseen field unaided.

## Week 4 — Decision tables, states, exploration
- Lessons 4-7. Write a decision table for your app's discount/shipping rules.
- Draw a state diagram for an order; list 4 forbidden transitions.
- Run a **45-minute chartered exploratory session**; keep SBTM notes.
- **Deliverable:** decision table + state diagram + session notes. **Checkpoint:** Test-design quiz ≥ 80%.

## Week 5 — Documentation
- `test-docs` lessons 1-6. Draft the test plan for your practice app (all 13 sections).
- Write 15 test cases in the standard format; build the RTM.
- Estimate effort bottom-up and write a 3-item risk register.
- **Deliverable:** draft plan + RTM + 15 cases. **Checkpoint:** Test-docs quiz ≥ 80%.

## Week 6 — Defects, tools & communication; SHIP PROJECT 1
- `defects` lessons 1-6, `tools` lessons 1-5, `communication` lessons 1-4.
- Practise DevTools: save a HAR, copy a request as cURL, split a UI vs API bug.
- Log 5 full-format defect reports (mixed severities, one intermittent).
- Write the test summary report with exit criteria and a go/no-go recommendation.
- **Deliverable:** **PROJECT 1** — full manual test suite repo, README complete.
- **Checkpoint:** Defects quiz ≥ 80%; a stranger can follow your test case.

---

# Phase 2 — Technical foundations (Weeks 7-12)

## Week 7 — The web
- `web` lessons 1-3. Draw the request/response journey; memorise the status families.
- In DevTools, inspect a login request: method, status, payload, response, timing.
- **Deliverable:** labelled HTTP diagram + status-code cheat sheet. **Checkpoint:** Web quiz ≥ 80%.

## Week 8 — DevTools & first SQL
- `web` lessons 4-5. Produce one HAR with a written UI-vs-API triage note.
- `sql` lessons 1-2. Run every in-app SQL exercise; then write 10 of your own.
- **Deliverable:** HAR + triage note + 10 queries. **Checkpoint:** 10 basic queries unaided.

## Week 9 — SQL in depth
- `sql` lessons 3-5: NULL/IN/LIKE/BETWEEN, GROUP BY/HAVING, JOINs.
- Write `verification-queries.sql`: 15 commented queries (orphans, duplicates, impossible values, state mismatches).
- **Deliverable:** verification-queries.sql. **Checkpoint:** SQL quiz ≥ 80%.

## Week 10 — Safe writes, CLI, Git
- `sql` lessons 6-7; `cli-git` lessons 1-2.
- Practise `SELECT`-before-`UPDATE` and `BEGIN/ROLLBACK` in a sandbox DB.
- Bandit levels 0-10; write a CLI cheat sheet; first GitHub repo with a real README.
- **Deliverable:** CLI cheat sheet + first repo. **Checkpoint:** CLI/Git quiz ≥ 80%.

## Week 11 — Git collaboration + JavaScript basics
- `cli-git` lessons 3-5; open a PR to your own repo; write Markdown docs.
- `javascript` lessons 1-3: variables, conditions, loops, functions.
- **Deliverable:** a small JS script that classifies test results + a PR.
- **Checkpoint:** JavaScript quiz ≥ 80% (after Week 12).

## Week 12 — JS objects, JSON, async; API intro
- `javascript` lessons 4-6; `api` lesson 1.
- Write a script that fetches JSON and validates its shape; explain a Promise aloud.
- **Deliverable:** fetch-and-validate script. **Checkpoint:** explain an off-by-one and a Promise.

---

# Phase 3 — API testing (Weeks 13-14)

## Week 13 — REST, auth, errors
- `api` lessons 1-5. Build the 8-row auth negative matrix from memory.
- Write a 20-case test matrix for `POST /orders` (positive/negative/boundary/idempotency).
- **Deliverable:** 20-case API matrix. **Checkpoint:** API quiz ≥ 80%.

## Week 14 — Postman, Newman, SHIP PROJECT 3
- `postman` lessons 1-6. Build the collection, assertions, chaining, data file.
- Add the Newman GitHub Actions workflow with an uploaded HTML report.
- **Deliverable:** **PROJECT 3** — public API repo with a green CI badge.
- **Checkpoint:** Postman quiz ≥ 80%; `if: always()` report visible.

---

# Phase 4 — Automation & CI/CD (Weeks 15-20)

## Week 15 — Strategy
- `automation` lessons 1-4. Write an automation strategy for your app: what, why, and what NOT to automate.
- **Deliverable:** strategy doc. **Checkpoint:** Automation quiz ≥ 80%.

## Week 16 — First Playwright tests
- `playwright` lessons 1-2. Scaffold, configure, write 10 specs using getByRole/getByLabel only.
- Run in `--ui` mode and read a failure's call log.
- **Deliverable:** 10 passing specs. **Checkpoint:** all green in UI mode.

## Week 17 — Locators, waits, fixtures
- Lessons 3-5. Build a logged-in fixture, 3-browser config, storageState.
- Deliberately create and then diagnose one flaky test.
- **Deliverable:** fixture + config + flake notes. **Checkpoint:** Playwright quiz ≥ 80%.

## Week 18 — POM, data-driven, reports — PROJECT 4 part 1
- Lessons 6-7. Add Page Objects, a BVA data loop, traces and an HTML report.
- **Deliverable:** POM framework + flaky-test-journal.md. **Checkpoint:** green on Chromium + WebKit.

## Week 19 — CI/CD — PROJECT 4 part 2
- `cicd` lessons 1-2. Add the workflow: npm ci, secrets, report artefact, required check.
- **Deliverable:** live CI badge. **Checkpoint:** CI/CD quiz ≥ 80%.

## Week 20 — Gates, metrics, polish
- `cicd` lessons 3-5. Write a one-paragraph quality report for your portfolio app.
- Polish all four READMEs; verify no secrets; pin the repos.
- **Deliverable:** 4 polished repos. **Checkpoint:** 60-second skim works.

---

# Phase 5 — Beyond functional (Weeks 21-22)

## Week 21 — Performance, a11y, security
- `nonfunctional` lessons 1-3. Run a keyboard-only pass; install axe; run a Lighthouse audit.
- Write 3 measurable non-functional acceptance criteria (p95, WCAG AA, input handling).
- **Deliverable:** non-functional appendix to the Project 1 test plan.

## Week 22 — Usability, compatibility, localisation, gating
- Lessons 4-6. Build a pairwise browser/OS/role matrix; test a unicode name and a date-format edge.
- **Deliverable:** matrix + a WCAG-referenced finding. **Checkpoint:** Non-functional quiz ≥ 80%.

---

# Phase 6 — Get hired (Weeks 23-24)

## Week 23 — ISTQB + publish
- `istqb` lessons 1-4 (syllabus, gaps, terminology, exam strategy). Two timed mocks.
- `portfolio` lessons 1-5; finish and publish all four repos + optional one-page site.
- **Deliverable:** 4 pinned repos + 2 timed mocks. **Checkpoint:** ISTQB quiz ≥ 80%.

## Week 24 — Career sprint
- `career` lessons 1-7. Rewrite resume + LinkedIn; write 6 STAR stories; drill all 40 interview Q&As.
- Rehearse four 90-second repo walkthroughs aloud; do a mock interview.
- Send 20 tailored applications with a tracking spreadsheet and 2 referrals.
- **Deliverable:** one-page QA resume + 20 applications + 6 STAR stories.
- **Checkpoint:** Career quiz ≥ 80%; answer 15 core questions aloud without notes.

---

## After Week 24
Keep applying, keep the CI badges green, and keep adding one learning note a week.
Re-read the *First 90 Days* plan the day you get the offer. The portfolio is a
habit, not a one-off project — your first real sprint will produce better material
than any demo app ever could.
"""

PLAN_GUIDE = """# The Complete Service Desk → QA Analyst Career Guide

**Who this is for:** a service desk / application support technician with strong
troubleshooting, ticketing, SQL and documentation skills, and no formal QA job
history. **Target role:** Software QA Analyst (manual-first, with API and
automation skills). **Timeline:** 24 weeks part-time, ~8-10 h/week.

---

## 0. How to use this guide
- It is organised in **layers**. Each layer has: *why it matters → what to learn →
  hands-on drills → milestone artefact → interview questions → resources*.
- Study in the order in §2. **Do not skip manual test design** — everything else
  assumes you can decide what a good check is.
- For every layer, **build something**. Skills without a repo do not count in
  interviews, especially when you are changing careers.
- Keep a journal. Write definitions in your own words; copying is not learning.
- Repeat: SQL, glossary flashcards and interview answers all reward spaced
  repetition over cramming.

---

## 1. The skill stack at a glance

| Layer | Skill | Why it's there | Weeks |
|---|---|---|---|
| Mindset | QA role + transferable skills | Re-label what you already do | 1 |
| Core | Testing theory, STLC, Agile, 7 principles | The vocabulary and mental map | 1-2 |
| Core | Test design techniques | Choose the few tests that find the most bugs | 2-4 |
| Core | Test cases, plans, RTM, defect reports | The actual artefacts of the job | 3-6 |
| Tools | Jira, TestRail, DevTools, HAR | Operate in a real team | 5-6 |
| Technical | Web/HTTP, SQL, CLI, Git, JavaScript | Test below the UI | 7-12 |
| API | REST, auth, Postman, Newman | Highest-leverage automation for a first role | 13-14 |
| Automation | Strategy, Playwright, POM, CI/CD | Multiply your manual test design | 15-20 |
| Non-functional | Performance, a11y, security, compatibility | Quality is more than correctness | 21-22 |
| Career | ISTQB, portfolio, resume, interviews | Turn skills into an offer | 23-24 |

---

## 2. Study order and why it is this order

1. **Orientation** — know the destination and your starting advantage.
2. **Foundations** — SDLC/STLC, principles, levels/types, exact vocabulary.
3. **Manual test design** — equivalence partitioning, boundary values, decision
   tables, state transitions, exploratory/SBTM, pairwise.
4. **Test documentation & defects** — cases, plans, RTM, reports, lifecycle.
5. **Tools & communication** — Jira/JQL, test management, DevTools, evidence,
   requirements questions, triage and difficult quality conversations.
6. **Technical foundations** — HTTP/web, SQL, CLI/Git, JavaScript.
7. **API testing** — REST, auth, Postman assertions, Newman CI.
8. **Automation** — strategy, Playwright, POM, fixtures, traces, CI/CD, gates.
9. **Non-functional** — performance, accessibility, security, usability, i18n.
10. **Career** — certification, portfolio, resume, interviews, first 90 days.

Why manual before automation: **automation is coding a check for behaviour you
already understand**. If you cannot design a good test case by hand, your
automated test will simply assert the wrong thing very quickly. Hiring managers
for a first QA role care more about test thinking than framework syntax.

---

## 3. Layer detail

### 3a. Testing theory
**Why:** interviewers use this vocabulary as a filter, and it explains why some
habits waste time.

**Learn:** SDLC (Waterfall, V-Model, Agile/iterative); STLC's six phases with
entry/exit criteria; the seven testing principles; test levels (unit,
integration, system, acceptance) vs test types (functional, non-functional,
static, dynamic); verification vs validation; black-box vs white-box; retesting
vs regression; the fault/failure/error chain; test basis, oracle, coverage,
traceability, residual risk.

**Drills:** sketch STLC from memory; write 5 Given/When/Then acceptance criteria;
explain all 7 principles with a real example each; classify 10 scenarios by
level and type.

**Milestone:** a one-page cheat sheet in your own words + ≥80% on the Foundations
and Orientation quizzes.

**Interview:** 'What are the 7 principles?' · 'QA vs QC?' · 'Verification vs
validation?' · 'What does all tests passed actually mean?'

---

### 3b. Test design (the craft)
**Why:** exhaustive testing is impossible; technique makes your sampling
defensible.

**Learn:** equivalence partitioning (valid + invalid + special-state classes),
boundary value analysis (L-1, L, L+1, U-1, U, U+1 plus zero/empty/max/last),
decision tables (conditions → rules → actions, collapse impossible combos),
state transition testing (valid, forbidden, round trips, 1-switch), use-case
scenario testing, session-based exploratory testing (charter, time box, notes,
debrief, tours), error guessing, pairwise/all-pairs.

**Drills:** BVA table for a 1-100 field; decision table for premium + >$100 +
express; state diagram for an order with 4 forbidden transitions; a 45-minute
chartered session with notes; a 9-row pairwise browser/OS/role matrix.

**Milestone:** technique-labelled cases inside Portfolio Project 1.

**Interview:** 'Test a login page' · 'Design cases for 1-100' · 'Is exploratory
testing random clicking?' · 'When would you use a decision table?'

---

### 3c. Documentation & defects
**Why:** these artefacts are the job's output and the thing a hiring manager can
inspect.

**Learn:** test case anatomy (ID, title, AC ref, priority, preconditions, data,
numbered single-action steps, specific expected result including what must NOT
happen, postconditions); test data and independence (setup/teardown, unique
data, never production data); RTM and coverage reporting; the 13-section test
plan (scope IN and OUT, approach, environment, data, roles, schedule, risks +
mitigations, defect management, entry/exit criteria, approvals); risk-based
testing (likelihood × impact); bottom-up estimation with contingency; execution
statuses (Passed/Failed/Blocked/Not Run/Skipped/Retest); test summary report.

**Defects:** what counts as a bug (including implicit requirements); the perfect
report (title, severity/priority, environment/build, preconditions, minimal
steps, exact data, actual vs expected with AC ref, evidence, repro rate,
workaround, one issue per ticket); severity vs priority; lifecycle and triage;
confirmation vs regression; reproducibility and 5 Whys root cause.

**Milestone:** Portfolio Project 1 (plan + 25 cases + RTM + 5 reports + summary)
and Project 2 (bug hunt).

**Interview:** 'Severity vs priority with an example' · 'What's in a test plan?'
· 'Retest vs regression?' · 'What makes a good bug report?' · 'Works as designed
— what now?'

---

### 3d. Technical foundations
**Why:** the UI is the last 10% of the story. Test below it.

**Learn:**
- **Web/HTTP:** DNS → TCP/TLS → request → server/DB → response → render;
  methods (safe/idempotent); status families with 401/403/400/422/429/500;
  headers, cookies, tokens, cache; HTML/CSS/JS basics and locators; DevTools
  Elements/Console/Network/Application; HAR and Copy as cURL; the 30-second
  UI-vs-API triage.
- **SQL:** tables/keys/NULL; SELECT/WHERE/ORDER BY/LIMIT; IN/BETWEEN/LIKE/
  DISTINCT/IS NULL; aggregates + GROUP BY + HAVING; JOINs and anti-joins;
  INSERT/UPDATE/DELETE with transactions and SELECT-first safety; using SQL as
  an independent oracle to verify persistence and data integrity.
- **CLI/Git:** pwd/ls/cd/cat/less/head/tail/grep/find, pipes and redirection,
  permissions (754), processes/ports/logs with request IDs, Git working
  tree→stage→commit→remote, branches/PRs/diffs, Markdown, README/config/CI
  orientation.
- **JavaScript:** const/let, six types, ===, falsy values, template literals,
  if/else/ternary, for...of, bounded while, functions and purity, arrays
  (map/filter/find/reduce), objects (destructuring/spread/optional chaining),
  JSON, async/await, a repeatable debugging routine.

**Drills:** one HAR with a triage note; `verification-queries.sql` (15 commented
queries); Bandit 0-10; a PR to your own repo; a JS script that fetches and
validates JSON.

**Milestone:** first GitHub repo with a real README; SQL/JS quizzes ≥80%.

**Interview:** '401 vs 403?' · 'Count per status?' · '= NULL vs IS NULL?' ·
'UI shows wrong data but the API is right — where's the bug?' · 'What's a
Promise?'

---

### 3e. API testing
**Why:** fast, stable, early, and able to send payloads the UI never allows.

**Learn:** REST resources/statelessness/contracts (OpenAPI); JSON schemas and
breaking changes; auth (API keys, bearer/JWT, OAuth scopes) and the 8-row
negative matrix including IDOR; status/error bodies; idempotency and duplicate
POST; versioning, pagination boundaries, filter/date inclusivity; Postman
collections/environments/variables/chaining; `pm.test`/`pm.expect` assertions;
Collection Runner and CSV data-driven runs; Newman CLI + GitHub Actions;
mocks/stubs and residual risk; consumer-driven contract testing.

**Milestone:** Portfolio Project 3 — public asserted collection + green Newman CI.

**Interview:** 'What would you test on POST /orders?' · 'POST vs PUT?' · 'How do
you test auth?' · 'What is a contract test?'

---

### 3f. Automation & CI/CD
**Why:** encode your test thinking so it runs on every change.

**Learn:** the pyramid and the ice-cream-cone anti-pattern; what to automate
(stable, repetitive, high-risk, deterministic, clear oracle) and what not to;
ROI and the maintenance bill; tool choice (Playwright/Cypress/Selenium) and
transferable concepts; Arrange→Act→Assert→Cleanup; Node/npm setup, config
(baseURL, projects, retries, traces/reports); first tests, resilient locators,
actions, web-first assertions, auto-waiting; fixtures/hooks/storageState;
Page Object Model; data-driven boundary loops; traces/screenshots/videos;
flakiness diagnosis and quarantine; CI/CD concepts, a GitHub Actions workflow
with npm ci + secrets + `if: always()` artefacts, required status checks,
quality gates, Definition of Done, meaningful vs vanity metrics.

**Milestone:** Portfolio Project 4 — Playwright framework with a live CI badge.

**Interview:** 'Fix a flaky test' · 'Why POM?' · 'How do you choose locators?'
· 'Explain your CI pipeline' · 'What would you NOT automate?'

---

### 3g. Non-functional
**Why:** bug-free can still be slow, inaccessible, insecure or unusable — the
absence-of-errors fallacy.

**Learn:** load/stress/soak/spike, p95/p99 vs averages, measurable targets and
k6 thresholds; WCAG POUR and AA, keyboard/zoom/contrast/labels/headings/screen
readers, axe and its ~30-40% ceiling; OWASP Top 10 awareness with safe,
authorised checks (auth matrix, input handling, error hygiene, session, rate
limiting); usability; pairwise-driven compatibility and mobile risks;
localisation (dates, numbers, text expansion, unicode, RTL) and privacy
(masking, consent, erasure, no PII in logs/HARs); writing non-functional
acceptance criteria and gating cheap scans in CI.

**Milestone:** a non-functional appendix to the Project 1 test plan.

**Interview:** 'Why p95 not average?' · 'What is WCAG AA?' · 'What is IDOR?' ·
'Name 3 measurable non-functional requirements.'

---

## 4. The portfolio (the most important section)

Four shipped repos beat any certificate for a career changer:

| # | Repo | Proves |
|---|---|---|
| 1 | Manual test suite | Test design, documentation, defect reporting, risk judgement |
| 2 | Bug hunt | Reproducibility, triage, evidence, 5 Whys |
| 3 | Postman + Newman CI | API testing, assertions, CI |
| 4 | Playwright framework | Coding, structure, automation, CI |

Use **one target app** across all four. Each README needs purpose, prerequisites,
exact run commands, expected output, approach, a green CI badge and a 'what I'd
improve next'. No secrets. Pin the four best repos. Prepare a 90-second
walkthrough of each: problem → decision/technique → what you found → how you
automated it → hardest part → next step. See the Portfolio view for full
checklists and templates.

---

## 5. Certification
**ISTQB CTFL** is the one worth doing: recognised, cheap, and ~80% already
covered by Phases 0-2. Treat it as a vocabulary exam. Extra study: static
testing/reviews (roles, review types, process), exact ISTQB definitions, test
analysis vs design, psychology/independence, maintenance testing. Read the free
official syllabus, do 4+ timed mocks, and log every wrong answer. List it
honestly under Certifications, below Projects on the resume.

---

## 6. Repositioning your experience

The single most important rewrite: **tickets → defects, triage → severity/risk,
KB articles → test documentation, SQL checks → back-end verification, retesting
fixes → confirmation/regression testing**.

Summary statement: *'Service Desk Technician (4 yrs) transitioning to Software
QA Analyst. Investigated and documented 3,000+ application defects; strong in
structured reproduction, log/SQL-based verification, impact-based triage and
clear technical writing. Built a QA portfolio: a 28-case test suite with RTM, a
20-case Postman API collection in Newman CI, and a Playwright framework in
GitHub Actions. ISTQB CTFL (in progress).'*

Put **Projects above Experience**, one page, PDF, quantified bullets, standard
ATS headings. LinkedIn headline: `Service Desk → Software QA Analyst | Manual &
API testing | Playwright`. Cover letter: one confident paragraph on the switch,
then portfolio proof. Never apologise for the career change.

---

## 7. Interview preparation

**The loop:** recruiter screen → QA/technical interview → practical exercise →
team/behavioural → offer.

**Drill three banks** (see the Career view): ~15 manual/fundamentals Q&As, SQL/API/
automation Q&As, and 6 STAR stories drawn from real service desk work. Use
**PREP** (Point → Reason → Example → Point). In practical exercises, **state
your assumptions out loud** — that is the test-design mindset. For a live bug
hunt: talk through your charter, log 4-6 well-written defects, and say what you
deliberately did NOT log.

**Behavioural stories to prepare:** a difficult escalation, a pattern others
missed, a disagreement about a risky change, a mistake you owned, learning a
tool fast, and going beyond the ticket. End each with: *'That's the same instinct
I'd bring to QA — reproduce, isolate with evidence, document so it never costs
the team a day again.'*

**Questions to ask them:** about the regression pack, QA in refinement, the
team's biggest quality problem, release sign-off, and what success looks like in
90 days.

---

## 8. Resources
Free: Test Automation University, Guru99, freeCodeCamp, MDN HTTP, Postman
Academy, Playwright docs, SQLZoo, DataLemur, Learn Git Branching, Pro Git,
LinuxCommand.org, OverTheWire Bandit, PortSwigger Academy, OWASP Juice Shop,
Deque axe, WebAIM, Lighthouse. Practice apps: JSONPlaceholder, ReqRes,
httpbin, Petstore, SauceDemo, Automation Exercise, the-internet. Communities:
Ministry of Testing, sqa.stackexchange, r/softwaretesting, TestGuild. Books:
*Lessons Learned in Software Testing*, *Explore It!*, *Agile Testing*, *The Art
of Software Testing*. Full links are in the Toolkit view.

---

## 9. First 90 days and beyond
- **Days 1-30 Learn:** read the plan/RTM, run the suite, shadow triage, map
  environments and flags, read 20 escaped defects, fix one documentation gap.
- **Days 31-60 Contribute:** own one story end to end, run the regression pack,
  log 5 good defects, add a regression case for an escape, pair on a flake.
- **Days 61-90 Improve:** automate one high-value smoke flow or add a CI check,
  measure a before/after number, publish a defect-pattern report.

**Paths:** Senior QA / QA Lead, SDET / Test Automation Engineer, Quality
Engineer, specialist (performance, security, accessibility, data/ETL, mobile),
or adjacent (PO, BA, Release Manager). Your support background keeps paying off:
you know how software fails for real people better than most people who started
in QA. Keep that perspective — it is a differentiator, not baggage.

---

## 10. Rules to remember
1. Testing shows the presence of defects, not their absence.
2. If you cannot state the expected result precisely, you cannot automate it.
3. One defect per ticket; one action per step; one issue per conversation.
4. Record the build, environment and role with every result.
5. Never silently re-run a flaky test; never test against production data.
6. Every week ships an artefact. Every release names its residual risk.
7. Evidence beats claims — especially when you are changing careers.
"""

PLANS = [
    {"id": "study-schedule", "title": "24-Week Study Schedule", "subtitle": "Week-by-week daily plan",
     "description": "The full roadmap broken into 24 weeks: daily focus, a shipped deliverable each week, and a checkpoint self-test.",
     "color": "#3df2c0", "body": PLAN_SCHEDULE},
    {"id": "career-guide", "title": "The Complete QA Career Guide", "subtitle": "Detailed layer-by-layer guide",
     "description": "Every skill layer in depth with why/what/drills/milestone/interview questions/resources, plus the portfolio, resume and first-90-days playbooks.",
     "color": "#4f8cff", "body": PLAN_GUIDE},
]
