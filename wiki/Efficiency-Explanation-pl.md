[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-BR) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · **Polski** · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-TW)

# Efektywność - objaśnienie

*Zakładka: Dokumenty techniczne › Efektywność - objaśnienie.*

[![Efektywność - objaśnienie](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Dokument techniczny *"Come YA-MS calcola l'efficienza di uno sciame"* (Jak YA-MS oblicza efektywność roju), wyświetlany w programie jako jasna strona. Wyjaśnia **krok po kroku**, jak uzyskuje się efektywność, i dla każdego kroku podaje, **skąd on pochodzi**. Program wyświetla go **w języku interfejsu** (we wszystkich 36 językach), podobnie jak podręcznik obliczeń; ta wiki również przedstawia jego treść na stronach [Obliczanie efektywności](Efficiency-Calculation-pl#model) oraz [Geometria i tłumienie trasy](Geometry-and-Path-Loss-pl).

## Etykiety

Każdy krok ma kolorową etykietę:

| Etykieta | Kolor | Znaczenie |
|---|---|---|
| **FONTE** (źródło) | niebieski | krok przejmuje cytowane źródło; liczba w nawiasie odsyła do listy na końcu |
| **RILIEVO** (sprawdzenie) | zielony | porównanie programu ze źródłami, wraz z wynikiem |
| **SCELTA** (wybór) | pomarańczowy | wybór programu, niezaczerpnięty ze źródła: do sprawdzenia doświadczeniem na paśmie |

## Rozdziały

| Rozdział | Zawartość |
|---|---|
| 1. Wprowadzenie | Cel, etykiety, co oznacza efektywność (OH5IY, MCG_MS; YA-MS używa rzeczywistej trasy) |
| 2. Gdzie zachodzą odbicia: warstwa E | Ślady na 80–120 km; wysokość śladu = dominanta histogramu z Collm (sprawdzenie: 89,5 km w dniu 5/11/2026) |
| 3. Geometria trasy | Ziemia i punkt środkowy; elewacja anteny (wzór z artykułu); strefa wspólna i jej granice; Hot A / Hot B; listek anteny (DL6WU, Kraus, W4RNL) |
| 4. Radiant roju | Położenie radiantu (IMO 2026/2027), data maksimum (IMO lub długość ekliptyczna Słońca), profil aktywności |
| 5. Warunek odbicia | Odbicie zwierciadlane (McKinley), tolerancja gaussowska 0,05 rad, najlepszy kierunek (SM6FHZ), wzór DH9GCD |
| 6. Od jednego punktu do efektywności | Punkty odbicia co 15 km, waga każdego punktu, procent; porównanie z QTFGUI (DJ5HG) |
| 7. Odczyt wyników | Strona A / B, indeks trasy, kolory radiantów, strefy PREV, przekrój widziany od strony anteny |
| 8. Częstotliwość robocza i tłumienie trasy | Reguły λ³ / λ², od radaru do pasma amatorskiego, wartości odniesienia tłumienia trasy |
| 9. Znane ograniczenia | Tylko ślady podgęste, anteny izotropowe, wartości robocze |
| 10. Źródła | 17 ponumerowanych źródeł |

## Przyciski

| Przycisk | Działanie |
|---|---|
| **Eksportuj do Worda (.docx)...** | Zapisuje kopię `data/efficienza_spiegazione.docx` w wybranym miejscu (proponowana nazwa *YA-MS - calcolo dell'efficienza.docx*) |
| **Otwórz w Wordzie** | Otwiera ten sam plik `.docx` domyślnym programem dla dokumentów Word (Word, LibreOffice, …) |

## Pliki

| Plik | Zawartość |
|---|---|
| `data/efficienza_spiegazione.txt` | Tekst wyświetlany w zakładce, jeden blok w wierszu (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Wersja Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Ten sam dokument w pozostałych 35 językach (np. `_en`, `_de`, `_pt-BR`) |
| `doc/YA-MS_manuale_calcoli.docx` | **Podręcznik obliczeń** (po włosku): wszystkie równania (edytor równań Worda), ponumerowane, wraz ze źródłami |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Podręcznik obliczeń w pozostałych 35 językach |

Oba dokumenty są generowane ze źródeł poleceniami `tools/build_spiegazione.py data [code]` oraz `node tools/build_manuale.js <file.docx> [code]`; tłumaczenia znajdują się w `tools/traduzioni_doc/` (`tools/build_documenti.sh` odbudowuje wszystkie języki).
