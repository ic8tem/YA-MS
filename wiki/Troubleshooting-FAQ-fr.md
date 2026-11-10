[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · **Français** · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Dépannage et FAQ

## Installation et démarrage

### Windows SmartScreen affiche « Windows a protégé votre ordinateur »
Le programme n'est pas signé avec un certificat commercial. Cliquez sur *Informations complémentaires* → *Exécuter quand même*. Ne le téléchargez que depuis la page [Releases](https://github.com/ic8tem/YA-MS/releases).

### Sous macOS, impossible d'ouvrir un programme d'un développeur non identifié
YA-MS n'est pas signé par Apple, donc **Gatekeeper** le bloque la première fois. Dans le `.dmg`, faites **clic droit sur « Installa YA-MS.command » → Ouvrir** et confirmez. Le script retire de `~/YA-MS/YA-MS.app` l'attribut de quarantaine « téléchargé depuis internet » et l'ouvre. Si macOS refuse encore, ouvrez *Réglages Système → Confidentialité et sécurité* et cliquez sur *Ouvrir quand même*.

### macOS : quel .dmg choisir ?
`-mac-apple-silicon.dmg` pour les processeurs M1/M2/M3/M4, `-mac-intel.dmg` pour les Mac Intel (menu Apple → *À propos de ce Mac* vous l'indique).

### Linux : YA-MS n'apparaît pas dans le menu des applications
Lancez `./installa.sh` depuis le dossier décompressé (pas depuis `~/YA-MS`). Certains bureaux demandent une déconnexion/reconnexion pour afficher les nouvelles entrées. Vous pouvez toujours le lancer avec `~/YA-MS/YA-MS`.

### La carte d'Europe est absente
*Carte d'Europe non disponible (réseau nécessaire au premier démarrage).* La carte Natural Earth est téléchargée dans `data/mappa` au premier démarrage. Connectez-vous à internet et relancez YA-MS.

## Affichage

### Sous Linux, le texte japonais s'affiche en carrés
Votre système n'a pas de polices CJK. Installez les polices **Noto CJK** et relancez YA-MS :

| Distribution | Commande |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Le texte est trop petit, ou les graphiques manquent de place
Utilisez le curseur **Police** (100–300 %) et repliez les rangées avec **Commandes**. Voir [Réglages](Settings-and-Data-Folder-fr#police-et-commandes).

### L'écran est trop lumineux la nuit
Choisissez **Nuit** ou **Noir** dans la liste **Thème**.

## Internet et données radar

### Message « Pas de connexion internet »
YA-MS l'affiche **une seule fois** quand aucune source n'est joignable ; la barre d'état passe au rouge. Le programme continue de fonctionner avec les **dernières données enregistrées** et réessaie seul toutes les 5 minutes ; *Connexion rétablie.* apparaît quand le réseau revient. Rien à faire.

### Avertissement orange dans Flux radar : « Impossible de lire l'échelle verticale du flux … »
Le radar de Collm change son échelle verticale chaque jour et YA-MS la lit sur les étiquettes du graphique. Si une étiquette ne peut pas être lue, le programme utilise l'échelle étalonnée 0–1200 météores/heure et avertit que les **valeurs sont à vérifier**. En général, le graphique horaire suivant est lu correctement. Si vous voyez *Format du graphique modifié* ou *Axes du flux introuvables à la position attendue* pendant de nombreuses heures, le radar a changé le format de son graphique : merci de [le signaler](Contributing-and-Contacts-fr).

### « L'échelle du graphique des altitudes a changé »
Les statistiques des altitudes (mode, moyenne, médiane) restent valables ; seuls les comptages absolus de l'histogramme des altitudes ne le sont plus.

### « Flux radar : aucune donnée »
Appuyez sur **Télécharger maintenant** dans [Flux radar](Radar-Flux-fr), et vérifiez que `data/fonti_radar.csv` contient `attivo=1` pour Collm.

### RMOB : pourquoi la récupération automatique est-elle désactivée ?
RMOB demande que les **programmes automatiques ne récupèrent pas ses fichiers**. N'activez la *récupération automatique toutes les 5 minutes* qu'après avoir obtenu l'autorisation de RMOB. En attendant, utilisez **Télécharger RMOB maintenant** ou **Charger un fichier RMOB depuis le disque...**. Voir [Prévisions expérimentales](Experimental-Forecasts-fr#rmob-et-programmes-automatiques).

### RMOB : « Format de fichier non reconnu » ou peu d'heures lues
Utilisez le fichier texte mensuel de l'observateur (`NAME_MMYYYYrmob.TXT`) ou un tableau de bulletin ne contenant qu'un seul observateur. L'ajustement de l'exposant demande au moins 3 heures communes avec les données de Collm (hier et aujourd'hui).

## Calculs

### « Locator de la station non valide » / « Locator du correspondant non valide »
Les locators doivent avoir 4, 6 ou 8 caractères (par ex. `JN70`, `JN70CN`, `JN70CN12`).

### « Aucune zone commune de la couche E »
Le trajet est plus long que deux fois la portée à l'altitude des traînées (environ 2 × 1062 km avec le lobe à 0° et des traînées à 89,5 km) : un seul bond meteor scatter ne peut pas le couvrir. Relever l'**Élévation du lobe** réduit encore la portée.

### Hot A / Hot B sont gris
Ils sont déjà **dans le lobe de votre antenne** quand elle est pointée vers le correspondant : inutile de tourner. Voir [Voûte céleste](Sky-View-fr#avertissements).

### L'efficacité diffère de MCG_MS ou de MS-Soft
YA-MS utilise le trajet réel et son propre modèle ; l'échelle d'OH5IY et de MCG_MS n'est pas documentée en détail. Comparez les heures et les tendances plutôt que les pourcentages absolus, et consultez le [modèle](Efficiency-Calculation-fr#le-modèle).

### Le passage du faisceau GRAVES semble décalé
La séquence du faisceau est calculée à partir de l'horloge du PC : synchronisez-la avec un serveur NTP. La station de commande de GRAVES décale aussi parfois la séquence de quelques pas ; le détail est une prévision à confirmer par l'écoute.

## Autres questions

**YA-MS est-il gratuit ?** Oui, c'est un programme gratuit pour les radioamateurs.

**Pilote-t-il mon rotor ou mon transceiver ?** Non. YA-MS est un outil de prévision et de planification ; utilisez votre programme de modes numériques (par ex. MSHV, WSJT-X) pour le QSO.

**Fonctionne-t-il au-dessus de 432 MHz ?** La liste des bandes s'arrête à 432 MHz (28, 50, 70, 144, 222, 432). La prévision expérimentale accepte toute fréquence de 28 à 1300 MHz, mais les règles de SM6FHZ qu'elle utilise viennent de l'expérience sur 144 et 432 MHz.

**Quelque chose ne va pas.** Écrivez à l'auteur en indiquant votre système d'exploitation, la version de YA-MS et ce que vous avez fait : voir [Contribuer et contacts](Contributing-and-Contacts-fr).
