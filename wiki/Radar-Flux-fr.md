[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · **Français** · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-BR) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-TW)

# Flux radar

*Onglet : Direct et données en temps réel › Flux radar.*

[![Flux radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Cet onglet montre ce que comptent **en ce moment** les radars météoriques professionnels : les comptages horaires de météores et les altitudes des traînées du radar SKiYMET de **Collm** (Université de Leipzig / IAP Kühlungsborn, Allemagne, 36,2 MHz), et la dernière image du radar de **Sodankylä** (SGO, Finlande). Les comptages de Collm alimentent l'estimation sur votre bande et les [Prévisions expérimentales](Experimental-Forecasts-fr) ; l'altitude des traînées mesurée alimente toute la géométrie.

## Commandes

| Commande | Rôle |
|---|---|
| **Télécharger maintenant** | Vérifie immédiatement toutes les sources externes. |
| **Mise à jour automatique de toutes les sources toutes les 5 minutes** | Activée par défaut. Toutes les 5 minutes, toutes les sources sont vérifiées et **seules celles qui ont changé** sont retéléchargées (*inchangé (vérifié à … UTC)* / *nouvelle donnée à … UTC*). |
| **Exposant λ (SM6FHZ)** | Exposant k de la règle de fréquence, 3 par défaut (1–4). |

## Ce qui est affiché

| Panneau | Contenu |
|---|---|
| **Météores/heure – hier et aujourd'hui (UTC)** | Barres cyan = comptages de Collm (valides), barres rouges = écartés, ligne orange épaisse = *estimation à … MHz* sur l'échelle de droite |
| **Altitudes des traînées (Collm)** | Météores par km d'altitude entre 70 et 110 km, avec l'altitude la plus fréquente (mode), la moyenne, la médiane et l'écart type |
| Image de Collm | Le graphique SKiYMET original, tel que téléchargé |
| Image de Sodankylä | La dernière image des comptages de météores du radar de Sodankylä (affichée seulement ; son format n'est pas lu) |

La ligne au-dessus des graphiques indique quand le graphique de Collm a été lu et quelle échelle verticale a été trouvée (*échelle lue sur le graphique : 0-… météores/heure*).

## Comment le graphique de Collm est lu

Le graphique de Collm (720 × 720 pixels, couleurs pures) a des axes à position fixe, mais le radar **adapte chaque jour l'échelle verticale** aux valeurs mesurées (par ex. 0–1,2·10³ le 5/11/2026 et 0–1,0·10³ le 6/11/2026, avec des graduations déplacées). YA-MS procède donc ainsi :

1. il repère les grandes graduations de l'axe ;
2. il **lit les étiquettes** de la graduation la plus haute et du zéro en comparant chaque caractère avec la police matricielle du graphique ;
3. pour chaque heure i (0–47, hier et aujourd'hui), il prend la colonne centrale et le premier pixel cyan en partant du haut, y :

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top et y0 sont les lignes de la graduation la plus haute et du zéro, N_top la valeur lue sur l'étiquette la plus haute (×1000). Résolution : environ 7–8 météores/heure par pixel. *Choix du programme (manuel, éq. 42).*

Si une étiquette ne peut pas être lue, le programme se rabat sur l'étalonnage du 5/11/2026 (**échelle étalonnée 0-1200 météores/heure**) et le signale en orange : *Impossible de lire l'échelle verticale du flux (étiquette en haut : …) : valeurs à vérifier.* Si c'est le format du graphique lui-même qui change (*Format du graphique modifié (…x…) : lecture impossible* ou *Axes du flux introuvables à la position attendue*), la lecture doit être réétalonnée : merci de le signaler (voir [Contribuer](Contributing-and-Contacts-fr)).

### Altitudes des traînées

À partir de l'histogramme des altitudes (n_k météores dans le km k, altitude moyenne h_k) :

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Manuel, éq. 43.* Avec **du radar** coché (rangée 2 des commandes), le **mode** devient l'altitude des traînées de tous les calculs. Vérification : graphique du 5/11/2026 – mode 89,5 km, moyenne 88,6 km, écart type 6,8 km, ce qui confirme les ~90 km de l'article Cerrotta–Sartori (moyenne SKiYMET).

Si l'échelle du graphique des altitudes change, le programme avertit : *les statistiques des altitudes (mode, moyenne, médiane) restent valables, les comptages absolus non.*

## Estimation sur votre bande

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Règles expérimentales de **SM6FHZ** (VUSHF 2025) : le nombre et l'intensité des réflexions varient en λ³, la durée en λ² (chez McKinley, λ³ est la puissance d'une traînée ; le nombre de traînées varie environ en λ^1,5, et en diffusion vers l'avant les durées croissent aussi en sec²φ : voir [Prévisions expérimentales](Experimental-Forecasts-fr)). La durée maximale des pings selon l'IARU Région 1 est aussi affichée (1000 ms à 50 MHz, 500 ms à 70 MHz, 100 ms à 144 MHz, 13 ms à 432 MHz). Les valeurs sont indicatives, à comparer avec l'expérience sur l'air. Le facteur de station K et la comparaison avec RMOB se trouvent dans [Prévisions expérimentales](Experimental-Forecasts-fr).

## Hors ligne

Si aucune source n'est joignable, un message apparaît **une seule fois** : *Pas de connexion internet. Les données des radars et de RMOB ne peuvent pas être mises à jour : le programme utilise les dernières données enregistrées et réessaie seul toutes les 5 minutes.* La barre d'état en bas passe au rouge (*PAS DE CONNEXION INTERNET …*) jusqu'au retour de la connexion (*Connexion rétablie.*).

## Archives et sources

| Fichier (dans `data/`) | Contenu |
|---|---|
| `flusso_collm.csv` | Archive horaire du flux lu sur Collm (les heures déjà présentes sont mises à jour) |
| `quote_collm.csv` | Archive des altitudes des traînées |
| `radar/` | Dernières images téléchargées (et fichiers RMOB) |
| `fonti_radar.csv` | Adresses des sources radar, `attivo=1/0` pour activer/désactiver chacune |

| Source | Fréquence | Remarques |
|---|---|---|
| Radar météorique de Collm, Université de Leipzig (LIM) et IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | mis à jour toutes les heures à la minute 10 UTC ; flux d'hier + aujourd'hui, distribution des altitudes |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | image seulement (radar en cours de modernisation, projet DECC) |
| swan.ms (copie de Collm) | 36,2 MHz | désactivé par défaut ; à n'utiliser qu'avec l'autorisation de DL1DBC |

> Les données radar appartiennent à leurs institutions (Université de Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
