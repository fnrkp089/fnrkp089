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
.ps{animation:pr 1.2s steps(1,end) infinite}
@keyframes pr{0%,59%{opacity:1}60%,100%{opacity:.2}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>"""


def svg(w, h, body, label):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'role="img" aria-label="{label}" shape-rendering="crispEdges">{STYLE}{body}</svg>\n')


def rect(x, y, w, h, fill, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}"{extra}/>'


def text(x, y, s, fill=INK, size=14, weight=400, anchor="start"):
    s = s.replace("&", "&amp;").replace("<", "&lt;")
    return (f'<text x="{x}" y="{y}" fill="{fill}" font-family="{MONO}" font-size="{size}" '
            f'font-weight="{weight}" text-anchor="{anchor}">{s}</text>')


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


def pixel_text(s, x, y, px, fill, cls=""):
    rows = [""] * 7
    for ch in s.upper():
        glyph = FONT.get(ch, FONT[" "]).split()
        for i in range(7):
            rows[i] += glyph[i] + "."
    c = f' class="{cls}"' if cls else ""
    return f'<g{c}><g transform="translate({x} {y}) scale({px})">' + grid_rects(rows, {"#": fill}) + '</g></g>'


def pixel_text_width(s, px):
    return (len(s) * 6 - 1) * px


def skyline_layer(color, lit, unlit, hmin, hmax, seed, base):
    rnd = random.Random(seed)
    x, out = 0, []
    while x < W:
        w = rnd.choice([36, 44, 52, 60, 72])
        cap = 62 if x < 360 else hmax          # keep the title area clear
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
    h = 240
    body = "".join(rect(0, i * 40, W, 40, c) for i, c in
                   enumerate(["#17123a", "#1f1750", "#2c1f69", "#40297c", "#5b3487", "#7b4290"]))
    rnd = random.Random(7)
    for i in range(30):
        x, y = rnd.randint(300, 820), rnd.randint(10, 118)
        if (590 < x < 690 and 20 < y < 134) or (728 < x < 800 and 18 < y < 86):
            continue
        s = rnd.choice([3, 3, 4])
        tw = f' class="tw" style="animation-delay:{rnd.random() * 2:.1f}s"' if i % 3 == 0 else ""
        body += rect(x, y, s, s, WHITE, tw)
    body += skyline_layer("#2a1f63", None, None, 50, 108, 3, h)
    body += skyline_layer("#0e0b24", "#ffd97a", "#2a2256", 24, 78, 11, h)
    body += ('<g transform="translate(740 28) scale(6)">'
             + grid_rects(MOON, {"M": "#ffe9a8", "D": "#e8c877"}) + '</g>')
    body += ghost(604, 40, 6)
    body += pixel_text(NAME, 39, 33, 5, "#6b4fc4")      # drop shadow
    body += pixel_text(NAME, 36, 30, 5, WHITE)
    body += text(36, 92, "@" + HANDLE, INK, 14)
    x = 36
    for chip in CHIPS:
        w = round(len(chip) * 7.4 + 22)
        body += (f'<rect x="{x + 1}" y="105" width="{w - 2}" height="24" fill="#17123a" '
                 f'stroke="{ACCENT}" stroke-width="2"/>')
        body += text(x + w / 2, 121, chip, WHITE, 12, 400, "middle")
        x += w + 8
    return svg(W, h, body, f"{NAME.title()}'s GitHub: a pixel ghost floating over a night city")


def divider():
    pal = [ACCENT, "#5a3fb0", "#ff9ecb", "#5a3fb0"]
    body = "".join(rect(i * 16 + 2, 0 if i % 2 == 0 else 8, 8, 8, pal[i % 4]) for i in range(W // 16))
    return svg(W, 16, body, "divider")


def terminal():
    top = 38
    block = max(len(INFO) + 2, 7) * 24
    h = top + 24 + block + 20 + 24 + 24 + 2
    body = f'<rect x="1" y="1" width="{W - 2}" height="{h - 2}" fill="#0a0817" stroke="{LINE}" stroke-width="2"/>'
    body += rect(2, 2, W - 4, 35, "#17123a") + rect(2, 36, W - 4, 2, LINE)
    for i, c in enumerate(["#ff9ecb", "#ffd97a", "#9be89b"]):
        body += rect(18 + i * 18, 14, 10, 10, c)
    body += text(84, 24, f"{NAME.lower()}@github: ~", MUTED, 13)
    y0 = top + 24
    body += ghost(38, y0 + (block - 154) // 2, 11)
    tx = 214
    body += text(tx, y0 + 17, f"{NAME.lower()}@github", ACCENT, 14, 700)
    body += text(tx, y0 + 41, "-" * (len(NAME) + 7), MUTED)
    for i, (k, v) in enumerate(INFO):
        y = y0 + 17 + (i + 2) * 24
        body += text(tx, y, k, ACCENT) + text(tx + 72, y, v)
    py = y0 + block + 20
    body += text(26, py + 17, "$", ACCENT)
    body += rect(44, py + 3, 9, 18, INK, ' class="cur"')
    label = f"{NAME.lower()}@github: " + ", ".join(v for _, v in INFO)
    return svg(W, h, body, label)


def skills():
    h = 24 + 20 + 16 + len(SKILLS) * 16 + (len(SKILLS) - 1) * 12 + 24 + 4
    body = f'<rect x="1" y="1" width="{W - 2}" height="{h - 2}" fill="#110e26" stroke="{LINE}" stroke-width="2"/>'
    body += text(26, 41, "$", ACCENT, 13) + text(42, 41, "skills --bars", MUTED, 13)
    tx, tw = 146, W - 146 - 26
    for i, (label, pct) in enumerate(SKILLS):
        y = 62 + i * 28
        body += text(26, y + 12, label, INK, 13)
        body += (f'<rect x="{tx + 1}" y="{y + 1}" width="{tw - 2}" height="14" fill="#0a0817" '
                 f'stroke="{LINE}" stroke-width="2"/>')
        fw = round((tw - 4) * pct / 100)
        d = round(0.15 * i / 2.4, 3)                    # stagger: hold at 0, then fill
        body += (f'<rect x="{tx + 2}" y="{y + 2}" width="{fw}" height="12" fill="{ACCENT}">'
                 f'<animate attributeName="width" values="0;0;{fw}" keyTimes="0;{d};1" dur="2.4s" '
                 f'calcMode="spline" keySplines="0 0 1 1;0.2 0.7 0.3 1" fill="freeze"/></rect>')
    return svg(W, h, body, "Skills: " + ", ".join(s for s, _ in SKILLS))


def footer():
    h = 110
    body = f'<rect x="1" y="1" width="{W - 2}" height="{h - 2}" fill="#17123a" stroke="{LINE}" stroke-width="2"/>'
    tw = pixel_text_width("PRESS START", 3)
    x = (W - (48 + 28 + tw)) // 2
    body += ghost(x, 27, 4)
    body += pixel_text("PRESS START", x + 76, 30, 3, "#ffd97a", "ps")
    body += text(x + 76, 76, "thanks for visiting", MUTED, 13)
    return svg(W, h, body, "Press start. Thanks for visiting")


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
    files = {"banner.svg": banner(), "divider.svg": divider(), "terminal.svg": terminal(),
             "skills.svg": skills(), "footer.svg": footer(), "btn-email.svg": btn_email()}
    for name, data in files.items():
        with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
            f.write(data)
        print(f"assets/{name}  {len(data) / 1024:.1f} KB")
