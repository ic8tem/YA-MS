[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · **中文 (繁體)**

# 效率計算

*頁籤：預報計算 › 效率計算。*

[![效率計算](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

一個流星雨的**效率**以百分比表示其輻射點的位置在多大程度上允許在**您的**路徑上產生反射。這個概念由 Ilkka **OH5IY**（MS-Soft）提出，並為 Cerrotta–Sartori 的文章所採用：效率峰值與目視峰值（ZHR）並不一致，因為它取決於輻射點相對於兩個電台的位置。DL5MCG 的 MCG_MS 將同樣的構想套用於四個固定方向；YA-MS 則針對兩個網格座標之間的**實際路徑**進行計算。

這個頁籤會依 *24 h 表格的日期（UTC）* 中所選的日期，逐小時顯示效率（數值取每小時的半點）。

## 概覽卡片

| 卡片 | 內容 |
|---|---|
| **一天中的最佳時段** | 路徑指數最高的小時、該指數以及主要側（A/B 及其百分比） |
| **最有利的流星雨** | 當天 ZHR × 效率最大的流星雨、其效率、時刻與側別，以及**最佳指向**（輻射點方位角 +90° / −90°） |
| **現在** | 這個小時的指數與主要側，以及建議的 Hot（僅當所選日期為今天時） |
| **實驗性預報** | 在預報頻率上，目前、1 小時後與 2 小時後的預期反射/小時（Collm，SM6FHZ 法則；請參閱[預報（實驗性）](Experimental-Forecasts-zh-tw)） |

卡片下方有一條說明列，解釋字母 A 與 B 的意義（見下文）。

## 圖表

*… 於 … 的每小時效率（UTC，數值取每小時的半點）。* 最多顯示五個流星雨：效率 % 以實線表示，DH9GCD 公式以同色的點線表示；**路徑指數**以藍色長條表示，對應右側刻度。

## 每小時表格

當天每個活躍的流星雨占一列（依 ZHR 排序），24 欄對應各小時（UTC）：

| 儲存格 | 意義 |
|---|---|
| `63A` | 效率 63 %，大多數反射來自 **A** 側 |
| `41B` | 效率 41 %，**B** 側 |
| `3` | 效率低於 5 %：只有數字，不加側別字母 |
| 空白 | 效率低於 1 % |
| `…↑` | 該小時從您的電台看，輻射點**高於 70°**（太高） |
| 黃色文字 | 效率 ≥ 50 % |

- **A** = 從您的電台望向對方電台時的**左方**（Hot A 區域）；**B** = **右方**（Hot B 區域）。值得將天線**朝該側偏轉 10–30°**（側向散射，Cerrotta–Sartori 文章）。
- **淺藍色列**（每個流星雨下方的 *DH9GCD %*）：DH9GCD 公式，供比較用。
- **Σ 列**：*路徑指數（ZHR×效率）*。
- **橘色列**（*預報 … MHz（反射/小時）*）：實驗性預報，僅在有預報的小時顯示（今天與明天的一部分）。

## 模型

所有步驟都在[計算手冊](Efficiency-Explanation-zh-tw)中（`doc/YA-MS_manuale_calcoli.docx`，第 5 章）。簡述如下：

**1. 鏡面反射。** 只有當餘跡與以 A、B 為焦點的橢球面相切時，它才能把訊號從 A 送到 B（McKinley 1961）。同一流星雨的餘跡都平行於輻射點方向 ŝ（文章；McKinley）。對 E 層上的每個點 P，取指向兩個電台的單位向量：

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

DJ5HG 的 QTFGUI（錐面散射）也是以同一定律為基礎。這個條件以高斯容許值 σ = 0.05 rad（約 3°）放寬接受：*程式的選擇*：

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. 每個點的權重。** 欠密餘跡的功率（McKinley），φ = 散射角的一半（限制在 85° 以內，*選擇*）：

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

到達某一點的流星數與該處輻射點仰角的正弦值（ŝ·û_P）成正比，這與 IMO 對 ZHR 所用的修正相同。

**3. 加總與百分比。** 在餘跡高度上每 15 km 取一個點，只取兩個電台都能在波瓣仰角以上看到的點（*選擇*）。100 % 對應該路徑最有利的輻射點位置：

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F 對每條路徑只在一個方向網格（方位角每 5°，仰角每 2.5°）上計算一次，然後內插。

**4. 側別與指數。**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

表格中的字母是比例較大的一側。*程式的選擇（手冊式 32–33）。*

## DH9GCD 比較

一項獨立的驗證：**DH9GCD** 的最佳方向公式，由 **DF5HC** 轉述（DARC 研討會，2018 年 1 月），其中 El 與 Az 為從您的電台看的輻射點仰角與方位角，P 為對方電台的方位角：

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

當輻射點位於 45° 且與路徑垂直時，此值最大。DF5HC 認為輻射點低於 20° 太低，**高於 70° 太高**：這些小時在表格中標有 ↑，並在[天球](Sky-View-zh-tw#警告)上顯示警告。這個公式忽略了距離與高度，但仍是很好的參考。

## 驗證

| 驗證 | 結果 |
|---|---|
| SM6FHZ 法則（VUSHF 2025）：最佳路徑與輻射點方位角正交，指向 = 輻射點方位角 ±90°，容許 ±40–50° | 模型可以重現；當輻射點與路徑方向一致且位於高空時，效率幾乎為零 |
| DJ5HG 的 QTFGUI，漢堡 JO53IM – 巴塞隆納，象限儀座流星雨，1 月 4 日（其手冊中的範例） | QTFGUI：07:00 指向 252°，−8 dB；08:00 沒有反射區域；09:00 指向 168°，−4 dB。YA-MS（與 QTFGUI 同樣取高度 102 km）：07:00 241°，−5.4 dB；08:00 0.6 %（−22 dB）；09:00 161°，−4.0 dB。DH9GCD：26 %、2 %、32 %。三種方法都看到了 08:00 的空洞，此時輻射點幾乎位於天頂 |
| 每 5 km 而非每 15 km 取樣 | 百分比的變化小於 0.3 個百分點 |

> OH5IY 與 MCG_MS 所用刻度的細節並不清楚（MS-Soft 的手冊已無法取得）：在將百分比視為等同之前，請先與這些程式比較。此模型只考慮欠密餘跡，天線為等向性；過密餘跡的長回波與偶發流星背景不計入效率（偶發流星背景由雷達通量呈現）。
