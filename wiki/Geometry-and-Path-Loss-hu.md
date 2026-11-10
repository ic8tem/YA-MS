[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · **Magyar** · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometria és útcsillapítás

*Fül: Előrejelzés-számítás › Geometria és útcsillapítás.*

[![Geometria és útcsillapítás](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Az útvonal szöveges jelentése (kijelölhető, így kimásolható), jobb oldalon pedig az **Antennaeleváció a szórási ponttól mért távolság függvényében** grafikon. A szögletes zárójelben lévő számok a számítási kézikönyv (`doc/YA-MS_manuale_calcoli.docx`) egyenleteire utalnak.

## A fül bemenetei

| Mező | Alapértelmezés | Felhasználás |
|---|---|---|
| **Teljesítmény W** | 400 | Adóteljesítmény az összeköttetési mérleghez |
| **Antennanyereség dBi (adó = vevő)** | 14 | Mindkét végen ugyanaz az antenna |
| **Minimális jel dBm** | −130 | A legkisebb észlelhető jel (a cikk szerint: 8 elemes Yagi + előerősítő) |
| **Nyomsűrűség q = 10^ … elektron/m** | 14 | Az alulsűrű nyom lineáris elektronsűrűsége |

Az állomások, a sáv, a nyommagasság, a nyalábeleváció, a boom és a hot spot-távolság a [vezérlősorokból](Getting-Started-hu#1-a-három-vezérlősor) származik.

## A jelentés szakaszai

| Szakasz | Tartalom |
|---|---|
| **AZ ÚTVONAL GEOMETRIÁJA (gömb alakú Föld, R = 6372,7955 km)** | Állomás és DX magassággal; távolság, azimut és visszairány-azimut; felezőpont (lokátor és koordináták); nyommagasság (*← a collmi radar által mért módusz*, ha a radarból származik); antennaeleváció a felezőpont felé |
| **HOT A / HOT B (klasszikus hot spotok, az antenna irányításához)** | Mindegyikhez: lokátor, azimut az Ön állomásától és eltérés a közvetlen útvonaltól, azimut a DX-től, távolság, eleváció |
| **A KÖZÖS ZÓNA HATÁRAI** | Hatótáv a nyommagasságban a nyalábelevációval; A határ / B határ azimutokkal |
| Antenna | Boom λ-ban, nyereség, vízszintes / függőleges nyaláb; Hot A és Hot B a nyalábon belül vagy kívül esik-e |
| **ÚTCSILLAPÍTÁS (alulsűrű nyom, McKinley 1961; antennanyereségek nélkül)** | Táblázat a felezőpontra (előre), Hot A-ra és Hot B-re 28, 50, 70, 144, 222 és 432 MHz-en |
| **ÖSSZEKÖTTETÉSI MÉRLEG … MHz-EN (felezőpont)** | Teljesítmény és EIRP, útcsillapítás, jel az antennán, legkisebb észlelhető jel, **tartalék**; ugyanez a tartalék OH5IY átlagos csillapításával |
| **KÍSÉRLETI SZABÁLYOK A SÁVOK KÖZÖTT (SM6FHZ, VUSHF 2025)** | Szám/erősség és időtartam a 144 MHz-hez képest; IARU szerinti legnagyobb ping |

## Lokátor és útvonal

Lokátor (4, 6 vagy 8 karakter; a négyzet középpontja, IARU Maidenhead-rendszer) [14]. Távolság, azimut és felezőpont főkörképletekkel, **r = 6372,7955 km** sugarú gömbön (Cerrotta–Sartori-cikk) [15–16]. Az időfüggő számítások a **felezőpontra** vonatkoznak, mert a legjobb időpont a két végpont között akár 1,5 órával is eltérhet (SM6FHZ).

## Antennaeleváció

**Forrás:** a Cerrotta–Sartori-cikk képlete (7. ábra), ahol x = d/r, d a reflexiós pontig mért földfelszíni távolság, H a nyommagasság és h az állomás magassága [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Ellenőrzés:** 0,03°-on belül egyezik a pontos gömbi geometriával. A program a kétargumentumú arkusztangenst használja, amely a horizonton túl negatív értékeket ad, és elkerüli a cikkben említett periodicitási problémát. A felezőpont felé mutató negatív eleváció azt jelenti: *az útvonal egyetlen ugrás geometriai hatótávján túl van*.

## Horizont-hatótáv

Az a földfelszíni távolság, amelynél egy e elevációjú sugár eléri a H magasságot (a fenti képlet geometriai inverze) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Ellenőrzés:** H = 89,5 km, e = 0° → **1062 km**. A cikk példájában (JN44BB–IO53RT) az ábra a horizontmetszéseket kb. 870 km-re teszi az állomásoktól, ami kb. 2°-kal megemelt nyalábnak felel meg (865 km).

## A közös zóna határai

**Forrás:** a cikk azoknak a görbéknek a metszéspontjait határozza meg, ahol az egyes állomások horizontja eléri az E-réteget: ezek két, A és B középpontú, ρ = d_H/r szögsugarú kör metszéspontjai [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Ha 1 − |p0|² < 0, az útvonal hosszabb, mint 2·d_H, és az állomások **nem látnak közös E-réteg-zónát**.

**Ellenőrzés:** ezek a mindkét állomás által látott égbolt **legtávolabbi szélei**, **nem célzási pontok**. A JN70CN–IN78UO útvonalon (1710 km, azimut 308°) az állomástól 1062 km-re, a közvetlen útvonaltól 37°-kal balra és jobbra esnek, míg az MSHV 10°-ot javasol. Ezért hívják őket *A határ* / *B határ* néven, és ezért halványan rajzolja őket a térkép.

## Hot A és Hot B

**Forrás:** a sporadikus meteorok reflexiói két zónában („hot spotok”) összpontosulnak a felezőpont két oldalán. J. Richardson (AMS) a DJ5HG által idézett táblázatban (*Die Geometrie von Meteorscatterverbindungen*, 2004) megadja az antenna eltérítését a közvetlen iránytól: **13° 1000 km-nél, 11° 1250 km-nél, 10° 1500 és 2000 km-nél**. Az AMS Bulletin 203. száma, amelyet W8WN is átvett, 10°-ot ad 1500 és 1800 km-re.

**Döntés:** Hot A és Hot B a felezőponttól (M) s távolságra, az útvonalra merőlegesen elhelyezkedő pontok. Az *auto (AMS)* bejelölésekor (alapértelmezés) s Richardson táblázatának eltérítéséből adódik, lineáris interpolációval (1000 km alatt 13°, 2000 km felett 10°): s = (D/2)·tan(eltérítés). Kikapcsolt állapotban s kézzel adható meg, 30–400 km (az MSHV 150 km-t használ); A az Ön állomásától a DX felé nézve balra, B jobbra van [21]. Az állomásról látott eltérés kb. [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Ellenőrzés:** az AMS-táblázattal 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, ugyanannyi, mint a korábban és az MSHV által használt 150 km; rövid útvonalakon a táblázat közelebb hozza a hot spotokat a felezőponthoz.

## Alulsűrű útcsillapítás

**Forrás:** McKinley egyenlete és az ITU-R P.843 ajánlás alulsűrű nyomokra (sin α = 1), antennanyereségek nélkül; q = lineáris elektronsűrűség, r_e = klasszikus elektronsugár = 2,818·10⁻¹⁵ m, R1, R2 a nyomtól mért távolságok, φ a szórási szög fele, β a nyom és az útvonal síkja által bezárt szög, a₁ a kezdeti sugár tényezője, r₀ m-ben és h km-ben (P.843, 4. és 7. egyenlet) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Döntés:** a mérleg és a csillapítástáblázat β = 90°-kal számol (a nyom keresztezi az útvonal síkját, ez a legkedvezőtlenebb eset: óvatos érték), a mérleg pedig a legjobb esetet, β = 0-t is megmutatja. r₀-t a frekvenciához tartozó átlagos visszhangmagasságon veszi, h = 124 − 17 log f (P.843, 15. egyenlet): 0,76 m 95 km-en 50 MHz-hez, 0,40 m 87 km-en 144 MHz-hez, 0,21 m 79 km-en 432 MHz-hez. 1000 km-en a₁ 0,2 dB 50 MHz-en, 0,6 dB 144 MHz-en és 1,4 dB 432 MHz-en (2,9 dB 600 km-en); DJ5HG rögzített 102 km-es értékénél 432 MHz-en kb. 70 dB lenne, vagyis egyáltalán nem lenne visszhang.

**Ellenőrzés:** q = 10¹⁴ elektron/m, 89,5 km-es nyomok és β = 0 mellett 144 MHz-en: **182–192 dB** 600 és 2100 km között (185 dB 1000 km-en), ami a John Worsnop **G4BAO** doktori értekezésében számított **172–190 dB**-es tartományon belül van, GM8JBJ közlése szerint. β = 90°-nál a csillapítás 600 km-en 10 dB-lel, 1000 km-en 13 dB-lel, 2100 km-en 16 dB-lel nő; OH5IY **200 dB-es átlaga** a két eset közé esik. A GM8JBJ táblázatában szereplő 182 dB nem megerősítés: a táblázat nem ad meg frekvenciát, a szakaszonkénti 86,4 dB-je 500 km-es szabadtéri csillapítás 1 MHz-en (hiányzik a 20 log f tag: 144 MHz-en 129,6 dB), tételei pedig 163,8 dB-t adnak ki, nem 182-t; az oldal sem „minimumot”, sem „144 MHz-et” nem említ.

## Összeköttetési mérleg

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. A nyereségeket dBi-ben kell megadni és abban is használja: McKinley csillapítása izotróp antennákra vonatkozik, így nem von le 2,15 dB-es dipólkorrekciót (EIRP = teljesítmény + nyereség). A jelentés megadja a tartalékot **OH5IY átlagos útcsillapításával** is (200 dB 144 MHz-en, λ³-nel a választott sávra skálázva). A cikk referenciaértéke: kb. **70 dBm EIRP** szükséges (−130 dBm + 200 dB, pl. kb. 400 W egy 14 dBi-s antennába).

## Antennanyereség és nyaláb

**Nyereség – forrás:** Günter Hoch **DL6WU** görbéje hosszú Yagikra a boomhossz (L) függvényében, W8IO közlése szerint (kb. 2 λ-tól érvényes) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Ellenőrzés L.B. Cebik W4RNL 432 MHz-es NEC-modelljeivel** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemszám | Boom (λ) | W4RNL NEC (dBi) | Képlet (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Az eltérés sosem haladja meg a **0,1 dB**-t: a nyereség inkább a boomhossztól függ, mint a konstrukciótól (a VK3AUU-Yagik boomja azonos elemszámnál rövidebb). A VK5DJ-féle Yagi Calculator a VK3AUU, WA2PHW és DJ9BV változatokra is ad becslést, ezek képletei azonban nem publikusak.

**Nyaláb – forrás:** Kraus-szabály, kör alakú nyalábbal, θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Ellenőrzés:** W4RNL DL6WU-Yagikra készült NEC-modelljei **5–10 %-kal keskenyebb vízszintes nyalábot** adnak, mint a Kraus-szabály: 33,8° / 26,4° / 22,6° 12, 19 és 26 elemre, szemben a 37,3° / 28,0° / 23,9° értékkel. Az egyszerű képletek figyelmen kívül hagyják az előre irányuló oldalnyalábokat (W4RNL, *Long-Boom Yagi Rules of Thumb*). Hosszú boomoknál a függőleges nyaláb kissé szélesebb a vízszintesnél (14 λ: 18,4° / 18,8°).

**Döntés** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Példa: 14 λ-s Yagi 432 MHz-en → 20,3 dBi, a nyaláb vízszintesen 18,1°, függőlegesen 19,5°; W4RNL modelljei 20,4 dBi-t és 18,4° / 18,8°-ot adnak. Ezek néhány DL6WU-antennából levezetett közelítő szabályok.

Az antennát a program mindig a DX felé irányítottnak tekinti. Egy hot spot akkor van **a nyalábon belül**, ha |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: ekkor szürkén jelenik meg az [Égbolt-kupolán](Sky-View-hu), és figyelmeztetés jelenik meg. A hatékonyság-számításban az antennák izotrópok; a valós nyalábot csak ehhez az ellenőrzéshez használja.

## Kísérleti szabályok a sávok között

A 144 MHz-hez képest: szám/erősség × (144/f)³ (dB-ben), időtartam × (144/f)² (SM6FHZ, VUSHF 2025). Az IARU Region 1 szerinti legnagyobb pingidőtartam: 1000 ms 50 MHz-en, 500 ms 70 MHz-en, 100 ms 144 MHz-en, 13 ms 432 MHz-en (VHF Handbook, a cikk idézete szerint). Lásd még: [Kísérleti előrejelzések](Experimental-Forecasts-hu).
