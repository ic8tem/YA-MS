**English** · [Русский](Showers-ru) · [Deutsch](Showers-de) · [日本語](Showers-ja)

# Srautai

*Kortelė: Srautai.*

[![Srautai](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Visuose skaičiavimuose naudojamas srautų katalogas: **45 srautai** iš **IMO Meteor Shower Calendar 2026 ir 2027** (5 ir 7 lentelės) ir **Antihelio šaltinis** (6 lentelė), kiekvienas su **kitu maksimumu**.

## Stulpeliai

| Stulpelis | Reikšmė |
|---|---|
| Kodas | IMO kodas (QUA, PER, GEM, …) |
| Srautas | Pavadinimas |
| Aktyvumas | Aktyvumo laikotarpis (diena/mėnuo – diena/mėnuo) |
| λ max | Maksimumo Saulės ilguma (J2000), pagal IMO |
| **Kitas maksimumas (UTC)** | Kito maksimumo data ir laikas (žr. toliau) |
| **Maksimumo šaltinis** | *IMO 2026* / *IMO 2027* = IMO paskelbta data ir laikas; *IMO 2026 (diena)* = IMO nurodo tik dieną, rodomas laikas apskaičiuotas (*~hh:mm apsk.*); *apskaičiuota iš λ* = tiems metams IMO vertės nėra |
| R.A., Dekl. | Radiantas maksimumo metu (Antihelio šaltiniui – *judantis*) |
| v km/s, r | Geocentrinis greitis ir populiacijos indeksas |
| ZHR | Maksimumo ZHR (*kint.* = kintamas) |
| Tipas | *vizualinis* arba *radijo, dieninis* |
| Aktyvus šiandien | *taip*, kai srautas dabar aktyvus |

## Kitas maksimumas

Programa visada rodo **kitą** maksimumą. Kai IMO yra paskelbusi tų metų kalendorių, naudojama **IMO data ir laikas** iš `data/massimi_imo.csv` (2026 ir 2027 įtraukti); kitu atveju apskaičiuojamas momentas, kai Saulė pasiekia maksimumo Saulės ilgumą (Meeus, *Astronomical Algorithms*, 25 sk., sprendžiama Niutono metodu).

**Patikra:** skaičiavimas sutampa su IMO 2026 ir 2027 kalendoriais kelių minučių tikslumu ten, kur IMO nurodo laiką (pvz., Kvadrantidai 2026-01-03 21:13, palyginti su 21:00; Geminidai 2027-12-14 19:51, palyginti su 20:00). Išimtys: Dieniniai kapa Leonidai 2026 viena diena vėliau (09-26 vietoj 09-25) ir eta Akvaridų 2027 laikas (15:10, palyginti su IMO 09:00) – šiais atvejais naudojama IMO vertė.

**Metų pridėjimas:** kai IMO paskelbia naują kalendorių, pridėkite jo eilutes į `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, laikas tuščias, jei IMO nurodo tik dieną). Iki tol maksimumas skaičiuojamas.

## Smulkūs ir dieniniai srautai

Kataloge yra IMO sąrašo **smulkūs srautai** – pavyzdžiui, Spalio Kamelopardalidai (OCT, ZHR 5, aktyvūs spalio 5–6 d.), Andromedidai, gama Ursae Minoridai – ir balandžio–spalio **dieniniai radijo srautai** (Dieniniai balandžio Piscidai, Dieniniai Arietidai, Dieniniai zeta Perseidai, Dieniniai beta Tauridai, Dieniniai kapa Leonidai, Dieniniai Sextantidai, …). Net ir su mažais ZHR jie prisideda prie [trasos indekso](Efficiency-Calculation-lt#modelis) ir [rekomenduojamo Hot](Sky-View-lt#rekomenduojamas-hot). Dieniniams radijo srautams IMO ZHR nepateikia: kai jo nėra, programa naudoja darbinę vertę 5.

## Aktyvumo profilis ir radianto slinkimas

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 ir λ_max – iš IMO kalendoriaus; nuolydžiai B (skirtingi prieš maksimumą ir po jo) ir paros slinkimai dα/dλ, dδ/dλ yra **darbinės vertės**, įrašytos `data/sciami.csv` (IMO slinkimų lentelė dar neįvesta). *Vadovo 9 ir 13 lygtys.* Antihelio šaltinio padėtis tiesiškai interpoliuojama tarp IMO 6 lentelės datų (`data/ant_radiante.csv`; aktyvus nuo gruodžio 10 d. iki rugsėjo 20 d., ZHR apie 4).

## Katalogo redagavimas

`data/sciami.csv` – paprastas tekstinis failas (skirtukas `;`), kurį galite redaguoti: kodas, pavadinimas, pradžia ir pabaiga (MM-DD), λ max, R.A., Dekl., slinkimai, v, r, ZHR, B prieš/po, tipas (V vizualinis, R dieninis radijo). Jei eilutė klaidinga, programa paleidžiant parodo pranešimą ir ją ignoruoja.

Šaltiniai: International Meteor Organization – Meteor Shower Calendar 2026 ir 2027, [www.imo.net](https://www.imo.net) (5, 6 ir 7 lentelės); Philip G0ISW (didžiausi radijo valandiniai dažniai); Rossano IZ5TEK (scattertek).
