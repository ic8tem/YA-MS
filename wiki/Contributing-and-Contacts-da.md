**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

# Bidrag og kontakt

YA-MS bliver bedre takket være rapporterne fra dem, der bruger det på båndet. Hver rettelse krediteres sin kilde.

## Kontakt

| | |
|---|---|
| Forfatter | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Rapportér et problem

Opret et **issue på GitHub**, eller skriv en e-mail med:

- styresystem og YA-MS-version (i vinduets titellinje);
- de to lokatorer, bånd og UTC-tid;
- hvad du forventede, og hvad du så (et skærmbillede hjælper);
- ved radarproblemer: meddelelsen, der vises i fanen [Radarflux](Radar-Flux-da).

## Hvad der er særligt nyttigt

- **Rapporter fra båndet.** Timer og strækninger, hvor effektiviteten eller prognosen ramte rigtigt – eller forkert. Modellen er eksperimentel og skal sammenlignes med faktiske QSO'er og med MCG_MS / MS-Soft.
- **Sammenligninger med RMOB.** Værdier for stationsfaktoren K og eksponenten k, som du har fundet med [sammenligningen med RMOB](Experimental-Forecasts-da#sammenligning-med-rmob), med angivelse af bånd og station.
- **Data med kilde.** Bedre radiantvandringer, aktivitetsprofiler, nye datoer for IMO-maksima (`data/massimi_imo.csv`), antennedata: angiv kilden, så bliver den citeret.
- **Ændringer i radargraferne.** Hvis formatet på Collm-grafen ændres, hjælper en kopi af billedet (`data/radar/`) med at kalibrere aflæsningen igen.

## Oversættelser

Oversættelserne af brugerfladen er almindelige tekstfiler i **`data/lingue/<code>.txt`** (UTF-8), og **alle kan rette dem**:

```
<Italian text><TAB><translation>
```

- Én post pr. linje; linjer, der begynder med `#`, er kommentarer.
- I begge kolonner betyder de to tegn `\n` et linjeskift.
- Bevar pladsholderne `{0}`, `{1}`, … med deres format (fx `{0:F1}`, `{3:+0;-0}`) i den rækkefølge, dit sprog kræver.
- Manglende eller tomme poster vises på italiensk. Listen over alle nøgler er `data/lingue/chiavi.txt` (genereret af `tools/estrai_chiavi.py`, må ikke redigeres).

Redigér filen i mappen `data/lingue` i din installation, og genstart YA-MS (eller skift sprog) for at se resultatet. Da disse filer **udskiftes af nyere versioner ved hver opdatering**, så **send også dine rettelser** – pr. e-mail eller som pull request på GitHub (`data/lingue/`) – så de kommer med i næste udgivelse.

Denne wiki findes på English, Русский, Deutsch og 日本語; rettelser til wikisiderne er også velkomne.
