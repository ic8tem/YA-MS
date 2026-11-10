[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · **Latviešu** · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Plūsmas

*Cilne: Plūsmas.*

[![Plūsmas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Plūsmu katalogs, ko izmanto visi aprēķini: **45 plūsmas** no **IMO Meteor Shower Calendar 2026 un 2027** (5. un 7. tabula) un **Antihēlija avots** (6. tabula), katrai ar **nākamo maksimumu**.

## Kolonnas

| Kolonna | Nozīme |
|---|---|
| Kods | IMO kods (QUA, PER, GEM, …) |
| Plūsma | Nosaukums |
| Aktivitāte | Aktivitātes periods (diena/mēnesis – diena/mēnesis) |
| λ max | Maksimuma Saules garums (J2000), no IMO |
| **Nākamais maksimums (UTC)** | Nākamā maksimuma datums un laiks (sk. zemāk) |
| **Maksimuma avots** | *IMO 2026* / *IMO 2027* = IMO publicētais datums un laiks; *IMO 2026 (diena)* = IMO dod tikai dienu, parādītais laiks ir aprēķināts (*~hh:mm aprēķ.*); *aprēķināts no λ* = šim gadam nav IMO vērtības |
| RA, Dekl. | Radiants maksimumā (*kustīgs* Antihēlija avotam) |
| v km/s, r | Ģeocentriskais ātrums un populācijas indekss |
| ZHR | Maksimālais ZHR (*main.* = mainīgs) |
| Tips | *vizuāli* vai *radio, dienas* |
| Aktīva šodien | *jā*, ja plūsma tagad ir aktīva |

## Nākamais maksimums

Programma vienmēr rāda **nākamo** maksimumu. Ja IMO ir publicējusi attiecīgā gada kalendāru, tiek izmantots **IMO datums un laiks** no `data/massimi_imo.csv` (iekļauti 2026. un 2027. gads); citādi tiek aprēķināts brīdis, kad Saule sasniedz maksimuma Saules garumu (Meeus, *Astronomical Algorithms*, 25. nod., atrisināts ar Ņūtona metodi).

**Pārbaude:** aprēķins sakrīt ar IMO 2026. un 2027. gada kalendāriem dažu minūšu robežās tur, kur IMO norāda laiku (piem. Kvadrantīdas 3/1/2026 21:13 pret 21:00; Geminīdas 14/12/2027 19:51 pret 20:00). Izņēmumi: Dienas kappa-Leonīdas 2026 vienu dienu vēlāk (26/9, nevis 25/9) un eta-Akvarīdu 2027 laiks (15:10 pret 09:00 IMO) – šajos gadījumos tiek izmantota IMO vērtība.

**Gada pievienošana:** kad IMO publicē jaunu kalendāru, pievieno tā rindas failam `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, laiks tukšs, ja IMO dod tikai dienu). Līdz tam maksimums tiek aprēķināts.

## Mazās un dienas plūsmas

Katalogā ir IMO saraksta **mazās plūsmas** – piemēram, Oktobra Kamelopardalīdas (OCT, ZHR 5, aktīvas 5.–6. oktobrī), Andromedīdas, gamma-Ursae Minorīdas – un aprīļa–oktobra **dienas radio plūsmas** (Dienas aprīļa Piscīdas, Dienas Arietīdas, Dienas zeta-Perseīdas, Dienas beta-Taurīdas, Dienas kappa-Leonīdas, Dienas Sekstantīdas, …). Arī ar maziem ZHR tās dod ieguldījumu [trases indeksā](Efficiency-Calculation-lv#modelis) un [ieteicamajā Hot](Sky-View-lv#ieteicamais-hot). Dienas radio plūsmām IMO nedod ZHR: kur tas nav norādīts, programma izmanto darba vērtību 5.

## Aktivitātes profils un radianta pārvietošanās

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 un λ_max ir no IMO kalendāra; slīpumi B (atšķirīgi pirms un pēc maksimuma) un ikdienas pārvietojumi dα/dλ, dδ/dλ ir **darba vērtības**, kas ierakstītas failā `data/sciami.csv` (IMO pārvietojumu tabula vēl nav ievadīta). *Rokasgrāmatas 9. un 13. vien.* Antihēlija avota stāvoklis tiek lineāri interpolēts starp IMO 6. tabulas datumiem (`data/ant_radiante.csv`; aktīvs no 10. decembra līdz 20. septembrim, ZHR ap 4).

## Kataloga rediģēšana

`data/sciami.csv` ir vienkāršs teksta fails (atdalītājs `;`), ko var rediģēt: kods, nosaukums, sākums un beigas (MM-DD), λ max, RA, Dekl., pārvietojumi, v, r, ZHR, B pirms/pēc, tips (V vizuāla, R dienas radio). Ja rinda ir kļūdaina, programma startējot parāda ziņojumu un to ignorē.

Avoti: International Meteor Organization – Meteor Shower Calendar 2026 un 2027, [www.imo.net](https://www.imo.net) (5., 6. un 7. tabula); Philip G0ISW (maksimālie radio stundas skaiti); Rossano IZ5TEK (scattertek).
