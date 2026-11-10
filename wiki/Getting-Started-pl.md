**English** · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Pierwsze kroki

Przy pierwszym uruchomieniu YA-MS pokazuje przykładową trasę (JN70CN → JO62QM na 144 MHz). Pięć minut wystarczy, aby skonfigurować program dla twojej stacji.

## 1. Trzy wiersze elementów sterujących

Nad zakładkami znajdują się trzy wiersze elementów sterujących, wspólne dla wszystkich zakładek. Przycisk **Sterowanie** w prawym górnym rogu zwija je i rozwija (przydatne przy dużych czcionkach); wybór jest zapamiętywany.

**Wiersz 1 – stacje i pasmo**

| Element | Działanie |
|---|---|
| **Mój lokator** / **wysokość m** | Twój lokator Maidenhead (4, 6 lub 8 znaków; używany jest środek kwadratu) i wysokość stacji nad poziomem morza. |
| **Stacja DX** / **wysokość m** | Lokator i wysokość stacji, z którą chcesz przeprowadzić łączność. |
| **Pasmo MHz** | 28, 50, 70, 144, 222 lub 432 MHz: używane do zysku i listka anteny, szacowania strumienia i bilansu łącza. |
| **Oblicz** | Przelicza trasę (próbkowanie warstwy E: kilka sekund). |
| **Az anteny** | Azymut twojej anteny: zawsze **w stronę DX** (azymut trasy). |
| **Czcionka** | Rozmiar całego tekstu, 100–300 %. Zob. [Ustawienia](Settings-and-Data-Folder-pl#czcionka-i-sterowanie). |

**Wiersz 2 – warstwa E i antena**

| Element | Działanie |
|---|---|
| **Wysokość śladu km** + **z radaru** | Wysokość śladów meteorów (domyślnie 90 km). Przy zaznaczonym *z radaru* używana jest najczęstsza wysokość (dominanta) zmierzona przez radar w Collm; zob. [Strumień radarowy](Radar-Flux-pl). |
| **Elewacja listka °** | Najniższa elewacja listka twojej anteny (0° = horyzont). Używane są tylko te punkty warstwy E, które obie stacje widzą powyżej tej elewacji. |
| **Antena Yagi: boom m** | Długość boomu twojej anteny Yagi. Program pokazuje długość w λ, zysk (krzywa DL6WU) i listek −3 dB, poziomy i pionowy; zob. [Geometria i tłumienie trasy](Geometry-and-Path-Loss-pl#zysk-i-listek-anteny). Poniżej 2 λ szacunek jest przybliżony. |
| **Hot spot od punktu środkowego km** + **auto (AMS)** | Odległość Hot A i Hot B od punktu środkowego. Przy zaznaczonym *auto (AMS)* (domyślnie) wynika z tabeli odchyleń anteny J. Richardsona (AMS) przytoczonej przez DJ5HG: 13° przy 1000 km, 11° przy 1250 km, 10° przy 1500 i 2000 km (około 115, 121, 132 i 176 km od punktu środkowego). Odznacz, aby wpisać ręcznie 30–400 km (MSHV używa 150 km). |

**Wiersz 3 – czas**

| Element | Działanie |
|---|---|
| **Czas** | Zegar UTC. |
| **Data obliczeń (UTC)** | Dzień obliczeń dla zakładek [Obliczanie prognozy](Sky-View-pl) i [Radar GRAVES](GRAVES-Radar-pl) (domyślnie dziś), o bieżącej porze dnia. |
| **Godziny (−12 do +36 h)** | Przesuwa moment obliczeń od 12 godzin przed do 36 godzin po tej porze, w krokach co 15 minut. Obok: *Obliczenia dla: teraz* lub *Obliczenia dla: dd/mm hh:mm UTC*. |
| **Czas rzeczywisty** | Powrót do chwili obecnej. |
| **Dzień dla tabeli 24 h (UTC)** | Dzień wyświetlany w zakładce [Obliczanie efektywności](Efficiency-Calculation-pl) i na osi czasu GRAVES. |

## 2. Twoja stacja i DX

1. Wpisz **Mój lokator** i **wysokość m**.
2. Wpisz lokator i wysokość **stacji DX** – albo kliknij mapę na [kopule nieba](Sky-View-pl): **lewy klik = lokator stacji DX**, **prawy klik = lokator mojej stacji**.
3. Wybierz **Pasmo MHz** i naciśnij **Oblicz**.

Pasek stanu na dole potwierdza: *Trasa obliczona: … km, … próbkowanych punktów odbicia w … s*.

## 3. Twoja antena

Wpisz **długość boomu** swojej anteny Yagi. Program wyznacza zysk i listek oraz ostrzega, jeśli Hot A lub Hot B wypadają już **wewnątrz listka**, gdy antena jest skierowana na DX (są wtedy rysowane na szaro: nie trzeba obracać anteny).

## 4. Odczytaj wyniki

| Pytanie | Gdzie szukać |
|---|---|
| Który rój pomaga teraz mojej trasie i z której strony? | [Kopuła nieba](Sky-View-pl): lista rojów, zalecany Hot na czerwono, strefy PREV |
| Jaka jest dziś najlepsza godzina? | [Obliczanie efektywności](Efficiency-Calculation-pl): karty podsumowania i tabela godzinowa |
| Ile meteorów liczy radar? | [Strumień radarowy](Radar-Flux-pl) |
| Ilu pingów mogę się spodziewać na 144 MHz? | [Prognozy eksperymentalne](Experimental-Forecasts-pl) (eksperymentalnie) |
| Czy moja stacja zamknie trasę? | [Geometria i tłumienie trasy](Geometry-and-Path-Loss-pl): tłumienie trasy i zapas |
| Kiedy jest następne maksimum? | [Roje](Showers-pl) |
| Czy mogę przetestować stację z GRAVES? | [Radar GRAVES](GRAVES-Radar-pl) |

## Praktyczne zasady (ze źródeł)

- **Kieruj prostopadle do roju**: najlepsza trasa jest prostopadła do azymutu radiantu; najlepszy kierunek = azymut radiantu ±90°, tolerancja ±40–50° (SM6FHZ).
- **Side-scatter**: obróć antenę o 10–30° w stronę (A lub B), z której przychodzi większość odbić (artykuł Cerrotta–Sartori).
- **Radiant zbyt wysoko** (powyżej 70°) lub zbyt nisko (poniżej 20°) daje mało użytecznych śladów (DF5HC, DH9GCD).
- Meteory sporadyczne mają maksimum około **06 UTC** (artykuł; potwierdzone przez strumień z Collm).
- Użyteczne odległości na 432 MHz: 800–2000 km, najlepiej około 1400 km (SM6FHZ); najlepsza odległość ogólnie 1300–1500 km (DF5HC).

Dalej: [Kopuła nieba](Sky-View-pl).
