[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · **中文** · [中文 (繁體)](Getting-Started-zh-tw)

# 入门

首次启动时，YA-MS 显示一条示例路径（JN70CN → JO62QM，144 MHz）。只需五分钟即可为您的电台完成设置。

## 1. 三行控件

选项卡上方有三行控件，对所有选项卡都有效。右上角的**控制**按钮可折叠和展开它们（使用大字体时很有用）；该选择会被记住。

**第 1 行 – 电台与频段**

| 控件 | 作用 |
|---|---|
| **我的网格坐标** / **高度 m** | 您的 Maidenhead 网格坐标（4、6 或 8 位；取方格中心）以及电台的海拔高度。 |
| **对方电台** / **高度 m** | 地图右侧是对方电台的框：输入呼号并按回车，定位符取自 CALL3 数据库（与 YAEC 和 LIVETROPOVHF 相同）；下面是定位符和海拔。也可以把呼号写在定位符框里。 |
| **频段 MHz** | 28、50、70、144、222 或 432 MHz：用于天线增益和波瓣、流量估算以及链路预算。 |
| **计算** | 重新计算路径（E 层采样：需要几秒钟）。 |
| **天线方位** | 在地图旁对方电台框的顶部：你的天线方位，始终 **指向 DX**（路径方位）。其下方同一列中是地图图例。 |

**第 2 行 – E 层与天线**

| 控件 | 作用 |
|---|---|
| **余迹高度 km** + **来自雷达** | 流星余迹的高度（默认 90 km）。勾选*来自雷达*时，使用 Collm 雷达测得的最常见高度（众数）；参见[雷达流量](Radar-Flux-zh)。 |
| **波瓣仰角 °** | 天线垂直波瓣最大值的仰角：固定在 0° 的定向天线由于地面反射，波瓣仍位于地平线以上几度（通常 3-8°）。开启 **天线方向图** 复选框时（默认），E 层的点按两副天线的垂直方向图加权；关闭时只使用两个电台都能在此仰角以上看到的点。 |
| **八木天线：横梁 m** | 您的八木天线横梁长度。程序显示以 λ 表示的长度、增益（DL6WU 曲线）以及水平和垂直方向的 −3 dB 波瓣；参见[几何与路径损耗](Geometry-and-Path-Loss-zh#天线增益与波瓣)。低于 2 λ 时估算较粗略。 |
| **热点距中点 km** + **auto (AMS)** | Hot A 和 Hot B 到中点的距离。勾选 *auto (AMS)*（默认）时，按 DJ5HG 引用的 J. Richardson（AMS）天线偏角表确定：1000 km 为 13°，1250 km 为 11°，1500 和 2000 km 为 10°（距中点约 115、121、132 和 176 km）。取消勾选可手动输入 30–400 km（MSHV 使用 150 km）。 |

**第 3 行 – 时间**

| 控件 | 作用 |
|---|---|
| **时间** | UTC 时钟。 |
| **计算日期（UTC）** | [预报计算](Sky-View-zh)和 [GRAVES 雷达](GRAVES-Radar-zh)的计算日期（默认为今天），时刻取当天的当前时间。 同时也是：[效率计算](Efficiency-Calculation-zh)和 GRAVES 时间线中显示的日期。 |
| **小时（−12 至 +36 h）** | 将计算时刻在该时间之前 12 小时到之后 36 小时之间移动，步长 15 分钟。旁边显示*计算时间：当前*或*计算时间：dd/mm hh:mm UTC*。 |
| **实时** | 回到当前时刻。 |

## 2. 本台与对方电台

1. 输入**我的网格坐标**和**高度 m**。
2. 输入**对方电台**的网格坐标和高度——或在[天穹](Sky-View-zh)中点击地图：**左键 = 对方电台网格坐标**，**右键 = 本台网格坐标**。
3. 选择**频段 MHz** 并点击**计算**。

底部状态栏会确认：*路径已计算：… km，… s 内采样了 … 个反射点*。

## 3. 您的天线

输入八木天线的**横梁长度**。程序据此推算增益和波瓣；当天线指向 DX 时，如果 Hot A 或 Hot B 已经落在**波瓣内**，程序会提醒您（此时它们以灰色绘出：无需转动天线）。

## 4. 阅读结果

| 问题 | 查看位置 |
|---|---|
| 现在哪个流星雨对我的路径有帮助？来自哪一侧？ | [天穹](Sky-View-zh)：流星雨列表、红色的推荐 Hot、PREV 区域 |
| 今天哪个时段最好？ | [效率计算](Efficiency-Calculation-zh)：概览卡片和逐时表格 |
| 雷达正在统计多少流星？ | [雷达流量](Radar-Flux-zh) |
| 在 144 MHz 上我能期望多少个 ping？ | [试验性预报](Experimental-Forecasts-zh)（试验性） |
| 我的电台能打通这条路径吗？ | [几何与路径损耗](Geometry-and-Path-Loss-zh)：路径损耗和余量 |
| 下一个峰值是什么时候？ | [流星雨](Showers-zh) |
| 我能用 GRAVES 做测试吗？ | [GRAVES 雷达](GRAVES-Radar-zh) |

## 实用规则（来自文献）

- **与流星雨方向垂直指向**：最佳路径与辐射点方位正交；最佳指向 = 辐射点方位 ±90°，容差 ±40–50°（SM6FHZ）。
- **侧向散射**：将天线向大多数反射到达的一侧（A 或 B）偏转 10–30°（Cerrotta–Sartori 文章）。
- **辐射点过高**（高于 70°）或过低（低于 20°）时，有用的余迹很少（DF5HC、DH9GCD）。
- 偶发流星在 **06 UTC** 左右达到峰值（文章；Collm 流量也证实了这一点）。
- 432 MHz 上的有效距离：800–2000 km，最佳约 1400 km（SM6FHZ）；一般而言最佳距离为 1300–1500 km（DF5HC）。

下一步：[天穹](Sky-View-zh)。
