[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-BR) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · **Polski** · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-TW)

# Kopuła nieba

*Zakładka: Obliczanie prognozy › Obliczanie prognozy.*

[![Kopuła nieba](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ta podzakładka (kopuła nieba z wcześniejszych wersji) zbiera na jednym ekranie informacje o tym, **gdzie** są teraz użyteczne ślady i **gdzie kierować antenę**. Po lewej **widok z góry** trasy; po prawej lista rojów, mała kopuła nieba z radiantami, tekst obliczeń oraz **przekrój** widziany od strony twojej anteny. Wszystko odnosi się do momentu wybranego polem *Data obliczeń (UTC)* i suwakiem *Godziny (−12 do +36 h)* (domyślnie czas rzeczywisty, kroki co 15 minut).

**Pasek nad widokiem z góry** podsumowuje obliczenia dla tego momentu: data i godzina (*teraz* lub liczba godzin od teraz), **indeks trasy Σ ZHR×η**, **najbardziej użyteczny rój** z jego ZHR i efektywnością (również w dB względem odniesienia DJ5HG, zob. [Obliczanie efektywności](Efficiency-Calculation-pl)), liczba rojów nad horyzontem oraz **zalecany Hot** z jego azymutem.

Na małej kopule nieba **pomarańczowa linia** przechodząca przez zenit zawsze wskazuje **właściwe kierunki anteny**, prostopadłe do dryfu wybranego roju (lub najkorzystniejszego): azymut radiantu ±90°, opisane na obu końcach jako *antena NNN°*, z tolerancją ±45° zaznaczoną cienkimi liniami. Krótkie pomarańczowe kreski na obwodzie wskazują kierunki prostopadłe dla pozostałych użytecznych rojów.

## Widok z góry (po lewej)

Mapa Europy widziana z góry (**E po prawej**) ze skalą stopni dookoła. Podpis pod mapą podaje jej promień (*Mapa: krawędź = … km od stacji*).

| Element | Rysunek |
|---|---|
| Trasa / DX | Zielona linia od twojej stacji do stacji DX (zawsze rzeczywista trasa po ortodromie między lokatorami) |
| **Hot A / Hot B** | Punkty po obu stronach punktu środkowego, prostopadle do trasy, w odległości wynikającej z tabeli odchyleń AMS (lub wpisanej ręcznie). **Czerwony = zalecany**, **różowy = poza listkiem anteny**, **szary = wewnątrz listka** (z ostrzeżeniem) |
| Listek anteny | Listek poziomy −3 dB wokół azymutu anteny (antena zawsze skierowana na DX), opisany jako *listek …°* |
| Granice strefy wspólnej | Blade punkty *gr. A* / *gr. B* i dwa okręgi, w których horyzont każdej stacji spotyka warstwę E (zob. [Geometria](Geometry-and-Path-Loss-pl#granice-strefy-wspólnej)) |
| Dryf roju | **Żółta linia**: kierunek, w którym wybrany rój (lub najkorzystniejszy) przesuwa się po niebie, czyli azymut radiantu |
| Najlepsze kierunki | **Pomarańczowe kropki**: dwa kierunki prostopadłe do dryfu (azymut radiantu ±90°, SM6FHZ) |
| **Strefy PREV** | Jasne elipsy: miejsca, w których **teraz** wypadają najbardziej prawdopodobne ślady, po jednej na każdą stronę trasy |

Etykiety nie nachodzą na siebie: Hot A i PREV A są opisane po lewej stronie trasy, B po prawej. **Legenda** to zwijana kolumna po prawej stronie mapy.

**Mysz na mapie:** **lewy klik = lokator stacji DX**, **prawy klik = lokator mojej stacji**. Trasa jest natychmiast przeliczana.

Opcje nad listą rojów: **Kierunki Hot A / Hot B**, **Mapa Europy** (Natural Earth, pobierana do `data/mappa` przy pierwszym uruchomieniu), **Widok z góry (E po prawej)**.

### Zalecany Hot

Dla wyświetlanej pory program sumuje po wszystkich rojach nad horyzontem wagę ZHR × efektywność, podzieloną między stronę A (udział f_A) i stronę B. Strona o większej wadze wyznacza zalecany Hot, rysowany na czerwono:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Wybór programu (podręcznik, wz. 23).* Źródło pomysłu: DJ5HG, przytoczony przez DF5HC (konferencja DARC 2018) – w zależności od położenia radiantu jeden z dwóch punktów, HOT-A lub HOT-B, jest korzystniejszy. Obrót o 10–30° w tę stronę (side-scatter) pochodzi z artykułu Cerrotta–Sartori.

### Strefy PREV

Dla każdego punktu P warstwy E sumowane są przyczynki wszystkich aktywnych rojów do efektywności (ten sam warunek zwierciadlany co dla [efektywności](Efficiency-Calculation-pl#model)), ważone ZHR. Punkty o wartości co najmniej 3 % maksimum tworzą strefy PREV; każda jest rysowana jako elipsa ze środkiem = średnia ważona punktów i osiami = dwukrotność ich rozrzutu.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Wybór programu (podręcznik, wz. 34).* To praktyczna reguła: jeśli rój przesuwa się z północy na południe, użyteczne ślady wypadają na wschodzie i zachodzie.

## Lista rojów (u góry po prawej)

| Kolumna | Znaczenie |
|---|---|
| Rój, Kod | Nazwa i kod IMO |
| ZHR teraz | Aktywność w tym momencie (ZHR w maksimum wg IMO z profilem aktywności) |
| Azymut, Elew. | Położenie radiantu widziane z twojej stacji |
| Efekt. % | Efektywność roju dla tej trasy |
| Strona | A lub B, strona, z której przychodzi większość odbić |
| Najlepszy kierunek | Azymut radiantu ±90° |
| Wschód, Zachód | Wschód i zachód radiantu (UTC); *okołobiegunowy* lub *zawsze pod horyzontem*, gdy ma to zastosowanie |

Kliknij wiersz, aby wybrać rój: żółta linia dryfu i pomarańczowe kropki podążają za nim.

## Mała kopuła nieba (w środku po prawej)

Radianty na kopule nieba widzianej z twojej stacji, z ich **kodem IMO** i **dziennym torem w kolorze cyjanowym** (godziny UTC). **Kliknij radiant**, aby go wybrać. Kolory:

| Kolor | Znaczenie |
|---|---|
| Żółty | efektywność ≥ 50 % i ZHR ≥ 2 |
| Pomarańczowy | efektywność ≥ 20 % |
| Ciemnoczerwony | efektywność < 20 % |
| Szary | prawie nieaktywny |

Obok tekst obliczeń: długość i azymut trasy, punkt środkowy i jego elewacja, azymuty i odchylenia Hot A / Hot B, zalecany Hot (*… zalecany teraz: az. …° (…% oczekiwanych odbić)*), granice strefy wspólnej oraz przypomnienie: *najlepsze kierowanie anteny dla roju: PROSTOPADLE do kierunku nadejścia (azymut radiantu ±90°, tolerancja ±40–50°, SM6FHZ)*.

## Przekrój (na dole po prawej)

*PRZEKRÓJ – najbardziej prawdopodobne ślady widziane od strony anteny w kierunku stacji DX.* W poziomie **azymut względem stacji DX** (← A lewo, B → prawo), w pionie **elewacja**. Dla każdego roju brane jest 14 najsilniejszych punktów odbicia; każdy ślad to odcinek skierowany ku radiantowi, od 10 km powyżej do 10 km poniżej wysokości śladu (co najwyżej 60 km na stronę), grubszy, gdy jest bardziej prawdopodobny. Rysowane są także: listek anteny (okrąg −3 dB wokół elewacji listka), stacja DX oraz Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Wybór programu (podręcznik, wz. 35).*

## Ostrzeżenia

| Ostrzeżenie | Kiedy |
|---|---|
| **UWAGA: Hot A (i/lub Hot B) wypada wewnątrz listka anteny …** | Hot spot leży w granicach ±θ/2 od azymutu anteny (θ = poziomy listek −3 dB): przy tym kierunku jest już pokryty. Na mapie wyświetlany na szaro. Zalecany Hot pozostaje czerwony. |
| **RADIANT ZBYT WYSOKO (powyżej 70°)** | Użyteczny radiant znajduje się powyżej 70° nad twoją stacją: ślady spadają prawie pionowo i odbijają niewiele w stronę trasy (DF5HC, DH9GCD). Te same godziny są oznaczone ↑ w [tabeli godzinowej](Efficiency-Calculation-pl#tabela-godzinowa). |
| **NISKI RADIANT WZDŁUŻ TRASY** | Aktywny radiant jest poniżej 20° i w granicach 30° od kierunku trasy. Obliczona efektywność pozostaje niska (ostrożnie), ale DJ5HG spodziewa się rzadkich, silnych odbić od ślizgowych śladów ułożonych wzdłuż trasy (Hamburg–Narwik, Kwadrantydy, około 19 UTC): warto słuchać. |
| **TRASA POZA HORYZONTEM ŚLADÓW** | Na wysokości śladów punkt środkowy trasy jest poniżej horyzontu obu stacji (około 2120 km przy śladach na 90 km). Ostrzeżenie podaje minimalną potrzebną wysokość śladu (około 96 km dla 2200 km, 105 km dla 2300 km): łączność jest możliwa tylko przy najwyższych śladach, a efektywności i tłumienia są na granicy możliwości modelu |
| *Brak wspólnej strefy warstwy E* | Trasa jest dłuższa niż dwukrotność zasięgu na wysokości śladu: obie stacje nie widzą wspólnej części warstwy E (pojedynczy skok niemożliwy). |
| *Brak zalecanego Hot* | O tej porze prawie żaden rój nie jest aktywny. |

Wzór dla grafiki kopuły nieba: Swan Meteor Skyview autorstwa DL1DBC (swan.ms); wykres biegunowy z najlepszym kierunkiem: RadiantCalc autorstwa SM6FHZ.
