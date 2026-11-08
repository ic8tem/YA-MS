[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · **Deutsch** · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Mitarbeit und Kontakt

YA-MS wird durch die Rückmeldungen derer besser, die es auf dem Band einsetzen. Jede Korrektur wird mit ihrer Quelle genannt.

## Kontakt

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-Mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Ein Problem melden

Eröffne ein **Issue auf GitHub** oder schreibe eine E-Mail mit:

- Betriebssystem und YA-MS-Version (im Fenstertitel);
- den beiden Locatoren, Band und UTC-Zeit;
- was du erwartet und was du gesehen hast (ein Bildschirmfoto hilft);
- bei Radarproblemen der Meldung, die im Reiter [Radarfluss](Radar-Flux-de) angezeigt wird.

## Was besonders nützlich ist

- **Berichte vom Band.** Stunden und Strecken, bei denen Effektivität oder Vorhersage richtig – oder falsch – lagen. Das Modell ist experimentell und braucht den Vergleich mit echten QSOs und mit MCG_MS / MS-Soft.
- **RMOB-Vergleiche.** Werte des Stationsfaktors K und des Exponenten k, die du mit dem [RMOB-Vergleich](Experimental-Forecasts-de#rmob-vergleich) gefunden hast, mit deinem Band und deiner Station.
- **Daten mit Quelle.** Bessere Radiantenwanderungen, Aktivitätsprofile, neue IMO-Maxima (`data/massimi_imo.csv`), Antennendaten: Gib die Quelle an, sie wird zitiert.
- **Änderungen der Radardiagramme.** Ändert sich das Format des Collm-Diagramms, hilft eine Kopie des Bildes (`data/radar/`), das Ablesen neu zu kalibrieren.

## Übersetzungen

Die Übersetzungen der Oberfläche sind einfache Textdateien in **`data/lingue/<code>.txt`** (UTF-8), und **jeder kann sie korrigieren**:

```
<Italian text><TAB><translation>
```

- Ein Eintrag pro Zeile; Zeilen, die mit `#` beginnen, sind Kommentare.
- In beiden Spalten bedeuten die zwei Zeichen `\n` einen Zeilenumbruch.
- Behalte die Platzhalter `{0}`, `{1}`, … mit ihrem Format bei (z. B. `{0:F1}`, `{3:+0;-0}`), in der Reihenfolge, die deine Sprache braucht.
- Fehlende oder leere Einträge werden auf Italienisch angezeigt. Die Liste aller Schlüssel ist `data/lingue/chiavi.txt` (erzeugt von `tools/estrai_chiavi.py`, nicht von Hand bearbeiten).

Bearbeite die Datei im Ordner `data/lingue` deiner Installation und starte YA-MS neu (oder wechsle die Sprache), um das Ergebnis zu sehen. Da diese Dateien **bei jedem Update durch neuere Versionen ersetzt werden**, **schicke** bitte auch **deine Korrekturen** – per E-Mail oder als Pull Request auf GitHub (`data/lingue/`) –, damit sie in das nächste Release einfließen.

Dieses Wiki gibt es auf English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文; Korrekturen an den Wiki-Seiten sind ebenfalls willkommen.
