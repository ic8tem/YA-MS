[English](Installation) · [Русский](Installation-ru) · **Deutsch** · [日本語](Installation-ja)

# Installation

Alle Pakete findest du auf der Seite **[Releases](https://github.com/ic8tem/YA-MS/releases)** (in den Dateinamen unten steht `x.y.z` für die Version, z. B. `1.2.0`). Es muss nichts kompiliert und nichts zusätzlich installiert werden: Jedes Paket enthält die .NET-8-Laufzeit.

| System | Datei | Installiert nach |
|---|---|---|
| Windows (64 Bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (Installationsprogramm) | `C:\YA-MS` |
| Windows (64 Bit), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | jeden Ordner, in dem du schreiben darfst |
| Linux (64 Bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 Bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 Bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple Silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

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

Das Programm ist nicht von Apple signiert, deshalb fragt macOS beim ersten Mal nach einer Bestätigung; siehe [Fehlerbehebung](Troubleshooting-FAQ-de#macos-programm-kann-nicht-geöffnet-werden-nicht-verifizierter-entwickler).

## Erster Start

- Die **Europakarte** (Küsten und Grenzen von Natural Earth) wird beim ersten Start automatisch nach `data/mappa` geladen: Einmalig ist eine Internetverbindung nötig.
- Die **Radardaten** (Collm, Sodankylä) werden sofort geladen und danach alle 5 Minuten geprüft.
- Die Oberfläche startet in deiner Systemsprache, wenn sie eine der sechs verfügbaren ist, sonst auf Italienisch; ändern kannst du sie oben rechts (siehe [Einstellungen](Settings-and-Data-Folder-de#sprache)).

## Aktualisieren

Installiere die neue Version **über die alte** (gleiches Installationsprogramm, gleicher Ordner). Die Einstellungen (`config.ini`), die Flussarchive und die Karte bleiben in `data`. Die Übersetzungsdateien in `data/lingue` werden ersetzt, wenn die neuen aktueller sind.

## Aus dem Quellcode bauen (nur für Entwickler)

Die Installationspakete werden von GitHub Actions (`.github/workflows/build.yml`) bei jeder Aktualisierung des Zweigs `release` erzeugt (Version aus der Datei `VERSION`), wobei auch das Release `vX.Y.Z` angelegt wird. Lokal:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Die Dokumente werden mit `tools/build_spiegazione.py data` und `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` neu erzeugt.

Weiter: [Erste Schritte](Getting-Started-de).
