[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · **中文 (繁體)**

# 幾何與路徑損耗

*頁籤：預報計算 › 幾何與路徑損耗。*

[![幾何與路徑損耗](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

一份路徑的文字報告（文字可選取，方便複製），右側則是圖表**天線仰角與到散射點距離的關係**。方括號中的數字對應計算手冊（`doc/YA-MS_manuale_calcoli.docx`）中的方程式編號。

## 本頁籤的輸入

| 欄位 | 預設 | 用途 |
|---|---|---|
| **功率 W** | 400 | 用於鏈路預算的發射功率 |
| **天線增益 dBi（tx = rx）** | 14 | 兩端使用相同的天線 |
| **最小訊號 dBm** | −130 | 最低可接收訊號（文章：8 元件八木 + 前置放大器） |
| **餘跡密度 q = 10^ … 電子/m** | 14 | 欠密餘跡的電子線密度 |

電台、頻段、餘跡高度、波瓣仰角、橫桿與熱點距離取自[控制項列](Getting-Started-zh-tw#1-三列控制項)。

## 報告的各段

| 段落 | 內容 |
|---|---|
| **路徑幾何（球形地球，R = 6372.7955 km）** | 本台與 DX 及其高度；距離、方位角與反方位角；中點（網格座標與經緯度）；餘跡高度（取自雷達時註明 *<- Collm 雷達量測的眾數*）；朝向中點的天線仰角 |
| **HOT A / HOT B（經典熱點，供天線指向用）** | 每個熱點：網格座標、從您的電台看的方位角及相對於直接路徑的偏移、從 DX 看的方位角、距離、仰角 |
| **共同區域界限** | 在給定波瓣仰角下，於餘跡高度的涵蓋距離；界限 A / 界限 B 及其方位角 |
| 天線 | 以 λ 表示的橫桿長度、增益、水平/垂直波瓣；Hot A 與 Hot B 在波瓣內或波瓣外 |
| **路徑損耗（欠密餘跡，McKinley 1961；不含天線增益）** | 中點（前向）、Hot A 與 Hot B 在 28、50、70、144、222 與 432 MHz 的數值表 |
| **… MHz 鏈路預算（中點）** | 功率與 EIRP、路徑損耗、天線端訊號、最低可接收訊號、**餘裕**；以及採用 OH5IY 平均損耗時的同一餘裕 |
| **頻段間的經驗法則（SM6FHZ，VUSHF 2025）** | 與 144 MHz 相比的數量/強度與持續時間；IARU 最大 ping |

## 網格座標與路徑

網格座標（4、6 或 8 個字元；取網格中心，IARU Maidenhead 系統）[14]。距離、方位角與中點以半徑 **r = 6372.7955 km**（Cerrotta–Sartori 文章）之球面上的大圓公式計算 [15–16]。與時間相關的計算以**中點**為準，因為兩端的最佳時間可能相差多達 1.5 小時（SM6FHZ）。

## 天線仰角

**來源：** Cerrotta–Sartori 文章中的公式（圖 7），其中 x = d/r，d 為到反射點的地面距離，H 為餘跡高度，h 為電台高度 [17]：

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**驗證：** 與精確的球面幾何相差在 0.03° 以內。程式使用雙引數反正切函數，在地平線以外會得到負值，並避開了文章中提到的週期性問題。朝向中點的仰角為負值，表示*路徑超出單跳的幾何距離*。

## 地平線涵蓋距離

仰角為 e 的射線到達高度 H 時的地面距離（上式的幾何反算）[18]：

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**驗證：** H = 89.5 km、e = 0° → **1062 km**。在文章的範例（JN44BB–IO53RT）中，圖上的地平線交點距電台約 870 km，相當於波瓣抬高約 2°（865 km）。

## 共同區域界限

**來源：** 文章找出了各電台地平線與 E 層交會之曲線的交點：也就是以 A 與 B 為圓心、角半徑 ρ = d_H/r 之兩個圓的交點 [19–20]：

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

若 1 − |p0|² < 0，則路徑長於 2·d_H，兩個電台**沒有 E 層共同區域**。

**驗證：** 這些是兩個電台都看得到之天空的**最遠邊緣**，**而不是要瞄準的點**。在 JN70CN–IN78UO（1710 km，方位角 308°）上，它們位於距電台 1062 km 處、直接路徑左右 37°，而 MSHV 建議的是 10°。因此它們被稱為*界限 A* / *界限 B*，並在地圖上以淡色繪出。

## Hot A 與 Hot B

**來源：** 反射集中在中點兩側約 **50–150 km** 的兩個區域（「熱點」）。這是 AMS Bulletin No. 203 天線偏移表的基礎，W8WN 沿用了它（1500 與 1800 km 的路徑偏移 10°）；LZ2HV 的 MSHV 也採用同樣的準則。

**選擇：** Hot A 與 Hot B 是距中點 M 為 s、垂直於路徑的點（s = 150 km，可在 30–400 km 之間調整）；從您的電台望向 DX 時，A 在左、B 在右 [21]。從電台看的偏移約為 [22]：

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**驗證：** JN70CN–IN78UO，D = 1710 km：s = 100 km 時為 6.7°，**s = 150 km 時為 10.0°**（與 MSHV 及 AMS/W8WN 相同），s = 200 km 時為 13.2°。

## 欠密餘跡的路徑損耗

**來源：** McKinley 的欠密餘跡方程式（β = 0，sin α = 1），不含天線增益；q = 電子線密度，r_e = 古典電子半徑 = 2.818·10⁻¹⁵ m，R1、R2 為到餘跡的距離，φ 為散射角的一半 [36]：

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**驗證：** 在 144 MHz、q = 10¹⁴ 電子/m 時：600 至 2200 km 之間為 **181–192 dB**，與文章中 144 MHz 的參考值一致：**最小 182 dB**（GM8JBJ，引自 Kaiser & Closs 1952）與**平均 200 dB**（OH5IY）。

## 鏈路預算

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]。增益以 dBi 輸入，以 dBd（dBi − 2.15）使用。報告也列出採用 **OH5IY 平均路徑損耗**（144 MHz 時 200 dB，依 λ³ 換算至所選頻段）時的餘裕。文章的參考值：約需 **70 dBm EIRP**（−130 dBm + 200 dB，例如約 400 W 饋入 14 dBi 天線）。

## 天線增益與波瓣

**增益 – 來源：** Günter Hoch **DL6WU** 針對長八木天線、以橫桿長度 L 為變數的曲線，由 W8IO 轉述（約 2 λ 以上有效）[39]：

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**與 L.B. Cebik W4RNL 在 432 MHz 的 NEC 模型比對驗證**（*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*；*70-CM Yagi Stacks Part 2*）：

| 八木天線 | 元件數 | 橫桿（λ） | W4RNL NEC（dBi） | 公式（dBi） |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU（David Tanner） | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

差異從未超過 **0.1 dB**：增益主要取決於橫桿長度，而非設計本身（元件數相同時，VK3AUU 八木的橫桿較短）。VK5DJ 的 Yagi Calculator 也提供 VK3AUU、WA2PHW 與 DJ9BV 變體的估計值，但其公式並未公開。

**波瓣 – 來源：** Kraus 法則，取圓形波瓣 θE = θH = θK [40]：

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**驗證：** W4RNL 對 DL6WU 八木的 NEC 模型得出的**水平波瓣比 Kraus 窄 5–10 %**：12、19 與 26 元件分別為 33.8° / 26.4° / 22.6°，而 Kraus 為 37.3° / 28.0° / 23.9°。簡單公式忽略了前向旁瓣（W4RNL，*Long-Boom Yagi Rules of Thumb*）。在長橫桿上，垂直波瓣略寬於水平波瓣（14 λ：18.4° / 18.8°）。

**選擇** [41]：

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

範例：432 MHz 上 14 λ 的八木 → 20.3 dBi，水平波瓣 18.1°，垂直波瓣 19.5°；W4RNL 的模型得出 20.4 dBi 與 18.4° / 18.8°。這些是由少數幾支 DL6WU 天線推導出的近似法則。

天線一律視為指向 DX。若 |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2，熱點就位於**波瓣內**：此時它會在[天球](Sky-View-zh-tw)上以灰色繪出，並出現注意訊息。在效率計算中天線視為等向性；實際的波瓣只用於這項檢查。

## 頻段間的經驗法則

與 144 MHz 相比：數量/強度 × (144/f)³（以 dB 計），持續時間 × (144/f)²（SM6FHZ，VUSHF 2025）。IARU 第一區最大 ping 持續時間：50 MHz 為 1000 ms，70 MHz 為 500 ms，144 MHz 為 100 ms，432 MHz 為 13 ms（VHF Handbook，文章中引用）。另請參閱[預報（實驗性）](Experimental-Forecasts-zh-tw)。
