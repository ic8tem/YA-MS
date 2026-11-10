[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-BR) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · **Tagalog** · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-TW)

# Pag-install

Nasa pahinang **[Releases](https://github.com/ic8tem/YA-MS/releases)** ang lahat ng package (sa mga pangalan ng file sa ibaba, ang `x.y.z` ay ang bersyon, hal. `1.2.0`). Walang kailangang i-compile at walang ibang kailangang i-install: may kasamang .NET 8 runtime ang bawat package.

| Sistema | File | Saan ini-install |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installer) | `C:\YA-MS` |
| Windows (64-bit), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | anumang folder na may pahintulot kang magsulat |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` o `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (kinokopya roon sa unang pagsisimula) |
| Linux (64-bit), anumang distribution | `YA-MS-x.y.z-linux-x64.tar.gz` (portable o gamit ang `./installa.sh`) | `~/YA-MS` o anumang folder |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian package | `ya-ms_x.y.z_arm64.deb` (64-bit) o `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (kinokopya roon sa unang pagsisimula) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, application lamang | `YA-MS-x.y.z-mac-apple-silicon-app.zip` o `...-mac-intel-app.zip` | ang folder kung saan mo ie-extract ang `YA-MS.app` |

**Laging magkasama ang programa at ang `data` folder nito** sa folder na YA-MS: naroon ang lahat ng datos at setting (walang AppData, walang system folder). Tingnan ang [Mga setting at folder ng datos](Settings-and-Data-Folder-tl).

## Windows

### Installer
1. I-download ang `YA-MS-x.y.z-windows-x64-setup.exe` at patakbuhin ito.
2. Kung magpakita ang **SmartScreen** ng "Windows protected your PC": *More info* → *Run anyway* (hindi naka-sign ang programa ng komersiyal na sertipiko).
3. Ini-install ang YA-MS sa **`C:\YA-MS`**, **nang walang karapatang administrator**, na may icon sa Start menu at, kung lalagyan mo ng tsek, isang icon sa desktop.

### Portable
I-extract ang `YA-MS-x.y.z-windows-x64-portatile.zip` kahit saan mo gusto (isang folder na may pahintulot kang magsulat, hindi *Program Files*) at patakbuhin ang `YA-MS.exe`. Maaari mong kopyahin ang buong folder sa isang USB stick o sa ibang computer.

## Linux

1. I-extract ang `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Mula sa na-extract na folder, patakbuhin ang:
   ```sh
   ./installa.sh
   ```
3. Kinokopya ng script ang YA-MS sa **`~/YA-MS`** (hindi kailangan ng root) at idinadagdag ang **YA-MS** sa menu ng mga application (kategoryang *HamRadio*). Maaari mo rin itong simulan gamit ang `~/YA-MS/YA-MS`.

### Debian package (.deb)
Sa Debian, Ubuntu, Mint at Raspberry Pi OS, maaari mo ring i-install sa halip ang `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` sa Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Inilalagay ng package ang programa sa `/opt/ya-ms` at idinadagdag ang **YA-MS** sa menu. Sa unang pagsisimula (at pagkatapos ng bawat bagong bersyon), kinokopya nito ang sarili sa **`~/YA-MS`** at doon tumatakbo, kaya nananatili ang folder na `data` sa tabi ng programa at naiingatan ang iyong mga setting.

### Portable
Gumagana rin ang `.tar.gz` nang hindi ini-install: i-extract ito kahit saan na may pahintulot kang magsulat at patakbuhin ang `./YA-MS` mula sa folder na iyon.

Para sa tekstong Hapones, maaaring kailanganin mo ang mga font na Noto CJK: tingnan ang [Pag-troubleshoot](Troubleshooting-FAQ-tl#linux-lumalabas-na-mga-kahon-ang-tekstong-hapones).

## Raspberry Pi

Kapareho ng pamamaraan sa Linux: i-extract ang `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (o `-32bit` sa Raspberry Pi OS 32-bit) at patakbuhin ang `./installa.sh` mula sa na-extract na folder.

- Para malaman kung aling sistema ang mayroon ka, i-type ang `uname -m` sa terminal: `aarch64` → package na 64-bit, `armv7l` → package na 32-bit.
- Suportado: Raspberry Pi 2 (32-bit lamang), 3, 4, 5, 400 at 500, na may desktop na bersyon ng Raspberry Pi OS. **Hindi suportado:** Pi Zero / Zero W at Pi 1 (processor na ARMv6, hindi tumatakbo roon ang .NET); gumagana ang Pi Zero 2 W sa package na 64-bit pero kapos ang 512 MB na RAM.
- Inirerekomenda ang Pi 4 o 5 na may hindi bababa sa 2 GB na RAM; ilang segundong mas matagal ang unang pagsisimula kaysa sa PC.

## macOS

1. Piliin ang tamang file: `-mac-apple-silicon.dmg` para sa mga processor na M1/M2/M3/M4, `-mac-intel.dmg` para sa mga Mac na Intel.
2. Buksan ang `.dmg`, **i-right-click ang "Installa YA-MS.command" → Open** at kumpirmahin.
3. Kinokopya ng script ang `YA-MS.app` sa **`~/YA-MS`** at binubuksan ito.

Bilang alternatibo, ang `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` ay naglalaman lamang ng `YA-MS.app`: i-extract ito sa folder na gusto mo (na may pahintulot kang magsulat); ginagawa ang folder na `data` sa tabi ng `YA-MS.app`. Sa unang pagkakataon: i-right-click → **Open**.

Hindi naka-sign ng Apple ang programa, kaya sa unang pagkakataon ay hihingi ng kumpirmasyon ang macOS; tingnan ang [Pag-troubleshoot](Troubleshooting-FAQ-tl#macos-hindi-mabuksan-dahil-galing-ito-sa-hindi-kilalang-developer).

## Unang pagsisimula

- Awtomatikong dina-download sa `data/mappa` ang **mapa ng Europa** (mga baybayin at hangganan ng Natural Earth) sa unang pagkakataon: minsan lang kailangan ng koneksiyon sa internet.
- Agad na dina-download ang **datos ng radar** (Collm, Sodankylä) at pagkatapos ay sinusuri bawat 5 minuto.
- Nagsisimula ang interface sa wika ng iyong sistema kung isa ito sa 28 na available, kung hindi ay sa Italyano; palitan ito sa kanang itaas (tingnan ang [Mga setting](Settings-and-Data-Folder-tl#wika)).

## Pag-update

I-install ang bagong bersyon **sa ibabaw ng luma** (parehong installer, parehong folder). Nananatili sa `data` ang mga setting (`config.ini`), ang mga archive ng flux at ang mapa. Pinapalitan ang mga file ng salin sa `data/lingue` kapag mas bago ang mga bago.

## Pag-build mula sa source (para sa mga developer lamang)

Ginagawa ang mga installer ng GitHub Actions (`.github/workflows/build.yml`) sa bawat update ng branch na `release` (kinukuha ang bersyon mula sa file na `VERSION`), na lumilikha rin ng release na `vX.Y.Z`. Sa lokal:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # o linux-x64, linux-arm64, linux-arm, osx-arm64
```

Muling nililikha ang mga dokumento gamit ang `tools/build_spiegazione.py data` at `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Susunod: [Pagsisimula](Getting-Started-tl).
