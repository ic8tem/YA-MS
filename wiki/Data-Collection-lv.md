[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · **Latviešu** · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Datu vākšana

*Cilne: Tiešsaiste un reāllaika dati › Datu vākšana.*

[![Datu vākšana](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Četri avoti

Cilne vāc **meteor scatter spotus** no trim telnet plūsmām un no PSKReporter MQTT plūsmas, katru savā apakšcilnē:

| Apakšcilne | Noklusējums | Piezīmes |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Klasteris pēc izvēles. ON0DXK VHF joslas ir filtrētas: ieslēdz tās ar `set/filter dxbm/pass 6` (tad 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmeri MS modas dekodē reti. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X klasteris ar **PSKReporter** spotiem: šeit nonāk WSJT-X un MSHV MSK144 dekodējumi. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporter spoti reāllaikā caur **MQTT** (M0LTE pakalpojums): bez pieteikšanās, katrā spotā jau ir raidošās un uztverošās stacijas lokatori. Noklusējuma tēmas: MSK144 6 m, 4 m, 2 m, 1,25 m, 70 cm joslā un FSK441 2 m joslā (`pskr/filter/v2/band/mode/#`); *Noklusējuma tēmas* tās atjauno. |
| **Savāktie MS spoti** | – | Pieņemto spotu tabula, jaunākie pirmie. |

Katrai plūsmai ir resursdators, ports, komandas, ko sūta pēc pieteikšanās, *Savienot vēlreiz*, *Savienot startējot*, konsole un rinda komandu sūtīšanai. Augšā ieraksti savu **izsaukuma signālu pieteikšanās vajadzībām**. MQTT avotam ir resursdators, ports, tēmas (pa vienai rindā vai atdalītas ar `;`), *Savienot vēlreiz* un *Savienot startējot* (noklusējumā izslēgts) un konsole ar saņemtajiem spotiem; tā spoti iet caur to pašu filtru. Josla rāda visu četru avotu stāvokli (zaļš punkts = savienots). Sesijas paliek atvērtas, kad maini valodu vai krāsu shēmu.

## Filtrs (40 % no loga)

- **Neobligāts lokālais filtrs:** klasteru rindas zem **27990,0 kHz** tiek atmestas uzreiz (netiek rādītas, netiek saglabātas).
- CW spoti tiek uzreiz izmesti (CW vai WPM komentārā vai 28000-28070 kHz): tie neparādās konsolē un netiek saglabāti, ja vien nav atzīmēti ar <MS>. Rūtiņu var izslēgt.

CALL3 datubāze ar LIVETROPOVHF noteikumiem. „Atjaunināt tagad" lejupielādē CALL3.TXT no MMMonVHF (vismaz 100 000 derīgu rindu, iepriekšējais paliek data/call3.bak); ar „Atjaunināt pašam ik pēc 7 dienām" tas notiek palaišanas brīdī. Virs faila secībā darbojas: rokas ieraksti (data/CALL3-MANUALE.TXT), klastera labojumi (6 rakstzīmju lokators, ko spotētājs paziņo par sevi), pievienotie faili (data/CALL3-AGGIUNTE), tad CALL3.TXT un tiešraidē apgūtie 6 rakstzīmju lokatori (data/LOC6.TXT). Saņemts 4 rakstzīmju lokators vai tāds, kas beidzas ar LL vai MM, tiek aizstāts ar 6 rakstzīmju lokatoru no datubāzes; portatīvās (ar slīpsvītru) tikai ar precīzu ierakstu.

Pēdējais avots, kā LIVETROPOVHF: izsaukuma signāliem, kuriem nevienā citā avotā nav 6 rakstzīmju lokatora, programma fonā vaicā G7VRD publisko API (api.g7vrd.co.uk). Tiek pieņemts tikai 6 rakstzīmju lokators, nevis kvadrāta centrs (LL vai MM), tajā pašā kvadrātā kā saņemtais; ne vairāk kā 40 izsaukumi minūtē, katrs reizi dienā. Rezultāti ir data/CALL3-G7VRD.TXT.
- Spoti starp stacijām, kas ir tuvāk par 500 km, tiek uzreiz atmesti, jo šādā attālumā sakari ir tieši vai troposfēriski, nevis meteor scatter: tie neparādās konsolē un netiek saglabāti. Ja trūkst lokatora, spots paliek. Attālumu var mainīt zem rūtiņas.
- **1. kritērijs – tipiskās MS frekvences:** 50190–50300, 70100–70400, 144290–144399 kHz. Spots šajos logos tiek pieņemts arī bez modas nosaukuma, ja vien komentārā nav norādīta cita izplatīšanās: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Logus un birkas var rediģēt.
- **2. kritērijs – MS modas:** ārpus logiem vai ar kādu no šīm birkām spots tiek saglabāts tikai tad, ja tajā ir **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitālās modas, ko izmanto tikai MS) vai **\<MS\>**, ar lielajiem, mazajiem vai jauktiem burtiem. Vārdus var izslēgt, pievienot un dzēst; katram ir savs skaitītājs.
- **Joslas** 28, 50, 70, 144, 222, 432 MHz; **filtra pārbaude** ar ielīmētu rindu; **skaitītāji**.

## Lokatori un glabāšana

Trūkstošie lokatori vai lokatori tikai ar 4 rakstzīmēm tiek ņemti no **CALL3** arhīva (`data/call3.txt`, JTDX fails, vairāk nekā miljons izsaukuma signālu), kas vienmēr ir pārāks par 4 rakstzīmju lokatoru. Pieņemtie spoti tiek saglabāti mapē `data/spot_ms`, viens CSV fails dienā, un baro karti [Satiksme tiešsaistē](Live-Traffic-lv).
