**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

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

Denne wikien finnes på English, Русский, Deutsch og 日本語; rettelser til wikisidene er også velkomne.
