[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · **Français** · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Calcul de l'efficacité

*Onglet : Calcul prévisionnel › Calcul de l'efficacité.*

[![Calcul de l'efficacité](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

L'**efficacité** d'un essaim indique, en pour cent, dans quelle mesure la position de son radiant permet des réflexions sur **votre** trajet. Le concept est dû à Ilkka **OH5IY** (MS-Soft) et il est repris dans l'article Cerrotta–Sartori : le maximum d'efficacité ne coïncide pas avec le maximum visuel (ZHR), car il dépend de la position du radiant par rapport aux deux stations. MCG_MS de DL5MCG applique la même idée à quatre directions fixes ; YA-MS la calcule pour le **trajet réel** entre les deux locators.

Cet onglet l'affiche heure par heure pour le jour choisi dans *Jour pour le tableau 24 h (UTC)* (valeurs à la demi de chaque heure).

## Cartes de synthèse

| Carte | Contenu |
|---|---|
| **MEILLEURE HEURE DE LA JOURNÉE** | Heure où l'indice du trajet est le plus élevé, l'indice et le côté dominant (A/B avec son %) |
| **ESSAIM LE PLUS FAVORABLE** | L'essaim au plus grand ZHR × efficacité de la journée, son efficacité, l'heure et le côté, et le **meilleur pointage** (azimut du radiant +90° / −90°) |
| **MAINTENANT** | Indice et côté dominant à cette heure, et le Hot conseillé (uniquement si le jour choisi est aujourd'hui) |
| **PRÉVISION EXPÉRIMENTALE** | Réflexions/heure attendues maintenant, dans 1 h et dans 2 h à la fréquence de prévision (Collm, règles de SM6FHZ ; voir [Prévisions expérimentales](Experimental-Forecasts-fr)) |

Sous les cartes, un bandeau explique les lettres A et B (voir plus bas).

## Graphique

*Efficacité horaire pour … le … (UTC, valeurs à la demi-heure).* Pour cinq essaims au plus : efficacité en % en trait plein et formule de DH9GCD en pointillés de la même couleur ; l'**indice du trajet** en barres bleues sur l'échelle de droite.

## Tableau horaire

Une ligne par essaim actif ce jour-là (triés par ZHR), 24 colonnes pour les heures (UTC) :

| Cellule | Signification |
|---|---|
| `63A` | efficacité 63 %, la plupart des réflexions viennent du côté **A** |
| `41B` | efficacité 41 %, côté **B** |
| `3` | efficacité inférieure à 5 % : chiffre sans lettre de côté |
| vide | efficacité inférieure à 1 % |
| `…↑` | le radiant est **au-dessus de 70°** vu de votre station à cette heure (trop haut) |
| texte jaune | efficacité ≥ 50 % |

- **A** = **à gauche** en regardant de votre station vers le correspondant (zone Hot A) ; **B** = **à droite** (zone Hot B). Il convient de tourner l'antenne de **10–30° vers ce côté** (side-scatter, article Cerrotta–Sartori).
- **Lignes bleu clair** (*DH9GCD %*, sous chaque essaim) : la formule de DH9GCD, pour comparaison.
- **Ligne Σ** : *Indice trajet (ZHR×eff.)*.
- **Ligne orange** (*Prévision … MHz (réfl./heure)*) : la prévision expérimentale, pour les heures où elle existe (aujourd'hui et une partie de demain).

## Le modèle

Toutes les étapes figurent dans le [manuel de calcul](Efficiency-Explanation-fr) (`doc/YA-MS_manuale_calcoli.docx`, chapitre 5). En résumé :

**1. Réflexion spéculaire.** Une traînée renvoie le signal de A vers B seulement si elle est tangente à un ellipsoïde dont A et B sont les foyers (McKinley 1961). Les traînées d'un essaim sont parallèles à la direction du radiant ŝ (article ; McKinley). Pour chaque point P de la couche E, avec les vecteurs unitaires vers les stations :

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

La même loi est à la base de QTFGUI de DJ5HG et de son texte *"Die Geometrie von Meteorscatterverbindungen"* (2004) : la traînée diffuse sur un cône dont elle est l'axe, et seul un récepteur situé sur le cône l'entend. Pour une traînée idéale, la paroi du cône est très mince (un radiateur long de milliers de longueurs d'onde) ; le programme accepte la condition avec une tolérance gaussienne σ = 0,05 rad (environ 3°), qui représente ce que le cône idéal ne voit pas : la dispersion des radiants des essaims (0,3–1,4° mesurés par le GMN), les traînées courbées par le vent et leur longueur finie – *choix du programme* :

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Poids de chaque point.** Puissance d'une traînée sous-dense (McKinley ; ITU-R P.843, éq. 3), φ = demi-angle de diffusion (limité à 85°, *choix*), β = angle entre la traînée et le plan de propagation A-P-B, p̂ = normale unitaire à ce plan :

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Option « Angle β entre traînée et trajet (McKinley complet) »** (activée par défaut, réglage prudent). Activée : les traînées qui traversent le plan de propagation valent 10–15 dB de moins que celles qui s'y trouvent, si bien qu'aucune traînée n'est surestimée. Désactivée : chaque traînée est pondérée comme si elle se trouvait dans le plan (β = 0, poids avec cos²φ), comme jusqu'à la version 1.6. *Vérification :* sur un trajet de 1000 km, sans β le meilleur azimut du radiant est à 15°–90° du trajet selon l'élévation du radiant (30° avec le radiant à 30°, perpendiculaire au trajet avec le radiant à 60°), et le radiant perpendiculaire vaut 67 % à 30° d'élévation ; avec β le meilleur radiant est toujours dans l'axe du trajet et le perpendiculaire tombe à 15 %. Avec β, la règle de la meilleure direction de SM6FHZ / DH9GCD est perdue ; β reste une option, activée par défaut parce qu'elle donne les valeurs les plus prudentes, et la désactiver rétablit la règle.

Le nombre de météores qui atteignent un point est proportionnel au sinus de l'élévation du radiant en ce point (ŝ·û_P), la même correction que celle utilisée par l'IMO pour le ZHR.

**Option « Traînées plus longues avec un radiant bas (DJ5HG) »** (case au-dessus du graphique, désactivée par défaut, avec infobulle) : DJ5HG remarque qu'avec un radiant bas il tombe moins de météores par km², mais que les traînées sont plus longues (jusqu'à 100 km utiles) et satisfont plus souvent la loi de réflexion. Option activée, le poids devient min(sin El, 15/100) : l'épaisseur utile de la couche, 15 km, divisée par le sinus de l'élévation donne la longueur de la traînée, plafonnée à 100 km. Au-dessus d'environ 9°, les deux effets se compensent. Désactivée, le calcul reste prudent.

**Réglage du calcul** (même rangée, boutons radio) : **Prudent** (par défaut, les valeurs les plus prudentes : altitude des traînées du radar, traînées normales, β activé), **Comme DJ5HG** (102 km, traînées plus longues, β) et **Personnalisé**, sélectionné automatiquement lorsque vous modifiez à la main l'altitude, la case *du radar*, l'option des traînées plus longues ou β.

**3. Somme et pourcentage.** Points tous les 15 km à l'altitude des traînées, uniquement là où les deux stations les voient au-dessus de l'élévation du lobe (*choix*). 100 % correspond à la position de radiant la plus favorable pour ce trajet :

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F est calculé une fois par trajet sur une grille de directions (azimut tous les 5°, élévation tous les 2,5°) puis interpolé.

**Efficacité en dB (référence DJ5HG).** Le pourcentage se rapporte uniquement à la meilleure position du radiant pour ce trajet. Pour comparer des trajets différents, le programme donne aussi l'efficacité en dB par rapport à la référence fixe de DJ5HG : 0 dB est le maximum d'un trajet nord–sud de 1000 km à cheval sur l'équateur, avec le radiant sur l'équateur céleste à l'équinoxe, calculé avec la même altitude et les mêmes poids. DJ5HG donne ses valeurs à mieux que 6 dB.

**4. Côté et indice.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

La lettre du tableau est le côté qui a la plus grande fraction. *Choix du programme (manuel, éq. 32–33).*

## Comparaison DH9GCD

Les sources primaires pour la meilleure direction sont Eshleman & Mlodnosky et Meeks & James (Proc. IRE, 1957), Hines (1955) et sa vérification expérimentale par Forsyth, Hines & Vogan (1955) : seuls les radiants situés sur le demi-cercle de ciel perpendiculaire à la bissectrice de l'angle de diffusion sont utiles, le nombre de traînées croît avec sin El et, près du point milieu, les traînées utiles tombent à environ H·tan El sur le côté, du côté opposé au radiant. DJ5HG ajoute une réserve : avec un radiant **bas** exactement dans l'axe du trajet, la formule de McKinley donne des signaux forts (Hambourg–Narvik, Quadrantides, vers 19 UTC), donc « radiant aligné avec le trajet = presque zéro » ne vaut que pour un radiant haut ; le programme reste prudent et affiche l'avertissement *RADIANT BAS LE LONG DU TRAJET*.

Une vérification indépendante : la formule de la meilleure direction de **DH9GCD**, rapportée par **DF5HC** (conférence DARC, janvier 2018) – elle n'a pas de source primaire publiée –, où El et Az sont l'élévation et l'azimut du radiant vus de votre station et P l'azimut du correspondant :

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Elle est maximale avec le radiant à 45° et perpendiculaire au trajet. DF5HC considère le radiant trop bas sous 20° et **trop haut au-dessus de 70°** : ces heures reçoivent ↑ dans le tableau et un avertissement sur la [voûte céleste](Sky-View-fr#avertissements). La formule ignore la distance et les altitudes, mais c'est une bonne référence.

## Vérifications

| Vérification | Résultat |
|---|---|
| Règle de SM6FHZ (VUSHF 2025) : meilleur trajet orthogonal à l'azimut du radiant, pointage = az du radiant ±90°, tolérance ±40–50° | Reproduite par le modèle ; avec le radiant aligné sur le trajet et haut dans le ciel, l'efficacité est presque nulle |
| QTFGUI de DJ5HG, Hambourg JO53IM – Barcelone, Quadrantides, 4 janvier (exemple de son manuel) | QTFGUI : 07:00 pointage 252°, −8 dB ; 08:00 aucune zone de réflexion ; 09:00 pointage 168°, −4 dB. YA-MS (altitude 102 km comme QTFGUI) : 07:00 241°, −5,4 dB ; 08:00 0,6 % (−22 dB) ; 09:00 161°, −4,0 dB. DH9GCD : 26 %, 2 %, 32 %. Les trois méthodes voient le creux de 08:00, avec le radiant presque au zénith |
| Courbes de DJ5HG (*Die Geometrie…*, Bild 8–9 : depuis Hambourg et Munich, Quadrantides, 4 janvier ; lues sur le graphique, environ ±0,5 dB et ±15 min) comparées au test automatique `--prova-dj5hg` (une valeur par heure) | Horaires : le creux avec le radiant près du zénith tombe aux mêmes heures (Barcelone 07:30–08:30 contre 07–09 ; Sofia 06:36–07:48 contre 07–08 ; Narvik 07–08:30 contre 07–09) ; Moscou est fermé de 03 à 10 dans les deux cas, ouvert depuis Hambourg jusque vers 02:30 et depuis Munich jusque vers 00:30, comme l'écrit DJ5HG. Pointages : 2–10° d'écart. Niveaux et forme à 102 km (écart moyen et RMS par rapport aux courbes) : sans β ni traînées plus longues −1,6 / 4,0 dB ; traînées plus longues +1,1 / 4,6 dB ; β −5,4 / 6,2 dB mais avec la meilleure forme (3,0 dB une fois la moyenne retirée, contre 3,6) : les minima profonds avec un radiant bas apparaissent (Barcelone −15,6 dB à 17 contre −16 dB à 19:36 ; Sofia −18,5 dB à 20 contre −14 dB). β et traînées plus longues (*Comme DJ5HG*) −2,2 / 4,7 dB ; le réglage prudent (altitude radar 89,5 km, β activé, sans traînées plus longues) −6,9 / 7,6 dB, forme 3,3 dB. Sans β, YA-MS montre à peine le minimum avec le radiant bas et presque aligné avec le trajet (−8,6 et −10,4 dB) : c'est la réserve de DJ5HG lui-même, d'où l'avertissement |
| Échantillonnage tous les 5 km au lieu de 15 km | les pourcentages varient de moins de 0,3 point |

> La documentation de MS-Soft 5.2 définit l'efficacité d'OH5IY comme un indice relatif pour les seules traînées sous-denses, avec deux facteurs (élévation du radiant, optimale vers 45°, et angle avec le trajet, optimal à 90°) et un minimum relevé à la main à 20 % pour les traînées sur-denses ; la formule n'est pas publiée. MCG_MS la calcule pour quatre directions fixes et, avec le locator du correspondant, pour le trajet réel. Le modèle ne prend en compte que les traînées sous-denses, avec des antennes isotropes ; les salves sur-denses et le fond sporadique ne font pas partie de l'efficacité (le fond sporadique est représenté par le flux radar).
