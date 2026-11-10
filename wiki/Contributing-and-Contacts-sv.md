[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · **Svenska** · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Bidrag och kontakter

YA-MS blir bättre tack vare rapporter från dem som använder det i luften. Varje rättelse krediteras sin källa.

## Kontakter

| | |
|---|---|
| Upphovsman | Costantino Cerrotta **IC8TEM** |
| E-post | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Rapportera ett problem

Öppna ett **issue på GitHub** eller skicka ett e-postmeddelande med:

- operativsystem och YA-MS-version (i fönstrets titel);
- de två lokatorerna, band och UTC-tid;
- vad du väntade dig och vad du såg (en skärmbild hjälper);
- vid radarproblem, meddelandet som visas i fliken [Radarflöde](Radar-Flux-sv).

## Vad som är särskilt användbart

- **Rapporter från luften.** Timmar och sträckor där effektiviteten eller prognosen stämde – eller inte stämde. Modellen är experimentell och behöver jämföras med verkliga QSO och med MCG_MS / MS-Soft.
- **Jämförelser med RMOB.** Värden på stationsfaktorn K och exponenten k som du har fått fram med [jämförelsen med RMOB](Experimental-Forecasts-sv#jämförelse-med-rmob), med ditt band och din station.
- **Data med källa.** Bättre radiantdrift, aktivitetsprofiler, nya datum för maximum från IMO (`data/massimi_imo.csv`), antenndata: ange källan så kommer den att citeras.
- **Ändringar i radardiagrammen.** Om formatet på Collm-diagrammet ändras hjälper en kopia av bilden (`data/radar/`) till att kalibrera om avläsningen.

## Översättningar

Gränssnittets översättningar är vanliga textfiler i **`data/lingue/<code>.txt`** (UTF-8) och **vem som helst kan rätta dem**:

```
<Italian text><TAB><translation>
```

- En post per rad; rader som börjar med `#` är kommentarer.
- I båda kolumnerna betyder de två tecknen `\n` en radbrytning.
- Behåll platshållarna `{0}`, `{1}`, … med sitt format (t.ex. `{0:F1}`, `{3:+0;-0}`), i den ordning ditt språk kräver.
- Saknade eller tomma poster visas på italienska. Listan över alla nycklar är `data/lingue/chiavi.txt` (genereras av `tools/estrai_chiavi.py`, redigera den inte).

Redigera filen i mappen `data/lingue` i din installation och starta om YA-MS (eller byt språk) för att se resultatet. Eftersom dessa filer **ersätts av nyare versioner vid varje uppdatering**, **skicka också dina rättelser** – via e-post eller som en pull request på GitHub (`data/lingue/`) – så att de kommer med i nästa release.

Den här wikin finns på 36 språk (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); rättelser till wikisidorna är också välkomna.
