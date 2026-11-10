[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · **Deutsch** · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# Fehlerbehebung und FAQ

## Installation und Start

### Windows SmartScreen meldet „Der Computer wurde durch Windows geschützt“
Das Programm ist nicht mit einem kommerziellen Zertifikat signiert. Klicke auf *Weitere Informationen* → *Trotzdem ausführen*. Lade es nur von der Seite [Releases](https://github.com/ic8tem/YA-MS/releases) herunter.

### macOS: Programm kann nicht geöffnet werden (nicht verifizierter Entwickler)
YA-MS ist nicht von Apple signiert, deshalb blockiert **Gatekeeper** es beim ersten Mal. In der `.dmg`: **Rechtsklick auf „Installa YA-MS.command“ → Öffnen** und bestätigen. Das Skript entfernt die Quarantäne-Markierung „aus dem Internet geladen“ von `~/YA-MS/YA-MS.app` und öffnet es. Verweigert macOS weiterhin den Start, öffne *Systemeinstellungen → Datenschutz & Sicherheit* und drücke *Trotzdem öffnen*.

### macOS: Welche .dmg?
`-mac-apple-silicon.dmg` für Prozessoren M1/M2/M3/M4, `-mac-intel.dmg` für Intel-Macs (Apple-Menü → *Über diesen Mac* sagt dir, welcher es ist).

### Linux: YA-MS fehlt im Anwendungsmenü
Führe `./installa.sh` im entpackten Ordner aus (nicht in `~/YA-MS`). Manche Desktops zeigen neue Einträge erst nach Ab- und Anmelden. Du kannst es jederzeit mit `~/YA-MS/YA-MS` starten.

### Die Europakarte fehlt
*Europakarte nicht verfügbar (beim ersten Start wird Internet benötigt).* Die Karte von Natural Earth wird beim ersten Start nach `data/mappa` geladen. Verbinde dich mit dem Internet und starte YA-MS neu.

## Anzeige

### Linux: Japanischer Text zeigt Kästchen
Deinem System fehlen CJK-Schriften (Chinesisch, Japanisch, Koreanisch). Installiere die Schriften **Noto CJK** und starte YA-MS neu. Dasselbe passiert bei Arabisch, Hebräisch, Urdu, Hindi und Bengalisch: Unter Debian, Ubuntu und Raspberry Pi OS installiere zusätzlich `fonts-noto-core`.

| Distribution | Befehl |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Der Text ist zu klein oder die Diagramme haben keinen Platz
Verwende den Schieberegler **Schrift** (100–300 %) und klappe die Zeilen mit **Bedienung** ein. Siehe [Einstellungen](Settings-and-Data-Folder-de#schrift-und-bedienung).

### Der Bildschirm ist nachts zu hell
Wähle **Nacht** oder **Schwarz** in der Liste **Farbschema**.

## Internet und Radardaten

### Meldung „Keine Internetverbindung“
YA-MS zeigt sie **einmal**, wenn keine Quelle erreichbar ist; die Statusleiste wird rot. Das Programm arbeitet mit den **zuletzt gespeicherten Daten** weiter und versucht es selbstständig alle 5 Minuten erneut; *Verbindung wiederhergestellt.* erscheint, sobald das Netz wieder da ist. Du musst nichts tun.

### Orange Warnung im Radarfluss: „Vertikale Flussskala nicht lesbar …“
Das Collm-Radar ändert seine vertikale Skala jeden Tag, und YA-MS liest sie aus den Beschriftungen des Diagramms. Lässt sich eine Beschriftung nicht lesen, verwendet das Programm die kalibrierte Skala 0–1200 Meteore/h und warnt, dass die **Werte zu prüfen sind**. Meist wird das nächste stündliche Diagramm korrekt gelesen. Siehst du über viele Stunden *Diagrammformat geändert* oder *Flussachsen nicht an der erwarteten Position gefunden*, hat das Radar das Format seines Diagramms geändert: Bitte [melde es](Contributing-and-Contacts-de).

### „Die Skala des Höhendiagramms hat sich geändert“
Die Höhenstatistik (Modalwert, Mittel, Median) bleibt gültig; nur die absoluten Zählwerte des Höhenhistogramms nicht.

### „Radarfluss: keine Daten“
Drücke **Jetzt laden** im Reiter [Radarfluss](Radar-Flux-de) und prüfe, ob `data/fonti_radar.csv` für Collm `attivo=1` enthält.

### RMOB: Warum ist der automatische Abruf ausgeschaltet?
RMOB bittet darum, dass **automatische Programme seine Dateien nicht abrufen**. Aktiviere *automatischer Abruf alle 5 Minuten* erst, wenn RMOB dir die Erlaubnis gegeben hat. Verwende bis dahin **RMOB jetzt laden** oder **RMOB-Datei von Festplatte laden...**. Siehe [Experimentelle Vorhersage](Experimental-Forecasts-de#rmob-und-automatische-programme).

### RMOB: „Dateiformat nicht erkannt.“ oder wenige Stunden gelesen
Verwende die monatliche Textdatei des Beobachters (`NAME_MMYYYYrmob.TXT`) oder eine Tabelle des Bulletins mit nur einem Beobachter. Die Anpassung des Exponenten braucht mindestens 3 gemeinsame Stunden mit den Collm-Daten (gestern und heute).

## Berechnungen

### „Locator der Station ungültig“ / „Locator der Gegenstation ungültig“
Locatoren müssen 4, 6 oder 8 Zeichen haben (z. B. `JN70`, `JN70CN`, `JN70CN12`).

### „Keine gemeinsame Zone der E-Schicht“
Die Strecke ist länger als die doppelte Reichweite in Spurhöhe (etwa 2 × 1062 km mit der Keule auf 0° und Spuren in 89,5 km): Ein einzelner Meteorscatter-Sprung kann sie nicht überbrücken. Eine höhere **Keulenelev.** verkürzt die Reichweite noch weiter.

### Hot A / Hot B sind grau
Sie liegen bereits **in deiner Antennenkeule**, wenn die Antenne auf die Gegenstation zeigt: Drehen ist nicht nötig. Siehe [Himmelsansicht](Sky-View-de#warnungen).

### Die Effektivität weicht von MCG_MS oder MS-Soft ab
YA-MS verwendet die tatsächliche Strecke und ein eigenes Modell; die Skala von OH5IY und MCG_MS ist nicht im Detail dokumentiert. Vergleiche eher Stunden und Tendenzen als absolute Prozentwerte, und siehe das [Modell](Efficiency-Calculation-de#das-modell).

### Der Strahldurchgang von GRAVES scheint verschoben
Die Strahlfolge wird aus der PC-Uhr berechnet: Synchronisiere sie mit einem NTP-Server. Die Kommandostation von GRAVES verschiebt die Folge außerdem manchmal um einige Schritte; das Detail ist eine Vorhersage, die durch Abhören zu bestätigen ist.

## Weitere Fragen

**Ist YA-MS kostenlos?** Ja, es ist ein kostenloses Programm für Funkamateure.

**Steuert es meinen Rotor oder mein Funkgerät?** Nein. YA-MS ist ein Werkzeug für Vorhersage und Planung; für das QSO verwendest du dein Programm für digitale Betriebsarten (z. B. MSHV, WSJT-X).

**Funktioniert es oberhalb von 432 MHz?** Die Bandliste endet bei 432 MHz (28, 50, 70, 144, 222, 432). Die experimentelle Vorhersage akzeptiert jede Frequenz von 28 bis 1300 MHz, aber die verwendeten SM6FHZ-Regeln stammen aus der Erfahrung auf 144 und 432 MHz.

**Etwas ist schiefgegangen.** Schreibe dem Autor mit deinem Betriebssystem, der YA-MS-Version und dem, was du getan hast: siehe [Mitarbeit und Kontakt](Contributing-and-Contacts-de).
