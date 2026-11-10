[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · **中文**

# 故障排除与常见问题

## 安装与启动

### Windows SmartScreen 显示“Windows 已保护你的电脑”
本程序未使用商业证书签名。点击*更多信息* → *仍要运行*。请只从 [Releases](https://github.com/ic8tem/YA-MS/releases) 页面下载。

### macOS 无法打开（来自身份不明的开发者）
YA-MS 未经 Apple 签名，因此 **Gatekeeper** 会在首次运行时阻止它。在 `.dmg` 中，**右键单击“Installa YA-MS.command” → 打开**并确认。该脚本会移除 `~/YA-MS/YA-MS.app` 上“从互联网下载”的隔离标记并打开它。如果 macOS 仍然拒绝，请打开*系统设置 → 隐私与安全性*，然后点击*仍要打开*。

### macOS 该用哪个 .dmg
M1/M2/M3/M4 处理器用 `-mac-apple-silicon.dmg`，Intel Mac 用 `-mac-intel.dmg`（苹果菜单 → *关于本机*可查看是哪种）。

### Linux 应用程序菜单中没有 YA-MS
从解压出的文件夹（而不是 `~/YA-MS`）中运行 `./installa.sh`。有些桌面环境需要注销后重新登录才会显示新条目。您始终可以用 `~/YA-MS/YA-MS` 启动程序。

### 缺少欧洲地图
*欧洲地图不可用（首次启动需要网络）。* Natural Earth 地图在首次启动时下载到 `data/mappa`。请连接互联网并重新启动 YA-MS。

## 显示

### Linux 下日文显示为方框
您的系统缺少 CJK 字体。请安装 **Noto CJK** 字体并重新启动 YA-MS：

| 发行版 | 命令 |
|---|---|
| Debian、Ubuntu、Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### 文字太小，或图表没有空间
使用**字体**滑块（100–300 %），并用**控制**折叠控件行。参见[设置](Settings-and-Data-Folder-zh#字体与控制)。

### 夜间屏幕太亮
在**主题**列表中选择**夜间**或**黑色**。

## 互联网与雷达数据

### “无互联网连接”消息
当所有数据源都无法访问时，YA-MS 会**只显示一次**该消息；状态栏变为红色。程序继续使用**最后保存的数据**工作，并每 5 分钟自动重试；网络恢复后会显示*连接已恢复。*。无需任何操作。

### 雷达流量中的橙色警告“无法读取流量纵轴刻度 …”
Collm 雷达每天都会更改纵轴刻度，YA-MS 从图表标签中读取它。如果某个标签无法读取，程序会使用已校准的刻度 0–1200 流星/小时，并提示**数值需核实**。通常下一个小时的图表就能正确读取。如果连续多个小时看到*图表格式已变化*或*未在预期位置找到流量坐标轴*，说明雷达更改了图表格式：请[报告此问题](Contributing-and-Contacts-zh)。

### “高度图表的刻度已变化”
高度统计（众数、平均值、中位数）仍然有效；只有高度直方图的绝对计数不再有效。

### “雷达流量：无数据”
在[雷达流量](Radar-Flux-zh)中点击**立即下载**，并检查 `data/fonti_radar.csv` 中 Collm 是否为 `attivo=1`。

### RMOB 为什么自动下载是关闭的
RMOB 要求**自动程序不要抓取其文件**。请只在 RMOB 给予您许可后，再启用*每 5 分钟自动下载*。在此之前，请使用**立即下载 RMOB** 或**从磁盘载入 RMOB 文件...**。参见[试验性预报](Experimental-Forecasts-zh#rmob-与自动程序)。

### RMOB“无法识别文件格式”或读取的小时很少
请使用观测者的月度文本文件（`NAME_MMYYYYrmob.TXT`）或只含一位观测者的公报表格。拟合指数至少需要与 Collm 数据（昨天和今天）有 3 个共同小时。

## 计算

### “本台网格坐标无效” / “对方电台网格坐标无效”
网格坐标必须为 4、6 或 8 位（例如 `JN70`、`JN70CN`、`JN70CN12`）。

### “没有 E 层公共区域”
路径长度超过余迹高度处覆盖距离的两倍（波瓣仰角 0°、余迹高度 89.5 km 时约为 2 × 1062 km）：单次流星散射跳跃无法覆盖。提高**波瓣仰角**会进一步缩短覆盖距离。

### Hot A / Hot B 显示为灰色
当天线指向 DX 时，它们已经位于**您的天线波瓣内**：无需转动天线。参见[天穹](Sky-View-zh#警告)。

### 效率与 MCG_MS 或 MS-Soft 的结果不同
YA-MS 使用实际路径和自己的模型；OH5IY 和 MCG_MS 的刻度没有详细的文档说明。请比较小时和趋势，而不是绝对百分比，并参见[模型](Efficiency-Calculation-zh#模型)。

### GRAVES 波束扫过的时间似乎有偏移
波束序列根据电脑时钟计算：请将其与 NTP 服务器同步。GRAVES 指挥站有时也会把序列平移几个步进；这些细节是需要通过收听来确认的预测。

## 其他问题

**YA-MS 免费吗？** 是的，它是一款面向业余无线电爱好者的免费程序。

**它能控制我的转台或电台吗？** 不能。YA-MS 是预报和规划工具；进行 QSO 请使用您的数字模式程序（例如 MSHV、WSJT-X）。

**它能用于 432 MHz 以上吗？** 频段列表止于 432 MHz（28、50、70、144、222、432）。试验性预报接受 28 至 1300 MHz 的任意频率，但其所用的 SM6FHZ 规则来自 144 和 432 MHz 上的经验。

**出了问题。** 请写信给作者，说明您的操作系统、YA-MS 版本以及您做了什么：参见[参与贡献与联系方式](Contributing-and-Contacts-zh)。
