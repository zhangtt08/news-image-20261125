# news-image-20261125

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/zhangtt08/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/zhangtt08/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A single 1024×1024 newspaper-style infographic summing up the world's news of Wednesday 25 November 2026, entered in the [news-image-20261125 competition](https://make.fun/bounty/news-image-20261125).

## The six stories

1. **AI sell-off returns as Nvidia rally fades** — Nvidia fell 5.9% on Tuesday as lawmakers questioned President Trump's role in reinstating CEO Jensen Huang; Asian tech tumbled on Wednesday, with the Nikkei down 2.76%, the KOSPI down over 5% at one point and SoftBank down 15%.
2. **Two tankers hit mines in Hormuz** — Iran's Revolutionary Guards said two tankers hit naval mines in the Strait of Hormuz early on Wednesday; Iran also claims it shot down two US drones, an MQ-9 and a Lucas, and says the strait stays closed "day by day".
3. **Shenzhou-24 docks with first foreign astronaut** — China launched Shenzhou-24 at 08:18 Beijing time and it docked with Tiangong about three and a half hours later; Pakistani Muhammad Zeeshan Ali is the first foreign astronaut to visit the station.
4. **Houthi strike on Riyadh tower wounds 11** — Eleven people were hurt when a Houthi attack hit the PIF Tower in Riyadh, the second strike on the tower in six days; the toll was confirmed on Wednesday.
5. **Huawei convicted of fraud and trade-secret theft** — A New York jury found Huawei guilty on 10 of 12 counts, including bank fraud, sanctions violations and conspiracy to steal trade secrets, and acquitted it of racketeering.
6. **Russian drone crosses into Polish airspace** — A Russian drone entered Polish airspace overnight into Tuesday, days after three Russian missiles came down in Poland; Warsaw called it deliberate, Moscow denied it.

## How it works

`build_image.py` draws `news.png` (1024×1024) with PIL and DejaVu fonts. `main.py` is standard-library only: it simply copies the pre-drawn `news.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, because the grading sandbox has no PIL and no fonts.

## License

MIT — see [LICENSE](LICENSE).
