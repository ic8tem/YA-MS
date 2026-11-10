[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · **Română** · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Depanare și întrebări frecvente

## Instalare și pornire

### Windows SmartScreen spune „Windows a protejat PC-ul”
Programul nu este semnat cu un certificat comercial. Fă clic pe *Mai multe informații* → *Rulează oricum*. Descarcă-l doar de pe pagina [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: nu poate fi deschis deoarece provine de la un dezvoltator neidentificat
YA-MS nu este semnat de Apple, așa că **Gatekeeper** îl blochează prima dată. În `.dmg`, **clic dreapta pe „Installa YA-MS.command” → Deschide** și confirmă. Scriptul elimină marcajul de carantină „descărcat de pe internet” de pe `~/YA-MS/YA-MS.app` și îl deschide. Dacă macOS tot refuză, deschide *Setări sistem → Confidențialitate și securitate* și apasă *Deschide oricum*.

### macOS: care .dmg?
`-mac-apple-silicon.dmg` pentru procesoarele M1/M2/M3/M4, `-mac-intel.dmg` pentru Mac-urile Intel (meniul Apple → *Despre acest Mac* îți spune care).

### Linux: YA-MS nu apare în meniul aplicațiilor
Rulează `./installa.sh` din dosarul extras (nu din `~/YA-MS`). Unele medii desktop au nevoie de o deconectare/reconectare pentru a afișa intrările noi. Îl poți porni oricând cu `~/YA-MS/YA-MS`.

### Lipsește harta Europei
*Harta Europei nu este disponibilă (este nevoie de rețea la prima pornire).* Harta Natural Earth se descarcă în `data/mappa` la prima pornire. Conectează-te la internet și repornește YA-MS.

## Afișare

### Linux: textul japonez apare ca pătrățele
Sistemului tău îi lipsesc fonturile CJK. Instalează fonturile **Noto CJK** și repornește YA-MS:

| Distribuție | Comandă |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Textul este prea mic sau graficele nu au loc
Folosește cursorul **Font** (100–300 %) și pliază rândurile cu **Comenzi**. Vezi [Setări](Settings-and-Data-Folder-ro#font-și-comenzi).

### Ecranul este prea luminos noaptea
Alege **Noapte** sau **Negru** din lista **Temă**.

## Internet și date radar

### Mesajul „Fără conexiune la internet”
YA-MS îl afișează **o singură dată** când nicio sursă nu poate fi accesată; bara de stare devine roșie. Programul continuă să lucreze cu **ultimele date salvate** și reîncearcă singur la fiecare 5 minute; când rețeaua revine apare *Conexiune restabilită.* Nu este nimic de făcut.

### Avertisment portocaliu în Flux radar: „Nu reușesc să citesc scara verticală a fluxului …”
Radarul Collm își schimbă scara verticală în fiecare zi, iar YA-MS o citește din etichetele graficului. Dacă o etichetă nu poate fi citită, programul folosește scara calibrată 0–1200 meteori/oră și avertizează că sunt **valori de verificat**. De obicei următorul grafic orar este citit corect. Dacă vezi *Formatul graficului s-a schimbat* sau *Axele fluxului nu au fost găsite în poziția așteptată* timp de multe ore, radarul și-a schimbat formatul graficului: te rog [semnalează](Contributing-and-Contacts-ro).

### „Scara graficului altitudinilor s-a schimbat”
Statisticile altitudinilor (moda, media, mediana) rămân valide; doar numărătorile absolute ale histogramei altitudinilor nu.

### „Flux radar: nicio dată”
Apasă **Descarcă acum** în [Flux radar](Radar-Flux-ro) și verifică dacă `data/fonti_radar.csv` are `attivo=1` pentru Collm.

### RMOB: de ce este dezactivată descărcarea automată?
RMOB cere ca **programele automate să nu-i preia fișierele**. Activează *preluare automată la fiecare 5 minute* doar după ce RMOB ți-a dat permisiunea. Între timp folosește **Descarcă RMOB acum** sau **Încarcă fișier RMOB de pe disc...**. Vezi [Implementare experimentală a prognozelor](Experimental-Forecasts-ro#rmob-și-programele-automate).

### RMOB: „Nu am recunoscut formatul fișierului” sau puține ore citite
Folosește fișierul text lunar al observatorului (`NAME_MMYYYYrmob.TXT`) sau un tabel de buletin cu un singur observator. Ajustarea exponentului are nevoie de cel puțin 3 ore în comun cu datele Collm (ieri și azi).

## Calcule

### „Locatorul stației nu este valid” / „Locatorul corespondentului nu este valid”
Locatorii trebuie să aibă 4, 6 sau 8 caractere (de ex. `JN70`, `JN70CN`, `JN70CN12`).

### „Nicio zonă comună a stratului E”
Traseul este mai lung decât dublul bătăii la altitudinea urmelor (circa 2 × 1062 km cu lobul la 0° și urmele la 89,5 km): un singur salt meteor scatter nu îl poate acoperi. Creșterea **Elevației lobului** scurtează și mai mult bătaia.

### Hot A / Hot B sunt gri
Se află deja **în lobul antenei tale** când aceasta este orientată spre DX: nu este nevoie să o rotești. Vezi [Bolta cerească](Sky-View-ro#avertismente).

### Eficiența diferă de MCG_MS sau MS-Soft
YA-MS folosește traseul real și propriul model; scara lui OH5IY și a MCG_MS nu este documentată în detaliu. Compară orele și tendințele mai degrabă decât procentele absolute și vezi [modelul](Efficiency-Calculation-ro#modelul).

### Trecerea fasciculului GRAVES pare decalată
Secvența fasciculului se calculează din ceasul PC-ului: sincronizează-l cu un server NTP. Stația de comandă GRAVES deplasează uneori și ea secvența cu câțiva pași; detaliul este o prognoză de confirmat prin ascultare.

## Alte întrebări

**Este YA-MS gratuit?** Da, este un program gratuit pentru radioamatori.

**Îmi comandă rotorul sau stația?** Nu. YA-MS este un instrument de prognoză și planificare; pentru QSO folosește programul tău de moduri digitale (de ex. MSHV, WSJT-X).

**Funcționează peste 432 MHz?** Lista benzilor se oprește la 432 MHz (28, 50, 70, 144, 222, 432). Prognoza experimentală acceptă orice frecvență între 28 și 1300 MHz, dar regulile SM6FHZ pe care le folosește provin din experiența pe 144 și 432 MHz.

**Ceva nu a mers bine.** Scrie-i autorului indicând sistemul de operare, versiunea YA-MS și ce ai făcut: vezi [Contribuții și contacte](Contributing-and-Contacts-ro).
