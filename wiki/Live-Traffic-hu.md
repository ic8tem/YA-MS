[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · **Magyar** · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Élő forgalom

*Fül: Élő és valós idejű adatok › Élő forgalom.*

[![Élő forgalom](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Mit mutat

Az Ön állomására középpontos **azimutális távolságtartó térkép** (a középponttól mért távolság = valós távolság, a szög = azimut), rajta az [Adatgyűjtés](Data-Collection-hu) által összegyűjtött **teljes meteorszórásos forgalommal**. Minden összeköttetéshez a program megrajzolja:

- a két állomás közötti **útvonalat** a sávja színével: 28 MHz barna, 50 MHz zöld, 70 MHz cián, 144 MHz narancs, 222 MHz rózsaszín, 432 MHz ibolya;
- a két **állomást** az útvonal végein;
- a **felhőt**: azt a területet, ahol az adott útvonalra és időpontra a legvalószínűbb meteornyomok összpontosulnak.

Azok a spotok, amelyeknek valamelyik állomása **a térképen kívül** esik, elvetésre kerülnek. Az **éppen beérkezett** spot (legfeljebb 3 perces) **egy percig villog**, így az új aktivitás azonnal szembetűnik.

Mutasd, ki figyel: a sáv színű háromszögek jelölik azokat az állomásokat, amelyek a PSKReporter szerint a választott időablakban MSK144, FSK441, PSK2K vagy JTMS módban vesznek 28, 50, 70, 144 és 432 MHz-en. Egy háromszögre kattintva látszik a hívójel, a lokátor, a módok és az utolsó spot. Az Adatgyűjtés fül MQTT-folyamának csatlakoztatva kell lennie.

A térkép minden spot mindkét állomásának hívójelét kiírja, állomásonként egyszer. A vetület választható: azimutális (középen az állomásod) vagy Mercator. A Felhő oszlop buboréksúgója elmagyarázza a jelentését.

Minden sáv spotjai látszanak, azoké is, amelyeket az Adatgyűjtésben nem választottál ki (ezek nem tárolódnak). A CW spotok és a túl közeli állomások közötti spotok nem látszanak, ha az Adatgyűjtésben elvetésre kerülnek.

## Hogyan számítja a felhőt

A program minden spothoz felépíti a két lokátor közötti útvonalat (ugyanazzal a geometriával, mint az Ön saját útvonalánál, lásd: [Geometria és útcsillapítás](Geometry-and-Path-Loss-hu)), és a spot időpontjában az E-réteg minden pontjára összeadja **az összes aktív raj tükrös reflexiós hozzájárulását** a ZHR-jével súlyozva – ugyanez a számítás készíti az [égbolt-kupola](Sky-View-hu) **PREV zónáit** is. Az útvonal minden olyan oldalán, amely az összegnek legalább 15 %-át adja, a felhő egy **ellipszis**: középpontja a pontok súlyozott átlaga, féltengelyei a szórásmátrix sajátértékei négyzetgyökének 1,5-szerese, nagytengelye a fő sajátvektor irányába esik. Ha egyetlen raj sem járul hozzá (csak sporadikus meteorok), a felhők a két klasszikus **hot spot**, szaggatott vonallal rajzolva. A teljes egyenletek a számítási kézikönyv 10. fejezetében találhatók.

## Vezérlők

| Vezérlő | Jelentés |
|---|---|
| **Térkép sugara** | 600–3500 km az Ön állomásától. |
| **Megjelenítendő spotok** | Az utolsó 15 vagy 30 perc, az utolsó óra, az utolsó 3 óra, az utolsó 24 óra. |
| **Táblázat** | A térképen lévő összeköttetések, a legújabb elöl, a sáv színével; a *Felhő* oszlop a fő oldalra eső reflexiók arányát mutatja, vagy azt, hogy *sporadikus*. |
| **Kattintás** | Egy útvonalra vagy táblázatsorra: az összeköttetés kiemelődik, és a mező kiírja a felhő középpontjának lokátorát, arányát, méretét és tengelyét. |
