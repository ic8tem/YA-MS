[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · **中文**

# 几何与路径损耗

*选项卡：预报计算 › 几何与路径损耗。*

[![几何与路径损耗](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

一份路径的文字报告（文字可选中，便于复制），右侧是图表**天线仰角与到散射点距离的关系**。方括号中的数字对应计算手册（`doc/YA-MS_manuale_calcoli.docx`）中的公式编号。

## 本选项卡的输入

| 字段 | 默认 | 用途 |
|---|---|---|
| **功率 W** | 400 | 用于链路预算的发射功率 |
| **天线增益 dBi（发 = 收）** | 14 | 两端使用相同的天线 |
| **最小信号 dBm** | −130 | 最小可检测信号（文章：8 单元八木 + 前置放大器） |
| **余迹密度 q = 10^ … 电子/m** | 14 | 欠密余迹的电子线密度 |

电台、频段、余迹高度、波瓣仰角、横梁和热点距离取自[控件行](Getting-Started-zh#1-三行控件)。

## 报告各部分

| 部分 | 内容 |
|---|---|
| **路径几何（球形地球，R = 6372.7955 km）** | 本台和 DX 及其高度；距离、方位和反方位；中点（网格坐标和经纬度）；余迹高度（取自雷达时注明 *<- Collm 雷达测得的众数*）；指向中点的天线仰角 |
| **HOT A / HOT B（经典热点，用于天线指向）** | 每个热点：网格坐标、从本台看的方位及相对直达路径的偏角、从 DX 看的方位、距离、仰角 |
| **公共区域边界** | 在给定波瓣仰角下余迹高度处的覆盖距离；边界 A / 边界 B 及其方位 |
| 天线 | 以 λ 表示的横梁长度、增益、水平/垂直波瓣；Hot A 和 Hot B 在波瓣内还是外 |
| **路径损耗（欠密余迹，McKinley 1961；不含天线增益）** | 中点（前向）、Hot A 和 Hot B 在 28、50、70、144、222 和 432 MHz 上的数值表 |
| **… MHz 链路预算（中点）** | 功率和 EIRP、路径损耗、天线处信号、最小可接收信号、**余量**；以及采用 OH5IY 平均损耗时的余量 |
| **频段间经验规则（SM6FHZ，VUSHF 2025）** | 与 144 MHz 相比的数量/强度和持续时间；IARU 最大 ping |

## 网格坐标与路径

网格坐标（4、6 或 8 位；取方格中心，IARU Maidenhead 系统）[14]。距离、方位和中点采用半径 **r = 6372.7955 km**（Cerrotta–Sartori 文章）球面上的大圆公式计算 [15–16]。与时间相关的计算以**中点**为准，因为两端的最佳时间可能相差多达 1.5 小时（SM6FHZ）。

## 天线仰角

**来源：** Cerrotta–Sartori 文章中的公式（图 7），其中 x = d/r，d 为到反射点的地面距离，H 为余迹高度，h 为电台高度 [17]：

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**验证：** 与精确球面几何的差异在 0.03° 以内。程序使用双参数反正切函数，在地平线以外给出负值，并避免了文章中提到的周期性问题。指向中点的仰角为负，意味着*路径超出单跳的几何范围*。

## 地平线覆盖距离

仰角为 e 的射线到达高度 H 时的地面距离（上式的几何反算）[18]：

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**验证：** H = 89.5 km、e = 0° → **1062 km**。在文章的示例（JN44BB–IO53RT）中，图上的地平线交点距电台约 870 km，相当于波瓣抬高约 2°（865 km）。

## 公共区域边界

**来源：** 文章给出了各台站地平线与 E 层相交曲线的交点：即以 A 和 B 为圆心、角半径为 ρ = d_H/r 的两个圆的交点 [19–20]：

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

若 1 − |p0|² < 0，则路径长于 2·d_H，两个电台**没有 E 层公共区域**。

**验证：** 这些是两个电台都能看到的天空的**最远边缘**，**而不是瞄准点**。在 JN70CN–IN78UO（1710 km，方位 308°）上，它们位于距电台 1062 km 处、直达路径左右 37°，而 MSHV 建议的是 10°。因此它们被称为*边界 A* / *边界 B*，并在地图上以淡色绘出。

## Hot A 与 Hot B

**来源：** 反射集中在中点两侧约 **50–150 km** 的两个区域（“热点”）。这是 AMS Bulletin No. 203 天线偏角表的基础，W8WN 沿用了它（1500 和 1800 km 路径偏 10°）；LZ2HV 的 MSHV 也采用同样的标准。

**选择：** Hot A 和 Hot B 是距中点 M 为 s、垂直于路径的点（s = 150 km，可在 30–400 km 之间调整）；从本台望向 DX 时 A 在左、B 在右 [21]。从电台看的偏角约为 [22]：

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**验证：** JN70CN–IN78UO，D = 1710 km：s = 100 km 时为 6.7°，**s = 150 km 时为 10.0°**（与 MSHV 和 AMS/W8WN 相同），s = 200 km 时为 13.2°。

## 欠密余迹路径损耗

**来源：** McKinley 的欠密余迹方程（β = 0，sin α = 1），不含天线增益；q = 电子线密度，r_e = 经典电子半径 = 2.818·10⁻¹⁵ m，R1、R2 为到余迹的距离，φ 为散射角的一半 [36]：

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\cos^2\varphi}{\lambda^3 q^2 r_e^2}\right]\ \mathrm{dB}
```

**验证：** 在 144 MHz、q = 10¹⁴ 电子/m 时：600 至 2200 km 之间为 **181–192 dB**，与文章中 144 MHz 的参考值一致：**最小 182 dB**（GM8JBJ，引自 Kaiser & Closs 1952）和**平均 200 dB**（OH5IY）。

## 链路预算

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - 2{.}15 - L + G_{rx} - 2{.}15,\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]。增益以 dBi 输入，按 dBd（dBi − 2.15）使用。报告还给出采用 **OH5IY 平均路径损耗**（144 MHz 时 200 dB，按 λ³ 换算到所选频段）时的余量。文章参考值：约需 **70 dBm EIRP**（−130 dBm + 200 dB，例如约 400 W 馈入 14 dBi 天线）。

## 天线增益与波瓣

**增益 – 来源：** Günter Hoch **DL6WU** 给出的长八木天线增益随横梁长度 L 变化的曲线，由 W8IO 转述（约 2 λ 以上有效）[39]：

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**与 L.B. Cebik W4RNL 在 432 MHz 上的 NEC 模型对比验证**（*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*；*70-CM Yagi Stacks Part 2*）：

| 八木天线 | 单元数 | 横梁（λ） | W4RNL NEC（dBi） | 公式（dBi） |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU（David Tanner） | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

差异从未超过 **0.1 dB**：增益更多取决于横梁长度，而不是具体设计（单元数相同时，VK3AUU 八木的横梁更短）。VK5DJ 的 Yagi Calculator 也给出了 VK3AUU、WA2PHW 和 DJ9BV 型号的估算值，但其公式未公开。

**波瓣 – 来源：** Kraus 规则，取圆形波瓣 θE = θH = θK [40]：

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**验证：** W4RNL 对 DL6WU 八木的 NEC 模型给出的**水平波瓣比 Kraus 窄 5–10 %**：12、19 和 26 单元分别为 33.8° / 26.4° / 22.6°，而 Kraus 为 37.3° / 28.0° / 23.9°。简单公式忽略了前向旁瓣（W4RNL，*Long-Boom Yagi Rules of Thumb*）。长横梁上垂直波瓣略宽于水平波瓣（14 λ：18.4° / 18.8°）。

**选择** [41]：

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

示例：432 MHz 上 14 λ 的八木 → 20.3 dBi，水平波瓣 18.1°，垂直波瓣 19.5°；W4RNL 的模型给出 20.4 dBi 和 18.4° / 18.8°。这些是由少数几副 DL6WU 天线得出的近似规则。

天线始终被视为指向 DX。若 |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2，则热点位于**波瓣内**：此时它在[天穹](Sky-View-zh)上以灰色绘出，并出现提示。在效率计算中天线被视为各向同性；实际波瓣只用于这项检查。

## 频段间经验规则

与 144 MHz 相比：数量/强度 × (144/f)³（以 dB 计），持续时间 × (144/f)²（SM6FHZ，VUSHF 2025）。IARU 第一区最大 ping 持续时间：50 MHz 为 1000 ms，70 MHz 为 500 ms，144 MHz 为 100 ms，432 MHz 为 13 ms（VHF Handbook，文章中引用）。另见[试验性预报](Experimental-Forecasts-zh)。
