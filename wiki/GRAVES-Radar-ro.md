[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · **Română** · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [ไทย](GRAVES-Radar-th) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# Radar GRAVES

*Fila: Live și date în timp real › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Ce este GRAVES

**GRAVES** este un radar francez care emite **CW pe 143,050 MHz** de la **Broye-lès-Pesmes** (47,348° N 5,515° E, locator **JN27SI**, circa 200 m deasupra nivelului mării; Wikipedia). Urmele meteorice din zona pe care o văd atât GRAVES, cât și tu îi reflectă semnalul spre tine prin **forward scatter**: auzi *ping-uri* scurte lângă purtătoare. Așa numără observatorii **RMOB** de pe 143,050 MHz meteorii oră de oră, iar pentru stația ta de meteor scatter pe 2 m este un semnal de test gratuit și mereu prezent.

Fila tratează **GRAVES → tu** ca pe un traseu meteor scatter de sine stătător: cu aceleași funcții ca traseul principal (aceeași altitudine a urmelor, aceeași elevație a lobului și aceeași distanță a hot spot-urilor) calculează eficiența roiurilor, Hot-ul recomandat și zonele PREV, apoi verifică dacă acea zonă este **în fasciculul GRAVES** și **când** o iluminează fasciculul.

## Bara de sus

| Comandă | Ce face |
|---|---|
| **Acum** | Readuce ora bolții cerești la timpul real (fila urmează cursorul *Ora bolții cerești*). |
| **Pune GRAVES ca DX** | Corespondentul devine GRAVES (JN27SI, altitudine 200 m), iar traseul principal se recalculează: toate celelalte file arată apoi traseul GRAVES. |
| **Secvența fasciculului** | *0,8 s pe pas · ciclu 4,8 s (PE1ITR 2021)* (implicit) sau *3,2 s pe pas · ciclu 19,2 s (PE1ITR 2007)*. |

## Cele patru casete

| Casetă | Conținut |
|---|---|
| **ZONA UTILĂ ÎN FASCICULUL GRAVES** | *Da · sector X* cu azimutul și elevația hot spot-ului recomandat văzute de la GRAVES și pasul (1–6); sau *Nu: în afara sectoarelor* / *Nu: sub orizontul GRAVES* / *Nu: deasupra fasciculului (circa 25°)* |
| **EFICIENȚA TRASEULUI GRAVES → TU ACUM** | Indicele traseului Σ ZHR × eficiență, cel mai bun roi, latura predominantă A/B și *ecouri așteptate ≈ …/oră* (experimental, vezi mai jos) |
| **TRASEU** | Distanța până la GRAVES; antena spre Hot-ul recomandat (azimut și elevație); azimutul direct spre GRAVES |
| **URMĂTOAREA TRECERE A FASCICULULUI PESTE ZONĂ** | *acum · încă … s* sau *peste … s*, pasul (de ex. *B4*), următoarele trei momente (secundele din minut) și fracțiunea de urme prinse |

Dacă niciun roi nu este util în acel moment, programul arată hot spot-ul **cel mai potrivit pentru fascicul** (în interiorul sectoarelor, cel mai apropiat de sud) și o spune.

## Cerul văzut de GRAVES

Potrivit lui PE1ITR și wiki-ului Bolidozor, **patru rețele fazate** acoperă cerul sudic de la **90° la 270°** azimut în patru **sectoare de 45°**:

| Sector | Azimut de la GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Fiecare sector este împărțit în **6 pași de 7,5°**, numerotați de la 1 la 6 începând cu azimutul cel mai mic, iluminați unul după altul, **în același moment în toate cele patru sectoare**. Fasciculul are o lățime de circa **25° în elevație**: la altitudinea urmelor acoperă inelul colorat dintre cele două cercuri punctate (*orizontul fasciculului*). Pe desen: puncte portocalii/roz = zonele PREV ale traseului GRAVES → tu, linie verde = direcția stației tale, linie roșie = de la stația ta la hot spot-ul recomandat; pasul iluminat acum este evidențiat.

## Reconstituire cronologică

*RECONSTITUIRE CRONOLOGICĂ · dată UTC* (aceeași zi ca tabelul 24 h): pentru fiecare oră, eficiența traseului GRAVES → tu, roiul cel mai favorabil și fereastra utilă (*hh:00 → hh:00 UTC · n h*), cu maximul (*max Σ … la hh:30*) și un marcaj roșu *acum*. Dedesubt, **detaliul secundelor următoare**: cei șase pași ai sectorului, pasul care iluminează zona utilă și *ecou posibil (+0,3 s de urmă)*.

### Temporizarea fasciculului

Secvența este legată de **UTC** (PE1ITR): pasul iluminat acum se calculează din secundele scurse de la 00:00 UTC modulo ciclul (86 400 s este multiplu atât de 4,8 s, cât și de 19,2 s). Stația de comandă deplasează uneori secvența cu câțiva pași, așa că detaliul este o **prognoză de confirmat prin ascultare**. Pastila galbenă **ceasul PC-ului sincronizat** îți amintește: sincronizează-ți PC-ul cu un server NTP (eroare de cel mult câteva zecimi de secundă).

### Factorul de detecție

O urmă se aude doar dacă fasciculul o iluminează cât timp durează:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s este o durată tipică a unei urme subdense la 143 MHz – o valoare fixă, *alegere a programului* (regula λ² a lui SM6FHZ scalează duratele între benzi, dar nu dă o valoare de pornire).

### Ecouri așteptate (experimental)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Prognoza din [Implementare experimentală a prognozelor](Experimental-Forecasts-ro) (care conține deja factorul stației K) este transpusă de la frecvența ei f_fc la 143,050 MHz cu regula SM6FHZ (același exponent k), corectată cu raportul indicilor roiurilor celor două trasee (constanta 10 reprezintă fondul sporadic, ca în prognoză) și înmulțită cu factorul de detecție. Doar orientativ: compară cu observatorii RMOB.

## Cum se ascultă ping-urile GRAVES

| Pas | Ce este de făcut |
|---|---|
| Receptor | **USB pe 143,049 MHz** (notă la circa 1 kHz) sau 143,050 MHz, **AGC lent sau oprit**, bandă audio de **cel puțin 2,4 kHz** |
| Antenă | Spre **hot spot-ul recomandat** al traseului GRAVES → tu (caseta *TRASEU*), cu **elevație mică** |
| Waterfall | Ping-urile sunt **linii scurte lângă purtătoare**; urmele lungi (overdense) sunt mai late și arată efectul Doppler |
| Număr | RMOB folosește GRAVES pentru numărătorile orare ale meteorilor: **compară ping-urile tale cu observatorii de pe 143,050 MHz** ([Implementare experimentală a prognozelor](Experimental-Forecasts-ro#comparația-rmob)) |

## Surse

1. Rob Hardenberg **PE1ITR**, *„The 143.050 MHz Graves Radar, a VHF Beacon”* (DUBUS 4/2007) și *„Graves Radar Update April 2021”* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki-ul **Bolidozor**, „Graves” – rețele, sectoare și temporizarea fasciculului
3. **Wikipedia**, „GRAVES (system)” – emițător la Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observatori pe 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** de IC8TEM – fila Radar GRAVES (schița din care derivă această filă)
