[English](Installation) · [Русский](Installation-ru) · [Deutsch](Installation-de) · **日本語**

# インストール

すべてのパッケージは **[Releases](https://github.com/ic8tem/YA-MS/releases)** ページにあります (以下のファイル名の `x.y.z` はバージョン、例: `1.2.0`)。コンパイルも追加のインストールも不要です。各パッケージに .NET 8 ランタイムが含まれています。

| システム | ファイル | インストール先 |
|---|---|---|
| Windows (64 ビット) | `YA-MS-x.y.z-windows-x64-setup.exe` (インストーラー) | `C:\YA-MS` |
| Windows (64 ビット)、ポータブル版 | `YA-MS-x.y.z-windows-x64-portatile.zip` | 書き込み可能な任意のフォルダー |
| Linux (64 ビット) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5、400/500 (Raspberry Pi OS 64 ビット) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 ビット) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS、Apple シリコン (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS、Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

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

このプログラムは Apple の署名がないため、初回は macOS が確認を求めます。[トラブルシューティング](Troubleshooting-FAQ-ja#macos-開発元を確認できないため開けない) を参照してください。

## 初回起動

- **ヨーロッパ地図** (Natural Earth の海岸線と国境) は初回に `data/mappa` へ自動的にダウンロードされます。インターネット接続が 1 度だけ必要です。
- **レーダーデータ** (Collm、Sodankylä) はすぐにダウンロードされ、その後 5 分ごとに確認されます。
- 表示言語は、システムの言語が 6 つの対応言語のいずれかであればその言語、そうでなければイタリア語で始まります。右上で変更できます ([設定](Settings-and-Data-Folder-ja#表示言語) を参照)。

## アップデート

新しいバージョンを**古いバージョンの上に**インストールします (同じインストーラー、同じフォルダー)。設定 (`config.ini`)、フラックスのアーカイブ、地図は `data` に残ります。`data/lingue` の翻訳ファイルは、新しいものの方が新しければ置き換えられます。

## ソースからのビルド (開発者向け)

インストーラーは `release` ブランチが更新されるたびに GitHub Actions (`.github/workflows/build.yml`) で作られ (バージョンは `VERSION` ファイルから取得)、リリース `vX.Y.Z` も作成されます。ローカルでは:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

文書は `tools/build_spiegazione.py data` と `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` で再生成します。

次へ: [はじめに](Getting-Started-ja)。
