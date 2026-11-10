[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · **Magyar** · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [ไทย](Live-Traffic-th) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Élő forgalom

*Fül: Élő és valós idejű adatok › Élő forgalom.*

[![Élő forgalom](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Mit mutat

Egy az Ön állomására központosított **azimutális távolságtartó térkép** (a középponttól mért távolság = valódi távolság, a szög = azimut) az [Adatgyűjtés](Data-Collection-hu) által összegyűjtött **teljes meteor scatter forgalommal**. Minden összeköttetéshez a program megrajzolja:

- a két állomás közötti **útvonalat** a sávja színével: 28 MHz barna, 50 MHz zöld, 70 MHz cián, 144 MHz narancs, 222 MHz rózsaszín, 432 MHz ibolya;
- a két **állomást** az útvonal végein;
- a **felhőt**: ahol az adott útvonalra és időpontra a legvalószínűbb meteornyomok koncentrálódnak.

A **térképen kívül** eső állomást tartalmazó spotokat a program elveti. Az **éppen beérkezett** (legfeljebb 3 perces) spot **egy percig villog**, így az új aktivitás első pillantásra feltűnik.

## Hogyan számítódik a felhő

Minden spothoz a program felépíti a két lokátor közötti útvonalat (ugyanazzal a geometriával, mint az Ön saját útvonalánál, lásd [Geometria és útvonalcsillapítás](Geometry-and-Path-Loss-hu)), és a spot időpontjában az E-réteg minden pontjára összegzi **az összes aktív raj tükrös visszaverődési hozzájárulását**, a ZHR-rel súlyozva – ugyanaz a számítás, mint az [égbolt-kupola](Sky-View-hu) **PREV zónáinál**. Az útvonal minden olyan oldalán, amely az összes legalább 15 %-át tartalmazza, a felhő egy **ellipszis**: középpontja a pontok súlyozott átlaga, féltengelyei a szórásuk sajátértékeinek négyzetgyökeinek 1,5-szeresei, nagytengelye a fő sajátvektor mentén fekszik. Ha egyetlen raj sem járul hozzá (csak sporadikus meteorok), a felhők a két klasszikus **hot spot**, szaggatott vonallal rajzolva. A teljes egyenletek a számítási kézikönyv 10. fejezetében találhatók.

## Vezérlők

| Vezérlő | Jelentés |
|---|---|
| **Térkép sugara** | 600–3500 km az Ön állomásától. |
| **Megjelenítendő spotok** | Az utolsó 15 vagy 30 perc, az utolsó óra, az utolsó 3 óra, az utolsó 24 óra. |
| **Táblázat** | A térképen lévő összeköttetések, a legújabb elöl, a sáv színével; a *Felhő* oszlop a fő oldalra eső visszaverődések arányát adja, vagy azt, hogy *sporadikusak*. |
| **Kattintás** | Egy útvonalra vagy táblázatsorra: az összeköttetés kiemelődik, a mező pedig a felhő középpontjának lokátorát, arányát, méretét és tengelyét mutatja. |
