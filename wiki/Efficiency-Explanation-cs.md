**English** · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# Účinnost - vysvětlení

*Karta: Technické dokumenty › Účinnost - vysvětlení.*

[![Účinnost - vysvětlení](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Technický dokument *„Come YA-MS calcola l'efficienza di uno sciame“* (Jak YA-MS počítá účinnost roje), zobrazený v programu jako světlá stránka. Vysvětluje **krok za krokem**, jak se účinnost získává, a u každého kroku uvádí, **odkud pochází**. Dokument je zatím **v italštině**; tato wiki podává jeho obsah česky na stránkách [Výpočet účinnosti](Efficiency-Calculation-cs#model) a [Geometrie a útlum trasy](Geometry-and-Path-Loss-cs).

## Štítky

Každý krok nese barevný štítek:

| Štítek | Barva | Význam |
|---|---|---|
| **FONTE** (zdroj) | modrá | krok přebírá citovaný zdroj; číslo v závorce odkazuje na seznam na konci |
| **RILIEVO** (ověření) | zelená | srovnání programu se zdroji, s výsledkem |
| **SCELTA** (volba) | oranžová | volba programu, nepřevzatá ze zdroje: je třeba ji ověřit zkušeností z pásma |

## Kapitoly

| Kapitola | Obsah |
|---|---|
| 1. Úvod | Účel, štítky, co znamená účinnost (OH5IY, MCG_MS; YA-MS používá skutečnou trasu) |
| 2. Kde dochází k odrazům: vrstva E | Stopy v 80–120 km; výška stop = modus histogramu z Collmu (ověření: 89,5 km dne 5. 11. 2026) |
| 3. Geometrie trasy | Země a střed trasy; elevace antény (vzorec z článku); společná zóna a její meze; Hot A / Hot B; lalok antény (DL6WU, Kraus, W4RNL) |
| 4. Radiant roje | Poloha radiantu (IMO 2026/2027), datum maxima (IMO nebo sluneční délka), profil aktivity |
| 5. Podmínka odrazu | Zrcadlový odraz (McKinley), gaussovská tolerance 0,05 rad, nejlepší směr (SM6FHZ), vzorec DH9GCD |
| 6. Od jednoho bodu k účinnosti | Body odrazu každých 15 km, váha každého bodu, procenta; srovnání s QTFGUI (DJ5HG) |
| 7. Čtení výsledků | Strana A / B, index trasy, barvy radiantů, zóny PREV, řez viděný od antény |
| 8. Pracovní frekvence a útlum trasy | Pravidla λ³ / λ², od radaru k radioamatérskému pásmu, referenční hodnoty útlumu trasy |
| 9. Známá omezení | Jen podhusté stopy, izotropní antény, pracovní hodnoty |
| 10. Zdroje | 17 číslovaných zdrojů |

## Tlačítka

| Tlačítko | Co dělá |
|---|---|
| **Exportovat do Wordu (.docx)...** | Uloží kopii `data/efficienza_spiegazione.docx` na zvolené místo (navržený název *YA-MS - calcolo dell'efficienza.docx*) |
| **Otevřít ve Wordu** | Otevře tentýž `.docx` ve výchozím programu pro dokumenty Word (Word, LibreOffice, …) |

## Soubory

| Soubor | Obsah |
|---|---|
| `data/efficienza_spiegazione.txt` | Text zobrazený na kartě, jeden blok na řádek (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Verze pro Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Manuál výpočtů**: všechny rovnice (editor rovnic Wordu), číslované, se svými zdroji |

Oba dokumenty se ze zdrojového kódu znovu vygenerují pomocí `tools/build_spiegazione.py data` a `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
