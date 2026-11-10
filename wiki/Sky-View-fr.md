[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · **Français** · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Voûte céleste

*Onglet : Calcul prévisionnel › Calcul prévisionnel.*

[![Voûte céleste](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ce sous-onglet (la voûte céleste des versions précédentes) réunit sur un seul écran **où** se trouvent en ce moment les traînées utiles et **où pointer**. À gauche, la **vue en plan** du trajet ; à droite, la liste des essaims, une petite voûte céleste avec les radiants, le texte du calcul et la **coupe** vue depuis votre antenne. Tout se rapporte à l'instant choisi avec *Date du calcul (UTC)* et le curseur *Heures (de −12 à +36 h)* (temps réel par défaut, par pas de 15 minutes).

Un **bandeau au-dessus de la vue en plan** résume le calcul pour cet instant : date et heure (*maintenant* ou nombre d'heures par rapport à maintenant), l'**indice du trajet Σ ZHR×η**, l'**essaim le plus utile** avec son ZHR et son efficacité (aussi en dB par rapport à la référence DJ5HG, voir [Calcul de l'efficacité](Efficiency-Calculation-fr)), le nombre d'essaims au-dessus de l'horizon et le **Hot conseillé** avec son azimut.

Dans la petite voûte céleste, une **ligne orange** passant par le zénith donne toujours les **bonnes directions d'antenne**, orthogonales au déplacement de l'essaim sélectionné (ou du plus favorable) : azimut du radiant ±90°, avec l'étiquette *antenne NNN°* aux deux extrémités et la tolérance de ±45° en traits fins. De petits traits orange sur le bord indiquent les directions orthogonales des autres essaims utiles.

## Vue en plan (à gauche)

Une carte de l'Europe vue de dessus (**E à droite**) avec une graduation en degrés tout autour. La légende sous la carte en donne le rayon (*Carte : bord = … km de la station*).

| Élément | Représentation |
|---|---|
| Trajet / DX | Ligne verte de votre station au correspondant (toujours le trajet orthodromique réel entre les locators) |
| **Hot A / Hot B** | Points de part et d'autre du point milieu, perpendiculairement au trajet, à la distance donnée par le tableau des décalages AMS (ou saisie à la main). **Rouge = conseillé**, **rose = hors du lobe de l'antenne**, **gris = dans le lobe** (avec un avertissement) |
| Lobe de l'antenne | Le lobe horizontal à −3 dB autour de l'azimut de l'antenne (antenne toujours pointée vers le correspondant), étiqueté *lobe …°* |
| Limites de la zone commune | Points pâles *lim. A* / *lim. B* et les deux cercles où l'horizon de chaque station rencontre la couche E (voir [Géométrie](Geometry-and-Path-Loss-fr#limites-de-la-zone-commune)) |
| Déplacement de l'essaim | **Ligne jaune** : direction dans laquelle l'essaim sélectionné (ou le plus favorable) balaie le ciel, c'est-à-dire l'azimut du radiant |
| Meilleurs pointages | **Points orange** : les deux directions perpendiculaires au déplacement (azimut du radiant ±90°, SM6FHZ) |
| **Zones PREV** | Ellipses claires : là où tombent **en ce moment** les traînées les plus probables, une de chaque côté du trajet |

Les étiquettes ne se chevauchent pas : Hot A et PREV A sont écrits à gauche du trajet, B à droite. La **Légende** est une colonne repliable à droite de la carte.

**Souris sur la carte :** **clic gauche = locator du correspondant**, **clic droit = locator de ma station**. Le trajet est recalculé immédiatement.

Options au-dessus de la liste des essaims : **Directions Hot A / Hot B**, **Carte d'Europe** (Natural Earth, téléchargée dans `data/mappa` au premier démarrage), **Vue de dessus (E à droite)**.

### Hot conseillé

Pour l'heure affichée, le programme additionne sur tous les essaims au-dessus de l'horizon le poids ZHR × efficacité, réparti entre le côté A (fraction f_A) et le côté B. Le côté dont le poids est le plus grand donne le Hot conseillé, dessiné en rouge :

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Choix du programme (manuel, éq. 23).* Origine de l'idée : DJ5HG, rapporté par DF5HC (conférence DARC 2018) – selon la position du radiant, l'un des deux points, HOT-A ou HOT-B, est plus favorable. Tourner de 10–30° vers ce côté (side-scatter) vient de l'article Cerrotta–Sartori.

### Zones PREV

Pour chaque point P de la couche E, on additionne les contributions à l'efficacité de tous les essaims actifs (même condition spéculaire que pour l'[efficacité](Efficiency-Calculation-fr#le-modèle)), pondérées par le ZHR. Les points qui atteignent au moins 3 % du maximum forment les zones PREV ; chacune est dessinée comme une ellipse dont le centre est la moyenne pondérée des points et dont les axes valent deux fois leur dispersion.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Choix du programme (manuel, éq. 34).* C'est la règle pratique : si l'essaim balaie du nord au sud, les traînées utiles tombent à l'est et à l'ouest.

## Liste des essaims (en haut à droite)

| Colonne | Signification |
|---|---|
| Essaim, Code | Nom et code IMO |
| ZHR maintenant | Activité à cet instant (ZHR IMO au maximum avec le profil d'activité) |
| Azimut, Élév. | Position du radiant vue de votre station |
| Effic. % | Efficacité de l'essaim pour ce trajet |
| Côté | A ou B, le côté d'où arrive la majorité des réflexions |
| Meilleur point. | Azimut du radiant ±90° |
| Lever, Coucher | Lever et coucher du radiant (UTC) ; *circumpolaire* ou *toujours en dessous* le cas échéant |

Cliquez sur une ligne pour sélectionner l'essaim : la ligne jaune de déplacement et les points orange le suivent.

## Petite voûte céleste (au milieu à droite)

Les radiants sur une voûte céleste vue de votre station, avec leur **code IMO** et leur **parcours quotidien en cyan** (heures UTC). **Cliquez sur un radiant** pour le sélectionner. Couleurs :

| Couleur | Signification |
|---|---|
| Jaune | efficacité ≥ 50 % et ZHR ≥ 2 |
| Orange | efficacité ≥ 20 % |
| Rouge foncé | efficacité < 20 % |
| Gris | presque inactif |

À côté, le texte du calcul : longueur et azimut du trajet, point milieu et son élévation, azimuts et décalages de Hot A / Hot B, le Hot conseillé (*… conseillé maintenant : az. …° (…% des réflexions prévues)*), les limites de la zone commune et le rappel : *meilleur pointage pour l'essaim : PERPENDICULAIRE à la direction d'arrivée (azimut du radiant ±90°, tolérance ±40–50°, SM6FHZ)*.

## Coupe (en bas à droite)

*COUPE – les traînées les plus probables vues de l'antenne vers le correspondant.* En abscisse, l'**azimut par rapport au correspondant** (← A à gauche, B → à droite), en ordonnée l'**élévation**. Pour chaque essaim, on retient les 14 points de réflexion les plus forts ; chaque traînée est un segment orienté vers le radiant, de 10 km au-dessus à 10 km au-dessous de l'altitude des traînées (60 km au plus de chaque côté), d'autant plus épais qu'elle est probable. Sont aussi dessinés : le lobe de l'antenne (cercle à −3 dB autour de l'élévation du lobe), le correspondant et Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Choix du programme (manuel, éq. 35).*

## Avertissements

| Avertissement | Quand |
|---|---|
| **ATTENTION : Hot A (et/ou Hot B) est dans le lobe de l'antenne …** | Le hot spot se trouve à ±θ/2 de l'azimut de l'antenne (θ = lobe horizontal à −3 dB) : avec ce pointage, il est déjà couvert. Affiché en gris sur la carte. Le Hot conseillé reste rouge. |
| **RADIANT TROP HAUT (au-dessus de 70°)** | Un radiant utile est à plus de 70° vu de votre station : les traînées descendent presque verticalement et réfléchissent peu vers le trajet (DF5HC, DH9GCD). Les mêmes heures sont marquées ↑ dans le [tableau horaire](Efficiency-Calculation-fr#tableau-horaire). |
| **RADIANT BAS LE LONG DU TRAJET** | Un radiant actif est sous 20° et à moins de 30° de la direction du trajet. L'efficacité calculée reste faible (prudente), mais DJ5HG s'attend à des réflexions rares et fortes de traînées rasantes alignées avec le trajet (Hambourg–Narvik, Quadrantides, vers 19 UTC) : cela vaut la peine d'écouter. |
| *Aucune zone commune de la couche E* | Le trajet est plus long que deux fois la portée à l'altitude des traînées : les deux stations ne voient aucune partie commune de la couche E (bond unique impossible). |
| *Aucun Hot conseillé* | Presque aucun essaim actif à cette heure. |

Référence pour le graphisme de la voûte céleste : Swan Meteor Skyview de DL1DBC (swan.ms) ; graphique polaire avec la meilleure direction : RadiantCalc de SM6FHZ.
