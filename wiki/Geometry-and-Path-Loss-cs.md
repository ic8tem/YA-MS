[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · **Čeština** · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometrie a útlum trasy

*Karta: Výpočet předpovědi › Geometrie a útlum trasy.*

[![Geometrie a útlum trasy](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Textová zpráva o trase (lze ji označit, takže ji můžete zkopírovat) a vpravo graf **Elevace antény v závislosti na vzdálenosti od bodu rozptylu**. Čísla v hranatých závorkách odkazují na rovnice výpočetní příručky (`doc/YA-MS_manuale_calcoli.docx`).

## Vstupy této karty

| Pole | Výchozí | Použití |
|---|---|---|
| **Výkon W** | 400 | Výkon vysílače pro energetickou bilanci spoje |
| **Zisk antény dBi (tx = rx)** | 14 | Stejná anténa na obou koncích |
| **Minimální signál dBm** | −130 | Minimální detekovatelný signál (článek: 8prvková Yagi + předzesilovač) |
| **Hustota stopy q = 10^ … elektronů/m** | 14 | Lineární hustota elektronů podhusté stopy |

Stanice, pásmo, výška stopy, elevace laloku, ráhno a vzdálenost hot spotů se berou z [řad ovládacích prvků](Getting-Started-cs#1-tři-řady-ovládacích-prvků).

## Oddíly zprávy

| Oddíl | Obsah |
|---|---|
| **GEOMETRIE TRASY (kulová Země, R = 6372,7955 km)** | Stanice a DX s výškami; vzdálenost, azimut a zpětný azimut; střed trasy (lokátor a souřadnice); výška stopy (*← modus změřený radarem Collm*, pokud je převzata z radaru); elevace antény směrem ke středu trasy |
| **HOT A / HOT B (klasické hot spoty, pro směrování antény)** | Pro každý: lokátor, azimut od vás a odsazení od přímé trasy, azimut od DX, vzdálenost, elevace |
| **MEZE SPOLEČNÉ ZÓNY** | Dosah ve výšce stopy s danou elevací laloku; Mez A / Mez B s azimuty |
| Anténa | Ráhno v λ, zisk, vodorovný / svislý lalok; zda Hot A a Hot B leží uvnitř, nebo mimo lalok |
| **ÚTLUM TRASY (podhustá stopa, McKinley 1961; bez zisků antén)** | Tabulka pro střed trasy (dopředný), Hot A a Hot B na 28, 50, 70, 144, 222 a 432 MHz |
| **ENERGETICKÁ BILANCE SPOJE NA … MHz (střed trasy)** | Výkon a EIRP, útlum trasy, signál na anténě, minimální detekovatelný signál, **rezerva**; tatáž rezerva s průměrným útlumem podle OH5IY |
| **EXPERIMENTÁLNÍ PRAVIDLA MEZI PÁSMY (SM6FHZ, VUSHF 2025)** | Počet/intenzita a trvání ve srovnání se 144 MHz; maximální ping podle IARU |

## Lokátor a trasa

Lokátor (4, 6 nebo 8 znaků; střed čtverce, systém IARU Maidenhead) [14]. Vzdálenost, azimut a střed trasy podle vzorců pro hlavní kružnici na kouli o poloměru **r = 6372,7955 km** (článek Cerrotta–Sartori) [15–16]. Výpočty závislé na čase se vztahují ke **středu trasy**, protože nejlepší čas se mezi oběma konci může lišit až o 1,5 hodiny (SM6FHZ).

## Elevace antény

**Zdroj:** vzorec z článku Cerrotta–Sartori (obrázek 7), kde x = d/r, d je vzdálenost po povrchu k bodu odrazu, H výška stopy a h výška stanice [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Ověření:** s přesnou sférickou geometrií se shoduje do 0,03°. Program používá arkustangens se dvěma argumenty, který za obzorem dává záporné hodnoty a vyhýbá se problému s periodicitou zmíněnému v článku. Záporná elevace směrem ke středu trasy znamená *trasa mimo geometrický dosah jednoho skoku*.

## Dosah k obzoru

Vzdálenost po povrchu, ve které paprsek s elevací e dosáhne výšky H (geometrická inverze výše uvedeného vzorce) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Ověření:** H = 89,5 km, e = 0° → **1062 km**. V příkladu z článku (JN44BB–IO53RT) klade obrázek průsečíky s obzorem asi 870 km od stanic, což odpovídá laloku zvednutému asi o 2° (865 km).

## Meze společné zóny

**Zdroj:** článek určuje průsečíky křivek, kde obzor každé stanice protíná vrstvu E: průsečíky dvou kružnic o úhlovém poloměru ρ = d_H/r se středy v A a B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Pokud 1 − |p0|² < 0, je trasa delší než 2·d_H a stanice nevidí **žádnou společnou zónu vrstvy E**.

**Ověření:** jsou to **nejvzdálenější okraje** oblohy viděné oběma stanicemi, **nikoli body, na které se má mířit**. Na trase JN70CN–IN78UO (1710 km, azimut 308°) leží 1062 km od stanice, 37° vlevo a vpravo od přímé trasy, zatímco MSHV navrhuje 10°. Proto se nazývají *Mez A* / *Mez B* a na mapě jsou vykresleny slabě.

## Hot A a Hot B

**Zdroj:** odrazy se soustřeďují do dvou zón („hot spotů“) asi **50–150 km na obě strany od středu trasy**. To je základ tabulky odsazení antény z AMS Bulletin No. 203, kterou převzal W8WN (odsazení 10° pro trasy 1500 a 1800 km); MSHV od LZ2HV používá stejné kritérium.

**Volba:** Hot A a Hot B jsou body ve vzdálenosti s od středu trasy M, kolmo na trasu (s = 150 km, nastavitelné 30–400 km); A vlevo při pohledu od vaší stanice k DX, B vpravo [21]. Odsazení viděné ze stanice je přibližně [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Ověření:** JN70CN–IN78UO, D = 1710 km: 6,7° při s = 100 km, **10,0° při s = 150 km** (stejně jako MSHV a AMS/W8WN), 13,2° při s = 200 km.

## Útlum trasy u podhusté stopy

**Zdroj:** McKinleyho rovnice pro podhusté stopy (β = 0, sin α = 1), bez zisků antén; q = lineární hustota elektronů, r_e = klasický poloměr elektronu = 2,818·10⁻¹⁵ m, R1, R2 vzdálenosti od stopy, φ polovina úhlu rozptylu [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Ověření:** s q = 10¹⁴ elektronů/m na 144 MHz: **181–192 dB** mezi 600 a 2200 km, v souladu s odkazy článku na 144 MHz: **minimum 182 dB** (GM8JBJ, podle Kaiser & Closs 1952) a **průměr 200 dB** (OH5IY).

## Energetická bilance spoje

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Zisky se zadávají v dBi a používají v dBd (dBi − 2,15). Zpráva uvádí i rezervu s **průměrným útlumem trasy podle OH5IY** (200 dB na 144 MHz, přepočteno pomocí λ³ na zvolené pásmo). Odkaz z článku: je potřeba asi **70 dBm EIRP** (−130 dBm + 200 dB, např. asi 400 W do 14 dBi).

## Zisk a lalok antény

**Zisk – zdroj:** křivka Güntera Hocha **DL6WU** pro dlouhé antény Yagi v závislosti na délce ráhna L, podle W8IO (platí přibližně od 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Ověření proti modelům NEC od L. B. Cebika W4RNL na 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Prvky | Ráhno (λ) | W4RNL NEC (dBi) | Vzorec (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Rozdíl nikdy nepřekročí **0,1 dB**: zisk závisí víc na délce ráhna než na konstrukci (antény Yagi VK3AUU mají při stejném počtu prvků kratší ráhno). Yagi Calculator od VK5DJ dává odhady i pro varianty VK3AUU, WA2PHW a DJ9BV, jejichž vzorce nejsou zveřejněny.

**Lalok – zdroj:** Krausovo pravidlo s kruhovým lalokem θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Ověření:** modely NEC antén Yagi DL6WU od W4RNL dávají **vodorovný lalok o 5–10 % užší** než Kraus: 33,8° / 26,4° / 22,6° pro 12, 19 a 26 prvků oproti 37,3° / 28,0° / 23,9°. Jednoduché vzorce ignorují přední postranní laloky (W4RNL, *Long-Boom Yagi Rules of Thumb*). U dlouhých ráhen je svislý lalok o něco širší než vodorovný (14 λ: 18,4° / 18,8°).

**Volba** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Příklad: Yagi 14 λ na 432 MHz → 20,3 dBi, lalok 18,1° vodorovně a 19,5° svisle; modely W4RNL dávají 20,4 dBi a 18,4° / 18,8°. Jde o přibližná pravidla odvozená z několika antén DL6WU.

Anténa se vždy považuje za nasměrovanou na DX. Hot spot leží **uvnitř laloku**, pokud |Az(Hot) − Az(antény)| ≤ θ_vodorovný/2: pak je v [Nebeské klenbě](Sky-View-cs) vykreslen šedě a objeví se upozornění. Ve výpočtu účinnosti jsou antény izotropní; skutečný lalok se používá jen pro tuto kontrolu.

## Experimentální pravidla mezi pásmy

Ve srovnání se 144 MHz: počet/intenzita × (144/f)³ (v dB), trvání × (144/f)² (SM6FHZ, VUSHF 2025). Maximální trvání pingu podle IARU Region 1: 1000 ms na 50 MHz, 500 ms na 70 MHz, 100 ms na 144 MHz, 13 ms na 432 MHz (VHF Handbook, citováno v článku). Viz také [Experimentální předpovědi](Experimental-Forecasts-cs).
