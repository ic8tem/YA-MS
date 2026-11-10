[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · **Lietuvių** · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Diegimas

Visi paketai yra puslapyje **[Releases](https://github.com/ic8tem/YA-MS/releases)** (toliau pateiktuose failų pavadinimuose `x.y.z` yra versija, pvz., `1.2.0`). Nieko nereikia kompiliuoti ir nieko papildomai diegti: kiekviename pakete yra .NET 8 vykdymo aplinka.

| Sistema | Failas | Įdiegiama į |
|---|---|---|
| Windows (64 bitų) | `YA-MS-x.y.z-windows-x64-setup.exe` (diegimo programa) | `C:\YA-MS` |
| Windows (64 bitų), nešiojamoji | `YA-MS-x.y.z-windows-x64-portatile.zip` | bet kurį aplanką, į kurį galite rašyti |
| Windows (32 bitų, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` arba `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bitų): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (nukopijuojama ten pirmą kartą paleidžiant) |
| Linux (64 bitų), bet kuris distributyvas | `YA-MS-x.y.z-linux-x64.tar.gz` (nešiojamoji arba su `./installa.sh`) | `~/YA-MS` arba bet kuris aplankas |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bitų) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bitų) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian paketas | `ya-ms_x.y.z_arm64.deb` (64 bitų) arba `ya-ms_x.y.z_armhf.deb` (32 bitų) | `~/YA-MS` (nukopijuojama ten pirmą kartą paleidžiant) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, tik programa | `YA-MS-x.y.z-mac-apple-silicon-app.zip` arba `...-mac-intel-app.zip` | aplankas, į kurį išskleidžiate `YA-MS.app` |

**Programa ir jos aplankas `data` visada būna kartu** YA-MS aplanke: ten yra visi duomenys ir nustatymai (jokio AppData, jokių sisteminių aplankų). Žr. [Nustatymai ir duomenų aplankas](Settings-and-Data-Folder-lt).

## Windows

### Diegimo programa
1. Atsisiųskite `YA-MS-x.y.z-windows-x64-setup.exe` ir paleiskite.
2. Jei **SmartScreen** rodo „Windows protected your PC“: *More info* → *Run anyway* (programa nepasirašyta komerciniu sertifikatu).
3. YA-MS įdiegiama į **`C:\YA-MS`**, **be administratoriaus teisių**, su piktograma meniu Start ir, jei pažymėsite, darbalaukyje.

### Nešiojamoji versija
Išskleiskite `YA-MS-x.y.z-windows-x64-portatile.zip` kur norite (į aplanką, į kurį galite rašyti, ne į *Program Files*) ir paleiskite `YA-MS.exe`. Visą aplanką galite nukopijuoti į USB atmintinę ar kitą kompiuterį.

## Linux

1. Išskleiskite `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Iš išskleisto aplanko paleiskite:
   ```sh
   ./installa.sh
   ```
3. Scenarijus nukopijuoja YA-MS į **`~/YA-MS`** (root teisių nereikia) ir prideda **YA-MS** į programų meniu (kategorija *HamRadio*). Programą taip pat galite paleisti komanda `~/YA-MS/YA-MS`.

### Debian paketas (.deb)
Debian, Ubuntu, Mint ir Raspberry Pi OS sistemose vietoj to galite įdiegti `ya-ms_x.y.z_amd64.deb` (Raspberry Pi – `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Paketas įdiegia programą į `/opt/ya-ms` ir prideda **YA-MS** į meniu. Pirmą kartą paleidžiant (ir po kiekvienos naujos versijos) programa nusikopijuoja į **`~/YA-MS`** ir veikia iš ten, todėl aplankas `data` lieka šalia programos, o jūsų nustatymai išsaugomi.

### Nešiojamoji versija
`.tar.gz` veikia ir be diegimo: išskleiskite jį bet kur, kur galite rašyti, ir paleiskite `./YA-MS` iš to aplanko.

Japoniškam tekstui gali prireikti Noto CJK šriftų: žr. [Trikčių šalinimas](Troubleshooting-FAQ-lt#linux-japoniškas-tekstas-rodomas-kvadratėliais).

## Raspberry Pi

Ta pati procedūra kaip Linux: išskleiskite `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (arba `-32bit` su 32 bitų Raspberry Pi OS) ir iš išskleisto aplanko paleiskite `./installa.sh`.

- Norėdami sužinoti, kokią sistemą turite, terminale įveskite `uname -m`: `aarch64` → 64 bitų paketas, `armv7l` → 32 bitų paketas.
- Palaikoma: Raspberry Pi 2 (tik 32 bitų), 3, 4, 5, 400 ir 500 su Raspberry Pi OS darbalaukio versija. **Nepalaikoma:** Pi Zero / Zero W ir Pi 1 (ARMv6 procesorius, .NET ten neveikia); Pi Zero 2 W veikia su 64 bitų paketu, bet 512 MB RAM yra mažoka.
- Rekomenduojamas Pi 4 arba 5 su bent 2 GB RAM; pirmasis paleidimas trunka keliomis sekundėmis ilgiau nei PC.

## macOS

1. Pasirinkite tinkamą failą: `-mac-apple-silicon.dmg` procesoriams M1/M2/M3/M4, `-mac-intel.dmg` Intel Mac kompiuteriams.
2. Atverkite `.dmg`, **dešiniuoju pelės mygtuku spustelėkite „Installa YA-MS.command“ → Open** ir patvirtinkite.
3. Scenarijus nukopijuoja `YA-MS.app` į **`~/YA-MS`** ir jį atveria.

Arba `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` turi tik `YA-MS.app`: išskleiskite jį į pasirinktą aplanką (į kurį galite rašyti); aplankas `data` sukuriamas šalia `YA-MS.app`. Pirmą kartą – dešinysis pelės mygtukas → **Open**.

Programa nepasirašyta Apple, todėl pirmą kartą macOS prašo patvirtinimo; žr. [Trikčių šalinimas](Troubleshooting-FAQ-lt#macos-negalima-atverti-nes-kūrėjas-nenustatytas).

## Pirmasis paleidimas

- **Europos žemėlapis** (Natural Earth pakrantės ir sienos) pirmą kartą automatiškai atsisiunčiamas į `data/mappa`: interneto ryšio reikia vieną kartą.
- **Radarų duomenys** (Collm, Sodankylä) atsisiunčiami iš karto, o paskui tikrinami kas 5 minutes.
- Sąsaja paleidžiama jūsų sistemos kalba, jei ji yra viena iš šešių galimų, kitu atveju itališkai; kalbą galima pakeisti viršuje dešinėje (žr. [Nustatymai](Settings-and-Data-Folder-lt#kalba)).

## Atnaujinimas

Įdiekite naują versiją **ant senosios** (ta pati diegimo programa, tas pats aplankas). Nustatymai (`config.ini`), srauto archyvai ir žemėlapis lieka aplanke `data`. Vertimų failai aplanke `data/lingue` pakeičiami, jei naujieji yra naujesni.

## Kompiliavimas iš išeitinio kodo (tik kūrėjams)

Diegimo programas sukuria GitHub Actions (`.github/workflows/build.yml`) kiekvieną kartą atnaujinus šaką `release` (versija imama iš failo `VERSION`); taip pat sukuriamas leidimas `vX.Y.Z`. Vietoje:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # arba linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumentai iš naujo sugeneruojami komandomis `tools/build_spiegazione.py data` ir `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Toliau: [Pradžia](Getting-Started-lt).
