[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · **Čeština** · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Sběr dat

*Karta: Živá data a data v reálném čase › Sběr dat.*

[![Sběr dat](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Tři proudy clusterů

Karta shromažďuje **spoty meteor scatter** ze tří telnetových proudů, každý ve vlastní podkartě:

| Podkarta | Výchozí | Poznámky |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Cluster dle vlastní volby. Na ON0DXK jsou pásma VKV filtrována: povolte je příkazem `set/filter dxbm/pass 6` (pak 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmery druhy provozu MS dekódují jen zřídka. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X přenášející spoty **PSKReporter**: sem přicházejí dekódování MSK144 z WSJT-X a MSHV. |
| **Shromážděné spoty MS** | – | Tabulka přijatých spotů, nejnovější nahoře. |

Každý proud má hostitele, port, příkazy odesílané po přihlášení, *Znovu připojit*, *Připojit při spuštění*, konzoli a řádek pro odesílání příkazů. Nahoře napište svou **značku pro přihlášení**. Pruh ukazuje stav tří relací (zelená tečka = připojeno). Relace zůstávají otevřené, když změníte jazyk nebo barevné schéma.

## Filtr (40 % okna)

- **Volitelný místní filtr:** řádky clusteru pod **27990,0 kHz** se okamžitě zahazují (nezobrazují se, neukládají se).
- **1. kritérium – typické kmitočty MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot v těchto oknech se přijme i bez názvu druhu provozu, pokud komentář neuvádí jiné šíření: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Okna i značky lze upravovat.
- **2. kritérium – druhy provozu MS:** mimo okna, nebo s jednou z těchto značek, se spot ponechá jen tehdy, obsahuje-li **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitální druhy provozu používané jen pro MS) nebo **\<MS\>**, velkými, malými či smíšenými písmeny. Slova lze vypínat, přidávat a odebírat; každé má své počitadlo.
- **Pásma** 28, 50, 70, 144, 222, 432 MHz; **test filtru** na vloženém řádku; **počitadla**.

## Lokátory a ukládání

Chybějící lokátory nebo lokátory jen se 4 znaky se berou z archivu **CALL3** (`data/call3.txt`, soubor JTDX, přes milion značek), který má vždy přednost před 4znakovým lokátorem. Přijaté spoty se ukládají do `data/spot_ms`, jeden soubor CSV na den, a napájejí mapu [Živý provoz](Live-Traffic-cs).
