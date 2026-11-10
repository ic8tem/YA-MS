[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-BR) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · **Polski** · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-TW)

# Roje

*Zakładka: Roje.*

[![Roje](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Katalog rojów używany we wszystkich obliczeniach: **45 rojów** z **IMO Meteor Shower Calendar 2026 i 2027** (tabele 5 i 7) oraz **Antihelion Source** (tabela 6), każdy z **następnym maksimum**.

## Kolumny

| Kolumna | Znaczenie |
|---|---|
| Kod | Kod IMO (QUA, PER, GEM, …) |
| Rój | Nazwa |
| Aktywność | Okres aktywności (dzień/miesiąc – dzień/miesiąc) |
| λ max | Długość ekliptyczna Słońca w maksimum (J2000), wg IMO |
| **Następne maksimum (UTC)** | Data i godzina następnego maksimum (zob. niżej) |
| **Źródło maksimum** | *IMO 2026* / *IMO 2027* = data i godzina opublikowane przez IMO; *IMO 2026 (dzień)* = IMO podaje tylko dzień, wyświetlana godzina jest obliczona (*~hh:mm oblicz.*); *obliczone z λ* = brak wartości IMO dla danego roku |
| R.A., Dec. | Radiant w maksimum (*ruchomy* dla Antihelion Source) |
| v km/s, r | Prędkość geocentryczna i indeks populacji |
| ZHR | ZHR w maksimum (*zm.* = zmienny) |
| Typ | *wizualny* lub *radiowy, dzienny* |

Roje **aktywne dziś (UTC)** są wyróżnione żółtym tłem i pogrubionym tekstem.

## Następne maksimum

Program zawsze pokazuje **następne** maksimum. Gdy IMO opublikowała kalendarz na dany rok, używana jest **data i godzina IMO** z `data/massimi_imo.csv` (lata 2026 i 2027 są dołączone); w przeciwnym razie program oblicza moment, w którym Słońce osiąga długość ekliptyczną maksimum (Meeus, *Astronomical Algorithms*, rozdz. 25, rozwiązane metodą Newtona).

**Sprawdzenie:** obliczenia zgadzają się z kalendarzami IMO 2026 i 2027 z dokładnością do kilku minut tam, gdzie IMO podaje godzinę (np. Kwadrantydy 3/1/2026 21:13 wobec 21:00; Geminidy 14/12/2027 19:51 wobec 20:00). Wyjątki: Dzienne kappa Leonidy 2026 o jeden dzień później (26/9 zamiast 25/9) oraz godzina eta Akwarydów 2027 (15:10 wobec 09:00 wg IMO) – w tych przypadkach używana jest wartość IMO.

**Dodawanie roku:** gdy IMO opublikuje nowy kalendarz, dodaj jego wiersze do `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, godzina pusta, jeśli IMO podaje tylko dzień). Do tego czasu maksimum jest obliczane.

## Roje mniejsze i dzienne

Katalog obejmuje **roje mniejsze** z listy IMO – na przykład Październikowe Kamelopardalidy (OCT, ZHR 5, aktywne 5–6 października), Andromedydy, gamma Ursae Minorydy – oraz **dzienne roje radiowe** od kwietnia do października (Dzienne kwietniowe Piscydy, Dzienne Arietydy, Dzienne zeta Perseidy, Dzienne beta Taurydy, Dzienne kappa Leonidy, Dzienne Sekstantydy, …). Nawet przy małych ZHR wnoszą one wkład do [indeksu trasy](Efficiency-Calculation-pl#model) i do [zalecanego Hot](Sky-View-pl#zalecany-hot). Dla dziennych rojów radiowych IMO nie podaje ZHR: tam, gdzie go brak, program używa wartości roboczej 5.

## Profil aktywności i dryf radiantu

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 i λ_max pochodzą z kalendarza IMO; nachylenia B (różne przed maksimum i po nim) oraz dzienne dryfy dα/dλ, dδ/dλ to **wartości robocze** zapisane w `data/sciami.csv` (tabela dryfów IMO nie została jeszcze wprowadzona). *Podręcznik, wz. 9 i 13.* Położenie Antihelion Source jest interpolowane liniowo między datami z tabeli 6 IMO (`data/ant_radiante.csv`; aktywne od 10 grudnia do 20 września, ZHR około 4).

## Edycja katalogu

`data/sciami.csv` to zwykły plik tekstowy (separator `;`), który możesz edytować: kod, nazwa, początek i koniec (MM-DD), λ max, R.A., Dec., dryfy, v, r, ZHR, B przed/po, typ (V wizualny, R dzienny radiowy). Jeśli wiersz jest błędny, program wyświetla komunikat przy uruchomieniu i go pomija.

Źródła: International Meteor Organization – Meteor Shower Calendar 2026 i 2027, [www.imo.net](https://www.imo.net) (tabele 5, 6 i 7); Rossano IZ5TEK (scattertek).
