[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · **Eesti** · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [ไทย](Experimental-Forecasts-th) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Eksperimentaalsed prognoosid

*Sakk: Prognoosarvutus › Eksperimentaalsed prognoosid.*

[![Eksperimentaalsed prognoosid](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

See sakk muudab **Collmi radari (36,2 MHz)** meteooriloendused hinnanguks **peegelduste arvu kohta tunnis amatöörsagedusalal** (vaikimisi 144 MHz, mis tahes sagedus 28 kuni 1300 MHz), prognoosib sinu trassi **järgmised 24 tundi** ja võimaldab hinnangut **võrrelda** **RMOB-i** vaatlejaga – näiteks sellisega, kes kuulab GRAVESi sagedusel 143,050 MHz.

> Kõik siin on **eksperimentaalne**: sagedusreegel on empiiriline ja jaama tegur sõltub sinu jaamast. Kasuta numbreid tundide ja päevade võrdlemiseks ning kontrolli neid eetris.

## Juhtnupud

| Juhtnupp | Vaikimisi | Mida see teeb |
|---|---|---|
| **Sihtsagedus MHz** | 144 | Prognoosi sagedus (28–1300 MHz) |
| **λ^k astendaja** | 3 | Sagedusreegli astendaja k (SM6FHZ: 3) |
| **Jaama tegur K** | 1 | Arvestab vastuvõtvat jaama (võimsus, antennid); tuletatakse võrdlusest RMOB-i vaatlejaga samal sagedusalal |
| **Laadi RMOB-fail kettalt...** | | Loeb RMOB-i igakuise tekstifaili (vt allpool) |
| **Leia astendaja RMOB-failist** | | Sobitab k Collmi ja RMOB-i ühiste tundide põhjal |
| **RMOB-i vaatleja** | tühi | Vaatleja nimi nii, nagu see on failinimes (nt `NAME_112026rmob.TXT` → `NAME`) |
| **Laadi RMOB kohe alla** | | Laadib selle vaatleja jooksva kuu faili ühe korra alla |
| **automaatne allalaadimine iga 5 minuti järel (lülita sisse ainult RMOB-i loal)** | **väljas** | Vt [RMOB ja automaatprogrammid](#rmob-ja-automaatprogrammid) |

Juhtnuppude all olev oranž rida näitab reeglit praeguste numbritega, nt *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, kestuse skaleerimist ja IARU maksimaalset pingi kestust sellel sagedusel.

## Radarilt amatöörsagedusalale

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Allikas:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45. Nordic VUSHF, mai 2025 – peegelduste arv ja intensiivsus skaleeruvad **λ³** järgi, kestus **λ²** järgi (432 MHz on 14–15 dB madalam kui 144 MHz ja kestab 1/9). **Kontroll:** λ³ sõltuvus on sama mis McKinley alatiheda jälje võrrandis. Kui k = 3, muutuvad Collmi 1000 meteoori tunnis umbes **16 peegelduseks tunnis 144 MHz-l**; GRAVESi RMOB-i vaatlejad sagedusel 143,050 MHz loendavad tavaliselt **20 kuni 140 kaja tunnis** (RMOB-i bülletään, juuni 2018): suurusjärk on ühilduv ja erinevus on jaama tegur K. (Juhendi võrrandid 44–45.)

## Järgmised 24 tundi

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Püsivus:** eelmise päeva sama tunni skaleeritud väärtus (või puudumisel kaks päeva tagasi), korrigeeritud **trassi meteoorivoolude indeksi** I muutusega (Σ ZHR × efektiivsus, vt [Efektiivsuse arvutus](Efficiency-Calculation-et#mudel)). Konstant 10 esindab sporaadilist fooni ja piirab parandust, kui indeks on väike. *Programmi valik (juhendi võrrand 47).*

| Paneel | Sisu |
|---|---|
| **Mõõdetud Collmis ja teisendatud sagedusele f MHz – eile ja täna (UTC)** | Collmi radari meteoore tunnis; skaleeritud väärtused (oranž, parem skaala); RMOB-i loendused, kui laaditud (roheline, parem skaala) |
| **Järgmise 24 tunni eksperimentaalne prognoos sagedusel f MHz: …** | Prognoositud peegeldused tunnis (tulbad) ja trassi meteoorivoolude indeks (parem skaala) |
| Tabel | UTC aeg · Collm samal tunnil · Teisendatud · Trassi meteoorivoolude indeks · Prognoos /tunnis · **Hinnang** |

**Hinnang:** *hea*, kui prognoos on vähemalt 1,3 × 24 tunni keskmine, *keskmine* alates 0,8 ×, *nõrk* sellest allpool. Sama prognoos ilmub infokaardil **EKSPERIMENTAALNE PROGNOOS** ja [Efektiivsuse arvutuse](Efficiency-Calculation-et) oranžis reas ning see on oodatavate kajade alus sakil [GRAVESi radar](GRAVES-Radar-et#oodatavad-kajad-eksperimentaalne).

## Võrdlus RMOB-iga

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) kogub raadiovaatlejate meteooride tunniloendusi; paljud Itaalias kuulavad GRAVESi sagedusel 143,050 MHz (Veneetsia planetaarium, Faenza, Rovereto jt).

**RMOB-failide lugemine.** Aktsepteeritakse kahte tekstivormingut:

| Vorming | Välimus | Märkused |
|---|---|---|
| Kuufail (Colorgramme / Spectrum Lab) | üks rida päeva kohta, `day| n| n| …` 24 tunniväärtusega | tavaline `NAME_MMYYYYrmob.TXT` |
| Bülletääni tabel | päis ` UT |  1   2   3 …`, read `0h|175 166 …` | kui failis on mitu vaatlejat, loetakse need järjest: kasuta ühe vaatlejaga faili |

Kuu ja aasta võetakse failinimest (`…_MMYYYYrmob…`) või päisest; muidu kasutatakse jooksvat kuud (ja programm ütleb seda).

**Astendaja sobitamine.** K = 1 korral RMOB/Collm suhete mediaanist ühistel tundidel (vähemalt 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Programmi valik (juhendi võrrand 46).* Dialoog näitab ühiseid tunde, suhte mediaani ja k-d; **Jah** rakendab k (ja seab K = 1), **Ei** jätab k = 3 – siis reguleeri K käsitsi samas dialoogis soovitatud väärtusele.

## RMOB ja automaatprogrammid

RMOB palub, et **automaatprogrammid selle faile ei laadiks**. Seetõttu on **automaatne allalaadimine** alguses **väljas** ja selle tohib sisse lülitada **ainult pärast RMOB-ilt loa küsimist**. Ilma selleta saad alati kasutada nuppu **Laadi RMOB-fail kettalt...** või vajutada vajadusel **Laadi RMOB kohe alla**.

Allalaadimisaadress on mall failis `config.ini` (võti `rmob_url`, vaikimisi `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kus `{NOME}` on vaatleja ning `{MMAAAA}` kuu ja aasta); alla laaditud failid hoitakse kaustas `data/radar/`.
