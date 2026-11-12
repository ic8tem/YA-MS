[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · **Español** · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalación

Todos los paquetes están en la página **[Releases](https://github.com/ic8tem/YA-MS/releases)** (en los nombres de archivo de abajo `x.y.z` es la versión, p. ej. `1.2.0`). No hay que compilar nada ni instalar nada más: cada paquete contiene el runtime de .NET 8.

| Sistema | Archivo | Se instala en |
|---|---|---|
| Windows (64 bits) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalador) | `C:\YA-MS` |
| Windows (64 bits), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | cualquier carpeta en la que puedas escribir |
| Windows (32 bits, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` o `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows en ARM (64 bits, PC con Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` o `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 bits): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copiado allí en el primer arranque) |
| Linux (64 bits), cualquier distribución | `YA-MS-x.y.z-linux-x64.tar.gz` (portable o con `./installa.sh`) | `~/YA-MS` o cualquier carpeta |
| Linux (64 bits): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (copiado allí en el primer arranque) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (copiado allí en el primer arranque) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (copiado allí en el primer arranque) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (copiado allí en el primer arranque) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` o cualquier carpeta |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bits) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bits) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, paquete Debian | `ya-ms_x.y.z_arm64.deb` (64 bits) o `ya-ms_x.y.z_armhf.deb` (32 bits) | `~/YA-MS` (copiado allí en el primer arranque) |
| Linux ARM 64 bits, cualquier distribución (p. ej. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (portable o con `./installa.sh`) | `~/YA-MS` o cualquier carpeta |
| Linux armv7l (ARM 32 bits), cualquier distribución | `YA-MS-x.y.z-linux-armv7l.tar.gz` (portable o con `./installa.sh`) | `~/YA-MS` o cualquier carpeta |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, solo la aplicación | `YA-MS-x.y.z-mac-apple-silicon-app.zip` o `...-mac-intel-app.zip` | la carpeta donde descomprimas `YA-MS.app` |

**El programa y su carpeta `data` siempre van juntos** en la carpeta YA-MS: todos los datos y ajustes están ahí (nada de AppData ni carpetas del sistema). Ver [Ajustes y carpeta de datos](Settings-and-Data-Folder-es).

## Windows

### Instalador
1. Descarga `YA-MS-x.y.z-windows-x64-setup.exe` y ejecútalo.
2. Si **SmartScreen** muestra "Windows protegió su PC": *Más información* → *Ejecutar de todas formas* (el programa no está firmado con un certificado comercial).
3. YA-MS se instala en **`C:\YA-MS`**, **sin derechos de administrador**, con un icono en el menú Inicio y, si lo marcas, un icono en el escritorio.

### Portable
Descomprime `YA-MS-x.y.z-windows-x64-portatile.zip` donde quieras (una carpeta en la que puedas escribir, no *Archivos de programa*) y ejecuta `YA-MS.exe`. Puedes copiar la carpeta entera a una memoria USB o a otro ordenador.

## Linux

1. Descomprime `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Desde la carpeta descomprimida ejecuta:
   ```sh
   ./installa.sh
   ```
3. El script copia YA-MS en **`~/YA-MS`** (no hace falta root) y añade **YA-MS** al menú de aplicaciones (categoría *HamRadio*). También puedes iniciarlo con `~/YA-MS/YA-MS`.

### Paquete Debian (.deb)
En Debian, Ubuntu, Mint y Raspberry Pi OS puedes instalar en su lugar `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` en la Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
El paquete coloca el programa en `/opt/ya-ms` y añade **YA-MS** al menú. En el primer arranque (y después de cada nueva versión) se copia a **`~/YA-MS`** y se ejecuta desde allí, de modo que la carpeta `data` queda junto al programa y se conservan tus ajustes.

### Portable
El `.tar.gz` también funciona sin instalar: descomprímelo en cualquier lugar donde puedas escribir y ejecuta `./YA-MS` desde esa carpeta.

Para el texto japonés pueden hacer falta las fuentes Noto CJK: ver [Problemas](Troubleshooting-FAQ-es#linux-el-texto-japonés-aparece-como-cuadraditos).

## Raspberry Pi

Mismo procedimiento que en Linux: descomprime `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (o `-32bit` en Raspberry Pi OS de 32 bits) y ejecuta `./installa.sh` desde la carpeta descomprimida.

- Para saber qué sistema tienes, escribe `uname -m` en un terminal: `aarch64` → paquete de 64 bits, `armv7l` → paquete de 32 bits.
- Compatibles: Raspberry Pi 2 (solo 32 bits), 3, 4, 5, 400 y 500, con la versión de escritorio de Raspberry Pi OS. **No compatibles:** Pi Zero / Zero W y Pi 1 (procesador ARMv6, .NET no funciona en ellos); la Pi Zero 2 W funciona con el paquete de 64 bits, pero 512 MB de RAM se quedan cortos.
- Se recomienda una Pi 4 o 5 con al menos 2 GB de RAM; el primer arranque tarda unos segundos más que en un PC.

## macOS

1. Elige el archivo adecuado: `-mac-apple-silicon.dmg` para procesadores M1/M2/M3/M4, `-mac-intel.dmg` para Mac Intel.
2. Abre el `.dmg`, **clic derecho en "Installa YA-MS.command" → Abrir** y confirma.
3. El script copia `YA-MS.app` en **`~/YA-MS`** y lo abre.

Como alternativa, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` contiene solo `YA-MS.app`: descomprímelo en una carpeta de tu elección (donde puedas escribir); la carpeta `data` se crea junto a `YA-MS.app`. La primera vez, clic derecho → **Abrir**.

El programa no está firmado por Apple, así que la primera vez macOS pide confirmación; ver [Problemas](Troubleshooting-FAQ-es#macos-no-se-puede-abrir-porque-es-de-un-desarrollador-no-identificado).

## Primer arranque

- El **mapa de Europa** (costas y fronteras de Natural Earth) se descarga automáticamente en `data/mappa` la primera vez: hace falta conexión a internet una sola vez.
- Los **datos de radar** (Collm, Sodankylä) se descargan enseguida y luego se comprueban cada 5 minutos.
- La interfaz arranca en el idioma del sistema si es uno de los 36 disponibles; si no, en italiano; se cambia arriba a la derecha (ver [Ajustes](Settings-and-Data-Folder-es#idioma)).

## Actualización

Instala la nueva versión **encima de la anterior** (mismo instalador, misma carpeta). Los ajustes (`config.ini`), los archivos históricos del flujo y el mapa se quedan en `data`. Los archivos de traducción de `data/lingue` se sustituyen cuando los nuevos son más recientes.

**Desde la 1.8.0, YA-MS se actualiza solo.** Al arrancar, una vez al día, comprueba en GitHub si hay una versión nueva y la propone; el botón **Actualizaciones** de la barra inferior hace la comprobación a mano. *Actualizar ahora* descarga el paquete portátil de tu sistema, sustituye los archivos del programa, conserva la carpeta `data` (los archivos del programa que cambian se copian antes en `data/backup/v<versión anterior>`) y se reinicia; hay que poder escribir en la carpeta del programa. Si al arrancar faltan archivos del programa (en `data` o `doc`), una ventana los enumera y propone descargarlos de nuevo de GitHub. Para no buscar versiones nuevas pon `controlla_aggiornamenti=0` en `config.ini`.

## Compilar desde el código fuente (solo desarrolladores)

Los instaladores los genera GitHub Actions (`.github/workflows/build.yml`) en cada actualización de la rama `release` (versión tomada del archivo `VERSION`), que además crea la release `vX.Y.Z`. En local:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # o linux-x64, linux-arm64, linux-arm, osx-arm64
```

Los documentos (todos los idiomas) se regeneran con `tools/build_documenti.sh`.

Siguiente: [Primeros pasos](Getting-Started-es).
