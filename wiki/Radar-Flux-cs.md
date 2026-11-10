**English** · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Tok z radaru

*Karta: Živě a data v reálném čase › Tok z radaru.*

[![Tok z radaru](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Tato karta ukazuje, co profesionální meteorické radary počítají **právě teď**: hodinové počty meteorů a výšky stop z radaru SKiYMET v **Collmu** (Lipská univerzita / IAP Kühlungsborn, Německo, 36,2 MHz) a nejnovější obrázek z radaru **Sodankylä** (SGO, Finsko). Počty z Collmu napájejí odhad pro vaše pásmo a [Experimentální předpovědi](Experimental-Forecasts-cs); naměřená výška stop napájí celou geometrii.

## Ovládací prvky

| Ovládací prvek | Co dělá |
|---|---|
| **Stáhnout nyní** | Zkontroluje najednou všechny externí zdroje. |
| **Automatická aktualizace všech zdrojů každých 5 minut** | Ve výchozím stavu zapnuto. Každých 5 minut se zkontrolují všechny zdroje a znovu se stáhnou **jen ty, které se změnily** (*beze změny (kontrolováno v … UTC)* / *nový údaj v … UTC*). |
| **Exponent λ (SM6FHZ)** | Exponent k frekvenčního pravidla, výchozí 3 (1–4). |

## Co se zobrazuje

| Panel | Obsah |
|---|---|
| **Meteory/hod - včera a dnes (UTC)** | Azurové sloupce = počty z Collmu (platné), červené sloupce = vyřazené, silná oranžová čára = *odhad na … MHz* na pravé stupnici |
| **Výšky stop (Collm)** | Meteory na km výšky mezi 70 a 110 km, s nejčastější výškou (modus), průměrem, mediánem a směrodatnou odchylkou |
| Obrázek z Collmu | Původní graf SKiYMET tak, jak byl stažen |
| Obrázek ze Sodankylä | Nejnovější obrázek s počty meteorů z radaru Sodankylä (jen se zobrazuje; jeho formát se nečte) |

Řádek nad grafy říká, kdy byl graf z Collmu přečten a jaká svislá stupnice byla nalezena (*měřítko přečtené z grafu: 0-… meteorů/hod*).

## Jak se čte graf z Collmu

Graf z Collmu (720 × 720 pixelů, čisté barvy) má pevné polohy os, ale radar **každý den přizpůsobuje svislou stupnici** naměřeným hodnotám (např. 0–1,2·10³ dne 5. 11. 2026 a 0–1,0·10³ dne 6. 11. 2026, s posunutými dílky). YA-MS proto:

1. najde dlouhé dílky osy;
2. **přečte popisky** nejvyššího dílku a nuly porovnáním každého znaku s maticovým písmem grafu;
3. pro každou hodinu i (0–47, včera a dnes) vezme prostřední sloupec a první azurový pixel shora, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top a y0 jsou řádky nejvyššího dílku a nuly, N_top hodnota přečtená na nejvyšším popisku (×1000). Rozlišení: asi 7–8 meteorů/hodinu na pixel. *Volba programu (manuál, rov. 42).*

Pokud popisek nelze přečíst, program se vrátí ke kalibraci z 5. 11. 2026 (**kalibrované měřítko 0-1200 meteorů/hod**) a oznámí to oranžově: *Nelze přečíst svislé měřítko toku (popisek nahoře: …): hodnoty je třeba ověřit.* Pokud se změní samotný formát grafu (*Formát grafu se změnil (…x…): nelze přečíst* nebo *Osy toku nebyly nalezeny v očekávané poloze*), je třeba čtení znovu zkalibrovat: prosím nahlaste to (viz [Spolupráce](Contributing-and-Contacts-cs)).

### Výšky stop

Z histogramu výšek (n_k meteorů v km k, střední výška h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Manuál, rov. 43.* Při zaškrtnutí **z radaru** (řada 2 ovládacích prvků) se **modus** stane výškou stop pro všechny výpočty. Ověření: graf z 5. 11. 2026 – modus 89,5 km, průměr 88,6 km, směrodatná odchylka 6,8 km, což potvrzuje ~90 km z článku Cerrotta–Sartori (průměr SKiYMET).

Pokud se změní stupnice grafu výšek, program upozorní: *statistiky výšek (modus, průměr, medián) zůstávají platné, absolutní počty ne.*

## Odhad pro vaše pásmo

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Experimentální pravidla od **SM6FHZ** (VUSHF 2025): počet a intenzita odrazů se mění s λ³, délka s λ² (u McKinleyho je λ³ výkon jedné stopy; počet stop se mění přibližně s λ^1,5 a při dopředném rozptylu délky rostou také se sec²φ: viz [Experimentální předpovědi](Experimental-Forecasts-cs)). Zobrazuje se také maximální délka pingu podle IARU Region 1 (1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz). Hodnoty jsou orientační, k porovnání se zkušeností z pásma. Faktor stanice K a srovnání s RMOB jsou na stránce [Experimentální předpovědi](Experimental-Forecasts-cs).

## Bez připojení

Pokud není dostupný žádný zdroj, objeví se **jednou** zpráva: *Chybí připojení k internetu. Data radarů a RMOB nelze aktualizovat: program používá naposledy uložená data a sám to zkouší znovu každých 5 minut.* Stavový řádek dole zčervená (*ŽÁDNÉ PŘIPOJENÍ K INTERNETU …*), dokud se připojení neobnoví (*Připojení obnoveno.*).

## Archivy a zdroje

| Soubor (v `data/`) | Obsah |
|---|---|
| `flusso_collm.csv` | Hodinový archiv toku načteného z Collmu (již přítomné hodiny se aktualizují) |
| `quote_collm.csv` | Archiv výšek stop |
| `radar/` | Naposledy stažené obrázky (a soubory RMOB) |
| `fonti_radar.csv` | Adresy radarových zdrojů, `attivo=1/0` pro zapnutí/vypnutí každého z nich |

| Zdroj | Frekvence | Poznámky |
|---|---|---|
| Meteorický radar Collm, Lipská univerzita (LIM) a IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | aktualizace každou hodinu v 10. minutě UTC; tok včera + dnes, rozložení výšek |
| Geofyzikální observatoř Sodankylä – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | jen obrázek (radar se modernizuje, projekt DECC) |
| swan.ms (kopie dat z Collmu) | 36,2 MHz | ve výchozím stavu vypnuto; používejte jen se svolením DL1DBC |

> Radarová data patří svým institucím (Lipská univerzita / IAP Kühlungsborn, Geofyzikální observatoř Sodankylä).
