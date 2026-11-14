[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · **日本語** · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# ライブトラフィック

*タブ: ライブとリアルタイムデータ › ライブトラフィック。*

[![ライブトラフィック](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/ja-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/ja-1_1.png)

## 表示内容

自局を中心とする**正距方位図法の地図** (中心からの距離 = 実際の距離、角度 = 方位) に、[データ収集](Data-Collection-ja) で集めた**すべての流星散乱通信のトラフィック**を表示します。交信ごとに次のものを描きます:

- 2 局間の**パス**。色はバンドごとに、28 MHz 茶、50 MHz 緑、70 MHz シアン、144 MHz 橙、222 MHz ピンク、432 MHz 紫です;
- パスの両端の 2 つの**局**;
- **雲**: そのパスとその時刻で最も可能性の高い流星痕が集中する場所。

**地図の外**にある局を含むスポットは破棄します。**届いたばかり**のスポット (3 分以内) は **1 分間点滅**するので、新しい活動がひと目でわかります。

受信中の局を表示：バンドの色の三角形は、PSKReporter によると選んだ時間帯に 28、50、70、144、432 MHz で MSK144、FSK441、PSK2K、JTMS を受信している局です。三角形をクリックすると、コールサイン、ロケーター、モード、最後のスポットが表示されます。「データ収集」タブの MQTT を接続しておく必要があります。

PSKReporter マップのアクティブなモニターも表示: pskreporter.info の地図に MSK144、FSK441、PSK2K、JTMS で表示されているが、まだスポットを受信していない局を白抜きの三角で示します (MQTT は何かを受信した局だけを送ります)。YA-MS は PSKReporter の検索サービスに 1 回に 1 モードずつ、3 分ごとに問い合わせるため、各モードは 12 分ごとに更新されます (サービスの規則どおり)。三角をクリックすると、コールサイン、ロケーター、デコードソフト、モニターがアクティブだった時刻が表示されます。初期設定でオン。

地図には各スポットの両局のコールサインが、局ごとに 1 回だけ書かれます。投影法は正距方位 (自局が中心) とメルカトルから選べます。「雲」列のツールチップがその意味を説明します。

すべてのバンドのスポットが表示されます。データ収集で選んでいないバンドのものも表示されます（これらは保存されません）。CW のスポットと近すぎる局どうしのスポットは、データ収集で破棄する設定なら表示されません。

## 雲の計算方法

スポットごとに 2 つのロケーター間のパスを作り (自局のパスと同じ幾何。[幾何と損失](Geometry-and-Path-Loss-ja) を参照)、スポットの時刻について、E 層の点ごとに**活動中のすべての流星群の鏡面反射の寄与**を ZHR で重み付けして合計します。これは [天球図](Sky-View-ja) の **PREV 領域**と同じ計算です。合計の 15 % 以上を占めるパスの側ごとに、雲は**楕円**になります: 中心は点の加重平均、半軸はその広がりの固有値の平方根の 1.5 倍、長軸は主固有ベクトルの方向です。寄与する流星群がない場合 (散在流星のみ)、雲は従来の 2 つの**ホットスポット**となり、破線で描かれます。式の詳細は計算マニュアルの第 10 章にあります。

## 操作

| 操作 | 意味 |
|---|---|
| **地図の半径** | 自局から 600–3500 km。 |
| **表示するスポット** | 直近 15 分または 30 分、直近 1 時間、直近 3 時間、直近 24 時間。 |
| **表** | 地図上の交信。新しいものが上で、バンドの色で表示します。*雲* はメイン側の反射の割合、または *散在流星* を示します。 |
| **クリック** | パスまたは表の行をクリックすると、その交信が強調表示され、ボックスに雲の中心のロケーター、割合、大きさ、軸が表示されます。 |
