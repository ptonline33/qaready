/* QAReady service worker: cache the entire app shell up front so every
 * lesson, exercise, quiz and the offline SQL engine work with no connection.
 * Bump VERSION whenever a shipped file changes. */
const VERSION = "qaready-v3";
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
  event.respondWith(cacheFirst(req));
});

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
