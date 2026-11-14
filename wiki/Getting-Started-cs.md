[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · **Čeština** · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# První kroky

Při prvním spuštění zobrazí YA-MS ukázkovou trasu (JN70CN → JO62QM na 144 MHz). Na nastavení pro vaši stanici stačí pět minut.

## 1. Dva řady ovládacích prvků

Nad kartami jsou dva řady ovládacích prvků, které platí pro všechny karty. Tlačítko **Ovládání** vpravo nahoře je skryje a znovu zobrazí (užitečné při velkém písmu); volba se pamatuje. Vaše stanice (lokátor, výška, pásmo a Vypočítat) je vpravo nahoře na záložce Provoz živě.

**Moje stanice – Provoz živě**

| Ovládací prvek | Co dělá |
|---|---|
| **Můj lokátor** / **výška m** | Váš lokátor Maidenhead (4, 6 nebo 8 znaků; použije se střed čtverce) a nadmořská výška stanice. |
| **Protistanice** / **výška m** | Vedle mapy vpravo je rámeček protistanice: napiš značku a stiskni Enter, lokátor se vezme z databáze CALL3 (jako v YAEC a LIVETROPOVHF); pod ní jsou lokátor a výška. Značku lze napsat i do pole lokátoru. |
| **Pásmo MHz** | 28, 50, 70, 144, 222 nebo 432 MHz: používá se pro zisk a lalok antény, odhad toku a energetickou bilanci spoje. |
| **Vypočítat** | Přepočítá trasu (vzorkování vrstvy E: několik sekund). |
| **Az antény** | Nahoře v rámečku protistanice, vedle mapy: azimut vaší antény, vždy **na DX** (azimut trasy). Pod ním, ve stejném sloupci, je legenda mapy. |

**Řada 1 – vrstva E a anténa**

| Ovládací prvek | Co dělá |
|---|---|
| **Výška stop km** + **z radaru** | Výška meteorických stop (výchozí 90 km). Při zaškrtnutí *z radaru* se použije nejčastější výška (modus) naměřená radarem v Collmu; viz [Tok z radaru](Radar-Flux-cs). |
| **Elevace laloku °** | Elevace maxima svislého laloku tvé antény: směrovka upevněná na 0° má kvůli odrazu od země přesto lalok několik stupňů nad obzorem (obvykle 3-8°). Při zapnutém políčku **diagram antény** (výchozí) se body vrstvy E váží svislým diagramem obou antén; při vypnutém se použijí jen body, které obě stanice vidí nad touto elevací. |
| **Anténa Yagi: ráhno m** | Délka ráhna vaší Yagi. Program zobrazí délku v λ, zisk (křivka DL6WU) a lalok −3 dB, vodorovný i svislý; viz [Geometrie a útlum](Geometry-and-Path-Loss-cs#zisk-a-lalok-antény). Pod 2 λ je odhad hrubý. |
| **Hot spot od středu trasy km** + **auto (AMS)** | Vzdálenost Hot A a Hot B od středu trasy. Při zaškrtnutí *auto (AMS)* (výchozí) se řídí tabulkou odklonu antény od J. Richardsona (AMS), kterou cituje DJ5HG: 13° při 1000 km, 11° při 1250 km, 10° při 1500 a 2000 km (asi 115, 121, 132 a 176 km od středu). Po zrušení zaškrtnutí zadáte ručně 30–400 km (MSHV používá 150 km). |

**Řada 2 – čas**

| Ovládací prvek | Co dělá |
|---|---|
| **Čas** | Hodiny UTC. |
| **Datum výpočtu (UTC)** | Den výpočtu pro [Předpovědní výpočet](Sky-View-cs) a [Radar GRAVES](GRAVES-Radar-cs) (výchozí dnes), v aktuální denní době. Také: den zobrazený ve [Výpočtu účinnosti](Efficiency-Calculation-cs) a na časové ose GRAVES. |
| **Hodiny (od −12 do +36 h)** | Posouvá okamžik výpočtu od 12 hodin před do 36 hodin po tomto čase, v krocích po 15 minutách. Vedle je *Výpočet pro: nyní* nebo *Výpočet pro: dd/mm hh:mm UTC*. |
| **Reálný čas** | Návrat na současnost. |

## 2. Vaše stanice a DX

1. Zadejte **Můj lokátor** a **výška m**.
2. Zadejte lokátor a výšku **protistanice** – nebo klikněte do mapy na kartě [Nebeská klenba](Sky-View-cs): **levé kliknutí = lokátor protistanice**, **pravé kliknutí = lokátor mé stanice**.
3. Zvolte **Pásmo MHz** a stiskněte **Vypočítat**.

Stavový řádek dole potvrdí: *Trasa vypočtena: … km, … bodů odrazu vzorkováno za … s*.

## 3. Vaše anténa

Zadejte **délku ráhna** vaší Yagi. Program z ní odvodí zisk a lalok a upozorní vás, pokud Hot A nebo Hot B leží již **uvnitř laloku**, když anténa míří na DX (pak se kreslí šedě: anténu není třeba otáčet).

## 4. Čtení výsledků

| Otázka | Kde hledat |
|---|---|
| Který roj teď pomáhá mé trase a z které strany? | [Nebeská klenba](Sky-View-cs): seznam rojů, doporučený Hot červeně, zóny PREV |
| Která hodina je dnes nejlepší? | [Výpočet účinnosti](Efficiency-Calculation-cs): přehledové karty a hodinová tabulka |
| Kolik meteorů radar počítá? | [Tok z radaru](Radar-Flux-cs) |
| Kolik pingů mohu čekat na 144 MHz? | [Experimentální předpovědi](Experimental-Forecasts-cs) (experimentální) |
| Zvládne moje stanice trasu? | [Geometrie a útlum](Geometry-and-Path-Loss-cs): útlum trasy a rezerva |
| Kdy je příští maximum? | [Roje](Showers-cs) |
| Mohu zkoušet s GRAVES? | [Radar GRAVES](GRAVES-Radar-cs) |

## Praktická pravidla (ze zdrojů)

- **Miřte kolmo na roj**: nejlepší trasa je kolmá na azimut radiantu; nejlepší směr = azimut radiantu ±90°, tolerance ±40–50° (SM6FHZ).
- **Side-scatter**: natočte anténu o 10–30° ke straně (A nebo B), ze které přichází většina odrazů (článek Cerrotta–Sartori).
- **Příliš vysoký radiant** (nad 70°) nebo příliš nízký (pod 20°) dává málo užitečných stop (DF5HC, DH9GCD).
- Sporadické meteory mají maximum kolem **06 UTC** (článek; potvrzeno tokem z Collmu).
- Užitečné vzdálenosti na 432 MHz: 800–2000 km, nejlépe asi 1400 km (SM6FHZ); obecně nejlepší vzdálenost 1300–1500 km (DF5HC).

Dále: [Nebeská klenba](Sky-View-cs).
