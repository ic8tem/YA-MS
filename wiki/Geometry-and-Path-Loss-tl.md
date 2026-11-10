[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · **Tagalog** · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Heometriya at path loss

*Tab: Kalkulasyon ng pagtataya › Heometriya at path loss.*

[![Heometriya at path loss](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Isang tekstong ulat ng landas (napipili, kaya maaari mo itong kopyahin) at, sa kanan, ang graph na **Elebasyon ng antenna ayon sa distansiya mula sa scatter point**. Ang mga numero sa loob ng bracket ay tumutukoy sa mga ekwasyon ng manwal ng kalkulasyon (`doc/YA-MS_manuale_calcoli.docx`).

## Mga input ng tab na ito

| Field | Default | Gamit |
|---|---|---|
| **Power W** | 400 | Power ng transmitter para sa link budget |
| **Gain ng antenna dBi (tx = rx)** | 14 | Parehong antenna sa magkabilang dulo |
| **Pinakamahinang signal dBm** | −130 | Pinakamahinang signal na matatanggap (artikulo: 8-element na Yagi + preamp) |
| **Densidad ng bakas q = 10^ … electron/m** | 14 | Linear na densidad ng electron ng underdense na bakas |

Ang mga istasyon, banda, taas ng bakas, elebasyon ng lobe, boom at distansiya ng hot spot ay kinukuha mula sa [mga hanay ng kontrol](Getting-Started-tl#1-ang-tatlong-hanay-ng-mga-kontrol).

## Mga seksiyon ng ulat

| Seksiyon | Nilalaman |
|---|---|
| **HEOMETRIYA NG LANDAS (pabilog na Daigdig, R = 6372.7955 km)** | Istasyon at DX kasama ang taas; distansiya, azimuth at pabalik na azimuth; gitnang punto (locator at coordinates); taas ng bakas (*<- moda na sinukat ng radar ng Collm* kapag kinuha mula sa radar); elebasyon ng antenna patungo sa gitnang punto |
| **HOT A / HOT B (klasikong hot spot, para sa pagtutok ng antenna)** | Para sa bawat isa: locator, azimuth mula sa iyo at offset mula sa tuwirang landas, azimuth mula sa DX, distansiya, elebasyon |
| **MGA HANGGANAN NG KARANIWANG SONA** | Abot sa taas ng bakas na may elebasyon ng lobe; Hangganan A / Hangganan B kasama ang mga azimuth |
| Antenna | Boom sa λ, gain, pahalang / patayong lobe; kung nasa loob o labas ng lobe ang Hot A at Hot B |
| **PATH LOSS NG LANDAS (underdense na bakas, McKinley 1961; hindi kasama ang gain ng antenna)** | Talahanayan para sa gitnang punto (forward), Hot A at Hot B sa 28, 50, 70, 144, 222 at 432 MHz |
| **LINK BUDGET SA … MHz (gitnang punto)** | Power at EIRP, path loss, signal sa antenna, pinakamababang matatanggap, **margin**; ang parehong margin gamit ang karaniwang loss ni OH5IY |
| **MGA EKSPERIMENTAL NA PATAKARAN SA PAGITAN NG MGA BANDA (SM6FHZ, VUSHF 2025)** | Bilang/lakas at tagal kumpara sa 144 MHz; pinakamahabang ping ng IARU |

## Locator at landas

Locator (4, 6 o 8 character; gitna ng grid square, sistemang Maidenhead ng IARU) [14]. Distansiya, azimuth at gitnang punto gamit ang mga pormulang great-circle sa isang globo na may radius na **r = 6372.7955 km** (artikulong Cerrotta–Sartori) [15–16]. Ang mga kalkulasyong nakadepende sa oras ay tumutukoy sa **gitnang punto**, dahil maaaring magkaiba nang hanggang 1.5 oras ang pinakamahusay na oras sa dalawang dulo (SM6FHZ).

## Elebasyon ng antenna

**Sanggunian:** pormula ng artikulong Cerrotta–Sartori (Larawan 7), kung saan x = d/r, d ang distansiya sa lupa patungo sa punto ng repleksiyon, H ang taas ng bakas at h ang taas ng istasyon [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Pagsusuri:** tumutugma ito sa eksaktong spherical na heometriya sa loob ng 0.03°. Ginagamit ng programa ang two-argument na arctangent, na nagbibigay ng negatibong halaga lampas sa horizon at umiiwas sa problema ng periodicity na binanggit sa artikulo. Ang negatibong elebasyon patungo sa gitnang punto ay nangangahulugang *landas na lampas sa heometrikong abot ng iisang hop*.

## Abot ng horizon

Distansiya sa lupa kung saan naaabot ng sinag na may elebasyong e ang taas na H (heometrikong kabaligtaran ng pormula sa itaas) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Pagsusuri:** H = 89.5 km, e = 0° → **1062 km**. Sa halimbawa ng artikulo (JN44BB–IO53RT), inilalagay ng drowing ang mga tawiran ng horizon nang mga 870 km mula sa mga istasyon, na tumutugma sa lobe na itinaas nang mga 2° (865 km).

## Mga hangganan ng karaniwang sona

**Sanggunian:** tinutukoy ng artikulo ang mga pagtatagpo ng mga kurba kung saan sinasalubong ng horizon ng bawat istasyon ang E layer: ang mga pagtatagpo ng dalawang bilog na may angular na radius na ρ = d_H/r na nakasentro sa A at B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Kung 1 − |p0|² < 0, mas mahaba ang landas kaysa 2·d_H at **walang karaniwang sona ng E layer** na nakikita ang mga istasyon.

**Pagsusuri:** ito ang **pinakamalayong gilid** ng langit na nakikita ng dalawang istasyon, **hindi mga puntong tututukan**. Sa JN70CN–IN78UO (1710 km, azimuth 308°), bumabagsak ang mga ito 1062 km mula sa istasyon, 37° sa kaliwa at kanan ng tuwirang landas, samantalang 10° ang iminumungkahi ng MSHV. Kaya tinatawag ang mga ito na *Hangganan A* / *Hangganan B* at malabong iginuguhit sa mapa.

## Hot A at Hot B

**Sanggunian:** nakatipon ang mga repleksiyon sa dalawang sona ("hot spot") na mga **50–150 km sa magkabilang panig ng gitnang punto**. Ito ang batayan ng talahanayan ng offset ng antenna ng AMS Bulletin No. 203, na ginamit ni W8WN (10° na offset para sa mga landas na 1500 at 1800 km); ginagamit din ng MSHV ni LZ2HV ang parehong pamantayan.

**Pagpili:** ang Hot A at Hot B ay ang mga punto sa distansiyang s mula sa gitnang punto M, patayo sa landas (s = 150 km, naaayos sa 30–400 km); ang A ay nasa kaliwa kung titingin mula sa iyong istasyon patungo sa DX, ang B ay nasa kanan [21]. Ang offset na nakikita mula sa istasyon ay humigit-kumulang [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Pagsusuri:** JN70CN–IN78UO, D = 1710 km: 6.7° kapag s = 100 km, **10.0° kapag s = 150 km** (kapareho ng MSHV at AMS/W8WN), 13.2° kapag s = 200 km.

## Underdense na path loss

**Sanggunian:** ekwasyon ni McKinley para sa mga underdense na bakas (β = 0, sin α = 1), hindi kasama ang gain ng antenna; q = linear na densidad ng electron, r_e = klasikong radius ng electron = 2.818·10⁻¹⁵ m, R1, R2 ang mga distansiya mula sa bakas, φ kalahati ng scattering angle [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Pagsusuri:** kapag q = 10¹⁴ electron/m sa 144 MHz: **181–192 dB** sa pagitan ng 600 at 2200 km, kaayon ng mga sanggunian ng artikulo sa 144 MHz: **182 dB pinakamababa** (GM8JBJ, mula kina Kaiser & Closs 1952) at **200 dB karaniwan** (OH5IY).

## Link budget

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Inilalagay ang mga gain sa dBi at ginagamit sa dBd (dBi − 2.15). Ibinibigay rin ng ulat ang margin gamit ang **karaniwang path loss ni OH5IY** (200 dB sa 144 MHz, iniskala sa λ³ sa napiling banda). Sanggunian ng artikulo: mga **70 dBm na EIRP** ang kailangan (−130 dBm + 200 dB, hal. mga 400 W sa 14 dBi).

## Gain at lobe ng antenna

**Gain – sanggunian:** kurba ni Günter Hoch **DL6WU** para sa mahahabang Yagi bilang function ng haba ng boom L, ayon sa ulat ni W8IO (balido mula mga 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Pagsusuri laban sa mga NEC model ni L.B. Cebik W4RNL sa 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Mga element | Boom (λ) | W4RNL NEC (dBi) | Pormula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

Hindi kailanman lumalampas sa **0.1 dB** ang pagkakaiba: mas nakadepende ang gain sa haba ng boom kaysa sa disenyo (mas maikli ang boom ng mga Yagi ng VK3AUU para sa parehong bilang ng element). Nagbibigay rin ang Yagi Calculator ni VK5DJ ng mga tantiya para sa mga bersyong VK3AUU, WA2PHW at DJ9BV, na hindi nailathala ang mga pormula.

**Lobe – sanggunian:** tuntunin ni Kraus, na may pabilog na lobe θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Pagsusuri:** ang mga NEC model ni W4RNL ng mga Yagi ng DL6WU ay nagbibigay ng **pahalang na lobe na 5–10 % na mas makitid** kaysa kay Kraus: 33.8° / 26.4° / 22.6° para sa 12, 19 at 26 na element, laban sa 37.3° / 28.0° / 23.9°. Hindi isinasaalang-alang ng mga simpleng pormula ang mga forward side lobe (W4RNL, *Long-Boom Yagi Rules of Thumb*). Sa mahahabang boom, bahagyang mas malapad ang patayong lobe kaysa sa pahalang (14 λ: 18.4° / 18.8°).

**Pagpili** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Halimbawa: Yagi na 14 λ sa 432 MHz → 20.3 dBi, lobe na 18.1° pahalang at 19.5° patayo; ang mga model ni W4RNL ay nagbibigay ng 20.4 dBi at 18.4° / 18.8°. Mga tinatayang tuntunin ito na hinango mula sa ilang antenna ng DL6WU.

Laging itinuturing na nakatutok sa DX ang antenna. Ang hot spot ay **nasa loob ng lobe** kung |Az(Hot) − Az(antenna)| ≤ θ_horizontal/2: kulay abo itong iginuguhit sa [Kalangitan](Sky-View-tl) at lumalabas ang isang babala. Sa kalkulasyon ng episyensya, isotropic ang mga antenna; para lamang sa pagsusuring ito ginagamit ang totoong lobe.

## Mga eksperimental na tuntunin sa pagitan ng mga banda

Kumpara sa 144 MHz: bilang/lakas × (144/f)³ (sa dB), tagal × (144/f)² (SM6FHZ, VUSHF 2025). Pinakamahabang tagal ng ping ayon sa IARU Region 1: 1000 ms sa 50 MHz, 500 ms sa 70 MHz, 100 ms sa 144 MHz, 13 ms sa 432 MHz (VHF Handbook, binanggit sa artikulo). Tingnan din ang [Eksperimental na pagtataya](Experimental-Forecasts-tl).
