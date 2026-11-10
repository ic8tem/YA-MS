[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-BR) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · **Polski** · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-TW)

# Geometria i tłumienie trasy

*Zakładka: Obliczanie prognozy › Geometria i tłumienie trasy.*

[![Geometria i tłumienie trasy](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Tekstowy raport trasy (z możliwością zaznaczania, więc możesz go skopiować), a po prawej wykres **Elewacja anteny w funkcji odległości od punktu rozpraszania**. Liczby w nawiasach kwadratowych odsyłają do równań podręcznika obliczeń (`doc/YA-MS_manuale_calcoli.docx`).

## Dane wejściowe tej zakładki

| Pole | Domyślnie | Zastosowanie |
|---|---|---|
| **Moc W** | 400 | Moc nadajnika do bilansu łącza |
| **Zysk anteny dBi (tx = rx)** | 14 | Ta sama antena po obu stronach |
| **Minimalny sygnał dBm** | −130 | Minimalny wykrywalny sygnał (artykuł: Yagi 8-elementowa + przedwzmacniacz) |
| **Gęstość śladu q = 10^ … elektronów/m** | 14 | Liniowa gęstość elektronów śladu podgęstego |

Stacje, pasmo, wysokość śladu, elewacja listka, boom i odległość hot spotu pochodzą z [wierszy elementów sterujących](Getting-Started-pl#1-trzy-wiersze-elementów-sterujących).

## Sekcje raportu

| Sekcja | Zawartość |
|---|---|
| **GEOMETRIA TRASY (Ziemia kulista, R = 6372,7955 km)** | Stacja i DX z wysokościami; odległość, azymut i azymut odwrotny; punkt środkowy (lokator i współrzędne); wysokość śladu (*← dominanta zmierzona przez radar w Collm*, gdy pobrana z radaru); elewacja anteny w stronę punktu środkowego |
| **HOT A / HOT B (klasyczne hot spoty, do kierowania anteny)** | Dla każdego: lokator, azymut od ciebie i odchylenie od trasy bezpośredniej, azymut od DX, odległość, elewacja |
| **GRANICE STREFY WSPÓLNEJ** | Zasięg na wysokości śladu przy danej elewacji listka; Granica A / Granica B z azymutami |
| Antena | Boom w λ, zysk, listek poziomy / pionowy; czy Hot A i Hot B są wewnątrz, czy na zewnątrz listka |
| **TŁUMIENIE TRASY (ślad podgęsty, McKinley 1961; bez zysków anten)** | Tabela dla punktu środkowego (do przodu), Hot A i Hot B na 28, 50, 70, 144, 222 i 432 MHz |
| **BILANS ŁĄCZA NA … MHz (punkt środkowy)** | Moc i EIRP, tłumienie trasy, sygnał na antenie, minimalny wykrywalny, **zapas**; ten sam zapas przy średnim tłumieniu wg OH5IY |
| **REGUŁY EKSPERYMENTALNE MIĘDZY PASMAMI (SM6FHZ, VUSHF 2025)** | Liczba/natężenie i czas trwania w porównaniu ze 144 MHz; maksymalny ping wg IARU |

## Lokator i trasa

Lokator (4, 6 lub 8 znaków; środek kwadratu, system IARU Maidenhead) [14]. Odległość, azymut i punkt środkowy wg wzorów ortodromicznych na sferze o promieniu **r = 6372,7955 km** (artykuł Cerrotta–Sartori) [15–16]. Obliczenia zależne od czasu odnoszą się do **punktu środkowego**, ponieważ najlepsza pora może różnić się nawet o 1,5 godziny między oboma końcami trasy (SM6FHZ).

## Elewacja anteny

**Źródło:** wzór z artykułu Cerrotta–Sartori (rysunek 7), gdzie x = d/r, d to odległość po powierzchni do punktu odbicia, H wysokość śladu, a h wysokość stacji [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Sprawdzenie:** zgadza się z dokładną geometrią sferyczną z dokładnością do 0,03°. Program używa dwuargumentowego arcus tangensa, który daje wartości ujemne poza horyzontem i unika problemu okresowości wspomnianego w artykule. Ujemna elewacja w stronę punktu środkowego oznacza *trasę poza geometrycznym zasięgiem pojedynczego skoku*.

## Zasięg horyzontu

Odległość po powierzchni, na której promień o elewacji e osiąga wysokość H (geometryczna odwrotność powyższego wzoru) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Sprawdzenie:** H = 89,5 km, e = 0° → **1062 km**. W przykładzie z artykułu (JN44BB–IO53RT) rysunek umieszcza przecięcia z horyzontem około 870 km od stacji, co odpowiada listkowi podniesionemu o około 2° (865 km).

## Granice strefy wspólnej

**Źródło:** artykuł lokalizuje przecięcia krzywych, w których horyzont każdej ze stacji spotyka warstwę E: przecięcia dwóch okręgów o promieniu kątowym ρ = d_H/r o środkach w A i B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Jeśli 1 − |p0|² < 0, trasa jest dłuższa niż 2·d_H i stacje **nie widzą wspólnej strefy warstwy E**.

**Sprawdzenie:** są to **najdalsze krawędzie** nieba widzianego przez obie stacje, **a nie punkty, w które należy celować**. Na trasie JN70CN–IN78UO (1710 km, azymut 308°) wypadają 1062 km od stacji, 37° w lewo i w prawo od trasy bezpośredniej, podczas gdy MSHV sugeruje 10°. Dlatego nazywają się *Granica A* / *Granica B* i są rysowane na mapie blado.

## Hot A i Hot B

**Źródło:** odbicia od meteorów sporadycznych koncentrują się w dwóch strefach („hot spotach”) po obu stronach punktu środkowego. J. Richardson (AMS), w tabeli przytoczonej przez DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), podaje odchylenie anteny od kierunku bezpośredniego: **13° przy 1000 km, 11° przy 1250 km, 10° przy 1500 i 2000 km**. AMS Bulletin nr 203, przejęty przez W8WN, podaje 10° przy 1500 i 1800 km.

**Wybór:** Hot A i Hot B to punkty w odległości s od punktu środkowego M, prostopadle do trasy. Przy zaznaczonym *auto (AMS)* (domyślnie) s wynika z odchylenia z tabeli Richardsona, interpolowanego liniowo (13° poniżej 1000 km, 10° powyżej 2000 km): s = (D/2)·tan(odchylenie). Bez zaznaczenia s wpisuje się ręcznie, 30–400 km (MSHV używa 150 km); A po lewej, patrząc od twojej stacji w stronę DX, B po prawej [21]. Odchylenie widziane ze stacji wynosi około [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Sprawdzenie:** z tabelą AMS: 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, tyle samo co 150 km używane wcześniej i przez MSHV; na krótkich trasach tabela przybliża hot spoty do punktu środkowego.

## Tłumienie trasy dla śladu podgęstego

**Źródło:** równanie McKinleya i zalecenie ITU-R P.843 dla śladów podgęstych (sin α = 1), bez zysków anten; q = liniowa gęstość elektronów, r_e = klasyczny promień elektronu = 2,818·10⁻¹⁵ m, R1, R2 odległości od śladu, φ połowa kąta rozpraszania, β kąt między śladem a płaszczyzną trasy, a₁ współczynnik promienia początkowego, z r₀ w m i h w km (P.843, wz. 4 i 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Wybór:** bilans i tabela tłumienia używają β = 90° (ślad przecinający płaszczyznę trasy, przypadek najmniej korzystny: wartość ostrożna), a bilans pokazuje też przypadek najlepszy, β = 0. r₀ jest brane na średniej wysokości ech dla danej częstotliwości, h = 124 − 17 log f (P.843, wz. 15): 0,76 m na 95 km dla 50 MHz, 0,40 m na 87 km dla 144 MHz, 0,21 m na 79 km dla 432 MHz. Na 1000 km a₁ wynosi 0,2 dB na 50 MHz, 0,6 dB na 144 MHz i 1,4 dB na 432 MHz (2,9 dB na 600 km); przy stałych 102 km DJ5HG wynosiłby około 70 dB na 432 MHz, czyli żadnego echa.

**Sprawdzenie:** przy q = 10¹⁴ elektronów/m, śladach na 89,5 km i β = 0, na 144 MHz: **182–192 dB** między 600 a 2100 km (185 dB przy 1000 km), w zakresie **172–190 dB** obliczonym przez Johna Worsnopa **G4BAO** w jego pracy doktorskiej, jak podaje GM8JBJ. Przy β = 90° tłumienie rośnie o 10 dB przy 600 km, 13 dB przy 1000 km i 16 dB przy 2100 km; **średnie 200 dB** wg OH5IY leży między oboma przypadkami. 182 dB w tabeli GM8JBJ nie są potwierdzeniem: tabela nie podaje częstotliwości, jej 86,4 dB na odcinek to tłumienie wolnej przestrzeni na 500 km przy 1 MHz (brakuje członu 20 log f: 129,6 dB na 144 MHz), a jej pozycje sumują się do 163,8 dB, nie do 182; strona nie mówi ani o „minimum”, ani o „144 MHz”.

## Bilans łącza

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Zyski są wpisywane i używane w dBi: tłumienie McKinleya odnosi się do anten izotropowych, więc nie odejmuje się poprawki dipola 2,15 dB (EIRP = moc + zysk). Raport podaje też zapas przy **średnim tłumieniu trasy wg OH5IY** (200 dB na 144 MHz, przeskalowane z λ³ do wybranego pasma). Odniesienie z artykułu: potrzeba około **70 dBm EIRP** (−130 dBm + 200 dB, np. około 400 W do anteny 14 dBi).

## Zysk i listek anteny

**Zysk – źródło:** krzywa Güntera Hocha **DL6WU** dla długich anten Yagi w funkcji długości boomu L, przytoczona przez W8IO (ważna od około 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Sprawdzenie względem modeli NEC L.B. Cebika W4RNL na 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementy | Boom (λ) | W4RNL NEC (dBi) | Wzór (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Różnica nigdy nie przekracza **0,1 dB**: zysk zależy bardziej od długości boomu niż od konstrukcji (anteny Yagi VK3AUU mają krótszy boom przy tej samej liczbie elementów). Yagi Calculator autorstwa VK5DJ podaje także szacunki dla wariantów VK3AUU, WA2PHW i DJ9BV, których wzory nie zostały opublikowane.

**Listek – źródło:** reguła Krausa, z listkiem kołowym θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Sprawdzenie:** modele NEC W4RNL anten Yagi DL6WU dają **listek poziomy o 5–10 % węższy** niż według Krausa: 33,8° / 26,4° / 22,6° dla 12, 19 i 26 elementów, wobec 37,3° / 28,0° / 23,9°. Proste wzory pomijają przednie listki boczne (W4RNL, *Long-Boom Yagi Rules of Thumb*). Przy długich boomach listek pionowy jest nieco szerszy niż poziomy (14 λ: 18,4° / 18,8°).

**Wybór** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Przykład: Yagi 14 λ na 432 MHz → 20,3 dBi, listek 18,1° w poziomie i 19,5° w pionie; modele W4RNL dają 20,4 dBi oraz 18,4° / 18,8°. Są to reguły przybliżone, wyprowadzone z kilku anten DL6WU.

Zakłada się zawsze, że antena jest skierowana na DX. Hot spot leży **wewnątrz listka**, jeśli |Az(Hot) − Az(antena)| ≤ θ_poziomy/2: jest wtedy rysowany na szaro na [kopule nieba](Sky-View-pl) i pojawia się ostrzeżenie. W obliczeniach efektywności anteny są izotropowe; rzeczywisty listek służy tylko do tego sprawdzenia.

## Reguły eksperymentalne między pasmami

W porównaniu ze 144 MHz: liczba/natężenie × (144/f)³ (w dB), czas trwania × (144/f)² (SM6FHZ, VUSHF 2025). Maksymalny czas trwania pingu wg IARU Region 1: 1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz (VHF Handbook, cytowany w artykule). Zob. też [Prognozy eksperymentalne](Experimental-Forecasts-pl).
