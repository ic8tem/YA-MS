[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · **Latviešu** · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh)

# Satiksme tiešsaistē

*Cilne: Tiešsaiste un reāllaika dati › Satiksme tiešsaistē.*

[![Satiksme tiešsaistē](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ko tā rāda

**Azimutāla ekvidistanta karte** ar centru tavā stacijā (attālums no centra = patiesais attālums, leņķis = azimuts) ar **visu meteor scatter satiksmi**, ko savākusi [Datu vākšana](Data-Collection-lv). Katram sakaram programma zīmē:

- **trasi** starp abām stacijām tās joslas krāsā: 28 MHz brūna, 50 MHz zaļa, 70 MHz ciāna, 144 MHz oranža, 222 MHz rozā, 432 MHz violeta;
- abas **stacijas** trases galos;
- **mākoni**: vietu, kur koncentrējas šai trasei un šim laikam varbūtīgākās meteoru sliedes.

Spoti, kuru stacija ir **ārpus kartes**, tiek atmesti. **Tikko pienācis** spots (ne vecāks par 3 minūtēm) **mirgo vienu minūti**, lai jaunā aktivitāte uzreiz būtu pamanāma.

## Kā tiek aprēķināts mākonis

Katram spotam programma izveido trasi starp abiem lokatoriem (tā pati ģeometrija kā tavai trasei, sk. [Ģeometrija un vājinājums](Geometry-and-Path-Loss-lv)) un spota laikā E slāņa punktu pa punktam saskaita **katras aktīvās plūsmas spoguļatstarošanas devumus**, svērtus ar tās ZHR – tas pats aprēķins kā [debess velves](Sky-View-lv) **PREV zonām**. Katrai trases pusei, kurā ir vismaz 15 % no kopējā, mākonis ir **elipse**: centrs punktu svērtajā vidējā, pusasis 1,5 reizes lielākas par to izkliedes īpašvērtību kvadrātsaknēm, lielā ass pa galveno īpašvektoru. Ja neviena plūsma nedod devumu (tikai sporādiskie meteori), mākoņi ir divi klasiskie **hot spot**, zīmēti ar raustītu līniju. Pilnie vienādojumi ir aprēķinu rokasgrāmatas 10. nodaļā.

## Vadība

| Vadīkla | Nozīme |
|---|---|
| **Kartes rādiuss** | 600–3500 km no tavas stacijas. |
| **Rādāmie spoti** | Pēdējās 15 vai 30 minūtes, pēdējā stunda, pēdējās 3 stundas, pēdējās 24 stundas. |
| **Tabula** | Sakari kartē, jaunākie pirmie, joslas krāsā; *Mākonis* rāda atstarojumu daļu galvenajā pusē vai *sporādiskie*. |
| **Klikšķis** | Uz trases vai tabulas rindas: sakars tiek izcelts, un lodziņā redzams mākoņa centra lokators, tā daļa, izmērs un ass. |
