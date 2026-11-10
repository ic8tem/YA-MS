[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · **Lietuvių** · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Eismas realiuoju laiku

*Kortelė: Tiesiogiai ir realiojo laiko duomenys › Eismas realiuoju laiku.*

[![Eismas realiuoju laiku](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ką rodo

**Azimutinis vienodų atstumų žemėlapis**, kurio centras – jūsų stotis (atstumas nuo centro = tikrasis atstumas, kampas = azimutas), su **visu meteor scatter eismu**, surinktu kortelėje [Duomenų rinkimas](Data-Collection-lt). Kiekvienam ryšiui programa piešia:

- **trasą** tarp dviejų stočių jos juostos spalva: 28 MHz ruda, 50 MHz žalia, 70 MHz žydra, 144 MHz oranžinė, 222 MHz rožinė, 432 MHz violetinė;
- dvi **stotis** trasos galuose;
- **debesį**: kur susitelkia labiausiai tikėtini tos trasos ir to laiko meteorų pėdsakai.

Spotai, kurių viena stotis yra **už žemėlapio ribų**, atmetami. **Ką tik atėjęs** spotas (ne senesnis nei 3 minutės) **mirksi vieną minutę**, todėl nauja veikla iš karto krenta į akis.

## Kaip skaičiuojamas debesis

Kiekvienam spotui programa sudaro trasą tarp dviejų lokatorių (ta pati geometrija kaip jūsų trasai, žr. [Geometrija ir slopinimas](Geometry-and-Path-Loss-lt)) ir spoto laiku E sluoksnio taškas po taško susumuoja **kiekvieno aktyvaus srauto veidrodinio atspindžio indėlius**, pasvertus jo ZHR, – tas pats skaičiavimas kaip [dangaus skliauto](Sky-View-lt) **PREV zonų**. Kiekvienoje trasos pusėje, kurioje yra bent 15 % visos sumos, debesis yra **elipsė**: centras – svertiniame taškų vidurkyje, pusašės – 1,5 karto jų išsibarstymo tikrinių verčių kvadratinės šaknys, didžioji ašis – išilgai pagrindinio tikrinio vektoriaus. Kai jokio srauto indėlio nėra (tik sporadiniai meteorai), debesys yra du klasikiniai **hot spot**, piešiami brūkšnine linija. Visos lygtys pateiktos skaičiavimų vadovo 10 skyriuje.

## Valdikliai

| Valdiklis | Reikšmė |
|---|---|
| **Žemėlapio spindulys** | 600–3500 km nuo jūsų stoties. |
| **Rodomi spotai** | Paskutinės 15 arba 30 minučių, paskutinė valanda, paskutinės 3 valandos, paskutinės 24 valandos. |
| **Lentelė** | Ryšiai žemėlapyje, naujausi viršuje, juostos spalva; *Debesis* rodo atspindžių dalį pagrindinėje pusėje arba *sporadiniai*. |
| **Spustelėjimas** | Ant trasos arba lentelės eilutės: ryšys paryškinamas, o langelis rodo debesies centro lokatorių, jo dalį, dydį ir ašį. |
