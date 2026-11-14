[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · **中文 (繁體)**

# 效率計算

*分頁：預報計算 › 效率計算。*

[![效率計算](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

一個流星雨的**效率**以百分比表示其輻射點位置在多大程度上允許在**您的**路徑上產生反射。這個概念由 Ilkka **OH5IY**（MS-Soft）提出，並被 Cerrotta–Sartori 的文章採用：效率峰值與目視峰值（ZHR）並不重合，因為它取決於輻射點相對於兩個電台的位置。DL5MCG 的 MCG_MS 把同樣的思路應用於四個固定方向；YA-MS 則針對兩個網格座標之間的**實際路徑**進行計算。

本分頁依*計算日期（UTC）*中選擇的日期逐小時顯示效率（取每小時半點的值）。

## 概覽卡片

| 卡片 | 內容 |
|---|---|
| **當天最佳時段** | 路徑指數最高的小時、該指數以及主要的一側（A/B 及其百分比） |
| **最有利的流星雨** | 當天 ZHR × 效率最大的流星雨、其效率、時刻和一側，以及**最佳指向**（輻射點方位 +90° / −90°） |
| **現在 · 1、3、6、12 和 24 小時後** | 每個時間點取從那裡開始的一小時的平均值（四個取樣）：路徑指數、主要一側、貢獻最大的流星雨，有雷達資料時還有實驗性預報的每小時反射次數。在「現在」中，沒有雷達資料時顯示建議的 Hot。每分鐘更新。 |

這些方框位於時間列下方、分頁上方的一條橫欄中，即使收合命令列也始終可見：左邊是所選日期的兩個方框，然後是從現在開始的六個預報時間點。

卡片下方的一條說明列解釋字母 A 和 B 的含義（見下文）。

## 圖表

*… 在 … 的逐時效率（UTC，取每小時半點的值）。* 最多顯示五個流星雨：效率 % 用實線表示，DH9GCD 公式用同色虛線表示；**路徑指數**以藍色長條表示，對應右側刻度。

## 逐時表格

當天每個活躍流星雨佔一列（依 ZHR 排序），24 欄對應各小時（UTC）：

| 儲存格 | 含義 |
|---|---|
| `63A` | 效率 63 %，大多數反射來自 **A** 側 |
| `41B` | 效率 41 %，**B** 側 |
| 空白 | 效率低於 1 % |
| `…↑` | 該小時從本台看輻射點**高於 70°**（過高） |
| 黃色文字 | 效率 ≥ 50 % |

- **A** = 從本台望向對方電台時的**左側**（Hot A 區域）；**B** = **右側**（Hot B 區域）。值得將天線**向該側偏轉 10–30°**（側向散射，Cerrotta–Sartori 文章）。
- **淺藍色列**（每個流星雨下方的 *DH9GCD %*）：DH9GCD 公式，用於比較。
- **Σ 列**：*路徑指數（ZHR×效率）*。
- **橘色列**（*預報 … MHz（反射/小時）*）：試驗性預報，只在有預報的小時顯示（今天及明天的一部分）。

## 模型

所有步驟都在[計算手冊](Efficiency-Explanation-zh-tw)中（`doc/YA-MS_manuale_calcoli.docx`，第 5 章）。簡述如下：

**1. 鏡面反射。** 只有當餘跡與以 A 和 B 為焦點的橢球面相切時，它才能把訊號從 A 送到 B（McKinley 1961）。同一流星雨的餘跡都平行於輻射點方向 ŝ（文章；McKinley）。對 E 層上的每個點 P，取指向兩個電台的單位向量：

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

DJ5HG 的 QTFGUI 及其文章 *"Die Geometrie von Meteorscatterverbindungen"*（2004）也以同一定律為基礎：餘跡在以餘跡為軸的圓錐面上散射，只有位於圓錐面上的接收台才能聽到。對於理想餘跡，圓錐壁非常薄（一個長達數千波長的輻射體）；程式以高斯容差 σ = 0.05 rad（約 3°）接受該條件，用來代表理想圓錐未考慮的因素：流星雨輻射點的彌散（GMN 測得 0.3–1.4°）、被風吹彎的餘跡以及餘跡的有限長度——*程式的選擇*：

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. 每個點的權重。** 欠密餘跡的功率（McKinley；ITU-R P.843，公式 3），φ = 散射角的一半（限制在 85° 以內，*選擇*），β = 餘跡與傳播平面 A-P-B 之間的夾角，p̂ = 該平面的單位法向量：

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**選項「餘跡與路徑之間的 β 角（完整 McKinley 公式）」**（預設啟用，保守設定）。啟用時：穿過傳播平面的餘跡比位於平面內的餘跡低 10–15 dB，因此不會高估任何餘跡。關閉時：每條餘跡都按位於該平面內來加權（β = 0，權重含 cos²φ），與 1.6 版及以前相同。*驗證：* 在 1000 km 的路徑上，不用 β 時，最佳輻射點方位角距路徑 15°–90°，取決於輻射點仰角（輻射點在 30° 時為 30°，在 60° 時與路徑垂直），仰角 30° 時垂直方向的輻射點為 67 %；用 β 時，最佳輻射點總是沿路徑方向，垂直方向的降到 15 %。使用 β 會失去 SM6FHZ / DH9GCD 的最佳方向規則；β 仍是一個選項，因為它給出最保守的數值而預設啟用，關閉它即可恢復該規則。

到達某點的流星數與該處輻射點仰角的正弦（ŝ·û_P）成正比，這與 IMO 對 ZHR 使用的修正相同。

**選項「輻射點低時餘跡更長（DJ5HG）」**（圖表上方的核取方塊，預設關閉，附提示）：DJ5HG 指出，輻射點低時每 km² 落下的流星較少，但餘跡更長（有效長度可達 100 km），更常滿足反射定律。啟用該選項後，權重變為 min(sin El, 15/100)：有效層厚 15 km 除以仰角的正弦即為餘跡長度，上限 100 km。約 9° 以上兩種效應相互抵消。關閉時，計算保持保守。

**計算設定**（同一列，選項按鈕）：**保守**（預設，數值最保守：雷達測得的餘跡高度、一般餘跡、啟用 β）、**同 DJ5HG**（102 km、較長餘跡、β）和**自訂**；當您手動變更高度、*來自雷達*核取方塊、較長餘跡選項或 β 時，會自動選取「自訂」。

**3. 加總與百分比。** 在餘跡高度每隔 15 km 的點，兩個電台都能在地平線以上看到，並依兩副天線的垂直場型加權（*天線場型* 核取方塊，預設開啟；關閉時只用波瓣仰角以上的點）（*選擇*）。100 % 是該路徑上最有利的輻射點位置：

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F 對每條路徑只在一個方向網格（方位每 5°，仰角每 2.5°）上計算一次，然後進行內插。

**以 dB 表示的效率（DJ5HG 基準）。** 百分比僅相對於該路徑的最佳輻射點位置。為了比較不同路徑，程式還提供相對於 DJ5HG 固定基準的 dB 效率：0 dB 是一條跨越赤道、長 1000 km 的南北向路徑在分點時輻射點位於天赤道上的最大值，用相同的高度和權重計算。DJ5HG 稱其數值的精度優於 6 dB。

**4. 側別與指數。**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

表格中的字母是比例較大的一側。*程式的選擇（手冊公式 32–33）。*

## DH9GCD 對比

最佳方向的原始文獻是 Eshleman & Mlodnosky 和 Meeks & James（Proc. IRE，1957）、Hines（1955）以及 Forsyth、Hines & Vogan（1955）對其的實驗驗證：只有位於與散射角平分線垂直的半圈天空上的輻射點才有用，餘跡數量隨 sin El 增加，且在中點附近，有用餘跡落在側向約 H·tan El 處、與輻射點相反的一側。DJ5HG 補充了一點保留意見：當**低**輻射點正好沿著路徑方向時，McKinley 公式給出強訊號（漢堡–納爾維克，象限儀座流星雨，約 19 UTC），因此「輻射點與路徑同向 = 幾乎為零」只適用於高輻射點；程式保持保守，並顯示警告 *輻射點低且沿路徑方向*。

一項獨立的驗證：**DH9GCD** 的最佳方向公式，由 **DF5HC** 轉述（DARC 會議，2018 年 1 月）——沒有已發表的原始文獻——其中 El 和 Az 為從本台看的輻射點仰角和方位，P 為對方電台的方位：

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

當輻射點位於 45° 且與路徑垂直時，該值最大。DF5HC 認為輻射點低於 20° 過低，**高於 70° 過高**：這些小時在表格中標有 ↑，並在[天穹](Sky-View-zh-tw#警告)上給出警告。該公式忽略了距離和高度，但仍是很好的參考。

## 驗證

| 驗證 | 結果 |
|---|---|
| SM6FHZ 規則（VUSHF 2025）：最佳路徑與輻射點方位正交，指向 = 輻射點方位 ±90°，容差 ±40–50° | 模型能夠重現；當輻射點與路徑方向一致且位於高空時，效率幾乎為零 |
| DJ5HG 的 QTFGUI，漢堡 JO53IM – 巴塞隆納，象限儀座流星雨，1 月 4 日（其手冊中的範例） | QTFGUI：07:00 指向 252°，−8 dB；08:00 無反射區；09:00 指向 168°，−4 dB。YA-MS（與 QTFGUI 一樣取高度 102 km）：07:00 241°，−5.4 dB；08:00 0.6 %（−22 dB）；09:00 161°，−4.0 dB。DH9GCD：26 %、2 %、32 %。三種方法都看到了 08:00 的空洞，此時輻射點幾乎位於天頂 |
| DJ5HG 的曲線（*Die Geometrie…*，Bild 8–9：從漢堡和慕尼黑出發，象限儀座流星雨，1 月 4 日；從圖上讀取，約 ±0.5 dB 和 ±15 分鐘）與自動測試 `--prova-dj5hg`（每小時一個值）的對比 | 時間：輻射點接近天頂時的空洞出現在相同的時段（巴塞隆納 07:30–08:30 對 07–09；索菲亞 06:36–07:48 對 07–08；納爾維克 07–08:30 對 07–09）；莫斯科在兩者中 03–10 時均不通，正如 DJ5HG 所寫，從漢堡可通到約 02:30，從慕尼黑可通到約 00:30。方向：相差 2–10°。102 km 時的電平與形狀（與曲線的平均差和 RMS 差）：不用 β、不用較長餘跡 −1.6 / 4.0 dB；較長餘跡 +1.1 / 4.6 dB；β −5.4 / 6.2 dB，但形狀最好（去掉平均值後 3.0 dB，對 3.6）：出現了低輻射點時的深極小值（巴塞隆納 17 時 −15.6 dB，對 19:36 的 −16 dB；索菲亞 20 時 −18.5 dB，對 −14 dB）。β 加較長餘跡（*同 DJ5HG*）−2.2 / 4.7 dB；保守設定（雷達高度 89.5 km、啟用 β、不用較長餘跡）−6.9 / 7.6 dB，形狀 3.3 dB。不用 β 時，YA-MS 幾乎看不出輻射點低且幾乎與路徑同向時的極小值（−8.6 和 −10.4 dB）：這正是 DJ5HG 本人的保留，因此程式給出警告 |
| 每 5 km 而非每 15 km 取樣 | 百分比變化不到 0.3 個百分點 |

> MS-Soft 5.2 的文件將 OH5IY 的效率定義為僅針對欠密餘跡的相對指數，包含兩個因子（輻射點仰角，最佳約 45°；與路徑的夾角，最佳 90°），並為過密餘跡手動把最小值提高到 20 %；公式未公開。MCG_MS 針對四個固定方向計算效率，輸入 DX 定位符後也針對實際路徑計算。該模型只考慮欠密餘跡，天線為等向性；過密餘跡的長回波和偶發流星背景不計入效率（偶發流星背景由雷達流量體現）。 自 1.8.1 起，開啟「天線場型」核取方塊時會套用天線的垂直場型；在方位上天線仍視為等向性。
