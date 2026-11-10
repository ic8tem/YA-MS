[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-BR) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · **Română** · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-TW)

# Previziuni experimentale

*Filă: Calcul previzional › Previziuni experimentale.*

[![Previziuni experimentale](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Această filă transformă numărul de meteori al **radarului din Collm (36,2 MHz)** într-o estimare a **reflexiilor pe oră pe o bandă de radioamatori** (implicit 144 MHz, orice frecvență între 28 și 1300 MHz), face previziunea pentru **următoarele 24 de ore** pe traseul dumneavoastră și vă permite să **comparați** estimarea cu un observator **RMOB** – de exemplu unul care ascultă GRAVES pe 143,050 MHz.

> Totul aici este **experimental**: regula de frecvență este o regulă empirică, iar factorul de stație depinde de stația dumneavoastră. Folosiți cifrele pentru a compara ore și zile și verificați-le în eter.

## Comenzi

| Comandă | Implicit | Ce face |
|---|---|---|
| **Frecvența țintă MHz** | 144 | Frecvența previziunii (28–1300 MHz) |
| **Exponentul λ^k** | 3 | Exponentul k al regulii de frecvență (SM6FHZ: 3) |
| **Factorul de stație K** | 1 | Ține cont de stația de recepție (putere, antene); dedus prin comparație cu un observator RMOB pe aceeași bandă |
| **Încarcă fișier RMOB de pe disc...** | | Citește un fișier text lunar RMOB (vedeți mai jos) |
| **Deduce exponentul din fișierul RMOB** | | Ajustează k din orele comune ale Collm și RMOB |
| **Observator RMOB** | gol | Numele observatorului așa cum apare în numele fișierului (de ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Descarcă RMOB acum** | | Descarcă o singură dată fișierul lunii curente al acelui observator |
| **descărcare automată la fiecare 5 minute (activați doar cu permisiunea RMOB)** | **dezactivată** | Vedeți [RMOB și programele automate](#rmob-și-programele-automate) |

Linia portocalie de sub comenzi arată regula cu cifrele curente, de ex. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, scalarea duratei și ping-ul maxim IARU la acea frecvență.

## De la radar la banda de radioamatori

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Sursă:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, al 45-lea Nordic VUSHF, mai 2025 – numărul și intensitatea reflexiilor scalează cu **λ³**, durata cu **λ²** (432 MHz este cu 14–15 dB sub 144 MHz și durează 1/9). **Verificare:** în ecuația lui McKinley, λ³ este puterea unei singure urme subdense, nu numărul de urme; pentru indicele de masă 2, numărul de urme peste un prag fix scalează aproximativ ca λ^1,5 (IZ5TEK; OH5IY). Programul păstrează k = 3, regula experimentală a lui SM6FHZ, și o spune; k-ul potrivit pentru stația dumneavoastră provine din comparația cu RMOB. În forward scatter, durata crește și cu sec²φ (McKinley; OH5IY): Collm măsoară în backscatter (φ = 0), deci previziunea înmulțește cu sec²φ în punctul median al traseului (×4 la 60°, ×8,5 la 70°, ×33 la 80°). Cu k = 3, 1000 de meteori/oră la Collm devin aproximativ **16 reflexii/oră la 144 MHz**; observatorii RMOB ai GRAVES pe 143,050 MHz numără de obicei **20 până la 140 de ecouri/oră** (buletinul RMOB, iunie 2018): ordinul de mărime este compatibil, iar diferența este factorul de stație K. (Ec. 44–45 din manual.)

## Următoarele 24 de ore

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Persistență:** valoarea scalată a aceleiași ore din ziua precedentă (sau de acum două zile dacă lipsește), corectată cu variația **indicelui roiurilor pe traseu** I (Σ ZHR × eficiență, vedeți [Calculul eficienței](Efficiency-Calculation-ro#modelul)). Constanta 10 reprezintă fondul sporadic și limitează corecția când indicele este mic. *Alegere a programului (ec. 47 din manual).*

| Panou | Conținut |
|---|---|
| **Măsurat la Collm și scalat la f MHz – ieri și astăzi (UTC)** | Meteori/oră ai radarului din Collm; valorile scalate (portocaliu, scala din dreapta); numărătorile RMOB dacă sunt încărcate (verde, scala din dreapta) |
| **Previziune experimentală pentru următoarele 24 de ore la f MHz pentru …** | Reflexii/oră prevăzute (bare) și indicele roiurilor pe traseu (scala din dreapta) |
| Tabel | Ora UTC · Collm aceeași oră · Scalat · Indicele roiurilor pe traseu · Previziune /oră · **Evaluare** |

**Evaluare:** *bună* când previziunea este de cel puțin 1,3 × media pe 24 de ore, *acceptabilă* de la 0,8 ×, *slabă* sub această valoare. Aceeași previziune apare în cardul **PREVIZIUNE EXPERIMENTALĂ** și în rândul portocaliu din [Calculul eficienței](Efficiency-Calculation-ro) și este baza ecourilor așteptate în fila [Radar GRAVES](GRAVES-Radar-ro#ecouri-așteptate-experimental).

## Comparația cu RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) colectează numărătorile orare de meteori ale observatorilor radio; mulți din Italia ascultă GRAVES pe 143,050 MHz (Planetariul din Veneția, Faenza, Rovereto și alții).

**Citirea fișierelor RMOB.** Sunt acceptate două formate text:

| Format | Aspect | Note |
|---|---|---|
| Fișier lunar (Colorgramme / Spectrum Lab) | un rând pe zi, `day| n| n| …` cu 24 de valori orare | obișnuitul `NAME_MMYYYYrmob.TXT` |
| Tabelul buletinului | antet ` UT |  1   2   3 …`, rânduri `0h|175 166 …` | dacă fișierul conține mai mulți observatori, aceștia sunt citiți unul după altul: folosiți un fișier cu un singur observator |

Luna și anul provin din numele fișierului (`…_MMYYYYrmob…`) sau din antet; altfel se folosește luna curentă (și programul o spune).

**Ajustarea exponentului.** Cu K = 1, din mediana rapoartelor RMOB/Collm pe orele comune (cel puțin 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Alegere a programului (ec. 46 din manual).* Dialogul arată orele comune, raportul median și k; **Da** aplică k (și setează K = 1), **Nu** păstrează k = 3 – apoi ajustați manual K la valoarea sugerată în același dialog.

## RMOB și programele automate

RMOB cere ca **programele automate să nu-i descarce fișierele**. Din acest motiv, **descărcarea automată este dezactivată** la pornire și ar trebui activată **doar după ce ați cerut permisiunea RMOB**. Fără ea puteți folosi oricând **Încarcă fișier RMOB de pe disc...** sau puteți apăsa **Descarcă RMOB acum** când aveți nevoie.

Adresa de descărcare este un șablon în `config.ini` (cheia `rmob_url`, implicit `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, unde `{NOME}` este observatorul și `{MMAAAA}` luna și anul); fișierele descărcate se păstrează în `data/radar/`.
