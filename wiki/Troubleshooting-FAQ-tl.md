[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · **Tagalog** · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Pag-troubleshoot at FAQ

## Pag-install at pagsisimula

### Sinasabi ng Windows SmartScreen na "Windows protected your PC"
Hindi naka-sign ang programa ng komersiyal na sertipiko. I-click ang *More info* → *Run anyway*. I-download lamang ito mula sa pahinang [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: hindi mabuksan dahil galing ito sa hindi kilalang developer
Hindi naka-sign ng Apple ang YA-MS, kaya hinaharangan ito ng **Gatekeeper** sa unang pagkakataon. Sa `.dmg`, **i-right-click ang "Installa YA-MS.command" → Open** at kumpirmahin. Inaalis ng script ang quarantine flag na "na-download mula sa internet" sa `~/YA-MS/YA-MS.app` at binubuksan ito. Kung tumatanggi pa rin ang macOS, buksan ang *System Settings → Privacy & Security* at pindutin ang *Open Anyway*.

### macOS: aling .dmg?
`-mac-apple-silicon.dmg` para sa mga processor na M1/M2/M3/M4, `-mac-intel.dmg` para sa mga Mac na Intel (sinasabi ito ng Apple menu → *About This Mac*).

### Linux: wala ang YA-MS sa menu ng mga application
Patakbuhin ang `./installa.sh` mula sa na-extract na folder (hindi mula sa `~/YA-MS`). May ilang desktop na nangangailangan ng log-out/log-in para lumabas ang mga bagong entry. Palagi mo itong masisimulan gamit ang `~/YA-MS/YA-MS`.

### Nawawala ang mapa ng Europa
*Hindi available ang mapa ng Europa (kailangan ng network sa unang pagsisimula).* Dina-download ang mapa ng Natural Earth sa `data/mappa` sa unang pagsisimula. Kumonekta sa internet at i-restart ang YA-MS.

## Display

### Linux: lumalabas na mga kahon ang tekstong Hapones
Walang CJK na font (Tsino, Hapones, Koreano) ang iyong sistema. I-install ang mga font na **Noto CJK** at i-restart ang YA-MS. Ganoon din sa Arabe, Hebreo, Urdu, Hindi at Bengali: sa Debian, Ubuntu at Raspberry Pi OS, i-install din ang `fonts-noto-core`.

| Distribusyon | Command |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Masyadong maliit ang teksto, o walang puwang ang mga graph
Gamitin ang slider na **Font** (85–140 %) at itiklop ang mga hanay gamit ang **Mga kontrol**. Tingnan ang [Mga setting](Settings-and-Data-Folder-tl#font-at-mga-kontrol).

### Masyadong maliwanag ang screen sa gabi
Piliin ang **Gabi** o **Itim** sa listahang **Tema**.

## Internet at datos ng radar

### Mensaheng "Walang koneksiyon sa internet"
Ipinapakita ito ng YA-MS **nang isang beses** kapag walang maabot na sanggunian; nagiging pula ang status bar. Patuloy na gumagana ang programa gamit ang **huling na-save na datos** at kusang sumusubok muli bawat 5 minuto; lumalabas ang *Naibalik ang koneksiyon.* kapag bumalik na ang network. Walang kailangang gawin.

### Kahel na babala sa Flux ng radar: "Hindi mabasa ang patayong iskala ng flux …"
Binabago ng radar ng Collm ang patayong iskala nito araw-araw at binabasa ito ng YA-MS mula sa mga label ng graph. Kung hindi mabasa ang isang label, ginagamit ng programa ang kalibradong iskala na 0–1200 meteor/oras at nagbababalang **kailangang suriin ang mga halaga**. Karaniwang nababasa nang tama ang susunod na graph bawat oras. Kung makikita mo ang *Nagbago ang format ng graph* o *Hindi nakita ang mga axis ng flux sa inaasahang posisyon* sa loob ng maraming oras, binago ng radar ang format ng graph nito: pakiulat ito ([mag-ulat](Contributing-and-Contacts-tl)).

### "Nagbago ang iskala ng graph ng taas"
Balido pa rin ang estadistika ng taas (moda, mean, median); ang absolutong bilang lamang ng histogram ng taas ang hindi na.

### "Flux ng radar: walang datos"
Pindutin ang **I-download ngayon** sa [Flux ng radar](Radar-Flux-tl), at tiyaking may `attivo=1` para sa Collm ang `data/fonti_radar.csv`.

### RMOB: bakit naka-off ang awtomatikong pag-download?
Hinihiling ng RMOB na **huwag kunin ng mga awtomatikong programa ang mga file nito**. I-enable ang *awtomatikong pag-download bawat 5 minuto* pagkatapos lamang mabigyan ka ng pahintulot ng RMOB. Samantala, gamitin ang **I-download ang RMOB ngayon** o **Ikarga ang RMOB file mula sa disk...**. Tingnan ang [Eksperimental na pagtataya](Experimental-Forecasts-tl#ang-rmob-at-mga-awtomatikong-programa).

### RMOB: "Hindi nakilala ang format ng file" o kaunting oras ang nabasa
Gamitin ang buwanang text file ng observer (`NAME_MMYYYYrmob.TXT`) o isang talahanayan ng bulletin na may iisang observer. Kailangan ng pag-aangkop ng exponent ng hindi bababa sa 3 oras na kapareho ng datos ng Collm (kahapon at ngayon).

## Mga kalkulasyon

### "Hindi balidong locator ng istasyon" / "Hindi balidong locator ng DX station"
Dapat may 4, 6 o 8 character ang mga locator (hal. `JN70`, `JN70CN`, `JN70CN12`).

### "Walang karaniwang sona ng E layer"
Mas mahaba ang landas kaysa dalawang ulit ng abot sa taas ng bakas (mga 2 × 1062 km kapag ang lobe ay nasa 0° at ang mga bakas ay nasa 89.5 km): hindi ito masasaklaw ng iisang hop ng meteor scatter. Lalo pang pinaiikli ng pagtaas ng **Elebasyon ng lobe** ang abot.

### Kulay abo ang Hot A / Hot B
**Nasa loob na sila ng lobe ng iyong antenna** kapag nakatutok sa DX: hindi na kailangang ipihit. Tingnan ang [Kalangitan](Sky-View-tl#mga-babala).

### Iba ang episyensya kaysa sa MCG_MS o MS-Soft
Ginagamit ng YA-MS ang totoong landas at ang sarili nitong modelo; hindi nakadokumento nang detalyado ang iskala ng OH5IY at MCG_MS. Paghambingin ang mga oras at trend sa halip na ang absolutong porsiyento, at tingnan ang [modelo](Efficiency-Calculation-tl#ang-modelo).

### Parang nakausog ang pagdaan ng beam ng GRAVES
Kinakalkula ang sequence ng beam mula sa orasan ng PC: i-synchronize ito sa isang NTP server. Paminsan-minsan ding inililipat ng command station ng GRAVES ang sequence nang ilang hakbang; ang detalye ay isang prediksiyon na dapat kumpirmahin sa pakikinig.

## Iba pang tanong

**Libre ba ang YA-MS?** Oo, isa itong libreng programa para sa mga radio amateur.

**Kinokontrol ba nito ang aking rotator o radyo?** Hindi. Ang YA-MS ay kasangkapan sa pagtataya at pagpaplano; gamitin ang iyong programa para sa digital mode (hal. MSHV, WSJT-X) para sa QSO.

**Gumagana ba ito sa itaas ng 432 MHz?** Hanggang 432 MHz lamang ang listahan ng banda (28, 50, 70, 144, 222, 432). Tumatanggap ang eksperimental na pagtataya ng anumang frequency mula 28 hanggang 1300 MHz, pero ang mga tuntunin ni SM6FHZ na ginagamit nito ay mula sa karanasan sa 144 at 432 MHz.

**May nagkaproblema.** Sumulat sa may-akda, kasama ang iyong operating system, ang bersyon ng YA-MS at ang ginawa mo: tingnan ang [Pag-ambag at pakikipag-ugnayan](Contributing-and-Contacts-tl).
