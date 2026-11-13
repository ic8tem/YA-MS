[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · **Eesti** · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Andmete kogumine

*Sakk: Otse ja reaalajas andmed › Andmete kogumine.*

[![Andmete kogumine](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Neli allikat

Sakk kogub **meteor scatteri spotte** kolmest telneti voost ja PSKReporteri MQTT voost, igaüks oma alamsakil:

| Alamsakk | Vaikimisi | Märkused |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Vabalt valitav klaster. ON0DXK-l on VHF sagedusalad filtreeritud: lülita need sisse käsuga `set/filter dxbm/pass 6` (seejärel 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmerid dekodeerivad MS-moodusi harva. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-i klaster, mis edastab **PSKReporteri** spotte: siia jõuavad WSJT-X-i ja MSHV MSK144 dekodeeringud. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | PSKReporteri spotid reaalajas **MQTT** kaudu (M0LTE teenus): sisselogimist pole vaja, iga spot sisaldab juba saatva ja vastuvõtva jaama lokaatoreid. Vaiketeemad: MSK144 sagedusaladel 6 m, 4 m, 2 m, 1,25 m, 70 cm ja FSK441 sagedusalal 2 m (`pskr/filter/v2/band/mode/#`); *Vaiketeemad* taastab need. |
| **Kogutud MS-spotid** | – | Aktsepteeritud spotide tabel, uusimad eespool. |

Igal vool on host, port, pärast sisselogimist saadetavad käsud, *Ühenda uuesti*, *Ühenda käivitamisel*, konsool ja rida käskude saatmiseks. Kirjuta üles oma **kutsung sisselogimiseks**. MQTT allikal on host, port, teemad (üks rea kohta või eraldajaks `;`), *Ühenda uuesti* ja *Ühenda käivitamisel* (vaikimisi väljas) ning konsool vastuvõetud spotidega; selle spotid läbivad sama filtri. Riba näitab nelja allika olekut (roheline punkt = ühendatud). Seansid jäävad avatuks, kui vahetad keelt või värviskeemi.

## Filter (40 % aknast)

- **Valikuline kohalik filter:** klastri read alla **27990,0 kHz** jäetakse kohe kõrvale (ei näidata, ei salvestata).
- CW-spotid visatakse kohe ära (CW või WPM kommentaaris või 28000-28070 kHz): need ei ilmu konsooli ega salvestu, välja arvatud <MS> märgiga. Kasti saab välja lülitada.
- **1. kriteerium – tüüpilised MS-sagedused:** 50190–50300, 70100–70400, 144290–144399 kHz. Nendes akendes olev spot aktsepteeritakse ka ilma mooduse nimeta, välja arvatud juhul, kui kommentaar märgib muud levi: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Aknaid ja märgendeid saab muuta.
- **2. kriteerium – MS-moodused:** väljaspool aknaid või ühega neist märgenditest säilitatakse spot ainult siis, kui see sisaldab **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (ainult MS-i jaoks kasutatavad digitaalsed moodused) või **\<MS\>**, suur-, väike- või segatähtedega. Sõnu saab välja lülitada, lisada ja eemaldada; igal on oma loendur.
- **Sagedusalad** 28, 50, 70, 144, 222, 432 MHz; **filtri test** kleebitud real; **loendurid**.

## Lokaatorid ja salvestamine

Puuduvad lokaatorid või ainult 4-märgilised lokaatorid võetakse **CALL3** andmebaasist (`data/call3.txt`, JTDX-i fail, üle miljoni kutsungi), mis on alati eelistatud 4-märgilisele lokaatorile. Aktsepteeritud spotid salvestatakse kausta `data/spot_ms`, üks CSV-fail päevas, ja need toidavad kaarti [Liiklus otse](Live-Traffic-et).
