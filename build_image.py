#!/usr/bin/env python3
"""Build the 1024x1024 newspaper-style infographic for 25 November 2026.

Draws news.png with PIL. Layout, written fresh for this entry:
masthead -> lead story (full width) -> stat strip -> 3-column row
of three stories -> 2-column row of two stories -> footer.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 242, 231)   # off-white newsprint
INK = (26, 26, 26)        # near-black
ACCENT = (155, 28, 28)    # restrained deep red
GREY = (90, 84, 76)
RULE = (60, 55, 48)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

HERE = os.path.dirname(os.path.abspath(__file__))


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_para(draw, x, y, max_w, text, fnt, leading, color=INK):
    lines = wrap(draw, text, fnt, max_w)
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def draw_headline(draw, x, y, max_w, text, fnt, leading, color=INK):
    return draw_para(draw, x, y, max_w, text, fnt, leading, color)


def kicker(draw, x, y, text):
    f = font(SANS_B, 15)
    draw.text((x, y), text.upper(), font=f, fill=ACCENT)
    return y + 22


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 44  # side margin

    # ---- masthead ----
    d.line([(mx, 26), (W - mx, 26)], fill=RULE, width=2)
    d.text((W // 2, 34), "THE WORLD TODAY", font=font(SERIF_B, 64),
           fill=INK, anchor="ma")
    d.text((W // 2, 108), "WEDNESDAY  25  NOVEMBER  2026",
           font=font(SANS_B, 19), fill=ACCENT, anchor="ma")
    d.line([(mx, 140), (W - mx, 140)], fill=RULE, width=4)
    d.line([(mx, 147), (W - mx, 147)], fill=RULE, width=1)

    # ---- lead story ----
    y = 164
    y = kicker(d, mx, y, "Lead story  ·  Markets")
    y = draw_headline(d, mx, y, W - 2 * mx,
                      "AI sell-off returns as Nvidia rally fades",
                      font(SERIF_B, 40), 48)
    lead = ("Nvidia fell 5.9% on Tuesday after its 31% rebound on "
            "Jensen Huang's return as chief executive faded, as "
            "lawmakers questioned President Trump's role in the "
            "reinstatement. Huang told staff he broke conduct rules "
            "and is in therapy; Trump said he would consider a "
            "pardon, and Huang is due to testify before the Senate.")
    y = draw_para(d, mx, y + 4, W - 2 * mx, lead,
                  font(SERIF, 20), 27)
    # stat strip
    y += 12
    d.line([(mx, y), (W - mx, y)], fill=ACCENT, width=2)
    y += 10
    stats = "Nikkei -2.76%    ·    KOSPI down over 5%    ·    SoftBank -15%    ·    New US tariffs eyed on 16 economies"
    d.text((W // 2, y), stats, font=font(SANS_B, 16), fill=INK, anchor="ma")
    y += 30
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=2)

    # ---- story grid ----
    stories = [
        ("Conflict · Strait of Hormuz",
         "Two tankers hit mines in Hormuz",
         "Iran's Revolutionary Guards said two tankers hit naval "
         "mines in the Strait of Hormuz early on Wednesday. Iran "
         "also claims it shot down two US drones, an MQ-9 and a "
         "Lucas. Tehran says the strait stays closed \"day by day\"; "
         "the US is reported to be weighing strikes on Iranian "
         "leaders."),
        ("Space · China",
         "Shenzhou-24 docks with first foreign astronaut",
         "China launched Shenzhou-24 at 08:18 Beijing time and it "
         "docked with Tiangong about three and a half hours later. "
         "Pakistani payload specialist Muhammad Zeeshan Ali is the "
         "first foreign astronaut to visit the station."),
        ("Conflict · Riyadh",
         "Houthi strike on Riyadh tower wounds 11",
         "Eleven people were hurt when a Houthi attack hit the PIF "
         "Tower in Riyadh, the second strike on the tower in six "
         "days; the toll was confirmed on Wednesday. The Saudi-led "
         "coalition struck Hodeidah, and the Houthis threatened "
         "Jeddah and other Red Sea ports."),
        ("Justice · New York",
         "Huawei convicted of fraud and trade-secret theft",
         "A New York jury found Huawei guilty on 10 of 12 counts, "
         "including bank fraud, sanctions violations and conspiracy "
         "to steal trade secrets, and acquitted it of racketeering. "
         "Sentencing is set for September 2027; Huawei says it "
         "will appeal."),
        ("Europe · NATO",
         "Russian drone crosses into Polish airspace",
         "A Russian drone entered Polish airspace overnight into "
         "Tuesday, days after three Russian missiles came down in "
         "Poland. Warsaw called the incursion deliberate; Moscow "
         "denied it. Poland renewed its push for a permanent US "
         "troop presence."),
    ]

    grid_top = y + 14
    col_w = (W - 2 * mx - 2 * 24) // 3
    row_h = 312
    # row 1: three stories
    for i in range(3):
        x = mx + i * (col_w + 24)
        yy = grid_top
        yy = kicker(d, x, yy, stories[i][0])
        yy = draw_headline(d, x, yy, col_w, stories[i][1],
                           font(SERIF_B, 23), 28)
        draw_para(d, x, yy + 3, col_w, stories[i][2],
                  font(SERIF, 16), 22)
        if i < 2:
            d.line([(x + col_w + 12, grid_top),
                    (x + col_w + 12, grid_top + row_h - 18)],
                   fill=(200, 192, 178), width=1)
    # divider between rows
    d.line([(mx, grid_top + row_h), (W - mx, grid_top + row_h)],
           fill=RULE, width=1)
    # row 2: two stories, wider columns
    row2_top = grid_top + row_h + 14
    col2_w = (W - 2 * mx - 24) // 2
    for i in range(2):
        x = mx + i * (col2_w + 24)
        yy = row2_top
        yy = kicker(d, x, yy, stories[3 + i][0])
        yy = draw_headline(d, x, yy, col2_w, stories[3 + i][1],
                           font(SERIF_B, 24), 29)
        draw_para(d, x, yy + 3, col2_w, stories[3 + i][2],
                  font(SERIF, 16), 22)
        if i == 0:
            d.line([(x + col2_w + 12, row2_top),
                    (x + col2_w + 12, row2_top + 190)],
                   fill=(200, 192, 178), width=1)

    # ---- footer ----
    fy = H - 44
    d.line([(mx, fy), (W - mx, fy)], fill=RULE, width=2)
    d.text((W // 2, fy + 9),
           "The World Today  ·  Wednesday 25 November 2026  ·  All six stories reported on 25 November 2026",
           font=font(SANS, 14), fill=GREY, anchor="ma")

    out = os.path.join(HERE, "news.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, img.size)


if __name__ == "__main__":
    main()
