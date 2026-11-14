[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · **Magyar** · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteorszórás-előrejelzés és a meteorrajok élő hatékonysága

*Szerző: Costantino Cerrotta IC8TEM*

A **YA-MS** ingyenes program azoknak a rádióamatőröknek, akik **meteorszórásos (MS) összeköttetéseket létesítenek az 50, 70, 144, 222 és 432 MHz-es sávokban**. Az Ön lokátora és a DX-állomás lokátora közötti valós útvonalra óránként kiszámítja, mennyit segít az útvonalon az egyes aktív meteorrajok (ez a **hatékonyság**), az útvonal melyik oldaláról érkeznek a reflexiók (**Hot A / Hot B**), merre kell fordítani az antennát, valamint egy **élő meteorradarból** (Collm, Németország) származtatott kísérleti előrejelzést ad az óránkénti reflexiók számára. Fut **Windows, Linux, Raspberry Pi és macOS** rendszeren (.NET 8 + Avalonia), 36 felületi nyelven.

A fő forrás **C. Cerrotta IC8TEM és G. Sartori IV3GTH** cikke: *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese”* (Meteorszórás – avagy hogyan érjük el Európát VHF-en egész évben, különösebb igények nélkül; 7. változat). A programban minden képlet és adat megjelöli a forrását; lásd: [Források](Sources-hu).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Égbolt-kupola"></a><br><sub>Égbolt-kupola</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Hatékonyság-számítás"></a><br><sub>Hatékonyság-számítás</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES-radar"></a><br><sub>GRAVES-radar</sub></td>
</tr></table>

## Kinek szól

- Azoknak az operátoroknak, akik tudni szeretnék, **mikor** nyitott egy meteorszórásos útvonal és **merre** kell fordítani az antennát – túl az általános „ma éjjel van a raj csúcsa” kijelentésen.
- Azoknak az állomásoknak, amelyek **hosszú útvonalakon dolgoznak 144 és 432 MHz-en**, ahol a radiáns helyzete dönti el, hogy egy raj hasznos vagy haszontalan.
- Mindenkinek, aki **ellenőrizni szeretné a számokat**: a számítási kézikönyv és a programon belüli magyarázat minden lépést a származásával együtt közöl: publikált forrás, a programon végzett ellenőrzés vagy a program saját döntése.

## A fülek

Az 1.6-os változat óta a fő fülek **alfülekkel** rendelkeznek (egy világosabb sor a fő sor alatt). Indításkor egy 5 másodperces nyitókép a Perseidákat mutatja az ESO VLT távcsövei felett (fotó: ESO/S. Guisard, CC BY 4.0).

| Fül | Alfül | Mit mutat |
|---|---|---|
| **Élő és valós idejű adatok** | [Élő forgalom](Live-Traffic-hu) | Az összes gyűjtött MS-forgalom azimutális térképe, minden összeköttetéshez a legvalószínűbb meteornyomok felhőjével, sávonkénti színekkel, villogással, ha egy ellenállomás válaszol neked |
| | [Radarfluxus](Radar-Flux-hu) | Óránkénti meteorszámok és nyommagasságok a Collm SKiYMET radarból, a sodankyläi kép, becslés az Ön sávjára |
| | [GRAVES-radar](GRAVES-Radar-hu) | A GRAVES → Ön előreszórásos útvonal: hasznos zóna a nyalábban, szektor és lépés, a nyaláb következő áthaladása, hogyan érdemes hallgatni |
| | [Adatgyűjtés](Data-Collection-hu) | Három telnetes clusterfolyam (DX cluster, RBN, DM4X/PSKReporter) és az MS-spotszűrő |
| **Előrejelzés-számítás** | [Előrejelzés-számítás](Sky-View-hu) | Az útvonal felülnézeti térképe Hot A / Hot B pontokkal, antennanyalábbal, PREV zónákkal és a rajok vándorlásával; rajlista; kis égbolt-kupola a radiánsokkal és a helyes antennairányokkal; az antennából látott metszet |
| | [Geometria és útcsillapítás](Geometry-and-Path-Loss-hu) | Távolság, felezőpont, elevációs szög, Hot A / Hot B, a közös zóna határai, útcsillapítás 28–432 MHz-en, összeköttetési mérleg, antenna |
| | [Hatékonyság-számítás](Efficiency-Calculation-hu) | Áttekintő kártyák, az egyes rajok óránkénti hatékonysága A/B oldallal, útvonalindex, összevetés a DH9GCD-vel, grafikon |
| | [Kísérleti előrejelzések](Experimental-Forecasts-hu) | A collmi fluxus 144 MHz-re (vagy bármely frekvenciára) skálázva λ^k-val és a K állomástényezővel, 24 órás előrejelzés, összehasonlítás az RMOB-bal |
| [Élő rajok](Live-Showers-hu) | – | A Global Meteor Network által mért ZHR és a CMOR radiánstérképei |
| [Meteorrajok](Showers-hu) | – | IMO-katalógus a következő csúccsal (IMO-dátum és -időpont vagy számított) |
| [Lokátornégyzet-térkép](Grid-Square-Map-hu) | – | Ledolgozott és visszaigazolt Maidenhead-négyzetek egy ADIF-fájlból, sávonként egy fül |
| **Műszaki dokumentumok** | [Források](Sources-hu) | Az összes forrás; a fő forrás a Cerrotta–Sartori-cikk |
| | [Európai radarok térképe](European-Radar-Map-hu) | Hol van Collm, Sodankylä, a GRAVES és a CMOR az Ön állomásához képest |
| | [A hatásfok számításának magyarázata](Efficiency-Explanation-hu) | Lépésről lépésre bemutatja a hatékonyság kiszámítását, Wordbe exportálható |

A fülek felett három sor vezérlőelem található (saját lokátor, DX-állomás, sáv, antenna, nyommagasság, idő); lásd: [Első lépések](Getting-Started-hu). A **Vezérlők** gomb összecsukja őket, a nyelv és a színséma pedig a jobb felső sarokban választható ki; lásd: [Beállítások és adatmappa](Settings-and-Data-Folder-hu).

## Röviden

- **Valós útvonal, nem rögzített irányok**: a hatékonyságot a két lokátor közötti főkörív menti útvonalra számítja (a régebbi programok négy rögzített irányt használtak).
- **Tükrös reflexiós modell** (McKinley) az E-réteg 15 km-enként felvett pontjain, a nyommagasságot élőben olvassa a collmi radarból.
- **Hot A / Hot B** a felezőponttól 150 km-re mindkét oldalon (30–400 km között állítható), az ajánlott pirossal, az antennanyalábon már belül esők szürkével.
- **Élő radar**: Collm ötpercenkénti ellenőrzése, csak a megváltozott források töltődnek le újra; internet nélkül a program az utoljára mentett adatokkal dolgozik tovább.
- **Kísérleti** előrejelzés 50/144/432 MHz-re az SM6FHZ-féle λ³-szabállyal, összevethető az RMOB-megfigyelőkkel.
- Minden egyetlen **`data`** mappában van a program mellett: nincs AppData, nincsenek rendszermappák.

> A hatékonyság kísérleti modell (tükrös reflexió + alulsűrű nyomok). Vesse össze az MCG_MS, az MS-Soft eredményeivel és saját forgalmazási tapasztalataival.

## Hol kezdjem

1. [Telepítés](Installation-hu)
2. [Első lépések](Getting-Started-hu)
3. [Hibaelhárítás és GYIK](Troubleshooting-FAQ-hu), ha valami nem működik.

Letöltések: **[Releases](https://github.com/ic8tem/YA-MS/releases)** a GitHubon.
