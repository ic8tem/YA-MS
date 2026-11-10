[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · **Ελληνικά** · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Βροχές μετεώρων

*Καρτέλα: Βροχές μετεώρων.*

[![Βροχές μετεώρων](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Ο κατάλογος βροχών που χρησιμοποιείται σε όλους τους υπολογισμούς: **45 βροχές** από το **IMO Meteor Shower Calendar 2026 και 2027** (πίνακες 5 και 7) συν την **Antihelion Source** (πίνακας 6), καθεμία με την **επόμενη κορύφωσή** της.

## Στήλες

| Στήλη | Σημασία |
|---|---|
| Κωδικός | Κωδικός IMO (QUA, PER, GEM, …) |
| Βροχή | Όνομα |
| Δραστηριότητα | Περίοδος δραστηριότητας (ημέρα/μήνας – ημέρα/μήνας) |
| λ max | Ηλιακό μήκος της κορύφωσης (J2000), από το IMO |
| **Επόμενη κορύφωση (UTC)** | Ημερομηνία και ώρα της επόμενης κορύφωσης (δείτε παρακάτω) |
| **Πηγή κορύφωσης** | *IMO 2026* / *IMO 2027* = ημερομηνία και ώρα που δημοσίευσε το IMO· *IMO 2026 (ημέρα)* = το IMO δίνει μόνο την ημέρα, η ώρα που εμφανίζεται είναι υπολογισμένη (*~ωω:λλ υπολ.*)· *υπολογισμένο από λ* = δεν υπάρχει τιμή IMO για εκείνο το έτος |
| R.A., Dec. | Ακτινοβόλο σημείο στην κορύφωση (*κινούμενο* για την Antihelion Source) |
| v km/s, r | Γεωκεντρική ταχύτητα και δείκτης πληθυσμού |
| ZHR | ZHR κορύφωσης (*μεταβλ.* = μεταβλητό) |
| Τύπος | *οπτική* ή *ραδιο, ημερήσια* |

Οι βροχές που είναι **ενεργές σήμερα (UTC)** επισημαίνονται με κίτρινο πέπλο και έντονο κείμενο.

## Επόμενη κορύφωση

Το πρόγραμμα δείχνει πάντα την **επόμενη** κορύφωση. Όταν το IMO έχει δημοσιεύσει το ημερολόγιο εκείνου του έτους, χρησιμοποιεί την **ημερομηνία και ώρα του IMO** από το `data/massimi_imo.csv` (περιλαμβάνονται τα 2026 και 2027)· διαφορετικά υπολογίζει τη στιγμή κατά την οποία ο Ήλιος φτάνει στο ηλιακό μήκος της κορύφωσης (Meeus, *Astronomical Algorithms*, κεφ. 25, με επίλυση με τη μέθοδο Newton).

**Έλεγχος:** ο υπολογισμός συμφωνεί με τα ημερολόγια IMO 2026 και 2027 με απόκλιση λίγων λεπτών όπου το IMO δίνει την ώρα (π.χ. Τεταρτημορίδες 3/1/2026 21:13 έναντι 21:00· Διδυμίδες 14/12/2027 19:51 έναντι 20:00). Εξαιρέσεις: οι Daytime kappa Leonids 2026 μία ημέρα αργότερα (26/9 αντί για 25/9) και η ώρα των eta Aquariids 2027 (15:10 έναντι 09:00 του IMO) – σε αυτές τις περιπτώσεις χρησιμοποιείται η τιμή του IMO.

**Προσθήκη έτους:** όταν το IMO δημοσιεύσει νέο ημερολόγιο, προσθέστε τις γραμμές του στο `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, ώρα κενή αν το IMO δίνει μόνο την ημέρα). Μέχρι τότε η κορύφωση υπολογίζεται.

## Δευτερεύουσες και ημερήσιες βροχές

Ο κατάλογος περιλαμβάνει τις **δευτερεύουσες βροχές** της λίστας του IMO – για παράδειγμα τις October Camelopardalids (OCT, ZHR 5, ενεργές 5–6 Οκτωβρίου), τις Ανδρομεδίδες, τις gamma Ursae Minorids – και τις **ημερήσιες ραδιοβροχές** Απριλίου–Οκτωβρίου (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Ακόμη και με μικρά ZHR συνεισφέρουν στον [δείκτη διαδρομής](Efficiency-Calculation-el#το-μοντέλο) και στο [συνιστώμενο Hot](Sky-View-el#συνιστώμενο-hot). Για τις ημερήσιες ραδιοβροχές το IMO δεν δίνει ZHR: όπου δεν δίνεται, το πρόγραμμα χρησιμοποιεί τιμή εργασίας 5.

## Προφίλ δραστηριότητας και ολίσθηση του ακτινοβόλου σημείου

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

Τα ZHR_max, α0, δ0 και λ_max προέρχονται από το ημερολόγιο του IMO· οι κλίσεις B (διαφορετικές πριν και μετά την κορύφωση) και οι ημερήσιες ολισθήσεις dα/dλ, dδ/dλ είναι **τιμές εργασίας** γραμμένες στο `data/sciami.csv` (ο πίνακας ολισθήσεων του IMO δεν έχει εισαχθεί ακόμη). *Εγχειρίδιο εξ. 9 και 13.* Η θέση της Antihelion Source παρεμβάλλεται γραμμικά ανάμεσα στις ημερομηνίες του πίνακα 6 του IMO (`data/ant_radiante.csv`· ενεργή 10 Δεκεμβρίου – 20 Σεπτεμβρίου, ZHR περίπου 4).

## Επεξεργασία του καταλόγου

Το `data/sciami.csv` είναι ένα απλό αρχείο κειμένου (διαχωριστικό `;`) που μπορείτε να επεξεργαστείτε: κωδικός, όνομα, αρχή και τέλος (MM-DD), λ max, R.A., Dec., ολισθήσεις, v, r, ZHR, B πριν/μετά, τύπος (V οπτική, R ημερήσια ραδιο). Αν μια γραμμή είναι λανθασμένη, το πρόγραμμα εμφανίζει μήνυμα κατά την εκκίνηση και την αγνοεί.

Πηγές: International Meteor Organization – Meteor Shower Calendar 2026 και 2027, [www.imo.net](https://www.imo.net) (πίνακες 5, 6 και 7)· Rossano IZ5TEK (scattertek).
