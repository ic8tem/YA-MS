[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · **Lietuvių** · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Duomenų rinkimas

*Kortelė: Tiesiogiai ir realiojo laiko duomenys › Duomenų rinkimas.*

[![Duomenų rinkimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Keturi šaltiniai

Kortelė renka **meteor scatter spotus** iš trijų telnet srautų ir iš PSKReporter MQTT srauto, kiekvieną savo vidinėje kortelėje:

| Vidinė kortelė | Numatytasis | Pastabos |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Pasirinktas klasteris. ON0DXK VHF juostos filtruojamos: įjunkite jas komanda `set/filter dxbm/pass 6` (paskui 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimeriai MS modas dekoduoja retai. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X klasteris, perduodantis **PSKReporter** spotus: čia ateina WSJT-X ir MSHV MSK144 dekodavimai. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporter spotai realiuoju laiku per **MQTT** (M0LTE paslauga): prisijungti nereikia, kiekviename spote jau yra siunčiančios ir priimančios stoties lokatoriai. Numatytosios temos: MSK144 6 m, 4 m, 2 m, 1,25 m, 70 cm juostose ir FSK441 2 m juostoje (`pskr/filter/v2/band/mode/#`); *Numatytosios temos* jas atkuria. |
| **Surinkti MS spotai** | – | Priimtų spotų lentelė, naujausi viršuje. |

Kiekvienas srautas turi serverį, prievadą, po prisijungimo siunčiamas komandas, *Prisijungti iš naujo*, *Prisijungti paleidžiant*, konsolę ir eilutę komandoms siųsti. Viršuje įrašykite savo **šaukinį prisijungimui**. MQTT šaltinis turi serverį, prievadą, temas (po vieną eilutėje arba atskirtas `;`), *Prisijungti iš naujo* ir *Prisijungti paleidžiant* (pagal nutylėjimą išjungta) bei konsolę su gautais spotais; jo spotai eina per tą patį filtrą. Juostelė rodo keturių šaltinių būseną (žalias taškas = prisijungta). Seansai lieka atviri keičiant kalbą ar spalvų schemą.

## Filtras (40 % lango)

- **Neprivalomas vietinis filtras:** klasterio eilutės žemiau **27990,0 kHz** iš karto atmetamos (nerodomos, nesaugomos).
- CW spotai iškart atmetami (CW ar WPM komentare arba 28000-28070 kHz): jie nerodomi konsolėje ir neišsaugomi, nebent pažymėti <MS>. Langelį galima išjungti.

CALL3 duomenų bazė su LIVETROPOVHF taisyklėmis. „Atnaujinti dabar" atsisiunčia CALL3.TXT iš MMMonVHF (bent 100 000 tinkamų eilučių, ankstesnis lieka data/call3.bak); pasirinkus „Atnaujinti pačiam kas 7 dienas" tai daroma paleidžiant. Virš failo eilės tvarka galioja: rankiniai įrašai (data/CALL3-MANUALE.TXT), klasterio pataisos (6 simbolių lokatorius, kurį spotintojas nurodo apie save), pridėti failai (data/CALL3-AGGIUNTE), tada CALL3.TXT ir tiesiogiai išmokti 6 simbolių lokatoriai (data/LOC6.TXT). Gautas 4 simbolių lokatorius arba besibaigiantis LL ar MM pakeičiamas 6 simbolių lokatoriumi iš duomenų bazės; portatyvinės (su pasviruoju brūkšniu) tik su tiksliu įrašu.

Paskutinis šaltinis, kaip LIVETROPOVHF: šaukiniams, kurie jokiame kitame šaltinyje neturi 6 simbolių lokatoriaus, programa automatiškai kas 6 valandas klausia viešosios G7VRD API (api.g7vrd.co.uk), grupėmis po 40 šaukinių; kiekvieną šaukinį ne dažniau kaip kartą per dieną. Priimamas tik 6 simbolių lokatorius, ne kvadrato centras (LL ar MM), tame pačiame kvadrate kaip gautasis. Rezultatai saugomi data/CALL3-G7VRD.TXT ir, kaip visos pataisos, įrašomi ir į data/call3.txt.
- Spotai tarp stočių, esančių arčiau nei 500 km, iš karto atmetami, nes tokiu atstumu ryšys yra tiesioginis arba troposferinis, o ne meteor scatter: jie nerodomi konsolėje ir neišsaugomi. Jei trūksta lokatoriaus, spotas paliekamas. Atstumą galima pakeisti po langeliu.
- **1-as kriterijus – tipiniai MS dažniai:** 50190–50300, 70100–70400, 144290–144399 kHz. Šiuose languose esantis spotas priimamas ir be modos pavadinimo, nebent komentare nurodytas kitas sklidimas: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Langus ir žymas galima keisti.
- **2-as kriterijus – MS modos:** už langų arba su viena iš tų žymų spotas paliekamas tik tada, jei jame yra **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (skaitmeninės modos, naudojamos tik MS) arba **\<MS\>**, didžiosiomis, mažosiomis ar mišriomis raidėmis. Žodžius galima išjungti, pridėti ir pašalinti; kiekvienas turi savo skaitiklį.
- **Juostos** 28, 50, 70, 144, 222, 432 MHz; **filtro bandymas** su įklijuota eilute; **skaitikliai**.

## Lokatoriai ir saugojimas

Trūkstami lokatoriai arba lokatoriai tik su 4 simboliais imami iš **CALL3** bazės (`data/call3.txt`, JTDX failas, daugiau nei milijonas šaukinių), kuri visada turi pirmenybę prieš 4 simbolių lokatorių. Priimti spotai įrašomi į `data/spot_ms`, po vieną CSV failą per dieną, ir naudojami žemėlapyje [Eismas realiuoju laiku](Live-Traffic-lt).
