[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · **Ελληνικά** · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [ไทย](Efficiency-Explanation-th) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Απόδοση - επεξήγηση

*Καρτέλα: Τεχνικά έγγραφα › Απόδοση - επεξήγηση.*

[![Απόδοση - επεξήγηση](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Ένα τεχνικό έγγραφο, *"Come YA-MS calcola l'efficienza di uno sciame"* (Πώς το YA-MS υπολογίζει την απόδοση μιας βροχής μετεώρων), που εμφανίζεται μέσα στο πρόγραμμα ως ανοιχτόχρωμη σελίδα. Εξηγεί **βήμα προς βήμα** πώς προκύπτει η απόδοση και αναφέρει για κάθε βήμα **από πού προέρχεται**. Το έγγραφο είναι προς το παρόν **στα ιταλικά**· αυτό το wiki δίνει το περιεχόμενό του στα ελληνικά στον [Υπολογισμό απόδοσης](Efficiency-Calculation-el#το-μοντέλο) και στη [Γεωμετρία και απώλειες διαδρομής](Geometry-and-Path-Loss-el).

## Ετικέτες

Κάθε βήμα φέρει μια χρωματιστή ετικέτα:

| Ετικέτα | Χρώμα | Σημασία |
|---|---|---|
| **FONTE** (πηγή) | μπλε | το βήμα υιοθετεί μια παρατιθέμενη πηγή· ο αριθμός σε αγκύλες παραπέμπει στη λίστα στο τέλος |
| **RILIEVO** (έλεγχος) | πράσινο | σύγκριση μεταξύ του προγράμματος και των πηγών, με το αποτέλεσμα |
| **SCELTA** (επιλογή) | πορτοκαλί | μια επιλογή του προγράμματος, που δεν προέρχεται από πηγή: πρέπει να ελεγχθεί με την εμπειρία στον αέρα |

## Κεφάλαια

| Κεφάλαιο | Περιεχόμενο |
|---|---|
| 1. Εισαγωγή | Σκοπός, ετικέτες, τι σημαίνει απόδοση (OH5IY, MCG_MS· το YA-MS χρησιμοποιεί την πραγματική διαδρομή) |
| 2. Πού συμβαίνουν οι ανακλάσεις: το στρώμα E | Ίχνη στα 80–120 km· ύψος ίχνους = επικρατούσα τιμή του ιστογράμματος του Collm (έλεγχος: 89,5 km στις 5/11/2026) |
| 3. Γεωμετρία της διαδρομής | Γη και μέσο σημείο· ανύψωση της κεραίας (τύπος του άρθρου)· κοινή ζώνη και τα όριά της· Hot A / Hot B· λοβός κεραίας (DL6WU, Kraus, W4RNL) |
| 4. Το ακτινοβόλο σημείο της βροχής μετεώρων | Θέση του ακτινοβόλου σημείου (IMO 2026/2027), ημερομηνία κορύφωσης (IMO ή ηλιακό μήκος), προφίλ δραστηριότητας |
| 5. Συνθήκη ανάκλασης | Κατοπτρική ανάκλαση (McKinley), γκαουσιανή ανοχή 0,05 rad, βέλτιστος προσανατολισμός (SM6FHZ), τύπος του DH9GCD |
| 6. Από ένα σημείο στην απόδοση | Σημεία ανάκλασης ανά 15 km, βάρος κάθε σημείου, ποσοστό· σύγκριση με το QTFGUI (DJ5HG) |
| 7. Ανάγνωση των αποτελεσμάτων | Πλευρά A / B, δείκτης διαδρομής, χρώματα των ακτινοβόλων σημείων, ζώνες PREV, τομή όπως φαίνεται από την κεραία |
| 8. Συχνότητα εργασίας και απώλειες διαδρομής | Κανόνες λ³ / λ², από το ραντάρ στην ερασιτεχνική μπάντα, αναφορές για τις απώλειες διαδρομής |
| 9. Γνωστά όρια | Μόνο υποπυκνά ίχνη, ισοτροπικές κεραίες, τιμές εργασίας |
| 10. Πηγές | 17 αριθμημένες πηγές |

## Κουμπιά

| Κουμπί | Τι κάνει |
|---|---|
| **Εξαγωγή σε Word (.docx)...** | Αποθηκεύει ένα αντίγραφο του `data/efficienza_spiegazione.docx` όπου επιλέξετε (προτεινόμενο όνομα *YA-MS - calcolo dell'efficienza.docx*) |
| **Άνοιγμα στο Word** | Ανοίγει το ίδιο `.docx` με το προεπιλεγμένο πρόγραμμα για έγγραφα Word (Word, LibreOffice, …) |

## Αρχεία

| Αρχείο | Περιεχόμενο |
|---|---|
| `data/efficienza_spiegazione.txt` | Το κείμενο που εμφανίζεται στην καρτέλα, ένα τμήμα ανά γραμμή (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Η έκδοση Word |
| `doc/YA-MS_manuale_calcoli.docx` | Το **εγχειρίδιο υπολογισμών**: όλες οι εξισώσεις (επεξεργαστής εξισώσεων του Word), αριθμημένες, με τις πηγές τους |

Τα δύο έγγραφα αναπαράγονται από τον πηγαίο κώδικα με `tools/build_spiegazione.py data` και `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
