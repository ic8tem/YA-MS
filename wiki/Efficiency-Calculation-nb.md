[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · **Norsk** · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Samme lov ligger til grunn for QTFGUI av DJ5HG (kjegleformet spredning). Betingelsen godtas med en gaussisk toleranse σ = 0,05 rad (ca. 3°) – *programmets valg*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Vekten til hvert punkt.** Effekten fra et underdenst spor (McKinley), φ = halve spredningsvinkelen (begrenset til 85°, *valg*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Antallet meteorer som når et punkt, er proporsjonalt med sinus til radiantens elevasjon der (ŝ·û_P), den samme korreksjonen som IMO bruker for ZHR.

**3. Sum og prosent.** Punkter for hver 15 km i sporhøyden, bare der begge stasjonene ser dem over lobeelevasjonen (*valg*). 100 % er den gunstigste radiantposisjonen for den strekningen:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F beregnes én gang per strekning på et rutenett av retninger (asimut for hver 5°, elevasjon for hver 2,5°) og interpoleres.

**4. Side og indeks.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Bokstaven i tabellen er siden med størst andel. *Programmets valg (håndbokens likn. 32–33).*

## Sammenligning med DH9GCD

En uavhengig kontroll: formelen for beste retning av **DH9GCD**, gjengitt av **DF5HC** (DARC-konferansen, januar 2018), der El og Az er radiantens elevasjon og asimut sett fra stasjonen din og P er motstasjonens asimut:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Den er størst med radianten på 45° og på tvers av strekningen. DF5HC regner radianten som for lav under 20° og **for høy over 70°**: disse timene får ↑ i tabellen og en advarsel i [himmelhvelvingen](Sky-View-nb#advarsler). Formelen ser bort fra avstand og høyder, men er en god referanse.

## Kontroller

| Kontroll | Resultat |
|---|---|
| SM6FHZ-regelen (VUSHF 2025): beste strekning vinkelrett på radiantens asimut, retning = radiantens az ±90°, toleranse ±40–50° | Gjengis av modellen; med radianten på linje med strekningen og høyt på himmelen er effektiviteten nesten null |
| QTFGUI av DJ5HG, Hamburg JO53IM – Barcelona, Kvadrantidene, 4. januar (eksempel fra håndboken) | QTFGUI: 07:00 retning 252°, −8 dB; 08:00 ingen refleksjonssone; 09:00 retning 168°, −4 dB. YA-MS (høyde 102 km som QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Alle tre metodene ser hullet kl. 08:00, med radianten nesten i senit |
| Sampling for hver 5 km i stedet for 15 km | prosentene endres med mindre enn 0,3 poeng |

> Skalaen som OH5IY og MCG_MS bruker, er ikke kjent i detalj (MS-Soft-håndbøkene er ikke tilgjengelige): sammenlign prosentene med disse programmene før du regner dem som likeverdige. Modellen tar bare hensyn til underdense spor, med isotrope antenner; overdense utbrudd og sporadisk bakgrunn inngår ikke i effektiviteten (den sporadiske bakgrunnen representeres av radarfluksen).
