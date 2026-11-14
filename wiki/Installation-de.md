[English](Installation) · [Italiano](Installation-it) · **Deutsch** · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Installation

Alle Pakete findest du auf der Seite **[Releases](https://github.com/ic8tem/YA-MS/releases)** (in den Dateinamen unten steht `x.y.z` für die Version, z. B. `1.2.0`). Es muss nichts kompiliert und nichts zusätzlich installiert werden: Jedes Paket enthält die .NET-8-Laufzeit.

| System | Datei | Installiert nach |
|---|---|---|
| Windows (64 Bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (Installationsprogramm) | `C:\YA-MS` |
| Windows (64 Bit), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | jeden Ordner, in dem du schreiben darfst |
| Windows (32 Bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` oder `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows auf ARM (64 Bit, PCs mit Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` oder `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 Bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| Linux (64 Bit), jede Distribution | `YA-MS-x.y.z-linux-x64.tar.gz` (portabel oder mit `./installa.sh`) | `~/YA-MS` oder jeder Ordner |
| Linux (64 Bit): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` oder jeder Ordner |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 Bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 Bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian-Paket | `ya-ms_x.y.z_arm64.deb` (64 Bit) oder `ya-ms_x.y.z_armhf.deb` (32 Bit) | `~/YA-MS` (beim ersten Start dorthin kopiert) |
| Linux ARM 64 Bit, jede Distribution (z. B. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (portabel oder mit `./installa.sh`) | `~/YA-MS` oder jeder Ordner |
| Linux armv7l (ARM 32 Bit), jede Distribution | `YA-MS-x.y.z-linux-armv7l.tar.gz` (portabel oder mit `./installa.sh`) | `~/YA-MS` oder jeder Ordner |
| macOS, Apple Silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, nur die Anwendung | `YA-MS-x.y.z-mac-apple-silicon-app.zip` oder `...-mac-intel-app.zip` | der Ordner, in den du `YA-MS.app` entpackst |

**Das Programm und sein Ordner `data` bleiben immer zusammen** im Ordner YA-MS: Dort liegen alle Daten und Einstellungen (kein AppData, keine Systemordner). Siehe [Einstellungen und Datenordner](Settings-and-Data-Folder-de).

## Windows

### Installationsprogramm
1. Lade `YA-MS-x.y.z-windows-x64-setup.exe` herunter und starte es.
2. Wenn **SmartScreen** „Der Computer wurde durch Windows geschützt“ anzeigt: *Weitere Informationen* → *Trotzdem ausführen* (das Programm ist nicht mit einem kommerziellen Zertifikat signiert).
3. YA-MS wird nach **`C:\YA-MS`** installiert, **ohne Administratorrechte**, mit einem Symbol im Startmenü und, wenn du es ankreuzt, einem Symbol auf dem Desktop.

### Portabel
Entpacke `YA-MS-x.y.z-windows-x64-portatile.zip` an einen beliebigen Ort (einen Ordner, in dem du schreiben darfst, nicht *Program Files*) und starte `YA-MS.exe`. Du kannst den ganzen Ordner auf einen USB-Stick oder einen anderen Computer kopieren.

## Linux

1. Entpacke `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Führe im entpackten Ordner aus:
   ```sh
   ./installa.sh
   ```
3. Das Skript kopiert YA-MS nach **`~/YA-MS`** (kein root nötig) und fügt **YA-MS** dem Anwendungsmenü hinzu (Kategorie *HamRadio*). Du kannst es auch mit `~/YA-MS/YA-MS` starten.

### Debian-Paket (.deb)
Unter Debian, Ubuntu, Mint und Raspberry Pi OS kannst du stattdessen `ya-ms_x.y.z_amd64.deb` installieren (`_arm64.deb` / `_armhf.deb` auf dem Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Das Paket legt das Programm in `/opt/ya-ms` ab und fügt **YA-MS** dem Menü hinzu. Beim ersten Start (und nach jeder neuen Version) kopiert es sich nach **`~/YA-MS`** und läuft von dort, sodass der Ordner `data` neben dem Programm bleibt und deine Einstellungen erhalten bleiben.

### Portabel
Das `.tar.gz` funktioniert auch ohne Installation: Entpacke es an einen beliebigen Ort, an dem du schreiben darfst, und starte `./YA-MS` in diesem Ordner.

Für japanischen Text brauchst du eventuell die Noto-CJK-Schriften: siehe [Fehlerbehebung](Troubleshooting-FAQ-de#linux-japanischer-text-zeigt-kästchen).

## Raspberry Pi

Wie unter Linux: `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (bzw. `-32bit` unter Raspberry Pi OS 32 Bit) entpacken und im entpackten Ordner `./installa.sh` starten.

- Welches System du hast, zeigt `uname -m` im Terminal: `aarch64` → 64-Bit-Paket, `armv7l` → 32-Bit-Paket.
- Unterstützt: Raspberry Pi 2 (nur 32 Bit), 3, 4, 5, 400 und 500 mit der Desktop-Version von Raspberry Pi OS. **Nicht unterstützt:** Pi Zero / Zero W und Pi 1 (ARMv6-Prozessor, .NET läuft dort nicht); der Pi Zero 2 W läuft mit dem 64-Bit-Paket, aber 512 MB RAM sind knapp.
- Empfohlen wird ein Pi 4 oder 5 mit mindestens 2 GB RAM; der erste Start dauert ein paar Sekunden länger als auf einem PC.

## macOS

1. Wähle die richtige Datei: `-mac-apple-silicon.dmg` für Prozessoren M1/M2/M3/M4, `-mac-intel.dmg` für Intel-Macs.
2. Öffne die `.dmg`, **Rechtsklick auf „Installa YA-MS.command“ → Öffnen** und bestätige.
3. Das Skript kopiert `YA-MS.app` nach **`~/YA-MS`** und öffnet es.

Alternativ enthält `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` nur `YA-MS.app`: Entpacke es in einen Ordner deiner Wahl (in dem du schreiben darfst); der Ordner `data` wird neben `YA-MS.app` angelegt. Beim ersten Mal: Rechtsklick → **Öffnen**.

Das Programm ist nicht von Apple signiert, deshalb fragt macOS beim ersten Mal nach einer Bestätigung; siehe [Fehlerbehebung](Troubleshooting-FAQ-de#macos-programm-kann-nicht-geöffnet-werden-nicht-verifizierter-entwickler).

## Erster Start

- Die **Europakarte** (Küsten und Grenzen von Natural Earth) wird beim ersten Start automatisch nach `data/mappa` geladen: Einmalig ist eine Internetverbindung nötig.
- Die **Radardaten** (Collm, Sodankylä) werden sofort geladen und danach alle 5 Minuten geprüft.
- Die Oberfläche startet in deiner Systemsprache, wenn sie eine der 36 verfügbaren ist, sonst auf Italienisch; ändern kannst du sie oben rechts (siehe [Einstellungen](Settings-and-Data-Folder-de#sprache)).

## Aktualisieren

Installiere die neue Version **über die alte** (gleiches Installationsprogramm, gleicher Ordner). Die Einstellungen (`config.ini`), die Flussarchive und die Karte bleiben in `data`. Die Übersetzungsdateien in `data/lingue` werden ersetzt, wenn die neuen aktueller sind.

**Ab 1.8.0 aktualisiert sich YA-MS selbst.** Beim Start prüft es einmal am Tag auf GitHub, ob es eine neue Version gibt, und bietet sie an; die Schaltfläche **Aktualisierungen** in der unteren Leiste prüft von Hand. *Jetzt aktualisieren* lädt das portable Paket für dein System herunter, ersetzt die Programmdateien, behält den Ordner `data` (geänderte Programmdateien werden vorher nach `data/backup/v<alte Version>` kopiert) und startet neu; der Programmordner muss beschreibbar sein. Fehlen beim Start Programmdateien (in `data` oder `doc`), listet ein Fenster sie auf und bietet an, sie erneut von GitHub herunterzuladen. Um nicht mehr nach neuen Versionen zu suchen, setze `controlla_aggiornamenti=0` in `config.ini`.

Ab Version 1.8.6 erfolgen Updates automatisch und still: beim Start und dann alle 30 Minuten prüft YA-MS GitHub und lädt eine neue Version, falls vorhanden, herunter, installiert sie und startet sich selbst neu, ohne etwas zu fragen (nur die Statusleiste meldet es). Auch fehlende Dateien werden ohne Rückfrage neu geladen. Das unten beschriebene Fenster erscheint nur beim Drücken von "Aktualisierungen" oder wenn du aggiornamenti_automatici=0 in die Datei data/config.ini schreibst.

## Aus dem Quellcode bauen (nur für Entwickler)

Die Installationspakete werden von GitHub Actions (`.github/workflows/build.yml`) bei jeder Aktualisierung des Zweigs `release` erzeugt (Version aus der Datei `VERSION`), wobei auch das Release `vX.Y.Z` angelegt wird. Lokal:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Die Dokumente (alle Sprachen) werden mit `tools/build_documenti.sh` neu erzeugt.

Weiter: [Erste Schritte](Getting-Started-de).
