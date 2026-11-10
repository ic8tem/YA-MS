[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · **Ελληνικά** · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Εγκατάσταση

Όλα τα πακέτα βρίσκονται στη σελίδα **[Releases](https://github.com/ic8tem/YA-MS/releases)** (στα ονόματα αρχείων παρακάτω το `x.y.z` είναι η έκδοση, π.χ. `1.2.0`). Δεν χρειάζεται μεταγλώττιση ούτε εγκατάσταση οτιδήποτε άλλου: κάθε πακέτο περιέχει το runtime του .NET 8.

| Σύστημα | Αρχείο | Εγκαθίσταται στο |
|---|---|---|
| Windows (64 bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (πρόγραμμα εγκατάστασης) | `C:\YA-MS` |
| Windows (64 bit), φορητό | `YA-MS-x.y.z-windows-x64-portatile.zip` | οποιονδήποτε φάκελο όπου μπορείτε να γράψετε |
| Windows (32 bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ή `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Το πρόγραμμα και ο φάκελός του `data` μένουν πάντα μαζί** στον φάκελο YA-MS: εκεί βρίσκονται όλα τα δεδομένα και οι ρυθμίσεις (χωρίς AppData, χωρίς φακέλους συστήματος). Δείτε [Ρυθμίσεις και φάκελος δεδομένων](Settings-and-Data-Folder-el).

## Windows

### Πρόγραμμα εγκατάστασης
1. Κατεβάστε το `YA-MS-x.y.z-windows-x64-setup.exe` και εκτελέστε το.
2. Αν το **SmartScreen** εμφανίσει «Τα Windows προστάτευσαν τον υπολογιστή σας»: *Περισσότερες πληροφορίες* → *Εκτέλεση οπωσδήποτε* (το πρόγραμμα δεν είναι υπογεγραμμένο με εμπορικό πιστοποιητικό).
3. Το YA-MS εγκαθίσταται στο **`C:\YA-MS`**, **χωρίς δικαιώματα διαχειριστή**, με εικονίδιο στο μενού Έναρξη και, αν το επιλέξετε, εικονίδιο στην επιφάνεια εργασίας.

### Φορητή έκδοση
Αποσυμπιέστε το `YA-MS-x.y.z-windows-x64-portatile.zip` όπου θέλετε (σε φάκελο όπου μπορείτε να γράψετε, όχι στο *Program Files*) και εκτελέστε το `YA-MS.exe`. Μπορείτε να αντιγράψετε ολόκληρο τον φάκελο σε ένα USB stick ή σε άλλον υπολογιστή.

## Linux

1. Αποσυμπιέστε το `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Από τον φάκελο που αποσυμπιέσατε εκτελέστε:
   ```sh
   ./installa.sh
   ```
3. Το script αντιγράφει το YA-MS στο **`~/YA-MS`** (δεν χρειάζεται root) και προσθέτει το **YA-MS** στο μενού εφαρμογών (κατηγορία *HamRadio*). Μπορείτε επίσης να το εκκινήσετε με `~/YA-MS/YA-MS`.

Για το ιαπωνικό κείμενο μπορεί να χρειαστείτε τις γραμματοσειρές Noto CJK: δείτε [Αντιμετώπιση προβλημάτων](Troubleshooting-FAQ-el#linux-το-ιαπωνικό-κείμενο-εμφανίζεται-ως-τετραγωνάκια).

## Raspberry Pi

Ίδια διαδικασία με το Linux: αποσυμπιέστε το `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (ή το `-32bit` σε Raspberry Pi OS 32 bit) και εκτελέστε `./installa.sh` από τον φάκελο που αποσυμπιέσατε.

- Για να δείτε ποιο σύστημα έχετε, πληκτρολογήστε `uname -m` σε ένα τερματικό: `aarch64` → πακέτο 64 bit, `armv7l` → πακέτο 32 bit.
- Υποστηρίζονται: Raspberry Pi 2 (μόνο 32 bit), 3, 4, 5, 400 και 500, με την έκδοση desktop του Raspberry Pi OS. **Δεν υποστηρίζονται:** Pi Zero / Zero W και Pi 1 (επεξεργαστής ARMv6, το .NET δεν τρέχει εκεί)· το Pi Zero 2 W λειτουργεί με το πακέτο 64 bit, αλλά τα 512 MB RAM είναι οριακά.
- Συνιστάται Pi 4 ή 5 με τουλάχιστον 2 GB RAM· η πρώτη εκκίνηση διαρκεί λίγα δευτερόλεπτα περισσότερο απ' ό,τι σε PC.

## macOS

1. Επιλέξτε το σωστό αρχείο: `-mac-apple-silicon.dmg` για επεξεργαστές M1/M2/M3/M4, `-mac-intel.dmg` για Mac με Intel.
2. Ανοίξτε το `.dmg`, **δεξί κλικ στο «Installa YA-MS.command» → Άνοιγμα** και επιβεβαιώστε.
3. Το script αντιγράφει το `YA-MS.app` στο **`~/YA-MS`** και το ανοίγει.

Το πρόγραμμα δεν είναι υπογεγραμμένο από την Apple, γι' αυτό την πρώτη φορά το macOS ζητά επιβεβαίωση· δείτε [Αντιμετώπιση προβλημάτων](Troubleshooting-FAQ-el#macos-δεν-μπορεί-να-ανοίξει-επειδή-είναι-από-μη-ταυτοποιημένο-προγραμματιστή).

## Πρώτη εκκίνηση

- Ο **χάρτης της Ευρώπης** (ακτογραμμές και σύνορα του Natural Earth) κατεβαίνει αυτόματα στο `data/mappa` την πρώτη φορά: χρειάζεται σύνδεση στο διαδίκτυο μία φορά.
- Τα **δεδομένα ραντάρ** (Collm, Sodankylä) κατεβαίνουν αμέσως και στη συνέχεια ελέγχονται κάθε 5 λεπτά.
- Η διεπαφή ξεκινά στη γλώσσα του συστήματός σας αν είναι μία από τις 36 διαθέσιμες, αλλιώς στα ιταλικά· αλλάξτε τη πάνω δεξιά (δείτε [Ρυθμίσεις](Settings-and-Data-Folder-el#γλώσσα)).

## Ενημέρωση

Εγκαταστήστε τη νέα έκδοση **πάνω από την παλιά** (ίδιο πρόγραμμα εγκατάστασης, ίδιος φάκελος). Οι ρυθμίσεις (`config.ini`), τα αρχεία ροής και ο χάρτης παραμένουν στο `data`. Τα αρχεία μετάφρασης στο `data/lingue` αντικαθίστανται όταν τα νέα είναι πιο πρόσφατα.

## Μεταγλώττιση από τον πηγαίο κώδικα (μόνο για προγραμματιστές)

Τα προγράμματα εγκατάστασης παράγονται από το GitHub Actions (`.github/workflows/build.yml`) σε κάθε ενημέρωση του κλάδου `release` (η έκδοση λαμβάνεται από το αρχείο `VERSION`), το οποίο δημιουργεί και το release `vX.Y.Z`. Τοπικά:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # or linux-x64, linux-arm64, linux-arm, osx-arm64
```

Τα έγγραφα αναπαράγονται με `tools/build_spiegazione.py data` και `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Επόμενο: [Πρώτα βήματα](Getting-Started-el).
