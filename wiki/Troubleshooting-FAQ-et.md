[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · **Eesti** · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Tõrkeotsing ja KKK

## Paigaldamine ja käivitamine

### Windows SmartScreen ütleb "Windows protected your PC"
Programm ei ole allkirjastatud kommertssertifikaadiga. Klõpsa *More info* → *Run anyway*. Laadi programmi alla ainult lehelt [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: ei saa avada, sest arendaja on tuvastamata
YA-MS ei ole Apple'i poolt allkirjastatud, seega blokeerib **Gatekeeper** selle esimesel korral. Tee `.dmg`-s **paremklõps failil "Installa YA-MS.command" → Open** ja kinnita. Skript eemaldab faililt `~/YA-MS/YA-MS.app` karantiinimärgi "Internetist alla laaditud" ja avab programmi. Kui macOS ikka keeldub, ava *System Settings → Privacy & Security* ja vajuta *Open Anyway*.

### macOS: milline .dmg?
`-mac-apple-silicon.dmg` protsessoritele M1/M2/M3/M4, `-mac-intel.dmg` Inteli Macidele (Apple'i menüü → *About This Mac* ütleb, milline sul on).

### Linux: YA-MS-i pole rakenduste menüüs
Käivita `./installa.sh` lahtipakitud kaustast (mitte kaustast `~/YA-MS`). Mõned töölauad vajavad uute kirjete kuvamiseks välja- ja sisselogimist. Programmi saab alati käivitada käsuga `~/YA-MS/YA-MS`.

### Euroopa kaart puudub
*Euroopa kaart pole saadaval (esimesel käivitusel on vaja võrku).* Natural Earthi kaart laaditakse esimesel käivitusel kausta `data/mappa`. Ühenda internetiga ja käivita YA-MS uuesti.

## Kuvamine

### Linux: jaapani tekst kuvatakse kastikestena
Sinu süsteemis puuduvad CJK-fondid (hiina, jaapani, korea). Paigalda **Noto CJK** fondid ja käivita YA-MS uuesti. Sama juhtub araabia, heebrea, urdu, hindi ja bengali keelega: Debianis, Ubuntus ja Raspberry Pi OS-is paigalda ka `fonts-noto-core`.

| Distributsioon | Käsk |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Tekst on liiga väike või graafikutel pole ruumi
Kasuta liugurit **Font** (100–300 %) ja peida read nupuga **Juhtnupud**. Vt [Seaded](Settings-and-Data-Folder-et#font-ja-juhtnupud).

### Ekraan on öösel liiga ere
Vali loendist **Teema** **Öö** või **Must**.

## Internet ja radariandmed

### Teade "Internetiühendus puudub"
YA-MS näitab seda **üks kord**, kui ükski allikas pole kättesaadav; olekuriba muutub punaseks. Programm töötab edasi **viimati salvestatud andmetega** ja proovib ise uuesti iga 5 minuti järel; kui võrk taastub, ilmub *Ühendus taastatud.* Midagi pole vaja teha.

### Oranž hoiatus sakil Radari voog: "Voo vertikaalskaalat ei õnnestu lugeda …"
Collmi radar muudab oma vertikaalskaalat iga päev ja YA-MS loeb selle graafiku siltidelt. Kui silti ei õnnestu lugeda, kasutab programm kalibreeritud skaalat 0–1200 meteoori tunnis ja hoiatab, et **väärtusi tuleb kontrollida**. Tavaliselt loetakse järgmine tunnigraafik õigesti. Kui näed paljude tundide jooksul teadet *Graafiku vorming muutus* või *Voo telgi ei leitud oodatud kohast*, on radar muutnud oma graafiku vormingut: palun [teata sellest](Contributing-and-Contacts-et).

### "Kõrguste graafiku skaala on muutunud"
Kõrguste statistika (mood, keskmine, mediaan) jääb kehtima; ainult kõrguste histogrammi absoluutsed loendused mitte.

### "Radari voog: andmed puuduvad"
Vajuta sakil [Radari voog](Radar-Flux-et) nuppu **Laadi kohe alla** ja kontrolli, et failis `data/fonti_radar.csv` on Collmi jaoks `attivo=1`.

### RMOB: miks on automaatne allalaadimine väljas?
RMOB palub, et **automaatprogrammid selle faile ei laadiks**. Lülita *automaatne allalaadimine iga 5 minuti järel* sisse ainult siis, kui RMOB on sulle loa andnud. Seni kasuta nuppe **Laadi RMOB kohe alla** või **Laadi RMOB-fail kettalt...**. Vt [Eksperimentaalsed prognoosid](Experimental-Forecasts-et#rmob-ja-automaatprogrammid).

### RMOB: "Faili vormingut ei tuvastatud" või loeti vähe tunde
Kasuta vaatleja igakuist tekstifaili (`NAME_MMYYYYrmob.TXT`) või ühe vaatlejaga bülletääni tabelit. Astendaja sobitamiseks on vaja vähemalt 3 tundi, mis ühtivad Collmi andmetega (eile ja täna).

## Arvutused

### "Jaama lokaator on vigane" / "Korrespondendi lokaator on vigane"
Lokaatoris peab olema 4, 6 või 8 märki (nt `JN70`, `JN70CN`, `JN70CN12`).

### "E-kihi ühisala puudub"
Trass on pikem kui kahekordne ulatus jälgede kõrgusel (umbes 2 × 1062 km, kui peaharu on 0° ja jäljed 89,5 km kõrgusel): üks meteor scatteri hüpe ei suuda seda katta. **Peaharu elevatsiooni** tõstmine lühendab ulatust veelgi.

### Hot A / Hot B on hallid
Need on DX-ile suunatud antenni korral juba **sinu antenni peaharu sees**: pole vaja keerata. Vt [Taevavõlv](Sky-View-et#hoiatused).

### Efektiivsus erineb MCG_MS-ist või MS-Softist
YA-MS kasutab tegelikku trassi ja oma mudelit; OH5IY ja MCG_MS-i skaala pole üksikasjalikult dokumenteeritud. Võrdle tunde ja suundumusi, mitte absoluutseid protsente, ning vaata [mudelit](Efficiency-Calculation-et#mudel).

### GRAVESi kiire möödumine tundub nihkes olevat
Kiire järjestus arvutatakse arvuti kella järgi: sünkrooni see NTP-serveriga. Ka GRAVESi juhtimisjaam nihutab järjestust aeg-ajalt mõne sammu võrra; detail on prognoos, mida tuleb kuulamisega kinnitada.

## Muud küsimused

**Kas YA-MS on tasuta?** Jah, see on tasuta programm raadioamatööridele.

**Kas see juhib mu pöörlit või raadiojaama?** Ei. YA-MS on prognoosimise ja planeerimise tööriist; QSO jaoks kasuta oma digimoodusi toetavat programmi (nt MSHV, WSJT-X).

**Kas see töötab üle 432 MHz?** Sagedusalade loetelu lõpeb 432 MHz-ga (28, 50, 70, 144, 222, 432). Eksperimentaalne prognoos aktsepteerib mis tahes sagedust 28 kuni 1300 MHz, kuid selles kasutatavad SM6FHZ reeglid põhinevad kogemusel 144 ja 432 MHz-l.

**Midagi läks valesti.** Kirjuta autorile, märkides oma operatsioonisüsteemi, YA-MS-i versiooni ja selle, mida tegid: vt [Kaastöö ja kontaktid](Contributing-and-Contacts-et).
