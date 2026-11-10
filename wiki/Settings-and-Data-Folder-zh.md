[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · **中文**

# 设置与数据文件夹

## 选项卡栏

在选项卡栏的右端，从右到左依次为：

| 控件 | 作用 |
|---|---|
| **界面语言**（列表） | 界面语言；参见[界面语言](#界面语言) |
| **主题**（列表） | 配色方案；参见[配色方案](#配色方案) |
| **控制 ▴ / ▾** | 折叠或展开选项卡上方的三行控件；参见[字体与控制](#字体与控制) |

更改语言或主题时会保存设置，并以相同的位置和大小、在同一个选项卡上**重建窗口**：无需重启。

## 界面语言

六种界面语言：

| 语言 | 代码 | 文件 |
|---|---|---|
| Italiano | `it` | 无：意大利语是基础语言（即键） |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

首次启动时，如果**系统语言**是其中之一，YA-MS 就使用系统语言，否则使用意大利语。数字和日期遵循所选语言的格式（例如英语用小数点，意大利语和德语用逗号）。翻译文件中缺少的文字以意大利语显示。在 Linux 上，日语需要合适的字体：参见[故障排除](Troubleshooting-FAQ-zh#linux-下日文显示为方框)。

[效率 - 说明](Efficiency-Explanation-zh)文档和计算手册为意大利语。

## 配色方案

**主题**列表提供 12 种方案，与作者的 EME 程序 YAEC 相同，另加 YA-MS 原有的配色：

| 方案 | 说明 |
|---|---|
| **浅色** | 默认 |
| **夜间** | 深蓝色调，适合夜间使用 |
| **黑色** | 黑色背景，适合暗处和 OLED 屏幕 |
| 粉彩浅蓝 · 粉彩橙 · 粉彩海蓝 · 粉彩绿 · 粉彩粉红 · 粉彩淡紫 · 粉彩靛蓝 · 粉彩棕 | 八种浅色粉彩方案 |
| **流星余迹** | YA-MS 原有风格（至 1.2.0 版）：夜紫色，配以浅蓝、紫、浅绿、黄和橙色 |

方案适用于所有选项卡，并保存在 `config.ini` 中（键 `tema`）。

## 字体与控制

- **字体**（第一行控件末尾）：将**所有文字**从 **100 % 放大到 300 %**，步长 10 %；线条、圆和地图保持原有大小。使用大字体时，选项卡会换到第二行，卡片也会变大。
- **控制**：在使用大字体或屏幕较小时，折叠三行控件，为地图和图表腾出空间。该状态会被记住。

## 数据文件夹

所有数据和设置都在**程序旁**的一个 **`data`** 文件夹中——不使用 AppData，不使用系统文件夹：

| 系统 | 程序 | 数据 |
|---|---|---|
| Windows（安装程序） | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows（便携版） | 解压到的位置 | `YA-MS.exe` 旁的 `data` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data`（在应用旁边） |

启动时，程序会在需要时创建该文件夹，并只复制**缺失的**初始文件：您修改过的文件永远不会被覆盖。`data/lingue` 中的翻译文件属于程序文件，如果新版本的文件更新，则会被替换。

### 可以编辑的文件

| 文件 | 内容 |
|---|---|
| `sciami.csv` | 流星雨目录（IMO 数值和工作值）；参见[流星雨](Showers-zh#编辑目录) |
| `massimi_imo.csv` | IMO 公布的峰值日期和时间（2026、2027）：在此**添加新的年份** |
| `ant_radiante.csv` | 反日点源的位置（IMO 表 6） |
| `fonti_radar.csv` | 雷达地址；`attivo=1` 下载，`0` 忽略 |
| `regole_sperimentali.csv` | 所用的常数和规则，每项注明来源（参考用） |
| `lingue/<code>.txt` | 界面翻译；参见[参与贡献](Contributing-and-Contacts-zh#翻译) |
| `config.ini` | 设置（见下文） |

### 程序创建的文件

| 文件 / 文件夹 | 内容 |
|---|---|
| `config.ini` | 设置 |
| `flusso_collm.csv` | Collm 流量的逐时档案 |
| `quote_collm.csv` | 余迹高度档案 |
| `radar/` | 最新的雷达图像和 RMOB 文件 |
| `mappa/` | Natural Earth 海岸线和国界（首次启动时下载） |
| `adif_quadrati.csv` | 最近一次载入的 ADIF 中的方格 |
| `efficienza_spiegazione.txt`、`.docx` | [说明文档](Efficiency-Explanation-zh) |

## config.ini

纯文本文件，每行一个 `key=value`（以 `#` 或 `;` 开头的行为注释）。程序在关闭时写入该文件，因此**请在 YA-MS 关闭时编辑它**。您可能需要了解的键：

| 键 | 默认 | 含义 |
|---|---|---|
| `mio_locator`、`mia_quota_m` | JN70CN, 62 | 本台网格坐标和高度（m） |
| `dx_locator`、`dx_quota_m` | JO62QM, 50 | 对方电台网格坐标和高度（m） |
| `banda_MHz` | 144 | 频段（28、50、70、144、222、432） |
| `quota_scie_km`、`quota_da_radar` | 90, 1 | 余迹高度（km）；1 = 使用 Collm 众数 |
| `elevazione_lobo_gradi` | 0 | 波瓣仰角（°） |
| `boom_m` | 4.6 | 八木天线横梁长度（m） |
| `hot_spot_km` | 150 | Hot A / Hot B 到中点的距离（30–400 km） |
| `lingua` | 系统 / `it` | 语言代码（`it`、`en`、`ru`、`ja`、`de`、`nl`） |
| `tema` | `chiaro` | 配色方案：`chiaro`（浅色）、`scuro`（夜间）、`nero`（黑色）、`pastello-azzurro`、`pastello-arancione`、`pastello-acquamarina`、`pastello-verde`、`pastello-rosa`、`pastello-lilla`、`pastello-indaco`、`pastello-marrone`、`scia`（流星余迹） |
| `carattere_pct` | 100 | 字体大小（100–300 %） |
| `comandi_visibili` | 1 | 1 = 显示控件行，0 = 折叠 |
| `mostra_mappa`、`vista_alto` | 1, 1 | 天穹中的欧洲地图、俯视图 |
| `aggiornamento_automatico` | 1 | 每 5 分钟自动检查数据源 |
| `esponente_lambda` | 3 | 雷达流量选项卡中的 λ 指数 |
| `potenza_W`、`guadagno_dBi`、`sensibilita_dBm`、`densita_esponente_q` | 400, 14, −130, 14 | 链路预算输入 |
| `prev_frequenza_MHz`、`prev_esponente`、`prev_fattore_stazione` | 144, 3, 1 | 试验性预报：频率、k、K |
| `rmob_osservatore` | 空 | RMOB 观测者名称 |
| `rmob_automatico` | 0 | 自动下载 RMOB（仅在获得 RMOB 许可后启用） |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB 地址模板 |
| `graves_sequenza` | 0 | GRAVES 波束序列：0 = 0.8 s（2021），1 = 3.2 s（2007） |

## 隐私

YA-MS 不收集任何数据，也不显示广告。它只在下载公开数据时连接互联网：Collm 和 Sodankylä 雷达图像、Natural Earth 地图（首次启动时），以及在您要求时下载的 RMOB 文件。
