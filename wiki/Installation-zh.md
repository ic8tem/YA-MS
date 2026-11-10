[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · **中文** · [中文 (繁體)](Installation-zh-tw)

# 安装

所有安装包都在 **[Releases](https://github.com/ic8tem/YA-MS/releases)** 页面上（下面文件名中的 `x.y.z` 为版本号，例如 `1.2.0`）。无需编译，也无需另外安装任何东西：每个安装包都已包含 .NET 8 运行时。

| 系统 | 文件 | 安装位置 |
|---|---|---|
| Windows（64 位） | `YA-MS-x.y.z-windows-x64-setup.exe`（安装程序） | `C:\YA-MS` |
| Windows（64 位），便携版 | `YA-MS-x.y.z-windows-x64-portatile.zip` | 任何您有写入权限的文件夹 |
| Windows（32 位，Windows 10/11） | `YA-MS-x.y.z-windows-x86-setup.exe` 或 `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux（64 位） | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5、400/500（Raspberry Pi OS 64 位） | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4（Raspberry Pi OS 32 位） | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS，Apple 芯片（M1/M2/M3/M4） | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS，Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**程序与其 `data` 文件夹始终放在一起**，位于 YA-MS 文件夹中：所有数据和设置都在那里（不使用 AppData，不使用系统文件夹）。参见[设置与数据文件夹](Settings-and-Data-Folder-zh)。

## Windows

### 安装程序
1. 下载 `YA-MS-x.y.z-windows-x64-setup.exe` 并运行。
2. 如果 **SmartScreen** 显示“Windows 已保护你的电脑”：点击*更多信息* → *仍要运行*（本程序未使用商业证书签名）。
3. YA-MS 安装到 **`C:\YA-MS`**，**无需管理员权限**，并在开始菜单中创建图标；如果勾选，还会在桌面创建图标。

### 便携版
将 `YA-MS-x.y.z-windows-x64-portatile.zip` 解压到任意位置（一个您有写入权限的文件夹，不要放在 *Program Files* 中），然后运行 `YA-MS.exe`。您可以把整个文件夹复制到 U 盘或另一台电脑上。

## Linux

1. 解压 `YA-MS-x.y.z-linux-x64.tar.gz`。
2. 在解压出的文件夹中运行：
   ```sh
   ./installa.sh
   ```
3. 该脚本会把 YA-MS 复制到 **`~/YA-MS`**（无需 root 权限），并将 **YA-MS** 添加到应用程序菜单（*HamRadio* 类别）。也可以用 `~/YA-MS/YA-MS` 启动。

显示日文可能需要 Noto CJK 字体：参见[故障排除](Troubleshooting-FAQ-zh#linux-下日文显示为方框)。

## Raspberry Pi

步骤与 Linux 相同：解压 `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz`（32 位 Raspberry Pi OS 上则用 `-32bit`），然后在解压出的文件夹中运行 `./installa.sh`。

- 要查看您的系统类型，在终端中输入 `uname -m`：`aarch64` → 64 位安装包，`armv7l` → 32 位安装包。
- 支持：Raspberry Pi 2（仅 32 位）、3、4、5、400 和 500，需使用带桌面的 Raspberry Pi OS。**不支持：** Pi Zero / Zero W 和 Pi 1（ARMv6 处理器，.NET 无法在其上运行）；Pi Zero 2 W 可使用 64 位安装包，但 512 MB 内存比较紧张。
- 推荐使用至少 2 GB 内存的 Pi 4 或 5；首次启动会比在 PC 上多花几秒钟。

## macOS

1. 选择正确的文件：M1/M2/M3/M4 处理器用 `-mac-apple-silicon.dmg`，Intel Mac 用 `-mac-intel.dmg`。
2. 打开 `.dmg`，**右键单击“Installa YA-MS.command” → 打开**并确认。
3. 该脚本会把 `YA-MS.app` 复制到 **`~/YA-MS`** 并打开它。

本程序未经 Apple 签名，因此首次运行时 macOS 会要求确认；参见[故障排除](Troubleshooting-FAQ-zh#macos-无法打开来自身份不明的开发者)。

## 首次启动

- **欧洲地图**（Natural Earth 海岸线和国界）会在首次启动时自动下载到 `data/mappa`：只需联网一次。
- **雷达数据**（Collm、Sodankylä）会立即下载，之后每 5 分钟检查一次。
- 如果系统语言是六种可用语言之一，界面将以系统语言启动，否则使用意大利语；可在右上角更改（参见[设置](Settings-and-Data-Folder-zh#界面语言)）。

## 更新

将新版本**直接安装在旧版本之上**（同一个安装程序，同一个文件夹）。设置（`config.ini`）、流量档案和地图都保留在 `data` 中。`data/lingue` 中的翻译文件如果新版本的更新，则会被替换。

## 从源代码构建（仅限开发者）

安装包由 GitHub Actions（`.github/workflows/build.yml`）在 `release` 分支每次更新时生成（版本号取自 `VERSION` 文件），同时会创建发布版本 `vX.Y.Z`。本地构建：

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # 或 linux-x64、linux-arm64、linux-arm、osx-arm64
```

文档通过 `tools/build_spiegazione.py data` 和 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` 重新生成。

下一步：[入门](Getting-Started-zh)。
