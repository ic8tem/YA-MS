[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · **Norsk** · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Effektivitetsberegning

*Fane: Prognoseberegning › Effektivitetsberegning.*

[![Effektivitetsberegning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

En sverms **effektivitet** sier, i prosent, hvor mye posisjonen til radianten tillater refleksjoner på **din** strekning. Begrepet stammer fra Ilkka **OH5IY** (MS-Soft) og er tatt opp i artikkelen av Cerrotta–Sartori: effektivitetens maksimum faller ikke sammen med det visuelle maksimumet (ZHR), fordi det avhenger av hvor radianten står i forhold til de to stasjonene. MCG_MS av DL5MCG bruker samme idé på fire faste retninger; YA-MS beregner den for den **faktiske strekningen** mellom de to lokatorene.

Fanen viser den time for time for dagen som er valgt i *Dag for 24 t-tabellen (UTC)* (verdier ved halv time).

## Oversiktspaneler

| Panel | Innhold |
|---|---|
| **DAGENS BESTE TIDSPUNKT** | Timen med høyest strekningsindeks, indeksen og dominerende side (A/B med sin %) |
| **GUNSTIGSTE SVERM** | Svermen med størst ZHR × effektivitet den dagen, dens effektivitet, time og side, og **beste retning** (radiantens asimut +90° / −90°) |
| **NÅ** | Indeks og dominerende side i denne timen, og anbefalt Hot (bare når valgt dag er i dag) |
| **EKSPERIMENTELL PROGNOSE** | Forventede refleksjoner/time nå, om 1 t og om 2 t på prognosefrekvensen (Collm, SM6FHZ-regler; se [Eksperimentelle prognoser](Experimental-Forecasts-nb)) |

Under panelene forklarer et bånd bokstavene A og B (se nedenfor).

## Diagram

*Effektivitet time for time for … den … (UTC, verdier ved halv time).* For inntil fem svermer: effektivitet % som heltrukken linje og DH9GCD-formelen som prikket linje i samme farge; **strekningsindeksen** som blå søyler på høyre skala.

## Timetabell

Én rad per sverm som er aktiv den dagen (sortert etter ZHR), 24 kolonner for timene (UTC):

| Celle | Betydning |
|---|---|
| `63A` | effektivitet 63 %, de fleste refleksjonene fra side **A** |
| `41B` | effektivitet 41 %, side **B** |
| `3` | effektivitet under 5 %: tall uten sidebokstav |
| tom | effektivitet under 1 % |
| `…↑` | radianten står **over 70°** sett fra stasjonen din i den timen (for høyt) |
| gul tekst | effektivitet ≥ 50 % |

- **A** = **venstre** sett fra stasjonen din mot motstasjonen (Hot A-sonen); **B** = **høyre** (Hot B-sonen). Det lønner seg å dreie antennen **10–30° mot den siden** (side-scatter, artikkelen av Cerrotta–Sartori).
- **Lyseblå rader** (*DH9GCD %*, under hver sverm): DH9GCD-formelen, til sammenligning.
- **Σ-raden**: *Strekningsindeks (ZHR×eff.)*.
- **Oransje rad** (*Prognose … MHz (refl./time)*): den eksperimentelle prognosen, for timene der den finnes (i dag og en del av i morgen).

## Modellen

Alle trinnene står i [beregningshåndboken](Efficiency-Explanation-nb) (`doc/YA-MS_manuale_calcoli.docx`, kapittel 5). Kort fortalt:

**1. Speilrefleksjon.** Et spor sender signalet fra A til B bare hvis det tangerer en ellipsoide med A og B i brennpunktene (McKinley 1961). Sporene fra en sverm er parallelle med radiantretningen ŝ (artikkelen; McKinley). For hvert punkt P i E-laget, med enhetsvektorer mot stasjonene:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Samme lov ligger til grunn for QTFGUI av DJ5HG og teksten hans *"Die Geometrie von Meteorscatterverbindungen"* (2004): sporet sprer på en kjegle med sporet som akse, og bare en mottaker på kjeglen hører det. For et ideelt spor er kjegleveggen svært tynn (en stråler tusenvis av bølgelengder lang); programmet godtar betingelsen med en gaussisk toleranse σ = 0,05 rad (ca. 3°), som står for det den ideelle kjeglen ikke ser: spredningen av svermenes radianter (0,3–1,4° målt av GMN), spor bøyd av vinden og den endelige lengden deres – *programmets valg*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Vekten til hvert punkt.** Effekten fra et underdenst spor (McKinley; ITU-R P.843, likn. 3), φ = halve spredningsvinkelen (begrenset til 85°, *valg*), β = vinkelen mellom sporet og utbredelsesplanet A-P-B, p̂ = enhetsnormalen til dette planet:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Alternativet «β-vinkel mellom spor og strekning (full McKinley)»** (på som standard, forsiktig innstilling). På: spor som krysser utbredelsesplanet, er verdt 10–15 dB mindre enn dem som ligger i det, slik at ingen spor overvurderes. Av: hvert spor vektes som om det lå i planet (β = 0, vekt med cos²φ), som til og med versjon 1.6. *Kontroll:* på en strekning på 1000 km ligger beste radiantasimut uten β 15°–90° fra strekningen avhengig av radiantens elevasjon (30° med radianten på 30°, på tvers av strekningen med radianten på 60°), og radianten på tvers er verdt 67 % ved 30° elevasjon; med β ligger den beste radianten alltid langs strekningen, og den på tvers faller til 15 %. Med β går SM6FHZ / DH9GCD-regelen for beste retning tapt; β forblir et alternativ, på som standard fordi det gir de mest forsiktige verdiene, og slås det av, kommer regelen tilbake.

Antallet meteorer som når et punkt, er proporsjonalt med sinus til radiantens elevasjon der (ŝ·û_P), den samme korreksjonen som IMO bruker for ZHR.

**Alternativet «Lengre spor med lav radiant (DJ5HG)»** (avkrysningsboks over diagrammet, av som standard, med verktøytips): DJ5HG påpeker at med lav radiant faller færre meteorer per km², men sporene er lengre (opptil 100 km brukbare) og oppfyller refleksjonsloven oftere. Med alternativet på blir vekten min(sin El, 15/100): den brukbare lagtykkelsen, 15 km, delt på sinus til elevasjonen gir sporlengden, begrenset til 100 km. Over ca. 9° opphever de to effektene hverandre. Av forblir beregningen forsiktig.

**Beregningsinnstilling** (samme rad, radioknapper): **Forsiktig** (standard, de mest forsiktige verdiene: sporhøyde fra radaren, normale spor, β på), **Som DJ5HG** (102 km, lengre spor, β) og **Egendefinert**, som velges automatisk når du endrer høyden, boksen *fra radar*, alternativet for lengre spor eller β for hånd.

**3. Sum og prosent.** Punkter for hver 15 km i sporhøyden, bare der begge stasjonene ser dem over lobeelevasjonen (*valg*). 100 % er den gunstigste radiantposisjonen for den strekningen:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F beregnes én gang per strekning på et rutenett av retninger (asimut for hver 5°, elevasjon for hver 2,5°) og interpoleres.

**Effektivitet i dB (DJ5HG-referanse).** Prosenten er bare relativ til den beste radiantposisjonen for den strekningen. For å sammenligne ulike strekninger gir programmet også effektiviteten i dB i forhold til den faste referansen til DJ5HG: 0 dB er maksimum for en 1000 km nord–sør-strekning over ekvator med radianten på himmelekvator ved jevndøgn, beregnet med samme høyde og samme vekter. DJ5HG oppgir verdiene sine som bedre enn 6 dB.

**4. Side og indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Bokstaven i tabellen er siden med størst andel. *Programmets valg (håndbokens likn. 32–33).*

## Sammenligning med DH9GCD

Primærkildene for beste retning er Eshleman & Mlodnosky og Meeks & James (Proc. IRE, 1957), Hines (1955) og den eksperimentelle kontrollen av den ved Forsyth, Hines & Vogan (1955): bare radianter på halvsirkelen på himmelen vinkelrett på halveringslinjen for spredningsvinkelen er nyttige, antall spor øker med sin El, og nær midtpunktet faller de nyttige sporene ca. H·tan El til siden, på motsatt side av radianten. DJ5HG tar et forbehold: med en **lav** radiant rett langs strekningen gir McKinleys formel sterke signaler (Hamburg–Narvik, Kvadrantidene, ca. 19 UTC), så «radiant på linje med strekningen = nesten null» gjelder bare for en høy radiant; programmet forblir forsiktig og viser advarselen *LAV RADIANT LANGS STREKNINGEN*.

En uavhengig kontroll: formelen for beste retning av **DH9GCD**, gjengitt av **DF5HC** (DARC-konferansen, januar 2018) – den har ingen publisert primærkilde – der El og Az er radiantens elevasjon og asimut sett fra stasjonen din og P er motstasjonens asimut:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Den er størst med radianten på 45° og på tvers av strekningen. DF5HC regner radianten som for lav under 20° og **for høy over 70°**: disse timene får ↑ i tabellen og en advarsel i [himmelhvelvingen](Sky-View-nb#advarsler). Formelen ser bort fra avstand og høyder, men er en god referanse.

## Kontroller

| Kontroll | Resultat |
|---|---|
| SM6FHZ-regelen (VUSHF 2025): beste strekning vinkelrett på radiantens asimut, retning = radiantens az ±90°, toleranse ±40–50° | Gjengis av modellen; med radianten på linje med strekningen og høyt på himmelen er effektiviteten nesten null |
| QTFGUI av DJ5HG, Hamburg JO53IM – Barcelona, Kvadrantidene, 4. januar (eksempel fra håndboken) | QTFGUI: 07:00 retning 252°, −8 dB; 08:00 ingen refleksjonssone; 09:00 retning 168°, −4 dB. YA-MS (høyde 102 km som QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle tre metodene ser hullet kl. 08:00, med radianten nesten i senit |
| Kurvene til DJ5HG (*Die Geometrie…*, Bild 8–9: fra Hamburg og München, Kvadrantidene, 4. januar; avlest fra diagrammet, ca. ±0,5 dB og ±15 min) mot den automatiske testen `--prova-dj5hg` (én verdi per time) | Tidspunkter: hullet med radianten nær senit faller på de samme timene (Barcelona 07:30–08:30 mot 07–09; Sofia 06:36–07:48 mot 07–08; Narvik 07–08:30 mot 07–09); Moskva er stengt 03–10 i begge, åpen fra Hamburg til ca. 02:30 og fra München til ca. 00:30, slik DJ5HG skriver. Retninger: 2–10° forskjell. Nivåer og form ved 102 km (middel- og RMS-avvik fra kurvene): ingen β, ingen lengre spor −1,6 / 4,0 dB; lengre spor +1,1 / 4,6 dB; β −5,4 / 6,2 dB, men med best form (3,0 dB etter at middelverdien er trukket fra, mot 3,6): de dype minimaene med lav radiant kommer fram (Barcelona −15,6 dB kl. 17 mot −16 dB kl. 19:36; Sofia −18,5 dB kl. 20 mot −14 dB). β og lengre spor (*Som DJ5HG*) −2,2 / 4,7 dB; den forsiktige innstillingen (radarhøyde 89,5 km, β på, ingen lengre spor) −6,9 / 7,6 dB, form 3,3 dB. Uten β viser YA-MS knapt minimumet med radianten lavt og nesten på linje med strekningen (−8,6 og −10,4 dB): dette er DJ5HGs eget forbehold, derav advarselen |
| Sampling for hver 5 km i stedet for 15 km | prosentene endres med mindre enn 0,3 poeng |

> Dokumentasjonen til MS-Soft 5.2 definerer effektiviteten til OH5IY som en relativ indeks bare for underdense spor, med to faktorer (radiantens elevasjon, best rundt 45°, og vinkel mot strekningen, best 90°) og et minimum som er hevet for hånd til 20 % for overdense spor; formelen er ikke publisert. MCG_MS beregner den for fire faste retninger og, med DX-lokatoren, for den faktiske strekningen. Modellen tar bare hensyn til underdense spor, med isotrope antenner; overdense utbrudd og sporadisk bakgrunn inngår ikke i effektiviteten (den sporadiske bakgrunnen representeres av radarfluksen).
