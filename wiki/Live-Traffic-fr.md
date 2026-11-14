[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · **Français** · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafic en direct

*Onglet : Direct et données en temps réel › Trafic en direct.*

[![Trafic en direct](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ce qu'il montre

Une **carte azimutale équidistante** centrée sur votre station (distance au centre = distance réelle, angle = azimut) avec **tout le trafic meteor scatter** recueilli par la [Collecte de données](Data-Collection-fr). Pour chaque liaison, le programme dessine :

- le **trajet** entre les deux stations, dans la couleur de sa bande : 28 MHz marron, 50 MHz vert, 70 MHz cyan, 144 MHz orange, 222 MHz rose, 432 MHz violet ;
- les deux **stations** aux extrémités du trajet ;
- le **zone de l'essaim** : là où se concentrent les traînées météoriques les plus probables pour ce trajet et à cette heure.

Les spots dont une station est **hors de la carte** sont écartés. Un spot **qui vient d'arriver** (datant de moins de 3 minutes) **clignote pendant une minute**, pour que la nouvelle activité saute aux yeux.

Afficher qui écoute : des triangles de la couleur de la bande marquent les stations qui, selon PSKReporter, reçoivent en MSK144, FSK441, PSK2K ou JTMS sur 28, 50, 70, 144 et 432 MHz dans la fenêtre de temps choisie. Un clic sur un triangle affiche indicatif, locator, modes et dernier spot. Le flux MQTT de l'onglet Collecte de données doit être connecté.

Aussi les moniteurs actifs de la carte PSKReporter : triangles vides pour les stations qui apparaissent sur la carte de pskreporter.info en MSK144, FSK441, PSK2K ou JTMS mais n'ont encore reçu aucun spot (MQTT n'envoie que les stations qui reçoivent quelque chose). YA-MS interroge le service de consultation de PSKReporter une fois toutes les 5 minutes pour tous les modes, comme le demandent les règles du service ; un moniteur reste sur la carte au moins 11 minutes. Un clic sur le triangle montre l'indicatif, le locator, le logiciel de décodage et l'heure à laquelle le moniteur était actif. Activé par défaut.

FT8 au-delà de 1100 km sans trajets parallèles : un spot FT8 (de PSKReporter MQTT, des clusters ou de WSJT-X via UDP) entre stations distantes de plus de 1100 km qui n'a aucun trajet parallèle dans les 3 minutes avant et après (même bande, milieu à moins de 300 km, direction à moins de 15°, une autre paire de stations) est dessiné en vert clair et sa ligne dans le tableau en bas à droite clignote toujours. L'E sporadique et la tropo donnent beaucoup de trajets proches et parallèles ; un spot isolé peut être une traînée météorique. Pour cela YA-MS reçoit aussi par MQTT les spots FT8 de 6 m, 4 m, 2 m, 1,25 m et 70 cm (jamais 28 MHz, en aucun cas). Ces spots n'entrent pas dans l'archive MS. Activé par défaut.

Les spots de WSJT-X via UDP qui concernent votre station (le décodage contient votre indicatif : qui vous appelle ou vous répond) sont dessinés en pointillés qui clignotent toujours, dans tous les modes et à toute distance.

Échange entre utilisateurs de YA-MS : quand un autre utilisateur de YA-MS décode par UDP un message adressé à votre station (en MSK144, FSK441, PSK2K ou JTMS, ou en FT8 au-delà de 1100 km), son YA-MS vous l'envoie chiffré via trois brokers MQTT publics (HiveMQ, Mosquitto, EMQX) ; vous le voyez en pointillés violets qui clignotent toujours et dans une ligne de la console UDP. Vous seul pouvez le lire (clés ECDH P-256, AES-256 et HMAC-SHA256). Les spots FT8 ne s'affichent que s'ils n'ont aucun trajet parallèle dans les 3 minutes. Activé par défaut ; yams_scambio=0 dans data/config.ini le désactive.

La carte affiche les indicatifs des deux stations de chaque spot, une seule fois par station. La projection se choisit entre azimutale (centrée sur votre station) et Mercator. L'info-bulle de la colonne zone de l'essaim en explique le sens.

Les spots de toutes les bandes sont affichés, y compris ceux des bandes non choisies dans Collecte de données (ceux-ci ne sont pas enregistrés). Les spots CW et ceux entre stations trop proches ne sont pas affichés s'ils sont rejetés dans Collecte de données.

## Comment le zone de l'essaim est calculé

Pour chaque spot, le programme construit le trajet entre les deux locators (même géométrie que pour votre propre trajet, voir [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr)) et, à l'heure du spot, additionne point par point de la couche E les **contributions de réflexion spéculaire de chaque essaim actif**, pondérées par son ZHR – le même calcul que celui des **zones PREV** de la [voûte céleste](Sky-View-fr). Pour chaque côté du trajet qui réunit au moins 15 % du total, le zone de l'essaim est une **ellipse** : centre à la moyenne pondérée des points, demi-axes égaux à 1,5 fois les racines carrées des valeurs propres de leur dispersion, grand axe selon le vecteur propre principal. Quand aucun essaim ne contribue (météores sporadiques seulement), les zone de l'essaim sont les deux **hot spots** classiques, dessinés en tirets. Les équations complètes se trouvent au chapitre 10 du manuel de calcul.

## Commandes

| Commande | Signification |
|---|---|
| **Rayon de la carte** | 600–3500 km autour de votre station. |
| **Spots à afficher** | 15 ou 30 dernières minutes, dernière heure, 3 dernières heures, 24 dernières heures. |
| **Tableau** | Liaisons présentes sur la carte, les plus récentes en premier, dans la couleur de la bande ; *% essaim* donne la part des réflexions du côté principal, ou *sporadiques*. |
| **Clic** | Sur un trajet ou une ligne du tableau : la liaison est mise en évidence et l'encadré affiche le locator du centre du zone de l'essaim, sa part, sa taille et son axe. |
