**English** · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Χάρτης τετραγώνων

*Καρτέλα: Χάρτης τετραγώνων.*

[![Χάρτης τετραγώνων](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Τα τετράγωνα Maidenhead (4 χαρακτήρες) που έχετε **δουλέψει** και **επιβεβαιώσει**, όπως διαβάζονται από το αρχείο ADIF του ημερολογίου σας, πάνω σε έναν χάρτη της Ευρώπης – **μία υποκαρτέλα ανά μπάντα: 50, 70, 144, 222 και 432 MHz**.

## Χειριστήρια

| Χειριστήριο | Τι κάνει |
|---|---|
| **Φόρτωση αρχείου ADIF...** | Διαβάζει ένα αρχείο `.adi` / `.adif`. Ένα νέο ADIF **αντικαθιστά** τα προηγούμενα δεδομένα. |
| **Διαγραφή μνήμης** | Διαγράφει όλα τα τετράγωνα που φορτώθηκαν από ADIF (ζητά επιβεβαίωση). |
| Ποντίκι | **Ροδέλα = ζουμ, σύρσιμο = μετακίνηση, ποντίκι πάνω σε τετράγωνο = QSO** (έως έξι διακριτικά κλήσης με ημερομηνία, *(επιβεβαιωμένο)* όταν έχει επιβεβαιωθεί) |

Μετά τη φόρτωση, η κατάσταση δείχνει *… QSO διαβάστηκαν, … τετράγωνα QSO στις μπάντες 50-432 MHz, … QSO απορρίφθηκαν (άλλες μπάντες ή χωρίς τετράγωνο)*. Κάθε χάρτης μπάντας έχει τη λεζάντα *… τετράγωνα δουλεμένα, … επιβεβαιωμένα*.

| Χρώμα | Σημασία |
|---|---|
| Πορτοκαλί | δουλεμένο |
| Πράσινο | επιβεβαιωμένο (QSL ή LoTW) |

## Πώς διαβάζεται το ADIF

- Πεδία που χρησιμοποιούνται: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (προδιαγραφή ADIF).
- Μπάντα από το `BAND` ή από τη συχνότητα: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Ένα τετράγωνο είναι **επιβεβαιωμένο** αν τουλάχιστον ένα QSO σε αυτό έχει `QSL_RCVD = Y` ή `LOTW_QSL_RCVD = Y`.
- Τα τετράγωνα διατηρούνται στο `data/adif_quadrati.csv` μέχρι να φορτώσετε άλλο αρχείο ή να πατήσετε **Διαγραφή μνήμης**.

Το YA-MS **δεν** συνδέεται στο LoTW: εξαγάγετε το ADIF από το πρόγραμμα ημερολογίου σας (ή από το LoTW) και φορτώστε το εδώ.
