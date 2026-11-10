[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · **Čeština** · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalace

Všechny balíčky jsou na stránce **[Releases](https://github.com/ic8tem/YA-MS/releases)** (v názvech souborů níže je `x.y.z` verze, např. `1.2.0`). Nic se nemusí kompilovat ani doinstalovat: každý balíček obsahuje runtime .NET 8.

| Systém | Soubor | Instaluje se do |
|---|---|---|
| Windows (64bitové) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalátor) | `C:\YA-MS` |
| Windows (64bitové), přenosná verze | `YA-MS-x.y.z-windows-x64-portatile.zip` | libovolná složka, do které můžete zapisovat |
| Windows (32bitové, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` nebo `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64bitový): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (zkopíruje se tam při prvním spuštění) |
| Linux (64bitový), libovolná distribuce | `YA-MS-x.y.z-linux-x64.tar.gz` (přenosně nebo pomocí `./installa.sh`) | `~/YA-MS` nebo libovolná složka |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64bitový) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32bitový) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, balíček Debian | `ya-ms_x.y.z_arm64.deb` (64bitový) nebo `ya-ms_x.y.z_armhf.deb` (32bitový) | `~/YA-MS` (zkopíruje se tam při prvním spuštění) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, jen aplikace | `YA-MS-x.y.z-mac-apple-silicon-app.zip` nebo `...-mac-intel-app.zip` | složka, do které rozbalíte `YA-MS.app` |

**Program a jeho složka `data` zůstávají vždy spolu** ve složce YA-MS: jsou v ní všechna data a nastavení (žádné AppData, žádné systémové složky). Viz [Nastavení a datová složka](Settings-and-Data-Folder-cs).

## Windows

### Instalátor
1. Stáhněte `YA-MS-x.y.z-windows-x64-setup.exe` a spusťte ho.
2. Pokud **SmartScreen** zobrazí „Systém Windows ochránil váš počítač“: *Další informace* → *Přesto spustit* (program není podepsán komerčním certifikátem).
3. YA-MS se nainstaluje do **`C:\YA-MS`**, **bez práv správce**, s ikonou v nabídce Start a, pokud ji zaškrtnete, s ikonou na ploše.

### Přenosná verze
Rozbalte `YA-MS-x.y.z-windows-x64-portatile.zip` kamkoli chcete (do složky, do které můžete zapisovat, ne do *Program Files*) a spusťte `YA-MS.exe`. Celou složku můžete zkopírovat na USB disk nebo na jiný počítač.

## Linux

1. Rozbalte `YA-MS-x.y.z-linux-x64.tar.gz`.
2. V rozbalené složce spusťte:
   ```sh
   ./installa.sh
   ```
3. Skript zkopíruje YA-MS do **`~/YA-MS`** (root není potřeba) a přidá **YA-MS** do nabídky aplikací (kategorie *HamRadio*). Spustit ho můžete také pomocí `~/YA-MS/YA-MS`.

### Balíček Debian (.deb)
V systémech Debian, Ubuntu, Mint a Raspberry Pi OS můžete místo toho nainstalovat `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` na Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Balíček umístí program do `/opt/ya-ms` a přidá **YA-MS** do nabídky. Při prvním spuštění (a po každé nové verzi) se zkopíruje do **`~/YA-MS`** a spouští se odtud, takže složka `data` zůstává vedle programu a vaše nastavení se zachovají.

### Přenosná verze
Soubor `.tar.gz` funguje i bez instalace: rozbalte ho kamkoli, kam můžete zapisovat, a v této složce spusťte `./YA-MS`.

Pro japonský text možná budete potřebovat písma Noto CJK: viz [Řešení problémů](Troubleshooting-FAQ-cs#linux-japonský-text-se-zobrazuje-jako-čtverečky).

## Raspberry Pi

Stejný postup jako u Linuxu: rozbalte `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (nebo `-32bit` na 32bitovém Raspberry Pi OS) a v rozbalené složce spusťte `./installa.sh`.

- Jaký systém máte, zjistíte příkazem `uname -m` v terminálu: `aarch64` → 64bitový balíček, `armv7l` → 32bitový balíček.
- Podporováno: Raspberry Pi 2 (jen 32bitově), 3, 4, 5, 400 a 500 s desktopovou verzí Raspberry Pi OS. **Nepodporováno:** Pi Zero / Zero W a Pi 1 (procesor ARMv6, .NET na něm neběží); Pi Zero 2 W funguje s 64bitovým balíčkem, ale 512 MB RAM je na hraně.
- Doporučuje se Pi 4 nebo 5 s alespoň 2 GB RAM; první spuštění trvá o několik sekund déle než na PC.

## macOS

1. Zvolte správný soubor: `-mac-apple-silicon.dmg` pro procesory M1/M2/M3/M4, `-mac-intel.dmg` pro Macy s procesorem Intel.
2. Otevřete `.dmg`, **klikněte pravým tlačítkem na „Installa YA-MS.command“ → Otevřít** a potvrďte.
3. Skript zkopíruje `YA-MS.app` do **`~/YA-MS`** a otevře ji.

Případně `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` obsahuje jen `YA-MS.app`: rozbalte ji do složky podle svého výběru (do které můžete zapisovat); složka `data` se vytvoří vedle `YA-MS.app`. Poprvé klikněte pravým tlačítkem → **Otevřít**.

Program není podepsán společností Apple, takže macOS poprvé požádá o potvrzení; viz [Řešení problémů](Troubleshooting-FAQ-cs#macos-nelze-otevřít-protože-pochází-od-neidentifikovaného-vývojáře).

## První spuštění

- **Mapa Evropy** (pobřeží a hranice z Natural Earth) se poprvé automaticky stáhne do `data/mappa`: jednou je potřeba připojení k internetu.
- **Radarová data** (Collm, Sodankylä) se stáhnou ihned a pak se kontrolují každých 5 minut.
- Rozhraní se spustí v jazyce systému, pokud je mezi 36 dostupnými, jinak v italštině; změníte ho vpravo nahoře (viz [Nastavení](Settings-and-Data-Folder-cs#jazyk)).

## Aktualizace

Novou verzi nainstalujte **přes starou** (stejný instalátor, stejná složka). Nastavení (`config.ini`), archivy toku a mapa zůstávají v `data`. Soubory překladů v `data/lingue` se nahradí, pokud jsou nové novější.

## Sestavení ze zdrojového kódu (jen pro vývojáře)

Instalátory vytváří GitHub Actions (`.github/workflows/build.yml`) při každé aktualizaci větve `release` (verze se bere ze souboru `VERSION`), které také vytvoří vydání `vX.Y.Z`. Lokálně:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenty (ve všech jazycích) se znovu vygenerují pomocí `tools/build_documenti.sh`.

Dále: [První kroky](Getting-Started-cs).
