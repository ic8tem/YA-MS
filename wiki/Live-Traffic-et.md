[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · **Eesti** · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Liiklus otse

*Sakk: Otse ja reaalajas andmed › Liiklus otse.*

[![Liiklus otse](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Mida see näitab

Sinu jaamale tsentreeritud **asimuutne kaugustruu kaart** (kaugus keskpunktist = tegelik kaugus, nurk = asimuut) **kogu meteor scatteri liiklusega**, mille on kogunud [Andmete kogumine](Data-Collection-et). Iga side kohta joonistab programm:

- kahe jaama vahelise **trassi** oma sagedusala värvis: 28 MHz pruun, 50 MHz roheline, 70 MHz tsüaansinine, 144 MHz oranž, 222 MHz roosa, 432 MHz violetne;
- trassi otstes olevad kaks **jaama**;
- **pilve**: kuhu koonduvad selle trassi ja selle aja kõige tõenäolisemad meteoorijäljed.

Spotid, mille üks jaam on **kaardist väljas**, jäetakse kõrvale. **Äsja saabunud** spot (mitte vanem kui 3 minutit) **vilgub ühe minuti**, nii et uus aktiivsus torkab kohe silma.

Näita, kes kuulab: riba värvi kolmnurgad märgivad jaamu, mis PSKReporteri järgi võtavad valitud ajaaknas vastu MSK144, FSK441, PSK2K või JTMS režiimis 28, 50, 70, 144 ja 432 MHz sagedusel. Klõps kolmnurgal näitab kutsungit, lokaatorit, režiime ja viimast spotti. Vahekaardi Andmete kogumine MQTT-voog peab olema ühendatud.

Ka PSKReporteri kaardi aktiivsed monitorid: tühjad kolmnurgad jaamadele, mis on pskreporter.info kaardil MSK144, FSK441, PSK2K või JTMS režiimis, kuid pole veel ühtegi spotti vastu võtnud (MQTT saadab ainult jaamu, mis midagi vastu võtavad). YA-MS pärib PSKReporteri päringuteenust üks režiim korraga, iga 3 minuti järel, seega iga režiim uueneb iga 12 minuti järel, nagu teenuse reeglid nõuavad. Klõps kolmnurgal näitab kutsungit, lokaatorit, dekodeerimisprogrammi ja aega, mil monitor oli aktiivne. Vaikimisi sees.

Kaardil kirjutatakse iga spoti mõlema jaama kutsung, üks kord jaama kohta. Projektsioon on valitav: asimuutne (keskel sinu jaam) või Mercator. Veeru Pilv kohtspikker selgitab selle tähendust.

Näidatakse kõigi sagedusalade spotte, ka nende, mida Andmekogumises ei ole valitud (neid ei salvestata). CW-spotte ja liiga lähedaste jaamade vahelisi spotte ei näidata, kui need Andmekogumises ära visatakse.

## Kuidas pilve arvutatakse

Iga spoti jaoks ehitab programm kahe lokaatori vahelise trassi (sama geomeetria nagu sinu enda trassil, vt [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et)) ja liidab spoti ajal E-kihi punkt-punktilt **iga aktiivse meteoorivoolu peegelpeegelduse panused**, kaalutuna selle ZHR-iga – sama arvutus nagu [taevavõlvi](Sky-View-et) **PREV alade** puhul. Igal trassi poolel, kus on vähemalt 15 % kogusummast, on pilv **ellips**: keskpunkt punktide kaalutud keskmises, pooltelgedeks 1,5-kordsed ruutjuured nende hajuvuse omaväärtustest, suur telg piki peamist omavektorit. Kui ükski meteoorivool ei panusta (ainult sporaadilised meteoorid), on pilvedeks kaks klassikalist **hot spoti**, joonistatud katkendjoonega. Täielikud võrrandid on arvutusjuhendi 10. peatükis.

## Juhtnupud

| Juhtnupp | Tähendus |
|---|---|
| **Kaardi raadius** | 600–3500 km sinu jaamast. |
| **Näidatavad spotid** | Viimased 15 või 30 minutit, viimane tund, viimased 3 tundi, viimased 24 tundi. |
| **Tabel** | Kaardil olevad sided, uusimad eespool, sagedusala värvis; *Pilv* annab peegelduste osa põhipoolel või *sporaadilised*. |
| **Klõps** | Trassil või tabeli real: side tõstetakse esile ja kast näitab pilve keskpunkti lokaatorit, selle osa, suurust ja telge. |
