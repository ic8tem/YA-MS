[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · **Svenska** · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [ไทย](Troubleshooting-FAQ-th) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Felsökning och FAQ

## Installation och start

### Windows SmartScreen säger "Windows skyddade datorn"
Programmet är inte signerat med ett kommersiellt certifikat. Klicka på *Mer information* → *Kör ändå*. Ladda bara ned det från sidan [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: kan inte öppnas eftersom den kommer från en oidentifierad utvecklare
YA-MS är inte signerat av Apple, så **Gatekeeper** blockerar det första gången. I `.dmg`-filen, **högerklicka på "Installa YA-MS.command" → Öppna** och bekräfta. Skriptet tar bort karantänflaggan "hämtad från internet" från `~/YA-MS/YA-MS.app` och öppnar det. Om macOS fortfarande vägrar, öppna *Systeminställningar → Integritet och säkerhet* och tryck på *Öppna ändå*.

### macOS: vilken .dmg?
`-mac-apple-silicon.dmg` för processorerna M1/M2/M3/M4, `-mac-intel.dmg` för Mac med Intel (Apple-menyn → *Om den här datorn* visar vilken du har).

### Linux: YA-MS finns inte i programmenyn
Kör `./installa.sh` i den uppackade mappen (inte i `~/YA-MS`). Vissa skrivbordsmiljöer kräver utloggning/inloggning för att visa nya poster. Du kan alltid starta det med `~/YA-MS/YA-MS`.

### Europakartan saknas
*Europakartan är inte tillgänglig (nätverk krävs vid första start).* Kartan från Natural Earth hämtas till `data/mappa` vid första starten. Anslut till internet och starta om YA-MS.

## Visning

### Linux: japansk text visas som rutor
Ditt system saknar CJK-typsnitt. Installera typsnitten **Noto CJK** och starta om YA-MS:

| Distribution | Kommando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Texten är för liten, eller diagrammen får inte plats
Använd reglaget **Typsnitt** (100–300 %) och fäll ihop raderna med **Reglage**. Se [Inställningar](Settings-and-Data-Folder-sv#typsnitt-och-reglage).

### Skärmen är för ljus på natten
Välj **Natt** eller **Svart** i listan **Tema**.

## Internet och radardata

### Meddelandet "Ingen internetanslutning"
YA-MS visar det **en gång** när ingen källa kan nås; statusraden blir röd. Programmet fortsätter att arbeta med **senast sparade data** och försöker igen automatiskt var 5:e minut; *Anslutningen återställd.* visas när nätverket är tillbaka. Du behöver inte göra något.

### Orange varning i Radarflöde: "Kan inte läsa flödets vertikala skala …"
Collm-radarn ändrar sin vertikala skala varje dag och YA-MS läser den från diagrammets etiketter. Om en etikett inte kan läsas använder programmet den kalibrerade skalan 0–1200 meteorer/timme och varnar att **värdena bör kontrolleras**. Oftast läses nästa timdiagram korrekt. Om du ser *Diagrammets format har ändrats* eller *Flödesaxlarna hittades inte på förväntad plats* under många timmar har radarn ändrat sitt diagramformat: [rapportera det](Contributing-and-Contacts-sv) gärna.

### "Höjddiagrammets skala har ändrats"
Höjdstatistiken (typvärde, medel, median) gäller fortfarande; det är bara de absoluta antalen i höjdhistogrammet som inte gör det.

### "Radarflöde: inga data"
Tryck på **Hämta nu** i [Radarflöde](Radar-Flux-sv) och kontrollera att `data/fonti_radar.csv` har `attivo=1` för Collm.

### RMOB: varför är automatisk hämtning avstängd?
RMOB ber att **automatiska program inte hämtar dess filer**. Aktivera *automatisk hämtning var 5:e minut* först när RMOB har gett dig tillstånd. Använd under tiden **Hämta RMOB nu** eller **Läs in RMOB-fil från disk...**. Se [Experimentella prognoser](Experimental-Forecasts-sv#rmob-och-automatiska-program).

### RMOB: "Filformatet känns inte igen." eller få timmar lästa
Använd observatörens månatliga textfil (`NAME_MMYYYYrmob.TXT`) eller en bulletintabell med en enda observatör. Anpassningen av exponenten kräver minst 3 timmar gemensamt med data från Collm (igår och idag).

## Beräkningar

### "Ogiltig stationslokator" / "Ogiltig lokator för motstationen"
Lokatorer måste ha 4, 6 eller 8 tecken (t.ex. `JN70`, `JN70CN`, `JN70CN12`).

### "Ingen gemensam zon i E-skiktet"
Sträckan är längre än två gånger räckvidden på spårhöjden (omkring 2 × 1062 km med loben på 0° och spår på 89,5 km): ett enda meteorscatterhopp kan inte täcka den. Att höja **Lobelevation** förkortar räckvidden ytterligare.

### Hot A / Hot B är grå
De ligger redan **inom din antennlob** när du riktar mot DX: du behöver inte vrida. Se [Himlavalv](Sky-View-sv#varningar).

### Effektiviteten skiljer sig från MCG_MS eller MS-Soft
YA-MS använder den verkliga sträckan och en egen modell; skalan i OH5IY och MCG_MS är inte dokumenterad i detalj. Jämför timmar och trender snarare än absoluta procentsatser, och se [modellen](Efficiency-Calculation-sv#modellen).

### GRAVES lobpassage verkar förskjuten
Lobsekvensen beräknas från datorns klocka: synkronisera den mot en NTP-server. GRAVES kommandostation förskjuter också ibland sekvensen några steg; detaljvyn är en förutsägelse som ska bekräftas genom att lyssna.

## Övriga frågor

**Är YA-MS gratis?** Ja, det är ett gratisprogram för radioamatörer.

**Styr det min rotor eller min radio?** Nej. YA-MS är ett verktyg för prognoser och planering; använd ditt program för digitala moder (t.ex. MSHV, WSJT-X) för QSO:t.

**Fungerar det över 432 MHz?** Bandlistan slutar vid 432 MHz (28, 50, 70, 144, 222, 432). Den experimentella prognosen godtar valfri frekvens från 28 till 1300 MHz, men SM6FHZ:s regler som den använder kommer från erfarenheter på 144 och 432 MHz.

**Något gick fel.** Skriv till upphovsmannen och ange operativsystem, YA-MS-version och vad du gjorde: se [Bidrag och kontakter](Contributing-and-Contacts-sv).
