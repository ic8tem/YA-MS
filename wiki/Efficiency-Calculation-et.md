[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · **Eesti** · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Efektiivsuse arvutus

*Sakk: Prognoosarvutus › Efektiivsuse arvutus.*

[![Efektiivsuse arvutus](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Meteoorivoolu **efektiivsus** näitab protsentides, kui palju selle radiandi asend võimaldab peegeldusi **sinu** trassil. Mõiste pärineb Ilkka **OH5IY**-lt (MS-Soft) ja on üle võetud Cerrotta–Sartori artiklis: efektiivsuse maksimum ei lange kokku visuaalse maksimumiga (ZHR), sest see sõltub sellest, kus radiant kahe jaama suhtes asub. DL5MCG MCG_MS rakendab sama ideed neljale fikseeritud suunale; YA-MS arvutab selle kahe lokaatori vahelise **tegeliku trassi** jaoks.

See sakk näitab efektiivsust tund-tunnilt päeval, mis on valitud väljal *Arvutuse kuupäev (UTC)* (väärtused iga tunni poole peal).

## Ülevaatekaardid

| Infokaart | Sisu |
|---|---|
| **PÄEVA PARIM AEG** | Kõrgeima trassi indeksiga tund, indeks ja valdav pool (A/B koos protsendiga) |
| **KÕIGE SOODSAM METEOORIVOOL** | Päeva suurima ZHR × efektiivsusega meteoorivool, selle efektiivsus, tund ja pool ning **parim suund** (radiandi asimuut +90° / −90°) |
| **PRAEGU · 1, 3, 6, 12 JA 24 TUNNI PÄRAST** | iga horisondi jaoks seal algava tunni keskmine (neli proovi): teekonna indeks, valdav pool, kõige rohkem panustav vool ja radari andmete olemasolul eksperimentaalse prognoosi peegeldused tunnis. Kastis PRAEGU näidatakse radari andmeteta soovitatud Hot. Uueneb iga minut. |

Need kastid on ribas ajarea all, sakkide kohal, alati nähtaval ka kokku volditud käsuridade korral: vasakul valitud päeva kaks kasti, siis kuus prognoosihorisonti, mis algavad praegusest hetkest.

Infokaartide all selgitab riba tähti A ja B (vt allpool).

## Graafik

*Tunnipõhine efektiivsus: …, … (UTC, väärtused poole tunni ajal).* Kuni viie meteoorivoolu kohta: efektiivsus % pideva joonena ja DH9GCD valem sama värvi punktiirjoonena; **trassi indeks** siniste tulpadena parempoolsel skaalal.

## Tunnitabel

Üks rida iga sel päeval aktiivse meteoorivoolu kohta (sorteeritud ZHR järgi), 24 veergu tundide jaoks (UTC):

| Lahter | Tähendus |
|---|---|
| `63A` | efektiivsus 63 %, enamik peegeldusi poolelt **A** |
| `41B` | efektiivsus 41 %, pool **B** |
| tühi | efektiivsus alla 1 % |
| `…↑` | radiant on sel tunnil sinu jaamast **üle 70°** (liiga kõrgel) |
| kollane tekst | efektiivsus ≥ 50 % |

- **A** = **vasakul**, vaadates oma jaamast korrespondendi poole (Hot A ala); **B** = **paremal** (Hot B ala). Antenni tasub keerata **10–30° sellele poole** (külghajumine, Cerrotta–Sartori artikkel).
- **Helesinised read** (*DH9GCD %*, iga meteoorivoolu all): DH9GCD valem võrdluseks.
- **Rida Σ**: *Trassi indeks (ZHR×efekt.)*.
- **Oranž rida** (*Prognoos … MHz (peegl./tunnis)*): eksperimentaalne prognoos tundide jaoks, mille kohta see on olemas (täna ja osa homsest).

## Mudel

Kõik sammud on [arvutusjuhendis](Efficiency-Explanation-et) (`doc/YA-MS_manuale_calcoli.docx`, 5. peatükk). Lühidalt:

**1. Peegelpeegeldus.** Jälg saadab signaali A-st B-sse ainult siis, kui see puutub ellipsoidi, mille fookustes on A ja B (McKinley 1961). Meteoorivoolu jäljed on paralleelsed radiandi suunaga ŝ (artikkel; McKinley). Iga E-kihi punkti P jaoks, ühikvektoritega jaamade suunas:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Sama seadus on DJ5HG QTFGUI ja tema teksti *"Die Geometrie von Meteorscatterverbindungen"* (2004) aluseks: jälg hajutab koonusele, mille teljeks on jälg ise, ja ainult koonusel asuv vastuvõtja kuuleb seda. Ideaalse jälje puhul on koonuse sein väga õhuke (tuhandete lainepikkuste pikkune kiirgur); programm aktsepteerib tingimust Gaussi tolerantsiga σ = 0,05 rad (umbes 3°), mis esindab seda, mida ideaalne koonus ei näe: meteoorivoolude radiantide hajuvust (GMN-i mõõtmistel 0,3–1,4°), tuule painutatud jälgi ja nende lõplikku pikkust – *programmi valik*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Iga punkti kaal.** Alatiheda jälje võimsus (McKinley; ITU-R P.843, võrrand 3), φ = pool hajumisnurgast (piiratud 85°-ga, *valik*), β = nurk jälje ja levitasandi A-P-B vahel, p̂ = selle tasandi ühiknormaal:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Valik „β-nurk jälje ja trassi vahel (täielik McKinley)“** (vaikimisi sees, ettevaatlik seadistus). Sees: levitasandit ristuvad jäljed on 10–15 dB vähem väärt kui selles asuvad, nii et ühtegi jälge ei ülehinnata. Väljas: iga jälge kaalutakse nii, nagu asuks see tasandis (β = 0, kaal koos cos²φ-ga), nagu kuni versioonini 1.6. *Kontroll:* 1000 km trassil on ilma β-ta parim radiandi asimuut trassist 15°–90° kaugusel sõltuvalt radiandi elevatsioonist (30°, kui radiant on 30° kõrgusel, risti trassiga, kui radiant on 60° kõrgusel), ja ristisuunaline radiant on 30° elevatsioonil 67 % väärt; β-ga on parim radiant alati piki trassi ja ristisuunaline langeb 15 %-ni. β-ga kaob SM6FHZ / DH9GCD parima suuna reegel; β jääb valikuks, vaikimisi sees, sest see annab kõige ettevaatlikumad väärtused, ja selle väljalülitamine toob reegli tagasi.

Punkti jõudvate meteooride arv on võrdeline seal radiandi elevatsiooni siinusega (ŝ·û_P), sama parandus, mida IMO kasutab ZHR-i jaoks.

**Valik „Pikemad jäljed madala radiandiga (DJ5HG)“** (märkeruut graafiku kohal, vaikimisi väljas, kohtspikriga): DJ5HG märgib, et madala radiandi korral langeb ruutkilomeetrile vähem meteoore, kuid jäljed on pikemad (kuni 100 km kasutatavat) ja täidavad peegeldumisseadust sagedamini. Kui valik on sees, muutub kaal väärtuseks min(sin El, 15/100): kasutatav kihi paksus, 15 km, jagatuna elevatsiooni siinusega annab jälje pikkuse, piiratuna 100 km-ga. Umbes 9° kohal tühistavad kaks mõju teineteist. Väljas jääb arvutus ettevaatlikuks.

**Arvutuse seadistus** (samas reas, raadionupud): **Ettevaatlik** (vaikimisi, kõige ettevaatlikumad väärtused: jälgede kõrgus radarilt, tavalised jäljed, β sees), **Nagu DJ5HG** (102 km, pikemad jäljed, β) ja **Kohandatud**, mis valitakse automaatselt, kui muudad käsitsi kõrgust, märkeruutu *radarilt*, pikemate jälgede valikut või β-d.

**3. Summa ja protsent.** Punktid iga 15 km järel jälgede kõrgusel, mida mõlemad jaamad näevad horisondist kõrgemal ja mida kaalutakse mõlema antenni vertikaalse suunadiagrammiga (kast *antenni suunadiagramm*, vaikimisi sees; väljas ainult keila kõrgusnurgast kõrgemad punktid) (*valik*). 100 % on radiandi soodsaim asend selle teekonna jaoks:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F arvutatakse iga trassi jaoks üks kord suundade võrgustikul (asimuut iga 5°, elevatsioon iga 2,5° järel) ja interpoleeritakse.

**Efektiivsus dB-des (DJ5HG viide).** Protsent on suhteline ainult selle trassi parima radiandi asendi suhtes. Erinevate trasside võrdlemiseks annab programm efektiivsuse ka dB-des DJ5HG fikseeritud viite suhtes: 0 dB on 1000 km pikkuse ekvaatorit ületava põhja–lõuna trassi maksimum, kui radiant on pööripäeval taevaekvaatoril, arvutatuna sama kõrguse ja samade kaaludega. DJ5HG annab oma väärtuste täpsuseks parem kui 6 dB.

**4. Pool ja indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Tabelis olev täht on suurema osaga pool. *Programmi valikud (juhendi võrrandid 32–33).*

## DH9GCD võrdlus

Parima suuna esmased allikad on Eshleman & Mlodnosky ja Meeks & James (Proc. IRE, 1957), Hines (1955) ning selle eksperimentaalne kontroll Forsythi, Hinesi & Vogani poolt (1955): kasulikud on ainult radiandid taeva poolringil, mis on risti hajumisnurga poolitajaga, jälgede arv kasvab koos sin El-ga ning keskpunkti lähedal langevad kasulikud jäljed umbes H·tan El võrra külje peale, radiandile vastaspoolele. DJ5HG lisab reservatsiooni: **madala** radiandi korral täpselt piki trassi annab McKinley valem tugevaid signaale (Hamburg–Narvik, kvadrantiidid, umbes 19 UTC), seega „trassiga joondatud radiant = peaaegu null“ kehtib ainult kõrge radiandi kohta; programm jääb ettevaatlikuks ja näitab hoiatust *MADAL RADIANT PIKI TRASSI*.

Sõltumatu kontroll: **DH9GCD** parima suuna valem, mida vahendas **DF5HC** (DARC-i konverents, jaanuar 2018) – sellel puudub avaldatud esmane allikas –, kus El ja Az on sinu jaamast nähtava radiandi elevatsioon ja asimuut ning P korrespondendi asimuut:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

See on maksimaalne, kui radiant on 45° kõrgusel ja trassiga risti. DF5HC peab radianti alla 20° liiga madalaks ja **üle 70° liiga kõrgeks**: need tunnid saavad tabelis ↑ ja [Taevavõlvis](Sky-View-et#hoiatused) hoiatuse. Valem ignoreerib kaugust ja kõrgusi, kuid on hea võrdlusalus.

## Kontrollid

| Kontroll | Tulemus |
|---|---|
| SM6FHZ reegel (VUSHF 2025): parim trass on radiandi asimuudiga risti, suund = radiandi az ±90°, tolerants ±40–50° | Mudel reprodutseerib selle; kui radiant on trassiga joondatud ja taevas kõrgel, on efektiivsus peaaegu null |
| DJ5HG QTFGUI, Hamburg JO53IM – Barcelona, Kvadrantiidid, 4. jaanuar (selle juhendi näide) | QTFGUI: 07:00 suund 252°, −8 dB; 08:00 peegeldusala puudub; 09:00 suund 168°, −4 dB. YA-MS (kõrgus 102 km nagu QTFGUI-s): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Kõik kolm meetodit näevad kella 08:00 auku, kui radiant on peaaegu seniidis |
| DJ5HG kõverad (*Die Geometrie…*, Bild 8–9: Hamburgist ja Münchenist, kvadrantiidid, 4. jaanuar; graafikult loetud, umbes ±0,5 dB ja ±15 min) võrrelduna automaatse testiga `--prova-dj5hg` (üks väärtus tunnis) | Ajad: auk, kui radiant on seniidi lähedal, langeb samadele tundidele (Barcelona 07:30–08:30 vs 07–09; Sofia 06:36–07:48 vs 07–08; Narvik 07–08:30 vs 07–09); Moskva on mõlemas 03–10 suletud, avatud Hamburgist umbes kella 02:30-ni ja Münchenist umbes kella 00:30-ni, nagu DJ5HG kirjutab. Suunad: 2–10° erinevus. Tasemed ja kuju 102 km juures (keskmine ja RMS-erinevus kõveratest): β-ta, pikemate jälgedeta −1,6 / 4,0 dB; pikemad jäljed +1,1 / 4,6 dB; β −5,4 / 6,2 dB, kuid parima kujuga (3,0 dB pärast keskmise eemaldamist, vs 3,6): ilmuvad sügavad miinimumid madala radiandiga (Barcelona −15,6 dB kell 17 vs −16 dB kell 19:36; Sofia −18,5 dB kell 20 vs −14 dB). β ja pikemad jäljed (*Nagu DJ5HG*) −2,2 / 4,7 dB; ettevaatlik seadistus (radari kõrgus 89,5 km, β sees, pikemate jälgedeta) −6,9 / 7,6 dB, kuju 3,3 dB. Ilma β-ta näitab YA-MS vaevu miinimumi, kui radiant on madalal ja peaaegu trassi suunas (−8,6 ja −10,4 dB): see on DJ5HG enda reservatsioon, sellest ka hoiatus |
| Proovivõtt iga 5 km järel 15 km asemel | protsendid muutuvad vähem kui 0,3 punkti |

> MS-Soft 5.2 dokumentatsioon määratleb OH5IY efektiivsuse suhtelise indeksina ainult alatihedate jälgede jaoks, kahe teguriga (radiandi elevatsioon, parim umbes 45°, ja nurk trassiga, parim 90°) ning ületihedate jälgede jaoks käsitsi 20 %-ni tõstetud miinimumiga; valemit pole avaldatud. MCG_MS arvutab selle nelja fikseeritud suuna jaoks ja DX-lokaatori olemasolul tegeliku trassi jaoks. Mudel arvestab ainult alatihedaid jälgi ja isotroopseid antenne; ületihedad pursked ja sporaadiline foon ei kuulu efektiivsuse hulka (sporaadilist fooni esindab radari voog). Alates 1.8.1 rakendatakse kasti «antenni suunadiagramm» sisselülitamisel antennide vertikaalset suunadiagrammi; asimuudis jäävad antennid isotroopseks.
