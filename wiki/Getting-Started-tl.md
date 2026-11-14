[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · **Tagalog** · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Pagsisimula

Sa unang pagsisimula, nagpapakita ang YA-MS ng halimbawang landas (JN70CN → JO62QM sa 144 MHz). Sapat na ang limang minuto para i-set up ito para sa iyong istasyon.

## 1. Ang tatlong hanay ng mga kontrol

Sa itaas ng mga tab ay may tatlong hanay ng mga kontrol, balido para sa lahat ng tab. Itinitiklop at ibinubuka ang mga ito ng button na **Mga kontrol** sa kanang itaas (kapaki-pakinabang kapag malaki ang font); natatandaan ang pinili.

**Hanay 1 – mga istasyon at banda**

| Kontrol | Ano ang ginagawa |
|---|---|
| **Ang aking locator** / **taas m** | Ang iyong Maidenhead locator (4, 6 o 8 character; ginagamit ang gitna ng grid square) at ang taas ng istasyon mula sa antas ng dagat. |
| **DX station** / **taas m** | Sa tabi ng mapa, sa kanan, ang kahon ng kausap: i-type ang callsign at pindutin ang Enter, kinukuha ang locator mula sa database ng CALL3 (tulad ng sa YAEC at LIVETROPOVHF); sa ilalim ang locator at ang taas. Maaari ring i-type ang callsign sa kahon ng locator. |
| **Banda MHz** | 28, 50, 70, 144, 222 o 432 MHz: ginagamit para sa gain at lobe ng antenna, sa tantiya ng flux at sa link budget. |
| **Kalkulahin** | Muling kinakalkula ang landas (pag-sample ng E layer: ilang segundo). |
| **Antenna az** | Sa itaas ng kahon ng kausap, sa tabi ng mapa: azimuth ng iyong antena, laging **patungo sa DX** (azimuth ng daan). Sa ibaba, sa parehong kolum, ang alamat ng mapa. |

**Hanay 2 – E layer at antenna**

| Kontrol | Ano ang ginagawa |
|---|---|
| **Taas ng bakas km** + **mula sa radar** | Taas ng mga bakas ng meteor (default 90 km). Kapag may tsek ang *mula sa radar*, ginagamit ang pinakamadalas na taas (moda) na sinukat ng radar ng Collm; tingnan ang [Flux ng radar](Radar-Flux-tl). |
| **Elebasyon ng lobe °** | Elevation ng rurok ng patayong lobe ng iyong antena: ang direksyonal na antenang nakapirmi sa 0° ay may lobe pa rin na ilang digri sa itaas ng abot-tanaw dahil sa repleksyon sa lupa (karaniwang 3-8°). Kapag nakabukas ang kahong **pattern ng antena** (default), tinitimbang ang mga punto ng E layer ayon sa patayong pattern ng dalawang antena; kapag nakasara, ang mga puntong nakikita ng dalawang istasyon sa itaas ng elevation na ito lang ang ginagamit. |
| **Yagi antenna: boom m** | Haba ng boom ng iyong Yagi. Ipinapakita ng programa ang haba sa λ, ang gain (kurba ng DL6WU) at ang −3 dB na lobe, pahalang at patayo; tingnan ang [Heometriya at path loss](Geometry-and-Path-Loss-tl#gain-at-lobe-ng-antenna). Sa ilalim ng 2 λ, magaspang ang tantiya. |
| **Hot spot mula sa gitnang punto km** + **auto (AMS)** | Distansiya ng Hot A at Hot B mula sa gitnang punto. Kapag may tsek ang *auto (AMS)* (default), sinusunod nito ang talahanayan ng offset ng antenna ni J. Richardson (AMS) na sinipi ni DJ5HG: 13° sa 1000 km, 11° sa 1250 km, 10° sa 1500 at 2000 km (mga 115, 121, 132 at 176 km mula sa gitnang punto). Alisin ang tsek para mano-manong ilagay ang 30–400 km (150 km ang ginagamit ng MSHV). |

**Hanay 3 – oras**

| Kontrol | Ano ang ginagawa |
|---|---|
| **Oras** | Orasang UTC. |
| **Petsa ng kalkulasyon (UTC)** | Ang araw ng kalkulasyon para sa [Kalkulasyon ng pagtataya](Sky-View-tl) at [Radar GRAVES](GRAVES-Radar-tl) (ngayong araw bilang default), sa kasalukuyang oras ng araw. Gayundin: ang araw na ipinapakita sa [Kalkulasyon ng episyensya](Efficiency-Calculation-tl) at sa timeline ng GRAVES. |
| **Mga oras (mula −12 hanggang +36 h)** | Inililipat ang sandali ng kalkulasyon mula 12 oras bago hanggang 36 na oras pagkatapos ng oras na iyon, sa mga hakbang na 15 minuto. Sa tabi nito: *Kalkulasyon para sa: ngayon* o *Kalkulasyon para sa: dd/mm hh:mm UTC*. |
| **Real time** | Bumalik sa ngayon. |

## 2. Ang iyong istasyon at ang DX

1. I-type ang **Ang aking locator** at **taas m**.
2. I-type ang locator at taas ng **DX station** – o i-click ang mapa sa [Kalangitan](Sky-View-tl): **kaliwang click = locator ng DX station**, **kanang click = locator ng aking istasyon**.
3. Piliin ang **Banda MHz** at pindutin ang **Kalkulahin**.

Kinukumpirma ito ng status bar sa ibaba: *Nakalkula ang landas: … km, … punto ng repleksiyon na na-sample sa … s*.

## 3. Ang iyong antenna

Ilagay ang **haba ng boom** ng iyong Yagi. Hinahango ng programa ang gain at lobe, at binabalaan ka kung ang Hot A o Hot B ay **nasa loob na ng lobe** kapag nakatutok ang antenna sa DX (kulay abo ang guhit sa mga ito: hindi na kailangang ipihit ang antenna).

## 4. Basahin ang mga resulta

| Tanong | Saan titingin |
|---|---|
| Aling shower ang nakatutulong sa aking landas ngayon, at mula sa aling panig? | [Kalangitan](Sky-View-tl): listahan ng mga shower, inirerekomendang Hot na pula, mga PREV na sona |
| Ano ang pinakamahusay na oras ngayong araw? | [Kalkulasyon ng episyensya](Efficiency-Calculation-tl): mga card at talahanayan bawat oras |
| Ilang meteor ang binibilang ng radar? | [Flux ng radar](Radar-Flux-tl) |
| Ilang ping ang maaasahan ko sa 144 MHz? | [Eksperimental na pagtataya](Experimental-Forecasts-tl) (eksperimental) |
| Kaya ba ng aking istasyon na isara ang landas? | [Heometriya at path loss](Geometry-and-Path-Loss-tl): path loss at margin |
| Kailan ang susunod na peak? | [Mga shower](Showers-tl) |
| Puwede ba akong sumubok gamit ang GRAVES? | [Radar GRAVES](GRAVES-Radar-tl) |

## Mga praktikal na tuntunin (mula sa mga sanggunian)

- **Itutok nang patayo sa shower**: ang pinakamahusay na landas ay orthogonal sa azimuth ng radiant; pinakamahusay na tutok = azimuth ng radiant ±90°, tolerance ±40–50° (SM6FHZ).
- **Side-scatter**: ipihit ang antenna nang 10–30° patungo sa panig (A o B) na pinagmumulan ng karamihan ng repleksiyon (artikulong Cerrotta–Sartori).
- **Masyadong mataas na radiant** (higit sa 70°) o masyadong mababa (mas mababa sa 20°) ay nagbibigay ng kaunting magagamit na bakas (DF5HC, DH9GCD).
- Nasa peak ang mga sporadic na meteor bandang **06 UTC** (artikulo; kinumpirma ng flux ng Collm).
- Mga magagamit na distansiya sa 432 MHz: 800–2000 km, pinakamahusay mga 1400 km (SM6FHZ); pinakamahusay na distansiya sa pangkalahatan 1300–1500 km (DF5HC).

Susunod: [Kalangitan](Sky-View-tl).
