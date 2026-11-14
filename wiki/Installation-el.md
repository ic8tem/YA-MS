[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · **Ελληνικά** · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Εγκατάσταση

Όλα τα πακέτα βρίσκονται στη σελίδα **[Releases](https://github.com/ic8tem/YA-MS/releases)** (στα ονόματα αρχείων παρακάτω το `x.y.z` είναι η έκδοση, π.χ. `1.2.0`). Δεν χρειάζεται να μεταγλωττίσετε τίποτα ούτε να εγκαταστήσετε κάτι άλλο: κάθε πακέτο περιέχει το runtime του .NET 8.

| Σύστημα | Αρχείο | Εγκαθίσταται στο |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (πρόγραμμα εγκατάστασης) | `C:\YA-MS` |
| Windows (64-bit), φορητή έκδοση | `YA-MS-x.y.z-windows-x64-portatile.zip` | οποιονδήποτε φάκελο όπου μπορείτε να γράψετε |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ή `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Windows σε ARM (64 bit, PC με Snapdragon) | `YA-MS-x.y.z-windows-arm64-setup.exe` ή `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| Linux (64-bit), οποιαδήποτε διανομή | `YA-MS-x.y.z-linux-x64.tar.gz` (φορητό ή με `./installa.sh`) | `~/YA-MS` ή οποιονδήποτε φάκελο |
| Linux (64 bit): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` ή οποιονδήποτε φάκελο |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, πακέτο Debian | `ya-ms_x.y.z_arm64.deb` (64-bit) ή `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (αντιγράφεται εκεί στην πρώτη εκκίνηση) |
| Linux ARM 64 bit, οποιαδήποτε διανομή (π.χ. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (φορητό ή με `./installa.sh`) | `~/YA-MS` ή οποιονδήποτε φάκελο |
| Linux armv7l (ARM 32 bit), οποιαδήποτε διανομή | `YA-MS-x.y.z-linux-armv7l.tar.gz` (φορητό ή με `./installa.sh`) | `~/YA-MS` ή οποιονδήποτε φάκελο |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, μόνο η εφαρμογή | `YA-MS-x.y.z-mac-apple-silicon-app.zip` ή `...-mac-intel-app.zip` | ο φάκελος όπου αποσυμπιέζετε το `YA-MS.app` |

**Το πρόγραμμα και ο φάκελος `data` μένουν πάντα μαζί** στον φάκελο του YA-MS: εκεί βρίσκονται όλα τα δεδομένα και οι ρυθμίσεις (χωρίς AppData, χωρίς φακέλους συστήματος). Δείτε [Ρυθμίσεις και φάκελος δεδομένων](Settings-and-Data-Folder-el).

## Windows

### Πρόγραμμα εγκατάστασης
1. Κατεβάστε το `YA-MS-x.y.z-windows-x64-setup.exe` και εκτελέστε το.
2. Αν το **SmartScreen** εμφανίσει «Τα Windows προστάτευσαν τον υπολογιστή σας»: *Περισσότερες πληροφορίες* → *Εκτέλεση οπωσδήποτε* (το πρόγραμμα δεν είναι υπογεγραμμένο με εμπορικό πιστοποιητικό).
3. Το YA-MS εγκαθίσταται στο **`C:\YA-MS`**, **χωρίς δικαιώματα διαχειριστή**, με εικονίδιο στο μενού Έναρξη και, αν το επιλέξετε, εικονίδιο στην επιφάνεια εργασίας.

### Φορητή έκδοση
Αποσυμπιέστε το `YA-MS-x.y.z-windows-x64-portatile.zip` όπου θέλετε (σε φάκελο όπου μπορείτε να γράψετε, όχι στο *Program Files*) και εκτελέστε το `YA-MS.exe`. Μπορείτε να αντιγράψετε ολόκληρο τον φάκελο σε ένα USB stick ή σε άλλον υπολογιστή.

## Linux

1. Αποσυμπιέστε το `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Από τον φάκελο που αποσυμπιέστηκε εκτελέστε:
   ```sh
   ./installa.sh
   ```
3. Το script αντιγράφει το YA-MS στο **`~/YA-MS`** (δεν χρειάζεται root) και προσθέτει το **YA-MS** στο μενού εφαρμογών (κατηγορία *HamRadio*). Μπορείτε επίσης να το ξεκινήσετε με `~/YA-MS/YA-MS`.

### Πακέτο Debian (.deb)
Σε Debian, Ubuntu, Mint και Raspberry Pi OS μπορείτε εναλλακτικά να εγκαταστήσετε το `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` στο Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Το πακέτο τοποθετεί το πρόγραμμα στο `/opt/ya-ms` και προσθέτει το **YA-MS** στο μενού. Στην πρώτη εκκίνηση (και μετά από κάθε νέα έκδοση) αντιγράφεται στο **`~/YA-MS`** και εκτελείται από εκεί, ώστε ο φάκελος `data` να μένει δίπλα στο πρόγραμμα και να διατηρούνται οι ρυθμίσεις σας.

### Φορητή έκδοση
Το `.tar.gz` λειτουργεί και χωρίς εγκατάσταση: αποσυμπιέστε το οπουδήποτε μπορείτε να γράψετε και εκτελέστε το `./YA-MS` από εκείνον τον φάκελο.

Για ιαπωνικό κείμενο μπορεί να χρειαστείτε τις γραμματοσειρές Noto CJK: δείτε [Επίλυση προβλημάτων](Troubleshooting-FAQ-el#linux-το-ιαπωνικό-κείμενο-εμφανίζεται-ως-κουτάκια).

## Raspberry Pi

Ίδια διαδικασία με το Linux: αποσυμπιέστε το `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (ή το `-32bit` σε Raspberry Pi OS 32-bit) και εκτελέστε το `./installa.sh` από τον φάκελο που αποσυμπιέστηκε.

- Για να δείτε ποιο σύστημα έχετε, πληκτρολογήστε `uname -m` σε ένα τερματικό: `aarch64` → πακέτο 64-bit, `armv7l` → πακέτο 32-bit.
- Υποστηρίζονται: Raspberry Pi 2 (μόνο 32-bit), 3, 4, 5, 400 και 500, με την έκδοση desktop του Raspberry Pi OS. **Δεν υποστηρίζονται:** Pi Zero / Zero W και Pi 1 (επεξεργαστής ARMv6, το .NET δεν τρέχει εκεί)· το Pi Zero 2 W λειτουργεί με το πακέτο 64-bit, αλλά τα 512 MB RAM είναι οριακά.
- Συνιστάται Pi 4 ή 5 με τουλάχιστον 2 GB RAM· η πρώτη εκκίνηση διαρκεί λίγα δευτερόλεπτα περισσότερο απ' ό,τι σε PC.

## macOS

1. Επιλέξτε το σωστό αρχείο: `-mac-apple-silicon.dmg` για επεξεργαστές M1/M2/M3/M4, `-mac-intel.dmg` για Mac με Intel.
2. Ανοίξτε το `.dmg`, κάντε **δεξί κλικ στο "Installa YA-MS.command" → Άνοιγμα** και επιβεβαιώστε.
3. Το script αντιγράφει το `YA-MS.app` στο **`~/YA-MS`** και το ανοίγει.

Εναλλακτικά, το `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` περιέχει μόνο το `YA-MS.app`: αποσυμπιέστε το σε έναν φάκελο της επιλογής σας (όπου μπορείτε να γράψετε)· ο φάκελος `data` δημιουργείται δίπλα στο `YA-MS.app`. Την πρώτη φορά, δεξί κλικ → **Άνοιγμα**.

Το πρόγραμμα δεν είναι υπογεγραμμένο από την Apple, οπότε την πρώτη φορά το macOS ζητά επιβεβαίωση· δείτε [Επίλυση προβλημάτων](Troubleshooting-FAQ-el#macos-δεν-μπορεί-να-ανοίξει-επειδή-προέρχεται-από-μη-αναγνωρισμένο-προγραμματιστή).

## Πρώτη εκκίνηση

- Ο **χάρτης της Ευρώπης** (ακτογραμμές και σύνορα του Natural Earth) κατεβαίνει αυτόματα στο `data/mappa` την πρώτη φορά: χρειάζεται σύνδεση στο διαδίκτυο μία φορά.
- Τα **δεδομένα ραντάρ** (Collm, Sodankylä) κατεβαίνουν αμέσως και στη συνέχεια ελέγχονται κάθε 5 λεπτά.
- Η διεπαφή ξεκινά στη γλώσσα του συστήματός σας αν είναι μία από τις 36 διαθέσιμες, αλλιώς στα ιταλικά· αλλάξτε την πάνω δεξιά (δείτε [Ρυθμίσεις](Settings-and-Data-Folder-el#γλώσσα)).

## Ενημέρωση

Εγκαταστήστε τη νέα έκδοση **πάνω από την παλιά** (ίδιο πρόγραμμα εγκατάστασης, ίδιος φάκελος). Οι ρυθμίσεις (`config.ini`), τα αρχεία ροής και ο χάρτης μένουν στο `data`. Τα αρχεία μετάφρασης στο `data/lingue` αντικαθίστανται όταν τα νέα είναι πιο πρόσφατα.

**Από την 1.8.0 το YA-MS ενημερώνεται μόνο του.** Κατά την εκκίνηση, μία φορά την ημέρα, ελέγχει στο GitHub αν υπάρχει νέα έκδοση και την προτείνει· το κουμπί **Ενημερώσεις** στην κάτω γραμμή κάνει τον έλεγχο χειροκίνητα. Το *Ενημέρωση τώρα* κατεβάζει το φορητό πακέτο για το σύστημά σας, αντικαθιστά τα αρχεία του προγράμματος, κρατά τον φάκελο `data` (τα αρχεία του προγράμματος που αλλάζουν αντιγράφονται πρώτα στο `data/backup/v<παλιά έκδοση>`) και επανεκκινείται· ο φάκελος του προγράμματος πρέπει να είναι εγγράψιμος. Αν κατά την εκκίνηση λείπουν αρχεία του προγράμματος (στο `data` ή στο `doc`), ένα παράθυρο τα απαριθμεί και προτείνει να τα κατεβάσει ξανά από το GitHub. Για να μην αναζητούνται νέες εκδόσεις, ορίστε `controlla_aggiornamenti=0` στο `config.ini`.

Από την έκδοση 1.8.6 οι ενημερώσεις είναι αυτόματες και σιωπηλές: κατά την εκκίνηση και μετά κάθε 30 λεπτά το YA-MS ελέγχει το GitHub και, αν υπάρχει νέα έκδοση, την κατεβάζει, την εγκαθιστά και επανεκκινείται μόνο του χωρίς να ρωτήσει τίποτα (το δείχνει μόνο η γραμμή κατάστασης). Και τα αρχεία που λείπουν κατεβαίνουν ξανά χωρίς ερώτηση. Το παράθυρο που περιγράφεται παρακάτω εμφανίζεται μόνο πατώντας "Ενημερώσεις" ή αν γράψεις aggiornamenti_automatici=0 στο αρχείο data/config.ini.

## Μεταγλώττιση από τον πηγαίο κώδικα (μόνο για προγραμματιστές)

Τα προγράμματα εγκατάστασης παράγονται από το GitHub Actions (`.github/workflows/build.yml`) σε κάθε ενημέρωση του κλάδου `release` (η έκδοση λαμβάνεται από το αρχείο `VERSION`), το οποίο δημιουργεί επίσης το release `vX.Y.Z`. Τοπικά:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Τα έγγραφα (όλες οι γλώσσες) αναπαράγονται με `tools/build_documenti.sh`.

Επόμενο: [Πρώτα βήματα](Getting-Started-el).
