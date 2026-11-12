[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · **Latviešu** · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalēšana

Visas pakotnes ir lapā **[Releases](https://github.com/ic8tem/YA-MS/releases)** (zemāk failu nosaukumos `x.y.z` ir versija, piem. `1.2.0`). Nekas nav jākompilē un nekas cits nav jāinstalē: katrā pakotnē ir .NET 8 izpildlaiks.

| Sistēma | Fails | Instalē mapē |
|---|---|---|
| Windows (64 biti) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalētājs) | `C:\YA-MS` |
| Windows (64 biti), portatīvā | `YA-MS-x.y.z-windows-x64-portatile.zip` | jebkurā mapē, kurā vari rakstīt |
| Windows (32 biti, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` vai `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows uz ARM (64 bitu, datori ar Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` vai `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 biti): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| Linux (64 biti), jebkurš distributīvs | `YA-MS-x.y.z-linux-x64.tar.gz` (portatīvi vai ar `./installa.sh`) | `~/YA-MS` vai jebkura mape |
| Linux (64 bitu): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` vai jebkura mape |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 biti) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 biti) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian pakotne | `ya-ms_x.y.z_arm64.deb` (64 biti) vai `ya-ms_x.y.z_armhf.deb` (32 biti) | `~/YA-MS` (tur nokopēts pirmajā palaišanā) |
| Linux ARM 64 bitu, jebkurš distributīvs (piem. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (portatīvi vai ar `./installa.sh`) | `~/YA-MS` vai jebkura mape |
| Linux armv7l (ARM 32 bitu), jebkurš distributīvs | `YA-MS-x.y.z-linux-armv7l.tar.gz` (portatīvi vai ar `./installa.sh`) | `~/YA-MS` vai jebkura mape |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, tikai lietotne | `YA-MS-x.y.z-mac-apple-silicon-app.zip` vai `...-mac-intel-app.zip` | mape, kurā atarhivē `YA-MS.app` |

**Programma un tās `data` mape vienmēr paliek kopā** YA-MS mapē: tur ir visi dati un iestatījumi (ne AppData, ne sistēmas mapes). Sk. [Iestatījumi un datu mape](Settings-and-Data-Folder-lv).

## Windows

### Instalētājs
1. Lejupielādē `YA-MS-x.y.z-windows-x64-setup.exe` un palaid to.
2. Ja **SmartScreen** rāda "Windows aizsargāja jūsu datoru": *Papildinformācija* → *Tik un tā palaist* (programma nav parakstīta ar komerciālu sertifikātu).
3. YA-MS tiek instalēta mapē **`C:\YA-MS`** **bez administratora tiesībām**, ar ikonu izvēlnē Sākt un, ja to atzīmē, ar ikonu uz darbvirsmas.

### Portatīvā versija
Atarhivē `YA-MS-x.y.z-windows-x64-portatile.zip`, kur vēlies (mapē, kurā vari rakstīt, nevis *Program Files*), un palaid `YA-MS.exe`. Visu mapi var nokopēt uz USB zibatmiņu vai citu datoru.

## Linux

1. Atarhivē `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Atarhivētajā mapē palaid:
   ```sh
   ./installa.sh
   ```
3. Skripts nokopē YA-MS uz **`~/YA-MS`** (root tiesības nav vajadzīgas) un pievieno **YA-MS** lietotņu izvēlnei (kategorija *HamRadio*). Programmu var palaist arī ar `~/YA-MS/YA-MS`.

### Debian pakotne (.deb)
Debian, Ubuntu, Mint un Raspberry Pi OS sistēmās tā vietā vari instalēt `ya-ms_x.y.z_amd64.deb` (Raspberry Pi – `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Pakotne ievieto programmu mapē `/opt/ya-ms` un pievieno **YA-MS** izvēlnei. Pirmajā palaišanā (un pēc katras jaunas versijas) programma nokopē sevi uz **`~/YA-MS`** un darbojas no turienes, tāpēc mape `data` paliek blakus programmai un tavi iestatījumi saglabājas.

### Portatīvā versija
`.tar.gz` darbojas arī bez instalēšanas: atarhivē to jebkur, kur vari rakstīt, un palaid `./YA-MS` no šīs mapes.

Japāņu tekstam var būt vajadzīgi Noto CJK fonti: sk. [Problēmu risināšana](Troubleshooting-FAQ-lv#linux-japāņu-teksts-redzams-kā-kvadrātiņi).

## Raspberry Pi

Tāpat kā Linux: atarhivē `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (vai `-32bit` 32 bitu Raspberry Pi OS) un atarhivētajā mapē palaid `./installa.sh`.

- Lai uzzinātu, kāda sistēma tev ir, terminālī ieraksti `uname -m`: `aarch64` → 64 bitu pakotne, `armv7l` → 32 bitu pakotne.
- Atbalstīti: Raspberry Pi 2 (tikai 32 biti), 3, 4, 5, 400 un 500 ar Raspberry Pi OS darbvirsmas versiju. **Nav atbalstīti:** Pi Zero / Zero W un Pi 1 (ARMv6 procesors, .NET tur nedarbojas); Pi Zero 2 W darbojas ar 64 bitu pakotni, bet 512 MB RAM ir knapi.
- Ieteicams Pi 4 vai 5 ar vismaz 2 GB RAM; pirmā palaišana aizņem dažas sekundes ilgāk nekā datorā.

## macOS

1. Izvēlies pareizo failu: `-mac-apple-silicon.dmg` procesoriem M1/M2/M3/M4, `-mac-intel.dmg` Intel Mac datoriem.
2. Atver `.dmg`, **labais klikšķis uz "Installa YA-MS.command" → Open** un apstiprini.
3. Skripts nokopē `YA-MS.app` uz **`~/YA-MS`** un atver to.

Kā alternatīva, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` satur tikai `YA-MS.app`: atarhivē to paša izvēlētā mapē (kurā vari rakstīt); mape `data` tiek izveidota blakus `YA-MS.app`. Pirmo reizi – labais klikšķis → **Open**.

Programmu nav parakstījis Apple, tāpēc pirmo reizi macOS prasa apstiprinājumu; sk. [Problēmu risināšana](Troubleshooting-FAQ-lv#macos-nevar-atvērt-jo-izstrādātājs-nav-identificēts).

## Pirmā palaišana

- **Eiropas karte** (Natural Earth krasta līnijas un robežas) pirmajā reizē tiek automātiski lejupielādēta mapē `data/mappa`: interneta savienojums vajadzīgs vienu reizi.
- **Radaru dati** (Collm, Sodankylä) tiek lejupielādēti uzreiz un pēc tam pārbaudīti ik pēc 5 minūtēm.
- Saskarne startē tavas sistēmas valodā, ja tā ir viena no 36 pieejamajām, citādi itāļu valodā; to var mainīt augšā pa labi (sk. [Iestatījumi](Settings-and-Data-Folder-lv#valoda)).

## Atjaunināšana

Instalē jauno versiju **virs vecās** (tas pats instalētājs, tā pati mape). Iestatījumi (`config.ini`), meteoru skaita arhīvi un karte paliek mapē `data`. Tulkojumu faili mapē `data/lingue` tiek aizstāti, ja jaunie ir svaigāki.

**No 1.8.0 YA-MS atjauninās pati.** Startējot vienreiz dienā tā pārbauda GitHub, vai ir jauna versija, un to piedāvā; poga **Atjauninājumi** apakšējā joslā pārbauda manuāli. *Atjaunināt tagad* lejupielādē jūsu sistēmas pārnēsājamo pakotni, aizstāj programmas failus, saglabā mapi `data` (mainītie programmas faili vispirms tiek nokopēti uz `data/backup/v<vecā versija>`) un restartējas; programmas mapei jābūt rakstāmai. Ja startējot trūkst programmas failu (mapē `data` vai `doc`), logs tos uzskaita un piedāvā tos atkal lejupielādēt no GitHub. Lai vairs nemeklētu jaunas versijas, `config.ini` iestatiet `controlla_aggiornamenti=0`.

## Kompilēšana no pirmkoda (tikai izstrādātājiem)

Instalētājus veido GitHub Actions (`.github/workflows/build.yml`) pie katras zara `release` atjaunināšanas (versija tiek ņemta no faila `VERSION`), un tas izveido arī laidienu `vX.Y.Z`. Lokāli:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # vai linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumentus (visās valodās) no jauna ģenerē ar `tools/build_documenti.sh`.

Tālāk: [Darba sākšana](Getting-Started-lv).
