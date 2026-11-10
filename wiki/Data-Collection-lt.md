[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · **Lietuvių** · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Duomenų rinkimas

*Kortelė: Tiesiogiai ir realiojo laiko duomenys › Duomenų rinkimas.*

[![Duomenų rinkimas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Trys klasterių srautai

Kortelė renka **meteor scatter spotus** iš trijų telnet srautų, kiekvieną savo vidinėje kortelėje:

| Vidinė kortelė | Numatytasis | Pastabos |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Pasirinktas klasteris. ON0DXK VHF juostos filtruojamos: įjunkite jas komanda `set/filter dxbm/pass 6` (paskui 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimeriai MS modas dekoduoja retai. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X klasteris, perduodantis **PSKReporter** spotus: čia ateina WSJT-X ir MSHV MSK144 dekodavimai. |
| **Surinkti MS spotai** | – | Priimtų spotų lentelė, naujausi viršuje. |

Kiekvienas srautas turi serverį, prievadą, po prisijungimo siunčiamas komandas, *Prisijungti iš naujo*, *Prisijungti paleidžiant*, konsolę ir eilutę komandoms siųsti. Viršuje įrašykite savo **šaukinį prisijungimui**. Juostelė rodo trijų seansų būseną (žalias taškas = prisijungta). Seansai lieka atviri keičiant kalbą ar spalvų schemą.

## Filtras (40 % lango)

- **Neprivalomas vietinis filtras:** klasterio eilutės žemiau **27990,0 kHz** iš karto atmetamos (nerodomos, nesaugomos).
- **1-as kriterijus – tipiniai MS dažniai:** 50190–50300, 70100–70400, 144290–144399 kHz. Šiuose languose esantis spotas priimamas ir be modos pavadinimo, nebent komentare nurodytas kitas sklidimas: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Langus ir žymas galima keisti.
- **2-as kriterijus – MS modos:** už langų arba su viena iš tų žymų spotas paliekamas tik tada, jei jame yra **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (skaitmeninės modos, naudojamos tik MS) arba **\<MS\>**, didžiosiomis, mažosiomis ar mišriomis raidėmis. Žodžius galima išjungti, pridėti ir pašalinti; kiekvienas turi savo skaitiklį.
- **Juostos** 28, 50, 70, 144, 222, 432 MHz; **filtro bandymas** su įklijuota eilute; **skaitikliai**.

## Lokatoriai ir saugojimas

Trūkstami lokatoriai arba lokatoriai tik su 4 simboliais imami iš **CALL3** bazės (`data/call3.txt`, JTDX failas, daugiau nei milijonas šaukinių), kuri visada turi pirmenybę prieš 4 simbolių lokatorių. Priimti spotai įrašomi į `data/spot_ms`, po vieną CSV failą per dieną, ir naudojami žemėlapyje [Eismas realiuoju laiku](Live-Traffic-lt).
