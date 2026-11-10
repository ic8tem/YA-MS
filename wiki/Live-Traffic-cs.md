[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · **Čeština** · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [ไทย](Live-Traffic-th) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Živý provoz

*Karta: Živá data a data v reálném čase › Živý provoz.*

[![Živý provoz](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Co zobrazuje

**Azimutální ekvidistantní mapa** se středem ve vaší stanici (vzdálenost od středu = skutečná vzdálenost, úhel = azimut) s **veškerým provozem meteor scatter** shromážděným na kartě [Sběr dat](Data-Collection-cs). Pro každé spojení program vykreslí:

- **trasu** mezi oběma stanicemi v barvě jejího pásma: 28 MHz hnědá, 50 MHz zelená, 70 MHz azurová, 144 MHz oranžová, 222 MHz růžová, 432 MHz fialová;
- obě **stanice** na koncích trasy;
- **oblak**: kde se soustřeďují nejpravděpodobnější meteorické stopy pro danou trasu a daný čas.

Spoty se stanicí **mimo mapu** se zahazují. Spot, který **právě přišel** (ne starší než 3 minuty), **bliká po dobu jedné minuty**, takže nová aktivita je vidět na první pohled.

## Jak se počítá oblak

Pro každý spot program sestaví trasu mezi oběma lokátory (stejná geometrie jako pro vaši vlastní trasu, viz [Geometrie a útlum trasy](Geometry-and-Path-Loss-cs)) a v čase spotu sečte bod po bodu vrstvy E **příspěvky zrcadlového odrazu všech aktivních rojů**, vážené jejich ZHR – stejný výpočet jako u **zón PREV** v [nebeské klenbě](Sky-View-cs). Pro každou stranu trasy, která drží alespoň 15 % celku, je oblak **elipsa**: střed ve váženém průměru bodů, poloosy 1,5násobek odmocnin vlastních čísel jejich rozptylu, hlavní osa podél hlavního vlastního vektoru. Když žádný roj nepřispívá (jen sporadické meteory), jsou oblaky dvěma klasickými **hot spoty**, vykreslenými čárkovaně. Úplné rovnice jsou v kapitole 10 výpočetní příručky.

## Ovládání

| Ovládací prvek | Význam |
|---|---|
| **Poloměr mapy** | 600–3500 km od vaší stanice. |
| **Spoty k zobrazení** | Posledních 15 nebo 30 minut, poslední hodina, poslední 3 hodiny, posledních 24 hodin. |
| **Tabulka** | Spojení na mapě, nejnovější nahoře, v barvě pásma; *Oblak* udává podíl odrazů na hlavní straně, nebo *sporadické*. |
| **Kliknutí** | Na trasu nebo řádek tabulky: spojení se zvýrazní a rámeček ukáže lokátor středu oblaku, jeho podíl, velikost a osu. |
