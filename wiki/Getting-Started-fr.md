[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · **Français** · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Premiers pas

Au premier démarrage, YA-MS affiche un trajet d'exemple (JN70CN → JO62QM sur 144 MHz). Cinq minutes suffisent pour le configurer pour votre station.

## 1. Les trois rangées de commandes

Au-dessus des onglets se trouvent trois rangées de commandes, valables pour tous les onglets. Le bouton **Commandes** en haut à droite les replie et les déplie (pratique avec de grandes polices) ; le choix est mémorisé.

**Rangée 1 – stations et bande**

| Commande | Rôle |
|---|---|
| **Mon locator** / **altitude m** | Votre locator Maidenhead (4, 6 ou 8 caractères ; c'est le centre du carré qui est utilisé) et l'altitude de la station au-dessus du niveau de la mer. |
| **Correspondant** / **altitude m** | Locator et altitude de la station que vous voulez contacter. |
| **Bande MHz** | 28, 50, 70, 144, 222 ou 432 MHz : sert pour le gain et le lobe de l'antenne, l'estimation du flux et le bilan de liaison. |
| **Calculer** | Recalcule le trajet (échantillonnage de la couche E : quelques secondes). |
| **Antenne az** | Azimut de votre antenne : toujours **vers le correspondant** (azimut du trajet). |
| **Police** | Taille de tout le texte, 100–300 %. Voir [Réglages](Settings-and-Data-Folder-fr#police-et-commandes). |

**Rangée 2 – couche E et antenne**

| Commande | Rôle |
|---|---|
| **Altitude traînées km** + **du radar** | Altitude des traînées météoriques (90 km par défaut). Avec *du radar* coché, c'est l'altitude la plus fréquente (mode) mesurée par le radar de Collm qui est utilisée ; voir [Flux radar](Radar-Flux-fr). |
| **Élévation du lobe °** | Élévation minimale du lobe de votre antenne (0° = horizon). Seuls les points de la couche E que les deux stations voient au-dessus de cette élévation sont pris en compte. |
| **Antenne Yagi : boom m** | Longueur du boom de votre Yagi. Le programme affiche la longueur en λ, le gain (courbe DL6WU) et le lobe à −3 dB, horizontal et vertical ; voir [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr#gain-et-lobe-de-lantenne). Sous 2 λ, l'estimation est grossière. |
| **Hot spot depuis le point milieu km** | Distance de Hot A et Hot B au point milieu, 30–400 km (150 km par défaut, comme AMS Bulletin 203 / W8WN / MSHV). |

**Rangée 3 – heure**

| Commande | Rôle |
|---|---|
| **Heure** | Horloge UTC. |
| **Date du calcul (UTC)** | Le jour du calcul pour [Calcul prévisionnel](Sky-View-fr) et [Radar GRAVES](GRAVES-Radar-fr) (aujourd'hui par défaut), à l'heure actuelle de la journée. |
| **Heures (de −12 à +36 h)** | Déplace l'instant du calcul de 12 heures avant à 36 heures après cette heure, par pas de 15 minutes. À côté : *Calcul pour : maintenant* ou *Calcul pour : jj/mm hh:mm UTC*. |
| **Temps réel** | Revient à l'instant présent. |
| **Jour pour le tableau 24 h (UTC)** | Le jour affiché dans [Calcul de l'efficacité](Efficiency-Calculation-fr) et dans la chronologie GRAVES. |

## 2. Votre station et le correspondant

1. Saisissez **Mon locator** et **altitude m**.
2. Saisissez le locator et l'altitude du **correspondant** – ou cliquez sur la carte de la [voûte céleste](Sky-View-fr) : **clic gauche = locator du correspondant**, **clic droit = locator de ma station**.
3. Choisissez la **Bande MHz** et appuyez sur **Calculer**.

La barre d'état en bas confirme : *Trajet calculé : … km, … points de réflexion échantillonnés en … s*.

## 3. Votre antenne

Saisissez la **longueur du boom** de votre Yagi. Le programme en déduit le gain et le lobe et vous avertit si Hot A ou Hot B tombent déjà **dans le lobe** quand l'antenne est pointée vers le correspondant (ils sont alors dessinés en gris : inutile de tourner l'antenne).

## 4. Lire les résultats

| Question | Où regarder |
|---|---|
| Quel essaim favorise mon trajet en ce moment, et de quel côté ? | [Voûte céleste](Sky-View-fr) : liste des essaims, Hot conseillé en rouge, zones PREV |
| Quelle est la meilleure heure aujourd'hui ? | [Calcul de l'efficacité](Efficiency-Calculation-fr) : cartes de synthèse et tableau horaire |
| Combien de météores le radar compte-t-il ? | [Flux radar](Radar-Flux-fr) |
| Combien de pings puis-je attendre sur 144 MHz ? | [Prévisions expérimentales](Experimental-Forecasts-fr) (expérimental) |
| Ma station peut-elle boucler le trajet ? | [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr) : affaiblissement de trajet et marge |
| Quand a lieu le prochain maximum ? | [Essaims](Showers-fr) |
| Puis-je faire un essai avec GRAVES ? | [Radar GRAVES](GRAVES-Radar-fr) |

## Règles pratiques (tirées des sources)

- **Pointer perpendiculairement à l'essaim** : le meilleur trajet est orthogonal à l'azimut du radiant ; meilleur pointage = azimut du radiant ±90°, tolérance ±40–50° (SM6FHZ).
- **Side-scatter** : tournez l'antenne de 10–30° vers le côté (A ou B) d'où arrive la majorité des réflexions (article Cerrotta–Sartori).
- **Radiant trop haut** (au-dessus de 70°) ou trop bas (sous 20°) : peu de traînées utiles (DF5HC, DH9GCD).
- Les météores sporadiques culminent vers **06 UTC** (article ; confirmé par le flux de Collm).
- Distances utiles sur 432 MHz : 800–2000 km, optimum vers 1400 km (SM6FHZ) ; meilleure distance en général 1300–1500 km (DF5HC).

Suite : [Voûte céleste](Sky-View-fr).
