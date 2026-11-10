[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · **Română** · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – previziuni meteor-scatter și eficiența roiurilor în timp real

*de Costantino Cerrotta IC8TEM*

**YA-MS** este un program gratuit pentru radioamatorii care lucrează în **meteor scatter (MS) pe 50, 70, 144, 222 și 432 MHz**. Pentru traseul real dintre locatorul dumneavoastră și cel al stației DX, calculează oră de oră cât ajută traseul fiecare roi de meteori activ (**eficiența** sa), din ce parte a traseului vin reflexiile (**Hot A / Hot B**), unde să orientați antena și o previziune experimentală a reflexiilor pe oră derivată dintr-un **radar de meteori live** (Collm, Germania). Rulează pe **Windows, Linux, Raspberry Pi și macOS** (.NET 8 + Avalonia), în 6 limbi ale interfeței.

Sursa principală este articolul lui **C. Cerrotta IC8TEM și G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versiunea 7). Fiecare formulă și fiecare dată din program își citează sursa; vedeți [Surse](Sources-ro).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Bolta cerească"></a><br><sub>Bolta cerească</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Calculul eficienței"></a><br><sub>Calculul eficienței</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Pentru cine este

- Operatorii care vor să știe **când** este deschis un traseu meteor-scatter și **unde** să orienteze antena, dincolo de genericul „roiul are maximul în seara asta”.
- Stațiile care lucrează **trasee lungi pe 144 și 432 MHz**, unde poziția radiantului decide dacă un roi este util sau inutil.
- Oricine vrea să **verifice cifrele**: manualul de calcul și explicația din program dau fiecare pas cu originea sa: o sursă publicată, o verificare făcută pe program sau o alegere a programului.

## Filele

Începând cu versiunea 1.6, filele principale au **subfile** (un rând mai deschis sub cel principal). La pornire, un ecran de întâmpinare de 5 secunde arată Perseidele deasupra VLT de la ESO (foto ESO/S. Guisard, CC BY 4.0).

| Filă | Subfilă | Ce arată |
|---|---|---|
| **Date live și în timp real** | [Trafic live](Live-Traffic-ro) | Hartă azimutală a întregului trafic MS colectat, cu un nor al celor mai probabile urme pentru fiecare legătură, culori pe benzi, spoturi noi care clipesc |
| | [Flux radar](Radar-Flux-ro) | Numărul orar de meteori și înălțimea urmelor citite de la radarul SKiYMET din Collm, imaginea de la Sodankylä, estimarea pe banda dumneavoastră |
| | [Radar GRAVES](GRAVES-Radar-ro) | Traseul forward-scatter GRAVES → dumneavoastră: zona utilă din fascicul, sectorul și pasul, următoarea trecere a fasciculului, cum să ascultați |
| | [Colectare date](Data-Collection-ro) | Trei fluxuri de cluster telnet (DX cluster, RBN, DM4X/PSKReporter) și filtrul de spoturi MS |
| **Calcul previzional** | [Calcul previzional](Sky-View-ro) | Hartă în plan a traseului cu Hot A / Hot B, lobul antenei, zonele PREV și deriva roiurilor; lista roiurilor; mică boltă cerească cu radianții și direcțiile corecte ale antenei; secțiunea văzută de la antenă |
| | [Geometrie și atenuare](Geometry-and-Path-Loss-ro) | Distanță, punct median, elevație, Hot A / Hot B, limitele zonei comune, atenuarea pe traseu 28–432 MHz, bilanțul legăturii, antena |
| | [Calculul eficienței](Efficiency-Calculation-ro) | Carduri de sinteză, eficiența orară a fiecărui roi cu latura A/B, indicele traseului, comparația cu DH9GCD, grafic |
| | [Previziuni experimentale](Experimental-Forecasts-ro) | Fluxul de la Collm scalat la 144 MHz (sau orice frecvență) cu λ^k și factorul de stație K, previziune pe 24 de ore, comparația cu RMOB |
| **Documente tehnice** | [Surse](Sources-ro) | Toate sursele; cea principală este articolul Cerrotta–Sartori |
| | [Harta radarelor europene](European-Radar-Map-ro) | Unde se află Collm, Sodankylä, GRAVES și CMOR față de stația dumneavoastră |
| | [Eficiența - explicație](Efficiency-Explanation-ro) | Document pas cu pas despre cum se calculează eficiența, exportabil în Word |
| [Roiuri live](Live-Showers-ro) | – | ZHR măsurat de Global Meteor Network și hărțile radianților CMOR |
| [Roiuri](Showers-ro) | – | Catalogul IMO cu următorul maxim (data și ora IMO sau calculate) |
| [Harta pătratelor](Grid-Square-Map-ro) | – | Pătratele Maidenhead lucrate și confirmate dintr-un fișier ADIF, câte o filă pentru fiecare bandă |

Deasupra filelor sunt trei rânduri de comenzi (locatorul dumneavoastră, stația DX, banda, antena, înălțimea urmei, ora); vedeți [Primii pași](Getting-Started-ro). Butonul **Comenzi** le pliază, iar limba și schema de culori se aleg în dreapta sus; vedeți [Setări și dosarul de date](Settings-and-Data-Folder-ro).

## Pe scurt

- **Traseu real, nu direcții fixe**: eficiența se calculează pentru traseul pe cercul mare dintre cei doi locatori (programele mai vechi foloseau patru direcții fixe).
- **Model de reflexie speculară** (McKinley) în puncte ale stratului E la fiecare 15 km, cu înălțimea urmei citită live de la radarul din Collm.
- **Hot A / Hot B** la 150 km de o parte și de alta a punctului median (reglabil 30–400 km), cel recomandat în roșu, cele aflate deja în lobul antenei dumneavoastră în gri.
- **Radar live**: Collm verificat la fiecare 5 minute, se descarcă din nou doar sursele modificate; fără conexiune, programul continuă să funcționeze cu ultimele date salvate.
- Previziune **experimentală** la 50/144/432 MHz cu regula λ³ a lui SM6FHZ, comparabilă cu observatorii RMOB.
- Totul într-un singur dosar **`data`** lângă program: fără AppData, fără dosare de sistem.

> Eficiența este un model experimental (reflexie speculară + urme subdense). Comparați-o cu MCG_MS, MS-Soft și cu propria experiență în eter.

## De unde să începeți

1. [Instalare](Installation-ro)
2. [Primii pași](Getting-Started-ro)
3. [Rezolvarea problemelor și întrebări frecvente](Troubleshooting-FAQ-ro) dacă ceva nu funcționează.

Descărcări: **[Releases](https://github.com/ic8tem/YA-MS/releases)** pe GitHub.
