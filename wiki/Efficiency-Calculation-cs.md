LANGBAR

# Výpočet účinnosti

*Karta: Výpočet předpovědi › Výpočet účinnosti.*

[![Výpočet účinnosti](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Účinnost** roje udává v procentech, nakolik poloha jeho radiantu umožňuje odrazy na **vaší** trase. Pojem pochází od Ilkky **OH5IY** (MS-Soft) a převzal ho článek Cerrotta–Sartori: maximum účinnosti se neshoduje s vizuálním maximem (ZHR), protože závisí na tom, kde je radiant vzhledem k oběma stanicím. MCG_MS od DL5MCG uplatňuje stejnou myšlenku na čtyři pevné směry; YA-MS ji počítá pro **skutečnou trasu** mezi oběma lokátory.

Tato karta ji ukazuje hodinu po hodině pro den zvolený v poli *Den pro tabulku 24 h (UTC)* (hodnoty v půl každé hodiny).

## Přehledové karty

| Karta | Obsah |
|---|---|
| **NEJLEPŠÍ DENNÍ DOBA** | Hodina s nejvyšším indexem trasy, tento index a převládající strana (A/B s jejím %) |
| **NEJPŘÍZNIVĚJŠÍ ROJ** | Roj s největším ZHR × účinnost za den, jeho účinnost, hodina a strana a **nejlepší směrování** (azimut radiantu +90° / −90°) |
| **NYNÍ** | Index a převládající strana v této hodině a doporučený Hot (jen pokud je zvolený den dnešek) |
| **EXPERIMENTÁLNÍ PŘEDPOVĚĎ** | Očekávané odrazy/hodinu nyní, za 1 h a za 2 h na kmitočtu předpovědi (Collm, pravidla SM6FHZ; viz [Experimentální předpovědi](Experimental-Forecasts-cs)) |

Pod kartami vysvětluje pruh písmena A a B (viz níže).

## Graf

*Hodinová účinnost pro … dne … (UTC, hodnoty v půl hodiny).* Až pro pět rojů: účinnost % plnou čarou a vzorec DH9GCD tečkovanou čarou stejné barvy; **index trasy** jako modré sloupce na pravé stupnici.

## Hodinová tabulka

Jeden řádek na každý roj aktivní v daný den (seřazeno podle ZHR), 24 sloupců pro hodiny (UTC):

| Buňka | Význam |
|---|---|
| `63A` | účinnost 63 %, většina odrazů ze strany **A** |
| `41B` | účinnost 41 %, strana **B** |
| `3` | účinnost pod 5 %: číslo bez písmene strany |
| prázdná | účinnost pod 1 % |
| `…↑` | radiant je v té hodině z vaší stanice **výše než 70°** (příliš vysoko) |
| žlutý text | účinnost ≥ 50 % |

- **A** = **vlevo** při pohledu od vaší stanice ke stanici DX (zóna Hot A); **B** = **vpravo** (zóna Hot B). Vyplatí se natočit anténu o **10–30° k této straně** (side-scatter, článek Cerrotta–Sartori).
- **Světle modré řádky** (*DH9GCD %*, pod každým rojem): vzorec DH9GCD pro srovnání.
- **Řádek Σ**: *Index trasy (ZHR×účin.)*.
- **Oranžový řádek** (*Předpověď … MHz (odr./hodinu)*): experimentální předpověď pro hodiny, pro které existuje (dnešek a část zítřka).

## Model

Všechny kroky jsou ve [výpočetní příručce](Efficiency-Explanation-cs) (`doc/YA-MS_manuale_calcoli.docx`, kapitola 5). Ve zkratce:

**1. Zrcadlový odraz.** Stopa pošle signál z A do B jen tehdy, je-li tečnou k elipsoidu s ohnisky v A a B (McKinley 1961). Stopy roje jsou rovnoběžné se směrem k radiantu ŝ (článek; McKinley). Pro každý bod P vrstvy E, s jednotkovými vektory směrem ke stanicím:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Na stejném zákonu je založen QTFGUI od DJ5HG (kuželový rozptyl). Podmínka se přijímá s gaussovskou tolerancí σ = 0,05 rad (asi 3°) – *volba programu*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Váha každého bodu.** Výkon podhusté stopy (McKinley), φ = polovina úhlu rozptylu (omezeno na 85°, *volba*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Počet meteorů dopadajících do bodu je úměrný sinu elevace radiantu v tomto bodě (ŝ·û_P), což je stejná korekce, jakou IMO používá pro ZHR.

**3. Součet a procento.** Body po 15 km ve výšce stopy, jen tam, kde je obě stanice vidí nad elevací laloku (*volba*). 100 % je nejpříznivější poloha radiantu pro danou trasu:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F se počítá jednou pro každou trasu na mřížce směrů (azimut po 5°, elevace po 2,5°) a interpoluje se.

**4. Strana a index.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Písmeno v tabulce je strana s větším podílem. *Volby programu (rov. 32–33 příručky).*

## Srovnání s DH9GCD

Nezávislá kontrola: vzorec nejlepšího směru od **DH9GCD**, citovaný **DF5HC** (konference DARC, leden 2018), kde El a Az jsou elevace a azimut radiantu viděné z vaší stanice a P je azimut stanice DX:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Maximum má při radiantu ve 45° a kolmo na trasu. DF5HC považuje radiant pod 20° za příliš nízký a **nad 70° za příliš vysoký**: tyto hodiny dostanou v tabulce ↑ a na [Nebeské klenbě](Sky-View-cs#upozornění) upozornění. Vzorec ignoruje vzdálenost a výšky, ale je dobrou referencí.

## Ověření

| Ověření | Výsledek |
|---|---|
| Pravidlo SM6FHZ (VUSHF 2025): nejlepší trasa kolmá na azimut radiantu, směrování = az. radiantu ±90°, tolerance ±40–50° | Model ho reprodukuje; s radiantem v ose trasy a vysoko na obloze je účinnost téměř nulová |
| QTFGUI od DJ5HG, Hamburk JO53IM – Barcelona, Kvadrantidy, 4. ledna (příklad z jeho příručky) | QTFGUI: 07:00 směrování 252°, −8 dB; 08:00 žádná zóna odrazu; 09:00 směrování 168°, −4 dB. YA-MS (výška 102 km jako QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Všechny tři metody vidí díru v 08:00, kdy je radiant téměř v zenitu |
| Vzorkování po 5 km místo po 15 km | procenta se změní o méně než 0,3 bodu |

> Stupnice používaná OH5IY a MCG_MS není podrobně známa (příručky MS-Soft nejsou k dispozici): než budete procenta považovat za rovnocenná, porovnejte je s těmito programy. Model uvažuje jen podhusté stopy s izotropními anténami; nadhusté záblesky a sporadické pozadí v účinnosti nejsou (sporadické pozadí představuje tok z radaru).
