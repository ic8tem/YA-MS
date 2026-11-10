[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · **中文 (繁體)**

# 雷達流量

*分頁：實況與即時資料 › 雷達流量。*

[![雷達流量](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

本分頁顯示專業流星雷達**此刻**的統計結果：來自 **Collm** SKiYMET 雷達（德國萊比錫大學 / IAP Kühlungsborn，36.2 MHz）的逐時流星計數和餘跡高度，以及 **Sodankylä** 雷達（SGO，芬蘭）的最新影像。Collm 的計數用於您所用頻段上的估算以及[試驗性預報](Experimental-Forecasts-zh-tw)；測得的餘跡高度則用於全部幾何計算。

## 控制項

| 控制項 | 作用 |
|---|---|
| **立即下載** | 立即檢查所有外部資料來源。 |
| **每 5 分鐘自動更新所有資料來源** | 預設開啟。每 5 分鐘檢查一次所有資料來源，**只重新下載有變化的**（*未變化（… UTC 檢查）* / *… UTC 有新資料*）。 |
| **λ 指數（SM6FHZ）** | 頻率規則的指數 k，預設 3（1–4）。 |

## 顯示內容

| 面板 | 內容 |
|---|---|
| **流星數/小時 - 昨天和今天（UTC）** | 青色長條 = Collm 計數（有效），紅色長條 = 已捨棄，橘色粗線 = 右側刻度上的 *… MHz 估算* |
| **餘跡高度（Collm）** | 70 至 110 km 之間每 km 高度的流星數，附最常見高度（眾數）、平均值、中位數和標準差 |
| Collm 影像 | 下載得到的原始 SKiYMET 圖表 |
| Sodankylä 影像 | Sodankylä 雷達最新的流星計數影像（僅顯示；不讀取其格式） |

圖表上方的一行說明 Collm 圖表的讀取時間以及辨識出的縱軸刻度（*從圖表讀取的刻度：0-… 流星/小時*）。

## 如何讀取 Collm 圖表

Collm 圖表（720 × 720 像素，純色）的座標軸位置固定，但雷達**每天都會根據實測值調整縱軸刻度**（例如 2026 年 11 月 5 日為 0–1.2·10³，11 月 6 日為 0–1.0·10³，刻度線位置也隨之移動）。因此 YA-MS：

1. 找出座標軸上的長刻度線；
2. 將每個字元與圖表的點陣字型比較，**讀出**最高刻度和零點的**標籤**；
3. 對每個小時 i（0–47，昨天和今天）取中心欄，從上往下找到第一個青色像素 y：

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top 和 y0 分別是最高刻度和零點所在的列，N_top 是從最高標籤讀出的值（×1000）。解析度：每像素約 7–8 流星/小時。*程式的選擇（手冊公式 42）。*

如果某個標籤無法讀取，程式退回到 2026 年 11 月 5 日的校準值（**已校準刻度 0-1200 流星/小時**），並以橘色提示：*無法讀取流量縱軸刻度（頂部標籤：…）：數值需核實。* 如果圖表格式本身發生變化（*圖表格式已變化（…x…）：無法讀取* 或 *未在預期位置找到流量座標軸*），就必須重新校準讀取方式：請回報此問題（請參閱[參與貢獻](Contributing-and-Contacts-zh-tw)）。

### 餘跡高度

由高度直方圖（第 k km 中有 n_k 顆流星，平均高度 h_k）得到：

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*手冊公式 43。* 勾選**來自雷達**（控制項第 2 列）時，**眾數**即作為所有計算中的餘跡高度。驗證：2026 年 11 月 5 日的圖表——眾數 89.5 km，平均 88.6 km，標準差 6.8 km，與 Cerrotta–Sartori 文章中約 90 km（SKiYMET 平均值）相符。

如果高度圖表的刻度發生變化，程式會提示：*高度統計（眾數、平均值、中位數）仍然有效，絕對計數則不再有效。*

## 您所用頻段上的估算

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

**SM6FHZ** 的經驗規則（VUSHF 2025）：反射的數量和強度依 λ³ 縮放，持續時間依 λ² 縮放（在 McKinley 中 λ³ 是單條餘跡的功率；餘跡數量約依 λ^1.5 縮放，在前向散射中持續時間還隨 sec²φ 增長：請參閱[試驗性預報](Experimental-Forecasts-zh-tw)）。同時顯示 IARU 第一區的最大 ping 持續時間（50 MHz 為 1000 ms，70 MHz 為 500 ms，144 MHz 為 100 ms，432 MHz 為 13 ms）。這些數值僅供參考，應與實際上線經驗比較。電台因子 K 以及與 RMOB 的比較見[試驗性預報](Experimental-Forecasts-zh-tw)。

## 離線

如果所有資料來源都無法存取，程式會**只顯示一次**訊息：*無網際網路連線。雷達和 RMOB 資料無法更新：程式使用最後儲存的資料，並每 5 分鐘自動重試。* 底部狀態列變為紅色（*無網際網路連線 …*），直到連線恢復（*連線已恢復。*）。

## 檔案庫與資料來源

| 檔案（位於 `data/`） | 內容 |
|---|---|
| `flusso_collm.csv` | 從 Collm 讀取的流量逐時檔案庫（已存在的小時會被更新） |
| `quote_collm.csv` | 餘跡高度檔案庫 |
| `radar/` | 最新下載的影像（以及 RMOB 檔案） |
| `fonti_radar.csv` | 雷達資料來源網址，`attivo=1/0` 用於啟用/停用各個資料來源 |

| 資料來源 | 頻率 | 說明 |
|---|---|---|
| Collm 流星雷達，萊比錫大學（LIM）和 IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | 每小時第 10 分鐘（UTC）更新；昨天 + 今天的流量、高度分布 |
| Sodankylä 地球物理觀測站 – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | 僅影像（雷達正在升級，DECC 計畫） |
| swan.ms（Collm 的副本） | 36.2 MHz | 預設停用；僅在獲得 DL1DBC 許可後使用 |

> 雷達資料歸各自機構所有（萊比錫大學 / IAP Kühlungsborn、Sodankylä 地球物理觀測站）。
