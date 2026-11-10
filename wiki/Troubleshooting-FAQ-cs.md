LANGBAR

# Řešení problémů a FAQ

## Instalace a spuštění

### Windows SmartScreen hlásí „Systém Windows ochránil váš počítač“
Program není podepsán komerčním certifikátem. Klikněte na *Další informace* → *Přesto spustit*. Stahujte ho jen ze stránky [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: program nelze otevřít, protože je od neidentifikovaného vývojáře
YA-MS není podepsán společností Apple, takže ho **Gatekeeper** napoprvé zablokuje. V `.dmg` **klikněte pravým tlačítkem na „Installa YA-MS.command“ → Otevřít** a potvrďte. Skript odstraní z `~/YA-MS/YA-MS.app` karanténní příznak „staženo z internetu“ a otevře ho. Pokud macOS stále odmítá, otevřete *Nastavení systému → Soukromí a zabezpečení* a stiskněte *Přesto otevřít*.

### macOS: který .dmg?
`-mac-apple-silicon.dmg` pro procesory M1/M2/M3/M4, `-mac-intel.dmg` pro Macy s procesorem Intel (který máte, zjistíte v nabídce Apple → *O tomto Macu*).

### Linux: YA-MS chybí v nabídce aplikací
Spusťte `./installa.sh` z rozbalené složky (ne z `~/YA-MS`). Některá desktopová prostředí potřebují k zobrazení nových položek odhlášení a přihlášení. Program lze vždy spustit příkazem `~/YA-MS/YA-MS`.

### Chybí mapa Evropy
*Mapa Evropy není k dispozici (při prvním spuštění je potřeba síť).* Mapa Natural Earth se stáhne do `data/mappa` při prvním spuštění. Připojte se k internetu a YA-MS restartujte.

## Zobrazení

### Linux: japonský text se zobrazuje jako čtverečky
Vašemu systému chybí písma CJK. Nainstalujte písma **Noto CJK** a YA-MS restartujte:

| Distribuce | Příkaz |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Text je příliš malý nebo grafy nemají místo
Použijte posuvník **Písmo** (100–300 %) a sbalte řady tlačítkem **Ovládání**. Viz [Nastavení](Settings-and-Data-Folder-cs#písmo-a-ovládání).

### Obrazovka je v noci příliš jasná
V seznamu **Motiv** zvolte **Noc** nebo **Černé**.

## Internet a data radarů

### Zpráva „Žádné připojení k internetu“
YA-MS ji zobrazí **jednou**, když nelze dosáhnout žádného zdroje; stavový řádek zčervená. Program pracuje dál s **posledními uloženými daty** a sám to zkouší znovu každých 5 minut; když je síť zpět, objeví se *Připojení obnoveno.* Není třeba nic dělat.

### Oranžové upozornění na kartě Tok z radaru: „Nelze přečíst svislou stupnici toku …“
Radar v Collmu mění svislou stupnici každý den a YA-MS ji čte z popisků grafu. Pokud popisek nelze přečíst, program použije kalibrovanou stupnici 0–1200 meteorů/hodinu a upozorní, že **hodnoty je třeba zkontrolovat**. Obvykle se další hodinový graf přečte správně. Pokud po mnoho hodin vidíte *Formát grafu se změnil* nebo *Osy toku nenalezeny na očekávaném místě*, radar změnil formát grafu: [nahlaste to](Contributing-and-Contacts-cs) prosím.

### „Měřítko grafu výšek se změnilo“
Statistiky výšek (modus, průměr, medián) zůstávají platné; neplatí jen absolutní počty histogramu výšek.

### „Tok z radaru: žádná data“
Stiskněte **Stáhnout nyní** na kartě [Tok z radaru](Radar-Flux-cs) a zkontrolujte, že `data/fonti_radar.csv` má u Collmu `attivo=1`.

### RMOB: proč je automatické stahování vypnuto?
RMOB žádá, aby **automatické programy jeho soubory nestahovaly**. Volbu *automatické stahování každých 5 minut* zapněte až poté, co vám RMOB dá svolení. Mezitím používejte **Stáhnout RMOB nyní** nebo **Načíst soubor RMOB z disku...**. Viz [Experimentální předpovědi](Experimental-Forecasts-cs#rmob-a-automatické-programy).

### RMOB: „Formát souboru nerozpoznán.“ nebo načteno málo hodin
Použijte měsíční textový soubor pozorovatele (`NAME_MMYYYYrmob.TXT`) nebo tabulku z bulletinu s jediným pozorovatelem. Odvození exponentu potřebuje alespoň 3 hodiny společné s daty z Collmu (včera a dnes).

## Výpočty

### „Neplatný lokátor stanice“ / „Neplatný lokátor stanice DX“
Lokátory musí mít 4, 6 nebo 8 znaků (např. `JN70`, `JN70CN`, `JN70CN12`).

### „Žádná společná zóna vrstvy E“
Trasa je delší než dvojnásobek dosahu ve výšce stopy (asi 2 × 1062 km s lalokem na 0° a stopami ve výšce 89,5 km): jeden skok meteor scatter ji nemůže pokrýt. Zvýšení **Elevace laloku** dosah dále zkracuje.

### Hot A / Hot B jsou šedé
Při směrování na DX už leží **uvnitř laloku vaší antény**: není třeba otáčet. Viz [Nebeská klenba](Sky-View-cs#upozornění).

### Účinnost se liší od MCG_MS nebo MS-Soft
YA-MS používá skutečnou trasu a vlastní model; stupnice OH5IY a MCG_MS není podrobně zdokumentována. Porovnávejte spíše hodiny a trendy než absolutní procenta a podívejte se na [model](Efficiency-Calculation-cs#model).

### Průchod svazku GRAVES se zdá posunutý
Sekvence svazku se počítá z hodin PC: synchronizujte je se serverem NTP. Řídicí stanice GRAVES navíc občas posune sekvenci o několik kroků; podrobnosti jsou předpovědí, kterou je třeba potvrdit poslechem.

## Další otázky

**Je YA-MS zdarma?** Ano, je to bezplatný program pro radioamatéry.

**Ovládá můj rotátor nebo rádio?** Ne. YA-MS je nástroj pro předpovědi a plánování; pro QSO použijte svůj program pro digitální druhy provozu (např. MSHV, WSJT-X).

**Funguje nad 432 MHz?** Seznam pásem končí na 432 MHz (28, 50, 70, 144, 222, 432). Experimentální předpověď přijímá libovolný kmitočet od 28 do 1300 MHz, ale pravidla SM6FHZ, která používá, vycházejí ze zkušeností na 144 a 432 MHz.

**Něco se pokazilo.** Napište autorovi s uvedením operačního systému, verze YA-MS a toho, co jste udělali: viz [Přispívání a kontakty](Contributing-and-Contacts-cs).
