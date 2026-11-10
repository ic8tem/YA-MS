[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · **中文 (繁體)**

# 幾何與路徑損耗

*分頁：預報計算 › 幾何與路徑損耗。*

[![幾何與路徑損耗](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

一份路徑的文字報告（文字可選取，方便複製），右側是圖表**天線仰角與到散射點距離的關係**。方括號中的數字對應計算手冊（`doc/YA-MS_manuale_calcoli.docx`）中的公式編號。

## 本分頁的輸入

| 欄位 | 預設 | 用途 |
|---|---|---|
| **功率 W** | 400 | 用於鏈路預算的發射功率 |
| **天線增益 dBi（發 = 收）** | 14 | 兩端使用相同的天線 |
| **最小訊號 dBm** | −130 | 最小可偵測訊號（文章：8 單元八木 + 前置放大器） |
| **餘跡密度 q = 10^ … 電子/m** | 14 | 欠密餘跡的電子線密度 |

電台、頻段、餘跡高度、波瓣仰角、橫桿和熱點距離取自[控制項列](Getting-Started-zh-tw#1-三列控制項)。

## 報告各部分

| 部分 | 內容 |
|---|---|
| **路徑幾何（球形地球，R = 6372.7955 km）** | 本台和 DX 及其高度；距離、方位和反方位；中點（網格座標和經緯度）；餘跡高度（取自雷達時註明 *<- Collm 雷達測得的眾數*）；指向中點的天線仰角 |
| **HOT A / HOT B（經典熱點，用於天線指向）** | 每個熱點：網格座標、從本台看的方位及相對直達路徑的偏角、從 DX 看的方位、距離、仰角 |
| **公共區域邊界** | 在給定波瓣仰角下餘跡高度處的涵蓋距離；邊界 A / 邊界 B 及其方位 |
| 天線 | 以 λ 表示的橫桿長度、增益、水平/垂直波瓣；Hot A 和 Hot B 在波瓣內還是外 |
| **路徑損耗（欠密餘跡，McKinley 1961；不含天線增益）** | 中點（前向）、Hot A 和 Hot B 在 28、50、70、144、222 和 432 MHz 上的數值表 |
| **… MHz 鏈路預算（中點）** | 功率和 EIRP、路徑損耗、天線處訊號、最小可接收訊號、**餘裕**；以及採用 OH5IY 平均損耗時的餘裕 |
| **頻段間經驗規則（SM6FHZ，VUSHF 2025）** | 與 144 MHz 相比的數量/強度和持續時間；IARU 最大 ping |

## 網格座標與路徑

網格座標（4、6 或 8 位；取方格中心，IARU Maidenhead 系統）[14]。距離、方位和中點採用半徑 **r = 6372.7955 km**（Cerrotta–Sartori 文章）球面上的大圓公式計算 [15–16]。與時間相關的計算以**中點**為準，因為兩端的最佳時間可能相差多達 1.5 小時（SM6FHZ）。

## 天線仰角

**來源：** Cerrotta–Sartori 文章中的公式（圖 7），其中 x = d/r，d 為到反射點的地面距離，H 為餘跡高度，h 為電台高度 [17]：

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**驗證：** 與精確球面幾何的差異在 0.03° 以內。程式使用雙參數反正切函式，在地平線以外給出負值，並避免了文章中提到的週期性問題。指向中點的仰角為負，表示*路徑超出單跳的幾何範圍*。

## 地平線涵蓋距離

仰角為 e 的射線到達高度 H 時的地面距離（上式的幾何反算）[18]：

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**驗證：** H = 89.5 km、e = 0° → **1062 km**。在文章的範例（JN44BB–IO53RT）中，圖上的地平線交點距電台約 870 km，相當於波瓣抬高約 2°（865 km）。

## 公共區域邊界

**來源：** 文章給出了各台站地平線與 E 層相交曲線的交點：即以 A 和 B 為圓心、角半徑為 ρ = d_H/r 的兩個圓的交點 [19–20]：

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

若 1 − |p0|² < 0，則路徑長於 2·d_H，兩個電台**沒有 E 層公共區域**。

**驗證：** 這些是兩個電台都能看到的天空的**最遠邊緣**，**而不是瞄準點**。在 JN70CN–IN78UO（1710 km，方位 308°）上，它們位於距電台 1062 km 處、直達路徑左右 37°，而 MSHV 建議的是 10°。因此它們被稱為*邊界 A* / *邊界 B*，並在地圖上以淡色繪出。

## Hot A 與 Hot B

**來源：** 偶發流星的反射集中在中點兩側的兩個區域（「熱點」）。J. Richardson（AMS）在 DJ5HG 引用的表格中（*Die Geometrie von Meteorscatterverbindungen*，2004）列出了相對於直接方向的天線偏角：**1000 km 為 13°，1250 km 為 11°，1500 和 2000 km 為 10°**。W8WN 沿用的 AMS Bulletin No. 203 列出 1500 和 1800 km 為 10°。

**選擇：** Hot A 和 Hot B 是距中點 M 為 s、垂直於路徑的點。勾選 *auto (AMS)*（預設）時，s 由 Richardson 表格的偏角線性內插得出（1000 km 以下取 13°，2000 km 以上取 10°）：s = (D/2)·tan(偏角)。不勾選時，s 手動輸入，30–400 km（MSHV 使用 150 km）；從本台望向 DX 時 A 在左、B 在右 [21]。從電台看的偏角約為 [22]：

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**驗證：** 依 AMS 表格，1000 km → 13°，s ≈ 115 km；1250 km → 11°，s ≈ 121 km；1500 km → 10°，s ≈ 132 km；2000 km → 10°，s ≈ 176 km。JN70CN–IN78UO（1710 km）→ 10°，s ≈ 151 km，與先前及 MSHV 使用的 150 km 相同；在短路徑上，該表格使熱點更靠近中點。

## 欠密餘跡路徑損耗

**來源：** McKinley 的欠密餘跡方程式和 ITU-R P.843 建議書（sin α = 1），不含天線增益；q = 電子線密度，r_e = 古典電子半徑 = 2.818·10⁻¹⁵ m，R1、R2 為到餘跡的距離，φ 為散射角的一半，β 為餘跡與路徑平面之間的夾角，a₁ 為初始半徑因子，r₀ 以 m 計、h 以 km 計（P.843，公式 4 和 7）[36]：

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**選擇：** 鏈路預算和損耗表使用 β = 90°（餘跡穿過路徑平面，最不利的情況：保守值），鏈路預算同時也顯示最好的情況 β = 0。r₀ 取該頻率的平均回波高度，h = 124 − 17 log f（P.843，公式 15）：50 MHz 為 95 km 處 0.76 m，144 MHz 為 87 km 處 0.40 m，432 MHz 為 79 km 處 0.21 m。在 1000 km 上，a₁ 在 50 MHz 為 0.2 dB，在 144 MHz 為 0.6 dB，在 432 MHz 為 1.4 dB（600 km 時為 2.9 dB）；若用 DJ5HG 固定的 102 km，432 MHz 時約為 70 dB，即完全沒有回波。

**驗證：** 在 144 MHz、q = 10¹⁴ 電子/m、餘跡高度 89.5 km 且 β = 0 時：600 至 2100 km 之間為 **182–192 dB**（1000 km 時 185 dB），落在 GM8JBJ 所引用的 John Worsnop **G4BAO** 博士論文計算的 **172–190 dB** 範圍內。β = 90° 時，損耗在 600 km 增加 10 dB，在 1000 km 增加 13 dB，在 2100 km 增加 16 dB；OH5IY 的**平均 200 dB** 介於兩種情況之間。GM8JBJ 表中的 182 dB 並不構成佐證：該表沒有列出頻率，其每段 86.4 dB 是 1 MHz 下 500 km 的自由空間損耗（缺少 20 log f 項：144 MHz 時為 129.6 dB），各項相加為 163.8 dB 而不是 182；該頁面既沒有寫「最小」，也沒有寫「144 MHz」。

## 鏈路預算

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]。增益以 dBi 輸入並以 dBi 使用：McKinley 損耗以等向性天線為基準，因此不減去 2.15 dB 的偶極天線修正（EIRP = 功率 + 增益）。報告還列出採用 **OH5IY 平均路徑損耗**（144 MHz 時 200 dB，依 λ³ 換算到所選頻段）時的餘裕。文章參考值：約需 **70 dBm EIRP**（−130 dBm + 200 dB，例如約 400 W 饋入 14 dBi 天線）。

## 天線增益與波瓣

**增益 – 來源：** Günter Hoch **DL6WU** 提出的長八木天線增益隨橫桿長度 L 變化的曲線，由 W8IO 轉述（約 2 λ 以上有效）[39]：

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**與 L.B. Cebik W4RNL 在 432 MHz 上的 NEC 模型對比驗證**（*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*；*70-CM Yagi Stacks Part 2*）：

| 八木天線 | 單元數 | 橫桿（λ） | W4RNL NEC（dBi） | 公式（dBi） |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU（David Tanner） | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

差異從未超過 **0.1 dB**：增益更多取決於橫桿長度，而不是具體設計（單元數相同時，VK3AUU 八木的橫桿較短）。VK5DJ 的 Yagi Calculator 也提供了 VK3AUU、WA2PHW 和 DJ9BV 型號的估算值，但其公式未公開。

**波瓣 – 來源：** Kraus 規則，取圓形波瓣 θE = θH = θK [40]：

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**驗證：** W4RNL 對 DL6WU 八木的 NEC 模型給出的**水平波瓣比 Kraus 窄 5–10 %**：12、19 和 26 單元分別為 33.8° / 26.4° / 22.6°，而 Kraus 為 37.3° / 28.0° / 23.9°。簡單公式忽略了前向旁瓣（W4RNL，*Long-Boom Yagi Rules of Thumb*）。長橫桿上垂直波瓣略寬於水平波瓣（14 λ：18.4° / 18.8°）。

**選擇** [41]：

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

範例：432 MHz 上 14 λ 的八木 → 20.3 dBi，水平波瓣 18.1°，垂直波瓣 19.5°；W4RNL 的模型給出 20.4 dBi 和 18.4° / 18.8°。這些是由少數幾副 DL6WU 天線得出的近似規則。

天線始終被視為指向 DX。若 |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2，則熱點位於**波瓣內**：此時它在[天穹](Sky-View-zh-tw)上以灰色繪出，並出現提示。在效率計算中天線被視為等向性；實際波瓣只用於這項檢查。

## 頻段間經驗規則

與 144 MHz 相比：數量/強度 × (144/f)³（以 dB 計），持續時間 × (144/f)²（SM6FHZ，VUSHF 2025）。IARU 第一區最大 ping 持續時間：50 MHz 為 1000 ms，70 MHz 為 500 ms，144 MHz 為 100 ms，432 MHz 為 13 ms（VHF Handbook，文章中引用）。另見[試驗性預報](Experimental-Forecasts-zh-tw)。
