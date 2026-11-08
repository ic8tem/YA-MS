**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Efektivitāte - skaidrojums

*Cilne: Tehniskie dokumenti › Efektivitāte - skaidrojums.*

[![Efektivitāte - skaidrojums](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Tehnisks dokuments *"Come YA-MS calcola l'efficienza di uno sciame"* (Kā YA-MS aprēķina plūsmas efektivitāti), kas programmā parādīts kā gaiša lapa. Tas **soli pa solim** izskaidro, kā tiek iegūta efektivitāte, un katram solim norāda, **no kurienes tas nāk**. Dokuments pašlaik ir **itāļu valodā**; šī wiki tā saturu latviski sniedz lapās [Efektivitātes aprēķins](Efficiency-Calculation-lv#modelis) un [Ģeometrija un vājinājums](Geometry-and-Path-Loss-lv).

## Etiķetes

Katram solim ir krāsaina etiķete:

| Etiķete | Krāsa | Nozīme |
|---|---|---|
| **FONTE** (avots) | zila | solis pārņem citētu avotu; skaitlis iekavās attiecas uz sarakstu beigās |
| **RILIEVO** (pārbaude) | zaļa | programmas un avotu salīdzinājums ar rezultātu |
| **SCELTA** (izvēle) | oranža | programmas izvēle, kas nav ņemta no avota: jāpārbauda ar pieredzi ēterā |

## Nodaļas

| Nodaļa | Saturs |
|---|---|
| 1. Ievads | Mērķis, etiķetes, ko nozīmē efektivitāte (OH5IY, MCG_MS; YA-MS izmanto reālo trasi) |
| 2. Kur notiek atstarošana: E slānis | Sliedes 80–120 km augstumā; sliežu augstums = Collm histogrammas moda (pārbaude: 89,5 km 5/11/2026) |
| 3. Trases ģeometrija | Zeme un viduspunkts; antenas elevācija (raksta formula); kopējā zona un tās robežas; Hot A / Hot B; antenas ziedlapiņa (DL6WU, Kraus, W4RNL) |
| 4. Plūsmas radiants | Radianta stāvoklis (IMO 2026/2027), maksimuma datums (IMO vai Saules garums), aktivitātes profils |
| 5. Atstarošanas nosacījums | Spoguļatstarošana (McKinley), Gausa pielaide 0,05 rad, labākais virziens (SM6FHZ), DH9GCD formula |
| 6. No viena punkta līdz efektivitātei | Atstarošanas punkti ik pēc 15 km, katra punkta svars, procenti; salīdzinājums ar QTFGUI (DJ5HG) |
| 7. Rezultātu lasīšana | Puse A / B, trases indekss, radiantu krāsas, PREV zonas, griezums, kā to redz antena |
| 8. Darba frekvence un trases vājinājums | λ³ / λ² likumi, no radara uz amatieru joslu, trases vājinājuma atsauces |
| 9. Zināmie ierobežojumi | Tikai zema blīvuma sliedes, izotropas antenas, darba vērtības |
| 10. Avoti | 17 numurēti avoti |

## Pogas

| Poga | Ko tā dara |
|---|---|
| **Eksportēt uz Word (.docx)...** | Saglabā faila `data/efficienza_spiegazione.docx` kopiju tevis izvēlētā vietā (ieteiktais nosaukums *YA-MS - calcolo dell'efficienza.docx*) |
| **Atvērt Word** | Atver to pašu `.docx` ar noklusējuma programmu Word dokumentiem (Word, LibreOffice, …) |

## Faili

| Fails | Saturs |
|---|---|
| `data/efficienza_spiegazione.txt` | Cilnē rādītais teksts, viens bloks rindā (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word versija |
| `doc/YA-MS_manuale_calcoli.docx` | **Aprēķinu rokasgrāmata**: visi vienādojumi (Word vienādojumu redaktors), numurēti, ar avotiem |

Abus dokumentus no pirmkoda ģenerē no jauna ar `tools/build_spiegazione.py data` un `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
