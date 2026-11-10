[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · **Svenska** · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [ไทย](Sky-View-th) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Himlavalv

*Flik: Prognosberäkning › Prognosberäkning.*

[![Himlavalv](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Den här underfliken (himlavalvet i tidigare versioner) samlar på en skärm **var** de användbara spåren finns just nu och **vart du ska rikta**. Till vänster **planvyn** över sträckan; till höger svärmlistan, ett litet himlavalv med radianterna, beräkningstexten och **tvärsnittet** sett från din antenn. Allt avser tiden på reglaget *Himlavalvets tid* (realtid som standard; ±36 h i steg om 15 minuter).

I det lilla himlavalvet ger en **orange linje** genom zenit alltid **rätt antennriktningar**, ortogonala mot den valda (eller den mest gynnsamma) svärmens drift: radiantens azimut ±90°, märkt *antenn NNN°* i båda ändarna, med toleransen ±45° som tunna linjer. Korta orange streck på kanten anger de ortogonala riktningarna för de andra användbara svärmarna.

## Planvy (vänster)

En karta över Europa sedd uppifrån (**Ö till höger**) med en gradskala runt om. Texten under kartan anger dess radie (*Karta: kant = … km från stationen*).

| Element | Ritning |
|---|---|
| Sträcka / DX | Grön linje från din station till motstationen (alltid den verkliga storcirkelsträckan mellan lokatorerna) |
| **Hot A / Hot B** | Punkter 150 km (justerbart) på var sida om mittpunkten, vinkelrätt mot sträckan. **Rött = rekommenderad**, **rosa = utanför antennloben**, **grått = inom loben** (med varning) |
| Antennlob | Den horisontella −3 dB-loben kring antennens azimut (antennen alltid riktad mot DX), märkt *lob …°* |
| Gränser för den gemensamma zonen | Svaga punkter *gr. A* / *gr. B* och de två cirklarna där varje stations horisont möter E-skiktet (se [Geometri](Geometry-and-Path-Loss-sv#gränser-för-den-gemensamma-zonen)) |
| Svärmens drift | **Gul linje**: den riktning i vilken den valda (eller den mest gynnsamma) svärmen sveper över himlen, dvs. radiantens azimut |
| Bästa riktningar | **Orange punkter**: de två riktningarna vinkelräta mot driften (radiantens azimut ±90°, SM6FHZ) |
| **PREV-zoner** | Ljusa ellipser: där de mest sannolika spåren hamnar **nu**, en per sida av sträckan |

Etiketterna överlappar inte: Hot A och PREV A skrivs till vänster om sträckan, B till höger. **Teckenförklaring** är en hopfällbar kolumn till höger om kartan.

**Musen på kartan:** **vänsterklick = motstationens lokator**, **högerklick = min stations lokator**. Sträckan beräknas om direkt.

Alternativ ovanför svärmlistan: **Riktningar Hot A / Hot B**, **Europakarta** (Natural Earth, hämtas till `data/mappa` vid första starten), **Vy ovanifrån (Ö till höger)**.

### Rekommenderad Hot

För den visade tiden summerar programmet över alla svärmar ovanför horisonten vikten ZHR × effektivitet, fördelad mellan sida A (andelen f_A) och sida B. Sidan med störst vikt ger den rekommenderade Hot, ritad i rött:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        rekommenderad = sidan med störst W
```

*Programmets val (handboken ekv. 23).* Idéns källa: DJ5HG, återgiven av DF5HC (DARC-konferensen 2018) – beroende på radiantens läge är en av de två punkterna, HOT-A eller HOT-B, gynnsammare. Att vrida 10–30° åt den sidan (side-scatter) kommer från artikeln av Cerrotta–Sartori.

### PREV-zoner

För varje punkt P i E-skiktet summeras alla aktiva svärmars bidrag till effektiviteten (samma spegelvillkor som för [effektiviteten](Efficiency-Calculation-sv#modellen)), viktade med ZHR. Punkter med minst 3 % av maximum bildar PREV-zonerna; var och en ritas som en ellips med mittpunkt = punkternas viktade medelvärde och axlar = två gånger deras spridning.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Programmets val (handboken ekv. 34).* Det är den praktiska regeln: om svärmen sveper från norr till söder hamnar de användbara spåren i öster och väster.

## Svärmlista (uppe till höger)

| Kolumn | Betydelse |
|---|---|
| Svärm, Kod | Namn och IMO-kod |
| ZHR nu | Aktiviteten i detta ögonblick (IMO:s ZHR vid maximum med aktivitetsprofilen) |
| Azimut, Elev. | Radiantens läge sett från din station |
| Eff. % | Svärmens effektivitet för denna sträcka |
| Sida | A eller B, den sida varifrån flest reflexer kommer |
| Bästa riktn. | Radiantens azimut ±90° |
| Uppgång, Nedgång | Radiantens upp- och nedgång (UTC); *cirkumpolär* eller *alltid under* när det gäller |

Klicka på en rad för att välja svärmen: den gula driftlinjen och de orange punkterna följer med.

## Litet himlavalv (mitten till höger)

Radianterna på ett himlavalv sett från din station, med sin **IMO-kod** och sin **dagliga bana i cyan** (UTC-timmar). **Klicka på en radiant** för att välja den. Färger:

| Färg | Betydelse |
|---|---|
| Gul | effektivitet ≥ 50 % och ZHR ≥ 2 |
| Orange | effektivitet ≥ 20 % |
| Mörkröd | effektivitet < 20 % |
| Grå | nästan inaktiv |

Bredvid finns beräkningstexten: sträckans längd och azimut, mittpunkten och dess elevation, azimut och förskjutning för Hot A / Hot B, den rekommenderade Hot (*… rekommenderas nu: az. …° (…% av förväntade reflexioner)*), gränserna för den gemensamma zonen och påminnelsen: *bästa riktning för svärmen: VINKELRÄTT mot ankomstriktningen (radiantens azimut ±90°, tolerans ±40–50°, SM6FHZ)*.

## Tvärsnitt (nere till höger)

*TVÄRSNITT – de mest sannolika spåren sedda från antennen mot motstationen.* Horisontellt **azimuten relativt motstationen** (← A vänster, B → höger), vertikalt **elevationen**. För varje svärm tas de 14 starkaste reflexionspunkterna; varje spår är ett segment riktat mot radianten, från 10 km över till 10 km under spårhöjden (högst 60 km per sida), tjockare ju mer sannolikt det är. Dessutom ritas antennloben (−3 dB-cirkel kring lobelevationen), motstationen och Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Programmets val (handboken ekv. 35).*

## Varningar

| Varning | När |
|---|---|
| **VARNING: Hot A (och/eller Hot B) ligger inom antennloben …** | Hot spoten ligger inom ±θ/2 från antennens azimut (θ = horisontell −3 dB-lob): med denna riktning täcks den redan. Visas i grått på kartan. Den rekommenderade Hot förblir röd. |
| **RADIANTEN FÖR HÖGT (över 70°)** | En användbar radiant står över 70° sett från din station: spåren faller nästan lodrätt och reflekterar lite mot sträckan (DF5HC, DH9GCD). Samma timmar markeras med ↑ i [timtabellen](Efficiency-Calculation-sv#timtabell). |
| *Ingen gemensam zon i E-skiktet* | Sträckan är längre än två gånger räckvidden på spårhöjden: de två stationerna ser ingen gemensam del av E-skiktet (enkelhopp omöjligt). |
| *Ingen rekommenderad Hot* | Nästan ingen aktiv svärm vid denna tid. |

Referens för himlavalvets grafik: Swan Meteor Skyview av DL1DBC (swan.ms); polärdiagram med bästa riktning: RadiantCalc av SM6FHZ.
