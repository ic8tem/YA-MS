[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · **中文**

# 试验性预报

*选项卡：预报计算 › 试验性预报。*

[![试验性预报](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

本选项卡将 **Collm 雷达（36.2 MHz）**的流星计数换算为**业余频段上每小时反射次数**的估算值（默认 144 MHz，可选 28 至 1300 MHz 的任意频率），为您的路径预报**未来 24 小时**，并可将估算值与 **RMOB** 观测者的数据进行**比较**——例如一位在 143.050 MHz 上收听 GRAVES 的观测者。

> 这里的一切都是**试验性**的：频率规则是一条经验规则，电台因子取决于您的电台。请用这些数字来比较不同的小时和日期，并在实际通联中加以检验。

## 控件

| 控件 | 默认 | 作用 |
|---|---|---|
| **目标频率 MHz** | 144 | 预报的频率（28–1300 MHz） |
| **λ^k 指数** | 3 | 频率规则的指数 k（SM6FHZ：3） |
| **电台因子 K** | 1 | 体现接收电台的情况（功率、天线）；通过与同一频段上的 RMOB 观测者比较得出 |
| **从磁盘载入 RMOB 文件...** | | 读取一个 RMOB 月度文本文件（见下文） |
| **由 RMOB 文件推算指数** | | 根据 Collm 和 RMOB 的共同小时拟合 k |
| **RMOB 观测者** | 空 | 观测者名称，与文件名中的写法一致（例如 `NAME_112026rmob.TXT` → `NAME`） |
| **立即下载 RMOB** | | 下载该观测者当月的文件一次 |
| **每 5 分钟自动下载（仅在获得 RMOB 许可后启用）** | **关闭** | 参见[RMOB 与自动程序](#rmob-与自动程序) |

控件下方的橙色行显示代入当前数值后的规则，例如 *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*，以及持续时间的换算和该频率下的 IARU 最大 ping。

## 从雷达到业余频段

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**来源：** SM6FHZ，*"432 MHz Meteorscatter, Challenges and Techniques"*，第 45 届 Nordic VUSHF，2025 年 5 月——反射的数量和强度按 **λ³** 缩放，持续时间按 **λ²** 缩放（432 MHz 比 144 MHz 低 14–15 dB，持续时间为其 1/9）。**验证：** 在 McKinley 方程中，λ³ 是单条欠密余迹的功率，而不是余迹的数量；质量指数为 2 时，高于固定阈值的余迹数量约按 λ^1.5 缩放（IZ5TEK；OH5IY）。程序保留 SM6FHZ 的经验规则 k = 3，并加以说明；适合你电台的 k 来自与 RMOB 的比较。在前向散射中，持续时间还随 sec²φ 增长（McKinley；OH5IY）：Collm 以后向散射（φ = 0）测量，因此预报乘以路径中点处的 sec²φ（60° 时 ×4，70° 时 ×8.5，80° 时 ×33）。取 k = 3 时，Collm 的 1000 流星/小时约相当于 **144 MHz 上 16 次反射/小时**；在 143.050 MHz 上收听 GRAVES 的 RMOB 观测者通常统计到 **20 至 140 次回波/小时**（RMOB 公报，2018 年 6 月）：数量级相符，差异即为电台因子 K。（手册公式 44–45。）

## 未来 24 小时

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**持续性：** 取前一天同一时刻的换算值（若缺失则取前两天的），并按**路径流星雨指数** I（Σ ZHR × 效率，参见[效率计算](Efficiency-Calculation-zh#模型)）的变化加以修正。常数 10 代表偶发流星背景，在指数很小时限制修正幅度。*程序的选择（手册公式 47）。*

| 面板 | 内容 |
|---|---|
| **在 Collm 测得并换算至 f MHz - 昨天和今天（UTC）** | Collm 雷达流星数/小时；换算值（橙色，右侧刻度）；如已载入则显示 RMOB 计数（绿色，右侧刻度） |
| **… 未来 24 小时 f MHz 试验性预报** | 预报的反射次数/小时（柱）以及路径流星雨指数（右侧刻度） |
| 表格 | UTC 时间 · Collm 同一时刻 · 换算 · 路径流星雨指数 · 预报 /小时 · **评价** |

**评价：** 预报值至少为 24 小时平均值的 1.3 倍时为*良好*，0.8 倍起为*一般*，低于此为*差*。同一预报也出现在**试验性预报**卡片和[效率计算](Efficiency-Calculation-zh)的橙色行中，并且是 [GRAVES 雷达](GRAVES-Radar-zh#预期回波试验性)选项卡中预期回波的基础。

## RMOB 比较

[RMOB](https://www.rmob.org)（Radio Meteor Observatories On Line，Pierre Terrier）汇集无线电观测者的逐时流星计数；意大利有许多观测者在 143.050 MHz 上收听 GRAVES（威尼斯天文馆、Faenza、Rovereto 等）。

**读取 RMOB 文件。** 接受两种文本格式：

| 格式 | 样式 | 说明 |
|---|---|---|
| 月度文件（Colorgramme / Spectrum Lab） | 每天一行，`day| n| n| …`，含 24 个逐时数值 | 常见的 `NAME_MMYYYYrmob.TXT` |
| 公报表格 | 表头 ` UT |  1   2   3 …`，数据行 `0h|175 166 …` | 如果文件中有多位观测者，会依次读取：请使用只含一位观测者的文件 |

月份和年份取自文件名（`…_MMYYYYrmob…`）或表头；否则使用当前月份（程序会加以说明）。

**拟合指数。** 取 K = 1，由共同小时（至少 3 个）上 RMOB/Collm 比值的中位数求得：

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*程序的选择（手册公式 46）。* 对话框显示共同小时、比值中位数和 k；**是** 采用 k（并设 K = 1），**否** 保持 k = 3——之后请将 K 手动调整为同一对话框中建议的值。

## RMOB 与自动程序

RMOB 要求**自动程序不要抓取其文件**。因此**自动下载**在初始时是**关闭**的，并且**只有在征得 RMOB 许可之后**才应启用。即使没有许可，您也随时可以使用**从磁盘载入 RMOB 文件...**，或在需要时点击**立即下载 RMOB**。

下载地址是 `config.ini` 中的一个模板（键 `rmob_url`，默认 `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`，其中 `{NOME}` 是观测者，`{MMAAAA}` 是月份和年份）；下载的文件保存在 `data/radar/` 中。
