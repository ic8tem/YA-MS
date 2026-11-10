[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · **Dansk** · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Effektivitetsberegning

*Fane: Prognoseberegning › Effektivitetsberegning.*

[![Effektivitetsberegning](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

En sværms **effektivitet** angiver i procent, hvor meget dens radiants position tillader refleksioner på **din** strækning. Begrebet stammer fra Ilkka **OH5IY** (MS-Soft) og tages op i artiklen af Cerrotta–Sartori: effektivitetens maksimum falder ikke sammen med det visuelle maksimum (ZHR), fordi det afhænger af, hvor radianten står i forhold til de to stationer. MCG_MS af DL5MCG anvender samme idé på fire faste retninger; YA-MS beregner den for den **faktiske strækning** mellem de to lokatorer.

Fanen viser den time for time for den dag, der er valgt i *Dag for 24 t-tabellen (UTC)* (værdier ved halv).

## Overbliksbokse

| Boks | Indhold |
|---|---|
| **DAGENS BEDSTE TIDSPUNKT** | Timen med det højeste strækningsindeks, indekset og den fremherskende side (A/B med sin %) |
| **MEST GUNSTIGE SVÆRM** | Den sværm, der har dagens største ZHR × effektivitet, dens effektivitet, time og side og **bedste retning** (radiantens azimut +90° / −90°) |
| **NU** | Indeks og fremherskende side i denne time samt det anbefalede Hot (kun når den valgte dag er i dag) |
| **EKSPERIMENTEL PROGNOSE** | Forventede refleksioner/time nu, om 1 t og om 2 t ved prognosefrekvensen (Collm, SM6FHZ-regler; se [Eksperimentelle prognoser](Experimental-Forecasts-da)) |

Under boksene forklarer en bjælke bogstaverne A og B (se nedenfor).

## Graf

*Effektivitet pr. time for … den … (UTC, værdier ved halv).* For op til fem sværme: effektivitet % som fuldt optrukket linje og DH9GCD-formlen som prikket linje i samme farve; **strækningsindekset** som blå søjler på højre skala.

## Timetabel

Én række pr. sværm, der er aktiv den dag (sorteret efter ZHR), 24 kolonner for timerne (UTC):

| Celle | Betydning |
|---|---|
| `63A` | effektivitet 63 %, de fleste refleksioner fra side **A** |
| `41B` | effektivitet 41 %, side **B** |
| `3` | effektivitet under 5 %: tal uden sidebogstav |
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

Samme lov ligger til grund for QTFGUI af DJ5HG (keglespredning). Betingelsen accepteres med en gaussisk tolerance σ = 0,05 rad (ca. 3°) – *programmets valg*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Hvert punkts vægt.** Effekten fra et underdenst spor (McKinley), φ = halvdelen af spredningsvinklen (begrænset til 85°, *valg*):

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad w_P = \frac{1}{R_1 R_2 (R_1+R_2)\cos^2\varphi}
```

Antallet af meteorer, der når et punkt, er proportionalt med sinus til radiantens elevation dér (ŝ·û_P) – samme korrektion, som IMO bruger for ZHR.

**3. Sum og procent.** Punkter for hver 15 km i sporhøjde, kun hvor begge stationer ser dem over lapelevationen (*valg*). 100 % er den mest gunstige radiantposition for den strækning:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F beregnes én gang pr. strækning på et gitter af retninger (azimut for hver 5°, elevation for hver 2,5°) og interpoleres.

**4. Side og indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Bogstavet i tabellen er den side, der har den største andel. *Programmets valg (manualens lign. 32–33).*

## Sammenligning med DH9GCD

En uafhængig kontrol: formlen for bedste retning af **DH9GCD**, gengivet af **DF5HC** (DARC-konferencen, januar 2018), hvor El og Az er radiantens elevation og azimut set fra din station, og P er modstationens azimut:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Den er maksimal med radianten i 45° og på tværs af strækningen. DF5HC anser radianten for for lav under 20° og **for høj over 70°**: disse timer får ↑ i tabellen og en advarsel i [himmelkuplen](Sky-View-da#advarsler). Formlen ser bort fra afstand og højder, men er en god reference.

## Kontroller

| Kontrol | Resultat |
|---|---|
| SM6FHZ-reglen (VUSHF 2025): bedste strækning vinkelret på radiantens azimut, retning = radiantens az ±90°, tolerance ±40–50° | Gengives af modellen; med radianten på linje med strækningen og højt på himlen er effektiviteten næsten nul |
| QTFGUI af DJ5HG, Hamborg JO53IM – Barcelona, Quadrantiderne, 4. januar (eksempel fra dens manual) | QTFGUI: 07:00 retning 252°, −8 dB; 08:00 ingen refleksionszone; 09:00 retning 168°, −4 dB. YA-MS (højde 102 km som QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle tre metoder ser hullet kl. 08:00, hvor radianten står næsten i zenit |
| Sampling for hver 5 km i stedet for 15 km | procenterne ændrer sig mindre end 0,3 point |

> Den skala, som OH5IY og MCG_MS bruger, kendes ikke i detaljer (MS-Soft-manualerne er ikke tilgængelige): sammenlign procenterne med disse programmer, før du betragter dem som ækvivalente. Modellen tager kun højde for underdense spor med isotrope antenner; overdense bursts og den sporadiske baggrund indgår ikke i effektiviteten (den sporadiske baggrund repræsenteres af radarfluxen).
