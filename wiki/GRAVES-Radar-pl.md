**English** · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Zakładka: Dane na żywo i w czasie rzeczywistym › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Czym jest GRAVES

**GRAVES** to francuski radar, który nadaje **CW na 143,050 MHz** z miejscowości **Broye-lès-Pesmes** (47,348° N 5,515° E, lokator **JN27SI**, około 200 m n.p.m.; Wikipedia). Ślady meteorów w strefie widocznej zarówno dla GRAVES, jak i dla ciebie odbijają jego sygnał w twoją stronę przez **rozpraszanie do przodu (forward scatter)**: słyszysz krótkie *pingi* blisko nośnej. W ten sposób obserwatorzy **RMOB** na 143,050 MHz liczą meteory godzina po godzinie; jest to też darmowy, zawsze dostępny sygnał testowy dla twojej stacji meteor scatter na 2 m.

Zakładka traktuje **GRAVES → ty** jako osobną trasę meteor scatter: przy użyciu tych samych funkcji co dla głównej trasy (ta sama wysokość śladu, elewacja listka i odległość hot spotu) oblicza efektywność rojów, zalecany Hot i strefy PREV, a następnie sprawdza, czy ta strefa leży **wewnątrz wiązki GRAVES** i **kiedy** wiązka ją oświetla.

## Górny pasek

| Element | Działanie |
|---|---|
| **Teraz** | Przywraca obliczenia do czasu rzeczywistego: dzisiejsza data i suwak godzin na zero (zakładka podąża za polami *Data obliczeń* i *Godziny*). |
| **Ustaw GRAVES jako DX** | Stacją DX staje się GRAVES (JN27SI, wysokość 200 m) i główna trasa jest przeliczana: wszystkie pozostałe zakładki pokazują wtedy trasę do GRAVES. |
| **Sekwencja wiązki** | *0,8 s na krok · cykl 4,8 s (PE1ITR 2021)* (domyślnie) lub *3,2 s na krok · cykl 19,2 s (PE1ITR 2007)*. |

## Cztery karty

| Karta | Zawartość |
|---|---|
| **STREFA UŻYTECZNA W WIĄZCE GRAVES** | *Tak · sektor X* z azymutem i elewacją zalecanego hot spotu widzianego z GRAVES oraz krokiem (1–6); albo *Nie: poza sektorami* / *Nie: poniżej horyzontu GRAVES* / *Nie: powyżej wiązki (około 25°)* |
| **EFEKTYWNOŚĆ TRASY GRAVES → TY TERAZ** | Indeks trasy Σ ZHR × efektywność, najlepszy rój, przeważająca strona A/B oraz *oczekiwane echa ≈ …/godz.* (eksperymentalnie, zob. niżej) |
| **TRASA** | Odległość do GRAVES; antena w stronę zalecanego Hot (azymut i elewacja); bezpośredni azymut na GRAVES |
| **NASTĘPNE PRZEJŚCIE WIĄZKI NAD STREFĄ** | *teraz · pozostało … s* lub *za … s*, krok (np. *B4*), trzy kolejne momenty (sekundy w ramach minuty) oraz odsetek uchwyconych śladów |

Jeśli w danym momencie żaden rój nie jest użyteczny, program pokazuje hot spot **najlepiej dopasowany do wiązki** (wewnątrz sektorów, najbliżej południa) i informuje o tym.

## Niebo widziane z GRAVES

Według PE1ITR i wiki Bolidozor **cztery szyki fazowane** pokrywają południowe niebo od **90° do 270°** azymutu w czterech **sektorach po 45°**:

| Sektor | Azymut od GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Każdy sektor jest podzielony na **6 kroków po 7,5°**, ponumerowanych od 1 do 6 od najmniejszego azymutu, oświetlanych jeden po drugim, **w tym samym momencie we wszystkich czterech sektorach**. Wiązka ma około **25° szerokości w elewacji**: na wysokości śladów pokrywa kolorowy pierścień między dwoma okręgami kreskowanymi (*horyzont wiązki*). Na rysunku: pomarańczowe/różowe kropki = strefy PREV trasy GRAVES → ty, zielona linia = kierunek twojej stacji, czerwona linia = od twojej stacji do zalecanego hot spotu; aktualnie oświetlany krok jest wyróżniony.

## Rekonstrukcja osi czasu

*REKONSTRUKCJA OSI CZASU · data UTC* (ten sam dzień co tabela 24 h): dla każdej godziny efektywność trasy GRAVES → ty, najkorzystniejszy rój i okno użyteczne (*hh:00 → hh:00 UTC · n h*), z maksimum (*max Σ … o hh:30*) i czerwonym znacznikiem *teraz*. Poniżej **szczegóły najbliższych sekund**: sześć kroków sektora, krok oświetlający strefę użyteczną oraz *możliwe echo (+0,3 s śladu)*.

### Taktowanie wiązki

Sekwencja jest powiązana z **UTC** (PE1ITR): aktualnie oświetlany krok jest obliczany z liczby sekund od 00:00 UTC modulo cykl (86 400 s jest wielokrotnością zarówno 4,8 s, jak i 19,2 s). Stacja sterująca czasem przesuwa sekwencję o kilka kroków, więc szczegóły są **przewidywaniem do potwierdzenia nasłuchem**. Żółta etykieta **Zegar PC zsynchronizowany** przypomina: zsynchronizuj komputer z serwerem NTP (błąd co najwyżej kilku dziesiątych sekundy).

### Współczynnik wykrycia

Ślad jest słyszalny tylko wtedy, gdy wiązka oświetli go w czasie jego trwania:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s to typowy czas trwania śladu podgęstego na 143 MHz – wartość stała, *wybór programu* (reguła λ² SM6FHZ skaluje czasy trwania między pasmami, ale nie podaje wartości wyjściowej).

### Oczekiwane echa (eksperymentalne)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Prognoza z zakładki [Prognozy eksperymentalne](Experimental-Forecasts-pl) (która zawiera już współczynnik stacji K) jest skalowana z jej częstotliwości f_fc do 143,050 MHz regułą SM6FHZ (ten sam wykładnik k), korygowana stosunkiem indeksów rojów obu tras (stała 10 reprezentuje tło sporadyczne, jak w prognozie) i mnożona przez współczynnik wykrycia. Wartość wyłącznie orientacyjna: porównaj z obserwatorami RMOB.

## Jak usłyszeć pingi GRAVES

| Krok | Co zrobić |
|---|---|
| Odbiornik | **USB na 143,049 MHz** (ton około 1 kHz) lub 143,050 MHz, **ARW wolne lub wyłączone**, pasmo audio **co najmniej 2,4 kHz** |
| Antena | W stronę **zalecanego hot spotu** trasy GRAVES → ty (karta *TRASA*), przy **niskiej elewacji** |
| Waterfall | Pingi to **krótkie kreski blisko nośnej**; długie (nadgęste) ślady są szersze i wykazują Dopplera |
| Zliczanie | RMOB używa GRAVES do godzinowych zliczeń meteorów: **porównaj swoje pingi z obserwatorami na 143,050 MHz** ([Prognozy eksperymentalne](Experimental-Forecasts-pl#porównanie-z-rmob)) |

## Źródła

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) oraz *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, "Graves" – szyki antenowe, sektory i taktowanie wiązki
3. **Wikipedia**, "GRAVES (system)" – nadajnik w Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – obserwatorzy na 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** autorstwa IC8TEM – zakładka GRAVES Radar (pierwowzór, z którego wywodzi się ta zakładka)
