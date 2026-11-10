[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · **中文 (繁體)**

# 效率 - 說明

*頁籤：技術文件 › 效率 - 說明。*

[![效率 - 說明](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

一份技術文件 *"Come YA-MS calcola l'efficienza di uno sciame"*（YA-MS 如何計算流星雨的效率），在程式中以淺色頁面顯示。它**逐步**說明效率是如何得出的，並針對每一個步驟說明其**出處**。這份文件目前**只有義大利文版**；本 wiki 在[效率計算](Efficiency-Calculation-zh-tw#模型)與[幾何與路徑損耗](Geometry-and-Path-Loss-zh-tw)中以中文提供其內容。

## 標籤

每個步驟都附有一個彩色標籤：

| 標籤 | 顏色 | 意義 |
|---|---|---|
| **FONTE**（來源） | 藍色 | 該步驟採用了所引用的資料來源；方括號中的數字對應文末的清單 |
| **RILIEVO**（驗證） | 綠色 | 程式與資料來源之間的比較及其結果 |
| **SCELTA**（選擇） | 橘色 | 程式本身的選擇，並非取自資料來源：有待實際上線的經驗驗證 |

## 章節

| 章節 | 內容 |
|---|---|
| 1. 引言 | 目的、標籤、效率的意義（OH5IY、MCG_MS；YA-MS 使用實際路徑） |
| 2. 反射發生在哪裡：E 層 | 餘跡位於 80–120 km；餘跡高度 = Collm 直方圖的眾數（驗證：2026 年 11 月 5 日為 89.5 km） |
| 3. 路徑幾何 | 地球與中點；天線仰角（文章公式）；共同區域及其界限；Hot A / Hot B；天線波瓣（DL6WU、Kraus、W4RNL） |
| 4. 流星雨的輻射點 | 輻射點位置（IMO 2026/2027）、峰值日期（IMO 或太陽黃經）、活動曲線 |
| 5. 反射條件 | 鏡面反射（McKinley）、高斯容許值 0.05 rad、最佳指向（SM6FHZ）、DH9GCD 公式 |
| 6. 從單一點到效率 | 每 15 km 一個反射點、每個點的權重、百分比；與 QTFGUI（DJ5HG）的比較 |
| 7. 解讀結果 | A / B 側、路徑指數、輻射點顏色、PREV 區域、從天線看出去的剖面 |
| 8. 工作頻率與路徑損耗 | λ³ / λ² 法則、從雷達到業餘頻段、路徑損耗的參考值 |
| 9. 已知限制 | 僅限欠密餘跡、等向性天線、工作值 |
| 10. 資料來源 | 17 個編號的資料來源 |

## 按鈕

| 按鈕 | 作用 |
|---|---|
| **匯出為 Word (.docx)...** | 將 `data/efficienza_spiegazione.docx` 的副本儲存到您選擇的位置（建議檔名 *YA-MS - calcolo dell'efficienza.docx*） |
| **以 Word 開啟** | 以 Word 文件的預設程式（Word、LibreOffice 等）開啟同一個 `.docx` |

## 檔案

| 檔案 | 內容 |
|---|---|
| `data/efficienza_spiegazione.txt` | 頁籤中顯示的文字，每行一個區塊（`TITLE`、`SUB`、`H1`、`H2`、`P`、`TAG|FONTE|…`、`TAG|RILIEVO|…`、`TAG|SCELTA|…`、`EQ`、`LI`、`SRC`） |
| `data/efficienza_spiegazione.docx` | Word 版本 |
| `doc/YA-MS_manuale_calcoli.docx` | **計算手冊**：所有方程式（Word 方程式編輯器），附編號與出處 |

這兩份文件以 `tools/build_spiegazione.py data` 與 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` 從原始碼重新產生。
