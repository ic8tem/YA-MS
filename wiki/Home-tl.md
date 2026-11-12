[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · **Tagalog** · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – pagtataya ng meteor scatter at live na episyensya ng mga meteor shower

*inihanda ni Costantino Cerrotta IC8TEM*

Ang **YA-MS** ay isang libreng programa para sa mga radio amateur na gumagawa ng **meteor scatter (MS) sa 50, 70, 144, 222 at 432 MHz**. Para sa totoong landas sa pagitan ng iyong locator at ng locator ng DX station, kinakalkula nito bawat oras kung gaano nakatutulong ang bawat aktibong meteor shower sa landas (ang **episyensya** nito), mula sa aling panig ng landas dumarating ang mga repleksiyon (**Hot A / Hot B**), saan itututok ang antenna, at isang eksperimental na pagtataya ng mga repleksiyon bawat oras na hinango mula sa isang **live na meteor radar** (Collm, Germany). Tumatakbo ito sa **Windows, Linux, Raspberry Pi at macOS** (.NET 8 + Avalonia), sa 36 na wika ng interface.

Ang pangunahing sanggunian ay ang artikulo nina **C. Cerrotta IC8TEM at G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (bersyon 7). Bawat pormula at datos sa programa ay may binabanggit na sanggunian; tingnan ang [Mga sanggunian](Sources-tl).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Kalangitan"></a><br><sub>Kalangitan (sky dome)</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Kalkulasyon ng episyensya"></a><br><sub>Kalkulasyon ng episyensya</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Para kanino ito

- Mga operator na gustong malaman **kailan** bukas ang isang landas na meteor scatter at **saan** itututok, higit pa sa pangkalahatang "mamayang gabi ang peak ng shower".
- Mga istasyong gumagawa ng **mahahabang landas sa 144 at 432 MHz**, kung saan ang posisyon ng radiant ang nagpapasya kung kapaki-pakinabang o walang silbi ang isang shower.
- Sinumang gustong **suriin ang mga numero**: ibinibigay ng manwal ng kalkulasyon at ng paliwanag sa loob ng programa ang bawat hakbang kasama ang pinagmulan nito: isang nailathalang sanggunian, isang pagsusuring ginawa sa programa, o isang pagpili ng programa.

## Ang mga tab

Mula bersyon 1.6, may mga **sub-tab** ang mga pangunahing tab (isang mas mapusyaw na hanay sa ilalim ng pangunahin). Sa pagsisimula, isang 5-segundong splash screen ang nagpapakita ng Perseids sa ibabaw ng VLT ng ESO (larawan ESO/S. Guisard, CC BY 4.0).

| Tab | Sub-tab | Ano ang ipinapakita |
|---|---|---|
| **Live at real-time na datos** | [Live na trapiko](Live-Traffic-tl) | Azimuthal na mapa ng lahat ng nakolektang trapikong MS, may ulap ng pinakamalamang na bakas para sa bawat contact, kulay ayon sa banda, at kumikislap na bagong spot |
| | [Flux ng radar](Radar-Flux-tl) | Bilang ng meteor bawat oras at taas ng mga bakas na binasa mula sa SKiYMET radar ng Collm, larawan ng Sodankylä, tantiya para sa iyong banda |
| | [Radar GRAVES](GRAVES-Radar-tl) | Ang forward-scatter na landas na GRAVES → ikaw: magagamit na sona sa beam, sektor at hakbang, susunod na pagdaan ng beam, paano makinig |
| | [Pangongolekta ng data](Data-Collection-tl) | Tatlong telnet stream ng cluster (DX cluster, RBN, DM4X/PSKReporter) at ang filter ng mga MS spot |
| **Kalkulasyon ng pagtataya** | [Kalkulasyon ng pagtataya](Sky-View-tl) | Planong mapa ng landas na may Hot A / Hot B, lobe ng antenna, mga PREV na sona at pag-usad ng shower; listahan ng mga shower; maliit na kalangitan na may mga radiant at ang tamang direksiyon ng antenna; seksiyong nakikita mula sa antenna |
| | [Heometriya at path loss](Geometry-and-Path-Loss-tl) | Distansiya, gitnang punto, elebasyon, Hot A / Hot B, mga hangganan ng karaniwang sona, path loss 28–432 MHz, link budget, antenna |
| | [Kalkulasyon ng episyensya](Efficiency-Calculation-tl) | Mga card na mabilisang tingnan, episyensya bawat oras ng bawat shower na may panig A/B, indeks ng landas, paghahambing sa DH9GCD, graph |
| | [Eksperimental na pagtataya](Experimental-Forecasts-tl) | Flux ng Collm na iniskala sa 144 MHz (o anumang frequency) gamit ang λ^k at station factor K, pagtataya sa 24 na oras, paghahambing sa RMOB |
| [Mga live na shower](Live-Showers-tl) | – | Sinukat na ZHR ng Global Meteor Network at mga mapa ng radiant ng CMOR |
| [Mga shower](Showers-tl) | – | Katalogo ng IMO na may susunod na peak (petsa at oras ng IMO o kinalkula) |
| [Mapa ng grid square](Grid-Square-Map-tl) | – | Mga nakontak at kumpirmadong Maidenhead grid square mula sa isang ADIF file, isang tab bawat banda |
| **Mga teknikal na dokumento** | [Mga sanggunian](Sources-tl) | Lahat ng sanggunian; ang pangunahin ay ang artikulong Cerrotta–Sartori |
| | [Mapa ng mga radar sa Europa](European-Radar-Map-tl) | Kung nasaan ang Collm, Sodankylä, GRAVES at CMOR kaugnay ng iyong istasyon |
| | [Episyensya - paliwanag](Efficiency-Explanation-tl) | Hakbang-hakbang na dokumento kung paano kinakalkula ang episyensya, maaaring i-export sa Word |

Sa itaas ng mga tab ay may tatlong hanay ng mga kontrol (ang iyong locator, DX station, banda, antenna, taas ng bakas, oras); tingnan ang [Pagsisimula](Getting-Started-tl). Itinitiklop ang mga ito ng button na **Mga kontrol**, at pinipili sa kanang itaas ang wika at scheme ng kulay; tingnan ang [Mga setting at folder ng datos](Settings-and-Data-Folder-tl).

## Sa madaling salita

- **Totoong landas, hindi nakapirming direksiyon**: kinakalkula ang episyensya para sa great-circle na landas sa pagitan ng dalawang locator (apat na nakapirming direksiyon ang gamit ng mas lumang mga programa).
- **Modelo ng specular na repleksiyon** (McKinley) sa mga punto ng E layer bawat 15 km, na ang taas ng bakas ay live na binabasa mula sa radar ng Collm.
- **Hot A / Hot B** 150 km sa magkabilang panig ng gitnang punto (naaayos sa 30–400 km), pula ang inirerekomenda, kulay abo ang mga nasa loob na ng lobe ng iyong antenna.
- **Live na radar**: sinusuri ang Collm bawat 5 minuto, at ang mga nagbagong sanggunian lamang ang muling dina-download; kapag offline, patuloy na gumagana ang programa gamit ang huling na-save na datos.
- **Eksperimental** na pagtataya sa 50/144/432 MHz gamit ang λ³ na tuntunin ni SM6FHZ, maihahambing sa mga RMOB observer.
- Lahat ay nasa iisang **`data`** folder katabi ng programa: walang AppData, walang system folder.

> Eksperimental na modelo ang episyensya (specular na repleksiyon + underdense na bakas). Ihambing ito sa MCG_MS, MS-Soft at sa sarili mong karanasan sa ere.

## Saan magsisimula

1. [Pag-install](Installation-tl)
2. [Pagsisimula](Getting-Started-tl)
3. [Pag-troubleshoot at FAQ](Troubleshooting-FAQ-tl) kung may hindi gumagana.

Mga download: **[Releases](https://github.com/ic8tem/YA-MS/releases)** sa GitHub.
