"""Phase 3-5 courses: APIs, Postman, automation strategy, Playwright, CI/CD, non-functional."""
from . import lesson, course, quiz, mcq, inp, order, mdex, P, table

# ---------------------------------------------------------------------------
# 11. APIs & REST
# ---------------------------------------------------------------------------
API = course(
    "api", "APIs & REST", "The application without the UI",
    "From zero: what an API is, resources and REST constraints, JSON and schemas, authentication, status codes and errors, idempotency and versioning. The foundation for the Postman course.",
    "#3df2c0", "p3", "Weeks 12-13", "Core",
    [
        lesson("api-01", "What an API is, and what REST means", 12,
               "An **API (Application Programming Interface)** is a contract that lets one program talk to another. Testing the API directly is often faster, more stable and more revealing than testing through the UI.",
               [
                 ("The contract idea", """A web API exposes **endpoints** (URLs) that accept requests and return responses. The UI is just one client of that API; mobile apps, integrations, and your Postman collection are others.

```
GET  /api/users/14          -> 200 { "id": 14, "email": "...", "role": "member" }
POST /api/orders            -> 201 { "id": 9001, "total": 108.00, "status": "PAID" }
GET  /api/orders/9001       -> 200 { ... }
DELETE /api/orders/9001     -> 204 (no content)
```

The **contract** is: which endpoints exist, what they accept, what they return, what errors they produce, and what authentication they require. An **API specification** (OpenAPI / Swagger) documents that contract — a primary test basis, and a great oracle."""),
                 ("REST constraints (plain English)", """**REST** is an architectural style, not a protocol. Its key ideas:

| Idea | Meaning | Test implication |
|---|---|---|
| **Resources** | URLs name *things* (`/users/14`), not actions (`/getUser`) | Check resource paths and IDs |
| **Uniform interface** | Standard HTTP methods carry the intent | Use GET to read, POST to create, PUT/PATCH to update |
| **Stateless** | Each request contains all the info needed; the server stores no client session between requests | Send the token every time; test with/without it |
| **Representations** | Resources are returned as JSON/XML, with `Content-Type` | Validate body shape and media type |
| **HATEOAS** (optional) | Responses include links to related actions | Rarely implemented; nice when present |
| **Cacheable** | Responses declare caching | Test `Cache-Control`, ETag, conditional GETs |

Not every 'REST API' follows all of these. Test what the **spec** says, not what the textbook says — but use the principles to ask good questions."""),
                 ("Why API testing is high leverage", """- **Earlier**: APIs exist before the UI; you can test during development (shift-left).
- **Faster and more stable**: no browser rendering, no flaky CSS selectors.
- **Deeper**: you can send invalid, extreme and malicious payloads the UI would never allow.
- **Broader**: covers every client (mobile, partner integrations, batch jobs).
- **Better bugs**: a wrong `total` found at the API is a one-line report with an exact payload.

> **From the desk:** calling the backend directly is the equivalent of checking the database instead of trusting the ticket status field. Same instinct, one layer up."""),
               ],
               desk="You've used a tool or script to hit a service directly to see whether the front-end was lying. That's API testing — now with a documented contract behind it.",
               takeaway="An API is a documented contract of endpoints, methods, payloads, responses and errors. REST = resources + HTTP methods + statelessness.",
               ex=[
                   mcq("Which URL is most RESTful for fetching user 14?", [
                       "/getUser?id=14", "/api/users/14", "/doFetchUser", "/api?action=user14"], 1),
                   mcq("'Stateless' in REST means:", [
                       "The server never stores data", "Each request must carry all info needed; no client session state between requests", "No authentication is needed", "Responses cannot be cached"], 1),
                   mcq("The primary document describing an API contract is called:", [
                       "A test plan", "An OpenAPI / Swagger specification", "A HAR file", "A README logo"], 1),
                   inp("What word describes a URL that accepts requests and returns responses? (8 letters)", ["endpoint", "Endpoint"], hint="A single address in an API."),
               ]),

        lesson("api-02", "JSON, schemas and payloads", 12,
               "Almost every API speaks JSON. A tester must be able to read a payload, spot a wrong shape, and know which deviations are real defects.",
               [
                 ("Reading a response", """```json
{
  "id": 9001,
  "status": "PAID",
  "total": 108.00,
  "currency": "GBP",
  "customer": { "id": 14, "email": "qa.user14@example.com" },
  "items": [ { "sku": "SKU-88", "qty": 2, "unitPrice": 60.00 } ],
  "createdAt": "2026-04-07T09:14:22Z"
}
```

Check: **keys present and correctly spelled**, **types** (is `total` a number or a string?), **nested objects/arrays**, **null vs missing**, **units/currency**, **date format and timezone**, and **enum values** (`status` should be one of the documented set)."""),
                 ("Schemas and contract validation", """A **JSON Schema** declares the expected shape:

```json
{
  "type": "object",
  "required": ["id", "status", "total"],
  "properties": {
    "id": { "type": "integer" },
    "status": { "enum": ["NEW", "PAID", "CANCELLED"] },
    "total": { "type": "number", "minimum": 0 }
  }
}
```

Validating a response against a schema catches whole classes of defects (missing field, wrong type, unexpected enum) in one assertion. In Postman you can do a lightweight version by checking `typeof` and required keys; later, tools like `ajv` or contract-test tools (Pact, Schemathesis) automate it.

**Breaking changes** to watch: a removed/renamed field, a type change (`total` number → string), a new required request field, or a stricter enum. These break *other* clients that don't get retested — classic regression territory."""),
                 ("Crafting request payloads", """Request bodies must match the documented schema and `Content-Type: application/json`. Test:

- **Valid** payload → expected 2xx + correct resource.
- **Missing required field** → 400/422 with a clear error, no partial write.
- **Wrong type** (`"qty": "two"`) → 400, not a 500 stack trace.
- **Boundary / extreme** (`qty: 0`, `-1`, `999999`, very long strings) → BVA from Phase 1.
- **Extra/unknown fields** → documented behaviour (ignore or reject, consistently).
- **Injection-ish strings** (`"' OR 1=1 --`, `<script>`) → escaped/handled safely, never a 500.
- **Empty body / null / wrong Content-Type** → graceful 400/415."""),
               ],
               desk="A malformed import file or a weird character in a form field breaking an app is the same class of defect. Now you can send those values deliberately at the API, where the UI can't stop you.",
               takeaway="Validate keys, types, nesting, nulls, enums and units; use schemas; test missing/wrong-type/boundary/extra/malicious payloads.",
               ex=[
                   mcq("A response previously returned `total: 108.00` (number) and now returns `total: \"108.00\"` (string). This is:", [
                       "Harmless", "A breaking contract change that can break clients", "A UI-only issue", "A caching feature"], 1),
                   mcq("Which is the best expected result for a missing required field?", [
                       "500 Internal Server Error", "400/422 with a clear error and no partial write", "200 with an empty object", "A redirect"], 1),
                   mcq("Why send invalid payloads the UI would never allow?", [
                       "To make tests slower", "To verify server-side validation, which is the real security/robustness boundary", "Because the UI is broken", "It's required by REST"], 1),
               ]),

        lesson("api-03", "Authentication: keys, tokens, OAuth", 12,
               "Most API defects and most API test failures come down to authentication. Learn the three common schemes and the negative tests that belong with each.",
               [
                 ("The three schemes", """| Scheme | How it works | What to test |
|---|---|---|
| **API key** | A secret sent in a header (`X-API-Key`) or query param | Missing, wrong, expired, revoked key; key in query string (leaks in logs — flag it) |
| **Bearer / JWT token** | `Authorization: Bearer <token>`; often short-lived with a refresh token | Missing, malformed, expired, tampered signature, wrong audience, token after logout/password change |
| **OAuth 2.0 / OIDC** | An authorisation server issues tokens after a consent/login flow | Wrong scope, expired token, refresh rotation, callback/redirect validation, state parameter |

A **JWT** has three base64 parts: `header.payload.signature`. You can decode the payload at jwt.io to inspect claims (`sub`, `exp`, `role`, `scope`) — but **never paste a real production token into a public website**; use a throwaway test token."""),
                 ("The negative-test matrix (a portfolio favourite)", """For every protected endpoint, run this small matrix:

| # | Request | Expected |
|---|---|---|
| 1 | Valid token, correct role | 200 + correct data |
| 2 | No `Authorization` header | **401** |
| 3 | Malformed / random token | 401 |
| 4 | Expired token | 401 (and refresh works) |
| 5 | Valid token, insufficient role/scope | **403** |
| 6 | Valid token for user A requesting user B's resource | 403/404 — **IDOR / broken access control** |
| 7 | Token after logout or password change | 401 (revoked) |
| 8 | Token with a modified payload / bad signature | 401 |

Row 6 (accessing another user's data by changing an ID) is one of the most common serious security findings — and it is trivially testable by a manual QA Analyst with Postman."""),
                 ("Handling secrets in tests", """Never commit tokens, passwords or API keys. Store them as **environment variables / Postman environment variables**, use short-lived test credentials, rotate them, and redact them from HAR files and screenshots. A leaked secret in a public GitHub portfolio repo is an embarrassing and real problem."""),
               ],
               desk="'It works for me but not for them' is often a token/role difference. Row 6 is the same investigation as 'can this user see another user's ticket?' — now with a security name: IDOR.",
               takeaway="API keys, bearer/JWT, OAuth scopes; always run the 8-row auth negative matrix; keep secrets in env vars, never in repos or HARs.",
               ex=[
                   mcq("Valid token, wrong role. Expected status:", ["400", "401", "403", "500"], 2, "Authenticated but not authorised."),
                   mcq("Changing `/api/orders/9001` to `/api/orders/9002` and successfully reading someone else's order is:", [
                       "A caching feature", "An IDOR / broken access control defect", "A 404", "Expected REST behaviour"], 1),
                   mcq("Where should a test API token be stored?", [
                       "Hard-coded in the collection", "An environment variable / secret store", "In the README", "In a HAR attachment"], 1),
               ]),

        lesson("api-04", "Status codes, errors and idempotency", 12,
               "A good API is predictable when things go wrong. This lesson turns the HTTP status table into a concrete test matrix, and shows why idempotency deserves its own test cases.",
               [
                 ("The API test matrix", """For each endpoint, derive cases from the method and the spec:

| Case | Expected |
|---|---|
| Valid request | 200 / 201 / 204 + correct body/headers |
| Missing required field | 400 or 422 + helpful error body |
| Invalid value / boundary | 400/422; no partial state change |
| Unauthenticated / unauthorised | 401 / 403 |
| Resource not found | 404 (with a body that doesn't leak existence if privacy matters) |
| Wrong method (`PUT` on a GET-only route) | 405 + `Allow` header |
| Duplicate create / conflicting state | 409 |
| Too many requests | 429 + `Retry-After` |
| Upstream failure | 5xx with a clean error body, no stack trace, logged request ID |

Also assert the **error body shape** is consistent (`{ "error": { "code": "...", "message": "..." } }`) and that no stack trace or SQL is exposed. Error responses are part of the contract and are routinely under-tested."""),
                 ("Idempotency and the duplicate-submit test", """`PUT` and `DELETE` are idempotent; `POST` is not. Repeating a `POST /api/orders` normally creates **two orders** — exactly the double-click/double-submit defect from Phase 1, now visible at the API.

Test explicitly:

1. Send the same `POST` twice quickly → does it create duplicates? (If the spec says it should be idempotent, check for an **Idempotency-Key** header.)
2. Retry a failed payment after a timeout — is the customer charged twice?
3. `PUT /users/14` twice → same final state, no error.
4. `DELETE` twice → second returns 204 or 404, consistently.

Duplicate-order bugs cost real money and are a brilliant thing to have found in a portfolio project. They also explain why 'wait for the condition, not a fixed sleep' matters in UI tests."""),
                 ("Headers and response contracts", """Assert on more than the body: `Content-Type: application/json`, `Location` on a 201 (points to the new resource), `Cache-Control`/`ETag` where specified, `X-Request-ID` for traceability, and CORS headers for browser clients. A missing `Location` on a 201 or a `Content-Type: text/html` on a JSON endpoint is a legitimate defect."""),
               ],
               desk="'User clicked twice and got charged twice' is an incident you've seen. At the API layer it's a 30-second test — that's the leverage API testing gives you.",
               takeaway="Build a positive/negative/edge matrix per endpoint, assert error bodies and headers, and explicitly test duplicate POSTs and idempotency.",
               ex=[
                   mcq("Creating the same order twice with POST usually means:", [
                       "Idempotency", "Two orders — a duplicate-submit risk", "A 405", "A cache hit"], 1),
                   mcq("A 429 response should normally include:", ["A stack trace", "A Retry-After header", "A Location header", "A Set-Cookie"], 1),
                   mcq("Why assert on the error BODY, not just the status code?", [
                       "Status codes don't exist", "Consistent, leak-free error bodies are part of the API contract", "It's faster", "Postman requires it"], 1),
               ]),

        lesson("api-05", "Versioning, pagination and filtering", 11,
               "Real APIs return lists and evolve over time. Versioning, pagination and filtering produce a surprising number of off-by-one and compatibility defects — easy wins for a thorough tester.",
               [
                 ("Versioning", """Common strategies: URL path (`/api/v2/orders`), header (`Accept: application/vnd.shop.v2+json`), or query param. Test that:

- The old version still behaves as documented during the deprecation window.
- The new version's changed fields are handled by all clients.
- An unsupported version returns a clear 4xx, not a mysterious 500.
- Deprecation/`Sunset` headers and docs match reality.

A version bump is a **high-risk change** — regression-test every consumer you know about, including mobile apps that can't be force-updated."""),
                 ("Pagination", """```json
{ "items": [ ...20 objects... ], "page": 2, "pageSize": 20, "total": 47 }
```

Test the boundary set from Phase 1: page `0`, `1`, last page, last+1, `pageSize` 0 / 1 / max / max+1, negative values, non-numeric values, and sorting stability. Classic defects: an off-by-one that skips or duplicates the 20th/21st item, inconsistent ordering between page 1 and page 2, a `total` that doesn't match the actual rows, and a changed dataset between page requests causing duplicates."""),
                 ("Filtering, sorting and searching", """Test each documented filter individually and in combination: `?status=PAID&from=2026-04-01&to=2026-04-07&sort=total,desc`. Check case sensitivity, empty results (a clean empty array, not a 500), special characters in search terms, URL encoding, and **inclusive/exclusive date boundaries** (`from`/`to` — is midnight included?). Then verify the result against an independent SQL query — exactly the oracle idea from the SQL course."""),
               ],
               desk="'Page 2 shows one item twice and misses another' is a classic boundary/pagination ticket. You can now design that test before release instead of diagnosing it afterwards.",
               takeaway="Version bumps are high-risk regressions; test page 0/1/last/last+1, pageSize boundaries, filter combinations, and inclusive date edges.",
               ex=[
                   mcq("A list endpoint with pageSize=20 and total=47 has how many pages?", ["2", "3", "4", "20"], 1, "ceil(47/20) = 3 — and page 3 has 7 items, a boundary worth testing."),
                   mcq("A version bump to /api/v2 is a high-regression-risk change mainly because:", [
                       "URLs are longer", "Existing clients may break on changed fields", "It's slower", "It needs new icons"], 1),
                   mcq("For a date filter `from=2026-04-01&to=2026-04-07`, a key boundary question is:", [
                       "The server timezone only", "Whether the endpoints are inclusive and what timezone midnight means", "The font", "The HTTP method"], 1),
               ]),
    ],
    quiz="api-quiz",
)

# ---------------------------------------------------------------------------
# 12. Postman
# ---------------------------------------------------------------------------
POSTMAN = course(
    "postman", "Postman & API Test Automation", "Build a collection you can show an employer",
    "Hands-on from your first request to automated assertions: collections, environments, variables, the pm API, test-case design, the Collection Runner, Newman, and mocking. Ends with a public portfolio artefact.",
    "#ff6b35", "p3", "Weeks 13-14", "Core",
    [
        lesson("post-01", "Your first request", 10,
               "Postman is a client for sending HTTP requests and inspecting responses. No installation needed to start — you can use a free account or the desktop app. Everything here applies to Insomnia, Bruno, Hoppscotch or cURL too.",
               [
                 ("The anatomy of a request", """1. **Method** dropdown: `GET`, `POST`, ...
2. **URL**: `https://jsonplaceholder.typicode.com/users/1` (a free public practice API).
3. **Params** tab: query string key/values (`?page=2&limit=20`).
4. **Authorization** tab: No Auth / Bearer Token / API Key / OAuth 2.0.
5. **Headers** tab: `Content-Type: application/json`, custom headers.
6. **Body** tab (for POST/PUT): `raw` → JSON.
7. **Send** → the response pane: status, time, size, **Body**, **Headers**, **Cookies**, **Test Results**.

A good first exercise: `GET https://jsonplaceholder.typicode.com/users/1`, then inspect the 200 response, the `Content-Type` header and the timing. Then change the id to a non-existent one and observe the 404."""),
                 ("Saving and organising", """Save requests into a **Collection** (a folder of requests) named for the API, e.g. `Shop API — v2`. Group by resource with folders: `Auth / Users / Orders / Cart`. Give every request a meaningful name (`GET /orders/{id} — valid id`, `POST /orders — missing required field`), because the collection itself becomes documentation and a portfolio artefact. Add a **description** to each request explaining what it verifies."""),
                 ("Practice targets", """Free, no-key practice APIs: **JSONPlaceholder** (`jsonplaceholder.typicode.com`), **ReqRes** (`reqres.in`), **Petstore** (`petstore.swagger.io`), **httpbin** (`httpbin.org`, echoes requests — great for learning headers/status codes), **REST Countries**, and **DummyJSON**. Use these, never a real production API, for learning and for your portfolio."""),
               ],
               desk="Sending a request in Postman is the API equivalent of reproducing an issue directly against the service instead of through the front end — and you get the exact response as evidence.",
               takeaway="Method + URL + params + auth + headers + body → Send → inspect status, body, headers, timing. Save into a named collection.",
               ex=[
                   mcq("Where do you set `Content-Type: application/json` for a POST?", [
                       "The Params tab", "The Headers tab (and choose raw JSON in Body)", "The URL", "The Tests tab"], 1),
                   mcq("Which practice site echoes your request back, useful for learning headers/status codes?", [
                       "httpbin.org", "A production bank API", "Your email", "Google Fonts"], 0),
                   inp("What is a named folder of saved Postman requests called? (10 letters)", ["Collection", "collection"], hint="A group you can run together."),
               ]),

        lesson("post-02", "Environments, variables and chaining requests", 12,
               "Hard-coding URLs and tokens into every request is the fastest way to build a collection that breaks the moment you switch environments. Variables fix that — and let requests feed each other.",
               [
                 ("Variable scopes", """| Scope | Use |
|---|---|
| **Global** | Available everywhere (use sparingly) |
| **Environment** | `baseUrl`, `token`, `userId` per environment (dev / staging / prod) |
| **Collection** | Shared by all requests in a collection |
| **Local / data** | Per-run, e.g. from a CSV data file |

Reference them with double braces: `{{baseUrl}}/orders/{{orderId}}`. Create two environments — **Staging** and **Dev** — with different `baseUrl` values, and switch with one dropdown. That single habit makes your collection portable and safe."""),
                 ("Capturing values with the pm API", """The **Tests** tab runs JavaScript after the response arrives. Capture a value from one request and reuse it in the next:

```js
// In "POST /orders" → Tests tab
pm.test("Status is 201 Created", () => {
  pm.response.to.have.status(201);
});
const body = pm.response.json();
pm.collectionVariables.set("orderId", body.id);   // chain to the next request
```

Then `GET {{baseUrl}}/orders/{{orderId}}` uses it. This is a real **end-to-end API flow**: create → read → update → delete — exactly the scenario testing from the design course, without a browser."""),
                 ("Pre-request scripts and dynamic data", """The **Pre-request Script** tab runs *before* the request. Use it to generate unique test data or a timestamp:

```js
pm.collectionVariables.set("email", `qa+${Date.now()}@example.com`);
pm.collectionVariables.set("ts", new Date().toISOString());
```

Unique data prevents collisions when the collection runs repeatedly or in parallel. Also useful: computing a signature, refreshing a token, or reading a value from a CSV data file in the Collection Runner."""),
               ],
               desk="Using a variable is like using a ticket template with placeholders instead of pasting customer details into every note: one source of truth, no stale copies.",
               takeaway="Use {{variables}} and environments; chain requests by capturing IDs in the Tests tab; generate unique data in Pre-request scripts.",
               ex=[
                   mcq("Which syntax references a Postman variable?", ["${baseUrl}", "{{baseUrl}}", "#baseUrl", "(baseUrl)"], 1),
                   mcq("Which tab runs BEFORE the request is sent?", ["Tests", "Pre-request Script", "Body", "Cookies"], 1),
                   mcq("Why generate `qa+${Date.now()}@example.com` for test data?", [
                       "It looks realistic", "Unique values avoid collisions on repeated/parallel runs", "It's shorter", "Postman requires timestamps"], 1),
               ]),

        lesson("post-03", "Assertions with pm.test", 13,
               "A request that returns 200 is not a test. A test is a request plus **assertions** that fail when the contract is broken. This is the core skill of API test automation.",
               [
                 ("The assertion toolkit", """```js
pm.test("Status code is 200", () => {
  pm.response.to.have.status(200);
});

pm.test("Response is JSON and has the expected shape", () => {
  const body = pm.response.json();
  pm.expect(body).to.have.property("id");
  pm.expect(body.total).to.be.a("number");
  pm.expect(body.status).to.be.oneOf(["NEW", "PAID", "CANCELLED"]);
});

pm.test("Total matches the expected 10% discount", () => {
  pm.expect(pm.response.json().total).to.eql(108.00);
});

pm.test("Responds within 800 ms", () => {
  pm.expect(pm.response.responseTime).to.be.below(800);
});

pm.test("No stack trace leaked", () => {
  pm.expect(pm.response.text()).to.not.include("StackTrace");
});

pm.test("Content-Type is JSON", () => {
  pm.response.to.have.header("Content-Type", /application\\/json/);
});
```

`pm.test(name, callback)` creates a named result; `pm.expect` uses the Chai assertion library (`to.eql`, `to.be.a`, `to.have.property`, `to.be.oneOf`, `to.be.below`, `to.include`). One request can hold many tests — each appears separately in **Test Results**, which makes failures diagnosable."""),
                 ("What to assert, in priority order", """1. **Status code** (200/201/204/4xx/5xx as designed).
2. **Schema / shape**: required keys, types, enums, non-null.
3. **Business value**: the computed total, the persisted status, the returned ID format.
4. **Side effects**: a follow-up `GET` confirms creation/update; `DELETE` then `GET` → 404.
5. **Headers**: Content-Type, Location, Cache-Control, request ID.
6. **Performance budget**: response time below the agreed threshold (a light non-functional check).
7. **Security hygiene**: no stack trace, no secrets in the body, auth enforced.

> **Anti-pattern:** asserting only `status === 200`. A 200 with the wrong total passes that test — the exact class of bug from the discount example."""),
                 ("Negative tests in Postman", """Duplicate the request, rename it (`POST /orders — missing required field`), change the body, and change the assertion to `pm.response.to.have.status(422)`. Keep positive and negative cases side by side in the collection so the coverage is visible to anyone reviewing your portfolio."""),
               ],
               desk="A check without an assertion is like a ticket that says 'looked at it'. You already write down the expected vs actual; `pm.expect(actual).to.eql(expected)` is that sentence in code.",
               takeaway="Every request gets named pm.test assertions: status, shape, business value, side effects, headers, timing, hygiene.",
               ex=[
                   mcq("Which assertion checks that `total` is a number?", [
                       "pm.response.to.have.status(200)", "pm.expect(body.total).to.be.a('number')", "pm.response.json()", "pm.test('ok')"], 1),
                   mcq("Why is `pm.response.to.have.status(200)` alone a weak test?", [
                       "It's too slow", "A 200 with wrong data still passes — no business verification", "Postman can't do it", "It only works on GET"], 1),
                   inp("Which Postman object provides `response`, `test`, `expect` and `collectionVariables`?", ["pm"], hint="Two letters."),
               ]),

        lesson("post-04", "Designing API test cases", 12,
               "A collection is only as good as its test design. This lesson applies the Phase 1 techniques — equivalence partitioning, boundaries, decision tables, negative paths — to an API endpoint, producing a compact, defensible case list.",
               [
                 ("A worked case list for POST /api/orders", """| # | Case | Input | Expected |
|---|---|---|---|
| 1 | Valid order | 1 item, qty 2, valid coupon | 201, total 108.00, `Location` header |
| 2 | Missing required field | no `items` | 422 + error code |
| 3 | Wrong type | `"qty": "two"` | 400, no write |
| 4 | qty = 0 (boundary) | qty 0 | 422 |
| 5 | qty = 1 (boundary) | qty 1 | 201 |
| 6 | qty = max (boundary) | qty 999 | 201 or 422 per spec |
| 7 | qty = max+1 | qty 1000 | 422 |
| 8 | Negative qty | qty -1 | 422 |
| 9 | Empty items array | `[]` | 422 |
| 10 | Unknown coupon | `NOPE` | 422, total unchanged |
| 11 | Expired coupon | `EXPIRED` | 422 |
| 12 | Two coupons (decision rule) | both codes | documented behaviour |
| 13 | Premium + >$100 + express (decision table) | flags | correct discount/shipping |
| 14 | No auth | — | 401 |
| 15 | Wrong role | — | 403 |
| 16 | Duplicate POST | same body twice | 2 orders unless Idempotency-Key |
| 17 | Injection string in `note` | `' OR 1=1 --` | escaped, no 500 |
| 18 | Very long `note` | 10k chars | 422 or truncated per spec |
| 19 | Follow-up GET | id from #1 | 200 with same values |
| 20 | DELETE then GET | id from #1 | 204, then 404 |

Twenty cases, each one line — and the collection becomes a **living test-design document**. Add the requirement/spec reference in each request description."""),
                 ("Organising by risk", """Not all 20 are equal. Mark the auth, payment/total, and duplicate-submit cases `High`; put them in a **Smoke** folder that runs on every build. Keep the full set as the regression collection. This is risk-based testing from the documentation course applied to APIs."""),
                 ("Data-driven runs", """The Collection Runner can iterate a **CSV/JSON data file**: one row per case with `input` and `expectedStatus` columns, referenced as `{{input}}` / `{{expectedStatus}}` and `pm.iterationData.get('expectedStatus')` in tests. One request + 20 rows replaces 20 near-identical requests — a clean introduction to data-driven testing that you'll reuse in Playwright."""),
               ],
               desk="Twenty lines in a table is a familiar escalation matrix. You've written these by hand; now they're executable requests with assertions.",
               takeaway="Apply EP/BVA/decision tables/negative/auth/idempotency per endpoint; tag High-risk into a smoke folder; drive repeats with a data file.",
               ex=[
                   mcq("Which case is a boundary value for a quantity field capped at 999?", [
                       "qty 500", "qty 999 and qty 1000", "qty 2", "qty -999"], 1),
                   mcq("What belongs in a 'Smoke' folder for an orders API?", [
                       "All 20 cases", "High-risk auth, total, and duplicate-submit cases that run every build", "Only the slowest cases", "Only the UI tests"], 1),
                   mcq("The Collection Runner data file mainly enables:", [
                       "Faster internet", "Data-driven testing — one request, many input/expected rows", "Automatic screenshots", "Writing SQL"], 1),
               ]),

        lesson("post-05", "Collection Runner, Newman and CI", 12,
               "A collection you click by hand is useful; a collection that runs unattended on every push is a quality gate. This lesson takes it into the command line and CI.",
               [
                 ("Collection Runner", """Postman's **Collection Runner** executes every request in a collection in order, with optional iterations, delays and a data file. It shows pass/fail per assertion, timings, and lets you export results. Use it to check the whole flow after a change. Make sure requests are **order-independent where possible** (or explicitly chain via variables) and that the collection cleans up the data it creates."""),
                 ("Newman: the CLI runner", """```bash
npm install -g newman
newman run shop-api.postman_collection.json \
  -e staging.postman_environment.json \
  --reporters cli,htmlextra \
  --reporter-htmlextra-export report.html
```

Export your collection and environment as JSON from Postman and commit them to a repo (with **secrets removed** — use environment variables or a CI secret store). Newman exits with a **non-zero code on failure**, which is exactly what CI needs to fail a build. Add an HTML report as a build artefact so anyone can see what broke."""),
                 ("A minimal GitHub Actions job", """```yaml
name: API tests
on: [push, pull_request]
jobs:
  api:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20' }
      - run: npm install -g newman newman-reporter-htmlextra
      - run: newman run collections/shop.json -e env/staging.json \
               --env-var "token=${{ secrets.QA_TOKEN }}" \
               --reporters cli,htmlextra
      - uses: actions/upload-artifact@v4
        if: always()
        with: { name: api-report, path: report.html }
```

`if: always()` uploads the report even when tests fail — a small detail that makes debugging CI failures much less painful. Note `secrets.QA_TOKEN`, never a literal token in YAML."""),
               ],
               desk="Scheduled checks and alerting are already familiar. Newman is the same idea as a scheduled script that exits non-zero and pages someone — but for API contracts instead of server health.",
               takeaway="Runner for local full runs; Newman for CLI/CI with exit codes and HTML reports; keep secrets in CI variables, always upload reports.",
               ex=[
                   mcq("Why does Newman exit with a non-zero code when a test fails?", [
                       "To annoy developers", "So CI can fail the build automatically", "It's a bug", "To delete the report"], 1),
                   mcq("Where should an API token live in a CI workflow?", [
                       "Hard-coded in the YAML", "A CI secret / environment variable", "In the collection JSON", "In the README"], 1),
                   inp("What is the name of Postman's command-line collection runner? (6 letters)", ["Newman", "newman"], hint="Not 'Postman' — the CLI tool."),
               ]),

        lesson("post-06", "Mocks, contract testing and your portfolio collection", 12,
               "The final API skill: working when a dependency isn't ready, and turning everything you've built into a public artefact a hiring manager can actually inspect.",
               [
                 ("Mock servers and stubs", """When the real API is unfinished, unavailable, or charges money, a **mock server** returns controlled responses. Postman can generate a mock from example responses; tools like **WireMock**, **Mockoon**, **MSW**, or **Prism** (from an OpenAPI spec) do the same. Mocks let front-end and test work proceed in parallel.

Important honesty: a mock only proves your client handles the *documented* responses. It cannot catch a real integration defect. Record 'tested against mock, real integration pending' as **residual risk** — the same discipline as the environment lesson."""),
                 ("Contract testing in one paragraph", """A **contract** is the agreed request/response shape between a consumer (front end) and a provider (API). **Consumer-driven contract testing** (Pact) has the consumer publish its expectations, and the provider verifies it still satisfies them in its own pipeline. It catches breaking changes *before* integration, without a full end-to-end environment. For a first QA role you only need the concept and the vocabulary; knowing that schema validation and contract tests exist puts you ahead of most manual-only candidates."""),
                 ("Ship the portfolio collection", """Your Week 14 deliverable:

1. A public GitHub repo `qa-portfolio-api-tests` with a strong README.
2. `collections/shop-api.postman_collection.json` — 15+ requests, folders by resource, positive AND negative cases, descriptions with spec references.
3. `env/staging.postman_environment.json` with **placeholder** variables (no real secrets).
4. `tests/` notes: a markdown table of your 20 test cases and the techniques behind them.
5. A Newman command + GitHub Actions workflow that runs the collection.
6. An example HTML report (or a screenshot of a green run).
7. A short **'what I found'** section: list 2-3 deliberate defects you seeded or discovered, with the assertion that catches each.

That repo demonstrates test design, automation, tooling, CI and documentation in one link — the single most valuable artefact for a career changer with no QA job history."""),
               ],
               desk="A public, well-documented repo is the equivalent of a pristine knowledge base article: proof you can do the work, readable by someone who wasn't there when you did it.",
               takeaway="Mocks unblock work but leave residual risk; contract tests catch breaking changes; publish a documented collection + Newman CI run as a portfolio repo.",
               ex=[
                   mcq("A test passing against a mock proves:", [
                       "The real integration works", "The client handles the documented responses", "The database is correct", "Nothing at all"], 1),
                   mcq("Consumer-driven contract testing mainly catches:", [
                       "Slow queries", "Breaking API changes before integration", "UI typos", "Browser incompatibility"], 1),
                   mcq("Which file should NEVER be committed with real credentials?", [
                       "README.md", "The environment JSON / .env with tokens", "The collection JSON", "The workflow YAML"], 1),
               ]),
    ],
    quiz="postman-quiz",
)

# ---------------------------------------------------------------------------
# 13. Automation strategy
# ---------------------------------------------------------------------------
AUTOMATION = course(
    "automation", "Test Automation Strategy", "Decide WHAT to automate before HOW",
    "The test automation pyramid, what to automate (and what not to), ROI and maintenance cost, and choosing between Playwright, Cypress and Selenium. Thinking before tooling.",
    "#a78bfa", "p4", "Week 15", "Core",
    [
        lesson("auto-01", "The test automation pyramid", 11,
               "The pyramid is the most important idea in automation strategy: most tests should be small, fast and cheap; few should be slow end-to-end UI tests. Most failing automation efforts get this inverted.",
               [
                 ("The layers", """```
        /  E2E / UI  \\        Few: slow, brittle, expensive, high confidence
       /  Integration \\       Some: API/service tests, faster, stable
      /      Unit      \\      Many: fast, isolated, cheap, pinpoint failures
```

| Layer | Speed | Stability | Cost | Who | What it catches |
|---|---|---|---|---|---|
| Unit | milliseconds | Very high | Low | Developer | Logic errors in a function |
| API / integration | ~100 ms | High | Medium | QA + dev | Contract, business rules, data |
| E2E / UI | seconds-minutes | Lower | High | QA | Real user journeys across the stack |

The **anti-pattern** is the *ice-cream cone*: dozens of slow UI tests, almost no unit/API tests. Symptoms: a suite that takes an hour, fails randomly, and everyone ignores the results. Fix it by pushing checks down: if a rule can be verified at the API, don't verify it only through the browser."""),
                 ("Why UI tests are brittle", """UI tests depend on the DOM, CSS, timing, network, browser, animations, third-party scripts and test data. Any of those can change without a behaviour change. That's why **locators** (Phase 2, web-03) and **waits** matter so much. A UI test should verify *user-visible journeys*, not re-test every business rule already covered by API tests."""),
                 ("A practical split for a small team", """- **Unit**: developers, in their pipeline.
- **API contract + business rules**: your Postman/Newman collection (Phase 3) — high value, low maintenance.
- **E2E**: 10-25 critical journeys in Playwright — login, checkout, password reset, key admin flow.
- **Manual/exploratory**: usability, accessibility, visual, new features, edge cases — irreplaceable.

> Automation does **not** replace manual testing. It frees humans to do the testing that requires judgement."""),
               ],
               desk="Most incidents are found by users, not by checks. The pyramid is about putting cheap, fast checks where they catch the most, instead of a few slow ones everywhere.",
               takeaway="Many unit → some API → few E2E. Push checks down the pyramid; use UI tests for journeys, not business rules.",
               ex=[
                   mcq("Which layer should contain the MOST tests?", ["E2E / UI", "Integration / API", "Unit", "Manual"], 2),
                   mcq("The 'ice-cream cone' anti-pattern is:", [
                       "Too many unit tests", "Lots of slow UI tests and few unit/API tests", "Only manual testing", "No CI"], 1),
                   mcq("A discount calculation rule is best verified primarily at:", [
                       "The E2E UI layer only", "Unit / API layer, with one UI journey as a smoke check", "Manual only", "The CSS layer"], 1),
               ]),

        lesson("auto-02", "What to automate (and what not to)", 11,
               "Automation is an investment with an ongoing maintenance bill. Choosing the right candidates is a QA Analyst's strategic contribution — and a common interview question.",
               [
                 ("Good candidates", """Use a checklist; automate when most are true:

- **Repetitive** — run on every build/regression (smoke, login, checkout).
- **Stable / well understood** — requirements unlikely to churn.
- **High risk & high value** — payments, auth, data integrity.
- **Deterministic** — a clear, verifiable expected result (a good oracle).
- **Data-driven** — many input combinations from one script (BVA sets, pairwise).
- **Tedious or slow by hand** — large volumes, cross-browser matrix, bulk checks.
- **Deterministic environment** — test data and services are controllable."""),
                 ("Bad candidates", """- **One-off / exploratory** investigations and brand-new, changing features.
- **Usability, visual design, accessibility judgement** (axe can catch *some* a11y issues, but human review is essential).
- **Anything requiring human intuition**, subjective 'looks right', or unknown expected results.
- **Highly unstable features** — you'll spend all your time fixing the test, not finding bugs.
- **Tests with flaky external dependencies** you cannot control (fix the dependency or mock it first).

> **Rule of thumb:** if you can't state the expected result precisely, you can't automate the check. That's why test design comes first in this roadmap."""),
                 ("ROI and the maintenance bill", """A test's value = (bugs it catches × cost of those bugs) + (time saved per run × number of runs). Its cost = writing + **maintenance** + debugging false failures + infrastructure. A flaky test has *negative* value: it trains the team to ignore red builds.

Track and act on **flakiness rate**, not just pass rate. Quarantine a flaky test, fix or delete it — never just re-run until green. Prune stale tests (pesticide paradox) and add one test per escaped defect."""),
               ],
               desk="You know which repetitive checks on the desk are worth scripting and which need a human. Same judgement, applied to test suites.",
               takeaway="Automate stable, repetitive, high-risk, deterministic checks with clear oracles. Don't automate judgement or churn. Budget for maintenance; kill flaky tests.",
               ex=[
                   mcq("Which is the WORST automation candidate?", [
                       "Login smoke test run every build", "A brand-new feature changing daily that needs human exploratory judgement", "A 20-row boundary-value data set", "Checkout regression"], 1),
                   mcq("A test that fails randomly 20% of the time should be:", [
                       "Re-run until green", "Quarantined and fixed or deleted", "Left alone", "Marked as expected failure forever"], 1),
                   inp("What is the term for a test that sometimes passes and sometimes fails with no code change? (6 letters)", ["Flaky", "flaky test"], hint="Rhymes with 'shaky'."),
               ]),

        lesson("auto-03", "Choosing a tool: Playwright vs Cypress vs Selenium", 11,
               "You only need one tool for a first QA role. Understand the trade-offs so your choice is reasoned — and so you can answer 'why did you pick X?' in an interview.",
               [
                 ("The comparison", table(
                     ["", "Playwright", "Cypress", "Selenium WebDriver"],
                     [["Languages", "JS/TS, Python, Java, .NET", "JS/TS only", "Almost all languages"],
                      ["Browsers", "Chromium, Firefox, WebKit (Safari)", "Chromium, Firefox, WebKit (newer)", "All via drivers"],
                      ["Speed / stability", "Fast, auto-waiting, built-in parallelism", "Fast, excellent DX, runs in-browser", "Slower, more setup, most mature"],
                      ["Key strength", "Modern API, tracing, multi-tab/mobile emulation", "Time-travel debugging, great docs", "Legacy/enterprise breadth, W3C standard"],
                      ["Best for", "New projects, cross-browser, CI", "Front-end-heavy JS teams", "Large existing suites, multi-language shops"]])),
                 ("Why this roadmap uses Playwright", """- Modern, actively developed, and **auto-waits** on elements/actions — fewer flaky sleeps.
- **User-facing locators** (`getByRole`, `getByLabel`) match how we test by hand.
- Built-in **trace viewer**, screenshots, video, HTML reports and parallelism — all free.
- Excellent **API testing** support too (`request` fixture), so one framework covers UI + API.
- TypeScript/JavaScript — the language you just learned in Phase 2.

That said: **the concepts transfer**. Locators, assertions, waits, fixtures, the Page Object Model and CI are the same everywhere. If a job ad says Cypress or Selenium, you can switch in a week. Say that explicitly in interviews — it turns 'I only know one tool' into 'I understand the category'."""),
                 ("What to say in an interview", """*'I chose Playwright because of auto-waiting, cross-browser coverage with WebKit, and built-in traces and reports. But the underlying principles — resilient locators, explicit assertions, the Page Object Model, running in CI — are tool-independent; I could pick up Cypress quickly.'* Also mention that you deliberately **started with manual test design** so your automated checks assert the right things."""),
               ],
               desk="'I know this ticketing system, but the concepts transfer to yours' is a line you've probably used. Same answer, different tool category.",
               takeaway="Pick one modern tool and learn the transferable concepts. Playwright for this roadmap: auto-waits, user-facing locators, traces, free parallelism.",
               ex=[
                   mcq("Which Playwright feature most reduces flaky tests?", [
                       "Built-in video", "Auto-waiting for elements to be actionable before interacting", "Dark mode", "Multiple languages"], 1),
                   mcq("Which tool is a W3C standard with the broadest language support and the most legacy suites?", [
                       "Playwright", "Cypress", "Selenium WebDriver", "Postman"], 2),
                   mcq("The best answer to 'why Playwright?' emphasises:", [
                       "It's the newest", "Tool-independent principles plus concrete reasons (auto-wait, cross-browser, tracing)", "It's free", "Everyone uses it"], 1),
               ]),

        lesson("auto-04", "Anatomy of an automated test", 11,
               "Before writing Playwright, understand the shape every automated test shares. It is the same structure as a manual test case — setup, actions, assertion, cleanup — expressed as code.",
               [
                 ("The four phases", """```js
import { test, expect } from '@playwright/test';

test('rejects an invalid coupon at checkout', async ({ page }) => {
  // 1. SETUP / ARRANGE — preconditions & test data
  await page.goto('https://staging.example.com/cart');
  await page.getByLabel('Email').fill('qa.user14@example.com');
  // ... log in, add SKU-88 ...

  // 2. ACT — the steps
  await page.getByLabel('Promo code').fill('NOPE');
  await page.getByRole('button', { name: 'Apply' }).click();

  // 3. ASSERT — the expected result (the oracle!)
  await expect(page.getByText('Coupon NOPE is not valid')).toBeVisible();
  await expect(page.getByTestId('cart-total')).toHaveText('$50.00');

  // 4. CLEANUP / TEARDOWN — often handled by fixtures
});
```

Map it to a manual test case: **preconditions → setup**, **steps → act**, **expected result → assert**, **postconditions → teardown**. If you can't fill in the assert, you don't have a test — you have a script that clicks things."""),
                 ("Assertions, fixtures and hooks", """Assertions should be **specific and user-facing** (`toHaveText('$50.00')`, not `toBeTruthy()`). A **fixture** provides a prepared resource (a logged-in `page`, a fresh database, a seeded user) and cleans it up automatically. **Hooks** (`beforeEach`, `afterEach`) run setup/teardown around each test, so each case starts from a known state — the independence principle from the docs course.

Avoid **test interdependency**: `test B` must never rely on `test A` having run first. Parallel execution will expose that immediately."""),
                 ("Names, tags and reports", """A test name should complete the sentence 'this test verifies that...'. Use tags (`@smoke`, `@regression`, `@checkout`) so CI can run a subset: `npx playwright test --grep @smoke`. Good names and tags make a failure report readable at 2 a.m. — the same reason you write a clear ticket title."""),
               ],
               desk="Setup / steps / expected / cleanup is the manual test case you already write, in code. Nothing conceptually new — just executable.",
               takeaway="Arrange → Act → Assert → Cleanup; specific assertions; fixtures/hooks for independence; descriptive names and tags.",
               ex=[
                   order("Put the phases of an automated test in order:", [
                       "Arrange / setup & preconditions", "Act / perform the steps", "Assert / verify the expected result", "Cleanup / teardown"]),
                   mcq("Which assertion is better?", [
                       "expect(x).toBeTruthy()", "expect(page.getByTestId('cart-total')).toHaveText('$50.00')", "console.log(x)", "expect(true).toBe(true)"], 1),
                   mcq("Why should tests not depend on each other?", [
                       "They run faster that way", "Parallel/isolated execution and reliable failure diagnosis require independence", "Playwright forbids it", "It uses less memory"], 1),
               ]),
    ],
    quiz="automation-quiz",
)

# ---------------------------------------------------------------------------
# 14. Playwright from scratch
# ---------------------------------------------------------------------------
PLAYWRIGHT = course(
    "playwright", "Playwright from Scratch", "Write a real automated suite",
    "Node.js setup, first test, resilient locators, actions/assertions/waits, fixtures and config, the Page Object Model, data-driven tests, debugging and reports. Assumes only the JavaScript course.",
    "#3ddc84", "p4", "Weeks 16-18", "Hands-on",
    [
        lesson("pw-01", "Set up Node.js and a project", 11,
               "Everything here runs locally on your machine. Ten minutes of setup now saves hours of confusion later. Work inside the sandbox repo you created in Week 1.",
               [
                 ("Install and initialise", """```bash
# 1. Install Node.js LTS from nodejs.org, then verify:
node --version
npm --version

# 2. Create the project
mkdir qa-playwright && cd qa-playwright
npm init -y

# 3. Install Playwright and its test runner + browsers
npm init playwright@latest        # interactive: choose JS or TS, add GitHub Actions
# or manually:
npm i -D @playwright/test
npx playwright install            # downloads Chromium, Firefox, WebKit

# 4. Run the sample test
npx playwright test
npx playwright show-report        # opens the HTML report
```

`npm init playwright@latest` scaffolds `playwright.config.js`, a `tests/` folder, and an example spec — the fastest path to a working suite. Node's **package.json scripts** let you define `npm test`, `npm run test:smoke`, etc."""),
                 ("The files you'll work with", """| File | Purpose |
|---|---|
| `playwright.config.js` | Browsers/projects, `baseURL`, timeouts, retries, reporters, `webServer` |
| `tests/*.spec.js` | The test files |
| `pages/*.js` | Page objects (later lesson) |
| `test-results/` | Traces, screenshots, videos on failure (gitignored) |
| `playwright-report/` | HTML report (gitignored) |
| `package.json` / `package-lock.json` | Dependencies and scripts |
| `.github/workflows/playwright.yml` | CI job (scaffolded for you) |

Add to `.gitignore`: `node_modules/`, `test-results/`, `playwright-report/`, `.env`. **Never commit node_modules.**"""),
                 ("Config essentials", """```js
import { defineConfig, devices } from '@playwright/test';
export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  retries: process.env.CI ? 2 : 0,       // retry only in CI, and investigate flakes
  reporter: [['html'], ['list']],
  use: {
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox',  use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit',   use: { ...devices['Desktop Safari'] } },
  ],
});
```

`baseURL` means tests can use `page.goto('/cart')`. `trace` + screenshot + video on failure give you evidence without slowing every run. Retries in CI should be a **signal to investigate**, not a way to hide flakiness."""),
               ],
               desk="Installing and configuring a tool, then verifying it works, is the same discipline as setting up a new ticketing client or VPN profile — plus a `.gitignore` so you don't ship the whole toolbox.",
               takeaway="Node LTS → npm init playwright → install browsers → run sample → read the report; know config, test files, reports and .gitignore.",
               ex=[
                   mcq("Which command downloads the browser binaries Playwright needs?", [
                       "npm test", "npx playwright install", "npm init -y", "git clone"], 1),
                   mcq("Which folder should be in .gitignore?", [
                       "tests/", "node_modules/ and test-results/", "playwright.config.js", "package.json"], 1),
                   inp("Which config key lets tests use `page.goto('/cart')` instead of a full URL?", ["baseURL", "baseUrl"], hint="Set under `use`."),
               ]),

        lesson("pw-02", "Your first test", 11,
               "Write a test that fails for the right reason, then make it pass. Understanding the run/fix loop matters more than memorising syntax.",
               [
                 ("A complete first spec", """```js
// tests/login.spec.js
import { test, expect } from '@playwright/test';

test('a valid user can sign in', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('qa.user14@example.com');
  await page.getByLabel('Password').fill('ValidPass!23');
  await page.getByRole('button', { name: 'Sign in' }).click();

  await expect(page).toHaveURL(/.*dashboard/);
  await expect(page.getByRole('heading', { name: 'Welcome back' })).toBeVisible();
});

test('an invalid password shows an error', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('qa.user14@example.com');
  await page.getByLabel('Password').fill('wrong');
  await page.getByRole('button', { name: 'Sign in' }).click();

  await expect(page.getByText('Invalid email or password')).toBeVisible();
  await expect(page).toHaveURL(/.*login/);   // must NOT have navigated away
});
```

Two tests, one positive and one negative — exactly the pairing you learned in test design. Run with `npx playwright test tests/login.spec.js`, then `npx playwright show-report`."""),
                 ("Running, filtering and debugging", """```bash
npx playwright test                         # all tests, all browsers
npx playwright test tests/login.spec.js      # one file
npx playwright test -g "invalid password"   # grep by title
npx playwright test --project=chromium       # one browser
npx playwright test --headed                 # watch it run
npx playwright test --debug                  # step through with the inspector
npx playwright test --ui                     # interactive UI mode (excellent for learning)
```

**UI mode** is the best learning environment: it shows each step, the DOM snapshot, and lets you pick locators interactively. When a test fails, read the **error + the call log** first — Playwright tells you exactly which locator it waited for and why it timed out."""),
                 ("Auto-waiting: the big difference", """`getByRole(...).click()` automatically waits for the element to be **visible, stable, enabled and receiving events** before acting. `expect(locator).toBeVisible()` retries until the assertion passes or the timeout expires. That is why you almost never need `sleep()`.

```js
// BAD — arbitrary sleep, slow and flaky
await page.waitForTimeout(3000);

// GOOD — wait for the actual condition
await expect(page.getByText('Order confirmed')).toBeVisible();
```

If a test still fails intermittently, that is either a real race-condition defect or a locator/wait problem — investigate, don't paper over it."""),
               ],
               desk="'Click, then check the expected message appeared' is literally a manual test case. Playwright just runs it 200 times without getting bored.",
               takeaway="Positive + negative pair; use UI mode and call logs; trust auto-waiting; assert on user-visible outcomes, never fixed sleeps.",
               ex=[
                   mcq("Why is `await expect(locator).toBeVisible()` better than `waitForTimeout(3000)`?", [
                       "It's shorter", "It waits for the actual condition and adapts — faster and less flaky", "It's required syntax", "It changes the browser"], 1),
                   mcq("Which command opens Playwright's interactive step-through UI?", [
                       "--headed", "--ui", "--debug", "--grep"], 1),
                   mcq("What does `click()` auto-wait for?", [
                       "Nothing", "Element to be visible, stable, enabled and receiving events", "The whole page to load every image", "3 seconds exactly"], 1),
               ]),

        lesson("pw-03", "Locators: the #1 maintenance skill", 12,
               "Most automation maintenance is fixing broken locators. Choosing resilient, user-facing locators from day one is the highest-leverage habit in this whole course.",
               [
                 ("Preference order", """```js
page.getByRole('button', { name: 'Sign in' })     // BEST: mirrors what a user perceives
page.getByLabel('Email')                          // form fields via their <label>
page.getByPlaceholder('Search orders')
page.getByText('Order confirmed')
page.getByTestId('cart-total')                    // explicit, stable test hook
page.locator('[data-testid="submit"]')            // CSS attribute selector
page.locator('#email')                            // id — OK if stable
page.locator('//html/body/div[3]/...')            // WORST: brittle absolute XPath
```

Why roles/labels win: they survive CSS/layout refactors, they match how a manual tester describes the element, and they double as a **partial accessibility check** (if `getByRole` can't find a button, maybe it isn't marked up as one)."""),
                 ("Strictness, filtering and chaining", """Playwright locators are **strict**: an action fails if the locator matches *more than one* element. That is a feature — ambiguity should be resolved, not silently picked.

```js
page.getByRole('listitem').filter({ hasText: 'SKU-88' })
    .getByRole('button', { name: 'Remove' });

page.getByRole('row', { name: /Order 9001/ }).getByTestId('total');

const submit = page.getByRole('button', { name: 'Sign in' });
await expect(submit).toBeEnabled();
await submit.click();
```

Chain from a **container** to disambiguate repeated elements. Use `nth()` only as a last resort (it reintroduces positional brittleness). Use `page.locator('...').count()` in assertions when you truly need a number."""),
                 ("Locators and accessibility", """Ask your team to add `data-testid` attributes to elements that are genuinely hard to target — that's a normal, valuable QA/developer collaboration. And when `getByRole('button', {name: ...})` fails on a `<div onclick>`, you've found an accessibility defect worth logging: keyboard and screen-reader users can't operate it either."""),
               ],
               desk="A brittle locator is like a runbook step that says 'click the third button' — it breaks the moment someone reorders the page. Describe the element by what it *is* instead.",
               takeaway="Prefer role/label/text/testid; avoid absolute XPath and nth(); scope with filter/chaining; ask for data-testid when needed.",
               ex=[
                   mcq("Which locator is most resilient?", [
                       "page.locator('/html/body/div[2]/button')", "page.getByRole('button', { name: 'Sign in' })", "page.locator('div > button:nth-child(3)')", "A coordinate click"], 1),
                   mcq("Playwright locators are 'strict'. That means:", [
                       "They only work in strict mode", "An action fails if the locator matches multiple elements, forcing you to disambiguate", "They reject CSS", "They run slower"], 1),
                   mcq("A `getByRole('button')` lookup fails on a clickable `<div>`. Besides a locator problem, this suggests:", [
                       "A database issue", "An accessibility defect (not keyboard/screen-reader operable)", "A slow network", "A CSS typo"], 1),
               ]),

        lesson("pw-04", "Actions, assertions and waits", 12,
               "A compact reference for the interactions and assertions you'll use in almost every test, plus the waiting rules that keep suites reliable.",
               [
                 ("Actions", """```js
await page.goto('/cart');
await locator.fill('text');            // clears then types (inputs)
await locator.type('text');            // keystrokes (rarely needed)
await locator.click();
await locator.check() / uncheck();     // checkboxes
await locator.selectOption('GB');      // <select>
await locator.press('Enter');
await locator.hover();
await locator.setInputFiles('file.pdf');
await page.keyboard.press('Tab');
await page.reload();
await page.goBack();
```

Prefer `fill()` over `type()` for inputs — it's faster and deterministic. For file uploads, keep a small sample file in the repo (`fixtures/`)."""),
                 ("Assertions", """```js
await expect(page).toHaveURL(/dashboard/);
await expect(page).toHaveTitle(/Shop/);
await expect(locator).toBeVisible();
await expect(locator).toBeHidden();
await expect(locator).toHaveText('$50.00');
await expect(locator).toContainText('not valid');
await expect(locator).toHaveValue('qa@example.com');
await expect(locator).toBeEnabled() / toBeDisabled();
await expect(locator).toHaveCount(3);
await expect(locator).toHaveAttribute('aria-invalid', 'true');
```

Use `toHaveText` for exact values and `toContainText` for messages. Assert **what should NOT happen too** (`toHaveURL(/login/)` after a failed sign-in) — negative assertions catch silent failures. Avoid `expect(await locator.textContent()).toBe(...)`; it snapshots once instead of retrying."""),
                 ("Waiting rules", """1. Trust **auto-waiting** for actions and web-first assertions.
2. For a specific event: `await page.waitForResponse(r => r.url().includes('/api/orders') && r.status() === 201)`.
3. For navigation: `await page.waitForURL('**/confirmation')`.
4. For network idle, prefer a concrete signal over `waitForLoadState('networkidle')` (unreliable with polling/analytics).
5. Set a sane global timeout (e.g. 30 s) and per-assertion timeouts for genuinely slow operations.
6. **Never** `waitForTimeout` to 'fix' a flaky test — find the condition or the real race condition."""),
               ],
               desk="Checking both 'the confirmation appeared' AND 'the URL did not change to an error page' is the same thoroughness as checking a service is up *and* its dependencies are healthy.",
               takeaway="fill/click/check/selectOption; web-first expect() assertions including negatives; wait on real signals, never arbitrary sleeps.",
               ex=[
                   mcq("Which assertion retries until the condition is met (web-first)?", [
                       "expect(await locator.textContent()).toBe('x')", "await expect(locator).toHaveText('x')", "console.log", "assert(true)"], 1),
                   mcq("What is the right way to wait for a specific API response?", [
                       "waitForTimeout(2000)", "page.waitForResponse(r => r.url().includes('/api/orders') && r.status() === 201)", "A for loop", "disable cache"], 1),
                   mcq("Why assert `toHaveURL(/login/)` after a failed sign-in?", [
                       "It's required", "It catches the silent failure of navigating away despite an error", "It speeds up the test", "It sets a cookie"], 1),
               ]),

        lesson("pw-05", "Fixtures, hooks, config and environments", 12,
               "Repeating login in every test is slow and makes suites order-dependent. Fixtures and configuration solve both, and they're what turns a folder of scripts into a framework.",
               [
                 ("Hooks", """```js
test.describe('Checkout', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
    await loginAs(page, 'qa.user14@example.com');
    await page.goto('/cart');
  });
  test.afterEach(async ({ page }) => {
    await clearCart(page);          // leave a clean state
  });

  test('applies a valid coupon', async ({ page }) => { /* ... */ });
});
```

`beforeEach`/`afterEach` run around **every** test, guaranteeing a known starting state. Keep them short; a slow hook multiplies across the whole suite."""),
                 ("Custom fixtures", """Playwright lets you **extend** the built-in `page` fixture:

```js
// fixtures.js
import { test as base } from '@playwright/test';
export const test = base.extend({
  loggedInPage: async ({ page }, use) => {
    await page.goto('/login');
    await page.getByLabel('Email').fill(process.env.QA_EMAIL);
    await page.getByLabel('Password').fill(process.env.QA_PASSWORD);
    await page.getByRole('button', { name: 'Sign in' }).click();
    await page.waitForURL('**/dashboard');
    await use(page);                 // hand the ready page to the test
    await page.context().clearCookies();  // teardown
  },
});
export { expect } from '@playwright/test';
```

Tests import `test` from your fixture file instead of `@playwright/test` and get a ready-to-use `loggedInPage`. Note credentials come from **environment variables**, never hard-coded."""),
                 ("Environments, projects and parallelism", """```js
use: {
  baseURL: process.env.BASE_URL,          // dev / staging switch
  storageState: 'auth/state.json',         // reuse a logged-in session
}
```

`storageState` saves cookies/localStorage after one login and reuses them across tests — a big speed win. `projects` run the same tests across browsers/devices/viewports; `fullyParallel: true` and `workers` control concurrency. Parallelism exposes hidden test-data collisions and ordering dependencies, which is *good*: those are real defects in your suite. Set `retries` in CI but always investigate the flakes."""),
               ],
               desk="A standard operating environment / template with the right accounts pre-provisioned is a fixture. You already know why reusing a broken starting state wastes everyone's time.",
               takeaway="beforeEach/afterEach for a known state; custom fixtures (use + teardown); env vars for config; storageState, projects and workers for speed and coverage.",
               ex=[
                   mcq("What is the main benefit of `storageState`?", [
                       "It makes tests slower", "Reuse one authenticated session instead of logging in for every test", "It stores screenshots", "It disables parallelism"], 1),
                   mcq("Where should test credentials live?", [
                       "In the spec file", "Environment variables / CI secrets", "In the README", "In the HTML report"], 1),
                   mcq("Running tests in parallel is useful because it also:", [
                       "Uses less CPU", "Exposes hidden data collisions and ordering dependencies", "Removes the need for assertions", "Guarantees no flakes"], 1),
               ]),

        lesson("pw-06", "Page Object Model and data-driven tests", 13,
               "Two techniques that keep a growing suite maintainable: separate *what the page looks like* from *what the test verifies*, and drive many cases from one test.",
               [
                 ("Page Object Model (POM)", """```js
// pages/CartPage.js
export class CartPage {
  constructor(page) { this.page = page; }
  async goto()      { await this.page.goto('/cart'); }
  async apply(code) {
    await this.page.getByLabel('Promo code').fill(code);
    await this.page.getByRole('button', { name: 'Apply' }).click();
  }
  total()           { return this.page.getByTestId('cart-total'); }
  error()           { return this.page.getByTestId('promo-error'); }
}

// tests/cart.spec.js
test('rejects an invalid coupon', async ({ page }) => {
  const cart = new CartPage(page);
  await cart.goto();
  await cart.apply('NOPE');
  await expect(cart.error()).toContainText('not valid');
  await expect(cart.total()).toHaveText('$50.00');
});
```

When the UI changes, you update **one** page object, not 30 tests. Tests read like business rules; selectors live in one place. Avoid the trap of putting assertions inside page objects — keep them in tests (or expose query methods). POM is tool-independent and a common interview topic."""),
                 ("Data-driven / parameterised tests", """```js
const cases = [
  { qty: 0,    expected: 'reject' },
  { qty: 1,    expected: 'accept' },
  { qty: 999,  expected: 'accept' },
  { qty: 1000, expected: 'reject' },
  { qty: -1,   expected: 'reject' },
];

for (const { qty, expected } of cases) {
  test(`quantity ${qty} is ${expected}ed`, async ({ page }) => {
    await page.goto('/cart');
    await page.getByLabel('Quantity').fill(String(qty));
    await page.getByRole('button', { name: 'Update' }).click();
    const err = page.getByText('Invalid quantity');
    if (expected === 'reject') await expect(err).toBeVisible();
    else await expect(err).toBeHidden();
  });
}
```

That's the **boundary value set from Phase 1, executable**. One test definition, five named cases, each reported separately. For larger matrices, load data from a JSON/CSV file or generate a pairwise set."""),
                 ("Test data helpers and faker", """Keep fixtures in `fixtures/` (JSON files, sample uploads). Generate unique values with a timestamp or a library like `@faker-js/faker` (`faker.internet.email()`) so repeated runs don't collide. Clean up created records via an API call in `afterEach` — faster and more reliable than clicking through a UI to delete them."""),
               ],
               desk="A POM is a runbook: one documented procedure for 'apply a coupon' that every test reuses. Change the app, update the runbook once — not 30 copies.",
               takeaway="POM = selectors/actions in one class, assertions in tests; loop over data tables for BVA/pairwise; generate unique data and clean up via API.",
               ex=[
                   mcq("What is the main benefit of the Page Object Model?", [
                       "Tests run faster", "A UI change is fixed in one place instead of every test", "It removes assertions", "It replaces CI"], 1),
                   mcq("Where should assertions live in a POM design?", [
                       "Inside page objects", "In the test files", "In the config", "In the README"], 1),
                   mcq("Driving 5 boundary values through one test definition is called:", [
                       "Exploratory testing", "Data-driven / parameterised testing", "Smoke testing", "Manual testing"], 1),
               ]),

        lesson("pw-07", "Debugging, reports, flakiness and cross-browser", 12,
               "A suite is only trustworthy if failures are diagnosable. This lesson covers the evidence Playwright gives you, how to kill flakiness, and how to run the same suite across browsers in parallel.",
               [
                 ("Failure evidence", """```bash
npx playwright show-report                 # HTML report with steps, errors, attachments
npx playwright show-trace trace.zip        # time-travel: DOM snapshots, network, console
```

On failure (with `trace: 'on-first-retry'`), you get a **screenshot**, a **video**, and a **trace** you can scrub through: DOM snapshot per action, network requests, console logs, and the exact locator that timed out. Attach these from CI as build artefacts. This is the automated equivalent of the evidence pack from the Defects course — and it's why 'works on my machine' stops being a debate."""),
                 ("A flakiness-killing checklist", """1. Reproduce with `--repeat-each=20` on the single test.
2. Read the error and call log — which locator/condition timed out?
3. Replace any `waitForTimeout` with a real condition.
4. Make locators strict and unambiguous.
5. Remove ordering dependencies; ensure each test creates its own data.
6. Check for races: duplicate submits, animations, network polling, debounce.
7. Stabilise the environment: seeded data, no shared mutable records, mocked flaky 3rd parties.
8. **Quarantine** a still-flaky test, open a ticket, fix or delete. Never just raise retries to hide it.

Track flakiness **rate** and quarantine count as suite health metrics — not just pass %."""),
                 ("Cross-browser, mobile and parallelism", """`projects` in config run the same tests against Chromium, Firefox and WebKit (Safari's engine). Add a mobile project with `devices['iPhone 13']` for responsive checks — but don't duplicate *all* tests on mobile; pick key journeys (risk-based again). Use `npx playwright test --project=webkit --workers=4` for targeted runs. `shard` splits a suite across CI machines (`--shard=1/3`).

Common cross-browser findings: date input formats, `Intl`/locale differences, CSS features, optional chaining on older engines, viewport/overflow issues, and file-upload behaviour. Each one is a genuine defect worth a well-written report."""),
               ],
               desk="A trace viewer is the log bundle, screenshot and timeline rolled into one — exactly what you wish every escalation came with. Make your automation produce that automatically.",
               takeaway="Use reports/traces/screenshots as evidence; kill flakes with a checklist, quarantine the rest; run projects across browsers/devices with parallelism and sharding.",
               ex=[
                   mcq("Which command replays a recorded trace with DOM snapshots and network calls?", [
                       "npx playwright test", "npx playwright show-trace trace.zip", "npm install", "npx playwright codegen"], 1),
                   mcq("The correct response to a persistently flaky test is:", [
                       "Increase retries to 10", "Quarantine, investigate, fix or delete it", "Run it only at night", "Ignore it"], 1),
                   mcq("Which browser engine does Playwright's 'webkit' project represent?", [
                       "Chrome", "Safari", "Edge legacy", "Firefox"], 1),
               ]),
    ],
    quiz="playwright-quiz",
)

# ---------------------------------------------------------------------------
# 15. CI/CD & quality engineering
# ---------------------------------------------------------------------------
CICD = course(
    "cicd", "CI/CD & Quality Engineering", "Make quality automatic",
    "What CI/CD means for a tester, a GitHub Actions pipeline that runs your tests on every push, reports and artefacts, quality gates and shift-left, and metrics that inform rather than mislead.",
    "#4f8cff", "p4", "Weeks 19-20", "Core",
    [
        lesson("ci-01", "CI/CD in plain language", 11,
               "Continuous Integration and Continuous Delivery are just disciplined automation of the steps a team already does: build, test, review, deploy. QA's job is to put the right checks in the right place.",
               [
                 ("The pipeline", """```
Developer pushes code
   ↓  CI (Continuous Integration)
  lint / static checks → unit tests → build → API tests → E2E smoke tests
   ↓  CD (Continuous Delivery / Deployment)
  deploy to staging → more tests → (approval) → deploy to production → smoke
```

**CI** = merge small changes frequently into a shared branch, each automatically built and tested. **CD** = keep the code in a deployable state; *delivery* means a human approves production, *deployment* means it's automatic. The point is **fast feedback**: a defect found 10 minutes after a commit is cheap; one found in next week's manual regression is not."""),
                 ("Where QA adds checks", """| Stage | Fast checks to add | Why |
|---|---|---|
| Pre-commit / PR | lint, unit tests, type checks, API contract tests | Seconds; catches most mistakes |
| Post-merge to staging | E2E smoke, full API suite, DB migrations | Minutes; realistic environment |
| Pre-release gate | High-risk regression pack, a11y scan, security scan | Go/no-go evidence |
| Post-deploy (prod) | Tiny smoke + synthetic monitoring | Catches environment/config issues |

The **test pyramid** is a pipeline design: cheap checks early and often, expensive checks later and less often. A tester who can say 'put the API contract tests in the PR gate and keep only 10 smoke E2E tests there' is thinking like a quality engineer."""),
                 ("Shift-left, concretely", """Shift-left isn't a slogan: it's reviewing acceptance criteria before coding, adding a failing test with the bug report, running contract tests on every PR, and giving developers a fast local test command. The measurable outcome is a shorter **feedback loop** and fewer escaped defects."""),
               ],
               desk="A change advisory process with checks before go-live is a pipeline with human gates. CI automates the checks so the humans only handle the exceptions.",
               takeaway="CI = build+test every change; CD = keep deployable. Put cheap checks early, expensive checks later; shorten the feedback loop.",
               ex=[
                   mcq("What does CI primarily give a team?", [
                       "Longer releases", "Fast automated feedback on every change", "Fewer developers", "No need for tests"], 1),
                   mcq("Which checks belong in a PR gate?", [
                       "A 2-hour full E2E suite", "Fast lint/unit/API contract tests", "Manual exploratory only", "Production load tests"], 1),
                   mcq("Continuous *Delivery* vs *Deployment* differs by:", [
                       "The programming language", "Whether a human approves the production release", "The number of tests", "The browser"], 1),
               ]),

        lesson("ci-02", "A GitHub Actions pipeline for Playwright", 12,
               "Turn your local suite into a quality gate that runs on every push and pull request. This lesson gives a complete, explained workflow you can paste into your portfolio repo.",
               [
                 ("The workflow", """```yaml
# .github/workflows/playwright.yml
name: Playwright tests
on:
  push: { branches: [main] }
  pull_request:
  workflow_dispatch:            # allow a manual run

jobs:
  test:
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '20', cache: 'npm' }
      - run: npm ci                       # clean, lockfile-exact install
      - run: npx playwright install --with-deps chromium
      - run: npm test
        env:
          BASE_URL: ${{ vars.STAGING_URL }}
          QA_EMAIL: ${{ secrets.QA_EMAIL }}
          QA_PASSWORD: ${{ secrets.QA_PASSWORD }}
      - uses: actions/upload-artifact@v4
        if: always()                      # upload even on failure
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 7
```

Key details: `npm ci` (reproducible, not `npm install`), `timeout-minutes` (no hung builds), secrets in the GitHub secret store, `if: always()` for reports, and `workflow_dispatch` so anyone can trigger a run by hand."""),
                 ("Reading a failed run", """1. Open the job log; find the failing **step** and read the error (Playwright prints a concise summary).
2. Download the **report artefact**; open `index.html` or the trace.
3. Decide: is it a **product defect** (log it), a **test defect** (fix the locator/assertion), or an **environment/infra defect** (staging down, secret expired, browser download failed)?
4. Fix, push, and confirm green. Never re-run blindly three times to get a green tick — that's the CI version of ignoring a flaky test.

Classify failures explicitly in your notes; teams that don't will slowly stop trusting the pipeline."""),
                 ("Branch protection and required checks", """In repo settings, mark the test job as a **required status check** for `main`, so a PR cannot merge while tests are red. Add a **CODEOWNERS** rule so test-code changes get reviewed by QA. That's a real quality gate — policy, not just a script."""),
               ],
               desk="A failed scheduled job with logs and an artefact is a ticket with evidence attached. You already triage those; now you author the job itself.",
               takeaway="Checkout → setup-node → npm ci → install browsers → test → always upload report; secrets in the store; required checks enforce the gate.",
               ex=[
                   mcq("Why `npm ci` instead of `npm install` in CI?", [
                       "It's faster", "It installs exactly the lockfile versions — reproducible builds", "It downloads browsers", "It skips tests"], 1),
                   mcq("Why `if: always()` on the upload-artifact step?", [
                       "To make builds slower", "To keep the report downloadable even when tests fail", "It's required syntax", "To delete old runs"], 1),
                   mcq("A required status check means:", [
                       "Tests run only once", "A PR cannot merge while the test job is red", "Everyone must comment", "The branch is deleted"], 1),
               ]),

        lesson("ci-03", "Reports, artefacts and failure triage", 11,
               "A pipeline nobody can read is a pipeline nobody trusts. This lesson covers what a useful report contains and how to turn a red build into an actionable decision.",
               [
                 ("What a good test report shows", """- **Summary**: total, passed, failed, skipped, duration, per-browser breakdown.
- **Each failure**: test name, error, the failing step, call log, screenshot, trace/video link, environment variables (redacted), build/commit SHA.
- **Trends**: pass rate and duration over the last N runs; flakiness rate; slowest tests.
- **Links**: the commit/PR, the deployed build, the defect tracker.

Playwright's HTML reporter and `htmlextra` for Newman give most of this free. Allure and ReportPortal add history and dashboards for larger teams. Keep reports as **build artefacts** with a retention window, and link them from the PR."""),
                 ("Triage categories", """| Category | Action |
|---|---|
| **Product defect** | Reproduce, log a defect with build + trace, link to the failed test |
| **Test defect** | Fix locator/assertion/data; add a regression test for the test itself if needed |
| **Flake** | Quarantine the test, open a ticket, fix root cause; do not just retry |
| **Environment / infra** | Staging down, expired secret, browser download failed — fix infra, re-run once |
| **Expected change** | UI/API intentionally changed → update tests as part of the same PR |

The discipline: **every red build gets one of these labels**. Unclassified failures are how pipelines lose credibility."""),
                 ("Dashboards without vanity metrics", """Show: build pass rate, flakiness rate, mean time to feedback, escaped defects, open defects by severity, and coverage of high-risk requirements. Avoid: raw number of tests (bigger isn't better), bugs-per-tester (weaponises metrics), and %-closed without context. A dashboard should change a decision, not decorate a wall."""),
               ],
               desk="Incident dashboards already taught you that a green overall status can hide a red critical service. Same rule: show the breakdown, not just the headline percentage.",
               takeaway="Reports need per-failure evidence + trends; label every red build as product/test/flake/infra/expected; measure feedback time and escapes.",
               ex=[
                   mcq("A test fails because staging was down. Category:", [
                       "Product defect", "Environment / infra", "Test defect", "Expected change"], 1),
                   mcq("Which metric should NOT be used to judge a tester's productivity?", [
                       "Mean time to feedback", "Number of bugs logged per tester", "Escaped defect trend", "Flakiness rate"], 1),
                   mcq("A good failure report includes:", [
                       "Only a red X", "Test name, error, build SHA, screenshot/trace and environment", "The developer's home address", "Nothing but a timestamp"], 1),
               ]),

        lesson("ci-04", "Quality gates, shift-left and Definition of Done", 11,
               "A quality gate is an automated, measurable condition that must pass before code advances. This lesson connects gates to the Definition of Done and to the risk-based decisions from Phase 1.",
               [
                 ("Designing gates", """| Gate | Example condition | Blocks |
|---|---|---|
| Pre-merge | Unit tests pass, lint clean, API contract suite green, no new Critical static findings | Merging the PR |
| Post-deploy to staging | Smoke E2E suite green, no 5xx in the first 5 min | Promotion to release candidate |
| Pre-release | 0 open Critical/Major defects, 100% of High-priority cases executed, PO sign-off | Production release |
| Post-release | Production smoke + synthetic monitor green | Declaring the release done |

A gate must be **fast, deterministic and actionable**. A slow or flaky gate gets disabled by the team — the fastest way to lose all the value. Keep the PR gate under ~5-10 minutes; push slower suites to nightly or pre-release."""),
                 ("Definition of Done", """A story is 'Done' only when the team-wide checklist is satisfied:

```
[ ] Acceptance criteria verified (QA)
[ ] Code reviewed and merged
[ ] Unit tests + relevant automated suites green in CI
[ ] No open Critical/Major defects for this story
[ ] Test cases written and linked in the RTM
[ ] Docs / release notes / config updated
[ ] Deployed to staging and smoke-tested
```

QA owns the first, fourth and fifth lines. When someone asks 'is it done?', the DoD gives a measurable answer instead of an opinion — the same function as exit criteria in the test plan."""),
                 ("The tester's role in quality ownership", """A modern QA Analyst does not 'own quality' alone — **the whole team does**. Your job is to make quality visible: define gates, provide fast feedback, coach on testability, and surface risk with evidence. Phrase it as *'I help the team make good release decisions'*, not *'I block releases'*. That framing lands very well in interviews."""),
               ],
               desk="Change approval gates and a 'definition of done' for resolving a ticket are the same concept. You've worked inside them for years; now you help design them.",
               takeaway="Gates are fast, deterministic, actionable conditions at each stage; the DoD makes 'done' measurable; QA makes risk visible, the whole team owns quality.",
               ex=[
                   mcq("What makes a quality gate effective?", [
                       "It runs as many tests as possible", "It is fast, deterministic and actionable", "It requires manager approval for everything", "It never fails"], 1),
                   mcq("Who owns quality on a modern Agile team?", [
                       "QA alone", "The whole team; QA makes quality visible and actionable", "The Product Owner alone", "Nobody"], 1),
                   mcq("Which belongs in a Definition of Done?", [
                       "'Looks fine'", "'AC verified, CI green, no open Critical/Major defects, tests linked'", "'Merged before review'", "'Will test later'"], 1),
               ]),

        lesson("ci-05", "Metrics that inform rather than mislead", 11,
               "You'll be asked to report on quality. Knowing which numbers are meaningful — and which actively cause bad behaviour — is a senior-level skill you can demonstrate early.",
               [
                 ("Metrics worth keeping", """| Metric | Question it answers |
|---|---|
| **Escaped defect rate** (found after release) | How good is our test design? |
| **Defect arrival vs closure rate** | Is the backlog growing? |
| **Mean time to feedback** | How fast do developers learn about a problem? |
| **Flakiness rate** | Can we trust the pipeline? |
| **Requirements / risk coverage** | What haven't we tested? |
| **Reopen rate** | Are fixes actually good? |
| **Defect density by module** | Where should we focus (clustering principle)? |
| **Mean time to detect / resolve** | How fast do we respond to production issues? |

Always show a **trend** and the **denominator**, and pair numbers with a recommendation."""),
                 ("Goodhart's law and vanity metrics", """*'When a measure becomes a target, it ceases to be a good measure.'* Consequences:

- Rewarding **bugs logged** → trivial reports and adversarial QA/dev relationships.
- Rewarding **100% pass rate** → tests get deleted or marked skipped.
- Rewarding **test count** → hundreds of worthless cases.
- Rewarding **speed of closure** → defects closed as 'not a bug' without investigation.

Never attach individual performance targets to these numbers. Use them to find **process** problems."""),
                 ("A one-paragraph quality report", """*'Release 2026.04: 148 of 150 planned cases executed (2 blocked by the staging data outage, both low-risk). 0 open Critical, 1 open Major (DEF-512, tooltip on the admin export, workaround documented, PO accepted). High-risk requirement coverage 100%. One defect escaped from the previous release — a duplicate-submit case, now added to the regression pack and automated. Flakiness down from 4% to 0.5%. **Recommendation: go**, with DEF-512 deferred to 2026.05.'*

That paragraph demonstrates honesty, risk thinking, residual risk, continuous improvement and a decision — everything a hiring manager wants to hear."""),
               ],
               desk="Service desk reports already use SLA %, backlog growth, and reopen rates. Same discipline: trend + denominator + recommendation, never a naked percentage.",
               takeaway="Measure escapes, feedback time, flakiness, risk coverage and reopens as trends; never weaponise metrics; always end with a recommendation.",
               ex=[
                   mcq("Which metric best reflects test-design quality?", [
                       "Tests written", "Escaped defect rate", "Bugs logged per tester", "Lines of code"], 1),
                   mcq("Goodhart's law warns that:", [
                       "All metrics are useless", "When a measure becomes a target, it stops being a good measure", "More tests are always better", "Dashboards are mandatory"], 1),
                   mcq("A quality report should always end with:", [
                       "A raw percentage", "A go/no-go recommendation and residual risk", "A list of names", "The budget"], 1),
               ]),
    ],
    quiz="cicd-quiz",
)

# ---------------------------------------------------------------------------
# 16. Non-functional testing
# ---------------------------------------------------------------------------
NONFUNCTIONAL = course(
    "nonfunctional", "Beyond Functional Testing", "How well, not just whether",
    "Performance, accessibility, security awareness, usability, compatibility/mobile and localisation — the quality attributes that functional tests miss, at a first-role-appropriate depth.",
    "#ff3d81", "p5", "Weeks 21-22", "Broadening",
    [
        lesson("nf-01", "Performance testing basics", 12,
               "'Does it work?' is functional. 'Does it work for 500 users at once without falling over?' is performance. You don't need to be a performance engineer, but you need the vocabulary and a few practical checks.",
               [
                 ("The types", """| Type | Question | Typical shape |
|---|---|---|
| **Load** | Does it meet targets under expected peak load? | Ramp to N concurrent users, hold 30-60 min |
| **Stress** | Where does it break, and how does it fail? | Increase load until errors/latency spike |
| **Soak / endurance** | Does it degrade over hours (memory leaks, connection pools)? | Moderate load for 8-24 h |
| **Spike** | What happens with a sudden burst? | 0 → 10× users instantly |
| **Scalability** | Does adding resources increase capacity? | Repeat at several load levels |"""),
                 ("Metrics and targets", """- **Response time**: look at **percentiles**, not averages — p95/p99 is what real users feel. 'Average 200 ms' can hide 5% of requests at 8 s.
- **Throughput**: requests/second, transactions/second.
- **Error rate**: % of failed requests under load.
- **Concurrency**: simultaneous virtual users.
- **Resource utilisation**: CPU, memory, DB connections, thread pools.

A **performance requirement** must be measurable: *'checkout p95 ≤ 2 s at 500 concurrent users with <0.1% errors'*. 'The site should be fast' is untestable — flag it in refinement, exactly as you would any vague acceptance criterion.

Tools: **k6** (JS-based, developer-friendly), **JMeter** (classic, GUI), **Gatling**, **Locust** (Python), plus Lighthouse for front-end page performance."""),
                 ("A starter k6 script", """```js
import http from 'k6/http';
import { check, sleep } from 'k6';
export const options = { vus: 50, duration: '5m',
  thresholds: { http_req_duration: ['p(95)<2000'], http_req_failed: ['rate<0.01'] } };
export default function () {
  const res = http.get('https://staging.example.com/api/products');
  check(res, { 'status is 200': (r) => r.status === 200 });
  sleep(1);
}
```

`thresholds` turn a load run into a **pass/fail gate**. Never load-test production without explicit approval and a maintenance window — you can cause a real outage. Use a staging environment sized like production, with realistic (masked) data."""),
               ],
               desk="The 'system is slow at month-end / Monday 9am' incident is a load/spike pattern. You've seen the symptom; now you can name it and design a test that catches it before release.",
               takeaway="Load/stress/soak/spike; measure p95/p99, throughput, errors; demand measurable targets; k6 thresholds make a gate; never load-test production.",
               ex=[
                   mcq("Why is p95 response time more useful than the average?", [
                       "It's easier to compute", "Averages hide the slow tail that real users experience", "It's always smaller", "It's required by k6"], 1),
                   mcq("A soak test primarily finds:", [
                       "Typos", "Memory leaks / degradation over many hours", "CSS bugs", "Missing buttons"], 1),
                   mcq("'The site should be fast' is a bad requirement because it is:", [
                       "Too short", "Not measurable — no load, metric or target", "Written by a developer", "About the UI"], 1),
               ]),

        lesson("nf-02", "Accessibility testing (WCAG and axe)", 12,
               "Accessibility is both a legal requirement in many sectors and a quality attribute functional tests miss entirely. Basic a11y testing is a very employable skill and a genuine differentiator for a first QA role.",
               [
                 ("WCAG in one paragraph", """**WCAG** (Web Content Accessibility Guidelines) is organised around four principles — **POUR**: content must be **Perceivable** (text alternatives, contrast, captions), **Operable** (keyboard accessible, enough time, no seizure-inducing motion), **Understandable** (clear labels, predictable behaviour, error messages), and **Robust** (valid markup, works with assistive tech). Conformance levels: **A** (minimum), **AA** (the usual legal target), **AAA** (specialist).

~15% of people have a disability; accessibility also helps everyone on a keyboard, a phone in sunlight, or a broken mouse."""),
                 ("Practical checks a manual tester can run", """1. **Keyboard only**: unplug the mouse. `Tab` through the whole flow — can you reach every control, is focus visible, is the order logical, does `Enter`/`Space` activate buttons, can you escape a modal with `Esc`?
2. **Zoom** to 200% / 400% — does content reflow without horizontal scrolling or clipping?
3. **Colour contrast**: use a contrast checker; text should be ≥4.5:1 (≥3:1 for large text). Never convey meaning by colour alone ('red = error' needs text/icon too).
4. **Images / icons**: meaningful `alt` text; decorative images `alt=""`.
5. **Forms**: every input has an associated `<label>`; errors name the field and describe the fix (`aria-describedby`, `aria-invalid`).
6. **Headings and landmarks**: one `h1`, logical heading order, `nav`/`main`/`footer`.
7. **Screen reader** spot check: VoiceOver (Mac), NVDA (Windows, free), TalkBack (Android).
8. **Automated scan**: **axe DevTools** / Lighthouse / `pa11y` / `axe-core` in Playwright (`@axe-core/playwright`). Automated tools catch roughly 30-40% of issues — the rest need a human."""),
                 ("An automated a11y assertion", """```js
import AxeBuilder from '@axe-core/playwright';
test('login page has no automatically detectable a11y violations', async ({ page }) => {
  await page.goto('/login');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();
  expect(results.violations).toEqual([]);
});
```

Log findings like any defect: WCAG criterion (e.g. *1.4.3 Contrast (Minimum)*), steps, screenshot, impact (serious/critical), and a suggested fix. Accessibility work pairs naturally with the **user-facing locators** you learned in Playwright — both reward semantic HTML."""),
               ],
               desk="You've supported users who can't use a mouse or read small text. Formalising that empathy into WCAG checks is one of the most valuable and human skills you can bring into QA.",
               takeaway="POUR + AA target; keyboard/zoom/contrast/labels/headings/screen reader; axe for the automated 30-40%, humans for the rest.",
               ex=[
                   mcq("Which is NOT one of the four WCAG principles (POUR)?", [
                       "Perceivable", "Operable", "Performant", "Robust"], 2),
                   mcq("Automated a11y tools typically catch:", [
                       "All issues", "Roughly 30-40%; human checks are still required", "Nothing", "Only colour issues"], 1),
                   mcq("The conformance level most commonly required by law/policy is:", [
                       "A", "AA", "AAA", "None"], 1),
               ]),

        lesson("nf-03", "Security basics for testers", 12,
               "You are not being asked to become a penetration tester. But a QA Analyst who can spot common web vulnerabilities and knows which negative tests to run is dramatically more valuable — and safer.",
               [
                 ("The OWASP Top 10 (awareness level)", """The **OWASP Top 10** is the standard list of the most critical web application risks. Know these well enough to test the basics:

| Risk | A tester's quick check |
|---|---|
| **Broken access control** | Change an ID in a URL/API call — can I see another user's data? (**IDOR**) |
| **Cryptographic failures** | Is data in transit HTTPS? are passwords/tokens ever exposed in logs/URLs? |
| **Injection** | Send `' OR 1=1 --`, `<script>alert(1)</script>` — is it escaped/rejected, never a 500? |
| **Insecure design** | Are business rules enforced server-side (price, qty, role)? |
| **Security misconfiguration** | Default credentials, verbose stack traces, open debug endpoints, missing security headers |
| **Vulnerable components** | Are dependencies outdated? |
| **Auth failures** | Session fixation, weak password policy, token not invalidated on logout, no rate limiting |
| **Data integrity failures** | Unsigned updates, deserialisation of untrusted data |
| **Logging/monitoring failures** | Are security events logged (without secrets)? |
| **SSRF** | Does a URL input let the server fetch internal resources? |"""),
                 ("High-value, safe tests for a manual QA Analyst", """1. **Auth negative matrix** (from the API course): 401/403/expired/IDOR.
2. **Input handling**: quotes, `<`, `>`, `&`, unicode, very long strings, path traversal `../../etc/passwd` in file parameters.
3. **Client vs server validation**: submit an invalid price/qty directly with Postman — is the server fooled?
4. **Error hygiene**: no stack traces, SQL, absolute paths or secrets in responses.
5. **Session**: logout invalidates the token; cookies have `HttpOnly`/`Secure`/`SameSite`; password change kills old sessions.
6. **Rate limiting**: hammer a login/reset endpoint → 429, not unlimited attempts.
7. **Headers**: HTTPS, HSTS, CSP, X-Content-Type-Options.

Only ever test systems you are **authorised** to test. Use staging or deliberately vulnerable practice apps (OWASP Juice Shop, DVWA, PortSwigger Web Security Academy) — never a live third-party site."""),
                 ("Reporting security findings", """Log them as defects with **high severity**, clear repro, evidence, and impact ('any logged-in user can read another user's order by changing the ID'), and mark them appropriately (some teams use a security label / private issue type). Don't shout 'we've been hacked' — state the observed behaviour and the potential impact factually. Escalate to the security team per your org's process."""),
               ],
               desk="'Can this user see another user's ticket?' is an access-control question you've asked before. Naming it IDOR and testing it deliberately is the whole leap.",
               takeaway="Know the OWASP Top 10 at awareness level; run auth/input/error/session/rate-limit checks; only test authorised systems; report impact factually.",
               ex=[
                   mcq("Changing an ID in a URL and reading another user's record is:", [
                       "An injection flaw", "IDOR / broken access control", "A caching issue", "A CSS bug"], 1),
                   mcq("Which is a legitimate manual security check for a QA Analyst?", [
                       "Port-scanning a third-party site", "Submitting invalid data directly via Postman to verify server-side validation", "Guessing a colleague's password", "Disabling the firewall"], 1),
                   mcq("Where should you practise security testing?", [
                       "A live bank site", "OWASP Juice Shop / DVWA / PortSwigger Academy on your own machine", "Production", "A customer's account"], 1),
               ]),

        lesson("nf-04", "Usability, compatibility and mobile", 11,
               "A feature can be functionally correct and still fail users. This lesson covers the human-facing checks and the device/browser matrix, and how to keep them tractable with risk-based selection.",
               [
                 ("Usability checks", """- **Clarity**: does the user know what to do next? are labels, button text and error messages plain and actionable ('Coupon SAVE10 is not valid' vs 'Error 42')?
- **Feedback**: loading indicators, success confirmation, disabled states, progress on long operations.
- **Recovery**: can the user undo, go back, correct an error without losing everything?
- **Consistency**: same words, colours, and patterns across the app.
- **Cognitive load**: minimal steps, sensible defaults, no unnecessary fields.
- **Error prevention**: confirmations for destructive actions, sensible input constraints.

Usability findings are often **'works as designed'** — that's fine. Log them as *usability improvements* with user impact, not as functional defects. This is exactly the 'absence-of-errors fallacy' from the principles: bug-free can still be bad."""),
                 ("Compatibility matrix (kept sane)", """Dimensions: browser (Chrome, Edge, Firefox, Safari), OS (Windows, macOS, iOS, Android), viewport/device, and version. Full coverage exploded in the pairwise lesson — use **pairwise/all-pairs** to build a small matrix, then **add explicit high-risk rows** (your analytics' top 3 real user configurations). Prioritise by **actual usage data**, not by what the team happens to have installed.

Check: layout/overflow, date & number formats, fonts, touch targets, file inputs, print, zoom, and browser-specific JS/CSS support. Note which combinations are explicitly **out of scope** in the test plan."""),
                 ("Mobile-specific risks", """Small viewports and touch (no hover), on-screen keyboard covering inputs, orientation change, interrupted network (tube/tunnel), low battery/low memory, app backgrounding and resume, push notifications, permission prompts (camera/location), OS-level font scaling, and flaky connectivity. **Real devices** beat emulators for these; use BrowserStack / Sauce Labs or a small physical device library when available. Also test **responsive breakpoints** and 200% zoom — that overlaps with accessibility."""),
               ],
               desk="Desktop thin-client vs laptop vs phone reproduces are compatibility tickets you've triaged. A small, evidence-based device matrix turns that reactive work into planned coverage.",
               takeaway="Usability = clarity, feedback, recovery, consistency; build a pairwise + usage-driven compatibility matrix; test mobile interruptions and permissions on real devices.",
               ex=[
                   mcq("How do you keep a browser/OS/device matrix tractable?", [
                       "Test every combination", "Pairwise coverage plus explicit high-risk real-user configurations", "Test only Chrome", "Skip mobile"], 1),
                   mcq("A usability finding that is 'working as designed' should be:", [
                       "Deleted silently", "Logged as a usability improvement with user impact", "Marked Critical", "Ignored forever"], 1),
                   mcq("Which is a mobile-specific risk?", [
                       "DNS lookup", "App backgrounding/resume, interrupted network, on-screen keyboard", "SQL joins", "Server-side caching"], 1),
               ]),

        lesson("nf-05", "Localisation, internationalisation and data privacy", 11,
               "Names, dates, currencies and right-to-left layouts break software in ways English-language testing never reveals. Add these checks and you'll find defects most testers miss.",
               [
                 ("i18n and l10n", """**Internationalisation (i18n)** = designing the app so it *can* be localised; **localisation (l10n)** = adapting it for a specific locale. Test with more than translated strings:

- **Date/time**: `03/04/2026` means 4 March in the UK and 3 April in the US; timezones, DST, 12/24-hour clocks, week start (Sun vs Mon).
- **Numbers & currency**: `1,234.56` vs `1.234,56`; currency symbol position; rounding rules.
- **Text expansion**: German strings can be 30-40% longer → clipped buttons, overflowing tables.
- **Unicode**: accented characters, non-Latin scripts, emoji, combining characters, and special names (`O'Brien`, `李`, `Ñ`, hyphenated, very long).
- **Right-to-left** (Arabic/Hebrew): mirrored layout, mixed-direction numbers, punctuation.
- **Sorting/collation**: does 'Å' sort correctly? (locale-aware comparisons)
- **Input methods**: IME for CJK, address/postcode formats, phone number formats.

Pseudolocalisation (replacing text with accented, lengthened pseudo-text) catches layout/hard-coded-string defects before real translations arrive."""),
                 ("Privacy and data-protection checks for QA", """- **Masking/anonymisation**: test data must not contain real customer PII. Check exports, logs, HARs, screenshots and error messages for leaked data.
- **Consent**: cookie banners, marketing opt-ins, and 'do not track' behaviour.
- **Data minimisation / retention**: is deleted data actually removed (including backups/search indexes)? Test the **right to erasure** flow if relevant.
- **Access & audit**: can users see only their own data? are accesses logged?
- **Secure transport & storage**: HTTPS everywhere, no secrets in URLs (they leak into logs/history), no tokens in localStorage without reason.
- **Third parties**: analytics/payment/CDN requests — do they receive more data than necessary?

Regulations (GDPR, HIPAA, PCI-DSS) vary by sector; you don't need to be a lawyer, but you do need to know your product's obligations and design tests for them. In regulated industries, this evidence is auditable."""),
               ],
               desk="Special characters in names breaking an import or a report is a support classic. Now it's a planned test case, alongside privacy checks on the logs and exports you already handle.",
               takeaway="Test dates, numbers, expansion, unicode, RTL and collation; pseudolocalise early; verify masking, consent, erasure and no PII in logs/exports/screenshots.",
               ex=[
                   mcq("'03/04/2026' is ambiguous because of:", [
                       "A browser bug", "Locale-specific date formats", "A database index", "Caching"], 1),
                   mcq("Text expansion matters because translated strings can be:", [
                       "Shorter always", "30-40% longer, clipping buttons and tables", "Automatically resized", "Invisible"], 1),
                   mcq("Which is a QA privacy check?", [
                       "Button colour", "No real PII in test data, logs, HARs or screenshots", "Page load speed", "Font choice"], 1),
               ]),

        lesson("nf-06", "Putting non-functional checks into the plan", 10,
               "Non-functional testing fails when it's an afterthought ('we'll do a security scan before go-live'). This lesson shows how to bake it into the test plan, the DoD and the pipeline from the start.",
               [
                 ("Make them requirements", """The same rule as everything else: **if it isn't measurable, it isn't testable**. Push for acceptance criteria like:

- *'Checkout p95 ≤ 2 s at 500 concurrent users, error rate < 0.1%.'*
- *'All interactive elements reachable and operable by keyboard; axe reports 0 WCAG 2.1 AA violations on the login and checkout pages.'*
- *'All form inputs accept Unicode names up to 100 characters without a 500.'*
- *'No PII in application logs or exported CSVs.'*

Once written as AC, they become test cases, get traced in the RTM, and can be gated in CI."""),
                 ("Where each check lives", """| Check | Where | Frequency |
|---|---|---|
| axe / a11y scan | PR pipeline + manual keyboard pass per feature | Every PR / per story |
| Lighthouse / bundle budget | CI | Every build |
| k6 smoke load (short) | Nightly | Nightly |
| Full load / soak | Pre-release, scheduled | Per release |
| Security scan (SAST/dependency) | CI | Every push |
| Auth/input negative matrix | API regression suite | Every build |
| Compatibility matrix | Pre-release + on UI overhaul | Per release / on change |
| Exploratory usability charter | Each sprint | Per sprint |

Note that many are **cheap and automatable** (axe, SAST, dependency checks, Lighthouse) and belong in the PR gate; the expensive ones (full soak, real-device matrix) are risk-scheduled."""),
                 ("Residual risk, again", """You will never cover every device, every locale, or every load profile. List what you did **not** test in the summary with a reason ('real-device iOS testing deferred to next release; emulator coverage only'). That honest statement is a sign of maturity, not weakness — it's the same residual-risk discipline from the test plan and CI gates."""),
               ],
               desk="A go-live checklist with security, backup and performance sign-offs is a non-functional gate. Formalise each line as a measurable AC and automate the cheap ones.",
               takeaway="Write non-functional requirements as measurable AC; automate cheap scans in CI; schedule expensive tests by risk; record what you didn't test.",
               ex=[
                   mcq("What makes a non-functional requirement testable?", [
                       "A long description", "A measurable target (metric + load + threshold)", "A screenshot", "A manager's approval"], 1),
                   mcq("Which non-functional check belongs in a fast PR gate?", [
                       "A 12-hour soak test", "An axe accessibility scan / dependency scan", "A full device matrix", "A 500-user stress test"], 1),
                   mcq("Listing untested devices/locales in the summary is:", [
                       "A weakness", "Honest residual-risk reporting", "Forbidden", "A defect"], 1),
               ]),
    ],
    quiz="nonfunctional-quiz",
)

COURSES_03 = [API, POSTMAN, AUTOMATION, PLAYWRIGHT, CICD, NONFUNCTIONAL]

QUIZZES_03 = [
    quiz("api-quiz", "api", "API fundamentals checkpoint", [
        ("Which URL is most RESTful for reading user 14?", ["/getUser?id=14", "/api/users/14", "/doUser", "/api?u=14"], 1, ""),
        ("401 vs 403:", ["401 forbidden / 403 unauthenticated", "401 unauthenticated / 403 forbidden", "Both client errors only", "Both server errors"], 1, ""),
        ("'Stateless' means:", ["No database", "Each request carries all needed context", "No caching", "No auth"], 1, ""),
        ("Reading someone else's record by changing an ID is:", ["A 404", "IDOR / broken access control", "Idempotency", "Caching"], 1, ""),
        ("A missing required field should return:", ["500 with a stack trace", "400/422 with a clear error and no partial write", "200 empty", "302"], 1, ""),
        ("Repeating a POST usually:", ["Is idempotent", "Can create a duplicate — test it explicitly", "Returns 405", "Is cached"], 1, ""),
        ("201 responses should usually include:", ["A Set-Cookie", "A Location header pointing to the new resource", "A stack trace", "A Retry-After"], 1, ""),
    ]),
    quiz("postman-quiz", "postman", "Postman checkpoint", [
        ("Variable syntax in Postman:", ["${baseUrl}", "{{baseUrl}}", "#baseUrl", "(baseUrl)"], 1, ""),
        ("Which tab runs BEFORE the request?", ["Tests", "Pre-request Script", "Cookies", "Body"], 1, ""),
        ("`pm.expect(body.total).to.eql(108.00)` is:", ["An environment variable", "A named assertion on business value", "A status check", "A schema"], 1, ""),
        ("Asserting only status 200 is weak because:", ["It's slow", "Wrong data still passes", "Postman can't", "It needs auth"], 1, ""),
        ("Newman is:", ["A browser", "Postman's CLI collection runner", "A mock server", "A database"], 1, ""),
        ("Why commit a collection with secrets removed?", ["It's smaller", "Secrets must never be in a public repo; use CI secrets", "It runs faster", "Postman requires it"], 1, ""),
        ("A mock server proves:", ["Real integration works", "The client handles documented responses", "The DB is correct", "Nothing"], 1, ""),
    ]),
    quiz("automation-quiz", "automation", "Automation strategy checkpoint", [
        ("Which layer should have the MOST tests?", ["E2E/UI", "Integration/API", "Unit", "Manual"], 2, ""),
        ("The 'ice-cream cone' anti-pattern is:", ["Too many unit tests", "Lots of UI tests, few unit/API", "No CI", "Only manual"], 1, ""),
        ("The WORST automation candidate is:", ["Login smoke", "A brand-new feature needing human judgement", "A boundary data set", "Checkout regression"], 1, ""),
        ("A flaky test should be:", ["Retried until green", "Quarantined, investigated, fixed or deleted", "Ignored", "Run only at night"], 1, ""),
        ("Playwright's big flakiness reducer is:", ["Video", "Auto-waiting", "Dark mode", "Multiple languages"], 1, ""),
        ("Arrange → Act → Assert → Cleanup maps to:", ["Nothing", "Preconditions → steps → expected → postconditions", "Phases of SDLC", "Git commands"], 1, ""),
    ]),
    quiz("playwright-quiz", "playwright", "Playwright checkpoint", [
        ("Download browser binaries with:", ["npm test", "npx playwright install", "npm init", "git push"], 1, ""),
        ("Most resilient locator:", ["Absolute XPath", "getByRole/getByLabel", "nth-child", "Coordinates"], 1, ""),
        ("Web-first assertion:", ["expect(await locator.textContent())", "await expect(locator).toHaveText('x')", "console.log", "assert(true)"], 1, ""),
        ("Instead of waitForTimeout you should:", ["Use longer sleeps", "Wait for the actual condition/signal", "Disable JS", "Add retries"], 1, ""),
        ("Page Object Model's benefit:", ["Faster browsers", "One place to fix a UI change", "No assertions", "No CI"], 1, ""),
        ("storageState is used to:", ["Store screenshots", "Reuse an authenticated session across tests", "Save videos", "Set the base URL"], 1, ""),
        ("Replay a recorded trace with:", ["show-report", "npx playwright show-trace trace.zip", "npm ci", "--headed"], 1, ""),
    ]),
    quiz("cicd-quiz", "cicd", "CI/CD checkpoint", [
        ("CI gives primarily:", ["Longer releases", "Fast automated feedback on each change", "Fewer devs", "No tests"], 1, ""),
        ("Why `npm ci` in CI?", ["Faster only", "Reproducible lockfile-exact installs", "Installs browsers", "Skips tests"], 1, ""),
        ("`if: always()` on artefact upload:", ["Slows builds", "Keeps reports downloadable even when tests fail", "Deletes runs", "Is required"], 1, ""),
        ("A required status check means:", ["Tests run once", "PRs can't merge while the job is red", "Comments required", "Branch deleted"], 1, ""),
        ("Quality is owned by:", ["QA alone", "The whole team; QA makes risk visible", "PO alone", "Nobody"], 1, ""),
        ("Best metric for test-design quality:", ["Tests written", "Escaped defect rate", "Bugs per tester", "Lines of code"], 1, ""),
    ]),
    quiz("nonfunctional-quiz", "nonfunctional", "Non-functional checkpoint", [
        ("p95 beats average because:", ["Easier math", "Averages hide the slow tail users feel", "It's smaller", "k6 requires it"], 1, ""),
        ("A soak test finds:", ["Typos", "Memory leaks / degradation over hours", "CSS bugs", "Missing alt text"], 1, ""),
        ("WCAG level commonly required is:", ["A", "AA", "AAA", "None"], 1, ""),
        ("Automated a11y tools catch roughly:", ["100%", "30-40%", "Nothing", "Only colours"], 1, ""),
        ("IDOR is:", ["An injection flaw", "Broken access control via changed IDs", "A cache issue", "A CSS bug"], 1, ""),
        ("A performance requirement must be:", ["Short", "Measurable (metric + load + threshold)", "Written by devs", "About the UI"], 1, ""),
        ("Listing untested locales/devices in a summary is:", ["A weakness", "Honest residual risk", "Forbidden", "A defect"], 1, ""),
    ]),
]
