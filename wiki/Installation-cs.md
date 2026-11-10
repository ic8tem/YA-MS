LANGBAR

# Instalace

Všechny balíčky jsou na stránce **[Releases](https://github.com/ic8tem/YA-MS/releases)** (v názvech souborů níže je `x.y.z` verze, např. `1.2.0`). Nic není třeba kompilovat ani nic dalšího instalovat: každý balíček obsahuje běhové prostředí .NET 8.

| Systém | Soubor | Instaluje se do |
|---|---|---|
| Windows (64bitové) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalátor) | `C:\YA-MS` |
| Windows (64bitové), přenosná verze | `YA-MS-x.y.z-windows-x64-portatile.zip` | libovolná složka, do které můžete zapisovat |
| Windows (32bitové, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` nebo `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64bitový) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64bitový) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32bitový) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Program a jeho složka `data` zůstávají vždy pohromadě** ve složce YA-MS: jsou v ní všechna data a nastavení (žádné AppData, žádné systémové složky). Viz [Nastavení a datová složka](Settings-and-Data-Folder-cs).

## Windows

### Instalátor
1. Stáhněte `YA-MS-x.y.z-windows-x64-setup.exe` a spusťte ho.
2. Pokud **SmartScreen** zobrazí „Systém Windows ochránil váš počítač“: *Další informace* → *Přesto spustit* (program není podepsán komerčním certifikátem).
3. YA-MS se nainstaluje do **`C:\YA-MS`**, **bez práv správce**, s ikonou v nabídce Start a, pokud to zaškrtnete, s ikonou na ploše.

### Přenosná verze
Rozbalte `YA-MS-x.y.z-windows-x64-portatile.zip` kamkoli chcete (do složky, do které můžete zapisovat, ne do *Program Files*) a spusťte `YA-MS.exe`. Celou složku můžete zkopírovat na USB flash disk nebo na jiný počítač.

## Linux

1. Rozbalte `YA-MS-x.y.z-linux-x64.tar.gz`.
2. V rozbalené složce spusťte:
   ```sh
   ./installa.sh
   ```
3. Skript zkopíruje YA-MS do **`~/YA-MS`** (root není potřeba) a přidá **YA-MS** do nabídky aplikací (kategorie *HamRadio*). Program lze spustit také příkazem `~/YA-MS/YA-MS`.

Pro japonský text mohou být potřeba písma Noto CJK: viz [Řešení problémů](Troubleshooting-FAQ-cs#linux-japonský-text-se-zobrazuje-jako-čtverečky).

## Raspberry Pi

Stejný postup jako u Linuxu: rozbalte `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (nebo `-32bit` na 32bitovém Raspberry Pi OS) a v rozbalené složce spusťte `./installa.sh`.

- Jaký systém máte, zjistíte příkazem `uname -m` v terminálu: `aarch64` → 64bitový balíček, `armv7l` → 32bitový balíček.
- Podporováno: Raspberry Pi 2 (jen 32bitový), 3, 4, 5, 400 a 500, s desktopovou verzí Raspberry Pi OS. **Nepodporováno:** Pi Zero / Zero W a Pi 1 (procesor ARMv6, .NET na něm neběží); Pi Zero 2 W funguje s 64bitovým balíčkem, ale 512 MB RAM je málo.
- Doporučuje se Pi 4 nebo 5 s alespoň 2 GB RAM; první spuštění trvá o několik sekund déle než na PC.

## macOS

1. Zvolte správný soubor: `-mac-apple-silicon.dmg` pro procesory M1/M2/M3/M4, `-mac-intel.dmg` pro Macy s procesorem Intel.
2. Otevřete `.dmg`, **klikněte pravým tlačítkem na „Installa YA-MS.command“ → Otevřít** a potvrďte.
3. Skript zkopíruje `YA-MS.app` do **`~/YA-MS`** a otevře ho.

Program není podepsán společností Apple, takže macOS si poprvé vyžádá potvrzení; viz [Řešení problémů](Troubleshooting-FAQ-cs#macos-program-nelze-otevřít-protože-je-od-neidentifikovaného-vývojáře).

## První spuštění

- **Mapa Evropy** (pobřeží a hranice z Natural Earth) se při prvním spuštění automaticky stáhne do `data/mappa`: připojení k internetu je potřeba jednou.
- **Data radarů** (Collm, Sodankylä) se stáhnou ihned a poté se kontrolují každých 5 minut.
- Rozhraní se spustí v jazyce vašeho systému, pokud je jedním z 36 dostupných, jinak v italštině; změníte ho vpravo nahoře (viz [Nastavení](Settings-and-Data-Folder-cs#jazyk)).

## Aktualizace

Novou verzi nainstalujte **přes starou** (stejný instalátor, stejná složka). Nastavení (`config.ini`), archivy toku a mapa zůstávají v `data`. Soubory překladů v `data/lingue` se nahradí, pokud jsou nové novější.

## Sestavení ze zdrojového kódu (jen pro vývojáře)

Instalátory vytváří GitHub Actions (`.github/workflows/build.yml`) při každé aktualizaci větve `release` (verze se bere ze souboru `VERSION`), které zároveň vytvoří vydání `vX.Y.Z`. Lokálně:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumenty se znovu generují příkazy `tools/build_spiegazione.py data` a `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Dále: [Začínáme](Getting-Started-cs).
