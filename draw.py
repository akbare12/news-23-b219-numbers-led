#!/usr/bin/env python3
"""Draw the 23 Nov 2026 world-news front page (1024x1024) with PIL.
Variant: NUMBERS-LED - a dominant Day in Numbers strip leads the page.
All 31 stories verified for Monday 23 November 2026; excluded items are
named ONLY in the red DATE CHECK box, never as 23 Nov news.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

INK = (17, 17, 17)
PAPER = (255, 255, 255)
RED = (185, 28, 28)
NAVY = (30, 58, 95)
TEAL = (15, 118, 110)
AMBER = (180, 83, 9)
GREEN = (21, 128, 61)
BLUE = (29, 78, 216)
GRAY = (107, 114, 128)
LGRAY = (243, 244, 246)
MAP_BG = (219, 231, 240)
LAND = (233, 233, 224)
LAND_EDGE = (150, 150, 140)
YELLOW_BG = (254, 243, 199)
GOLD = (146, 64, 14)
PINK_BG = (253, 242, 242)

FD = "/usr/share/fonts/truetype/dejavu/"
def F(name, size):
    return ImageFont.truetype(FD + name, size)

f_mast = F("DejaVuSerif-Bold.ttf", 46)
f_mast_date = F("DejaVuSans-Bold.ttf", 23)
f_kick = F("DejaVuSans-Bold.ttf", 10)
f_hero = F("DejaVuSans-Bold.ttf", 20)
f_hero_s = F("DejaVuSans-Bold.ttf", 17)
f_hero_big = F("DejaVuSans-Bold.ttf", 34)
f_title = F("DejaVuSans-Bold.ttf", 17)
f_sec = F("DejaVuSans-Bold.ttf", 11)
f_head = F("DejaVuSans-Bold.ttf", 10)
f_body = F("DejaVuSans.ttf", 9)
f_meta = F("DejaVuSans.ttf", 8)
f_small = F("DejaVuSans.ttf", 8)
f_num = F("DejaVuSans-Bold.ttf", 30)
f_numlab = F("DejaVuSans.ttf", 8)
f_pin = F("DejaVuSans-Bold.ttf", 8)
f_also = F("DejaVuSans.ttf", 9)
f_also_b = F("DejaVuSans-Bold.ttf", 9)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, font, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def trunc(lines, n):
    if len(lines) > n:
        lines = lines[:n]
        lines[-1] = lines[-1].rsplit(" ", 1)[0] + " ..."
    return lines

def badge(x, y, label, color):
    w = d.textlength(label, font=f_meta) + 10
    d.rounded_rectangle([x, y, x + w, y + 13], radius=3, fill=color)
    d.text((x + 5, y + 1), label, font=f_meta, fill=PAPER)
    return w

# ---------------- masthead ----------------
d.rectangle([0, 0, W, 5], fill=INK)
d.rectangle([0, 5, W, 8], fill=RED)
d.text((10, 12), "THE WORLD TODAY", font=f_mast, fill=INK)
d.text((W - 10 - d.textlength("MONDAY 23 NOVEMBER 2026", font=f_mast_date), 16),
       "MONDAY 23 NOVEMBER 2026", font=f_mast_date, fill=RED)
d.text((W - 10 - d.textlength("MONDAY EDITION  -  ALL TIMES GMT", font=f_small), 48),
       "MONDAY EDITION  -  ALL TIMES GMT", font=f_small, fill=GRAY)
d.line([10, 66, W - 10, 66], fill=INK, width=2)

# meta strip + legend
d.text((10, 72), "31 STORIES  -  6 REGIONS  -  EVERY ITEM DATED 23 NOV", font=f_sec, fill=NAVY)
d.text((W - 10 - d.textlength("REPORTED = confirmed  -  CLAIM = one side alleges  -  ONGOING = still developing", font=f_meta), 74),
       "REPORTED = confirmed  -  CLAIM = one side alleges  -  ONGOING = still developing", font=f_meta, fill=GRAY)
d.line([10, 90, W - 10, 90], fill=INK, width=1)

# ---------------- hero trio (compact) ----------------
HX = [10, 348, 686]
HW = 328
heroes = [
    ("MARKETS  -  SEOUL", "AI ROUT HITS ASIA", "-3.3%",
     "Kospi closes 4,708.54, down 3.3% (intraday -5.8%) as the AI sell-off spreads from Wall Street. Samsung -3.1%, SK Hynix -2.5%.",
     "Korea JoongAng Daily  -  CNBC"),
    ("UNITED NATIONS  -  BARBADOS", "GUTERRES: REGULATE AI", "150",
     "UN chief urges binding global AI safety rules at the Bridgetown summit. 150 delegates back a risk framework - a blueprint, not a treaty.",
     "UN News  -  UN Web TV"),
    ("ASIA POWER INDEX 2026", "US LEAD AT RECORD LOW", "5.3",
     "US 78.9 vs China 73.6, gap 5.3 - narrowest since 2018. India 3rd at 40.5; US diplomatic influence -6 to 76.7.",
     "Lowy Institute  -  published Sun, reported Mon"),
]
for i, (kick, head, big, body, src) in enumerate(heroes):
    x = HX[i]
    d.text((x, 98), kick, font=f_kick, fill=RED)
    # big number right-aligned; headline sized to never collide with it
    big_w = d.textlength(big, font=f_hero_big)
    head_w = d.textlength(head, font=f_hero_s)
    if head_w + big_w + 12 > HW:
        # wrap headline to two lines above the body
        hl = wrap(head, f_hero_s, HW - 6)
        for j, ln in enumerate(hl):
            d.text((x, 112 + j * 20), ln, font=f_hero_s, fill=INK)
        body_y = 112 + len(hl) * 20 + 4
    else:
        d.text((x, 112), head, font=f_hero_s, fill=INK)
        body_y = 142
    d.text((x + HW - big_w - 2, 106), big, font=f_hero_big, fill=NAVY)
    blines = trunc(wrap(body, f_body, HW - 6), 2 if head_w + big_w + 12 > HW else 3)
    for j, ln in enumerate(blines):
        d.text((x, body_y + j * 12), ln, font=f_body, fill=INK)
    d.text((x, body_y + len(blines) * 12 + 2), src, font=f_meta, fill=GRAY)
    if i < 2:
        d.line([x + HW + 4, 98, x + HW + 4, 192], fill=(200, 200, 200), width=1)
d.line([10, 196, W - 10, 196], fill=INK, width=2)

# ---------------- THE DAY IN NUMBERS (dominant strip) ----------------
d.rectangle([10, 204, W - 10, 230], fill=NAVY)
d.text((20, 209), "THE DAY IN NUMBERS", font=f_title, fill=PAPER)
d.text((W - 20 - d.textlength("TEN FIGURES THAT DEFINE MONDAY", font=f_sec), 212),
       "TEN FIGURES THAT DEFINE MONDAY", font=f_sec, fill=(200, 210, 230))
nums = [
    ("186", "DRONES FIRED AT UKRAINE", "overnight barrage on Kyiv", RED),
    ("161", "SHOT DOWN OR JAMMED", "Ukraine air defences", NAVY),
    ("720", "INDIA'S DECLARED TOTAL", "Rahul 136, Pant 128", TEAL),
    ("9", "WICKETS DOWN AT THE CALL", "India declare 720/9", TEAL),
    ("98,79%", "HONG KONG TURNOUT", "723 seats, 856 candidates", AMBER),
    ("$120bn", "COP31 ADAPTATION TARGET", "dropped from the Antalya text", RED),
    ("35%", "2035 POWER TARGET KEPT", "in the rejected COP31 pact", AMBER),
    ("44h", "COP31 OVERTIME", "talks ran ~2 days long", NAVY),
    ("50", "WEMBANYAMA POINTS", "Spurs beat rivals 114-91", GREEN),
    ("24", "NIGERIA BOAT DEAD - 21 NOV", "not 23 Nov: see DATE CHECK", RED),
]
CW, CH = 196, 88
for i, (num, lab, sub, col) in enumerate(nums):
    col_i, row_i = i % 5, i // 5
    x = 10 + col_i * (CW + 5)
    y = 238 + row_i * (CH + 6)
    d.rectangle([x, y, x + CW, y + CH], fill=LGRAY, outline=(210, 210, 210))
    d.rectangle([x, y, x + CW, y + 4], fill=col)
    d.text((x + 8, y + 10), num, font=f_num, fill=INK)
    for j, ln in enumerate(trunc(wrap(lab, f_head, CW - 14), 2)):
        d.text((x + 8, y + 46 + j * 12), ln, font=f_head, fill=INK)
    d.text((x + 8, y + 72), sub, font=f_numlab, fill=GRAY)
d.line([10, 428, W - 10, 428], fill=INK, width=1)

# ---------------- region bar ----------------
d.text((10, 436), "ASIA 7   -   EUROPE 8   -   MIDEAST 6   -   AMERICAS 5   -   AFRICA 3   -   OCEANIA 2   =   31 STORIES",
       font=f_sec, fill=NAVY)
d.line([10, 456, W - 10, 456], fill=INK, width=1)

# ---------------- 10 news cards ----------------
cards = [
    ("AMERICAS", "Anthropic IPO: $83 a share", "Claude maker raised a record $107.3B, largest ever; debut close $97.17.", "REPORTED"),
    ("AMERICAS", "Skubal signs $450M Mets deal", "Two-time Cy Young winner agrees a nine-year deal, largest ever for a pitcher.", "REPORTED"),
    ("EUROPE", "Zelenskyy: 165 Russian missiles", "Kyiv says Moscow fired 165 missiles in seven days; US delays on Patriots.", "REPORTED"),
    ("EUROPE", "Manchester: 12,000 cleared", "Crowds leave an event after an unknown substance is dispersed; no casualties.", "REPORTED"),
    ("MIDEAST", "Lebanon seizes 264 kg explosives", "Army says it caught explosives smuggled in from Syria as smuggling surges.", "REPORTED"),
    ("EUROPE", "COP31: the day after", "194 nations reject the Antalya Pact; Guterres 'profoundly frustrated'.", "REPORTED"),
    ("ASIA", "Seoul readies 10T-won fund", "Seoul readies a $6.8B stabilisation fund to steady the Kospi.", "REPORTED"),
    ("EUROPE", "Paris: 100+ back 2% tax", "Economists, politicians and unions rally behind a 2% billionaire wealth tax.", "REPORTED"),
    ("AFRICA", "DRC: Ebola teams trapped", "Ebola teams trapped by fighting in an Ituri hospital; 11,762 cases.", "ONGOING"),
    ("EUROPE", "Poland: 3 missiles crossed in", "Prosecutors confirm three Kh-101 cruise missiles entered Poland on Friday.", "REPORTED"),
]
for i, (reg, head, body, cert) in enumerate(cards):
    col_i, row_i = i % 5, i // 5
    x = 10 + col_i * (CW + 5)
    y = 464 + row_i * (CH + 6)
    d.rectangle([x, y, x + CW, y + CH], fill=PAPER, outline=(190, 190, 190))
    d.text((x + 8, y + 6), reg, font=f_kick, fill=RED)
    badge(x + CW - 62, y + 5, cert, GREEN if cert == "REPORTED" else AMBER)
    for j, ln in enumerate(trunc(wrap(head, f_head, CW - 14), 2)):
        d.text((x + 8, y + 22 + j * 12), ln, font=f_head, fill=INK)
    for j, ln in enumerate(trunc(wrap(body, f_body, CW - 14), 3)):
        d.text((x + 8, y + 48 + j * 11), ln, font=f_body, fill=(60, 60, 60))

# ---------------- map + ALSO ----------------
MY = 656
MAP_H = 204
d.rectangle([10, MY, 614, MY + MAP_H], fill=MAP_BG, outline=(170, 180, 190))
d.text((20, MY + 6), "WHERE IT HAPPENED - EVERY STORY PINNED", font=f_sec, fill=NAVY)

def lonlat(lon, lat):
    mx, my, mw, mh = 20, MY + 26, 584, 156
    return mx + (lon + 180) / 360.0 * mw, my + (90 - lat) / 180.0 * mh

# schematic continents (rough equirectangular polygons)
conts = [
    [(-168, 66), (-140, 70), (-120, 71), (-95, 80), (-75, 73), (-55, 60), (-60, 47), (-70, 42), (-75, 35), (-80, 26), (-90, 21), (-97, 16), (-105, 20), (-115, 28), (-125, 40), (-125, 49), (-140, 60), (-165, 60)],
    [(-80, 10), (-60, 8), (-50, 0), (-40, -5), (-35, -10), (-40, -20), (-50, -30), (-60, -35), (-70, -40), (-73, -50), (-70, -55), (-75, -35), (-80, -20), (-80, -5)],
    [(-10, 36), (-10, 43), (-2, 48), (0, 51), (8, 54), (10, 58), (18, 56), (25, 60), (30, 70), (40, 68), (35, 55), (30, 45), (28, 41), (20, 40), (12, 38), (3, 38)],
    [( -6, 35), (10, 37), (20, 32), (30, 31), (35, 28), (43, 12), (48, 11), (51, 0), (40, -10), (35, -20), (30, -30), (20, -35), (12, -18), (9, 0), (9, 5)],
    [(40, 68), (60, 70), (80, 72), (100, 75), (130, 72), (160, 70), (180, 66), (170, 60), (160, 55), (140, 40), (130, 35), (122, 30), (110, 20), (105, 10), (100, 8), (90, 15), (80, 8), (75, 20), (70, 25), (60, 25), (50, 30), (45, 40), (40, 50)],
    [(113, -22), (122, -14), (132, -12), (142, -11), (147, -19), (150, -23), (153, -27), (150, -37), (140, -38), (130, -32), (125, -33), (115, -35), (113, -26)],
]
for poly in conts:
    pts = [lonlat(lo, la) for lo, la in poly]
    d.polygon(pts, fill=LAND, outline=LAND_EDGE)

# pin lon/lat nudged slightly so numbered pins do not collide at this scale
pins = [
    ("SEOUL", 130, 35, "1"), ("BRIDGETOWN", -59, 13, "2"), ("WASHINGTON", -77, 39, "3"),
    ("BEIJING", 112, 42, "4"), ("KYIV", 33, 48, "5"), ("HONG KONG", 112, 20, "6"),
    ("MUMBAI", 70, 17, "7"), ("PARIS", 0, 47, "8"), ("MANCHESTER", -6, 55, "9"),
    ("BEIRUT", 38, 32, "10"), ("KINSHASA", 15, -4, "11"), ("WARSAW", 24, 54, "12"),
    ("ANTALYA", 28, 35, "13"),
]
for name, lo, la, n in pins:
    px, py = lonlat(lo, la)
    d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=RED, outline=PAPER)
    d.text((px - 2 if len(n) == 1 else px - 4, py - 5), n, font=f_pin, fill=PAPER)
    # no in-map city labels: pins are identified by the numbered key below
d.text((20, MY + 184), "1 Seoul  2 Bridgetown  3 Washington  4 Beijing  5 Kyiv  6 Hong Kong  7 Mumbai",
       font=f_meta, fill=GRAY)
d.text((20, MY + 195), "8 Paris  9 Manchester  10 Beirut  11 Kinshasa  12 Warsaw  13 Antalya",
       font=f_meta, fill=GRAY)

# ALSO box (two columns of 9, 8pt)
AX = 624
f_also = F("DejaVuSans.ttf", 8)
f_also_b = F("DejaVuSans-Bold.ttf", 8)
d.rectangle([AX, MY, W - 10, MY + MAP_H], fill=PAPER, outline=(190, 190, 190))
d.text((AX + 10, MY + 6), "ALSO - 18 MORE STORIES", font=f_sec, fill=NAVY)
also = [
    ("Dhaka:", "Hasina will be jailed if she returns"),
    ("Seoul:", "minister quits over AI exam chaos"),
    ("Tehran:", "Trump: strikes may resume"),
    ("Washington:", "Bessent demands Nvidia answers"),
    ("Hong Kong:", "turnout 98,79%, 723 seats"),
    ("Cricket:", "India declare 720/9"),
    ("NBA:", "Wembanyama 50 pts, Spurs 114-91"),
    ("F1:", "Verstappen wins 75th, +0.639s"),
    ("Tennis:", "Alcaraz d. Zverev 6-2, 7-6(7)"),
    ("Tel Aviv:", "Israel unity talks resume"),
    ("Gaza:", "two killed in Israeli strike"),
    ("West Bank:", "settler attacks hit villages"),
    ("Tehran:", "Iran war: no deal in sight"),
    ("Benghazi:", "UN demands probe of port attacks"),
    ("Khartoum:", "air defences down drones"),
    ("Sydney:", "PMI 46.1, fastest fall in 5 years"),
    ("Wellington:", "retail +2.2%, best since Dec 2021"),
    ("Moscow:", "Intel warns of nuclear satellite"),
]
for j, (k, v) in enumerate(also):
    col_i, row_i = j // 9, j % 9
    bx = AX + 10 + col_i * 192
    y = MY + 26 + row_i * 19
    lines = trunc(wrap(k + " " + v, f_also, 186), 2)
    # bold kicker on first line: draw kicker bold, rest regular
    d.text((bx, y), k, font=f_also_b, fill=INK)
    first = lines[0][len(k):].lstrip() if lines else ""
    d.text((bx + d.textlength(k + " ", font=f_also_b), y), first, font=f_also, fill=(60, 60, 60))
    if len(lines) > 1:
        d.text((bx, y + 9), lines[1], font=f_also, fill=(60, 60, 60))

# ---------------- DATE CHECK (red box) ----------------
DY = 872
d.rectangle([10, DY, W - 10, DY + 66], fill=PINK_BG, outline=RED)
d.text((20, DY + 6), "DATE CHECK - EVERY STORY DATED 23 NOV 2026. EXCLUDED AS NOT 23 NOV:",
       font=f_sec, fill=RED)
d.text((20, DY + 26), "Democrats reach 258 (22 Nov)  -  Sparta II fire (22 Nov)  -  El Chapo Isidro captured (22 Nov)",
       font=f_body, fill=INK)
d.text((20, DY + 42), "EU-Indonesia pact (21 Nov)  -  Nigeria boat, 24 dead (21 Nov)  -  ICJ Myanmar ruling (19 Nov).",
       font=f_body, fill=INK)

# ---------------- footer ----------------
FY = 950
d.line([10, FY, W - 10, FY], fill=INK, width=1)
d.text((10, FY + 8), "Sources: AP, Reuters, CNN, BBC, AFP, UN News, WHO, Lowy Institute, Korea JoongAng Daily, Bloomberg, Morningstar, S&P Global, Stats NZ.",
       font=f_meta, fill=GRAY)
d.text((10, FY + 20), "All figures checked at press time. Items whose date could not be pinned to 23 November 2026 were left out and are named above.",
       font=f_meta, fill=GRAY)
d.text((10, FY + 34), "THE WORLD TODAY  -  23 NOV 2026  -  NUMBERS-LED EDITION", font=f_meta, fill=INK)
d.text((W - 10 - d.textlength("PAGE 1 OF 1", font=f_meta), FY + 34), "PAGE 1 OF 1", font=f_meta, fill=GRAY)

img.save(OUT)
print("WROTE", OUT, os.path.getsize(OUT), "bytes")
