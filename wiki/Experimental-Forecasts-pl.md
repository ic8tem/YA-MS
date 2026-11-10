[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · **Polski** · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Prognozy eksperymentalne

*Zakładka: Obliczanie prognozy › Prognozy eksperymentalne.*

[![Prognozy eksperymentalne](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ta zakładka przelicza zliczenia meteorów z **radaru w Collm (36,2 MHz)** na szacunkową liczbę **odbić na godzinę w paśmie amatorskim** (domyślnie 144 MHz, dowolna częstotliwość od 28 do 1300 MHz), prognozuje **następne 24 godziny** dla twojej trasy i pozwala **porównać** szacunek z obserwatorem **RMOB** – na przykład z kimś, kto nasłuchuje GRAVES na 143,050 MHz.

> Wszystko tutaj jest **eksperymentalne**: reguła częstotliwościowa jest regułą empiryczną, a współczynnik stacji zależy od twojej stacji. Używaj tych liczb do porównywania godzin i dni i sprawdzaj je na paśmie.

## Elementy sterujące

| Element | Domyślnie | Działanie |
|---|---|---|
| **Częstotliwość docelowa MHz** | 144 | Częstotliwość prognozy (28–1300 MHz) |
| **Wykładnik λ^k** | 3 | Wykładnik k reguły częstotliwościowej (SM6FHZ: 3) |
| **Współczynnik stacji K** | 1 | Uwzględnia stację odbiorczą (moc, anteny); wyznaczany przez porównanie z obserwatorem RMOB w tym samym paśmie |
| **Wczytaj plik RMOB z dysku...** | | Odczytuje miesięczny plik tekstowy RMOB (zob. niżej) |
| **Wyznacz wykładnik z pliku RMOB** | | Dopasowuje k na podstawie wspólnych godzin Collm i RMOB |
| **Obserwator RMOB** | pusty | Nazwa obserwatora taka, jak w nazwie pliku (np. `NAME_112026rmob.TXT` → `NAME`) |
| **Pobierz RMOB teraz** | | Jednorazowo pobiera plik bieżącego miesiąca tego obserwatora |
| **automatyczne pobieranie co 5 minut (włączaj tylko za zgodą RMOB)** | **wył.** | Zob. [RMOB a programy automatyczne](#rmob-a-programy-automatyczne) |

Pomarańczowy wiersz pod elementami sterującymi pokazuje regułę z bieżącymi liczbami, np. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, skalowanie czasu trwania oraz maksymalny ping wg IARU dla tej częstotliwości.

## Od radaru do pasma amatorskiego

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Źródło:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 – liczba i natężenie odbić skalują się z **λ³**, czas trwania z **λ²** (432 MHz jest 14–15 dB poniżej 144 MHz i trwa 1/9 czasu). **Sprawdzenie:** w równaniu McKinleya λ³ to moc pojedynczego śladu podgęstego, a nie liczba śladów; dla indeksu masowego 2 liczba śladów powyżej stałego progu skaluje się mniej więcej jak λ^1.5 (IZ5TEK; OH5IY). Program zachowuje k = 3, eksperymentalną regułę SM6FHZ, i wyraźnie to zaznacza; właściwe k dla twojej stacji wynika z porównania z RMOB. W rozpraszaniu do przodu (forward scatter) czas trwania rośnie także z sec²φ (McKinley; OH5IY): Collm mierzy w rozpraszaniu wstecznym (φ = 0), więc prognoza jest mnożona przez sec²φ w punkcie środkowym trasy (×4 przy 60°, ×8,5 przy 70°, ×33 przy 80°). Przy k = 3 1000 meteorów/godzinę w Collm daje około **16 odbić/godzinę na 144 MHz**; obserwatorzy RMOB nasłuchujący GRAVES na 143,050 MHz zwykle liczą **od 20 do 140 ech/godzinę** (biuletyn RMOB, czerwiec 2018): rząd wielkości jest zgodny, a różnicę stanowi współczynnik stacji K. (Podręcznik, wz. 44–45.)

## Następne 24 godziny

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Persystencja:** przeskalowana wartość z tej samej godziny dnia poprzedniego (lub sprzed dwóch dni, jeśli jej brak), skorygowana o zmianę **indeksu rojów na trasie** I (Σ ZHR × efektywność, zob. [Obliczanie efektywności](Efficiency-Calculation-pl#model)). Stała 10 reprezentuje tło sporadyczne i ogranicza korekcję, gdy indeks jest mały. *Wybór programu (podręcznik, wz. 47).*

| Panel | Zawartość |
|---|---|
| **Zmierzone w Collm i przeskalowane do f MHz – wczoraj i dziś (UTC)** | Meteory/godzinę z radaru w Collm; wartości przeskalowane (pomarańczowe, prawa skala); zliczenia RMOB, jeśli wczytane (zielone, prawa skala) |
| **Prognoza eksperymentalna na następne 24 godziny na f MHz dla …** | Prognozowane odbicia/godzinę (słupki) i indeks rojów na trasie (prawa skala) |
| Tabela | Czas UTC · Collm ta sama godzina · Przeskalowane · Indeks rojów na trasie · Prognoza /godz. · **Ocena** |

**Ocena:** *dobra*, gdy prognoza wynosi co najmniej 1,3 × średnia z 24 godzin, *średnia* od 0,8 ×, *słaba* poniżej. Ta sama prognoza pojawia się na karcie **PROGNOZA EKSPERYMENTALNA** i w pomarańczowym wierszu zakładki [Obliczanie efektywności](Efficiency-Calculation-pl) i stanowi podstawę oczekiwanych ech w zakładce [Radar GRAVES](GRAVES-Radar-pl#oczekiwane-echa-eksperymentalne).

## Porównanie z RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) zbiera godzinowe zliczenia meteorów od obserwatorów radiowych; wielu we Włoszech nasłuchuje GRAVES na 143,050 MHz (Planetarium w Wenecji, Faenza, Rovereto i inni).

**Odczyt plików RMOB.** Akceptowane są dwa formaty tekstowe:

| Format | Wygląd | Uwagi |
|---|---|---|
| Plik miesięczny (Colorgramme / Spectrum Lab) | jeden wiersz na dzień, `day| n| n| …` z 24 wartościami godzinowymi | typowy `NAME_MMYYYYrmob.TXT` |
| Tabela z biuletynu | nagłówek ` UT |  1   2   3 …`, wiersze `0h|175 166 …` | jeśli plik zawiera kilku obserwatorów, są oni wczytywani jeden po drugim: użyj pliku z jednym obserwatorem |

Miesiąc i rok są brane z nazwy pliku (`…_MMYYYYrmob…`) lub z nagłówka; w przeciwnym razie używany jest bieżący miesiąc (a program to sygnalizuje).

**Dopasowanie wykładnika.** Przy K = 1, z mediany stosunków RMOB/Collm we wspólnych godzinach (co najmniej 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Wybór programu (podręcznik, wz. 46).* Okno dialogowe pokazuje wspólne godziny, medianę stosunku i k; **Tak** stosuje k (i ustawia K = 1), **Nie** zachowuje k = 3 – wtedy ręcznie dostosuj K do wartości zaproponowanej w tym samym oknie.

## RMOB a programy automatyczne

RMOB prosi, aby **programy automatyczne nie pobierały jego plików**. Z tego powodu **automatyczne pobieranie jest na starcie wyłączone** i należy je włączać **dopiero po uzyskaniu zgody RMOB**. Bez niej zawsze możesz użyć **Wczytaj plik RMOB z dysku...** albo nacisnąć **Pobierz RMOB teraz**, gdy tego potrzebujesz.

Adres pobierania to szablon w `config.ini` (klucz `rmob_url`, domyślnie `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, gdzie `{NOME}` to obserwator, a `{MMAAAA}` miesiąc i rok); pobrane pliki są przechowywane w `data/radar/`.
