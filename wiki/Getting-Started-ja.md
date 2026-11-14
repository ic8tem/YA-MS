[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · **日本語** · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# はじめに

初回起動時、YA-MS は例として 144 MHz の JN70CN → JO62QM のパスを表示します。自局用の設定は 5 分もあれば終わります。

## 1. 3 段の操作部

タブの上には、すべてのタブに共通の 3 段の操作部があります。右上の **操作** ボタンで折りたたみ・展開ができ (大きなフォントのときに便利)、その状態は記憶されます。

**1 段目 – 局とバンド**

| 操作 | 機能 |
|---|---|
| **自局ロケーター** / **標高 m** | 自局のマイデンヘッド ロケーター (4、6、8 文字。グリッドの中心を使用) と局の海抜高度。 |
| **相手局** / **標高 m** | 地図の右側に相手局の枠があります。コールサインを入力して Enter を押すと、ロケーターが CALL3 データベースから取得されます (YAEC や LIVETROPOVHF と同じ)。その下にロケーターと高さがあります。コールサインはロケーター欄に入力することもできます。 |
| **バンド MHz** | 28、50、70、144、222、432 MHz: アンテナの利得とビーム幅、フラックスの推定、回線計算に使います。 |
| **計算** | パスを再計算します (E 層のサンプリング: 数秒)。 |
| **アンテナ方位** | 地図の横、相手局の枠の上部: 自局アンテナの方位、常に **DX 方向** (パスの方位)。その下、同じ列に地図の凡例があります。 |

**2 段目 – E 層とアンテナ**

| 操作 | 機能 |
|---|---|
| **流星痕高度 km** + **レーダーより** | 流星痕の高度 (既定 90 km)。*レーダーより* にチェックを入れると、Collm レーダーが測定した最も多い高度 (最頻値) を使います。[レーダーフラックス](Radar-Flux-ja) を参照。 |
| **ビーム仰角 °** | アンテナの垂直ローブの最大の仰角：0° に固定した八木アンテナでも、大地反射のためローブは地平線より数度上にあります（通常 3〜8°）。**アンテナパターン** のチェックがオン（既定）のとき、E 層の点を 2 本のアンテナの垂直パターンで重み付けします。オフのときは、両局がこの仰角より上に見る点だけを使います。 |
| **八木アンテナ: ブーム長 m** | 八木アンテナのブーム長。プログラムは λ 単位の長さ、利得 (DL6WU 曲線)、水平・垂直の −3 dB ビーム幅を表示します。[幾何と損失](Geometry-and-Path-Loss-ja#アンテナの利得とビーム幅) を参照。2 λ 未満では推定精度が低くなります。 |
| **中間点からのホットスポット km** + **auto (AMS)** | 中間点から Hot A と Hot B までの距離。*auto (AMS)* にチェックを入れると (既定)、DJ5HG が引用した J. Richardson (AMS) のアンテナ偏差の表に従います: 1000 km で 13°、1250 km で 11°、1500 km と 2000 km で 10° (中間点から約 115、121、132、176 km)。チェックを外すと 30–400 km を手入力できます (MSHV は 150 km を使用)。 |

**3 段目 – 時刻**

| 操作 | 機能 |
|---|---|
| **現在時刻** | UTC の時計。 |
| **計算日 (UTC)** | [予測計算](Sky-View-ja) と [GRAVES レーダー](GRAVES-Radar-ja) の計算日 (既定は今日) で、時刻は現在の時刻です。 また：[効率の計算](Efficiency-Calculation-ja) と GRAVES の時系列に表示する日。 |
| **時間 (−12〜+36 h)** | 計算の時刻をその時刻の 12 時間前から 36 時間後まで、15 分刻みで動かします。横に *計算時刻: 現在* または *計算時刻: dd/mm hh:mm UTC* と表示されます。 |
| **リアルタイム** | 現在に戻します。 |

## 2. 自局と相手局

1. **自局ロケーター** と **標高 m** を入力します。
2. **相手局** のロケーターと標高を入力します – または [天球図](Sky-View-ja) の地図をクリックします: **左クリック = 相手局のロケーター**、**右クリック = 自局のロケーター**。
3. **バンド MHz** を選び、**計算** を押します。

下部のステータスバーに確認が表示されます: *パス計算完了: … km、反射点 … 個を … s でサンプリング*。

## 3. 自局のアンテナ

八木アンテナの **ブーム長** を入力します。プログラムは利得とビーム幅を求め、アンテナを相手局に向けたときに Hot A や Hot B が既に**ビーム内**に入る場合は注意を表示します (そのときは灰色で描かれます: アンテナを振る必要はありません)。

## 4. 結果の読み方

| 知りたいこと | 見る場所 |
|---|---|
| 今どの流星群が自分のパスに役立ち、どちら側からか? | [天球図](Sky-View-ja): 流星群リスト、赤の推奨 Hot、PREV 領域 |
| 今日の最良の時間帯は? | [効率の計算](Efficiency-Calculation-ja): 概要カードと時間別の表 |
| レーダーは流星をいくつ数えているか? | [レーダーフラックス](Radar-Flux-ja) |
| 144 MHz でピングはいくつ期待できるか? | [実験的予報](Experimental-Forecasts-ja) (実験的) |
| 自局の設備でパスを成立させられるか? | [幾何と損失](Geometry-and-Path-Loss-ja): パス損失とマージン |
| 次の極大はいつか? | [流星群](Showers-ja) |
| GRAVES で試験できるか? | [GRAVES レーダー](GRAVES-Radar-ja) |

## 実用上のルール (出典より)

- **流星群に対して直交方向に向ける**: 最良のパスは放射点の方位に直交します。最良方向 = 放射点方位 ±90°、許容 ±40–50° (SM6FHZ)。
- **サイドスキャッター**: 反射の大部分が来る側 (A または B) へアンテナを 10–30° 振ります (Cerrotta–Sartori の記事)。
- **放射点が高すぎる** (70° 超) か低すぎる (20° 未満) と、有効な流星痕は少なくなります (DF5HC, DH9GCD)。
- 散在流星は **06 UTC** 頃に最も多くなります (記事。Collm のフラックスでも確認)。
- 432 MHz の有効距離: 800–2000 km、最良は約 1400 km (SM6FHZ)。一般的な最良距離は 1300–1500 km (DF5HC)。

次へ: [天球図](Sky-View-ja)。
