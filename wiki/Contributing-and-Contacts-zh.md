[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · **中文** · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# 参与贡献与联系方式

YA-MS 依靠在实际通联中使用它的人们的报告不断改进。每一处修正都会注明其来源。

## 联系方式

| | |
|---|---|
| 作者 | Costantino Cerrotta **IC8TEM** |
| 电子邮件 | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## 报告问题

在 **GitHub 上提交 issue** 或发送电子邮件，并附上：

- 操作系统和 YA-MS 版本（见窗口标题）；
- 两个网格坐标、频段和 UTC 时间；
- 您预期的结果和实际看到的结果（附截图会更有帮助）；
- 如果是雷达问题，请附上[雷达流量](Radar-Flux-zh)选项卡中显示的消息。

## 特别有用的内容

- **上机报告。** 效率或预报准确——或不准确——的时段和路径。该模型是试验性的，需要与实际 QSO 以及 MCG_MS / MS-Soft 进行比较。
- **RMOB 比较。** 您通过 [RMOB 比较](Experimental-Forecasts-zh#rmob-比较)得到的电台因子 K 和指数 k 的数值，以及您的频段和电台情况。
- **附有来源的数据。** 更好的辐射点漂移、活动曲线、新的 IMO 峰值日期（`data/massimi_imo.csv`）、天线数据：请附上来源，它将被引用。
- **雷达图表的变化。** 如果 Collm 图表格式发生变化，提供一份图像副本（`data/radar/`）有助于重新校准读取方式。

## 翻译

界面翻译是位于 **`data/lingue/<code>.txt`** 的纯文本文件（UTF-8），**任何人都可以修改**：

```
<Italian text><TAB><translation>
```

- 每行一个条目；以 `#` 开头的行为注释。
- 在两列中，两个字符 `\n` 都表示换行。
- 保留占位符 `{0}`、`{1}` … 及其格式（例如 `{0:F1}`、`{3:+0;-0}`），并按您的语言需要的顺序排列。
- 缺失或为空的条目以意大利语显示。所有键的列表在 `data/lingue/chiavi.txt` 中（由 `tools/estrai_chiavi.py` 生成，请勿编辑）。

在您安装目录的 `data/lingue` 文件夹中编辑文件，然后重新启动 YA-MS（或切换语言）即可看到效果。由于这些文件**在每次更新时都会被新版本替换**，请同时**发送您的修改**——通过电子邮件或在 GitHub 上提交 pull request（`data/lingue/`）——以便将其纳入下一个版本。

本 wiki 提供 English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文 版本；同样欢迎对 wiki 页面提出修改意见。
