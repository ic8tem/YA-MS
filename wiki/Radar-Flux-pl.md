[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · **Polski** · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Strumień radarowy

*Zakładka: Dane na żywo i w czasie rzeczywistym › Strumień radarowy.*

[![Strumień radarowy](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Ta zakładka pokazuje, co profesjonalne radary meteorowe liczą **teraz**: godzinowe zliczenia meteorów i wysokości śladów z radaru SKiYMET w **Collm** (Uniwersytet w Lipsku / IAP Kühlungsborn, Niemcy, 36,2 MHz) oraz najnowszy obraz z radaru w **Sodankylä** (SGO, Finlandia). Zliczenia z Collm zasilają szacunek dla twojego pasma i [Prognozy eksperymentalne](Experimental-Forecasts-pl); zmierzona wysokość śladów zasila całą geometrię.

## Elementy sterujące

| Element | Działanie |
|---|---|
| **Pobierz teraz** | Sprawdza od razu wszystkie źródła zewnętrzne. |
| **Automatyczna aktualizacja wszystkich źródeł co 5 minut** | Domyślnie włączona. Co 5 minut sprawdzane są wszystkie źródła i ponownie pobierane są **tylko te, które się zmieniły** (*bez zmian (sprawdzono o … UTC)* / *nowe dane o … UTC*). |
| **Wykładnik λ (SM6FHZ)** | Wykładnik k reguły częstotliwościowej, domyślnie 3 (1–4). |

## Co jest wyświetlane

| Panel | Zawartość |
|---|---|
| **Meteory/godzinę – wczoraj i dziś (UTC)** | Słupki cyjanowe = zliczenia z Collm (ważne), słupki czerwone = odrzucone, gruba pomarańczowa linia = *szacunek na … MHz* na prawej skali |
| **Wysokości śladów (Collm)** | Meteory na km wysokości między 70 a 110 km, z najczęstszą wysokością (dominantą), średnią, medianą i odchyleniem standardowym |
| Obraz z Collm | Oryginalny wykres SKiYMET, w postaci pobranej |
| Obraz z Sodankylä | Najnowszy obraz zliczeń meteorów z radaru w Sodankylä (tylko wyświetlany; jego format nie jest odczytywany) |

Wiersz nad wykresami informuje, kiedy wykres z Collm został odczytany i jaką skalę pionową znaleziono (*skala odczytana z wykresu: 0-… meteorów/godzinę*).

## Jak odczytywany jest wykres z Collm

Wykres z Collm (720 × 720 pikseli, czyste kolory) ma stałe położenie osi, ale radar **codziennie dostosowuje skalę pionową** do zmierzonych wartości (np. 0–1,2·10³ w dniu 5/11/2026 i 0–1,0·10³ w dniu 6/11/2026, z przesuniętymi znacznikami podziałki). YA-MS zatem:

1. znajduje długie znaczniki podziałki osi;
2. **odczytuje etykiety** najwyższego znacznika i zera, porównując każdy znak z czcionką matrycową wykresu;
3. dla każdej godziny i (0–47, wczoraj i dziś) bierze środkową kolumnę i pierwszy cyjanowy piksel od góry, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top i y0 to wiersze najwyższego znacznika i zera, N_top to wartość odczytana z najwyższej etykiety (×1000). Rozdzielczość: około 7–8 meteorów/godzinę na piksel. *Wybór programu (podręcznik, wz. 42).*

Jeśli etykiety nie da się odczytać, program wraca do kalibracji z 5/11/2026 (**skalibrowana skala 0-1200 meteorów/godzinę**) i informuje o tym na pomarańczowo: *Nie można odczytać pionowej skali strumienia (górna etykieta: …): wartości wymagają sprawdzenia.* Jeśli zmieni się sam format wykresu (*Zmienił się format wykresu (…x…): nie można go odczytać* lub *Nie znaleziono osi strumienia w oczekiwanym miejscu*), odczyt trzeba ponownie skalibrować: prosimy o zgłoszenie (zob. [Współpraca](Contributing-and-Contacts-pl)).

### Wysokości śladów

Z histogramu wysokości (n_k meteorów w kilometrze k, średnia wysokość h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Podręcznik, wz. 43.* Przy zaznaczonym **z radaru** (wiersz 2 elementów sterujących) **dominanta** staje się wysokością śladu we wszystkich obliczeniach. Sprawdzenie: wykres z 5/11/2026 – dominanta 89,5 km, średnia 88,6 km, odchylenie standardowe 6,8 km, co potwierdza ~90 km z artykułu Cerrotta–Sartori (średnia SKiYMET).

Jeśli zmieni się skala wykresu wysokości, program ostrzega: *statystyki wysokości (dominanta, średnia, mediana) pozostają ważne, bezwzględne liczebności nie.*

## Szacunek dla twojego pasma

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Reguły eksperymentalne **SM6FHZ** (VUSHF 2025): liczba i natężenie odbić skalują się z λ³, czas trwania z λ² (u McKinleya λ³ to moc pojedynczego śladu; liczba śladów skaluje się mniej więcej jak λ^1.5, a w rozpraszaniu do przodu czasy trwania rosną też z sec²φ: zob. [Prognozy eksperymentalne](Experimental-Forecasts-pl)). Wyświetlany jest też maksymalny czas trwania pingu wg IARU Region 1 (1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz). Wartości są orientacyjne, do porównania z doświadczeniem na paśmie. Współczynnik stacji K i porównanie z RMOB znajdziesz w zakładce [Prognozy eksperymentalne](Experimental-Forecasts-pl).

## Bez połączenia

Jeśli żadne źródło nie jest osiągalne, **jeden raz** pojawia się komunikat: *Brak połączenia z internetem. Nie można zaktualizować danych radarowych i RMOB: program używa ostatnio zapisanych danych i sam ponawia próbę co 5 minut.* Pasek stanu na dole zmienia kolor na czerwony (*BRAK POŁĄCZENIA Z INTERNETEM …*), dopóki połączenie nie wróci (*Połączenie przywrócone.*).

## Archiwa i źródła

| Plik (w `data/`) | Zawartość |
|---|---|
| `flusso_collm.csv` | Godzinowe archiwum strumienia odczytanego z Collm (godziny już obecne są aktualizowane) |
| `quote_collm.csv` | Archiwum wysokości śladów |
| `radar/` | Najnowsze pobrane obrazy (i pliki RMOB) |
| `fonti_radar.csv` | Adresy źródeł radarowych, `attivo=1/0`, aby włączyć/wyłączyć każde z nich |

| Źródło | Częstotliwość | Uwagi |
|---|---|---|
| Radar meteorowy w Collm, Uniwersytet w Lipsku (LIM) i IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | aktualizowany co godzinę w 10. minucie UTC; strumień wczoraj + dziś, rozkład wysokości |
| Obserwatorium Geofizyczne Sodankylä – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | tylko obraz (radar w trakcie modernizacji, projekt DECC) |
| swan.ms (kopia danych z Collm) | 36,2 MHz | domyślnie wyłączone; używać tylko za zgodą DL1DBC |

> Dane radarowe należą do swoich instytucji (Uniwersytet w Lipsku / IAP Kühlungsborn, Obserwatorium Geofizyczne Sodankylä).
