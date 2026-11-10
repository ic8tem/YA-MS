[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [ไทย](Live-Traffic-th) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · **中文 (繁體)**

# 即時通訊

*頁籤：Live 與即時資料 › 即時通訊。*

[![即時通訊](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## 顯示內容

一張以您的電台為中心的**方位等距地圖**（到中心的距離 = 真實距離，角度 = 方位角），顯示由[資料收集](Data-Collection-zh-tw)匯集的**所有流星散射通訊**。對每一筆通聯，程式會繪出：

- 兩個電台之間的**路徑**，以其頻段的顏色顯示：28 MHz 棕色，50 MHz 綠色，70 MHz 青色，144 MHz 橘色，222 MHz 粉紅色，432 MHz 紫色；
- 路徑兩端的兩個**電台**；
- **雲團**：該路徑在該時刻最可能出現流星餘跡的集中區域。

有電台位於**地圖之外**的 spot 會被捨棄。**剛剛到達**（不超過 3 分鐘）的 spot 會**閃爍一分鐘**，讓新的活動一眼就能看出。

## 雲團如何計算

對每一筆 spot，程式會建立兩個網格座標之間的路徑（與您自己的路徑使用相同的幾何，請參閱[幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw)），並在 spot 的時刻，逐點累加 E 層上**每個活躍流星雨的鏡面反射貢獻**，以其 ZHR 加權：與[天球](Sky-View-zh-tw)的 **PREV 區域**是同一種計算。對於占總量至少 15 % 的路徑每一側，雲團是一個**橢圓**：中心為各點的加權平均位置，半軸為各點分散程度之特徵值平方根的 1.5 倍，長軸沿主特徵向量方向。如果沒有任何流星雨有貢獻（只有偶發流星），雲團就是兩個經典的**熱點**，以虛線繪出。完整的方程式見計算手冊第 10 章。

## 控制項

| 控制項 | 意義 |
|---|---|
| **地圖半徑** | 距您的電台 600–3500 km。 |
| **要顯示的 spot** | 最近 15 或 30 分鐘、最近一小時、最近 3 小時、最近 24 小時。 |
| **表格** | 地圖上的通聯，最新的在最前面，以頻段顏色顯示；*雲團* 欄顯示主要一側所占的反射比例，或顯示*偶發流星*。 |
| **點選** | 點選路徑或表格中的一列：該通聯會被醒目標示，資訊框中顯示雲團中心的網格座標、其所占比例、大小與軸向。 |
