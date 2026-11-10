[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · **日本語** · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# トラブルシューティングと FAQ

## インストールと起動

### Windows SmartScreen が「Windows によって PC が保護されました」と表示する
このプログラムは商用証明書で署名されていません。*詳細情報* → *実行* をクリックしてください。ダウンロードは必ず [Releases](https://github.com/ic8tem/YA-MS/releases) ページから行ってください。

### macOS 開発元を確認できないため開けない
YA-MS は Apple の署名がないため、初回は **Gatekeeper** がブロックします。`.dmg` 内で **「Installa YA-MS.command」を右クリック → 開く** を選んで確認してください。スクリプトが `~/YA-MS/YA-MS.app` から「インターネットからダウンロード」の隔離フラグを外して起動します。それでも macOS が拒否する場合は、*システム設定 → プライバシーとセキュリティ* を開き、*このまま開く* を押してください。

### macOS どの .dmg を使うか
M1/M2/M3/M4 プロセッサーには `-mac-apple-silicon.dmg`、Intel Mac には `-mac-intel.dmg` (どちらかは Apple メニュー → *この Mac について* で分かります)。

### Linux アプリケーションメニューに YA-MS がない
展開したフォルダー (`~/YA-MS` ではなく) から `./installa.sh` を実行してください。デスクトップによっては、新しい項目を表示するのにログアウト/ログインが必要です。`~/YA-MS/YA-MS` でいつでも起動できます。

### ヨーロッパ地図が表示されない
*ヨーロッパ地図がありません (初回起動時にネット接続が必要)。* Natural Earth の地図は初回起動時に `data/mappa` へダウンロードされます。インターネットに接続して YA-MS を再起動してください。

## 表示

### Linux で日本語が四角で表示される
システムに CJK フォント (中国語・日本語・韓国語) がありません。**Noto CJK** フォントをインストールして YA-MS を再起動してください。アラビア語、ヘブライ語、ウルドゥー語、ヒンディー語、ベンガル語でも同じことが起こります: Debian、Ubuntu、Raspberry Pi OS では `fonts-noto-core` もインストールしてください。

| ディストリビューション | コマンド |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### 文字が小さすぎる、またはグラフの場所が足りない
**フォント** スライダー (100–300 %) を使い、**操作** で操作部を折りたたんでください。[設定](Settings-and-Data-Folder-ja#フォントと操作) を参照。

### 夜間に画面が明るすぎる
**テーマ** のリストで **夜間** または **ブラック** を選んでください。

## インターネットとレーダーデータ

### 「インターネット接続がありません」のメッセージ
どのソースにも接続できないとき、YA-MS はこれを **1 度だけ** 表示し、ステータスバーが赤くなります。プログラムは**最後に保存したデータ**で動作を続け、5 分ごとに自動で再試行します。ネットワークが戻ると *接続が回復しました。* と表示されます。何もする必要はありません。

### レーダーフラックスの橙の警告「フラックスの縦軸目盛を読み取れません …」
Collm レーダーは縦軸目盛を毎日変え、YA-MS はそれをグラフのラベルから読み取ります。ラベルを読み取れない場合、プログラムは校正済み目盛 0–1200 流星/時を使い、**値は要確認**と警告します。通常は次の時間のグラフが正しく読み取られます。*グラフの形式が変更されました* または *フラックスグラフの軸が想定位置に見つかりません* が何時間も続く場合は、レーダーがグラフの形式を変えています: [報告してください](Contributing-and-Contacts-ja)。

### 「高度グラフの目盛が変更されました」
高度の統計 (最頻値・平均・中央値) は有効です。無効になるのは高度ヒストグラムの絶対数だけです。

### 「レーダーフラックス: データなし」
[レーダーフラックス](Radar-Flux-ja) で **今すぐ取得** を押し、`data/fonti_radar.csv` で Collm が `attivo=1` になっているか確認してください。

### RMOB なぜ自動取得がオフなのか
RMOB は**自動プログラムがファイルを取得しないよう**求めています。*5 分ごとに自動取得* は RMOB から許可を得た後でのみ有効にしてください。それまでは **RMOB を今すぐ取得** または **RMOB ファイルをディスクから読込...** を使ってください。[実験的予報](Experimental-Forecasts-ja#rmob-と自動プログラム) を参照。

### RMOB「ファイル形式を認識できません」または読み込まれた時間が少ない
観測者の月間テキストファイル (`NAME_MMYYYYrmob.TXT`) か、観測者 1 人の会報の表を使ってください。指数の当てはめには、Collm のデータ (昨日と今日) と共通の時間が 3 時間以上必要です。

## 計算

### 「自局のロケーターが無効です」/「相手局のロケーターが無効です」
ロケーターは 4、6、8 文字でなければなりません (例: `JN70`、`JN70CN`、`JN70CN12`)。

### 「E 層の共通領域なし」
パスが流星痕高度での到達距離の 2 倍 (ビーム仰角 0°、流星痕 89.5 km で約 2 × 1062 km) より長い: 1 回の流星散乱ホップではカバーできません。**ビーム仰角** を上げると到達距離はさらに短くなります。

### Hot A / Hot B が灰色になっている
相手局に向けたときに既に**アンテナビーム内**にあります: アンテナを振る必要はありません。[天球図](Sky-View-ja#警告) を参照。

### 効率が MCG_MS や MS-Soft と異なる
YA-MS は実際のパスと独自のモデルを使います。OH5IY と MCG_MS の目盛は詳しく文書化されていません。絶対的なパーセントではなく時間帯や傾向を比較し、[モデル](Efficiency-Calculation-ja#モデル) を参照してください。

### GRAVES のビーム通過がずれているように見える
ビームのシーケンスは PC の時計から計算します: NTP サーバーで同期してください。GRAVES の指令局もときどきシーケンスを数ステップずらします。詳細は予測であり、受信して確認してください。

## その他の質問

**YA-MS は無料ですか?** はい、アマチュア無線家のための無料プログラムです。

**ローテーターや無線機を制御しますか?** いいえ。YA-MS は予報と計画のためのツールです。QSO にはデジタルモードのプログラム (例: MSHV、WSJT-X) を使ってください。

**432 MHz より上でも使えますか?** バンドリストは 432 MHz まで (28、50、70、144、222、432) です。実験的予報は 28–1300 MHz の任意の周波数を受け付けますが、使用する SM6FHZ 則は 144 MHz と 432 MHz での経験に基づくものです。

**何かがおかしい。** オペレーティングシステム、YA-MS のバージョン、行った操作を添えて作者に連絡してください: [貢献と連絡先](Contributing-and-Contacts-ja) を参照。
