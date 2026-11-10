**English** · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometrie a útlum trasy

*Karta: Výpočet předpovědi › Geometrie a útlum trasy.*

[![Geometrie a útlum trasy](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Textová zpráva o trase (text lze označit, takže si ho můžete zkopírovat) a vpravo graf **Elevace antény v závislosti na vzdálenosti od bodu rozptylu**. Čísla v hranatých závorkách odkazují na rovnice manuálu výpočtů (`doc/YA-MS_manuale_calcoli.docx`).

## Vstupy této karty

| Pole | Výchozí | Použití |
|---|---|---|
| **Výkon W** | 400 | Výkon vysílače pro energetickou bilanci spoje |
| **Zisk antény dBi (tx = rx)** | 14 | Stejná anténa na obou koncích |
| **Minimální signál dBm** | −130 | Minimální detekovatelný signál (článek: 8prvková Yagi + předzesilovač) |
| **Hustota stopy q = 10^ … elektronů/m** | 14 | Lineární hustota elektronů podhusté stopy |

Stanice, pásmo, výška stop, elevace laloku, ráhno a vzdálenost hot spotu se berou z [řad ovládacích prvků](Getting-Started-cs#1-tři-řady-ovládacích-prvků).

## Oddíly zprávy

| Oddíl | Obsah |
|---|---|
| **GEOMETRIE TRASY (kulová Země, R = 6372,7955 km)** | Stanice a DX s výškami; vzdálenost, azimut a zpětný azimut; střed trasy (lokátor a souřadnice); výška stop (*← modus naměřený radarem v Collmu*, pokud je převzata z radaru); elevace antény směrem ke středu trasy |
| **HOT A / HOT B (klasické hot spoty pro směrování antény)** | Pro každý: lokátor, azimut od vás a odklon od přímé trasy, azimut od DX, vzdálenost, elevace |
| **MEZE SPOLEČNÉ ZÓNY** | Dosah ve výšce stop při dané elevaci laloku; Mez A / Mez B s azimuty |
| Anténa | Ráhno v λ, zisk, vodorovný / svislý lalok; zda Hot A a Hot B leží uvnitř, nebo vně laloku |
| **ÚTLUM TRASY (podhustá stopa, McKinley 1961; bez zisků antén)** | Tabulka pro střed trasy (dopředně), Hot A a Hot B na 28, 50, 70, 144, 222 a 432 MHz |
| **ENERGETICKÁ BILANCE SPOJE NA … MHz (střed trasy)** | Výkon a EIRP, útlum trasy, signál na anténě, minimální detekovatelný, **rezerva**; stejná rezerva s průměrným útlumem podle OH5IY |
| **EXPERIMENTÁLNÍ PRAVIDLA MEZI PÁSMY (SM6FHZ, VUSHF 2025)** | Počet/intenzita a délka ve srovnání se 144 MHz; maximální ping podle IARU |

## Lokátor a trasa

Lokátor (4, 6 nebo 8 znaků; střed čtverce, systém IARU Maidenhead) [14]. Vzdálenost, azimut a střed trasy se počítají vzorci pro hlavní kružnici na kouli o poloměru **r = 6372,7955 km** (článek Cerrotta–Sartori) [15–16]. Výpočty závislé na čase se vztahují ke **středu trasy**, protože nejlepší doba se mezi oběma konci může lišit až o 1,5 hodiny (SM6FHZ).

## Elevace antény

**Zdroj:** vzorec z článku Cerrotta–Sartori (obrázek 7), kde x = d/r, d je pozemní vzdálenost k bodu odrazu, H výška stop a h výška stanice [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Ověření:** souhlasí s přesnou sférickou geometrií s odchylkou do 0,03°. Program používá arkustangens se dvěma argumenty, který za obzorem dává záporné hodnoty a vyhýbá se problému s periodicitou zmíněnému v článku. Záporná elevace směrem ke středu trasy znamená *trasa za geometrickým dosahem jednoho skoku*.

## Dosah k obzoru

Pozemní vzdálenost, ve které paprsek s elevací e dosáhne výšky H (geometrická inverze vzorce výše) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Ověření:** H = 89,5 km, e = 0° → **1062 km**. V příkladu z článku (JN44BB–IO53RT) klade výkres průsečíky obzoru asi 870 km od stanic, což odpovídá laloku zvednutému asi o 2° (865 km).

## Meze společné zóny

**Zdroj:** článek umisťuje průsečíky křivek tam, kde obzor každé stanice protíná vrstvu E: jsou to průsečíky dvou kružnic s úhlovým poloměrem ρ = d_H/r se středy v A a B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Je-li 1 − |p0|² < 0, je trasa delší než 2·d_H a stanice nevidí **žádnou společnou zónu vrstvy E**.

**Ověření:** jde o **nejvzdálenější okraje** oblohy viděné oběma stanicemi, **nikoli o body, na které mířit**. Na trase JN70CN–IN78UO (1710 km, azimut 308°) leží 1062 km od stanice, 37° vlevo a vpravo od přímé trasy, zatímco MSHV doporučuje 10°. Proto se nazývají *Mez A* / *Mez B* a na mapě se kreslí slabě.

## Hot A a Hot B

**Zdroj:** odrazy sporadických meteorů se soustřeďují ve dvou zónách („hot spotech“) na obou stranách středu trasy. J. Richardson (AMS) v tabulce citované DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004) udává odklon antény od přímého směru: **13° při 1000 km, 11° při 1250 km, 10° při 1500 a 2000 km**. AMS Bulletin č. 203, který převzal W8WN, udává 10° při 1500 a 1800 km.

**Volba:** Hot A a Hot B jsou body ve vzdálenosti s od středu trasy M, kolmo na trasu. Při zaškrtnutí *auto (AMS)* (výchozí) se s odvodí z odklonu podle Richardsonovy tabulky, lineárně interpolovaného (13° pod 1000 km, 10° nad 2000 km): s = (D/2)·tan(odklon). Bez zaškrtnutí se s zadává ručně, 30–400 km (MSHV používá 150 km); A vlevo při pohledu od vaší stanice k DX, B vpravo [21]. Odklon viděný ze stanice je přibližně [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Ověření:** s tabulkou AMS 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, tedy stejně jako dříve používaných 150 km a jako MSHV; na krátkých trasách tabulka přibližuje hot spoty ke středu trasy.

## Útlum trasy podhusté stopy

**Zdroj:** McKinleyho rovnice a doporučení ITU-R P.843 pro podhusté stopy (sin α = 1), bez zisků antén; q = lineární hustota elektronů, r_e = klasický poloměr elektronu = 2,818·10⁻¹⁵ m, R1, R2 vzdálenosti od stopy, φ polovina úhlu rozptylu, β úhel mezi stopou a rovinou trasy, a₁ faktor počátečního poloměru s r₀ v m a h v km (P.843, rov. 4 a 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Volba:** bilance a tabulka útlumů používají β = 90° (stopa křížící rovinu trasy, nejméně příznivý případ: opatrná hodnota) a bilance ukazuje i nejlepší případ, β = 0. r₀ se bere ve střední výšce ech pro danou frekvenci, h = 124 − 17 log f (P.843, rov. 15): 0,76 m v 95 km pro 50 MHz, 0,40 m v 87 km pro 144 MHz, 0,21 m v 79 km pro 432 MHz. Na 1000 km je a₁ 0,2 dB na 50 MHz, 0,6 dB na 144 MHz a 1,4 dB na 432 MHz (2,9 dB na 600 km); při pevných 102 km podle DJ5HG by to na 432 MHz bylo asi 70 dB, tedy žádné echo.

**Ověření:** s q = 10¹⁴ elektronů/m, stopami v 89,5 km a β = 0 na 144 MHz: **182–192 dB** mezi 600 a 2100 km (185 dB při 1000 km), uvnitř rozsahu **172–190 dB** vypočteného Johnem Worsnopem **G4BAO** v jeho disertační práci, jak uvádí GM8JBJ. S β = 90° roste útlum o 10 dB při 600 km, 13 dB při 1000 km a 16 dB při 2100 km; **průměr 200 dB** podle OH5IY leží mezi oběma případy. 182 dB v tabulce GM8JBJ nejsou potvrzením: tabulka neuvádí frekvenci, jejích 86,4 dB na úsek je útlum volného prostoru na 500 km při 1 MHz (chybí člen 20 log f: 129,6 dB na 144 MHz) a její položky dávají součet 163,8 dB, ne 182; stránka neuvádí ani „minimum“, ani „144 MHz“.

## Energetická bilance spoje

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Zisky se zadávají a používají v dBi: McKinleyho útlum se vztahuje k izotropním anténám, takže se neodečítá korekce 2,15 dB pro dipól (EIRP = výkon + zisk). Zpráva uvádí také rezervu s **průměrným útlumem trasy podle OH5IY** (200 dB na 144 MHz, přepočteno s λ³ na zvolené pásmo). Referenční hodnota z článku: potřeba je asi **70 dBm EIRP** (−130 dBm + 200 dB, např. asi 400 W do 14 dBi).

## Zisk a lalok antény

**Zisk – zdroj:** křivka Güntera Hocha **DL6WU** pro dlouhé Yagi v závislosti na délce ráhna L, kterou uvádí W8IO (platí asi od 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Ověření proti modelům NEC L.B. Cebika W4RNL na 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Prvky | Ráhno (λ) | W4RNL NEC (dBi) | Vzorec (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Rozdíl nikdy nepřesáhne **0,1 dB**: zisk závisí více na délce ráhna než na konstrukci (Yagi VK3AUU mají při stejném počtu prvků kratší ráhno). Yagi Calculator od VK5DJ dává také odhady pro varianty VK3AUU, WA2PHW a DJ9BV, jejichž vzorce nejsou publikovány.

**Lalok – zdroj:** Krausovo pravidlo s kruhovým lalokem θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Ověření:** modely NEC od W4RNL pro Yagi DL6WU dávají **vodorovný lalok o 5–10 % užší** než Kraus: 33,8° / 26,4° / 22,6° pro 12, 19 a 26 prvků, oproti 37,3° / 28,0° / 23,9°. Jednoduché vzorce ignorují přední postranní laloky (W4RNL, *Long-Boom Yagi Rules of Thumb*). U dlouhých ráhen je svislý lalok o něco širší než vodorovný (14 λ: 18,4° / 18,8°).

**Volba** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Příklad: Yagi 14 λ na 432 MHz → 20,3 dBi, lalok 18,1° vodorovně a 19,5° svisle; modely W4RNL dávají 20,4 dBi a 18,4° / 18,8°. Jde o přibližná pravidla odvozená z několika antén DL6WU.

Anténa se vždy považuje za nasměrovanou na DX. Hot spot je **uvnitř laloku**, pokud |Az(Hot) − Az(anténa)| ≤ θ_vodorovný/2: pak se na [Nebeské klenbě](Sky-View-cs) kreslí šedě a objeví se varování. Ve výpočtu účinnosti jsou antény izotropní; skutečný lalok se používá jen pro toto ověření.

## Experimentální pravidla mezi pásmy

Ve srovnání se 144 MHz: počet/intenzita × (144/f)³ (v dB), délka × (144/f)² (SM6FHZ, VUSHF 2025). Maximální délka pingu podle IARU Region 1: 1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz (VHF Handbook, citováno v článku). Viz také [Experimentální předpovědi](Experimental-Forecasts-cs).
