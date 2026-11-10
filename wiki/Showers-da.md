[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · **Dansk** · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [ไทย](Showers-th) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Sværme

*Fane: Sværme.*

[![Sværme](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Sværmkataloget, som alle beregninger bruger: **45 sværme** fra **IMO Meteor Shower Calendar 2026 og 2027** (tabel 5 og 7) plus **Antihelion-kilden** (tabel 6), hver med sit **næste maksimum**.

## Kolonner

| Kolonne | Betydning |
|---|---|
| Kode | IMO-kode (QUA, PER, GEM, …) |
| Sværm | Navn |
| Aktivitet | Aktivitetsperiode (dag/måned – dag/måned) |
| λ max | Solens længde ved maksimum (J2000), fra IMO |
| **Næste maksimum (UTC)** | Dato og tidspunkt for næste maksimum (se nedenfor) |
| **Kilde til maksimum** | *IMO 2026* / *IMO 2027* = dato og tidspunkt publiceret af IMO; *IMO 2026 (dag)* = IMO angiver kun dagen, det viste tidspunkt er beregnet (*~hh:mm beregn.*); *beregnet ud fra λ* = ingen IMO-værdi for det år |
| R.A., Dekl. | Radianten ved maksimum (*bevægelig* for Antihelion-kilden) |
| v km/s, r | Geocentrisk hastighed og populationsindeks |
| ZHR | Maksimal ZHR (*var.* = variabel) |
| Type | *visuel* eller *radio, dagtid* |
| Aktiv i dag | *ja*, når sværmen er aktiv nu |

## Næste maksimum

Programmet viser altid det **næste** maksimum. Når IMO har publiceret kalenderen for det år, bruges **IMO's dato og tidspunkt** fra `data/massimi_imo.csv` (2026 og 2027 er med); ellers beregnes det øjeblik, hvor Solen når solens længde for maksimum (Meeus, *Astronomical Algorithms*, kap. 25, løst med Newtons metode).

**Kontrol:** beregningen stemmer med IMO-kalenderne for 2026 og 2027 inden for nogle få minutter, hvor IMO angiver tidspunktet (fx Quadrantiderne 3.1.2026 21:13 mod 21:00; Geminiderne 14.12.2027 19:51 mod 20:00). Undtagelser: kappa-Leoniderne (dag) 2026 én dag senere (26.9 i stedet for 25.9) og tidspunktet for eta-Aquariiderne 2027 (15:10 mod IMO's 09:00) – i disse tilfælde bruges IMO's værdi.

**Tilføjelse af et år:** når IMO publicerer en ny kalender, føjes dens rækker til `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, tidspunktet tomt, hvis IMO kun angiver dagen). Indtil da beregnes maksimum.

## Mindre sværme og dagsværme

Kataloget indeholder IMO-listens **mindre sværme** – fx Oktober-Camelopardaliderne (OCT, ZHR 5, aktive 5.–6. oktober), Andromediderne og gamma-Ursae Minoriderne – og **radiodagsværmene** fra april–oktober (April-Pisciderne (dag), Arietiderne (dag), zeta-Perseiderne (dag), beta-Tauriderne (dag), kappa-Leoniderne (dag), Sextantiderne (dag), …). Selv med små ZHR bidrager de til [strækningsindekset](Efficiency-Calculation-da#modellen) og til det [anbefalede Hot](Sky-View-da#anbefalet-hot). For radiodagsværmene angiver IMO ingen ZHR: hvor der ikke er nogen, bruger programmet en arbejdsværdi på 5.

## Aktivitetsprofil og radiantens vandring

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 og λ_max fra IMO-kalenderen; hældningerne B (forskellige før og efter maksimum) og de daglige vandringer dα/dλ, dδ/dλ er **arbejdsværdier** skrevet i `data/sciami.csv` (IMO's tabel over radiantvandring er endnu ikke indlagt). *Manualens lign. 9 og 13.* Antihelion-kildens position interpoleres lineært mellem datoerne i IMO's tabel 6 (`data/ant_radiante.csv`; aktiv 10. december – 20. september, ZHR ca. 4).

## Redigering af kataloget

`data/sciami.csv` er en almindelig tekstfil (skilletegn `;`), som du kan redigere: kode, navn, start og slut (MM-DD), λ max, R.A., Dekl., vandringer, v, r, ZHR, B før/efter, type (V visuel, R radio dagtid). Hvis en linje er forkert, viser programmet en meddelelse ved opstart og ignorerer den.

Kilder: International Meteor Organization – Meteor Shower Calendar 2026 og 2027, [www.imo.net](https://www.imo.net) (tabel 5, 6 og 7); Philip G0ISW (maksimale radiorater pr. time); Rossano IZ5TEK (scattertek).
