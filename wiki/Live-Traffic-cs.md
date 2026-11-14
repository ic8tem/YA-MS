[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · **Čeština** · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Provoz živě

*Karta: Živě a data v reálném čase › Provoz živě.*

[![Provoz živě](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Co zobrazuje

**Azimutální ekvidistantní mapu** se středem ve vaší stanici (vzdálenost od středu = skutečná vzdálenost, úhel = azimut) s **veškerým provozem meteor scatter**, který shromáždila karta [Sběr dat](Data-Collection-cs). Pro každé spojení program kreslí:

- **trasu** mezi oběma stanicemi v barvě jejího pásma: 28 MHz hnědá, 50 MHz zelená, 70 MHz azurová, 144 MHz oranžová, 222 MHz růžová, 432 MHz fialová;
- obě **stanice** na koncích trasy;
- **zóna roje**: kde se soustřeďují nejpravděpodobnější meteorické stopy pro danou trasu a daný čas.

Spoty se stanicí **mimo mapu** se zahazují. Spot, který **právě přišel** (ne starší než 3 minuty), **bliká po dobu jedné minuty**, takže nová aktivita je vidět na první pohled.

Ukázat, kdo poslouchá: trojúhelníky v barvě pásma označují stanice, které podle PSKReporteru ve zvoleném časovém okně přijímají MSK144, FSK441, PSK2K nebo JTMS na 28, 50, 70, 144 a 432 MHz. Klepnutí na trojúhelník ukáže značku, lokátor, druhy provozu a poslední spot. Proud MQTT na kartě Sběr dat musí být připojen.

Také aktivní monitory z mapy PSKReporter: prázdné trojúhelníky pro stanice, které jsou na mapě pskreporter.info v MSK144, FSK441, PSK2K nebo JTMS, ale ještě nepřijaly žádný spot (MQTT posílá jen stanice, které něco přijímají). YA-MS se dotazuje vyhledávací služby PSKReporter jednou za 5 minut pro všechny druhy provozu, jak žádají pravidla služby; monitor zůstává na mapě nejméně 11 minut. Klepnutí na trojúhelník ukáže značku, lokátor, dekódovací program a čas, kdy byl monitor aktivní. Ve výchozím stavu zapnuto.

FT8 nad 1100 km bez souběžných tras: spot FT8 (z PSKReporter MQTT, z clusterů nebo z WSJT-X přes UDP) mezi stanicemi vzdálenými více než 1100 km, který 3 minuty před a po nemá souběžné trasy (stejné pásmo, střed do 300 km, směr do 15°, jiná dvojice stanic), se kreslí světle zeleně a jeho řádek v tabulce vpravo dole stále bliká. Sporadická E a tropo dávají mnoho blízkých souběžných tras; osamocený spot může být meteorická stopa. Proto YA-MS přijímá z MQTT i spoty FT8 z pásem 6 m, 4 m, 2 m, 1,25 m a 70 cm (nikdy 28 MHz, v žádném případě). Tyto spoty se neukládají do archivu MS. Ve výchozím stavu zapnuto.

Spoty WSJT-X přes UDP, které se týkají vaší stanice (dekódování obsahuje vaši značku: kdo vás volá nebo vám odpovídá), se kreslí stále blikající přerušovanou čarou, v jakémkoli druhu provozu a na jakoukoli vzdálenost.

Výměna mezi uživateli YA-MS: když jiný uživatel YA-MS dekóduje přes UDP zprávu určenou vaší stanici (v MSK144, FSK441, PSK2K nebo JTMS, nebo v FT8 nad 1100 km), jeho YA-MS vám ji pošle zašifrovanou přes tři veřejné MQTT brokery (HiveMQ, Mosquitto, EMQX); uvidíte ji jako fialovou přerušovanou čáru, která stále bliká, a jako řádek v konzoli UDP. Přečíst ji můžete jen vy (klíče ECDH P-256, AES-256 a HMAC-SHA256). Spoty FT8 se ukazují, jen pokud během 3 minut nemají souběžné trasy. Ve výchozím stavu zapnuto; yams_scambio=0 v data/config.ini vypne.

Na mapě se píší značky obou stanic každého spotu, jednou pro každou stanici. Projekci lze zvolit: azimutální (uprostřed tvoje stanice) nebo Mercatorova. Bublina na sloupci Mrak vysvětluje jeho význam.

Zobrazují se spoty všech pásem, i těch, která nejsou vybrána ve Sběru dat (ty se neukládají). Spoty CW a spoty mezi příliš blízkými stanicemi se nezobrazují, pokud se ve Sběru dat zahazují.

## Jak se počítá zóna roje

Pro každý spot program sestaví trasu mezi oběma lokátory (stejná geometrie jako pro vaši vlastní trasu, viz [Geometrie a útlum](Geometry-and-Path-Loss-cs)) a v čase spotu sečte bod po bodu vrstvy E **příspěvky zrcadlového odrazu všech aktivních rojů**, vážené jejich ZHR – stejný výpočet jako u **zón PREV** na [nebeské klenbě](Sky-View-cs). Pro každou stranu trasy, která drží alespoň 15 % celku, je zóna roje **elipsa**: střed ve váženém průměru bodů, poloosy 1,5násobek odmocnin vlastních čísel jejich rozptylu, hlavní osa podél hlavního vlastního vektoru. Když žádný roj nepřispívá (jen sporadické meteory), jsou zóna roje dvěma klasickými **hot spoty**, kreslenými čárkovaně. Úplné rovnice jsou v kapitole 10 manuálu výpočtů.

## Ovládací prvky

| Ovládací prvek | Význam |
|---|---|
| **Poloměr mapy** | 600–3500 km od vaší stanice. |
| **Spoty k zobrazení** | Posledních 15 nebo 30 minut, poslední hodina, poslední 3 hodiny, posledních 24 hodin. |
| **Tabulka** | Spojení na mapě, nejnovější nahoře, v barvě pásma; *% roje* udává podíl odrazů na hlavní straně, případně *sporadické*. |
| **Kliknutí** | Na trasu nebo řádek tabulky: spojení se zvýrazní a rámeček ukáže lokátor středu zóna roje, jeho podíl, velikost a osu. |
