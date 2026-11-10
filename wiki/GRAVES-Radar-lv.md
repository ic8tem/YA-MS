[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · **Latviešu** · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [ไทย](GRAVES-Radar-th) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# GRAVES radars

*Cilne: Tiešsaiste un reāllaika dati › GRAVES radars.*

[![GRAVES radars](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Kas ir GRAVES

**GRAVES** ir Francijas radars, kas raida **CW 143,050 MHz** no **Broye-lès-Pesmes** (47,348° N 5,515° E, lokators **JN27SI**, ap 200 m v.j.l.; Wikipedia). Meteoru sliedes zonā, ko redz gan GRAVES, gan tu, atstaro tā signālu pie tevis ar **forward scatter**: tu dzirdi īsus *pingus* tuvu nesējam. Tā **RMOB** novērotāji 143,050 MHz skaita meteorus stundu pa stundai, un tas ir bezmaksas, vienmēr ieslēgts testa signāls tavai 2 m meteor scatter stacijai.

Cilne aplūko **GRAVES → tu** kā atsevišķu meteor scatter trasi: ar tām pašām funkcijām kā galvenajai trasei (tas pats sliežu augstums, ziedlapiņas elevācija un hot spot attālums) tā aprēķina plūsmu efektivitāti, ieteicamo Hot un PREV zonas, pēc tam pārbauda, vai šī zona ir **GRAVES kūlī** un **kad** kūlis to apgaismo.

## Augšējā josla

| Vadīkla | Ko tā dara |
|---|---|
| **Tagad** | Atgriež aprēķinu reālajā laikā: šodienas datums un stundu slīdnis uz nulles (cilne seko *Aprēķina datums* un *Stundas*). |
| **Iestatīt GRAVES kā DX** | Korespondents kļūst par GRAVES (JN27SI, augstums 200 m), un galvenā trase tiek pārrēķināta: visas pārējās cilnes tad rāda GRAVES trasi. |
| **Kūļa secība** | *0,8 s solī · cikls 4,8 s (PE1ITR 2021)* (noklusējumā) vai *3,2 s solī · cikls 19,2 s (PE1ITR 2007)*. |

## Četras kartītes

| Kartīte | Saturs |
|---|---|
| **LIETDERĪGĀ ZONA GRAVES KŪLĪ** | *Jā · sektors X* ar ieteicamā hot spot azimutu un elevāciju, kā to redz GRAVES, un soli (1–6); vai *Nē: ārpus sektoriem* / *Nē: zem GRAVES horizonta* / *Nē: virs kūļa (ap 25°)* |
| **TRASES GRAVES → TEVI EFEKTIVITĀTE TAGAD** | Trases indekss Σ ZHR × efektivitāte, labākā plūsma, dominējošā puse A/B un *gaidāmās atbalsis ≈ …/stundā* (eksperimentāli, sk. zemāk) |
| **TRASE** | Attālums līdz GRAVES; antena uz ieteicamo Hot (azimuts un elevācija); GRAVES tiešais azimuts |
| **NĀKAMĀ KŪĻA PĀREJA PĀR ZONU** | *tagad · atlikušas … s* vai *pēc … s*, solis (piem. *B4*), nākamie trīs laiki (sekundes minūtes ietvaros) un notverto sliežu daļa |

Ja tajā brīdī neviena plūsma nav lietderīga, programma rāda **kūlim piemērotāko** hot spot (sektoru iekšpusē, vistuvāk dienvidiem) un to arī norāda.

## Debess, kā to redz GRAVES

Saskaņā ar PE1ITR un Bolidozor wiki **četri fāzēti antenu režģi** pārklāj dienvidu debesis no **90° līdz 270°** azimutā četros **45° sektoros**:

| Sektors | Azimuts no GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Katrs sektors ir sadalīts **6 soļos pa 7,5°**, numurētos no 1 līdz 6 no mazākā azimuta, kas tiek apgaismoti viens pēc otra **vienlaikus visos četros sektoros**. Kūlis elevācijā ir ap **25° plats**: sliežu augstumā tas pārklāj krāsaino gredzenu starp abiem raustītajiem apļiem (*kūļa horizonts*). Zīmējumā: oranži/rozā punkti = trases GRAVES → tu PREV zonas, zaļa līnija = tavas stacijas virziens, sarkana līnija = no tavas stacijas uz ieteicamo hot spot; tagad apgaismotais solis ir izcelts.

## Hronoloģiskā rekonstrukcija

*HRONOLOĢISKA REKONSTRUKCIJA · datums UTC* (tā pati diena kā 24 h tabulai): katrai stundai trases GRAVES → tu efektivitāte, visizdevīgākā plūsma un lietderīgais logs (*hh:00 → hh:00 UTC · n h*), ar maksimumu (*maks. Σ … plkst. hh:30*) un sarkanu atzīmi *tagad*. Zemāk – **nākamo sekunžu detaļas**: sektora seši soļi, solis, kas apgaismo lietderīgo zonu, un *iespējama atbalss (+0,3 s sliedes)*.

### Kūļa laiki

Secība ir piesaistīta **UTC** (PE1ITR): tagad apgaismotais solis tiek aprēķināts no sekundēm kopš 00:00 UTC pēc cikla moduļa (86 400 s ir gan 4,8 s, gan 19,2 s daudzkārtnis). Vadības stacija dažkārt nobīda secību par dažiem soļiem, tāpēc detaļas ir **prognoze, kas jāapstiprina klausoties**. Dzeltenā etiķete **datora pulkstenis sinhronizēts** atgādina: sinhronizē datoru ar NTP serveri (kļūda ne vairāk par dažām sekundes desmitdaļām).

### Uztveršanas koeficients

Sliedi dzird tikai tad, ja kūlis to apgaismo, kamēr tā pastāv:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s ir tipisks zema blīvuma sliedes ilgums 143 MHz – fiksēta vērtība, *programmas izvēle* (SM6FHZ λ² likums pārrēķina ilgumus starp joslām, bet nedod sākuma vērtību).

### Gaidāmās atbalsis (eksperimentāli)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

[Eksperimentālo prognožu](Experimental-Forecasts-lv) prognoze (kurā jau ir stacijas koeficients K) tiek pārrēķināta no tās frekvences f_fc uz 143,050 MHz ar SM6FHZ likumu (tas pats kāpinātājs k), koriģēta ar abu trašu plūsmu indeksu attiecību (konstante 10 attēlo sporādisko fonu, tāpat kā prognozē) un reizināta ar uztveršanas koeficientu. Tikai orientējoši: salīdzini ar RMOB novērotājiem.

## Kā dzirdēt GRAVES pingus

| Solis | Ko darīt |
|---|---|
| Uztvērējs | **USB 143,049 MHz** (tonis ap 1 kHz) vai 143,050 MHz, **lēns vai izslēgts AGC**, audio josla **vismaz 2,4 kHz** |
| Antena | Uz trases GRAVES → tu **ieteicamo hot spot** (kartīte *TRASE*), ar **zemu elevāciju** |
| Ūdenskritums | Pingi ir **īsas līnijas tuvu nesējam**; garas (augsta blīvuma) sliedes ir platākas un rāda Doplera efektu |
| Skaitīšana | RMOB izmanto GRAVES meteoru skaitīšanai pa stundām: **salīdzini savus pingus ar novērotājiem 143,050 MHz** ([Eksperimentālas prognozes](Experimental-Forecasts-lv#salīdzinājums-ar-rmob)) |

## Avoti

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) un *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – antenu režģi, sektori un kūļa laiki
3. **Wikipedia**, "GRAVES (system)" – raidītājs Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – novērotāji uz 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** (IC8TEM) – cilne GRAVES Radar (skice, no kuras šī cilne atvasināta)
