[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · **Română** · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# Radar GRAVES

*Filă: Date live și în timp real › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Ce este GRAVES

**GRAVES** este un radar francez care emite **CW pe 143,050 MHz** din **Broye-lès-Pesmes** (47,348° N 5,515° E, locator **JN27SI**, aproximativ 200 m deasupra nivelului mării; Wikipedia). Urmele de meteori din zona pe care o văd atât GRAVES, cât și dumneavoastră îi reflectă semnalul spre dumneavoastră prin **forward scatter**: auziți *ping-uri* scurte aproape de purtătoare. Așa numără observatorii **RMOB** de pe 143,050 MHz meteorii oră de oră și este un semnal de test gratuit, mereu activ, pentru stația dumneavoastră de meteor-scatter pe 2 m.

Fila tratează **GRAVES → dumneavoastră** ca pe un traseu meteor-scatter separat: cu aceleași funcții ca traseul principal (aceeași înălțime a urmei, aceeași elevație a lobului și aceeași distanță a hot spot-ului) calculează eficiența roiurilor, Hot-ul recomandat și zonele PREV, apoi verifică dacă acea zonă este **în interiorul fasciculului GRAVES** și **când** o iluminează fasciculul.

## Bara de sus

| Comandă | Ce face |
|---|---|
| **Acum** | Readuce calculul la timpul real: data de astăzi și cursorul orelor la zero (fila urmează *Data calculului* și *Ore*). |
| **Setează GRAVES ca DX** | Stația DX devine GRAVES (JN27SI, înălțime 200 m) și traseul principal este recalculat: toate celelalte file arată atunci traseul GRAVES. |
| **Secvența fasciculului** | *0,8 s pe pas · ciclu de 4,8 s (PE1ITR 2021)* (implicit) sau *3,2 s pe pas · ciclu de 19,2 s (PE1ITR 2007)*. |

## Cele patru carduri

| Card | Conținut |
|---|---|
| **ZONĂ UTILĂ ÎN FASCICULUL GRAVES** | *Da · sectorul X* cu azimutul și elevația hot spot-ului recomandat văzute de la GRAVES și pasul (1–6); sau *Nu: în afara sectoarelor* / *Nu: sub orizontul GRAVES* / *Nu: deasupra fasciculului (aproximativ 25°)* |
| **EFICIENȚA TRASEULUI GRAVES → DUMNEAVOASTRĂ ACUM** | Indicele traseului Σ ZHR × eficiență, cel mai bun roi, latura predominantă A/B și *ecouri așteptate ≈ …/oră* (experimental, vedeți mai jos) |
| **TRASEU** | Distanța până la GRAVES; antena spre Hot-ul recomandat (azimut și elevație); azimutul direct spre GRAVES |
| **URMĂTOAREA TRECERE A FASCICULULUI PESTE ZONĂ** | *acum · mai sunt … s* sau *peste … s*, pasul (de ex. *B4*), următoarele trei momente (secunde în cadrul minutului) și fracțiunea de urme captate |

Dacă niciun roi nu este util în acel moment, programul arată hot spot-ul **cel mai potrivit pentru fascicul** (în interiorul sectoarelor, cel mai apropiat de sud) și o spune.

## Cerul văzut de la GRAVES

Potrivit lui PE1ITR și wiki-ului Bolidozor, **patru rețele fazate** acoperă cerul sudic de la **90° la 270°** azimut în patru **sectoare de 45°**:

| Sector | Azimut de la GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Fiecare sector este împărțit în **6 pași de 7,5°**, numerotați de la 1 la 6 începând cu azimutul cel mai mic, iluminați unul după altul, **în același moment în toate cele patru sectoare**. Fasciculul are o lățime de aproximativ **25° în elevație**: la înălțimea urmei acoperă inelul colorat dintre cele două cercuri punctate (*orizontul fasciculului*). Pe desen: puncte portocalii/roz = zonele PREV ale traseului GRAVES → dumneavoastră, linia verde = direcția stației dumneavoastră, linia roșie = de la stația dumneavoastră la hot spot-ul recomandat; pasul iluminat acum este evidențiat.

## Reconstituirea cronologiei

*RECONSTITUIREA CRONOLOGIEI · data UTC* (aceeași zi ca tabelul de 24 h): pentru fiecare oră, eficiența traseului GRAVES → dumneavoastră, cel mai favorabil roi și fereastra utilă (*hh:00 → hh:00 UTC · n h*), cu maximul (*max Σ … la hh:30*) și un marcaj roșu *acum*. Dedesubt, **detaliul secundelor următoare**: cei șase pași ai sectorului, pasul care iluminează zona utilă și *ecou posibil (+0,3 s de urmă)*.

### Sincronizarea fasciculului

Secvența este legată de **UTC** (PE1ITR): pasul iluminat acum se calculează din secundele scurse de la 00:00 UTC modulo ciclul (86 400 s este multiplu atât al lui 4,8 s, cât și al lui 19,2 s). Stația de comandă decalează uneori secvența cu câțiva pași, așa că detaliul este o **predicție care trebuie confirmată prin ascultare**. Eticheta galbenă **Ceasul PC sincronizat** vă reamintește: sincronizați PC-ul cu un server NTP (eroare de cel mult câteva zecimi de secundă).

### Factorul de detecție

O urmă se aude doar dacă fasciculul o iluminează cât timp durează:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s este o durată tipică a unei urme subdense la 143 MHz – o valoare fixă, *alegere a programului* (regula λ² a lui SM6FHZ scalează duratele între benzi, dar nu dă o valoare de pornire).

### Ecouri așteptate (experimental)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Previziunea din [Previziuni experimentale](Experimental-Forecasts-ro) (care conține deja factorul de stație K) este scalată de la frecvența sa f_fc la 143,050 MHz cu regula SM6FHZ (același exponent k), corectată cu raportul dintre indicii roiurilor celor două trasee (constanta 10 reprezintă fondul sporadic, ca în previziune) și înmulțită cu factorul de detecție. Doar orientativ: comparați cu observatorii RMOB.

## Cum să auziți ping-urile GRAVES

| Pas | Ce trebuie făcut |
|---|---|
| Receptor | **USB pe 143,049 MHz** (ton la aproximativ 1 kHz) sau 143,050 MHz, **AGC lent sau dezactivat**, lățime de bandă audio de **cel puțin 2,4 kHz** |
| Antenă | Spre **hot spot-ul recomandat** al traseului GRAVES → dumneavoastră (cardul *TRASEU*), la **elevație joasă** |
| Waterfall | Ping-urile sunt **linii scurte aproape de purtătoare**; urmele lungi (supradense) sunt mai late și arată efect Doppler |
| Numărare | RMOB folosește GRAVES pentru numărătorile orare de meteori: **comparați ping-urile dumneavoastră cu observatorii de pe 143,050 MHz** ([Previziuni experimentale](Experimental-Forecasts-ro#comparația-cu-rmob)) |

## Surse

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) și *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki-ul **Bolidozor**, „Graves” – rețele, sectoare și sincronizarea fasciculului
3. **Wikipedia**, „GRAVES (system)” – emițătorul de la Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observatorii de pe 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** de IC8TEM – fila GRAVES Radar (macheta din care derivă această filă)
