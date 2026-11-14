/* QAReady service worker: cache the entire app shell up front so every
 * lesson, exercise, quiz and the offline SQL engine work with no connection.
 * Bump VERSION whenever a shipped file changes. */
const VERSION = "qaready-v4";
const SHELL = [
  "./",
  "index.html",
  "styles.css",
  "manifest.webmanifest",
  "vendor/marked.js",
  "data/content.js",
  "js/sql-engine.js",
  "js/app.js",
  "fonts/atkinson-hyperlegible-latin-400-normal.woff2",
  "fonts/atkinson-hyperlegible-latin-700-normal.woff2",
  "fonts/opendyslexic-latin-400-normal.woff2",
  "fonts/opendyslexic-latin-700-normal.woff2",
  "fonts/lexend-latin-400-normal.woff2",
  "fonts/lexend-latin-700-normal.woff2",
  "fonts/literata-latin-400-normal.woff2",
  "fonts/literata-latin-700-normal.woff2",
  "fonts/lora-latin-400-normal.woff2",
  "fonts/lora-latin-700-normal.woff2",
  "fonts/dancing-script-latin-400-normal.woff2",
  "fonts/dancing-script-latin-700-normal.woff2",
  "icons/icon-192.png",
  "icons/icon-512.png",
  "icons/apple-touch-icon.png",
  "icons/favicon.png",
  "icons/favicon.svg",
];

self.addEventListener("install", (event) => {
  event.waitUntil(
    caches.open(VERSION)
      .then((cache) => cache.addAll(SHELL))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.filter((k) => k !== VERSION).map((k) => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener("fetch", (event) => {
  const req = event.request;
  const url = new URL(req.url);
  if (url.origin !== self.location.origin || req.method !== "GET") return;
  // Media elements use Range requests for seeking. Caching a 206 response
  // would break playback, so audiobooks get their own handler.
  if (url.pathname.startsWith("/audio/")) {
    event.respondWith(audioResponse(event));
    return;
  }
  event.respondWith(cacheFirst(req));
});

async function audioResponse(event) {
  const req = event.request;
  const cache = await caches.open(VERSION);
  const key = new Request(req.url, { method: "GET" });   // no Range header
  const full = await cache.match(key);

  if (!full) {
    // First play: stream this request straight through (fast, correct 206),
    // and quietly fetch the whole file in the background for offline use later.
    event.waitUntil((async () => {
      try {
        const r = await fetch(key);
        if (r.ok && r.status === 200) await cache.put(key, r.clone());
      } catch (_) { /* offline; try again next time */ }
    })());
    try {
      return await fetch(req);
    } catch (_) {
      return new Response("Audio unavailable offline", { status: 503 });
    }
  }

  // Cached: serve byte ranges from the complete file so seeking still works.
  const buf = await full.arrayBuffer();
  const type = full.headers.get("content-type") || "audio/mpeg";
  const base = { "Content-Type": type, "Accept-Ranges": "bytes" };
  const range = req.headers.get("range");
  const m = range && /^bytes=(\d+)-(\d*)$/.exec(range.trim());
  if (!m) {
    return new Response(buf, {
      status: 200,
      headers: { ...base, "Content-Length": String(buf.byteLength) },
    });
  }
  const start = Number(m[1]);
  const end = m[2] ? Math.min(Number(m[2]), buf.byteLength - 1) : buf.byteLength - 1;
  if (start >= buf.byteLength || end < start) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${buf.byteLength}` } });
  }
  const slice = buf.slice(start, end + 1);
  return new Response(slice, {
    status: 206,
    headers: {
      ...base,
      "Content-Length": String(slice.byteLength),
      "Content-Range": `bytes ${start}-${end}/${buf.byteLength}`,
    },
  });
}

async function cacheFirst(req) {
  const cache = await caches.open(VERSION);
  const cached = await cache.match(req);
  if (cached) return cached;
  try {
    const res = await fetch(req);
    if (res.ok && res.status === 200) cache.put(req, res.clone());
    return res;
  } catch {
    // Navigation while offline: serve the cached app shell.
    if (req.mode === "navigate") {
      const shell = await cache.match("index.html");
      if (shell) return shell;
    }
    return new Response("Offline and not cached", { status: 503 });
  }
}

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "CLEAR_CACHE") {
    event.waitUntil(
      caches.keys()
        .then((keys) => Promise.all(keys.map((k) => caches.delete(k))))
        .then(() => caches.open(VERSION).then((c) => c.addAll(SHELL)))
        .then(() => self.skipWaiting())
    );
  }
});
