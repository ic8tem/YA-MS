[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · **Čeština** · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Výpočet účinnosti

*Karta: Předpovědní výpočet › Výpočet účinnosti.*

[![Výpočet účinnosti](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Účinnost** roje udává v procentech, nakolik poloha jeho radiantu umožňuje odrazy na **vaší** trase. Koncept pochází od Ilkky **OH5IY** (MS-Soft) a přebírá ho článek Cerrotta–Sartori: maximum účinnosti se neshoduje s vizuálním maximem (ZHR), protože závisí na tom, kde je radiant vzhledem k oběma stanicím. MCG_MS od DL5MCG uplatňuje stejnou myšlenku na čtyři pevné směry; YA-MS ji počítá pro **skutečnou trasu** mezi oběma lokátory.

Tato karta ji ukazuje hodinu po hodině pro den zvolený v *Datum výpočtu (UTC)* (hodnoty v půl každé hodiny).

## Přehledové karty

| Karta | Obsah |
|---|---|
| **NEJLEPŠÍ DOBA DNE** | Hodina s nejvyšším indexem trasy, index a převažující strana (A/B s jejím %) |
| **NEJPŘÍZNIVĚJŠÍ ROJ** | Roj s největším ZHR × účinnost za den, jeho účinnost, hodina a strana a **nejlepší směr** (azimut radiantu +90° / −90°) |
| **NYNÍ** | Index a převažující strana v tuto hodinu a doporučený Hot (jen když je zvolený den dnešek) |
| **EXPERIMENTÁLNÍ PŘEDPOVĚĎ** | Očekávané odrazy/hodinu nyní, za 1 h a za 2 h na frekvenci předpovědi (Collm, pravidla SM6FHZ; viz [Experimentální předpovědi](Experimental-Forecasts-cs)) |

Pod kartami pruh vysvětluje písmena A a B (viz níže).

## Graf

*Hodinová účinnost pro … dne … (UTC, hodnoty v půl hodiny).* Až pro pět rojů: účinnost v % jako plná čára a vzorec DH9GCD jako tečkovaná čára stejné barvy; **index trasy** jako modré sloupce na pravé stupnici.

## Hodinová tabulka

Jeden řádek pro každý roj aktivní v daný den (seřazeno podle ZHR), 24 sloupců pro hodiny (UTC):

| Buňka | Význam |
|---|---|
| `63A` | účinnost 63 %, většina odrazů ze strany **A** |
| `41B` | účinnost 41 %, strana **B** |
| `3` | účinnost pod 5 %: číslo bez písmena strany |
| prázdná | účinnost pod 1 % |
| `…↑` | radiant je v tu hodinu z vaší stanice **výše než 70°** (příliš vysoko) |
| žlutý text | účinnost ≥ 50 % |

- **A** = **vlevo** při pohledu od vaší stanice k DX stanici (zóna Hot A); **B** = **vpravo** (zóna Hot B). Vyplatí se natočit anténu o **10–30° k této straně** (side-scatter, článek Cerrotta–Sartori).
- **Světle modré řádky** (*DH9GCD %*, pod každým rojem): vzorec DH9GCD pro srovnání.
- **Řádek Σ**: *Index trasy (ZHR×úč.)*.
- **Oranžový řádek** (*Předpověď … MHz (odr./hod)*): experimentální předpověď pro hodiny, pro které existuje (dnes a část zítřka).

## Model

Všechny kroky jsou v [manuálu výpočtů](Efficiency-Explanation-cs) (`doc/YA-MS_manuale_calcoli.docx`, kapitola 5). Ve zkratce:

**1. Zrcadlový odraz.** Stopa pošle signál z A do B, jen pokud je tečnou k elipsoidu s ohnisky v A a B (McKinley 1961). Stopy roje jsou rovnoběžné se směrem radiantu ŝ (článek; McKinley). Pro každý bod P vrstvy E, s jednotkovými vektory směrem ke stanicím:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Stejný zákon je základem QTFGUI od DJ5HG a jeho textu *„Die Geometrie von Meteorscatterverbindungen“* (2004): stopa rozptyluje na kužel, jehož osou je stopa, a slyší ji jen přijímač ležící na kuželu. U ideální stopy je stěna kuželu velmi tenká (zářič dlouhý tisíce vlnových délek); program přijímá podmínku s gaussovskou tolerancí σ = 0,05 rad (asi 3°), která zastupuje to, co ideální kužel nevidí: rozptyl radiantů roje (0,3–1,4° naměřeno GMN), stopy ohnuté větrem a jejich konečnou délku – *volba programu*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Váha každého bodu.** Výkon podhusté stopy (McKinley; ITU-R P.843, rov. 3), φ = polovina úhlu rozptylu (omezená na 85°, *volba*), β = úhel mezi stopou a rovinou šíření A-P-B, p̂ = jednotková normála této roviny:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Volba „Úhel β mezi stopou a trasou (úplný McKinley)“** (ve výchozím stavu zapnuto, opatrné nastavení). Zapnuto: stopy křížící rovinu šíření mají o 10–15 dB menší váhu než ty, které v ní leží, takže žádná stopa není přeceněna. Vypnuto: každá stopa se váží, jako by ležela v rovině (β = 0, váha s cos²φ), jako do verze 1.6. *Ověření:* na trase 1000 km je bez β nejlepší azimut radiantu 15°–90° od trasy v závislosti na elevaci radiantu (30° při radiantu ve 30°, kolmo při radiantu v 60°) a kolmý radiant má při elevaci 30° hodnotu 67 %; s β je nejlepší radiant vždy podél trasy a kolmý klesne na 15 %. S β se pravidlo nejlepšího směru SM6FHZ / DH9GCD ztrácí; β zůstává volbou, ve výchozím stavu zapnutou, protože dává nejopatrnější hodnoty, a jejím vypnutím se pravidlo vrátí.

Počet meteorů dopadajících do bodu je úměrný sinu elevace radiantu v tomto bodě (ŝ·û_P), což je stejná korekce, jakou IMO používá pro ZHR.

**Volba „Delší stopy při nízkém radiantu (DJ5HG)“** (zaškrtávací políčko nad grafem, ve výchozím stavu vypnuto, s nápovědou): DJ5HG poznamenává, že při nízkém radiantu dopadá méně meteorů na km², ale stopy jsou delší (užitečných až 100 km) a častěji splňují zákon odrazu. Při zapnuté volbě se váha změní na min(sin El, 15/100): užitečná tloušťka vrstvy, 15 km, dělená sinem elevace dává délku stopy, omezenou na 100 km. Nad asi 9° se oba efekty vyruší. Při vypnuté volbě zůstává výpočet opatrný.

**Nastavení výpočtu** (na stejném řádku, přepínače): **Opatrné** (výchozí, nejopatrnější hodnoty: výška stop z radaru, normální stopy, β zapnuto), **Jako DJ5HG** (102 km, delší stopy, β) a **Vlastní**, které se vybere automaticky, když ručně změníte výšku, políčko *z radaru*, volbu delších stop nebo β.

**3. Součet a procenta.** Body každých 15 km ve výšce stop, jen tam, kde je obě stanice vidí nad elevací laloku (*volba*). 100 % je nejpříznivější poloha radiantu pro danou trasu:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F se počítá jednou pro každou trasu na mřížce směrů (azimut po 5°, elevace po 2,5°) a interpoluje se.

**Účinnost v dB (reference DJ5HG).** Procenta se vztahují jen k nejlepší poloze radiantu pro danou trasu. Pro porovnání různých tras program udává také účinnost v dB vzhledem k pevné referenci DJ5HG: 0 dB je maximum trasy sever–jih o délce 1000 km přes rovník s radiantem na nebeském rovníku v době rovnodennosti, vypočtené se stejnou výškou a vahami. DJ5HG uvádí přesnost svých hodnot lepší než 6 dB.

**4. Strana a index.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Písmeno v tabulce je strana s větším podílem. *Volby programu (manuál, rov. 32–33).*

## Srovnání s DH9GCD

Primárními zdroji pro nejlepší směr jsou Eshleman & Mlodnosky a Meeks & James (Proc. IRE, 1957), Hines (1955) a jeho experimentální ověření Forsythem, Hinesem a Voganem (1955): užitečné jsou jen radianty na polokružnici oblohy kolmé na osu úhlu rozptylu, počet stop roste se sin El a v blízkosti středu trasy padají užitečné stopy asi H·tan El stranou, na stranu opačnou k radiantu. DJ5HG přidává výhradu: při **nízkém** radiantu přesně podél trasy dává McKinleyho vzorec silné signály (Hamburk–Narvik, Kvadrantidy, asi 19 UTC), takže „radiant rovnoběžný s trasou = téměř nula“ platí jen pro vysoký radiant; program zůstává opatrný a zobrazuje varování *NÍZKÝ RADIANT PODÉL TRASY*.

Nezávislé ověření: vzorec nejlepšího směru od **DH9GCD**, který uvádí **DF5HC** (konference DARC, leden 2018) – nemá publikovaný primární zdroj – kde El a Az jsou elevace a azimut radiantu viděné z vaší stanice a P azimut DX stanice:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Maxima dosahuje s radiantem ve 45° a kolmo na trasu. DF5HC považuje radiant pod 20° za příliš nízký a **nad 70° za příliš vysoký**: tyto hodiny dostanou v tabulce ↑ a na [Nebeské klenbě](Sky-View-cs#varování) se zobrazí varování. Vzorec ignoruje vzdálenost a výšky, ale je to dobrá reference.

## Ověření

| Ověření | Výsledek |
|---|---|
| Pravidlo SM6FHZ (VUSHF 2025): nejlepší trasa kolmá na azimut radiantu, směr = az radiantu ±90°, tolerance ±40–50° | Model ho reprodukuje; s radiantem rovnoběžným s trasou a vysoko na obloze je účinnost téměř nulová |
| QTFGUI od DJ5HG, Hamburk JO53IM – Barcelona, Kvadrantidy, 4. ledna (příklad z jeho manuálu) | QTFGUI: 07:00 směr 252°, −8 dB; 08:00 žádná zóna odrazu; 09:00 směr 168°, −4 dB. YA-MS (výška 102 km jako QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Všechny tři metody vidí díru v 08:00, s radiantem téměř v zenitu |
| Křivky DJ5HG (*Die Geometrie…*, Bild 8–9: z Hamburku a Mnichova, Kvadrantidy, 4. ledna; odečteno z grafu, asi ±0,5 dB a ±15 min) oproti automatickému testu `--prova-dj5hg` (jedna hodnota za hodinu) | Časování: díra s radiantem blízko zenitu připadá na stejné hodiny (Barcelona 07:30–08:30 vs 07–09; Sofie 06:36–07:48 vs 07–08; Narvik 07–08:30 vs 07–09); Moskva je v obou případech zavřená 03–10, otevřená z Hamburku do asi 02:30 a z Mnichova do asi 00:30, jak píše DJ5HG. Směry: rozdíl 2–10°. Úrovně a tvar při 102 km (průměrný a RMS rozdíl od křivek): bez β, bez delších stop −1,6 / 4,0 dB; delší stopy +1,1 / 4,6 dB; β −5,4 / 6,2 dB, ale s nejlepším tvarem (3,0 dB po odečtení průměru, vs 3,6): objeví se hluboká minima při nízkém radiantu (Barcelona −15,6 dB v 17 vs −16 dB v 19:36; Sofie −18,5 dB ve 20 vs −14 dB). β a delší stopy (*Jako DJ5HG*) −2,2 / 4,7 dB; opatrné nastavení (výška z radaru 89,5 km, β zapnuto, bez delších stop) −6,9 / 7,6 dB, tvar 3,3 dB. Bez β ukazuje YA-MS jen slabě minimum s radiantem nízko a téměř rovnoběžným s trasou (−8,6 a −10,4 dB): to je právě výhrada DJ5HG, odtud varování |
| Vzorkování po 5 km místo 15 km | procenta se změní o méně než 0,3 bodu |

> Dokumentace MS-Soft 5.2 definuje účinnost OH5IY jako relativní index jen pro podhusté stopy, se dvěma faktory (elevace radiantu, nejlépe asi 45°, a úhel k trase, nejlépe 90°) a s minimem ručně zvýšeným na 20 % pro přehusté stopy; vzorec není publikován. MCG_MS ji počítá pro čtyři pevné směry a s lokátorem DX pro skutečnou trasu. Model uvažuje jen podhusté stopy s izotropními anténami; přehusté záblesky a sporadické pozadí nejsou v účinnosti zahrnuty (sporadické pozadí představuje tok z radaru).
