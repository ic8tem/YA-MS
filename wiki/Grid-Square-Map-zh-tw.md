[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [ไทย](Grid-Square-Map-th) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · **中文 (繁體)**

# 網格地圖

*頁籤：網格地圖。*

[![網格地圖](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

從您日誌的 ADIF 檔案讀取已**通聯**與已**確認**的 Maidenhead 網格（4 個字元），顯示在歐洲地圖上：**每個頻段一個子頁籤：50、70、144、222 與 432 MHz**。

## 控制項

| 控制項 | 作用 |
|---|---|
| **載入 ADIF 檔案...** | 讀取 `.adi` / `.adif` 檔案。新的 ADIF 會**取代**先前的資料。 |
| **清除記憶** | 刪除所有從 ADIF 載入的網格（會要求確認）。 |
| 滑鼠 | **滾輪 = 縮放，拖曳 = 平移，滑鼠移到網格上 = 通聯**（最多六個呼號及日期，已確認的會標示 *（已確認）*） |

載入後，狀態列會顯示 *讀取 … 筆通聯，50-432 MHz 頻段 … 個通聯網格，捨棄 … 筆通聯（其他頻段或無網格）*。每個頻段的地圖都有說明 *已通聯 … 個網格，已確認 … 個*。

| 顏色 | 意義 |
|---|---|
| 橘色 | 已通聯 |
| 綠色 | 已確認（QSL 或 LoTW） |

## 如何讀取 ADIF

- 使用的欄位：`CALL`、`GRIDSQUARE`、`VUCC_GRIDS`、`BAND`、`FREQ`、`QSO_DATE`、`QSL_RCVD`、`LOTW_QSL_RCVD`（ADIF 規格）。
- 頻段取自 `BAND`，或由頻率推得：50–54 MHz = 6 m，69.9–71.5 MHz = 4 m，144–148 MHz = 2 m，219–225 MHz = 1.25 m，420–450 MHz = 70 cm。
- 如果某網格中至少有一筆通聯的 `QSL_RCVD = Y` 或 `LOTW_QSL_RCVD = Y`，該網格即為**已確認**。
- 網格保存在 `data/adif_quadrati.csv` 中，直到您載入另一個檔案或按下**清除記憶**為止。

YA-MS **不會**連線到 LoTW：請從您的日誌程式（或從 LoTW）匯出 ADIF，然後在這裡載入。
