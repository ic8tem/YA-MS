LANGBAR

# Źródła

*Zakładka: Dokumenty techniczne › Źródła.*

[![Źródła](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Zakładka **Źródła** wymienia wszystkie prace, na których opiera się YA-MS, pogrupowane jak poniżej (tekst można zaznaczać, więc odnośniki da się skopiować). Te same źródła, ponumerowane, zamykają podręcznik obliczeń (`doc/YA-MS_manuale_calcoli.docx`) i dokument [Efektywność - wyjaśnienie](Efficiency-Explanation-pl).

## ŹRÓDŁO GŁÓWNE

| Źródło | Zastosowanie |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (artykuł po włosku, wersja 7) | Ślady w warstwie E na wysokości około 90 km (radar SKiYMET), promień Ziemi 6372,7955 km, wzór na elewację, Hot A / Hot B, side-scatter 10–30°, tłumienie trasy 182–200 dB, minimalny sygnał −130 dBm, czasy trwania pingów według IARU, maksimum sporadycznych o 06 UTC |

## OBLICZANIE I TEORIA EFEKTYWNOŚCI

| Źródło | Zastosowanie |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (strona historyczna) | Pojęcie efektywności roju; średnie tłumienie trasy 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Efektywność dla czterech stałych kierunków (porównanie) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 | Reguły λ³ i λ², punkt środkowy, najlepszy kierunek (az radiantu ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Odbicie zwierciadlane, równanie śladu podkrytycznego |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (za Kaiser & Closs 1952) | Minimalne tłumienie trasy 182 dB |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tabela przesunięć z AMS Bulletin 203) | Optymalna elewacja i przesunięcie, hot spoty 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (porównanie; w podręczniku) |
| Klaus von der Heide **DJ5HG** – QTFGUI i podręcznik „QTFGUI Help” (2007) | Prawo cone scattering; przypadek testowy Hamburg – Barcelona, Kwadrantydy, użyty do weryfikacji modelu |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, konferencja DARC, styczeń 2018 | Wzór na najlepszy kierunek autorstwa **DH9GCD**; cone scattering i wybór HOT-A / HOT-B według DJ5HG; użyteczny radiant 20–70°; najlepsza odległość 1300–1500 km; meteory sporadyczne według KB0VUK |
| Günter Hoch **DL6WU** – zysk w funkcji długości boomu długich anten Yagi, przytoczony przez W8IO (w8io.com) | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (anteny Yagi VK3AUU Davida Tannera) | Symulacje NEC użyte do weryfikacji krzywej zysku i korekty wiązki poziomej (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Szacunki zysku dla wariantów VK3AUU, WA2PHW i DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, wyd. 2, Willmann-Bell, 1998 | Data juliańska, czas gwiazdowy, długość ekliptyczna Słońca, azymut/elewacja (w podręczniku) |

## DANE ROJÓW

| Źródło | Zastosowanie |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (i 2027), www.imo.net, tabele 5, 6 i 7 | Radianty, λ max, v, r, ZHR, Źródło Antyhelionu, daty i godziny maksimów |
| Philip **G0ISW** – www.qsl.net/g0isw/g0iswms.htm | Maksymalne radiowe liczby godzinowe |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Dane rojów |

## DANE RADAROWE NA ŻYWO

| Źródło | Zastosowanie |
|---|---|
| Radar meteorowy Collm, Uniwersytet w Lipsku (LIM) i IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Godzinowy strumień meteorów i wysokości śladów ([Strumień radarowy](Radar-Flux-pl)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Obraz z liczbą meteorów |
| DL1DBC – Swan Meteor Skyview, swan.ms | Wzór dla grafiki sklepienia niebieskiego |
| SM6FHZ – RadiantCalc | Wykres biegunowy z najlepszym kierunkiem |
| Natural Earth – linie brzegowe i granice w skali 1:50 milionów, domena publiczna, www.naturalearthdata.com | Mapa Europy |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; biuletyny miesięczne rmob.org/rmobtext | Obserwatorzy GRAVES na 143,050 MHz (Planetarium w Wenecji, Faenza, Rovereto i inni) do porównania |

## RADAR GRAVES

| Źródło | Zastosowanie |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) oraz *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sektory, kroki, czasy kroków 0,8 s / 3,2 s |
| Wiki Bolidozor, "Graves" | Szyki antenowe, sektory i czasy wiązki |
| Wikipedia, "GRAVES (system)" | Nadajnik w Broye-lès-Pesmes (47,348° N 5,515° E) |

Zob. [Radar GRAVES](GRAVES-Radar-pl).

## INNE ODNOŚNIKI Z ARTYKUŁU

G3WZT, DH8BQA, geekshed.co.uk, podręcznik WSJT-X, WB2FKO (pingi), IU6GIR (aktywność na 143,050 MHz), IARU Region 1 VHF Handbook.

## Stałe wraz ze źródłami

`data/regole_sperimentali.csv` zawiera stałe i reguły używane przez program, każdą z jej źródłem (typowa wysokość śladów, zakres wysokości, promień Ziemi, reguły λ³ / λ², czasy trwania pingów według IARU, tłumienia trasy, minimalny sygnał, orientacyjne EIRP, maksimum sporadycznych, użyteczne odległości na 432 MHz, najlepszy kierunek, maksymalna użyteczna elewacja radiantu na 432 MHz, side-scatter).

> Dane radarowe należą do swoich instytucji. Przed automatycznym pobieraniem ich w rozpowszechnianym programie trzeba poprosić o zgodę.
