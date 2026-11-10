[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · **Română** · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – prognoze meteor scatter și eficiența roiurilor în direct

*realizat de Costantino Cerrotta IC8TEM*

**YA-MS** este un program gratuit pentru radioamatorii care lucrează **meteor scatter (MS) pe 50, 70, 144, 222 și 432 MHz**. Pentru traseul real dintre locatorul tău și cel al corespondentului, calculează oră de oră cât ajută traseul fiecare roi de meteori activ (**eficiența** lui), din ce parte a traseului sosesc reflexiile (**Hot A / Hot B**), unde să orientezi antena și o prognoză experimentală a reflexiilor pe oră, derivată dintr-un **radar meteoric în direct** (Collm, Germania). Rulează pe **Windows, Linux și macOS** (.NET 8 + Avalonia), cu interfața în 36 de limbi.

Sursa principală este articolul lui **C. Cerrotta IC8TEM și G. Sartori IV3GTH**, *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese”* (versiunea 7). Fiecare formulă și fiecare dată din program își citează sursa; vezi [Surse](Sources-ro).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Bolta cerească"></a><br><sub>Bolta cerească</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Calculul eficienței"></a><br><sub>Calculul eficienței</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Cui se adresează

- Operatorilor care vor să știe **când** este deschis un traseu meteor scatter și **unde** să orienteze antena, dincolo de genericul „roiul are maximul în seara asta”.
- Stațiilor care lucrează **trasee lungi pe 144 și 432 MHz**, unde poziția radiantului decide dacă un roi este util sau inutil.
- Oricui vrea să **verifice cifrele**: manualul de calcul și explicația din program dau fiecare pas cu originea lui: o sursă publicată, o verificare făcută pe program sau o alegere a programului.

## Filele

Începând cu versiunea 1.6, filele principale au **sub-file** (un rând mai deschis sub cel principal). La pornire, un ecran de deschidere de 5 secunde arată Perseidele deasupra VLT-ului ESO (foto ESO/S. Guisard, CC BY 4.0).

| Filă | Sub-filă | Ce arată |
|---|---|---|
| **Live și date în timp real** | [Trafic în direct](Live-Traffic-ro) | Hartă azimutală a întregului trafic MS colectat, cu un nor al urmelor celor mai probabile pentru fiecare legătură, culori pe benzi, spoturile noi clipind |
| | [Flux radar](Radar-Flux-ro) | Numărătorile orare ale meteorilor și altitudinile urmelor citite de la radarul SKiYMET din Collm, imaginea de la Sodankylä, estimarea pentru banda ta |
| | [Radar GRAVES](GRAVES-Radar-ro) | Traseul forward-scatter GRAVES → tu: zona utilă în fascicul, sectorul și pasul, următoarea trecere a fasciculului, cum se ascultă |
| | [Colectare date](Data-Collection-ro) | Trei fluxuri telnet de cluster (DX cluster, RBN, DM4X/PSKReporter) și filtrul spoturilor MS |
| **Calcul previzional** | [Calcul previzional](Sky-View-ro) | Harta în plan a traseului cu Hot A / Hot B, lobul antenei, zonele PREV și deplasarea roiului; lista roiurilor; bolta cerească mică cu radianții și direcțiile corecte ale antenei; secțiunea văzută de antenă |
| | [Geometrie și atenuare](Geometry-and-Path-Loss-ro) | Distanța, punctul median, elevația, Hot A / Hot B, limitele zonei comune, atenuarea 28–432 MHz, bilanțul legăturii, antena |
| | [Calculul eficienței](Efficiency-Calculation-ro) | Casete de sinteză, eficiența orară a fiecărui roi cu latura A/B, indicele traseului, comparația DH9GCD, grafic |
| | [Implementare experimentală a prognozelor](Experimental-Forecasts-ro) | Fluxul Collm transpus la 144 MHz (sau la orice frecvență) cu λ^k și factorul stației K, prognoza pe 24 de ore, comparația RMOB |
| **Documente tehnice** | [Surse](Sources-ro) | Toate sursele; cea principală este articolul Cerrotta–Sartori |
| | [Harta radarelor europene](European-Radar-Map-ro) | Unde se află Collm, Sodankylä, GRAVES și CMOR față de stația ta |
| | [Eficiență - explicație](Efficiency-Explanation-ro) | Document pas cu pas despre cum se calculează eficiența, exportabil în Word |
| [Roiuri în direct](Live-Showers-ro) | – | ZHR măsurate de Global Meteor Network și hărțile radianților CMOR |
| [Roiuri](Showers-ro) | – | Catalogul IMO cu următorul maxim (data și ora IMO sau calculate) |
| [Harta pătratelor](Grid-Square-Map-ro) | – | Pătratele Maidenhead lucrate și confirmate dintr-un fișier ADIF, câte o filă pe bandă |

Deasupra filelor sunt trei rânduri de comenzi (locatorul tău, corespondentul, banda, antena, altitudinea urmelor, ora); vezi [Primii pași](Getting-Started-ro). Butonul **Comenzi** le pliază, iar limba și schema de culori se aleg în dreapta sus; vezi [Setări și dosarul de date](Settings-and-Data-Folder-ro).

## Pe scurt

- **Traseu real, nu direcții fixe**: eficiența se calculează pentru traseul pe cercul mare dintre cei doi locatori (programele mai vechi foloseau patru direcții fixe).
- **Model de reflexie speculară** (McKinley) pe puncte ale stratului E la fiecare 15 km, cu altitudinea urmelor citită în direct de la radarul Collm.
- **Hot A / Hot B** la 150 km de o parte și de alta a punctului median (reglabil 30–400 km), cel recomandat cu roșu, cele aflate deja în lobul antenei tale cu gri.
- **Radar în direct**: Collm verificat la fiecare 5 minute, se descarcă din nou doar sursele modificate; fără conexiune, programul continuă să lucreze cu ultimele date salvate.
- Prognoză **experimentală** la 50/144/432 MHz cu regula λ³ a lui SM6FHZ, comparabilă cu observatorii RMOB.
- Totul într-un singur dosar **`data`** lângă program: fără AppData, fără dosare de sistem.

> Eficiența este un model experimental (reflexie speculară + urme subdense). Compar-o cu MCG_MS, MS-Soft și cu propria experiență în trafic.

## De unde să începi

1. [Instalare](Installation-ro)
2. [Primii pași](Getting-Started-ro)
3. [Depanare și întrebări frecvente](Troubleshooting-FAQ-ro) dacă ceva nu funcționează.

Descărcări: **[Releases](https://github.com/ic8tem/YA-MS/releases)** pe GitHub.
