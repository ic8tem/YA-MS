[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-BR) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · **中文 (繁體)**

# 試驗性預報

*分頁：預報計算 › 試驗性預報。*

[![試驗性預報](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

本分頁將 **Collm 雷達（36.2 MHz）**的流星計數換算為**業餘頻段上每小時反射次數**的估算值（預設 144 MHz，可選 28 至 1300 MHz 的任意頻率），為您的路徑預報**未來 24 小時**，並可將估算值與 **RMOB** 觀測者的資料進行**比較**——例如一位在 143.050 MHz 上收聽 GRAVES 的觀測者。

> 這裡的一切都是**試驗性**的：頻率規則是一條經驗規則，電台因子取決於您的電台。請用這些數字來比較不同的小時和日期，並在實際通聯中加以檢驗。

## 控制項

| 控制項 | 預設 | 作用 |
|---|---|---|
| **目標頻率 MHz** | 144 | 預報的頻率（28–1300 MHz） |
| **λ^k 指數** | 3 | 頻率規則的指數 k（SM6FHZ：3） |
| **電台因子 K** | 1 | 反映接收電台的情況（功率、天線）；透過與同一頻段上的 RMOB 觀測者比較得出 |
| **從磁碟載入 RMOB 檔案...** | | 讀取一個 RMOB 月度文字檔（見下文） |
| **由 RMOB 檔案推算指數** | | 根據 Collm 和 RMOB 的共同小時擬合 k |
| **RMOB 觀測者** | 空白 | 觀測者名稱，與檔名中的寫法一致（例如 `NAME_112026rmob.TXT` → `NAME`） |
| **立即下載 RMOB** | | 下載該觀測者當月的檔案一次 |
| **每 5 分鐘自動下載（僅在獲得 RMOB 許可後啟用）** | **關閉** | 請參閱[RMOB 與自動程式](#rmob-與自動程式) |

控制項下方的橘色列顯示代入目前數值後的規則，例如 *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*，以及持續時間的換算和該頻率下的 IARU 最大 ping。

## 從雷達到業餘頻段

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**來源：** SM6FHZ，*"432 MHz Meteorscatter, Challenges and Techniques"*，第 45 屆 Nordic VUSHF，2025 年 5 月——反射的數量和強度依 **λ³** 縮放，持續時間依 **λ²** 縮放（432 MHz 比 144 MHz 低 14–15 dB，持續時間為其 1/9）。**驗證：** 在 McKinley 方程式中，λ³ 是單條欠密餘跡的功率，而不是餘跡的數量；質量指數為 2 時，高於固定閾值的餘跡數量約依 λ^1.5 縮放（IZ5TEK；OH5IY）。程式保留 SM6FHZ 的經驗規則 k = 3，並加以說明；適合您電台的 k 來自與 RMOB 的比較。在前向散射中，持續時間還隨 sec²φ 增長（McKinley；OH5IY）：Collm 以後向散射（φ = 0）量測，因此預報乘以路徑中點處的 sec²φ（60° 時 ×4，70° 時 ×8.5，80° 時 ×33）。取 k = 3 時，Collm 的 1000 流星/小時約相當於 **144 MHz 上 16 次反射/小時**；在 143.050 MHz 上收聽 GRAVES 的 RMOB 觀測者通常統計到 **20 至 140 次回波/小時**（RMOB 公報，2018 年 6 月）：數量級相符，差異即為電台因子 K。（手冊公式 44–45。）

## 未來 24 小時

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**持續性：** 取前一天同一時刻的換算值（若缺少則取前兩天的），並依**路徑流星雨指數** I（Σ ZHR × 效率，請參閱[效率計算](Efficiency-Calculation-zh-TW#模型)）的變化加以修正。常數 10 代表偶發流星背景，在指數很小時限制修正幅度。*程式的選擇（手冊公式 47）。*

| 面板 | 內容 |
|---|---|
| **在 Collm 測得並換算至 f MHz - 昨天和今天（UTC）** | Collm 雷達流星數/小時；換算值（橘色，右側刻度）；如已載入則顯示 RMOB 計數（綠色，右側刻度） |
| **… 未來 24 小時 f MHz 試驗性預報** | 預報的反射次數/小時（長條）以及路徑流星雨指數（右側刻度） |
| 表格 | UTC 時間 · Collm 同一時刻 · 換算 · 路徑流星雨指數 · 預報 /小時 · **評價** |

**評價：** 預報值至少為 24 小時平均值的 1.3 倍時為*良好*，0.8 倍起為*普通*，低於此為*差*。同一預報也出現在**試驗性預報**卡片和[效率計算](Efficiency-Calculation-zh-TW)的橘色列中，並且是 [GRAVES 雷達](GRAVES-Radar-zh-TW#預期回波試驗性)分頁中預期回波的基礎。

## RMOB 比較

[RMOB](https://www.rmob.org)（Radio Meteor Observatories On Line，Pierre Terrier）彙集無線電觀測者的逐時流星計數；義大利有許多觀測者在 143.050 MHz 上收聽 GRAVES（威尼斯天文館、Faenza、Rovereto 等）。

**讀取 RMOB 檔案。** 接受兩種文字格式：

| 格式 | 樣式 | 說明 |
|---|---|---|
| 月度檔案（Colorgramme / Spectrum Lab） | 每天一行，`day| n| n| …`，含 24 個逐時數值 | 常見的 `NAME_MMYYYYrmob.TXT` |
| 公報表格 | 表頭 ` UT |  1   2   3 …`，資料行 `0h|175 166 …` | 如果檔案中有多位觀測者，會依序讀取：請使用只含一位觀測者的檔案 |

月份和年份取自檔名（`…_MMYYYYrmob…`）或表頭；否則使用目前月份（程式會加以說明）。

**擬合指數。** 取 K = 1，由共同小時（至少 3 個）上 RMOB/Collm 比值的中位數求得：

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*程式的選擇（手冊公式 46）。* 對話框顯示共同小時、比值中位數和 k；**是** 採用 k（並設 K = 1），**否** 保持 k = 3——之後請將 K 手動調整為同一對話框中建議的值。

## RMOB 與自動程式

RMOB 要求**自動程式不要抓取其檔案**。因此**自動下載**在初始時是**關閉**的，並且**只有在徵得 RMOB 許可之後**才應啟用。即使沒有許可，您也隨時可以使用**從磁碟載入 RMOB 檔案...**，或在需要時點選**立即下載 RMOB**。

下載網址是 `config.ini` 中的一個範本（鍵 `rmob_url`，預設 `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`，其中 `{NOME}` 是觀測者，`{MMAAAA}` 是月份和年份）；下載的檔案儲存在 `data/radar/` 中。
