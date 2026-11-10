[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · **Lietuvių** · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [ไทย](Troubleshooting-FAQ-th) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Trikčių šalinimas ir DUK

## Diegimas ir paleidimas

### Windows SmartScreen rodo „Windows protected your PC“
Programa nepasirašyta komerciniu sertifikatu. Spustelėkite *More info* → *Run anyway*. Atsisiųskite ją tik iš puslapio [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: negalima atverti, nes kūrėjas nenustatytas
YA-MS nepasirašyta Apple, todėl **Gatekeeper** pirmą kartą ją blokuoja. `.dmg` faile **dešiniuoju pelės mygtuku spustelėkite „Installa YA-MS.command“ → Open** ir patvirtinkite. Scenarijus pašalina „atsisiųsta iš interneto“ karantino žymą nuo `~/YA-MS/YA-MS.app` ir atveria programą. Jei macOS vis tiek atsisako, atverkite *System Settings → Privacy & Security* ir spauskite *Open Anyway*.

### macOS: kuris .dmg?
`-mac-apple-silicon.dmg` procesoriams M1/M2/M3/M4, `-mac-intel.dmg` Intel Mac kompiuteriams (Apple meniu → *About This Mac* parodo, kurį turite).

### Linux: YA-MS nėra programų meniu
Paleiskite `./installa.sh` iš išskleisto aplanko (ne iš `~/YA-MS`). Kai kurioms darbalaukio aplinkoms reikia atsijungti ir vėl prisijungti, kad būtų parodyti nauji įrašai. Programą visada galite paleisti komanda `~/YA-MS/YA-MS`.

### Nėra Europos žemėlapio
*Europos žemėlapis neprieinamas (pirmą kartą paleidžiant reikia tinklo).* Natural Earth žemėlapis atsisiunčiamas į `data/mappa` pirmą kartą paleidžiant. Prisijunkite prie interneto ir paleiskite YA-MS iš naujo.

## Rodymas

### Linux: japoniškas tekstas rodomas kvadratėliais
Jūsų sistemoje trūksta CJK šriftų. Įdiekite **Noto CJK** šriftus ir paleiskite YA-MS iš naujo:

| Distribucija | Komanda |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Tekstas per mažas arba grafikams trūksta vietos
Naudokite slankiklį **Šriftas** (100–300 %) ir suskleiskite eilutes mygtuku **Valdymas**. Žr. [Nustatymai](Settings-and-Data-Folder-lt#šriftas-ir-valdymas).

### Ekranas naktį per ryškus
Sąraše **Tema** pasirinkite **Naktis** arba **Juoda**.

## Internetas ir radarų duomenys

### Pranešimas „Nėra interneto ryšio“
YA-MS jį rodo **vieną kartą**, kai nepasiekiamas nė vienas šaltinis; būsenos juosta tampa raudona. Programa toliau veikia su **paskutiniais išsaugotais duomenimis** ir pati bando iš naujo kas 5 minutes; kai tinklas atsistato, pasirodo *Ryšys atkurtas.* Nieko daryti nereikia.

### Oranžinis įspėjimas kortelėje Radaro srautas: „Nepavyko nuskaityti vertikalios srauto skalės …“
Collm radaras kasdien keičia savo vertikalią skalę, o YA-MS ją nuskaito iš grafiko užrašų. Jei užrašo nuskaityti nepavyksta, programa naudoja kalibruotą skalę 0–1200 meteorų/val. ir įspėja, kad **vertes reikia patikrinti**. Paprastai kitas valandinis grafikas nuskaitomas teisingai. Jei daug valandų matote *Pasikeitė grafiko formatas* arba *Srauto ašys nerastos numatytoje vietoje*, radaras pakeitė grafiko formatą: [praneškite apie tai](Contributing-and-Contacts-lt).

### „Pasikeitė aukščių grafiko skalė“
Aukščių statistika (moda, vidurkis, mediana) lieka galioti; negalioja tik absoliutūs aukščių histogramos skaičiai.

### „Radaro srautas: duomenų nėra“
Kortelėje [Radaro srautas](Radar-Flux-lt) spauskite **Atsisiųsti dabar** ir patikrinkite, ar `data/fonti_radar.csv` faile Collm turi `attivo=1`.

### RMOB: kodėl automatinis atsisiuntimas išjungtas?
RMOB prašo, kad **automatinės programos neatsisiųstų jo failų**. Įjunkite *automatinis atsisiuntimas kas 5 minutes* tik tada, kai RMOB jums davė leidimą. Iki tol naudokite **Atsisiųsti RMOB dabar** arba **Įkelti RMOB failą iš disko...**. Žr. [Eksperimentinės prognozės](Experimental-Forecasts-lt#rmob-ir-automatinės-programos).

### RMOB: „Failo formatas neatpažintas“ arba nuskaityta mažai valandų
Naudokite stebėtojo mėnesio tekstinį failą (`NAME_MMYYYYrmob.TXT`) arba biuletenio lentelę su vienu stebėtoju. Rodikliui pritaikyti reikia bent 3 valandų, bendrų su Collm duomenimis (vakar ir šiandien).

## Skaičiavimai

### „Netinkamas stoties lokatorius“ / „Netinkamas korespondento lokatorius“
Lokatorius turi turėti 4, 6 arba 8 simbolius (pvz., `JN70`, `JN70CN`, `JN70CN12`).

### „Nėra bendrosios E sluoksnio zonos“
Trasa ilgesnė nei dvigubas nuotolis pėdsakų aukštyje (apie 2 × 1062 km, kai lapelis 0°, o pėdsakai 89,5 km aukštyje): vienas meteor scatter šuolis jos neįveikia. Padidinus **Lapelio elevaciją**, nuotolis dar sutrumpėja.

### Hot A / Hot B pilki
Kai antena nukreipta į DX, jie jau yra **jūsų antenos lapelyje**: sukti nereikia. Žr. [Dangaus skliautas](Sky-View-lt#įspėjimai).

### Efektyvumas skiriasi nuo MCG_MS ar MS-Soft
YA-MS naudoja realią trasą ir savo modelį; OH5IY ir MCG_MS skalė detaliai neaprašyta. Lyginkite valandas ir tendencijas, o ne absoliučius procentus, ir žr. [modelį](Efficiency-Calculation-lt#modelis).

### GRAVES pluošto praėjimas atrodo paslinktas
Pluošto seka skaičiuojama pagal PC laikrodį: sinchronizuokite jį su NTP serveriu. GRAVES valdymo stotis taip pat kartais paslenka seką keliais žingsniais; detalės yra prognozė, kurią reikia patvirtinti klausantis.

## Kiti klausimai

**Ar YA-MS nemokama?** Taip, tai nemokama programa radijo mėgėjams.

**Ar ji valdo mano sukimo įrenginį ar radijo stotį?** Ne. YA-MS – prognozavimo ir planavimo priemonė; QSO naudokite savo skaitmeninių modų programą (pvz., MSHV, WSJT-X).

**Ar ji veikia aukščiau 432 MHz?** Juostų sąrašas baigiasi ties 432 MHz (28, 50, 70, 144, 222, 432). Eksperimentinė prognozė priima bet kurį dažnį nuo 28 iki 1300 MHz, bet jos naudojamos SM6FHZ taisyklės kilusios iš patirties 144 ir 432 MHz juostose.

**Kažkas nepavyko.** Parašykite autoriui, nurodydami savo operacinę sistemą, YA-MS versiją ir ką darėte: žr. [Prisidėjimas ir kontaktai](Contributing-and-Contacts-lt).
