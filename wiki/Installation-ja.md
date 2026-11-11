[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · **日本語** · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# インストール

すべてのパッケージは **[Releases](https://github.com/ic8tem/YA-MS/releases)** ページにあります (以下のファイル名の `x.y.z` はバージョン、例: `1.2.0`)。コンパイルも追加のインストールも不要です。各パッケージに .NET 8 ランタイムが含まれています。

| システム | ファイル | インストール先 |
|---|---|---|
| Windows (64 ビット) | `YA-MS-x.y.z-windows-x64-setup.exe` (インストーラー) | `C:\YA-MS` |
| Windows (64 ビット)、ポータブル版 | `YA-MS-x.y.z-windows-x64-portatile.zip` | 書き込み可能な任意のフォルダー |
| Windows (32 ビット、Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` または `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 ビット): Debian、Ubuntu、Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (初回起動時にそこへコピー) |
| Linux (64 ビット)、任意のディストリビューション | `YA-MS-x.y.z-linux-x64.tar.gz` (ポータブル、または `./installa.sh` で) | `~/YA-MS` または任意のフォルダー |
| Raspberry Pi 3/4/5、400/500 (Raspberry Pi OS 64 ビット) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 ビット) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi、Debian パッケージ | `ya-ms_x.y.z_arm64.deb` (64 ビット) または `ya-ms_x.y.z_armhf.deb` (32 ビット) | `~/YA-MS` (初回起動時にそこへコピー) |
| macOS、Apple シリコン (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS、Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS、アプリケーションのみ | `YA-MS-x.y.z-mac-apple-silicon-app.zip` または `...-mac-intel-app.zip` | `YA-MS.app` を展開したフォルダー |

**プログラムとその `data` フォルダーは常に一緒に** YA-MS フォルダー内に置かれます。すべてのデータと設定はそこにあります (AppData もシステムフォルダーも使いません)。[設定とデータフォルダー](Settings-and-Data-Folder-ja) を参照してください。

## Windows

### インストーラー
1. `YA-MS-x.y.z-windows-x64-setup.exe` をダウンロードして実行します。
2. **SmartScreen** が「Windows によって PC が保護されました」と表示した場合: *詳細情報* → *実行* (このプログラムは商用証明書で署名されていません)。
3. YA-MS は **`C:\YA-MS`** に**管理者権限なしで**インストールされ、スタートメニューのアイコンと、チェックを入れた場合はデスクトップのアイコンが作られます。

### ポータブル版
`YA-MS-x.y.z-windows-x64-portatile.zip` を好きな場所 (書き込み可能なフォルダー。*Program Files* は不可) に展開し、`YA-MS.exe` を実行します。フォルダーごと USB メモリや別のコンピューターにコピーできます。

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz` を展開します。
2. 展開したフォルダーで次を実行します:
   ```sh
   ./installa.sh
   ```
3. スクリプトが YA-MS を **`~/YA-MS`** にコピーし (root 権限不要)、アプリケーションメニュー (カテゴリー *HamRadio*) に **YA-MS** を追加します。`~/YA-MS/YA-MS` で起動することもできます。

### Debian パッケージ (.deb)
Debian、Ubuntu、Mint、Raspberry Pi OS では、代わりに `ya-ms_x.y.z_amd64.deb` (Raspberry Pi では `_arm64.deb` / `_armhf.deb`) をインストールすることもできます:
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
パッケージはプログラムを `/opt/ya-ms` に置き、メニューに **YA-MS** を追加します。初回起動時 (および新しいバージョンのたび) に自身を **`~/YA-MS`** にコピーしてそこから実行するため、`data` フォルダーはプログラムの隣に保たれ、設定も維持されます。

### ポータブル版
`.tar.gz` はインストールせずに使うこともできます。書き込み可能な任意の場所に展開し、そのフォルダーで `./YA-MS` を実行します。

日本語を表示するには Noto CJK フォントが必要な場合があります。[トラブルシューティング](Troubleshooting-FAQ-ja#linux-で日本語が四角で表示される) を参照してください。

## Raspberry Pi

手順は Linux と同じです。`YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (32 ビット版 Raspberry Pi OS では `-32bit`) を展開し、展開したフォルダーで `./installa.sh` を実行します。

- システムの種類はターミナルで `uname -m` を実行すると分かります。`aarch64` → 64 ビット版パッケージ、`armv7l` → 32 ビット版パッケージ。
- 対応機種: Raspberry Pi 2 (32 ビットのみ)、3、4、5、400、500 (デスクトップ版 Raspberry Pi OS)。**非対応:** Pi Zero / Zero W と Pi 1 (ARMv6 プロセッサーでは .NET が動作しません)。Pi Zero 2 W は 64 ビット版で動作しますが、512 MB のメモリーでは余裕がありません。
- メモリー 2 GB 以上の Pi 4 または 5 を推奨します。初回起動は PC より数秒長くかかります。

## macOS

1. 正しいファイルを選びます: M1/M2/M3/M4 プロセッサーには `-mac-apple-silicon.dmg`、Intel Mac には `-mac-intel.dmg`。
2. `.dmg` を開き、**「Installa YA-MS.command」を右クリック → 開く** を選んで確認します。
3. スクリプトが `YA-MS.app` を **`~/YA-MS`** にコピーして起動します。

別の方法として、`YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` には `YA-MS.app` だけが入っています。好きなフォルダー (書き込み可能な場所) に展開してください。`data` フォルダーは `YA-MS.app` の隣に作成されます。初回は右クリック → **開く** を選びます。

このプログラムは Apple の署名がないため、初回は macOS が確認を求めます。[トラブルシューティング](Troubleshooting-FAQ-ja#macos-開発元を確認できないため開けない) を参照してください。

## 初回起動

- **ヨーロッパ地図** (Natural Earth の海岸線と国境) は初回に `data/mappa` へ自動的にダウンロードされます。インターネット接続が 1 度だけ必要です。
- **レーダーデータ** (Collm、Sodankylä) はすぐにダウンロードされ、その後 5 分ごとに確認されます。
- 表示言語は、システムの言語が 36 の対応言語のいずれかであればその言語、そうでなければイタリア語で始まります。右上で変更できます ([設定](Settings-and-Data-Folder-ja#表示言語) を参照)。

## アップデート

新しいバージョンを**古いバージョンの上に**インストールします (同じインストーラー、同じフォルダー)。設定 (`config.ini`)、フラックスのアーカイブ、地図は `data` に残ります。`data/lingue` の翻訳ファイルは、新しいものの方が新しければ置き換えられます。

**1.8.0 から YA-MS は自動で更新されます。** 起動時（1 日 1 回）に GitHub で新しいバージョンがあるか確認し、あれば案内します。下部バーの **更新** ボタンで手動でも確認できます。*今すぐ更新* を選ぶと、お使いのシステム用のポータブルパッケージをダウンロードし、プログラムのファイルを置き換え、`data` フォルダーは残し（変更されるプログラムのファイルは先に `data/backup/v<旧バージョン>` にコピー）、再起動します。プログラムのフォルダーに書き込める必要があります。起動時にプログラムのファイル（`data` または `doc` 内）が欠けている場合は、ウィンドウに一覧が表示され、GitHub から再ダウンロードするか尋ねられます。新しいバージョンを確認しないようにするには、`config.ini` に `controlla_aggiornamenti=0` を設定します。

## ソースからのビルド (開発者向け)

インストーラーは `release` ブランチが更新されるたびに GitHub Actions (`.github/workflows/build.yml`) で作られ (バージョンは `VERSION` ファイルから取得)、リリース `vX.Y.Z` も作成されます。ローカルでは:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

文書 (全言語) は `tools/build_documenti.sh` で再生成します。

次へ: [はじめに](Getting-Started-ja)。
