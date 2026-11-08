[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · **Tagalog** · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Eksperimental na pagtataya

*Tab: Kalkulasyon ng pagtataya › Eksperimental na pagtataya.*

[![Eksperimental na pagtataya](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ginagawa ng tab na ito ang bilang ng meteor ng **radar ng Collm (36.2 MHz)** na isang tantiya ng **repleksiyon bawat oras sa isang amateur band** (144 MHz bilang default, anumang frequency mula 28 hanggang 1300 MHz), tinataya ang **susunod na 24 na oras** para sa iyong landas at hinahayaan kang **ihambing** ang tantiya sa isang **RMOB** observer – halimbawa, isang nakikinig sa GRAVES sa 143.050 MHz.

> **Eksperimental** ang lahat dito: empirikal na tuntunin ang tuntunin ng frequency, at nakadepende sa iyong istasyon ang station factor. Gamitin ang mga numero para paghambingin ang mga oras at araw, at suriin ang mga ito sa ere.

## Mga kontrol

| Kontrol | Default | Ano ang ginagawa |
|---|---|---|
| **Target na frequency MHz** | 144 | Frequency ng pagtataya (28–1300 MHz) |
| **Exponent ng λ^k** | 3 | Exponent k ng tuntunin ng frequency (SM6FHZ: 3) |
| **Station factor K** | 1 | Isinasaalang-alang ang tumatanggap na istasyon (power, antenna); hinahango sa paghahambing sa isang RMOB observer sa parehong banda |
| **Ikarga ang RMOB file mula sa disk...** | | Binabasa ang isang buwanang RMOB text file (tingnan sa ibaba) |
| **Kunin ang exponent mula sa RMOB file** | | Inaangkop ang k mula sa magkatugmang oras ng Collm at RMOB |
| **RMOB observer** | walang laman | Pangalan ng observer gaya ng nasa pangalan ng file (hal. `NAME_112026rmob.TXT` → `NAME`) |
| **I-download ang RMOB ngayon** | | Dina-download nang isang beses ang file ng kasalukuyang buwan ng observer na iyon |
| **awtomatikong pag-download bawat 5 minuto (i-on lamang kung may pahintulot ng RMOB)** | **naka-off** | Tingnan ang [Ang RMOB at mga awtomatikong programa](#ang-rmob-at-mga-awtomatikong-programa) |

Ipinapakita ng kahel na linya sa ilalim ng mga kontrol ang tuntunin na may kasalukuyang mga numero, hal. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, ang pag-iskala ng tagal at ang pinakamahabang ping ng IARU sa frequency na iyon.

## Mula sa radar patungo sa amateur band

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Sanggunian:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, Mayo 2025 – ang bilang at lakas ng mga repleksiyon ay sumusunod sa **λ³**, ang tagal sa **λ²** (ang 432 MHz ay 14–15 dB na mas mababa sa 144 MHz at tumatagal nang 1/9). **Pagsusuri:** ang pagdepende sa λ³ ay kapareho ng nasa underdense na ekwasyon ni McKinley. Kapag k = 3, ang 1000 meteor/oras sa Collm ay nagiging mga **16 na repleksiyon/oras sa 144 MHz**; karaniwang nakabibilang ang mga RMOB observer ng GRAVES sa 143.050 MHz ng **20 hanggang 140 echo/oras** (bulletin ng RMOB, Hunyo 2018): magkatugma ang order of magnitude, at ang pagkakaiba ay ang station factor K. (Manwal eq. 44–45.)

## Susunod na 24 na oras

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistence:** ang iniskalang halaga ng parehong oras noong nakaraang araw (o dalawang araw bago kung nawawala), na itinama ng pagbabago ng **indeks ng mga shower sa landas** I (Σ ZHR × episyensya, tingnan ang [Kalkulasyon ng episyensya](Efficiency-Calculation-tl#ang-modelo)). Ang constant na 10 ay kumakatawan sa sporadic na background at nililimitahan ang koreksiyon kapag maliit ang indeks. *Pagpili ng programa (manwal eq. 47).*

| Panel | Nilalaman |
|---|---|
| **Sinukat sa Collm at iniskala sa f MHz – kahapon at ngayon (UTC)** | Meteor/oras ng radar ng Collm; mga iniskalang halaga (kahel, iskala sa kanan); ang bilang ng RMOB kung naikarga (berde, iskala sa kanan) |
| **Eksperimental na pagtataya ng susunod na 24 oras sa f MHz para sa …** | Tinatayang repleksiyon/oras (mga bar) at ang indeks ng mga shower sa landas (iskala sa kanan) |
| Talahanayan | Oras UTC · Collm sa parehong oras · Iniskala · Indeks ng mga shower sa landas · Pagtataya /oras · **Pagtatasa** |

**Pagtatasa:** *mabuti* kapag ang pagtataya ay hindi bababa sa 1.3 × ng mean ng 24 na oras, *katamtaman* mula 0.8 ×, *mahina* sa ilalim nito. Lumalabas din ang parehong pagtataya sa card na **EKSPERIMENTAL NA PAGTATAYA** at sa kahel na hanay ng [Kalkulasyon ng episyensya](Efficiency-Calculation-tl), at ito ang batayan ng inaasahang echo sa tab na [Radar GRAVES](GRAVES-Radar-tl#inaasahang-echo-eksperimental).

## Paghahambing sa RMOB

Kinokolekta ng [RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) ang bilang ng meteor bawat oras ng mga radio observer; marami sa Italya ang nakikinig sa GRAVES sa 143.050 MHz (Planetarium ng Venice, Faenza, Rovereto at iba pa).

**Pagbasa ng mga RMOB file.** Dalawang text format ang tinatanggap:

| Format | Itsura | Mga tala |
|---|---|---|
| Buwanang file (Colorgramme / Spectrum Lab) | isang hanay bawat araw, `day| n| n| …` na may 24 na halaga bawat oras | ang karaniwang `NAME_MMYYYYrmob.TXT` |
| Talahanayan ng bulletin | header na ` UT |  1   2   3 …`, mga hanay na `0h|175 166 …` | kung may ilang observer ang file, binabasa sila nang sunud-sunod: gumamit ng file na may iisang observer |

Ang buwan at taon ay kinukuha mula sa pangalan ng file (`…_MMYYYYrmob…`) o mula sa header; kung hindi, ginagamit ang kasalukuyang buwan (at sinasabi ito ng programa).

**Pag-aangkop ng exponent.** Kapag K = 1, mula sa median ng mga ratio na RMOB/Collm sa magkatugmang oras (hindi bababa sa 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Pagpili ng programa (manwal eq. 46).* Ipinapakita ng dialog ang magkatugmang oras, ang median na ratio at ang k; inilalapat ng **Oo** ang k (at itinatakda ang K = 1), pinananatili ng **Hindi** ang k = 3 – pagkatapos ay ayusin nang mano-mano ang K sa halagang iminumungkahi sa parehong dialog.

## Ang RMOB at mga awtomatikong programa

Hinihiling ng RMOB na **huwag kunin ng mga awtomatikong programa ang mga file nito**. Dahil dito, **naka-off ang awtomatikong pag-download** sa simula at dapat lamang itong i-enable **pagkatapos humingi ng pahintulot sa RMOB**. Kung wala nito, palagi mong magagamit ang **Ikarga ang RMOB file mula sa disk...** o pindutin ang **I-download ang RMOB ngayon** kapag kailangan mo.

Ang address ng pag-download ay isang template sa `config.ini` (key na `rmob_url`, default `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kung saan ang `{NOME}` ay ang observer at ang `{MMAAAA}` ay buwan at taon); iniimbak ang mga na-download na file sa `data/radar/`.
