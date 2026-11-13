[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · **中文 (繁體)**

# 資料收集

*分頁：實況與即時資料 › 資料收集。*

[![資料收集](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## 四個資料來源

本分頁從三路 telnet 資料流和 PSKReporter 的 MQTT 資料來源中收集**流星散射 spot**，每路各佔一個子分頁：

| 子分頁 | 預設 | 說明 |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 可自選 cluster。ON0DXK 預設篩除了 VHF 頻段：用 `set/filter dxbm/pass 6`（然後 4、2…）啟用。 |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network（7000 = CW/RTTY，7001 = FT8）。Skimmer 很少能解碼 MS 模式。 |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X 的 cluster，轉發 **PSKReporter** 的 spot：WSJT-X 和 MSHV 的 MSK144 解碼結果會出現在這裡。 |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | 透過 **MQTT** 取得的 PSKReporter 即時 spot（M0LTE 提供的服務）：無需登入，每筆 spot 已帶有發射台和接收台的網格座標。預設主題：6 m、4 m、2 m、1.25 m、70 cm 上的 MSK144 以及 2 m 上的 FSK441（`pskr/filter/v2/band/mode/#`）；*預設主題*可將其還原。 |
| **已收集的 MS spot** | – | 已接受的 spot 表格，最新的在前。 |

每路資料流都有主機、連接埠、登入後傳送的指令、*重新連線*、*啟動時連線*、一個主控台以及一列用於傳送指令的輸入框。請在頂部填寫**登入呼號**。MQTT 資料來源有主機、連接埠、主題（每行一個或用 `;` 分隔）、*重新連線*和*啟動時連線*（預設關閉），以及一個顯示已接收 spot 的主控台；其 spot 同樣經過該篩選器。一條狀態列顯示四個資料來源的狀態（綠點 = 已連線）。變更語言或配色方案時，連線工作階段保持開啟。

## 篩選器（佔視窗的 40 %）

- **可選的本機篩選：** 低於 **27990.0 kHz** 的 cluster 行會被立即捨棄（不顯示，也不儲存）。
- CW 報點會被立即丟棄（註解中有 CW 或 WPM，或 28000-28070 kHz）：除非標有 <MS>，否則不在主控台顯示也不儲存。可以關閉此核取方塊。

採用 LIVETROPOVHF 規則的 CALL3 資料庫。「立即更新」從 MMMonVHF 下載 CALL3.TXT（至少 100,000 行有效，舊檔案留在 data/call3.bak）；勾選「每 7 天自動更新」則在啟動時進行。檔案之上依序生效：手動條目（data/CALL3-MANUALE.TXT）、叢集修正（報告者自報的 6 碼定位碼）、加入的檔案（data/CALL3-AGGIUNTE），然後是 CALL3.TXT 和即時學到的 6 碼定位碼（data/LOC6.TXT）。收到的 4 碼定位碼，或以 LL、MM 結尾的定位碼，以資料庫中的 6 碼定位碼取代；攜帶式電台（帶斜線）只認完全一致的條目。
- 距離小於 500 公里的電台之間的報告會立即捨棄，因為在此距離上通聯為直達或對流層傳播，而不是流星餘跡（meteor scatter）：它們不會出現在主控台中，也不會被儲存。缺少定位碼時保留該報告。距離可在核取方塊下方修改。
- **第 1 條標準 – 典型 MS 頻率：** 50190–50300、70100–70400、144290–144399 kHz。落在這些視窗內的 spot 即使沒有寫模式名稱也會被接受，除非註解中聲明了其他傳播方式：`<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`。視窗和標籤都可以編輯。
- **第 2 條標準 – MS 模式：** 在視窗之外，或帶有上述某個標籤時，只有包含 **MSK144、FSK441、FSK41、PSK2K、JTMS、JT6M**（僅用於 MS 的數位模式）或 **\<MS\>** 的 spot 才會保留，不分大小寫。各個關鍵字可以停用、新增和刪除；每個都有自己的計數器。
- **頻段** 28、50、70、144、222、432 MHz；可對貼上的一行進行**篩選器測試**；**計數器**。

## 網格座標與儲存

缺少的網格座標或只有 4 位的網格座標，從 **CALL3** 資料庫（`data/call3.txt`，JTDX 檔案，超過一百萬個呼號）中取得，CALL3 中的座標總是優先於 4 位網格座標。已接受的 spot 儲存在 `data/spot_ms` 中，每天一個 CSV 檔案，並供[即時通訊](Live-Traffic-zh-tw)地圖使用。
