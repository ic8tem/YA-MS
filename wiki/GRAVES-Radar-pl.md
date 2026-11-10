LANGBAR

# Radar GRAVES

*Zakładka: Na żywo i dane w czasie rzeczywistym › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Czym jest GRAVES

**GRAVES** to francuski radar nadający **CW na 143,050 MHz** z **Broye-lès-Pesmes** (47,348° N 5,515° E, lokator **JN27SI**, około 200 m n.p.m.; Wikipedia). Ślady meteorów w strefie widocznej zarówno dla GRAVES, jak i dla ciebie odbijają jego sygnał w twoją stronę przez **forward scatter**: słyszysz krótkie *pingi* blisko nośnej. W ten sposób obserwatorzy **RMOB** na 143,050 MHz liczą meteory godzina po godzinie; jest to też darmowy, stale nadający sygnał testowy dla twojej stacji meteor scatter na 2 m.

Zakładka traktuje **GRAVES → ty** jako osobną trasę meteor scatter: tymi samymi funkcjami co trasę główną (ta sama wysokość śladów, elewacja wiązki i odległość hot spotów) oblicza efektywność rojów, zalecany Hot i strefy PREV, a następnie sprawdza, czy ta strefa jest **wewnątrz wiązki GRAVES** i **kiedy** wiązka ją oświetla.

## Górny pasek

| Element | Co robi |
|---|---|
| **Teraz** | Przywraca czas sklepienia niebieskiego do czasu rzeczywistego (zakładka podąża za suwakiem *Czas sklepienia niebieskiego*). |
| **Ustaw GRAVES jako DX** | Korespondentem staje się GRAVES (JN27SI, wysokość 200 m), a trasa główna jest obliczana ponownie: wszystkie pozostałe zakładki pokazują wtedy trasę do GRAVES. |
| **Sekwencja wiązki** | *0,8 s na krok · cykl 4,8 s (PE1ITR 2021)* (domyślnie) lub *3,2 s na krok · cykl 19,2 s (PE1ITR 2007)*. |

## Cztery karty

| Karta | Zawartość |
|---|---|
| **STREFA UŻYTECZNA W WIĄZCE GRAVES** | *Tak · sektor X* z azymutem i elewacją zalecanego hot spotu widzianego z GRAVES oraz krokiem (1–6); albo *Nie: poza sektorami* / *Nie: poniżej horyzontu GRAVES* / *Nie: powyżej wiązki (około 25°)* |
| **EFEKTYWNOŚĆ TRASY GRAVES → TY TERAZ** | Indeks trasy Σ ZHR × efektywność, najlepszy rój, przeważająca strona A/B oraz *oczekiwane echa ≈ …/godz.* (eksperymentalnie, zob. niżej) |
| **TRASA** | Odległość do GRAVES; antena w stronę zalecanego Hot (azymut i elewacja); azymut GRAVES w linii prostej |
| **NASTĘPNE PRZEJŚCIE WIĄZKI NAD STREFĄ** | *teraz · jeszcze … s* lub *za … s*, krok (np. *B4*), trzy następne chwile (sekundy w obrębie minuty) i odsetek uchwyconych śladów |

Jeśli w danej chwili żaden rój nie jest użyteczny, program pokazuje hot spot **najlepiej dopasowany do wiązki** (wewnątrz sektorów, najbliżej południa) i o tym informuje.

## Niebo widziane z GRAVES

Według PE1ITR i wiki Bolidozor **cztery szyki fazowane** pokrywają południową część nieba od **90° do 270°** azymutu w czterech **sektorach po 45°**:

| Sektor | Azymut od GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Każdy sektor jest podzielony na **6 kroków po 7,5°**, numerowanych od 1 do 6 od najmniejszego azymutu, oświetlanych jeden po drugim, **w tej samej chwili we wszystkich czterech sektorach**. Wiązka ma szerokość około **25° w elewacji**: na wysokości śladów pokrywa kolorowy pierścień między dwoma przerywanymi okręgami (*horyzont wiązki*). Na rysunku: punkty pomarańczowe/różowe = strefy PREV trasy GRAVES → ty, zielona linia = kierunek twojej stacji, czerwona linia = od twojej stacji do zalecanego hot spotu; krok oświetlany w tej chwili jest wyróżniony.

## Rekonstrukcja chronologiczna

*REKONSTRUKCJA CHRONOLOGICZNA · data UTC* (ten sam dzień co w tabeli 24 h): dla każdej godziny efektywność trasy GRAVES → ty, najkorzystniejszy rój i okno użyteczne (*gg:00 → gg:00 UTC · n h*), z maksimum (*maks. Σ … o gg:30*) i czerwonym znacznikiem *teraz*. Poniżej **szczegóły najbliższych sekund**: sześć kroków sektora, krok oświetlający strefę użyteczną oraz *możliwe echo (+0,3 s śladu)*.

### Czasy wiązki

Sekwencja jest powiązana z **UTC** (PE1ITR): krok oświetlany w tej chwili oblicza się z liczby sekund od 00:00 UTC modulo cykl (86 400 s jest wielokrotnością zarówno 4,8 s, jak i 19,2 s). Stacja sterująca czasem przesuwa sekwencję o kilka kroków, więc szczegóły są **przewidywaniem do potwierdzenia nasłuchem**. Żółta etykieta **zegar PC zsynchronizowany** przypomina: zsynchronizuj komputer z serwerem NTP (błąd najwyżej kilku dziesiątych sekundy).

### Współczynnik detekcji

Ślad jest słyszalny tylko wtedy, gdy wiązka oświetli go w czasie jego trwania:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s to typowy czas trwania śladu podkrytycznego na 143 MHz – wartość stała, *wybór programu* (reguła λ² SM6FHZ skaluje czasy trwania między pasmami, ale nie podaje wartości początkowej).

### Oczekiwane echa (eksperymentalnie)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Prognoza z [Eksperymentalnych prognoz](Experimental-Forecasts-pl) (która zawiera już współczynnik stacji K) jest przeliczana z jej częstotliwości f_fc na 143,050 MHz regułą SM6FHZ (ten sam wykładnik k), korygowana stosunkiem indeksów rojów obu tras (stała 10 reprezentuje tło sporadyczne, jak w prognozie) i mnożona przez współczynnik detekcji. Wartość wyłącznie orientacyjna: porównuj z obserwatorami RMOB.

## Jak słuchać pingów GRAVES

| Krok | Co zrobić |
|---|---|
| Odbiornik | **USB na 143,049 MHz** (ton około 1 kHz) lub 143,050 MHz, **AGC wolne lub wyłączone**, pasmo audio **co najmniej 2,4 kHz** |
| Antena | W stronę **zalecanego hot spotu** trasy GRAVES → ty (karta *TRASA*), przy **niskiej elewacji** |
| Waterfall | Pingi to **krótkie kreski blisko nośnej**; długie ślady (nadkrytyczne) są szersze i wykazują przesunięcie Dopplera |
| Zliczanie | RMOB używa GRAVES do godzinowego zliczania meteorów: **porównaj swoje pingi z obserwatorami na 143,050 MHz** ([Eksperymentalne prognozy](Experimental-Forecasts-pl#porównanie-z-rmob)) |

## Źródła

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) oraz *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, "Graves" – szyki antenowe, sektory i czasy wiązki
3. **Wikipedia**, "GRAVES (system)" – nadajnik w Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – obserwatorzy na 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** autorstwa IC8TEM – zakładka Radar GRAVES (szkic, z którego wywodzi się ta zakładka)
