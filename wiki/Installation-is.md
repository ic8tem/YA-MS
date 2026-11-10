[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · **Íslenska** · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Uppsetning

Allir pakkar eru á síðunni **[Releases](https://github.com/ic8tem/YA-MS/releases)** (í skráarheitunum hér fyrir neðan er `x.y.z` útgáfan, t.d. `1.2.0`). Ekkert þarf að þýða og ekkert annað þarf að setja upp: hver pakki inniheldur .NET 8-keyrsluumhverfið.

| Kerfi | Skrá | Sett upp í |
|---|---|---|
| Windows (64 bita) | `YA-MS-x.y.z-windows-x64-setup.exe` (uppsetningarforrit) | `C:\YA-MS` |
| Windows (64 bita), færanleg útgáfa | `YA-MS-x.y.z-windows-x64-portatile.zip` | hvaða möppu sem þú getur skrifað í |
| Windows (32 bita, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` eða `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bita): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (afritað þangað við fyrstu ræsingu) |
| Linux (64 bita), hvaða dreifing sem er | `YA-MS-x.y.z-linux-x64.tar.gz` (færanlegt eða með `./installa.sh`) | `~/YA-MS` eða hvaða mappa sem er |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bita) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bita) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian-pakki | `ya-ms_x.y.z_arm64.deb` (64 bita) eða `ya-ms_x.y.z_armhf.deb` (32 bita) | `~/YA-MS` (afritað þangað við fyrstu ræsingu) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, aðeins forritið | `YA-MS-x.y.z-mac-apple-silicon-app.zip` eða `...-mac-intel-app.zip` | mappan þar sem þú afþjappar `YA-MS.app` |

**Forritið og mappan þess `data` eru alltaf saman** í möppunni YA-MS: þar eru öll gögn og stillingar (engin AppData, engar kerfismöppur). Sjá [Stillingar og gagnamappa](Settings-and-Data-Folder-is).

## Windows

### Uppsetningarforrit
1. Sæktu `YA-MS-x.y.z-windows-x64-setup.exe` og keyrðu það.
2. Ef **SmartScreen** birtir „Windows verndaði tölvuna þína“: *Frekari upplýsingar* → *Keyra samt* (forritið er ekki undirritað með viðskiptavottorði).
3. YA-MS er sett upp í **`C:\YA-MS`**, **án stjórnandaréttinda**, með tákni í Start-valmyndinni og, ef þú hakar við það, tákni á skjáborðinu.

### Færanleg útgáfa
Afþjappaðu `YA-MS-x.y.z-windows-x64-portatile.zip` hvar sem þú vilt (í möppu sem þú getur skrifað í, ekki *Program Files*) og keyrðu `YA-MS.exe`. Þú getur afritað alla möppuna á USB-lykil eða aðra tölvu.

## Linux

1. Afþjappaðu `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Keyrðu í afþjöppuðu möppunni:
   ```sh
   ./installa.sh
   ```
3. Skriftan afritar YA-MS í **`~/YA-MS`** (root ekki nauðsynlegt) og bætir **YA-MS** við forritavalmyndina (flokkur *HamRadio*). Þú getur líka ræst það með `~/YA-MS/YA-MS`.

### Debian-pakki (.deb)
Á Debian, Ubuntu, Mint og Raspberry Pi OS getur þú í staðinn sett upp `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` á Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Pakkinn setur forritið í `/opt/ya-ms` og bætir **YA-MS** við valmyndina. Við fyrstu ræsingu (og eftir hverja nýja útgáfu) afritar það sig í **`~/YA-MS`** og keyrir þaðan, svo `data`-mappan helst við hlið forritsins og stillingarnar þínar haldast.

### Færanleg útgáfa
`.tar.gz`-skráin virkar líka án uppsetningar: afþjappaðu hana hvar sem þú getur skrifað og keyrðu `./YA-MS` úr þeirri möppu.

Fyrir japanskan texta gætir þú þurft Noto CJK-letrið: sjá [Úrræðaleit](Troubleshooting-FAQ-is#linux-japanskur-texti-birtist-sem-kassar).

## Raspberry Pi

Sama aðferð og á Linux: afþjappaðu `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (eða `-32bit` á 32 bita Raspberry Pi OS) og keyrðu `./installa.sh` í afþjöppuðu möppunni.

- Til að sjá hvaða kerfi þú ert með skaltu slá `uname -m` í útstöð: `aarch64` → 64 bita pakkinn, `armv7l` → 32 bita pakkinn.
- Stutt: Raspberry Pi 2 (aðeins 32 bita), 3, 4, 5, 400 og 500, með skjáborðsútgáfu Raspberry Pi OS. **Ekki stutt:** Pi Zero / Zero W og Pi 1 (ARMv6-örgjörvi, .NET keyrir ekki þar); Pi Zero 2 W virkar með 64 bita pakkanum en 512 MB vinnsluminni er naumt.
- Mælt er með Pi 4 eða 5 með a.m.k. 2 GB vinnsluminni; fyrsta ræsing tekur nokkrum sekúndum lengur en á PC-tölvu.

## macOS

1. Veldu rétta skrá: `-mac-apple-silicon.dmg` fyrir M1/M2/M3/M4-örgjörva, `-mac-intel.dmg` fyrir Mac með Intel.
2. Opnaðu `.dmg`-skrána, **hægrismelltu á "Installa YA-MS.command" → Opna** og staðfestu.
3. Skriftan afritar `YA-MS.app` í **`~/YA-MS`** og opnar það.

Einnig má nota `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip`, sem inniheldur aðeins `YA-MS.app`: afþjappaðu hana í möppu að eigin vali (sem þú getur skrifað í); `data`-mappan er búin til við hlið `YA-MS.app`. Í fyrsta skiptið: hægrismelltu → **Opna**.

Forritið er ekki undirritað af Apple, svo macOS biður um staðfestingu í fyrsta skiptið; sjá [Úrræðaleit](Troubleshooting-FAQ-is#macos-ekki-hægt-að-opna-því-hann-er-frá-óþekktum-hönnuði).

## Fyrsta ræsing

- **Kort af Evrópu** (strandlínur og landamæri frá Natural Earth) er sótt sjálfkrafa í `data/mappa` í fyrsta skiptið: nettenging þarf einu sinni.
- **Ratsjárgögnin** (Collm, Sodankylä) eru sótt strax og síðan athuguð á 5 mínútna fresti.
- Viðmótið ræsist á tungumáli kerfisins ef það er eitt af þeim 28 sem í boði eru, annars á ítölsku; breyttu því efst til hægri (sjá [Stillingar](Settings-and-Data-Folder-is#tungumál)).

## Uppfærsla

Settu nýju útgáfuna upp **yfir þá gömlu** (sama uppsetningarforrit, sama mappa). Stillingar (`config.ini`), flæðisskjalasöfnin og kortið verða áfram í `data`. Þýðingarskrár í `data/lingue` eru endurnýjaðar þegar nýju skrárnar eru nýrri.

## Smíði úr frumkóða (aðeins fyrir forritara)

Uppsetningarforritin eru búin til af GitHub Actions (`.github/workflows/build.yml`) við hverja uppfærslu greinarinnar `release` (útgáfan er tekin úr skránni `VERSION`), sem býr einnig til útgáfuna `vX.Y.Z`. Staðbundið:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # eða linux-x64, linux-arm64, linux-arm, osx-arm64
```

Skjölin eru endurgerð með `tools/build_spiegazione.py data` og `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Næst: [Fyrstu skrefin](Getting-Started-is).
