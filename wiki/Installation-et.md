[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · **Eesti** · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Paigaldamine

Kõik paketid on lehel **[Releases](https://github.com/ic8tem/YA-MS/releases)** (allpool toodud failinimedes on `x.y.z` versioon, nt `1.2.0`). Midagi ei pea kompileerima ega lisaks paigaldama: iga pakett sisaldab .NET 8 käituskeskkonda.

| Süsteem | Fail | Paigaldatakse kausta |
|---|---|---|
| Windows (64-bitine) | `YA-MS-x.y.z-windows-x64-setup.exe` (paigaldaja) | `C:\YA-MS` |
| Windows (64-bitine), kaasaskantav | `YA-MS-x.y.z-windows-x64-portatile.zip` | mis tahes kaust, kuhu saad kirjutada |
| Windows (32-bitine, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` või `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bitine) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bitine) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bitine) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Programm ja selle kaust `data` on alati koos** YA-MS-i kaustas: kõik andmed ja seaded on seal (ei AppData-t ega süsteemikaustu). Vt [Seaded ja andmekaust](Settings-and-Data-Folder-et).

## Windows

### Paigaldaja
1. Laadi alla `YA-MS-x.y.z-windows-x64-setup.exe` ja käivita see.
2. Kui **SmartScreen** näitab "Windows protected your PC": *More info* → *Run anyway* (programm ei ole allkirjastatud kommertssertifikaadiga).
3. YA-MS paigaldatakse kausta **`C:\YA-MS`**, **ilma administraatoriõigusteta**, koos Start-menüü ikooni ja soovi korral töölaua ikooniga.

### Kaasaskantav
Paki `YA-MS-x.y.z-windows-x64-portatile.zip` lahti kuhu soovid (kausta, kuhu saad kirjutada, mitte *Program Files*) ja käivita `YA-MS.exe`. Kogu kausta võid kopeerida USB-mälupulgale või teise arvutisse.

## Linux

1. Paki lahti `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Käivita lahtipakitud kaustast:
   ```sh
   ./installa.sh
   ```
3. Skript kopeerib YA-MS-i kausta **`~/YA-MS`** (root-õigusi pole vaja) ja lisab **YA-MS-i** rakenduste menüüsse (kategooria *HamRadio*). Programmi saab käivitada ka käsuga `~/YA-MS/YA-MS`.

Jaapani teksti jaoks võib olla vaja Noto CJK fonte: vt [Tõrkeotsing](Troubleshooting-FAQ-et#linux-jaapani-tekst-kuvatakse-kastikestena).

## Raspberry Pi

Sama toiming nagu Linuxis: paki lahti `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (või 32-bitise Raspberry Pi OS-i korral `-32bit`) ja käivita lahtipakitud kaustast `./installa.sh`.

- Et teada saada, milline süsteem sul on, sisesta terminali `uname -m`: `aarch64` → 64-bitine pakett, `armv7l` → 32-bitine pakett.
- Toetatud: Raspberry Pi 2 (ainult 32-bitine), 3, 4, 5, 400 ja 500, Raspberry Pi OS-i töölauaversiooniga. **Ei ole toetatud:** Pi Zero / Zero W ja Pi 1 (ARMv6 protsessor, .NET seal ei tööta); Pi Zero 2 W töötab 64-bitise paketiga, kuid 512 MB RAM-i on napp.
- Soovitatav on Pi 4 või 5 vähemalt 2 GB RAM-iga; esimene käivitus võtab mõne sekundi kauem kui PC-l.

## macOS

1. Vali õige fail: `-mac-apple-silicon.dmg` protsessoritele M1/M2/M3/M4, `-mac-intel.dmg` Inteli Macidele.
2. Ava `.dmg`, **paremklõps failil "Installa YA-MS.command" → Open** ja kinnita.
3. Skript kopeerib `YA-MS.app` kausta **`~/YA-MS`** ja avab selle.

Programm ei ole Apple'i poolt allkirjastatud, seega küsib macOS esimesel korral kinnitust; vt [Tõrkeotsing](Troubleshooting-FAQ-et#macos-ei-saa-avada-sest-arendaja-on-tuvastamata).

## Esimene käivitus

- **Euroopa kaart** (Natural Earthi rannajooned ja piirid) laaditakse esimesel korral automaatselt alla kausta `data/mappa`: internetiühendust on vaja üks kord.
- **Radariandmed** (Collm, Sodankylä) laaditakse kohe alla ja seejärel kontrollitakse neid iga 5 minuti järel.
- Kasutajaliides käivitub sinu süsteemi keeles, kui see on üks kuuest saadaolevast, muidu itaalia keeles; keelt saab muuta paremal üleval (vt [Seaded](Settings-and-Data-Folder-et#keel)).

## Uuendamine

Paigalda uus versioon **vana peale** (sama paigaldaja, sama kaust). Seaded (`config.ini`), vooarhiivid ja kaart jäävad kausta `data`. Kausta `data/lingue` tõlkefailid asendatakse, kui uued on värskemad.

## Lähtekoodist ehitamine (ainult arendajatele)

Paigaldajad toodab GitHub Actions (`.github/workflows/build.yml`) iga `release` haru uuendusega (versioon võetakse failist `VERSION`), mis loob ka väljalaske `vX.Y.Z`. Kohalikult:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # või linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumendid luuakse uuesti käskudega `tools/build_spiegazione.py data` ja `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Edasi: [Alustamine](Getting-Started-et).
