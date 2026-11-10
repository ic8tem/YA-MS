[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-BR) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · **Polski** · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-TW)

# Obliczanie efektywności

*Zakładka: Obliczanie prognozy › Obliczanie efektywności.*

[![Obliczanie efektywności](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Efektywność** roju mówi, w procentach, w jakim stopniu położenie jego radiantu umożliwia odbicia na **twojej** trasie. Koncepcja pochodzi od Ilkki **OH5IY** (MS-Soft) i została przejęta w artykule Cerrotta–Sartori: maksimum efektywności nie pokrywa się z maksimum wizualnym (ZHR), ponieważ zależy od tego, gdzie znajduje się radiant względem obu stacji. MCG_MS autorstwa DL5MCG stosuje tę samą ideę do czterech stałych kierunków; YA-MS oblicza ją dla **rzeczywistej trasy** między dwoma lokatorami.

Ta zakładka pokazuje ją godzina po godzinie dla dnia wybranego w polu *Dzień dla tabeli 24 h (UTC)* (wartości w połowie każdej godziny).

## Karty podsumowania

| Karta | Zawartość |
|---|---|
| **NAJLEPSZA PORA DNIA** | Godzina z najwyższym indeksem trasy, wartość indeksu i przeważająca strona (A/B wraz z jej %) |
| **NAJKORZYSTNIEJSZY RÓJ** | Rój o największym iloczynie ZHR × efektywność w danym dniu, jego efektywność, godzina i strona oraz **najlepszy kierunek** (azymut radiantu +90° / −90°) |
| **TERAZ** | Indeks i przeważająca strona w bieżącej godzinie oraz zalecany Hot (tylko gdy wybrany dzień to dziś) |
| **PROGNOZA EKSPERYMENTALNA** | Oczekiwane odbicia/godzinę teraz, za 1 h i za 2 h na częstotliwości prognozy (Collm, reguły SM6FHZ; zob. [Prognozy eksperymentalne](Experimental-Forecasts-pl)) |

Pod kartami pasek objaśnia litery A i B (zob. niżej).

## Wykres

*Godzinowa efektywność dla … w dniu … (UTC, wartości w połowie godziny).* Dla maksymalnie pięciu rojów: efektywność % jako linia ciągła i wzór DH9GCD jako linia kropkowana w tym samym kolorze; **indeks trasy** jako niebieskie słupki na prawej skali.

## Tabela godzinowa

Jeden wiersz na każdy rój aktywny w danym dniu (posortowane wg ZHR), 24 kolumny dla godzin (UTC):

| Komórka | Znaczenie |
|---|---|
| `63A` | efektywność 63 %, większość odbić od strony **A** |
| `41B` | efektywność 41 %, strona **B** |
| `3` | efektywność poniżej 5 %: liczba bez litery strony |
| pusta | efektywność poniżej 1 % |
| `…↑` | radiant znajduje się **powyżej 70°** nad twoją stacją o tej godzinie (zbyt wysoko) |
| żółty tekst | efektywność ≥ 50 % |

- **A** = **lewo**, patrząc od twojej stacji w stronę stacji DX (strefa Hot A); **B** = **prawo** (strefa Hot B). Warto obrócić antenę o **10–30° w tę stronę** (side-scatter, artykuł Cerrotta–Sartori).
- **Jasnoniebieskie wiersze** (*DH9GCD %*, pod każdym rojem): wzór DH9GCD, dla porównania.
- **Wiersz Σ**: *Indeks trasy (ZHR×efekt.)*.
- **Pomarańczowy wiersz** (*Prognoza … MHz (odb./godz.)*): prognoza eksperymentalna, dla godzin, w których istnieje (dziś i część jutra).

## Model

Wszystkie kroki znajdują się w [podręczniku obliczeń](Efficiency-Explanation-pl) (`doc/YA-MS_manuale_calcoli.docx`, rozdział 5). W skrócie:

**1. Odbicie zwierciadlane.** Ślad przesyła sygnał z A do B tylko wtedy, gdy jest styczny do elipsoidy z A i B w ogniskach (McKinley 1961). Ślady roju są równoległe do kierunku radiantu ŝ (artykuł; McKinley). Dla każdego punktu P warstwy E, z wektorami jednostkowymi skierowanymi do stacji:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

To samo prawo leży u podstaw QTFGUI autorstwa DJ5HG i jego tekstu *"Die Geometrie von Meteorscatterverbindungen"* (2004): ślad rozprasza sygnał na stożku, którego osią jest ślad, i tylko odbiornik leżący na stożku go słyszy. Dla idealnego śladu ścianka stożka jest bardzo cienka (promiennik o długości tysięcy długości fali); program przyjmuje warunek z tolerancją gaussowską σ = 0,05 rad (około 3°), która reprezentuje to, czego idealny stożek nie uwzględnia: rozrzut radiantów roju (0,3–1,4° wg pomiarów GMN), ślady wygięte przez wiatr i ich skończoną długość – *wybór programu*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Waga każdego punktu.** Moc śladu podgęstego (McKinley; ITU-R P.843, wz. 3), φ = połowa kąta rozpraszania (ograniczona do 85°, *wybór*), β = kąt między śladem a płaszczyzną propagacji A-P-B, p̂ = wektor jednostkowy normalny do tej płaszczyzny:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opcja „Kąt β między śladem a trasą (pełny McKinley)”** (domyślnie włączona, ustawienie ostrożne). Włączona: ślady przecinające płaszczyznę propagacji są warte o 10–15 dB mniej niż te, które w niej leżą, więc żaden ślad nie jest przeszacowany. Wyłączona: każdy ślad jest ważony tak, jakby leżał w płaszczyźnie (β = 0, waga z cos²φ), jak do wersji 1.6. *Sprawdzenie:* na trasie 1000 km bez β najlepszy azymut radiantu leży 15°–90° od trasy, zależnie od elewacji radiantu (30° przy radiancie na 30°, prostopadle przy radiancie na 60°), a radiant prostopadły do trasy jest wart 67 % przy elewacji 30°; z β najlepszy radiant leży zawsze wzdłuż trasy, a prostopadły spada do 15 %. Z β traci się regułę najlepszego kierunku SM6FHZ / DH9GCD; β pozostaje opcją, domyślnie włączoną, bo daje najostrożniejsze wartości, a jej wyłączenie przywraca regułę.

Liczba meteorów docierających do punktu jest proporcjonalna do sinusa elewacji radiantu w tym punkcie (ŝ·û_P) – to ta sama poprawka, której IMO używa dla ZHR.

**Opcja „Dłuższe ślady przy niskim radiancie (DJ5HG)”** (pole wyboru nad wykresem, domyślnie wyłączone, z podpowiedzią): DJ5HG zauważa, że przy niskim radiancie na km² spada mniej meteorów, ale ślady są dłuższe (do 100 km użytecznej długości) i częściej spełniają prawo odbicia. Przy włączonej opcji waga staje się równa min(sin El, 15/100): użyteczna grubość warstwy, 15 km, podzielona przez sinus elewacji daje długość śladu, ograniczoną do 100 km. Powyżej około 9° oba efekty się znoszą. Przy wyłączonej opcji obliczenia pozostają ostrożne.

**Ustawienia obliczeń** (ten sam wiersz, przyciski opcji): **Ostrożne** (domyślne, najostrożniejsze wartości: wysokość śladu z radaru, normalne ślady, β włączone), **Jak DJ5HG** (102 km, dłuższe ślady, β) i **Własne**, wybierane automatycznie, gdy ręcznie zmienisz wysokość, pole *z radaru*, opcję dłuższych śladów lub β.

**3. Suma i procent.** Punkty co 15 km na wysokości śladu, tylko tam, gdzie obie stacje widzą je powyżej elewacji listka (*wybór*). 100 % to najkorzystniejsze położenie radiantu dla danej trasy:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F jest obliczane raz dla trasy na siatce kierunków (azymut co 5°, elewacja co 2,5°) i interpolowane.

**Efektywność w dB (odniesienie DJ5HG).** Procent odnosi się wyłącznie do najlepszego położenia radiantu dla danej trasy. Aby porównywać różne trasy, program podaje też efektywność w dB względem stałego odniesienia DJ5HG: 0 dB to maksimum dla trasy północ–południe o długości 1000 km przecinającej równik, z radiantem na równiku niebieskim w czasie równonocy, obliczone przy tej samej wysokości i tych samych wagach. DJ5HG podaje swoje wartości z dokładnością lepszą niż 6 dB.

**4. Strona i indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Litera w tabeli to strona o większym udziale. *Wybory programu (podręcznik, wz. 32–33).*

## Porównanie z DH9GCD

Źródłami pierwotnymi dotyczącymi najlepszego kierunku są Eshleman & Mlodnosky oraz Meeks & James (Proc. IRE, 1957), Hines (1955) i jego eksperymentalna weryfikacja przez Forsytha, Hinesa i Vogana (1955): użyteczne są tylko radianty leżące na półokręgu nieba prostopadłym do dwusiecznej kąta rozpraszania, liczba śladów rośnie z sin El, a w pobliżu punktu środkowego użyteczne ślady wypadają w odległości około H·tan El z boku, po stronie przeciwnej do radiantu. DJ5HG dodaje zastrzeżenie: przy **niskim** radiancie leżącym dokładnie wzdłuż trasy wzór McKinleya daje silne sygnały (Hamburg–Narwik, Kwadrantydy, około 19 UTC), więc zasada „radiant w linii trasy = prawie zero” obowiązuje tylko dla wysokiego radiantu; program pozostaje ostrożny i wyświetla ostrzeżenie *NISKI RADIANT WZDŁUŻ TRASY*.

Niezależne sprawdzenie: wzór na najlepszy kierunek autorstwa **DH9GCD**, przytoczony przez **DF5HC** (konferencja DARC, styczeń 2018) – nie ma opublikowanego źródła pierwotnego – gdzie El i Az to elewacja i azymut radiantu widziane z twojej stacji, a P to azymut stacji DX:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Osiąga maksimum przy radiancie na 45° i prostopadłym do trasy. DF5HC uważa radiant za zbyt niski poniżej 20° i **zbyt wysoki powyżej 70°**: te godziny otrzymują ↑ w tabeli i ostrzeżenie na [kopule nieba](Sky-View-pl#ostrzeżenia). Wzór pomija odległość i wysokości, ale jest dobrym punktem odniesienia.

## Weryfikacje

| Weryfikacja | Wynik |
|---|---|
| Reguła SM6FHZ (VUSHF 2025): najlepsza trasa prostopadła do azymutu radiantu, kierunek = azymut radiantu ±90°, tolerancja ±40–50° | Odtworzona przez model; gdy radiant leży w linii trasy i wysoko na niebie, efektywność jest prawie zerowa |
| QTFGUI autorstwa DJ5HG, Hamburg JO53IM – Barcelona, Kwadrantydy, 4 stycznia (przykład z jego podręcznika) | QTFGUI: 07:00 kierunek 252°, −8 dB; 08:00 brak strefy odbić; 09:00 kierunek 168°, −4 dB. YA-MS (wysokość 102 km jak w QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Wszystkie trzy metody widzą dziurę o 08:00, gdy radiant jest prawie w zenicie |
| Krzywe DJ5HG (*Die Geometrie…*, Bild 8–9: z Hamburga i Monachium, Kwadrantydy, 4 stycznia; odczytane z wykresu, około ±0,5 dB i ±15 min) w porównaniu z testem automatycznym `--prova-dj5hg` (jedna wartość na godzinę) | Czas: dziura przy radiancie w pobliżu zenitu wypada w tych samych godzinach (Barcelona 07:30–08:30 wobec 07–09; Sofia 06:36–07:48 wobec 07–08; Narwik 07–08:30 wobec 07–09); Moskwa jest zamknięta 03–10 w obu przypadkach, otwarta z Hamburga do około 02:30, a z Monachium do około 00:30, jak pisze DJ5HG. Kierunki: różnica 2–10°. Poziomy i kształt przy 102 km (średnia i RMS różnicy względem krzywych): bez β, bez dłuższych śladów −1,6 / 4,0 dB; dłuższe ślady +1,1 / 4,6 dB; β −5,4 / 6,2 dB, ale z najlepszym kształtem (3,0 dB po odjęciu średniej, wobec 3,6): pojawiają się głębokie minima przy niskim radiancie (Barcelona −15,6 dB o 17 wobec −16 dB o 19:36; Sofia −18,5 dB o 20 wobec −14 dB). β i dłuższe ślady (*Jak DJ5HG*) −2,2 / 4,7 dB; ustawienie ostrożne (wysokość z radaru 89,5 km, β włączone, bez dłuższych śladów) −6,9 / 7,6 dB, kształt 3,3 dB. Bez β YA-MS ledwie pokazuje minimum przy radiancie niskim i prawie w linii trasy (−8,6 i −10,4 dB): to jest właśnie zastrzeżenie samego DJ5HG, stąd ostrzeżenie |
| Próbkowanie co 5 km zamiast co 15 km | procenty zmieniają się o mniej niż 0,3 punktu |

> Dokumentacja MS-Soft 5.2 definiuje efektywność OH5IY jako względny indeks wyłącznie dla śladów podgęstych, z dwoma czynnikami (elewacja radiantu, najlepsza około 45°, i kąt względem trasy, najlepszy 90°) oraz minimum podniesionym ręcznie do 20 % dla śladów nadgęstych; wzór nie został opublikowany. MCG_MS oblicza ją dla czterech stałych kierunków oraz, przy podanym lokatorze DX, dla rzeczywistej trasy. Model uwzględnia wyłącznie ślady podgęste, z antenami izotropowymi; rozbłyski nadgęste i tło sporadyczne nie wchodzą do efektywności (tło sporadyczne reprezentuje strumień radarowy).
