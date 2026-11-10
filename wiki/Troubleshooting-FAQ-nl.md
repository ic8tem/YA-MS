[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · **Nederlands** · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Problemen en FAQ

## Installatie en opstarten

### Windows SmartScreen zegt "Windows heeft uw pc beschermd"
Het programma is niet ondertekend met een commercieel certificaat. Klik op *Meer informatie* → *Toch uitvoeren*. Download het alleen van de pagina [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: kan niet worden geopend omdat het van een onbekende ontwikkelaar is
YA-MS is niet door Apple ondertekend, dus **Gatekeeper** blokkeert het de eerste keer. Klik in de `.dmg` **met de rechtermuisknop op "Installa YA-MS.command" → Open** en bevestig. Het script verwijdert de quarantainemarkering "gedownload van internet" van `~/YA-MS/YA-MS.app` en opent het. Als macOS nog steeds weigert, open dan *Systeeminstellingen → Privacy en beveiliging* en druk op *Open toch*.

### macOS: welke .dmg?
`-mac-apple-silicon.dmg` voor M1/M2/M3/M4-processors, `-mac-intel.dmg` voor Intel-Macs (Apple-menu → *Over deze Mac* vertelt je welke je hebt).

### Linux: YA-MS staat niet in het toepassingenmenu
Voer `./installa.sh` uit vanuit de uitgepakte map (niet vanuit `~/YA-MS`). Sommige desktops hebben uitloggen/inloggen nodig om nieuwe items te tonen. Je kunt het altijd starten met `~/YA-MS/YA-MS`.

### De kaart van Europa ontbreekt
*Kaart van Europa niet beschikbaar (netwerk nodig bij de eerste start).* De kaart van Natural Earth wordt bij de eerste start gedownload naar `data/mappa`. Maak verbinding met internet en start YA-MS opnieuw.

## Weergave

### Linux: Japanse tekst verschijnt als vierkantjes
Je systeem mist CJK-lettertypen. Installeer de **Noto CJK**-lettertypen en start YA-MS opnieuw:

| Distributie | Commando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### De tekst is te klein, of de grafieken hebben geen ruimte
Gebruik de schuifregelaar **Lettertype** (100–300 %) en klap de rijen in met **Bediening**. Zie [Instellingen](Settings-and-Data-Folder-nl#lettertype-en-bediening).

### Het scherm is 's nachts te fel
Kies **Nacht** of **Zwart** in de lijst **Kleurenschema**.

## Internet en radargegevens

### Melding "Geen internetverbinding"
YA-MS toont die **eenmalig** als geen enkele bron bereikbaar is; de statusbalk wordt rood. Het programma blijft werken met de **laatst opgeslagen gegevens** en probeert het zelf elke 5 minuten opnieuw; *Verbinding hersteld.* verschijnt als het netwerk terug is. Je hoeft niets te doen.

### Oranje waarschuwing in Radarflux: "Kan de verticale schaal van de flux niet lezen …"
De radar in Collm verandert elke dag zijn verticale schaal en YA-MS leest die uit de labels van de grafiek. Als een label niet leesbaar is, gebruikt het programma de geijkte schaal 0–1200 meteoren/uur en waarschuwt dat de **waarden gecontroleerd moeten worden**. Meestal wordt de grafiek van het volgende uur goed gelezen. Als je urenlang *Grafiekformaat gewijzigd* of *Fluxassen niet op de verwachte positie gevonden* ziet, heeft de radar het formaat van de grafiek veranderd: [meld het](Contributing-and-Contacts-nl) alsjeblieft.

### "De schaal van de hoogtegrafiek is gewijzigd"
De hoogtestatistieken (modus, gemiddelde, mediaan) blijven geldig; alleen de absolute aantallen van het hoogtehistogram niet.

### "Radarflux: geen gegevens"
Druk op **Nu downloaden** in [Radarflux](Radar-Flux-nl) en controleer of `data/fonti_radar.csv` voor Collm `attivo=1` heeft.

### RMOB: waarom staat het automatisch ophalen uit?
RMOB vraagt **automatische programma's om zijn bestanden niet op te halen**. Schakel *automatisch ophalen elke 5 minuten* pas in nadat RMOB je toestemming heeft gegeven. Gebruik intussen **RMOB nu downloaden** of **RMOB-bestand van schijf laden...**. Zie [Experimentele voorspelling](Experimental-Forecasts-nl#rmob-en-automatische-programmas).

### RMOB: "Bestandsformaat niet herkend" of weinig uren gelezen
Gebruik het maandelijkse tekstbestand van de waarnemer (`NAAM_MMJJJJrmob.TXT`) of een bulletintabel met één waarnemer. Voor het bepalen van de exponent zijn minstens 3 uren nodig die gemeenschappelijk zijn met de gegevens van Collm (gisteren en vandaag).

## Berekeningen

### "Ongeldige locator van het station" / "Ongeldige locator van het tegenstation"
Locators moeten 4, 6 of 8 tekens hebben (bijv. `JN70`, `JN70CN`, `JN70CN12`).

### "Geen gemeenschappelijke zone in de E-laag"
Het traject is langer dan tweemaal het bereik op spoorhoogte (ongeveer 2 × 1062 km met de bundel op 0° en sporen op 89,5 km): één meteorscatter-sprong kan het niet overbruggen. Door de **Elevatie bundel** te verhogen, wordt het bereik nog korter.

### Hot A / Hot B zijn grijs
Ze liggen al **binnen je antennebundel** als je op de DX richt: draaien is niet nodig. Zie [Hemelkoepel](Sky-View-nl#waarschuwingen).

### De efficiëntie wijkt af van MCG_MS of MS-Soft
YA-MS gebruikt het werkelijke traject en een eigen model; de schaal van OH5IY en MCG_MS is niet in detail gedocumenteerd. Vergelijk liever uren en trends dan absolute percentages, en zie het [model](Efficiency-Calculation-nl#het-model).

### De bundeldoorgang van GRAVES lijkt verschoven
De bundelvolgorde wordt berekend uit de pc-klok: synchroniseer die met een NTP-server. Bovendien verschuift het commandostation van GRAVES de volgorde soms een paar stappen; het detail is een voorspelling die je door te luisteren moet bevestigen.

## Overige vragen

**Is YA-MS gratis?** Ja, het is een gratis programma voor radioamateurs.

**Bestuurt het mijn rotor of transceiver?** Nee. YA-MS is een hulpmiddel voor voorspelling en planning; gebruik voor de QSO je programma voor digitale modes (bijv. MSHV, WSJT-X).

**Werkt het boven 432 MHz?** De bandenlijst stopt bij 432 MHz (28, 50, 70, 144, 222, 432). De experimentele voorspelling accepteert elke frequentie van 28 tot 1300 MHz, maar de regels van SM6FHZ die ze gebruikt, komen uit ervaring op 144 en 432 MHz.

**Er ging iets mis.** Schrijf de auteur met je besturingssysteem, de versie van YA-MS en wat je hebt gedaan: zie [Bijdragen en contact](Contributing-and-Contacts-nl).
