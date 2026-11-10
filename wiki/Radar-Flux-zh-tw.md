[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [ไทย](Radar-Flux-th) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · **中文 (繁體)**

# 雷達通量

*頁籤：Live 與即時資料 › 雷達通量。*

[![雷達通量](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

這個頁籤顯示專業流星雷達**此刻**的計數結果：來自 **Collm** SKiYMET 雷達（德國萊比錫大學 / IAP Kühlungsborn，36.2 MHz）的每小時流星計數與餘跡高度，以及 **Sodankylä** 雷達（SGO，芬蘭）的最新影像。Collm 的計數用於您所用頻段的估計值以及[預報（實驗性）](Experimental-Forecasts-zh-tw)；量測到的餘跡高度則用於整個幾何計算。

## 控制項

| 控制項 | 作用 |
|---|---|
| **立即下載** | 立即檢查所有外部資料來源。 |
| **每 5 分鐘自動更新所有資料來源** | 預設開啟。每 5 分鐘檢查一次所有資料來源，**只重新下載有變更的**（*無變化（於 … UTC 檢查）* / *… UTC 有新資料*）。 |
| **λ 指數（SM6FHZ）** | 頻率規則的指數 k，預設 3（1–4）。 |

## 顯示內容

| 面板 | 內容 |
|---|---|
| **每小時流星數 - 昨天與今天（UTC）** | 青色長條 = Collm 計數（有效），紅色長條 = 已捨棄，橘色粗線 = 右側刻度上的 *… MHz 估計值* |
| **餘跡高度（Collm）** | 70 至 110 km 之間每 km 高度的流星數，附最常見高度（眾數）、平均數、中位數與標準差 |
| Collm 影像 | 下載得到的原始 SKiYMET 圖表 |
| Sodankylä 影像 | Sodankylä 雷達最新的流星計數影像（僅顯示；不讀取其格式） |

圖表上方的一行說明 Collm 圖表的讀取時間，以及找到的垂直刻度（*從圖表讀取的刻度：0-… 流星/小時*）。

## 如何讀取 Collm 圖表

Collm 圖表（720 × 720 像素，純色）的座標軸位置固定，但雷達**每天都會依實測值調整垂直刻度**（例如 2026 年 11 月 5 日為 0–1.2·10³，11 月 6 日為 0–1.0·10³，刻度線的位置也跟著移動）。因此 YA-MS 會：

1. 找出座標軸上的長刻度線；
2. 將每個字元與圖表的點陣字型比對，**讀出**最高刻度與零點的**標籤**；
3. 對每個小時 i（0–47，昨天與今天）取中心那一欄，由上往下找到第一個青色像素 y：

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top 與 y0 分別是最高刻度與零點所在的像素列，N_top 是從最高標籤讀出的值（×1000）。解析度：每像素約 7–8 流星/小時。*程式的選擇（手冊式 42）。*

如果某個標籤無法讀取，程式會改用 2026 年 11 月 5 日的校準值（**校準刻度 0-1200 流星/小時**），並以橘色提示：*無法讀取通量的垂直刻度（頂端標籤：…）：數值需要核對。* 如果圖表格式本身變更了（*圖表格式已變更（…x…）：無法讀取* 或 *在預期位置找不到通量圖的座標軸。*），就必須重新校準讀取方式：請回報此問題（請參閱[參與貢獻](Contributing-and-Contacts-zh-tw)）。

### 餘跡高度

由高度直方圖（第 k 個 km 中有 n_k 顆流星，平均高度 h_k）得到：

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*手冊式 43。* 勾選**來自雷達**（控制項第 2 列）時，**眾數**就成為所有計算所用的餘跡高度。驗證：2026 年 11 月 5 日的圖表：眾數 89.5 km，平均 88.6 km，標準差 6.8 km，證實了 Cerrotta–Sartori 文章中約 90 km 的數值（SKiYMET 平均值）。

如果高度圖的刻度變更，程式會提示：*高度統計（眾數、平均數、中位數）仍然有效，絕對計數則否。*

## 您所用頻段的估計值

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ** 的經驗法則（VUSHF 2025）：反射的數量與強度隨 λ³ 變化，持續時間隨 λ² 變化；λ³ 的關係與 McKinley 的欠密餘跡方程式相同。同時也顯示 IARU 第一區的最大 ping 持續時間（50 MHz 為 1000 ms，70 MHz 為 500 ms，144 MHz 為 100 ms，432 MHz 為 13 ms）。這些數值僅供參考，應與實際上線的經驗比較。電台因子 K 與 RMOB 比對請見[預報（實驗性）](Experimental-Forecasts-zh-tw)。

## 離線

如果所有資料來源都無法連線，會**只出現一次**訊息：*無網際網路連線。雷達與 RMOB 資料無法更新：程式使用最後儲存的資料，並每 5 分鐘自動重試。* 底部的狀態列會變成紅色（*無網際網路連線 …*），直到連線恢復（*連線已恢復。*）。

## 封存檔與資料來源

| 檔案（位於 `data/`） | 內容 |
|---|---|
| `flusso_collm.csv` | 從 Collm 讀取之通量的每小時封存檔（已存在的小時會被更新） |
| `quote_collm.csv` | 餘跡高度的封存檔 |
| `radar/` | 最新下載的影像（以及 RMOB 檔案） |
| `fonti_radar.csv` | 雷達資料來源的位址，以 `attivo=1/0` 個別啟用/停用 |

| 資料來源 | 頻率 | 說明 |
|---|---|---|
| Collm 流星雷達，萊比錫大學（LIM）與 IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | 每小時第 10 分鐘（UTC）更新；昨天 + 今天的通量、高度分布 |
| Sodankylä 地球物理觀測站 – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | 僅有影像（雷達更新中，DECC 計畫） |
| swan.ms（Collm 的副本） | 36.2 MHz | 預設停用；僅在取得 DL1DBC 同意後使用 |

> 雷達資料屬於其所屬機構（萊比錫大學 / IAP Kühlungsborn、Sodankylä 地球物理觀測站）。
