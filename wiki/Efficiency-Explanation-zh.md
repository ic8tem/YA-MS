**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# 效率 - 说明

*选项卡：技术文档 › 效率 - 说明。*

[![效率 - 说明](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

一份技术文档 *"Come YA-MS calcola l'efficienza di uno sciame"*（YA-MS 如何计算流星雨的效率），在程序内以浅色页面显示。它**逐步**说明效率是如何得出的，并对每一步说明其**出处**。该文档目前**只有意大利语版**；本 wiki 在[效率计算](Efficiency-Calculation-zh#模型)和[几何与路径损耗](Geometry-and-Path-Loss-zh)中给出了其内容的中文版本。

## 标签

每一步都带有一个彩色标签：

| 标签 | 颜色 | 含义 |
|---|---|---|
| **FONTE**（来源） | 蓝色 | 该步骤采用了所引用的来源；方括号中的数字对应文末的来源列表 |
| **RILIEVO**（验证） | 绿色 | 程序与来源之间的比较及其结果 |
| **SCELTA**（选择） | 橙色 | 程序自己的选择，并非取自某个来源：有待实际上机经验检验 |

## 章节

| 章节 | 内容 |
|---|---|
| 1. 引言 | 目的、标签、效率的含义（OH5IY、MCG_MS；YA-MS 使用实际路径） |
| 2. 反射发生在哪里：E 层 | 余迹位于 80–120 km；余迹高度 = Collm 直方图的众数（验证：2026 年 11 月 5 日为 89.5 km） |
| 3. 路径几何 | 地球与中点；天线仰角（文章公式）；公共区域及其边界；Hot A / Hot B；天线波瓣（DL6WU、Kraus、W4RNL） |
| 4. 流星雨的辐射点 | 辐射点位置（IMO 2026/2027）、峰值日期（IMO 或太阳黄经）、活动曲线 |
| 5. 反射条件 | 镜面反射（McKinley）、高斯容差 0.05 rad、最佳指向（SM6FHZ）、DH9GCD 公式 |
| 6. 从单个点到效率 | 每 15 km 一个反射点、各点权重、百分比；与 QTFGUI（DJ5HG）的比较 |
| 7. 解读结果 | A / B 侧、路径指数、辐射点颜色、PREV 区域、从天线看出去的剖面 |
| 8. 工作频率与路径损耗 | λ³ / λ² 规则、从雷达到业余频段、路径损耗参考值 |
| 9. 已知局限 | 仅限欠密余迹、各向同性天线、工作值 |
| 10. 来源 | 17 个编号来源 |

## 按钮

| 按钮 | 作用 |
|---|---|
| **导出为 Word (.docx)...** | 将 `data/efficienza_spiegazione.docx` 的副本保存到您选择的位置（建议文件名 *YA-MS - calcolo dell'efficienza.docx*） |
| **在 Word 中打开** | 用 Word 文档的默认程序（Word、LibreOffice 等）打开同一个 `.docx` |

## 文件

| 文件 | 内容 |
|---|---|
| `data/efficienza_spiegazione.txt` | 选项卡中显示的文字，每行一个块（`TITLE`、`SUB`、`H1`、`H2`、`P`、`TAG|FONTE|…`、`TAG|RILIEVO|…`、`TAG|SCELTA|…`、`EQ`、`LI`、`SRC`） |
| `data/efficienza_spiegazione.docx` | Word 版本 |
| `doc/YA-MS_manuale_calcoli.docx` | **计算手册**：全部公式（Word 公式编辑器），带编号及出处 |

这两份文档通过 `tools/build_spiegazione.py data` 和 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` 从源代码重新生成。
