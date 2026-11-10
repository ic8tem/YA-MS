[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · **Français** · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Onglet : Direct et données en temps réel › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Qu'est-ce que GRAVES

**GRAVES** est un radar français qui émet en **CW sur 143,050 MHz** depuis **Broye-lès-Pesmes** (47,348° N 5,515° E, locator **JN27SI**, environ 200 m d'altitude ; Wikipedia). Les traînées météoriques situées dans la zone que voient à la fois GRAVES et vous renvoient son signal vers vous par **diffusion vers l'avant** (forward scatter) : vous entendez de brefs *pings* près de la porteuse. C'est ainsi que les observateurs **RMOB** sur 143,050 MHz comptent les météores heure par heure, et c'est un signal d'essai gratuit, toujours actif, pour votre station meteor scatter 2 m.

L'onglet traite **GRAVES → vous** comme un trajet meteor scatter à part entière : avec les mêmes fonctions que pour le trajet principal (même altitude des traînées, même élévation du lobe et même distance des hot spots), il calcule l'efficacité des essaims, le Hot conseillé et les zones PREV, puis vérifie si cette zone est **dans le faisceau de GRAVES** et **quand** le faisceau l'éclaire.

## Barre du haut

| Commande | Rôle |
|---|---|
| **Maintenant** | Ramène l'instant du calcul au temps réel (l'onglet suit le curseur *Instant du calcul*). |
| **Mettre GRAVES comme DX** | Le correspondant devient GRAVES (JN27SI, altitude 200 m) et le trajet principal est recalculé : tous les autres onglets affichent alors le trajet GRAVES. |
| **Séquence du faisceau** | *0,8 s par pas · cycle 4,8 s (PE1ITR 2021)* (par défaut) ou *3,2 s par pas · cycle 19,2 s (PE1ITR 2007)*. |

## Les quatre cartes

| Carte | Contenu |
|---|---|
| **ZONE UTILE DANS LE FAISCEAU DE GRAVES** | *Oui · secteur X* avec l'azimut et l'élévation du hot spot conseillé vus depuis GRAVES et le pas (1–6) ; ou *Non : hors des secteurs* / *Non : sous l'horizon de GRAVES* / *Non : au-dessus du faisceau (environ 25°)* |
| **EFFICACITÉ DU TRAJET GRAVES → VOUS MAINTENANT** | Indice du trajet Σ ZHR × efficacité, meilleur essaim, côté dominant A/B et *échos attendus ≈ …/heure* (expérimental, voir plus bas) |
| **TRAJET** | Distance jusqu'à GRAVES ; antenne vers le Hot conseillé (azimut et élévation) ; azimut direct de GRAVES |
| **PROCHAIN PASSAGE DU FAISCEAU SUR LA ZONE** | *maintenant · encore … s* ou *dans … s*, le pas (par ex. *B4*), les trois prochains instants (secondes dans la minute) et la fraction de traînées captées |

Si aucun essaim n'est utile à ce moment-là, le programme affiche le hot spot **le mieux adapté au faisceau** (dans les secteurs, le plus proche du sud) et le signale.

## Le ciel vu depuis GRAVES

D'après PE1ITR et le wiki Bolidozor, **quatre réseaux à commande de phase** couvrent le ciel au sud, de **90° à 270°** d'azimut, en quatre **secteurs de 45°** :

| Secteur | Azimut depuis GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Chaque secteur est divisé en **6 pas de 7,5°**, numérotés de 1 à 6 à partir de l'azimut le plus bas, éclairés l'un après l'autre, **au même moment dans les quatre secteurs**. Le faisceau a une **largeur d'environ 25° en élévation** : à l'altitude des traînées, il couvre la couronne colorée entre les deux cercles en pointillés (*horizon du faisceau*). Sur le dessin : points orange/rose = zones PREV du trajet GRAVES → vous, ligne verte = direction de votre station, ligne rouge = de votre station au hot spot conseillé ; le pas éclairé en ce moment est mis en évidence.

## Reconstitution chronologique

*RECONSTITUTION CHRONOLOGIQUE · date UTC* (même jour que le tableau 24 h) : pour chaque heure, l'efficacité du trajet GRAVES → vous, l'essaim le plus favorable et la fenêtre utile (*hh:00 → hh:00 UTC · n h*), avec le maximum (*max Σ … à hh:30*) et un repère rouge *maintenant*. En dessous, le **détail des secondes à venir** : les six pas du secteur, le pas qui éclaire la zone utile et *écho possible (+0,3 s de traînée)*.

### Temporisation du faisceau

La séquence est liée à l'heure **UTC** (PE1ITR) : le pas éclairé en ce moment est calculé à partir des secondes écoulées depuis 00:00 UTC modulo le cycle (86 400 s est un multiple à la fois de 4,8 s et de 19,2 s). La station de commande décale parfois la séquence de quelques pas : le détail est donc une **prévision à confirmer par l'écoute**. La pastille jaune **horloge du PC synchronisée** vous le rappelle : synchronisez votre PC avec un serveur NTP (erreur de quelques dixièmes de seconde au plus).

### Facteur de détection

Une traînée n'est entendue que si le faisceau l'éclaire pendant qu'elle dure :

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s est une durée typique de traînée sous-dense à 143 MHz – une valeur fixe, *choix du programme* (la règle λ² de SM6FHZ transpose les durées d'une bande à l'autre mais ne donne pas de valeur de départ).

### Échos attendus (expérimental)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

La prévision des [Prévisions expérimentales](Experimental-Forecasts-fr) (qui contient déjà le facteur de station K) est transposée de sa fréquence f_fc à 143,050 MHz avec la règle de SM6FHZ (même exposant k), corrigée par le rapport des indices d'essaims des deux trajets (la constante 10 représente le fond sporadique, comme dans la prévision) et multipliée par le facteur de détection. Purement indicatif : comparez avec les observateurs RMOB.

## Comment entendre les pings de GRAVES

| Étape | Que faire |
|---|---|
| Récepteur | **USB sur 143,049 MHz** (tonalité vers 1 kHz) ou 143,050 MHz, **AGC lente ou coupée**, bande passante audio d'**au moins 2,4 kHz** |
| Antenne | Vers le **hot spot conseillé** du trajet GRAVES → vous (carte *TRAJET*), à **faible élévation** |
| Waterfall | Les pings sont de **courts traits près de la porteuse** ; les traînées longues (sur-denses) sont plus larges et montrent un Doppler |
| Comptage | RMOB utilise GRAVES pour les comptages horaires de météores : **comparez vos pings avec ceux des observateurs sur 143,050 MHz** ([Prévisions expérimentales](Experimental-Forecasts-fr#comparaison-rmob)) |

## Sources

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) et *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, "Graves" – réseaux, secteurs et temporisation du faisceau
3. **Wikipedia**, "GRAVES (system)" – émetteur à Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observateurs sur 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** de IC8TEM – onglet Radar GRAVES (la maquette dont cet onglet est dérivé)
