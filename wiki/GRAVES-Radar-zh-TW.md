[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-BR) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · **中文 (繁體)**

# GRAVES 雷達

*分頁：實況與即時資料 › GRAVES 雷達。*

[![GRAVES 雷達](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## GRAVES 是什麼

**GRAVES** 是一部法國雷達，在 **143.050 MHz 上發射連續波（CW）**，發射站位於 **Broye-lès-Pesmes**（47.348° N 5.515° E，網格座標 **JN27SI**，海拔約 200 m；Wikipedia）。位於 GRAVES 和您都能看到的區域中的流星餘跡會透過**前向散射**把它的訊號反射給您：您會在載波附近聽到短促的 *ping*。**RMOB** 的觀測者正是用這種方式在 143.050 MHz 上逐小時統計流星的；對您的 2 m 流星散射電台來說，它也是一個免費且始終在線的測試訊號。

本分頁把 **GRAVES → 本台**當作一條獨立的流星散射路徑：使用與主路徑相同的函式（相同的餘跡高度、波瓣仰角和熱點距離），計算流星雨效率、建議的 Hot 和 PREV 區域，然後檢查該區域是否**位於 GRAVES 波束內**，以及波束**何時**照射到它。

## 頂部列

| 控制項 | 作用 |
|---|---|
| **目前** | 將計算恢復為即時：日期設為今天，小時滑桿歸零（本分頁跟隨*計算日期*和*小時*）。 |
| **將 GRAVES 設為 DX** | 對方電台變為 GRAVES（JN27SI，高度 200 m），主路徑隨之重新計算：此後其他所有分頁都顯示 GRAVES 路徑。 |
| **波束序列** | *每步 0.8 s · 週期 4.8 s（PE1ITR 2021）*（預設）或 *每步 3.2 s · 週期 19.2 s（PE1ITR 2007）*。 |

## 四張卡片

| 卡片 | 內容 |
|---|---|
| **GRAVES 波束中的有效區域** | *是 · 扇區 X*，並列出從 GRAVES 看建議熱點的方位角和仰角以及步進（1–6）；或者 *否：在扇區外* / *否：在 GRAVES 地平線以下* / *否：高於波束（約 25°）* |
| **目前 GRAVES → 本台路徑的效率** | 路徑指數 Σ ZHR × 效率、最佳流星雨、主要的 A/B 側，以及 *預期回波 ≈ …/小時*（試驗性，見下文） |
| **路徑** | 到 GRAVES 的距離；天線朝向建議 Hot 的方位和仰角；GRAVES 直射方位 |
| **波束下次掃過該區域** | *目前 · 剩餘 … s* 或 *… s 後*，步進（例如 *B4*），接下來的三個時刻（以分鐘內的秒數表示）以及能捕捉到的餘跡比例 |

如果此刻沒有有用的流星雨，程式會顯示**最適合該波束**的熱點（位於扇區內、最靠近正南方向），並加以說明。

## 從 GRAVES 看到的天空

根據 PE1ITR 和 Bolidozor wiki 的資料，**四個相位陣列**涵蓋方位 **90° 至 270°** 的南方天空，分為四個 **45° 扇區**：

| 扇區 | 從 GRAVES 看的方位 |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

每個扇區分為 **6 個 7.5° 的步進**，從方位最小的一端起編號 1 至 6，依序點亮，**四個扇區同時進行**。波束在**仰角方向寬約 25°**：在餘跡高度上，它涵蓋兩個虛線圓（*波束地平線*）之間的彩色環帶。圖中：橘色/粉紅色點 = GRAVES → 本台路徑的 PREV 區域，綠線 = 本台方向，紅線 = 從本台到建議熱點；目前點亮的步進會被突顯。

## 時間線重建

*時間線重建 · 日期 UTC*（與 24 h 表格同一天）：對每個小時列出 GRAVES → 本台路徑的效率、最有利的流星雨以及有效視窗（*hh:00 → hh:00 UTC · n h*），並標出最大值（*最大 Σ …，hh:30*）和紅色的*目前*標記。下方是**接下來幾秒的細節**：扇區的六個步進、照射到有效區域的步進，以及*可能有回波（餘跡 +0.3 s）*。

### 波束時序

序列與 **UTC** 綁定（PE1ITR）：目前點亮的步進由自 00:00 UTC 起的秒數對週期取模計算得出（86 400 s 同時是 4.8 s 和 19.2 s 的整數倍）。指揮站有時會把序列平移幾個步進，因此這些細節是**需要透過收聽來確認的預測**。黃色標籤**電腦時鐘已同步**提醒您：請將電腦與 NTP 伺服器同步（誤差最多零點幾秒）。

### 偵測因子

只有當餘跡存在期間被波束照射到時，才能聽到它：

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0.3 s 是 143 MHz 上欠密餘跡的典型持續時間——這是一個固定值，屬於*程式的選擇*（SM6FHZ 的 λ² 規則可在頻段之間換算持續時間，但不提供起始值）。

### 預期回波（試驗性）

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

[試驗性預報](Experimental-Forecasts-zh-TW)中的預報（已包含電台因子 K）用 SM6FHZ 規則（相同的指數 k）從其頻率 f_fc 換算到 143.050 MHz，再用兩條路徑流星雨指數之比加以修正（常數 10 代表偶發流星背景，與預報中相同），最後乘以偵測因子。僅供參考：請與 RMOB 觀測者的資料比較。

## 如何收聽 GRAVES 的 ping

| 步驟 | 操作方法 |
|---|---|
| 接收機 | **USB 143.049 MHz**（約 1 kHz 音調）或 143.050 MHz，**AGC 設為慢速或關閉**，音訊頻寬**至少 2.4 kHz** |
| 天線 | 朝向 GRAVES → 本台路徑的**建議熱點**（*路徑*卡片），採用**低仰角** |
| 瀑布圖 | ping 是**靠近載波的短線**；長時間（過密）餘跡較寬，並顯示都卜勒頻移 |
| 計數 | RMOB 使用 GRAVES 做逐時流星計數：**將您的 ping 與 143.050 MHz 上的觀測者進行比較**（[試驗性預報](Experimental-Forecasts-zh-TW#rmob-比較)） |

## 來源

1. Rob Hardenberg **PE1ITR**，*"The 143.050 MHz Graves Radar, a VHF Beacon"*（DUBUS 4/2007）及 *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki，"Graves" – 天線陣列、扇區和波束時序
3. **Wikipedia**，"GRAVES (system)" – 位於 Broye-lès-Pesmes 的發射站（47.348° N 5.515° E）
4. **RMOB** – 143.050 MHz 上的觀測者（[rmob.org](https://www.rmob.org)）
5. IC8TEM 的 **YAEC** – GRAVES Radar 分頁（本分頁由其原型演變而來）
