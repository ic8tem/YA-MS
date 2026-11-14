[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · **中文 (繁體)**

# 即時通訊

*分頁：實況與即時資料 › 即時通訊。*

[![即時通訊](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## 顯示內容

一張以本台為中心的**方位等距地圖**（到中心的距離 = 真實距離，角度 = 方位角），顯示由[資料收集](Data-Collection-zh-tw)彙集的**所有流星散射通訊**。對每個通聯，程式繪出：

- 兩個電台之間的**路徑**，依頻段著色：28 MHz 棕色，50 MHz 綠色，70 MHz 青色，144 MHz 橘色，222 MHz 粉紅色，432 MHz 紫色；
- 路徑兩端的兩個**電台**；
- **雲團**：該路徑在該時刻最可能出現流星餘跡的集中區域。

有電台位於**地圖之外**的 spot 會被捨棄。**剛剛到達**（不超過 3 分鐘）的 spot 會**閃爍一分鐘**，讓新的活動一目了然。

顯示誰在收聽：波段顏色的三角形標出 PSKReporter 顯示在所選時間窗內於 28、50、70、144 和 432 MHz 接收 MSK144、FSK441、PSK2K 或 JTMS 的電台。點擊三角形可查看呼號、網格、模式和最近報點。需要連線「資料收集」分頁中的 MQTT 資料流。

同時顯示 PSKReporter 地圖上的活動監聽站：在 pskreporter.info 地圖上以 MSK144、FSK441、PSK2K 或 JTMS 出現但尚未收到任何報告的電台顯示為空心三角形（MQTT 只傳送有接收的電台）。YA-MS 依照該服務的規定，每 5 分鐘對所有模式查詢一次 PSKReporter 查詢服務；監聽站在地圖上至少保留 11 分鐘。點擊三角形可顯示呼號、網格定位、解碼軟體和監聽站活動的時間。預設開啟。

超過 1100 公里且無平行路徑的 FT8：相距超過 1100 公里的電台之間的 FT8 報告（來自 PSKReporter MQTT、叢集或經 UDP 的 WSJT-X），如果在其前後 3 分鐘內沒有平行路徑（同一波段、中點相距 300 公里以內、方向相差 15° 以內、另一對電台），則以淺綠色繪製，其在右下方表格中的列始終閃爍。偶發 E 層和對流層傳播會產生許多相近的平行路徑；孤立的報告可能是流星餘跡。為此 YA-MS 也從 MQTT 接收 6 m、4 m、2 m、1.25 m 和 70 cm 的 FT8 報告（不含 10 m，數量太多）。這些報告不進入 MS 存檔。預設開啟。

經 UDP 收到、與你的電台有關的 WSJT-X 報告（解碼中含有你的呼號：呼叫你或回覆你的電台）以始終閃爍的虛線繪製，任何模式、任何距離皆然。

YA-MS 使用者之間的交換：當另一位 YA-MS 使用者透過 UDP 解碼到發給你電台的訊息（MSK144、FSK441、PSK2K 或 JTMS，或超過 1100 公里的 FT8）時，他的 YA-MS 會透過三個公共 MQTT 代理（HiveMQ、Mosquitto、EMQX）把訊息加密傳給你；你會看到一條始終閃爍的紫色虛線，並在 UDP 主控台中看到一行。只有你能讀取（ECDH P-256 金鑰、AES-256 和 HMAC-SHA256）。FT8 報告僅在 3 分鐘內沒有平行路徑時才顯示。預設開啟；在 data/config.ini 中設 yams_scambio=0 可關閉。

地圖上寫出每筆報告兩端電台的呼號，每個電台只寫一次。投影可選：方位投影（以你的電台為中心）或麥卡托。「雲團」欄的提示說明其含義。

顯示所有波段的報告，包括資料收集中未選擇的波段（這些不會被儲存）。如果在資料收集中被捨棄，CW 報告和距離過近的電台之間的報告不會顯示。

## 雲團如何計算

對每筆 spot，程式建立兩個網格座標之間的路徑（與本台路徑使用相同的幾何，請參閱[幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw)），並在 spot 的時刻，逐點累加 E 層上**每個活躍流星雨的鏡面反射貢獻**，以其 ZHR 加權——與[天穹](Sky-View-zh-tw)中的 **PREV 區域**是同一種計算。對於佔總量至少 15 % 的路徑每一側，雲團是一個**橢圓**：中心為各點的加權平均位置，半軸為各點離散度特徵值平方根的 1.5 倍，長軸沿主特徵向量方向。如果沒有任何流星雨做出貢獻（只有偶發流星），雲團就是兩個經典的**熱點**，以虛線繪出。完整的公式見計算手冊第 10 章。

## 控制項

| 控制項 | 含義 |
|---|---|
| **地圖半徑** | 距本台 600–3500 km。 |
| **要顯示的 spot** | 最近 15 或 30 分鐘、最近 1 小時、最近 3 小時、最近 24 小時。 |
| **表格** | 地圖上的通聯，最新的在前，以頻段顏色顯示；*雲團* 欄列出主要一側所佔的反射比例，或顯示*偶發流星*。 |
| **點選** | 點選路徑或表格中的一列：該通聯會被突顯，資訊框中顯示雲團中心的網格座標、其所佔比例、大小和軸向。 |
