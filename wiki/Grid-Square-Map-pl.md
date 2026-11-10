[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · **Polski** · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Mapa kwadratów

*Zakładka: Mapa kwadratów.*

[![Mapa kwadratów](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Kwadraty Maidenhead (4 znaki), które masz **zrobione** i **potwierdzone**, odczytane z pliku ADIF twojego dziennika, na mapie Europy – **jedna podzakładka na pasmo: 50, 70, 144, 222 i 432 MHz**.

## Elementy sterujące

| Element | Co robi |
|---|---|
| **Wczytaj plik ADIF...** | Odczytuje plik `.adi` / `.adif`. Nowy ADIF **zastępuje** poprzednie dane. |
| **Wyczyść pamięć** | Usuwa wszystkie kwadraty wczytane z ADIF (prosi o potwierdzenie). |
| Mysz | **Kółko myszy = powiększenie, przeciągnij = przesuń, mysz nad kwadratem = QSO** (do sześciu znaków wywoławczych z datą, *(potwierdzone)*, gdy potwierdzone) |

Po wczytaniu pasek stanu pokazuje *Odczytano … QSO, … kwadratów-QSO w pasmach 50-432 MHz, odrzucono … QSO (inne pasma lub brak kwadratu)*. Każda mapa pasma ma podpis *… kwadratów zrobionych, … potwierdzonych*.

| Kolor | Znaczenie |
|---|---|
| Pomarańczowy | zrobiony |
| Zielony | potwierdzone (QSL lub LoTW) |

## Jak odczytywany jest ADIF

- Używane pola: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (specyfikacja ADIF).
- Pasmo z pola `BAND` albo z częstotliwości: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Kwadrat jest **potwierdzony**, jeśli co najmniej jedno QSO w nim ma `QSL_RCVD = Y` lub `LOTW_QSL_RCVD = Y`.
- Kwadraty są przechowywane w `data/adif_quadrati.csv`, dopóki nie wczytasz innego pliku lub nie naciśniesz **Wyczyść pamięć**.

YA-MS **nie** łączy się z LoTW: wyeksportuj ADIF ze swojego programu do prowadzenia dziennika (lub z LoTW) i wczytaj go tutaj.
