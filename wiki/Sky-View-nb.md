[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · **Norsk** · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Himmelhvelving

*Fane: Prognoseberegning › Prognoseberegning.*

[![Himmelhvelving](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Denne underfanen (himmelhvelvingen fra tidligere versjoner) samler på én skjerm **hvor** de nyttige sporene er nå, og **hvor** antennen skal peke. Til venstre **grunnrisset** av strekningen; til høyre svermlisten, en liten himmelhvelving med radiantene, beregningsteksten og **snittet** sett fra antennen din. Alt gjelder tidspunktet som er valgt med *Beregningsdato (UTC)* og glidebryteren *Timer (−12 til +36 t)* (sanntid som standard, i steg på 15 minutter).

En **stripe over grunnrisset** oppsummerer beregningen for det tidspunktet: dato og klokkeslett (*nå* eller timer fra nå), **strekningsindeksen Σ ZHR×η**, den **mest nyttige svermen** med ZHR og effektivitet (også i dB i forhold til DJ5HG-referansen, se [Effektivitetsberegning](Efficiency-Calculation-nb)), antall svermer over horisonten og **anbefalt Hot** med asimut.

I den lille himmelhvelvingen viser en **oransje linje** gjennom senit alltid de **riktige antenneretningene**, vinkelrett på forflytningen til den valgte svermen (eller den gunstigste): radiantens asimut ±90°, merket *antenne NNN°* i begge ender, med toleransen ±45° som tynne linjer. Korte oransje streker på kanten viser de vinkelrette retningene for de andre nyttige svermene.

## Grunnriss (venstre)

Et kart over Europa sett ovenfra (**Ø til høyre**) med en gradskala rundt. Bildeteksten under kartet oppgir radien (*Kart: kant = … km fra stasjonen*).

| Element | Tegning |
|---|---|
| Strekning / DX | Grønn linje fra stasjonen din til motstasjonen (alltid den faktiske storsirkelstrekningen mellom lokatorene) |
| **Hot A / Hot B** | Punkter på hver side av midtpunktet, vinkelrett på strekningen, i avstanden som AMS-forskyvningstabellen gir (eller lagt inn for hånd). **Rød = anbefalt**, **rosa = utenfor antenneloben**, **grå = innenfor loben** (med en advarsel) |
| Antennelobe | Den horisontale −3 dB-loben rundt antennens asimut (antennen peker alltid mot DX), merket *lobe …°* |
| Grenser for fellessonen | Svake *gr. A* / *gr. B*-punkter og de to sirklene der hver stasjons horisont møter E-laget (se [Geometri](Geometry-and-Path-Loss-nb#grenser-for-fellessonen)) |
| Svermens forflytning | **Gul linje**: retningen den valgte svermen (eller den gunstigste) sveiper over himmelen i, dvs. radiantens asimut |
| Beste retninger | **Oransje punkter**: de to retningene vinkelrett på forflytningen (radiantens asimut ±90°, SM6FHZ) |
| **PREV-soner** | Lyse ellipser: der de mest sannsynlige sporene faller **nå**, én per side av strekningen |

Etikettene overlapper ikke: Hot A og PREV A skrives til venstre for strekningen, B til høyre. **Tegnforklaring** er en sammenleggbar kolonne til høyre for kartet.

**Mus på kartet:** **venstreklikk = motstasjonens lokator**, **høyreklikk = min stasjons lokator**. Strekningen beregnes på nytt med en gang.

Valg over svermlisten: **Retninger Hot A / Hot B**, **Europakart** (Natural Earth, lastes ned til `data/mappa` ved første oppstart), **Sett ovenfra (Ø til høyre)**.

### Anbefalt Hot

For tidspunktet som vises, summerer programmet vekten ZHR × effektivitet over alle svermer over horisonten, fordelt mellom side A (andel f_A) og side B. Siden med størst vekt gir anbefalt Hot, som tegnes i rødt:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Programmets valg (håndbokens likn. 23).* Kilden til idéen: DJ5HG, gjengitt av DF5HC (DARC-konferansen 2018) – avhengig av radiantens posisjon er ett av de to punktene, HOT-A eller HOT-B, gunstigst. Å dreie 10–30° mot den siden (side-scatter) kommer fra artikkelen av Cerrotta–Sartori.

### PREV-soner

For hvert punkt P i E-laget summeres bidragene til effektiviteten fra alle aktive svermer (samme speilbetingelse som for [effektiviteten](Efficiency-Calculation-nb#modellen)), vektet med ZHR. Punkter med minst 3 % av maksimum danner PREV-sonene; hver tegnes som en ellipse med sentrum = punktenes vektede middel og akser = to ganger spredningen.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Programmets valg (håndbokens likn. 34).* Det er den praktiske regelen: hvis svermen sveiper fra nord mot sør, faller de nyttige sporene i øst og vest.

## Svermliste (øverst til høyre)

| Kolonne | Betydning |
|---|---|
| Sverm, Kode | Navn og IMO-kode |
| ZHR nå | Aktivitet i øyeblikket (IMOs maksimale ZHR med aktivitetsprofilen) |
| Asimut, Elev. | Radiantens posisjon sett fra stasjonen din |
| Effekt. % | Svermens effektivitet for denne strekningen |
| Side | A eller B, siden de fleste refleksjonene kommer fra |
| Beste retning | Radiantens asimut ±90° |
| Opp, Ned | Radiantens oppgang og nedgang (UTC); *sirkumpolar* eller *alltid under* når det gjelder |

Klikk på en rad for å velge svermen: den gule forflytningslinjen og de oransje punktene følger den.

## Liten himmelhvelving (midten til høyre)

Radiantene på en himmelhvelving sett fra stasjonen din, med **IMO-kode** og **daglig bane i cyan** (UTC-tider). **Klikk på en radiant** for å velge den. Farger:

| Farge | Betydning |
|---|---|
| Gul | effektivitet ≥ 50 % og ZHR ≥ 2 |
| Oransje | effektivitet ≥ 20 % |
| Mørkerød | effektivitet < 20 % |
| Grå | nesten inaktiv |

Ved siden av står beregningsteksten: strekningens lengde og asimut, midtpunktet og dets elevasjon, asimut og forskyvning for Hot A / Hot B, anbefalt Hot (*… anbefalt nå: az. …° (…% av forventede refleksjoner)*), grensene for fellessonen og påminnelsen: *beste retning for svermen: VINKELRETT på ankomstretningen (radiantens asimut ±90°, toleranse ±40–50°, SM6FHZ)*.

## Snitt (nederst til høyre)

*SNITT – de mest sannsynlige sporene sett fra antennen mot motstasjonen.* Horisontalt **asimut i forhold til motstasjonen** (← A venstre, B → høyre), vertikalt **elevasjon**. For hver sverm tas de 14 sterkeste refleksjonspunktene; hvert spor er et linjestykke orientert mot radianten, fra 10 km over til 10 km under sporhøyden (høyst 60 km per side), tykkere jo mer sannsynlig. Dessuten tegnes antenneloben (−3 dB-sirkel rundt lobeelevasjonen), motstasjonen og Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Programmets valg (håndbokens likn. 35).*

## Advarsler

| Advarsel | Når |
|---|---|
| **ADVARSEL: Hot A (og/eller Hot B) ligger innenfor antenneloben …** | Hot spot-et ligger innenfor ±θ/2 av antennens asimut (θ = horisontal −3 dB-lobe): med denne retningen er det allerede dekket. Vist i grått på kartet. Anbefalt Hot forblir rødt. |
| **RADIANTEN FOR HØYT (over 70°)** | En nyttig radiant står over 70° sett fra stasjonen din: sporene faller nesten loddrett og reflekterer lite mot strekningen (DF5HC, DH9GCD). De samme timene merkes med ↑ i [timetabellen](Efficiency-Calculation-nb#timetabell). |
| **LAV RADIANT LANGS STREKNINGEN** | En aktiv radiant står under 20° og innenfor 30° av strekningens retning. Den beregnede effektiviteten forblir lav (forsiktig), men DJ5HG venter sjeldne, sterke refleksjoner fra streifende spor på linje med strekningen (Hamburg–Narvik, Kvadrantidene, ca. 19 UTC): verdt å lytte etter. |
| **STREKNING FORBI SPORENES HORISONT** | I sporhøyde ligger strekningens midtpunkt under horisonten til begge stasjonene (omkring 2120 km med spor i 90 km). Advarselen oppgir minste nødvendige sporhøyde (omkring 96 km for 2200 km, 105 km for 2300 km): forbindelsen er bare mulig med de høyeste sporene, og effektiviteter og demping er på grensen av modellen. |
| *Ingen felles sone i E-laget* | Strekningen er lengre enn dobbelt rekkevidde i sporhøyden: de to stasjonene ser ingen felles del av E-laget (enkelthopp umulig). |
| *Ingen anbefalt Hot* | Nesten ingen aktive svermer akkurat nå. |

Forbilde for grafikken til himmelhvelvingen: Swan Meteor Skyview av DL1DBC (swan.ms); polardiagram med beste retning: RadiantCalc av SM6FHZ.
