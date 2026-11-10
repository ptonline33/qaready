"""Phase 0-1 courses: orientation, foundations, test design, docs, defects."""
from . import lesson, course, quiz, mcq, inp, order, mdex, sqlex, P, table

# ---------------------------------------------------------------------------
# 1. Orientation
# ---------------------------------------------------------------------------
ORIENTATION = course(
    "orientation", "Welcome to QA", "Your bridge from the service desk",
    "What a Software QA Analyst actually does, why your service desk experience is a genuine advantage, and how to use this 24-week roadmap. Start here.",
    "#7b5cff", "p0", "Week 1", "Beginner",
    [
        lesson("orient-01", "The job you are aiming for", 10,
               "A **Software QA Analyst** (often called QA Engineer, Test Analyst, or Software Tester) is the person who makes sure software does what it is supposed to do — before real users find out that it doesn't. This lesson maps the role, the team around it, and the career ladder, so you know exactly what you are training for.",
               [
                 ("What a QA Analyst actually does", """A QA Analyst does far more than 'click around and find bugs'. A typical week includes:

- Reading requirements and user stories, then asking the awkward questions nobody else asked.
- Designing **test cases** that cover normal use, edge cases, and failure paths.
- Executing tests by hand and with automated scripts, and recording the results.
- Writing **defect reports** clear enough that a developer can reproduce and fix the problem.
- Retesting fixes, running **regression suites**, and reporting on quality and risk.
- Improving the process: better test data, better environments, better automation.

The output of QA is not 'bugs found'. It is **confidence**: a reasoned, evidence-backed answer to *'is this safe to release?'*"""),
                 ("Where QA sits in the team", table(
                     ["Role", "What they own", "How you work with them"],
                     [["Product Owner / BA", "What to build and why", "You clarify acceptance criteria and edge cases"],
                      ["Developers", "How it is built", "You report defects, reproduce issues, verify fixes"],
                      ["QA Analyst (you)", "Whether it works as intended", "You design and run tests, report risk"],
                      ["SDET / Automation Engineer", "Test frameworks and tooling", "You may grow into this role later"],
                      ["DevOps / Release", "Builds, environments, deployments", "You get stable builds to test against"],
                      ["Support / Service Desk", "Real user problems after release", "Your old team — a goldmine of real defect scenarios"]])),
                 ("Titles, levels and pay", """Job titles to search for: *QA Analyst, Software Test Analyst, Manual QA Tester, Quality Assurance Engineer, Functional Tester, Test Engineer, QA Specialist, UAT Analyst*. The ladder usually runs **Junior QA → QA Analyst → Senior QA → QA Lead / QA Manager** on one track, and **SDET / Test Automation Engineer / Quality Engineer** on the coding-heavy track.

A first QA role is one of the most realistic career changes from the service desk, because the core skill — *methodical investigation and clear documentation of problems* — is identical. The main gaps are testing vocabulary, test-design technique, and light technical skills, all of which this app teaches from zero."""),
               ],
               desk="You already investigate symptoms, reproduce issues, gather logs, escalate with evidence, and write ticket notes that someone else can act on. That is roughly 60% of a QA Analyst's day. You are not starting from nothing — you are re-labelling and extending skills you use every shift.",
               takeaway="QA = evidence-based confidence about a release. Your investigation and documentation skills already transfer.",
               ex=[
                   mcq("What is the primary *output* of a QA Analyst's work?", [
                       "A list of bugs found", "Automated scripts", "Evidence-backed confidence about release risk", "The software itself"], 2,
                       "Finding bugs is an activity, not the deliverable. The deliverable is a reasoned judgement about quality and risk."),
                   mcq("Which of these is NOT typically a QA Analyst responsibility?", [
                       "Reviewing acceptance criteria", "Writing a defect report", "Deciding which features the business builds next", "Retesting a fixed defect"], 2,
                       "Prioritising the product backlog belongs to the Product Owner, though QA advises on risk."),
                   inp("What is the coding-heavy sibling role to QA Analyst that many testers grow into? (4 letters)", ["SDET"], "Software Development Engineer in Test.", hint="It stands for Software Development Engineer in Test."),
               ]),

        lesson("orient-02", "Your service desk superpowers", 12,
               "Career changers often undersell themselves. This lesson translates what you already do on the desk into the exact language hiring managers use for QA roles — and identifies the small number of genuine gaps you need to close.",
               [
                 ("A translation table", table(
                     ["Service desk skill", "QA equivalent", "How to say it on a resume"],
                     [["Reproducing a user's issue", "Reproducing a defect with exact steps", "'Reproduced and isolated defects using minimal deterministic steps'"],
                      ["Reading logs and error messages", "Gathering evidence / root-cause analysis", "'Analysed application logs to isolate failure conditions'"],
                      ["Ticket documentation", "Defect reports and test evidence", "'Authored clear, actionable defect reports with severity and evidence'"],
                      ["Priority / SLA triage (P1-P4)", "Severity vs priority assessment", "'Triaged defects by severity and business impact'"],
                      ["Escalation to L2/L3", "Cross-team defect triage", "'Partnered with engineering to resolve and verify fixes'"],
                      ["Knowledge base articles", "Test documentation / test cases", "'Maintained reusable documentation of expected behaviour'"],
                      ["SQL queries against a support DB", "Back-end data verification", "'Validated data integrity with SQL'"],
                      ["Following ITIL change/incident process", "STLC / defect workflow / release process", "'Worked within structured change and release processes'"]])),
                 ("The honest gaps", """Be realistic about what you must actually learn, so you can plan:

1. **Testing vocabulary and theory** — levels, types, the 7 principles, STLC, ISTQB terms.
2. **Test design techniques** — equivalence partitioning, boundary value analysis, decision tables. Interviewers ask these directly.
3. **Test artefacts** — test cases, test plans, traceability matrices, bug reports in a standard format.
4. **Light technical skills** — HTTP, SQL, DevTools, JSON, a scripting language. Not 'become a developer', but enough to test below the UI.
5. **One automation tool** — even basic Playwright or Postman automation makes you far more hireable.
6. **A portfolio** — because you have no QA job history yet, you need artefacts that prove skill."""),
                 ("How to talk about the switch", """Never frame it as 'I want to escape the helpdesk'. Frame it as a direction of travel: *'I've spent years being the last line of defence for users, finding and documenting problems. I want to move upstream and prevent those problems before release, and I've built the testing skills to do it.'* That single sentence is your cover letter, your LinkedIn headline, and your interview opener."""),
               ],
               desk="Bring real (anonymised) examples: a time you found a pattern across several tickets, a time your documentation stopped a repeat incident, a time you pushed back with evidence. These become STAR stories later in the Career section.",
               takeaway="You are a career changer with directly relevant experience, not a beginner with none. Re-label, then fill the six gaps.",
               ex=[
                   mcq("The best way to frame a service-desk-to-QA move in an interview is:", [
                       "'I want to get away from users and tickets'", "'I want to move upstream and prevent problems before release'", "'QA is easier than support'", "'I have no relevant experience but I'll learn'"], 1,
                       "Frame it as a natural progression of investigative skill, not an escape."),
                   order("Put the typical escalation path for a defect in order:", [
                       "Reproduce the issue with minimal steps", "Write a defect report with evidence and severity", "Triage with the team and assign to a developer", "Developer fixes it", "QA retests and runs regression"], explain="This is the shape of the defect lifecycle you'll learn in detail later."),
                   mcq("Which of these is a genuine skill gap you must close, rather than a re-labelled existing skill?", [
                       "Writing clear documentation", "Investigating symptoms", "Test design techniques like boundary value analysis", "Triaging by impact"], 2,
                       "Most of your skills transfer; formal test design technique is new knowledge."),
               ]),

        lesson("orient-03", "How this app works (and how to study)", 8,
               "QAReady is a 24-week, part-time roadmap (about 8-10 hours a week). This lesson explains the structure of the app and a study rhythm that actually survives a working week.",
               [
                 ("The structure", """Everything is organised as **Phase → Course → Lesson → Exercise**.

- **Roadmap** — the 24-week plan, with a weekly focus, deliverable and checkpoint.
- **Courses** — 20 courses from absolute basics to job hunting. Each has 4-7 short lessons.
- **Lessons** — a 5-15 minute read followed by 2-3 interactive exercises. Exercises are checked instantly and saved on this device.
- **Quizzes** — one per course; take them to prove you retained the material.
- **Glossary / Flashcards** — ~90 QA terms; drill them until the vocabulary is automatic.
- **Toolkit** — curated free and paid courses, tools, books and practice sites.
- **Portfolio** — five projects with checklists, so you finish with evidence of skill.
- **Career** — resume rewrite, 40+ interview questions, and the first 90 days.
- **Plans** — two long-form documents: the week-by-week schedule and the full career guide.

Progress is saved in your browser, works offline, and you can export it as a JSON file from Settings."""),
                 ("A study week that survives shift work", """For each week: **2 short sessions + 1 longer session + 1 ship**.

| Day | Session | What you do |
|---|---|---|
| Mon/Tue (30-45 min) | Learn | Read one lesson, do its exercises |
| Wed/Thu (30-45 min) | Learn + drill | Read the next lesson, drill 10 glossary cards |
| Sat (2-3 h) | Build | Work on that week's portfolio deliverable |
| Sun (30 min) | Checkpoint | Take the course quiz, write 5 lines in your study journal |

The rule: **ship something every week** — a file, a repo, a test case, a bug report. If a week slips, drop the stretch reading, never the deliverable. Skills without an artefact don't count in interviews."""),
                 ("Set up once, before Week 2", """1. Create a **GitHub** account and a folder for your learning repos.
2. Install **VS Code**, **Git**, and **Node.js** (LTS). You will not need them until Week 7, but having them ready removes friction.
3. Start a `journal.md`: one paragraph per study day — what you did, what confused you, what you'll revisit.
4. Pick a **note system** (this app's per-lesson notes, or your own file). Write definitions in your own words; copying is not learning.
5. Book a recurring calendar block. Treat it like a shift you cannot swap."""),
               ],
               desk="You already work to SLAs and rotas — treat your study plan like a rota. Consistency beats intensity: 45 minutes four times a week beats one exhausted 6-hour Sunday.",
               takeaway="Short reads, instant exercises, one shipped artefact per week. Export your progress occasionally.",
               ex=[
                   mcq("What is the recommended weekly rhythm?", [
                       "One 8-hour session on Sunday", "Two short learn sessions, one build session, one checkpoint", "Read everything first, practise at the end", "Only watch video courses"], 1,
                       "Distributed practice plus a weekly shipped artefact is the pattern."),
                   inp("Which key in Settings lets you keep your progress safe across devices?", ["Export", "Export progress", "Export JSON", "export"], "Download the JSON and import it on another device."),
                   mcq("If a week slips behind, what should you drop?", [
                       "The deliverable", "The checkpoint quiz", "The stretch / extra reading", "The whole week and start over"], 2,
                       "Protect the shipped artefact; drop optional extras."),
               ]),

        lesson("orient-04", "The 24-week plan at a glance", 10,
               "Here is the whole journey in one view: seven phases, from zero knowledge to a job application. Knowing the shape of the path stops the middle weeks feeling aimless.",
               [
                 ("The seven phases", table(
                     ["Phase", "Weeks", "Theme", "What you can do at the end"],
                     [["0 · Start here", "1", "Orientation & mindset", "Explain the QA role, your transferable skills, your study plan"],
                      ["1 · Manual QA craft", "2-6", "Testing fundamentals, test design, docs, defects, tools", "Write test cases, a test plan, and professional bug reports"],
                      ["2 · Technical foundations", "7-11", "Web, SQL, CLI/Git, JavaScript", "Test below the UI, query the DB, read code, use DevTools"],
                      ["3 · API testing", "12-14", "REST, Postman, auth, assertions", "Design and automate API tests"],
                      ["4 · Automation", "15-20", "Strategy, Playwright, CI/CD", "Build and run a maintainable automated suite in a pipeline"],
                      ["5 · Beyond functional", "21-22", "Performance, accessibility, security, compatibility", "Cover non-functional risks"],
                      ["6 · Get hired", "23-24", "ISTQB, portfolio, interviews, job search", "Apply with a portfolio and pass a QA interview"]])),
                 ("Why manual first, automation second", """It is tempting to jump straight to Selenium because it sounds more 'technical'. Resist it. Automation is *coding a check for behaviour you already understand*. If you cannot design a good test case by hand, your automated test will simply assert the wrong thing very quickly. Every hiring manager for a first QA role cares more about your test thinking than your framework syntax.

The plan deliberately makes you fluent in manual test design first, adds technical depth (so you can test APIs and data), then automates the checks you already know how to write."""),
                 ("Milestones to look forward to", """- **End of Week 6:** a full test suite (test plan + 25 test cases + 5 defect reports) for a real public app.
- **End of Week 11:** a SQL cheat sheet and a GitHub repo with your first scripts.
- **End of Week 14:** a public Postman collection with automated assertions.
- **End of Week 20:** a Playwright framework running in GitHub Actions with an HTML report.
- **End of Week 24:** a tailored resume, polished LinkedIn/GitHub, and 20+ targeted applications sent.

Each milestone is a **portfolio artefact** — the thing that replaces 'years of QA experience' on your resume."""),
               ],
               desk="Your incident-management instinct already tells you to check for regressions after a fix. That instinct is the seed of the whole plan: make it formal, add evidence, then automate it.",
               takeaway="Manual thinking → technical depth → automation → proof of skill → job search. Every phase ships an artefact.",
               ex=[
                   order("Put the seven phases in the order you'll study them:", [
                       "Orientation & mindset", "Manual QA craft", "Technical foundations", "API testing", "Test automation & CI/CD", "Non-functional testing", "Certification, portfolio & job search"]),
                   mcq("Why does the plan teach manual testing before automation?", [
                       "Automation tools are too expensive", "You must understand what to check before you can code a reliable check of it", "Manual QA jobs pay more", "Automation is being phased out"], 1,
                       "Automation encodes test thinking; it doesn't replace it."),
                   inp("How many weeks is the full roadmap?", ["24", "twenty-four"], hint="Six months, part-time."),
               ]),
    ],
    quiz="orientation-quiz",
)

# ---------------------------------------------------------------------------
# 2. Foundations
# ---------------------------------------------------------------------------
FOUNDATIONS = course(
    "foundations", "Software & Testing Foundations", "The theory behind everything else",
    "SDLC and STLC, Agile and Scrum, the seven testing principles, test levels and types, verification vs validation, and the vocabulary every QA interview assumes.",
    "#4f8cff", "p0", "Week 1-2", "Beginner",
    [
        lesson("found-01", "How software gets built: the SDLC", 12,
               "Before you can test a product you need a mental map of how it comes into existence. The **Software Development Life Cycle (SDLC)** is that map — and QA has a seat at every stage now, not just at the end.",
               [
                 ("The classic stages", """| Stage | What happens | QA involvement |
|---|---|---|
| Requirements | Decide what to build | Review for ambiguity, testability, missing edge cases |
| Design | Architecture, UI, data model | Review designs, identify risk areas |
| Implementation | Developers write code | Write test cases, unit-test support, static reviews |
| Testing | Execute tests, log defects | Your main stage: execute, report, retest |
| Deployment | Release to users | Smoke test in production, verify release notes |
| Maintenance | Fix, enhance, support | Regression testing, analyse escaped defects |

In old **Waterfall** projects these stages are sequential and QA only appears in the 'Testing' box. That is exactly why bugs were found late and cost a fortune. Modern teams do QA continuously."""),
                 ("Waterfall, V-Model and iterative", """- **Waterfall:** linear, document-heavy, each phase signed off. Testing is a late, separate phase. Still common in regulated industries (health, finance, government).
- **V-Model:** the important idea — *every development stage has a matching test stage*. Requirements ↔ Acceptance testing, Design ↔ System testing, Code ↔ Unit testing. It makes 'test early' explicit.
- **Iterative / Agile:** build in small increments (1-4 week sprints), test each increment, get feedback, adjust. This is what most job ads mean by 'Agile environment'.

> **From the desk:** a V-Model diagram looks a lot like an incident → problem → change → release process. You already think in linked, traceable stages."""),
                 ("Shift-left, and why it matters to you", """**Shift-left** means moving testing activities earlier (left) in the timeline: reviewing requirements, joining design discussions, writing tests before code exists. Finding an ambiguous requirement during a backlog refinement costs minutes. Finding it after release costs a hotfix, a support queue, and customer trust — a cost you have seen first-hand.

As a QA Analyst you will be asked 'how do you shift left?' A strong answer: *'I review acceptance criteria before development starts, ask for concrete examples of edge cases, and write test charters early so developers know what I'll check.'*"""),
               ],
               desk="Your queue of repeat incidents is 'shift-right' evidence. In interviews, say you want to move upstream to stop those tickets existing — that is shift-left in language a hiring manager loves.",
               takeaway="SDLC stages all have a QA activity. V-Model pairs each build stage with a test stage. Shift-left = test earlier, cheaper.",
               ex=[
                   mcq("In the V-Model, which test stage pairs with the Requirements stage?", [
                       "Unit testing", "Integration testing", "Acceptance testing", "Regression testing"], 2,
                       "Requirements ↔ Acceptance; Design ↔ System; Code ↔ Unit."),
                   mcq("What does 'shift-left' mean?", [
                       "Move testers to a different team", "Move testing activities earlier in the lifecycle", "Test only on the left-hand side of the UI", "Release on Fridays"], 1,
                       "Earlier involvement = cheaper defects."),
                   order("Put the classic SDLC stages in order:", [
                       "Requirements", "Design", "Implementation", "Testing", "Deployment", "Maintenance"]),
               ]),

        lesson("found-02", "Agile, Scrum and the tester's calendar", 12,
               "Most QA jobs are in Agile teams. This lesson covers the ceremonies, the artefacts, and — crucially — where a tester adds value in each, using plain language rather than certification jargon.",
               [
                 ("Agile in one paragraph", """Agile is a mindset: deliver small, working increments frequently, inspect and adapt, collaborate closely with the business. **Scrum** is the most common framework for doing it. Work is planned in fixed-length **sprints** (usually 2 weeks), pulled from a prioritised **product backlog**, and the team commits to a **sprint backlog**. The goal of each sprint is a potentially shippable increment."""),
                 ("The ceremonies and your role", table(
                     ["Ceremony", "When", "What QA does"],
                     [["Backlog refinement / grooming", "Mid-sprint", "Ask 'how will we test this?', demand acceptance criteria and edge-case examples, split stories"],
                      ["Sprint planning", "Start of sprint", "Estimate testing effort, flag test-data / environment needs, add testing tasks"],
                      ["Daily stand-up", "Every day", "Report progress, raise blockers ('I'm blocked: staging DB is down')"],
                      ["Sprint review / demo", "End of sprint", "Demo tested behaviour, be honest about known defects and coverage gaps"],
                      ["Retrospective", "End of sprint", "Suggest process improvements ('devs and QA pair on bug reproduction')"],
                      ["Three Amigos", "Before a story is built", "BA + Dev + QA agree on examples and expected behaviour"]])),
                 ("Stories, acceptance criteria and Definition of Done", """A **user story** is a short promise: *'As a customer, I want to reset my password so I can regain access.'* **Acceptance criteria (AC)** are the concrete conditions that make it true:

```
- Given a registered email, when I request a reset, then an email arrives within 2 minutes.
- Given an unregistered email, when I request a reset, then no account is revealed.
- A reset link expires after 30 minutes and can be used only once.
```

Notice the **Given / When / Then** format — that is Gherkin, and each line is basically a test case. The **Definition of Done (DoD)** is the team-wide checklist for *any* story: code reviewed, unit tests pass, AC verified, no open critical defects, documentation updated, deployed to staging. QA owns the quality parts of the DoD.

> **Key insight:** if a story has no acceptance criteria, it has no definition of correct — so it cannot be tested. Your most valuable sentence in refinement is *'What should happen when...?'*"""),
               ],
               desk="Stand-ups, shift handovers, and incident bridges are the same muscle: short, factual status plus blockers. The only new habit is translating 'what should happen when...' into acceptance criteria.",
               takeaway="QA joins every ceremony. Acceptance criteria are your test cases in disguise; the DoD is your quality gate.",
               ex=[
                   mcq("Which ceremony is specifically for BA + Developer + QA to agree on examples before coding?", [
                       "Sprint review", "Retrospective", "Three Amigos", "Daily stand-up"], 2,
                       "Three Amigos (also called a story kick-off) aligns understanding early."),
                   mcq("A user story arrives with no acceptance criteria. What is the tester's best first move?", [
                       "Write test cases anyway using guesswork", "Ask for concrete examples of expected behaviour before development starts", "Log a defect immediately", "Wait until the code exists and explore"], 1,
                       "Untestable requirements are a requirements problem, not a testing problem."),
                   inp("In Gherkin, what keyword starts the line that describes the trigger/action? (4 letters)", ["When"], "'Given' sets context, 'When' is the action, 'Then' is the outcome."),
                   mdex("Write one Given/When/Then acceptance criterion for a login lockout after 5 failed attempts.",
                        [P(r"Given", "a Given line"), P(r"When", "a When line"), P(r"Then", "a Then line"), P(r"5|five", "the number five")],
                        "Given a registered user with 4 failed login attempts\nWhen they enter a wrong password a 5th time\nThen the account is locked for 15 minutes and a lockout email is sent",
                        starter="Given a registered user...\nWhen ...\nThen ...",
                        explain="Concrete, testable, and includes the boundary."),
               ]),

        lesson("found-03", "STLC: the tester's own lifecycle", 12,
               "Just as development has an SDLC, testing has the **Software Test Life Cycle (STLC)** — six phases with named entry criteria, activities and deliverables. Interviewers love this question, and it is the backbone of how a QA Analyst organises a release.",
               [
                 ("The six phases", table(
                     ["#", "Phase", "Key activity", "Deliverable"],
                     [["1", "Requirement analysis", "Review AC, ask questions, identify what is testable, define test basis", "Requirement Traceability Matrix (RTM) skeleton, query log"],
                      ["2", "Test planning", "Decide scope, approach, resources, schedule, risks, tools", "Test Plan / Test Strategy"],
                      ["3", "Test case development", "Design test cases and test data, review them", "Test cases, test scripts, test data"],
                      ["4", "Test environment setup", "Get builds, environments, accounts, data, access", "Smoke-test result confirming the environment works"],
                      ["5", "Test execution", "Run tests, log results, report defects, retest fixes", "Test execution report, defect reports"],
                      ["6", "Test cycle closure", "Check exit criteria, summarise coverage and residual risk, lessons learned", "Test summary report / sign-off"]])),
                 ("Entry and exit criteria", """A phase should not begin until its **entry criteria** are met, and the whole cycle should not close until its **exit criteria** are met. Examples:

- *Entry to execution:* the build is deployed to staging, smoke tests pass, test data is loaded, and the defect tracker is available.
- *Exit / release:* all planned high-priority tests executed, ≥95% pass rate, zero open critical/major defects, and any deferred defects are documented and accepted by the Product Owner.

Without these, 'are we done?' becomes an opinion. With them, it is a measured decision. **Never confuse 'all tests passed' with 'no bugs exist'** — it means no bugs were found *by the tests we designed*."""),
                 ("Test basis and traceability", """The **test basis** is everything you test against: requirements, user stories, designs, API specs, regulatory rules, even old support tickets. A **traceability matrix** links each requirement to the test case(s) that cover it, so you can prove coverage and see instantly what a changed requirement affects.

```
REQ-12 (password reset)  ->  TC-031 valid reset, TC-032 unknown email,
                              TC-033 expired link, TC-034 single-use link
```

> **From the desk:** this is change/incident traceability applied to tests. You already know why an auditor asks 'show me the record'."""),
               ],
               desk="When a release goes out with a known issue, you already write a 'known issues / workaround' note. That's a cut-down test summary report — you're halfway to phase 6.",
               takeaway="STLC = analyse → plan → design → setup → execute → close. Entry/exit criteria turn opinions into decisions.",
               ex=[
                   order("Put the six STLC phases in order:", [
                       "Requirement analysis", "Test planning", "Test case development", "Test environment setup", "Test execution", "Test cycle closure"]),
                   mcq("What is a 'test basis'?", [
                       "The server tests run on", "The documents and specifications you derive tests from", "The total number of test cases", "The budget for testing"], 1,
                       "Requirements, designs, specs, regulations, user stories — the source of truth."),
                   mcq("Which is a sensible exit criterion for a release?", [
                       "All developers say it looks fine", "Zero open critical/major defects and planned high-priority tests executed", "The sprint ended", "No tests failed, so there are no bugs"], 1,
                       "It is measurable, and it doesn't claim the impossible ('no bugs')."),
                   mcq("'All our tests passed' means:", [
                       "The software is bug-free", "No defects were found by the tests we designed", "Testing is complete forever", "The test plan was wrong"], 1,
                       "Coverage is always limited by the quality of your test design — a favourite interview trap."),
               ]),

        lesson("found-04", "The seven testing principles", 12,
               "The ISTQB defines seven principles that underpin the whole discipline. They are examined directly, quoted constantly, and — more usefully — they explain why some testing habits are a waste of time.",
               [
                 ("The seven, with the reasoning", """1. **Testing shows the presence of defects, not their absence.** Testing can prove something is broken; it can never prove nothing is broken. This is why 'all tests passed' is not 'no bugs'.
2. **Exhaustive testing is impossible.** A form with 10 fields and 10 values each has 10 billion combinations. You must sample intelligently using risk and test design techniques (next course).
3. **Early testing saves time and money.** A requirement ambiguity fixed in refinement costs minutes; the same misunderstanding after release costs a hotfix and a support queue.
4. **Defects cluster together.** A small number of modules usually contain most defects (the Pareto 80/20 rule). History, complexity and churn tell you where to look hardest — and your old incident queue is exactly that history.
5. **Beware the pesticide paradox.** If you run the same tests repeatedly, they stop finding new bugs, just as pests develop resistance. Review and refresh tests, add new scenarios, rotate exploratory charters.
6. **Testing is context dependent.** Testing a medical device, a mobile game and a payroll API are different jobs with different rigour, evidence and regulation.
7. **Absence-of-errors is a fallacy.** A system with zero defects can still be a failure if it is unusable, slow, inaccessible, or simply not what the customer asked for. Quality is fitness for purpose, not just correctness."""),
                 ("Applying them, not memorising them", """| Principle | Practical consequence for you |
|---|---|
| Defects cluster | Spend extra time on recently changed, complex, historically buggy modules |
| Pesticide paradox | Add 2-3 new exploratory charters each sprint; retire stale cases |
| Exhaustive is impossible | Use equivalence partitioning + boundary values + risk to choose samples |
| Early testing | Ask for acceptance criteria *before* code exists |
| Context | Ask 'what is the worst thing that could go wrong here?' to set rigour |
| Absence-of-errors | Include usability, accessibility and performance checks, not just functional ones |"""),
               ],
               desk="Principle 4 is your superpower: you know which modules generate the most tickets. Bring that instinct into test planning as 'risk-based prioritisation' and you'll sound like a senior tester.",
               takeaway="Testing reduces risk and finds defects; it never proves perfection. Design intelligently, refresh tests, test early, mind the context.",
               ex=[
                   mcq("Which principle explains why repeating the exact same test suite eventually stops finding new bugs?", [
                       "Defects cluster", "Pesticide paradox", "Early testing", "Absence-of-errors fallacy"], 1,
                       "Tests need reviewing and refreshing, like rotating crops or pesticides."),
                   mcq("'Testing shows the presence of defects, not their absence' means:", [
                       "Testing is pointless", "Passing tests cannot prove the software is defect-free", "All tests must fail", "Only developers can find bugs"], 1),
                   mcq("A flawless, bug-free app that nobody can figure out how to use violates which principle?", [
                       "Exhaustive testing is impossible", "Early testing", "Absence-of-errors is a fallacy", "Defects cluster"], 2,
                       "Correctness is not the whole of quality; fitness for purpose matters."),
                   inp("Which principle says roughly 80% of defects are often found in 20% of modules?", ["Defects cluster together", "Defect clustering", "Defects cluster"], hint="Think of the Pareto principle."),
               ]),

        lesson("found-05", "Test levels and test types", 14,
               "'Levels' and 'types' are not the same thing, and mixing them up is a classic junior interview mistake. Levels describe *when / at what scope* you test; types describe *what attribute* you are checking.",
               [
                 ("The four test levels", """| Level | Scope | Usually done by | Example |
|---|---|---|---|
| **Unit / component** | A single function or class in isolation | Developer | `calculateDiscount(100, 10)` returns 90 |
| **Integration** | Two or more components talking | Dev + QA | Cart service calls pricing API and stores the total |
| **System** | The whole integrated application, end to end | **QA Analyst (you)** | Log in → add item → apply coupon → pay → receive email |
| **Acceptance** | Does it meet business need? | Customer / PO / UAT users | Business signs off on the new refund workflow |

There is also **regression testing** (re-running existing tests after a change) which is an *activity across levels*, not a level itself. And a **smoke test** — a tiny subset that answers 'is this build even testable?' — run before every deep test cycle."""),
                 ("Functional vs non-functional", """- **Functional testing** asks *does it do the right thing?* Based on requirements: login works, totals are correct, the report exports.
- **Non-functional testing** asks *how well does it do it?* Performance, security, accessibility, usability, reliability, compatibility, localisation. Covered in Phase 5.

Other important distinctions:

| Pair | Difference |
|---|---|
| **Verification vs Validation** | Verification: *are we building the product right?* (reviews, static checks, docs). Validation: *are we building the right product?* (executing the software against real needs) |
| **Static vs Dynamic** | Static: no code runs (reviews, walkthroughs, linting). Dynamic: code executes (actually running tests) |
| **Black-box vs White-box** | Black-box: no knowledge of internals, based on specs. White-box: based on code structure and branches |
| **Positive vs Negative** | Positive: valid input, expected success. Negative: invalid input, graceful failure |
| **Retesting vs Regression** | Retest: re-run the *failed* case after a fix. Regression: re-run *other* cases to catch side effects |"""),
                 ("Worked example: a password reset", """A single feature fans out across levels and types:

- *Unit:* does `hashToken()` produce a 64-char hash?
- *Integration:* does the mail service receive the token the API generated?
- *System/functional:* does a user complete a reset end to end in the browser?
- *Negative:* expired link, reused link, unknown email, malformed token.
- *Security (non-functional):* does the response reveal whether an email is registered?
- *Usability:* is the 'check your inbox' message clear?
- *Regression:* does normal login still work after the reset feature shipped?

> **From the desk:** 'is this a user problem, an app problem, or a data problem?' is exactly the level/thinking split, just with different labels."""),
               ],
               desk="Your instinct to isolate where a failure lives (client? network? server? DB?) is integration-level thinking. Naming it makes it interview-ready.",
               takeaway="Levels = scope/timing (unit→integration→system→acceptance). Types = attribute (functional, non-functional, static/dynamic, etc.).",
               ex=[
                   mcq("Which level is a QA Analyst most associated with executing end to end?", [
                       "Unit", "Integration", "System", "Compiler"], 2),
                   mcq("Checking that a 500-user load does not slow checkout below 2s is what kind of testing?", [
                       "Functional", "Non-functional (performance)", "Unit", "Static"], 1),
                   mcq("Re-running the test that failed to confirm the fix is:", [
                       "Regression testing", "Smoke testing", "Retesting", "Exploratory testing"], 2,
                       "Regression re-runs *other* cases to detect side effects of the fix."),
                   mcq("Reading a requirements document and finding an ambiguity, without running any code, is:", [
                       "Dynamic validation", "Static verification", "System testing", "White-box testing"], 1,
                       "Static = nothing executes; verification = are we building it right."),
                   inp("What short test answers 'is this build stable enough to bother testing?' (5 letters)", ["Smoke", "smoke test"], hint="Named after hardware engineers powering on a board and watching for..."),
               ]),

        lesson("found-06", "The vocabulary you must own", 12,
               "QA has a precise vocabulary, and interviewers use it as a filter. This lesson is a fast tour of the terms you will meet constantly; the Glossary and Flashcards sections let you drill all of them until they are automatic.",
               [
                 ("Core nouns", """| Term | Meaning |
|---|---|
| **Test basis** | The source you derive tests from (requirements, specs, stories) |
| **Test condition** | A single item or event you could verify ('invalid password is rejected') |
| **Test case** | Preconditions + input steps + expected result for one condition |
| **Test procedure / script** | The ordered sequence of steps to run a test case |
| **Test suite** | A collection of test cases grouped for one run |
| **Test data** | The values and records used during execution |
| **Test environment** | The configured hardware/software/data/accounts tests run against |
| **Test oracle** | How you decide whether the actual result is correct (spec, a reference system, a calculation, an expert) |
| **Defect / bug / fault** | A flaw in the software; a *failure* is what the user sees when a fault executes |
| **Error / mistake** | The human action that introduced the fault |
| **Coverage** | The degree to which the test basis has been exercised, expressed as a percentage |
| **Traceability** | The link from requirement → test → defect |
| **Risk** | The possibility of a negative outcome, usually rated likelihood × impact |
| **Severity / Priority** | Technical impact / order of fixing (covered in depth in the Defects course) |"""),
                 ("Fault vs failure vs error — exam favourite", """A developer makes an **error** (mistake) and writes `if (age >= 18)` where the rule was `> 18`. That creates a **fault** (defect) in the code. When a 18-year-old signs up and is wrongly allowed, the system exhibits a **failure**. Testing observes failures; debugging finds faults; process improvement prevents errors.

Not every fault causes a failure (the faulty line may never execute), and not every failure means a fault (a user may have misused the system — something you know well from the desk)."""),
                 ("Two phrases that sound senior", """- *'What is the test oracle here?'* — i.e. how will we know the result is right? For a report you might compare against a SQL query; for a calculation, a spreadsheet; for a migration, a row-count and checksum.
- *'What is the residual risk?'* — the risk you knowingly accept at release (deferred minor defects, untested low-risk browsers, a 3rd-party sandbox you couldn't test). Naming residual risk is what separates a sign-off from a shrug."""),
               ],
               desk="'User says it's broken' vs 'reproducible fault in module X' is a distinction you already make between a ticket and a known error record. Same idea, new nouns.",
               takeaway="Learn the nouns precisely; fault ≠ failure ≠ error. Ask 'what's the oracle?' and 'what's the residual risk?'",
               ex=[
                   mcq("A developer's typo that introduces a wrong condition in the code is a(n):", [
                       "Failure", "Error", "Fault", "Incident"], 1,
                       "Error = human mistake; fault = the resulting defect in code; failure = the observable wrong behaviour."),
                   mcq("What is a 'test oracle'?", [
                       "The test management tool", "The mechanism or source used to decide if the actual result is correct", "The senior tester", "The database server"], 1),
                   inp("What do we call the risk we knowingly accept when we sign off a release?", ["Residual risk", "residual risk"], hint="'Residual' = what's left over."),
                   order("Put the chain of causation in order:", [
                       "Human error / mistake", "Fault (defect) introduced in code", "Fault executes", "Failure observed by the user"]),
               ]),
    ],
    quiz="foundations-quiz",
)

# ---------------------------------------------------------------------------
# 3. Test design
# ---------------------------------------------------------------------------
TEST_DESIGN = course(
    "test-design", "Test Design Techniques", "Choose the few tests that matter",
    "You cannot test everything. Learn black-box techniques — equivalence partitioning, boundary value analysis, decision tables, state transitions, use-case and exploratory testing — with fully worked examples.",
    "#3ddc84", "p1", "Weeks 2-3", "Core",
    [
        lesson("design-01", "Why we need technique (black vs white box)", 10,
               "Exhaustive testing is impossible, so the whole craft of QA is **choosing a small set of tests that find the most defects**. Test design techniques are the systematic way to make that choice defensible rather than guesswork.",
               [
                 ("The size of the problem", """Consider a simple field: *age*, with values 0-120, and a *country* dropdown with 20 options, plus a *promo code* text field. Even ignoring the free-text field, that's 121 × 20 = 2,420 combinations. Add 5 checkbox options and you are past 77,000. Now add browser, user role, and data state. You cannot test all of it.

Techniques reduce this without losing coverage: **equivalence partitioning** cuts the age field to 3-4 representative values; **boundary value analysis** adds the edges where bugs hide; **decision tables** handle the checkbox rules; **pairwise** covers combinations efficiently."""),
                 ("Black-box, white-box, experience-based", """| Approach | Basis | Examples |
|---|---|---|
| **Black-box (specification-based)** | Requirements and behaviour, no code knowledge | Equivalence partitioning, boundary values, decision tables, state transition, use case |
| **White-box (structure-based)** | Code structure, branches, paths | Statement coverage, branch/decision coverage, path testing |
| **Experience-based** | Tester knowledge, intuition, similar systems | Exploratory testing, error guessing, checklists, attack patterns |

As a manual QA Analyst you will mostly use black-box and experience-based techniques. White-box is mainly developers and SDETs, but you should understand *coverage* when talking to them. **Error guessing** — 'what has broken here before?' — is where service desk experience beats any textbook."""),
                 ("Coverage is a measure, not a goal", """When someone says 'we have 90% coverage', ask *of what?* Requirements coverage (every AC has a test), code coverage (every line executed), risk coverage (every high risk has a test), or platform coverage (every supported browser)? A suite can execute 90% of lines and still miss a critical business rule that was never coded. Coverage tells you what you have *not* tested, not that you have tested well."""),
               ],
               desk="You never checked every possible cause of a ticket — you pattern-matched to the likely ones. That's error guessing, a recognised technique. Now give it a name and a structure.",
               takeaway="Technique turns 'I clicked around' into a defensible, minimal, high-yield test set.",
               ex=[
                   mcq("Equivalence partitioning and boundary value analysis are what kind of techniques?", [
                       "White-box", "Black-box / specification-based", "Experience-based", "Performance"], 1),
                   mcq("Which approach relies most on the tester's knowledge of similar systems and past failures?", [
                       "Statement coverage", "Experience-based (error guessing / exploratory)", "Boundary value analysis", "Decision table testing"], 1),
                   mcq("'We have 90% coverage' is incomplete without saying:", [
                       "Who ran the tests", "Which browser was used", "Coverage of *what* — requirements, code, risk, or platform", "How long it took"], 2),
               ]),

        lesson("design-02", "Equivalence partitioning, worked", 12,
               "**Equivalence partitioning (EP)** divides input data into classes where the system should behave the same way for every member. Test one value from each class instead of every value. It is the single most examined technique.",
               [
                 ("The rule", """1. Identify the input condition (a field, parameter, or state).
2. Divide its possible values into **partitions** (classes) that you expect to be treated identically:
   - one **valid** class for values that should be accepted,
   - one or more **invalid** classes for values that should be rejected,
   - plus classes for special states (empty, null, out of range, wrong type).
3. Pick **one representative value** from each class.

The assumption: if the system handles 17-year-olds one way and 35-year-olds another, testing one value from each class covers the whole class. If that assumption is wrong, you have found a defect."""),
                 ("Worked example: age field", """Rule: *Age must be an integer from 18 to 65 inclusive to open an account.*

| Partition | Type | Representative | Expected |
|---|---|---|---|
| < 18 | invalid | `17` | Reject, 'must be 18 or over' |
| 18-65 | valid | `35` (and we'll add edges in the next lesson) | Accept |
| > 65 | invalid | `66` | Reject, 'must be 65 or under' |
| non-numeric | invalid | `abc` | Validation error, no crash |
| empty / null | invalid | *(blank)* | 'Age is required' |
| decimal | invalid | `30.5` | Reject or truncate per spec |
| negative | invalid | `-1` | Reject |

Nine partitions → about 7-9 test cases instead of hundreds of values. Notice we deliberately include **invalid** classes: negative testing is where most real defects live."""),
                 ("Common mistakes", """- **Overlapping partitions** — e.g. '0-18' and '18-65' both contain 18. Classes must be disjoint.
- **Forgetting invalid classes** — testing only happy paths is the #1 junior mistake.
- **Assuming identical behaviour without evidence** — if the spec says 'silver members aged 60-65 get a different fee', that is a separate valid partition.
- **Ignoring non-input partitions** — output values, states (logged in / locked), and time ('within 30 days' vs 'older') also need partitioning."""),
               ],
               desk="When you triaged tickets you instinctively grouped 'same underlying problem'. EP is that grouping applied to input values before a single test runs.",
               takeaway="Valid + invalid + special-state classes; one representative each; keep classes disjoint; always test invalid.",
               ex=[
                   mcq("A field accepts values 1-100 inclusive. Which set of values represents correct equivalence classes (before boundary analysis)?", [
                       "1, 50, 100", "0, 50, 101", "0, 1, 50, 100, 101", "0, 1, 50, 101"], 1,
                       "One representative per class: below-range (invalid), in-range (valid), above-range (invalid). Edge values belong to boundary analysis."),
                   mcq("Which of these is NOT an equivalence partition for a 'quantity' field that must be 1-99?", [
                       "Values 1-99 (valid)", "Values below 1 (invalid)", "Values above 99 (invalid)", "Values that the developer forgot to handle"], 3,
                       "Classes come from the specification, not from speculation about implementation."),
                   inp("A password field requires 8-20 characters. How many *valid* equivalence classes are there for that length rule?", ["1", "one"], hint="All acceptable lengths should be treated identically — unless the spec says otherwise."),
                   mcq("Why do we include invalid partitions?", [
                       "To increase the test count", "Because negative/invalid handling is where many defects and crashes hide", "Because ISTQB requires exactly 3 invalid classes", "They are easier to automate"], 1),
               ]),

        lesson("design-03", "Boundary value analysis, worked", 12,
               "Defects cluster at the edges: off-by-one errors, `>` instead of `>=`, empty vs one item, exactly-at-limit. **Boundary Value Analysis (BVA)** is the systematic way to test those edges, and it pairs naturally with equivalence partitioning.",
               [
                 ("The rule", """For a range with a lower boundary **L** and upper boundary **U**, test:

- **L-1** (just below, invalid), **L** (at boundary, valid), **L+1** (just above, valid)
- **U-1** (just below, valid), **U** (at boundary, valid), **U+1** (just above, invalid)

That is the **3-point (full) BVA** style, giving 6 values. A leaner **2-point BVA** uses L, L+1, U-1, U (or just L-1, L, U, U+1). Both are acceptable; the ISTQB CTFL generally teaches the boundary and its immediate neighbours. The point is to test *at and around* each edge.

Also test the **'zero' boundaries**: empty list, empty string, 0 items, null, maximum-length string, first/last record, midnight, end of month, leap day."""),
                 ("Worked example: discount rule", """Rule: *Orders of $100.00-$500.00 inclusive get a 10% discount; below $100 none, above $500 a flat $60 cap.*

| Value | Why | Expected |
|---|---|---|
| 99.99 | L-1 | No discount |
| 100.00 | L | 10% = 10.00 |
| 100.01 | L+1 | 10% = 10.001 → rounding rule needed |
| 499.99 | U-1 | 10% = 49.999 → rounding |
| 500.00 | U | 10% = 50.00 |
| 500.01 | U+1 | Flat 60.00 |

Already the boundary table has surfaced an unasked question: **how are fractional cents rounded?** Boundary analysis doesn't just find code bugs — it finds *specification gaps*. Raise it in refinement rather than guessing."""),
                 ("Non-numeric boundaries", """- **Strings:** length 0, 1, max-1, max, max+1; leading/trailing spaces; unicode.
- **Lists:** 0 items, 1 item, full page (e.g. 20), 21 items (pagination off-by-one).
- **Dates:** 29 Feb on a leap year, 31 Dec → 1 Jan, timezone midnight, DST change.
- **Files:** 0 bytes, exactly the size limit, limit + 1 byte.
- **Counts:** max concurrent users, exactly the licence limit, limit + 1.

> **From the desk:** 'it only breaks when there are more than 20 items / at month end / for the first user of the day' — classic boundary defects you've seen in tickets. Now you'll catch them before release."""),
               ],
               desk="Boundary conditions are the 'it only happens at month-end' tickets. Formalising them means you proactively test the calendar edge instead of waiting for the incident.",
               takeaway="Test at and just around every edge. Boundary tables routinely reveal missing requirements, not just code bugs.",
               ex=[
                   mcq("A field accepts 1-10 inclusive. Which set is full 3-point boundary value analysis?", [
                       "1, 5, 10", "0, 1, 2, 9, 10, 11", "0, 1, 10, 11", "1, 2, 9, 10"], 1,
                       "L-1, L, L+1, U-1, U, U+1 → 0,1,2,9,10,11."),
                   mcq("Testing a 20-item-per-page list with 21 items is checking for:", [
                       "An equivalence class", "A pagination boundary / off-by-one defect", "A performance bottleneck", "A security flaw"], 1),
                   mcq("Boundary analysis on a discount rule revealed that fractional cents are unrounded. What should the tester do?", [
                       "Guess and write the test case", "Raise it as a specification gap / question before coding", "Skip that value", "Log it as a defect immediately"], 1,
                       "Missing requirements are requirements problems; get the oracle defined first."),
                   inp("For a password max length of 20, name one boundary value *above* the limit.", ["21", "twenty-one", "20+1"], hint="One past the maximum."),
               ]),

        lesson("design-04", "Decision tables for business rules", 13,
               "When behaviour depends on **combinations of conditions** (if this AND that, unless the other), prose requirements become ambiguous and test cases get missed. A decision table makes every combination explicit and countable.",
               [
                 ("The anatomy", """A decision table has four quadrants:

| Conditions \\ Rules | R1 | R2 | R3 | R4 |
|---|---|---|---|---|
| Valid login? | Y | Y | N | N |
| 2FA enabled? | Y | N | Y | N |
| **Actions** | | | | |
| Ask for OTP | X | | | |
| Grant access | | X | | |
| Show 'invalid credentials' | | | X | X |

Each column is a **rule** = one test case. With 2 binary conditions you get 4 rules. With 4 binary conditions, 16 — which is exactly why you need a table: without it you will silently forget six of them."""),
                 ("Worked example: e-commerce discount", """Business rules: *Premium members get 15% off. Orders over $100 get free shipping. Free shipping does not apply to express delivery.*

Conditions: `Premium?`, `Total > 100?`, `Express?` → 8 rules. Some are equivalent or impossible and can be collapsed (a **don't care** entry, shown as `—`): once Express is Y, free shipping is already excluded regardless of the others.

```
Rule:  Premium  Total>100  Express  | Discount  Shipping
 R1       Y         Y         N      |   15%      Free
 R2       Y         N         N      |   15%      Standard
 R3       N         Y         N      |    0%      Free
 R4       N         N         N      |    0%      Standard
 R5       —         —         Y      |  (per member) Express
```

Collapsing impossible/irrelevant combinations keeps the suite small. **Always check with the business which combinations are impossible** — that question is itself a valuable QA contribution."""),
                 ("When to use a decision table", """- Pricing, discounts, eligibility, permissions, approval flows, insurance rules, tax rules.
- Any requirement containing *if / unless / except / and / or / provided that*.
- Whenever you catch yourself writing 'and also if...' in a test case.

A decision table also doubles as a great artefact for a portfolio project and a strong whiteboard answer in interviews."""),
               ],
               desk="ITIL approval matrices and escalation rules are decision tables. You've read one; now you'll write one from a messy paragraph of requirements.",
               takeaway="List conditions, enumerate rules, mark actions, collapse impossible combinations, one test per column.",
               ex=[
                   mcq("A decision table has 3 binary conditions. How many rules exist before collapsing any?", [
                       "3", "6", "8", "9"], 2,
                       "2^3 = 8."),
                   mcq("What is a 'don't care' entry in a decision table?", [
                       "A rule nobody will test", "A condition whose value does not change the outcome for that rule, letting you collapse columns", "A bug in the table", "A requirement that was deleted"], 1),
                   mcq("Which requirement most needs a decision table?", [
                       "'The page must load'", "'Premium members get 15% off unless the order is express, and orders over $100 ship free'", "'The logo must be blue'", "'The button says Submit'"], 1,
                       "Multiple interacting conditions = decision table territory."),
               ]),

        lesson("design-05", "State transition testing", 12,
               "Many bugs only appear after a particular *sequence* of events: pay → refund → repay, or login → lock → unlock. **State transition testing** models the states a thing can be in, the events that move it, and the transitions that should (or should not) be allowed.",
               [
                 ("States, events, transitions", """A **state** is a condition an object rests in; an **event** triggers a change; a **transition** is the resulting move; an **action** may happen during it.

Example — an order:

```
NEW --[pay OK]--> PAID --[ship]--> SHIPPED --[deliver]--> DELIVERED
NEW --[cancel]--> CANCELLED
PAID --[refund]--> REFUNDED
```

From this model, derive tests for: every valid transition, **invalid transitions** (can you ship a NEW order? refund a CANCELLED one?), and *round trips* (PAID → REFUNDED → PAID?). Invalid transitions are where the juicy defects live."""),
                 ("A state transition table", """| From state | Event | To state | Allowed? |
|---|---|---|---|
| NEW | pay OK | PAID | Yes |
| NEW | ship | — | **No — must reject** |
| PAID | refund | REFUNDED | Yes |
| PAID | pay again | — | No (duplicate charge!) |
| CANCELLED | pay OK | — | No |
| DELIVERED | refund | REFUNDED | Yes, within 30 days |

The duplicate-payment row is the kind of defect that costs real money. You find it by *enumerating forbidden transitions*, not by clicking the happy path."""),
                 ("State transition diagrams plus 'N-switch' coverage", """A **state transition diagram** is the visual version (circles = states, arrows = events). Coverage levels: **0-switch** = test each valid transition once; **1-switch** = test every pair of consecutive transitions (A→B→C); **N-switch** = sequences of N+1 transitions. For a critical workflow, 1-switch catches most sequence defects. Also test **self-transitions** (submitting the same form twice) and **timeouts** (session expires mid-flow).

> **From the desk:** 'the ticket only appears if the user does X, then Y, then goes back' is a state-sequence bug. You already reproduce these; now you'll design for them upfront."""),
               ],
               desk="Ticket status flows (New → Assigned → Pending → Resolved → Closed) are state machines. You know them intimately — apply the same thinking to orders, accounts and sessions.",
               takeaway="Model states and events, test valid transitions, forbidden transitions, round trips, and sequences.",
               ex=[
                   mcq("Testing that a CANCELLED order cannot be paid for is an example of:", [
                       "Equivalence partitioning", "Testing an invalid / forbidden transition", "Boundary value analysis", "Performance testing"], 1),
                   mcq("'0-switch coverage' means:", [
                       "No transitions tested", "Every valid transition exercised at least once", "Every pair of consecutive transitions (A→B→C)", "Only the initial state"], 1),
                   order("Put a typical defect lifecycle in order:", [
                       "New", "Assigned / Open", "Fixed (Ready for Retest)", "Retested / Verified", "Closed"]),
               ]),

        lesson("design-06", "Use case, exploratory and error guessing", 12,
               "Not every valuable test comes from a specification table. This lesson covers scenario-driven and experience-driven approaches — the ones closest to the investigative instincts you already have.",
               [
                 ("Use case / scenario testing", """A **use case** describes an end-to-end interaction between an actor and the system to achieve a goal. Test the **main success scenario** plus each **alternative** and **exception** flow:

> *Use case: 'Buy a book'* — main flow: search → add to cart → checkout → pay → confirmation email. Exceptions: out of stock mid-checkout, card declined, session expires, address validation fails, duplicate submit, promo code expired.

Scenario tests are excellent for finding **integration defects** that unit-level tests miss, and they map nicely onto acceptance criteria and user stories."""),
                 ("Exploratory testing, structured", """Exploratory testing is *simultaneously learning, designing and executing* tests — not random clicking. Make it rigorous with **session-based test management (SBTM)**:

- A **charter** states the mission: *'Explore the password reset flow focusing on expired links and error messages, 45 minutes.'*
- A **time box** (usually 45-90 min, no interruptions).
- **Session notes**: what you did, what you found, what you'd explore next, questions raised.
- A short **debrief** with the team.

Use **tours** to structure exploration: the *landmark tour* (visit key features), the *money tour* (revenue-critical paths), the *back-alley tour* (least-used features), the *fedex tour* (follow data through the system), the *saboteur tour* (try to break it), and the *superhero tour* (test with extreme data)."""),
                 ("Error guessing and attack patterns", """Experienced testers aim at known weak spots: empty/null values, very long strings, special characters (`'`, `<`, `&`, emoji), duplicate submits, back/refresh/browser-back, double-click, interrupted network mid-request, clock changes, timezone/DST, concurrent edits, copy-paste from Word, huge files, special names (O'Brien, 李, hyphenated), zero and negative numbers, and permission changes mid-session.

Keep a personal **bug taxonomy** — a list of defect patterns you've seen. Every time a production incident crosses your desk, ask *'what test would have caught this?'* and add it to your checklist. That habit turns support experience into a testing advantage no course can teach."""),
               ],
               desk="This is your home turf. The upgrade is structure: charter, time box, notes, debrief — so 'I had a poke around' becomes auditable, repeatable coverage.",
               takeaway="Scenario tests cover end-to-end flows; exploratory testing is structured by charters and time boxes; error guessing targets known weak spots.",
               ex=[
                   mcq("What makes exploratory testing 'structured' rather than random clicking?", [
                       "Using an automated tool", "A charter, a time box, session notes and a debrief", "Following a scripted test case word for word", "Testing only the happy path"], 1),
                   mcq("Which is an 'error guessing' target?", [
                       "A value from the valid equivalence class", "Submitting a form twice and pressing browser Back mid-request", "The 3-point boundary set", "A decision table column"], 1),
                   inp("What do we call the short mission statement that scopes an exploratory session?", ["Charter", "test charter"], hint="It answers 'what am I exploring in this session?'"),
               ]),

        lesson("design-07", "Pairwise / combinatorial testing", 11,
               "When several independent inputs interact, full combinations explode. **Pairwise (all-pairs) testing** is a pragmatic compromise based on a striking empirical fact: most defects are triggered by a single input or a *pair* of inputs, rarely by three or more together.",
               [
                 ("The idea", """You do not test every combination; you ensure that **every pair of values from any two parameters appears together at least once**.

Example: 4 parameters, each with 3 values → 3⁴ = 81 full combinations. A pairwise set covers all value pairs in about 9-10 test cases. That is a ~8× reduction with very little loss of defect-finding power for interaction bugs."""),
                 ("Worked example: browser matrix", """| Param | Values |
|---|---|
| Browser | Chrome, Firefox, Safari |
| OS | Windows, macOS, iOS |
| User role | Guest, Member, Admin |

Full = 3×3×3 = 27 combos. A valid pairwise set (9 rows):

| # | Browser | OS | Role |
|---|---|---|---|
| 1 | Chrome | Windows | Guest |
| 2 | Chrome | macOS | Member |
| 3 | Chrome | iOS | Admin |
| 4 | Firefox | Windows | Member |
| 5 | Firefox | macOS | Admin |
| 6 | Firefox | iOS | Guest |
| 7 | Safari | Windows | Admin |
| 8 | Safari | macOS | Guest |
| 9 | Safari | iOS | Member |

Every browser×OS, browser×role, and OS×role pair appears. Generate these with a tool (e.g. `pairwise` tools, PICT, or an online all-pairs generator) rather than by hand — but know what the tool is doing and always **add explicit high-risk combinations** (e.g. Safari + iOS + Guest) even if the algorithm covers them."""),
                 ("When to use it — and when not to", """Use pairwise for **configuration/compatibility matrices**, feature-flag combinations, and form fields with many independent options. Do **not** use it to replace boundary analysis or decision tables for business rules: if three conditions genuinely interact (premium AND over $100 AND express), a decision table is the right tool. Pairwise assumes interactions are mostly pairwise; business logic often is not.

> **From the desk:** 'it only breaks on Safari on the iPad for guests' is a *pairwise (actually 3-way)* interaction defect. You've troubleshot these; now you'll design a small matrix that catches them systematically."""),
               ],
               desk="Compatibility tickets ('works in Chrome, not in Edge on the VPN') are interaction defects. Pairwise is the systematic version of your browser/OS/role troubleshooting grid.",
               takeaway="Cover every pair of parameter values; a handful of rows replace dozens. Keep decision tables for real business-rule interactions.",
               ex=[
                   mcq("Pairwise testing is based on which observation?", [
                       "Most defects involve 4+ interacting inputs", "Most defects are caused by a single input or a pair of inputs", "All combinations must be tested", "Browsers never interact with OS"], 1),
                   mcq("3 parameters with 3 values each have how many full combinations?", [
                       "9", "27", "6", "81"], 1, "3^3 = 27."),
                   mcq("For a business rule where premium + >$100 + express delivery all interact, the better technique is:", [
                       "Pairwise", "A decision table", "Boundary value analysis", "Random exploratory"], 1,
                       "Real 3-way business logic needs explicit rules, not pairwise coverage."),
               ]),
    ],
    quiz="test-design-quiz",
)

# ---------------------------------------------------------------------------
# 4. Test documentation
# ---------------------------------------------------------------------------
TEST_DOCS = course(
    "test-docs", "Test Cases, Plans & Documentation", "Artefacts a team can actually use",
    "Write test cases that anyone can run, build a test plan section by section, design test data, trace requirements to tests, and estimate and prioritise with risk.",
    "#ffb020", "p1", "Weeks 3-4", "Core",
    [
        lesson("docs-01", "Anatomy of a great test case", 12,
               "A test case is a reusable instruction, not a note to yourself. Its quality is measured by one question: *could a colleague who has never seen this feature run it and get the same verdict?*",
               [
                 ("The standard fields", """| Field | What it holds | Bad → Good |
|---|---|---|
| **ID** | Unique, stable | 'test1' → `TC_AUTH_014` |
| **Title** | One-line intent | 'login' → 'Reject login for a locked account' |
| **Requirement / AC ref** | Traceability link | — → `REQ-12 / AC-3` |
| **Priority** | High / Medium / Low | — → High |
| **Preconditions** | State before step 1 | — → 'Registered user exists; account locked after 5 failed attempts' |
| **Test data** | Concrete values | 'a user' → `qa.user14@example.com` |
| **Steps** | Numbered, one action each | vague → '1. Navigate to /login 2. Enter email ... 3. Click Sign in' |
| **Expected result** | Specific, observable, includes *what not* to happen | 'error' → 'Inline message "Account locked. Try again in 15 minutes"; no auth cookie set; no redirect' |
| **Actual result / Status** | Filled at execution | Pass / Fail / Blocked / Not Run / Skipped |
| **Postconditions** | Cleanup | 'Unlock account / delete test user' |"""),
                 ("A worked test case", """```text
ID:            TC_AUTH_014
Title:         Reject login for a locked account
Requirement:   REQ-12 / AC-3
Priority:      High
Preconditions: User qa.user14@example.com exists with password ValidPass!23;
               account has been locked by 5 failed attempts.
Test data:     email=qa.user14@example.com  password=ValidPass!23
Steps:
  1. Open https://staging.example.com/login
  2. Enter the email and password above
  3. Click "Sign in"
Expected result:
  - Sign-in is refused within 2 seconds.
  - Inline message: "Account locked. Try again in 15 minutes or reset your password."
  - URL remains /login; no session cookie is created.
  - The password field is cleared; no stack trace is shown.
Postconditions: Unlock the account in the admin tool for later tests.
```

Notice the expected result covers **behaviour, message, state, and security** — not just 'it fails'. Vague expected results are the main reason two testers disagree about whether a test passed."""),
                 ("Good test case checklist", """- One clear objective per case (split if you find yourself writing 'and also').
- **Reproducible**: concrete data, no 'some value'.
- **Atomic**: one action per step; numbered.
- **Independent**: does not depend on another test's leftovers (or states that dependency explicitly).
- **Traceable**: linked to a requirement.
- **Maintainable**: no duplicated setup; use shared preconditions / fixtures.
- **Self-cleaning**: leaves the environment as it found it.
- Includes both **positive and negative** cases, and a **reusable** naming convention."""),
               ],
               desk="A well-written ticket note and a well-written test case have the same DNA: exact steps, exact data, exact observed vs expected. You write these all day — you're just adding a 'precondition' and an ID.",
               takeaway="Concrete data, numbered single-action steps, specific observable expected results, traceable ID, cleanup.",
               ex=[
                   mcq("Which expected result is best?", [
                       "'It should error'", "'Login fails'", "'Inline message \"Account locked\"; no session cookie; URL remains /login'", "'Check the logs'"], 2,
                       "Specific, observable, verifiable — including what must NOT happen."),
                   mcq("Why should each step contain one action?", [
                       "It looks tidier", "Failures become pinpointable and the case is reproducible", "ISTQB mandates exactly 5 steps", "Automation requires it"], 1),
                   mdex("Write a minimal test case for 'apply an invalid coupon at checkout'. Include an ID, one precondition, numbered steps, and an expected result.",
                        [P(r"TC[_-]?\w+", "a test case ID"), P(r"[Pp]recondition", "a precondition"), P(r"1\.", "a numbered step 1"), P(r"2\.", "a numbered step 2"), P(r"[Ee]xpected", "an expected result"), P(r"invalid|not applied|rejected", "the rejection outcome")],
                        "ID: TC_CART_022\nTitle: Reject an invalid coupon\nPrecondition: Basket contains one $50 item; user is signed in.\nSteps:\n1. Go to /cart and enter coupon SAVE99 in the promo field.\n2. Click Apply.\nExpected result: Inline message \"Coupon SAVE99 is not valid\"; total remains $50.00; no discount row appears; order is not submitted.",
                        starter="ID: TC_CART_022\nPrecondition: ...\nSteps:\n1. ...\n2. ...\nExpected result: ...",
                        explain="Concrete data, single-action steps, specific expected result including what must not change."),
               ]),

        lesson("docs-02", "Test data, preconditions and independence", 11,
               "Most flaky, un-runnable test suites fail not because the tests are wrong but because the **data** is wrong. This lesson covers designing data deliberately and keeping tests independent.",
               [
                 ("Types of test data", """| Kind | Use | Example |
|---|---|---|
| **Static master data** | Reference values that rarely change | Countries, roles, product categories |
| **Transactional data** | Created/consumed by a test | A new order, a new user |
| **Boundary data** | Edge cases | 17, 18, 65, 66; empty string; max+1 |
| **Negative data** | Invalid input | `abc` in a number field, SQL-ish strings |
| **Masked / synthetic production data** | Realistic volume without privacy risk | Anonymised customer records |
| **Stateful data** | Specific lifecycle state | An *already locked* account, an *expired* link |"""),
                 ("Independence and cleanup", """A test that depends on the previous test's leftovers is a **fragile** test: run it alone and it fails; run the suite in a different order and it fails. Fix this with:

- **Setup / teardown**: create what you need at the start, delete it at the end.
- **Unique data**: generate emails like `qa+<timestamp>@example.com` so parallel runs don't collide.
- **Known baselines**: reset the DB or use a seeded fixture before a suite.
- **Explicit dependencies**: where a chain is unavoidable (e.g. create → approve → ship), name them and group them into one procedure.
- **Idempotency**: running the same test twice should not change the outcome.

> **Never test against production data.** Besides the privacy/regulatory problem, you will corrupt real records. Use staging with synthetic or masked data."""),
                 ("The data checklist for each test case", """1. What exact values do I type? 2. What state must the system already be in? 3. What other records must exist (user, product, permission)? 4. Who am I logged in as (role matters!)? 5. What must be cleaned up? 6. Could another test be using the same record right now? 7. Is any personal data involved, and is it masked?

> **From the desk:** 'works with my account, not with theirs' is almost always a data/permission difference. You've debugged this a hundred times — now design for it deliberately by naming the role and record state in every case."""),
               ],
               desk="Permission and data-state differences are the classic 'cannot reproduce' ticket. Writing preconditions explicitly is how you eliminate that whole class of noise.",
               takeaway="Name exact values, roles, and system state. Create what you need, clean up after yourself, never use production data.",
               ex=[
                   mcq("A test passes when run in the full suite but fails when run alone. The most likely cause is:", [
                       "A browser bug", "The test depends on data left behind by an earlier test", "The requirement changed", "The tester made a typo"], 1),
                   mcq("Which is the safest source of realistic high-volume test data?", [
                       "A copy of the live production database", "Anonymised / masked or synthetic data", "Whatever the developer has locally", "Real customer records from a support ticket"], 1),
                   inp("What property means running the same test twice leaves the same outcome and no duplicate state?", ["Idempotent", "idempotency", "Idempotence"], hint="A word from API design too: repeating the call has no extra effect."),
               ]),

        lesson("docs-03", "Traceability matrices and coverage reporting", 11,
               "A **Requirements Traceability Matrix (RTM)** maps each requirement to the test cases that verify it and to any defects found. It answers the questions managers and auditors actually ask: 'is everything covered?' and 'what does this change affect?'",
               [
                 ("A worked RTM", """| Req ID | Requirement | Test case(s) | Status | Defects |
|---|---|---|---|---|
| REQ-12 | Reset password by email | TC-031, TC-032, TC-033, TC-034 | 4/4 Passed | DEF-503 (fixed) |
| REQ-13 | Lock account after 5 failures | TC-014, TC-015 | 1 Passed, 1 Failed | DEF-501 (open, Critical) |
| REQ-14 | Cart accepts promo codes | TC-022, TC-023 | 2/2 Passed | — |
| REQ-15 | Guest checkout | TC-107 | **Not covered yet** | — |

The RTM exposes: **coverage gaps** (REQ-15 has no completed test), **orphan tests** (a test case linked to no requirement — probably wasted effort), and **impact analysis** (if REQ-12 changes, you know exactly which 4 tests and which defect to revisit). It is also your defence when someone asks 'why did we miss this bug?' — you can show what was and wasn't in scope."""),
                 ("Coverage measures to report carefully", """- **Requirements coverage** = requirements with at least one passing test ÷ total requirements.
- **Risk coverage** = high-risk items with a test ÷ high-risk items (more meaningful than raw %).
- **Execution status** = Passed / Failed / Blocked / Not Run counts (a blocked test is *not* a pass).
- **Defect density** = defects per module or per KLOC — useful for the clustering principle.

Report the **denominator** and the **status mix**. '90% coverage' where 10% is 'Blocked' is very different from 90% all-passed. And always list what is **out of scope** and the **residual risk**."""),
                 ("Keeping an RTM lightweight", """For a small Agile team, a full formal RTM is overkill. A pragmatic version: tag each test case with the story key (`PROJ-142`) in your test management tool, and generate a coverage report from those tags. The *principle* (every requirement has a verifiable test) matters more than the spreadsheet. In regulated industries, the formal document is mandatory and auditable."""),
               ],
               desk="Auditors and problem managers have asked you to 'show the record' for a change. An RTM is the testing equivalent — and 'impact analysis' is literally change management.",
               takeaway="Link requirement → test → defect. Report coverage with its denominator, status mix, out-of-scope items and residual risk.",
               ex=[
                   mcq("An RTM shows REQ-15 linked to TC-107 with status 'Not Run'. What does that tell you?", [
                       "REQ-15 is fully covered", "There is a coverage gap — the requirement has no completed verification", "TC-107 is an orphan test", "The requirement is defective"], 1),
                   mcq("Which coverage statement is most meaningful to a release decision?", [
                       "'90% of test cases passed'", "'100% of high-risk requirements have a passing test; 3 low-risk areas untested (accepted by PO)'", "'We ran 200 tests'", "'Coverage is 90%'"], 1,
                       "Risk-weighted, includes the denominator and explicit residual risk."),
                   mcq("A 'Blocked' test should be counted as:", [
                       "A pass", "A failure", "Not executed — neither a pass nor a fail", "Out of scope"], 2),
               ]),

        lesson("docs-04", "The test plan, section by section", 13,
               "A **test plan** is the document that says what you will test, how, with what, when, and what 'done' looks like. Writing one is a common interview task and a core portfolio artefact. This lesson walks every section.",
               [
                 ("Test plan vs test strategy", """A **test strategy** is a high-level, often organisation-level document: the general approach, standards, tooling and levels used across projects. A **test plan** is project- or release-specific: it turns the strategy into concrete scope, schedule, resources and criteria for *this* release. Small teams often merge them into one short page — that is fine; know the difference when asked."""),
                 ("The sections, in order", """1. **Identifier & version** — doc ID, version, author, date, approvers.
2. **Introduction / objectives** — what this release is and what testing must prove.
3. **Scope — in scope** — features, platforms, integrations, test levels and types.
4. **Scope — out of scope** — equally important: 'third-party payment sandbox, IE11, load above 500 users'.
5. **Test approach / strategy** — techniques (EP, BVA, decision tables), levels, manual vs automated split, entry/exit criteria.
6. **Test environment & tools** — URLs, builds, browsers/devices, DB, test management tool, defect tracker, accounts.
7. **Test data requirements** — what data, who provides it, masking, refresh cadence.
8. **Roles & responsibilities** — who writes cases, who runs, who triages, who signs off.
9. **Schedule & milestones** — aligned to sprint dates; include time for retest and regression.
10. **Risks & contingencies** — 'staging DB is shared; if unavailable, use the local container', 'late build → reduce exploratory time, never drop smoke'. Name the mitigation, not just the risk.
11. **Defect management** — tool, severity/priority definitions, triage cadence, escalation.
12. **Entry / exit criteria & deliverables** — measurable sign-off conditions; list the artefacts you will produce.
13. **Approvals** — names/signatures (or a Jira sign-off comment)."""),
                 ("A short real example (excerpt)", """```text
Test Plan TP-2026-04 — 'Coupons & Discounts' release
Scope IN:  cart coupon entry, discount calculation, express-shipping rule,
           Chrome/Edge/Firefox (latest), Safari 17, API contract v2.
Scope OUT: load > 500 concurrent users, legacy IE, 3rd-party tax service
           sandbox (mocked instead).
Approach:  decision table for the 3 discount conditions; BVA on the
           $100/$500 thresholds; pairwise for browser×OS×role; 45-min
           exploratory charter on coupon error messages. Manual execution
           now, automated regression in Phase 4.
Entry:     build 2026.04.7 deployed to staging + smoke suite green + seeded
           catalogue data loaded.
Exit:      100% of High-priority cases executed & passing, 0 open
           Critical/Major defects, all AC traced in the RTM, PO sign-off.
Risks:     shared staging DB → reserve a 2h window; late build → drop the
           stretch exploratory charter, keep smoke + regression.
```"""),
               ],
               desk="A change record / method statement you've written for a production change has the same sections: scope, approach, rollback, risk, approvals. Reuse that mental template.",
               takeaway="Scope (in AND out), approach, environment, data, roles, schedule, risks+mitigations, measurable entry/exit criteria, sign-off.",
               ex=[
                   mcq("Which section of a test plan is most often forgotten but most important for avoiding arguments?", [
                       "Version number", "Out of scope", "Author name", "Font choice"], 1),
                   mcq("A test strategy differs from a test plan in that it is:", [
                       "Shorter", "High-level and organisation-wide rather than release-specific", "Written by developers", "Only for automation"], 1),
                   mcq("Which is a well-formed exit criterion?", [
                       "'Testing feels complete'", "'0 open Critical/Major defects; 100% of High-priority cases executed; PO sign-off'", "'The sprint ended'", "'All tests passed' (with no denominator)"], 1),
                   mdex("Write a one-paragraph test plan excerpt with an 'In scope', 'Out of scope', and 'Exit criteria' heading.",
                        [P(r"[Ii]n [Ss]cope", "an In scope section"), P(r"[Oo]ut of [Ss]cope", "an Out of scope section"), P(r"[Ee]xit", "an Exit criteria section"), P(r"[Cc]ritical|[Mm]ajor|[Pp]riority", "a measurable condition")],
                        "## In scope\nLogin, password reset, cart totals on Chrome and Safari (latest).\n\n## Out of scope\nLoad testing above 200 users; legacy IE11.\n\n## Exit criteria\n100% of High-priority cases executed and passing; zero open Critical or Major defects; Product Owner sign-off recorded.",
                        starter="## In scope\n\n## Out of scope\n\n## Exit criteria\n"),
               ]),

        lesson("docs-05", "Risk-based testing and estimation", 12,
               "There is never enough time to test everything. **Risk-based testing** is how professionals decide what to test first, deepest, and what to consciously leave untested — and how to explain that decision without sounding careless.",
               [
                 ("Risk = likelihood × impact", """For each feature or area, score:

- **Likelihood of failure** — is it new? complex? recently changed? historically buggy? written by a new dev? dependent on a flaky 3rd party? has it got lots of boundary logic?
- **Impact if it fails** — revenue loss, data loss/corruption, security/privacy, legal/regulatory, number of users affected, reputational damage, reversibility.

A simple 1-5 × 1-5 grid gives a risk score. Put payments, auth, data migration and compliance in the top-right; put a typo on the About page in the bottom-left. Then: **more technique, more depth, more automation, earlier testing** for high-risk items; light smoke or even explicit no-test for low-risk ones."""),
                 ("A worked risk register", """| Area | Likelihood (1-5) | Impact (1-5) | Score | Decision |
|---|---|---|---|---|
| Payment capture | 4 | 5 | **20** | Decision table + BVA + negative + end-to-end + automated regression |
| New coupon logic | 5 | 4 | **20** | Full boundary set + pairwise + exploratory charter |
| Password reset | 3 | 5 | **15** | Security checks + negative paths + retest |
| Profile photo upload | 3 | 2 | 6 | Smoke + file-type boundaries |
| Footer copyright year | 1 | 1 | 1 | Visual check only |

Notice the score drives the *technique*, not just the order. And the low scores are explicitly recorded as accepted risk — that is defensible."""),
                 ("Estimating test effort", """Rough, transparent techniques beat false precision:

- **Bottom-up**: (# test cases × avg minutes per case) + setup + execution + defect retest + regression + reporting. E.g. 60 cases × 6 min = 6 h, plus 2 h setup, 2 h retest, 1 h regression, 1 h report = **12 h**.
- **Ratio**: testing effort often runs 30-50% of development effort for a manual-heavy release.
- **Three-point**: `(optimistic + 4×likely + pessimistic) / 6`.
- Always add **contingency** (15-25%) for blocked environments, late builds and defect investigation.

When asked 'how long will testing take?', give the breakdown and the assumptions, not a single number: *'12 hours assuming the staging build lands Monday and the seeded data is ready; if the build slips, I can drop the low-risk exploratory charter but not smoke or regression.'*"""),
               ],
               desk="P1-P4 triage is likelihood × impact with different labels. You already make this call under pressure; risk-based planning just does it before the incident, with a written record.",
               takeaway="Score likelihood × impact, let the score choose the technique and depth, record accepted low-risk, estimate with a visible breakdown + contingency.",
               ex=[
                   mcq("A brand-new complex payment flow with a history of defects would score:", [
                       "Low likelihood, low impact", "High likelihood, high impact → test earliest and deepest", "High likelihood, low impact", "Low likelihood, high impact → no testing"], 1),
                   mcq("Which estimate is most professional?", [
                       "'About 2 days'", "'12 h = 60 cases × 6 min + setup 2 h + retest 2 h + regression 1 h + report 1 h; assumes build lands Monday'", "'As long as it takes'", "'Fast'"], 1),
                   mcq("What should happen to low-risk areas you decide not to test deeply?", [
                       "Nothing — just don't mention them", "Record them explicitly as accepted residual risk", "Delete them from the requirements", "Test them after release"], 1),
               ]),

        lesson("docs-06", "Test execution, status and closure", 11,
               "Execution is where documentation meets reality: recording honest statuses, managing blocked tests, and producing a summary that lets someone else make the release call.",
               [
                 ("Statuses mean specific things", """| Status | Meaning |
|---|---|
| **Passed** | Actual result matched expected result |
| **Failed** | Actual differed; a defect should be raised (or linked) |
| **Blocked** | Cannot execute due to an environment/build/data issue — *not* a fail and *not* a pass |
| **Not Run / Untested** | Planned but not yet executed |
| **Skipped / N/A** | Deliberately excluded, with a reason (e.g. feature not in this build) |
| **Retest** | Previously failed, fix delivered, awaiting confirmation |

Never quietly turn a Blocked into a Passed. A blocked test hides risk; say so in the report and chase the blocker. Log the **build number, environment, browser/OS, time and tester** with each run — without that, a 'pass' is not evidence."""),
                 ("The test summary report", """At cycle closure, produce a short report:

1. **Scope & build** — what was tested, build/version, environment, period.
2. **Execution summary** — planned vs executed; Passed / Failed / Blocked / Not Run counts and %.
3. **Coverage** — requirements/risk coverage, and what was out of scope.
4. **Defects** — open by severity/priority, fixed/verified, deferred, defect trends (arrival vs closure rate).
5. **Exit criteria** — met / not met, item by item.
6. **Residual risk & recommendation** — the actual decision: *'Recommend release with DEF-512 (minor, tooltip typo) deferred; two Safari 16 cosmetic issues documented; payment path fully covered.'*
7. **Lessons for next cycle** — 'staging data was stale; add a data-refresh step to the checklist'."""),
                 ("Exit criteria in practice", """When an exit criterion is not met, do not fudge the numbers. Options: extend testing, reduce scope with PO agreement, defer documented minor defects, or **recommend no-go** with reasons. A QA Analyst's professional value is being the person who can say 'not yet' with evidence and without drama — a skill you have practised when escalating a bad change."""),
               ],
               desk="Shift handover notes and incident summaries are the same genre: what happened, what's outstanding, what the on-call person must know. You already write these under time pressure.",
               takeaway="Honest statuses, logged build/environment, exit criteria checked item by item, explicit residual risk and a clear recommendation.",
               ex=[
                   mcq("A test cannot run because the staging database is down. Its status is:", [
                       "Failed", "Passed", "Blocked", "Not Run"], 2),
                   mcq("Which of these belongs in a test summary report?", [
                       "Only the number of tests passed", "Defect counts by severity, exit criteria status, residual risk and a recommendation", "A list of every tester's hours", "The developer's code review comments"], 1),
                   mcq("An exit criterion ('0 open Critical defects') is not met. Best action:", [
                       "Mark it met to keep the release on time", "Report it clearly and recommend no-go / escalation with evidence", "Delete the criterion", "Silently defer it"], 1),
               ]),
    ],
    quiz="test-docs-quiz",
)

# ---------------------------------------------------------------------------
# 5. Defects
# ---------------------------------------------------------------------------
DEFECTS = course(
    "defects", "Defect Management", "Find it, prove it, get it fixed",
    "What counts as a defect, the anatomy of a perfect bug report (with a full example), severity vs priority, the defect lifecycle, retesting vs regression, and reproducibility.",
    "#ff5470", "p1", "Weeks 4-5", "Core",
    [
        lesson("defect-01", "What actually counts as a bug", 10,
               "Not every surprise is a defect, and not every defect is worth a ticket. Before writing a report, decide what you are looking at — this saves you credibility and the developers' patience.",
               [
                 ("Defect sources", """A defect is a deviation between **actual** and **expected** behaviour, where 'expected' comes from the test basis (requirements, AC, spec, or a reasonable implicit expectation). Sources include:

- Ambiguous or missing requirements ('the spec never said what happens for guest users').
- Coding errors, wrong boundary (`>` vs `>=`), null handling, race conditions.
- Integration mismatches (API changed its response shape, third-party outage).
- Environment/configuration differences (works on staging, not on the test VM).
- Data problems (a legacy record with a null field breaks the page).

**Not a defect:** a feature request ('it would be nice if...'), a misunderstanding of the spec, an environment outage that is an *incident* rather than a code fault, or a user error. Those still get recorded — as a change request, an incident, or a documentation issue — but don't inflate the defect count."""),
                 ("Implicit requirements count", """Some expectations are never written down but are universally reasonable: no stack traces shown to users, no 500 error on bad input, data is not lost on back/refresh, the app does not crash, passwords are not echoed, errors are understandable. You may log these as defects against an **implicit requirement**; note that basis in the report."""),
                 ("Duplicate and 'by design' handling", """Before logging: search the tracker for an existing report (a **duplicate** wastes everyone's time), check the latest AC/spec, and reproduce twice. If a developer closes it **'Works as designed'**, that is a signal the requirement was unclear — take it to refinement and get the AC clarified, rather than arguing in the ticket. If it is **'Not reproducible'**, improve your steps/environment detail, not your volume."""),
               ],
               desk="You already distinguish 'user error' from 'system fault' from 'enhancement request' on the desk. Same triage, different tracker.",
               takeaway="A defect = deviation from a stated or reasonable expected behaviour. Check for duplicates, reproduce twice, and classify enhancement/incident separately.",
               ex=[
                   mcq("A user asks 'it would be great if the report could export to PDF'. This is:", [
                       "A Critical defect", "An enhancement / change request, not a defect", "A regression", "A duplicate"], 1),
                   mcq("A page shows a raw Java stack trace to the user. The requirement says nothing about errors. Is it a defect?", [
                       "No — not in the spec", "Yes — against a reasonable implicit expectation", "Only if a user complains", "It's an incident"], 1),
                   mcq("What is the first thing to do before logging a bug you just found?", [
                       "Assign it to a developer", "Search the tracker for a duplicate and reproduce it again", "Set severity to Critical", "Email the whole team"], 1),
               ]),

        lesson("defect-02", "Anatomy of a perfect defect report", 14,
               "A bug report is a piece of technical writing whose only job is to let a stranger reproduce the problem, understand its impact, and fix it without asking you a single question. This is the single most examined practical skill in QA interviews.",
               [
                 ("The fields", """| Field | Rule |
|---|---|
| **ID** | Auto from tracker |
| **Title / Summary** | One line: `[Module] What is wrong, under what condition` — not 'doesn't work' |
| **Severity** | Technical impact (see next lesson) |
| **Priority** | Business order of fixing |
| **Environment** | Build/version, URL, browser+version, OS/device, DB, feature flags, user role |
| **Preconditions** | Account state, data state, config |
| **Steps to reproduce** | Numbered, minimal, one action each, starting from a known state |
| **Test data** | Exact values used |
| **Actual result** | What happened, verbatim messages, observed values |
| **Expected result** | What should have happened, with the requirement/AC reference |
| **Evidence** | Screenshot / screen recording, console errors, network (HAR), logs, timestamps, request IDs |
| **Reproducibility** | Always / intermittent (x of y attempts) / once |
| **Workaround** | If one exists |
| **Notes** | Related cases, suspected cause, first seen in build X (regression hint) |"""),
                 ("A full example — good vs bad", """**Bad:** *'Checkout broken. Total wrong. Pls fix ASAP.'*

**Good:**
```text
ID:          DEF-1042
Title:       [Cart] 10% discount is applied twice when coupon SAVE10 is
             used on an order over $100
Severity:    Major        Priority: High
Environment: staging build 2026.04.7, https://staging.example.com,
             Chrome 125 / Windows 11, signed in as standard Member,
             flag NEW_PRICING=on
Preconditions: Catalogue item SKU-88 priced $120.00; coupon SAVE10
             (10% off) active; user has no other discounts.
Steps:
  1. Add SKU-88 to the cart.
  2. Go to /cart and confirm the subtotal shows $120.00.
  3. Enter SAVE10 in the promo field and click Apply.
  4. Observe the order summary.
  5. Click "Place order".
Test data:   email qa.user14@example.com, coupon SAVE10, SKU-88
Actual:      Summary shows $96.00 (two 10% discounts, $120 -> $108 -> $96),
             and the confirmation email also shows $96.00.
Expected:    $108.00 (one 10% discount), per REQ-14 / AC-2.
Evidence:    screenshot cart-1042.png, network HAR cart-1042.har,
             console: no errors, API /cart/total returned 96.00.
Repro rate:  5/5 attempts. First seen on build 2026.04.7 (2026.04.6 OK).
Workaround:  Remove and re-add the coupon before paying — not reliable.
```

Note the **regression hint** ('2026.04.6 was OK') — that single line can save a developer an hour. Note also that the title names *module + fault + condition*."""),
                 ("Tone and common mistakes", """Write about the **system**, not the person: 'the total is recalculated twice', not 'the dev broke it again'. Never stack five problems in one report (one defect = one ticket, unless they share a root cause). Never include vague steps ('do the usual'), never omit the build number, never guess the root cause as fact. Attach evidence but also describe it in text, because screenshots are not searchable."""),
               ],
               desk="This is a high-quality escalation ticket with a build number and a repro rate added. You already know the pain of an L2 handoff that says 'not working' — be the person who never sends one.",
               takeaway="Minimal numbered steps, exact data, verbatim actual vs referenced expected, environment/build, evidence, repro rate, one issue per ticket.",
               ex=[
                   mcq("Which defect title is best?", [
                       "'Bug in cart'", "'Doesn't work'", "'[Cart] Discount applied twice when SAVE10 is used on orders over $100'", "'URGENT!!!'"], 2),
                   mcq("Why include 'first seen on build 2026.04.7; 2026.04.6 was OK'?", [
                       "It's required by Jira", "It flags a regression and narrows the developer's search to that build's changes", "It increases severity", "It's a workaround"], 1),
                   mcq("You find 4 unrelated UI problems on one page. Best practice:", [
                       "One report listing all 4", "Four separate reports (one defect each)", "Only report the worst one", "Report them verbally"], 1),
                   mdex("Write a defect report for: 'On Safari 17, clicking Save on the profile page shows a blank page; Chrome works.' Include a title, environment, numbered steps, actual, expected, and a repro rate.",
                        [P(r"[Tt]itle|#", "a title"), P(r"Safari", "the environment"), P(r"1\.", "step 1"), P(r"2\.", "step 2"), P(r"[Aa]ctual", "actual result"), P(r"[Ee]xpected", "expected result"), P(r"[0-9]/[0-9]|Always|always", "a repro rate")],
                        "Title: [Profile] Blank page after clicking Save on Safari 17\nEnvironment: staging build 2026.04.7, Safari 17 / macOS 14, signed in as Member.\nSteps:\n1. Open /profile and change the display name.\n2. Click Save.\nActual: browser shows a completely blank white page; console error 'SyntaxError: optional chaining unsupported'.\nExpected: 'Profile updated' confirmation and the new name persists, per REQ-08 / AC-1.\nRepro rate: 3/3 on Safari 17, 0/3 on Chrome 125.\nEvidence: screenshot profile-blank.png, console log attached.",
                        starter="Title: ...\nEnvironment: ...\nSteps:\n1. ...\n2. ...\nActual: ...\nExpected: ...\nRepro rate: ...",
                        hint="Include the browser, the build, and how often it happens."),
               ]),

        lesson("defect-03", "Severity vs priority (worked examples)", 11,
               "**Severity** = how bad the defect is technically. **Priority** = how soon the business needs it fixed. They are independent, and interviewers love to test the distinction with awkward examples.",
               [
                 ("The definitions", """| | Severity (technical impact) | Priority (business urgency) |
|---|---|---|
| Set by | **Tester / QA** | **Product Owner / business** (with QA input) |
| Scale | Critical / Major / Minor / Trivial (or S1-S4) | P1 / P2 / P3 / P4, or High/Medium/Low |
| Question | 'How badly is the system broken?' | 'When must it be fixed?' |
| Changes when | The technical impact is understood | Business deadlines, release dates, marketing, contracts change |

**Severity levels:** *Critical* — system crash, data loss/corruption, security breach, no workaround, blocks testing. *Major* — major feature broken, significant wrong result, workaround is painful. *Minor* — small functional issue, cosmetic-but-noticeable, easy workaround. *Trivial* — typo, alignment, tooltip text."""),
                 ("Worked examples that trip people up", table(
                     ["Scenario", "Severity", "Priority", "Why"],
                     [["Payments fail for all users; no workaround", "Critical", "P1", "Total business stoppage"],
                      ["Company logo is misspelled on the homepage", "Trivial", "P1", "Technically tiny, but the CEO's launch demo is tomorrow → business urgent"],
                      ["Rare crash in an admin-only report, workaround exists", "Major", "P4", "Bad but low business exposure"],
                      ["Checkout total wrong by 1 cent on leap days", "Major", "P2", "Financial correctness, rare condition"],
                      ["Tooltip typo in an internal settings page", "Trivial", "P4", "Neither bad nor urgent"]])),
                 ("Rules of thumb", """- QA proposes severity; PO owns priority. Don't inflate severity to get attention — it destroys your credibility and skews metrics.
- Re-assess priority near release: a P4 can become a P1 if it lands on the demo path.
- A **Critical severity** defect usually implies **P1 priority**, but not always (e.g. a crash in a feature being switched off next week).
- Include **workaround** in the report: a painful workaround raises effective priority even when severity is moderate.
- Define your scales in the test plan so everyone uses the same words."""),
               ],
               desk="P1-P4 incident priorities are business urgency. Severity is your technical assessment — exactly like distinguishing 'this is a cosmetic UI glitch' from 'this corrupts the customer record' before escalating.",
               takeaway="Severity = technical impact, set by QA. Priority = business order, set by PO. They can disagree; the logo-before-demo case proves it.",
               ex=[
                   mcq("A misspelled company logo on the homepage the day before a major launch is:", [
                       "Critical / P4", "Trivial severity / P1 priority", "Major / P4", "Trivial / P4"], 1,
                       "Technically trivial, business-critical timing."),
                   mcq("Who typically *owns* the priority field?", [
                       "The tester who found it", "The developer assigned", "The Product Owner / business", "The release manager only"], 2),
                   mcq("Payments failing for all users with no workaround is:", [
                       "Minor / P3", "Critical severity / P1 priority", "Trivial / P1", "Major / P4"], 1),
                   inp("Which word describes how bad a defect is *technically*, as opposed to how soon it must be fixed?", ["Severity", "severity"], hint="The other one is 'priority'."),
               ]),

        lesson("defect-04", "The defect lifecycle", 12,
               "A defect moves through a defined workflow with an owner at every step. Knowing the states — and who is allowed to move it — prevents the classic 'who's got this bug?' chaos.",
               [
                 ("A typical workflow", """```
New / Open
   -> Assigned (triage: valid? severity? priority? owner?)
   -> In Progress / Accepted (developer reproduces and works)
   -> Fixed / Ready for Retest (build deployed to test env)
        -> Retest (QA)
              -> Verified / Closed  (fix confirmed + regression OK)
              -> Reopened          (still broken -> back to Assigned)
   -> Rejected / Not a Defect  (with a reason + AC clarification)
   -> Deferred / Won't Fix      (documented, PO accepts residual risk)
   -> Duplicate                 (linked to the original)
```

Every transition should carry: **who** changed it, **when**, **why**, and often a **comment**. The 'Fixed' state must name the build the fix is in — otherwise QA retests the old build and reopens a perfectly good fix."""),
                 ("Triage: the meeting that matters", """**Defect triage** is a short, regular meeting (daily in crunch, weekly otherwise) with QA, dev lead and PO. For each new defect: is it real? is it a duplicate? what severity and priority? who owns it? which release? does it block testing? is there a workaround? Anything deferred gets an explicit reason and an accepted-risk note.

Good triage hygiene: no defect sits in 'New' for more than a day, no 'Rejected' without a clear reason, no 'Fixed' without a build number, and no silent priority changes."""),
                 ("Metrics that help (and ones that lie)", """Useful: **open defects by severity**, **defect arrival vs closure rate** (is the backlog growing?), **age of open defects**, **reopen rate** (are fixes actually good?), **escaped defects** (found after release — the honest measure of your test design), and **defect density by module** (feeds the clustering principle).

Misleading: *number of bugs found* as a productivity metric (it incentivises trivial reports and punishes good developers), and *% closed* without looking at what was deferred or rejected. Never weaponise a metric against a person — use it to find process problems."""),
               ],
               desk="Incident and problem record flows (New → Assigned → Resolved → Closed, with reopen when the fix didn't stick) are the same state machine. You know why 'Resolved without a build reference' causes pain.",
               takeaway="Every state has an owner, a reason and a build number. Triage regularly. Measure trends and escapes, not raw bug counts.",
               ex=[
                   order("Put a defect's happy-path lifecycle in order:", [
                       "New / logged", "Triaged & Assigned", "In Progress (developer fixes)", "Fixed / Ready for Retest in build X", "QA Retests", "Verified / Closed"]),
                   mcq("A developer marks a defect 'Fixed' but gives no build number. What should QA do?", [
                       "Retest on the current test environment anyway", "Ask which build contains the fix before retesting", "Close the defect", "Reopen it immediately"], 1),
                   mcq("Which metric best reflects the effectiveness of your test design?", [
                       "Number of defects logged", "Escaped defects (found after release)", "Lines of test code", "Hours worked"], 1),
                   mcq("A defect is closed as 'Rejected / Not a defect' with no explanation. The best QA response is:", [
                       "Reopen it angrily", "Get the requirement/AC clarified and record the reasoning so it doesn't recur", "Log a duplicate", "Delete the report"], 1),
               ]),

        lesson("defect-05", "Retesting, regression and test selection", 12,
               "A fix is never just 'does the bug still happen?'. The change that fixed it may have broken something else. This lesson covers the three test activities after a change and how to pick a regression suite you can actually run.",
               [
                 ("The three activities", """| Activity | What it is | Scope |
|---|---|---|
| **Confirmation / Retesting** | Re-run the *exact failed test case(s)* against the fixed build | Narrow — the specific defect |
| **Regression testing** | Re-run *other, previously passing* tests to detect side effects | Broader — related and high-risk areas |
| **Smoke / sanity** | Quick check that the build is fundamentally usable and testable | Tiny — before any of the above |

Example: a fix changes the discount calculation. Retest = re-run TC-022 (invalid coupon) and the failing boundary case. Regression = re-run cart totals, checkout, order confirmation, invoice PDF, and the promo API contract, because they all consume the same pricing function."""),
                 ("Choosing a regression suite", """You cannot re-run everything after every fix. Select by:

1. **Change impact** — what modules/functions/data does the fix touch? (Ask the dev; read the PR diff.)
2. **Risk** — high-impact paths always included (auth, payment, data writes).
3. **History** — modules with a high defect density (clustering principle).
4. **Dependencies** — shared components, APIs, DB schema, config.
5. **Recent escapes** — anything that broke last release.

Keep a **regression pack** — a stable, versioned subset of your suite. Grow it whenever a defect escapes ('add one test for every bug that reached production'), prune stale cases (pesticide paradox), and automate the stable, high-value ones later in Phase 4."""),
                 ("Regression-avoidance habits", """Tag test cases by feature/risk so you can filter a pack quickly. Record the build number for every result. If a supposedly passing case now fails after an unrelated fix, that is a **regression defect** — log it with 'introduced between builds X and Y'. That detail is gold for the developer doing a bisect."""),
               ],
               desk="'The fix worked but now printing is broken' is the classic side-effect incident you've seen after a change. Regression testing is the formal name for checking the neighbours, not just the patient.",
               takeaway="Retest the failed case, regression-test the neighbourhood, smoke-test the build; maintain a risk-selected regression pack and add one test per escaped bug.",
               ex=[
                   mcq("Re-running the exact test case that failed, after the fix, is called:", [
                       "Regression testing", "Confirmation / retesting", "Smoke testing", "Exploratory testing"], 1),
                   mcq("Which is the best trigger to ADD a case to the regression pack?", [
                       "Every new test case written", "A defect that escaped to production", "A typo fix", "A new tester joining"], 1,
                       "Add one test for every escaped bug; that's how the pack learns."),
                   mcq("A fix to the pricing function should have regression coverage on:", [
                       "Only the exact failing test", "Cart totals, checkout, invoice and the pricing API — everything consuming that function", "The homepage", "Nothing else"], 1),
                   inp("What small suite answers 'is this build even testable?' before any deep testing?", ["Smoke", "Smoke suite", "smoke test"], hint="Named after powering on hardware and watching for smoke."),
               ]),

        lesson("defect-06", "Reproducibility and root-cause thinking", 12,
               "An intermittent bug is the hardest kind to get fixed. This lesson gives you a method for turning 'it happens sometimes' into a deterministic repro, plus the root-cause mindset that makes your reports genuinely useful.",
               [
                 ("A method for intermittent defects", """1. **Record the exact context** each time: build, time, user/role, data, browser, network, sequence of prior actions, any feature flags.
2. **Look for the difference** between a pass and a fail: timing? specific record? order of steps? cache state? concurrent user?
3. **Control one variable at a time** — same data, same sequence, change only the suspected factor. (This is exactly the scientific method, and exactly how you troubleshoot on the desk.)
4. **Force the condition**: slow the network in DevTools, add a delay, run two sessions concurrently, use a fresh vs cached profile, clear/not clear storage.
5. **Quantify**: '2/10 attempts, always within 3 s of a cold start' is far more useful than 'sometimes'.
6. **Capture evidence automatically**: console log, HAR file, screen recording, timestamps, request IDs."""),
                 ("Common causes of 'cannot reproduce'", """| Cause | What to check |
|---|---|
| Different data | Exact record IDs, nulls, special characters, huge values |
| Different role/permissions | Guest vs member vs admin vs suspended |
| State/caching | Cookies, localStorage, service worker, stale CDN asset |
| Timing / race | Slow network, double-click, concurrent edits, session timeout |
| Environment | Build number, feature flags, config, third-party sandbox, timezone/locale |
| Sequence | Browser Back, refresh, tab duplication, previous test leftovers |

> **From the desk:** 'cannot reproduce' on a ticket usually means the reporter omitted context. You now know the exact list of context to capture — and to ask for."""),
                 ("Root cause vs symptom (and the 5 Whys)", """QA usually reports the **symptom**; developers find the **root cause**. But adding a *hypothesis* (clearly labelled) helps: 'suspect the total is recomputed on both the client and the server' or 'only fails when the user's display name contains an apostrophe'.

Use the **5 Whys** on escaped defects: *Why did the user see the wrong total? → the discount applied twice → why? → the coupon listener fired twice → why? → the button wasn't debounced → why? → no test covered rapid double-click → why? → our test design had no concurrency/duplicate-submit case.* The last 'why' is a **process fix**, and it becomes a new test case in your regression pack. That is how QA improves the system, not just the build."""),
               ],
               desk="Isolating one variable at a time is your daily troubleshooting method. Here it becomes a documented repro procedure that a developer can act on without a call.",
               takeaway="Capture full context, change one variable, quantify the repro rate, force the condition, and turn each escape into a process fix + regression case.",
               ex=[
                   mcq("An intermittent defect report should include:", [
                       "'Sometimes it breaks'", "A repro rate (e.g. 2/10), exact context, and what differs between pass and fail", "Only a screenshot", "A severity of Critical by default"], 1),
                   mcq("To isolate the cause of an intermittent bug you should:", [
                       "Change several things at once to save time", "Control one variable at a time", "Restart the whole environment repeatedly", "Wait for it to happen again naturally"], 1),
                   mcq("The final 'why' in a 5-Whys analysis of an escaped defect should usually produce:", [
                       "A person to blame", "A process/test-design improvement and a new regression case", "A longer meeting", "A higher severity"], 1),
               ]),
    ],
    quiz="defects-quiz",
)

COURSES_01 = [ORIENTATION, FOUNDATIONS, TEST_DESIGN, TEST_DOCS, DEFECTS]

QUIZZES_01 = [
    quiz("orientation-quiz", "orientation", "Orientation checkpoint", [
        ("The main deliverable of QA is:", ["Bugs found", "Evidence-based confidence about release risk", "Test scripts", "Bug-free software"], 1,
         "QA cannot prove the absence of bugs; it provides a reasoned risk judgement."),
        ("Which service desk skill maps MOST directly to defect reporting?", ["Password resets", "Writing clear ticket notes with steps and evidence", "Printer support", "Hardware imaging"], 1,
         "Both are precise, reproducible written records someone else must act on."),
        ("How many weeks is the QAReady roadmap?", ["12", "16", "24", "52"], 2, "Six months part-time at 8-10 h/week."),
        ("Which comes first in the plan?", ["Automation", "Manual test design", "Job applications", "Performance testing"], 1,
         "You must know what to check before you can code a reliable check of it."),
        ("A good framing for the career change is:", ["'I want fewer tickets'", "'I want to move upstream and prevent defects before release'", "'QA is easier'", "'I have no relevant skills'"], 1,
         "Progress, not escape."),
        ("If a study week slips, drop:", ["The deliverable", "The checkpoint quiz", "Stretch / optional reading", "The whole week"], 2,
         "Always ship the weekly artefact."),
    ]),
    quiz("foundations-quiz", "foundations", "Foundations checkpoint", [
        ("Which SDLC model explicitly pairs each dev stage with a test stage?", ["Waterfall", "V-Model", "Spiral", "Kanban"], 1, "V-Model: requirements↔acceptance, design↔system, code↔unit."),
        ("Which is NOT a testing principle?", ["Testing shows presence of defects", "Exhaustive testing is possible with enough time", "Defects cluster", "Pesticide paradox"], 1,
         "Exhaustive testing is impossible — that's the actual principle."),
        ("Given/When/Then is the syntax of:", ["SQL", "Gherkin / BDD", "HTTP", "Jira JQL"], 1, "Used for acceptance criteria and automated BDD scenarios."),
        ("System testing is primarily executed by:", ["Developers only", "QA Analyst end to end", "End users only", "DBAs"], 1, ""),
        ("Verification asks:", ["'Are we building the right product?'", "'Are we building the product right?'", "'Is it fast?'", "'Is it secure?'"], 1,
         "Validation = right product; verification = product right."),
        ("A 'test oracle' is:", ["A defect tracker", "How you decide whether a result is correct", "A test environment", "A senior tester"], 1, ""),
        ("STLC phase 6 is:", ["Requirement analysis", "Test execution", "Test cycle closure", "Test planning"], 2, "Closure produces the test summary report and sign-off."),
        ("'Shift-left' means:", ["Test later", "Test earlier in the lifecycle", "Move QA to another floor", "Only automate"], 1, ""),
    ]),
    quiz("test-design-quiz", "test-design", "Test design checkpoint", [
        ("For a range 10-20 inclusive, full 3-point BVA values are:", ["10, 15, 20", "9, 10, 11, 19, 20, 21", "9, 10, 20, 21", "10, 11, 19, 20"], 1, "L-1, L, L+1, U-1, U, U+1."),
        ("Equivalence partitioning is a:", ["White-box technique", "Black-box technique", "Performance technique", "Experience-based technique"], 1, ""),
        ("A decision table with 4 binary conditions has at most:", ["4 rules", "8 rules", "16 rules", "32 rules"], 2, "2^4 = 16 before collapsing."),
        ("Testing that a refunded order cannot be shipped is:", ["Boundary analysis", "An invalid state transition", "Pairwise testing", "Equivalence partitioning"], 1, ""),
        ("Pairwise testing covers:", ["Every combination", "Every pair of values from any two parameters", "Only boundaries", "Only invalid inputs"], 1, ""),
        ("Session-based exploratory testing uses a:", ["Test script", "Charter + time box + notes + debrief", "Decision table", "Full RTM"], 1, ""),
        ("Error guessing relies on:", ["Random clicks", "Tester experience and known weak spots", "Code coverage tools", "Requirements only"], 1, ""),
        ("Coverage of 90% is meaningless without knowing:", ["Who ran it", "Coverage of WHAT", "The time of day", "The tool name"], 1, ""),
    ]),
    quiz("test-docs-quiz", "test-docs", "Documentation checkpoint", [
        ("The most important quality of an expected result is that it is:", ["Short", "Specific and observable", "Written by a developer", "Optional"], 1, ""),
        ("A test that cannot run because staging is down is:", ["Failed", "Passed", "Blocked", "Skipped without reason"], 2, ""),
        ("An RTM links:", ["Devs to managers", "Requirements → tests → defects", "Browsers to OS", "Sprints to releases"], 1, ""),
        ("Which belongs in a test plan's OUT OF SCOPE section?", ["Payment testing", "'Legacy IE11 and load above 500 users are not tested'", "The test approach", "Exit criteria"], 1, ""),
        ("Risk is usually scored as:", ["Likelihood × impact", "Hours × testers", "Defects × builds", "Coverage × time"], 0, ""),
        ("A test strategy is:", ["Release-specific", "High-level and often organisation-wide", "Only for automation", "Written after release"], 1, ""),
        ("Which status is NOT a pass and NOT a fail?", ["Failed", "Blocked", "Passed", "Retest"], 1, ""),
        ("The final section of a test summary report should be:", ["A list of bugs", "Residual risk and a go/no-go recommendation", "The budget", "The tester's CV"], 1, ""),
    ]),
    quiz("defects-quiz", "defects", "Defect management checkpoint", [
        ("Severity is set primarily by:", ["Product Owner", "QA / tester (technical impact)", "Marketing", "The end user"], 1, "Priority is the PO's call."),
        ("A misspelled logo before a launch demo is:", ["Critical/P1", "Trivial severity / P1 priority", "Major/P4", "Trivial/P4"], 1, ""),
        ("Re-running the failed test case after a fix is:", ["Regression", "Confirmation retesting", "Smoke", "Exploratory"], 1, ""),
        ("A defect report must always include:", ["A suggested salary", "Environment/build and numbered repro steps", "A root cause proof", "The developer's name"], 1, ""),
        ("'First seen in build X; build X-1 was OK' indicates:", ["A duplicate", "A regression", "An enhancement", "A test data problem"], 1, ""),
        ("The best metric for test-design effectiveness is:", ["Bugs logged per tester", "Escaped defects", "Tests written", "Meetings held"], 1, ""),
        ("An intermittent defect report should quantify:", ["The developer's mood", "A repro rate like 3/10 attempts", "The release budget", "Nothing"], 1, ""),
        ("Four unrelated problems on one page should be:", ["One report", "Four reports", "Ignored", "A single severity"], 1, ""),
    ]),
]
