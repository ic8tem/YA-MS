[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · **Ελληνικά** · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Συνεισφορά και επικοινωνία

Το YA-MS βελτιώνεται χάρη στις αναφορές όσων το χρησιμοποιούν στον αέρα. Κάθε διόρθωση αποδίδεται στην πηγή της.

## Επικοινωνία

| | |
|---|---|
| Συγγραφέας | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Αναφορά προβλήματος

Ανοίξτε ένα **issue στο GitHub** ή στείλτε ένα e-mail με:

- λειτουργικό σύστημα και έκδοση του YA-MS (στον τίτλο του παραθύρου)·
- τα δύο locator, τη μπάντα και την ώρα UTC·
- τι περιμένατε και τι είδατε (ένα στιγμιότυπο οθόνης βοηθά)·
- για προβλήματα με το ραντάρ, το μήνυμα που εμφανίζεται στην καρτέλα [Ροή ραντάρ](Radar-Flux-el).

## Τι είναι ιδιαίτερα χρήσιμο

- **Αναφορές από τον αέρα.** Ώρες και διαδρομές όπου η απόδοση ή η πρόγνωση ήταν σωστές – ή λάθος. Το μοντέλο είναι πειραματικό και χρειάζεται σύγκριση με πραγματικά QSO και με τα MCG_MS / MS-Soft.
- **Συγκρίσεις με RMOB.** Τιμές του συντελεστή σταθμού K και του εκθέτη k που βρήκατε με τη [σύγκριση με RMOB](Experimental-Forecasts-el#σύγκριση-με-rmob), μαζί με τη μπάντα και τον σταθμό σας.
- **Δεδομένα με πηγή.** Καλύτερες ολισθήσεις ακτινοβόλων σημείων, προφίλ δραστηριότητας, νέες ημερομηνίες κορύφωσης IMO (`data/massimi_imo.csv`), δεδομένα κεραιών: αναφέρετε την πηγή και θα παρατεθεί.
- **Αλλαγές στα διαγράμματα του ραντάρ.** Αν αλλάξει η μορφή του διαγράμματος του Collm, ένα αντίγραφο της εικόνας (`data/radar/`) βοηθά να βαθμονομηθεί ξανά η ανάγνωση.

## Μεταφράσεις

Οι μεταφράσεις της διεπαφής είναι απλά αρχεία κειμένου στο **`data/lingue/<code>.txt`** (UTF-8) και **οποιοσδήποτε μπορεί να τις διορθώσει**:

```
<Italian text><TAB><translation>
```

- Μία καταχώριση ανά γραμμή· οι γραμμές που αρχίζουν με `#` είναι σχόλια.
- Και στις δύο στήλες οι δύο χαρακτήρες `\n` σημαίνουν αλλαγή γραμμής.
- Διατηρήστε τα σύμβολα κράτησης θέσης `{0}`, `{1}`, … με τη μορφή τους (π.χ. `{0:F1}`, `{3:+0;-0}`), με τη σειρά που χρειάζεται η γλώσσα σας.
- Οι καταχωρίσεις που λείπουν ή είναι κενές εμφανίζονται στα ιταλικά. Η λίστα όλων των κλειδιών είναι το `data/lingue/chiavi.txt` (παράγεται από το `tools/estrai_chiavi.py`, μην το επεξεργάζεστε).

Επεξεργαστείτε το αρχείο στον φάκελο `data/lingue` της εγκατάστασής σας και επανεκκινήστε το YA-MS (ή αλλάξτε γλώσσα) για να δείτε το αποτέλεσμα. Επειδή αυτά τα αρχεία **αντικαθίστανται από νεότερες εκδόσεις σε κάθε ενημέρωση**, παρακαλούμε **στείλτε και τις διορθώσεις σας** – με e-mail ή ως pull request στο GitHub (`data/lingue/`) – ώστε να μπουν στην επόμενη έκδοση.

Αυτό το wiki υπάρχει σε 36 γλώσσες (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體))· διορθώσεις στις σελίδες του wiki είναι επίσης ευπρόσδεκτες.
