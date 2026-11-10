[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · **中文 (繁體)**

# YA-MS – 流星散射預報與流星雨效率即時計算

*作者：Costantino Cerrotta IC8TEM*

**YA-MS** 是一套供業餘無線電愛好者使用的免費程式，適合在 **50、70、144、222 與 432 MHz 上進行流星散射（MS）通訊**的電台。針對您的網格座標與對方電台網格座標之間的實際路徑，程式逐小時計算每個活躍流星雨對該路徑的幫助程度（即其**效率**）、反射來自路徑的哪一側（**Hot A / Hot B**）、天線應指向何處，並根據**即時流星雷達**（德國 Collm）提供每小時反射次數的實驗性預報。程式可在 **Windows、Linux 與 macOS**（.NET 8 + Avalonia）上執行，介面提供 36 種語言。

主要資料來源是 **C. Cerrotta IC8TEM 與 G. Sartori IV3GTH** 的文章 *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"*（第 7 版）。程式中的每個公式與每筆資料都註明了出處，請參閱[資料來源](Sources-zh-tw)。

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="天球"></a><br><sub>天球</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="效率計算"></a><br><sub>效率計算</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES 雷達"></a><br><sub>GRAVES 雷達</sub></td>
</tr></table>

## 適用對象

- 想知道流星散射路徑**何時**開通、天線該指向**何處**的操作者，而不只滿足於籠統的「今晚流星雨達到峰值」。
- 在 **144 與 432 MHz 上進行長距離通聯**的電台：輻射點的位置決定了一個流星雨是有用還是無用。
- 想要**核對數字**的人：計算手冊與程式內的說明列出了每一個步驟及其出處：已發表的資料來源、對程式所做的驗證，或程式本身的選擇。

## 頁籤

自 1.6 版起，主頁籤下設有**子頁籤**（主頁籤下方顏色較淺的一列）。啟動時會顯示 5 秒鐘的啟動畫面：ESO 的 VLT 上空的英仙座流星雨（照片 ESO/S. Guisard，CC BY 4.0）。

| 頁籤 | 子頁籤 | 顯示內容 |
|---|---|---|
| **Live 與即時資料** | [即時通訊](Live-Traffic-zh-tw) | 所有已收集 MS 通訊的方位等距地圖，每筆通聯都繪出最可能餘跡所在的「雲團」，依頻段著色，新的 spot 會閃爍 |
| | [雷達通量](Radar-Flux-zh-tw) | 從 Collm SKiYMET 雷達讀取的每小時流星計數與餘跡高度、Sodankylä 影像、您所用頻段的估計值 |
| | [GRAVES 雷達](GRAVES-Radar-zh-tw) | GRAVES → 你 的前向散射路徑：波束中的有效區域、扇區與步進、波束下次掃過的時間、收聽方法 |
| | [資料收集](Data-Collection-zh-tw) | 三路 telnet cluster 資料串流（DX cluster、RBN、DM4X/PSKReporter）以及 MS spot 篩選器 |
| **預報計算** | [預報計算](Sky-View-zh-tw) | 路徑平面圖，含 Hot A / Hot B、天線波瓣、PREV 區域與流星雨移動軌跡；流星雨清單；含輻射點與正確天線方向的小天球；從天線看出去的剖面 |
| | [幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw) | 距離、中點、仰角、Hot A / Hot B、共同區域界限、28–432 MHz 路徑損耗、鏈路預算、天線 |
| | [效率計算](Efficiency-Calculation-zh-tw) | 概覽卡片、各流星雨每小時效率及 A/B 側、路徑指數、DH9GCD 比較、圖表 |
| | [預報（實驗性）](Experimental-Forecasts-zh-tw) | 以 λ^k 與電台因子 K 將 Collm 通量換算至 144 MHz（或任意頻率）、24 小時預報、RMOB 比對 |
| **技術文件** | [資料來源](Sources-zh-tw) | 所有資料來源；主要來源是 Cerrotta–Sartori 的文章 |
| | [歐洲雷達地圖](European-Radar-Map-zh-tw) | Collm、Sodankylä、GRAVES 與 CMOR 相對於您電台的位置 |
| | [效率 - 說明](Efficiency-Explanation-zh-tw) | 逐步說明效率如何計算的文件，可匯出為 Word |
| [即時流星雨](Live-Showers-zh-tw) | – | Global Meteor Network 實測的 ZHR 與 CMOR 輻射點地圖 |
| [流星雨](Showers-zh-tw) | – | IMO 目錄及下次峰值（IMO 日期與時間或計算值） |
| [網格地圖](Grid-Square-Map-zh-tw) | – | 依 ADIF 檔案顯示已通聯與已確認的 Maidenhead 網格，每個頻段一個頁籤 |

頁籤上方有三列控制項（您的網格座標、對方電台、頻段、天線、餘跡高度、時間），請參閱[入門](Getting-Started-zh-tw)。**控制**按鈕可將其收合；介面語言與配色方案在右上角選擇，請參閱[設定與資料資料夾](Settings-and-Data-Folder-zh-tw)。

## 簡要特點

- **實際路徑，而非固定方向**：效率是針對兩個網格座標之間的大圓路徑計算的（早期的程式只使用四個固定方向）。
- **鏡面反射模型**（McKinley），在 E 層上每 15 km 取一個點，餘跡高度即時讀取自 Collm 雷達。
- **Hot A / Hot B** 位於中點兩側 150 km（可在 30–400 km 之間調整），建議的一側以紅色標示，已落在天線波瓣內的以灰色標示。
- **即時雷達**：每 5 分鐘檢查一次 Collm，只重新下載有變更的資料來源；離線時程式會使用最後儲存的資料繼續運作。
- 依 SM6FHZ 的 λ³ 規則提供 50/144/432 MHz 的**實驗性**預報，可與 RMOB 觀測者的資料比較。
- 所有內容都在程式旁的單一 **`data`** 資料夾中：不使用 AppData，也不使用系統資料夾。

> 效率是一個實驗性模型（鏡面反射 + 欠密餘跡）。請將它與 MCG_MS、MS-Soft 以及您自己的上線經驗互相比較。

## 從哪裡開始

1. [安裝](Installation-zh-tw)
2. [入門](Getting-Started-zh-tw)
3. 如果有問題，請參閱[疑難排解與常見問題](Troubleshooting-FAQ-zh-tw)。

下載：GitHub 上的 **[Releases](https://github.com/ic8tem/YA-MS/releases)**。
