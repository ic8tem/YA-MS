LANGBAR

# Efektywność - wyjaśnienie

*Zakładka: Dokumenty techniczne › Efektywność - wyjaśnienie.*

[![Efektywność - wyjaśnienie](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Dokument techniczny *"Come YA-MS calcola l'efficienza di uno sciame"* (Jak YA-MS oblicza efektywność roju), wyświetlany w programie jako jasna strona. Wyjaśnia **krok po kroku**, jak otrzymuje się efektywność, i przy każdym kroku podaje, **skąd on pochodzi**. Dokument jest obecnie **po włosku**; ta wiki podaje jego treść po polsku w [Obliczaniu efektywności](Efficiency-Calculation-pl#model) oraz w [Geometrii i tłumieniu](Geometry-and-Path-Loss-pl).

## Etykiety

Każdy krok ma kolorową etykietę:

| Etykieta | Kolor | Znaczenie |
|---|---|---|
| **FONTE** (źródło) | niebieski | krok przejmuje cytowane źródło; liczba w nawiasie odsyła do listy na końcu |
| **RILIEVO** (sprawdzenie) | zielony | porównanie programu ze źródłami, wraz z wynikiem |
| **SCELTA** (wybór) | pomarańczowy | wybór programu, niezaczerpnięty ze źródła: do sprawdzenia doświadczeniem w eterze |

## Rozdziały

| Rozdział | Zawartość |
|---|---|
| 1. Wprowadzenie | Cel, etykiety, co oznacza efektywność (OH5IY, MCG_MS; YA-MS używa rzeczywistej trasy) |
| 2. Gdzie zachodzą odbicia: warstwa E | Ślady na 80–120 km; wysokość śladów = dominanta histogramu z Collm (sprawdzenie: 89,5 km w dniu 5/11/2026) |
| 3. Geometria trasy | Ziemia i punkt środkowy; elewacja anteny (wzór z artykułu); strefa wspólna i jej granice; Hot A / Hot B; wiązka anteny (DL6WU, Kraus, W4RNL) |
| 4. Radiant roju | Położenie radiantu (IMO 2026/2027), data maksimum (IMO lub długość ekliptyczna Słońca), profil aktywności |
| 5. Warunek odbicia | Odbicie zwierciadlane (McKinley), tolerancja gaussowska 0,05 rad, najlepszy kierunek (SM6FHZ), wzór DH9GCD |
| 6. Od jednego punktu do efektywności | Punkty odbicia co 15 km, waga każdego punktu, wartość procentowa; porównanie z QTFGUI (DJ5HG) |
| 7. Odczyt wyników | Strona A / B, indeks trasy, kolory radiantów, strefy PREV, przekrój widziany od strony anteny |
| 8. Częstotliwość pracy i tłumienie trasy | Reguły λ³ / λ², od radaru do pasma amatorskiego, odniesienia dla tłumienia trasy |
| 9. Znane ograniczenia | Tylko ślady podkrytyczne, anteny izotropowe, wartości robocze |
| 10. Źródła | 17 ponumerowanych źródeł |

## Przyciski

| Przycisk | Co robi |
|---|---|
| **Eksportuj do Worda (.docx)...** | Zapisuje kopię `data/efficienza_spiegazione.docx` we wskazanym miejscu (proponowana nazwa *YA-MS - calcolo dell'efficienza.docx*) |
| **Otwórz w Wordzie** | Otwiera ten sam plik `.docx` w domyślnym programie dla dokumentów Word (Word, LibreOffice, …) |

## Pliki

| Plik | Zawartość |
|---|---|
| `data/efficienza_spiegazione.txt` | Tekst wyświetlany w zakładce, jeden blok na wiersz (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Wersja Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Podręcznik obliczeń**: wszystkie równania (edytor równań Worda), ponumerowane, z ich źródłami |

Oba dokumenty generuje się ponownie ze źródeł poleceniami `tools/build_spiegazione.py data` i `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
