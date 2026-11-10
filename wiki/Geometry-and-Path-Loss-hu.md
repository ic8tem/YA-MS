[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · **Magyar** · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometria és útvonalcsillapítás

*Fül: Előrejelzés számítása › Geometria és útvonalcsillapítás.*

[![Geometria és útvonalcsillapítás](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Az útvonal szöveges jelentése (kijelölhető, így kimásolható), jobbra pedig az **Antennaeleváció a szórási ponttól mért távolság függvényében** diagram. A szögletes zárójelben lévő számok a számítási kézikönyv (`doc/YA-MS_manuale_calcoli.docx`) egyenleteire utalnak.

## A fül bemenetei

| Mező | Alapértelmezés | Felhasználás |
|---|---|---|
| **Teljesítmény W** | 400 | Az adó teljesítménye az összeköttetési mérleghez |
| **Antennanyereség dBi (adó = vevő)** | 14 | Ugyanaz az antenna mindkét végen |
| **Minimális jel dBm** | −130 | Legkisebb érzékelhető jel (cikk: 8 elemes Yagi + előerősítő) |
| **Nyomsűrűség q = 10^ … elektron/m** | 14 | Az alulsűrű nyom lineáris elektronsűrűsége |

Az állomások, a sáv, a nyommagasság, a lebenyeleváció, a tartócső és a hot spot-távolság a [vezérlősorokból](Getting-Started-hu#1-a-vezérlők-három-sora) származik.

## A jelentés részei

| Rész | Tartalom |
|---|---|
| **ÚTVONAL-GEOMETRIA (gömb alakú Föld, R = 6372,7955 km)** | Állomás és DX magasságokkal; távolság, azimut és visszairány; felezőpont (lokátor és koordináták); nyommagasság (*<- a Collm radar által mért leggyakoribb érték*, ha a radarból veszi); antennaeleváció a felezőpont felé |
| **HOT A / HOT B (klasszikus hot spotok az antenna irányzásához)** | Mindkettőhöz: lokátor, azimut Öntől és eltérés a közvetlen iránytól, azimut a DX-től, távolság, eleváció |
| **A KÖZÖS ZÓNA HATÁRAI** | Hatótávolság a nyommagasságban a lebenyelevációval; A határ / B határ azimutokkal |
| Antenna | Tartócső λ-ban, nyereség, vízszintes / függőleges lebeny; a Hot A és a Hot B a lebenyen belül vagy kívül van-e |
| **ÚTVONALCSILLAPÍTÁS (alulsűrű nyom, McKinley 1961; antennanyereség nélkül)** | Táblázat a felezőpontra (előre), a Hot A-ra és a Hot B-re 28, 50, 70, 144, 222 és 432 MHz-en |
| **ÖSSZEKÖTTETÉSI MÉRLEG … MHz-EN (felezőpont)** | Teljesítmény és EIRP, útvonalcsillapítás, jel az antennán, legkisebb érzékelhető jel, **tartalék**; ugyanez a tartalék OH5IY átlagos csillapításával |
| **KÍSÉRLETI SZABÁLYOK A SÁVOK KÖZÖTT (SM6FHZ, VUSHF 2025)** | Szám/intenzitás és időtartam a 144 MHz-hez képest; IARU legnagyobb ping |

## Lokátor és útvonal

Lokátor (4, 6 vagy 8 karakter; a négyzet középpontja, IARU Maidenhead-rendszer) [14]. Távolság, azimut és felezőpont főkör-képletekkel, **r = 6372,7955 km** sugarú gömbön (Cerrotta–Sartori cikk) [15–16]. Az időfüggő számítások a **felezőpontra** vonatkoznak, mert a legjobb időpont a két végpont között akár 1,5 órával is eltérhet (SM6FHZ).

## Antennaeleváció

**Forrás:** a Cerrotta–Sartori cikk képlete (7. ábra), ahol x = d/r, d a visszaverődési pontig mért földi távolság, H a nyommagasság és h az állomás magassága [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Ellenőrzés:** 0,03°-on belül egyezik a pontos gömbi geometriával. A program a kétargumentumú arkusztangenst használja, amely a horizonton túl negatív értékeket ad, és elkerüli a cikkben említett periodicitási problémát. A felezőpont felé mutató negatív eleváció azt jelenti: *az útvonal meghaladja egyetlen ugrás geometriai hatótávolságát*.

## Horizont-hatótávolság

Az a földi távolság, amelynél egy e elevációjú sugár eléri a H magasságot (a fenti képlet geometriai inverze) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Ellenőrzés:** H = 89,5 km, e = 0° → **1062 km**. A cikk példájában (JN44BB–IO53RT) a rajz a horizontmetszéseket kb. 870 km-re helyezi az állomásoktól, ami kb. 2°-kal megemelt lebenynek felel meg (865 km).

## A közös zóna határai

**Forrás:** a cikk azoknak a görbéknek a metszéspontjait határozza meg, ahol az egyes állomások horizontja eléri az E-réteget: két, A és B középpontú, ρ = d_H/r szögsugarú kör metszéspontjait [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Ha 1 − |p0|² < 0, az útvonal hosszabb, mint 2·d_H, és az állomások **nem látnak közös E-réteg-zónát**.

**Ellenőrzés:** ezek a mindkét állomás által látott égbolt **legtávolabbi szélei**, **nem célpontok**. A JN70CN–IN78UO útvonalon (1710 km, azimut 308°) az állomástól 1062 km-re, a közvetlen iránytól 37°-kal balra és jobbra esnek, míg az MSHV 10°-ot javasol. Ezért nevezik őket *A határ* / *B határ* néven, és ezért halványan jelennek meg a térképen.

## Hot A és Hot B

**Forrás:** a visszaverődések két zónában („hot spotok”) koncentrálódnak, kb. **50–150 km-re a felezőpont mindkét oldalán**. Ez az AMS Bulletin 203. számában közölt antennaeltérési táblázat alapja, amelyet W8WN is átvett (10°-os eltérés 1500 és 1800 km-es útvonalakra); az LZ2HV-féle MSHV ugyanezt a kritériumot használja.

**Választás:** a Hot A és a Hot B a felezőponttól (M) s távolságra, az útvonalra merőlegesen lévő pontok (s = 150 km, 30–400 km között állítható); A balra, az Ön állomásától a DX felé nézve, B jobbra [21]. Az állomásról nézett eltérés kb. [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Ellenőrzés:** JN70CN–IN78UO, D = 1710 km: 6,7° s = 100 km-nél, **10,0° s = 150 km-nél** (ugyanaz, mint az MSHV és az AMS/W8WN), 13,2° s = 200 km-nél.

## Alulsűrű útvonalcsillapítás

**Forrás:** McKinley egyenlete alulsűrű nyomokra (β = 0, sin α = 1), antennanyereség nélkül; q = lineáris elektronsűrűség, r_e = klasszikus elektronsugár = 2,818·10⁻¹⁵ m, R1, R2 a nyomtól mért távolságok, φ a szórási szög fele [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Ellenőrzés:** q = 10¹⁴ elektron/m mellett 144 MHz-en: **181–192 dB** 600 és 2200 km között, összhangban a cikk 144 MHz-es hivatkozásaival: **legalább 182 dB** (GM8JBJ, Kaiser & Closs 1952 alapján) és **átlagosan 200 dB** (OH5IY).

## Összeköttetési mérleg

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. A nyereségeket dBi-ben kell megadni, a program dBd-ben használja őket (dBi − 2,15). A jelentés a tartalékot **OH5IY átlagos útvonalcsillapításával** is megadja (200 dB 144 MHz-en, λ³ szerint a választott sávra skálázva). A cikk hivatkozása: kb. **70 dBm EIRP** szükséges (−130 dBm + 200 dB, pl. kb. 400 W 14 dBi-s antennára).

## Antennanyereség és lebeny

**Nyereség – forrás:** Günter Hoch **DL6WU** görbéje hosszú Yagikra a tartócső L hosszának függvényében, W8IO közlése szerint (kb. 2 λ-tól érvényes) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Ellenőrzés L.B. Cebik W4RNL 432 MHz-es NEC-modelljeivel** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemek | Tartócső (λ) | W4RNL NEC (dBi) | Képlet (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Az eltérés sosem haladja meg a **0,1 dB**-t: a nyereség inkább a tartócső hosszától függ, mint a konstrukciótól (a VK3AUU Yagik tartócsöve ugyanannyi elemnél rövidebb). A VK5DJ-féle Yagi Calculator a VK3AUU, WA2PHW és DJ9BV változatokra is ad becslést, ezek képletei azonban nem publikusak.

**Lebeny – forrás:** Kraus szabálya, kör alakú lebennyel θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Ellenőrzés:** W4RNL DL6WU Yagikra készített NEC-modelljei a Krausénál **5–10 %-kal keskenyebb vízszintes lebenyt** adnak: 33,8° / 26,4° / 22,6° 12, 19 és 26 elemre, szemben a 37,3° / 28,0° / 23,9°-kal. Az egyszerű képletek figyelmen kívül hagyják az előre irányuló mellékhurkokat (W4RNL, *Long-Boom Yagi Rules of Thumb*). Hosszú tartócsöveknél a függőleges lebeny kissé szélesebb a vízszintesnél (14 λ: 18,4° / 18,8°).

**Választás** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Példa: 14 λ-s Yagi 432 MHz-en → 20,3 dBi, lebeny 18,1° vízszintesen és 19,5° függőlegesen; W4RNL modelljei 20,4 dBi-t és 18,4° / 18,8°-ot adnak. Ezek néhány DL6WU antennából levezetett közelítő szabályok.

Az antennát a program mindig a DX felé irányítottnak tekinti. Egy hot spot **a lebenyen belül** van, ha |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: ekkor az [Égbolt-kupola](Sky-View-hu) fülön szürkével rajzolódik, és figyelmeztetés jelenik meg. A hatékonyságszámításban az antennák izotropok; a valódi lebenyt csak ehhez az ellenőrzéshez használja.

## Kísérleti szabályok a sávok között

A 144 MHz-hez képest: szám/intenzitás × (144/f)³ (dB-ben), időtartam × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1. Régió legnagyobb pingidőtartam: 1000 ms 50 MHz-en, 500 ms 70 MHz-en, 100 ms 144 MHz-en, 13 ms 432 MHz-en (VHF Handbook, a cikk idézete szerint). Lásd még: [Kísérleti előrejelzések](Experimental-Forecasts-hu).
