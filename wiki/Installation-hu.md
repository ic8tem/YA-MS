[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · **Magyar** · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Telepítés

Minden csomag a **[Releases](https://github.com/ic8tem/YA-MS/releases)** oldalon található (az alábbi fájlnevekben az `x.y.z` a változatszám, pl. `1.2.0`). Semmit sem kell lefordítani és semmi mást nem kell telepíteni: minden csomag tartalmazza a .NET 8 futtatókörnyezetet.

| Rendszer | Fájl | Telepítési hely |
|---|---|---|
| Windows (64 bites) | `YA-MS-x.y.z-windows-x64-setup.exe` (telepítő) | `C:\YA-MS` |
| Windows (64 bites), hordozható | `YA-MS-x.y.z-windows-x64-portatile.zip` | bármely mappa, ahová írhat |
| Windows (32 bites, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` vagy `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bites) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bites) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bites) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**A program és a `data` mappája mindig együtt marad** a YA-MS mappában: minden adat és beállítás ott van (nincs AppData, nincsenek rendszermappák). Lásd [Beállítások és adatmappa](Settings-and-Data-Folder-hu).

## Windows

### Telepítő
1. Töltse le a `YA-MS-x.y.z-windows-x64-setup.exe` fájlt, és futtassa.
2. Ha a **SmartScreen** azt írja, hogy „A Windows megvédte a számítógépet”: *További információ* → *Futtatás mindenképp* (a program nincs kereskedelmi tanúsítvánnyal aláírva).
3. A YA-MS a **`C:\YA-MS`** mappába települ, **rendszergazdai jogok nélkül**, Start menü ikonnal és – ha bejelöli – asztali ikonnal.

### Hordozható változat
Csomagolja ki a `YA-MS-x.y.z-windows-x64-portatile.zip` fájlt tetszőleges helyre (olyan mappába, ahová írhat, ne a *Program Files* mappába), és futtassa a `YA-MS.exe` fájlt. A teljes mappát átmásolhatja USB-kulcsra vagy másik számítógépre.

## Linux

1. Csomagolja ki a `YA-MS-x.y.z-linux-x64.tar.gz` fájlt.
2. A kicsomagolt mappából futtassa:
   ```sh
   ./installa.sh
   ```
3. A szkript a YA-MS-t a **`~/YA-MS`** mappába másolja (root jog nem kell), és felveszi a **YA-MS**-t az alkalmazásmenübe (*HamRadio* kategória). A `~/YA-MS/YA-MS` paranccsal is elindíthatja.

A japán szöveghez szükség lehet a Noto CJK betűtípusokra: lásd [Hibaelhárítás](Troubleshooting-FAQ-hu#linux-a-japán-szöveg-helyén-négyzetek-jelennek-meg).

## Raspberry Pi

Ugyanaz az eljárás, mint Linux alatt: csomagolja ki a `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` fájlt (32 bites Raspberry Pi OS esetén a `-32bit` változatot), és a kicsomagolt mappából futtassa a `./installa.sh` parancsot.

- Hogy megtudja, milyen rendszere van, írja be egy terminálba: `uname -m`. `aarch64` → 64 bites csomag, `armv7l` → 32 bites csomag.
- Támogatott: Raspberry Pi 2 (csak 32 bites), 3, 4, 5, 400 és 500, a Raspberry Pi OS asztali változatával. **Nem támogatott:** Pi Zero / Zero W és Pi 1 (ARMv6 processzor, a .NET nem fut rajta); a Pi Zero 2 W működik a 64 bites csomaggal, de az 512 MB RAM szűkös.
- Legalább 2 GB RAM-mal rendelkező Pi 4 vagy 5 ajánlott; az első indítás néhány másodperccel tovább tart, mint PC-n.

## macOS

1. Válassza a megfelelő fájlt: `-mac-apple-silicon.dmg` M1/M2/M3/M4 processzorokhoz, `-mac-intel.dmg` Intel alapú Macekhez.
2. Nyissa meg a `.dmg` fájlt, **kattintson jobb gombbal az „Installa YA-MS.command” elemre → Megnyitás**, és erősítse meg.
3. A szkript a `YA-MS.app` alkalmazást a **`~/YA-MS`** mappába másolja, és megnyitja.

A programot nem írta alá az Apple, ezért az első alkalommal a macOS megerősítést kér; lásd [Hibaelhárítás](Troubleshooting-FAQ-hu#macos-nem-nyitható-meg-mert-azonosítatlan-fejlesztőtől-származik).

## Első indítás

- Az **Európa-térkép** (Natural Earth partvonalak és határok) első alkalommal automatikusan letöltődik a `data/mappa` mappába: egyszer szükség van internetkapcsolatra.
- A **radaradatok** (Collm, Sodankylä) azonnal letöltődnek, majd ötpercenként ellenőrzésre kerülnek.
- A kezelőfelület a rendszer nyelvén indul, ha az a 36 elérhető nyelv egyike, egyébként olaszul; jobb felül módosítható (lásd [Beállítások](Settings-and-Data-Folder-hu#nyelv)).

## Frissítés

Telepítse az új változatot **a régire** (ugyanaz a telepítő, ugyanaz a mappa). A beállítások (`config.ini`), a fluxusarchívumok és a térkép a `data` mappában maradnak. A `data/lingue` mappa fordítási fájljai lecserélődnek, ha az újak frissebbek.

## Fordítás forráskódból (csak fejlesztőknek)

A telepítőket a GitHub Actions (`.github/workflows/build.yml`) készíti a `release` ág minden frissítésekor (a változatszámot a `VERSION` fájlból veszi), és ez hozza létre a `vX.Y.Z` kiadást is. Helyben:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

A dokumentumok újragenerálása: `tools/build_spiegazione.py data` és `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Következő: [Első lépések](Getting-Started-hu).
