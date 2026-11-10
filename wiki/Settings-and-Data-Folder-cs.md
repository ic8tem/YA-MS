**English** · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Nastavení a datová složka

## Lišta karet

Na pravém konci lišty karet, zprava doleva:

| Ovládací prvek | Co dělá |
|---|---|
| **Jazyk** (seznam) | Jazyk rozhraní; viz [Jazyk](#jazyk) |
| **Motiv** (seznam) | Barevné schéma; viz [Barevná schémata](#barevná-schémata) |
| **Ovládání ▴ / ▾** | Skryje nebo zobrazí tři řady ovládacích prvků nad kartami; viz [Písmo a Ovládání](#písmo-a-ovládání) |

Změna jazyka nebo motivu uloží nastavení a **znovu sestaví okno** ve stejné poloze a velikosti, na stejné kartě: restart není potřeba.

## Jazyk

28 jazyků rozhraní, stejných jako u YAEC a E-LAYER ANALYZER (pojmy společné s YAEC jsou přeloženy stejně):

| Jazyk | Kód | Soubor |
|---|---|---|
| Italiano | `it` | žádný: italština je základní jazyk (klíče) |
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

Při prvním spuštění použije YA-MS **jazyk systému**, pokud je mezi nimi, jinak italštinu. Čísla a data se řídí zvoleným jazykem (např. desetinná tečka v angličtině, čárka v italštině a němčině). Text, který v souboru překladu chybí, se zobrazí italsky. Na Linuxu potřebují čínština, japonština, korejština, arabština, hebrejština, urdština, hindština a bengálština vhodná písma (např. rodiny Noto): viz [Řešení problémů](Troubleshooting-FAQ-cs#linux-japonský-text-se-zobrazuje-jako-čtverečky).

Dokument [Účinnost - vysvětlení](Efficiency-Explanation-cs) a manuál výpočtů jsou v italštině.

## Barevná schémata

Seznam **Motiv** nabízí 12 schémat, stejných jako v autorově EME programu YAEC, plus původní paletu YA-MS:

| Schéma | Popis |
|---|---|
| **Světlé** | výchozí |
| **Noční** | tmavě modré tóny pro použití v noci |
| **Černé** | černé pozadí pro tmu a pro displeje OLED |
| Pastelová světle modrá · Pastelová oranžová · Pastelová akvamarínová · Pastelová zelená · Pastelová růžová · Pastelová šeříková · Pastelová indigová · Pastelová hnědá | osm světlých pastelových schémat |
| **Meteorická stopa** | původní styl YA-MS (do verze 1.2.0): noční fialová se světle modrou, fialovou, světle zelenou, žlutou a oranžovou |

Schéma platí pro všechny karty a ukládá se do `config.ini` (klíč `tema`).

## Písmo a Ovládání

- **Písmo** (na konci první řady ovládacích prvků): zvětší **veškerý text** ze **100 na 300 %** v krocích po 10 %; čáry, kružnice a mapy si zachovají velikost. Při velkém písmu se karty zalomí na druhý řádek a přehledové karty se zvětší.
- **Ovládání**: při velkém písmu nebo malé obrazovce skryjte tři řady ovládacích prvků, aby zůstalo místo pro mapy a grafy. Stav se pamatuje.

## Datová složka

Všechna data a nastavení jsou v jediné složce **`data`** **vedle programu** – žádné AppData, žádné systémové složky:

| Systém | Program | Data |
|---|---|---|
| Windows (instalátor) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (přenosná verze) | tam, kam jste ho rozbalili | `data` vedle `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (vedle aplikace) |

Při spuštění program v případě potřeby složku vytvoří a zkopíruje jen **chybějící** výchozí soubory: soubory, které jste změnili, se nikdy nepřepíší. Soubory překladů v `data/lingue` jsou soubory programu a nahradí se, pokud jsou soubory nové verze novější.

### Soubory, které můžete upravovat

| Soubor | Obsah |
|---|---|
| `sciami.csv` | Katalog rojů (hodnoty IMO a pracovní hodnoty); viz [Roje](Showers-cs#úprava-katalogu) |
| `massimi_imo.csv` | Data a časy maxim publikované IMO (2026, 2027): sem **přidávejte nové roky** |
| `ant_radiante.csv` | Poloha Antihelion Source (tabulka 6 IMO) |
| `fonti_radar.csv` | Adresy radarů; `attivo=1` stahuje, `0` ignoruje |
| `regole_sperimentali.csv` | Použité konstanty a pravidla, každé se svým zdrojem (odkazem) |
| `lingue/<code>.txt` | Překlady rozhraní; viz [Spolupráce](Contributing-and-Contacts-cs#překlady) |
| `config.ini` | Nastavení (viz níže) |

### Soubory vytvářené programem

| Soubor / složka | Obsah |
|---|---|
| `config.ini` | Nastavení |
| `flusso_collm.csv` | Hodinový archiv toku z Collmu |
| `quote_collm.csv` | Archiv výšek stop |
| `radar/` | Nejnovější radarové obrázky a soubory RMOB |
| `mappa/` | Pobřeží a hranice z Natural Earth (stažené při prvním spuštění) |
| `adif_quadrati.csv` | Čtverce z naposledy načteného ADIF |
| `efficienza_spiegazione.txt`, `.docx` | [Dokument s vysvětlením](Efficiency-Explanation-cs) |

## config.ini

Prostý text, jeden `key=value` na řádek (řádky začínající `#` nebo `;` jsou komentáře). Program ho zapisuje při ukončení, proto ho **upravujte, když je YA-MS zavřený**. Klíče, které se vám mohou hodit:

| Klíč | Výchozí | Význam |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Váš lokátor a výška (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Lokátor a výška DX stanice (m) |
| `banda_MHz` | 144 | Pásmo (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Výška stop (km); 1 = použít modus z Collmu |
| `elevazione_lobo_gradi` | 0 | Elevace laloku (°) |
| `boom_m` | 4,6 | Délka ráhna Yagi (m) |
| `hot_spot_km` | 150 | Vzdálenost Hot A / Hot B od středu trasy (30–400 km) |
| `lingua` | systém / `it` | Kód jazyka (jeden z 28 kódů výše, např. `it`, `en`, `de`) |
| `tema` | `chiaro` | Barevné schéma: `chiaro` (Světlé), `scuro` (Noční), `nero` (Černé), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteorická stopa) |
| `carattere_pct` | 100 | Velikost písma (100–300 %) |
| `comandi_visibili` | 1 | 1 = řady ovládacích prvků zobrazeny, 0 = skryty |
| `mostra_mappa`, `vista_alto` | 1, 1 | Mapa Evropy, pohled shora na Nebeské klenbě |
| `aggiornamento_automatico` | 1 | Automatická kontrola zdrojů každých 5 minut |
| `esponente_lambda` | 3 | Exponent λ na kartě Radarový tok |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Vstupy energetické bilance spoje |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Experimentální předpověď: frekvence, k, K |
| `rmob_osservatore` | prázdné | Jméno pozorovatele RMOB |
| `rmob_automatico` | 0 | Automatické stahování z RMOB (zapínejte jen se svolením RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Šablona adresy RMOB |
| `graves_sequenza` | 0 | Sekvence svazku GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Soukromí

YA-MS nesbírá žádná data a nezobrazuje reklamu. K internetu se připojuje jen kvůli stažení veřejných dat: radarových obrázků z Collmu a Sodankylä, mapy Natural Earth (při prvním spuštění) a, pokud o to požádáte, souboru RMOB.
