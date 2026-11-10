[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-BR) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · **Eesti** · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-TW)

# Radari voog

*Sakk: Otse ja reaalajas andmed › Radari voog.*

[![Radari voog](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

See sakk näitab, mida professionaalsed meteoorradarid **praegu** loendavad: **Collmi** SKiYMET-radari (Leipzigi Ülikool / IAP Kühlungsborn, Saksamaa, 36,2 MHz) meteooride tunniloendused ja jälgede kõrgused ning **Sodankylä** radari (SGO, Soome) viimase pildi. Collmi loendused toidavad hinnangut sinu sagedusalale ja [Eksperimentaalseid prognoose](Experimental-Forecasts-et); mõõdetud jälgede kõrgus toidab kogu geomeetriat.

## Juhtnupud

| Juhtnupp | Mida see teeb |
|---|---|
| **Laadi kohe alla** | Kontrollib kõiki välisallikaid korraga. |
| **Kõigi allikate automaatne uuendus iga 5 minuti järel** | Vaikimisi sees. Iga 5 minuti järel kontrollitakse kõiki allikaid ja uuesti laaditakse **ainult muutunud** (*muutumatu (kontrollitud kell … UTC)* / *uued andmed kell … UTC*). |
| **λ astendaja (SM6FHZ)** | Sagedusreegli astendaja k, vaikimisi 3 (1–4). |

## Mida näidatakse

| Paneel | Sisu |
|---|---|
| **Meteoore/tunnis – eile ja täna (UTC)** | Tsüaansinised tulbad = Collmi loendused (kehtivad), punased tulbad = kõrvale jäetud, paks oranž joon = *hinnang sagedusel … MHz* parempoolsel skaalal |
| **Jälgede kõrgused (Collm)** | Meteoore kõrguskilomeetri kohta vahemikus 70 kuni 110 km, koos sagedaseima kõrguse (mood), keskmise, mediaani ja standardhälbega |
| Collmi pilt | Originaalne SKiYMET-graafik, nagu alla laaditud |
| Sodankylä pilt | Sodankylä radari viimane meteooriloenduse pilt (ainult näidatakse; selle vormingut ei loeta) |

Graafikute kohal olev rida ütleb, millal Collmi graafik loeti ja milline vertikaalskaala leiti (*graafikult loetud skaala: 0-… meteoori/tunnis*).

## Kuidas Collmi graafikut loetakse

Collmi graafikul (720 × 720 pikslit, puhtad värvid) on telgede asukohad fikseeritud, kuid radar **kohandab vertikaalskaalat iga päev** mõõdetud väärtustele (nt 0–1,2·10³ 5.11.2026 ja 0–1,0·10³ 6.11.2026, nihutatud jaotiskriipsudega). Seepärast YA-MS:

1. leiab telje pikad jaotiskriipsud;
2. **loeb kõrgeima kriipsu ja nulli sildid**, võrreldes iga märki graafiku punktmaatriksfondiga;
3. võtab iga tunni i (0–47, eile ja täna) jaoks keskmise veeru ja esimese tsüaansinise piksli ülalt, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top ja y0 on kõrgeima kriipsu ja nulli read, N_top kõrgeimalt sildilt loetud väärtus (×1000). Eraldusvõime: umbes 7–8 meteoori tunnis piksli kohta. *Programmi valik (juhendi võrrand 42).*

Kui silti ei õnnestu lugeda, kasutab programm 5.11.2026 kalibreeringut (**kalibreeritud skaala 0-1200 meteoori/tunnis**) ja ütleb seda oranžiga: *Voo vertikaalskaalat ei õnnestu lugeda (ülemine silt: …): väärtusi tuleb kontrollida.* Kui muutub graafiku vorming ise (*Graafiku vorming muutus (…x…): lugemine pole võimalik* või *Voo telgi ei leitud oodatud kohast*), tuleb lugemine uuesti kalibreerida: palun teata sellest (vt [Kaastöö](Contributing-and-Contacts-et)).

### Jälgede kõrgused

Kõrguste histogrammist (n_k meteoori kilomeetril k, keskmine kõrgus h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Juhendi võrrand 43.* Kui **radarilt** on märgitud (juhtnuppude rida 2), saab **moodist** kõigi arvutuste jälgede kõrgus. Kontroll: 5.11.2026 graafik – mood 89,5 km, keskmine 88,6 km, standardhälve 6,8 km, mis kinnitab Cerrotta–Sartori artikli ~90 km (SKiYMET-i keskmine).

Kui kõrguste graafiku skaala muutub, hoiatab programm: *kõrguste statistika (mood, keskmine, mediaan) jääb kehtima, absoluutsed loendused mitte.*

## Hinnang sinu sagedusalale

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

**SM6FHZ** eksperimentaalsed reeglid (VUSHF 2025): peegelduste arv ja intensiivsus skaleeruvad λ³ järgi, kestus λ² järgi (McKinley juures on λ³ ühe jälje võimsus; jälgede arv skaleerub ligikaudu λ^1,5 järgi ja edasihajumisel kasvavad kestused lisaks koos sec²φ-ga: vt [Eksperimentaalsed prognoosid](Experimental-Forecasts-et)). Näidatakse ka IARU 1. regiooni maksimaalset pingi kestust (1000 ms 50 MHz-l, 500 ms 70 MHz-l, 100 ms 144 MHz-l, 13 ms 432 MHz-l). Väärtused on ligikaudsed ja neid tuleb võrrelda eetrikogemusega. Jaama tegur K ja võrdlus RMOB-iga on lehel [Eksperimentaalsed prognoosid](Experimental-Forecasts-et).

## Ilma võrguta

Kui ükski allikas pole kättesaadav, ilmub **üks kord** teade: *Internetiühendus puudub. Radarite ja RMOB-i andmeid ei saa uuendada: programm kasutab viimati salvestatud andmeid ja proovib ise uuesti iga 5 minuti järel.* Allosas olev olekuriba muutub punaseks (*INTERNETIÜHENDUS PUUDUB …*), kuni ühendus taastub (*Ühendus taastatud.*).

## Arhiivid ja allikad

| Fail (kaustas `data/`) | Sisu |
|---|---|
| `flusso_collm.csv` | Collmilt loetud voo tunniarhiiv (juba olemasolevad tunnid uuendatakse) |
| `quote_collm.csv` | Jälgede kõrguste arhiiv |
| `radar/` | Viimati alla laaditud pildid (ja RMOB-failid) |
| `fonti_radar.csv` | Radariallikate aadressid, `attivo=1/0` iga allika lubamiseks/keelamiseks |

| Allikas | Sagedus | Märkused |
|---|---|---|
| Collmi meteoorradar, Leipzigi Ülikool (LIM) ja IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | uuendatakse iga tund minutil 10 UTC; voog eile + täna, kõrguste jaotus |
| Sodankylä Geofüüsika Observatoorium – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | ainult pilt (radarit uuendatakse, projekt DECC) |
| swan.ms (Collmi koopia) | 36,2 MHz | vaikimisi keelatud; kasuta ainult DL1DBC loal |

> Radariandmed kuuluvad vastavatele asutustele (Leipzigi Ülikool / IAP Kühlungsborn, Sodankylä Geofüüsika Observatoorium).
