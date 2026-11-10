[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · **Eesti** · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# GRAVESi radar

*Sakk: Otse ja reaalajas andmed › GRAVESi radar.*

[![GRAVESi radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Mis on GRAVES

**GRAVES** on Prantsuse radar, mis saadab **CW-d sagedusel 143,050 MHz** asukohast **Broye-lès-Pesmes** (47,348° N 5,515° E, lokaator **JN27SI**, umbes 200 m üle merepinna; Wikipedia). Meteoorijäljed alal, mida näevad nii GRAVES kui ka sina, peegeldavad selle signaali sinuni **forward scatteri** abil: kuuled kandesageduse lähedal lühikesi *pinge*. Nii loendavad **RMOB-i** vaatlejad sagedusel 143,050 MHz meteoore tund-tunnilt, ja see on sinu 2 m meteor scatteri jaama jaoks tasuta, alati töötav katsesignaal.

Sakk käsitleb trassi **GRAVES → sina** omaette meteor scatteri trassina: samade funktsioonidega nagu põhitrassi puhul (sama jälgede kõrgus, peaharu elevatsioon ja hot spoti kaugus) arvutab see meteoorivoolude efektiivsuse, soovitatud Hoti ja PREV alad ning kontrollib seejärel, kas see ala on **GRAVESi kiire sees** ja **millal** kiir seda valgustab.

## Ülemine riba

| Juhtnupp | Mida see teeb |
|---|---|
| **Praegu** | Viib arvutuse tagasi reaalajale: tänane kuupäev ja tundide liugur nullis (sakk järgib välju *Arvutuse kuupäev* ja *Tunnid*). |
| **Määra GRAVES DX-iks** | Korrespondendiks saab GRAVES (JN27SI, kõrgus 200 m) ja põhitrass arvutatakse ümber: kõik teised sakid näitavad seejärel GRAVESi trassi. |
| **Kiire järjestus** | *0,8 s sammu kohta · tsükkel 4,8 s (PE1ITR 2021)* (vaikimisi) või *3,2 s sammu kohta · tsükkel 19,2 s (PE1ITR 2007)*. |

## Neli infokaarti

| Infokaart | Sisu |
|---|---|
| **KASULIK ALA GRAVESI KIIRES** | *Jah · sektor X* koos GRAVESist nähtava soovitatud hot spoti asimuudi ja elevatsiooni ning sammuga (1–6); või *Ei: väljaspool sektoreid* / *Ei: GRAVESi horisondi all* / *Ei: kiirest kõrgemal (umbes 25°)* |
| **GRAVES → SINA TRASSI EFEKTIIVSUS PRAEGU** | Trassi indeks Σ ZHR × efektiivsus, parim meteoorivool, valdav pool A/B ja *oodatud kajad ≈ …/tunnis* (eksperimentaalne, vt allpool) |
| **TRASS** | Kaugus GRAVESini; antenn soovitatud Hoti suunas (asimuut ja elevatsioon); GRAVESi otsesuuna asimuut |
| **KIIRE JÄRGMINE MÖÖDUMINE ALA KOHALT** | *praegu · veel … s* või *… s pärast*, samm (nt *B4*), kolm järgmist aega (sekundid minuti sees) ja püütud jälgede osa |

Kui sel hetkel pole ükski meteoorivool kasulik, näitab programm **kiirele sobivaimat** hot spoti (sektorite sees, lõunale kõige lähemal) ja ütleb seda.

## Taevas GRAVESi vaatest

PE1ITR-i ja Bolidozori wiki järgi katavad **neli faasantennimassiivi** lõunataevast asimuudil **90° kuni 270°** neljas **45° sektoris**:

| Sektor | Asimuut GRAVESist |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Iga sektor on jagatud **6 sammuks à 7,5°**, nummerdatud 1 kuni 6 alates väikseimast asimuudist, mida valgustatakse üksteise järel, **kõigis neljas sektoris samal ajal**. Kiir on **elevatsioonis umbes 25° lai**: jälgede kõrgusel katab see värvilise rõnga kahe katkendjoonega ringi vahel (*kiire horisont*). Joonisel: oranžid/roosad punktid = GRAVES → sina trassi PREV alad, roheline joon = sinu jaama suund, punane joon = sinu jaamast soovitatud hot spotini; praegu valgustatud samm on esile tõstetud.

## Ajaline rekonstruktsioon

*AJALINE REKONSTRUKTSIOON · kuupäev UTC* (sama päev mis 24 h tabelis): iga tunni kohta GRAVES → sina trassi efektiivsus, kõige soodsam meteoorivool ja kasulik aken (*hh:00 → hh:00 UTC · n h*), maksimumiga (*max Σ … kell hh:30*) ja punase märgiga *praegu*. All **järgmiste sekundite detailid**: sektori kuus sammu, kasulikku ala valgustav samm ja *võimalik kaja (+0,3 s jälge)*.

### Kiire ajastus

Järjestus on seotud **UTC** ajaga (PE1ITR): praegu valgustatud samm arvutatakse sekunditest alates 00:00 UTC mooduliga tsükkel (86 400 s on nii 4,8 s kui ka 19,2 s kordne). Juhtimisjaam nihutab järjestust mõnikord mõne sammu võrra, seega on detail **prognoos, mida tuleb kuulamisega kinnitada**. Kollane märk **arvuti kell sünkroonitud** tuletab meelde: sünkrooni oma arvuti NTP-serveriga (viga kõige rohkem mõni sekundikümnendik).

### Tuvastustegur

Jälge on kuulda ainult siis, kui kiir seda selle kestel valgustab:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s on alatiheda jälje tüüpiline kestus 143 MHz-l – fikseeritud väärtus, *programmi valik* (SM6FHZ-i λ² reegel skaleerib kestusi sagedusalade vahel, kuid ei anna algväärtust).

### Oodatavad kajad (eksperimentaalne)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

[Eksperimentaalsete prognooside](Experimental-Forecasts-et) prognoos (mis juba sisaldab jaama tegurit K) teisendatakse selle sageduselt f_fc sagedusele 143,050 MHz SM6FHZ reegliga (sama astendaja k), korrigeeritakse kahe trassi meteoorivoolude indeksite suhtega (konstant 10 esindab sporaadilist fooni, nagu prognoosis) ja korrutatakse tuvastusteguriga. Ainult ligikaudne: võrdle RMOB-i vaatlejatega.

## Kuidas kuulata GRAVESi pinge

| Samm | Mida teha |
|---|---|
| Vastuvõtja | **USB sagedusel 143,049 MHz** (toon umbes 1 kHz) või 143,050 MHz, **AGC aeglane või väljas**, helisagedusriba **vähemalt 2,4 kHz** |
| Antenn | GRAVES → sina trassi **soovitatud hot spoti** suunas (infokaart *TRASS*), **madala elevatsiooniga** |
| Waterfall | Pingid on **lühikesed jooned kandesageduse lähedal**; pikad (ületihedad) jäljed on laiemad ja näitavad Doppleri nihet |
| Loendus | RMOB kasutab meteooride tunniloendusteks GRAVESi: **võrdle oma pinge vaatlejatega sagedusel 143,050 MHz** ([Eksperimentaalsed prognoosid](Experimental-Forecasts-et#võrdlus-rmob-iga)) |

## Allikad

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) ja *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozori** wiki, "Graves" – antennimassiivid, sektorid ja kiire ajastus
3. **Wikipedia**, "GRAVES (system)" – saatja Broye-lès-Pesmes'is (47,348° N 5,515° E)
4. **RMOB** – vaatlejad sagedusel 143,050 MHz ([rmob.org](https://www.rmob.org))
5. IC8TEM-i **YAEC** – sakk Radar GRAVES (kavand, millest see sakk on tuletatud)
