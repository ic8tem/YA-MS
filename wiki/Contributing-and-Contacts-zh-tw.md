[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · **中文 (繁體)**

# 參與貢獻與聯絡方式

YA-MS 靠著在實際上線中使用它的人們所提供的回報而不斷改進。每一項修正都會註明其來源。

## 聯絡方式

| | |
|---|---|
| 作者 | Costantino Cerrotta **IC8TEM** |
| 電子郵件 | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## 回報問題

在 **GitHub 上開一個 issue**，或寄一封電子郵件，並附上：

- 作業系統與 YA-MS 版本（見視窗標題）；
- 兩個網格座標、頻段與 UTC 時間；
- 您預期的結果與實際看到的結果（附上螢幕截圖會很有幫助）；
- 若是雷達問題，請附上[雷達通量](Radar-Flux-zh-tw)頁籤中顯示的訊息。

## 特別有用的內容

- **上線回報。** 效率或預報準確（或不準確）的時段與路徑。這個模型是實驗性的，需要與實際的 QSO 以及 MCG_MS / MS-Soft 比較。
- **RMOB 比對。** 您透過 [RMOB 比對](Experimental-Forecasts-zh-tw#rmob-比對)得到的電台因子 K 與指數 k 的數值，並附上您的頻段與電台條件。
- **附有來源的資料。** 更好的輻射點漂移、活動曲線、新的 IMO 峰值日期（`data/massimi_imo.csv`）、天線資料：請附上來源，它將會被引用。
- **雷達圖表的變更。** 如果 Collm 圖表的格式改變了，提供一份影像副本（`data/radar/`）有助於重新校準讀取方式。

## 翻譯

介面翻譯是位於 **`data/lingue/<code>.txt`** 的純文字檔（UTF-8），**任何人都可以修正**：

```
<Italian text><TAB><translation>
```

- 每行一筆；以 `#` 開頭的行為註解。
- 在兩個欄位中，兩個字元 `\n` 都表示換行。
- 請保留佔位符 `{0}`、`{1}`、… 及其格式（例如 `{0:F1}`、`{3:+0;-0}`），並依您的語言所需的順序排列。
- 缺少或空白的項目會以義大利文顯示。所有鍵值的清單在 `data/lingue/chiavi.txt`（由 `tools/estrai_chiavi.py` 產生，請勿編輯）。

在您安裝目錄的 `data/lingue` 資料夾中編輯檔案，然後重新啟動 YA-MS（或切換語言）即可看到結果。由於這些檔案**在每次更新時都會被新版本取代**，也請**寄送您的修正**（透過電子郵件，或在 GitHub 上提交 pull request 到 `data/lingue/`），以便納入下一個版本。

本 wiki 提供 36 種語言版本（English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)）；同樣歡迎對 wiki 頁面提出修正。
