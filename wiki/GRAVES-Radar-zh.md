[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · **中文** · [中文 (繁體)](GRAVES-Radar-zh-tw)

# GRAVES 雷达

*选项卡：实况与实时数据 › GRAVES 雷达。*

[![GRAVES 雷达](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## GRAVES 是什么

**GRAVES** 是一部法国雷达，在 **143.050 MHz 上发射连续波（CW）**，发射站位于 **Broye-lès-Pesmes**（47.348° N 5.515° E，网格坐标 **JN27SI**，海拔约 200 m；Wikipedia）。位于 GRAVES 和您都能看到的区域中的流星余迹会通过**前向散射**把它的信号反射给您：您会在载波附近听到短促的 *ping*。**RMOB** 的观测者正是用这种方式在 143.050 MHz 上逐小时统计流星的；对您的 2 m 流星散射电台来说，它也是一个免费且始终在线的测试信号。

本选项卡把 **GRAVES → 本台**当作一条独立的流星散射路径：使用与主路径相同的函数（相同的余迹高度、波瓣仰角和热点距离），计算流星雨效率、推荐的 Hot 和 PREV 区域，然后检查该区域是否**位于 GRAVES 波束内**，以及波束**何时**照射到它。

## 顶部栏

| 控件 | 作用 |
|---|---|
| **当前** | 将计算恢复为实时：日期设为今天，小时滑块归零（本选项卡跟随*计算日期*和*小时*）。 |
| **将 GRAVES 设为 DX** | 对方电台变为 GRAVES（JN27SI，高度 200 m），主路径随之重新计算：此后其他所有选项卡都显示 GRAVES 路径。 |
| **波束序列** | *每步 0.8 s · 周期 4.8 s（PE1ITR 2021）*（默认）或 *每步 3.2 s · 周期 19.2 s（PE1ITR 2007）*。 |

## 四张卡片

| 卡片 | 内容 |
|---|---|
| **GRAVES 波束中的有效区域** | *是 · 扇区 X*，并给出从 GRAVES 看推荐热点的方位角和仰角以及步进（1–6）；或者 *否：在扇区外* / *否：在 GRAVES 地平线以下* / *否：高于波束（约 25°）* |
| **当前 GRAVES → 本台路径的效率** | 路径指数 Σ ZHR × 效率、最佳流星雨、主要的 A/B 侧，以及 *预期回波 ≈ …/小时*（试验性，见下文） |
| **路径** | 到 GRAVES 的距离；天线朝向推荐 Hot 的方位和仰角；GRAVES 直射方位 |
| **波束下次扫过该区域** | *当前 · 剩余 … s* 或 *… s 后*，步进（例如 *B4*），接下来的三个时刻（以分钟内的秒数表示）以及能捕捉到的余迹比例 |

如果此刻没有有用的流星雨，程序会显示**最适合该波束**的热点（位于扇区内、最靠近正南方向），并加以说明。

## 从 GRAVES 看到的天空

根据 PE1ITR 和 Bolidozor wiki 的资料，**四个相控阵**覆盖方位 **90° 至 270°** 的南方天空，分为四个 **45° 扇区**：

| 扇区 | 从 GRAVES 看的方位 |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

每个扇区分为 **6 个 7.5° 的步进**，从方位最小的一端起编号 1 至 6，依次点亮，**四个扇区同时进行**。波束在**仰角方向宽约 25°**：在余迹高度上，它覆盖两个虚线圆（*波束地平线*）之间的彩色环带。图中：橙色/粉色点 = GRAVES → 本台路径的 PREV 区域，绿线 = 本台方向，红线 = 从本台到推荐热点；当前点亮的步进被突出显示。

## 时间线重建

*时间线重建 · 日期 UTC*（与 24 h 表格同一天）：对每个小时给出 GRAVES → 本台路径的效率、最有利的流星雨以及有效窗口（*hh:00 → hh:00 UTC · n h*），并标出最大值（*最大 Σ …，hh:30*）和红色的*当前*标记。下方是**接下来几秒的细节**：扇区的六个步进、照射到有效区域的步进，以及*可能有回波（余迹 +0.3 s）*。

### 波束时序

序列与 **UTC** 绑定（PE1ITR）：当前点亮的步进由自 00:00 UTC 起的秒数对周期取模计算得出（86 400 s 同时是 4.8 s 和 19.2 s 的整数倍）。指挥站有时会把序列平移几个步进，因此这些细节是**需要通过收听来确认的预测**。黄色标签**电脑时钟已同步**提醒您：请将电脑与 NTP 服务器同步（误差最多零点几秒）。

### 检测因子

只有当余迹存在期间被波束照射到时，才能听到它：

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0.3 s 是 143 MHz 上欠密余迹的典型持续时间——这是一个固定值，属于*程序的选择*（SM6FHZ 的 λ² 规则可在频段之间换算持续时间，但不提供起始值）。

### 预期回波（试验性）

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

[试验性预报](Experimental-Forecasts-zh)中的预报（已包含电台因子 K）用 SM6FHZ 规则（相同的指数 k）从其频率 f_fc 换算到 143.050 MHz，再用两条路径流星雨指数之比加以修正（常数 10 代表偶发流星背景，与预报中相同），最后乘以检测因子。仅供参考：请与 RMOB 观测者的数据比较。

## 如何收听 GRAVES 的 ping

| 步骤 | 操作方法 |
|---|---|
| 接收机 | **USB 143.049 MHz**（约 1 kHz 音调）或 143.050 MHz，**AGC 设为慢速或关闭**，音频带宽**至少 2.4 kHz** |
| 天线 | 朝向 GRAVES → 本台路径的**推荐热点**（*路径*卡片），采用**低仰角** |
| 瀑布图 | ping 是**靠近载波的短线**；长时间（过密）余迹更宽，并显示多普勒频移 |
| 计数 | RMOB 使用 GRAVES 做逐时流星计数：**将您的 ping 与 143.050 MHz 上的观测者进行比较**（[试验性预报](Experimental-Forecasts-zh#rmob-比较)） |

## 来源

1. Rob Hardenberg **PE1ITR**，*"The 143.050 MHz Graves Radar, a VHF Beacon"*（DUBUS 4/2007）及 *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki，"Graves" – 天线阵、扇区和波束时序
3. **Wikipedia**，"GRAVES (system)" – 位于 Broye-lès-Pesmes 的发射站（47.348° N 5.515° E）
4. **RMOB** – 143.050 MHz 上的观测者（[rmob.org](https://www.rmob.org)）
5. IC8TEM 的 **YAEC** – GRAVES Radar 选项卡（本选项卡由其原型演变而来）
