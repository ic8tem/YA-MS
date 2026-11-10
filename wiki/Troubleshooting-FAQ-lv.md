[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · **Latviešu** · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Problēmu risināšana un BUJ

## Instalēšana un palaišana

### Windows SmartScreen saka "Windows aizsargāja jūsu datoru"
Programma nav parakstīta ar komerciālu sertifikātu. Noklikšķini *Papildinformācija* (More info) → *Tik un tā palaist* (Run anyway). Lejupielādē to tikai no lapas [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: nevar atvērt, jo izstrādātājs nav identificēts
YA-MS nav parakstījis Apple, tāpēc **Gatekeeper** pirmajā reizē to bloķē. Failā `.dmg` **labais klikšķis uz "Installa YA-MS.command" → Open** un apstiprini. Skripts noņem no `~/YA-MS/YA-MS.app` karantīnas atzīmi "lejupielādēts no interneta" un atver to. Ja macOS joprojām atsakās, atver *System Settings → Privacy & Security* (Sistēmas iestatījumi → Privātums un drošība) un nospied *Open Anyway* (Tomēr atvērt).

### macOS: kuru .dmg?
`-mac-apple-silicon.dmg` procesoriem M1/M2/M3/M4, `-mac-intel.dmg` Intel Mac datoriem (Apple izvēlne → *About This Mac* parāda, kurš tev ir).

### Linux: YA-MS nav lietotņu izvēlnē
Palaid `./installa.sh` no atarhivētās mapes (nevis no `~/YA-MS`). Dažām darbvirsmām jāiziet un jāpiesakās no jauna, lai jaunie ieraksti parādītos. Programmu vienmēr var palaist ar `~/YA-MS/YA-MS`.

### Trūkst Eiropas kartes
*Eiropas karte nav pieejama (pirmajā palaišanā vajadzīgs tīkls).* Natural Earth karte tiek lejupielādēta mapē `data/mappa` pirmajā palaišanā. Pieslēdzies internetam un restartē YA-MS.

## Attēlojums

### Linux: japāņu teksts redzams kā kvadrātiņi
Tavā sistēmā trūkst CJK fontu. Instalē **Noto CJK** fontus un restartē YA-MS:

| Distribūcija | Komanda |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Teksts ir pārāk mazs vai grafikiem nav vietas
Izmanto slīdni **Fonts** (100–300 %) un sakļauj rindas ar **Vadība**. Sk. [Iestatījumi](Settings-and-Data-Folder-lv#fonts-un-vadība).

### Ekrāns naktī ir pārāk spilgts
Sarakstā **Tēma** izvēlies **Nakts** vai **Melns**.

## Internets un radaru dati

### Ziņojums "Nav interneta savienojuma"
YA-MS to parāda **vienu reizi**, kad neviens avots nav sasniedzams; statusa josla kļūst sarkana. Programma turpina strādāt ar **pēdējiem saglabātajiem datiem** un pati mēģina vēlreiz ik pēc 5 minūtēm; kad tīkls atgriežas, parādās *Savienojums atjaunots.* Nekas nav jādara.

### Oranžs brīdinājums cilnē Radara meteoru skaits: "Nevar nolasīt meteoru skaita vertikālo skalu …"
Collm radars katru dienu maina vertikālo skalu, un YA-MS to nolasa no grafika etiķetēm. Ja etiķeti nevar nolasīt, programma izmanto kalibrēto skalu 0–1200 meteori/stundā un brīdina, ka **vērtības jāpārbauda**. Parasti nākamās stundas grafiks tiek nolasīts pareizi. Ja daudzas stundas redzi *Grafika formāts mainījies* vai *Meteoru skaita grafika asis nav atrastas gaidītajā vietā*, radars ir mainījis grafika formātu: lūdzu, [ziņo par to](Contributing-and-Contacts-lv).

### "Augstumu grafika skala ir mainījusies"
Augstumu statistika (moda, vidējais, mediāna) paliek derīga; neder tikai augstumu histogrammas absolūtie skaiti.

### "Radara meteoru skaits: nav datu"
Nospied **Lejupielādēt tagad** cilnē [Radara meteoru skaits](Radar-Flux-lv) un pārbaudi, vai failā `data/fonti_radar.csv` Collm ir `attivo=1`.

### RMOB: kāpēc automātiskā lejupielāde ir izslēgta?
RMOB lūdz **automātiskās programmas neielādēt tā failus**. Ieslēdz *automātiska lejupielāde ik pēc 5 minūtēm* tikai pēc tam, kad RMOB tev to ir atļāvis. Pa to laiku izmanto **Lejupielādēt RMOB tagad** vai **Ielādēt RMOB failu no diska...**. Sk. [Eksperimentālas prognozes](Experimental-Forecasts-lv#rmob-un-automātiskās-programmas).

### RMOB: "Faila formāts nav atpazīts" vai nolasītas maz stundas
Izmanto novērotāja mēneša teksta failu (`NAME_MMYYYYrmob.TXT`) vai biļetena tabulu ar vienu novērotāju. Kāpinātāja pielāgošanai vajadzīgas vismaz 3 stundas, kas kopējas ar Collm datiem (vakar un šodien).

## Aprēķini

### "Nederīgs stacijas lokators" / "Nederīgs korespondenta lokators"
Lokatoros jābūt 4, 6 vai 8 rakstzīmēm (piem. `JN70`, `JN70CN`, `JN70CN12`).

### "Nav kopējas E slāņa zonas"
Trase ir garāka par divkāršu sniedzamību sliežu augstumā (ap 2 × 1062 km ar ziedlapiņu 0° un sliedēm 89,5 km): ar vienu meteor scatter lēcienu to nevar pārklāt. Paaugstinot **Ziedlapiņas elevāciju**, sniedzamība samazinās vēl vairāk.

### Hot A / Hot B ir pelēki
Tie jau ir **tavas antenas ziedlapiņā**, kad tā vērsta uz DX: nav jāgroza. Sk. [Debess velve](Sky-View-lv#brīdinājumi).

### Efektivitāte atšķiras no MCG_MS vai MS-Soft
YA-MS izmanto reālo trasi un savu modeli; OH5IY un MCG_MS skala nav sīki dokumentēta. Salīdzini stundas un tendences, nevis absolūtos procentus, un sk. [modeli](Efficiency-Calculation-lv#modelis).

### GRAVES kūļa pāreja šķiet nobīdīta
Kūļa secība tiek aprēķināta no datora pulksteņa: sinhronizē to ar NTP serveri. GRAVES vadības stacija arī dažkārt nobīda secību par dažiem soļiem; detaļas ir prognoze, kas jāapstiprina klausoties.

## Citi jautājumi

**Vai YA-MS ir bezmaksas?** Jā, tā ir bezmaksas programma radioamatieriem.

**Vai tā vada manu rotatoru vai raidītāju?** Nē. YA-MS ir prognozēšanas un plānošanas rīks; QSO veikšanai izmanto savu digitālo modu programmu (piem. MSHV, WSJT-X).

**Vai tā darbojas virs 432 MHz?** Joslu saraksts beidzas pie 432 MHz (28, 50, 70, 144, 222, 432). Eksperimentālā prognoze pieņem jebkuru frekvenci no 28 līdz 1300 MHz, taču tās izmantotie SM6FHZ likumi nāk no pieredzes 144 un 432 MHz.

**Kaut kas nogāja greizi.** Raksti autoram, norādot operētājsistēmu, YA-MS versiju un ko darīji: sk. [Līdzdalība un kontakti](Contributing-and-Contacts-lv).
