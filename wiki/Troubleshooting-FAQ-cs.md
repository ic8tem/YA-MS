[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · **Čeština** · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Řešení problémů a FAQ

## Instalace a spuštění

### Windows SmartScreen hlásí „Systém Windows ochránil váš počítač“
Program není podepsán komerčním certifikátem. Klikněte na *Další informace* → *Přesto spustit*. Stahujte ho jen ze stránky [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: nelze otevřít, protože pochází od neidentifikovaného vývojáře
YA-MS není podepsán společností Apple, proto ho **Gatekeeper** poprvé zablokuje. V `.dmg` **klikněte pravým tlačítkem na „Installa YA-MS.command“ → Otevřít** a potvrďte. Skript odstraní z `~/YA-MS/YA-MS.app` karanténní příznak „staženo z internetu“ a aplikaci otevře. Pokud ji macOS stále odmítá, otevřete *Nastavení systému → Soukromí a zabezpečení* a stiskněte *Přesto otevřít*.

### macOS: který .dmg?
`-mac-apple-silicon.dmg` pro procesory M1/M2/M3/M4, `-mac-intel.dmg` pro Macy s procesorem Intel (nabídka Apple → *O tomto Macu* vám řekne, který máte).

### Linux: YA-MS není v nabídce aplikací
Spusťte `./installa.sh` z rozbalené složky (ne z `~/YA-MS`). Některá prostředí potřebují odhlášení a nové přihlášení, aby zobrazila nové položky. Vždy ho můžete spustit pomocí `~/YA-MS/YA-MS`.

### Chybí mapa Evropy
*Mapa Evropy není k dispozici (při prvním spuštění je potřeba síť).* Mapa Natural Earth se při prvním spuštění stáhne do `data/mappa`. Připojte se k internetu a spusťte YA-MS znovu.

## Zobrazení

### Linux: japonský text se zobrazuje jako čtverečky
Vašemu systému chybí písma CJK (čínština, japonština, korejština). Nainstalujte písma **Noto CJK** a spusťte YA-MS znovu. Totéž platí pro arabštinu, hebrejštinu, urdštinu, hindštinu a bengálštinu: v systémech Debian, Ubuntu a Raspberry Pi OS nainstalujte také `fonts-noto-core`.

| Distribuce | Příkaz |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Text je příliš malý nebo grafy nemají místo
Použijte posuvník **Písmo** (85–140 %) a skryjte řady ovládacích prvků tlačítkem **Ovládání**. Viz [Nastavení](Settings-and-Data-Folder-cs#písmo-a-ovládání).

### Obrazovka je v noci příliš jasná
V seznamu **Motiv** zvolte **Noc** nebo **Černý**.

## Internet a radarová data

### Zpráva „Chybí připojení k internetu“
YA-MS ji zobrazí **jednou**, když není dostupný žádný zdroj; stavový řádek zčervená. Program dál pracuje s **naposledy uloženými daty** a sám to zkouší znovu každých 5 minut; po obnovení sítě se objeví *Připojení obnoveno.* Nemusíte nic dělat.

### Oranžové varování na kartě Tok z radaru: „Nelze přečíst svislé měřítko toku …“
Radar v Collmu každý den mění svislou stupnici a YA-MS ji čte z popisků grafu. Pokud popisek nelze přečíst, program použije kalibrovanou stupnici 0–1200 meteorů/hodinu a upozorní, že **hodnoty je třeba ověřit**. Obvykle se další hodinový graf přečte správně. Pokud po mnoho hodin vidíte *Formát grafu se změnil* nebo *Osy toku nebyly nalezeny v očekávané poloze*, radar změnil formát grafu: prosím [nahlaste to](Contributing-and-Contacts-cs).

### „Měřítko grafu výšek se změnilo“
Statistiky výšek (modus, průměr, medián) zůstávají platné; neplatí jen absolutní počty v histogramu výšek.

### „Tok z radaru: žádná data“
Stiskněte **Stáhnout nyní** na kartě [Tok z radaru](Radar-Flux-cs) a zkontrolujte, že `data/fonti_radar.csv` má pro Collm `attivo=1`.

### RMOB: proč je automatické stahování vypnuté?
RMOB žádá, aby **automatické programy jeho soubory nestahovaly**. *Automatické stahování každých 5 minut* zapněte až poté, co vám RMOB dá svolení. Mezitím používejte **Stáhnout RMOB nyní** nebo **Načíst soubor RMOB z disku...**. Viz [Experimentální předpovědi](Experimental-Forecasts-cs#rmob-a-automatické-programy).

### RMOB: „Formát souboru nebyl rozpoznán“ nebo načteno málo hodin
Použijte měsíční textový soubor pozorovatele (`NAME_MMYYYYrmob.TXT`) nebo tabulku z bulletinu s jediným pozorovatelem. Proložení exponentu potřebuje alespoň 3 hodiny společné s daty z Collmu (včera a dnes).

## Výpočty

### „Neplatný lokátor stanice“ / „Neplatný lokátor protistanice“
Lokátory musí mít 4, 6 nebo 8 znaků (např. `JN70`, `JN70CN`, `JN70CN12`).

### „Žádná společná zóna vrstvy E“
Trasa je delší než dvojnásobek dosahu ve výšce stop (asi 2 × 1062 km při laloku 0° a stopách v 89,5 km): jeden skok meteor scatter ji nepokryje. Zvýšení **Elevace laloku** dosah dále zkracuje.

### Hot A / Hot B jsou šedé
Leží již **uvnitř laloku vaší antény**, když míří na DX: není třeba otáčet. Viz [Nebeská klenba](Sky-View-cs#varování).

### Účinnost se liší od MCG_MS nebo MS-Soft
YA-MS používá skutečnou trasu a vlastní model; stupnice OH5IY a MCG_MS není podrobně zdokumentována. Porovnávejte spíše hodiny a trendy než absolutní procenta a podívejte se na [model](Efficiency-Calculation-cs#model).

### Průchod svazku GRAVES se zdá posunutý
Sekvence svazku se počítá z hodin PC: synchronizujte je se serverem NTP. Řídicí stanice GRAVES také občas posune sekvenci o několik kroků; detail je předpověď, kterou je třeba potvrdit poslechem.

## Další otázky

**Je YA-MS zdarma?** Ano, je to bezplatný program pro radioamatéry.

**Ovládá můj rotátor nebo rádio?** Ne. YA-MS je nástroj pro předpověď a plánování; pro QSO použijte svůj program pro digitální druhy provozu (např. MSHV, WSJT-X).

**Funguje nad 432 MHz?** Seznam pásem končí na 432 MHz (28, 50, 70, 144, 222, 432). Experimentální předpověď přijímá libovolnou frekvenci od 28 do 1300 MHz, ale pravidla SM6FHZ, která používá, vycházejí ze zkušeností na 144 a 432 MHz.

**Něco se pokazilo.** Napište autorovi s uvedením operačního systému, verze YA-MS a toho, co jste dělali: viz [Spolupráce a kontakty](Contributing-and-Contacts-cs).
