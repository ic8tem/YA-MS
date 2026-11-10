[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [ไทย](Grid-Square-Map-th) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · **中文** · [中文 (繁體)](Grid-Square-Map-zh-tw)

# 方格地图

*选项卡：方格地图。*

[![方格地图](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

从您日志的 ADIF 文件中读取已**通联**和已**确认**的 Maidenhead 方格（4 位），显示在欧洲地图上——**每个频段一个子选项卡：50、70、144、222 和 432 MHz**。

## 控件

| 控件 | 作用 |
|---|---|
| **载入 ADIF 文件...** | 读取 `.adi` / `.adif` 文件。新的 ADIF 会**替换**之前的数据。 |
| **清除内存** | 删除所有从 ADIF 载入的方格（会要求确认）。 |
| 鼠标 | **滚轮 = 缩放，拖动 = 平移，鼠标悬停在方格上 = 显示 QSO**（最多六个呼号及日期，已确认的标注*（已确认）*） |

载入后，状态栏显示 *读取了 … 个 QSO，50-432 MHz 频段内有 … 个 QSO 方格，舍弃了 … 个 QSO（其他频段或无方格）*。每个频段的地图都有说明 *已通联 … 个方格，已确认 … 个*。

| 颜色 | 含义 |
|---|---|
| 橙色 | 已通联 |
| 绿色 | 已确认（QSL 或 LoTW） |

## 如何读取 ADIF

- 使用的字段：`CALL`、`GRIDSQUARE`、`VUCC_GRIDS`、`BAND`、`FREQ`、`QSO_DATE`、`QSL_RCVD`、`LOTW_QSL_RCVD`（ADIF 规范）。
- 频段取自 `BAND`，或由频率推断：50–54 MHz = 6 m，69.9–71.5 MHz = 4 m，144–148 MHz = 2 m，219–225 MHz = 1.25 m，420–450 MHz = 70 cm。
- 如果某方格中至少有一个 QSO 的 `QSL_RCVD = Y` 或 `LOTW_QSL_RCVD = Y`，该方格即为**已确认**。
- 方格保存在 `data/adif_quadrati.csv` 中，直到您载入另一个文件或点击**清除内存**。

YA-MS **不会**连接 LoTW：请从您的日志程序（或从 LoTW）导出 ADIF，然后在这里载入。
