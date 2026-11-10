[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Dansk](Showers-da) · **Norsk** · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Svermer

*Fane: Svermer.*

[![Svermer](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Svermkatalogen som alle beregningene bruker: **45 svermer** fra **IMO Meteor Shower Calendar 2026 og 2027** (tabell 5 og 7) pluss **Antihelion-kilden** (tabell 6), hver med sitt **neste maksimum**.

## Kolonner

| Kolonne | Betydning |
|---|---|
| Kode | IMO-kode (QUA, PER, GEM, …) |
| Sverm | Navn |
| Aktivitet | Aktivitetsperiode (dag/måned – dag/måned) |
| λ max | Solens lengde ved maksimum (J2000), fra IMO |
| **Neste maksimum (UTC)** | Dato og tidspunkt for neste maksimum (se nedenfor) |
| **Kilde for maksimum** | *IMO 2026* / *IMO 2027* = dato og tidspunkt publisert av IMO; *IMO 2026 (dag)* = IMO oppgir bare dagen, tidspunktet som vises er beregnet (*~hh:mm ber.*); *beregnet fra λ* = ingen IMO-verdi for det året |
| R.A., Dekl. | Radianten ved maksimum (*bevegelig* for Antihelion-kilden) |
| v km/s, r | Geosentrisk hastighet og populasjonsindeks |
| ZHR | Maksimal ZHR (*var.* = variabel) |
| Type | *visuell* eller *radio, dagtid* |

Svermene som er **aktive i dag (UTC)**, er uthevet med et gult slør og fet skrift.

## Neste maksimum

Programmet viser alltid det **neste** maksimumet. Når IMO har publisert kalenderen for det året, brukes **IMOs dato og tidspunkt** fra `data/massimi_imo.csv` (2026 og 2027 er med); ellers beregnes øyeblikket da Sola når solens lengde for maksimumet (Meeus, *Astronomical Algorithms*, kap. 25, løst med Newtons metode).

**Kontroll:** beregningen stemmer med IMO-kalenderne for 2026 og 2027 innenfor noen få minutter der IMO oppgir tidspunktet (f.eks. Kvadrantidene 3.1.2026 21:13 mot 21:00; Geminidene 14.12.2027 19:51 mot 20:00). Unntak: kappa-Leonidene (dagtid) 2026 én dag senere (26.9 i stedet for 25.9) og tidspunktet for eta-Akvaridene 2027 (15:10 mot IMOs 09:00) – i disse tilfellene brukes IMO-verdien.

**Legge til et år:** når IMO publiserer en ny kalender, legger du radene inn i `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, tidspunktet tomt hvis IMO bare oppgir dagen). Inntil da beregnes maksimumet.

## Mindre svermer og dagsvermer

Katalogen inneholder de **mindre svermene** på IMO-listen – for eksempel Oktober-Camelopardalidene (OCT, ZHR 5, aktive 5.–6. oktober), Andromedidene og gamma-Ursae Minoridene – og **radiodagsvermene** fra april–oktober (April-Piscidene (dagtid), Arietidene (dagtid), zeta-Perseidene (dagtid), beta-Tauridene (dagtid), kappa-Leonidene (dagtid), Sextantidene (dagtid), …). Selv med små ZHR bidrar de til [strekningsindeksen](Efficiency-Calculation-nb#modellen) og til [anbefalt Hot](Sky-View-nb#anbefalt-hot). For radiodagsvermene oppgir IMO ingen ZHR: der det ikke finnes noen, bruker programmet en arbeidsverdi på 5.

## Aktivitetsprofil og radiantens forflytning

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 og λ_max fra IMO-kalenderen; stigningstallene B (ulike før og etter maksimum) og de daglige forflytningene dα/dλ, dδ/dλ er **arbeidsverdier** skrevet i `data/sciami.csv` (IMOs tabell over radiantforflytning er ennå ikke lagt inn). *Håndbokens likn. 9 og 13.* Posisjonen til Antihelion-kilden interpoleres lineært mellom datoene i IMOs tabell 6 (`data/ant_radiante.csv`; aktiv 10. desember – 20. september, ZHR ca. 4).

## Redigere katalogen

`data/sciami.csv` er en vanlig tekstfil (skilletegn `;`) som du kan redigere: kode, navn, start og slutt (MM-DD), λ max, R.A., Dekl., forflytninger, v, r, ZHR, B før/etter, type (V visuell, R radio dagtid). Hvis en linje er feil, viser programmet en melding ved oppstart og ignorerer den.

Kilder: International Meteor Organization – Meteor Shower Calendar 2026 og 2027, [www.imo.net](https://www.imo.net) (tabell 5, 6 og 7); Rossano IZ5TEK (scattertek).
