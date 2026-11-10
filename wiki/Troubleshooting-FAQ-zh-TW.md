[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · **中文 (繁體)**

# 疑難排解與常見問題

## 安裝與啟動

### Windows SmartScreen 顯示「Windows 已保護您的電腦」
本程式未使用商業憑證簽署。點選*其他資訊* → *仍要執行*。請只從 [Releases](https://github.com/ic8tem/YA-MS/releases) 頁面下載。

### macOS 無法打開（來自未識別的開發者）
YA-MS 未經 Apple 簽署，因此 **Gatekeeper** 會在首次執行時阻擋它。在 `.dmg` 中，**按右鍵點選「Installa YA-MS.command」→ 打開**並確認。該指令碼會移除 `~/YA-MS/YA-MS.app` 上「從網際網路下載」的隔離標記並開啟它。如果 macOS 仍然拒絕，請開啟*系統設定 → 隱私權與安全性*，然後點選*強制打開*。

### macOS 該用哪個 .dmg
M1/M2/M3/M4 處理器用 `-mac-apple-silicon.dmg`，Intel Mac 用 `-mac-intel.dmg`（蘋果選單 → *關於這台 Mac* 可查看是哪種）。

### Linux 應用程式選單中沒有 YA-MS
從解壓縮出的資料夾（而不是 `~/YA-MS`）中執行 `./installa.sh`。有些桌面環境需要登出後重新登入才會顯示新項目。您隨時可以用 `~/YA-MS/YA-MS` 啟動程式。

### 缺少歐洲地圖
*歐洲地圖無法使用（首次啟動需要網路）。* Natural Earth 地圖在首次啟動時下載到 `data/mappa`。請連線到網際網路並重新啟動 YA-MS。

## 顯示

### Linux 下日文顯示為方框
您的系統缺少 CJK 字型（中文、日文、韓文）。請安裝 **Noto CJK** 字型並重新啟動 YA-MS。阿拉伯文、希伯來文、烏爾都文、印地文和孟加拉文也會出現同樣的情況：在 Debian、Ubuntu 和 Raspberry Pi OS 上還需安裝 `fonts-noto-core`。

| 發行版 | 指令 |
|---|---|
| Debian、Ubuntu、Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### 文字太小，或圖表沒有空間
使用**字型**滑桿（100–300 %），並用**控制**收合控制項列。請參閱[設定](Settings-and-Data-Folder-zh-TW#字型與控制)。

### 夜間螢幕太亮
在**主題**清單中選擇**夜間**或**黑色**。

## 網際網路與雷達資料

### 「無網際網路連線」訊息
當所有資料來源都無法存取時，YA-MS 會**只顯示一次**該訊息；狀態列變為紅色。程式繼續使用**最後儲存的資料**運作，並每 5 分鐘自動重試；網路恢復後會顯示*連線已恢復。*。無需任何操作。

### 雷達流量中的橘色警告「無法讀取流量縱軸刻度 …」
Collm 雷達每天都會變更縱軸刻度，YA-MS 從圖表標籤中讀取它。如果某個標籤無法讀取，程式會使用已校準的刻度 0–1200 流星/小時，並提示**數值需核實**。通常下一個小時的圖表就能正確讀取。如果連續多個小時看到*圖表格式已變化*或*未在預期位置找到流量座標軸*，表示雷達變更了圖表格式：請[回報此問題](Contributing-and-Contacts-zh-TW)。

### 「高度圖表的刻度已變化」
高度統計（眾數、平均值、中位數）仍然有效；只有高度直方圖的絕對計數不再有效。

### 「雷達流量：無資料」
在[雷達流量](Radar-Flux-zh-TW)中點選**立即下載**，並檢查 `data/fonti_radar.csv` 中 Collm 是否為 `attivo=1`。

### RMOB 為什麼自動下載是關閉的
RMOB 要求**自動程式不要抓取其檔案**。請只在 RMOB 給予您許可後，再啟用*每 5 分鐘自動下載*。在此之前，請使用**立即下載 RMOB** 或**從磁碟載入 RMOB 檔案...**。請參閱[試驗性預報](Experimental-Forecasts-zh-TW#rmob-與自動程式)。

### RMOB「無法辨識檔案格式」或讀取的小時很少
請使用觀測者的月度文字檔（`NAME_MMYYYYrmob.TXT`）或只含一位觀測者的公報表格。擬合指數至少需要與 Collm 資料（昨天和今天）有 3 個共同小時。

## 計算

### 「本台網格座標無效」 / 「對方電台網格座標無效」
網格座標必須為 4、6 或 8 位（例如 `JN70`、`JN70CN`、`JN70CN12`）。

### 「沒有 E 層公共區域」
路徑長度超過餘跡高度處涵蓋距離的兩倍（波瓣仰角 0°、餘跡高度 89.5 km 時約為 2 × 1062 km）：單次流星散射跳躍無法涵蓋。提高**波瓣仰角**會進一步縮短涵蓋距離。

### Hot A / Hot B 顯示為灰色
當天線指向 DX 時，它們已經位於**您的天線波瓣內**：無需轉動天線。請參閱[天穹](Sky-View-zh-TW#警告)。

### 效率與 MCG_MS 或 MS-Soft 的結果不同
YA-MS 使用實際路徑和自己的模型；OH5IY 和 MCG_MS 的刻度沒有詳細的文件說明。請比較小時和趨勢，而不是絕對百分比，並請參閱[模型](Efficiency-Calculation-zh-TW#模型)。

### GRAVES 波束掃過的時間似乎有偏移
波束序列根據電腦時鐘計算：請將其與 NTP 伺服器同步。GRAVES 指揮站有時也會把序列平移幾個步進；這些細節是需要透過收聽來確認的預測。

## 其他問題

**YA-MS 是免費的嗎？** 是的，它是一套為業餘無線電愛好者設計的免費程式。

**它能控制我的旋轉器或無線電機嗎？** 不能。YA-MS 是預報和規劃工具；進行 QSO 請使用您的數位模式程式（例如 MSHV、WSJT-X）。

**它能用於 432 MHz 以上嗎？** 頻段清單止於 432 MHz（28、50、70、144、222、432）。試驗性預報接受 28 至 1300 MHz 的任意頻率，但其所用的 SM6FHZ 規則來自 144 和 432 MHz 上的經驗。

**出了問題。** 請寫信給作者，說明您的作業系統、YA-MS 版本以及您做了什麼：請參閱[參與貢獻與聯絡方式](Contributing-and-Contacts-zh-TW)。
