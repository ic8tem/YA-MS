**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

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

Þessi wiki er til á English, Русский, Deutsch og 日本語; leiðréttingar á wiki-síðunum eru líka vel þegnar.
