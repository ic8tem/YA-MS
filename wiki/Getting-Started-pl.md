[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · **Polski** · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [ไทย](Getting-Started-th) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Pierwsze kroki

Przy pierwszym uruchomieniu YA-MS pokazuje przykładową trasę (JN70CN → JO62QM na 144 MHz). Pięć minut wystarczy, aby skonfigurować program dla twojej stacji.

## 1. Trzy wiersze elementów sterujących

Nad zakładkami znajdują się trzy wiersze elementów sterujących, wspólne dla wszystkich zakładek. Przycisk **Sterowanie** w prawym górnym rogu zwija je i rozwija (przydatne przy dużych czcionkach); wybór jest zapamiętywany.

**Wiersz 1 – stacje i pasmo**

| Element | Co robi |
|---|---|
| **Mój lokator** / **wysokość m** | Twój lokator Maidenhead (4, 6 lub 8 znaków; używany jest środek kwadratu) i wysokość stacji nad poziomem morza. |
| **Korespondent** / **wysokość m** | Lokator i wysokość stacji, z którą chcesz nawiązać łączność. |
| **Pasmo MHz** | 28, 50, 70, 144, 222 lub 432 MHz: używane do zysku i wiązki anteny, szacunku strumienia i bilansu łącza. |
| **Oblicz** | Ponownie oblicza trasę (próbkowanie warstwy E: kilka sekund). |
| **Azymut anteny** | Azymut twojej anteny: zawsze **w stronę DX** (azymut trasy). |
| **Czcionka** | Rozmiar całego tekstu, 100–300 %. Zob. [Ustawienia](Settings-and-Data-Folder-pl#czcionka-i-sterowanie). |

**Wiersz 2 – warstwa E i antena**

| Element | Co robi |
|---|---|
| **Wysokość śladów km** + **z radaru** | Wysokość śladów meteorów (domyślnie 90 km). Gdy zaznaczone jest *z radaru*, używana jest najczęstsza wysokość (dominanta) zmierzona przez radar w Collm; zob. [Strumień radarowy](Radar-Flux-pl). |
| **Elewacja wiązki °** | Najniższa elewacja wiązki twojej anteny (0° = horyzont). Używane są tylko te punkty warstwy E, które obie stacje widzą powyżej tej elewacji. |
| **Antena Yagi: boom m** | Długość boomu twojej anteny Yagi. Program pokazuje długość w λ, zysk (krzywa DL6WU) i wiązkę −3 dB w poziomie i w pionie; zob. [Geometria i tłumienie](Geometry-and-Path-Loss-pl#zysk-i-wiązka-anteny). Poniżej 2 λ szacunek jest mało dokładny. |
| **Hot spot od punktu środkowego km** | Odległość Hot A i Hot B od punktu środkowego, 30–400 km (domyślnie 150 km, jak w AMS Bulletin 203 / W8WN / MSHV). |

**Wiersz 3 – czas**

| Element | Co robi |
|---|---|
| **Godzina** | Zegar UTC. |
| **Czas sklepienia niebieskiego (±36 h)** | Przesuwa [Sklepienie niebieskie](Sky-View-pl) i zakładkę [Radar GRAVES](GRAVES-Radar-pl) do 36 godzin wstecz lub naprzód, w krokach co 15 minut. |
| **Czas rzeczywisty** | Powrót do chwili obecnej. |
| **Dzień dla tabeli 24 h (UTC)** | Dzień pokazywany w [Obliczaniu efektywności](Efficiency-Calculation-pl) i w rekonstrukcji chronologicznej GRAVES. |

## 2. Twoja stacja i DX

1. Wpisz **Mój lokator** i **wysokość m**.
2. Wpisz lokator i wysokość **korespondenta** – albo kliknij mapę na [Sklepieniu niebieskim](Sky-View-pl): **lewy klik = lokator korespondenta**, **prawy klik = lokator mojej stacji**.
3. Wybierz **Pasmo MHz** i naciśnij **Oblicz**.

Pasek stanu na dole potwierdza: *Obliczona trasa: … km, … punktów odbicia próbkowanych w … s*.

## 3. Twoja antena

Wpisz **długość boomu** swojej anteny Yagi. Program wyznacza zysk i wiązkę oraz ostrzega, jeśli Hot A lub Hot B już znajdują się **wewnątrz wiązki**, gdy antena jest skierowana na DX (wtedy są rysowane na szaro: nie trzeba obracać anteny).

## 4. Odczytaj wyniki

| Pytanie | Gdzie szukać |
|---|---|
| Który rój sprzyja teraz mojej trasie i z której strony? | [Sklepienie niebieskie](Sky-View-pl): lista rojów, zalecany Hot na czerwono, strefy PREV |
| Jaka jest dziś najlepsza godzina? | [Obliczanie efektywności](Efficiency-Calculation-pl): karty podsumowania i tabela godzinowa |
| Ile meteorów liczy radar? | [Strumień radarowy](Radar-Flux-pl) |
| Ilu pingów mogę się spodziewać na 144 MHz? | [Eksperymentalne prognozy](Experimental-Forecasts-pl) (eksperymentalne) |
| Czy moja stacja jest w stanie zamknąć trasę? | [Geometria i tłumienie](Geometry-and-Path-Loss-pl): tłumienie trasy i zapas |
| Kiedy jest następne maksimum? | [Roje](Showers-pl) |
| Czy mogę zrobić test z GRAVES? | [Radar GRAVES](GRAVES-Radar-pl) |

## Praktyczne reguły (ze źródeł)

- **Kieruj prostopadle do roju**: najlepsza trasa jest prostopadła do azymutu radiantu; najlepszy kierunek = azymut radiantu ±90°, tolerancja ±40–50° (SM6FHZ).
- **Side-scatter**: obróć antenę o 10–30° w stronę tej strony (A lub B), z której przychodzi najwięcej odbić (artykuł Cerrotta–Sartori).
- **Radiant zbyt wysoko** (powyżej 70°) lub zbyt nisko (poniżej 20°) daje mało użytecznych śladów (DF5HC, DH9GCD).
- Meteory sporadyczne mają maksimum około **06 UTC** (artykuł; potwierdzone przez strumień z Collm).
- Użyteczne odległości na 432 MHz: 800–2000 km, najlepiej około 1400 km (SM6FHZ); najlepsza odległość ogólnie 1300–1500 km (DF5HC).

Dalej: [Sklepienie niebieskie](Sky-View-pl).
