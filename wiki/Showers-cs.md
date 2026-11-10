[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · **Čeština** · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Roje

*Karta: Roje.*

[![Roje](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Katalog rojů používaný všemi výpočty: **45 rojů** z **IMO Meteor Shower Calendar 2026 a 2027** (tabulky 5 a 7) plus **Antihelion Source** (tabulka 6), každý s **příštím maximem**.

## Sloupce

| Sloupec | Význam |
|---|---|
| Zkratka | Kód IMO (QUA, PER, GEM, …) |
| Roj | Název |
| Aktivita | Období aktivity (den/měsíc – den/měsíc) |
| λ max | Sluneční délka maxima (J2000) podle IMO |
| **Příští maximum (UTC)** | Datum a čas příštího maxima (viz níže) |
| **Zdroj maxima** | *IMO 2026* / *IMO 2027* = datum a čas publikované IMO; *IMO 2026 (den)* = IMO udává jen den, zobrazený čas je vypočtený (*~hh:mm vyp.*); *vypočteno z λ* = pro daný rok není hodnota IMO |
| Rekt., Dekl. | Radiant v maximu (*pohyblivý* u Antihelion Source) |
| v km/s, r | Geocentrická rychlost a populační index |
| ZHR | ZHR v maximu (*prom.* = proměnné) |
| Typ | *vizuální* nebo *radiový, denní* |

Roje **aktivní dnes (UTC)** jsou zvýrazněny žlutým podkladem a tučným písmem.

## Příští maximum

Program vždy ukazuje **příští** maximum. Pokud IMO zveřejnila kalendář pro daný rok, použije **datum a čas podle IMO** z `data/massimi_imo.csv` (roky 2026 a 2027 jsou zahrnuty); jinak vypočte okamžik, kdy Slunce dosáhne sluneční délky maxima (Meeus, *Astronomical Algorithms*, kap. 25, řešeno Newtonovou metodou).

**Ověření:** výpočet souhlasí s kalendáři IMO 2026 a 2027 s přesností několika minut tam, kde IMO udává čas (např. Kvadrantidy 3. 1. 2026 21:13 oproti 21:00; Geminidy 14. 12. 2027 19:51 oproti 20:00). Výjimky: Denní kappa Leonidy 2026 o den později (26. 9. místo 25. 9.) a čas eta Akvaridů 2027 (15:10 oproti 09:00 podle IMO) – v těchto případech se použije hodnota IMO.

**Přidání roku:** když IMO zveřejní nový kalendář, přidejte jeho řádky do `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, čas prázdný, pokud IMO udává jen den). Do té doby se maximum počítá.

## Menší a denní roje

Katalog obsahuje **menší roje** ze seznamu IMO – například říjnové Camelopardalidy (OCT, ZHR 5, aktivní 5.–6. října), Andromedidy, gama Ursae Minoridy – a **denní radiové roje** od dubna do října (Denní dubnové Piscidy, Denní Arietidy, Denní zeta Perseidy, Denní beta Tauridy, Denní kappa Leonidy, Denní Sextantidy, …). I s malými ZHR přispívají k [indexu trasy](Efficiency-Calculation-cs#model) a k [doporučenému Hot](Sky-View-cs#doporučený-hot). Pro denní radiové roje IMO ZHR neudává: kde chybí, použije program pracovní hodnotu 5.

## Profil aktivity a drift radiantu

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 a λ_max pocházejí z kalendáře IMO; sklony B (různé před maximem a po něm) a denní drifty dα/dλ, dδ/dλ jsou **pracovní hodnoty** zapsané v `data/sciami.csv` (tabulka driftů IMO zatím nebyla zadána). *Manuál, rov. 9 a 13.* Poloha Antihelion Source se lineárně interpoluje mezi daty tabulky 6 IMO (`data/ant_radiante.csv`; aktivní 10. prosince – 20. září, ZHR asi 4).

## Úprava katalogu

`data/sciami.csv` je prostý textový soubor (oddělovač `;`), který můžete upravovat: kód, název, začátek a konec (MM-DD), λ max, R.A., Dec., drifty, v, r, ZHR, B před/po, typ (V vizuální, R denní radiový). Pokud je řádek chybný, program při spuštění zobrazí zprávu a řádek ignoruje.

Zdroje: International Meteor Organization – Meteor Shower Calendar 2026 a 2027, [www.imo.net](https://www.imo.net) (tabulky 5, 6 a 7); Rossano IZ5TEK (scattertek).
