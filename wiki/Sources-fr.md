[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · **Français** · [Español](Sources-es) · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-br) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-tw)

# Sources

*Onglet : Documents techniques › Sources.*

[![Sources](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

L'onglet **Sources** énumère tous les travaux sur lesquels repose YA-MS, regroupés comme ci-dessous (le texte est sélectionnable, vous pouvez donc copier les références). Les mêmes sources, numérotées, terminent le manuel de calcul (`doc/YA-MS_manuale_calcoli.docx`) et le document [Efficacité - explication](Efficiency-Explanation-fr).

## SOURCE PRINCIPALE

| Source | Utilisée pour |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (article en italien, version 7) | Traînées dans la couche E vers 90 km (radar SKiYMET), rayon terrestre 6372,7955 km, formule de l'élévation, Hot A / Hot B, side-scatter de 10–30°, affaiblissement de trajet, signal minimal −130 dBm, durées des pings IARU, maximum des sporadiques à 06 UTC |

## CALCUL ET THÉORIE DE L'EFFICACITÉ

| Source | Utilisée pour |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (site historique) | Concept d'efficacité d'un essaim ; affaiblissement moyen de 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Efficacité sur quatre directions fixes (comparaison) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45e Nordic VUSHF, mai 2025 | Règles λ³ et λ², point milieu, meilleure direction (az du radiant ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Réflexion spéculaire, équation des traînées sous-denses |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (d'après Kaiser & Closs 1952) | Affaiblissement de trajet de 172–190 dB calculé par John Worsnop **G4BAO** (thèse de doctorat), environ 6 dB de moins pour les traînées alignées avec le trajet ; le tableau de 182 dB de la page elle-même n'est pas utilisé (voir [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tableau des décalages de l'AMS Bulletin 203) | Élévation et décalage optimaux, hot spots à 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (comparaison ; dans le manuel) |
| Klaus von der Heide **DJ5HG** – QTFGUI et le manuel "QTFGUI Help" (2007) | Loi de diffusion en cône ; cas d'essai Hambourg – Barcelone dans les Quadrantides, utilisé pour vérifier le modèle |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, conférence DARC, janvier 2018 | Formule de la meilleure direction de **DH9GCD** ; diffusion en cône et choix HOT-A / HOT-B de DJ5HG ; radiant utile entre 20 et 70° ; meilleure distance 1300–1500 km ; météores sporadiques selon KB0VUK |
| Günter Hoch **DL6WU** – gain en fonction de la longueur de boom des Yagi longues, rapporté par W8IO (w8io.com) | G(dBi) = 7,773 log(L/λ) + 11,43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data* ; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design* ; *70-CM Yagi Stacks Part 2* (Yagi VK3AUU de David Tanner) | Simulations NEC utilisées pour vérifier la courbe de gain et corriger le lobe horizontal (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Estimations du gain pour les variantes VK3AUU, WA2PHW et DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2e éd., Willmann-Bell, 1998 | Jour julien, temps sidéral, longitude solaire, azimut/élévation (dans le manuel) |

## DONNÉES DES ESSAIMS

| Source | Utilisée pour |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (et 2027), www.imo.net, tableaux 5, 6 et 7 | Radiants, λ max, v, r, ZHR, Source de l'antihélion, dates et heures des maxima |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Données des essaims |

## DONNÉES RADAR EN DIRECT

| Source | Utilisée pour |
|---|---|
| Radar météorique de Collm, Université de Leipzig (LIM) et IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Flux horaire de météores et altitudes des traînées ([Flux radar](Radar-Flux-fr)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Image des comptages de météores |
| DL1DBC – Swan Meteor Skyview, swan.ms | Référence pour le graphisme de la voûte céleste |
| SM6FHZ – RadiantCalc | Graphique polaire avec la meilleure direction |
| Natural Earth – côtes et frontières au 1:50 millions, domaine public, www.naturalearthdata.com | Carte d'Europe |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org ; bulletins mensuels rmob.org/rmobtext | Observateurs de GRAVES sur 143,050 MHz (Planétarium de Venise, Faenza, Rovereto et d'autres) pour comparaison |

## RADAR GRAVES

| Source | Utilisée pour |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) et *"Graves Radar Update April 2021"* – pe1itr.com/graves | Secteurs, pas, durée des pas de 0,8 s / 3,2 s |
| Wiki Bolidozor, "Graves" | Réseaux, secteurs et temporisation du faisceau |
| Wikipedia, "GRAVES (system)" | Émetteur à Broye-lès-Pesmes (47,348° N 5,515° E) |

Voir [Radar GRAVES](GRAVES-Radar-fr).

## AUTRES RÉFÉRENCES DE L'ARTICLE

G3WZT, DH8BQA, geekshed.co.uk, manuel de WSJT-X, WB2FKO (pings), IU6GIR (activité sur 143,050 MHz), IARU Région 1 VHF Handbook.

## Constantes et leur source

`data/regole_sperimentali.csv` énumère les constantes et les règles utilisées par le programme, chacune avec sa source (altitude typique des traînées, plage d'altitudes, rayon terrestre, règles λ³ / λ², durées des pings IARU, affaiblissements de trajet, signal minimal, PIRE indicative, maximum des sporadiques, distances utiles à 432 MHz, meilleure direction, élévation maximale utile du radiant à 432 MHz, side-scatter).

> Les données radar appartiennent à leurs institutions. Il faut demander l'autorisation avant de les récupérer automatiquement dans un programme diffusé.
