[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · **Tagalog** · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

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

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Pagsusuri:** tumutugma ito sa eksaktong spherical na heometriya sa loob ng 0.03°. Ginagamit ng programa ang two-argument na arctangent, na nagbibigay ng negatibong halaga lampas sa horizon at umiiwas sa problema ng periodicity na binanggit sa artikulo. Ang negatibong elebasyon patungo sa gitnang punto ay nangangahulugang *landas na lampas sa heometrikong abot ng iisang hop*.

## Abot ng horizon

Distansiya sa lupa kung saan naaabot ng sinag na may elebasyong e ang taas na H (heometrikong kabaligtaran ng pormula sa itaas) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Pagsusuri:** H = 89.5 km, e = 0° → **1062 km**. Sa halimbawa ng artikulo (JN44BB–IO53RT), inilalagay ng drowing ang mga tawiran ng horizon nang mga 870 km mula sa mga istasyon, na tumutugma sa lobe na itinaas nang mga 2° (865 km).

## Mga hangganan ng karaniwang sona

**Sanggunian:** tinutukoy ng artikulo ang mga pagtatagpo ng mga kurba kung saan sinasalubong ng horizon ng bawat istasyon ang E layer: ang mga pagtatagpo ng dalawang bilog na may angular na radius na ρ = d_H/r na nakasentro sa A at B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Kung 1 − |p0|² < 0, mas mahaba ang landas kaysa 2·d_H at **walang karaniwang sona ng E layer** na nakikita ang mga istasyon.

**Pagsusuri:** ito ang **pinakamalayong gilid** ng langit na nakikita ng dalawang istasyon, **hindi mga puntong tututukan**. Sa JN70CN–IN78UO (1710 km, azimuth 308°), bumabagsak ang mga ito 1062 km mula sa istasyon, 37° sa kaliwa at kanan ng tuwirang landas, samantalang 10° ang iminumungkahi ng MSHV. Kaya tinatawag ang mga ito na *Hangganan A* / *Hangganan B* at malabong iginuguhit sa mapa.

## Hot A at Hot B

**Sanggunian:** nakatipon ang mga repleksiyon ng sporadic na meteor sa dalawang sona ("hot spot") sa magkabilang panig ng gitnang punto. Ibinibigay ni J. Richardson (AMS), sa talahanayang sinipi ni DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), ang offset ng antenna mula sa direktang direksiyon: **13° sa 1000 km, 11° sa 1250 km, 10° sa 1500 at 2000 km**. Ang AMS Bulletin No. 203, na ginamit ni W8WN, ay nagbibigay ng 10° sa 1500 at 1800 km.

**Pagpili:** ang Hot A at Hot B ay ang mga punto sa distansiyang s mula sa gitnang punto M, patayo sa landas. Kapag may tsek ang *auto (AMS)* (default), ang s ay mula sa offset ng talahanayan ni Richardson, linear na in-interpolate (13° sa ibaba ng 1000 km, 10° sa itaas ng 2000 km): s = (D/2)·tan(offset). Kapag walang tsek, mano-manong inilalagay ang s, 30–400 km (150 km ang ginagamit ng MSHV); ang A ay nasa kaliwa kung titingin mula sa iyong istasyon patungo sa DX, ang B ay nasa kanan [21]. Ang offset na nakikita mula sa istasyon ay humigit-kumulang [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Pagsusuri:** gamit ang talahanayan ng AMS, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, kapareho ng 150 km na ginamit dati at ng MSHV; sa maiikling landas, inilalapit ng talahanayan ang mga hot spot sa gitnang punto.

## Underdense na path loss

**Sanggunian:** ekwasyon ni McKinley at Rekomendasyong ITU-R P.843 para sa mga underdense na bakas (sin α = 1), hindi kasama ang gain ng antenna; q = linear na densidad ng electron, r_e = klasikong radius ng electron = 2.818·10⁻¹⁵ m, R1, R2 ang mga distansiya mula sa bakas, φ kalahati ng scattering angle, β anggulo sa pagitan ng bakas at ng plane ng landas, a₁ factor ng paunang radius na ang r₀ ay nasa m at ang h ay nasa km (P.843, eq. 4 at 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Pagpili:** gumagamit ang link budget at ang talahanayan ng loss ng β = 90° (bakas na tumatawid sa plane ng landas, ang pinakadi-paborableng kaso: maingat na halaga) at ipinapakita rin ng budget ang pinakamahusay na kaso, β = 0. Kinukuha ang r₀ sa karaniwang taas ng echo para sa frequency, h = 124 − 17 log f (P.843, eq. 15): 0.76 m sa 95 km para sa 50 MHz, 0.40 m sa 87 km para sa 144 MHz, 0.21 m sa 79 km para sa 432 MHz. Sa 1000 km ang a₁ ay 0.2 dB sa 50 MHz, 0.6 dB sa 144 MHz at 1.4 dB sa 432 MHz (2.9 dB sa 600 km); sa nakapirming 102 km ni DJ5HG, mga 70 dB ito sa 432 MHz, ibig sabihin ay walang echo talaga.

**Pagsusuri:** kapag q = 10¹⁴ electron/m, mga bakas sa 89.5 km at β = 0, sa 144 MHz: **182–192 dB** sa pagitan ng 600 at 2100 km (185 dB sa 1000 km), nasa loob ng saklaw na **172–190 dB** na kinalkula ni John Worsnop **G4BAO** sa kaniyang PhD thesis, ayon sa ulat ni GM8JBJ. Kapag β = 90°, lumalaki ang loss nang 10 dB sa 600 km, 13 dB sa 1000 km at 16 dB sa 2100 km; ang **200 dB na average** ni OH5IY ay nasa pagitan ng dalawang kaso. Ang 182 dB sa talahanayan ni GM8JBJ ay hindi kumpirmasyon: walang ibinibigay na frequency ang talahanayan, ang 86.4 dB nito bawat bahagi ay ang free-space loss sa 500 km sa 1 MHz (nawawala ang terminong 20 log f: 129.6 dB sa 144 MHz) at ang kabuuan ng mga item nito ay 163.8 dB, hindi 182; hindi sinasabi ng pahina ang "minimum" o ang "144 MHz".

## Link budget

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Inilalagay at ginagamit ang mga gain sa dBi: ang loss ni McKinley ay tumutukoy sa mga isotropic na antenna, kaya walang ibinabawas na 2.15 dB na dipole correction (EIRP = power + gain). Ibinibigay rin ng ulat ang margin gamit ang **karaniwang path loss ni OH5IY** (200 dB sa 144 MHz, iniskala sa λ³ sa napiling banda). Sanggunian ng artikulo: mga **70 dBm na EIRP** ang kailangan (−130 dBm + 200 dB, hal. mga 400 W sa 14 dBi).

## Gain at lobe ng antenna

**Gain – sanggunian:** kurba ni Günter Hoch **DL6WU** para sa mahahabang Yagi bilang function ng haba ng boom L, ayon sa ulat ni W8IO (balido mula mga 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Pagsusuri laban sa mga NEC model ni L.B. Cebik W4RNL sa 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Mga element | Boom (λ) | W4RNL NEC (dBi) | Pormula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

Hindi kailanman lumalampas sa **0.1 dB** ang pagkakaiba: mas nakadepende ang gain sa haba ng boom kaysa sa disenyo (mas maikli ang boom ng mga Yagi ng VK3AUU para sa parehong bilang ng element). Nagbibigay rin ang Yagi Calculator ni VK5DJ ng mga tantiya para sa mga bersyong VK3AUU, WA2PHW at DJ9BV, na hindi nailathala ang mga pormula.

**Lobe – sanggunian:** tuntunin ni Kraus, na may pabilog na lobe θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Pagsusuri:** ang mga NEC model ni W4RNL ng mga Yagi ng DL6WU ay nagbibigay ng **pahalang na lobe na 5–10 % na mas makitid** kaysa kay Kraus: 33.8° / 26.4° / 22.6° para sa 12, 19 at 26 na element, laban sa 37.3° / 28.0° / 23.9°. Hindi isinasaalang-alang ng mga simpleng pormula ang mga forward side lobe (W4RNL, *Long-Boom Yagi Rules of Thumb*). Sa mahahabang boom, bahagyang mas malapad ang patayong lobe kaysa sa pahalang (14 λ: 18.4° / 18.8°).

**Pagpili** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Halimbawa: Yagi na 14 λ sa 432 MHz → 20.3 dBi, lobe na 18.1° pahalang at 19.5° patayo; ang mga model ni W4RNL ay nagbibigay ng 20.4 dBi at 18.4° / 18.8°. Mga tinatayang tuntunin ito na hinango mula sa ilang antenna ng DL6WU.

Itinuturing na laging nakatutok sa DX ang antena. Ang isang hot spot ay **nasa loob ng lobe** kung |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: iginuguhit ito nang kulay abo sa [Kalangitan](Sky-View-tl) at may lumalabas na babala. Pumapasok din ang patayong lobe sa pagkalkula ng kahusayan: kapag nakabukas ang kahong *pattern ng antena*, tinitimbang ang mga punto ng repleksyon ayon sa patayong gain ng dalawang antena (lapad θ_vertical, rurok sa elevation ng lobe, salik ng lupa hanggang zero sa abot-tanaw).

## Mga eksperimental na tuntunin sa pagitan ng mga banda

Kumpara sa 144 MHz: bilang/lakas × (144/f)³ (sa dB), tagal × (144/f)² (SM6FHZ, VUSHF 2025). Pinakamahabang tagal ng ping ayon sa IARU Region 1: 1000 ms sa 50 MHz, 500 ms sa 70 MHz, 100 ms sa 144 MHz, 13 ms sa 432 MHz (VHF Handbook, binanggit sa artikulo). Tingnan din ang [Eksperimental na pagtataya](Experimental-Forecasts-tl).
