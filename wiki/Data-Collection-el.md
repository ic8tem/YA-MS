[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · **Ελληνικά** · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Συλλογή δεδομένων

*Καρτέλα: Ζωντανά δεδομένα και πραγματικός χρόνος › Συλλογή δεδομένων.*

[![Συλλογή δεδομένων](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Τέσσερις πηγές

Η καρτέλα συλλέγει **spots meteor scatter** από τρεις ροές telnet και από τη ροή MQTT του PSKReporter, καθεμία στη δική της υποκαρτέλα:

| Υποκαρτέλα | Προεπιλογή | Σημειώσεις |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Ένα cluster της επιλογής σας. Στο ON0DXK οι μπάντες VHF φιλτράρονται: ενεργοποιήστε τις με `set/filter dxbm/pass 6` (μετά 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Οι skimmers σπάνια αποκωδικοποιούν modes MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X που μεταφέρει τα spots του **PSKReporter**: εδώ φτάνουν οι αποκωδικοποιήσεις MSK144 των WSJT-X και MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spots του PSKReporter σε πραγματικό χρόνο μέσω **MQTT** (υπηρεσία του M0LTE): χωρίς login, κάθε spot περιέχει ήδη τα locator του σταθμού εκπομπής και του σταθμού λήψης. Προεπιλεγμένα topics: MSK144 στα 6 m, 4 m, 2 m, 1,25 m, 70 cm και FSK441 στα 2 m (`pskr/filter/v2/band/mode/#`)· το *Προεπιλεγμένα topics* τα επαναφέρει. |
| **Spots MS που συλλέχθηκαν** | – | Πίνακας των αποδεκτών spots, τα νεότερα πρώτα. |

Κάθε ροή έχει host, θύρα, εντολές που αποστέλλονται μετά το login, *Επανασύνδεση*, *Σύνδεση κατά την εκκίνηση*, μια κονσόλα και μια γραμμή για αποστολή εντολών. Γράψτε το **διακριτικό κλήσης σας για το login** στο πάνω μέρος. Η πηγή MQTT έχει host, θύρα, topics (ένα ανά γραμμή ή χωρισμένα με `;`), *Επανασύνδεση* και *Σύνδεση κατά την εκκίνηση* (απενεργοποιημένο από προεπιλογή) και μια κονσόλα με τα spots που λαμβάνονται· τα spots της περνούν από το ίδιο φίλτρο. Μια λωρίδα δείχνει την κατάσταση των τεσσάρων πηγών (πράσινη κουκκίδα = συνδεδεμένη). Οι συνεδρίες μένουν ανοιχτές όταν αλλάζετε γλώσσα ή χρωματικό συνδυασμό.

## Το φίλτρο (40 % του παραθύρου)

- **Προαιρετικό τοπικό φίλτρο:** οι γραμμές του cluster κάτω από **27990,0 kHz** απορρίπτονται αμέσως (δεν εμφανίζονται, δεν αποθηκεύονται).
- Τα spots CW απορρίπτονται αμέσως (CW ή WPM στο σχόλιο, ή 28000-28070 kHz): δεν εμφανίζονται στην κονσόλα και δεν αποθηκεύονται, εκτός αν έχουν την ένδειξη <MS>. Το πλαίσιο μπορεί να απενεργοποιηθεί.

Βάση CALL3 με τους κανόνες του LIVETROPOVHF. Το «Ενημέρωση τώρα» κατεβάζει το CALL3.TXT από το MMMonVHF (τουλάχιστον 100.000 έγκυρες γραμμές, το προηγούμενο μένει στο data/call3.bak)· με το «Αυτόματη ενημέρωση κάθε 7 ημέρες» γίνεται στην εκκίνηση. Πάνω από το αρχείο ισχύουν με σειρά: χειροκίνητες καταχωρίσεις (data/CALL3-MANUALE.TXT), διορθώσεις από cluster (ο 6ψήφιος locator που δηλώνει για τον εαυτό του όποιος κάνει spot), πρόσθετα αρχεία (data/CALL3-AGGIUNTE), μετά το CALL3.TXT και οι 6ψήφιοι locator που μάθαμε ζωντανά (data/LOC6.TXT). Ένας ληφθείς 4ψήφιος locator, ή που λήγει σε LL ή MM, αντικαθίσταται από τον 6ψήφιο της βάσης· οι φορητοί (με κάθετο) μόνο με ακριβή καταχώριση.

Τελευταία πηγή, όπως στο LIVETROPOVHF: για διακριτικά χωρίς 6ψήφιο locator σε καμία άλλη πηγή, το πρόγραμμα ρωτά στο παρασκήνιο το δημόσιο API του G7VRD (api.g7vrd.co.uk). Γίνεται δεκτός μόνο 6ψήφιος locator, όχι το κέντρο του τετραγώνου (LL ή MM), στο ίδιο τετράγωνο με τον ληφθέντα· το πολύ 40 διακριτικά το λεπτό, το καθένα μία φορά την ημέρα. Τα αποτελέσματα βρίσκονται στο data/CALL3-G7VRD.TXT.
- Τα spot μεταξύ σταθμών που απέχουν λιγότερο από 500 km απορρίπτονται αμέσως, επειδή σε αυτή την απόσταση η ζεύξη είναι απευθείας ή τροποσφαιρική και όχι meteor scatter: δεν εμφανίζονται στην κονσόλα και δεν αποθηκεύονται. Αν λείπει ένας locator, το spot διατηρείται. Η απόσταση αλλάζει κάτω από το πλαίσιο.
- **1ο κριτήριο – τυπικές συχνότητες MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Ένα spot μέσα σε αυτά τα παράθυρα γίνεται δεκτό ακόμη και χωρίς όνομα mode, εκτός αν το σχόλιο δηλώνει άλλη διάδοση: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Τα παράθυρα και οι ετικέτες μπορούν να τροποποιηθούν.
- **2ο κριτήριο – modes MS:** έξω από τα παράθυρα, ή με μία από αυτές τις ετικέτες, ένα spot κρατιέται μόνο αν περιέχει **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (ψηφιακά modes που χρησιμοποιούνται μόνο για MS) ή **\<MS\>**, με κεφαλαία, πεζά ή ανάμεικτα. Οι λέξεις μπορούν να απενεργοποιηθούν, να προστεθούν και να αφαιρεθούν· καθεμία έχει τον μετρητή της.
- **Μπάντες** 28, 50, 70, 144, 222, 432 MHz· **δοκιμή φίλτρου** σε μια γραμμή που επικολλάτε· **μετρητές**.

## Locator και αποθήκευση

Τα locator που λείπουν, ή που έχουν μόνο 4 χαρακτήρες, λαμβάνονται από το αρχείο **CALL3** (`data/call3.txt`, αρχείο του JTDX, πάνω από ένα εκατομμύριο διακριτικά κλήσης), το οποίο υπερισχύει πάντα ενός locator 4 χαρακτήρων. Τα αποδεκτά spots αποθηκεύονται στο `data/spot_ms`, ένα αρχείο CSV ανά ημέρα, και τροφοδοτούν τον χάρτη [Ζωντανή κίνηση](Live-Traffic-el).
