[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · **Latviešu** · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Eksperimentālas prognozes

*Cilne: Prognozes aprēķins › Eksperimentālas prognozes.*

[![Eksperimentālas prognozes](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Šī cilne pārvērš **Collm radara (36,2 MHz)** meteoru skaitu par **atstarojumu skaita stundā novērtējumu amatieru joslā** (noklusējumā 144 MHz, jebkura frekvence no 28 līdz 1300 MHz), prognozē **nākamās 24 stundas** tavai trasei un ļauj **salīdzināt** novērtējumu ar **RMOB** novērotāju – piemēram, tādu, kas klausās GRAVES 143,050 MHz.

> Viss šeit ir **eksperimentāls**: frekvences likums ir empīrisks, un stacijas koeficients atkarīgs no tavas stacijas. Izmanto skaitļus, lai salīdzinātu stundas un dienas, un pārbaudi tos ēterā.

## Vadība

| Vadīkla | Noklusējums | Ko tā dara |
|---|---|---|
| **Mērķa frekvence MHz** | 144 | Prognozes frekvence (28–1300 MHz) |
| **λ^k kāpinātājs** | 3 | Frekvences likuma kāpinātājs k (SM6FHZ: 3) |
| **Stacijas koeficients K** | 1 | Ņem vērā uztverošo staciju (jauda, antenas); iegūst, salīdzinot ar RMOB novērotāju tajā pašā joslā |
| **Ielādēt RMOB failu no diska...** | | Nolasa RMOB mēneša teksta failu (sk. zemāk) |
| **Iegūt kāpinātāju no RMOB faila** | | Pielāgo k pēc Collm un RMOB kopējām stundām |
| **RMOB novērotājs** | tukšs | Novērotāja vārds, kā tas redzams faila nosaukumā (piem. `NAME_112026rmob.TXT` → `NAME`) |
| **Lejupielādēt RMOB tagad** | | Vienreiz lejupielādē šī novērotāja kārtējā mēneša failu |
| **automātiska lejupielāde ik pēc 5 minūtēm (ieslēgt tikai ar RMOB atļauju)** | **izslēgta** | Sk. [RMOB un automātiskās programmas](#rmob-un-automātiskās-programmas) |

Oranžā rinda zem vadīklām rāda likumu ar pašreizējiem skaitļiem, piem. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, ilguma pārrēķinu un IARU maksimālo pingu šajā frekvencē.

## No radara uz amatieru joslu

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Avots:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, 2025. gada maijs – atstarojumu skaits un intensitāte mainās ar **λ³**, ilgums ar **λ²** (432 MHz ir 14–15 dB zem 144 MHz un ilgst 1/9). **Pārbaude:** McKinley vienādojumā λ³ ir vienas zema blīvuma sliedes jauda, nevis sliežu skaits; ar masas indeksu 2 sliežu skaits virs fiksēta sliekšņa mainās aptuveni ar λ^1,5 (IZ5TEK; OH5IY). Programma saglabā k = 3, SM6FHZ eksperimentālo likumu, un to norāda; tavai stacijai pareizo k dod salīdzinājums ar RMOB. Tiešajā izkliedē ilgums turklāt pieaug ar sec²φ (McKinley; OH5IY): Collm mēra atpakaļizkliedē (φ = 0), tāpēc prognoze reizina ar sec²φ trases viduspunktā (×4 pie 60°, ×8,5 pie 70°, ×33 pie 80°). Ar k = 3 1000 meteori stundā Collm kļūst par apmēram **16 atstarojumiem stundā 144 MHz**; RMOB GRAVES novērotāji 143,050 MHz parasti saskaita **no 20 līdz 140 atbalsīm stundā** (RMOB biļetens, 2018. gada jūnijs): lieluma kārta ir saderīga, un starpība ir stacijas koeficients K. (Rokasgrāmatas 44.–45. vien.)

## Nākamās 24 stundas

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Persistence:** iepriekšējās dienas (vai, ja tās trūkst, aizvakardienas) tās pašas stundas pārrēķinātā vērtība, koriģēta ar **trases plūsmu indeksa** I izmaiņu (Σ ZHR × efektivitāte, sk. [Efektivitātes aprēķins](Efficiency-Calculation-lv#modelis)). Konstante 10 attēlo sporādisko fonu un ierobežo korekciju, kad indekss ir mazs. *Programmas izvēle (rokasgrāmatas 47. vien.).*

| Panelis | Saturs |
|---|---|
| **Mērīts Collm un pārrēķināts uz f MHz – vakar un šodien (UTC)** | Collm radara meteori stundā; pārrēķinātās vērtības (oranžā, skala pa labi); RMOB skaiti, ja ielādēti (zaļā, skala pa labi) |
| **Eksperimentāla prognoze nākamajām 24 stundām pie f MHz: …** | Prognozētie atstarojumi stundā (joslas) un trases plūsmu indekss (skala pa labi) |
| Tabula | UTC laiks · Collm tajā pašā stundā · Pārrēķināts · Trases plūsmu indekss · Prognoze /stundā · **Vērtējums** |

**Vērtējums:** *labs*, ja prognoze ir vismaz 1,3 × 24 stundu vidējā, *vidējs* no 0,8 ×, *vājš* zem tā. Tā pati prognoze parādās kartītē **EKSPERIMENTĀLA PROGNOZE** un cilnes [Efektivitātes aprēķins](Efficiency-Calculation-lv) oranžajā rindā, un tā ir gaidāmo atbalsu pamatā cilnē [GRAVES radars](GRAVES-Radar-lv#gaidāmās-atbalsis-eksperimentāli).

## Salīdzinājums ar RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) vāc radio novērotāju meteoru skaitus pa stundām; daudzi Itālijā klausās GRAVES 143,050 MHz (Venēcijas planetārijs, Faenca, Roverēto un citi).

**RMOB failu nolasīšana.** Tiek pieņemti divi teksta formāti:

| Formāts | Izskats | Piezīmes |
|---|---|---|
| Mēneša fails (Colorgramme / Spectrum Lab) | viena rinda dienā, `day| n| n| …` ar 24 stundu vērtībām | parastais `NAME_MMYYYYrmob.TXT` |
| Biļetena tabula | galvene ` UT |  1   2   3 …`, rindas `0h|175 166 …` | ja failā ir vairāki novērotāji, tie tiek nolasīti viens pēc otra: izmanto failu ar vienu novērotāju |

Mēnesis un gads tiek ņemti no faila nosaukuma (`…_MMYYYYrmob…`) vai no galvenes; citādi tiek izmantots pašreizējais mēnesis (un programma to paziņo).

**Kāpinātāja pielāgošana.** Ar K = 1, no RMOB/Collm attiecību mediānas kopējās stundās (vismaz 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Programmas izvēle (rokasgrāmatas 46. vien.).* Dialogs rāda kopējās stundas, attiecību mediānu un k; **Jā** piemēro k (un iestata K = 1), **Nē** saglabā k = 3 – tad pielāgo K ar roku vērtībai, ko iesaka tas pats dialogs.

## RMOB un automātiskās programmas

RMOB lūdz **automātiskās programmas neielādēt tā failus**. Tāpēc **automātiskā lejupielāde** sākumā ir **izslēgta**, un to drīkst ieslēgt **tikai pēc atļaujas saņemšanas no RMOB**. Bez tās vienmēr var izmantot **Ielādēt RMOB failu no diska...** vai nospiest **Lejupielādēt RMOB tagad**, kad tas vajadzīgs.

Lejupielādes adrese ir veidne failā `config.ini` (atslēga `rmob_url`, noklusējumā `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kur `{NOME}` ir novērotājs un `{MMAAAA}` – mēnesis un gads); lejupielādētie faili tiek glabāti mapē `data/radar/`.
