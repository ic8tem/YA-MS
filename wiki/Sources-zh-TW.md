**English** · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh)

# 來源

*分頁：技術文件 › 來源。*

[![來源](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

**來源**分頁列出 YA-MS 所依據的全部著作，依下列分組排列（文字可選取，方便複製參考文獻）。同樣的來源也依編號列在計算手冊（`doc/YA-MS_manuale_calcoli.docx`）和[效率 - 說明](Efficiency-Explanation-zh-TW)文件的末尾。

## 主要來源

| 來源 | 用於 |
|---|---|
| Costantino Cerrotta **IC8TEM**、Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"*（義大利文文章，第 7 版） | E 層中約 90 km 高度的餘跡（SKiYMET 雷達）、地球半徑 6372.7955 km、仰角公式、Hot A / Hot B、10–30° 側向散射、路徑損耗、最小訊號 −130 dBm、IARU ping 持續時間、06 UTC 的偶發流星峰值 |

## 效率的計算與理論

| 來源 | 用於 |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft，www.kolumbus.fi/oh5iy（歷史網站） | 流星雨效率的概念；200 dB 平均路徑損耗 |
| Wilhelm Rauh **DL5MCG** – MCG_MS，MS Efficiency Calculator v1.61，qsl.net/dl5mcg | 四個固定方向上的效率（對比） |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*，第 45 屆 Nordic VUSHF，2025 年 5 月 | λ³ 和 λ² 規則、中點、最佳方向（輻射點方位 ±90°） |
| D.W.R. **McKinley** – *Meteor Science and Engineering*，McGraw-Hill，1961 | 鏡面反射、欠密餘跡方程式 |
| John **GM8JBJ** – Meteor scatter path loss，hamradio.engineering（引自 Kaiser & Closs 1952） | John Worsnop **G4BAO** 計算的 172–190 dB 路徑損耗（博士論文），與路徑同向的餘跡約少 6 dB；不使用該頁面自身的 182 dB 表（請參閱[幾何與路徑損耗](Geometry-and-Path-Loss-zh-TW)） |
| Shelby **W8WN** – qsl.net/w8wn/hscw（AMS Bulletin 203 偏角表） | 最佳仰角和偏角、50–150 km 的熱點 |
| **LZ2HV** – MSHV | Hot A / Hot B（對比；見手冊） |
| Klaus von der Heide **DJ5HG** – QTFGUI 及其 "QTFGUI Help" 手冊（2007） | 錐面散射定律；用於驗證模型的漢堡 – 巴塞隆納象限儀座流星雨測試案例 |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*，DARC 會議，2018 年 1 月 | **DH9GCD** 的最佳方向公式；DJ5HG 的錐面散射及 HOT-A / HOT-B 選擇；有效輻射點高度 20–70°；最佳距離 1300–1500 km；KB0VUK 的偶發流星 |
| Günter Hoch **DL6WU** – 長八木天線增益與橫桿長度的關係，由 W8IO 轉述（w8io.com） | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*，McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*；*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*；*70-CM Yagi Stacks Part 2*（David Tanner 的 VK3AUU 八木） | 用於驗證增益曲線和修正水平波瓣（0.93 × Kraus）的 NEC 模擬 |
| John Drew **VK5DJ** – Yagi Calculator | VK3AUU、WA2PHW 和 DJ9BV 型號的增益估算 |
| J. **Meeus** – *Astronomical Algorithms*，第 2 版，Willmann-Bell，1998 | 儒略日、恆星時、太陽黃經、方位角/仰角（見手冊） |

## 流星雨資料

| 來源 | 用於 |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026（及 2027），www.imo.net，表 5、6 和 7 | 輻射點、λ max、v、r、ZHR、反日點源、峰值日期和時間 |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | 流星雨資料 |

## 即時雷達資料

| 來源 | 用於 |
|---|---|
| Collm 流星雷達，萊比錫大學（LIM）和 IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 逐時流星流量和餘跡高度（[雷達流量](Radar-Flux-zh-TW)） |
| Sodankylä 地球物理觀測站 – sgo.fi/Data/RealTime/meteorRadar.php | 流星計數影像 |
| DL1DBC – Swan Meteor Skyview，swan.ms | 天穹圖形的參考 |
| SM6FHZ – RadiantCalc | 帶最佳方向的極座標圖 |
| Natural Earth – 1:5000 萬海岸線和國界，公有領域，www.naturalearthdata.com | 歐洲地圖 |
| RMOB，Radio Meteor Observatories On Line（Pierre Terrier）– www.rmob.org；月度公報 rmob.org/rmobtext | 用於比較的 GRAVES 143.050 MHz 觀測者（威尼斯天文館、Faenza、Rovereto 等） |

## GRAVES 雷達

| 來源 | 用於 |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"*（DUBUS 4/2007）及 *"Graves Radar Update April 2021"* – pe1itr.com/graves | 扇區、步進、0.8 s / 3.2 s 步進時序 |
| Bolidozor wiki，"Graves" | 天線陣列、扇區和波束時序 |
| Wikipedia，"GRAVES (system)" | 位於 Broye-lès-Pesmes 的發射站（47.348° N 5.515° E） |

請參閱 [GRAVES 雷達](GRAVES-Radar-zh-TW)。

## 文章的其他參考文獻

G3WZT、DH8BQA、geekshed.co.uk、WSJT-X 手冊、WB2FKO（ping）、IU6GIR（143.050 MHz 活動）、IARU 第一區 VHF Handbook。

## 常數及其來源

`data/regole_sperimentali.csv` 列出了程式使用的常數和規則，每項都註明來源（典型餘跡高度、高度範圍、地球半徑、λ³ / λ² 規則、IARU ping 持續時間、路徑損耗、最小訊號、參考 EIRP、偶發流星峰值、432 MHz 的有效距離、最佳方向、432 MHz 的最大有效輻射點仰角、側向散射）。

> 雷達資料歸各自機構所有。在散布的程式中自動取得這些資料之前，必須先申請許可。
