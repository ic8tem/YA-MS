[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · **Dansk** · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Himmelkuppel

*Fane: Prognoseberegning › Prognoseberegning.*

[![Himmelkuppel](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Denne underfane (himmelkuplen fra tidligere versioner) samler på én skærm, **hvor** de nyttige spor er nu, og **hvorhen** antennen skal pege. Til venstre strækningen **set ovenfra**; til højre sværmlisten, en lille himmelkuppel med radianterne, beregningens tekst og **snittet** set fra din antenne. Alt refererer til det tidspunkt, der er valgt med *Beregningsdato (UTC)* og skyderen *Timer (−12 til +36 t)* (realtid som standard, i trin på 15 minutter).

En **bjælke over visningen set ovenfra** opsummerer beregningen for det tidspunkt: dato og klokkeslæt (*nu* eller timer fra nu), **strækningsindekset Σ ZHR×η**, den **mest nyttige sværm** med dens ZHR og effektivitet, antallet af sværme over horisonten og det **anbefalede Hot** med dets azimut.

I den lille himmelkuppel angiver en **orange linje** gennem zenit altid de **rigtige antenneretninger**, vinkelret på vandringen af den valgte sværm (eller den mest gunstige): radiantens azimut ±90°, mærket *antenne NNN°* i begge ender, med tolerancen ±45° som tynde linjer. Korte orange streger på kanten angiver de vinkelrette retninger for de andre nyttige sværme.

## Set ovenfra (venstre)

Et kort over Europa set ovenfra (**Ø til højre**) med en gradskala rundt om. Billedteksten under kortet angiver radius (*Kort: kant = … km fra stationen*).

| Element | Tegning |
|---|---|
| Strækning / DX | Grøn linje fra din station til modstationen (altid den faktiske storcirkelstrækning mellem lokatorerne) |
| **Hot A / Hot B** | Punkter 150 km (kan indstilles) på hver side af midtpunktet, vinkelret på strækningen. **Rød = anbefalet**, **lyserød = uden for antennelappen**, **grå = inden for lappen** (med en advarsel) |
| Antennelap | Den vandrette −3 dB-lap omkring antennens azimut (antennen peger altid mod DX), mærket *lap …°* |
| Grænser for fælles zone | Svage *græn. A* / *græn. B*-punkter og de to cirkler, hvor hver stations horisont møder E-laget (se [Geometri](Geometry-and-Path-Loss-da#grænser-for-den-fælles-zone)) |
| Sværmens vandring | **Gul linje**: den retning, hvori den valgte sværm (eller den mest gunstige) fejer hen over himlen, dvs. radiantens azimut |
| Bedste retninger | **Orange prikker**: de to retninger vinkelret på vandringen (radiantens azimut ±90°, SM6FHZ) |
| **PREV-zoner** | Lyse ellipser: hvor de mest sandsynlige spor falder **nu**, én pr. side af strækningen |

Etiketterne overlapper ikke: Hot A og PREV A skrives til venstre for strækningen, B til højre. **Signaturforklaring** er en sammenfoldelig kolonne til højre for kortet.

**Mus på kortet:** **venstreklik = modstationens lokator**, **højreklik = min stations lokator**. Strækningen genberegnes med det samme.

Indstillinger over sværmlisten: **Hot A / Hot B-retninger**, **Europakort** (Natural Earth, hentes til `data/mappa` ved første opstart), **Set ovenfra (Ø til højre)**.

### Anbefalet Hot

For det viste tidspunkt lægger programmet vægten ZHR × effektivitet sammen for alle sværme over horisonten, fordelt mellem side A (andel f_A) og side B. Den side, der har den største vægt, giver det anbefalede Hot, som tegnes med rødt:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Programmets valg (manualens lign. 23).* Idéens kilde: DJ5HG, gengivet af DF5HC (DARC-konferencen 2018) – afhængigt af radiantens position er det ene af de to punkter, HOT-A eller HOT-B, mest gunstigt. At dreje 10–30° mod den side (side-scatter) stammer fra artiklen af Cerrotta–Sartori.

### PREV-zoner

For hvert punkt P i E-laget lægges bidragene til effektiviteten fra alle aktive sværme sammen (samme spejlingsbetingelse som for [effektiviteten](Efficiency-Calculation-da#modellen)), vægtet med ZHR. Punkter med mindst 3 % af maksimum danner PREV-zonerne; hver tegnes som en ellipse med centrum = punkternes vægtede middelværdi og akser = to gange deres spredning.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Programmets valg (manualens lign. 34).* Det er den praktiske regel: hvis sværmen fejer fra nord mod syd, falder de nyttige spor mod øst og vest.

## Sværmliste (øverst til højre)

| Kolonne | Betydning |
|---|---|
| Sværm, Kode | Navn og IMO-kode |
| ZHR nu | Aktivitet i øjeblikket (IMO's maksimale ZHR med aktivitetsprofilen) |
| Azimut, Elev. | Radiantens position set fra din station |
| Effekt. % | Sværmens effektivitet for denne strækning |
| Side | A eller B, den side hvorfra de fleste refleksioner kommer |
| Bedste retn. | Radiantens azimut ±90° |
| Op, Ned | Radiantens op- og nedgang (UTC); *cirkumpolar* eller *altid under*, når det er tilfældet |

Klik på en række for at vælge sværmen: den gule vandringslinje og de orange prikker følger den.

## Lille himmelkuppel (midten til højre)

Radianterne på en himmelkuppel set fra din station med deres **IMO-kode** og **daglige bane i cyan** (UTC-tider). **Klik på en radiant** for at vælge den. Farver:

| Farve | Betydning |
|---|---|
| Gul | effektivitet ≥ 50 % og ZHR ≥ 2 |
| Orange | effektivitet ≥ 20 % |
| Mørkerød | effektivitet < 20 % |
| Grå | næsten inaktiv |

Ved siden af står beregningens tekst: strækningens længde og azimut, midtpunktet og dets elevation, azimut og forskydning for Hot A / Hot B, det anbefalede Hot (*… anbefales nu: az. …° (…% af de forventede refleksioner)*), grænserne for den fælles zone og påmindelsen: *bedste retning for sværmen: VINKELRET på ankomstretningen (radiantens azimut ±90°, tolerance ±40–50°, SM6FHZ)*.

## Snit (nederst til højre)

*SNIT – de mest sandsynlige spor set fra antennen mod modstationen.* Vandret **azimut i forhold til modstationen** (← A venstre, B → højre), lodret **elevation**. For hver sværm tages de 14 kraftigste refleksionspunkter; hvert spor er et linjestykke orienteret mod radianten, fra 10 km over til 10 km under sporhøjden (højst 60 km pr. side), tykkere jo mere sandsynligt. Desuden tegnes antennelappen (−3 dB-cirkel omkring lapelevationen), modstationen og Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Programmets valg (manualens lign. 35).*

## Advarsler

| Advarsel | Hvornår |
|---|---|
| **ADVARSEL: Hot A (og/eller Hot B) ligger inden for antennens lap …** | Hot spottet ligger inden for ±θ/2 af antennens azimut (θ = vandret −3 dB-lap): med denne retning er det allerede dækket. Vist med gråt på kortet. Det anbefalede Hot forbliver rødt. |
| **RADIANT FOR HØJT (over 70°)** | En nyttig radiant står over 70° set fra din station: sporene falder næsten lodret og reflekterer kun lidt mod strækningen (DF5HC, DH9GCD). De samme timer markeres med ↑ i [timetabellen](Efficiency-Calculation-da#timetabel). |
| *Ingen fælles zone i E-laget* | Strækningen er længere end det dobbelte af rækkevidden i sporhøjde: de to stationer ser ingen fælles del af E-laget (ét hop umuligt). |
| *Ingen anbefalet Hot* | Næsten ingen aktive sværme i øjeblikket. |

Forbillede for himmelkuplens grafik: Swan Meteor Skyview af DL1DBC (swan.ms); polardiagram med den bedste retning: RadiantCalc af SM6FHZ.
