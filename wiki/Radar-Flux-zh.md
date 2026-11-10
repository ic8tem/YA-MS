[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · **中文**

# 雷达流量

*选项卡：实况与实时数据 › 雷达流量。*

[![雷达流量](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

本选项卡显示专业流星雷达**此刻**的统计结果：来自 **Collm** SKiYMET 雷达（德国莱比锡大学 / IAP Kühlungsborn，36.2 MHz）的逐时流星计数和余迹高度，以及 **Sodankylä** 雷达（SGO，芬兰）的最新图像。Collm 的计数用于您所用频段上的估算以及[试验性预报](Experimental-Forecasts-zh)；测得的余迹高度则用于全部几何计算。

## 控件

| 控件 | 作用 |
|---|---|
| **立即下载** | 立即检查所有外部数据源。 |
| **每 5 分钟自动更新所有数据源** | 默认开启。每 5 分钟检查一次所有数据源，**只重新下载有变化的**（*未变化（… UTC 检查）* / *… UTC 有新数据*）。 |
| **λ 指数（SM6FHZ）** | 频率规则的指数 k，默认 3（1–4）。 |

## 显示内容

| 面板 | 内容 |
|---|---|
| **流星数/小时 - 昨天和今天（UTC）** | 青色柱 = Collm 计数（有效），红色柱 = 已舍弃，橙色粗线 = 右侧刻度上的 *… MHz 估算* |
| **余迹高度（Collm）** | 70 至 110 km 之间每 km 高度的流星数，附最常见高度（众数）、平均值、中位数和标准差 |
| Collm 图像 | 下载得到的原始 SKiYMET 图表 |
| Sodankylä 图像 | Sodankylä 雷达最新的流星计数图像（仅显示；不读取其格式） |

图表上方的一行说明 Collm 图表的读取时间以及识别出的纵轴刻度（*从图表读取的刻度：0-… 流星/小时*）。

## 如何读取 Collm 图表

Collm 图表（720 × 720 像素，纯色）的坐标轴位置固定，但雷达**每天都会根据实测值调整纵轴刻度**（例如 2026 年 11 月 5 日为 0–1.2·10³，11 月 6 日为 0–1.0·10³，刻度线位置也随之移动）。因此 YA-MS：

1. 找出坐标轴上的长刻度线；
2. 将每个字符与图表的点阵字体比较，**读出**最高刻度和零点的**标签**；
3. 对每个小时 i（0–47，昨天和今天）取中心列，从上往下找到第一个青色像素 y：

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top 和 y0 分别是最高刻度和零点所在的行，N_top 是从最高标签读出的值（×1000）。分辨率：每像素约 7–8 流星/小时。*程序的选择（手册公式 42）。*

如果某个标签无法读取，程序退回到 2026 年 11 月 5 日的校准值（**已校准刻度 0-1200 流星/小时**），并以橙色提示：*无法读取流量纵轴刻度（顶部标签：…）：数值需核实。* 如果图表格式本身发生变化（*图表格式已变化（…x…）：无法读取* 或 *未在预期位置找到流量坐标轴*），就必须重新校准读取方式：请报告此问题（参见[参与贡献](Contributing-and-Contacts-zh)）。

### 余迹高度

由高度直方图（第 k km 中有 n_k 颗流星，平均高度 h_k）得到：

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*手册公式 43。* 勾选**来自雷达**（控件第 2 行）时，**众数**即作为所有计算中的余迹高度。验证：2026 年 11 月 5 日的图表——众数 89.5 km，平均 88.6 km，标准差 6.8 km，与 Cerrotta–Sartori 文章中约 90 km（SKiYMET 平均值）相符。

如果高度图表的刻度发生变化，程序会提示：*高度统计（众数、平均值、中位数）仍然有效，绝对计数则不再有效。*

## 您所用频段上的估算

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ** 的经验规则（VUSHF 2025）：反射的数量和强度按 λ³ 缩放，持续时间按 λ² 缩放；λ³ 关系与 McKinley 的欠密余迹方程一致。同时显示 IARU 第一区的最大 ping 持续时间（50 MHz 为 1000 ms，70 MHz 为 500 ms，144 MHz 为 100 ms，432 MHz 为 13 ms）。这些数值仅供参考，应与实际上机经验比较。电台因子 K 以及与 RMOB 的比较见[试验性预报](Experimental-Forecasts-zh)。

## 离线

如果所有数据源都无法访问，程序会**只显示一次**消息：*无互联网连接。雷达和 RMOB 数据无法更新：程序使用最后保存的数据，并每 5 分钟自动重试。* 底部状态栏变为红色（*无互联网连接 …*），直到连接恢复（*连接已恢复。*）。

## 档案与数据源

| 文件（位于 `data/`） | 内容 |
|---|---|
| `flusso_collm.csv` | 从 Collm 读取的流量逐时档案（已存在的小时会被更新） |
| `quote_collm.csv` | 余迹高度档案 |
| `radar/` | 最新下载的图像（以及 RMOB 文件） |
| `fonti_radar.csv` | 雷达数据源地址，`attivo=1/0` 用于启用/停用各个数据源 |

| 数据源 | 频率 | 说明 |
|---|---|---|
| Collm 流星雷达，莱比锡大学（LIM）和 IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | 每小时第 10 分钟（UTC）更新；昨天 + 今天的流量、高度分布 |
| Sodankylä 地球物理观测站 – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | 仅图像（雷达正在升级，DECC 项目） |
| swan.ms（Collm 的副本） | 36.2 MHz | 默认停用；仅在获得 DL1DBC 许可后使用 |

> 雷达数据归各自机构所有（莱比锡大学 / IAP Kühlungsborn、Sodankylä 地球物理观测站）。
