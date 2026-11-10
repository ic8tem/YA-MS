[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · **Français** · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-BR) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-TW)

# Géométrie et affaiblissement

*Onglet : Calcul prévisionnel › Géométrie et affaiblissement.*

[![Géométrie et affaiblissement](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Un rapport texte sur le trajet (sélectionnable, donc copiable) et, à droite, le graphique **Élévation d'antenne en fonction de la distance au scatter point**. Les numéros entre crochets renvoient aux équations du manuel de calcul (`doc/YA-MS_manuale_calcoli.docx`).

## Données propres à cet onglet

| Champ | Par défaut | Usage |
|---|---|---|
| **Puissance W** | 400 | Puissance de l'émetteur pour le bilan de liaison |
| **Gain antenne dBi (tx = rx)** | 14 | Même antenne aux deux extrémités |
| **Signal minimal dBm** | −130 | Signal minimal détectable (article : Yagi 8 éléments + préampli) |
| **Densité traînée q = 10^ … électrons/m** | 14 | Densité linéique d'électrons de la traînée sous-dense |

Les stations, la bande, l'altitude des traînées, l'élévation du lobe, le boom et la distance des hot spots viennent des [rangées de commandes](Getting-Started-fr#1-les-trois-rangées-de-commandes).

## Sections du rapport

| Section | Contenu |
|---|---|
| **GÉOMÉTRIE DU TRAJET (Terre sphérique, R = 6372,7955 km)** | Station et correspondant avec leurs altitudes ; distance, azimut et azimut inverse ; point milieu (locator et coordonnées) ; altitude des traînées (*<- mode mesuré par le radar de Collm* quand elle vient du radar) ; élévation de l'antenne vers le point milieu |
| **HOT A / HOT B (hot spots classiques, pour le pointage de l'antenne)** | Pour chacun : locator, azimut depuis vous et décalage par rapport au trajet direct, azimut depuis le correspondant, distance, élévation |
| **LIMITES DE LA ZONE COMMUNE** | Portée à l'altitude des traînées avec l'élévation du lobe ; Limite A / Limite B avec leurs azimuts |
| Antenne | Boom en λ, gain, lobe horizontal / vertical ; Hot A et Hot B dans ou hors du lobe |
| **AFFAIBLISSEMENT DE TRAJET (traînée sous-dense, McKinley 1961 ; gains d'antenne exclus)** | Tableau pour le point milieu (forward), Hot A et Hot B à 28, 50, 70, 144, 222 et 432 MHz |
| **BILAN À … MHz (point milieu)** | Puissance et PIRE, affaiblissement de trajet, signal à l'antenne, minimum détectable, **marge** ; la même marge avec l'affaiblissement moyen d'OH5IY |
| **RÈGLES EXPÉRIMENTALES ENTRE LES BANDES (SM6FHZ, VUSHF 2025)** | Nombre/intensité et durée par rapport au 144 MHz ; ping maximal IARU |

## Locator et trajet

Locator (4, 6 ou 8 caractères ; centre du carré, système Maidenhead de l'IARU) [14]. Distance, azimut et point milieu avec les formules orthodromiques sur une sphère de rayon **r = 6372,7955 km** (article Cerrotta–Sartori) [15–16]. Les calculs qui dépendent de l'heure se rapportent au **point milieu**, car la meilleure heure peut différer de jusqu'à 1,5 heure entre les deux extrémités (SM6FHZ).

## Élévation de l'antenne

**Source :** formule de l'article Cerrotta–Sartori (figure 7), avec x = d/r, d la distance au sol jusqu'au point de réflexion, H l'altitude des traînées et h l'altitude de la station [17] :

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Vérification :** elle concorde avec la géométrie sphérique exacte à 0,03° près. Le programme utilise l'arc tangente à deux arguments, qui donne des valeurs négatives au-delà de l'horizon et évite le problème de périodicité signalé dans l'article. Une élévation négative vers le point milieu signifie *trajet au-delà de la portée géométrique d'un bond unique*.

## Portée à l'horizon

Distance au sol à laquelle un rayon d'élévation e atteint l'altitude H (inverse géométrique de la formule ci-dessus) [18] :

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Vérification :** H = 89,5 km, e = 0° → **1062 km**. Dans l'exemple de l'article (JN44BB–IO53RT), le dessin place les croisements de l'horizon à environ 870 km des stations, ce qui correspond à un lobe relevé d'environ 2° (865 km).

## Limites de la zone commune

**Source :** l'article situe les croisements des courbes où l'horizon de chaque station rencontre la couche E : les intersections de deux cercles de rayon angulaire ρ = d_H/r centrés sur A et B [19–20] :

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Si 1 − |p0|² < 0, le trajet est plus long que 2·d_H et les stations ne voient **aucune zone commune de la couche E**.

**Vérification :** ce sont les **bords les plus éloignés** du ciel vu par les deux stations, **pas des points à viser**. Sur JN70CN–IN78UO (1710 km, azimut 308°), ils tombent à 1062 km de la station, à 37° à gauche et à droite du trajet direct, alors que MSHV suggère 10°. C'est pourquoi ils sont appelés *Limite A* / *Limite B* et dessinés en pâle sur la carte.

## Hot A et Hot B

**Source :** les réflexions des météores sporadiques se concentrent dans deux zones (« hot spots ») de part et d'autre du point milieu. J. Richardson (AMS), dans le tableau cité par DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), donne le décalage d'antenne par rapport au cap direct : **13° à 1000 km, 11° à 1250 km, 10° à 1500 et 2000 km**. L'AMS Bulletin No. 203, repris par W8WN, donne 10° à 1500 et 1800 km.

**Choix :** Hot A et Hot B sont les points situés à la distance s du point milieu M, perpendiculairement au trajet. Avec *auto (AMS)* coché (par défaut), s découle du décalage du tableau de Richardson, interpolé linéairement (13° en dessous de 1000 km, 10° au-delà de 2000 km) : s = (D/2)·tan(décalage). Décoché, s est saisi à la main, de 30 à 400 km (MSHV utilise 150 km) ; A à gauche en regardant de votre station vers le correspondant, B à droite [21]. Le décalage vu de la station vaut environ [22] :

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Vérification :** avec le tableau AMS, 1000 km → 13°, s ≈ 115 km ; 1250 km → 11°, s ≈ 121 km ; 1500 km → 10°, s ≈ 132 km ; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, comme les 150 km utilisés auparavant et par MSHV ; sur les trajets courts, le tableau rapproche les hot spots du point milieu.

## Affaiblissement sous-dense

**Source :** équation de McKinley et recommandation ITU-R P.843 pour les traînées sous-denses (sin α = 1), gains d'antenne exclus ; q = densité linéique d'électrons, r_e = rayon classique de l'électron = 2,818·10⁻¹⁵ m, R1, R2 distances à la traînée, φ demi-angle de diffusion, β angle entre la traînée et le plan du trajet, a₁ facteur de rayon initial avec r₀ en m et h en km (P.843, éq. 4 et 7) [36] :

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Choix :** le bilan et le tableau des affaiblissements utilisent β = 90° (traînée qui traverse le plan du trajet, le cas le moins favorable : valeur prudente) et le bilan affiche aussi le meilleur cas, β = 0. r₀ est pris à l'altitude moyenne des échos pour la fréquence, h = 124 − 17 log f (P.843, éq. 15) : 0,76 m à 95 km pour 50 MHz, 0,40 m à 87 km pour 144 MHz, 0,21 m à 79 km pour 432 MHz. Sur 1000 km, a₁ vaut 0,2 dB à 50 MHz, 0,6 dB à 144 MHz et 1,4 dB à 432 MHz (2,9 dB à 600 km) ; à l'altitude fixe de 102 km de DJ5HG, il serait d'environ 70 dB à 432 MHz, c'est-à-dire aucun écho.

**Vérification :** avec q = 10¹⁴ électrons/m, traînées à 89,5 km et β = 0, à 144 MHz : **182–192 dB** entre 600 et 2100 km (185 dB à 1000 km), dans la plage de **172–190 dB** calculée par John Worsnop **G4BAO** dans sa thèse de doctorat, telle que rapportée par GM8JBJ. Avec β = 90°, l'affaiblissement augmente de 10 dB à 600 km, 13 dB à 1000 km et 16 dB à 2100 km ; la **moyenne de 200 dB** d'OH5IY se situe entre les deux cas. Les 182 dB du tableau de GM8JBJ ne sont pas une confirmation : le tableau n'indique aucune fréquence, ses 86,4 dB par bond sont l'affaiblissement en espace libre sur 500 km à 1 MHz (le terme 20 log f manque : 129,6 dB à 144 MHz) et ses postes totalisent 163,8 dB, pas 182 ; la page ne dit ni « minimum » ni « 144 MHz ».

## Bilan de liaison

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Les gains sont saisis et utilisés en dBi : l'affaiblissement de McKinley se rapporte à des antennes isotropes, donc aucune correction de dipôle de 2,15 dB n'est soustraite (PIRE = puissance + gain). Le rapport donne aussi la marge avec l'**affaiblissement moyen d'OH5IY** (200 dB à 144 MHz, transposé en λ³ à la bande choisie). Référence de l'article : il faut environ **70 dBm de PIRE** (−130 dBm + 200 dB, par ex. environ 400 W dans 14 dBi).

## Gain et lobe de l'antenne

**Gain – source :** courbe de Günter Hoch **DL6WU** pour les Yagi longues en fonction de la longueur de boom L, rapportée par W8IO (valable à partir d'environ 2 λ) [39] :

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Vérification avec les modèles NEC de L.B. Cebik W4RNL à 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design* ; *70-CM Yagi Stacks Part 2*) :

| Yagi | Éléments | Boom (λ) | W4RNL NEC (dBi) | Formule (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

L'écart ne dépasse jamais **0,1 dB** : le gain dépend de la longueur du boom plus que du modèle (les Yagi VK3AUU ont un boom plus court à nombre d'éléments égal). Le Yagi Calculator de VK5DJ donne aussi des estimations pour les variantes VK3AUU, WA2PHW et DJ9BV, dont les formules ne sont pas publiées.

**Lobe – source :** règle de Kraus, avec un lobe circulaire θE = θH = θK [40] :

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Vérification :** les modèles NEC de W4RNL pour les Yagi DL6WU donnent un **lobe horizontal 5–10 % plus étroit** que Kraus : 33,8° / 26,4° / 22,6° pour 12, 19 et 26 éléments, contre 37,3° / 28,0° / 23,9°. Les formules simples ignorent les lobes secondaires avant (W4RNL, *Long-Boom Yagi Rules of Thumb*). Sur les booms longs, le lobe vertical est un peu plus large que l'horizontal (14 λ : 18,4° / 18,8°).

**Choix** [41] :

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Exemple : Yagi de 14 λ à 432 MHz → 20,3 dBi, lobe de 18,1° en horizontal et 19,5° en vertical ; les modèles de W4RNL donnent 20,4 dBi et 18,4° / 18,8°. Ce sont des règles approchées, tirées de quelques antennes DL6WU.

L'antenne est toujours considérée comme pointée vers le correspondant. Un hot spot est **dans le lobe** si |Az(Hot) − Az(antenne)| ≤ θ_horizontal/2 : il est alors dessiné en gris sur la [voûte céleste](Sky-View-fr) et un avertissement apparaît. Dans le calcul de l'efficacité, les antennes sont isotropes ; le lobe réel ne sert qu'à cette vérification.

## Règles expérimentales entre les bandes

Par rapport au 144 MHz : nombre/intensité × (144/f)³ (en dB), durée × (144/f)² (SM6FHZ, VUSHF 2025). Durée maximale des pings selon l'IARU Région 1 : 1000 ms à 50 MHz, 500 ms à 70 MHz, 100 ms à 144 MHz, 13 ms à 432 MHz (VHF Handbook, cité dans l'article). Voir aussi [Prévisions expérimentales](Experimental-Forecasts-fr).
