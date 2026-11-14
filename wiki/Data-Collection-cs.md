[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · **Čeština** · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Sběr dat

*Karta: Živě a data v reálném čase › Sběr dat.*

[![Sběr dat](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Čtyři zdroje

Karta sbírá **spoty meteor scatter** ze tří telnetových proudů a z MQTT kanálu PSKReporter, každý ve vlastní podkartě:

| Podkarta | Výchozí | Poznámky |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Cluster podle vašeho výběru. Na ON0DXK jsou pásma VHF filtrována: povolte je příkazem `set/filter dxbm/pass 6` (pak 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmery dekódují MS druhy provozu jen zřídka. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X přenášející spoty **PSKReporter**: sem přicházejí dekódování MSK144 z WSJT-X a MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Živé spoty PSKReporter přes **MQTT** (služba od M0LTE): bez přihlášení, každý spot už nese lokátory vysílající i přijímající stanice. Výchozí témata: MSK144 na 6 m, 4 m, 2 m, 1,25 m, 70 cm a FSK441 na 2 m (`pskr/filter/v2/band/mode/#`); *Výchozí témata* je obnoví. |
| **5. WSJT-X / JTDX / MSHV přes UDP** | 127.0.0.1 : 2237 → 2238 | Jako v LIVETROPOVHF: program poslouchá UDP zprávy digitálního programu (ve WSJT-X: Nastavení, Reporting, UDP Server 127.0.0.1 port 2237) a opakuje je beze změny na přeposílacím portu pro ostatní programy (GridTracker, JTAlert, deník). Každá dekódovaná stanice se stane spotem slyšeným tvou stanicí; závěrečné zprávy (RR73, 73, RRR) mezi dvěma jinými stanicemi se stanou trasou jejich QSO. Spoty procházejí stejnými filtry jako ostatní. |
| **Sebrané spoty MS** | – | Tabulka přijatých spotů, nejnovější nahoře. |

Každý proud má hostitele, port, příkazy odesílané po přihlášení, *Znovu připojit*, *Připojit při spuštění*, konzoli a řádek pro odesílání příkazů. Nahoře zadejte svou **značku pro přihlášení**. Zdroj MQTT má hostitele, port, témata (jedno na řádek nebo oddělená `;`), *Znovu připojit* a *Připojit při spuštění* (ve výchozím stavu vypnuto) a konzoli s přijatými spoty; jeho spoty procházejí stejným filtrem. Pruh ukazuje stav čtyř zdrojů (zelená tečka = připojeno). Relace zůstávají otevřené i při změně jazyka nebo barevného schématu.

## Filtr (40 % okna)

- **Volitelný místní filtr:** řádky clusteru pod **27990,0 kHz** se okamžitě zahodí (nezobrazí se ani neuloží).
- Spoty CW se hned zahazují (CW nebo WPM v komentáři, nebo 28000-28070 kHz): neobjeví se v konzoli a neukládají se, pokud nejsou označené <MS>. Políčko lze vypnout.

Databáze CALL3 s pravidly LIVETROPOVHF. „Aktualizovat teď" stáhne CALL3.TXT z MMMonVHF (aspoň 100 000 platných řádků, předchozí zůstane v data/call3.bak); s volbou „Aktualizovat samo každých 7 dní" se to děje při spuštění. Nad souborem platí v pořadí: ruční záznamy (data/CALL3-MANUALE.TXT), opravy z clusteru (6místný lokátor, který spotující uvádí o sobě), přidané soubory (data/CALL3-AGGIUNTE), pak CALL3.TXT a 6místné lokátory naučené naživo (data/LOC6.TXT). Přijatý 4místný lokátor nebo končící na LL či MM se nahradí 6místným z databáze; přenosné stanice (s lomítkem) jen přesným záznamem.

Poslední zdroj, jako v LIVETROPOVHF: pro značky, které v žádném jiném zdroji nemají 6místný lokátor, se program automaticky každých 6 hodin ptá veřejného API G7VRD (api.g7vrd.co.uk), po skupinách 40 značek; každou značku nejvýš jednou denně. Přijme se jen 6místný lokátor, ne střed čtverce (LL nebo MM), ve stejném čtverci jako přijatý. Výsledky jsou v data/CALL3-G7VRD.TXT a jako všechny opravy se zapisují i do data/call3.txt.
- Spoty mezi stanicemi bližšími než 500 km se okamžitě zahazují, protože na tuto vzdálenost je spojení přímé nebo troposférické, nikoli meteor scatter: neobjeví se v konzoli a neukládají se. Chybí-li lokátor, spot zůstane. Vzdálenost se mění pod zaškrtávacím políčkem.
- **1. kritérium – typické frekvence MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot v těchto oknech se přijme i bez názvu druhu provozu, pokud komentář neuvádí jiné šíření: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Okna i značky lze upravit.
- **2. kritérium – druhy provozu MS:** mimo okna nebo s některou z těchto značek se spot ponechá, jen pokud obsahuje **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (digitální druhy provozu používané jen pro MS) nebo **\<MS\>**, velkými, malými či smíšenými písmeny. Slova lze vypnout, přidat i odebrat; každé má své počítadlo.
- **Pásma** 28, 50, 70, 144, 222, 432 MHz; **test filtru** na vloženém řádku; **počítadla**.

## Lokátory a ukládání

Chybějící lokátory nebo lokátory jen se 4 znaky se doplní z archivu **CALL3** (`data/call3.txt`, soubor JTDX, přes milion značek), který má vždy přednost před 4znakovým lokátorem. Přijaté spoty se ukládají do `data/spot_ms`, jeden soubor CSV na den, a plní mapu [Provoz živě](Live-Traffic-cs).
