LANGBAR

# Nebeská klenba

*Karta: Výpočet předpovědi › Výpočet předpovědi.*

[![Nebeská klenba](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Tato podkarta (nebeská klenba z dřívějších verzí) ukazuje na jedné obrazovce, **kde** právě jsou užitečné stopy a **kam směrovat**. Vlevo je **půdorys** trasy; vpravo seznam rojů, malá nebeská klenba s radianty, text výpočtu a **řez** viděný od vaší antény. Vše se vztahuje k času posuvníku *Čas nebeské klenby* (výchozí je reálný čas; ±36 h v krocích po 15 minutách).

V malé nebeské klenbě udává **oranžová čára** procházející zenitem vždy **správné směry antény**, kolmé na posun vybraného roje (nebo nejpříznivějšího roje): azimut radiantu ±90°, s popiskem *anténa NNN°* na obou koncích a s tolerancí ±45° vyznačenou tenkými čarami. Krátké oranžové značky na okraji udávají kolmé směry ostatních užitečných rojů.

## Půdorys (vlevo)

Mapa Evropy viděná shora (**V vpravo**) se stupnicí ve stupních kolem dokola. Popisek pod mapou udává její poloměr (*Mapa: okraj = … km od stanice*).

| Prvek | Zobrazení |
|---|---|
| Trasa / DX | Zelená čára od vaší stanice ke stanici DX (vždy skutečná trasa po hlavní kružnici mezi lokátory) |
| **Hot A / Hot B** | Body 150 km (nastavitelné) na obě strany od středu trasy, kolmo na trasu. **Červeně = doporučený**, **růžově = mimo lalok antény**, **šedě = uvnitř laloku** (s upozorněním) |
| Lalok antény | Vodorovný lalok −3 dB kolem azimutu antény (anténa vždy směrovaná na DX), s popiskem *lalok …°* |
| Meze společné zóny | Slabé body *mez A* / *mez B* a dvě kružnice, kde obzor každé stanice protíná vrstvu E (viz [Geometrie](Geometry-and-Path-Loss-cs#meze-společné-zóny)) |
| Posun roje | **Žlutá čára**: směr, kterým vybraný roj (nebo nejpříznivější roj) přejíždí oblohu, tj. azimut radiantu |
| Nejlepší směrování | **Oranžové body**: dva směry kolmé na posun (azimut radiantu ±90°, SM6FHZ) |
| **Zóny PREV** | Světlé elipsy: kam **právě teď** padají nejpravděpodobnější stopy, jedna na každé straně trasy |

Popisky se nepřekrývají: Hot A a PREV A jsou psány vlevo od trasy, B vpravo. **Legenda** je sbalitelný sloupec vpravo od mapy.

**Myš na mapě:** **levé tlačítko = lokátor stanice DX**, **pravé tlačítko = lokátor mé stanice**. Trasa se okamžitě přepočítá.

Volby nad seznamem rojů: **Směry Hot A / Hot B**, **Mapa Evropy** (Natural Earth, stažená do `data/mappa` při prvním spuštění), **Pohled shora (V vpravo)**.

### Doporučený Hot

Pro zobrazený čas program sečte přes všechny roje nad obzorem váhu ZHR × účinnost, rozdělenou mezi stranu A (podíl f_A) a stranu B. Strana s větší váhou dává doporučený Hot, vykreslený červeně:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*Volba programu (rov. 23 příručky).* Zdroj myšlenky: DJ5HG, citovaný DF5HC (konference DARC 2018) – podle polohy radiantu je jeden ze dvou bodů, HOT-A nebo HOT-B, příznivější. Natočení o 10–30° k této straně (side-scatter) pochází z článku Cerrotta–Sartori.

### Zóny PREV

Pro každý bod P vrstvy E se sečtou příspěvky všech aktivních rojů k účinnosti (stejná zrcadlová podmínka jako u [účinnosti](Efficiency-Calculation-cs#model)), vážené ZHR. Body s alespoň 3 % maxima tvoří zóny PREV; každá je vykreslena jako elipsa se středem = vážený průměr bodů a osami = dvojnásobek jejich rozptylu.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Volba programu (rov. 34 příručky).* Je to praktické pravidlo: pokud roj přejíždí od severu k jihu, užitečné stopy padají na východ a na západ.

## Seznam rojů (vpravo nahoře)

| Sloupec | Význam |
|---|---|
| Roj, Kód | Název a kód IMO |
| ZHR nyní | Aktivita v tomto okamžiku (maximální ZHR podle IMO s profilem aktivity) |
| Azimut, Elev. | Poloha radiantu viděná z vaší stanice |
| Účin. % | Účinnost roje pro tuto trasu |
| Strana | A nebo B, strana, ze které přichází většina odrazů |
| Nejlepší směrování | Azimut radiantu ±90° |
| Východ, Západ | Východ a západ radiantu (UTC); *cirkumpolární* nebo *vždy pod obzorem*, pokud to platí |

Kliknutím na řádek roj vyberete: žlutá čára posunu a oranžové body ho následují.

## Malá nebeská klenba (uprostřed vpravo)

Radianty na nebeské klenbě viděné z vaší stanice, s jejich **kódem IMO** a **denní dráhou azurově** (hodiny UTC). **Kliknutím na radiant** ho vyberete. Barvy:

| Barva | Význam |
|---|---|
| Žlutá | účinnost ≥ 50 % a ZHR ≥ 2 |
| Oranžová | účinnost ≥ 20 % |
| Tmavě červená | účinnost < 20 % |
| Šedá | téměř neaktivní |

Vedle ní je text výpočtu: délka a azimut trasy, střed trasy a jeho elevace, azimuty a odsazení Hot A / Hot B, doporučený Hot (*… nyní doporučen: az. …° (…% očekávaných odrazů)*), meze společné zóny a připomínka: *nejlepší směrování pro roj: KOLMO na směr příchodu (azimut radiantu ±90°, tolerance ±40–50°, SM6FHZ)*.

## Řez (vpravo dole)

*ŘEZ – nejpravděpodobnější stopy viděné od antény směrem ke stanici DX.* Vodorovně je **azimut vůči stanici DX** (← A vlevo, B → vpravo), svisle **elevace**. Pro každý roj se vezme 14 nejsilnějších bodů odrazu; každá stopa je úsečka orientovaná k radiantu, od 10 km nad výškou stopy do 10 km pod ní (nejvýše 60 km na každou stranu), tím silnější, čím je pravděpodobnější. Vykreslen je také lalok antény (kružnice −3 dB kolem elevace laloku), stanice DX a Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Volba programu (rov. 35 příručky).*

## Upozornění

| Upozornění | Kdy |
|---|---|
| **UPOZORNĚNÍ: Hot A (a/nebo Hot B) leží uvnitř laloku antény …** | Hot spot leží v rozmezí ±θ/2 od azimutu antény (θ = vodorovný lalok −3 dB): s tímto směrováním je již pokryt. Na mapě zobrazen šedě. Doporučený Hot zůstává červený. |
| **RADIANT PŘÍLIŠ VYSOKO (nad 70°)** | Užitečný radiant je z vaší stanice výše než 70°: stopy padají téměř svisle a odrážejí málo směrem k trase (DF5HC, DH9GCD). Stejné hodiny jsou v [hodinové tabulce](Efficiency-Calculation-cs#hodinová-tabulka) označeny ↑. |
| *Žádná společná zóna vrstvy E* | Trasa je delší než dvojnásobek dosahu ve výšce stopy: obě stanice nevidí společnou část vrstvy E (jeden skok je nemožný). |
| *Žádný doporučený Hot* | V tuto dobu téměř žádný aktivní roj. |

Předloha grafiky nebeské klenby: Swan Meteor Skyview od DL1DBC (swan.ms); polární graf s nejlepším směrem: RadiantCalc od SM6FHZ.
