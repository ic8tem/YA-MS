[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · **Dansk** · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [ไทย](Troubleshooting-FAQ-th) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Fejlfinding og FAQ

## Installation og opstart

### Windows SmartScreen siger "Windows beskyttede din pc"
Programmet er ikke signeret med et kommercielt certifikat. Klik på *Flere oplysninger* → *Kør alligevel*. Hent det kun fra siden [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: kan ikke åbnes, fordi det er fra en ukendt udvikler
YA-MS er ikke signeret af Apple, så **Gatekeeper** blokerer det første gang. I `.dmg`-filen: **højreklik på "Installa YA-MS.command" → Åbn**, og bekræft. Scriptet fjerner karantænemarkeringen "hentet fra internettet" fra `~/YA-MS/YA-MS.app` og åbner det. Hvis macOS stadig nægter, så åbn *Systemindstillinger → Anonymitet & sikkerhed*, og tryk på *Åbn alligevel*.

### macOS: hvilken .dmg?
`-mac-apple-silicon.dmg` til M1/M2/M3/M4-processorer, `-mac-intel.dmg` til Intel-Mac'er (Apple-menuen → *Om denne Mac* fortæller, hvilken du har).

### Linux: YA-MS er ikke i programmenuen
Kør `./installa.sh` fra den udpakkede mappe (ikke fra `~/YA-MS`). Nogle skriveborde kræver, at man logger ud og ind igen, før nye punkter vises. Du kan altid starte det med `~/YA-MS/YA-MS`.

### Europakortet mangler
*Europakort ikke tilgængeligt (kræver netværk ved første opstart).* Natural Earth-kortet hentes til `data/mappa` ved første opstart. Opret forbindelse til internettet, og genstart YA-MS.

## Visning

### Linux: japansk tekst vises som firkanter
Dit system mangler CJK-skrifttyper. Installér **Noto CJK**-skrifttyperne, og genstart YA-MS:

| Distribution | Kommando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Teksten er for lille, eller graferne har ikke plads
Brug skyderen **Skrifttype** (100–300 %), og fold rækkerne sammen med **Betjening**. Se [Indstillinger](Settings-and-Data-Folder-da#skrifttype-og-betjening).

### Skærmen er for lys om natten
Vælg **Nat** eller **Sort** i listen **Tema**.

## Internet og radardata

### Meddelelsen "Ingen internetforbindelse"
YA-MS viser den **én gang**, når ingen kilde kan nås; statuslinjen bliver rød. Programmet arbejder videre med de **senest gemte data** og prøver selv igen hvert 5. minut; *Forbindelsen er genoprettet.* vises, når netværket er tilbage. Du skal ikke gøre noget.

### Orange advarsel i Radarflux: "Kan ikke aflæse fluxens lodrette skala …"
Collm-radaren ændrer sin lodrette skala hver dag, og YA-MS aflæser den fra grafens etiketter. Hvis en etiket ikke kan aflæses, bruger programmet den kalibrerede skala 0–1200 meteorer/time og advarer om, at **værdierne skal kontrolleres**. Som regel aflæses den næste timegraf korrekt. Hvis du ser *Grafens format er ændret* eller *Fluxakserne blev ikke fundet på den forventede plads* i mange timer, har radaren ændret sit grafformat: [meld det](Contributing-and-Contacts-da) venligst.

### "Skalaen på højdegrafen er ændret"
Højdestatistikken (typetal, middelværdi, median) er stadig gyldig; kun højdehistogrammets absolutte tællinger er det ikke.

### "Radarflux: ingen data"
Tryk på **Hent nu** i [Radarflux](Radar-Flux-da), og kontrollér, at `data/fonti_radar.csv` har `attivo=1` for Collm.

### RMOB: hvorfor er automatisk hentning slået fra?
RMOB beder om, at **automatiske programmer ikke henter deres filer**. Slå kun *automatisk hentning hvert 5. minut* til, når RMOB har givet dig tilladelse. Brug indtil da **Hent RMOB nu** eller **Indlæs RMOB-fil fra disken...**. Se [Eksperimentelle prognoser](Experimental-Forecasts-da#rmob-og-automatiske-programmer).

### RMOB: "Filformatet blev ikke genkendt" eller få timer læst
Brug observatørens månedlige tekstfil (`NAME_MMYYYYrmob.TXT`) eller en bulletintabel med kun én observatør. Tilpasningen af eksponenten kræver mindst 3 timer til fælles med Collm-dataene (i går og i dag).

## Beregninger

### "Ugyldig stationslokator" / "Ugyldig lokator for modstationen"
Lokatorer skal have 4, 6 eller 8 tegn (fx `JN70`, `JN70CN`, `JN70CN12`).

### "Ingen fælles zone i E-laget"
Strækningen er længere end det dobbelte af rækkevidden i sporhøjde (ca. 2 × 1062 km med lappen i 0° og spor i 89,5 km): ét enkelt meteor scatter-hop kan ikke dække den. Hæves **Lapelevation**, bliver rækkevidden endnu kortere.

### Hot A / Hot B er grå
De ligger allerede **inden for din antennelap**, når du peger mod DX: ingen grund til at dreje. Se [Himmelkuppel](Sky-View-da#advarsler).

### Effektiviteten afviger fra MCG_MS eller MS-Soft
YA-MS bruger den faktiske strækning og sin egen model; skalaen i OH5IY og MCG_MS er ikke dokumenteret i detaljer. Sammenlign timer og tendenser frem for absolutte procenter, og se [modellen](Efficiency-Calculation-da#modellen).

### GRAVES-strålens passage virker forskudt
Strålesekvensen beregnes ud fra pc'ens ur: synkronisér det med en NTP-server. GRAVES' kommandostation forskyder også sommetider sekvensen nogle trin; detaljen er en prognose, der skal bekræftes ved at lytte.

## Andre spørgsmål

**Er YA-MS gratis?** Ja, det er et gratis program til radioamatører.

**Styrer det min rotor eller radio?** Nej. YA-MS er et værktøj til prognoser og planlægning; brug dit program til digitale modes (fx MSHV, WSJT-X) til QSO'en.

**Virker det over 432 MHz?** Båndlisten stopper ved 432 MHz (28, 50, 70, 144, 222, 432). Den eksperimentelle prognose accepterer enhver frekvens fra 28 til 1300 MHz, men de SM6FHZ-regler, den bruger, stammer fra erfaringer på 144 og 432 MHz.

**Noget gik galt.** Skriv til forfatteren med dit styresystem, YA-MS-versionen og hvad du gjorde: se [Bidrag og kontakt](Contributing-and-Contacts-da).
