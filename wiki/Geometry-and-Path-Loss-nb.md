[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · **Norsk** · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometri og demping

*Fane: Prognoseberegning › Geometri og demping.*

[![Geometri og demping](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

En tekstrapport om strekningen (kan merkes, så du kan kopiere den) og, til høyre, diagrammet **Antenneelevasjon som funksjon av avstanden til scatter-punktet**. Tall i hakeparentes viser til likningene i beregningshåndboken (`doc/YA-MS_manuale_calcoli.docx`).

## Inndata i denne fanen

| Felt | Standard | Bruk |
|---|---|---|
| **Effekt W** | 400 | Sendereffekt for linkbudsjettet |
| **Antenneforsterkning dBi (tx = rx)** | 14 | Samme antenne i begge ender |
| **Minste signal dBm** | −130 | Minste detekterbare signal (artikkelen: 8-elements Yagi + forforsterker) |
| **Sportetthet q = 10^ … elektroner/m** | 14 | Lineær elektrontetthet i det underdense sporet |

Stasjoner, bånd, sporhøyde, lobeelevasjon, bom og hot spot-avstand kommer fra [radene med kontroller](Getting-Started-nb#1-de-tre-radene-med-kontroller).

## Rapportens avsnitt

| Avsnitt | Innhold |
|---|---|
| **STREKNINGSGEOMETRI (kuleformet jord, R = 6372,7955 km)** | Stasjon og DX med høyder; avstand, asimut og motsatt asimut; midtpunkt (lokator og koordinater); sporhøyde (*← typetall målt av Collm-radaren* når den er hentet fra radaren); antenneelevasjon mot midtpunktet |
| **HOT A / HOT B (klassiske hot spots, for antenneretning)** | For hvert: lokator, asimut fra deg og forskyvning fra den direkte strekningen, asimut fra DX, avstand, elevasjon |
| **GRENSER FOR FELLESSONEN** | Rekkevidde i sporhøyden med lobeelevasjonen; Grense A / Grense B med asimut |
| Antenne | Bom i λ, forsterkning, horisontal / vertikal lobe; om Hot A og Hot B ligger innenfor eller utenfor loben |
| **STREKNINGSDEMPING (underdenst spor, McKinley 1961; antenneforsterkning ikke medregnet)** | Tabell for midtpunktet (forward), Hot A og Hot B på 28, 50, 70, 144, 222 og 432 MHz |
| **LINKBUDSJETT PÅ … MHz (midtpunkt)** | Effekt og EIRP, strekningsdemping, signal ved antennen, minste detekterbare, **margin**; samme margin med OH5IYs gjennomsnittlige demping |
| **EKSPERIMENTELLE REGLER MELLOM BÅNDENE (SM6FHZ, VUSHF 2025)** | Antall/intensitet og varighet sammenlignet med 144 MHz; IARU maksimal ping |

## Lokator og strekning

Lokator (4, 6 eller 8 tegn; midten av ruten, IARUs Maidenhead-system) [14]. Avstand, asimut og midtpunkt med storsirkelformler på en kule med radius **r = 6372,7955 km** (artikkelen av Cerrotta–Sartori) [15–16]. Tidsavhengige beregninger gjelder **midtpunktet**, fordi det beste tidspunktet kan avvike med inntil 1,5 timer mellom de to endene (SM6FHZ).

## Antenneelevasjon

**Kilde:** formelen i artikkelen av Cerrotta–Sartori (figur 7), med x = d/r, d avstanden langs bakken til refleksjonspunktet, H sporhøyden og h stasjonens høyde [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Kontroll:** den stemmer med eksakt sfærisk geometri innenfor 0,03°. Programmet bruker arcustangens med to argumenter, som gir negative verdier bak horisonten og unngår periodisitetsproblemet som nevnes i artikkelen. En negativ elevasjon mot midtpunktet betyr *strekningen er lenger enn den geometriske rekkevidden for ett hopp*.

## Rekkevidde til horisonten

Avstand langs bakken der en stråle med elevasjon e når høyden H (geometrisk invers av formelen ovenfor) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Kontroll:** H = 89,5 km, e = 0° → **1062 km**. I artikkelens eksempel (JN44BB–IO53RT) plasserer tegningen horisontkryssingene ca. 870 km fra stasjonene, noe som svarer til en lobe hevet ca. 2° (865 km).

## Grenser for fellessonen

**Kilde:** artikkelen bestemmer kryssingspunktene mellom kurvene der hver stasjons horisont møter E-laget: skjæringspunktene mellom to sirkler med vinkelradius ρ = d_H/r sentrert i A og B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Hvis 1 − |p0|² < 0, er strekningen lengre enn 2·d_H, og stasjonene ser **ingen felles sone i E-laget**.

**Kontroll:** dette er de **fjerneste kantene** av himmelen sett fra begge stasjonene, **ikke punkter å rette mot**. På JN70CN–IN78UO (1710 km, asimut 308°) ligger de 1062 km fra stasjonen, 37° til venstre og høyre for den direkte strekningen, mens MSHV foreslår 10°. Derfor kalles de *Grense A* / *Grense B* og tegnes svakt på kartet.

## Hot A og Hot B

**Kilde:** refleksjonene samles i to soner («hot spots») ca. **50–150 km på hver side av midtpunktet**. Dette er grunnlaget for tabellen over antenneforskyvning i AMS Bulletin nr. 203, som W8WN har tatt opp (forskyvning på 10° for strekninger på 1500 og 1800 km); MSHV av LZ2HV bruker samme kriterium.

**Valg:** Hot A og Hot B er punktene i avstand s fra midtpunktet M, vinkelrett på strekningen (s = 150 km, justerbart 30–400 km); A til venstre sett fra stasjonen din mot DX, B til høyre [21]. Forskyvningen sett fra stasjonen er omtrent [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Kontroll:** JN70CN–IN78UO, D = 1710 km: 6,7° med s = 100 km, **10,0° med s = 150 km** (samme som MSHV og AMS/W8WN), 13,2° med s = 200 km.

## Demping for underdense spor

**Kilde:** McKinleys likning for underdense spor (β = 0, sin α = 1), antenneforsterkning ikke medregnet; q = lineær elektrontetthet, r_e = klassisk elektronradius = 2,818·10⁻¹⁵ m, R1, R2 avstander fra sporet, φ halve spredningsvinkelen [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Kontroll:** med q = 10¹⁴ elektroner/m på 144 MHz: **181–192 dB** mellom 600 og 2200 km, i tråd med artikkelens referanser på 144 MHz: **182 dB minimum** (GM8JBJ, etter Kaiser & Closs 1952) og **200 dB gjennomsnitt** (OH5IY).

## Linkbudsjett

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Forsterkning skrives inn i dBi og brukes i dBd (dBi − 2,15). Rapporten oppgir også marginen med **OH5IYs gjennomsnittlige strekningsdemping** (200 dB på 144 MHz, skalert med λ³ til valgt bånd). Artikkelens referanse: det trengs ca. **70 dBm EIRP** (−130 dBm + 200 dB, f.eks. ca. 400 W inn i 14 dBi).

## Antenneforsterkning og lobe

**Forsterkning – kilde:** kurve av Günter Hoch **DL6WU** for lange Yagier som funksjon av bomlengden L, gjengitt av W8IO (gyldig fra ca. 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Kontroll mot NEC-modellene til L.B. Cebik W4RNL på 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementer | Bom (λ) | W4RNL NEC (dBi) | Formel (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Forskjellen overstiger aldri **0,1 dB**: forsterkningen avhenger mer av bomlengden enn av konstruksjonen (VK3AUU-Yagier har kortere bom for samme antall elementer). Yagi Calculator av VK5DJ gir også estimater for variantene VK3AUU, WA2PHW og DJ9BV, men formlene er ikke publisert.

**Lobe – kilde:** Kraus' regel, med sirkulær lobe θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Kontroll:** NEC-modellene til W4RNL av DL6WU-Yagier gir en **horisontal lobe som er 5–10 % smalere** enn Kraus: 33,8° / 26,4° / 22,6° for 12, 19 og 26 elementer, mot 37,3° / 28,0° / 23,9°. Enkle formler ser bort fra sidelobene framover (W4RNL, *Long-Boom Yagi Rules of Thumb*). På lange bommer er den vertikale loben litt bredere enn den horisontale (14 λ: 18,4° / 18,8°).

**Valg** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Eksempel: Yagi på 14 λ på 432 MHz → 20,3 dBi, lobe 18,1° horisontalt og 19,5° vertikalt; modellene til W4RNL gir 20,4 dBi og 18,4° / 18,8°. Dette er tilnærmede regler utledet fra noen få DL6WU-antenner.

Antennen regnes alltid som rettet mot DX. Et hot spot ligger **innenfor loben** hvis |Az(Hot) − Az(antenne)| ≤ θ_horisontal/2: det tegnes da i grått i [himmelhvelvingen](Sky-View-nb), og det vises en advarsel. I effektivitetsberegningen er antennene isotrope; den faktiske loben brukes bare til denne kontrollen.

## Eksperimentelle regler mellom båndene

Sammenlignet med 144 MHz: antall/intensitet × (144/f)³ (i dB), varighet × (144/f)² (SM6FHZ, VUSHF 2025). IARU Region 1s maksimale pingvarighet: 1000 ms på 50 MHz, 500 ms på 70 MHz, 100 ms på 144 MHz, 13 ms på 432 MHz (VHF Handbook, sitert i artikkelen). Se også [Eksperimentelle prognoser](Experimental-Forecasts-nb).
