[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · **Magyar** · [Română](Grid-Square-Map-ro) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

# Négyzettérkép

*Fül: Négyzettérkép.*

[![Négyzettérkép](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Az Ön által **forgalmazott** és **megerősített** Maidenhead-négyzetek (4 karakter), a naplója ADIF-fájljából beolvasva, Európa térképén – **sávonként egy alfül: 50, 70, 144, 222 és 432 MHz**.

## Vezérlők

| Vezérlő | Mit csinál |
|---|---|
| **ADIF-fájl betöltése...** | Beolvas egy `.adi` / `.adif` fájlt. Az új ADIF **lecseréli** a korábbi adatokat. |
| **Memória törlése** | Törli az összes ADIF-ből betöltött négyzetet (megerősítést kér). |
| Egér | **Görgő = nagyítás, húzás = mozgatás, egér egy négyzet felett = QSO-k** (legfeljebb hat hívójel dátummal, *(megerősítve)*, ha megerősített) |

Betöltés után az állapotsor ezt mutatja: *… QSO beolvasva, … QSO-négyzet az 50-432 MHz-es sávokban, … QSO elvetve (más sáv vagy nincs négyzet)*. Minden sávtérkép felirata: *… négyzet forgalmazva, … megerősítve*.

| Szín | Jelentés |
|---|---|
| Narancs | forgalmazva |
| Zöld | megerősítve (QSL vagy LoTW) |

## Hogyan olvassa be a program az ADIF-et

- Használt mezők: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF-specifikáció).
- A sáv a `BAND` mezőből vagy a frekvenciából: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Egy négyzet **megerősített**, ha legalább egy benne lévő QSO-nál `QSL_RCVD = Y` vagy `LOTW_QSL_RCVD = Y`.
- A négyzetek a `data/adif_quadrati.csv` fájlban maradnak, amíg másik fájlt nem tölt be, vagy meg nem nyomja a **Memória törlése** gombot.

A YA-MS **nem** csatlakozik a LoTW-hez: exportálja az ADIF-et a naplóprogramjából (vagy a LoTW-ből), és töltse be itt.
