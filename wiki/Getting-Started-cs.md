[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · **Čeština** · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Začínáme

Při prvním spuštění YA-MS zobrazí ukázkovou trasu (JN70CN → JO62QM na 144 MHz). Na nastavení pro vaši stanici stačí pět minut.

## 1. Tři řady ovládacích prvků

Nad kartami jsou tři řady ovládacích prvků, platné pro všechny karty. Tlačítko **Ovládání** vpravo nahoře je sbalí a rozbalí (užitečné při velkém písmu); volba se pamatuje.

**Řada 1 – stanice a pásmo**

| Ovládací prvek | Co dělá |
|---|---|
| **Můj lokátor** / **výška m** | Váš lokátor Maidenhead (4, 6 nebo 8 znaků; použije se střed čtverce) a nadmořská výška stanice. |
| **Stanice DX** / **výška m** | Lokátor a výška stanice, se kterou chcete navázat spojení. |
| **Pásmo MHz** | 28, 50, 70, 144, 222 nebo 432 MHz: používá se pro zisk a lalok antény, odhad toku a energetickou bilanci spoje. |
| **Vypočítat** | Znovu vypočítá trasu (vzorkování vrstvy E: několik sekund). |
| **Az. antény** | Azimut vaší antény: vždy **směrem k DX** (azimut trasy). |
| **Písmo** | Velikost veškerého textu, 100–300 %. Viz [Nastavení](Settings-and-Data-Folder-cs#písmo-a-ovládání). |

**Řada 2 – vrstva E a anténa**

| Ovládací prvek | Co dělá |
|---|---|
| **Výška stopy km** + **z radaru** | Výška meteorických stop (výchozí 90 km). Při zaškrtnutém *z radaru* se použije nejčastější výška (modus) změřená radarem v Collmu; viz [Tok z radaru](Radar-Flux-cs). |
| **Elevace laloku °** | Nejnižší elevace laloku vaší antény (0° = obzor). Použijí se jen body vrstvy E, které obě stanice vidí nad touto elevací. |
| **Anténa Yagi: ráhno m** | Délka ráhna vaší Yagi. Program zobrazí délku v λ, zisk (křivka DL6WU) a lalok −3 dB, vodorovný i svislý; viz [Geometrie a útlum trasy](Geometry-and-Path-Loss-cs#zisk-a-lalok-antény). Pod 2 λ je odhad hrubý. |
| **Hot spot od středu trasy km** | Vzdálenost Hot A a Hot B od středu trasy, 30–400 km (výchozí 150 km, jako AMS Bulletin 203 / W8WN / MSHV). |

**Řada 3 – čas**

| Ovládací prvek | Co dělá |
|---|---|
| **Čas** | Hodiny UTC. |
| **Čas nebeské klenby (±36 h)** | Posune [Nebeskou klenbu](Sky-View-cs) a kartu [Radar GRAVES](GRAVES-Radar-cs) až o 36 hodin zpět nebo dopředu, v krocích po 15 minutách. |
| **Reálný čas** | Zpět na současnost. |
| **Den pro tabulku 24 h (UTC)** | Den zobrazený ve [Výpočtu účinnosti](Efficiency-Calculation-cs) a na časové ose GRAVES. |

## 2. Vaše stanice a DX

1. Zadejte **Můj lokátor** a **výška m**.
2. Zadejte lokátor a výšku **stanice DX** – nebo klikněte do mapy v [Nebeské klenbě](Sky-View-cs): **levé tlačítko = lokátor stanice DX**, **pravé tlačítko = lokátor mé stanice**.
3. Zvolte **Pásmo MHz** a stiskněte **Vypočítat**.

Stavový řádek dole potvrdí: *Trasa vypočtena: … km, … bodů odrazu vzorkováno za … s*.

## 3. Vaše anténa

Zadejte **délku ráhna** vaší Yagi. Program z ní odvodí zisk a lalok a upozorní vás, pokud Hot A nebo Hot B už při směrování antény na DX leží **uvnitř laloku** (pak jsou vykresleny šedě: anténu není třeba otáčet).

## 4. Čtení výsledků

| Otázka | Kde hledat |
|---|---|
| Který roj teď pomáhá mé trase a z které strany? | [Nebeská klenba](Sky-View-cs): seznam rojů, doporučený Hot červeně, zóny PREV |
| Která hodina je dnes nejlepší? | [Výpočet účinnosti](Efficiency-Calculation-cs): přehledové karty a hodinová tabulka |
| Kolik meteorů radar počítá? | [Tok z radaru](Radar-Flux-cs) |
| Kolik pingů mohu čekat na 144 MHz? | [Experimentální předpovědi](Experimental-Forecasts-cs) (experimentální) |
| Dokáže moje stanice trasu uzavřít? | [Geometrie a útlum trasy](Geometry-and-Path-Loss-cs): útlum trasy a rezerva |
| Kdy je příští maximum? | [Roje](Showers-cs) |
| Mohu zkoušet s GRAVES? | [Radar GRAVES](GRAVES-Radar-cs) |

## Praktická pravidla (ze zdrojů)

- **Směrujte kolmo k roji**: nejlepší trasa je kolmá na azimut radiantu; nejlepší směrování = azimut radiantu ±90°, tolerance ±40–50° (SM6FHZ).
- **Boční rozptyl (side-scatter)**: natočte anténu o 10–30° ke straně (A nebo B), ze které přichází většina odrazů (článek Cerrotta–Sartori).
- **Příliš vysoký radiant** (nad 70°) nebo příliš nízký (pod 20°) dává málo užitečných stop (DF5HC, DH9GCD).
- Sporadické meteory mají maximum kolem **06 UTC** (článek; potvrzeno tokem z Collmu).
- Užitečné vzdálenosti na 432 MHz: 800–2000 km, nejlepší asi 1400 km (SM6FHZ); nejlepší vzdálenost obecně 1300–1500 km (DF5HC).

Dále: [Nebeská klenba](Sky-View-cs).
