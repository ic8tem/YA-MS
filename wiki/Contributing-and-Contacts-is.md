[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · **Íslenska** · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Framlög og tengiliðir

YA-MS batnar þökk sé ábendingum þeirra sem nota það í loftinu. Hver leiðrétting er eignuð heimild sinni.

## Tengiliðir

| | |
|---|---|
| Höfundur | Costantino Cerrotta **IC8TEM** |
| Netfang | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Tilkynna vandamál

Opnaðu **issue á GitHub** eða sendu tölvupóst með:

- stýrikerfi og útgáfu YA-MS (í titli gluggans);
- locatorunum tveimur, tíðnisviði og UTC-tíma;
- því sem þú bjóst við og því sem þú sást (skjámynd hjálpar);
- ef um ratsjárvandamál er að ræða, skilaboðunum sem birtast á flipanum [Ratsjárflæði](Radar-Flux-is).

## Hvað er sérstaklega gagnlegt

- **Ábendingar úr loftinu.** Klukkustundir og leiðir þar sem nýtnin eða spáin reyndist rétt – eða röng. Líkanið er tilraun og þarf samanburð við raunveruleg QSO og við MCG_MS / MS-Soft.
- **Samanburður við RMOB.** Gildi stöðvarstuðulsins K og veldisvísisins k sem þú fannst með [samanburðinum við RMOB](Experimental-Forecasts-is#samanburður-við-rmob), ásamt tíðnisviði og stöð.
- **Gögn með heimild.** Betra rek geislapunkta, virknisnið, nýjar dagsetningar hámarka frá IMO (`data/massimi_imo.csv`), loftnetsgögn: tilgreindu heimildina og vitnað verður í hana.
- **Breytingar á gröfum ratsjánna.** Ef snið Collm-grafsins breytist hjálpar afrit af myndinni (`data/radar/`) við að kvarða lesturinn upp á nýtt.

## Þýðingar

Þýðingar viðmótsins eru venjulegar textaskrár í **`data/lingue/<code>.txt`** (UTF-8) og **hver sem er getur leiðrétt þær**:

```
<Italian text><TAB><translation>
```

- Ein færsla á hverri línu; línur sem byrja á `#` eru athugasemdir.
- Í báðum dálkum tákna stafirnir tveir `\n` línuskil.
- Haltu staðgenglunum `{0}`, `{1}`, … með sniði sínu (t.d. `{0:F1}`, `{3:+0;-0}`), í þeirri röð sem tungumálið þitt þarfnast.
- Færslur sem vantar eða eru auðar birtast á ítölsku. Listinn yfir alla lykla er `data/lingue/chiavi.txt` (búinn til af `tools/estrai_chiavi.py`, breyttu honum ekki).

Breyttu skránni í möppunni `data/lingue` í uppsetningunni þinni og endurræstu YA-MS (eða skiptu um tungumál) til að sjá niðurstöðuna. Þar sem **nýrri útgáfur koma í stað þessara skráa við hverja uppfærslu**, vinsamlegast **sendu einnig leiðréttingarnar þínar** – með tölvupósti eða sem pull request á GitHub (`data/lingue/`) – svo þær rati inn í næstu útgáfu.

Þessi wiki er til á 36 tungumálum (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); leiðréttingar á wiki-síðunum eru líka vel þegnar.
