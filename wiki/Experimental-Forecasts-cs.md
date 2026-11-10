[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · **Čeština** · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Experimentální předpovědi

*Karta: Výpočet předpovědi › Experimentální předpovědi.*

[![Experimentální předpovědi](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Tato karta převádí počty meteorů z **radaru v Collmu (36,2 MHz)** na odhad **odrazů za hodinu na radioamatérském pásmu** (výchozí 144 MHz, libovolný kmitočet od 28 do 1300 MHz), předpovídá **příštích 24 hodin** pro vaši trasu a umožňuje **porovnat** odhad s pozorovatelem **RMOB** – například s tím, kdo poslouchá GRAVES na 143,050 MHz.

> Vše zde je **experimentální**: kmitočtové pravidlo je empirické a faktor stanice závisí na vaší stanici. Čísla používejte k porovnání hodin a dnů a ověřujte je na pásmu.

## Ovládání

| Ovládací prvek | Výchozí | Co dělá |
|---|---|---|
| **Cílový kmitočet MHz** | 144 | Kmitočet předpovědi (28–1300 MHz) |
| **Exponent λ^k** | 3 | Exponent k kmitočtového pravidla (SM6FHZ: 3) |
| **Faktor stanice K** | 1 | Zohledňuje přijímací stanici (výkon, antény); odvozuje se srovnáním s pozorovatelem RMOB na stejném pásmu |
| **Načíst soubor RMOB z disku...** | | Načte měsíční textový soubor RMOB (viz níže) |
| **Odvodit exponent ze souboru RMOB** | | Odvodí k ze společných hodin Collmu a RMOB |
| **Pozorovatel RMOB** | prázdné | Jméno pozorovatele, jak se objevuje v názvu souboru (např. `NAME_112026rmob.TXT` → `NAME`) |
| **Stáhnout RMOB nyní** | | Jednorázově stáhne soubor aktuálního měsíce tohoto pozorovatele |
| **automatické stahování každých 5 minut (povolte jen se svolením RMOB)** | **vypnuto** | Viz [RMOB a automatické programy](#rmob-a-automatické-programy) |

Oranžový řádek pod ovládacími prvky ukazuje pravidlo s aktuálními čísly, např. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, přepočet trvání a maximální ping IARU na daném kmitočtu.

## Z radaru na radioamatérské pásmo

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Zdroj:** SM6FHZ, *„432 MHz Meteorscatter, Challenges and Techniques“*, 45. Nordic VUSHF, květen 2025 – počet a intenzita odrazů se mění s **λ³**, trvání s **λ²** (432 MHz je o 14–15 dB pod 144 MHz a trvá 1/9). **Ověření:** závislost na λ³ je stejná jako v McKinleyho rovnici pro podhusté stopy. Při k = 3 se z 1000 meteorů/hodinu v Collmu stane asi **16 odrazů/hodinu na 144 MHz**; pozorovatelé RMOB poslouchající GRAVES na 143,050 MHz obvykle počítají **20 až 140 ech/hodinu** (bulletin RMOB, červen 2018): řád je slučitelný a rozdíl tvoří faktor stanice K. (Rov. 44–45 příručky.)

## Příštích 24 hodin

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Perzistence:** přepočtená hodnota stejné hodiny předchozího dne (nebo dva dny zpět, pokud chybí), opravená o změnu **indexu rojů trasy** I (Σ ZHR × účinnost, viz [Výpočet účinnosti](Efficiency-Calculation-cs#model)). Konstanta 10 představuje sporadické pozadí a omezuje korekci, když je index malý. *Volba programu (rov. 47 příručky).*

| Panel | Obsah |
|---|---|
| **Změřeno v Collmu a přepočteno na f MHz – včera a dnes (UTC)** | Meteory/hodinu z radaru v Collmu; přepočtené hodnoty (oranžově, pravá stupnice); počty RMOB, pokud jsou načteny (zeleně, pravá stupnice) |
| **Experimentální předpověď na příštích 24 hodin na f MHz pro …** | Předpovídané odrazy/hodinu (sloupce) a index rojů trasy (pravá stupnice) |
| Tabulka | Čas UTC · Collm ve stejnou hodinu · Přepočteno · Index rojů trasy · Předpověď /hodinu · **Hodnocení** |

**Hodnocení:** *dobrá*, když je předpověď alespoň 1,3 × průměr za 24 hodin, *průměrná* od 0,8 ×, *slabá* pod tím. Stejná předpověď se objevuje v kartě **EXPERIMENTÁLNÍ PŘEDPOVĚĎ** a v oranžovém řádku [Výpočtu účinnosti](Efficiency-Calculation-cs) a je základem očekávaných ech na kartě [Radar GRAVES](GRAVES-Radar-cs#očekávaná-echa-experimentální).

## Srovnání s RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) shromažďuje hodinové počty meteorů od radiových pozorovatelů; mnozí v Itálii poslouchají GRAVES na 143,050 MHz (planetárium v Benátkách, Faenza, Rovereto a další).

**Čtení souborů RMOB.** Přijímají se dva textové formáty:

| Formát | Vzhled | Poznámky |
|---|---|---|
| Měsíční soubor (Colorgramme / Spectrum Lab) | jeden řádek na den, `day| n| n| …` s 24 hodinovými hodnotami | obvyklý `NAME_MMYYYYrmob.TXT` |
| Tabulka z bulletinu | záhlaví ` UT |  1   2   3 …`, řádky `0h|175 166 …` | pokud soubor obsahuje více pozorovatelů, čtou se jeden po druhém: použijte soubor s jediným pozorovatelem |

Měsíc a rok se berou z názvu souboru (`…_MMYYYYrmob…`) nebo ze záhlaví; jinak se použije aktuální měsíc (a program to oznámí).

**Odvození exponentu.** Při K = 1 z mediánu poměrů RMOB/Collm přes společné hodiny (alespoň 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Volba programu (rov. 46 příručky).* Dialog ukáže společné hodiny, mediánový poměr a k; **Ano** použije k (a nastaví K = 1), **Ne** ponechá k = 3 – pak ručně upravte K na hodnotu navrženou ve stejném dialogu.

## RMOB a automatické programy

RMOB žádá, aby **automatické programy jeho soubory nestahovaly**. Proto je **automatické stahování** po spuštění **vypnuto** a mělo by se zapnout **až po požádání RMOB o svolení**. Bez něj můžete vždy použít **Načíst soubor RMOB z disku...** nebo stisknout **Stáhnout RMOB nyní**, když to potřebujete.

Adresa pro stahování je šablona v `config.ini` (klíč `rmob_url`, výchozí `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kde `{NOME}` je pozorovatel a `{MMAAAA}` měsíc a rok); stažené soubory se ukládají do `data/radar/`.
