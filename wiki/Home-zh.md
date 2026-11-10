[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · **中文**

# YA-MS – 流星散射预报与流星雨效率实时计算

*作者：Costantino Cerrotta IC8TEM*

**YA-MS** 是一款面向业余无线电爱好者的免费程序，适用于在 **50、70、144、222 和 432 MHz 上进行流星散射（MS）通信**的电台。针对您的网格坐标与对方电台网格坐标之间的实际路径，程序逐小时计算每个活跃流星雨对该路径的帮助程度（即其**效率**）、反射来自路径的哪一侧（**Hot A / Hot B**）、天线应指向何处，并根据**实时流星雷达**（德国 Collm）给出每小时反射次数的试验性预报。程序可在 **Windows、Linux 和 macOS**（.NET 8 + Avalonia）上运行，界面提供 6 种语言。

主要来源是 **C. Cerrotta IC8TEM 与 G. Sartori IV3GTH** 的文章 *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"*（第 7 版）。程序中的每个公式和数据都注明了出处，参见[来源](Sources-zh)。

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="天穹"></a><br><sub>天穹</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="效率计算"></a><br><sub>效率计算</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES 雷达"></a><br><sub>GRAVES 雷达</sub></td>
</tr></table>

## 适用对象

- 想知道流星散射路径**何时**开通、天线该指向**何处**的操作者，而不满足于笼统的“今晚流星雨达到峰值”。
- 在 **144 和 432 MHz 上进行远距离通联**的电台：辐射点的位置决定了一个流星雨是有用还是无用。
- 希望**核对数字**的人：计算手册和程序内的说明给出了每一步及其出处——已发表的来源、对程序所做的验证，或程序自己的选择。

## 选项卡

自 1.6 版起，主选项卡下设有**子选项卡**（主选项卡下方颜色较浅的一行）。启动时会显示 5 秒钟的启动画面：ESO 的 VLT 上空的英仙座流星雨（照片 ESO/S. Guisard，CC BY 4.0）。

| 选项卡 | 子选项卡 | 显示内容 |
|---|---|---|
| **实况与实时数据** | [实时通信](Live-Traffic-zh) | 所有已收集 MS 通信的方位等距地图，每个通联都绘出最可能余迹所在的“云团”，按频段着色，新 spot 闪烁 |
| | [雷达流量](Radar-Flux-zh) | 从 Collm SKiYMET 雷达读取的逐时流星计数和余迹高度、Sodankylä 图像、您所用频段上的估算值 |
| | [GRAVES 雷达](GRAVES-Radar-zh) | GRAVES → 本台的前向散射路径：波束中的有效区域、扇区和步进、波束下次扫过的时间、收听方法 |
| | [数据收集](Data-Collection-zh) | 三路 telnet cluster 数据流（DX cluster、RBN、DM4X/PSKReporter）以及 MS spot 过滤器 |
| **预报计算** | [预报计算](Sky-View-zh) | 路径平面图，含 Hot A / Hot B、天线波瓣、PREV 区域和流星雨移动轨迹；流星雨列表；带辐射点和正确天线方向的小天穹；从天线看出去的剖面 |
| | [几何与路径损耗](Geometry-and-Path-Loss-zh) | 距离、中点、仰角、Hot A / Hot B、公共区域边界、28–432 MHz 路径损耗、链路预算、天线 |
| | [效率计算](Efficiency-Calculation-zh) | 概览卡片、各流星雨的逐时效率及 A/B 侧、路径指数、DH9GCD 对比、图表 |
| | [试验性预报](Experimental-Forecasts-zh) | 用 λ^k 和电台因子 K 将 Collm 流量换算到 144 MHz（或任意频率）、24 小时预报、与 RMOB 对比 |
| **技术文档** | [来源](Sources-zh) | 全部来源；主要来源是 Cerrotta–Sartori 的文章 |
| | [欧洲雷达地图](European-Radar-Map-zh) | Collm、Sodankylä、GRAVES 和 CMOR 相对于本台的位置 |
| | [效率 - 说明](Efficiency-Explanation-zh) | 逐步说明效率如何计算的文档，可导出为 Word |
| [实时流星雨](Live-Showers-zh) | – | Global Meteor Network 实测的 ZHR 和 CMOR 辐射点地图 |
| [流星雨](Showers-zh) | – | IMO 目录及下一个峰值（IMO 日期和时间或计算值） |
| [方格地图](Grid-Square-Map-zh) | – | 根据 ADIF 文件显示已通联和已确认的 Maidenhead 方格，每个频段一个选项卡 |

选项卡上方有三行控件（本台网格坐标、对方电台、频段、天线、余迹高度、时间），参见[入门](Getting-Started-zh)。**控制**按钮可将其折叠；界面语言和配色方案在右上角选择，参见[设置与数据文件夹](Settings-and-Data-Folder-zh)。

## 简要特点

- **实际路径，而非固定方向**：效率针对两个网格坐标之间的大圆路径计算（早期程序只使用四个固定方向）。
- **镜面反射模型**（McKinley），在 E 层上每 15 km 取一个点，余迹高度实时读取自 Collm 雷达。
- **Hot A / Hot B** 位于中点两侧 150 km（可在 30–400 km 之间调整），推荐的一侧以红色标示，已落在天线波瓣内的以灰色标示。
- **实时雷达**：每 5 分钟检查一次 Collm，只重新下载有变化的数据源；离线时程序使用最后保存的数据继续工作。
- 基于 SM6FHZ 的 λ³ 规则给出 50/144/432 MHz 的**试验性**预报，可与 RMOB 观测者的数据比较。
- 所有内容都在程序旁的一个 **`data`** 文件夹中：不使用 AppData，不使用系统文件夹。

> 效率是一个试验性模型（镜面反射 + 欠密余迹）。请将其与 MCG_MS、MS-Soft 以及您自己的上机经验进行比较。

## 从哪里开始

1. [安装](Installation-zh)
2. [入门](Getting-Started-zh)
3. 如果有问题，请参阅[故障排除与常见问题](Troubleshooting-FAQ-zh)。

下载：GitHub 上的 **[Releases](https://github.com/ic8tem/YA-MS/releases)**。
