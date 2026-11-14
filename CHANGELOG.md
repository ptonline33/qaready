# Changelog

## 2026-11-14 — Audiobooks (Andrew narration)

- Added an **Audiobooks** view (`#/audio`) with two full-length MP3s narrated by Andrew (`en-US-AndrewNeural`): *The QAReady Plan* (15 chapters, the 24-week schedule and career guide) and *ISTQB Foundation Level* (32 chapters, a complete CTFL v4.0 audio course). Both are generated from this curriculum's material.
- The same two books ship in the **Readalong** library as EPUB + per-chapter MP3s with read-along timings, built by `readalong/tools/make_qa_audiobooks.py` and `readalong/build.py`.
- `stage_public.py` now stages `audio/`. `sw.js` gained a Range-aware audio branch: the first play streams normally with a background full-file fetch, and later plays serve byte ranges from the cached copy so seeking works offline. Bumped `VERSION` to `qaready-v4`.
- New sidebar entry under LAUNCH; `preload="none"` so nothing downloads until a book is played.
