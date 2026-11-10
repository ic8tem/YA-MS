[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · **Français** · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Contribuer et contacts

YA-MS progresse grâce aux comptes rendus de ceux qui l'utilisent sur l'air. Chaque correction est attribuée à sa source.

## Contacts

| | |
|---|---|
| Auteur | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Signaler un problème

Ouvrez une **issue sur GitHub** ou écrivez un e-mail en indiquant :

- le système d'exploitation et la version de YA-MS (dans le titre de la fenêtre) ;
- les deux locators, la bande et l'heure UTC ;
- ce que vous attendiez et ce que vous avez vu (une capture d'écran aide) ;
- pour les problèmes de radar, le message affiché dans l'onglet [Flux radar](Radar-Flux-fr).

## Ce qui est particulièrement utile

- **Comptes rendus de trafic.** Les heures et les trajets où l'efficacité ou la prévision ont vu juste – ou faux. Le modèle est expérimental et doit être comparé avec des QSO réels et avec MCG_MS / MS-Soft.
- **Comparaisons RMOB.** Les valeurs du facteur de station K et de l'exposant k que vous avez trouvées avec la [comparaison RMOB](Experimental-Forecasts-fr#comparaison-rmob), avec votre bande et votre station.
- **Des données avec leur source.** De meilleurs déplacements de radiants, des profils d'activité, de nouvelles dates de maxima IMO (`data/massimi_imo.csv`), des données d'antennes : indiquez la source et elle sera citée.
- **Changements des graphiques radar.** Si le format du graphique de Collm change, une copie de l'image (`data/radar/`) aide à réétalonner la lecture.

## Traductions

Les traductions de l'interface sont de simples fichiers texte dans **`data/lingue/<code>.txt`** (UTF-8) et **tout le monde peut les corriger** :

```
<Italian text><TAB><translation>
```

- Une entrée par ligne ; les lignes commençant par `#` sont des commentaires.
- Dans les deux colonnes, les deux caractères `\n` indiquent un retour à la ligne.
- Conservez les paramètres `{0}`, `{1}`, … avec leur format (par ex. `{0:F1}`, `{3:+0;-0}`), dans l'ordre qu'exige votre langue.
- Les entrées manquantes ou vides s'affichent en italien. La liste de toutes les clés est `data/lingue/chiavi.txt` (générée par `tools/estrai_chiavi.py`, ne pas la modifier).

Modifiez le fichier dans le dossier `data/lingue` de votre installation et relancez YA-MS (ou changez de langue) pour voir le résultat. Comme ces fichiers sont **remplacés par des versions plus récentes à chaque mise à jour**, merci d'**envoyer aussi vos corrections** – par e-mail ou par une pull request sur GitHub (`data/lingue/`) – pour qu'elles entrent dans la prochaine version.

Ce wiki existe en English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文 ; les corrections des pages du wiki sont aussi les bienvenues.
