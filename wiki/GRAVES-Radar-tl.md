[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · **Tagalog** · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Tab: Live at real-time na datos › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Ano ang GRAVES

Ang **GRAVES** ay isang radar na Pranses na nagpapadala ng **CW sa 143.050 MHz** mula sa **Broye-lès-Pesmes** (47.348° N 5.515° E, locator **JN27SI**, mga 200 m mula sa antas ng dagat; Wikipedia). Ang mga bakas ng meteor sa sonang nakikita kapwa ng GRAVES at mo ay nagre-reflect ng signal nito patungo sa iyo sa pamamagitan ng **forward scatter**: nakaririnig ka ng maiikling *ping* malapit sa carrier. Ganito binibilang ng mga **RMOB** observer sa 143.050 MHz ang mga meteor bawat oras, at isa itong libre at laging naka-on na test signal para sa iyong istasyong meteor scatter sa 2 m.

Itinuturing ng tab ang **GRAVES → ikaw** bilang sariling landas na meteor scatter: gamit ang parehong mga function ng pangunahing landas (parehong taas ng bakas, elebasyon ng lobe at distansiya ng hot spot), kinakalkula nito ang episyensya ng mga shower, ang inirerekomendang Hot at ang mga PREV na sona, at pagkatapos ay sinusuri kung ang sonang iyon ay **nasa loob ng beam ng GRAVES** at **kailan** ito iniilawan ng beam.

## Itaas na bar

| Kontrol | Ano ang ginagawa |
|---|---|
| **Ngayon** | Ibinabalik sa real time ang oras ng kalangitan (sinusundan ng tab ang slider na *Oras ng kalangitan*). |
| **Gawing DX ang GRAVES** | Nagiging GRAVES ang DX station (JN27SI, taas 200 m) at muling kinakalkula ang pangunahing landas: ipapakita na ng lahat ng ibang tab ang landas ng GRAVES. |
| **Sequence ng beam** | *0.8 s bawat hakbang · siklo 4.8 s (PE1ITR 2021)* (default) o *3.2 s bawat hakbang · siklo 19.2 s (PE1ITR 2007)*. |

## Ang apat na card

| Card | Nilalaman |
|---|---|
| **MAGAGAMIT NA SONA SA BEAM NG GRAVES** | *Oo · sektor X* kasama ang azimuth at elebasyon ng inirerekomendang hot spot ayon sa GRAVES at ang hakbang (1–6); o *Hindi: labas sa mga sektor* / *Hindi: nasa ilalim ng horizon ng GRAVES* / *Hindi: nasa itaas ng beam (mga 25°)* |
| **EPISYENSYA NG LANDAS GRAVES → IKAW NGAYON** | Indeks ng landas Σ ZHR × episyensya, pinakamahusay na shower, nangingibabaw na panig A/B, at *inaasahang echo ≈ …/oras* (eksperimental, tingnan sa ibaba) |
| **LANDAS** | Distansiya sa GRAVES; antenna patungo sa inirerekomendang Hot (azimuth at elebasyon); tuwirang azimuth ng GRAVES |
| **SUSUNOD NA PAGDAAN NG BEAM SA SONA** | *ngayon · … s pa* o *sa loob ng … s*, ang hakbang (hal. *B4*), ang susunod na tatlong oras (mga segundo sa loob ng minuto) at ang bahagi ng mga bakas na nahuhuli |

Kung walang kapaki-pakinabang na shower sa sandaling iyon, ipinapakita ng programa ang hot spot na **pinakaangkop sa beam** (nasa loob ng mga sektor, pinakamalapit sa timog) at sinasabi ito.

## Ang langit ayon sa GRAVES

Ayon kay PE1ITR at sa Bolidozor wiki, **apat na phased array** ang sumasaklaw sa katimugang langit mula **90° hanggang 270°** na azimuth sa apat na **sektor na tig-45°**:

| Sektor | Azimuth mula sa GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Hinahati ang bawat sektor sa **6 na hakbang na tig-7.5°**, may bilang na 1 hanggang 6 mula sa pinakamababang azimuth, na iniilawan nang sunud-sunod, **sa iisang sandali sa lahat ng apat na sektor**. Mga **25° ang lapad ng beam sa elebasyon**: sa taas ng mga bakas, sinasaklaw nito ang may-kulay na singsing sa pagitan ng dalawang putol-putol na bilog (*horizon ng beam*). Sa drowing: mga kahel/rosas na tuldok = mga PREV na sona ng landas na GRAVES → ikaw, berdeng linya = direksiyon ng iyong istasyon, pulang linya = mula sa iyong istasyon patungo sa inirerekomendang hot spot; naka-highlight ang hakbang na naiilawan ngayon.

## Kronolohikong rekonstruksiyon

*KRONOLOHIKONG REKONSTRUKSIYON · petsa UTC* (parehong araw ng 24 h na talahanayan): para sa bawat oras, ang episyensya ng landas na GRAVES → ikaw, ang pinakapaborableng shower at ang magagamit na window (*hh:00 → hh:00 UTC · n h*), kasama ang pinakamataas (*max Σ … sa hh:30*) at isang pulang marka ng *ngayon*. Sa ibaba, ang **detalye ng susunod na mga segundo**: ang anim na hakbang ng sektor, ang hakbang na nag-iilaw sa magagamit na sona, at *posibleng echo (+0.3 s ng bakas)*.

### Tiyempo ng beam

Nakatali sa **UTC** ang sequence (PE1ITR): kinakalkula ang hakbang na naiilawan ngayon mula sa mga segundo mula 00:00 UTC modulo ang siklo (ang 86 400 s ay multiple ng 4.8 s at ng 19.2 s). Paminsan-minsan, inililipat ng command station ang sequence nang ilang hakbang, kaya ang detalye ay isang **prediksiyon na dapat kumpirmahin sa pakikinig**. Ipinapaalala ito ng dilaw na pill na **naka-synchronize ang orasan ng PC**: i-synchronize ang iyong PC sa isang NTP server (error na ilang ikasampu ng segundo lamang sa pinakamarami).

### Detection factor

Naririnig lamang ang isang bakas kung iniilawan ito ng beam habang tumatagal ito:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

Ang 0.3 s ay karaniwang tagal ng underdense na bakas sa 143 MHz – isang nakapirming halaga, *pagpili ng programa* (iniskala ng λ² na tuntunin ni SM6FHZ ang tagal sa pagitan ng mga banda pero hindi ito nagbibigay ng panimulang halaga).

### Inaasahang echo (eksperimental)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Ang pagtataya ng [Eksperimental na pagtataya](Experimental-Forecasts-tl) (na may kasama nang station factor K) ay iniiskala mula sa frequency nitong f_fc patungo sa 143.050 MHz gamit ang tuntunin ni SM6FHZ (parehong exponent k), itinatama ng ratio ng mga indeks ng shower ng dalawang landas (ang constant na 10 ay kumakatawan sa sporadic na background, gaya sa pagtataya) at minumultiply sa detection factor. Pahiwatig lamang: ihambing sa mga RMOB observer.

## Paano marinig ang mga ping ng GRAVES

| Hakbang | Ano ang gagawin |
|---|---|
| Receiver | **USB sa 143.049 MHz** (tono na mga 1 kHz) o 143.050 MHz, **mabagal o naka-off na AGC**, audio bandwidth na **hindi bababa sa 2.4 kHz** |
| Antenna | Patungo sa **inirerekomendang hot spot** ng landas na GRAVES → ikaw (card na *LANDAS*), sa **mababang elebasyon** |
| Waterfall | Ang mga ping ay **maiikling linya malapit sa carrier**; mas malapad ang mahahabang (overdense) bakas at may Doppler |
| Pagbilang | Ginagamit ng RMOB ang GRAVES para sa bilang ng meteor bawat oras: **ihambing ang iyong mga ping sa mga observer sa 143.050 MHz** ([Eksperimental na pagtataya](Experimental-Forecasts-tl#paghahambing-sa-rmob)) |

## Mga sanggunian

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) at *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – mga array, sektor at tiyempo ng beam
3. **Wikipedia**, "GRAVES (system)" – transmitter sa Broye-lès-Pesmes (47.348° N 5.515° E)
4. **RMOB** – mga observer sa 143.050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** ni IC8TEM – tab na Radar GRAVES (ang burador na pinagmulan ng tab na ito)
