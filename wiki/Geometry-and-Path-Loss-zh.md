[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · **中文** · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

## 对流层折射（GFS）

对流层折射（“对流层折射（GFS）”复选框，启动时关闭）。勾选后，程序从 Open-Meteo 下载两站上空的 GFS 模型廓线（地面及 1000 至 500 hPa 各层的气压、温度和湿度，取 6 小时内最近的时刻），用测高方程（虚温）求各层高度，并用 ITU-R P.453 建议书 的公式求折射率：

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

其中 P 和 e（水汽压，由 Magnus 公式求得）单位为 hPa，T 单位为开尔文。最高层以上 N 按 7.35 km 的标高指数递减。若 GFS 无响应，则使用 P.453 参考大气 N = 315·exp(−h/7.35)，并在报告中注明。

射线用球面形式的斯涅尔定律（n·r·cos e 为常数）穿过薄球壳一直追踪到流星余迹高度；由此得到高度 H 处的距离和仰角修正：

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

以参考大气、余迹高度 89.5 km 为例：0° 时距离由 1061.5 km 增至约 1133 km（+72 km），点看起来高 0.62°；4° 时距离增加 14 km，修正为 0.20°；10° 以上影响可忽略。修正用于朝中点的仰角、公共区半径、热点以及效率地图上的各点；低于折射地平线的点被舍去。报告在“折射”一行中给出。

等效地球半径 k = 4/3 适用于停留在对流层最初几公里内的射线，那里 N 每公里约减少 40 个单位。指向 90 km 处余迹的射线穿过整个对流层，在 N 几乎为零的 10-15 km 以上几乎直线前进：若整个上升过程都用 k = 4/3，0° 时距离约为 1230 km，比追踪的射线多出近 100 km。因此程序不使用 k = 4/3，而是像作者的 LIVETROPOVHF 处理对流层传播那样，在 GFS 廓线中追踪射线。

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

## 公共区域边界

**来源：** 文章给出了各台站地平线与 E 层相交曲线的交点：即以 A 和 B 为圆心、角半径为 ρ = d_H/r 的两个圆的交点 [19–20]：

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

若 1 − |p0|² < 0，则路径长于 2·d_H，两个电台**没有 E 层公共区域**。

**验证：** 这些是两个电台都能看到的天空的**最远边缘**，**而不是瞄准点**。在 JN70CN–IN78UO（1710 km，方位 308°）上，它们位于距电台 1062 km 处、直达路径左右 37°，而 MSHV 建议的是 10°。因此它们被称为*边界 A* / *边界 B*，并在地图上以淡色绘出。

## Hot A 与 Hot B

**来源：** 偶发流星的反射集中在中点两侧的两个区域（“热点”）。J. Richardson（AMS）在 DJ5HG 引用的表格中（*Die Geometrie von Meteorscatterverbindungen*，2004）给出了相对于直接方向的天线偏角：**1000 km 为 13°，1250 km 为 11°，1500 和 2000 km 为 10°**。W8WN 沿用的 AMS Bulletin No. 203 给出 1500 和 1800 km 为 10°。

**选择：** Hot A 和 Hot B 是距中点 M 为 s、垂直于路径的点。勾选 *auto (AMS)*（默认）时，s 由 Richardson 表格的偏角线性插值得出（1000 km 以下取 13°，2000 km 以上取 10°）：s = (D/2)·tan(偏角)。不勾选时，s 手动输入，30–400 km（MSHV 使用 150 km）；从本台望向 DX 时 A 在左、B 在右 [21]。从电台看的偏角约为 [22]：

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**验证：** 按 AMS 表格，1000 km → 13°，s ≈ 115 km；1250 km → 11°，s ≈ 121 km；1500 km → 10°，s ≈ 132 km；2000 km → 10°，s ≈ 176 km。JN70CN–IN78UO（1710 km）→ 10°，s ≈ 151 km，与此前及 MSHV 使用的 150 km 相同；在短路径上，该表格使热点更靠近中点。

## 欠密余迹路径损耗

**来源：** McKinley 的欠密余迹方程和 ITU-R P.843 建议书（sin α = 1），不含天线增益；q = 电子线密度，r_e = 经典电子半径 = 2.818·10⁻¹⁵ m，R1、R2 为到余迹的距离，φ 为散射角的一半，β 为余迹与路径平面之间的夹角，a₁ 为初始半径因子，r₀ 以 m 计、h 以 km 计（P.843，公式 4 和 7）[36]：

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**选择：** 链路预算和损耗表使用 β = 90°（余迹穿过路径平面，最不利的情况：保守值），链路预算同时也显示最好的情况 β = 0。r₀ 取该频率的平均回波高度，h = 124 − 17 log f（P.843，公式 15）：50 MHz 为 95 km 处 0.76 m，144 MHz 为 87 km 处 0.40 m，432 MHz 为 79 km 处 0.21 m。在 1000 km 上，a₁ 在 50 MHz 为 0.2 dB，在 144 MHz 为 0.6 dB，在 432 MHz 为 1.4 dB（600 km 时为 2.9 dB）；若用 DJ5HG 固定的 102 km，432 MHz 时约为 70 dB，即完全没有回波。

**验证：** 在 144 MHz、q = 10¹⁴ 电子/m、余迹高度 89.5 km 且 β = 0 时：600 至 2100 km 之间为 **182–192 dB**（1000 km 时 185 dB），落在 GM8JBJ 所引用的 John Worsnop **G4BAO** 博士论文计算的 **172–190 dB** 范围内。β = 90° 时，损耗在 600 km 增加 10 dB，在 1000 km 增加 13 dB，在 2100 km 增加 16 dB；OH5IY 的**平均 200 dB** 介于两种情况之间。GM8JBJ 表中的 182 dB 并不构成佐证：该表没有给出频率，其每段 86.4 dB 是 1 MHz 下 500 km 的自由空间损耗（缺少 20 log f 项：144 MHz 时为 129.6 dB），各项相加为 163.8 dB 而不是 182；该页面既没有写“最小”，也没有写“144 MHz”。

## 链路预算

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]。增益以 dBi 输入并按 dBi 使用：McKinley 损耗以各向同性天线为基准，因此不减去 2.15 dB 的偶极子修正（EIRP = 功率 + 增益）。报告还给出采用 **OH5IY 平均路径损耗**（144 MHz 时 200 dB，按 λ³ 换算到所选频段）时的余量。文章参考值：约需 **70 dBm EIRP**（−130 dBm + 200 dB，例如约 400 W 馈入 14 dBi 天线）。

## 天线增益与波瓣

**VE7BQH** – 八木天线增益与横梁长度 L 的关系：VE7BQH 表格 每个波段的平均直线（每个波段约 60 副八木天线，NEC 增益）。括号内为样本范围和标准差：

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0.3–5 λ, 0.25 dB · 144 MHz: 0.75–8.9 λ, 0.15 dB · 432 MHz: 1.8–16 λ, 0.17 dB)

使用最近波段的直线：低于 100 MHz 用 50 MHz 的，100 至 300 MHz 用 144 MHz 的，高于 300 MHz 用 432 MHz 的（对 1296 MHz 属外推）。超出样本范围时主窗口会提示估算不够精确。

DL6WU 的历史曲线（VHF Communications 3/1982，图 1）：1981 年在 432 和 1296 MHz 的测量，横梁每倍长 2.35 dB，标称精度 0.5 dB；G ≈ 9.2 + 7.81 log10(L/λ) dBd。W8IO 将其记作 7.773 log10(L/λ) + 11.43 dBi（相差不到 0.1 dB）。程序在报告中写出它作比较：

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**与 L.B. Cebik W4RNL 在 432 MHz 上的 NEC 模型对比验证**（*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*；*70-CM Yagi Stacks Part 2*）：

| 八木天线 | 单元数 | 横梁（λ） | W4RNL NEC（dBi） | 公式（dBi） |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU（David Tanner） | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

差异从未超过 **0.1 dB**：增益更多取决于横梁长度，而不是具体设计（单元数相同时，VK3AUU 八木的横梁更短）。VK5DJ 的 Yagi Calculator 也给出了 VK3AUU、WA2PHW 和 DJ9BV 型号的估算值，但其公式未公开。

VE7BQH 平均值减 DL6WU 曲线：50 MHz 在 2 至 16 λ 内相差不超过 0.25 dB；144 MHz 从 1 λ 时 −0.04 dB 到 10 λ 时 +0.42 dB；432 MHz 从 2 λ 时 −0.06 dB 到 10 λ 时 +0.55 dB。对 W4RNL 在 432 MHz 仿真的 DL6WU 和 VK3AUU 八木，VE7BQH 平均值比 NEC 高 0.15–0.55 dB：在长横梁上，表中经计算机优化的八木比原始设计性能更好。

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

按 VE7BQH 平均值，同一副 14 λ 八木为 21.0 dBi，波瓣水平 16.9°、垂直 18.1°；上面的 20.3 dBi 来自 DL6WU 曲线。波瓣修正（0.93 · θK 和 θK）仍沿用由 DL6WU 八木得出的值。

天线始终视为指向 DX。若 |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2，则 hot spot **位于波瓣内**：此时在[天穹](Sky-View-zh)中以灰色绘出，并显示警告。垂直波瓣也计入效率计算：开启 *天线方向图* 复选框时，反射点按两副天线的垂直增益加权（宽度 θ_vertical，最大值在波瓣仰角处，地面因子在地平线处降为零）。

## 频段间经验规则

与 144 MHz 相比：数量/强度 × (144/f)³（以 dB 计），持续时间 × (144/f)²（SM6FHZ，VUSHF 2025）。IARU 第一区最大 ping 持续时间：50 MHz 为 1000 ms，70 MHz 为 500 ms，144 MHz 为 100 ms，432 MHz 为 13 ms（VHF Handbook，文章中引用）。另见[试验性预报](Experimental-Forecasts-zh)。
