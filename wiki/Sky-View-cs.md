**English** · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Nebeská klenba

*Karta: Předpovědní výpočet › Předpovědní výpočet.*

[![Nebeská klenba](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Tato podkarta (nebeská klenba z dřívějších verzí) ukazuje na jedné obrazovce, **kde** jsou právě užitečné stopy a **kam mířit**. Vlevo je **půdorys** trasy; vpravo seznam rojů, malá nebeská klenba s radianty, text výpočtu a **řez** viděný od vaší antény. Vše se vztahuje k okamžiku zvolenému pomocí *Datum výpočtu (UTC)* a posuvníku *Hodiny (od −12 do +36 h)* (výchozí reálný čas, kroky po 15 minutách).

**Pruh nad půdorysem** shrnuje výpočet pro daný okamžik: datum a čas (*nyní* nebo počet hodin od teď), **index trasy Σ ZHR×η**, **nejužitečnější roj** s jeho ZHR a účinností (také v dB vzhledem k referenci DJ5HG, viz [Výpočet účinnosti](Efficiency-Calculation-cs)), počet rojů nad obzorem a **doporučený Hot** s jeho azimutem.

Na malé nebeské klenbě udává **oranžová čára** procházející zenitem vždy **správné směry antény**, kolmé na drift zvoleného roje (nebo toho nejpříznivějšího): azimut radiantu ±90°, s popiskem *anténa NNN°* na obou koncích, s tolerancí ±45° vyznačenou tenkými čarami. Krátké oranžové značky na okraji udávají kolmé směry ostatních užitečných rojů.

## Půdorys (vlevo)

Mapa Evropy viděná shora (**V vpravo**) se stupňovou škálou kolem. Popisek pod mapou udává její poloměr (*Mapa: okraj = … km od stanice*).

| Prvek | Zobrazení |
|---|---|
| Trasa / DX | Zelená čára od vaší stanice k DX stanici (vždy skutečná trasa po hlavní kružnici mezi lokátory) |
| **Hot A / Hot B** | Body na obou stranách středu trasy, kolmo na trasu, ve vzdálenosti podle tabulky odklonů AMS (nebo zadané ručně). **Červená = doporučený**, **růžová = mimo lalok antény**, **šedá = uvnitř laloku** (s varováním) |
| Lalok antény | Vodorovný lalok −3 dB kolem azimutu antény (anténa vždy míří na DX), s popiskem *lalok …°* |
| Meze společné zóny | Slabé body *mez A* / *mez B* a dvě kružnice, kde obzor každé stanice protíná vrstvu E (viz [Geometrie](Geometry-and-Path-Loss-cs#meze-společné-zóny)) |
| Drift roje | **Žlutá čára**: směr, ve kterém zvolený roj (nebo ten nejpříznivější) přechází oblohou, tj. azimut radiantu |
| Nejlepší směry | **Oranžové tečky**: dva směry kolmé na drift (azimut radiantu ±90°, SM6FHZ) |
| **Zóny PREV** | Světlé elipsy: kam **právě teď** padají nejpravděpodobnější stopy, jedna na každé straně trasy |

Popisky se nepřekrývají: Hot A a PREV A jsou napsány vlevo od trasy, B vpravo. **Legenda** je skládací sloupec vpravo od mapy.

**Myš na mapě:** **levé kliknutí = lokátor protistanice**, **pravé kliknutí = lokátor mé stanice**. Trasa se okamžitě přepočítá.

Volby nad seznamem rojů: **Směry Hot A / Hot B**, **Mapa Evropy** (Natural Earth, stažená do `data/mappa` při prvním spuštění), **Pohled shora (V vpravo)**.

### Doporučený Hot

Pro zobrazený čas program sečte přes všechny roje nad obzorem váhu ZHR × účinnost, rozdělenou mezi stranu A (podíl f_A) a stranu B. Strana s větší váhou dává doporučený Hot, kreslený červeně:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Volba programu (manuál, rov. 23).* Zdroj myšlenky: DJ5HG, podle DF5HC (konference DARC 2018) – v závislosti na poloze radiantu je příznivější jeden ze dvou bodů, HOT-A nebo HOT-B. Natočení o 10–30° k této straně (side-scatter) pochází z článku Cerrotta–Sartori.

### Zóny PREV

Pro každý bod P vrstvy E se sečtou příspěvky všech aktivních rojů k účinnosti (stejná zrcadlová podmínka jako u [účinnosti](Efficiency-Calculation-cs#model)), vážené ZHR. Body s alespoň 3 % maxima tvoří zóny PREV; každá se kreslí jako elipsa se středem = vážený průměr bodů a osami = dvojnásobek jejich rozptylu.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Volba programu (manuál, rov. 34).* Je to praktické pravidlo: pokud roj přechází od severu k jihu, užitečné stopy padají na východ a na západ.

## Seznam rojů (vpravo nahoře)

| Sloupec | Význam |
|---|---|
| Roj, Zkratka | Název a kód IMO |
| ZHR nyní | Aktivita v tomto okamžiku (ZHR v maximu podle IMO s profilem aktivity) |
| Azimut, Elev. | Poloha radiantu viděná z vaší stanice |
| Účin. % | Účinnost roje pro tuto trasu |
| Strana | A nebo B, strana, ze které přichází většina odrazů |
| Nejl. směr | Azimut radiantu ±90° |
| Vychází, Zapadá | Východ a západ radiantu (UTC); *cirkumpolární* nebo *stále pod obzorem*, pokud to platí |

Kliknutím na řádek roj vyberete: žlutá čára driftu a oranžové tečky se podle něj přizpůsobí.

## Malá nebeská klenba (vpravo uprostřed)

Radianty na nebeské klenbě viděné z vaší stanice, s jejich **kódem IMO** a **denní dráhou azurově** (hodiny UTC). **Kliknutím na radiant** ho vyberete. Barvy:

| Barva | Význam |
|---|---|
| Žlutá | účinnost ≥ 50 % a ZHR ≥ 2 |
| Oranžová | účinnost ≥ 20 % |
| Tmavě červená | účinnost < 20 % |
| Šedá | téměř neaktivní |

Vedle je text výpočtu: délka a azimut trasy, střed trasy a jeho elevace, azimuty a odklony Hot A / Hot B, doporučený Hot (*… doporučený nyní: az. …° (…% očekávaných odrazů)*), meze společné zóny a připomínka: *Nejlepší nasměrování pro roj: KOLMO ke směru příletu (azimut radiantu ±90°, tolerance ±40–50°, SM6FHZ)*.

## Řez (vpravo dole)

*ŘEZ - nejpravděpodobnější stopy viděné od antény směrem k protistanici.* Vodorovně **azimut vůči protistanici** (← A vlevo, B → vpravo), svisle **elevace**. Pro každý roj se vezme 14 nejsilnějších bodů odrazu; každá stopa je úsečka orientovaná k radiantu, od 10 km nad do 10 km pod výškou stop (nejvýše 60 km na každou stranu), silnější, čím je pravděpodobnější. Kreslí se také lalok antény (kružnice −3 dB kolem elevace laloku), DX stanice a Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Volba programu (manuál, rov. 35).*

## Varování

| Varování | Kdy |
|---|---|
| **VAROVÁNÍ: Hot A (a/nebo Hot B) spadá do laloku antény …** | Hot spot je v rozmezí ±θ/2 od azimutu antény (θ = vodorovný lalok −3 dB): při tomto směru je již pokryt. Na mapě se zobrazí šedě. Doporučený Hot zůstává červený. |
| **RADIANT PŘÍLIŠ VYSOKO (nad 70°)** | Užitečný radiant je z vaší stanice výše než 70°: stopy padají téměř svisle a k trase odrážejí málo (DF5HC, DH9GCD). Tytéž hodiny jsou v [hodinové tabulce](Efficiency-Calculation-cs#hodinová-tabulka) označeny ↑. |
| **NÍZKÝ RADIANT PODÉL TRASY** | Aktivní radiant je pod 20° a do 30° od směru trasy. Vypočtená účinnost zůstává nízká (opatrně), ale DJ5HG očekává vzácné silné odrazy od tečných stop rovnoběžných s trasou (Hamburk–Narvik, Kvadrantidy, asi 19 UTC): vyplatí se poslouchat. |
| **TRASA ZA HORIZONTEM STOPY** | Ve výšce stop je střed trasy pod obzorem obou stanic (asi 2120 km se stopami v 90 km). Varování uvádí potřebnou minimální výšku stop (asi 96 km pro 2200 km, 105 km pro 2300 km): spojení je možné jen s nejvyššími stopami a účinnosti i útlumy jsou na hranici modelu |
| *Žádná společná zóna vrstvy E* | Trasa je delší než dvojnásobek dosahu ve výšce stop: obě stanice nevidí společnou část vrstvy E (jeden skok je nemožný). |
| *Žádný doporučený Hot* | V tuto dobu není téměř žádný roj aktivní. |

Vzor pro grafiku nebeské klenby: Swan Meteor Skyview od DL1DBC (swan.ms); polární diagram s nejlepším směrem: RadiantCalc od SM6FHZ.
