[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · **中文** · [中文 (繁體)](Live-Traffic-zh-tw)

# 实时通信

*选项卡：实况与实时数据 › 实时通信。*

[![实时通信](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## 显示内容

一张以本台为中心的**方位等距地图**（到中心的距离 = 真实距离，角度 = 方位角），显示由[数据收集](Data-Collection-zh)汇集的**所有流星散射通信**。对每个通联，程序绘出：

- 两个电台之间的**路径**，按频段着色：28 MHz 棕色，50 MHz 绿色，70 MHz 青色，144 MHz 橙色，222 MHz 粉色，432 MHz 紫色；
- 路径两端的两个**电台**；
- **云团**：该路径在该时刻最可能出现流星余迹的集中区域。

有电台位于**地图之外**的 spot 会被舍弃。**刚刚到达**（不超过 3 分钟）的 spot 会**闪烁一分钟**，让新的活动一目了然。

显示谁在收听：波段颜色的三角形标出 PSKReporter 显示在所选时间窗内于 28、50、70、144 和 432 MHz 接收 MSK144、FSK441、PSK2K 或 JTMS 的电台。点击三角形可查看呼号、网格、模式和最近报点。需要连接“数据采集”选项卡中的 MQTT 数据流。

同时显示 PSKReporter 地图上的活动监听站：在 pskreporter.info 地图上以 MSK144、FSK441、PSK2K 或 JTMS 出现但尚未收到任何报告的电台显示为空心三角形（MQTT 只发送有接收的电台）。YA-MS 按照该服务的规定，每 5 分钟对所有模式查询一次 PSKReporter 查询服务；监听站在地图上至少保留 11 分钟。点击三角形可显示呼号、网格定位、解码软件和监听站活动的时间。默认开启。

超过 1100 公里且无平行路径的 FT8：相距超过 1100 公里的电台之间的 FT8 报告（来自 PSKReporter MQTT、集群或经 UDP 的 WSJT-X），如果在其前后 3 分钟内没有平行路径（同一波段、中点相距 300 公里以内、方向相差 20° 以内、另一对电台），则以浅绿色绘制，其在右下方表格中的行始终闪烁。偶发 E 层和对流层传播会产生许多相近的平行路径；孤立的报告可能是流星余迹。为此 YA-MS 也从 MQTT 接收 6 m、4 m、2 m、1.25 m 和 70 cm 的 FT8 报告（不含 10 m，数量太多）。这些报告不进入 MS 存档。默认开启。

经 UDP 收到、与你的电台有关的 WSJT-X 报告（解码中含有你的呼号：呼叫你或回复你的电台）以始终闪烁的虚线绘制，任何模式、任何距离均如此。

地图上写出每条报告两端电台的呼号，每个电台只写一次。投影可选：方位投影（以你的电台为中心）或墨卡托。“云团”列的提示说明其含义。

显示所有波段的报告，包括数据收集中未选择的波段（这些不会被保存）。如果在数据收集中被丢弃，CW 报告和距离过近的电台之间的报告不会显示。

## 云团如何计算

对每条 spot，程序构建两个网格坐标之间的路径（与本台路径使用相同的几何，参见[几何与路径损耗](Geometry-and-Path-Loss-zh)），并在 spot 的时刻，逐点累加 E 层上**每个活跃流星雨的镜面反射贡献**，以其 ZHR 加权——与[天穹](Sky-View-zh)中的 **PREV 区域**是同一种计算。对于占总量至少 15 % 的路径每一侧，云团是一个**椭圆**：中心为各点的加权平均位置，半轴为各点离散度特征值平方根的 1.5 倍，长轴沿主特征向量方向。如果没有任何流星雨作出贡献（只有偶发流星），云团就是两个经典的**热点**，以虚线绘出。完整的公式见计算手册第 10 章。

## 控件

| 控件 | 含义 |
|---|---|
| **地图半径** | 距本台 600–3500 km。 |
| **要显示的 spot** | 最近 15 或 30 分钟、最近 1 小时、最近 3 小时、最近 24 小时。 |
| **表格** | 地图上的通联，最新的在前，以频段颜色显示；*云团* 列给出主要一侧所占的反射比例，或显示*偶发流星*。 |
| **点击** | 点击路径或表格中的一行：该通联被突出显示，信息框中显示云团中心的网格坐标、其所占比例、大小和轴向。 |
