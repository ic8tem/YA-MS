**English** · [Русский](Data-Collection-ru) · [Deutsch](Data-Collection-de) · [日本語](Data-Collection-ja)

# Andmete kogumine

*Sakk: Otse ja reaalajas andmed › Andmete kogumine.*

[![Andmete kogumine](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Kolm klastrivoogu

Sakk kogub **meteor scatteri spotte** kolmest telneti voost, igaüks oma alamsakil:

| Alamsakk | Vaikimisi | Märkused |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Vabalt valitav klaster. ON0DXK-l on VHF sagedusalad filtreeritud: lülita need sisse käsuga `set/filter dxbm/pass 6` (seejärel 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmerid dekodeerivad MS-moodusi harva. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | DM4X-i klaster, mis edastab **PSKReporteri** spotte: siia jõuavad WSJT-X-i ja MSHV MSK144 dekodeeringud. |
| **Kogutud MS-spotid** | – | Aktsepteeritud spotide tabel, uusimad eespool. |

Igal vool on host, port, pärast sisselogimist saadetavad käsud, *Ühenda uuesti*, *Ühenda käivitamisel*, konsool ja rida käskude saatmiseks. Kirjuta üles oma **kutsung sisselogimiseks**. Riba näitab kolme seansi olekut (roheline punkt = ühendatud). Seansid jäävad avatuks, kui vahetad keelt või värviskeemi.

## Filter (40 % aknast)

- **Valikuline kohalik filter:** klastri read alla **27990,0 kHz** jäetakse kohe kõrvale (ei näidata, ei salvestata).
- **1. kriteerium – tüüpilised MS-sagedused:** 50190–50300, 70100–70400, 144290–144399 kHz. Nendes akendes olev spot aktsepteeritakse ka ilma mooduse nimeta, välja arvatud juhul, kui kommentaar märgib muud levi: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Aknaid ja märgendeid saab muuta.
- **2. kriteerium – MS-moodused:** väljaspool aknaid või ühega neist märgenditest säilitatakse spot ainult siis, kui see sisaldab **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (ainult MS-i jaoks kasutatavad digitaalsed moodused) või **\<MS\>**, suur-, väike- või segatähtedega. Sõnu saab välja lülitada, lisada ja eemaldada; igal on oma loendur.
- **Sagedusalad** 28, 50, 70, 144, 222, 432 MHz; **filtri test** kleebitud real; **loendurid**.

## Lokaatorid ja salvestamine

Puuduvad lokaatorid või ainult 4-märgilised lokaatorid võetakse **CALL3** andmebaasist (`data/call3.txt`, JTDX-i fail, üle miljoni kutsungi), mis on alati eelistatud 4-märgilisele lokaatorile. Aktsepteeritud spotid salvestatakse kausta `data/spot_ms`, üks CSV-fail päevas, ja need toidavad kaarti [Liiklus otse](Live-Traffic-et).
