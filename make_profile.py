#!/usr/bin/env python3
"""Kemmochi's pixel-night GitHub profile: generates the animated SVGs in assets/.

Edit the CONFIG block, then run:  python3 make_profile.py
No dependencies. Animations are plain CSS/SMIL inside each SVG, so they play
on GitHub (which strips JavaScript and blocks web fonts).
"""
import os
import random

# ----------------------------- CONFIG ---------------------------------
NAME = "KEMMOCHI"                 # banner title, A-Z and spaces only
HANDLE = "fnrkp089"
CHIPS = ["TS", "RUST", "C#", "UNREAL"]
INFO = [                          # neofetch lines in the terminal
    ("role", "Full-Stack / AI Security Engineer"),
    ("lang", "TypeScript, Rust, C#"),
    ("engine", "Unreal Engine"),
    ("api", "tRPC, gRPC, MCP"),
    ("test", "Vitest, Playwright"),
    ("infra", "AWS, Vercel, Supabase"),
    ("based", "Seoul"),
]
SKILLS = [                        # (label, bar length in percent)
    ("TypeScript", 85),
    ("Rust", 70),
    ("C#", 65),
    ("Unreal Engine", 55),
    ("AI Security", 60),
]
ACCENT = "#b79cff"
BANNER_H = 200
# ----------------------------------------------------------------------

W = 836
INK = "#e9e4ff"
WHITE = "#f4f1ff"
MUTED = "#9a93c4"
LINE = "#3a2f6b"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

STYLE = """<style>
.f{animation:fl 3.2s ease-in-out infinite}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.b{opacity:0;animation:bl 4.2s steps(1,end) infinite}
@keyframes bl{0%,92%{opacity:0}93%,97%{opacity:1}100%{opacity:0}}
.tw{animation:tw 3s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.25}}
.cur{animation:cu 1.1s steps(1,end) infinite}
@keyframes cu{0%,49%{opacity:1}50%,100%{opacity:0}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}" shape-rendering="crispEdges">{STYLE}{body}</svg>\n')


def rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{extra}/>'


def text(x, y, s, fill=INK, size=13, weight=400, anchor="start", length=None):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    fit = f' textLength="{length}" lengthAdjust="spacingAndGlyphs"' if length else ""
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{MONO}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}"{fit}>{s}</text>')


def grid_rects(rows, colors):
    """Turn a character grid into merged 1-unit-high rects."""
    out = []
    for y, row in enumerate(rows):
        x = 0
        while x < len(row):
            c = row[x]
            if c == "." or c == " ":
                x += 1
                continue
            x0 = x
            while x < len(row) and row[x] == c:
                x += 1
            out.append(rect(x0, y, x - x0, 1, colors[c]))
    return "".join(out)


GHOST = """
....WWWW....
..WWWWWWWW..
.WWWWWWWWWW.
.WWWWWWWWWW.
WWWEEWWEEWWW
WWWEEWWEEWWW
WWWEEWWEEWWW
WBBWWWWWWBBW
WWWWWWWWWWWW
WWWWWWWWWWWS
WWWWWWWWWWSS
WWWWWWWWWSSS
WWW.WWWW.WSS
.W...WW...S.
""".strip().split("\n")
GHOST_COLORS = {"W": WHITE, "S": "#cfc6f5", "E": "#17123a", "B": "#ff9ecb"}


def ghost(x, y, px):
    lids = ('<g class="b">' + rect(3, 4, 2, 2, WHITE) + rect(7, 4, 2, 2, WHITE) + '</g>')
    return (f'<g class="f"><g transform="translate({x} {y}) scale({px})">'
            + grid_rects(GHOST, GHOST_COLORS) + lids + '</g></g>')


MOON = """
..MMMM..
.MMMMMM.
MMMMDMMM
MMMMMMMM
MDMMMMMM
MMMMMDMM
.MMMMMM.
..MMMM..
""".strip().split("\n")

FONT = {
    "A": ".###. #...# #...# ##### #...# #...# #...#",
    "B": "####. #...# #...# ####. #...# #...# ####.",
    "C": ".###. #...# #.... #.... #.... #...# .###.",
    "D": "####. #...# #...# #...# #...# #...# ####.",
    "E": "##### #.... #.... ####. #.... #.... #####",
    "F": "##### #.... #.... ####. #.... #.... #....",
    "G": ".###. #...# #.... #.### #...# #...# .###.",
    "H": "#...# #...# #...# ##### #...# #...# #...#",
    "I": "##### ..#.. ..#.. ..#.. ..#.. ..#.. #####",
    "J": "..### ...#. ...#. ...#. ...#. #..#. .##..",
    "K": "#...# #..#. #.#.. ##... #.#.. #..#. #...#",
    "L": "#.... #.... #.... #.... #.... #.... #####",
    "M": "#...# ##.## #.#.# #.#.# #...# #...# #...#",
    "N": "#...# ##..# #.#.# #..## #...# #...# #...#",
    "O": ".###. #...# #...# #...# #...# #...# .###.",
    "P": "####. #...# #...# ####. #.... #.... #....",
    "Q": ".###. #...# #...# #...# #.#.# #..#. .##.#",
    "R": "####. #...# #...# ####. #.#.. #..#. #...#",
    "S": ".#### #.... #.... .###. ....# ....# ####.",
    "T": "##### ..#.. ..#.. ..#.. ..#.. ..#.. ..#..",
    "U": "#...# #...# #...# #...# #...# #...# .###.",
    "V": "#...# #...# #...# #...# #...# .#.#. ..#..",
    "W": "#...# #...# #...# #.#.# #.#.# ##.## #...#",
    "X": "#...# #...# .#.#. ..#.. .#.#. #...# #...#",
    "Y": "#...# #...# .#.#. ..#.. ..#.. ..#.. ..#..",
    "Z": "##### ....# ...#. ..#.. .#... #.... #####",
    " ": "..... ..... ..... ..... ..... ..... .....",
}


def pixel_text(s, x, y, px, fill):
    rows = [""] * 7
    for ch in s.upper():
        glyph = FONT.get(ch, FONT[" "]).split()
        for i in range(7):
            rows[i] += glyph[i] + "."
    return f'<g transform="translate({x} {y}) scale({px})">' + grid_rects(rows, {"#": fill}) + '</g>'


def skyline_layer(color, lit, unlit, hmin, hmax, seed, base):
    rnd = random.Random(seed)
    x, out = 0, []
    while x < W:
        w = rnd.choice([36, 44, 52, 60, 72])
        cap = min(52, hmax) if x < 360 else hmax     # keep the title area clear
        h = rnd.randint(hmin, cap) // 6 * 6
        y = base - h
        out.append(rect(x, y, w, h, color))
        if lit:
            for wy in range(y + 10, base - 6, 14):
                for wx in range(x + 8, x + w - 10, 12):
                    out.append(rect(wx, wy, 5, 6, lit if rnd.random() < 0.38 else unlit))
        x += w + rnd.choice([0, 0, 6])
    return "".join(out)


def banner():
    h = BANNER_H
    sky = ["#17123a", "#1f1750", "#2c1f69", "#40297c", "#5b3487", "#7b4290"]
    body = ""
    for i, c in enumerate(sky):
        y0, y1 = round(i * h / 6), round((i + 1) * h / 6)
        body += rect(0, y0, W, y1 - y0, c)
    rnd = random.Random(7)
    for i in range(30):
        x, y = rnd.randint(300, 820), rnd.randint(8, 96)
        if (590 < x < 690 and 12 < y < 120) or (728 < x < 800 and 10 < y < 78):
            continue
        s = rnd.choice([3, 3, 4])
        tw = f' class="tw" style="animation-delay:{rnd.random() * 2:.1f}s"' if i % 3 == 0 else ""
        body += rect(x, y, s, s, WHITE, tw)
    body += skyline_layer("#2a1f63", None, None, 40, 80, 3, h)
    body += skyline_layer("#0e0b24", "#ffd97a", "#2a2256", 20, 58, 11, h)
    body += ('<g transform="translate(740 20) scale(6)">'
             + grid_rects(MOON, {"M": "#ffe9a8", "D": "#e8c877"}) + '</g>')
    body += ghost(604, 28, 6)
    body += pixel_text(NAME, 39, 31, 5, "#6b4fc4")      # drop shadow
    body += pixel_text(NAME, 36, 28, 5, WHITE)
    body += text(36, 90, "@" + HANDLE, INK, 14)
    x = 36
    for chip in CHIPS:
        w = round(len(chip) * 7.4 + 22)
        body += (f'<rect x="{x + 1}" y="103" width="{w - 2}" height="24" fill="#17123a" '
                 f'stroke="{ACCENT}" stroke-width="2"/>')
        body += text(x + w / 2, 119, chip, WHITE, 12, 400, "middle")
        x += w + 8
    return svg(W, h, body, f"{NAME.title()}'s GitHub: a pixel ghost floating over a night city")


def terminal():
    """One card: ghost + neofetch lines on the left, skill bars on the right."""
    top, pad, lh = 38, 18, 22
    block = max((len(INFO) + 1) * lh, 20 + len(SKILLS) * 28)
    h = top + pad + block + pad
    body = f'<rect x="1" y="1" width="{W - 2}" height="{h - 2}" fill="#0a0817" stroke="{LINE}" stroke-width="2"/>'
    body += rect(2, 2, W - 4, 35, "#17123a") + rect(2, 36, W - 4, 2, LINE)
    for i, c in enumerate(["#ff9ecb", "#ffd97a", "#9be89b"]):
        body += rect(18 + i * 18, 14, 10, 10, c)
    title = f"{NAME.lower()}@github: ~ $"
    tlen = round(len(title) * 7.8)
    body += text(84, 24, title, MUTED, 13, length=tlen)
    body += rect(84 + tlen + 8, 12, 8, 15, INK, ' class="cur"')

    y0 = top + pad
    body += ghost(26, y0 + (block - 84) // 2, 6)
    tx = 120
    body += text(tx, y0 + 15, f"{NAME.lower()}@github", ACCENT, 13, 700)
    for i, (k, v) in enumerate(INFO):
        y = y0 + 15 + (i + 1) * lh
        body += text(tx, y, k, ACCENT) + text(tx + 62, y, v)

    sx = 496
    body += rect(sx - 22, y0, 2, block, LINE)
    body += text(sx, y0 + 15, "$", ACCENT) + text(sx + 16, y0 + 15, "skills --bars", MUTED)
    bx = sx + 112
    bw = W - 26 - bx
    for i, (label, pct) in enumerate(SKILLS):
        y = y0 + 30 + i * 28
        body += text(sx, y + 12, label)
        body += (f'<rect x="{bx + 1}" y="{y + 1}" width="{bw - 2}" height="14" fill="#110e26" '
                 f'stroke="{LINE}" stroke-width="2"/>')
        fw = round((bw - 4) * pct / 100)
        d = round(0.15 * i / 2.4, 3)                    # stagger: hold at 0, then fill
        body += (f'<rect x="{bx + 2}" y="{y + 2}" width="{fw}" height="12" fill="{ACCENT}">'
                 f'<animate attributeName="width" values="0;0;{fw}" keyTimes="0;{d};1" dur="2.4s" '
                 f'calcMode="spline" keySplines="0 0 1 1;0.2 0.7 0.3 1" fill="freeze"/></rect>')
    label = (f"{NAME.lower()}@github: " + ", ".join(v for _, v in INFO)
             + ". Skills: " + ", ".join(s for s, _ in SKILLS))
    return svg(W, h, body, label)


ENVELOPE = """
#########
##.....##
#.#...#.#
#..#.#..#
#...#...#
#.......#
#########
""".strip().split("\n")


def btn_email():
    w, h = 132, 44
    body = f'<rect x="1" y="1" width="{w - 2}" height="{h - 2}" fill="#0a0817" stroke="{ACCENT}" stroke-width="2"/>'
    body += '<g transform="translate(22 15) scale(2)">' + grid_rects(ENVELOPE, {"#": WHITE}) + '</g>'
    body += text(52, 27, "Email", INK, 13)
    return svg(w, h, body, "Email")


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    files = {"banner.svg": banner(), "terminal.svg": terminal(), "btn-email.svg": btn_email()}
    for name, data in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(data)
        print(f"assets/{name}  {len(data) / 1024:.1f} KB")
