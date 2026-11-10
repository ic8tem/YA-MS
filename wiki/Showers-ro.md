[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · **Română** · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [ไทย](Showers-th) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Roiuri

*Fila: Roiuri.*

[![Roiuri](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Catalogul roiurilor folosit de toate calculele: **45 de roiuri** din **IMO Meteor Shower Calendar 2026 și 2027** (tabelele 5 și 7) plus **Sursa Antihelion** (tabelul 6), fiecare cu **următorul maxim**.

## Coloane

| Coloană | Semnificație |
|---|---|
| Cod | Codul IMO (QUA, PER, GEM, …) |
| Roi | Numele |
| Activitate | Perioada de activitate (zi/lună – zi/lună) |
| λ max | Longitudinea solară a maximului (J2000), după IMO |
| **Următorul maxim (UTC)** | Data și ora următorului maxim (vezi mai jos) |
| **Sursa maximului** | *IMO 2026* / *IMO 2027* = data și ora publicate de IMO; *IMO 2026 (zi)* = IMO dă doar ziua, ora afișată este calculată (*~hh:mm calc.*); *calculat din λ* = nicio valoare IMO pentru acel an |
| A.R., Decl. | Radiantul la maxim (*mobil* pentru Sursa Antihelion) |
| v km/s, r | Viteza geocentrică și indicele populației |
| ZHR | ZHR la maxim (*var.* = variabil) |
| Tip | *vizual* sau *radio, diurn* |
| Activ azi | *da* când roiul este activ acum |

## Următorul maxim

Programul arată întotdeauna **următorul** maxim. Când IMO a publicat calendarul acelui an, folosește **data și ora IMO** din `data/massimi_imo.csv` (2026 și 2027 sunt incluse); altfel calculează momentul în care Soarele atinge longitudinea solară a maximului (Meeus, *Astronomical Algorithms*, cap. 25, rezolvat cu metoda lui Newton).

**Verificare:** calculul concordă cu calendarele IMO 2026 și 2027 în limita a câteva minute acolo unde IMO dă ora (de ex. Quadrantide 3/1/2026 21:13 față de 21:00; Geminide 14/12/2027 19:51 față de 20:00). Excepții: kappa-Leonide diurne 2026, cu o zi mai târziu (26/9 în loc de 25/9), și ora eta-Aquaridelor 2027 (15:10 față de 09:00 IMO) – în aceste cazuri se folosește valoarea IMO.

**Adăugarea unui an:** când IMO publică un calendar nou, adaugă rândurile lui în `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, ora goală dacă IMO dă doar ziua). Până atunci maximul este calculat.

## Roiuri minore și diurne

Catalogul include **roiurile minore** din lista IMO – de exemplu Camelopardalidele de octombrie (OCT, ZHR 5, active 5–6 octombrie), Andromedidele, gamma-Ursae Minoridele – și **roiurile radio diurne** din aprilie–octombrie (Piscide de aprilie diurne, Arietide diurne, zeta-Perseide diurne, beta-Tauride diurne, kappa-Leonide diurne, Sextantide diurne, …). Chiar și cu ZHR mici, ele contribuie la [indicele traseului](Efficiency-Calculation-ro#modelul) și la [Hot-ul recomandat](Sky-View-ro#hot-recomandat). Pentru roiurile radio diurne IMO nu dă ZHR: acolo unde nu este dat, programul folosește o valoare de lucru de 5.

## Profilul de activitate și deplasarea radiantului

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 și λ_max din calendarul IMO; pantele B (diferite înainte și după maxim) și deplasările zilnice dα/dλ, dδ/dλ sunt **valori de lucru** scrise în `data/sciami.csv` (tabelul de deplasări IMO nu a fost încă introdus). *Manual, ec. 9 și 13.* Poziția Sursei Antihelion este interpolată liniar între datele tabelului 6 IMO (`data/ant_radiante.csv`; activă între 10 decembrie și 20 septembrie, ZHR circa 4).

## Editarea catalogului

`data/sciami.csv` este un fișier text simplu (separator `;`) pe care îl poți edita: cod, nume, început și sfârșit (MM-DD), λ max, A.R., Decl., deplasări, v, r, ZHR, B înainte/după, tip (V vizual, R radio diurn). Dacă un rând este greșit, programul afișează un mesaj la pornire și îl ignoră.

Surse: International Meteor Organization – Meteor Shower Calendar 2026 și 2027, [www.imo.net](https://www.imo.net) (tabelele 5, 6 și 7); Philip G0ISW (rate orare radio maxime); Rossano IZ5TEK (scattertek).
