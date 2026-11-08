**English** · [Русский](Efficiency-Explanation-ru) · [Deutsch](Efficiency-Explanation-de) · [日本語](Efficiency-Explanation-ja)

# Efficacité - explication

*Onglet : Documents techniques › Efficacité - explication.*

[![Efficacité - explication](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Un document technique, *"Come YA-MS calcola l'efficienza di uno sciame"* (Comment YA-MS calcule l'efficacité d'un essaim), affiché dans le programme sous forme de page claire. Il explique **pas à pas** comment l'efficacité est obtenue et indique pour chaque étape **d'où elle vient**. Le document est actuellement **en italien** ; ce wiki en donne le contenu en français dans [Calcul de l'efficacité](Efficiency-Calculation-fr#le-modèle) et [Géométrie et affaiblissement](Geometry-and-Path-Loss-fr).

## Étiquettes

Chaque étape porte une étiquette de couleur :

| Étiquette | Couleur | Signification |
|---|---|---|
| **FONTE** (source) | bleu | l'étape reprend une source citée ; le numéro entre crochets renvoie à la liste en fin de document |
| **RILIEVO** (vérification) | vert | comparaison entre le programme et les sources, avec le résultat |
| **SCELTA** (choix) | orange | un choix du programme, non tiré d'une source : à vérifier par l'expérience sur l'air |

## Chapitres

| Chapitre | Contenu |
|---|---|
| 1. Introduction | Objet, étiquettes, ce que signifie l'efficacité (OH5IY, MCG_MS ; YA-MS utilise le trajet réel) |
| 2. Où se produisent les réflexions : la couche E | Traînées entre 80 et 120 km ; altitude des traînées = mode de l'histogramme de Collm (vérification : 89,5 km le 5/11/2026) |
| 3. Géométrie du trajet | Terre et point milieu ; élévation de l'antenne (formule de l'article) ; zone commune et ses limites ; Hot A / Hot B ; lobe de l'antenne (DL6WU, Kraus, W4RNL) |
| 4. Le radiant de l'essaim | Position du radiant (IMO 2026/2027), date du maximum (IMO ou longitude solaire), profil d'activité |
| 5. Condition de réflexion | Réflexion spéculaire (McKinley), tolérance gaussienne 0,05 rad, meilleur pointage (SM6FHZ), formule de DH9GCD |
| 6. D'un point à l'efficacité | Points de réflexion tous les 15 km, poids de chaque point, pourcentage ; comparaison avec QTFGUI (DJ5HG) |
| 7. Lecture des résultats | Côté A / B, indice du trajet, couleurs des radiants, zones PREV, coupe vue depuis l'antenne |
| 8. Fréquence de travail et affaiblissement | Règles λ³ / λ², du radar à la bande amateur, références d'affaiblissement de trajet |
| 9. Limites connues | Traînées sous-denses uniquement, antennes isotropes, valeurs de travail |
| 10. Sources | 17 sources numérotées |

## Boutons

| Bouton | Rôle |
|---|---|
| **Exporter vers Word (.docx)...** | Enregistre une copie de `data/efficienza_spiegazione.docx` à l'endroit choisi (nom proposé *YA-MS - calcolo dell'efficienza.docx*) |
| **Ouvrir dans Word** | Ouvre le même `.docx` avec le programme par défaut pour les documents Word (Word, LibreOffice, …) |

## Fichiers

| Fichier | Contenu |
|---|---|
| `data/efficienza_spiegazione.txt` | Le texte affiché dans l'onglet, un bloc par ligne (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | La version Word |
| `doc/YA-MS_manuale_calcoli.docx` | Le **manuel de calcul** : toutes les équations (éditeur d'équations de Word), numérotées, avec leurs sources |

Les deux documents sont régénérés à partir des sources avec `tools/build_spiegazione.py data` et `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
