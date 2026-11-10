LANGBAR

# Sklepienie niebieskie

*Zakładka: Obliczenie prognozy › Obliczenie prognozy.*

[![Sklepienie niebieskie](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ta podzakładka (sklepienie niebieskie z wcześniejszych wersji) pokazuje na jednym ekranie, **gdzie** są teraz użyteczne ślady i **gdzie kierować antenę**. Po lewej **rzut z góry** trasy; po prawej lista rojów, małe sklepienie niebieskie z radiantami, tekst obliczenia i **przekrój** widziany od strony twojej anteny. Wszystko odnosi się do czasu ustawionego suwakiem *Czas sklepienia niebieskiego* (domyślnie czas rzeczywisty; ±36 h w krokach co 15 minut).

Na małym sklepieniu niebieskim **pomarańczowa linia** przechodząca przez zenit zawsze wskazuje **właściwe kierunki anteny**, prostopadłe do przesuwania się wybranego roju (lub najkorzystniejszego): azymut radiantu ±90°, z etykietą *antena NNN°* na obu końcach i tolerancją ±45° zaznaczoną cienkimi liniami. Krótkie pomarańczowe kreski na obrzeżu wskazują prostopadłe kierunki pozostałych użytecznych rojów.

## Rzut z góry (po lewej)

Mapa Europy widziana z góry (**E po prawej**) z otaczającą ją skalą stopni. Podpis pod mapą podaje jej promień (*Mapa: krawędź = … km od stacji*).

| Element | Rysunek |
|---|---|
| Trasa / DX | Zielona linia od twojej stacji do korespondenta (zawsze rzeczywista trasa po ortodromie między lokatorami) |
| **Hot A / Hot B** | Punkty 150 km (regulowane) po obu stronach punktu środkowego, prostopadle do trasy. **Czerwony = zalecany**, **różowy = poza wiązką anteny**, **szary = wewnątrz wiązki** (z ostrzeżeniem) |
| Wiązka anteny | Pozioma wiązka −3 dB wokół azymutu anteny (antena zawsze skierowana na DX), z etykietą *wiązka …°* |
| Granice strefy wspólnej | Blade punkty *gr. A* / *gr. B* oraz dwa okręgi, w których horyzont każdej stacji przecina warstwę E (zob. [Geometria](Geometry-and-Path-Loss-pl#granice-strefy-wspólnej)) |
| Przesuwanie się roju | **Żółta linia**: kierunek, w którym wybrany rój (lub najkorzystniejszy) przemiata niebo, czyli azymut radiantu |
| Najlepsze kierunki | **Pomarańczowe punkty**: dwa kierunki prostopadłe do przesuwania się roju (azymut radiantu ±90°, SM6FHZ) |
| **Strefy PREV** | Jasne elipsy: gdzie **teraz** padają najbardziej prawdopodobne ślady, po jednej na każdą stronę trasy |

Etykiety nie nachodzą na siebie: Hot A i PREV A są opisane po lewej stronie trasy, B po prawej. **Legenda** to zwijana kolumna po prawej stronie mapy.

**Mysz na mapie:** **lewy klik = lokator korespondenta**, **prawy klik = lokator mojej stacji**. Trasa jest natychmiast obliczana ponownie.

Opcje nad listą rojów: **Kierunki Hot A / Hot B**, **Mapa Europy** (Natural Earth, pobierana do `data/mappa` przy pierwszym uruchomieniu), **Widok z góry (E po prawej)**.

### Zalecany Hot

Dla pokazywanego czasu program sumuje po wszystkich rojach nad horyzontem wagę ZHR × efektywność, podzieloną między stronę A (udział f_A) i stronę B. Strona o większej wadze wyznacza zalecany Hot, rysowany na czerwono:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*Wybór programu (podręcznik, wz. 23).* Źródło pomysłu: DJ5HG, za DF5HC (konferencja DARC 2018) – w zależności od położenia radiantu jeden z dwóch punktów, HOT-A lub HOT-B, jest korzystniejszy. Obrót o 10–30° w tę stronę (side-scatter) pochodzi z artykułu Cerrotta–Sartori.

### Strefy PREV

Dla każdego punktu P warstwy E sumowane są wkłady wszystkich aktywnych rojów do efektywności (ten sam warunek zwierciadlany co przy [efektywności](Efficiency-Calculation-pl#model)), ważone ZHR. Punkty z co najmniej 3 % maksimum tworzą strefy PREV; każda jest rysowana jako elipsa o środku = średnia ważona punktów i osiach = dwukrotność ich rozrzutu.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Wybór programu (podręcznik, wz. 34).* To reguła praktyczna: jeśli rój przemiata niebo z północy na południe, użyteczne ślady padają na wschodzie i zachodzie.

## Lista rojów (u góry po prawej)

| Kolumna | Znaczenie |
|---|---|
| Rój, Kod | Nazwa i kod IMO |
| ZHR teraz | Aktywność w tej chwili (ZHR maksimum według IMO z profilem aktywności) |
| Azymut, Elew. | Położenie radiantu widziane z twojej stacji |
| Efekt. % | Efektywność roju dla tej trasy |
| Strona | A lub B, strona, z której przychodzi najwięcej odbić |
| Najl. kierunek | Azymut radiantu ±90° |
| Wschód, Zachód | Wschód i zachód radiantu (UTC); *okołobiegunowy* lub *zawsze poniżej*, gdy ma to zastosowanie |

Kliknij wiersz, aby wybrać rój: żółta linia przesuwania się i pomarańczowe punkty podążają za nim.

## Małe sklepienie niebieskie (pośrodku po prawej)

Radianty na sklepieniu niebieskim widzianym z twojej stacji, z ich **kodem IMO** i **dziennym torem w kolorze cyjan** (godziny UTC). **Kliknij radiant**, aby go wybrać. Kolory:

| Kolor | Znaczenie |
|---|---|
| Żółty | efektywność ≥ 50 % i ZHR ≥ 2 |
| Pomarańczowy | efektywność ≥ 20 % |
| Ciemnoczerwony | efektywność < 20 % |
| Szary | prawie nieaktywny |

Obok tekst obliczenia: długość i azymut trasy, punkt środkowy i jego elewacja, azymuty i przesunięcia Hot A / Hot B, zalecany Hot (*… zalecany teraz: az. …° (…% przewidywanych odbić)*), granice strefy wspólnej oraz przypomnienie: *najlepsze ustawienie anteny dla roju: PROSTOPADLE do kierunku napływu (azymut radiantu ±90°, tolerancja ±40–50°, SM6FHZ)*.

## Przekrój (u dołu po prawej)

*PRZEKRÓJ – najbardziej prawdopodobne ślady widziane od strony anteny w kierunku korespondenta.* W poziomie **azymut względem korespondenta** (← A lewo, B → prawo), w pionie **elewacja**. Dla każdego roju brane jest 14 najsilniejszych punktów odbicia; każdy ślad to odcinek zorientowany w stronę radiantu, od 10 km powyżej do 10 km poniżej wysokości śladów (najwyżej 60 km w każdą stronę), grubszy, gdy jest bardziej prawdopodobny. Rysowane są też: wiązka anteny (okrąg −3 dB wokół elewacji wiązki), korespondent i Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Wybór programu (podręcznik, wz. 35).*

## Ostrzeżenia

| Ostrzeżenie | Kiedy |
|---|---|
| **UWAGA: Hot A (i/lub Hot B) znajduje się wewnątrz wiązki anteny …** | Hot spot leży w granicach ±θ/2 od azymutu anteny (θ = pozioma wiązka −3 dB): przy tym kierunku jest już pokryty. Pokazywany na szaro na mapie. Zalecany Hot pozostaje czerwony. |
| **RADIANT ZA WYSOKO (powyżej 70°)** | Użyteczny radiant jest wyżej niż 70° nad twoją stacją: ślady padają prawie pionowo i mało odbijają w stronę trasy (DF5HC, DH9GCD). Te same godziny są oznaczone ↑ w [tabeli godzinowej](Efficiency-Calculation-pl#tabela-godzinowa). |
| *Brak wspólnej strefy warstwy E* | Trasa jest dłuższa niż dwukrotność zasięgu na wysokości śladów: obie stacje nie widzą wspólnej części warstwy E (pojedynczy skok niemożliwy). |
| *Brak zalecanego Hot* | W tej chwili prawie brak aktywnych rojów. |

Wzór dla grafiki sklepienia niebieskiego: Swan Meteor Skyview autorstwa DL1DBC (swan.ms); wykres biegunowy z najlepszym kierunkiem: RadiantCalc autorstwa SM6FHZ.
