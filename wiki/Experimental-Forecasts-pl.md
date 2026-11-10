[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · **Polski** · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [ไทย](Experimental-Forecasts-th) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Eksperymentalne prognozy

*Zakładka: Obliczenie prognozy › Eksperymentalne prognozy.*

[![Eksperymentalne prognozy](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ta zakładka przelicza liczby meteorów z **radaru w Collm (36,2 MHz)** na szacunkową **liczbę odbić na godzinę w paśmie amatorskim** (domyślnie 144 MHz, dowolna częstotliwość od 28 do 1300 MHz), prognozuje **najbliższe 24 godziny** dla twojej trasy i pozwala **porównać** szacunek z obserwatorem **RMOB** – na przykład takim, który nasłuchuje GRAVES na 143,050 MHz.

> Wszystko tutaj jest **eksperymentalne**: reguła częstotliwościowa jest regułą empiryczną, a współczynnik stacji zależy od twojej stacji. Używaj tych liczb do porównywania godzin i dni i sprawdzaj je w eterze.

## Elementy sterujące

| Element | Domyślnie | Co robi |
|---|---|---|
| **Częstotliwość docelowa MHz** | 144 | Częstotliwość prognozy (28–1300 MHz) |
| **Wykładnik λ^k** | 3 | Wykładnik k reguły częstotliwościowej (SM6FHZ: 3) |
| **Współczynnik stacji K** | 1 | Uwzględnia stację odbiorczą (moc, anteny); wyznaczany przez porównanie z obserwatorem RMOB w tym samym paśmie |
| **Wczytaj plik RMOB z dysku...** | | Odczytuje miesięczny plik tekstowy RMOB (zob. niżej) |
| **Wyznacz wykładnik z pliku RMOB** | | Dopasowuje k na podstawie wspólnych godzin Collm i RMOB |
| **Obserwator RMOB** | puste | Nazwa obserwatora w takiej postaci, w jakiej występuje w nazwie pliku (np. `NAME_112026rmob.TXT` → `NAME`) |
| **Pobierz RMOB teraz** | | Jednorazowo pobiera plik bieżącego miesiąca tego obserwatora |
| **automatyczne pobieranie co 5 minut (włączać tylko za zgodą RMOB)** | **wyłączone** | Zob. [RMOB i programy automatyczne](#rmob-i-programy-automatyczne) |

Pomarańczowy wiersz pod elementami sterującymi pokazuje regułę z bieżącymi liczbami, np. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, skalowanie czasu trwania i maksymalny ping według IARU przy tej częstotliwości.

## Od radaru do pasma amatorskiego

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Źródło:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maj 2025 – liczba i natężenie odbić skalują się z **λ³**, czas trwania z **λ²** (432 MHz jest o 14–15 dB słabsze niż 144 MHz i trwa 1/9 tego czasu). **Sprawdzenie:** zależność od λ³ jest taka sama jak w równaniu McKinleya dla śladów podkrytycznych. Przy k = 3, 1000 meteorów/godz. w Collm daje około **16 odbić/godz. na 144 MHz**; obserwatorzy RMOB nasłuchujący GRAVES na 143,050 MHz liczą zwykle **od 20 do 140 ech/godz.** (biuletyn RMOB, czerwiec 2018): rząd wielkości jest zgodny, a różnicę stanowi współczynnik stacji K. (Podręcznik, wz. 44–45.)

## Najbliższe 24 godziny

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persystencja:** przeliczona wartość z tej samej godziny dnia poprzedniego (lub sprzed dwóch dni, jeśli jej brak), skorygowana o zmianę **indeksu rojów trasy** I (Σ ZHR × efektywność, zob. [Obliczanie efektywności](Efficiency-Calculation-pl#model)). Stała 10 reprezentuje tło sporadyczne i ogranicza korektę, gdy indeks jest mały. *Wybór programu (podręcznik, wz. 47).*

| Panel | Zawartość |
|---|---|
| **Zmierzone w Collm i przeliczone na f MHz – wczoraj i dziś (UTC)** | Meteory/godz. z radaru w Collm; wartości przeliczone (pomarańczowe, prawa skala); liczby RMOB, jeśli wczytano (zielone, prawa skala) |
| **Eksperymentalna prognoza na najbliższe 24 godziny przy f MHz dla …** | Prognozowane odbicia/godz. (słupki) i indeks rojów trasy (prawa skala) |
| Tabela | Godzina UTC · Collm ta sama godzina · Przeliczone · Indeks rojów trasy · Prognoza /godz. · **Ocena** |

**Ocena:** *dobry*, gdy prognoza wynosi co najmniej 1,3 × średnia z 24 godzin, *średni* od 0,8 ×, *słaby* poniżej. Ta sama prognoza pojawia się na karcie **PROGNOZA EKSPERYMENTALNA** i w pomarańczowym wierszu [Obliczania efektywności](Efficiency-Calculation-pl) oraz stanowi podstawę oczekiwanych ech w zakładce [Radar GRAVES](GRAVES-Radar-pl#oczekiwane-echa-eksperymentalnie).

## Porównanie z RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) zbiera godzinowe liczby meteorów od obserwatorów radiowych; wielu z nich we Włoszech nasłuchuje GRAVES na 143,050 MHz (Planetarium w Wenecji, Faenza, Rovereto i inni).

**Odczyt plików RMOB.** Akceptowane są dwa formaty tekstowe:

| Format | Wygląd | Uwagi |
|---|---|---|
| Plik miesięczny (Colorgramme / Spectrum Lab) | jeden wiersz na dzień, `day| n| n| …` z 24 wartościami godzinowymi | typowy `NAME_MMYYYYrmob.TXT` |
| Tabela z biuletynu | nagłówek ` UT |  1   2   3 …`, wiersze `0h|175 166 …` | jeśli plik zawiera kilku obserwatorów, są odczytywani jeden po drugim: używaj pliku z jednym obserwatorem |

Miesiąc i rok pochodzą z nazwy pliku (`…_MMYYYYrmob…`) lub z nagłówka; w przeciwnym razie używany jest bieżący miesiąc (i program o tym informuje).

**Dopasowanie wykładnika.** Przy K = 1, z mediany stosunków RMOB/Collm we wspólnych godzinach (co najmniej 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Wybór programu (podręcznik, wz. 46).* Okno dialogowe pokazuje wspólne godziny, medianę stosunku i k; **Tak** stosuje k (i ustawia K = 1), **Nie** zachowuje k = 3 – wtedy ustaw ręcznie K na wartość zaproponowaną w tym samym oknie.

## RMOB i programy automatyczne

RMOB prosi, aby **programy automatyczne nie pobierały jego plików**. Z tego powodu **automatyczne pobieranie jest na starcie wyłączone** i należy je włączać **tylko po uzyskaniu zgody RMOB**. Bez niej zawsze możesz użyć **Wczytaj plik RMOB z dysku...** albo nacisnąć **Pobierz RMOB teraz**, gdy tego potrzebujesz.

Adres pobierania jest szablonem w `config.ini` (klucz `rmob_url`, domyślnie `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, gdzie `{NOME}` to obserwator, a `{MMAAAA}` to miesiąc i rok); pobrane pliki są przechowywane w `data/radar/`.
