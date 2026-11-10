[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · **Afrikaans** · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Swerms

*Oortjie: Swerms.*

[![Swerms](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Die swermkatalogus wat deur al die berekeninge gebruik word: **45 swerms** uit die **IMO Meteor Shower Calendar 2026 en 2027** (tabelle 5 en 7) plus die **Antihelion-bron** (tabel 6), elkeen met sy **volgende maksimum**.

## Kolomme

| Kolom | Betekenis |
|---|---|
| Kode | IMO-kode (QUA, PER, GEM, …) |
| Swerm | Naam |
| Aktiwiteit | Aktiwiteitsperiode (dag/maand – dag/maand) |
| λ max | Sonlengte van die maksimum (J2000), volgens die IMO |
| **Volgende maksimum (UTC)** | Datum en tyd van die volgende maksimum (sien hieronder) |
| **Bron van die maksimum** | *IMO 2026* / *IMO 2027* = datum en tyd deur die IMO gepubliseer; *IMO 2026 (dag)* = die IMO gee slegs die dag, die getoonde tyd is bereken (*~hh:mm ber.*); *bereken uit λ* = geen IMO-waarde vir daardie jaar nie |
| R.A., Dekl. | Radiant by die maksimum (*bewegend* vir die Antihelion-bron) |
| v km/s, r | Geosentriese snelheid en populasie-indeks |
| ZHR | ZHR by die maksimum (*var.* = veranderlik) |
| Tipe | *visueel* of *radio, bedags* |
| Vandag aktief | *ja* wanneer die swerm nou aktief is |

## Volgende maksimum

Die program wys altyd die **volgende** maksimum. Wanneer die IMO daardie jaar se kalender gepubliseer het, gebruik dit die **IMO-datum en -tyd** uit `data/massimi_imo.csv` (2026 en 2027 is ingesluit); anders bereken dit die oomblik waarop die Son die sonlengte van die maksimum bereik (Meeus, *Astronomical Algorithms*, hfst. 25, opgelos met Newton se metode).

**Kontrole:** die berekening stem met die IMO-kalenders van 2026 en 2027 binne 'n paar minute ooreen waar die IMO die tyd gee (bv. Kwadrantiede 3/1/2026 21:13 teenoor 21:00; Geminiede 14/12/2027 19:51 teenoor 20:00). Uitsonderings: die kappa-Leoniede (bedags) van 2026, een dag later (26/9 in plaas van 25/9), en die tyd van die eta-Akwariede van 2027 (15:10 teenoor 09:00 IMO) – in hierdie gevalle word die IMO-waarde gebruik.

**'n Jaar byvoeg:** wanneer die IMO 'n nuwe kalender publiseer, voeg sy rye by `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, tyd leeg as die IMO slegs die dag gee). Tot dan word die maksimum bereken.

## Klein swerms en dagswerms

Die katalogus sluit die **klein swerms** van die IMO-lys in – byvoorbeeld die Oktober-Camelopardaliede (OCT, ZHR 5, aktief 5–6 Oktober), die Andromediede, die gamma-Ursae Minoriede – en die **radioswerms bedags** van April tot Oktober (April-Pisciede, Arietiede, zeta-Perseïede, beta-Tauriede, kappa-Leoniede, Sextantiede, almal bedags, …). Selfs met klein ZHR's dra hulle by tot die [padindeks](Efficiency-Calculation-af#die-model) en die [aanbevole Hot](Sky-View-af#aanbevole-hot). Vir die radioswerms bedags gee die IMO geen ZHR nie: waar geen gegee word nie, gebruik die program 'n werkwaarde van 5.

## Aktiwiteitsprofiel en radiantdrywing

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 en λ_max kom uit die IMO-kalender; die hellings B (verskillend voor en ná die maksimum) en die daaglikse drywings dα/dλ, dδ/dλ is **werkwaardes** wat in `data/sciami.csv` geskryf is (die IMO-drywingstabel is nog nie ingevoer nie). *Handleiding vgl. 9 en 13.* Die posisie van die Antihelion-bron word lineêr geïnterpoleer tussen die datums van IMO-tabel 6 (`data/ant_radiante.csv`; aktief 10 Desember – 20 September, ZHR ongeveer 4).

## Die katalogus wysig

`data/sciami.csv` is 'n gewone tekslêer (skeidingsteken `;`) wat jy kan wysig: kode, naam, begin en einde (MM-DD), λ max, R.A., Dekl., drywings, v, r, ZHR, B voor/ná, tipe (V visueel, R radio bedags). As 'n reël foutief is, wys die program by opstart 'n boodskap en ignoreer dit.

Bronne: International Meteor Organization – Meteor Shower Calendar 2026 en 2027, [www.imo.net](https://www.imo.net) (tabelle 5, 6 en 7); Philip G0ISW (maksimum radio-uurtempo's); Rossano IZ5TEK (scattertek).
