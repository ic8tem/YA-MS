[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · **Magyar** · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Telepítés

Minden csomag a **[Releases](https://github.com/ic8tem/YA-MS/releases)** oldalon található (az alábbi fájlnevekben az `x.y.z` a változatszám, pl. `1.2.0`). Semmit nem kell lefordítani és semmi mást nem kell telepíteni: minden csomag tartalmazza a .NET 8 futtatókörnyezetet.

| Rendszer | Fájl | Telepítés helye |
|---|---|---|
| Windows (64 bites) | `YA-MS-x.y.z-windows-x64-setup.exe` (telepítő) | `C:\YA-MS` |
| Windows (64 bites), hordozható | `YA-MS-x.y.z-windows-x64-portatile.zip` | bármely mappa, amelybe írási joga van |
| Windows (32 bites, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` vagy `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows ARM-on (64 bites, Snapdragon processzoros PC-k) | `YA-MS-x.y.z-windows-arm64-setup.exe` vagy `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 bites): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (az első indításkor oda másolódik) |
| Linux (64 bites), bármely disztribúció | `YA-MS-x.y.z-linux-x64.tar.gz` (hordozhatóként vagy a `./installa.sh` szkripttel) | `~/YA-MS` vagy bármely mappa |
| Linux (64 bites): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (az első indításkor oda másolódik) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (az első indításkor oda másolódik) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (az első indításkor oda másolódik) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (az első indításkor oda másolódik) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` vagy bármely mappa |
| Raspberry Pi 3/4/5, 400/500 (64 bites Raspberry Pi OS) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (32 bites Raspberry Pi OS) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian-csomag | `ya-ms_x.y.z_arm64.deb` (64 bites) vagy `ya-ms_x.y.z_armhf.deb` (32 bites) | `~/YA-MS` (az első indításkor oda másolódik) |
| Linux ARM 64 bites, bármely disztribúció (pl. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (hordozhatóként vagy a `./installa.sh` szkripttel) | `~/YA-MS` vagy bármely mappa |
| Linux armv7l (ARM 32 bites), bármely disztribúció | `YA-MS-x.y.z-linux-armv7l.tar.gz` (hordozhatóként vagy a `./installa.sh` szkripttel) | `~/YA-MS` vagy bármely mappa |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, csak az alkalmazás | `YA-MS-x.y.z-mac-apple-silicon-app.zip` vagy `...-mac-intel-app.zip` | az a mappa, ahová a `YA-MS.app` csomagot kibontja |

**A program és a `data` mappája mindig együtt marad** a YA-MS mappában: minden adat és beállítás ott található (nincs AppData, nincsenek rendszermappák). Lásd: [Beállítások és adatmappa](Settings-and-Data-Folder-hu).

## Windows

### Telepítő
1. Töltse le a `YA-MS-x.y.z-windows-x64-setup.exe` fájlt, és futtassa.
2. Ha a **SmartScreen** azt írja, hogy „A Windows megvédte a számítógépet”: *További információ* → *Futtatás mindenképp* (a program nincs kereskedelmi tanúsítvánnyal aláírva).
3. A YA-MS a **`C:\YA-MS`** mappába települ, **rendszergazdai jogok nélkül**, ikonnal a Start menüben, és ha bejelöli, az asztalon is.

### Hordozható változat
Bontsa ki a `YA-MS-x.y.z-windows-x64-portatile.zip` fájlt tetszőleges helyre (olyan mappába, amelybe írhat, ne a *Program Files* alá), és indítsa el a `YA-MS.exe` fájlt. A teljes mappát átmásolhatja pendrive-ra vagy másik számítógépre.

## Linux

1. Bontsa ki a `YA-MS-x.y.z-linux-x64.tar.gz` fájlt.
2. A kibontott mappában futtassa:
   ```sh
   ./installa.sh
   ```
3. A szkript a YA-MS-t a **`~/YA-MS`** mappába másolja (root jog nem kell), és felveszi a **YA-MS**-t az alkalmazások menüjébe (*HamRadio* kategória). A `~/YA-MS/YA-MS` paranccsal is elindítható.

### Debian-csomag (.deb)
Debian, Ubuntu, Mint és Raspberry Pi OS rendszeren ehelyett a `ya-ms_x.y.z_amd64.deb` csomagot is telepítheti (Raspberry Pi-n `_arm64.deb` / `_armhf.deb`):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
A csomag a programot a `/opt/ya-ms` mappába teszi, és felveszi a **YA-MS**-t a menübe. Az első indításkor (és minden új változat után) átmásolja magát a **`~/YA-MS`** mappába, és onnan fut, így a `data` mappa a program mellett marad, a beállítások pedig megmaradnak.

### Hordozható változat
A `.tar.gz` telepítés nélkül is működik: bontsa ki bárhová, ahol írási joga van, és abból a mappából futtassa a `./YA-MS` parancsot.

A japán szöveghez szükség lehet a Noto CJK betűtípusokra: lásd: [Hibaelhárítás](Troubleshooting-FAQ-hu#linux-a-japán-szöveg-helyén-négyzetek-jelennek-meg).

## Raspberry Pi

Ugyanaz az eljárás, mint Linuxon: bontsa ki a `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` fájlt (32 bites Raspberry Pi OS esetén a `-32bit` változatot), és a kibontott mappában futtassa a `./installa.sh` szkriptet.

- Hogy megtudja, milyen rendszere van, írja be egy terminálba: `uname -m`: `aarch64` → 64 bites csomag, `armv7l` → 32 bites csomag.
- Támogatott: Raspberry Pi 2 (csak 32 bit), 3, 4, 5, 400 és 500, a Raspberry Pi OS asztali változatával. **Nem támogatott:** Pi Zero / Zero W és Pi 1 (ARMv6 processzor, ezen a .NET nem fut); a Pi Zero 2 W működik a 64 bites csomaggal, de az 512 MB RAM szűkös.
- Legalább 2 GB RAM-mal rendelkező Pi 4 vagy 5 ajánlott; az első indítás néhány másodperccel tovább tart, mint PC-n.

## macOS

1. Válassza ki a megfelelő fájlt: `-mac-apple-silicon.dmg` M1/M2/M3/M4 processzorhoz, `-mac-intel.dmg` Intel-alapú Machez.
2. Nyissa meg a `.dmg` fájlt, **kattintson jobb gombbal az „Installa YA-MS.command” elemre → Megnyitás**, majd erősítse meg.
3. A szkript a `YA-MS.app` alkalmazást a **`~/YA-MS`** mappába másolja, és megnyitja.

Másik lehetőség: a `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` csak a `YA-MS.app` alkalmazást tartalmazza: bontsa ki egy tetszőleges mappába (amelybe írhat); a `data` mappa a `YA-MS.app` mellett jön létre. Első alkalommal: jobb gomb → **Megnyitás**.

A programot nem az Apple írta alá, ezért első alkalommal a macOS megerősítést kér; lásd: [Hibaelhárítás](Troubleshooting-FAQ-hu#macos-nem-nyitható-meg-mert-azonosítatlan-fejlesztőtől-származik).

## Első indítás

- Az **Európa-térkép** (Natural Earth partvonalak és határok) első alkalommal automatikusan letöltődik a `data/mappa` mappába: ehhez egyszer internetkapcsolat szükséges.
- A **radaradatok** (Collm, Sodankylä) azonnal letöltődnek, majd ötpercenként ellenőrzésre kerülnek.
- A felület a rendszer nyelvén indul, ha az a 36 elérhető nyelv egyike, egyébként olaszul; a jobb felső sarokban módosítható (lásd: [Beállítások](Settings-and-Data-Folder-hu#nyelv)).

## Frissítés

Telepítse az új változatot **a régire** (ugyanaz a telepítő, ugyanaz a mappa). A beállítások (`config.ini`), a fluxusarchívumok és a térkép a `data` mappában maradnak. A `data/lingue` mappában lévő fordítási fájlok lecserélődnek, ha az újak frissebbek.

**Az 1.8.0-tól a YA-MS önmagát frissíti.** Indításkor naponta egyszer megnézi a GitHubon, van-e új verzió, és felajánlja; az alsó sáv **Frissítések** gombja kézzel ellenőriz. A *Frissítés most* letölti a rendszeredhez való hordozható csomagot, lecseréli a program fájljait, megtartja a `data` mappát (a megváltozó programfájlokat előbb a `data/backup/v<régi verzió>` mappába másolja) és újraindul; a program mappájának írhatónak kell lennie. Ha indításkor programfájlok hiányoznak (a `data` vagy `doc` mappából), egy ablak felsorolja őket és felajánlja, hogy újra letölti a GitHubról. Ha nem akarsz új verziókat keresni, állítsd be a `controlla_aggiornamenti=0` értéket a `config.ini`-ben.

Az 1.8.6-os verziótól a frissítések automatikusak és csendesek: indításkor, majd 6 óránként a YA-MS megnézi a GitHubot, és ha új verzió van, letölti, telepíti és magától újraindul, semmit sem kérdezve (csak az állapotsor jelzi). A hiányzó fájlokat is kérdés nélkül újratölti. Az alább leírt ablak csak a "Frissítések" gomb megnyomásakor jelenik meg, vagy ha a data/config.ini fájlba beírod: aggiornamenti_automatici=0.

## Fordítás forráskódból (csak fejlesztőknek)

A telepítőket a GitHub Actions (`.github/workflows/build.yml`) készíti el a `release` ág minden frissítésekor (a változatszám a `VERSION` fájlból származik), és ez hozza létre a `vX.Y.Z` kiadást is. Helyben:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

A dokumentumok (minden nyelven) újragenerálása: `tools/build_documenti.sh`.

Következő: [Első lépések](Getting-Started-hu).
