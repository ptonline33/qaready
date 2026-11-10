#!/usr/bin/env python3
"""Generate QAReady PWA icons with the Python standard library only.

No Pillow / ImageMagick needed: a tiny PNG writer plus some pixel maths draws
a rounded indigo→violet tile with a white 'verified' check mark.
"""
import math
import struct
import zlib
from pathlib import Path

OUT = Path(__file__).resolve().parent / "icons"
OUT.mkdir(parents=True, exist_ok=True)

TOP = (0x4F, 0x46, 0xE5)      # indigo
BOTTOM = (0x8B, 0x5C, 0xF6)   # violet
WHITE = (0xFF, 0xFF, 0xFF)


def lerp(a, b, t):
    return a + (b - a) * t


def bg(x, y):
    t = max(0.0, min(1.0, y))
    # slight diagonal tilt so it doesn't look flat
    t = max(0.0, min(1.0, t * 0.85 + x * 0.15))
    return tuple(int(lerp(TOP[i], BOTTOM[i], t)) for i in range(3))


def rounded_rect(x, y, radius):
    """1.0 inside a rounded unit square, 0 outside (with a 1px-ish soft edge)."""
    # clamp coordinates to the inner square to measure corner distance
    cx = min(max(x, radius), 1 - radius)
    cy = min(max(y, radius), 1 - radius)
    dx, dy = x - cx, y - cy
    d = math.hypot(dx, dy)
    edge = 0.012
    if d <= radius - edge:
        return 1.0
    if d >= radius:
        return 0.0
    return (radius - d) / edge


def seg_dist(px, py, ax, ay, bx, by):
    vx, vy = bx - ax, by - ay
    wx, wy = px - ax, py - ay
    length2 = vx * vx + vy * vy
    t = 0.0 if length2 == 0 else max(0.0, min(1.0, (wx * vx + wy * vy) / length2))
    return math.hypot(px - (ax + t * vx), py - (ay + t * vy))


def glyph(x, y, scale=1.0):
    """White check mark + a small verified dot. Coordinates in 0..1."""
    # scale the glyph around the centre so maskable variants keep a safe zone
    x = 0.5 + (x - 0.5) / scale
    y = 0.5 + (y - 0.5) / scale

    w = 0.058
    best = min(
        seg_dist(x, y, 0.255, 0.515, 0.435, 0.700),
        seg_dist(x, y, 0.435, 0.700, 0.765, 0.315),
    )
    a = 1.0 if best <= w else (0.0 if best >= w + 0.012 else (w + 0.012 - best) / 0.012)

    # small dot at the top-right (a 'verified' accent)
    d = math.hypot(x - 0.775, y - 0.235)
    dot = 1.0 if d <= 0.035 else (0.0 if d >= 0.047 else (0.047 - d) / 0.012)
    return max(a, dot)


def render(size, maskable=False, ss=3):
    step = 1.0 / (size * ss)
    rows = []
    for py in range(size):
        row = bytearray()
        row.append(0)  # PNG filter type 0 (None)
        for px in range(size):
            r = g = b = coverage = 0
            for sy in range(ss):
                for sx in range(ss):
                    x = (px * ss + sx + 0.5) * step
                    y = (py * ss + sy + 0.5) * step
                    base = bg(x, y)
                    # maskable icons must be full-bleed; normal ones get a rounded tile
                    shape = 1.0 if maskable else rounded_rect(x, y, 0.22)
                    mark = glyph(x, y, 0.80 if maskable else 1.0)
                    r += base[0] * (1 - mark) + WHITE[0] * mark
                    g += base[1] * (1 - mark) + WHITE[1] * mark
                    b += base[2] * (1 - mark) + WHITE[2] * mark
                    coverage += shape
            n = ss * ss
            # RGB stays un-premultiplied; alpha carries the rounded-corner coverage
            row += bytes((int(r / n), int(g / n), int(b / n), int(255 * coverage / n)))
        rows.append(bytes(row))
    raw = b"".join(rows)

    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(raw, 9))
    png += chunk(b"IEND", b"")
    return png


def main():
    for size, name, maskable in [
        (192, "icon-192.png", False),
        (512, "icon-512.png", True),
        (180, "apple-touch-icon.png", False),
        (64, "favicon.png", False),
    ]:
        (OUT / name).write_bytes(render(size, maskable, ss=2 if size == 512 else 3))
        print("wrote", name)

    svg = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4f46e5"/><stop offset="1" stop-color="#8b5cf6"/>
  </linearGradient></defs>
  <rect width="64" height="64" rx="14" fill="url(#g)"/>
  <path d="M16 33 L27 45 L49 20" fill="none" stroke="#fff" stroke-width="7"
        stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="50" cy="15" r="3" fill="#fff"/>
</svg>
"""
    (OUT / "favicon.svg").write_text(svg, encoding="utf-8")
    print("wrote favicon.svg")


if __name__ == "__main__":
    main()
