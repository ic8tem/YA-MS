[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · **Deutsch** · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Einstellungen und Datenordner

## Die Reiterleiste

Am rechten Ende der Reiterleiste, von rechts nach links:

| Bedienelement | Was es tut |
|---|---|
| **Sprache der Oberfläche** (Liste) | Sprache der Oberfläche; siehe [Sprache](#sprache) |
| **Farbschema** (Liste) | Farbschema; siehe [Farbschemata](#farbschemata) |
| **Bedienung ▴ / ▾** | Klappt die drei Bedienzeilen über den Reitern ein oder aus; siehe [Schrift und Bedienung](#schrift-und-bedienung) |

Ein Wechsel von Sprache oder Farbschema speichert die Einstellungen und **baut das Fenster neu auf**, in gleicher Position und Größe, auf demselben Reiter: Ein Neustart ist nicht nötig.

## Sprache

28 Sprachen der Oberfläche, dieselben wie bei YAEC und E-LAYER ANALYZER (mit YAEC gemeinsame Begriffe sind gleich übersetzt):

| Sprache | Code | Datei |
|---|---|---|
| Italiano | `it` | keine: Italienisch ist die Basissprache (die Schlüssel) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português | `pt` | `data/lingue/pt.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |
| Svenska | `sv` | `data/lingue/sv.txt` |
| Norsk (bokmål) | `nb` | `data/lingue/nb.txt` |
| Dansk | `da` | `data/lingue/da.txt` |
| Íslenska | `is` | `data/lingue/is.txt` |
| Eesti | `et` | `data/lingue/et.txt` |
| Latviešu | `lv` | `data/lingue/lv.txt` |
| Lietuvių | `lt` | `data/lingue/lt.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| Українська | `uk` | `data/lingue/uk.txt` |
| Türkçe | `tr` | `data/lingue/tr.txt` |
| Afrikaans | `af` | `data/lingue/af.txt` |
| العربية | `ar` | `data/lingue/ar.txt` |
| עברית | `he` | `data/lingue/he.txt` |
| اردو | `ur` | `data/lingue/ur.txt` |
| हिन्दी | `hi` | `data/lingue/hi.txt` |
| বাংলা | `bn` | `data/lingue/bn.txt` |
| Bahasa Indonesia | `id` | `data/lingue/id.txt` |
| Tagalog | `tl` | `data/lingue/tl.txt` |
| 中文 (简体) | `zh` | `data/lingue/zh.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

Beim ersten Start verwendet YA-MS die **Systemsprache**, wenn sie eine dieser Sprachen ist, sonst Italienisch. Zahlen und Datumsangaben folgen der gewählten Sprache (z. B. Dezimalpunkt im Englischen, Komma im Italienischen und Deutschen). Texte, die in einer Übersetzungsdatei fehlen, werden auf Italienisch angezeigt. Unter Linux brauchen Chinesisch, Japanisch, Koreanisch, Arabisch, Hebräisch, Urdu, Hindi und Bengalisch passende Schriften (z. B. die Noto-Familien): siehe [Fehlerbehebung](Troubleshooting-FAQ-de#linux-japanischer-text-zeigt-kästchen).

Das Dokument [Effektivität - Erklärung](Efficiency-Explanation-de) und das Berechnungshandbuch sind auf Italienisch.

## Farbschemata

Die Liste **Farbschema** bietet 12 Schemata, dieselben wie im EME-Programm YAEC des Autors plus die ursprüngliche YA-MS-Palette:

| Schema | Beschreibung |
|---|---|
| **Hell** | Standard |
| **Nacht** | dunkle Blautöne, für den Einsatz bei Nacht |
| **Schwarz** | schwarzer Hintergrund, für die Dunkelheit und für OLED-Bildschirme |
| Pastell Hellblau · Pastell Orange · Pastell Aquamarin · Pastell Grün · Pastell Rosa · Pastell Flieder · Pastell Indigo · Pastell Braun | acht helle Pastellschemata |
| **Meteorspur** | der ursprüngliche YA-MS-Stil (bis Version 1.2.0): Nachtviolett mit Hellblau, Violett, Hellgrün, Gelb und Orange |

Das Schema gilt für alle Reiter und wird in `config.ini` gespeichert (Schlüssel `tema`).

## Schrift und Bedienung

- **Schrift** (Ende der ersten Bedienzeile): vergrößert **den gesamten Text** von **100 auf 300 %** in Schritten von 10 %; Linien, Kreise und Karten behalten ihre Größe. Bei großer Schrift brechen die Reiter in eine zweite Zeile um und die Karten werden größer.
- **Bedienung**: Bei großer Schrift oder kleinem Bildschirm klappst du die drei Bedienzeilen ein, um Platz für Karten und Diagramme zu schaffen. Der Zustand wird gespeichert.

## Datenordner

Alle Daten und Einstellungen liegen in einem einzigen Ordner **`data`** **neben dem Programm** – kein AppData, keine Systemordner:

| System | Programm | Daten |
|---|---|---|
| Windows (Installationsprogramm) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabel) | wo du es entpackt hast | `data` neben `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (neben der App) |

Beim Start legt das Programm den Ordner bei Bedarf an und kopiert nur die **fehlenden** Startdateien: Dateien, die du geändert hast, werden nie überschrieben. Die Übersetzungsdateien in `data/lingue` sind Programmdateien und werden ersetzt, wenn die Dateien der neuen Version aktueller sind.

### Dateien, die du bearbeiten kannst

| Datei | Inhalt |
|---|---|
| `sciami.csv` | Meteorstrom-Katalog (IMO-Werte und Arbeitswerte); siehe [Ströme](Showers-de#katalog-bearbeiten) |
| `massimi_imo.csv` | Von der IMO veröffentlichte Datum und Uhrzeit der Maxima (2026, 2027): **neue Jahre** hier **hinzufügen** |
| `ant_radiante.csv` | Position der Antihelion-Quelle (IMO-Tabelle 6) |
| `fonti_radar.csv` | Radaradressen; `attivo=1` lädt, `0` ignoriert |
| `regole_sperimentali.csv` | Verwendete Konstanten und Regeln, jede mit ihrer Quelle (zum Nachschlagen) |
| `lingue/<code>.txt` | Übersetzungen der Oberfläche; siehe [Mitarbeit](Contributing-and-Contacts-de#übersetzungen) |
| `config.ini` | Einstellungen (siehe unten) |

### Vom Programm erzeugte Dateien

| Datei / Ordner | Inhalt |
|---|---|
| `config.ini` | Einstellungen |
| `flusso_collm.csv` | Stündliches Archiv des Collm-Flusses |
| `quote_collm.csv` | Archiv der Spurhöhen |
| `radar/` | Neueste Radarbilder und RMOB-Dateien |
| `mappa/` | Küsten und Grenzen von Natural Earth (beim ersten Start geladen) |
| `adif_quadrati.csv` | Felder aus der zuletzt geladenen ADIF-Datei |
| `efficienza_spiegazione.txt`, `.docx` | Das [Erklärungsdokument](Efficiency-Explanation-de) |

## config.ini

Reiner Text, ein `key=value` pro Zeile (Zeilen, die mit `#` oder `;` beginnen, sind Kommentare). Das Programm schreibt die Datei beim Beenden, deshalb **bearbeite sie bei geschlossenem YA-MS**. Die Schlüssel, die du kennen solltest:

| Schlüssel | Standard | Bedeutung |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Dein Locator und deine Höhe (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locator und Höhe (m) der Gegenstation |
| `banda_MHz` | 144 | Band (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Spurhöhe (km); 1 = Collm-Modalwert verwenden |
| `elevazione_lobo_gradi` | 0 | Keulenelevation (°) |
| `boom_m` | 4.6 | Boomlänge der Yagi (m) |
| `hot_spot_km` | 150 | Abstand von Hot A / Hot B vom Mittelpunkt (30–400 km) |
| `lingua` | System / `it` | Sprachcode (einer der 28 Codes oben, z. B. `it`, `en`, `de`) |
| `tema` | `chiaro` | Farbschema: `chiaro` (Hell), `scuro` (Nacht), `nero` (Schwarz), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteorspur) |
| `carattere_pct` | 100 | Schriftgröße (100–300 %) |
| `comandi_visibili` | 1 | 1 = Bedienzeilen sichtbar, 0 = eingeklappt |
| `mostra_mappa`, `vista_alto` | 1, 1 | Europakarte, Draufsicht in der Himmelsansicht |
| `aggiornamento_automatico` | 1 | Automatische Prüfung der Quellen alle 5 Minuten |
| `esponente_lambda` | 3 | Exponent λ im Reiter Radarfluss |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Eingaben der Streckenbilanz |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Experimentelle Vorhersage: Frequenz, k, K |
| `rmob_osservatore` | leer | Name des RMOB-Beobachters |
| `rmob_automatico` | 0 | Automatischer RMOB-Abruf (nur mit Erlaubnis von RMOB aktivieren) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Vorlage der RMOB-Adresse |
| `graves_sequenza` | 0 | Strahlfolge von GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Datenschutz

YA-MS sammelt keine Daten und zeigt keine Werbung. Es verbindet sich nur mit dem Internet, um öffentliche Daten zu laden: die Radarbilder aus Collm und Sodankylä, die Karte von Natural Earth (erster Start) und, wenn du es anforderst, eine RMOB-Datei.
