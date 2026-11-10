[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · **中文**

# 数据收集

*选项卡：实况与实时数据 › 数据收集。*

[![数据收集](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## 三路 cluster 数据流

本选项卡从三路 telnet 数据流中收集**流星散射 spot**，每路各占一个子选项卡：

| 子选项卡 | 默认 | 说明 |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 可自选 cluster。ON0DXK 默认过滤了 VHF 频段：用 `set/filter dxbm/pass 6`（然后 4、2…）启用。 |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network（7000 = CW/RTTY，7001 = FT8）。Skimmer 很少能解码 MS 模式。 |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X 的 cluster，转发 **PSKReporter** 的 spot：WSJT-X 和 MSHV 的 MSK144 解码结果会出现在这里。 |
| **已收集的 MS spot** | – | 已接受的 spot 表格，最新的在前。 |

每路数据流都有主机、端口、登录后发送的命令、*重新连接*、*启动时连接*、一个控制台以及一行用于发送命令的输入框。请在顶部填写**登录呼号**。一条状态栏显示三个会话的状态（绿点 = 已连接）。更改语言或配色方案时，会话保持打开。

## 过滤器（占窗口的 40 %）

- **可选的本地过滤：** 低于 **27990.0 kHz** 的 cluster 行会被立即丢弃（不显示，也不保存）。
- **第 1 条标准 – 典型 MS 频率：** 50190–50300、70100–70400、144290–144399 kHz。落在这些窗口内的 spot 即使没有写模式名也会被接受，除非注释中声明了其他传播方式：`<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`。窗口和标签都可以编辑。
- **第 2 条标准 – MS 模式：** 在窗口之外，或带有上述某个标签时，只有包含 **MSK144、FSK441、FSK41、PSK2K、JTMS、JT6M**（仅用于 MS 的数字模式）或 **\<MS\>** 的 spot 才会保留，大小写不限。各个关键词可以停用、添加和删除；每个都有自己的计数器。
- **频段** 28、50、70、144、222、432 MHz；可对粘贴的一行进行**过滤器测试**；**计数器**。

## 网格坐标与存储

缺失的网格坐标或只有 4 位的网格坐标，从 **CALL3** 档案（`data/call3.txt`，JTDX 文件，超过一百万个呼号）中获取，CALL3 中的坐标总是优先于 4 位网格坐标。已接受的 spot 保存在 `data/spot_ms` 中，每天一个 CSV 文件，并供[实时通信](Live-Traffic-zh)地图使用。
