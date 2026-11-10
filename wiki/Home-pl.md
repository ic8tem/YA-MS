LANGBAR

# YA-MS – prognozy meteor scatter i efektywność rojów na żywo

*autor: Costantino Cerrotta IC8TEM*

**YA-MS** to darmowy program dla krótkofalowców pracujących przez **meteor scatter (MS) na 50, 70, 144, 222 i 432 MHz**. Dla rzeczywistej trasy między twoim lokatorem a lokatorem korespondenta oblicza godzina po godzinie, w jakim stopniu każdy aktywny rój meteorów sprzyja trasie (jego **efektywność**), z której strony trasy przychodzą odbicia (**Hot A / Hot B**), gdzie skierować antenę, a także eksperymentalną prognozę liczby odbić na godzinę, wyznaczoną na podstawie **radaru meteorowego na żywo** (Collm, Niemcy). Działa w systemach **Windows, Linux i macOS** (.NET 8 + Avalonia), w 36 językach interfejsu.

Głównym źródłem jest artykuł **C. Cerrotty IC8TEM i G. Sartoriego IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (wersja 7). Każdy wzór i każda dana w programie podaje swoje źródło; zob. [Źródła](Sources-pl).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Sklepienie niebieskie"></a><br><sub>Sklepienie niebieskie</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Obliczanie efektywności"></a><br><sub>Obliczanie efektywności</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Dla kogo

- Dla operatorów, którzy chcą wiedzieć, **kiedy** trasa meteor scatter jest otwarta i **gdzie** kierować antenę, a nie tylko ogólnikowe „rój ma dziś w nocy maksimum”.
- Dla stacji pracujących na **długich trasach na 144 i 432 MHz**, gdzie położenie radiantu decyduje, czy rój jest użyteczny, czy bezużyteczny.
- Dla każdego, kto chce **sprawdzić liczby**: podręcznik obliczeń i wyjaśnienie w programie podają każdy krok wraz z jego pochodzeniem: opublikowane źródło, sprawdzenie wykonane na programie albo wybór dokonany przez program.

## Zakładki

Od wersji 1.6 główne zakładki mają **podzakładki** (jaśniejszy wiersz pod głównym). Przy uruchomieniu przez 5 sekund wyświetla się ekran powitalny z Perseidami nad teleskopem VLT ESO (zdjęcie ESO/S. Guisard, CC BY 4.0).

| Zakładka | Podzakładka | Co pokazuje |
|---|---|---|
| **Na żywo i dane w czasie rzeczywistym** | [Ruch na żywo](Live-Traffic-pl) | Mapa azymutalna całego zebranego ruchu MS, z obłokiem najbardziej prawdopodobnych śladów dla każdej łączności, kolorami pasm i migającymi nowymi spotami |
| | [Strumień radarowy](Radar-Flux-pl) | Godzinowe liczby meteorów i wysokości śladów odczytane z radaru SKiYMET w Collm, obraz z Sodankylä, szacunek dla twojego pasma |
| | [Radar GRAVES](GRAVES-Radar-pl) | Trasa forward scatter GRAVES → ty: strefa użyteczna w wiązce, sektor i krok, następne przejście wiązki, jak słuchać |
| | [Zbieranie danych](Data-Collection-pl) | Trzy strumienie klastrów telnet (DX cluster, RBN, DM4X/PSKReporter) i filtr spotów MS |
| **Obliczenie prognozy** | [Obliczenie prognozy](Sky-View-pl) | Mapa trasy w rzucie z góry z Hot A / Hot B, wiązką anteny, strefami PREV i przesuwaniem się roju; lista rojów; małe sklepienie niebieskie z radiantami i właściwymi kierunkami anteny; przekrój widziany od strony anteny |
| | [Geometria i tłumienie](Geometry-and-Path-Loss-pl) | Odległość, punkt środkowy, elewacja, Hot A / Hot B, granice strefy wspólnej, tłumienie trasy 28–432 MHz, bilans łącza, antena |
| | [Obliczanie efektywności](Efficiency-Calculation-pl) | Karty podsumowania, godzinowa efektywność każdego roju ze stroną A/B, indeks trasy, porównanie z DH9GCD, wykres |
| | [Eksperymentalne prognozy](Experimental-Forecasts-pl) | Strumień z Collm przeliczony na 144 MHz (lub dowolną częstotliwość) z λ^k i współczynnikiem stacji K, prognoza 24-godzinna, porównanie z RMOB |
| **Dokumenty techniczne** | [Źródła](Sources-pl) | Wszystkie źródła; główne to artykuł Cerrotta–Sartori |
| | [Mapa radarów europejskich](European-Radar-Map-pl) | Gdzie znajdują się Collm, Sodankylä, GRAVES i CMOR względem twojej stacji |
| | [Efektywność - wyjaśnienie](Efficiency-Explanation-pl) | Dokument krok po kroku o tym, jak obliczana jest efektywność, z możliwością eksportu do Worda |
| [Roje na żywo](Live-Showers-pl) | – | Zmierzone ZHR z Global Meteor Network i mapy radiantów CMOR |
| [Roje](Showers-pl) | – | Katalog IMO z następnym maksimum (data i godzina według IMO lub obliczona) |
| [Mapa kwadratów](Grid-Square-Map-pl) | – | Zrobione i potwierdzone kwadraty Maidenhead z pliku ADIF, jedna zakładka na pasmo |

Nad zakładkami znajdują się trzy wiersze elementów sterujących (twój lokator, korespondent, pasmo, antena, wysokość śladów, czas); zob. [Pierwsze kroki](Getting-Started-pl). Przycisk **Sterowanie** je zwija, a język i schemat kolorów wybiera się w prawym górnym rogu; zob. [Ustawienia i folder danych](Settings-and-Data-Folder-pl).

## W skrócie

- **Rzeczywista trasa, a nie stałe kierunki**: efektywność jest obliczana dla trasy po ortodromie między dwoma lokatorami (starsze programy używały czterech stałych kierunków).
- **Model odbicia zwierciadlanego** (McKinley) w punktach warstwy E co 15 km, z wysokością śladów odczytywaną na żywo z radaru w Collm.
- **Hot A / Hot B** 150 km po obu stronach punktu środkowego (regulowane w zakresie 30–400 km); zalecany na czerwono, te, które już są wewnątrz wiązki twojej anteny, na szaro.
- **Radar na żywo**: Collm sprawdzany co 5 minut, ponownie pobierane są tylko zmienione źródła; bez sieci program działa dalej z ostatnio zapisanymi danymi.
- **Eksperymentalna** prognoza na 50/144/432 MHz z regułą λ³ SM6FHZ, porównywalna z obserwatorami RMOB.
- Wszystko w jednym folderze **`data`** obok programu: żadnego AppData, żadnych folderów systemowych.

> Efektywność to model eksperymentalny (odbicie zwierciadlane + ślady podkrytyczne). Porównuj ją z MCG_MS, MS-Soft i własnym doświadczeniem w eterze.

## Od czego zacząć

1. [Instalacja](Installation-pl)
2. [Pierwsze kroki](Getting-Started-pl)
3. [Rozwiązywanie problemów i FAQ](Troubleshooting-FAQ-pl), jeśli coś nie działa.

Pobieranie: **[Releases](https://github.com/ic8tem/YA-MS/releases)** na GitHubie.
