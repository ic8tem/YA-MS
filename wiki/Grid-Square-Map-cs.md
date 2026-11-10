LANGBAR

# Mapa čtverců

*Karta: Mapa čtverců.*

[![Mapa čtverců](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Čtverce Maidenhead (4 znaky), které jste **pracovali** a máte **potvrzené**, načtené ze souboru ADIF vašeho deníku, na mapě Evropy – **jedna podkarta na pásmo: 50, 70, 144, 222 a 432 MHz**.

## Ovládání

| Ovládací prvek | Co dělá |
|---|---|
| **Načíst soubor ADIF...** | Načte soubor `.adi` / `.adif`. Nový ADIF **nahradí** předchozí data. |
| **Vymazat paměť** | Smaže všechny čtverce načtené z ADIF (požádá o potvrzení). |
| Myš | **Kolečko = zoom, tažení = posun, myš nad čtvercem = QSO** (až šest značek s datem, *(potvrzeno)*, pokud je potvrzeno) |

Po načtení stavový řádek ukáže *… QSO načteno, … čtverců s QSO v pásmech 50-432 MHz, … QSO zahozeno (jiná pásma nebo bez čtverce)*. Mapa každého pásma má popisek *… čtverců pracováno, … potvrzeno*.

| Barva | Význam |
|---|---|
| Oranžová | pracováno |
| Zelená | potvrzeno (QSL nebo LoTW) |

## Jak se čte ADIF

- Použitá pole: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (specifikace ADIF).
- Pásmo z `BAND`, nebo z kmitočtu: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Čtverec je **potvrzený**, pokud alespoň jedno QSO v něm má `QSL_RCVD = Y` nebo `LOTW_QSL_RCVD = Y`.
- Čtverce se uchovávají v `data/adif_quadrati.csv`, dokud nenačtete jiný soubor nebo nestisknete **Vymazat paměť**.

YA-MS se **nepřipojuje** k LoTW: exportujte ADIF ze svého deníkového programu (nebo z LoTW) a načtěte ho sem.
