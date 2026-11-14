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

A PSKReporter térkép aktív monitorai is: üres háromszögek azoknak az állomásoknak, amelyek MSK144, FSK441, PSK2K vagy JTMS módban látszanak a pskreporter.info térképén, de még nem vettek spotot (az MQTT csak azokat küldi, akik vesznek valamit). A YA-MS 5 percenként egyszer kérdezi le a PSKReporter lekérdező szolgáltatását minden üzemmódra, ahogy a szolgáltatás szabályai kérik; egy monitor legalább 11 percig a térképen marad. A háromszögre kattintva látszik a hívójel, a lokátor, a dekódoló program és az idő, amikor a monitor aktív volt. Alapból bekapcsolva.

FT8 1100 km felett párhuzamos útvonal nélkül: egy FT8 spot (a PSKReporter MQTT-ből, a clusterekből vagy a WSJT-X-ből UDP-n), két 1100 km-nél távolabbi állomás között, amelynek az előtte és utána lévő 3 percben nincs párhuzamos útvonala (azonos sáv, felezőpont 300 km-en belül, irány 15°-on belül, másik állomáspár), világoszölddel rajzolódik, és a sora a jobb alsó táblázatban mindig villog. A sporadikus E és a tropo sok közeli, párhuzamos útvonalat ad; egy magányos spot meteornyom lehet. Ezért a YA-MS az MQTT-ből a 6 m, 4 m, 2 m, 1,25 m és 70 cm FT8 spotjait is fogadja (a 10 m-eseket nem, túl sok van). Ezek a spotok nem kerülnek az MS archívumba. Alapból bekapcsolva.

Az UDP-n érkező WSJT-X spotok, amelyek az állomásodat érintik (a dekódolásban szerepel a hívójeled: aki hív vagy válaszol neked), mindig villogó szaggatott vonallal rajzolódnak, bármely üzemmódban és bármilyen távolságon.

Csere a YA-MS felhasználói között: ha egy másik YA-MS-felhasználó UDP-n dekódol egy az állomásodnak szóló üzenetet (MSK144, FSK441, PSK2K vagy JTMS módban, vagy FT8-ban 1100 km felett), az ő YA-MS-e titkosítva elküldi neked három nyilvános MQTT-brókeren át (HiveMQ, Mosquitto, EMQX); mindig villogó lila szaggatott vonalként és egy sorként látod az UDP konzolban. Csak te olvashatod (ECDH P-256 kulcsok, AES-256 és HMAC-SHA256). Az FT8 spotok csak akkor látszanak, ha 3 percen belül nincs párhuzamos útvonaluk. Alapból bekapcsolva; a data/config.ini yams_scambio=0 sora kikapcsolja.

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
