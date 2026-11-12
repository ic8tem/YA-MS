[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · **Čeština** · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – předpovědi pro meteor scatter a účinnost rojů v reálném čase

*autor: Costantino Cerrotta IC8TEM*

**YA-MS** je bezplatný program pro radioamatéry, kteří pracují provozem **meteor scatter (MS) na 50, 70, 144, 222 a 432 MHz**. Pro skutečnou trasu mezi vaším lokátorem a lokátorem DX stanice počítá hodinu po hodině, jak moc každý aktivní meteorický roj trase pomáhá (jeho **účinnost**), z které strany trasy přicházejí odrazy (**Hot A / Hot B**), kam nasměrovat anténu, a experimentální předpověď počtu odrazů za hodinu odvozenou z **živého meteorického radaru** (Collm, Německo). Běží na **Windows, Linuxu, Raspberry Pi a macOS** (.NET 8 + Avalonia) v 36 jazycích rozhraní.

Hlavním zdrojem je článek **C. Cerrotty IC8TEM a G. Sartoriho IV3GTH** *„METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese“* (Meteor scatter aneb jak se spojit s Evropou na VHF po celý rok bez velkých nároků; verze 7). Každý vzorec a každý údaj v programu uvádí svůj zdroj; viz [Zdroje](Sources-cs).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Nebeská klenba"></a><br><sub>Nebeská klenba</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Výpočet účinnosti"></a><br><sub>Výpočet účinnosti</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Pro koho je určen

- Pro operátory, kteří chtějí vědět, **kdy** je trasa pro meteor scatter otevřená a **kam** směrovat anténu, nad rámec obecného „roj má dnes v noci maximum“.
- Pro stanice pracující na **dlouhých trasách na 144 a 432 MHz**, kde poloha radiantu rozhoduje o tom, zda je roj užitečný, nebo k ničemu.
- Pro každého, kdo si chce **ověřit čísla**: manuál výpočtů i vysvětlení v programu uvádějí každý krok s jeho původem – publikovaný zdroj, ověření provedené na programu, nebo volba programu.

## Karty

Od verze 1.6 mají hlavní karty **podkarty** (světlejší řada pod hlavní řadou). Při spuštění se na 5 sekund zobrazí úvodní obrazovka s Perseidami nad dalekohledem VLT observatoře ESO (foto ESO/S. Guisard, CC BY 4.0).

| Karta | Podkarta | Co zobrazuje |
|---|---|---|
| **Živě a data v reálném čase** | [Provoz živě](Live-Traffic-cs) | Azimutální mapa veškerého zachyceného MS provozu s oblakem nejpravděpodobnějších stop pro každé spojení, barvami pásem a blikajícími novými spoty |
| | [Tok z radaru](Radar-Flux-cs) | Hodinové počty meteorů a výšky stop načtené z radaru SKiYMET v Collmu, obrázek ze Sodankylä, odhad pro vaše pásmo |
| | [Radar GRAVES](GRAVES-Radar-cs) | Trasa dopředného rozptylu GRAVES → vy: užitečná zóna ve svazku, sektor a krok, příští průchod svazku, jak poslouchat |
| | [Sběr dat](Data-Collection-cs) | Tři telnetové proudy clusterů (DX cluster, RBN, DM4X/PSKReporter) a filtr MS spotů |
| **Předpovědní výpočet** | [Předpovědní výpočet](Sky-View-cs) | Půdorysná mapa trasy s Hot A / Hot B, lalokem antény, zónami PREV a driftem roje; seznam rojů; malá nebeská klenba s radianty a správnými směry antény; řez viděný od antény |
| | [Geometrie a útlum](Geometry-and-Path-Loss-cs) | Vzdálenost, střed trasy, elevace, Hot A / Hot B, meze společné zóny, útlum trasy 28–432 MHz, energetická bilance spoje, anténa |
| | [Výpočet účinnosti](Efficiency-Calculation-cs) | Přehledové karty, hodinová účinnost každého roje se stranou A/B, index trasy, srovnání s DH9GCD, graf |
| | [Experimentální předpovědi](Experimental-Forecasts-cs) | Tok z Collmu přepočtený na 144 MHz (nebo libovolnou frekvenci) pomocí λ^k a faktoru stanice K, předpověď na 24 hodin, srovnání s RMOB |
| [Roje živě](Live-Showers-cs) | – | Naměřené ZHR sítě Global Meteor Network a mapy radiantů CMOR |
| [Roje](Showers-cs) | – | Katalog IMO s příštím maximem (datum a čas podle IMO nebo vypočtené) |
| [Mapa čtverců](Grid-Square-Map-cs) | – | Navázané a potvrzené čtverce Maidenhead ze souboru ADIF, jedna karta pro každé pásmo |
| **Technické dokumenty** | [Zdroje](Sources-cs) | Všechny zdroje; hlavním je článek Cerrotta–Sartori |
| | [Mapa evropských radarů](European-Radar-Map-cs) | Kde leží Collm, Sodankylä, GRAVES a CMOR vzhledem k vaší stanici |
| | [Účinnost - vysvětlení](Efficiency-Explanation-cs) | Dokument krok za krokem o tom, jak se počítá účinnost, s možností exportu do Wordu |

Nad kartami jsou tři řady ovládacích prvků (váš lokátor, DX stanice, pásmo, anténa, výška stop, čas); viz [První kroky](Getting-Started-cs). Tlačítko **Ovládání** je skryje a jazyk a barevné schéma se volí vpravo nahoře; viz [Nastavení a datová složka](Settings-and-Data-Folder-cs).

## Ve zkratce

- **Skutečná trasa, ne pevné směry**: účinnost se počítá pro trasu po hlavní kružnici mezi oběma lokátory (starší programy používaly čtyři pevné směry).
- **Model zrcadlového odrazu** (McKinley) v bodech vrstvy E každých 15 km, s výškou stop načítanou živě z radaru v Collmu.
- **Hot A / Hot B** 150 km na obě strany od středu trasy (nastavitelné 30–400 km), doporučený červeně, ty, které již leží uvnitř laloku vaší antény, šedě.
- **Živý radar**: Collm se kontroluje každých 5 minut, znovu se stahují jen změněné zdroje; bez připojení program dál pracuje s naposledy uloženými daty.
- **Experimentální** předpověď pro 50/144/432 MHz podle pravidla λ³ od SM6FHZ, srovnatelná s pozorovateli RMOB.
- Vše v jediné složce **`data`** vedle programu: žádné AppData, žádné systémové složky.

> Účinnost je experimentální model (zrcadlový odraz + podhusté stopy). Porovnávejte ji s MCG_MS, MS-Soft a s vlastní zkušeností z pásma.

## Kde začít

1. [Instalace](Installation-cs)
2. [První kroky](Getting-Started-cs)
3. [Řešení problémů a FAQ](Troubleshooting-FAQ-cs), pokud něco nefunguje.

Ke stažení: **[Releases](https://github.com/ic8tem/YA-MS/releases)** na GitHubu.
