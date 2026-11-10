[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · **Français** · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Collecte de données

*Onglet : Direct et données en temps réel › Collecte de données.*

[![Collecte de données](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Quatre sources

L'onglet recueille les **spots meteor scatter** de trois flux telnet et du flux MQTT de PSKReporter, chacun dans son propre sous-onglet :

| Sous-onglet | Par défaut | Remarques |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Un cluster au choix. Sur ON0DXK, les bandes VHF sont filtrées : activez-les avec `set/filter dxbm/pass 6` (puis 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Les skimmers décodent rarement les modes MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X qui relaie les spots de **PSKReporter** : c'est là qu'arrivent les décodages MSK144 de WSJT-X et de MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spots PSKReporter en direct via **MQTT** (service de M0LTE) : pas de login, chaque spot contient déjà les locators de la station émettrice et de la station réceptrice. Sujets par défaut : MSK144 sur 6 m, 4 m, 2 m, 1,25 m, 70 cm et FSK441 sur 2 m (`pskr/filter/v2/band/mode/#`) ; *Sujets par défaut* les rétablit. |
| **Spots MS collectés** | – | Tableau des spots acceptés, les plus récents en premier. |

Chaque flux a son hôte, son port, les commandes envoyées après le login, *Reconnecter*, *Connecter au démarrage*, une console et une ligne pour envoyer des commandes. Saisissez votre **indicatif pour le login** en haut. La source MQTT a son hôte, son port, ses sujets (un par ligne ou séparés par `;`), *Reconnecter* et *Connecter au démarrage* (désactivé par défaut) et une console avec les spots reçus ; ses spots passent par le même filtre. Un bandeau montre l'état des quatre sources (point vert = connectée). Les sessions restent ouvertes quand vous changez de langue ou de schéma de couleurs.

## Le filtre (40 % de la fenêtre)

- **Filtre local facultatif :** les lignes du cluster sous **27990,0 kHz** sont écartées d'emblée (ni affichées, ni enregistrées).
- **1er critère – fréquences typiques du MS :** 50190–50300, 70100–70400, 144290–144399 kHz. Un spot dans ces fenêtres est accepté même sans nom de mode, sauf si le commentaire déclare une autre propagation : `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Fenêtres et balises sont modifiables.
- **2e critère – modes MS :** hors des fenêtres, ou avec l'une de ces balises, un spot n'est conservé que s'il contient **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modes numériques utilisés uniquement en MS) ou **\<MS\>**, en majuscules, minuscules ou casse mixte. Les mots peuvent être désactivés, ajoutés et supprimés ; chacun a son compteur.
- **Bandes** 28, 50, 70, 144, 222, 432 MHz ; **test du filtre** sur une ligne collée ; **compteurs**.

## Locators et archivage

Les locators manquants, ou réduits à 4 caractères, sont pris dans la base **CALL3** (`data/call3.txt`, fichier de JTDX, plus d'un million d'indicatifs), qui l'emporte toujours sur un locator à 4 caractères. Les spots acceptés sont enregistrés dans `data/spot_ms`, un fichier CSV par jour, et alimentent la carte du [Trafic en direct](Live-Traffic-fr).
