[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · **日本語** · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# 貢献と連絡先

YA-MS は、実際の運用で使っている方々の報告によって改善されていきます。すべての修正はその出典とともにクレジットされます。

## 連絡先

| | |
|---|---|
| 作者 | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## 問題の報告

**GitHub で issue** を開くか、次の情報を添えて e-mail を送ってください:

- オペレーティングシステムと YA-MS のバージョン (ウィンドウのタイトルにあります);
- 2 つのロケーター、バンド、UTC 時刻;
- 期待した結果と実際に表示されたもの (スクリーンショットがあると助かります);
- レーダーの問題の場合は、[レーダーフラックス](Radar-Flux-ja) タブに表示されたメッセージ。

## 特に役立つもの

- **運用レポート。** 効率や予報が当たった – あるいは外れた – 時間とパス。モデルは実験的であり、実際の QSO や MCG_MS / MS-Soft との比較が必要です。
- **RMOB との比較。** [RMOB との比較](Experimental-Forecasts-ja#rmob-との比較) で求めた局係数 K と指数 k の値を、バンドと局の設備とともに。
- **出典付きのデータ。** より良い放射点の移動、活動プロファイル、IMO の新しい極大日 (`data/massimi_imo.csv`)、アンテナのデータ: 出典を添えていただければ引用します。
- **レーダーのグラフの変更。** Collm のグラフ形式が変わった場合、画像のコピー (`data/radar/`) が読み取りの再校正に役立ちます。

## 翻訳

表示の翻訳は **`data/lingue/<code>.txt`** (UTF-8) にあるプレーンテキストファイルで、**誰でも修正できます**:

```
<Italian text><TAB><translation>
```

- 1 行に 1 項目。`#` で始まる行はコメントです。
- どちらの列でも、2 文字 `\n` は改行を意味します。
- プレースホルダー `{0}`、`{1}`、… はその書式 (例: `{0:F1}`、`{3:+0;-0}`) のまま残し、自分の言語に必要な順序で配置してください。
- 欠けている項目や空の項目はイタリア語で表示されます。全キーの一覧は `data/lingue/chiavi.txt` です (`tools/estrai_chiavi.py` で生成。編集しないでください)。

インストール先の `data/lingue` フォルダーにあるファイルを編集し、YA-MS を再起動 (または言語を切り替え) すると結果を確認できます。これらのファイルは**アップデートのたびに新しいバージョンで置き換えられる**ため、修正内容は e-mail または GitHub のプルリクエスト (`data/lingue/`) で**送ってください**。次のリリースに反映されます。

この wiki は English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文で提供されています。wiki ページの修正も歓迎します。
