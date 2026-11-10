[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · **Română** · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Implementare experimentală a prognozelor

*Fila: Calcul previzional › Implementare experimentală a prognozelor.*

[![Implementare experimentală a prognozelor](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Această filă transformă numărătorile de meteori ale **radarului Collm (36,2 MHz)** într-o estimare a **reflexiilor pe oră într-o bandă de radioamatori** (implicit 144 MHz, orice frecvență între 28 și 1300 MHz), face prognoza pentru **următoarele 24 de ore** pe traseul tău și îți permite să **compari** estimarea cu un observator **RMOB** – de exemplu unul care ascultă GRAVES pe 143,050 MHz.

> Totul aici este **experimental**: regula de frecvență este o regulă empirică, iar factorul stației depinde de stația ta. Folosește cifrele pentru a compara orele și zilele și verifică-le în trafic.

## Comenzi

| Comandă | Implicit | Ce face |
|---|---|---|
| **Frecvența de sosire MHz** | 144 | Frecvența prognozei (28–1300 MHz) |
| **Exponent λ^k** | 3 | Exponentul k al regulii de frecvență (SM6FHZ: 3) |
| **Factorul stației K** | 1 | Ține cont de stația de recepție (putere, antene); se obține prin comparație cu un observator RMOB pe aceeași bandă |
| **Încarcă fișier RMOB de pe disc...** | | Citește un fișier text lunar RMOB (vezi mai jos) |
| **Obține exponentul din fișierul RMOB** | | Ajustează k din orele comune Collm și RMOB |
| **Observator RMOB** | gol | Numele observatorului așa cum apare în numele fișierului (de ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Descarcă RMOB acum** | | Descarcă o dată fișierul lunii curente al acelui observator |
| **preluare automată la fiecare 5 minute (activați doar cu permisiunea RMOB)** | **dezactivat** | Vezi [RMOB și programele automate](#rmob-și-programele-automate) |

Linia portocalie de sub comenzi arată regula cu cifrele curente, de ex. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, transpunerea duratei și ping-ul maxim IARU la acea frecvență.

## De la radar la banda de radioamatori

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Sursă:** SM6FHZ, *„432 MHz Meteorscatter, Challenges and Techniques”*, al 45-lea Nordic VUSHF, mai 2025 – numărul și intensitatea reflexiilor se scalează cu **λ³**, durata cu **λ²** (432 MHz este cu 14–15 dB sub 144 MHz și durează 1/9). **Verificare:** dependența de λ³ este aceeași ca în ecuația lui McKinley pentru urmele subdense. Cu k = 3, 1000 de meteori/oră la Collm devin circa **16 reflexii/oră la 144 MHz**; observatorii RMOB ai GRAVES pe 143,050 MHz numără de obicei **între 20 și 140 de ecouri/oră** (buletinul RMOB, iunie 2018): ordinul de mărime este compatibil, iar diferența este factorul stației K. (Manual, ec. 44–45.)

## Următoarele 24 de ore

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistență:** valoarea transpusă a aceleiași ore din ziua precedentă (sau de acum două zile, dacă lipsește), corectată cu variația **indicelui roiurilor pe traseu** I (Σ ZHR × eficiență, vezi [Calculul eficienței](Efficiency-Calculation-ro#modelul)). Constanta 10 reprezintă fondul sporadic și limitează corecția când indicele este mic. *Alegere a programului (manual, ec. 47).*

| Panou | Conținut |
|---|---|
| **Măsurat la Collm și transpus la f MHz – ieri și azi (UTC)** | Meteori/oră ai radarului Collm; valorile transpuse (portocaliu, scara din dreapta); numărătorile RMOB, dacă sunt încărcate (verde, scara din dreapta) |
| **Prognoză experimentală pentru următoarele 24 de ore la f MHz pentru …** | Reflexiile/oră prevăzute (bare) și indicele roiurilor pe traseu (scara din dreapta) |
| Tabel | Ora UTC · Collm aceeași oră · Transpus · Indice roiuri traseu · Prognoză /oră · **Evaluare** |

**Evaluare:** *bun* când prognoza este de cel puțin 1,3 × media pe 24 de ore, *mediu* de la 0,8 ×, *slab* sub această valoare. Aceeași prognoză apare în caseta **PROGNOZĂ EXPERIMENTALĂ** și în rândul portocaliu din [Calculul eficienței](Efficiency-Calculation-ro) și stă la baza ecourilor așteptate din fila [Radar GRAVES](GRAVES-Radar-ro#ecouri-așteptate-experimental).

## Comparația RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) colectează numărătorile orare de meteori ale observatorilor radio; mulți din Italia ascultă GRAVES pe 143,050 MHz (Planetariul din Veneția, Faenza, Rovereto și alții).

**Citirea fișierelor RMOB.** Sunt acceptate două formate text:

| Format | Aspect | Note |
|---|---|---|
| Fișier lunar (Colorgramme / Spectrum Lab) | un rând pe zi, `day| n| n| …` cu 24 de valori orare | obișnuitul `NAME_MMYYYYrmob.TXT` |
| Tabel de buletin | antet ` UT |  1   2   3 …`, rânduri `0h|175 166 …` | dacă fișierul conține mai mulți observatori, aceștia sunt citiți unul după altul: folosește un fișier cu un singur observator |

Luna și anul provin din numele fișierului (`…_MMYYYYrmob…`) sau din antet; altfel se folosește luna curentă (iar programul o spune).

**Ajustarea exponentului.** Cu K = 1, din mediana rapoartelor RMOB/Collm pe orele comune (cel puțin 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Alegere a programului (manual, ec. 46).* Dialogul arată orele comune, raportul median și k; **Da** aplică k (și pune K = 1), **Nu** păstrează k = 3 – atunci ajustează manual K la valoarea sugerată în același dialog.

## RMOB și programele automate

RMOB cere ca **programele automate să nu-i preia fișierele**. Din acest motiv **descărcarea automată este dezactivată** la început și ar trebui activată **doar după ce ai cerut permisiunea RMOB**. Fără ea poți folosi oricând **Încarcă fișier RMOB de pe disc...** sau poți apăsa **Descarcă RMOB acum** când ai nevoie.

Adresa de descărcare este un model în `config.ini` (cheia `rmob_url`, implicit `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, unde `{NOME}` este observatorul, iar `{MMAAAA}` luna și anul); fișierele descărcate se păstrează în `data/radar/`.
