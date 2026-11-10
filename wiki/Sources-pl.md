[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-BR) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · **Polski** · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-TW)

# Źródła

*Zakładka: Dokumenty techniczne › Źródła.*

[![Źródła](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

Zakładka **Źródła** wymienia wszystkie prace, na których opiera się YA-MS, pogrupowane jak poniżej (tekst można zaznaczać, więc możesz skopiować odnośniki). Te same źródła, ponumerowane, zamykają podręcznik obliczeń (`doc/YA-MS_manuale_calcoli.docx`) oraz dokument [Efektywność - objaśnienie](Efficiency-Explanation-pl).

## GŁÓWNE ŹRÓDŁO

| Źródło | Zastosowanie |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* („METEOR-SCATTER, czyli jak łączyć się z Europą na VHF przez cały rok bez wielkich wymagań”; artykuł po włosku, wersja 7) | Ślady w warstwie E na około 90 km (radar SKiYMET), promień Ziemi 6372,7955 km, wzór na elewację, Hot A / Hot B, side-scatter 10–30°, tłumienie trasy, minimalny sygnał −130 dBm, czasy trwania pingów wg IARU, maksimum meteorów sporadycznych o 06 UTC |

## EFEKTYWNOŚĆ: OBLICZENIA I TEORIA

| Źródło | Zastosowanie |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (strona historyczna) | Koncepcja efektywności roju; średnie tłumienie trasy 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Efektywność dla czterech stałych kierunków (porównanie) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 | Reguły λ³ i λ², punkt środkowy, najlepszy kierunek (azymut radiantu ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Odbicie zwierciadlane, równanie śladu podgęstego |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (na podstawie Kaiser & Closs 1952) | Tłumienie trasy 172–190 dB obliczone przez Johna Worsnopa **G4BAO** (praca doktorska), o około 6 dB mniej dla śladów ułożonych wzdłuż trasy; własna tabela 182 dB z tej strony nie jest używana (zob. [Geometria i tłumienie trasy](Geometry-and-Path-Loss-pl)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tabela odchyleń z AMS Bulletin 203) | Optymalna elewacja i odchylenie, hot spoty 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (porównanie; w podręczniku) |
| Klaus von der Heide **DJ5HG** – QTFGUI i podręcznik "QTFGUI Help" (2007) | Prawo rozpraszania stożkowego; przypadek testowy Hamburg – Barcelona, Kwadrantydy, użyty do weryfikacji modelu |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, konferencja DARC, styczeń 2018 | Wzór na najlepszy kierunek autorstwa **DH9GCD**; rozpraszanie stożkowe i wybór HOT-A / HOT-B wg DJ5HG; użyteczny radiant 20–70°; najlepsza odległość 1300–1500 km; meteory sporadyczne wg KB0VUK |
| Günter Hoch **DL6WU** – zysk w funkcji długości boomu długich anten Yagi, przytoczone przez W8IO (w8io.com) | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (anteny Yagi VK3AUU autorstwa Davida Tannera) | Symulacje NEC użyte do weryfikacji krzywej zysku i korekty listka poziomego (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Szacunki zysku dla wariantów VK3AUU, WA2PHW i DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, wyd. 2, Willmann-Bell, 1998 | Dzień juliański, czas gwiazdowy, długość ekliptyczna Słońca, azymut/elewacja (w podręczniku) |

## DANE ROJÓW

| Źródło | Zastosowanie |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (i 2027), www.imo.net, tabele 5, 6 i 7 | Radianty, λ max, v, r, ZHR, Antihelion Source, daty i godziny maksimów |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Dane rojów |

## DANE RADAROWE NA ŻYWO

| Źródło | Zastosowanie |
|---|---|
| Radar meteorowy w Collm, Uniwersytet w Lipsku (LIM) i IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Godzinowy strumień meteorów i wysokości śladów ([Strumień radarowy](Radar-Flux-pl)) |
| Obserwatorium Geofizyczne Sodankylä – sgo.fi/Data/RealTime/meteorRadar.php | Obraz zliczeń meteorów |
| DL1DBC – Swan Meteor Skyview, swan.ms | Wzór dla grafiki kopuły nieba |
| SM6FHZ – RadiantCalc | Wykres biegunowy z najlepszym kierunkiem |
| Natural Earth – linie brzegowe i granice w skali 1:50 mln, domena publiczna, www.naturalearthdata.com | Mapa Europy |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; biuletyny miesięczne rmob.org/rmobtext | Obserwatorzy GRAVES na 143,050 MHz (Planetarium w Wenecji, Faenza, Rovereto i inni) do porównań |

## RADAR GRAVES

| Źródło | Zastosowanie |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) oraz *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sektory, kroki, taktowanie kroków 0,8 s / 3,2 s |
| Wiki Bolidozor, "Graves" | Szyki antenowe, sektory i taktowanie wiązki |
| Wikipedia, "GRAVES (system)" | Nadajnik w Broye-lès-Pesmes (47,348° N 5,515° E) |

Zob. [Radar GRAVES](GRAVES-Radar-pl).

## INNE ODNIESIENIA Z ARTYKUŁU

G3WZT, DH8BQA, geekshed.co.uk, podręcznik WSJT-X, WB2FKO (pingi), IU6GIR (aktywność na 143,050 MHz), IARU Region 1 VHF Handbook.

## Stałe wraz ze źródłami

`data/regole_sperimentali.csv` zawiera stałe i reguły używane przez program, każdą ze swoim źródłem (typowa wysokość śladu, zakres wysokości, promień Ziemi, reguły λ³ / λ², czasy trwania pingów wg IARU, tłumienia trasy, minimalny sygnał, orientacyjne EIRP, maksimum meteorów sporadycznych, użyteczne odległości na 432 MHz, najlepszy kierunek, maksymalna użyteczna elewacja radiantu na 432 MHz, side-scatter).

> Dane radarowe należą do swoich instytucji. Przed ich automatycznym pobieraniem w rozpowszechnianym programie należy poprosić o zgodę.
