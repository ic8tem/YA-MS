[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · **Eesti** · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Meteoorivoolud

*Sakk: Meteoorivoolud.*

[![Meteoorivoolud](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Kõigis arvutustes kasutatav meteoorivoolude kataloog: **45 meteoorivoolu** **IMO Meteor Shower Calendar 2026 ja 2027** põhjal (tabelid 5 ja 7) pluss **antiheeliumi allikas** (tabel 6), igaüks koos **järgmise maksimumiga**.

## Veerud

| Veerg | Tähendus |
|---|---|
| Lühend | IMO lühend (QUA, PER, GEM, …) |
| Meteoorivool | Nimi |
| Aktiivsus | Aktiivsusperiood (päev/kuu – päev/kuu) |
| λ max | Maksimumi Päikese pikkus (J2000), IMO-lt |
| **Järgmine maksimum (UTC)** | Järgmise maksimumi kuupäev ja kellaaeg (vt allpool) |
| **Maksimumi allikas** | *IMO 2026* / *IMO 2027* = IMO avaldatud kuupäev ja kellaaeg; *IMO 2026 (päev)* = IMO annab ainult päeva, näidatud kellaaeg on arvutatud (*~hh:mm arv.*); *arvutatud λ põhjal* = selle aasta kohta IMO väärtus puudub |
| R.A., Dekl. | Radiant maksimumi ajal (antiheeliumi allika puhul *liikuv*) |
| v km/s, r | Geotsentriline kiirus ja populatsiooniindeks |
| ZHR | Maksimumi ZHR (*muutuv* = muutuv) |
| Tüüp | *visuaalne* või *raadio, päevane* |
| Täna aktiivne | *jah*, kui meteoorivool on praegu aktiivne |

## Järgmine maksimum

Programm näitab alati **järgmist** maksimumi. Kui IMO on selle aasta kalendri avaldanud, kasutab programm **IMO kuupäeva ja kellaaega** failist `data/massimi_imo.csv` (2026 ja 2027 on sees); muidu arvutab see hetke, mil Päike jõuab maksimumi Päikese pikkuseni (Meeus, *Astronomical Algorithms*, ptk 25, lahendatud Newtoni meetodiga).

**Kontroll:** arvutus ühtib IMO 2026 ja 2027 kalendritega mõne minuti täpsusega seal, kus IMO annab kellaaja (nt Kvadrantiidid 3.1.2026 21:13 vs 21:00; Geminiidid 14.12.2027 19:51 vs 20:00). Erandid: päevased kappa-Leoniidid 2026 üks päev hiljem (26.9 asemel 25.9) ja eta-Akvariidide 2027 kellaaeg (15:10 vs IMO 09:00) – neil juhtudel kasutatakse IMO väärtust.

**Aasta lisamine:** kui IMO avaldab uue kalendri, lisa selle read faili `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, kellaaeg tühi, kui IMO annab ainult päeva). Seni maksimum arvutatakse.

## Väikesed ja päevased meteoorivoolud

Kataloog sisaldab IMO loetelu **väikeseid meteoorivoole** – näiteks Oktoobri Kamelopardaliidid (OCT, ZHR 5, aktiivne 5.–6. oktoobril), Andromediidid, gamma-Ursae Minoriidid – ning aprillist oktoobrini **päevaseid raadiovoole** (Päevased aprilli Pistsiidid, Päevased Arietiidid, Päevased zeeta-Perseiidid, Päevased beeta-Tauriidid, Päevased kappa-Leoniidid, Päevased Sekstantiidid, …). Ka väikeste ZHR-idega panustavad need [trassi indeksisse](Efficiency-Calculation-et#mudel) ja [soovitatud Hoti](Sky-View-et#soovitatud-hot). Päevaste raadiovoolude jaoks IMO ZHR-i ei anna: kui seda pole, kasutab programm tööväärtust 5.

## Aktiivsusprofiil ja radiandi nihkumine

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 ja λ_max IMO kalendrist; tõusud B (erinevad enne ja pärast maksimumi) ning päevased nihked dα/dλ, dδ/dλ on **tööväärtused**, mis on kirjas failis `data/sciami.csv` (IMO nihete tabelit pole veel sisestatud). *Juhendi võrrandid 9 ja 13.* Antiheeliumi allika asend interpoleeritakse lineaarselt IMO tabeli 6 kuupäevade vahel (`data/ant_radiante.csv`; aktiivne 10. detsembrist 20. septembrini, ZHR umbes 4).

## Kataloogi muutmine

`data/sciami.csv` on lihttekstifail (eraldaja `;`), mida saad muuta: lühend, nimi, algus ja lõpp (MM-DD), λ max, R.A., Dekl., nihked, v, r, ZHR, B enne/pärast, tüüp (V visuaalne, R päevane raadio). Kui rida on vigane, näitab programm käivitamisel teadet ja ignoreerib seda.

Allikad: International Meteor Organization – Meteor Shower Calendar 2026 ja 2027, [www.imo.net](https://www.imo.net) (tabelid 5, 6 ja 7); Philip G0ISW (maksimaalsed raadio tunnisagedused); Rossano IZ5TEK (scattertek).
