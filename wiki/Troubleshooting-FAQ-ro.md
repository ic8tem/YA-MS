[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · **Română** · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# Rezolvarea problemelor și întrebări frecvente

## Instalare și pornire

### Windows SmartScreen spune „Windows v-a protejat PC-ul”
Programul nu este semnat cu un certificat comercial. Faceți clic pe *Mai multe informații* → *Rulați oricum*. Descărcați-l doar de pe pagina [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: nu poate fi deschis deoarece provine de la un dezvoltator neidentificat
YA-MS nu este semnat de Apple, așa că **Gatekeeper** îl blochează prima dată. În `.dmg`, **clic dreapta pe „Installa YA-MS.command” → Deschide** și confirmați. Scriptul elimină marcajul de carantină „descărcat de pe internet” de pe `~/YA-MS/YA-MS.app` și îl deschide. Dacă macOS refuză în continuare, deschideți *Setări sistem → Confidențialitate și securitate* și apăsați *Deschide oricum*.

### macOS: care .dmg?
`-mac-apple-silicon.dmg` pentru procesoarele M1/M2/M3/M4, `-mac-intel.dmg` pentru Mac-urile Intel (meniul Apple → *Despre acest Mac* vă spune care).

### Linux: YA-MS nu apare în meniul de aplicații
Rulați `./installa.sh` din dosarul extras (nu din `~/YA-MS`). Unele medii desktop au nevoie de o deconectare/reconectare pentru a afișa intrările noi. Îl puteți porni oricând cu `~/YA-MS/YA-MS`.

### Lipsește harta Europei
*Harta Europei nu este disponibilă (este nevoie de rețea la prima pornire).* Harta Natural Earth se descarcă în `data/mappa` la prima pornire. Conectați-vă la internet și reporniți YA-MS.

## Afișare

### Linux: textul japonez apare ca pătrățele
Sistemului dumneavoastră îi lipsesc fonturile CJK (chineză, japoneză, coreeană). Instalați fonturile **Noto CJK** și reporniți YA-MS. La fel se întâmplă cu araba, ebraica, urdu, hindi și bengali: pe Debian, Ubuntu și Raspberry Pi OS instalați și `fonts-noto-core`.

| Distribuție | Comandă |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Textul este prea mic sau graficele nu au loc
Folosiți cursorul **Font** (100–300 %) și pliați rândurile cu **Comenzi**. Vedeți [Setări](Settings-and-Data-Folder-ro#font-și-comenzi).

### Ecranul este prea luminos noaptea
Alegeți **Noapte** sau **Negru** în lista **Temă**.

## Internet și date radar

### Mesajul „Nicio conexiune la internet”
YA-MS îl afișează **o singură dată** când nicio sursă nu poate fi accesată; bara de stare devine roșie. Programul continuă să funcționeze cu **ultimele date salvate** și reîncearcă singur la fiecare 5 minute; *Conexiune restabilită.* apare când rețeaua revine. Nu trebuie făcut nimic.

### Avertisment portocaliu în Flux radar: „Nu se poate citi scala verticală a fluxului …”
Radarul din Collm își schimbă scala verticală în fiecare zi, iar YA-MS o citește din etichetele graficului. Dacă o etichetă nu poate fi citită, programul folosește scala calibrată 0–1200 meteori/oră și avertizează că **valorile trebuie verificate**. De obicei, următorul grafic orar este citit corect. Dacă vedeți *Formatul graficului s-a schimbat* sau *Axele fluxului nu au fost găsite în poziția așteptată* timp de multe ore, radarul și-a schimbat formatul graficului: vă rugăm să [raportați](Contributing-and-Contacts-ro).

### „Scala graficului înălțimilor s-a schimbat”
Statisticile înălțimii (moda, media, mediana) rămân valabile; doar numărătorile absolute ale histogramei înălțimilor nu mai sunt.

### „Flux radar: nicio dată”
Apăsați **Descarcă acum** în [Flux radar](Radar-Flux-ro) și verificați că `data/fonti_radar.csv` are `attivo=1` pentru Collm.

### RMOB: de ce este dezactivată descărcarea automată?
RMOB cere ca **programele automate să nu-i descarce fișierele**. Activați *descărcare automată la fiecare 5 minute* doar după ce RMOB v-a dat permisiunea. Între timp, folosiți **Descarcă RMOB acum** sau **Încarcă fișier RMOB de pe disc...**. Vedeți [Previziuni experimentale](Experimental-Forecasts-ro#rmob-și-programele-automate).

### RMOB: „Format de fișier nerecunoscut” sau puține ore citite
Folosiți fișierul text lunar al observatorului (`NAME_MMYYYYrmob.TXT`) sau un tabel de buletin cu un singur observator. Ajustarea exponentului are nevoie de cel puțin 3 ore comune cu datele Collm (ieri și astăzi).

## Calcule

### „Locatorul stației nu este valid” / „Locatorul stației DX nu este valid”
Locatorii trebuie să aibă 4, 6 sau 8 caractere (de ex. `JN70`, `JN70CN`, `JN70CN12`).

### „Nicio zonă comună a stratului E”
Traseul este mai lung decât dublul razei la înălțimea urmei (aproximativ 2 × 1062 km cu lobul la 0° și urme la 89,5 km): un singur salt meteor-scatter nu îl poate acoperi. Ridicarea **Elevației lobului** scurtează și mai mult raza.

### Hot A / Hot B sunt gri
Se află deja **în interiorul lobului antenei dumneavoastră** când aceasta este îndreptată spre DX: nu este nevoie s-o rotiți. Vedeți [Bolta cerească](Sky-View-ro#avertismente).

### Eficiența diferă de cea din MCG_MS sau MS-Soft
YA-MS folosește traseul real și propriul model; scala lui OH5IY și a MCG_MS nu este documentată în detaliu. Comparați orele și tendințele mai degrabă decât procentele absolute și consultați [modelul](Efficiency-Calculation-ro#modelul).

### Trecerea fasciculului GRAVES pare decalată
Secvența fasciculului se calculează din ceasul PC-ului: sincronizați-l cu un server NTP. Stația de comandă GRAVES decalează și ea uneori secvența cu câțiva pași; detaliul este o predicție care trebuie confirmată prin ascultare.

## Alte întrebări

**Este YA-MS gratuit?** Da, este un program gratuit pentru radioamatori.

**Îmi controlează rotorul sau stația radio?** Nu. YA-MS este un instrument de previziune și planificare; folosiți programul dumneavoastră de moduri digitale (de ex. MSHV, WSJT-X) pentru QSO.

**Funcționează peste 432 MHz?** Lista benzilor se oprește la 432 MHz (28, 50, 70, 144, 222, 432). Previziunea experimentală acceptă orice frecvență între 28 și 1300 MHz, dar regulile SM6FHZ pe care le folosește provin din experiența pe 144 și 432 MHz.

**Ceva nu a mers bine.** Scrieți-i autorului cu sistemul de operare, versiunea YA-MS și ce ați făcut: vedeți [Contribuții și contacte](Contributing-and-Contacts-ro).
