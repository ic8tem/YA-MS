**English** · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Ustawienia i folder danych

## Pasek zakładek

Na prawym końcu paska zakładek, od prawej do lewej:

| Element | Działanie |
|---|---|
| **Język** (lista) | Język interfejsu; zob. [Język](#język) |
| **Motyw** (lista) | Schemat kolorów; zob. [Schematy kolorów](#schematy-kolorów) |
| **Sterowanie ▴ / ▾** | Zwija lub rozwija trzy wiersze elementów sterujących nad zakładkami; zob. [Czcionka i Sterowanie](#czcionka-i-sterowanie) |

Zmiana języka lub motywu zapisuje ustawienia i **odbudowuje okno** w tym samym położeniu i rozmiarze, na tej samej zakładce: ponowne uruchomienie nie jest potrzebne.

## Język

36 języków interfejsu, tych samych co w YAEC i E-LAYER ANALYZER (terminy wspólne z YAEC są tłumaczone tak samo):

| Język | Kod | Plik |
|---|---|---|
| Italiano | `it` | brak: włoski jest językiem bazowym (klucze) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português (Portugal) | `pt` | `data/lingue/pt.txt` |
| Português (Brasil) | `pt-BR` | `data/lingue/pt-BR.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |
| Svenska | `sv` | `data/lingue/sv.txt` |
| Norsk (bokmål) | `nb` | `data/lingue/nb.txt` |
| Dansk | `da` | `data/lingue/da.txt` |
| Íslenska | `is` | `data/lingue/is.txt` |
| Eesti | `et` | `data/lingue/et.txt` |
| Latviešu | `lv` | `data/lingue/lv.txt` |
| Lietuvių | `lt` | `data/lingue/lt.txt` |
| Polski | `pl` | `data/lingue/pl.txt` |
| Čeština | `cs` | `data/lingue/cs.txt` |
| Magyar | `hu` | `data/lingue/hu.txt` |
| Română | `ro` | `data/lingue/ro.txt` |
| Ελληνικά | `el` | `data/lingue/el.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| Українська | `uk` | `data/lingue/uk.txt` |
| Türkçe | `tr` | `data/lingue/tr.txt` |
| Afrikaans | `af` | `data/lingue/af.txt` |
| العربية | `ar` | `data/lingue/ar.txt` |
| עברית | `he` | `data/lingue/he.txt` |
| اردو | `ur` | `data/lingue/ur.txt` |
| हिन्दी | `hi` | `data/lingue/hi.txt` |
| বাংলা | `bn` | `data/lingue/bn.txt` |
| ไทย | `th` | `data/lingue/th.txt` |
| Bahasa Indonesia | `id` | `data/lingue/id.txt` |
| Tagalog | `tl` | `data/lingue/tl.txt` |
| 中文 (简体) | `zh` | `data/lingue/zh.txt` |
| 中文 (繁體) | `zh-TW` | `data/lingue/zh-TW.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

Przy pierwszym uruchomieniu YA-MS używa **języka systemu**, jeśli jest jednym z powyższych, w przeciwnym razie włoskiego. Liczby i daty są zgodne z wybranym językiem (np. kropka dziesiętna w angielskim, przecinek we włoskim, niemieckim i polskim). Każdy tekst, którego brakuje w pliku tłumaczenia, jest wyświetlany po włosku. W Linuksie chiński, japoński, koreański, arabski, hebrajski, urdu, hindi i bengalski wymagają odpowiednich czcionek (np. z rodziny Noto): zob. [Rozwiązywanie problemów](Troubleshooting-FAQ-pl#linux-tekst-japoński-wyświetla-się-jako-prostokąty).

Dokument [Efektywność - objaśnienie](Efficiency-Explanation-pl) jest wyświetlany w języku interfejsu; podręcznik obliczeń znajduje się w `doc/` (po włosku) i `doc/manuali/` (pozostałe 35 języków).

## Schematy kolorów

Lista **Motyw** oferuje 12 schematów, tych samych co w programie EME autora, YAEC, oraz oryginalną paletę YA-MS:

| Schemat | Opis |
|---|---|
| **Jasny** | domyślny |
| **Noc** | ciemnoniebieskie odcienie, do pracy w nocy |
| **Czarny** | czarne tło, do pracy w ciemności i dla ekranów OLED |
| Pastelowy jasnoniebieski · Pastelowy pomarańczowy · Pastelowy akwamaryna · Pastelowy zielony · Pastelowy różowy · Pastelowy liliowy · Pastelowy indygo · Pastelowy brązowy | osiem jasnych schematów pastelowych |
| **Ślad meteoru** | oryginalny styl YA-MS (do wersji 1.2.0): nocny fiolet z jasnoniebieskim, fioletowym, jasnozielonym, żółtym i pomarańczowym |

Schemat dotyczy wszystkich zakładek i jest zapisywany w `config.ini` (klucz `tema`).

## Czcionka i Sterowanie

- **Czcionka** (na końcu pierwszego wiersza elementów sterujących): powiększa **cały tekst** od **100 do 300 %** w krokach co 10 %; linie, okręgi i mapy zachowują swój rozmiar. Przy dużych czcionkach zakładki przechodzą do drugiego wiersza, a karty się powiększają.
- **Sterowanie**: przy dużych czcionkach lub małym ekranie zwiń trzy wiersze elementów sterujących, aby zostawić miejsce na mapy i wykresy. Stan jest zapamiętywany.

## Folder danych

Wszystkie dane i ustawienia znajdują się w jednym folderze **`data`** **obok programu** – bez AppData, bez folderów systemowych:

| System | Program | Dane |
|---|---|---|
| Windows (instalator) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (wersja przenośna) | tam, gdzie go rozpakowałeś | `data` obok `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (obok aplikacji) |

Przy uruchomieniu program w razie potrzeby tworzy folder i kopiuje tylko **brakujące** pliki startowe: pliki, które zmieniłeś, nigdy nie są nadpisywane. Pliki tłumaczeń w `data/lingue` są plikami programu i są zastępowane, gdy pliki nowej wersji są nowsze.

### Pliki, które możesz edytować

| Plik | Zawartość |
|---|---|
| `sciami.csv` | Katalog rojów (wartości IMO i wartości robocze); zob. [Roje](Showers-pl#edycja-katalogu) |
| `massimi_imo.csv` | Daty i godziny maksimów opublikowane przez IMO (2026, 2027): tutaj **dodawaj nowe lata** |
| `ant_radiante.csv` | Położenie Antihelion Source (tabela 6 IMO) |
| `fonti_radar.csv` | Adresy radarów; `attivo=1` pobiera, `0` pomija |
| `regole_sperimentali.csv` | Używane stałe i reguły, każda ze swoim źródłem (odniesieniem) |
| `lingue/<code>.txt` | Tłumaczenia interfejsu; zob. [Współpraca](Contributing-and-Contacts-pl#tłumaczenia) |
| `config.ini` | Ustawienia (zob. niżej) |

### Pliki tworzone przez program

| Plik / folder | Zawartość |
|---|---|
| `config.ini` | Ustawienia |
| `flusso_collm.csv` | Godzinowe archiwum strumienia z Collm |
| `quote_collm.csv` | Archiwum wysokości śladów |
| `radar/` | Najnowsze obrazy radarowe i pliki RMOB |
| `mappa/` | Linie brzegowe i granice Natural Earth (pobierane przy pierwszym uruchomieniu) |
| `adif_quadrati.csv` | Kwadraty z ostatnio wczytanego pliku ADIF |
| `efficienza_spiegazione.txt`, `.docx` | [Dokument z objaśnieniem](Efficiency-Explanation-pl) |

## config.ini

Zwykły tekst, jedna para `key=value` w wierszu (wiersze zaczynające się od `#` lub `;` są komentarzami). Program zapisuje go przy zamykaniu, więc **edytuj go przy zamkniętym YA-MS**. Klucze, które warto znać:

| Klucz | Domyślnie | Znaczenie |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Twój lokator i wysokość (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Lokator i wysokość stacji DX (m) |
| `banda_MHz` | 144 | Pasmo (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Wysokość śladu (km); 1 = użyj dominanty z Collm |
| `elevazione_lobo_gradi` | 0 | Elewacja listka (°) |
| `boom_m` | 4.6 | Długość boomu anteny Yagi (m) |
| `hot_spot_km` | 150 | Odległość Hot A / Hot B od punktu środkowego (30–400 km) |
| `lingua` | systemowy / `it` | Kod języka (jeden z 36 powyższych kodów, np. `it`, `en`, `de`) |
| `tema` | `chiaro` | Schemat kolorów: `chiaro` (Jasny), `scuro` (Noc), `nero` (Czarny), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Ślad meteoru) |
| `carattere_pct` | 100 | Rozmiar czcionki (100–300 %) |
| `comandi_visibili` | 1 | 1 = wiersze elementów sterujących widoczne, 0 = zwinięte |
| `mostra_mappa`, `vista_alto` | 1, 1 | Mapa Europy, widok z góry na kopule nieba |
| `aggiornamento_automatico` | 1 | Automatyczne sprawdzanie źródeł co 5 minut |
| `esponente_lambda` | 3 | Wykładnik λ w zakładce Strumień radarowy |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Dane wejściowe bilansu łącza |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Prognoza eksperymentalna: częstotliwość, k, K |
| `rmob_osservatore` | pusty | Nazwa obserwatora RMOB |
| `rmob_automatico` | 0 | Automatyczne pobieranie z RMOB (włączaj tylko za zgodą RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Szablon adresu RMOB |
| `graves_sequenza` | 0 | Sekwencja wiązki GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Prywatność

YA-MS nie zbiera żadnych danych i nie wyświetla reklam. Łączy się z internetem wyłącznie w celu pobrania danych publicznych: obrazów z radarów w Collm i Sodankylä, mapy Natural Earth (przy pierwszym uruchomieniu) oraz, jeśli o to poprosisz, pliku RMOB.
