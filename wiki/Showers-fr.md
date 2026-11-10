[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · **Français** · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [ไทย](Showers-th) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Essaims

*Onglet : Essaims.*

[![Essaims](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Le catalogue des essaims utilisé par tous les calculs : **45 essaims** du **IMO Meteor Shower Calendar 2026 et 2027** (tableaux 5 et 7) plus la **Source de l'antihélion** (tableau 6), chacun avec son **prochain maximum**.

## Colonnes

| Colonne | Signification |
|---|---|
| Code | Code IMO (QUA, PER, GEM, …) |
| Essaim | Nom |
| Activité | Période d'activité (jour/mois – jour/mois) |
| λ max | Longitude solaire du maximum (J2000), selon l'IMO |
| **Prochain maximum (UTC)** | Date et heure du prochain maximum (voir plus bas) |
| **Source du maximum** | *IMO 2026* / *IMO 2027* = date et heure publiées par l'IMO ; *IMO 2026 (jour)* = l'IMO ne donne que le jour, l'heure affichée est calculée (*~hh:mm calc.*) ; *calculé à partir de λ* = pas de valeur IMO pour cette année |
| A.D., Décl. | Radiant au maximum (*mobile* pour la Source de l'antihélion) |
| v km/s, r | Vitesse géocentrique et indice de population |
| ZHR | ZHR au maximum (*var.* = variable) |
| Type | *visuel* ou *radio, diurne* |
| Actif aujourd'hui | *oui* quand l'essaim est actif en ce moment |

## Prochain maximum

Le programme affiche toujours le **prochain** maximum. Quand l'IMO a publié le calendrier de l'année, il utilise la **date et l'heure IMO** de `data/massimi_imo.csv` (2026 et 2027 sont inclus) ; sinon il calcule l'instant où le Soleil atteint la longitude solaire du maximum (Meeus, *Astronomical Algorithms*, ch. 25, résolu par la méthode de Newton).

**Vérification :** le calcul concorde avec les calendriers IMO 2026 et 2027 à quelques minutes près lorsque l'IMO donne l'heure (par ex. Quadrantides 3/1/2026 21:13 contre 21:00 ; Géminides 14/12/2027 19:51 contre 20:00). Exceptions : les kappa-Léonides diurnes 2026, un jour plus tard (26/9 au lieu de 25/9), et l'heure des êta-Aquarides 2027 (15:10 contre 09:00 IMO) – dans ces cas, c'est la valeur IMO qui est utilisée.

**Ajouter une année :** quand l'IMO publie un nouveau calendrier, ajoutez ses lignes à `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, heure vide si l'IMO ne donne que le jour). D'ici là, le maximum est calculé.

## Essaims mineurs et diurnes

Le catalogue comprend les **essaims mineurs** de la liste IMO – par exemple les Camélopardalides d'octobre (OCT, ZHR 5, actives du 5 au 6 octobre), les Andromédides, les gamma-Ursae Minorides – et les **essaims radio diurnes** d'avril à octobre (Piscides d'avril diurnes, Arietides diurnes, zêta-Perséides diurnes, bêta-Taurides diurnes, kappa-Léonides diurnes, Sextantides diurnes, …). Même avec de faibles ZHR, ils contribuent à l'[indice du trajet](Efficiency-Calculation-fr#le-modèle) et au [Hot conseillé](Sky-View-fr#hot-conseillé). Pour les essaims radio diurnes, l'IMO ne donne pas de ZHR : à défaut, le programme utilise une valeur de travail de 5.

## Profil d'activité et déplacement du radiant

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 et λ_max viennent du calendrier IMO ; les pentes B (différentes avant et après le maximum) et les déplacements quotidiens dα/dλ, dδ/dλ sont des **valeurs de travail** inscrites dans `data/sciami.csv` (le tableau IMO des déplacements n'a pas encore été saisi). *Manuel, éq. 9 et 13.* La position de la Source de l'antihélion est interpolée linéairement entre les dates du tableau 6 de l'IMO (`data/ant_radiante.csv` ; active du 10 décembre au 20 septembre, ZHR environ 4).

## Modifier le catalogue

`data/sciami.csv` est un simple fichier texte (séparateur `;`) que vous pouvez modifier : code, nom, début et fin (MM-DD), λ max, A.D., Décl., déplacements, v, r, ZHR, B avant/après, type (V visuel, R radio diurne). Si une ligne est erronée, le programme affiche un message au démarrage et l'ignore.

Sources : International Meteor Organization – Meteor Shower Calendar 2026 et 2027, [www.imo.net](https://www.imo.net) (tableaux 5, 6 et 7) ; Philip G0ISW (taux horaires radio maximaux) ; Rossano IZ5TEK (scattertek).
