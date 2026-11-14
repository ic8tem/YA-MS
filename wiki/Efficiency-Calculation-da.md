[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · **Dansk** · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Effektivitetsberegning

*Fane: Prognoseberegning › Effektivitetsberegning.*

[![Effektivitetsberegning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

En sværms **effektivitet** angiver i procent, hvor meget dens radiants position tillader refleksioner på **din** strækning. Begrebet stammer fra Ilkka **OH5IY** (MS-Soft) og tages op i artiklen af Cerrotta–Sartori: effektivitetens maksimum falder ikke sammen med det visuelle maksimum (ZHR), fordi det afhænger af, hvor radianten står i forhold til de to stationer. MCG_MS af DL5MCG anvender samme idé på fire faste retninger; YA-MS beregner den for den **faktiske strækning** mellem de to lokatorer.

Fanen viser den time for time for den dag, der er valgt i *Beregningsdato (UTC)* (værdier ved halv).

## Overbliksbokse

| Boks | Indhold |
|---|---|
| **DAGENS BEDSTE TIDSPUNKT** | Timen med det højeste strækningsindeks, indekset og den fremherskende side (A/B med sin %) |
| **MEST GUNSTIGE SVÆRM** | Den sværm, der har dagens største ZHR × effektivitet, dens effektivitet, time og side og **bedste retning** (radiantens azimut +90° / −90°) |
| **NU · OM 1, 3, 6, 12 OG 24 TIMER** | for hver horisont gennemsnittet for timen, der starter dér (fire prøver): strækningsindeks, dominerende side, den sværm, der bidrager mest, og, når der er radardata, refleksioner pr. time fra den eksperimentelle prognose. I NU vises uden radardata den anbefalede Hot. Opdateres hvert minut. |

Boksene sidder i et bånd under tidsrækken, over fanerne, altid synligt også med kommandorækkerne foldet sammen: til venstre de to bokse for den valgte dag, derefter de seks prognosehorisonter, der starter nu.

Under boksene forklarer en bjælke bogstaverne A og B (se nedenfor).

## Graf

*Effektivitet pr. time for … den … (UTC, værdier ved halv).* For op til fem sværme: effektivitet % som fuldt optrukket linje og DH9GCD-formlen som prikket linje i samme farve; **strækningsindekset** som blå søjler på højre skala.

## Timetabel

Én række pr. sværm, der er aktiv den dag (sorteret efter ZHR), 24 kolonner for timerne (UTC):

| Celle | Betydning |
|---|---|
| `63A` | effektivitet 63 %, de fleste refleksioner fra side **A** |
| `41B` | effektivitet 41 %, side **B** |
| tom | effektivitet under 1 % |
| `…↑` | radianten står **over 70°** set fra din station i den time (for højt) |
| gul tekst | effektivitet ≥ 50 % |

- **A** = **venstre** set fra din station mod modstationen (Hot A-zone); **B** = **højre** (Hot B-zone). Det kan betale sig at dreje antennen **10–30° mod den side** (side-scatter, artiklen af Cerrotta–Sartori).
- **Lyseblå rækker** (*DH9GCD %*, under hver sværm): DH9GCD-formlen til sammenligning.
- **Σ-række**: *Strækningsindeks (ZHR×eff.)*.
- **Orange række** (*Prognose … MHz (refl./time)*): den eksperimentelle prognose for de timer, hvor den findes (i dag og en del af i morgen).

## Modellen

Alle trin står i [beregningsmanualen](Efficiency-Explanation-da) (`doc/YA-MS_manuale_calcoli.docx`, kapitel 5). Kort fortalt:

**1. Spejlende refleksion.** Et spor sender signalet fra A til B kun, hvis det tangerer en ellipsoide med A og B i brændpunkterne (McKinley 1961). En sværms spor er parallelle med radiantens retning ŝ (artiklen; McKinley). For hvert punkt P i E-laget, med enhedsvektorer mod stationerne:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Samme lov ligger til grund for QTFGUI af DJ5HG og hans tekst *"Die Geometrie von Meteorscatterverbindungen"* (2004): sporet spreder på en kegle med sporet som akse, og kun en modtager på keglen hører det. For et ideelt spor er keglevæggen meget tynd (en stråler tusindvis af bølgelængder lang); programmet accepterer betingelsen med en gaussisk tolerance σ = 0,05 rad (ca. 3°), som står for det, den ideelle kegle ikke ser: spredningen af sværmenes radianter (0,3–1,4° målt af GMN), spor bøjet af vinden og deres endelige længde – *programmets valg*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Hvert punkts vægt.** Effekten fra et underdenst spor (McKinley; ITU-R P.843, lign. 3), φ = halvdelen af spredningsvinklen (begrænset til 85°, *valg*), β = vinklen mellem sporet og udbredelsesplanet A-P-B, p̂ = enhedsnormalen til dette plan:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Indstillingen "β-vinkel mellem spor og strækning (fuld McKinley)"** (slået til som standard, forsigtig beregningsindstilling). Slået til: spor, der krydser udbredelsesplanet, er 10–15 dB mindre værd end dem, der ligger i det, så intet spor overvurderes. Slået fra: hvert spor vægtes, som om det lå i planet (β = 0, vægt med cos²φ), som til og med version 1.6. *Kontrol:* på en strækning på 1000 km ligger den bedste radiantazimut uden β 15°–90° fra strækningen afhængigt af radiantens elevation (30° med radianten i 30°, vinkelret på strækningen med radianten i 60°), og den vinkelrette radiant er 67 % værd ved 30° elevation; med β ligger den bedste radiant altid langs strækningen, og den vinkelrette falder til 15 %. Med β går SM6FHZ / DH9GCD-reglen for den bedste retning tabt; β forbliver en indstilling, slået til som standard, fordi den giver de mest forsigtige værdier, og slås den fra, kommer reglen tilbage.

Antallet af meteorer, der når et punkt, er proportionalt med sinus til radiantens elevation dér (ŝ·û_P) – samme korrektion, som IMO bruger for ZHR.

**Indstillingen "Længere spor med lav radiant (DJ5HG)"** (afkrydsningsfelt over diagrammet, slået fra som standard, med værktøjstip): DJ5HG bemærker, at der med lav radiant falder færre meteorer pr. km², men at sporene er længere (op til 100 km brugbare) og oftere opfylder refleksionsloven. Med indstillingen slået til bliver vægten min(sin El, 15/100): den brugbare lagtykkelse, 15 km, divideret med sinus til elevationen giver sporlængden, begrænset til 100 km. Over ca. 9° ophæver de to effekter hinanden. Slået fra forbliver beregningen forsigtig.

**Beregningsindstilling** (samme række, radioknapper): **Forsigtig** (standard, de mest forsigtige værdier: sporhøjde fra radaren, normale spor, β slået til), **Som DJ5HG** (102 km, længere spor, β) og **Brugerdefineret**, som vælges automatisk, når du manuelt ændrer højden, feltet *fra radar*, indstillingen for længere spor eller β.

**3. Sum og procent.** Punkter for hver 15 km i sporhøjde, set af begge stationer over horisonten og vægtet med begge antenners lodrette diagram (feltet *antennediagram*, slået til som standard; fra kun punkter over lobens elevation) (*valg*). 100 % er den gunstigste radiantposition for strækningen:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F beregnes én gang pr. strækning på et gitter af retninger (azimut for hver 5°, elevation for hver 2,5°) og interpoleres.

**Effektivitet i dB (DJ5HG-reference).** Procenten er kun relativ til den bedste radiantposition for den strækning. For at kunne sammenligne forskellige strækninger angiver programmet også effektiviteten i dB i forhold til DJ5HG's faste reference: 0 dB er maksimum for en 1000 km nord–syd-strækning over ækvator med radianten på himlens ækvator ved jævndøgn, beregnet med samme højde og samme vægte. DJ5HG angiver sine værdier som bedre end 6 dB.

**4. Side og indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Bogstavet i tabellen er den side, der har den største andel. *Programmets valg (manualens lign. 32–33).*

## Sammenligning med DH9GCD

De primære kilder til den bedste retning er Eshleman & Mlodnosky og Meeks & James (Proc. IRE, 1957), Hines (1955) og den eksperimentelle kontrol af den ved Forsyth, Hines & Vogan (1955): kun radianter på den halvcirkel på himlen, der står vinkelret på halveringslinjen for spredningsvinklen, er nyttige, antallet af spor vokser med sin El, og nær midtpunktet falder de nyttige spor ca. H·tan El til siden, på den side der vender væk fra radianten. DJ5HG tager et forbehold: med en **lav** radiant lige langs strækningen giver McKinleys formel stærke signaler (Hamburg–Narvik, Quadrantiderne, ca. 19 UTC), så "radiant på linje med strækningen = næsten nul" gælder kun for en høj radiant; programmet forbliver forsigtigt og viser advarslen *LAV RADIANT LANGS STRÆKNINGEN*.

En uafhængig kontrol: formlen for bedste retning af **DH9GCD**, gengivet af **DF5HC** (DARC-konferencen, januar 2018) – den har ingen offentliggjort primær kilde – hvor El og Az er radiantens elevation og azimut set fra din station, og P er modstationens azimut:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Den er maksimal med radianten i 45° og på tværs af strækningen. DF5HC anser radianten for for lav under 20° og **for høj over 70°**: disse timer får ↑ i tabellen og en advarsel i [himmelkuplen](Sky-View-da#advarsler). Formlen ser bort fra afstand og højder, men er en god reference.

## Kontroller

| Kontrol | Resultat |
|---|---|
| SM6FHZ-reglen (VUSHF 2025): bedste strækning vinkelret på radiantens azimut, retning = radiantens az ±90°, tolerance ±40–50° | Gengives af modellen; med radianten på linje med strækningen og højt på himlen er effektiviteten næsten nul |
| QTFGUI af DJ5HG, Hamborg JO53IM – Barcelona, Quadrantiderne, 4. januar (eksempel fra dens manual) | QTFGUI: 07:00 retning 252°, −8 dB; 08:00 ingen refleksionszone; 09:00 retning 168°, −4 dB. YA-MS (højde 102 km som QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle tre metoder ser hullet kl. 08:00, hvor radianten står næsten i zenit |
| DJ5HG's kurver (*Die Geometrie…*, Bild 8–9: fra Hamburg og München, Quadrantiderne, 4. januar; aflæst på diagrammet, ca. ±0,5 dB og ±15 min) over for den automatiske test `--prova-dj5hg` (én værdi pr. time) | Tidspunkter: hullet med radianten nær zenit falder på de samme timer (Barcelona 07:30–08:30 mod 07–09; Sofia 06:36–07:48 mod 07–08; Narvik 07–08:30 mod 07–09); Moskva er lukket 03–10 i begge, åben fra Hamburg til ca. 02:30 og fra München til ca. 00:30, som DJ5HG skriver. Retninger: 2–10° forskel. Niveauer og form ved 102 km (middel- og RMS-afvigelse fra kurverne): ingen β, ingen længere spor −1,6 / 4,0 dB; længere spor +1,1 / 4,6 dB; β −5,4 / 6,2 dB, men med den bedste form (3,0 dB efter fjernelse af middelværdien, mod 3,6): de dybe minima med lav radiant viser sig (Barcelona −15,6 dB kl. 17 mod −16 dB kl. 19:36; Sofia −18,5 dB kl. 20 mod −14 dB). β og længere spor (*Som DJ5HG*) −2,2 / 4,7 dB; den forsigtige beregningsindstilling (radarhøjde 89,5 km, β slået til, ingen længere spor) −6,9 / 7,6 dB, form 3,3 dB. Uden β viser YA-MS knap minimummet med radianten lavt og næsten på linje med strækningen (−8,6 og −10,4 dB): det er DJ5HG's eget forbehold, deraf advarslen |
| Sampling for hver 5 km i stedet for 15 km | procenterne ændrer sig mindre end 0,3 point |

> Dokumentationen til MS-Soft 5.2 definerer OH5IY's effektivitet som et relativt indeks kun for underdense spor, med to faktorer (radiantens elevation, bedst ca. 45°, og vinkel til strækningen, bedst 90°) og et minimum, der er hævet manuelt til 20 % for overdense spor; formlen er ikke offentliggjort. MCG_MS beregner den for fire faste retninger og, med DX-lokatoren, for den faktiske strækning. Modellen tager kun højde for underdense spor med isotrope antenner; overdense bursts og den sporadiske baggrund indgår ikke i effektiviteten (den sporadiske baggrund repræsenteres af radarfluxen). Fra 1.8.1 anvendes antennernes lodrette diagram, når feltet «antennediagram» er slået til; i azimut forbliver antennerne isotrope.
