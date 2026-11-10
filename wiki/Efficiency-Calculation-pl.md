[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · **Polski** · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Obliczanie efektywności

*Zakładka: Obliczenie prognozy › Obliczanie efektywności.*

[![Obliczanie efektywności](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Efektywność** roju mówi, w procentach, na ile położenie jego radiantu umożliwia odbicia na **twojej** trasie. Pojęcie pochodzi od Ilkki **OH5IY** (MS-Soft) i zostało przejęte w artykule Cerrotta–Sartori: maksimum efektywności nie pokrywa się z maksimum wizualnym (ZHR), ponieważ zależy od tego, gdzie znajduje się radiant względem obu stacji. MCG_MS autorstwa DL5MCG stosuje tę samą ideę do czterech stałych kierunków; YA-MS oblicza ją dla **rzeczywistej trasy** między dwoma lokatorami.

Ta zakładka pokazuje ją godzina po godzinie dla dnia wybranego w polu *Dzień dla tabeli 24 h (UTC)* (wartości w połowie każdej godziny).

## Karty podsumowania

| Karta | Zawartość |
|---|---|
| **NAJLEPSZA PORA DNIA** | Godzina z najwyższym indeksem trasy, ten indeks i przeważająca strona (A/B z jej %) |
| **NAJKORZYSTNIEJSZY RÓJ** | Rój z największym ZHR × efektywność w danym dniu, jego efektywność, godzina i strona oraz **najlepszy kierunek** (azymut radiantu +90° / −90°) |
| **TERAZ** | Indeks i przeważająca strona o tej godzinie oraz zalecany Hot (tylko gdy wybrany dzień jest dzisiejszy) |
| **PROGNOZA EKSPERYMENTALNA** | Oczekiwane odbicia/godz. teraz, za 1 h i za 2 h przy częstotliwości prognozy (Collm, reguły SM6FHZ; zob. [Eksperymentalne prognozy](Experimental-Forecasts-pl)) |

Pod kartami pasek objaśnia litery A i B (zob. niżej).

## Wykres

*Efektywność godzinowa dla … w dniu … (UTC, wartości w połowie godziny).* Dla maksymalnie pięciu rojów: efektywność % jako linia ciągła i wzór DH9GCD jako linia kropkowana w tym samym kolorze; **indeks trasy** jako niebieskie słupki na prawej skali.

## Tabela godzinowa

Jeden wiersz na każdy rój aktywny w danym dniu (posortowane według ZHR), 24 kolumny na godziny (UTC):

| Komórka | Znaczenie |
|---|---|
| `63A` | efektywność 63 %, większość odbić ze strony **A** |
| `41B` | efektywność 41 %, strona **B** |
| `3` | efektywność poniżej 5 %: liczba bez litery strony |
| pusta | efektywność poniżej 1 % |
| `…↑` | radiant jest o tej godzinie **wyżej niż 70°** nad twoją stacją (za wysoko) |
| żółty tekst | efektywność ≥ 50 % |

- **A** = **po lewej**, patrząc ze swojej stacji w stronę korespondenta (strefa Hot A); **B** = **po prawej** (strefa Hot B). Warto obrócić antenę **o 10–30° w tę stronę** (side-scatter, artykuł Cerrotta–Sartori).
- **Jasnoniebieskie wiersze** (*DH9GCD %*, pod każdym rojem): wzór DH9GCD, dla porównania.
- **Wiersz Σ**: *Indeks trasy (ZHR×efekt.)*.
- **Pomarańczowy wiersz** (*Prognoza … MHz (odb./godz.)*): prognoza eksperymentalna, dla godzin, dla których istnieje (dziś i część jutra).

## Model

Wszystkie kroki są w [podręczniku obliczeń](Efficiency-Explanation-pl) (`doc/YA-MS_manuale_calcoli.docx`, rozdział 5). W skrócie:

**1. Odbicie zwierciadlane.** Ślad przesyła sygnał z A do B tylko wtedy, gdy jest styczny do elipsoidy z A i B w ogniskach (McKinley 1961). Ślady roju są równoległe do kierunku radiantu ŝ (artykuł; McKinley). Dla każdego punktu P warstwy E, z wektorami jednostkowymi skierowanymi do stacji:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

To samo prawo leży u podstaw QTFGUI autorstwa DJ5HG (cone scattering). Warunek jest przyjmowany z tolerancją gaussowską σ = 0,05 rad (około 3°) – *wybór programu*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Waga każdego punktu.** Moc śladu podkrytycznego (McKinley), φ = połowa kąta rozpraszania (ograniczona do 85°, *wybór*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Liczba meteorów docierających do punktu jest proporcjonalna do sinusa elewacji radiantu w tym miejscu (ŝ·û_P) – to ta sama poprawka, której IMO używa dla ZHR.

**3. Suma i wartość procentowa.** Punkty co 15 km na wysokości śladów, tylko tam, gdzie obie stacje widzą je powyżej elewacji wiązki (*wybór*). 100 % to najkorzystniejsze położenie radiantu dla danej trasy:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F jest obliczane raz dla każdej trasy na siatce kierunków (azymut co 5°, elewacja co 2,5°) i interpolowane.

**4. Strona i indeks.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Litera w tabeli to strona z większym udziałem. *Wybory programu (podręcznik, wz. 32–33).*

## Porównanie z DH9GCD

Niezależne sprawdzenie: wzór na najlepszy kierunek autorstwa **DH9GCD**, przytoczony przez **DF5HC** (konferencja DARC, styczeń 2018), gdzie El i Az to elewacja i azymut radiantu widziane z twojej stacji, a P to azymut korespondenta:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Osiąga maksimum, gdy radiant jest na 45° i prostopadle do trasy. DF5HC uważa radiant za zbyt nisko poniżej 20° i **za wysoko powyżej 70°**: te godziny dostają w tabeli ↑ i ostrzeżenie na [Sklepieniu niebieskim](Sky-View-pl#ostrzeżenia). Wzór pomija odległość i wysokości, ale jest dobrym punktem odniesienia.

## Sprawdzenia

| Sprawdzenie | Wynik |
|---|---|
| Reguła SM6FHZ (VUSHF 2025): najlepsza trasa prostopadła do azymutu radiantu, kierunek = az radiantu ±90°, tolerancja ±40–50° | Odtworzona przez model; gdy radiant leży w linii trasy i wysoko na niebie, efektywność jest prawie zerowa |
| QTFGUI autorstwa DJ5HG, Hamburg JO53IM – Barcelona, Kwadrantydy, 4 stycznia (przykład z jego podręcznika) | QTFGUI: 07:00 kierunek 252°, −8 dB; 08:00 brak strefy odbicia; 09:00 kierunek 168°, −4 dB. YA-MS (wysokość 102 km jak w QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Wszystkie trzy metody widzą dziurę o 08:00, gdy radiant jest prawie w zenicie |
| Próbkowanie co 5 km zamiast co 15 km | wartości procentowe zmieniają się o mniej niż 0,3 punktu |

> Skala używana przez OH5IY i MCG_MS nie jest znana w szczegółach (podręczniki MS-Soft nie są dostępne): porównaj wartości procentowe z tymi programami, zanim uznasz je za równoważne. Model uwzględnia tylko ślady podkrytyczne, z antenami izotropowymi; rozbłyski od śladów nadkrytycznych i tło sporadyczne nie wchodzą w efektywność (tło sporadyczne reprezentuje strumień radarowy).
