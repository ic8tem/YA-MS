**English** · [Русский](Data-Collection-ru) · [Deutsch](Data-Collection-de) · [日本語](Data-Collection-ja)

# Collecte de données

*Onglet : Direct et données en temps réel › Collecte de données.*

[![Collecte de données](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Trois flux de cluster

L'onglet recueille les **spots meteor scatter** de trois flux telnet, chacun dans son propre sous-onglet :

| Sous-onglet | Par défaut | Remarques |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Un cluster au choix. Sur ON0DXK, les bandes VHF sont filtrées : activez-les avec `set/filter dxbm/pass 6` (puis 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Les skimmers décodent rarement les modes MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X qui relaie les spots de **PSKReporter** : c'est là qu'arrivent les décodages MSK144 de WSJT-X et de MSHV. |
| **Spots MS collectés** | – | Tableau des spots acceptés, les plus récents en premier. |

Chaque flux a son hôte, son port, les commandes envoyées après le login, *Reconnecter*, *Connecter au démarrage*, une console et une ligne pour envoyer des commandes. Saisissez votre **indicatif pour le login** en haut. Un bandeau montre l'état des trois sessions (point vert = connectée). Les sessions restent ouvertes quand vous changez de langue ou de schéma de couleurs.

## Le filtre (40 % de la fenêtre)

- **Filtre local facultatif :** les lignes du cluster sous **27990,0 kHz** sont écartées d'emblée (ni affichées, ni enregistrées).
- **1er critère – fréquences typiques du MS :** 50190–50300, 70100–70400, 144290–144399 kHz. Un spot dans ces fenêtres est accepté même sans nom de mode, sauf si le commentaire déclare une autre propagation : `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Fenêtres et balises sont modifiables.
- **2e critère – modes MS :** hors des fenêtres, ou avec l'une de ces balises, un spot n'est conservé que s'il contient **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modes numériques utilisés uniquement en MS) ou **\<MS\>**, en majuscules, minuscules ou casse mixte. Les mots peuvent être désactivés, ajoutés et supprimés ; chacun a son compteur.
- **Bandes** 28, 50, 70, 144, 222, 432 MHz ; **test du filtre** sur une ligne collée ; **compteurs**.

## Locators et archivage

Les locators manquants, ou réduits à 4 caractères, sont pris dans la base **CALL3** (`data/call3.txt`, fichier de JTDX, plus d'un million d'indicatifs), qui l'emporte toujours sur un locator à 4 caractères. Les spots acceptés sont enregistrés dans `data/spot_ms`, un fichier CSV par jour, et alimentent la carte du [Trafic en direct](Live-Traffic-fr).
