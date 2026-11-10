[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · **Français** · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [ไทย](Efficiency-Calculation-th) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

La même loi est à la base de QTFGUI de DJ5HG (diffusion en cône). La condition est acceptée avec une tolérance gaussienne σ = 0,05 rad (environ 3°) – *choix du programme* :

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Poids de chaque point.** Puissance d'une traînée sous-dense (McKinley), φ = demi-angle de diffusion (limité à 85°, *choix*) :

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Le nombre de météores qui atteignent un point est proportionnel au sinus de l'élévation du radiant en ce point (ŝ·û_P), la même correction que celle utilisée par l'IMO pour le ZHR.

**3. Somme et pourcentage.** Points tous les 15 km à l'altitude des traînées, uniquement là où les deux stations les voient au-dessus de l'élévation du lobe (*choix*). 100 % correspond à la position de radiant la plus favorable pour ce trajet :

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F est calculé une fois par trajet sur une grille de directions (azimut tous les 5°, élévation tous les 2,5°) puis interpolé.

**4. Côté et indice.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

La lettre du tableau est le côté qui a la plus grande fraction. *Choix du programme (manuel, éq. 32–33).*

## Comparaison DH9GCD

Une vérification indépendante : la formule de la meilleure direction de **DH9GCD**, rapportée par **DF5HC** (conférence DARC, janvier 2018), où El et Az sont l'élévation et l'azimut du radiant vus de votre station et P l'azimut du correspondant :

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Elle est maximale avec le radiant à 45° et perpendiculaire au trajet. DF5HC considère le radiant trop bas sous 20° et **trop haut au-dessus de 70°** : ces heures reçoivent ↑ dans le tableau et un avertissement sur la [voûte céleste](Sky-View-fr#avertissements). La formule ignore la distance et les altitudes, mais c'est une bonne référence.

## Vérifications

| Vérification | Résultat |
|---|---|
| Règle de SM6FHZ (VUSHF 2025) : meilleur trajet orthogonal à l'azimut du radiant, pointage = az du radiant ±90°, tolérance ±40–50° | Reproduite par le modèle ; avec le radiant aligné sur le trajet et haut dans le ciel, l'efficacité est presque nulle |
| QTFGUI de DJ5HG, Hambourg JO53IM – Barcelone, Quadrantides, 4 janvier (exemple de son manuel) | QTFGUI : 07:00 pointage 252°, −8 dB ; 08:00 aucune zone de réflexion ; 09:00 pointage 168°, −4 dB. YA-MS (altitude 102 km comme QTFGUI) : 07:00 241°, −5,4 dB ; 08:00 0,6 % (−22 dB) ; 09:00 161°, −4,0 dB. DH9GCD : 26 %, 2 %, 32 %. Les trois méthodes voient le creux de 08:00, avec le radiant presque au zénith |
| Échantillonnage tous les 5 km au lieu de 15 km | les pourcentages varient de moins de 0,3 point |

> L'échelle utilisée par OH5IY et MCG_MS n'est pas connue en détail (les manuels de MS-Soft ne sont pas disponibles) : comparez les pourcentages avec ces programmes avant de les considérer comme équivalents. Le modèle ne prend en compte que les traînées sous-denses, avec des antennes isotropes ; les salves sur-denses et le fond sporadique ne font pas partie de l'efficacité (le fond sporadique est représenté par le flux radar).
