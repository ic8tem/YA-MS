[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · **Afrikaans** · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Probleemoplossing en gereelde vrae

## Installering en opstart

### Windows SmartScreen sê "Windows protected your PC"
Die program is nie met 'n kommersiële sertifikaat onderteken nie. Klik op *More info* → *Run anyway*. Laai dit slegs van die [Releases](https://github.com/ic8tem/YA-MS/releases)-bladsy af.

### macOS: kan nie oopgemaak word nie omdat dit van 'n onbekende ontwikkelaar is
YA-MS is nie deur Apple onderteken nie, so **Gatekeeper** blokkeer dit die eerste keer. In die `.dmg`, **regsklik op "Installa YA-MS.command" → Open** en bevestig. Die skrip verwyder die kwarantynvlag "van die internet afgelaai" van `~/YA-MS/YA-MS.app` en open dit. As macOS steeds weier, open *System Settings → Privacy & Security* en druk *Open Anyway*.

### macOS: watter .dmg?
`-mac-apple-silicon.dmg` vir M1/M2/M3/M4-verwerkers, `-mac-intel.dmg` vir Intel-Macs (Apple-kieslys → *About This Mac* sê watter een).

### Linux: YA-MS is nie in die toepassingskieslys nie
Voer `./installa.sh` uit vanuit die uitgepakte gids (nie vanuit `~/YA-MS` nie). Sommige lessenaars het 'n afmeld/aanmeld nodig om nuwe inskrywings te wys. Jy kan dit altyd met `~/YA-MS/YA-MS` begin.

### Die kaart van Europa ontbreek
*Kaart van Europa nie beskikbaar nie (netwerk nodig by eerste opstart).* Die Natural Earth-kaart word by die eerste opstart in `data/mappa` afgelaai. Koppel aan die internet en begin YA-MS weer.

## Vertoning

### Linux: Japannese teks verskyn as blokkies
Jou stelsel het nie CJK-lettertipes (Chinees, Japannees, Koreaans) nie. Installeer die **Noto CJK**-lettertipes en begin YA-MS weer. Dieselfde gebeur met Arabies, Hebreeus, Oerdoe, Hindi en Bengaals: installeer op Debian, Ubuntu en Raspberry Pi OS ook `fonts-noto-core`.

| Distribusie | Opdrag |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Die teks is te klein, of die grafieke het nie plek nie
Gebruik die skuifbalk **Lettertipe** (85–140 %) en vou die rye weg met **Kontroles**. Sien [Instellings](Settings-and-Data-Folder-af#lettertipe-en-kontroles).

### Die skerm is snags te helder
Kies **Nag** of **Swart** in die lys **Tema**.

## Internet en radardata

### Boodskap "Geen internetverbinding nie"
YA-MS wys dit **een keer** wanneer geen bron bereik kan word nie; die statusbalk word rooi. Die program werk voort met die **laaste gestoorde data** en probeer self elke 5 minute weer; *Verbinding herstel.* verskyn wanneer die netwerk terug is. Niks om te doen nie.

### Oranje waarskuwing in Radarvloed: "Kan nie die vertikale vloedskaal lees nie …"
Die Collm-radar verander sy vertikale skaal elke dag en YA-MS lees dit van die grafiek se etikette af. As 'n etiket nie gelees kan word nie, gebruik die program die gekalibreerde skaal 0–1200 meteore/uur en waarsku dat die **waardes nagegaan moet word**. Gewoonlik word die volgende uurlikse grafiek reg gelees. As jy vir baie ure *Grafiekformaat het verander* of *Vloed-asse nie op die verwagte plek gevind nie* sien, het die radar sy grafiekformaat verander: [rapporteer dit asseblief](Contributing-and-Contacts-af).

### "Die skaal van die hoogtegrafiek het verander"
Hoogtestatistieke (modus, gemiddeld, mediaan) bly geldig; slegs die absolute tellings van die hoogtehistogram nie.

### "Radarvloed: geen data nie"
Druk **Laai nou af** in [Radarvloed](Radar-Flux-af), en kontroleer dat `data/fonti_radar.csv` `attivo=1` vir Collm het.

### RMOB: waarom is die outomatiese aflaai af?
RMOB vra dat **outomatiese programme nie sy lêers aflaai nie**. Skakel *outomatiese aflaai elke 5 minute* slegs aan nadat RMOB jou toestemming gegee het. Gebruik intussen **Laai RMOB nou af** of **Laai RMOB-lêer van skyf...**. Sien [Eksperimentele voorspellings](Experimental-Forecasts-af#rmob-en-outomatiese-programme).

### RMOB: "Lêerformaat nie herken nie" of min ure gelees
Gebruik die waarnemer se maandelikse tekslêer (`NAME_MMYYYYrmob.TXT`) of 'n bulletintabel met 'n enkele waarnemer. Die aanpassing van die eksponent het minstens 3 ure nodig wat met die Collm-data (gister en vandag) ooreenstem.

## Berekeninge

### "Ongeldige stasielokator" / "Ongeldige lokator van die DX-stasie"
Lokators moet 4, 6 of 8 karakters hê (bv. `JN70`, `JN70CN`, `JN70CN12`).

### "Geen gemeenskaplike E-laagsone nie"
Die pad is langer as twee keer die bereik op spoorhoogte (ongeveer 2 × 1062 km met die lob op 0° en spore op 89,5 km): 'n enkele meteor scatter-sprong kan dit nie dek nie. As jy die **Lob-elevasie** verhoog, word die bereik nog korter.

### Hot A / Hot B is grys
Hulle is reeds **binne jou antennalob** wanneer die antenna na die DX gerig is: dit is nie nodig om te draai nie. Sien [Hemelkoepel](Sky-View-af#waarskuwings).

### Die doeltreffendheid verskil van MCG_MS of MS-Soft
YA-MS gebruik die werklike pad en sy eie model; die skaal van OH5IY en MCG_MS is nie in besonderhede gedokumenteer nie. Vergelyk ure en tendense eerder as absolute persentasies, en sien die [model](Efficiency-Calculation-af#die-model).

### Die GRAVES-bundeldeurgang lyk verskuif
Die bundelvolgorde word uit die rekenaarhorlosie bereken: sinchroniseer dit met 'n NTP-bediener. Die GRAVES-beheerstasie skuif die volgorde ook soms 'n paar stappe; die besonderhede is 'n voorspelling wat deur luister bevestig moet word.

## Ander vrae

**Is YA-MS gratis?** Ja, dit is 'n gratis program vir radioamateurs.

**Beheer dit my rotor of radio?** Nee. YA-MS is 'n voorspellings- en beplanningshulpmiddel; gebruik jou program vir digitale modusse (bv. MSHV, WSJT-X) vir die QSO.

**Werk dit bo 432 MHz?** Die bandlys stop by 432 MHz (28, 50, 70, 144, 222, 432). Die eksperimentele voorspelling aanvaar enige frekwensie van 28 tot 1300 MHz, maar die SM6FHZ-reëls wat dit gebruik, kom uit ervaring op 144 en 432 MHz.

**Iets het verkeerd geloop.** Skryf aan die outeur met jou bedryfstelsel, die YA-MS-weergawe en wat jy gedoen het: sien [Bydra en kontak](Contributing-and-Contacts-af).
