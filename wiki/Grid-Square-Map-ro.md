**English** · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Harta pătratelor

*Filă: Harta pătratelor.*

[![Harta pătratelor](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Pătratele Maidenhead (4 caractere) pe care le-ați **lucrat** și **confirmat**, citite din fișierul ADIF al logului dumneavoastră, pe o hartă a Europei – **câte o subfilă pentru fiecare bandă: 50, 70, 144, 222 și 432 MHz**.

## Comenzi

| Comandă | Ce face |
|---|---|
| **Încarcă fișier ADIF...** | Citește un fișier `.adi` / `.adif`. Un ADIF nou **înlocuiește** datele anterioare. |
| **Golește memoria** | Șterge toate pătratele încărcate din ADIF (cere confirmare). |
| Mouse | **Rotița = zoom, tragere = deplasare, mouse-ul peste un pătrat = QSO-uri** (până la șase indicative cu data, *(confirmat)* când este confirmat) |

După încărcare, starea arată *… QSO-uri citite, … pătrate QSO în benzile 50-432 MHz, … QSO-uri eliminate (alte benzi sau fără pătrat)*. Fiecare hartă de bandă are legenda *… pătrate lucrate, … confirmate*.

| Culoare | Semnificație |
|---|---|
| Portocaliu | lucrat |
| Verde | confirmat (QSL sau LoTW) |

## Cum se citește ADIF-ul

- Câmpuri folosite: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (specificația ADIF).
- Banda din `BAND` sau din frecvență: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Un pătrat este **confirmat** dacă cel puțin un QSO din el are `QSL_RCVD = Y` sau `LOTW_QSL_RCVD = Y`.
- Pătratele sunt păstrate în `data/adif_quadrati.csv` până când încărcați alt fișier sau apăsați **Golește memoria**.

YA-MS **nu** se conectează la LoTW: exportați ADIF-ul din programul de log (sau din LoTW) și încărcați-l aici.
