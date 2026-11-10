[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · **Nederlands** · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Bijdragen en contact

YA-MS wordt beter dankzij de meldingen van wie het in de lucht gebruikt. Elke correctie wordt aan haar bron toegeschreven.

## Contact

| | |
|---|---|
| Auteur | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Een probleem melden

Open een **issue op GitHub** of stuur een e-mail met:

- besturingssysteem en versie van YA-MS (in de titel van het venster);
- de twee locators, band en UTC-tijd;
- wat je verwachtte en wat je zag (een schermafbeelding helpt);
- bij problemen met de radar: de melding in het tabblad [Radarflux](Radar-Flux-nl).

## Wat vooral nuttig is

- **Verslagen uit de lucht.** Uren en trajecten waarop de efficiëntie of de voorspelling klopte – of niet. Het model is experimenteel en moet worden vergeleken met echte QSO's en met MCG_MS / MS-Soft.
- **Vergelijkingen met RMOB.** Waarden van de stationsfactor K en van de exponent k die je met de [vergelijking met RMOB](Experimental-Forecasts-nl#vergelijking-met-rmob) hebt gevonden, met je band en station.
- **Gegevens met een bron.** Betere radiantverschuivingen, activiteitsprofielen, nieuwe IMO-data voor maxima (`data/massimi_imo.csv`), antennegegevens: vermeld de bron en die wordt geciteerd.
- **Wijzigingen van de radargrafieken.** Als het formaat van de grafiek van Collm verandert, helpt een kopie van het beeld (`data/radar/`) om het uitlezen opnieuw te kalibreren.

## Vertalingen

De vertalingen van de interface zijn gewone tekstbestanden in **`data/lingue/<code>.txt`** (UTF-8) en **iedereen kan ze verbeteren**:

```
<Italiaanse tekst><TAB><vertaling>
```

- Eén item per regel; regels die met `#` beginnen, zijn commentaar.
- In beide kolommen betekenen de twee tekens `\n` een regeleinde.
- Behoud de plaatshouders `{0}`, `{1}`, … met hun opmaak (bijv. `{0:F1}`, `{3:+0;-0}`), in de volgorde die jouw taal nodig heeft.
- Ontbrekende of lege items worden in het Italiaans getoond. De lijst van alle sleutels is `data/lingue/chiavi.txt` (gegenereerd door `tools/estrai_chiavi.py`, niet bewerken).

Bewerk het bestand in de map `data/lingue` van je installatie en start YA-MS opnieuw (of wissel van taal) om het resultaat te zien. Omdat deze bestanden **bij elke update door nieuwere versies worden vervangen**, vragen we je ook **je correcties op te sturen** – per e-mail of als pull request op GitHub (`data/lingue/`) – zodat ze in de volgende release terechtkomen.

Dit wiki bestaat in het English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文; correcties op de wikipagina's zijn ook welkom.
