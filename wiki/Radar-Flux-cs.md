LANGBAR

# Tok z radaru

*Karta: Živá data a data v reálném čase › Tok z radaru.*

[![Tok z radaru](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Tato karta ukazuje, co **právě teď** počítají profesionální meteorické radary: hodinové počty meteorů a výšky stop z radaru SKiYMET v **Collmu** (Univerzita Lipsko / IAP Kühlungsborn, Německo, 36,2 MHz) a nejnovější snímek radaru v **Sodankylä** (SGO, Finsko). Počty z Collmu napájejí odhad pro vaše pásmo a [Experimentální předpovědi](Experimental-Forecasts-cs); změřená výška stopy napájí celou geometrii.

## Ovládání

| Ovládací prvek | Co dělá |
|---|---|
| **Stáhnout nyní** | Okamžitě zkontroluje všechny externí zdroje. |
| **Automatická aktualizace všech zdrojů každých 5 minut** | Ve výchozím stavu zapnuto. Každých 5 minut se zkontrolují všechny zdroje a znovu se stáhnou **jen ty, které se změnily** (*beze změny (kontrolováno v … UTC)* / *nová data v … UTC*). |
| **Exponent λ (SM6FHZ)** | Exponent k kmitočtového pravidla, výchozí 3 (1–4). |

## Co se zobrazuje

| Panel | Obsah |
|---|---|
| **Meteory/hodinu – včera a dnes (UTC)** | Azurové sloupce = počty z Collmu (platné), červené sloupce = zahozené, silná oranžová čára = *odhad na … MHz* na pravé stupnici |
| **Výšky stop (Collm)** | Meteory na km výšky mezi 70 a 110 km, s nejčastější výškou (modus), průměrem, mediánem a směrodatnou odchylkou |
| Snímek z Collmu | Původní graf SKiYMET, tak jak byl stažen |
| Snímek ze Sodankylä | Nejnovější snímek počtů meteorů z radaru v Sodankylä (jen zobrazen; jeho formát se nečte) |

Řádek nad grafy uvádí, kdy byl graf z Collmu přečten a jaká svislá stupnice byla nalezena (*stupnice přečtená z grafu: 0-… meteorů/hodinu*).

## Jak se čte graf z Collmu

Graf z Collmu (720 × 720 pixelů, čisté barvy) má pevné polohy os, ale radar **každý den přizpůsobuje svislou stupnici** změřeným hodnotám (např. 0–1,2·10³ dne 5. 11. 2026 a 0–1,0·10³ dne 6. 11. 2026, s posunutými značkami). YA-MS proto:

1. najde dlouhé značky osy;
2. **přečte popisky** nejvyšší značky a nuly porovnáním každého znaku s maticovým písmem grafu;
3. pro každou hodinu i (0–47, včera a dnes) vezme prostřední sloupec a první azurový pixel shora, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top a y0 jsou řádky nejvyšší značky a nuly, N_top hodnota přečtená na nejvyšším popisku (×1000). Rozlišení: asi 7–8 meteorů/hodinu na pixel. *Volba programu (rov. 42 příručky).*

Pokud popisek nelze přečíst, program se vrátí ke kalibraci z 5. 11. 2026 (**kalibrovaná stupnice 0-1200 meteorů/hodinu**) a oznámí to oranžově: *Nelze přečíst svislou stupnici toku (horní popisek: …): hodnoty je třeba zkontrolovat.* Pokud se změní samotný formát grafu (*Formát grafu se změnil (…x…): nelze přečíst* nebo *Osy toku nenalezeny na očekávaném místě*), je třeba čtení znovu zkalibrovat: nahlaste to prosím (viz [Přispívání](Contributing-and-Contacts-cs)).

### Výšky stop

Z histogramu výšek (n_k meteorů v km k, střední výška h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Rov. 43 příručky.* Při zaškrtnutém **z radaru** (řada 2 ovládacích prvků) se **modus** stane výškou stopy pro všechny výpočty. Ověření: graf z 5. 11. 2026 – modus 89,5 km, průměr 88,6 km, směrodatná odchylka 6,8 km, což potvrzuje ~90 km z článku Cerrotta–Sartori (průměr SKiYMET).

Pokud se změní stupnice grafu výšek, program upozorní: *statistiky výšek (modus, průměr, medián) zůstávají platné, absolutní počty ne.*

## Odhad pro vaše pásmo

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Experimentální pravidla podle **SM6FHZ** (VUSHF 2025): počet a intenzita odrazů se mění s λ³, trvání s λ²; závislost na λ³ je stejná jako v McKinleyho rovnici pro podhusté stopy. Zobrazuje se také maximální trvání pingu podle IARU Region 1 (1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz). Hodnoty jsou orientační, k porovnání se zkušeností z pásma. Faktor stanice K a srovnání s RMOB jsou v [Experimentálních předpovědích](Experimental-Forecasts-cs).

## Bez připojení

Pokud nelze dosáhnout žádného zdroje, objeví se **jednou** zpráva: *Žádné připojení k internetu. Data radarů a RMOB nelze aktualizovat: program používá poslední uložená data a sám to zkouší znovu každých 5 minut.* Stavový řádek dole zčervená (*ŽÁDNÉ PŘIPOJENÍ K INTERNETU …*), dokud se připojení neobnoví (*Připojení obnoveno.*).

## Archivy a zdroje

| Soubor (v `data/`) | Obsah |
|---|---|
| `flusso_collm.csv` | Hodinový archiv toku přečteného z Collmu (již přítomné hodiny se aktualizují) |
| `quote_collm.csv` | Archiv výšek stop |
| `radar/` | Nejnovější stažené snímky (a soubory RMOB) |
| `fonti_radar.csv` | Adresy radarových zdrojů, `attivo=1/0` pro zapnutí/vypnutí každého z nich |

| Zdroj | Kmitočet | Poznámky |
|---|---|---|
| Meteorický radar Collm, Univerzita Lipsko (LIM) a IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | aktualizováno každou hodinu v 10. minutě UTC; tok včera + dnes, rozložení výšek |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | jen snímek (radar se modernizuje, projekt DECC) |
| swan.ms (kopie Collmu) | 36,2 MHz | ve výchozím stavu vypnuto; používejte jen se svolením DL1DBC |

> Data radarů patří příslušným institucím (Univerzita Lipsko / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
