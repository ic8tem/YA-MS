[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · **中文**

# 效率计算

*选项卡：预报计算 › 效率计算。*

[![效率计算](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

一个流星雨的**效率**以百分比表示其辐射点位置在多大程度上允许在**您的**路径上产生反射。这个概念由 Ilkka **OH5IY**（MS-Soft）提出，并被 Cerrotta–Sartori 的文章采用：效率峰值与目视峰值（ZHR）并不重合，因为它取决于辐射点相对于两个电台的位置。DL5MCG 的 MCG_MS 把同样的思路应用于四个固定方向；YA-MS 则针对两个网格坐标之间的**实际路径**进行计算。

本选项卡按*24 h 表格的日期（UTC）*中选择的日期逐小时显示效率（取每小时半点的值）。

## 概览卡片

| 卡片 | 内容 |
|---|---|
| **当天最佳时段** | 路径指数最高的小时、该指数以及主要的一侧（A/B 及其百分比） |
| **最有利的流星雨** | 当天 ZHR × 效率最大的流星雨、其效率、时刻和一侧，以及**最佳指向**（辐射点方位 +90° / −90°） |
| **当前** | 此刻的指数和主要的一侧，以及推荐的 Hot（仅当所选日期为今天时） |
| **试验性预报** | 在预报频率上当前、1 小时后和 2 小时后的预期反射次数/小时（Collm，SM6FHZ 规则；参见[试验性预报](Experimental-Forecasts-zh)） |

卡片下方的一条说明栏解释字母 A 和 B 的含义（见下文）。

## 图表

*… 在 … 的逐时效率（UTC，取每小时半点的值）。* 最多显示五个流星雨：效率 % 用实线表示，DH9GCD 公式用同色虚线表示；**路径指数**以蓝色柱表示，对应右侧刻度。

## 逐时表格

当天每个活跃流星雨占一行（按 ZHR 排序），24 列对应各小时（UTC）：

| 单元格 | 含义 |
|---|---|
| `63A` | 效率 63 %，大多数反射来自 **A** 侧 |
| `41B` | 效率 41 %，**B** 侧 |
| `3` | 效率低于 5 %：只有数字，不带侧别字母 |
| 空 | 效率低于 1 % |
| `…↑` | 该小时从本台看辐射点**高于 70°**（过高） |
| 黄色文字 | 效率 ≥ 50 % |

- **A** = 从本台望向对方电台时的**左侧**（Hot A 区域）；**B** = **右侧**（Hot B 区域）。值得将天线**向该侧偏转 10–30°**（侧向散射，Cerrotta–Sartori 文章）。
- **浅蓝色行**（每个流星雨下方的 *DH9GCD %*）：DH9GCD 公式，用于比较。
- **Σ 行**：*路径指数（ZHR×效率）*。
- **橙色行**（*预报 … MHz（反射/小时）*）：试验性预报，只在有预报的小时显示（今天及明天的一部分）。

## 模型

所有步骤都在[计算手册](Efficiency-Explanation-zh)中（`doc/YA-MS_manuale_calcoli.docx`，第 5 章）。简述如下：

**1. 镜面反射。** 只有当余迹与以 A 和 B 为焦点的椭球面相切时，它才能把信号从 A 送到 B（McKinley 1961）。同一流星雨的余迹都平行于辐射点方向 ŝ（文章；McKinley）。对 E 层上的每个点 P，取指向两个电台的单位矢量：

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

DJ5HG 的 QTFGUI（锥面散射）也基于同一定律。该条件以高斯容差 σ = 0.05 rad（约 3°）放宽接受——*程序的选择*：

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. 每个点的权重。** 欠密余迹的功率（McKinley），φ = 散射角的一半（限制在 85° 以内，*选择*）：

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

到达某点的流星数与该处辐射点仰角的正弦（ŝ·û_P）成正比，这与 IMO 对 ZHR 使用的修正相同。

**3. 求和与百分比。** 在余迹高度上每 15 km 取一个点，只取两个电台都能在波瓣仰角以上看到的点（*选择*）。100 % 对应该路径最有利的辐射点位置：

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F 对每条路径只在一个方向网格（方位每 5°，仰角每 2.5°）上计算一次，然后进行插值。

**4. 侧别与指数。**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

表格中的字母是比例较大的一侧。*程序的选择（手册公式 32–33）。*

## DH9GCD 对比

一项独立的验证：**DH9GCD** 的最佳方向公式，由 **DF5HC** 转述（DARC 会议，2018 年 1 月），其中 El 和 Az 为从本台看的辐射点仰角和方位，P 为对方电台的方位：

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

当辐射点位于 45° 且与路径垂直时，该值最大。DF5HC 认为辐射点低于 20° 过低，**高于 70° 过高**：这些小时在表格中标有 ↑，并在[天穹](Sky-View-zh#警告)上给出警告。该公式忽略了距离和高度，但仍是很好的参考。

## 验证

| 验证 | 结果 |
|---|---|
| SM6FHZ 规则（VUSHF 2025）：最佳路径与辐射点方位正交，指向 = 辐射点方位 ±90°，容差 ±40–50° | 模型能够再现；当辐射点与路径方向一致且位于高空时，效率几乎为零 |
| DJ5HG 的 QTFGUI，汉堡 JO53IM – 巴塞罗那，象限仪座流星雨，1 月 4 日（其手册中的示例） | QTFGUI：07:00 指向 252°，−8 dB；08:00 无反射区；09:00 指向 168°，−4 dB。YA-MS（与 QTFGUI 一样取高度 102 km）：07:00 241°，−5.4 dB；08:00 0.6 %（−22 dB）；09:00 161°，−4.0 dB。DH9GCD：26 %、2 %、32 %。三种方法都看到了 08:00 的空洞，此时辐射点几乎位于天顶 |
| 每 5 km 而非每 15 km 采样 | 百分比变化不到 0.3 个百分点 |

> OH5IY 和 MCG_MS 所用的刻度细节未知（MS-Soft 的手册已无法获得）：在把百分比视为等价之前，请先与这些程序比较。该模型只考虑欠密余迹，天线为各向同性；过密余迹的长回波和偶发流星背景不计入效率（偶发流星背景由雷达流量体现）。
