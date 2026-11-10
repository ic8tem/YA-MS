[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · **Magyar** · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter előrejelzések és élő rajhatékonyság

*készítette: Costantino Cerrotta IC8TEM*

A **YA-MS** ingyenes program azoknak a rádióamatőröknek, akik **meteor scatter (MS) összeköttetéseket folytatnak az 50, 70, 144, 222 és 432 MHz-es sávokon**. A saját lokátora és a DX állomás lokátora közötti valódi útvonalra óráról órára kiszámítja, mennyire segíti az útvonalat az egyes aktív meteorrajok (ez a **hatékonyság**), az útvonal melyik oldaláról érkeznek a visszaverődések (**Hot A / Hot B**), merre kell az antennát fordítani, valamint egy **élő meteorradar** (Collm, Németország) adataiból levezetett kísérleti előrejelzést ad az óránkénti visszaverődések számára. **Windows, Linux és macOS** alatt fut (.NET 8 + Avalonia), 36 kezelőfelületi nyelven.

A fő forrás **C. Cerrotta IC8TEM és G. Sartori IV3GTH** cikke: *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese”* (7. változat). A program minden képlete és adata megadja a forrását; lásd [Források](Sources-hu).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Égbolt-kupola"></a><br><sub>Égbolt-kupola</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Hatékonyság számítása"></a><br><sub>Hatékonyság számítása</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES radar"></a><br><sub>GRAVES radar</sub></td>
</tr></table>

## Kinek szól

- Azoknak az operátoroknak, akik tudni szeretnék, **mikor** nyitott egy meteor scatter útvonal és **merre** kell irányítani az antennát – túl az általános „ma éjjel van a raj csúcsa” megállapításon.
- **Hosszú útvonalakon dolgozó állomásoknak 144 és 432 MHz-en**, ahol a radiáns helyzete dönti el, hogy egy raj hasznos vagy haszontalan.
- Mindenkinek, aki **ellenőrizni szeretné a számokat**: a számítási kézikönyv és a programon belüli magyarázat minden lépést megad az eredetével együtt: publikált forrás, a programon végzett ellenőrzés vagy a program saját választása.

## A fülek

Az 1.6-os változat óta a fő füleknek **alfülei** vannak (egy világosabb sor a fő sor alatt). Induláskor egy 5 másodperces nyitókép a Perseidákat mutatja az ESO VLT felett (fotó: ESO/S. Guisard, CC BY 4.0).

| Fül | Alfül | Mit mutat |
|---|---|---|
| **Élő és valós idejű adatok** | [Élő forgalom](Live-Traffic-hu) | Az összes gyűjtött MS-forgalom azimutális térképe, minden összeköttetéshez a legvalószínűbb nyomok felhőjével, sávszínekkel, villogó új spotokkal |
| | [Radarfluxus](Radar-Flux-hu) | A Collm SKiYMET radarról leolvasott óránkénti meteorszámok és nyommagasságok, Sodankylä-kép, becslés az Ön sávjára |
| | [GRAVES radar](GRAVES-Radar-hu) | A GRAVES → Ön forward scatter útvonal: hasznos zóna a nyalábban, szektor és lépés, a nyaláb következő áthaladása, hogyan lehet hallgatni |
| | [Adatgyűjtés](Data-Collection-hu) | Három telnetes cluster-adatfolyam (DX cluster, RBN, DM4X/PSKReporter) és az MS-spotszűrő |
| **Előrejelzés számítása** | [Előrejelzés számítása](Sky-View-hu) | Az útvonal felülnézeti térképe Hot A / Hot B pontokkal, antennalebennyel, PREV zónákkal és a raj elmozdulásával; rajlista; kis égbolt-kupola a radiánsokkal és a helyes antennairányokkal; metszet az antenna felől nézve |
| | [Geometria és útvonalcsillapítás](Geometry-and-Path-Loss-hu) | Távolság, felezőpont, eleváció, Hot A / Hot B, a közös zóna határai, útvonalcsillapítás 28–432 MHz, összeköttetési mérleg, antenna |
| | [Hatékonyság számítása](Efficiency-Calculation-hu) | Áttekintő kártyák, az egyes rajok óránkénti hatékonysága A/B oldallal, útvonalindex, DH9GCD-összehasonlítás, grafikon |
| | [Kísérleti előrejelzések](Experimental-Forecasts-hu) | A Collm-fluxus 144 MHz-re (vagy bármely frekvenciára) skálázva λ^k-val és K állomástényezővel, 24 órás előrejelzés, RMOB-összehasonlítás |
| **Műszaki dokumentumok** | [Források](Sources-hu) | Az összes forrás; a fő forrás a Cerrotta–Sartori cikk |
| | [Az európai radarok térképe](European-Radar-Map-hu) | Hol van Collm, Sodankylä, GRAVES és CMOR az Ön állomásához képest |
| | [Hatékonyság - magyarázat](Efficiency-Explanation-hu) | Lépésről lépésre bemutató dokumentum a hatékonyság kiszámításáról, Wordbe exportálható |
| [Élő rajok](Live-Showers-hu) | – | A Global Meteor Network mért ZHR-értékei és a CMOR radiánstérképei |
| [Rajok](Showers-hu) | – | IMO-katalógus a következő csúccsal (IMO dátum és időpont, vagy számított) |
| [Négyzettérkép](Grid-Square-Map-hu) | – | Egy ADIF-fájl alapján forgalmazott és megerősített Maidenhead-négyzetek, sávonként egy füllel |

A fülek felett három sor vezérlő található (saját lokátor, DX állomás, sáv, antenna, nyommagasság, idő); lásd [Első lépések](Getting-Started-hu). A **Vezérlők** gomb összecsukja őket, a nyelv és a színséma pedig jobb felül választható; lásd [Beállítások és adatmappa](Settings-and-Data-Folder-hu).

## Röviden

- **Valódi útvonal, nem rögzített irányok**: a hatékonyság a két lokátor közötti főkör-útvonalra számítódik (a régebbi programok négy rögzített irányt használtak).
- **Tükrös visszaverődési modell** (McKinley) az E-réteg 15 km-enként felvett pontjain, a Collm radarról élőben leolvasott nyommagassággal.
- **Hot A / Hot B** a felezőponttól 150 km-re mindkét oldalon (30–400 km között állítható), az ajánlott pirossal, az antennalebenyen már belül esők szürkével.
- **Élő radar**: a Collm ötpercenként ellenőrizve, csak a megváltozott források töltődnek le újra; kapcsolat nélkül a program az utoljára mentett adatokkal dolgozik tovább.
- **Kísérleti** előrejelzés 50/144/432 MHz-en SM6FHZ λ³-szabályával, RMOB-megfigyelőkkel összevethetően.
- Minden egyetlen **`data`** mappában a program mellett: nincs AppData, nincsenek rendszermappák.

> A hatékonyság kísérleti modell (tükrös visszaverődés + alulsűrű nyomok). Vesse össze az MCG_MS, az MS-Soft eredményeivel és saját forgalmi tapasztalataival.

## Hol kezdjük

1. [Telepítés](Installation-hu)
2. [Első lépések](Getting-Started-hu)
3. [Hibaelhárítás és GYIK](Troubleshooting-FAQ-hu), ha valami nem működik.

Letöltések: **[Releases](https://github.com/ic8tem/YA-MS/releases)** a GitHubon.
