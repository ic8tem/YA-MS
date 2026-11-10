[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · **Français** · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafic en direct

*Onglet : Direct et données en temps réel › Trafic en direct.*

[![Trafic en direct](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ce qu'il montre

Une **carte azimutale équidistante** centrée sur votre station (distance au centre = distance réelle, angle = azimut) avec **tout le trafic meteor scatter** recueilli par la [Collecte de données](Data-Collection-fr). Pour chaque liaison, le programme dessine :

- le **trajet** entre les deux stations, dans la couleur de sa bande : 28 MHz marron, 50 MHz vert, 70 MHz cyan, 144 MHz orange, 222 MHz rose, 432 MHz violet ;
- les deux **stations** aux extrémités du trajet ;
- le **nuage** : là où se concentrent les traînées météoriques les plus probables pour ce trajet et à cette heure.

Les spots dont une station est **hors de la carte** sont écartés. Un spot **qui vient d'arriver** (datant de moins de 3 minutes) **clignote pendant une minute**, pour que la nouvelle activité saute aux yeux.

## Comment le nuage est calculé

Pour chaque spot, le programme construit le trajet entre les deux locators (même géométrie que pour votre propre trajet, voir [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr)) et, à l'heure du spot, additionne point par point de la couche E les **contributions de réflexion spéculaire de chaque essaim actif**, pondérées par son ZHR – le même calcul que celui des **zones PREV** de la [voûte céleste](Sky-View-fr). Pour chaque côté du trajet qui réunit au moins 15 % du total, le nuage est une **ellipse** : centre à la moyenne pondérée des points, demi-axes égaux à 1,5 fois les racines carrées des valeurs propres de leur dispersion, grand axe selon le vecteur propre principal. Quand aucun essaim ne contribue (météores sporadiques seulement), les nuages sont les deux **hot spots** classiques, dessinés en tirets. Les équations complètes se trouvent au chapitre 10 du manuel de calcul.

## Commandes

| Commande | Signification |
|---|---|
| **Rayon de la carte** | 600–3500 km autour de votre station. |
| **Spots à afficher** | 15 ou 30 dernières minutes, dernière heure, 3 dernières heures, 24 dernières heures. |
| **Tableau** | Liaisons présentes sur la carte, les plus récentes en premier, dans la couleur de la bande ; *Nuage* donne la part des réflexions du côté principal, ou *sporadiques*. |
| **Clic** | Sur un trajet ou une ligne du tableau : la liaison est mise en évidence et l'encadré affiche le locator du centre du nuage, sa part, sa taille et son axe. |
