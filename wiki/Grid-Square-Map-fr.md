**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Carte des carrés

*Onglet : Carte des carrés.*

[![Carte des carrés](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Les carrés Maidenhead (4 caractères) que vous avez **contactés** et **confirmés**, lus dans le fichier ADIF de votre log, sur une carte de l'Europe – **un sous-onglet par bande : 50, 70, 144, 222 et 432 MHz**.

## Commandes

| Commande | Rôle |
|---|---|
| **Charger un fichier ADIF...** | Lit un fichier `.adi` / `.adif`. Un nouvel ADIF **remplace** les données précédentes. |
| **Effacer la mémoire** | Supprime tous les carrés chargés depuis l'ADIF (demande confirmation). |
| Souris | **Molette = zoom, glisser = déplacer, souris sur un carré = QSO** (jusqu'à six indicatifs avec la date, *(confirmé)* lorsqu'il est confirmé) |

Après le chargement, l'état affiche *… QSO lus, … carrés-QSO dans les bandes 50-432 MHz, … QSO écartés (autres bandes ou sans carré)*. Chaque carte de bande porte la légende *… carrés contactés, … confirmés*.

| Couleur | Signification |
|---|---|
| Orange | contacté |
| Vert | confirmé (QSL ou LoTW) |

## Comment l'ADIF est lu

- Champs utilisés : `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (spécification ADIF).
- Bande tirée de `BAND`, ou de la fréquence : 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Un carré est **confirmé** si au moins un QSO dans ce carré a `QSL_RCVD = Y` ou `LOTW_QSL_RCVD = Y`.
- Les carrés sont conservés dans `data/adif_quadrati.csv` jusqu'à ce que vous chargiez un autre fichier ou appuyiez sur **Effacer la mémoire**.

YA-MS ne se connecte **pas** à LoTW : exportez l'ADIF depuis votre logiciel de log (ou depuis LoTW) et chargez-le ici.
