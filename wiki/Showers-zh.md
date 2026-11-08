**English** · [Русский](Showers-ru) · [Deutsch](Showers-de) · [日本語](Showers-ja)

# 流星雨

*选项卡：流星雨。*

[![流星雨](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

所有计算所用的流星雨目录：来自 **IMO Meteor Shower Calendar 2026 和 2027**（表 5 和 7）的 **45 个流星雨**，外加**反日点源**（表 6），每个都附有其**下一个峰值**。

## 列

| 列 | 含义 |
|---|---|
| 代码 | IMO 代码（QUA、PER、GEM …） |
| 流星雨 | 名称 |
| 活动 | 活动期（日/月 – 日/月） |
| λ max | 峰值时的太阳黄经（J2000），取自 IMO |
| **下一个峰值（UTC）** | 下一个峰值的日期和时间（见下文） |
| **峰值来源** | *IMO 2026* / *IMO 2027* = IMO 公布的日期和时间；*IMO 2026（日）* = IMO 只给出日期，显示的时间为计算值（*计算值 ~hh:mm*）；*由 λ 计算* = 该年份没有 IMO 数值 |
| 赤经、赤纬 | 峰值时的辐射点（反日点源为*移动*） |
| v km/s、r | 地心速度和布居指数 |
| ZHR | 峰值 ZHR（*变化* = 可变） |
| 类型 | *目视* 或 *无线电，白昼* |
| 今日活跃 | 流星雨当前活跃时显示*是* |

## 下一个峰值

程序始终显示**下一个**峰值。如果 IMO 已发布当年的日历，就使用 `data/massimi_imo.csv` 中的 **IMO 日期和时间**（已包含 2026 和 2027 年）；否则计算太阳到达峰值太阳黄经的时刻（Meeus，*Astronomical Algorithms*，第 25 章，用牛顿法求解）。

**验证：** 在 IMO 给出时间的情况下，计算结果与 IMO 2026 和 2027 年日历的差异在几分钟以内（例如象限仪座流星雨 2026 年 1 月 3 日 21:13，IMO 为 21:00；双子座流星雨 2027 年 12 月 14 日 19:51，IMO 为 20:00）。例外：2026 年白昼狮子座κ流星雨晚一天（9 月 26 日而非 9 月 25 日），以及 2027 年宝瓶座η流星雨的时间（15:10，IMO 为 09:00）——这些情况下使用 IMO 的数值。

**添加年份：** IMO 发布新日历后，将其各行添加到 `data/massimi_imo.csv` 中（`year;code;MM-DD;hh:mm`，如果 IMO 只给出日期，时间留空）。在此之前，峰值由计算得出。

## 小型与白昼流星雨

目录包含 IMO 列表中的**小型流星雨**——例如十月鹿豹座流星雨（OCT，ZHR 5，10 月 5–6 日活跃）、仙女座流星雨、小熊座γ流星雨——以及 4 月至 10 月的**白昼无线电流星雨**（白昼四月双鱼座流星雨、白昼白羊座流星雨、白昼英仙座ζ流星雨、白昼金牛座β流星雨、白昼狮子座κ流星雨、白昼六分仪座流星雨 …）。即使 ZHR 很小，它们也会计入[路径指数](Efficiency-Calculation-zh#模型)和[推荐的 Hot](Sky-View-zh#推荐的-hot)。IMO 不给出白昼无线电流星雨的 ZHR：在没有给出数值的情况下，程序使用工作值 5。

## 活动曲线与辐射点漂移

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max、α0、δ0 和 λ_max 取自 IMO 日历；斜率 B（峰值前后不同）以及每日漂移 dα/dλ、dδ/dλ 是写在 `data/sciami.csv` 中的**工作值**（IMO 的漂移表尚未录入）。*手册公式 9 和 13。* 反日点源的位置在 IMO 表 6 的各日期之间线性插值（`data/ant_radiante.csv`；12 月 10 日至 9 月 20 日活跃，ZHR 约 4）。

## 编辑目录

`data/sciami.csv` 是一个可以编辑的纯文本文件（分隔符 `;`）：代码、名称、开始和结束日期（MM-DD）、λ max、赤经、赤纬、漂移、v、r、ZHR、峰值前/后的 B、类型（V 目视，R 白昼无线电）。如果某一行有误，程序会在启动时显示消息并忽略该行。

来源：International Meteor Organization – Meteor Shower Calendar 2026 和 2027，[www.imo.net](https://www.imo.net)（表 5、6 和 7）；Philip G0ISW（无线电最大每小时数）；Rossano IZ5TEK（scattertek）。
