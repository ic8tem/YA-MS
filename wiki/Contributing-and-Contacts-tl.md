[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · **Tagalog** · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Pag-ambag at pakikipag-ugnayan

Humuhusay ang YA-MS sa pamamagitan ng mga ulat ng mga gumagamit nito sa ere. Bawat koreksiyon ay kinikilala ayon sa pinagmulan nito.

## Pakikipag-ugnayan

| | |
|---|---|
| May-akda | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Pag-uulat ng problema

Magbukas ng **issue sa GitHub** o sumulat ng e-mail na may:

- operating system at bersyon ng YA-MS (nasa title ng window);
- ang dalawang locator, banda at oras na UTC;
- ang inaasahan mo at ang nakita mo (nakatutulong ang screenshot);
- para sa mga problema sa radar, ang mensaheng ipinakita sa tab na [Flux ng radar](Radar-Flux-tl).

## Ano ang lalong kapaki-pakinabang

- **Mga ulat mula sa ere.** Mga oras at landas kung saan tama – o mali – ang episyensya o ang pagtataya. Eksperimental ang modelo at kailangan itong ihambing sa totoong mga QSO at sa MCG_MS / MS-Soft.
- **Mga paghahambing sa RMOB.** Mga halaga ng station factor K at ng exponent k na nakuha mo sa [paghahambing sa RMOB](Experimental-Forecasts-tl#paghahambing-sa-rmob), kasama ang iyong banda at istasyon.
- **Datos na may sanggunian.** Mas mahusay na pag-usad ng radiant, profile ng aktibidad, bagong petsa ng peak ng IMO (`data/massimi_imo.csv`), datos ng antenna: isama ang sanggunian at babanggitin ito.
- **Mga pagbabago sa graph ng radar.** Kung magbago ang format ng graph ng Collm, nakatutulong ang kopya ng larawan (`data/radar/`) para i-recalibrate ang pagbasa.

## Mga salin

Ang mga salin ng interface ay mga simpleng text file sa **`data/lingue/<code>.txt`** (UTF-8) at **maaaring itama ng sinuman**:

```
<Italian text><TAB><translation>
```

- Isang entry bawat linya; komento ang mga linyang nagsisimula sa `#`.
- Sa parehong column, ang dalawang character na `\n` ay nangangahulugang line break.
- Panatilihin ang mga placeholder na `{0}`, `{1}`, … kasama ang kanilang format (hal. `{0:F1}`, `{3:+0;-0}`), sa pagkakasunod na kailangan ng iyong wika.
- Ipinapakita sa Italyano ang mga nawawala o walang lamang entry. Ang listahan ng lahat ng key ay `data/lingue/chiavi.txt` (nililikha ng `tools/estrai_chiavi.py`, huwag itong i-edit).

I-edit ang file sa folder na `data/lingue` ng iyong instalasyon at i-restart ang YA-MS (o magpalit ng wika) para makita ang resulta. Dahil **pinapalitan ang mga file na ito ng mas bagong bersyon sa bawat update**, pakipadala rin ang iyong mga koreksiyon – sa e-mail o bilang pull request sa GitHub (`data/lingue/`) – para maisama sa susunod na release.

Umiiral ang wiki na ito sa 36 na wika (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); tinatanggap din ang mga koreksiyon sa mga pahina ng wiki.
