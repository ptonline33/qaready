"""Phase 1-2 courses: tools, web, SQL, CLI/Git, JavaScript."""
from . import lesson, course, quiz, mcq, inp, order, mdex, sqlex, P, table, QA_DB

# Extra mini database for aggregate exercises.
RUNS_DB = [
    {"name": "runs", "columns": ["id", "case_id", "ms", "status"], "rows": [
        [1, 101, 120, "Pass"],
        [2, 102, 340, "Fail"],
        [3, 104, 95, "Fail"],
        [4, 106, 210, "Pass"],
        [5, 108, 60, "Fail"],
    ]},
]

# ---------------------------------------------------------------------------
# 6. QA tools
# ---------------------------------------------------------------------------
TOOLS = course(
    "tools", "QA Tools & Workflows", "The toolchain, minus the mystique",
    "Jira and JQL for testers, test management tools, browser DevTools, capturing evidence, and understanding builds, environments and configuration.",
    "#3ee6ff", "p1", "Weeks 5-6", "Core",
    [
        lesson("tools-01", "Jira for QA: issues, workflows, JQL", 12,
               "Jira (or Azure Boards, Linear, YouTrack) is where work and defects live. A tester who can navigate it fluently — and write a useful query — is immediately more useful than one who can only click 'New'.",
               [
                 ("Issue types and fields a tester uses", """| Type | Use |
|---|---|
| **Story / Task** | The feature being built; holds acceptance criteria |
| **Bug / Defect** | A deviation from expected behaviour |
| **Test / Test Case** | In Jira with a test-management plugin (Zephyr, Xray) |
| **Sub-task** | 'Write test cases for PROJ-142' |
| **Epic** | A large theme containing many stories |

Fields that matter: **Summary, Description, Status, Assignee, Reporter, Priority, Severity (custom field), Fix Version/s, Affects Version/s, Environment, Labels/Components, Attachment, Links (blocks / is caused by / relates to), Sprint**. 'Affects Version' vs 'Fix Version' is how you answer *'which build did it break in, and which build fixes it?'* — gold for regression analysis."""),
                 ("Workflow and linking", """A typical workflow: `To Do → In Progress → In Review → Ready for Test → In Testing → Done`. Learn your team's exact transitions and **who** can move them. Use links deliberately:

- *DEF-1042 **is caused by** PROJ-142* (traceability)
- *DEF-1042 **blocks** TC-022* (explains a Blocked status)
- *DEF-1050 **duplicates** DEF-1042*

Add a comment with the build number, repro rate and environment when you change status. Never move a bug to Done yourself — **QA verifies, then closes**."""),
                 ("JQL you will actually use", """```sql
project = SHOP AND issuetype = Bug AND status != Done ORDER BY priority DESC
project = SHOP AND status = "Ready for Test" AND fixVersion = "2026.04.7"
project = SHOP AND issuetype = Bug AND severity in (Critical, Major)
  AND created >= -7d ORDER BY created DESC
assignee = currentUser() AND status = "In Testing"
text ~ "coupon" AND issuetype = Bug        -- full-text search
project = SHOP AND labels = regression AND status = Open
```

JQL (Jira Query Language) looks like SQL but is not SQL — no JOINs, different functions. Save the queries you use daily as **filters** and put them on a dashboard: 'My open bugs', 'Ready for retest in the current build', 'Open Criticals'. That dashboard is your morning stand-up prep."""),
               ],
               desk="You already live in a ticketing system. The new bits are the QA-specific issue types, 'Affects/Fix Version', defect links, and writing your own saved filters instead of relying on a queue someone else built.",
               takeaway="Know the workflow and who owns each transition; link defects to stories; learn 5 JQL filters; QA verifies before closing.",
               ex=[
                   mcq("Which field tells you which build a defect was FIRST observed in?", [
                       "Fix Version/s", "Affects Version/s", "Sprint", "Labels"], 1),
                   mcq("Who should close a verified defect?", [
                       "The reporter automatically", "QA after confirming the fix (per team workflow)", "The reporter's manager", "Nobody — bugs stay open"], 1),
                   inp("What is the name of Jira's query language (4 letters)?", ["JQL"], hint="Jira ... Language."),
                   mcq("Which JQL finds open Critical or Major bugs in project SHOP?", [
                       "project = SHOP", 'project = SHOP AND severity in (Critical, Major) AND status != Done', "SELECT * FROM bugs", "status = Open"], 1),
               ]),

        lesson("tools-02", "Test management tools", 11,
               "Test cases and results need a home. This lesson compares the options honestly — from a spreadsheet to TestRail, Zephyr, Xray and qTest — and shows what a good test run record looks like.",
               [
                 ("The options", table(
                     ["Tool", "Style", "Best for", "Trade-off"],
                     [["Spreadsheet (Excel/Sheets)", "Manual, free", "A first portfolio project, tiny teams", "No traceability, no audit trail, messy at scale"],
                      ["TestRail", "Dedicated SaaS test-case management", "Structured cases, runs, milestones, reports", "Paid; admin overhead"],
                      ["Zephyr / Xray", "Jira plugin — tests live as issues", "Teams already deep in Jira; link to stories", "Can get noisy; licensing"],
                      ["qTest / PractiTest / TestLink", "Enterprise / open source", "Regulated, audit-heavy environments", "Heavier setup"],
                      ["Markdown in Git", "Plain-text cases versioned with code", "Automation-heavy teams, portfolios", "No built-in run history"],
                      ["Cucumber / Gherkin feature files", "Executable specifications", "BDD teams", "Requires automation discipline"]])),
                 ("The hierarchy in any test tool", """Almost every tool uses the same shape:

```
Project
 └── Test Suite (e.g. 'Auth')
      └── Test Case (TC_AUTH_014 ...)
           └── Test Run / Execution (who, when, build, status, actual result)
                └── Defect link
```

A **test case** is the reusable definition; a **test run** (or *test execution*) is one instance of running it against one build. Never overwrite a previous run's result — history is how you prove a regression and satisfy an auditor. Configure **custom fields** for build number, browser, environment and requirement ID."""),
                 ("What to record per run", """Test case ID/version, **build/version**, environment (URL, browser+version, OS, device), tester, timestamp, status, actual result (verbatim), any defect IDs, and evidence attachments. If your tool supports **test plans / milestones**, group runs per release so you can produce the execution summary without manual counting."""),
               ],
               desk="A well-kept ticket history is an audit trail. Same idea: don't overwrite what happened; add a new run so the story can be reconstructed.",
               takeaway="Case ≠ run. Every execution records build, environment, tester, status, evidence and defect links. Start with a spreadsheet; graduate to a real tool.",
               ex=[
                   mcq("What is the difference between a test case and a test run?", [
                       "None", "The case is the reusable definition; the run is one execution against one build", "A run is a folder of cases", "A case is only for automation"], 1),
                   mcq("Which tool keeps tests as Jira issues alongside stories?", [
                       "TestRail", "Zephyr / Xray", "Excel", "Postman"], 1),
                   mcq("Why keep historical run results instead of overwriting them?", [
                       "Storage is cheap", "To prove regressions, trends and audit trails", "The tool requires it", "To make reports longer"], 1),
               ]),

        lesson("tools-03", "Browser DevTools for testers", 13,
               "DevTools turns a vague 'the page is broken' into precise evidence. You do not need to be a developer to use the four panels that matter: Elements, Console, Network and Application.",
               [
                 ("The four panels", """Open with `F12` / `Ctrl+Shift+I` (Windows) or `Cmd+Opt+I` (Mac).

| Panel | What it shows | How a tester uses it |
|---|---|---|
| **Elements** | Live DOM + CSS | Inspect an element, confirm the selector/locator, check hidden/disabled attributes, see computed styles, verify text and ARIA labels |
| **Console** | JS errors, warnings, logs | Copy the exact error and stack trace into the defect report; run a quick read-only JS expression |
| **Network** | Every HTTP request/response | Check status codes, request payload, response body, timing, failed/cancelled requests, and *Save all as HAR* |
| **Application / Storage** | Cookies, localStorage, sessionStorage, service workers, cache | Reproduce auth/session bugs, clear state to get a clean test, verify a cookie's flags |"""),
                 ("Three high-value moves", """1. **Preserve log + disable cache** (Network tab) so refreshes and redirects don't erase the evidence.
2. **Right-click a failed request → Copy → Copy as cURL**, then paste it into Postman to reproduce the API call independently of the UI. This is how you discover whether a bug is front-end or back-end.
3. **Throttle** the network (Fast 3G / offline) to reproduce timeouts, duplicate submits, and loading-state defects.

Also useful: the **device toolbar** for responsive/mobile viewport checks, `Ctrl+Shift+P` → 'Screenshot' → *Capture full size screenshot*, and the **Accessibility / Lighthouse** panel for a first-pass a11y audit."""),
                 ("Front-end or back-end? The 30-second triage", """When a page shows wrong data:

- Network request returned **wrong data** → back-end / API / DB defect. Attach the response body.
- Response is **correct** but the page shows something else → front-end rendering/state defect. Attach the response + a screenshot.
- Request **never fired** or has a wrong payload → front-end or client-side validation defect.
- **4xx/5xx** → attach status, URL, payload, and any `request-id` header.

That single distinction makes your report dramatically more actionable, and it is a classic interview answer."""),
               ],
               desk="You've collected logs and error messages for escalations. DevTools is the same skill one layer closer to the code — and the HAR file is the equivalent of attaching the full log bundle.",
               takeaway="Elements for locators, Console for errors, Network for status/payload/timing, Application for state. Use HAR + Copy as cURL to split UI vs API bugs.",
               ex=[
                   mcq("The API response contains the correct total but the page displays a different one. The defect is most likely:", [
                       "Back-end / database", "Front-end rendering or state", "A network outage", "A DNS problem"], 1),
                   mcq("Which DevTools panel shows cookies, localStorage and service workers?", [
                       "Elements", "Console", "Network", "Application / Storage"], 3),
                   inp("What file format captures ALL network requests and responses as evidence?", ["HAR", "har"], hint="HTTP ARchive — save all as ... with content."),
                   mcq("'Copy as cURL' is useful because it lets you:", [
                       "Fix the bug", "Reproduce the exact API request in Postman independently of the UI", "Change the database", "Screenshot the page"], 1),
               ]),

        lesson("tools-04", "Evidence: screenshots, logs and HAR files", 10,
               "Good evidence makes a defect report undeniable and reproducible. This lesson covers what to capture, how to label it, and the mistakes that make evidence useless.",
               [
                 ("A capture checklist", """- **Screenshot**: full page (not a cropped phone photo), with the URL bar and, if relevant, the browser/version visible. Annotate the exact area (arrow/box) and redact personal data.
- **Screen recording**: essential for intermittent, timing, animation and sequence bugs. Keep it short (10-30 s).
- **Console log**: copy the text, don't just screenshot it — text is searchable and copyable.
- **HAR file**: full network trace with content, for API/performance/timing issues.
- **Server logs**: timestamps, request IDs/correlation IDs, environment name.
- **Context block**: build, environment URL, user/role, test data, timestamp (with timezone!), browser/OS, feature flags."""),
                 ("Make it findable and safe", """Name files consistently: `DEF-1042_cart-total_chrome125_2026-04-07.png`. Attach to the ticket, not to a chat message that disappears. **Never paste real customer data, credentials, tokens or session cookies** into a ticket or screenshot — use synthetic/masked data. If you must show an auth header, redact it. A defect tracker is often visible to far more people than you think."""),
                 ("Describe the evidence in words too", """A screenshot alone is not a report. Write: *'Step 4: the order summary shows $96.00 (see cart-1042.png, highlighted); the API response in cart-1042.har also returns 96.00.'* Text makes the evidence searchable, accessible to screen readers, and understandable when an image fails to load."""),
               ],
               desk="You already know that an escalation without logs bounces straight back. This is that lesson, extended to HAR files and console text.",
               takeaway="Capture full context, annotate, redact, name consistently, attach to the ticket, and describe the evidence in text as well.",
               ex=[
                   mcq("Which of these should NEVER appear unredacted in a defect ticket?", [
                       "The build number", "A real session token / customer PII", "The repro steps", "The browser version"], 1),
                   mcq("Why also describe a screenshot in words?", [
                       "Screenshots are forbidden", "Text is searchable, accessible, and survives a broken image", "Developers can't see images", "It increases severity"], 1),
                   mcq("For an intermittent animation glitch, the best extra evidence is:", [
                       "A HAR file only", "A short screen recording plus a repro rate", "A spreadsheet", "A console log only"], 1),
               ]),

        lesson("tools-05", "Builds, environments and configuration", 11,
               "'Works on my machine' is an environment problem, not an opinion. Understanding the path from code to a testable build stops you wasting a day testing the wrong thing.",
               [
                 ("The environment ladder", """```
Developer local  →  CI build  →  Dev / Integration  →  Staging / QA  →  Production
```
Each environment has its own **URL, database, config, feature flags, third-party integrations and credentials**. A defect may exist in only one of them. Always record which environment you tested. **Never** test against production, and never use production data in staging."""),
                 ("Builds, versioning and smoke tests", """A **build** is a numbered, deployable artefact (`2026.04.7`, or a commit SHA like `a3f9c21`). Record the exact build in every test result and defect. When a build lands in staging:

1. Check the release notes / changelog for what changed (drives regression selection).
2. Run the **smoke suite** — 5-15 quick checks of core paths (app loads, login, one key transaction, logout).
3. If smoke fails, **reject the build** and report it rather than starting deep testing on a broken artefact.

This 'build verification test' (BVT) saves enormous time and is a standard interview answer to 'what do you do first when a new build arrives?'"""),
                 ("Configuration, flags and test doubles", """Modern apps are heavily driven by **feature flags** (`NEW_PRICING=on`), config files, environment variables, and third-party services. Two testers can see different behaviour with the same build because their flags differ — always capture flag state.

When a dependency is unavailable (payment gateway, email service, tax API), teams use **stubs / mocks / simulators**: a fake service returning controlled responses. Know which ones are in play, because a 'pass' against a mock is *not* a pass against the real integration — note that as residual risk."""),
               ],
               desk="'It works in the office but not on the VPN' is an environment/config difference. Same root cause, new vocabulary: build, flag, environment, mock.",
               takeaway="Record build + environment + flags; smoke-test every new build; reject broken builds; note mocked integrations as residual risk.",
               ex=[
                   mcq("What should you do FIRST when a new build is deployed to staging?", [
                       "Start the full regression suite", "Run a short smoke / build verification suite and check the changelog", "Log a defect", "Ask for a new build"], 1),
                   mcq("Two testers see different behaviour on the same build. Most likely cause:", [
                       "Different feature flags / config / data", "A virus", "The build number is wrong", "Browser fonts"], 0),
                   mcq("A test passes against a mocked payment gateway. What should the summary note?", [
                       "Nothing — it passed", "That real integration remains untested (residual risk)", "That the defect is Critical", "That testing is complete"], 1),
               ]),
    ],
    quiz="tools-quiz",
)

# ---------------------------------------------------------------------------
# 7. How the web works
# ---------------------------------------------------------------------------
WEB = course(
    "web", "How the Web Works", "Test below the surface",
    "From zero: client-server, DNS, HTTP request/response, methods and status codes, headers/cookies, HTML/CSS/JS basics, and reading the Network panel like a tester.",
    "#4f8cff", "p2", "Weeks 7-8", "Foundational",
    [
        lesson("web-01", "Client, server, DNS and the request/response cycle", 12,
               "Every click in a browser triggers a conversation between two computers. Understanding that conversation is what lets you test an application instead of just a screen.",
               [
                 ("The journey of one click", """1. You type `https://shop.example.com/cart`.
2. **DNS** resolves the hostname to an IP address (like a phone book for the internet).
3. The browser opens a **TCP** connection (and a **TLS** handshake for HTTPS — encryption and certificate validation).
4. The browser sends an **HTTP request**: a method, a path, headers, and optionally a body.
5. The **server** (application + database + other services) processes it.
6. The server returns an **HTTP response**: a status code, headers, and a body (HTML, JSON, an image...).
7. The browser renders the body, runs JavaScript, and fires more requests for CSS, JS, images and API calls.

A single page can easily make 50+ requests. **The UI is just the last 10% of the story** — which is why QA must look at the network and the data, not only the pixels."""),
                 ("Client-side vs server-side", """| | Client (browser / app) | Server |
|---|---|---|
| Runs | HTML/CSS/JavaScript | Application code, business rules, DB queries |
| Owns | Rendering, form validation, local state, cookies | Authentication, authorisation, data, pricing, persistence |
| Can be changed by | **The user** (DevTools, proxies, disabled JS) | Only the team |

**Golden rule of testing:** client-side validation is a convenience, not a security control. Always verify that the *server* rejects invalid data too — send the bad request directly with Postman/cURL. This is one of the highest-value tests a QA Analyst can add."""),
                 ("Three-tier mental model", """```
Presentation (browser/UI)
      ↓ HTTP
Application / API (business logic)
      ↓ SQL
Database (persistent state)
```

When a defect appears, localise it by layer: does the request go out with the right payload? does the response contain the right data? does the DB row match? That triage is exactly how you'll split UI bugs from API bugs from data bugs — and it maps to the unit/integration/system levels from Foundations."""),
               ],
               desk="You already ask 'is it the client, the network, or the server?' when diagnosing a ticket. This lesson just gives you the exact names and the order of the hops.",
               takeaway="DNS → TCP/TLS → request → server+DB → response → render. Trust server-side validation; localise defects by layer.",
               ex=[
                   mcq("What does DNS do?", [
                       "Encrypts the connection", "Translates a hostname into an IP address", "Stores cookies", "Renders HTML"], 1),
                   mcq("Why must you re-test validation at the server/API level?", [
                       "Browsers are slow", "Client-side validation can be bypassed or disabled", "Servers are always correct", "It's required by HTML"], 1),
                   order("Put the three-tier model from user to data in order:", [
                       "Presentation (browser UI)", "Application / API (business logic)", "Database (persistent state)"]),
               ]),

        lesson("web-02", "HTTP methods, status codes and headers", 14,
               "HTTP is the vocabulary of the web and of API testing. Learn the methods, the status code families, and the headers that matter — this lesson is reused constantly in the API and Postman courses.",
               [
                 ("Methods and what they mean", """| Method | Intent | Safe? | Idempotent? | Typical use |
|---|---|---|---|---|
| `GET` | Read a resource | Yes | Yes | Fetch a user, list orders |
| `POST` | Create / submit / trigger | No | No | Create order, log in |
| `PUT` | Replace a whole resource | No | **Yes** | Update entire profile |
| `PATCH` | Partially update | No | Not guaranteed | Change one field |
| `DELETE` | Remove | No | Yes | Delete a record |
| `OPTIONS` | Ask what's allowed / CORS preflight | Yes | Yes | Browser preflight |

**Safe** = no state change. **Idempotent** = repeating the call has the same effect as once (`PUT`/`DELETE` yes, `POST` no — double-submitting an order creates two orders). That distinction is a favourite API interview question and a great source of test cases: *what happens if the user clicks Pay twice?*"""),
                 ("Status code families", """| Range | Meaning | Codes a tester must know |
|---|---|---|
| **1xx** | Informational | 100 Continue |
| **2xx** | Success | 200 OK, **201 Created**, **204 No Content**, 202 Accepted |
| **3xx** | Redirection | 301/302 redirect, **304 Not Modified** (cache), 307/308 |
| **4xx** | **Client** error | **400 Bad Request**, **401 Unauthenticated**, **403 Forbidden**, **404 Not Found**, **405 Method Not Allowed**, **409 Conflict**, **422 Unprocessable Entity**, **429 Too Many Requests** |
| **5xx** | **Server** error | **500 Internal Server Error**, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout |

The 401 vs 403 distinction is examined constantly: **401 = you haven't identified yourself** (missing/invalid token); **403 = we know who you are but you're not allowed** (valid token, wrong role). A 400 means the request was malformed; a 422 means it was well-formed but semantically invalid (e.g. email missing an @)."""),
                 ("Headers and bodies", """Request headers: `Content-Type: application/json`, `Authorization: Bearer <token>`, `Accept`, `Cookie`, `User-Agent`, `X-Request-ID`. Response headers: `Content-Type`, `Set-Cookie`, `Cache-Control`, `Location` (for redirects), `Access-Control-Allow-*` (CORS), `RateLimit-*`.

A **body** carries data, commonly JSON. `Content-Type` tells the server how to parse it — a mismatch (`text/plain` body labelled `application/json`) is a classic 400/415 cause. Cookies ride in headers: the server sets them with `Set-Cookie`, the browser sends them back with `Cookie`."""),
               ],
               desk="401/403 and 4xx/5xx are the web version of 'user error vs permission vs system fault'. You already make that call; now you can quote the exact code in a bug report.",
               takeaway="GET/POST/PUT/PATCH/DELETE + safe/idempotent; 2xx success, 3xx redirect, 4xx client, 5xx server; 401 vs 403 is essential.",
               ex=[
                   mcq("A valid token but insufficient permissions returns:", [
                       "400", "401", "403", "500"], 2, "401 = not authenticated; 403 = authenticated but forbidden."),
                   mcq("Which method is NOT idempotent?", [
                       "GET", "PUT", "DELETE", "POST"], 3, "Repeating a POST can create multiple resources."),
                   mcq("201 Created means:", [
                       "The request was cached", "A resource was successfully created", "The client made a mistake", "The server crashed"], 1),
                   mcq("A '304 Not Modified' response relates to:", [
                       "Authentication", "Caching", "A database error", "Rate limiting"], 1),
                   inp("Which header commonly carries a bearer token? (13 letters, one word)", ["Authorization", "authorization"], hint="It starts with 'A'."),
               ]),

        lesson("web-03", "HTML, CSS and JavaScript basics for testers", 12,
               "You do not need to be a front-end developer, but you do need to read a page's structure well enough to write good locators, spot accessibility problems, and understand what the browser is doing.",
               [
                 ("HTML: structure and attributes", """```html
<form id="login-form">
  <label for="email">Email</label>
  <input id="email" name="email" type="email" required aria-describedby="email-hint">
  <button type="submit" data-testid="signin-btn" disabled>Sign in</button>
</form>
```

Key ideas: **elements** (`input`, `button`), **attributes** (`id`, `name`, `type`, `required`, `disabled`, `aria-*`), and the **DOM** — the live tree the browser builds. Attributes a tester cares about: `id`/`name` (stable locators), `data-testid` (a locator added specifically for tests), `disabled`/`readonly`/`hidden` (state), `aria-label` (accessible name), `type` and `pattern` (client validation). A `<label for="email">` correctly associated with its input is both an accessibility win and a locator hint."""),
                 ("CSS and selectors (the minimum)", """CSS selects elements to style them; test automation reuses the same selector language:

| Selector | Matches |
|---|---|
| `#email` | id="email" |
| `.btn-primary` | class contains btn-primary |
| `button[type="submit"]` | submit buttons |
| `[data-testid="signin-btn"]` | a test-specific attribute |
| `form input:disabled` | disabled inputs inside a form |

**Brittle locators** (long XPath like `/html/body/div[3]/div[2]/...`, or nth-child chains) break whenever the layout changes. Prefer **user-facing locators** — role, label, text — or a `data-testid`. That preference is the foundation of Playwright later."""),
                 ("JavaScript: what a tester must know", """JavaScript makes the page dynamic: it handles clicks, validates forms, calls APIs with `fetch`, updates the DOM, and stores state. You should be able to read a line like `document.querySelector('#email').value` and understand it fetches what the user typed. You'll learn JS properly in the Programming course; for now, know that:

- JS can **change the DOM after load** (so the HTML you see in View Source differs from Elements in DevTools — Elements shows the *live* DOM).
- JS errors appear in the **Console** and can silently break a feature.
- JS can be **disabled**, so server-side checks must still hold.
- Async behaviour (`fetch`, promises) explains loading spinners, race conditions, and why a click sometimes 'does nothing yet'."""),
               ],
               desk="'View Source vs right-click Inspect shows different HTML' has confused many an escalation. Now you know why: JavaScript rewrote the live DOM.",
               takeaway="Read elements/attributes, prefer role/label/testid locators over brittle XPath, know that JS mutates the DOM and can fail silently.",
               ex=[
                   mcq("Which locator is most resilient to layout changes?", [
                       "/html/body/div[3]/div[2]/button", "[data-testid='signin-btn'] or getByRole('button', {name: 'Sign in'})", "div:nth-child(7)", "A pixel coordinate"], 1),
                   mcq("The Elements panel differs from 'View Source' because:", [
                       "The server sent different HTML", "JavaScript has modified the live DOM after load", "CSS hides it", "The browser caches source"], 1),
                   mcq("What does `aria-label` primarily provide?", [
                       "A CSS class", "An accessible name for assistive technology", "A faster load time", "A database index"], 1),
               ]),

        lesson("web-04", "Reading the Network panel like a tester", 12,
               "The Network panel is where you prove what the application actually sent and received. This lesson turns it into a repeatable triage routine.",
               [
                 ("What to look at, in order", """1. **Filter** by `Fetch/XHR` to hide images and see API calls.
2. Tick **Preserve log** (survives navigation) and **Disable cache**.
3. For the failing action, find the request: check **Status**, **Method**, **Domain**, and **Time**.
4. Open **Headers** → note request URL, method, `Content-Type`, `Authorization`, and any `X-Request-ID`.
5. Open **Payload / Request** → was the data the UI sent correct? (e.g. did it send `quantity: -1`?)
6. Open **Response / Preview** → was the data returned correct?
7. Check **Timing** → is it slow (TTFB vs download vs waiting)?
8. Right-click → **Save all as HAR with content** for the ticket, or **Copy as cURL** for Postman."""),
                 ("A concrete triage example", """Symptom: *'Applying coupon SAVE10 shows the wrong total.'*

- Request: `POST /api/cart/total` with `{"items":[{"sku":"SKU-88"}],"coupon":"SAVE10"}` → payload correct.
- Response: `200 {"total":96.00}` → the server computed the wrong number.
- **Verdict:** back-end pricing defect. Attach the payload, the response and the request ID. Contrast: if the response were `{"total":108.00}` but the page showed 96.00, it would be a front-end defect.

This 3-line distinction is the single fastest way to look competent in a QA interview and on the job."""),
                 ("Failure signatures", """| What you see | Likely meaning |
|---|---|
| Request in red with `(failed)` / `net::ERR_*` | Network/CORS/DNS/offline, no response received |
| `4xx` | Client sent something wrong — check payload, token, method |
| `5xx` | Server error — grab the `X-Request-ID` for the logs |
| CORS error in Console | Cross-origin policy; often a config defect |
| `OPTIONS` then no follow-up | Preflight rejected |
| Status `200` but empty/wrong body | Application logic defect, not transport |
| Two identical `POST`s on one click | Missing debounce → duplicate-order risk |"""),
               ],
               desk="Attaching an HAR is the web equivalent of attaching the full event log bundle to an escalation. Same instinct, richer evidence.",
               takeaway="Preserve log → check method/status/payload/response/timing → decide UI vs API vs data → attach HAR or cURL.",
               ex=[
                   mcq("The API returns the correct data but the UI shows wrong data. Verdict:", [
                       "Back-end defect", "Front-end defect", "DNS failure", "Database corruption"], 1),
                   mcq("A request appears in red as `(failed)` with `net::ERR_CONNECTION_RESET` and no response. This is:", [
                       "A 500 error", "A transport/network-level failure, not an HTTP status", "A successful cached response", "A 404"], 1),
                   inp("Which filter in the Network panel isolates API calls?", ["Fetch/XHR", "XHR", "Fetch"], hint="Two labels joined by a slash."),
               ]),

        lesson("web-05", "Sessions, cookies, cache and auth basics", 11,
               "A surprising number of bugs are really *state* bugs: stale cache, an expired session, a cookie with the wrong flags. Understanding browser state makes you much better at reproducing them.",
               [
                 ("Cookies and sessions", """A **cookie** is a small piece of data the server sets with `Set-Cookie` and the browser sends back automatically on later requests. A **session** is server-side state identified by a session ID in that cookie. Authentication flows (login → token → cookie → subsequent authorised requests) are the most common source of state bugs.

Cookie flags worth checking in the Application panel: `HttpOnly` (JS can't read it — protects against XSS theft), `Secure` (only over HTTPS), `SameSite` (CSRF protection), `Expires`/`Max-Age`, and `Domain`/`Path` (scope). A tester should verify that logging out actually invalidates the session server-side, not just deletes the cookie in the browser."""),
                 ("Tokens, localStorage and JWT", """Modern apps often use a **JWT (JSON Web Token)** sent in `Authorization: Bearer <token>` instead of a session cookie. Tokens may live in memory, localStorage, or a cookie. Check: is the token still accepted after logout / password change / expiry? Does a token for a deleted or downgraded user still grant access? (Never store sensitive tokens where any script can read them without reason.)"""),
                 ("Cache, and the tests it breaks", """Caching happens at many layers: browser (memory/disk, `Cache-Control`, ETag/304), CDN, service worker, application, and DB/query cache. Symptoms: *'I deployed the fix but users still see the old page'*, or *'it works in a private window'*. Test with **hard reload**, **disable cache**, a **fresh/incognito profile**, and cache-busting query strings. Clear site data between test runs when a case depends on a clean state.

A related class: **back/refresh/duplicate tab** bugs. Browser Back after logout, refreshing a POST (the 'Confirm form resubmission' dialog), and two tabs editing the same record all produce real defects."""),
               ],
               desk="'Have you tried a hard refresh / incognito / clearing cookies?' is the first thing you ask on the desk — because cache and session state cause a huge share of 'broken' reports. Now you know exactly why each one works.",
               takeaway="Auth state lives in cookies/tokens; check flags and invalidation; cache causes stale-build bugs; always test Back, refresh and clean-profile scenarios.",
               ex=[
                   mcq("What does the `HttpOnly` cookie flag do?", [
                       "Forces HTTPS", "Prevents JavaScript from reading the cookie (XSS mitigation)", "Sets the expiry", "Blocks third parties"], 1),
                   mcq("After logout, what MUST be verified?", [
                       "That the browser deleted the cookie", "That the server actually invalidated the session/token", "That CSS reloaded", "That the URL changed"], 1,
                       "Deleting a cookie client-side is not logout if the token is still valid."),
                   mcq("A fix is deployed but users still see the old page. First suspect:", [
                       "A database crash", "Browser/CDN caching", "A DNS outage", "A 500 error"], 1),
               ]),
    ],
    quiz="web-quiz",
)

# ---------------------------------------------------------------------------
# 8. SQL for testers
# ---------------------------------------------------------------------------
SQL = course(
    "sql", "SQL for Testers", "Query the truth behind the UI",
    "From zero: relational concepts, SELECT/WHERE, filtering and NULLs, aggregates and GROUP BY, JOINs, safe writes and transactions, and using SQL to verify test results. Includes a runnable in-browser SQL engine.",
    "#7b5cff", "p2", "Weeks 8-10", "Foundational",
    [
        lesson("sql-01", "Tables, rows, keys and relationships", 11,
               "A relational database stores data in tables. Knowing the shape of the data is prerequisite to every verification query you'll write — and to understanding why a test failed.",
               [
                 ("The vocabulary", """| Concept | Meaning |
|---|---|
| **Table / relation** | A named collection of rows (e.g. `test_cases`) |
| **Column / field** | A typed attribute (`id`, `status`) |
| **Row / record** | One entity instance |
| **Primary key (PK)** | Unique identifier for a row (`id`) |
| **Foreign key (FK)** | A column referencing another table's PK (`owner_id` → `testers.id`) |
| **NULL** | *Unknown / no value* — not zero, not empty string, not false |
| **Schema** | The structure: tables, columns, types, constraints |
| **Index** | A structure that speeds up lookups |

Our practice database (used by the runnable exercises) has three tables:

```
testers(id, name, team, active)
test_cases(id, title, module, priority, status, owner_id)
defects(id, test_case_id, severity, status, assignee_id)
```

`test_cases.owner_id` → `testers.id`; `defects.test_case_id` → `test_cases.id`. That's a chain you can join across."""),
                 ("Why testers query databases", """The UI can lie (or at least hide things). SQL lets you verify **persistence**: did the order row actually get created? is the `status` really 'Paid'? was the discount written to the DB, or only displayed? did the soft-delete flag get set? is the audit log complete? You also use SQL to **create test data**, **clean up** after tests, and **count** things for reports.

> **From the desk:** you've probably already run a query to check whether a ticket's status in the UI matches the underlying record. That is exactly back-end verification."""),
                 ("NULL is special", """`NULL` means 'unknown'. Comparisons with it are not true or false — they are *unknown*, so `status = NULL` never matches anything. Use `IS NULL` / `IS NOT NULL`. Also `COUNT(*)` counts rows including NULLs, while `COUNT(column)` counts only non-NULL values in that column. This trips up almost everyone once."""),
               ],
               desk="You already know a ticket's 'status' in the UI is just a view of a database field. SQL is how you check the field directly.",
               takeaway="Tables → rows → keys; FK links tables; NULL is unknown, use IS NULL; SQL verifies persistence, not just display.",
               ex=[
                   mcq("What is a foreign key?", [
                       "A key that is broken", "A column referencing another table's primary key", "An encrypted column", "A backup key"], 1),
                   mcq("Which condition finds rows with no assignee?", [
                       "assignee_id = NULL", "assignee_id IS NULL", "assignee_id = 0", "assignee_id = ''"], 1,
                       "NULL comparisons are unknown; use IS NULL."),
                   mcq("Why would a tester query the database after a UI action?", [
                       "To make the UI faster", "To verify the data was actually persisted correctly", "To change the browser", "To avoid writing test cases"], 1),
                   sqlex("List the names of all testers.", "SELECT name FROM testers", {"columns": ["name"], "rows": [["Asha"], ["Ben"], ["Cy"], ["Dee"], ["Eli"]]},
                         explain="SELECT picks columns; FROM names the table."),
               ]),

        lesson("sql-02", "SELECT, WHERE, ORDER BY, LIMIT", 12,
               "The core query pattern you'll use dozens of times a day. The exercises below run in a real (mini) SQL engine inside this app — type a query and press Run.",
               [
                 ("The shape of a query", """```sql
SELECT id, title, status          -- which columns
FROM test_cases                   -- which table
WHERE priority = 'High'           -- which rows
ORDER BY id DESC                  -- which order
LIMIT 5;                          -- how many
```

The **logical** order of execution is `FROM → WHERE → SELECT → ORDER BY → LIMIT`, even though you write SELECT first. Remembering that explains why you cannot use a SELECT alias inside WHERE, but can in ORDER BY."""),
                 ("Comparisons and logic", """Operators: `=`, `!=` or `<>`, `<`, `>`, `<=`, `>=`, plus `AND`, `OR`, `NOT`, and parentheses for grouping. String literals use single quotes: `'High'`. Numbers are unquoted: `id >= 105`.

```sql
SELECT title FROM test_cases
WHERE module = 'Cart' AND status != 'Blocked';

SELECT id, severity FROM defects
WHERE severity = 'Critical' OR severity = 'Major';
```

**Parentheses matter:** `WHERE status = 'Failed' AND (module = 'Cart' OR module = 'Auth')` is very different from the same expression without brackets. When in doubt, bracket it."""),
                 ("Sorting and limiting", """`ORDER BY column ASC` (default) or `DESC`. `LIMIT n` returns the first n rows — combine it with `ORDER BY` for 'the 5 most recent' / 'the highest'. Without ORDER BY, row order is **not guaranteed**; never write a test that depends on unsorted database order."""),
               ],
               desk="Filtering a ticket queue by status/priority is a WHERE clause with AND/OR. You've been writing SQL logic in a GUI for years.",
               takeaway="SELECT … FROM … WHERE … ORDER BY … LIMIT …; quote strings, bracket logic, never rely on implicit row order.",
               ex=[
                   sqlex("List the titles of every High-priority test case.",
                         "SELECT title FROM test_cases WHERE priority = 'High'",
                         {"columns": ["title"], "rows": [
                             ["Login with valid credentials"], ["Login with locked account"],
                             ["Cart total with discount"], ["Checkout as guest"]]},
                         hint="Use single quotes around the string 'High'."),
                   sqlex("Show the id and title of all Failed test cases.",
                         "SELECT id, title FROM test_cases WHERE status = 'Failed'",
                         {"columns": ["id", "title"], "rows": [
                             [102, "Login with locked account"], [104, "Cart total with discount"],
                             [108, "Apply invalid coupon"]]}),
                   sqlex("Show open defect ids and severities, newest id first.",
                         "SELECT id, severity FROM defects WHERE status = 'Open' ORDER BY id DESC",
                         {"columns": ["id", "severity"], "rows": [[506, "Major"], [502, "Major"], [501, "Critical"]]}),
                   mcq("Which is the logical execution order?", [
                       "SELECT → FROM → WHERE → ORDER BY", "FROM → WHERE → SELECT → ORDER BY → LIMIT", "WHERE → SELECT → FROM", "LIMIT → ORDER BY → SELECT"], 1),
               ]),

        lesson("sql-03", "Filtering: IN, BETWEEN, LIKE, DISTINCT, NULL", 12,
               "Real test data needs richer filters. This lesson adds the operators that make queries concise and shows the classic NULL traps.",
               [
                 ("The operators", """```sql
WHERE team IN ('Web', 'API')                  -- any of a list
WHERE id BETWEEN 103 AND 105                  -- inclusive range
WHERE title LIKE 'Login%'                     -- % = any chars, _ = one char
WHERE module NOT IN ('Auth')                  -- exclude
WHERE assignee_id IS NULL                     -- unknown / unassigned
WHERE assignee_id IS NOT NULL                 -- has a value
SELECT DISTINCT module FROM test_cases        -- unique values only
```

`LIKE` patterns: `'%cart%'` contains cart, `'Login%'` starts with Login, `'%_v2'` one char before `_v2`. `BETWEEN` is **inclusive** on both ends — a nice tie-in to boundary value analysis: test the two endpoints.

> **Trap:** `NOT IN` with a NULL in the list can produce no rows at all, because comparison with NULL is unknown. Prefer explicit `<>` conditions or `IS NOT NULL` filters when NULLs are around."""),
                 ("A tester's filtering use cases", """- Find all cases owned by one team: `WHERE owner_id IN (SELECT ...)` — subqueries live in the next lesson; for now join instead.
- Find unassigned defects for triage: `WHERE assignee_id IS NULL`.
- Find cases created in a build range: `WHERE id BETWEEN 103 AND 108`.
- Find all distinct modules to build a regression filter: `SELECT DISTINCT module`.
- Spot data quality problems: `WHERE status = '' OR status IS NULL`."""),
                 ("NULL and aggregates", """`COUNT(*)` counts rows (8 in `test_cases`). `COUNT(assignee_id)` in `defects` counts only non-NULL values (5, because one defect is unassigned). `SUM`/`AVG` ignore NULLs entirely. So 'how many defects have an assignee?' needs `COUNT(assignee_id)` or a `WHERE assignee_id IS NOT NULL` — a subtle but common reporting bug."""),
               ],
               desk="'Show me all tickets with no assignee' is `IS NULL`. You've built that filter in a GUI; now you can write it and spot why `= NULL` returns nothing.",
               takeaway="IN / BETWEEN (inclusive) / LIKE / DISTINCT / IS NULL. NULL is unknown; COUNT(col) skips NULLs.",
               ex=[
                   sqlex("List the names of testers whose team is Web or API, using IN.",
                         "SELECT name FROM testers WHERE team IN ('Web', 'API')",
                         {"columns": ["name"], "rows": [["Asha"], ["Ben"], ["Cy"], ["Eli"]]},
                         hint="IN ('Web', 'API')"),
                   sqlex("Show the titles of test cases whose title starts with 'Login'.",
                         "SELECT title FROM test_cases WHERE title LIKE 'Login%'",
                         {"columns": ["title"], "rows": [["Login with valid credentials"], ["Login with locked account"]]},
                         hint="LIKE 'Login%'"),
                   sqlex("Find the ids of defects that have no assignee.",
                         "SELECT id FROM defects WHERE assignee_id IS NULL",
                         {"columns": ["id"], "rows": [[506]]},
                         explain="One defect is deliberately unassigned."),
                   sqlex("List each distinct module in test_cases.",
                         "SELECT DISTINCT module FROM test_cases",
                         {"columns": ["module"], "rows": [["Auth"], ["Cart"], ["Search"], ["Checkout"]]}),
                   mcq("`BETWEEN 103 AND 105` includes which ids?", [
                       "104 only", "103, 104, 105", "103 and 105 only", "everything above 103"], 1, "Inclusive both ends."),
               ]),

        lesson("sql-04", "Aggregates, GROUP BY and HAVING", 13,
               "Counting and summarising is how QA produces metrics: passes per module, defects per severity, average response time. Learn the aggregate functions and the grouping rules that make them meaningful.",
               [
                 ("Aggregate functions", """| Function | Result |
|---|---|
| `COUNT(*)` | Number of rows |
| `COUNT(col)` | Number of non-NULL values in col |
| `SUM(col)` | Total |
| `AVG(col)` | Mean (ignores NULLs) |
| `MIN(col)` / `MAX(col)` | Smallest / largest |

```sql
SELECT COUNT(*) FROM test_cases;                       -- 8
SELECT COUNT(*) FROM defects WHERE severity = 'Major'; -- 3
```

Without GROUP BY, an aggregate collapses the whole result into **one row**."""),
                 ("GROUP BY", """`GROUP BY` splits rows into buckets and applies the aggregate *per bucket*:

```sql
SELECT status, COUNT(*) FROM test_cases GROUP BY status;
```

produces one row per distinct status. The rule: **every non-aggregated column in SELECT must appear in GROUP BY**. Selecting `title, COUNT(*)` without grouping by `title` is invalid SQL (or produces an arbitrary value in lax engines).

```sql
SELECT module, COUNT(*) FROM test_cases
GROUP BY module ORDER BY module;
```

`HAVING` filters **groups** (after aggregation); `WHERE` filters **rows** (before aggregation):

```sql
SELECT status, COUNT(*) FROM test_cases
GROUP BY status HAVING COUNT(*) > 1;
```

So: WHERE → GROUP BY → aggregates → HAVING → ORDER BY."""),
                 ("QA metrics with SQL", """- Pass rate: `SELECT status, COUNT(*) FROM runs GROUP BY status;`
- Defects by severity: `SELECT severity, COUNT(*) FROM defects GROUP BY severity;`
- Slowest test runs: `SELECT case_id, ms FROM runs ORDER BY ms DESC LIMIT 3;`
- Data integrity: `SELECT COUNT(*) FROM orders WHERE total < 0;` should be zero.

The key habit: always sanity-check a count against the raw rows at least once. A query that returns a plausible-looking number can still be filtering out exactly the rows you care about."""),
               ],
               desk="Reporting 'tickets by category/priority per week' is a GROUP BY. Same thinking, now written in SQL, with the WHERE-vs-HAVING distinction making your reports accurate.",
               takeaway="COUNT/SUM/AVG/MIN/MAX; GROUP BY buckets; WHERE filters rows, HAVING filters groups; every plain SELECT column must be grouped.",
               ex=[
                   sqlex("Count all test cases.", "SELECT COUNT(*) FROM test_cases",
                         {"columns": ["COUNT(*)"], "rows": [[8]]}),
                   sqlex("Count the defects with severity Major.",
                         "SELECT COUNT(*) FROM defects WHERE severity = 'Major'",
                         {"columns": ["COUNT(*)"], "rows": [[3]]}),
                   sqlex("Show each test case status and how many cases have it.",
                         "SELECT status, COUNT(*) FROM test_cases GROUP BY status",
                         {"columns": ["status", "COUNT(*)"], "rows": [
                             ["Passed", 3], ["Failed", 3], ["Blocked", 1], ["Not Run", 1]]},
                         hint="GROUP BY status"),
                   sqlex("Using the runs table, show each status and its count.",
                         "SELECT status, COUNT(*) FROM runs GROUP BY status",
                         {"columns": ["status", "COUNT(*)"], "rows": [["Pass", 2], ["Fail", 3]]},
                         db=RUNS_DB),
                   mcq("Which clause filters groups AFTER aggregation?", [
                       "WHERE", "HAVING", "ORDER BY", "LIMIT"], 1),
                   mcq("`SUM(ms)` over the runs table returns:", [
                       "165", "825", "5", "60"], 1, "120+340+95+210+60 = 825; 165 is the AVG."),
               ]),

        lesson("sql-05", "JOINs: combining tables", 13,
               "Data is spread across tables; JOINs reassemble it. This is the SQL skill most often tested in QA interviews, and the one that lets you trace a defect back to a requirement.",
               [
                 ("The mental picture", """An `INNER JOIN` matches rows from two tables on a related column and keeps only **matching pairs**. A `LEFT JOIN` keeps **all** rows from the left table and fills the right side with NULLs where there's no match — which is exactly how you find 'records with no child rows'.

```sql
SELECT testers.name, test_cases.title
FROM testers
JOIN test_cases ON testers.id = test_cases.owner_id;
```

Read it as: start from `testers`, then for each tester find the test cases whose `owner_id` equals that tester's `id`. Use **qualified names** (`testers.id`) when both tables have an `id` column — otherwise the query is ambiguous."""),
                 ("Join types", table(
                     ["Join", "Keeps", "Classic QA use"],
                     [["INNER JOIN", "Only matching pairs", "List every defect with its test case title"],
                      ["LEFT JOIN", "All left rows + matches or NULL", "'Which test cases have NO defects?' (WHERE right.id IS NULL)"],
                      ["RIGHT / FULL OUTER", "All right / all rows from both", "Less common; many engines (SQLite) lack FULL"],
                      ["CROSS JOIN", "Every combination", "Generating test-data matrices"]])),
                 ("A worked anti-join", """```sql
-- Test cases that have no defect recorded against them
SELECT tc.id, tc.title
FROM test_cases AS tc
LEFT JOIN defects AS d ON tc.id = d.test_case_id
WHERE d.id IS NULL;
```

The `AS` alias shortens names. Understanding this pattern lets you answer interview questions like 'find users who never placed an order' — a LEFT JOIN plus `IS NULL` check on the right side.

**Join pitfalls:** joining on the wrong column silently produces a wrong-but-plausible result; one-to-many joins multiply row counts (a case with 3 defects appears 3 times); always check the row count before trusting a SUM/COUNT after a join."""),
               ],
               desk="Linking a ticket → user → asset in a support tool is a join. You already follow these relationships by clicking through the UI; SQL does it in one statement.",
               takeaway="INNER = matches only; LEFT = all left rows; use qualified names/aliases; LEFT JOIN + IS NULL finds missing relationships.",
               ex=[
                   sqlex("Show each tester's name and the titles of their FAILED test cases.",
                         "SELECT name, title FROM testers JOIN test_cases ON testers.id = test_cases.owner_id WHERE status = 'Failed'",
                         {"columns": ["name", "title"], "rows": [
                             ["Asha", "Login with locked account"], ["Ben", "Apply invalid coupon"],
                             ["Dee", "Cart total with discount"]]},
                         hint="Join on testers.id = test_cases.owner_id, then filter status."),
                   sqlex("List defect ids together with the title of the test case they belong to, ordered by defect id.",
                         "SELECT defects.id, test_cases.title FROM defects JOIN test_cases ON defects.test_case_id = test_cases.id ORDER BY defects.id",
                         {"columns": ["id", "title"], "rows": [
                             [501, "Login with locked account"], [502, "Cart total with discount"],
                             [503, "Cart total with discount"], [504, "Apply invalid coupon"],
                             [505, "Cart with empty basket"], [506, "Checkout as guest"]]},
                         hint="defects.test_case_id = test_cases.id"),
                   mcq("Which join keeps ALL rows from the left table even with no match?", [
                       "INNER JOIN", "LEFT JOIN", "CROSS JOIN", "SELF JOIN"], 1),
                   mcq("To find test cases with NO defects, use:", [
                       "INNER JOIN", "LEFT JOIN ... WHERE defects.id IS NULL", "CROSS JOIN", "GROUP BY without HAVING"], 1),
               ]),

        lesson("sql-06", "Writing data safely: INSERT, UPDATE, DELETE", 11,
               "Testers often create and clean up test data. Writing data is far more dangerous than reading it, so this lesson is mostly about the safety habits that stop you destroying a shared environment.",
               [
                 ("The statements", """```sql
INSERT INTO testers (id, name, team, active)
VALUES (99, 'QA Bot', 'Web', 1);

UPDATE test_cases SET status = 'Passed' WHERE id = 107;

DELETE FROM test_cases WHERE id = 99;
```

- `INSERT` adds rows; list the columns explicitly so a schema change doesn't silently shift values.
- `UPDATE` changes existing rows; **`WHERE` is not optional in practice** — `UPDATE test_cases SET status = 'Passed'` without a WHERE rewrites every row.
- `DELETE` removes rows; same warning, and deletes may be blocked by foreign keys."""),
                 ("Transactions: your undo button", """```sql
BEGIN;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
-- check with SELECT first...
ROLLBACK;   -- undo everything since BEGIN
-- or COMMIT;  -- make it permanent
```

A **transaction** groups statements into an all-or-nothing unit. Always `BEGIN`, write, `SELECT` to verify, then `COMMIT` or `ROLLBACK`. In a shared environment, this discipline is the difference between a clean test and an incident. ACID properties: **Atomicity, Consistency, Isolation, Durability**."""),
                 ("Safety rules for testers", """1. **Confirm the environment/URL/DB** before any write. Never run writes against production.
2. `SELECT` the rows you are about to change *first* with the same WHERE clause — see the count.
3. Wrap writes in a transaction; keep a ROLLBACK ready.
4. Use **unique, identifiable test data** (`qa_bot_...`) so cleanup is precise.
5. Prefer an API or admin UI for creating data (it applies business rules); hand-written INSERTs can skip validation and create unrealistic states.
6. Clean up in a teardown step; record what you changed in the test notes.
7. Backups / snapshots exist — but do not treat them as permission to be careless."""),
               ],
               desk="You've seen a bulk update go wrong in a production system. 'SELECT first, BEGIN, ROLLBACK if unsure' is the change-management checklist expressed in SQL.",
               takeaway="Always WHERE your UPDATE/DELETE; SELECT the target rows first; wrap in a transaction; never write to production.",
               ex=[
                   mcq("What does `UPDATE test_cases SET status='Passed'` (no WHERE) do?", [
                       "Nothing", "Updates every row in the table", "Updates only row 1", "Fails with a syntax error"], 1,
                       "This is the classic dangerous mistake."),
                   mcq("Which statement undoes everything since BEGIN?", [
                       "COMMIT", "ROLLBACK", "DELETE", "SAVE"], 1),
                   mcq("Before running an UPDATE on shared staging, best practice is to:", [
                       "Just run it quickly", "Run a SELECT with the same WHERE to see the affected rows, then wrap in a transaction", "Ask nobody", "Disable foreign keys"], 1),
               ]),

        lesson("sql-07", "Verifying test results with SQL", 12,
               "This is where SQL becomes a testing superpower: proving that what the UI shows actually happened in the database, and finding data-integrity defects no click-test will ever reveal.",
               [
                 ("The verification pattern", """For every action that changes data, design a **UI step + SQL assertion**:

```
1. In the UI: create an order for SKU-88, qty 2, coupon SAVE10.
2. In the DB: SELECT id, total, status FROM orders WHERE ref = 'QA-2026-0407-01';
   Expect exactly 1 row, total = 216.00, status = 'PAID'.
3. Check child rows: SELECT COUNT(*) FROM order_items WHERE order_id = <id>;  -- expect 2
4. Check the audit log / outbox: SELECT * FROM emails WHERE ...;
```

The UI can display a success message while the write silently failed, or display a rounded value while the DB stores something else. SQL catches that."""),
                 ("Data integrity checks worth scripting", """| Check | Query idea |
|---|---|
| Orphans | `LEFT JOIN ... WHERE child.id IS NULL` |
| Duplicates | `GROUP BY email HAVING COUNT(*) > 1` |
| Impossible values | `WHERE total < 0 OR quantity = 0` |
| Missing NULLs where required | `WHERE created_at IS NULL` |
| State mismatches | `WHERE status = 'PAID' AND paid_at IS NULL` |
| Boundary truncation | `CHAR_LENGTH(name)` near the column limit |
| Count drift | `COUNT(*)` before vs after a batch job |

These are excellent **portfolio** material: a `verification-queries.sql` file with comments explaining each check is a concrete, hireable artefact."""),
                 ("Oracles and checksums", """Remember the *test oracle* from Foundations: SQL can BE the oracle. For a report, compare its totals against a trusted aggregate query. For a data migration, compare row counts, sums and checksums before/after. For an API, compare the JSON response with the underlying row.

Caveat: a query that mirrors the same buggy logic as the application will agree with it and prove nothing. Use an **independent** calculation (a spreadsheet, a different query shape, a known reference fixture)."""),
               ],
               desk="Checking the backend record when a user says 'the system says it worked but my balance didn't change' is exactly this pattern. Formalise it and it becomes a test asset.",
               takeaway="Pair each state-changing test with an independent SQL assertion; script integrity checks; SQL can be the oracle, but keep it independent of the app's logic.",
               ex=[
                   mcq("Why verify in the DB after a UI 'success' message?", [
                       "The UI is always wrong", "A success message can appear even when the write failed or stored wrong values", "SQL is faster than clicking", "It's required by ISTQB"], 1),
                   mcq("To find duplicate emails, use:", [
                       "SELECT DISTINCT email", "GROUP BY email HAVING COUNT(*) > 1", "ORDER BY email", "WHERE email IS NULL"], 1),
                   mcq("A SQL oracle is only trustworthy if it:", [
                       "Uses the same logic as the application", "Is an independent calculation / reference", "Returns more rows", "Runs in production"], 1),
               ]),
    ],
    quiz="sql-quiz",
)

# ---------------------------------------------------------------------------
# 9. CLI & Git
# ---------------------------------------------------------------------------
CLI_GIT = course(
    "cli-git", "Command Line & Git", "Work where the code lives",
    "Terminal survival, files/permissions/processes/logs, Git fundamentals, branches and pull requests, and reading a repo as a tester. Assumes zero prior command-line experience.",
    "#ff8a3d", "p2", "Weeks 10-11", "Foundational",
    [
        lesson("cli-01", "Terminal survival skills", 11,
               "The command line is just a text interface to the same files and programs your GUI uses. This lesson covers the 15 commands that make you functional, with the safety habits that matter.",
               [
                 ("The essentials", """| Command | What it does |
|---|---|
| `pwd` | Print current directory |
| `ls -la` | List files (including hidden, with details) |
| `cd path` / `cd ..` | Change directory / go up |
| `mkdir -p a/b` | Create directories |
| `touch file` | Create an empty file |
| `cp -r src dst` / `mv a b` | Copy / move (move = rename) |
| `rm -r dir` | **Delete — no recycle bin** |
| `cat`, `less`, `head -n 20`, `tail -f` | View files / follow a growing log |
| `grep -rin "error" .` | Search text recursively, ignoring case |
| `find . -name "*.log"` | Find files |
| `curl -i URL` | Make an HTTP request from the shell |
| `man command` / `--help` | Built-in documentation |

Paths: `.` = here, `..` = up one, `~` = home, `/` = root. Tab-completion and `Ctrl+C` (cancel) are your best friends. `Ctrl+R` searches command history."""),
                 ("Pipes and redirection", """```bash
grep -i "error" app.log | sort | uniq -c | sort -nr | head -10
# the 10 most frequent error lines in a log

curl -s https://api.example.com/health | head -c 200   # peek at a response
./run-tests.sh > results.txt 2>&1                      # capture stdout AND stderr
tail -f /var/log/app.log | grep --line-buffered ERROR   # watch live errors
```

`|` pipes output into the next command; `>` overwrites a file, `>>` appends, `2>` redirects errors, `2>&1` merges them into stdout. This is how a tester turns a noisy log into evidence without a GUI."""),
                 ("Safety habits", """- `pwd` before any destructive command. Know where you are.
- Never run `rm -rf` with a variable or `/` in it. Prefer moving to a temp folder first.
- Quote paths with spaces: `cd "My Project"`.
- Use a **sandbox** folder for practice; keep production paths out of your muscle memory.
- Read before you run: paste unknown commands into `explainshell.com` if unsure."""),
               ],
               desk="Reading logs with `tail -f` and `grep` is a direct extension of what you already do in a log viewer — just faster, scriptable, and usable on a remote server with no GUI.",
               takeaway="pwd/ls/cd, cat/less/head/tail, grep/find, pipes, redirection, and a healthy fear of rm -rf.",
               ex=[
                   inp("Which command prints your current directory? (3 letters)", ["pwd"], hint="Print Working Directory."),
                   mcq("Which pipeline counts the most frequent error lines?", [
                       "cat app.log", "grep -i error app.log | sort | uniq -c | sort -nr", "rm app.log", "ls -la"], 1),
                   mcq("What does `2>&1` do?", [
                       "Deletes errors", "Merges stderr into stdout", "Runs the command twice", "Creates file 2"], 1),
                   inp("Which command follows a log file as it grows? (4 letters + flag)", ["tail -f", "tail"], hint="tail with the 'follow' flag."),
               ]),

        lesson("cli-02", "Files, permissions, processes and logs", 11,
               "A little Linux knowledge explains a whole class of 'works locally, fails on the server' defects. This lesson covers permissions, processes, and reading logs like an investigator.",
               [
                 ("Permissions", """```bash
-rw-r--r--  1 asha  qa  4.2K Apr  7 09:12 config.yaml
drwxr-xr-x  2 asha  qa  4.0K Apr  7 09:12 reports/
```

Three triplets: **owner / group / others**, each with `r` (read=4), `w` (write=2), `x` (execute=1). So `754` = owner rwx, group r-x, others r--. A tester-relevant classic: a test script that 'works for me' fails in CI because it isn't executable (`chmod +x run-tests.sh`), or because the CI user cannot write to the reports directory.

`chmod 600 secrets.env`, `chmod +x script.sh`, `chown user:group file`, `umask` for defaults."""),
                 ("Processes, ports and services", """```bash
ps aux | grep node          # is the app running?
top / htop                  # CPU / memory
kill -9 <pid>               # last resort
ss -tulpn                   # what is listening on which port
systemctl status myapp      # is the service up?
journalctl -u myapp -n 50   # its recent logs
df -h / du -sh *            # disk full? who is using the space?
```

'The app is down' triage in order: is the process alive → is the port listening → is the disk full → what do the last 50 log lines say → was there a deploy? Sound familiar?"""),
                 ("Reading a log line", """```
2026-04-07T09:14:22.118Z  WARN  [checkout] req=8f3c user=qa14
  coupon=SAVE10 total=96.00 expected=108.00
```

Extract: **timestamp (with timezone)**, **level** (DEBUG/INFO/WARN/ERROR/FATAL), **component**, **request/correlation ID** (the magic key for joining logs across services), **user**, and the **message/values**. Search by request ID, not by the user's name. Watch for **log levels** hiding errors, and for stack traces with a root cause ('Caused by:'). Always quote the exact line and the request ID in a defect report."""),
               ],
               desk="This entire lesson is your incident-troubleshooting playbook with the commands written down. You can already do this; now it works on any Linux box without a GUI.",
               takeaway="rwx triplets and chmod; ps/top/ss/systemctl/journalctl; parse logs by timestamp, level, component and request ID.",
               ex=[
                   mcq("`chmod 754` gives others:", ["rwx", "rw-", "r--", "---"], 2, "7=rwx owner, 5=r-x group, 4=r-- others."),
                   mcq("A script runs locally but CI says 'permission denied'. Likely fix:", [
                       "Rewrite it", "chmod +x so it is executable", "Increase RAM", "Change the browser"], 1),
                   mcq("The most useful key for tracing one request across several services is the:", [
                       "User's first name", "Correlation / request ID", "Log level", "Filename"], 1),
               ]),

        lesson("cli-03", "Git fundamentals", 12,
               "Git is how all code — and increasingly all test artefacts — is versioned. You need enough to clone a repo, work on a branch, commit your portfolio, and not lose anyone's work.",
               [
                 ("The mental model", """Git tracks **snapshots** of your files in a repository. Four areas:

```
Working tree  --(git add)-->  Staging area  --(git commit)-->  Local repo
                                                  --(git push)-->  Remote (GitHub)
```

A **commit** is a numbered snapshot with a message, author and parent. A **branch** is a movable pointer to a commit; `main` is just a convention. `HEAD` is where you are right now."""),
                 ("The daily commands", """```bash
git clone https://github.com/org/repo.git
cd repo
git status                         # what changed? (run this constantly)
git add file.txt                   # stage one file
git add .                          # stage everything (check status first!)
git commit -m "Add login test cases"
git log --oneline --graph -10      # readable history
git diff                           # unstaged changes; git diff --staged for staged
git pull                           # fetch + merge remote changes
git push origin my-branch          # publish
git restore file.txt               # discard local changes to a file
```

Commit hygiene: **small, focused commits**, imperative messages ('Add boundary tests for cart', not 'stuff'), never commit secrets/passwords or generated `node_modules`. A `.gitignore` file lists what to exclude."""),
                 ("Why a tester cares", """- You'll **clone** the application repo to read code, run tests, and reproduce issues locally.
- Your **portfolio** (test cases, Postman collection, Playwright framework) lives in Git — that's the artefact hiring managers inspect.
- Test code is **reviewed** like any other code; you'll open pull requests.
- `git bisect` can find which commit introduced a regression — useful context even if a developer runs it.
- Commit messages are a searchable history of *why* a change happened."""),
               ],
               desk="Version-controlled change records and rollback plans are Git's conceptual cousins. The new part is that *every* file change is tracked, not just production changes.",
               takeaway="Working tree → staging → commit → remote; status often; small focused commits; never commit secrets.",
               ex=[
                   order("Put the Git flow in order:", [
                       "Edit files in the working tree", "git add (stage)", "git commit (snapshot)", "git push (publish to remote)"]),
                   mcq("What does `git status` tell you?", [
                       "The remote URL", "Which files are modified/staged/untracked and your branch", "The commit message history", "The server CPU"], 1),
                   inp("Which file tells Git which files to exclude from tracking? (9 chars)", [".gitignore", "gitignore"], hint="Starts with a dot."),
               ]),

        lesson("cli-04", "Branches, pull requests and code review", 11,
               "Branches let many people work without colliding. Pull requests are where work gets reviewed — including your test code. This is the collaboration layer of Git.",
               [
                 ("Branching in practice", """```bash
git switch -c feature/cart-tests     # create + move to a branch (modern)
git checkout -b feature/cart-tests   # older equivalent
git switch main                      # go back
git merge feature/cart-tests         # bring changes in
git branch -d feature/cart-tests     # delete a merged branch
```

A common team flow: branch per story/defect, commit on the branch, push, open a **Pull Request (PR)**, get review + green CI, then merge into `main` (often squash or with a merge commit). Keep branches short-lived to avoid painful **merge conflicts** (two people changed the same lines). Resolve conflicts by reading both versions and deciding deliberately — never blindly accept one side."""),
                 ("Reading a pull request as QA", """In the PR, look at the **Files changed / diff**: what files and functions were touched? This directly drives your **regression test selection**. Check the linked story and acceptance criteria, the test evidence attached, whether new tests were added, and whether config/DB migrations/feature flags changed.

Useful reviewer comments from a tester: *'Does this handle the empty-cart case?'*, *'Should we add a test for the $100 boundary?'*, *'This changes the shared pricing helper — I'll add checkout and invoice to the regression pack.'* This is shift-left in action."""),
                 ("Your first portfolio PR", """Create a repo, add a `README.md` (what the project is, why, how to run it), commit in small steps, and open a PR against your own `main` even if you're solo — it teaches the workflow and leaves a visible, professional history. A clean README and a sensible commit history are part of what a hiring manager evaluates."""),
               ],
               desk="Reading a change record before approving a production change is a diff review. Same discipline: what changed, what could it affect, what evidence proves it's safe?",
               takeaway="Branch per unit of work; PR = diff + review + CI; use the diff to choose regression tests; keep commits small.",
               ex=[
                   mcq("What is the main QA reason to read a PR's diff?", [
                       "To check the developer's spelling", "To identify what changed and select regression tests", "To count lines of code", "To close the sprint"], 1),
                   mcq("Short-lived branches help mainly by:", [
                       "Making commits faster", "Reducing painful merge conflicts", "Deleting history", "Avoiding code review"], 1),
                   inp("What is the common abbreviation for a request to merge a branch after review? (2 letters)", ["PR"], hint="Pull ..."),
               ]),

        lesson("cli-05", "Reading a repo and writing Markdown", 10,
               "Your portfolio and your test documentation will live as plain text in a repo. Markdown is the formatting language of GitHub, Jira, and most test tools — learn it once, use it everywhere.",
               [
                 ("Repo orientation for testers", """When you clone a repo, find these first:

| File | Why |
|---|---|
| `README.md` | What the project is, how to install/run/test |
| `package.json` / `requirements.txt` / `pom.xml` | Dependencies and **scripts to run tests** |
| `/tests`, `/spec`, `__tests__`, `*.spec.*` | Where the tests live |
| `.github/workflows/*.yml` | CI: which tests run on each push |
| `playwright.config.*`, `cypress.config.*` | Framework config, base URLs, browsers |
| `/docs`, `CONTRIBUTING.md` | Conventions and setup |
| `.env.example` | Config keys (never commit real `.env`) |
| `CHANGELOG.md` | What changed per release — feeds regression scope |

Run `npm test` (or the documented command) and see what happens. Being able to *run someone else's test suite* is a concrete skill you can demonstrate in an interview."""),
                 ("Markdown essentials", """```markdown
# Heading 1        ## Heading 2        ### Heading 3
**bold**  *italic*  `inline code`   [link](https://example.com)
- bullet item
1. numbered item
> blockquote (great for a note)
| Column | Column |
|---|---|
| cell | cell |

```js
// fenced code block with a language tag
const x = 1;
```

Task lists: `- [x] done` / `- [ ] todo`. GitHub renders all of this. Use Markdown for README files, test plans, bug report templates, and your study journal — it's versionable and reviewable, unlike a Word doc."""),
                 ("Documentation habits that get noticed", """Write the **'how to run it'** section as if for a stranger: prerequisites, exact commands, expected output, and a troubleshooting note. Include a short **'what I tested and why'** section in portfolio repos. README quality is often the first thing a hiring manager sees — a clear one signals the same documentation discipline that QA requires."""),
               ],
               desk="Knowledge base articles are documentation for humans; a README is documentation for teammates who must also run the thing. Same clarity, slightly different audience.",
               takeaway="Find README, test scripts, config and CI first; write Markdown with headings, tables, code fences and task lists; document how to run everything.",
               ex=[
                   mcq("Which file usually lists the commands to run a project's tests?", [
                       "README.md and package.json scripts", ".gitignore", "LICENSE", "logo.png"], 0),
                   mdex("Write a short README section with a heading, a fenced code block, and a task list item.",
                        [P(r"^#{1,3}\s", "a Markdown heading"), P(r"```", "a fenced code block"), P(r"- \[[ xX]\]", "a task list item")],
                        "## Running the tests\n\n```bash\nnpm install\nnpx playwright test\n```\n\n- [x] Add login test cases\n- [ ] Add API contract tests",
                        starter="## Running the tests\n\n"),
                   mcq("Where do you find which tests run on every push in a GitHub repo?", [
                       "package.json only", ".github/workflows/*.yml", "The README logo", "node_modules"], 1),
               ]),
    ],
    quiz="cli-git-quiz",
)

# ---------------------------------------------------------------------------
# 10. JavaScript from scratch
# ---------------------------------------------------------------------------
JAVASCRIPT = course(
    "javascript", "Programming from Scratch (JavaScript)", "Read, write and debug code",
    "A gentle first programming course assuming zero experience: variables and types, conditions and loops, functions, arrays and objects, JSON and async, and debugging. Chosen because it powers Playwright, Postman scripts and the web itself.",
    "#f5a623", "p2", "Weeks 9-11", "Foundational",
    [
        lesson("js-01", "Variables, types and operators", 12,
               "Programming is giving the computer precise instructions about values. Start with the three ways to name a value and the six data types you'll meet constantly in test code.",
               [
                 ("Variables", """```js
let   count = 0;        // can change
const baseUrl = "https://staging.example.com";  // cannot be reassigned
let   user;             // undefined for now
```

Prefer `const` by default; use `let` when you really need to reassign. Avoid `var` (old, surprising scoping). Names are `camelCase` and should describe the value: `expectedTotal`, not `x`.

A **statement** is an instruction; an **expression** produces a value. `2 + 2` is an expression; `let n = 2 + 2;` is a statement."""),
                 ("Types", """| Type | Examples | Tester relevance |
|---|---|---|
| `string` | `"Hello"`, `'High'` | Expected messages, JSON values |
| `number` | `42`, `96.00` | Totals, counts, status codes |
| `boolean` | `true`, `false` | Assertions, flags, `isVisible()` |
| `null` | `null` | Intentional 'no value' (API responses) |
| `undefined` | `undefined` | Missing property / not initialised |
| `object` | `{...}`, arrays, `Date` | JSON payloads, config |

Check with `typeof value`. **Loose vs strict equality** is a classic bug: `==` coerces types (`"5" == 5` is `true`), `===` does not. **Always use `===` and `!==`** in test code. Similarly, `0`, `""`, `null`, `undefined` and `NaN` are all *falsy* — a test like `if (response.value)` will skip a legitimate `0`. Check explicitly: `if (value !== undefined)`."""),
                 ("Operators and template literals", """```js
const total = 120 * 0.9;            // arithmetic: + - * / %
const label = `Order ${id}: $${total.toFixed(2)}`;  // template literal
const isHigh = priority === "High" && status !== "Blocked";
const pct = (passed / totalCases) * 100;
```

Template literals (backticks) insert values with `${...}` — you'll use them in Playwright test names and Postman scripts. `console.log()` prints to the terminal/console; it's your first debugging tool."""),
               ],
               desk="You already reason about values and comparisons in ticket rules ('if priority = P1 and status ≠ Closed'). That's an `if` with `===` and `&&`, just written in a different syntax.",
               takeaway="const by default; six types; always ===; watch out for falsy 0/''; template literals with ${}.",
               ex=[
                   mcq("Which comparison should you use in test code?", ["==", "===", "=", "equals"], 1, "=== avoids type coercion surprises."),
                   mcq("What is `typeof []` in JavaScript?", ["array", "object", "list", "undefined"], 1, "Arrays are objects."),
                   mcq("Which value is FALSY in a condition?", ["'0'", "0", "'false'", "[]"], 1,
                       "The number 0 is falsy; the string '0' and an empty array [] are truthy."),
                   inp("Which keyword declares a variable that cannot be reassigned? (5 letters)", ["const"], hint="The opposite of let."),
               ]),

        lesson("js-02", "Conditions and loops", 12,
               "Decisions and repetition turn a list of values into a program. These are the structures behind every assertion, every data-driven test, and every retry loop.",
               [
                 ("If / else and switch", """```js
if (statusCode === 200 && body.ok) {
  console.log("PASS");
} else if (statusCode >= 500) {
  console.error("Server error", statusCode);
} else {
  console.warn("Unexpected response", statusCode);
}

const verdict = status === "Passed" ? "green" : "red";  // ternary
```

Braces are not optional in readable code. The **ternary** `condition ? a : b` is a compact one-line if — common in test assertions but don't nest them."""),
                 ("Loops", """```js
for (let i = 0; i < testCases.length; i++) {
  run(testCases[i]);
}

for (const tc of testCases) {      // cleaner: for...of
  console.log(tc.title);
}

let attempt = 0;
while (attempt < 3 && !isReady()) {
  attempt++;
  await wait(500);
}
```

`for...of` iterates values; avoid raw index loops when you don't need the index. **Off-by-one** errors (`i <= length` instead of `<`) are the same boundary defects you learned about — careful with `<=`."""),
                 ("Where testers use these", """- Data-driven tests: loop over an array of `{input, expected}` pairs.
- Assertions: `if (actual !== expected) throw new Error(...)`.
- Polling / retries: wait for an element or an async job with a bounded loop and a timeout.
- Guard clauses: skip a test if the environment isn't ready — but log the skip reason.

> **Never write an unbounded `while(true)` retry** — a hang in a CI pipeline is worse than a clear failure. Always bound attempts and timeouts."""),
               ],
               desk="A runbook step like 'repeat up to 3 times until the service responds, then escalate' is a bounded while loop. Same logic, new syntax.",
               takeaway="if/else, ternary, for...of, bounded while; every loop needs a clear exit and a timeout.",
               ex=[
                   mcq("Which loop is cleanest for iterating every item of an array when you don't need the index?", [
                       "while(true)", "for...of", "for(let i=0;i<=len;i++)", "goto"], 1),
                   mcq("Why bound a retry loop with a max attempt count / timeout?", [
                       "It's prettier", "An unbounded loop can hang a test run or CI pipeline forever", "JavaScript requires it", "It makes failures pass"], 1),
                   inp("What operator is the compact one-line if/else (`cond ? a : b`) called?", ["ternary", "ternary operator"], hint="Three operands."),
               ]),

        lesson("js-03", "Functions: reusable test logic", 12,
               "Functions let you name a piece of behaviour and reuse it — the foundation of maintainable test code and of the Page Object Model later.",
               [
                 ("Declaring and calling", """```js
function expectedDiscount(subtotal, rate) {
  return Math.round(subtotal * rate * 100) / 100;
}

const total = expectedDiscount(120, 0.10);  // 12

// Arrow function (common in test frameworks)
const isHigh = (tc) => tc.priority === "High";
```

`return` sends a value back and ends the function; without it the result is `undefined`. Parameters are the inputs; arguments are the actual values passed. Keep functions **small and single-purpose** with a verb name (`buildUser()`, `assertStatus()`, `formatCurrency()`)."""),
                 ("Scope, purity and side effects", """Variables declared inside a function are local to it. A **pure** function returns the same output for the same input and changes nothing else — perfect for a test oracle. A function with **side effects** writes to a file, calls an API, or mutates shared state; keep those separate and explicit, because they make tests order-dependent.

```js
// pure — easy to test
function classify(score) { return score >= 70 ? "Pass" : "Fail"; }

// side effect — needs setup/cleanup
async function createUser(user) { return fetch("/api/users", {method:"POST", body: JSON.stringify(user)}); }
```"""),
                 ("Why this matters for QA", """Every assertion helper, every fixture, every page object is a function. In Postman you'll write `pm.test(...)` callbacks; in Playwright, `test('name', async ({ page }) => {...})` — a function you pass to the framework. Understanding parameters, return values and scope is all you need to read those fluently."""),
               ],
               desk="Reusable checklists/macros on the desk are functions: a named procedure with inputs and an output. Same idea, now with `return`.",
               takeaway="Small single-purpose functions; return values; prefer pure oracles; isolate side effects; arrow functions appear everywhere in frameworks.",
               ex=[
                   mcq("A function with no `return` statement returns:", ["null", "undefined", "0", "an error"], 1),
                   mcq("Why prefer a 'pure' function as a test oracle?", [
                       "It is faster", "Same input always gives the same output and it changes nothing else", "It uses less memory", "It can't throw"], 1),
                   inp("What do we call inputs listed in a function declaration?", ["parameters", "parameter", "params"], hint="Arguments are the values you pass; these are the names."),
               ]),

        lesson("js-04", "Arrays and objects", 12,
               "Almost all test data and API payloads are arrays and objects. Being able to read, filter and transform them is the last 'pure language' step before JSON and async code.",
               [
                 ("Arrays", """```js
const cases = ["TC-101", "TC-102", "TC-103"];
cases.length;            // 3
cases[0];                // "TC-101"  (zero-indexed!)
cases.push("TC-104");    // add to end

const high = cases.filter(c => c.priority === "High");
const titles = cases.map(c => c.title);
const failed = cases.find(c => c.status === "Failed");
const count = cases.reduce((n, c) => n + (c.status === "Passed" ? 1 : 0), 0);
```

`map` transforms, `filter` selects, `find` returns the first match, `reduce` folds into one value, `some`/`every` test a condition. These replace most manual loops. Careful: arrays are **zero-indexed** — the classic off-by-one."""),
                 ("Objects and JSON-shaped data", """```js
const user = {
  id: 14,
  email: "qa.user14@example.com",
  role: "member",
  active: true,
  address: { city: "Leeds", postcode: "LS1 1AA" }
};

user.email;              // dot access
user["role"];            // bracket access (works with dynamic keys)
user.address.city;       // nested
const { email, role } = user;   // destructuring
const payload = { ...user, active: false };  // spread = copy with an override
```

Objects are key→value maps. `Object.keys(obj)`, `Object.values(obj)`, and `'key' in obj` are useful for assertions. **Optional chaining** `user?.address?.city` avoids a crash when a middle object is missing — very handy when an API response is partial."""),
                 ("Mutating vs copying", """`push`, `sort` (in place!) and assignment **mutate**; `map`, `filter`, `{...obj}` create new values. In tests, accidental mutation of shared fixture data causes the 'passes alone, fails in the suite' problem — copy fixtures before modifying them (`const data = structuredClone(fixture)`).""" ),
               ],
               desk="A ticket object with fields and nested customer/asset data is exactly this shape. JSON is just this, sent over the wire.",
               takeaway="Zero-indexed arrays; map/filter/find/reduce; objects with dot/bracket access, destructuring, spread, optional chaining; copy fixtures before mutating.",
               ex=[
                   mcq("Which array method returns a NEW array with only matching items?", ["forEach", "filter", "push", "sort"], 1),
                   mcq("What is `cases[0]`?", ["The last element", "The first element", "An error", "The length"], 1, "Zero-indexed."),
                   mcq("What does `user?.address?.city` protect against?", [
                       "Slow networks", "A missing intermediate object causing a TypeError", "Wrong capitalisation", "SQL injection"], 1),
               ]),

        lesson("js-05", "JSON, async and fetching data", 13,
               "APIs speak JSON and respond asynchronously. This lesson connects the language to the API testing you'll do next, and explains why a test sometimes checks a value before it exists.",
               [
                 ("JSON", """**JSON** (JavaScript Object Notation) is a text format for structured data:

```json
{
  "id": 1042,
  "title": "Discount applied twice",
  "severity": "Major",
  "open": true,
  "tags": ["cart", "pricing"],
  "assignee": null
}
```

Rules: double quotes only, no trailing commas, no comments, no functions/`undefined`. Values may be string, number, boolean, `null`, array, or object. Convert with `JSON.parse(text)` (string → object) and `JSON.stringify(obj)` (object → string). A malformed body is a classic 400 cause; a `Content-Type` mismatch is another."""),
                 ("Promises and async/await", """Network calls don't finish instantly. A **Promise** is a placeholder for a future value. `async/await` makes it readable:

```js
async function getOrder(id) {
  const response = await fetch(`https://api.example.com/orders/${id}`);
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const order = await response.json();
  return order.total;
}

const total = await getOrder(1042);
```

`await` pauses *inside the async function* until the promise settles; it does not block the whole program. Always **await** asynchronous assertions — forgetting `await` is the #1 cause of 'my Playwright test passes but shouldn't'. Handle rejection with `try/catch`."""),
                 ("Sync vs async test pitfalls", """- Reading `response.json()` before `await` gives a Promise, not data.
- An assertion that runs before the DOM updates gives a false failure (or worse, a false pass).
- Prefer **explicit waits for a condition** (`expect(locator).toBeVisible()` with auto-waiting) over fixed `sleep(2000)` — fixed sleeps make suites slow and flaky.
- Race conditions are real defects: double-click, concurrent edits, slow network. Test them deliberately."""),
               ],
               desk="'I clicked it but nothing happened yet' is an async timing issue. You've talked users through that; now you'll write tests that wait for the right condition instead of guessing a delay.",
               takeaway="JSON is strict structured text; async/await handles future values; always await; wait for conditions, not fixed sleeps.",
               ex=[
                   mcq("Which JSON snippet is valid?", [
                       "{ id: 14, }", '{"id": 14, "ok": true}', "{'id': 14}", '{ "id": 14, "note": undefined }'], 1,
                       "Double quotes, no trailing comma, no single quotes, no undefined."),
                   mcq("Forgetting `await` on `response.json()` gives you:", [
                       "The parsed object", "A Promise, not the data", "An empty string", "A syntax error"], 1),
                   mcq("Why prefer condition-based waiting over `sleep(2000)`?", [
                       "It looks nicer", "Fixed sleeps are slow and flaky; condition waits adapt to actual readiness", "sleep() doesn't exist", "It changes the status code"], 1),
               ]),

        lesson("js-06", "Debugging and reading other people's code", 11,
               "You'll spend more time reading code than writing it. This lesson gives a calm, repeatable debugging method — the programming version of the troubleshooting method you already know.",
               [
                 ("A repeatable debugging routine", """1. **Reproduce deterministically** and read the *exact* error message and stack trace (the first line matters most).
2. **Locate** the failing line: file + line number from the stack.
3. **Inspect values** just before it with `console.log({actual, expected, user})` or a breakpoint in VS Code / DevTools.
4. **Form ONE hypothesis**, change ONE thing, re-run. (Sound familiar? Same as isolating an intermittent defect.)
5. **Bisect**: comment out halves, or `git bisect` to find the commit that introduced a regression.
6. **Fix, then add a test** that would have caught it.
7. **Write down** the cause in your journal — debugging notes become your personal error-guessing checklist."""),
                 ("Common errors decoded", """| Message | Usually means |
|---|---|
| `Cannot read properties of undefined (reading 'x')` | An object you assumed existed is missing — check the API response / optional chaining |
| `Unexpected token ... in JSON` | Malformed JSON or an HTML error page where JSON was expected |
| `fetch failed` / `ECONNREFUSED` | Wrong URL, service down, or CORS |
| `is not a function` | Typo, or a value isn't the type you think (`typeof` it) |
| `Test timeout exceeded` | Missing `await`, an element never appeared, or an unbounded wait |
| `Cannot find module` | Missing `npm install` / wrong path or capitalisation |"""),
                 ("Reading unfamiliar test code", """Start at the **test name** (it states intent), then the **setup/fixtures**, then the **actions**, then the **assertions** — the same structure as a manual test case. Follow the imports to find helper/page-object definitions. Run the single test with a verbose reporter and watch what it does. Don't try to understand the whole framework on day one; trace one test end to end."""),
               ],
               desk="This is your troubleshooting method verbatim: reproduce, isolate, one variable, evidence, document. The only new part is that the 'system' is code you can step through.",
               takeaway="Read the error, inspect values, one hypothesis at a time, bisect, fix + add a test, document; read test code as name → setup → actions → assertions.",
               ex=[
                   mcq("The FIRST thing to read when a script fails is:", [
                       "The whole repository", "The exact error message and stack trace", "The README", "The git log"], 1),
                   mcq("A test times out and you find a missing `await` before an assertion. This is likely:", [
                       "A network outage", "The assertion raced ahead of the async action", "A CSS bug", "A database crash"], 1),
                   mcq("When reading an unfamiliar automated test, start with:", [
                       "The config file", "The test name (intent), then setup → actions → assertions", "The last line", "node_modules"], 1),
               ]),
    ],
    quiz="javascript-quiz",
)

COURSES_02 = [TOOLS, WEB, SQL, CLI_GIT, JAVASCRIPT]

QUIZZES_02 = [
    quiz("tools-quiz", "tools", "Tools & workflow checkpoint", [
        ("'Affects Version/s' in Jira records:", ["The build that will fix it", "The build where the defect was first seen", "The sprint", "The reporter"], 1, ""),
        ("Which DevTools panel shows request payloads and status codes?", ["Elements", "Console", "Network", "Sources"], 2, ""),
        ("'Copy as cURL' lets you:", ["Screenshot a page", "Replay the exact HTTP request in Postman", "Edit CSS", "Restart the server"], 1, ""),
        ("A new build lands in staging. First action:", ["Full regression", "Smoke / build verification test + read the changelog", "Log a defect", "Close the sprint"], 1, ""),
        ("Which evidence is best for a timing/intermittent bug?", ["A HAR only", "A short screen recording + repro rate", "A spreadsheet", "Nothing"], 1, ""),
        ("Test cases vs test runs:", ["The same thing", "Case = reusable definition; run = one execution against one build", "Run is a folder", "Case is only automated"], 1, ""),
    ]),
    quiz("web-quiz", "web", "Web fundamentals checkpoint", [
        ("DNS resolves:", ["IP to hostname", "Hostname to IP address", "Cookies to sessions", "JSON to HTML"], 1, ""),
        ("401 vs 403:", ["401 = forbidden, 403 = unauthenticated", "401 = unauthenticated, 403 = forbidden", "Both are server errors", "Both are redirects"], 1, ""),
        ("Which method is NOT idempotent?", ["GET", "PUT", "DELETE", "POST"], 3, ""),
        ("201 means:", ["Cached", "Created", "Bad request", "No content"], 1, ""),
        ("The most resilient locator is:", ["A long absolute XPath", "A role/label/data-testid locator", "An nth-child chain", "A pixel coordinate"], 1, ""),
        ("Client-side validation should be:", ["Trusted as the only check", "Treated as convenience; server must validate too", "Disabled in tests", "Replaced by CSS"], 1, ""),
        ("After logout, you must verify:", ["The URL", "The server invalidated the session/token", "CSS reloaded", "The cookie name"], 1, ""),
    ]),
    quiz("sql-quiz", "sql", "SQL checkpoint", [
        ("Which finds rows with no assignee?", ["assignee_id = NULL", "assignee_id IS NULL", "assignee_id = 0", "assignee_id = ''"], 1, ""),
        ("BETWEEN 103 AND 105 includes:", ["104 only", "103, 104, 105", "103, 105", "All >103"], 1, ""),
        ("Which clause filters GROUPS after aggregation?", ["WHERE", "HAVING", "LIMIT", "FROM"], 1, ""),
        ("COUNT(*) vs COUNT(col):", ["Identical", "COUNT(*) counts rows; COUNT(col) skips NULLs", "COUNT(col) is faster", "COUNT(*) skips NULLs"], 1, ""),
        ("To find test cases with NO defects, use:", ["INNER JOIN", "LEFT JOIN ... WHERE defects.id IS NULL", "CROSS JOIN", "ORDER BY"], 1, ""),
        ("The safest way to run an UPDATE on shared staging:", ["Run it immediately", "SELECT the same rows first, wrap in a transaction", "Disable foreign keys", "Use production"], 1, ""),
        ("A UI shows 'success' but you should still:", ["Trust it", "Verify persistence with an independent SQL query", "Close the test", "Take a screenshot"], 1, ""),
    ]),
    quiz("cli-git-quiz", "cli-git", "CLI & Git checkpoint", [
        ("`chmod 754` gives others:", ["rwx", "rw-", "r--", "---"], 2, ""),
        ("Git staging area sits between:", ["Remote and GitHub", "Working tree and local repo", "main and branch", "HEAD and tag"], 1, ""),
        ("Which file excludes files from Git tracking?", ["README.md", ".gitignore", ".env", "package.json"], 1, ""),
        ("The main QA reason to read a PR diff:", ["Count lines", "Select regression tests based on what changed", "Check spelling", "Close the sprint"], 1, ""),
        ("`tail -f` is used to:", ["Delete a file", "Follow a growing log live", "Change permissions", "List ports"], 1, ""),
        ("Which file usually documents how to run a project's tests?", ["LICENSE", "README.md + package.json scripts", "logo.png", ".gitignore"], 1, ""),
    ]),
    quiz("javascript-quiz", "javascript", "JavaScript checkpoint", [
        ("Which equality operator avoids type coercion?", ["==", "===", "=", "!="], 1, ""),
        ("`typeof []` is:", ["array", "object", "list", "undefined"], 1, ""),
        ("Which value is falsy?", ["'0'", "0", "[]", "'false'"], 1, ""),
        ("A function with no return gives:", ["null", "undefined", "0", "false"], 1, ""),
        ("`filter` returns:", ["A single value", "A new array of matching items", "Nothing", "A string"], 1, ""),
        ("Forgetting `await` on `response.json()` yields:", ["The data", "A Promise, not the data", "An error immediately", "undefined string"], 1, ""),
        ("Fixed `sleep(2000)` waits should be replaced by:", ["Longer sleeps", "Condition-based waits / auto-waiting assertions", "No waits at all", "A try/catch"], 1, ""),
    ]),
]
