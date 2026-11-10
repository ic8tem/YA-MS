[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · **Íslenska** · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – meteor scatter-spár og nýtni loftsteinadrífa í beinni

*eftir Costantino Cerrotta IC8TEM*

**YA-MS** er ókeypis forrit fyrir radíóamatöra sem stunda **meteor scatter (MS) á 50, 70, 144, 222 og 432 MHz**. Fyrir raunverulegu leiðina milli þíns locators og locators mótstöðvarinnar reiknar það klukkustund fyrir klukkustund hve mikið hver virk loftsteinadrífa hjálpar leiðinni (**nýtni** hennar), frá hvorri hlið leiðarinnar endurvörpin koma (**Hot A / Hot B**), hvert beina skal loftnetinu, og tilraunaspá um fjölda endurvarpa á klukkustund, leidda af **loftsteinaratsjá í beinni** (Collm, Þýskalandi). Það keyrir á **Windows, Linux og macOS** (.NET 8 + Avalonia), á 6 viðmótstungumálum.

Aðalheimildin er grein **C. Cerrotta IC8TEM og G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (útgáfa 7). Hver formúla og hvert gagnaatriði í forritinu vísar til heimildar sinnar; sjá [Heimildir](Sources-is).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Himinhvelfing"></a><br><sub>Himinhvelfing</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Útreikningur nýtni"></a><br><sub>Útreikningur nýtni</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES-ratsjá"></a><br><sub>GRAVES-ratsjá</sub></td>
</tr></table>

## Fyrir hverja það er

- Fjarskiptamenn sem vilja vita **hvenær** meteor scatter-leið er opin og **hvert** skal beina loftnetinu, umfram hið almenna „drífan nær hámarki í nótt“.
- Stöðvar sem vinna **langar leiðir á 144 og 432 MHz**, þar sem staða geislapunktsins ræður því hvort drífa er gagnleg eða gagnslaus.
- Alla sem vilja **sannreyna tölurnar**: reiknihandbókin og skýringarnar í forritinu sýna hvert skref ásamt uppruna þess: birta heimild, prófun gerða á forritinu eða val forritsins.

## Fliparnir

Frá útgáfu 1.6 hafa aðalfliparnir **undirflipa** (ljósari röð undir aðalröðinni). Við ræsingu birtist í 5 sekúndur upphafsmynd af Perseítum yfir VLT-sjónauka ESO (ljósmynd ESO/S. Guisard, CC BY 4.0).

| Flipi | Undirflipi | Hvað hann sýnir |
|---|---|---|
| **Beint og rauntímagögn** | [Umferð í beinni](Live-Traffic-is) | Jafnfjarlægðarkort með allri safnaðri MS-umferð, með skýi líklegustu slóðanna fyrir hvert samband, litum eftir tíðnisviði og blikkandi nýjum spotum |
| | [Ratsjárflæði](Radar-Flux-is) | Fjöldi loftsteina á klukkustund og hæð slóða lesin af SKiYMET-ratsjánni í Collm, mynd frá Sodankylä, mat fyrir þitt tíðnisvið |
| | [GRAVES-ratsjá](GRAVES-Radar-is) | Forward scatter-leiðin GRAVES → þú: nýtilegt svæði í geislanum, geiri og skref, næsta yfirferð geislans, hvernig á að hlusta |
| | [Gagnasöfnun](Data-Collection-is) | Þrír telnet-straumar frá klösum (DX cluster, RBN, DM4X/PSKReporter) og sía fyrir MS-spot |
| **Spáreikningur** | [Spáreikningur](Sky-View-is) | Grunnkort leiðarinnar með Hot A / Hot B, loftnetsgeisla, PREV-svæðum og reki drífunnar; listi yfir drífur; lítil himinhvelfing með geislapunktum og réttum loftnetsstefnum; snið séð frá loftnetinu |
| | [Rúmfræði og deyfing](Geometry-and-Path-Loss-is) | Fjarlægð, miðpunktur, hæðarhorn, Hot A / Hot B, mörk sameiginlega svæðisins, leiðardeyfing 28–432 MHz, aflreikningur, loftnet |
| | [Útreikningur nýtni](Efficiency-Calculation-is) | Yfirlitsspjöld, nýtni hverrar drífu klukkustund fyrir klukkustund með hlið A/B, leiðarstuðull, samanburður við DH9GCD, graf |
| | [Tilraunaspár](Experimental-Forecasts-is) | Flæði frá Collm kvarðað í 144 MHz (eða hvaða tíðni sem er) með λ^k og stöðvarstuðli K, spá fyrir 24 klukkustundir, samanburður við RMOB |
| **Tæknileg skjöl** | [Heimildir](Sources-is) | Allar heimildir; sú helsta er grein Cerrotta–Sartori |
| | [Kort af evrópskum ratsjám](European-Radar-Map-is) | Hvar Collm, Sodankylä, GRAVES og CMOR eru miðað við þína stöð |
| | [Nýtni - skýringar](Efficiency-Explanation-is) | Skjal sem sýnir skref fyrir skref hvernig nýtnin er reiknuð, hægt að flytja út í Word |
| [Drífur í beinni](Live-Showers-is) | – | Mælt ZHR frá Global Meteor Network og kort CMOR af geislapunktum |
| [Drífur](Showers-is) | – | Skrá IMO með næsta hámarki (dagsetning og tími IMO eða reiknað) |
| [Reitakort](Grid-Square-Map-is) | – | Unnir og staðfestir Maidenhead-reitir úr ADIF-skrá, einn flipi fyrir hvert tíðnisvið |

Fyrir ofan flipana eru þrjár raðir stýringa (þinn locator, mótstöð, tíðnisvið, loftnet, hæð slóða, tími); sjá [Fyrstu skrefin](Getting-Started-is). Hnappurinn **Stýringar** fellir þær saman, og tungumál og litaþema eru valin efst til hægri; sjá [Stillingar og gagnamappa](Settings-and-Data-Folder-is).

## Í stuttu máli

- **Raunveruleg leið, ekki fastar stefnur**: nýtnin er reiknuð fyrir stórhringsleiðina milli locatoranna tveggja (eldri forrit notuðu fjórar fastar stefnur).
- **Líkan speglunarendurvarps** (McKinley) í punktum E-lagsins á 15 km fresti, með hæð slóða lesinni í beinni af Collm-ratsjánni.
- **Hot A / Hot B** 150 km sitt hvorum megin við miðpunktinn (stillanlegt 30–400 km); sá ráðlagði í rauðu, þeir sem þegar eru innan loftnetsgeislans í gráu.
- **Ratsjá í beinni**: Collm er athuguð á 5 mínútna fresti og aðeins breyttar lindir sóttar aftur; án nettengingar heldur forritið áfram með síðustu vistuðu gögnum.
- **Tilraunaspá** á 50/144/432 MHz með λ³-reglu SM6FHZ, sambærileg við RMOB-athugendur.
- Allt í einni möppu, **`data`**, við hlið forritsins: engin AppData, engar kerfismöppur.

> Nýtnin er tilraunalíkan (speglunarendurvarp + undirþéttar slóðir). Berðu hana saman við MCG_MS, MS-Soft og eigin reynslu í loftinu.

## Hvar á að byrja

1. [Uppsetning](Installation-is)
2. [Fyrstu skrefin](Getting-Started-is)
3. [Úrræðaleit og algengar spurningar](Troubleshooting-FAQ-is) ef eitthvað virkar ekki.

Niðurhal: **[Releases](https://github.com/ic8tem/YA-MS/releases)** á GitHub.
