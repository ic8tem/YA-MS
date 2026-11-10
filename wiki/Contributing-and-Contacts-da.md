[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · **Dansk** · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

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

Denne wiki findes på 36 sprog (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); rettelser til wikisiderne er også velkomne.
