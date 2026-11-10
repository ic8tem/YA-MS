LANGBAR

# Geometria i tłumienie

*Zakładka: Obliczenie prognozy › Geometria i tłumienie.*

[![Geometria i tłumienie](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Tekstowy raport trasy (z możliwością zaznaczania, więc można go skopiować), a po prawej wykres **Elewacja anteny w funkcji odległości od punktu rozpraszania**. Liczby w nawiasach kwadratowych odsyłają do równań podręcznika obliczeń (`doc/YA-MS_manuale_calcoli.docx`).

## Dane wejściowe tej zakładki

| Pole | Domyślnie | Zastosowanie |
|---|---|---|
| **Moc W** | 400 | Moc nadajnika do bilansu łącza |
| **Zysk anteny dBi (tx = rx)** | 14 | Ta sama antena na obu końcach |
| **Minimalny sygnał dBm** | −130 | Minimalny wykrywalny sygnał (artykuł: Yagi 8-elementowa + przedwzmacniacz) |
| **Gęstość śladu q = 10^ … elektronów/m** | 14 | Liniowa gęstość elektronów śladu podkrytycznego |

Stacje, pasmo, wysokość śladów, elewacja wiązki, boom i odległość hot spotów pochodzą z [wierszy elementów sterujących](Getting-Started-pl#1-trzy-wiersze-elementów-sterujących).

## Sekcje raportu

| Sekcja | Zawartość |
|---|---|
| **GEOMETRIA TRASY (Ziemia sferyczna, R = 6372,7955 km)** | Stacja i korespondent z wysokościami; odległość, azymut i azymut odwrotny; punkt środkowy (lokator i współrzędne); wysokość śladów (*<- dominanta zmierzona przez radar Collm*, gdy pobrana z radaru); elewacja anteny w stronę punktu środkowego |
| **HOT A / HOT B (klasyczne hot spoty, do ustawiania anteny)** | Dla każdego: lokator, azymut od ciebie i przesunięcie względem trasy bezpośredniej, azymut od korespondenta, odległość, elewacja |
| **GRANICE STREFY WSPÓLNEJ** | Zasięg na wysokości śladów przy danej elewacji wiązki; Granica A / Granica B z azymutami |
| Antena | Boom w λ, zysk, wiązka pozioma / pionowa; czy Hot A i Hot B są wewnątrz, czy poza wiązką |
| **TŁUMIENIE TRASY (ślad podkrytyczny, McKinley 1961; bez zysków anten)** | Tabela dla punktu środkowego (forward), Hot A i Hot B na 28, 50, 70, 144, 222 i 432 MHz |
| **BILANS ŁĄCZA PRZY … MHz (punkt środkowy)** | Moc i EIRP, tłumienie trasy, sygnał na antenie, minimalny wykrywalny, **zapas**; ten sam zapas przy średnim tłumieniu według OH5IY |
| **REGUŁY EKSPERYMENTALNE MIĘDZY PASMAMI (SM6FHZ, VUSHF 2025)** | Liczba/natężenie i czas trwania w porównaniu z 144 MHz; maksymalny ping według IARU |

## Lokator i trasa

Lokator (4, 6 lub 8 znaków; środek kwadratu, system IARU Maidenhead) [14]. Odległość, azymut i punkt środkowy ze wzorów ortodromicznych na sferze o promieniu **r = 6372,7955 km** (artykuł Cerrotta–Sartori) [15–16]. Obliczenia zależne od czasu odnoszą się do **punktu środkowego**, ponieważ najlepsza pora może się różnić nawet o 1,5 godziny między oboma końcami (SM6FHZ).

## Elewacja anteny

**Źródło:** wzór z artykułu Cerrotta–Sartori (rysunek 7), gdzie x = d/r, d to odległość po powierzchni do punktu odbicia, H to wysokość śladów, a h to wysokość stacji [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Sprawdzenie:** zgadza się z dokładną geometrią sferyczną z dokładnością do 0,03°. Program używa arcus tangensa z dwoma argumentami, który daje wartości ujemne poza horyzontem i pozwala uniknąć problemu okresowości wspomnianego w artykule. Ujemna elewacja w stronę punktu środkowego oznacza *trasę poza zasięgiem geometrycznym pojedynczego skoku*.

## Zasięg horyzontu

Odległość po powierzchni, na której promień o elewacji e osiąga wysokość H (geometryczna odwrotność powyższego wzoru) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Sprawdzenie:** H = 89,5 km, e = 0° → **1062 km**. W przykładzie z artykułu (JN44BB–IO53RT) rysunek umieszcza przecięcia horyzontu około 870 km od stacji, co odpowiada wiązce podniesionej o około 2° (865 km).

## Granice strefy wspólnej

**Źródło:** artykuł wyznacza przecięcia krzywych, w których horyzont każdej ze stacji spotyka warstwę E: przecięcia dwóch okręgów o promieniu kątowym ρ = d_H/r ze środkami w A i B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Jeśli 1 − |p0|² < 0, trasa jest dłuższa niż 2·d_H, a stacje **nie widzą wspólnej strefy warstwy E**.

**Sprawdzenie:** są to **najdalsze krawędzie** nieba widzianego przez obie stacje, **a nie punkty, na które należy celować**. Na trasie JN70CN–IN78UO (1710 km, azymut 308°) wypadają 1062 km od stacji, 37° na lewo i na prawo od trasy bezpośredniej, podczas gdy MSHV sugeruje 10°. Dlatego nazywają się *Granica A* / *Granica B* i są rysowane na mapie blado.

## Hot A i Hot B

**Źródło:** odbicia skupiają się w dwóch strefach („hot spotach”) około **50–150 km po obu stronach punktu środkowego**. To podstawa tabeli przesunięć anteny z AMS Bulletin nr 203, przejętej przez W8WN (przesunięcie 10° dla tras 1500 i 1800 km); MSHV autorstwa LZ2HV stosuje to samo kryterium.

**Wybór:** Hot A i Hot B to punkty w odległości s od punktu środkowego M, prostopadle do trasy (s = 150 km, regulowane w zakresie 30–400 km); A po lewej, patrząc od twojej stacji w stronę DX, B po prawej [21]. Przesunięcie widziane ze stacji wynosi w przybliżeniu [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Sprawdzenie:** JN70CN–IN78UO, D = 1710 km: 6,7° przy s = 100 km, **10,0° przy s = 150 km** (tak samo jak MSHV i AMS/W8WN), 13,2° przy s = 200 km.

## Tłumienie trasy dla śladów podkrytycznych

**Źródło:** równanie McKinleya dla śladów podkrytycznych (β = 0, sin α = 1), bez zysków anten; q = liniowa gęstość elektronów, r_e = klasyczny promień elektronu = 2,818·10⁻¹⁵ m, R1, R2 odległości od śladu, φ połowa kąta rozpraszania [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Sprawdzenie:** przy q = 10¹⁴ elektronów/m na 144 MHz: **181–192 dB** między 600 a 2200 km, zgodnie z odniesieniami z artykułu dla 144 MHz: **minimum 182 dB** (GM8JBJ, za Kaiser & Closs 1952) i **średnio 200 dB** (OH5IY).

## Bilans łącza

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Zyski wprowadza się w dBi i używa w dBd (dBi − 2,15). Raport podaje też zapas przy **średnim tłumieniu trasy według OH5IY** (200 dB na 144 MHz, przeskalowane z λ³ na wybrane pasmo). Odniesienie z artykułu: potrzeba około **70 dBm EIRP** (−130 dBm + 200 dB, np. około 400 W do anteny 14 dBi).

## Zysk i wiązka anteny

**Zysk – źródło:** krzywa Güntera Hocha **DL6WU** dla długich anten Yagi w funkcji długości boomu L, przytoczona przez W8IO (ważna od około 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Sprawdzenie z modelami NEC L.B. Cebika W4RNL na 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementy | Boom (λ) | W4RNL NEC (dBi) | Wzór (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Różnica nigdy nie przekracza **0,1 dB**: zysk zależy bardziej od długości boomu niż od konstrukcji (anteny Yagi VK3AUU mają krótszy boom przy tej samej liczbie elementów). Yagi Calculator autorstwa VK5DJ podaje też szacunki dla wariantów VK3AUU, WA2PHW i DJ9BV, których wzory nie są opublikowane.

**Wiązka – źródło:** reguła Krausa, przy wiązce kołowej θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Sprawdzenie:** modele NEC W4RNL anten Yagi DL6WU dają **wiązkę poziomą o 5–10 % węższą** niż według Krausa: 33,8° / 26,4° / 22,6° dla 12, 19 i 26 elementów, wobec 37,3° / 28,0° / 23,9°. Proste wzory pomijają przednie listki boczne (W4RNL, *Long-Boom Yagi Rules of Thumb*). Przy długich boomach wiązka pionowa jest nieco szersza niż pozioma (14 λ: 18,4° / 18,8°).

**Wybór** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Przykład: Yagi 14 λ na 432 MHz → 20,3 dBi, wiązka 18,1° w poziomie i 19,5° w pionie; modele W4RNL dają 20,4 dBi i 18,4° / 18,8°. Są to reguły przybliżone, wyprowadzone z kilku anten DL6WU.

Antena jest zawsze uważana za skierowaną na DX. Hot spot jest **wewnątrz wiązki**, jeśli |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: jest wtedy rysowany na szaro na [Sklepieniu niebieskim](Sky-View-pl) i pojawia się ostrzeżenie. W obliczaniu efektywności anteny są izotropowe; rzeczywista wiązka jest używana tylko do tego sprawdzenia.

## Reguły eksperymentalne między pasmami

W porównaniu z 144 MHz: liczba/natężenie × (144/f)³ (w dB), czas trwania × (144/f)² (SM6FHZ, VUSHF 2025). Maksymalny czas trwania pingów według IARU Region 1: 1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz (VHF Handbook, cytowany w artykule). Zob. też [Eksperymentalne prognozy](Experimental-Forecasts-pl).
