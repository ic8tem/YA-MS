[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · **Français** · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-BR) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-TW)

# YA-MS – prévisions meteor scatter et efficacité des essaims en direct

*par Costantino Cerrotta IC8TEM*

**YA-MS** est un programme gratuit destiné aux radioamateurs qui pratiquent le **meteor scatter (MS) sur 50, 70, 144, 222 et 432 MHz**. Pour le trajet réel entre votre locator et celui du correspondant, il calcule heure par heure dans quelle mesure chaque essaim météorique actif favorise le trajet (son **efficacité**), de quel côté du trajet arrivent les réflexions (**Hot A / Hot B**), où pointer l'antenne, ainsi qu'une prévision expérimentale des réflexions par heure tirée d'un **radar météorique en direct** (Collm, Allemagne). Il fonctionne sous **Windows, Linux, Raspberry Pi et macOS** (.NET 8 + Avalonia), avec une interface en 36 langues.

La source principale est l'article de **C. Cerrotta IC8TEM et G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (version 7). Chaque formule et chaque donnée du programme cite sa source ; voir [Sources](Sources-fr).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Voûte céleste"></a><br><sub>Voûte céleste</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Calcul de l'efficacité"></a><br><sub>Calcul de l'efficacité</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## À qui il s'adresse

- Aux opérateurs qui veulent savoir **quand** un trajet meteor scatter est ouvert et **où** pointer, au-delà du vague « l'essaim culmine ce soir ».
- Aux stations qui travaillent des **trajets longs sur 144 et 432 MHz**, où la position du radiant décide si un essaim est utile ou inutile.
- À tous ceux qui veulent **vérifier les chiffres** : le manuel de calcul et l'explication intégrée au programme donnent chaque étape avec son origine : une source publiée, une vérification faite sur le programme ou un choix du programme.

## Les onglets

Depuis la version 1.6, les onglets principaux comportent des **sous-onglets** (une rangée plus claire sous la rangée principale). Au démarrage, un écran d'accueil de 5 secondes montre les Perséides au-dessus du VLT de l'ESO (photo ESO/S. Guisard, CC BY 4.0).

| Onglet | Sous-onglet | Ce qu'il montre |
|---|---|---|
| **Direct et données en temps réel** | [Trafic en direct](Live-Traffic-fr) | Carte azimutale de tout le trafic MS collecté, avec un nuage des traînées les plus probables pour chaque liaison, couleurs par bande, nouveaux spots clignotants |
| | [Flux radar](Radar-Flux-fr) | Comptages horaires de météores et altitudes des traînées lus sur le radar SKiYMET de Collm, image de Sodankylä, estimation sur votre bande |
| | [Radar GRAVES](GRAVES-Radar-fr) | Le trajet en diffusion vers l'avant GRAVES → vous : zone utile dans le faisceau, secteur et pas, prochain passage du faisceau, comment écouter |
| | [Collecte de données](Data-Collection-fr) | Trois flux de cluster telnet (DX cluster, RBN, DM4X/PSKReporter) et le filtre des spots MS |
| **Calcul prévisionnel** | [Calcul prévisionnel](Sky-View-fr) | Plan du trajet avec Hot A / Hot B, lobe d'antenne, zones PREV et déplacement des essaims ; liste des essaims ; petite voûte céleste avec les radiants et les bonnes directions d'antenne ; coupe vue depuis l'antenne |
| | [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr) | Distance, point milieu, élévation, Hot A / Hot B, limites de la zone commune, affaiblissement de trajet 28–432 MHz, bilan de liaison, antenne |
| | [Calcul de l'efficacité](Efficiency-Calculation-fr) | Cartes de synthèse, efficacité horaire de chaque essaim avec côté A/B, indice du trajet, comparaison DH9GCD, graphique |
| | [Prévisions expérimentales](Experimental-Forecasts-fr) | Flux de Collm transposé à 144 MHz (ou à toute fréquence) avec λ^k et facteur de station K, prévision sur 24 heures, comparaison RMOB |
| **Documents techniques** | [Sources](Sources-fr) | Toutes les sources ; la principale est l'article Cerrotta–Sartori |
| | [Carte des radars européens](European-Radar-Map-fr) | Où se trouvent Collm, Sodankylä, GRAVES et CMOR par rapport à votre station |
| | [Efficacité - explication](Efficiency-Explanation-fr) | Document pas à pas sur la façon dont l'efficacité est calculée, exportable vers Word |
| [Essaims en direct](Live-Showers-fr) | – | ZHR mesurés par le Global Meteor Network et cartes des radiants CMOR |
| [Essaims](Showers-fr) | – | Catalogue IMO avec le prochain maximum (date et heure IMO ou calculées) |
| [Carte des carrés](Grid-Square-Map-fr) | – | Carrés Maidenhead contactés et confirmés à partir d'un fichier ADIF, un onglet par bande |

Au-dessus des onglets se trouvent trois rangées de commandes (votre locator, correspondant, bande, antenne, altitude des traînées, heure) ; voir [Premiers pas](Getting-Started-fr). Le bouton **Commandes** les replie, et la langue ainsi que le schéma de couleurs se choisissent en haut à droite ; voir [Réglages et dossier des données](Settings-and-Data-Folder-fr).

## En bref

- **Trajet réel, pas de directions fixes** : l'efficacité est calculée pour le trajet orthodromique entre les deux locators (les programmes plus anciens utilisaient quatre directions fixes).
- **Modèle de réflexion spéculaire** (McKinley) sur des points de la couche E tous les 15 km, avec l'altitude des traînées lue en direct sur le radar de Collm.
- **Hot A / Hot B** à 150 km de part et d'autre du point milieu (réglable de 30 à 400 km), le hot spot conseillé en rouge, ceux déjà compris dans le lobe de votre antenne en gris.
- **Radar en direct** : Collm vérifié toutes les 5 minutes, seules les sources modifiées sont retéléchargées ; hors ligne, le programme continue de fonctionner avec les dernières données enregistrées.
- Prévision **expérimentale** à 50/144/432 MHz avec la règle λ³ de SM6FHZ, comparable aux observateurs RMOB.
- Tout se trouve dans un seul dossier **`data`** à côté du programme : pas d'AppData, pas de dossiers système.

> L'efficacité est un modèle expérimental (réflexion spéculaire + traînées sous-denses). Comparez-la avec MCG_MS, MS-Soft et votre propre expérience sur l'air.

## Par où commencer

1. [Installation](Installation-fr)
2. [Premiers pas](Getting-Started-fr)
3. [Dépannage et FAQ](Troubleshooting-FAQ-fr) si quelque chose ne fonctionne pas.

Téléchargements : **[Releases](https://github.com/ic8tem/YA-MS/releases)** sur GitHub.
