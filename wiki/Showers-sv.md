[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · **Svenska** · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Svärmar

*Flik: Svärmar.*

[![Svärmar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Den svärmkatalog som alla beräkningar använder: **45 svärmar** från **IMO Meteor Shower Calendar 2026 och 2027** (tabell 5 och 7) plus **Antihelion Source** (tabell 6), var och en med sitt **nästa maximum**.

## Kolumner

| Kolumn | Betydelse |
|---|---|
| Kod | IMO-kod (QUA, PER, GEM, …) |
| Svärm | Namn |
| Aktivitet | Aktivitetsperiod (dag/månad – dag/månad) |
| λ max | Solens longitud vid maximum (J2000), från IMO |
| **Nästa maximum (UTC)** | Datum och tid för nästa maximum (se nedan) |
| **Källa för maximum** | *IMO 2026* / *IMO 2027* = datum och tid publicerade av IMO; *IMO 2026 (dag)* = IMO anger bara dagen, den visade tiden är beräknad (*~hh:mm ber.*); *beräknad från λ* = inget IMO-värde för det året |
| R.A., Dekl. | Radianten vid maximum (*rörlig* för Antihelion Source) |
| v km/s, r | Geocentrisk hastighet och populationsindex |
| ZHR | ZHR vid maximum (*var.* = variabel) |
| Typ | *visuell* eller *radio, dagtid* |
| Aktiv idag | *ja* när svärmen är aktiv nu |

## Nästa maximum

Programmet visar alltid **nästa** maximum. När IMO har publicerat årets kalender används **IMO:s datum och tid** från `data/massimi_imo.csv` (2026 och 2027 ingår); annars beräknas det ögonblick då solen når maximumets solongitud (Meeus, *Astronomical Algorithms*, kap. 25, löst med Newtons metod).

**Kontroll:** beräkningen stämmer med IMO:s kalendrar för 2026 och 2027 inom några minuter där IMO anger tiden (t.ex. Quadrantiderna 3/1/2026 21:13 mot 21:00; Geminiderna 14/12/2027 19:51 mot 20:00). Undantag: Daytime kappa Leonids 2026 en dag senare (26/9 i stället för 25/9) och tiden för eta Aquariiderna 2027 (15:10 mot 09:00 enligt IMO) – i dessa fall används IMO:s värde.

**Lägga till ett år:** när IMO publicerar en ny kalender, lägg till dess rader i `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, tiden tom om IMO bara anger dagen). Tills dess beräknas maximum.

## Mindre svärmar och dagsvärmar

Katalogen omfattar de **mindre svärmarna** i IMO:s lista – till exempel October Camelopardalids (OCT, ZHR 5, aktiv 5–6 oktober), Andromediderna, gamma Ursae Minorids – och **dagsvärmarna (radio)** från april till oktober (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Även med små ZHR bidrar de till [sträckindex](Efficiency-Calculation-sv#modellen) och till [rekommenderad Hot](Sky-View-sv#rekommenderad-hot). För radiosvärmarna på dagtid anger IMO ingen ZHR: där ingen anges använder programmet arbetsvärdet 5.

## Aktivitetsprofil och radiantdrift

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 och λ_max kommer från IMO-kalendern; lutningarna B (olika före och efter maximum) och den dagliga driften dα/dλ, dδ/dλ är **arbetsvärden** som står i `data/sciami.csv` (IMO:s drifttabell har ännu inte förts in). *Handboken ekv. 9 och 13.* Positionen för Antihelion Source interpoleras linjärt mellan datumen i IMO:s tabell 6 (`data/ant_radiante.csv`; aktiv 10 december – 20 september, ZHR omkring 4).

## Redigera katalogen

`data/sciami.csv` är en vanlig textfil (avgränsare `;`) som du kan redigera: kod, namn, början och slut (MM-DD), λ max, R.A., Dekl., drift, v, r, ZHR, B före/efter, typ (V visuell, R radio dagtid). Om en rad är felaktig visar programmet ett meddelande vid start och hoppar över den.

Källor: International Meteor Organization – Meteor Shower Calendar 2026 och 2027, [www.imo.net](https://www.imo.net) (tabell 5, 6 och 7); Philip G0ISW (maximala timfrekvenser i radio); Rossano IZ5TEK (scattertek).
