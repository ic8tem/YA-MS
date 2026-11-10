[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · **Norsk** · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Bidra og kontakt

YA-MS blir bedre takket være rapportene fra dem som bruker programmet på båndet. Hver rettelse krediteres kilden.

## Kontakt

| | |
|---|---|
| Forfatter | Costantino Cerrotta **IC8TEM** |
| E-post | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Melde et problem

Opprett et **issue på GitHub** eller skriv en e-post med:

- operativsystem og YA-MS-versjon (i vinduets tittellinje);
- de to lokatorene, bånd og UTC-tid;
- hva du forventet og hva du så (et skjermbilde hjelper);
- ved radarproblemer: meldingen som vises i fanen [Radarfluks](Radar-Flux-nb).

## Hva som er særlig nyttig

- **Rapporter fra båndet.** Timer og strekninger der effektiviteten eller prognosen traff – eller bommet. Modellen er eksperimentell og må sammenlignes med virkelige QSO-er og med MCG_MS / MS-Soft.
- **Sammenligninger med RMOB.** Verdier for stasjonsfaktoren K og eksponenten k som du har funnet med [sammenligningen med RMOB](Experimental-Forecasts-nb#sammenligning-med-rmob), med bånd og stasjon.
- **Data med kilde.** Bedre radiantforflytninger, aktivitetsprofiler, nye datoer for IMO-maksima (`data/massimi_imo.csv`), antennedata: oppgi kilden, så blir den sitert.
- **Endringer i radardiagrammene.** Hvis formatet på Collm-diagrammet endres, hjelper en kopi av bildet (`data/radar/`) med å kalibrere avlesningen på nytt.

## Oversettelser

Oversettelsene av grensesnittet er rene tekstfiler i **`data/lingue/<code>.txt`** (UTF-8), og **alle kan rette dem**:

```
<Italian text><TAB><translation>
```

- Én oppføring per linje; linjer som begynner med `#`, er kommentarer.
- I begge kolonnene betyr de to tegnene `\n` et linjeskift.
- Behold plassholderne `{0}`, `{1}`, … med formatet sitt (f.eks. `{0:F1}`, `{3:+0;-0}`), i den rekkefølgen språket ditt krever.
- Manglende eller tomme oppføringer vises på italiensk. Listen over alle nøklene er `data/lingue/chiavi.txt` (generert av `tools/estrai_chiavi.py`, skal ikke redigeres).

Rediger filen i mappen `data/lingue` i installasjonen din og start YA-MS på nytt (eller bytt språk) for å se resultatet. Fordi disse filene **erstattes av nyere versjoner ved hver oppdatering**, ber vi deg også **sende rettelsene dine** – på e-post eller som pull request på GitHub (`data/lingue/`) – så de kommer med i neste utgivelse.

Denne wikien finnes på English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文; rettelser til wikisidene er også velkomne.
