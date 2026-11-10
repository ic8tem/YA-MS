[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · **Français** · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Prévisions expérimentales

*Onglet : Calcul prévisionnel › Prévisions expérimentales.*

[![Prévisions expérimentales](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Cet onglet convertit les comptages de météores du **radar de Collm (36,2 MHz)** en une estimation des **réflexions par heure sur une bande amateur** (144 MHz par défaut, n'importe quelle fréquence de 28 à 1300 MHz), établit la prévision des **24 prochaines heures** pour votre trajet et permet de **comparer** l'estimation avec un observateur **RMOB** – par exemple un observateur qui écoute GRAVES sur 143,050 MHz.

> Tout ici est **expérimental** : la règle de fréquence est une règle empirique, et le facteur de station dépend de votre station. Utilisez les chiffres pour comparer des heures et des jours, et vérifiez-les sur l'air.

## Commandes

| Commande | Par défaut | Rôle |
|---|---|---|
| **Fréquence cible MHz** | 144 | Fréquence de la prévision (28–1300 MHz) |
| **Exposant λ^k** | 3 | Exposant k de la règle de fréquence (SM6FHZ : 3) |
| **Facteur de station K** | 1 | Tient compte de la station de réception (puissance, antennes) ; obtenu par comparaison avec un observateur RMOB sur la même bande |
| **Charger un fichier RMOB depuis le disque...** | | Lit un fichier texte RMOB mensuel (voir plus bas) |
| **Déduire l'exposant du fichier RMOB** | | Ajuste k sur les heures communes à Collm et RMOB |
| **Observateur RMOB** | vide | Nom de l'observateur tel qu'il apparaît dans le nom du fichier (par ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Télécharger RMOB maintenant** | | Télécharge une fois le fichier du mois en cours de cet observateur |
| **récupération automatique toutes les 5 minutes (activer seulement avec l'autorisation de RMOB)** | **désactivé** | Voir [RMOB et programmes automatiques](#rmob-et-programmes-automatiques) |

La ligne orange sous les commandes affiche la règle avec les valeurs actuelles, par ex. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, la transposition de la durée et le ping maximal IARU à cette fréquence.

## Du radar à la bande amateur

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Source :** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45e Nordic VUSHF, mai 2025 – le nombre et l'intensité des réflexions varient en **λ³**, la durée en **λ²** (le 432 MHz est 14–15 dB sous le 144 MHz et dure 1/9). **Vérification :** la dépendance en λ³ est la même que dans l'équation sous-dense de McKinley. Avec k = 3, 1000 météores/heure à Collm deviennent environ **16 réflexions/heure à 144 MHz** ; les observateurs RMOB de GRAVES sur 143,050 MHz comptent habituellement **20 à 140 échos/heure** (bulletin RMOB, juin 2018) : l'ordre de grandeur est compatible, et la différence correspond au facteur de station K. (Manuel, éq. 44–45.)

## Les 24 prochaines heures

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistance :** la valeur transposée de la même heure de la veille (ou de l'avant-veille si elle manque), corrigée par la variation de l'**indice essaims du trajet** I (Σ ZHR × efficacité, voir [Calcul de l'efficacité](Efficiency-Calculation-fr#le-modèle)). La constante 10 représente le fond sporadique et limite la correction quand l'indice est faible. *Choix du programme (manuel, éq. 47).*

| Panneau | Contenu |
|---|---|
| **Mesuré à Collm et transposé à f MHz – hier et aujourd'hui (UTC)** | Météores/heure du radar de Collm ; valeurs transposées (orange, échelle de droite) ; les comptages RMOB s'ils sont chargés (vert, échelle de droite) |
| **Prévision expérimentale des prochaines 24 heures à f MHz pour …** | Réflexions/heure prévues (barres) et indice essaims du trajet (échelle de droite) |
| Tableau | Heure UTC · Collm même heure · Transposé · Indice essaims trajet · Prévision /heure · **Évaluation** |

**Évaluation :** *bon* quand la prévision atteint au moins 1,3 × la moyenne sur 24 heures, *moyen* à partir de 0,8 ×, *faible* en dessous. La même prévision apparaît dans la carte **PRÉVISION EXPÉRIMENTALE** et dans la ligne orange du [Calcul de l'efficacité](Efficiency-Calculation-fr), et elle sert de base aux échos attendus de l'onglet [Radar GRAVES](GRAVES-Radar-fr#échos-attendus-expérimental).

## Comparaison RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) recueille les comptages horaires de météores des observateurs radio ; en Italie, beaucoup écoutent GRAVES sur 143,050 MHz (Planétarium de Venise, Faenza, Rovereto et d'autres).

**Lecture des fichiers RMOB.** Deux formats texte sont acceptés :

| Format | Aspect | Remarques |
|---|---|---|
| Fichier mensuel (Colorgramme / Spectrum Lab) | une ligne par jour, `day| n| n| …` avec 24 valeurs horaires | le classique `NAME_MMYYYYrmob.TXT` |
| Tableau du bulletin | en-tête ` UT |  1   2   3 …`, lignes `0h|175 166 …` | si le fichier contient plusieurs observateurs, ils sont lus l'un après l'autre : utilisez un fichier avec un seul observateur |

Le mois et l'année sont tirés du nom du fichier (`…_MMYYYYrmob…`) ou de l'en-tête ; sinon, c'est le mois en cours qui est utilisé (et le programme le signale).

**Ajustement de l'exposant.** Avec K = 1, à partir de la médiane des rapports RMOB/Collm sur les heures communes (au moins 3) :

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Choix du programme (manuel, éq. 46).* La boîte de dialogue affiche les heures communes, le rapport médian et k ; **Oui** applique k (et fixe K = 1), **Non** garde k = 3 – ajustez alors K à la main à la valeur suggérée dans la même boîte de dialogue.

## RMOB et programmes automatiques

RMOB demande que les **programmes automatiques ne récupèrent pas ses fichiers**. C'est pourquoi la **récupération automatique est désactivée** au départ et ne doit être activée **qu'après avoir demandé l'autorisation à RMOB**. Sans elle, vous pouvez toujours utiliser **Charger un fichier RMOB depuis le disque...** ou appuyer sur **Télécharger RMOB maintenant** quand vous en avez besoin.

L'adresse de téléchargement est un modèle dans `config.ini` (clé `rmob_url`, par défaut `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, où `{NOME}` est l'observateur et `{MMAAAA}` le mois et l'année) ; les fichiers téléchargés sont conservés dans `data/radar/`.
