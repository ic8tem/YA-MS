[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · **Norsk** · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Feilsøking og FAQ

## Installasjon og oppstart

### Windows SmartScreen sier «Windows beskyttet PC-en»
Programmet er ikke signert med et kommersielt sertifikat. Klikk *Mer informasjon* → *Kjør likevel*. Last det bare ned fra siden [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: kan ikke åpnes fordi det er fra en ukjent utvikler
YA-MS er ikke signert av Apple, så **Gatekeeper** blokkerer det første gang. I `.dmg`-filen: **høyreklikk på «Installa YA-MS.command» → Åpne** og bekreft. Skriptet fjerner karantenemerket «lastet ned fra internett» fra `~/YA-MS/YA-MS.app` og åpner det. Hvis macOS fortsatt nekter, åpne *Systeminnstillinger → Personvern og sikkerhet* og trykk *Åpne likevel*.

### macOS: hvilken .dmg?
`-mac-apple-silicon.dmg` for M1/M2/M3/M4-prosessorer, `-mac-intel.dmg` for Intel-Macer (Apple-menyen → *Om denne Macen* viser hvilken du har).

### Linux: YA-MS er ikke i programmenyen
Kjør `./installa.sh` fra den utpakkede mappen (ikke fra `~/YA-MS`). Noen skrivebordsmiljøer krever at du logger ut og inn igjen før nye oppføringer vises. Du kan alltid starte det med `~/YA-MS/YA-MS`.

### Europakartet mangler
*Europakartet er ikke tilgjengelig (nett kreves ved første oppstart).* Natural Earth-kartet lastes ned til `data/mappa` ved første oppstart. Koble til internett og start YA-MS på nytt.

## Visning

### Linux: japansk tekst vises som firkanter
Systemet mangler CJK-skrifter. Installer **Noto CJK**-skriftene og start YA-MS på nytt:

| Distribusjon | Kommando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Teksten er for liten, eller diagrammene har ikke plass
Bruk glidebryteren **Skrift** (100–300 %) og fell sammen radene med **Kontroller**. Se [Innstillinger](Settings-and-Data-Folder-nb#skrift-og-kontroller).

### Skjermen er for lys om natten
Velg **Natt** eller **Svart** i listen **Tema**.

## Internett og radardata

### Meldingen «Ingen internettforbindelse»
YA-MS viser den **én gang** når ingen kilde kan nås; statuslinjen blir rød. Programmet arbeider videre med de **sist lagrede dataene** og prøver på nytt av seg selv hvert 5. minutt; *Forbindelsen er gjenopprettet.* vises når nettet er tilbake. Du trenger ikke gjøre noe.

### Oransje advarsel i Radarfluks: «Kan ikke lese den vertikale fluksskalaen …»
Collm-radaren endrer den vertikale skalaen hver dag, og YA-MS leser den fra etikettene i diagrammet. Hvis en etikett ikke kan leses, bruker programmet den kalibrerte skalaen 0–1200 meteorer/time og varsler at **verdiene må kontrolleres**. Som regel leses neste timediagram riktig. Hvis du ser *Diagramformatet er endret* eller *Fluksaksene ble ikke funnet på forventet sted* i mange timer, har radaren endret diagramformatet: [meld fra](Contributing-and-Contacts-nb) om det.

### «Skalaen i høydediagrammet er endret»
Høydestatistikken (typetall, middel, median) er fortsatt gyldig; bare de absolutte tellingene i høydehistogrammet er det ikke.

### «Radarfluks: ingen data»
Trykk **Last ned nå** i [Radarfluks](Radar-Flux-nb), og kontroller at `data/fonti_radar.csv` har `attivo=1` for Collm.

### RMOB: hvorfor er automatisk nedlasting avslått?
RMOB ber om at **automatiske programmer ikke henter filene deres**. Slå på *automatisk nedlasting hvert 5. minutt* bare etter at RMOB har gitt deg tillatelse. Bruk i mellomtiden **Last ned RMOB nå** eller **Last inn RMOB-fil fra disk...**. Se [Eksperimentelle prognoser](Experimental-Forecasts-nb#rmob-og-automatiske-programmer).

### RMOB: «Filformatet ble ikke gjenkjent» eller få timer lest
Bruk observatørens månedlige tekstfil (`NAME_MMYYYYrmob.TXT`) eller en bulletintabell med bare én observatør. Tilpasningen av eksponenten krever minst 3 timer felles med Collm-dataene (i går og i dag).

## Beregninger

### «Ugyldig stasjonslokator» / «Ugyldig lokator for motstasjonen»
Lokatorer må ha 4, 6 eller 8 tegn (f.eks. `JN70`, `JN70CN`, `JN70CN12`).

### «Ingen felles sone i E-laget»
Strekningen er lengre enn dobbelt rekkevidde i sporhøyden (ca. 2 × 1062 km med loben på 0° og spor i 89,5 km): ett enkelt meteor scatter-hopp kan ikke dekke den. Hever du **Lobeelevasjon**, blir rekkevidden enda kortere.

### Hot A / Hot B er grå
De ligger allerede **innenfor antenneloben** når du peker mot DX: ingen grunn til å dreie. Se [Himmelhvelving](Sky-View-nb#advarsler).

### Effektiviteten avviker fra MCG_MS eller MS-Soft
YA-MS bruker den faktiske strekningen og sin egen modell; skalaen til OH5IY og MCG_MS er ikke dokumentert i detalj. Sammenlign timer og tendenser heller enn absolutte prosenter, og se [modellen](Efficiency-Calculation-nb#modellen).

### GRAVES-strålens passering virker forskjøvet
Strålesekvensen beregnes ut fra PC-klokken: synkroniser den med en NTP-server. Kommandostasjonen til GRAVES forskyver også iblant sekvensen noen steg; detaljene er en prognose som må bekreftes ved lytting.

## Andre spørsmål

**Er YA-MS gratis?** Ja, det er et gratis program for radioamatører.

**Styrer det rotoren eller radioen min?** Nei. YA-MS er et verktøy for prognoser og planlegging; bruk programmet ditt for digitale modi (f.eks. MSHV, WSJT-X) til QSO-en.

**Fungerer det over 432 MHz?** Båndlisten stopper på 432 MHz (28, 50, 70, 144, 222, 432). Den eksperimentelle prognosen godtar vilkårlig frekvens fra 28 til 1300 MHz, men SM6FHZ-reglene den bruker, bygger på erfaring fra 144 og 432 MHz.

**Noe gikk galt.** Skriv til forfatteren med operativsystem, YA-MS-versjon og hva du gjorde: se [Bidra og kontakt](Contributing-and-Contacts-nb).
