[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · **Français** · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Installation

Tous les paquets se trouvent sur la page **[Releases](https://github.com/ic8tem/YA-MS/releases)** (dans les noms de fichiers ci-dessous, `x.y.z` est la version, par ex. `1.2.0`). Rien à compiler ni à installer en plus : chaque paquet contient le runtime .NET 8.

| Système | Fichier | S'installe dans |
|---|---|---|
| Windows (64 bits) | `YA-MS-x.y.z-windows-x64-setup.exe` (installeur) | `C:\YA-MS` |
| Windows (64 bits), portable | `YA-MS-x.y.z-windows-x64-portatile.zip` | tout dossier où vous pouvez écrire |
| Windows (32 bits, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ou `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows sur ARM (64 bits, PC avec Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` ou `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 bits) : Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copié là au premier démarrage) |
| Linux (64 bits), toute distribution | `YA-MS-x.y.z-linux-x64.tar.gz` (portable ou avec `./installa.sh`) | `~/YA-MS` ou tout dossier |
| Linux (64 bits) : Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (copié là au premier démarrage) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (copié là au premier démarrage) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (copié là au premier démarrage) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (copié là au premier démarrage) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` ou tout dossier |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bits) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bits) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, paquet Debian | `ya-ms_x.y.z_arm64.deb` (64 bits) ou `ya-ms_x.y.z_armhf.deb` (32 bits) | `~/YA-MS` (copié là au premier démarrage) |
| Linux ARM 64 bits, toute distribution (p. ex. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (portable ou avec `./installa.sh`) | `~/YA-MS` ou tout dossier |
| Linux armv7l (ARM 32 bits), toute distribution | `YA-MS-x.y.z-linux-armv7l.tar.gz` (portable ou avec `./installa.sh`) | `~/YA-MS` ou tout dossier |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, application seule | `YA-MS-x.y.z-mac-apple-silicon-app.zip` ou `...-mac-intel-app.zip` | le dossier où vous décompressez `YA-MS.app` |

**Le programme et son dossier `data` restent toujours ensemble** dans le dossier YA-MS : toutes les données et tous les réglages s'y trouvent (pas d'AppData, pas de dossiers système). Voir [Réglages et dossier des données](Settings-and-Data-Folder-fr).

## Windows

### Installeur
1. Téléchargez `YA-MS-x.y.z-windows-x64-setup.exe` et lancez-le.
2. Si **SmartScreen** affiche « Windows a protégé votre ordinateur » : *Informations complémentaires* → *Exécuter quand même* (le programme n'est pas signé avec un certificat commercial).
3. YA-MS s'installe dans **`C:\YA-MS`**, **sans droits d'administrateur**, avec une icône dans le menu Démarrer et, si vous cochez la case, une icône sur le bureau.

### Portable
Décompressez `YA-MS-x.y.z-windows-x64-portatile.zip` où vous voulez (un dossier où vous pouvez écrire, pas *Program Files*) et lancez `YA-MS.exe`. Vous pouvez copier tout le dossier sur une clé USB ou sur un autre ordinateur.

## Linux

1. Décompressez `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Depuis le dossier décompressé, lancez :
   ```sh
   ./installa.sh
   ```
3. Le script copie YA-MS dans **`~/YA-MS`** (pas besoin de root) et ajoute **YA-MS** au menu des applications (catégorie *HamRadio*). Vous pouvez aussi le lancer avec `~/YA-MS/YA-MS`.

### Paquet Debian (.deb)
Sous Debian, Ubuntu, Mint et Raspberry Pi OS, vous pouvez plutôt installer `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` sur le Raspberry Pi) :
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Le paquet place le programme dans `/opt/ya-ms` et ajoute **YA-MS** au menu. Au premier démarrage (et après chaque nouvelle version), il se copie dans **`~/YA-MS`** et s'exécute depuis là : le dossier `data` reste ainsi à côté du programme et vos réglages sont conservés.

### Portable
Le `.tar.gz` fonctionne aussi sans installation : décompressez-le n'importe où vous pouvez écrire et lancez `./YA-MS` depuis ce dossier.

Pour le texte japonais, il faut parfois les polices Noto CJK : voir [Dépannage](Troubleshooting-FAQ-fr#sous-linux-le-texte-japonais-saffiche-en-carrés).

## Raspberry Pi

Même procédure que sous Linux : décompressez `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (ou `-32bit` sous Raspberry Pi OS 32 bits) et lancez `./installa.sh` depuis le dossier décompressé.

- Pour savoir quel système vous avez, tapez `uname -m` dans un terminal : `aarch64` → paquet 64 bits, `armv7l` → paquet 32 bits.
- Pris en charge : Raspberry Pi 2 (32 bits uniquement), 3, 4, 5, 400 et 500, avec la version bureau de Raspberry Pi OS. **Non pris en charge :** Pi Zero / Zero W et Pi 1 (processeur ARMv6, .NET n'y fonctionne pas) ; le Pi Zero 2 W fonctionne avec le paquet 64 bits, mais 512 Mo de RAM, c'est juste.
- Un Pi 4 ou 5 avec au moins 2 Go de RAM est recommandé ; le premier démarrage prend quelques secondes de plus que sur un PC.

## macOS

1. Choisissez le bon fichier : `-mac-apple-silicon.dmg` pour les processeurs M1/M2/M3/M4, `-mac-intel.dmg` pour les Mac Intel.
2. Ouvrez le `.dmg`, faites **clic droit sur « Installa YA-MS.command » → Ouvrir** et confirmez.
3. Le script copie `YA-MS.app` dans **`~/YA-MS`** et l'ouvre.

Autre possibilité : `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` ne contient que `YA-MS.app` ; décompressez-le dans un dossier de votre choix (où vous pouvez écrire) ; le dossier `data` est créé à côté de `YA-MS.app`. La première fois, clic droit → **Ouvrir**.

Le programme n'est pas signé par Apple : la première fois, macOS demande donc une confirmation ; voir [Dépannage](Troubleshooting-FAQ-fr#sous-macos-impossible-douvrir-un-programme-dun-développeur-non-identifié).

## Premier démarrage

- La **carte d'Europe** (côtes et frontières Natural Earth) est téléchargée automatiquement dans `data/mappa` la première fois : une connexion internet est nécessaire une seule fois.
- Les **données radar** (Collm, Sodankylä) sont téléchargées immédiatement, puis vérifiées toutes les 5 minutes.
- L'interface démarre dans la langue de votre système si c'est l'une des 36 disponibles, sinon en italien ; changez-la en haut à droite (voir [Réglages](Settings-and-Data-Folder-fr#langue)).

## Mise à jour

Installez la nouvelle version **par-dessus l'ancienne** (même installeur, même dossier). Les réglages (`config.ini`), les archives du flux et la carte restent dans `data`. Les fichiers de traduction de `data/lingue` sont remplacés quand les nouveaux sont plus récents.

**Depuis la 1.8.0, YA-MS se met à jour tout seul.** Au démarrage, une fois par jour, il vérifie sur GitHub s'il existe une nouvelle version et la propose ; le bouton **Mises à jour** dans la barre du bas fait la vérification à la main. *Mettre à jour maintenant* télécharge le paquet portable de votre système, remplace les fichiers du programme, conserve le dossier `data` (les fichiers du programme modifiés sont d'abord copiés dans `data/backup/v<ancienne version>`) et redémarre ; il faut pouvoir écrire dans le dossier du programme. S'il manque des fichiers du programme au démarrage (dans `data` ou `doc`), une fenêtre les liste et propose de les télécharger à nouveau depuis GitHub. Pour ne plus chercher de nouvelles versions, mettez `controlla_aggiornamenti=0` dans `config.ini`.

Depuis la version 1.8.6, les mises à jour sont automatiques et silencieuses : au démarrage puis toutes les 6 heures, YA-MS consulte GitHub et, s'il y a une nouvelle version, la télécharge, l'installe et redémarre tout seul sans rien demander (seule la barre d'état l'indique). Les fichiers manquants sont aussi retéléchargés sans demander. La fenêtre décrite ci-dessous n'apparaît qu'en appuyant sur "Mises à jour" ou si vous écrivez aggiornamenti_automatici=0 dans le fichier data/config.ini.

## Compilation depuis les sources (développeurs uniquement)

Les installeurs sont produits par GitHub Actions (`.github/workflows/build.yml`) à chaque mise à jour de la branche `release` (version tirée du fichier `VERSION`), qui crée aussi la release `vX.Y.Z`. En local :

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # ou linux-x64, linux-arm64, linux-arm, osx-arm64
```

Les documents (toutes les langues) sont régénérés avec `tools/build_documenti.sh`.

Suite : [Premiers pas](Getting-Started-fr).
