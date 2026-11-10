[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · **中文 (繁體)**

# 安裝

所有安裝套件都在 **[Releases](https://github.com/ic8tem/YA-MS/releases)** 頁面上（下列檔名中的 `x.y.z` 為版本號，例如 `1.2.0`）。不需要編譯，也不需要另外安裝任何東西：每個套件都已內含 .NET 8 執行環境。

| 系統 | 檔案 | 安裝位置 |
|---|---|---|
| Windows（64 位元） | `YA-MS-x.y.z-windows-x64-setup.exe`（安裝程式） | `C:\YA-MS` |
| Windows（64 位元），免安裝版 | `YA-MS-x.y.z-windows-x64-portatile.zip` | 任何您有寫入權限的資料夾 |
| Windows（32 位元，Windows 10/11） | `YA-MS-x.y.z-windows-x86-setup.exe` 或 `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux（64 位元） | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5、400/500（Raspberry Pi OS 64 位元） | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4（Raspberry Pi OS 32 位元） | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS，Apple 晶片（M1/M2/M3/M4） | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS，Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**程式與它的 `data` 資料夾永遠放在一起**，位於 YA-MS 資料夾中：所有資料與設定都在那裡（不使用 AppData，也不使用系統資料夾）。請參閱[設定與資料資料夾](Settings-and-Data-Folder-zh-tw)。

## Windows

### 安裝程式
1. 下載 `YA-MS-x.y.z-windows-x64-setup.exe` 並執行。
2. 如果 **SmartScreen** 顯示「Windows 已保護您的電腦」：按*其他資訊* → *仍要執行*（本程式未使用商業憑證簽署）。
3. YA-MS 會安裝到 **`C:\YA-MS`**，**不需要系統管理員權限**，並在「開始」功能表建立圖示；若有勾選，也會在桌面建立圖示。

### 免安裝版
將 `YA-MS-x.y.z-windows-x64-portatile.zip` 解壓縮到任意位置（一個您有寫入權限的資料夾，不要放在 *Program Files* 中），然後執行 `YA-MS.exe`。您可以把整個資料夾複製到 USB 隨身碟或另一台電腦上。

## Linux

1. 解壓縮 `YA-MS-x.y.z-linux-x64.tar.gz`。
2. 在解壓縮出來的資料夾中執行：
   ```sh
   ./installa.sh
   ```
3. 這個指令稿會把 YA-MS 複製到 **`~/YA-MS`**（不需要 root 權限），並將 **YA-MS** 加入應用程式選單（*HamRadio* 類別）。也可以用 `~/YA-MS/YA-MS` 啟動。

顯示日文可能需要 Noto CJK 字型：請參閱[疑難排解](Troubleshooting-FAQ-zh-tw#linux-下日文顯示為方框)。

## Raspberry Pi

步驟與 Linux 相同：解壓縮 `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz`（32 位元的 Raspberry Pi OS 則用 `-32bit`），然後在解壓縮出來的資料夾中執行 `./installa.sh`。

- 要查看您的系統類型，請在終端機中輸入 `uname -m`：`aarch64` → 64 位元套件，`armv7l` → 32 位元套件。
- 支援：Raspberry Pi 2（僅 32 位元）、3、4、5、400 與 500，須使用含桌面環境的 Raspberry Pi OS。**不支援：** Pi Zero / Zero W 與 Pi 1（ARMv6 處理器，.NET 無法在上面執行）；Pi Zero 2 W 可使用 64 位元套件，但 512 MB 記憶體相當吃緊。
- 建議使用至少 2 GB 記憶體的 Pi 4 或 5；第一次啟動會比在 PC 上多花幾秒鐘。

## macOS

1. 選擇正確的檔案：M1/M2/M3/M4 處理器用 `-mac-apple-silicon.dmg`，Intel Mac 用 `-mac-intel.dmg`。
2. 開啟 `.dmg`，**在「Installa YA-MS.command」上按右鍵 → 打開**並確認。
3. 這個指令稿會把 `YA-MS.app` 複製到 **`~/YA-MS`** 並開啟它。

本程式未經 Apple 簽署，因此第一次執行時 macOS 會要求確認；請參閱[疑難排解](Troubleshooting-FAQ-zh-tw#macos-無法打開因為它來自未識別的開發者)。

## 第一次啟動

- **歐洲地圖**（Natural Earth 海岸線與國界）會在第一次啟動時自動下載到 `data/mappa`：只需要連上網路一次。
- **雷達資料**（Collm、Sodankylä）會立即下載，之後每 5 分鐘檢查一次。
- 如果系統語言是 36 種可用語言之一，介面就會以系統語言啟動，否則使用義大利文；可在右上角變更（請參閱[設定](Settings-and-Data-Folder-zh-tw#介面語言)）。

## 更新

將新版本**直接安裝在舊版本上**（同一個安裝程式，同一個資料夾）。設定（`config.ini`）、通量封存檔與地圖都會保留在 `data` 中。`data/lingue` 中的翻譯檔案若新版的較新，就會被取代。

## 從原始碼建置（僅限開發者）

安裝程式由 GitHub Actions（`.github/workflows/build.yml`）在 `release` 分支每次更新時產生（版本號取自 `VERSION` 檔案），同時也會建立發行版本 `vX.Y.Z`。在本機建置：

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # 或 linux-x64、linux-arm64、linux-arm、osx-arm64
```

文件以 `tools/build_spiegazione.py data` 與 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` 重新產生。

下一步：[入門](Getting-Started-zh-tw)。
