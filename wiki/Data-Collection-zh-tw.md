[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · **中文 (繁體)**

# 資料收集

*頁籤：Live 與即時資料 › 資料收集。*

[![資料收集](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## 三路 cluster 資料串流

這個頁籤從三路 telnet 資料串流收集**流星散射 spot**，每一路各有自己的子頁籤：

| 子頁籤 | 預設 | 說明 |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 自選的 cluster。ON0DXK 會篩除 VHF 頻段：以 `set/filter dxbm/pass 6`（然後 4、2…）啟用。 |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network（7000 = CW/RTTY，7001 = FT8）。Skimmer 很少能解碼 MS 模式。 |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | 轉送 **PSKReporter** spot 的 DM4X cluster：WSJT-X 與 MSHV 的 MSK144 解碼會送到這裡。 |
| **已收集的 MS spot** | – | 已接受之 spot 的表格，最新的在最前面。 |

每一路資料串流都有主機、連接埠、登入後送出的指令、*重新連線*、*啟動時連線*、一個主控台，以及一行用來送出指令的輸入欄。請在頂端填寫**登入用的呼號**。一條狀態列顯示三個連線階段的狀態（綠點 = 已連線）。變更語言或配色方案時，連線會保持開啟。

## 篩選器（占視窗的 40 %）

- **選用的本機篩選：** 低於 **27990.0 kHz** 的 cluster 行會立即捨棄（不顯示，也不儲存）。
- **第 1 項準則 – 典型 MS 頻率：** 50190–50300、70100–70400、144290–144399 kHz。落在這些頻率窗內的 spot 即使沒有寫出模式名稱也會被接受，除非備註中聲明了其他傳播方式：`<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`。頻率窗與標記都可以編輯。
- **第 2 項準則 – MS 模式：** 在頻率窗之外，或帶有上述標記之一時，只有包含 **MSK144、FSK441、FSK41、PSK2K、JTMS、JT6M**（僅用於 MS 的數位模式）或 **\<MS\>** 的 spot 才會保留，不分大小寫。每個字詞都可以停用、新增與移除；每個都有自己的計數器。
- **頻段** 28、50、70、144、222、432 MHz；可對貼上的一行進行**篩選測試**；**計數器**。

## 網格座標與儲存

缺少的網格座標，或只有 4 個字元的網格座標，會從 **CALL3** 資料庫（`data/call3.txt`，JTDX 的檔案，超過一百萬個呼號）取得；CALL3 中的網格座標一律優先於 4 個字元的網格座標。已接受的 spot 儲存在 `data/spot_ms`，每天一個 CSV 檔案，並提供給[即時通訊](Live-Traffic-zh-tw)地圖使用。
