[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [ไทย](Experimental-Forecasts-th) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · **中文 (繁體)**

# 預報（實驗性）

*頁籤：預報計算 › 預報（實驗性）。*

[![預報（實驗性）](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

這個頁籤將 **Collm 雷達（36.2 MHz）** 的流星計數換算為**業餘頻段上每小時反射次數**的估計值（預設 144 MHz，可選 28 至 1300 MHz 的任意頻率），為您的路徑預報**未來 24 小時**，並可將估計值與 **RMOB** 觀測者的資料**比對**，例如一位在 143.050 MHz 上收聽 GRAVES 的觀測者。

> 這裡的一切都是**實驗性**的：頻率規則是一條經驗法則，而電台因子取決於您的電台。請用這些數字來比較不同的小時與日期，並在實際上線時加以驗證。

## 控制項

| 控制項 | 預設 | 作用 |
|---|---|---|
| **目標頻率 MHz** | 144 | 預報的頻率（28–1300 MHz） |
| **λ^k 指數** | 3 | 頻率規則的指數 k（SM6FHZ：3） |
| **電台因子 K** | 1 | 反映接收電台的條件（功率、天線）；透過與同一頻段的 RMOB 觀測者比較而得出 |
| **從磁碟載入 RMOB 檔案...** | | 讀取一個 RMOB 月份文字檔（見下文） |
| **由 RMOB 檔案推算指數** | | 根據 Collm 與 RMOB 的共同時數擬合 k |
| **RMOB 觀測者** | 空白 | 觀測者名稱，與檔名中的寫法相同（例如 `NAME_112026rmob.TXT` → `NAME`） |
| **立即下載 RMOB** | | 下載該觀測者當月的檔案一次 |
| **每 5 分鐘自動下載（僅在取得 RMOB 許可後啟用）** | **關閉** | 請參閱[RMOB 與自動化程式](#rmob-與自動化程式) |

控制項下方的橘色行會顯示代入目前數值後的規則，例如 *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*，以及持續時間的換算與該頻率的 IARU 最大 ping。

## 從雷達到業餘頻段

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**來源：** SM6FHZ，*"432 MHz Meteorscatter, Challenges and Techniques"*，第 45 屆 Nordic VUSHF，2025 年 5 月：反射的數量與強度隨 **λ³** 變化，持續時間隨 **λ²** 變化（432 MHz 比 144 MHz 低 14–15 dB，持續時間為其 1/9）。**驗證：** λ³ 的關係與 McKinley 的欠密餘跡方程式相同。取 k = 3 時，Collm 的 1000 流星/小時約相當於 **144 MHz 上 16 次反射/小時**；在 143.050 MHz 上收聽 GRAVES 的 RMOB 觀測者通常計數到 **20 至 140 次回波/小時**（RMOB 公報，2018 年 6 月）：數量級相符，差異即為電台因子 K。（手冊式 44–45。）

## 未來 24 小時

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**持續性：** 取前一天同一時刻的換算值（若缺少則取前兩天的），並依**路徑流星雨指數** I（Σ ZHR × 效率，請參閱[效率計算](Efficiency-Calculation-zh-tw#模型)）的變化加以修正。常數 10 代表偶發流星的背景，在指數很小時限制修正幅度。*程式的選擇（手冊式 47）。*

| 面板 | 內容 |
|---|---|
| **在 Collm 量測並換算至 f MHz - 昨天與今天（UTC）** | Collm 雷達的每小時流星數；換算值（橘色，右側刻度）；若已載入則顯示 RMOB 計數（綠色，右側刻度） |
| **… 在 f MHz 的未來 24 小時實驗性預報** | 預報的反射/小時（長條）以及路徑流星雨指數（右側刻度） |
| 表格 | UTC 時間 · Collm 同一小時 · 已換算 · 路徑流星雨指數 · 預報 /小時 · **評等** |

**評等：** 預報值至少為 24 小時平均值的 1.3 倍時為*良好*，0.8 倍以上為*普通*，低於此為*差*。同一預報也會出現在**實驗性預報**卡片與[效率計算](Efficiency-Calculation-zh-tw)的橘色列中，並且是 [GRAVES 雷達](GRAVES-Radar-zh-tw#預期回波實驗性)頁籤中預期回波的基礎。

## RMOB 比對

[RMOB](https://www.rmob.org)（Radio Meteor Observatories On Line，Pierre Terrier）匯集無線電觀測者的每小時流星計數；義大利有許多觀測者在 143.050 MHz 上收聽 GRAVES（威尼斯天文館、Faenza、Rovereto 等）。

**讀取 RMOB 檔案。** 接受兩種文字格式：

| 格式 | 樣式 | 說明 |
|---|---|---|
| 月份檔（Colorgramme / Spectrum Lab） | 每天一行，`day| n| n| …`，含 24 個每小時數值 | 常見的 `NAME_MMYYYYrmob.TXT` |
| 公報表格 | 表頭 ` UT |  1   2   3 …`，資料行 `0h|175 166 …` | 若檔案中有多位觀測者，會依序接連讀取：請使用只含一位觀測者的檔案 |

月份與年份取自檔名（`…_MMYYYYrmob…`）或表頭；否則使用目前月份（程式會加以說明）。

**擬合指數。** 取 K = 1，由共同時數（至少 3 小時）上 RMOB/Collm 比值的中位數求得：

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*程式的選擇（手冊式 46）。* 對話框會顯示共同時數、比值中位數與 k；**是** 套用 k（並設 K = 1），**否** 保持 k = 3：之後請將 K 手動調整為同一對話框中建議的數值。

## RMOB 與自動化程式

RMOB 要求**自動化程式不要抓取它的檔案**。因此**自動下載**在一開始是**關閉**的，並且**只有在徵得 RMOB 許可之後**才應啟用。即使沒有許可，您也隨時可以使用**從磁碟載入 RMOB 檔案...**，或在需要時按下**立即下載 RMOB**。

下載位址是 `config.ini` 中的一個範本（鍵值 `rmob_url`，預設 `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`，其中 `{NOME}` 是觀測者，`{MMAAAA}` 是月份與年份）；下載的檔案保存在 `data/radar/` 中。
