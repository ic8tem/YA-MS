**English** · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Experimentální předpovědi

*Karta: Předpovědní výpočet › Experimentální předpovědi.*

[![Experimentální předpovědi](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Tato karta převádí počty meteorů z **radaru v Collmu (36,2 MHz)** na odhad **počtu odrazů za hodinu na radioamatérském pásmu** (výchozí 144 MHz, libovolná frekvence od 28 do 1300 MHz), předpovídá **příštích 24 hodin** pro vaši trasu a umožňuje **porovnat** odhad s pozorovatelem **RMOB** – například s tím, kdo poslouchá GRAVES na 143,050 MHz.

> Vše zde je **experimentální**: frekvenční pravidlo je empirické a faktor stanice závisí na vaší stanici. Čísla používejte k porovnávání hodin a dnů a ověřujte je na pásmu.

## Ovládací prvky

| Ovládací prvek | Výchozí | Co dělá |
|---|---|---|
| **Cílový kmitočet MHz** | 144 | Frekvence předpovědi (28–1300 MHz) |
| **Exponent λ^k** | 3 | Exponent k frekvenčního pravidla (SM6FHZ: 3) |
| **Faktor stanice K** | 1 | Zohledňuje přijímací stanici (výkon, antény); odvozuje se srovnáním s pozorovatelem RMOB na stejném pásmu |
| **Načíst soubor RMOB z disku...** | | Načte měsíční textový soubor RMOB (viz níže) |
| **Odvodit exponent ze souboru RMOB** | | Proloží k ze společných hodin Collmu a RMOB |
| **Pozorovatel RMOB** | prázdné | Jméno pozorovatele tak, jak se objevuje v názvu souboru (např. `NAME_112026rmob.TXT` → `NAME`) |
| **Stáhnout RMOB nyní** | | Jednou stáhne soubor daného pozorovatele za aktuální měsíc |
| **automatické stahování každých 5 minut (zapnout jen se svolením RMOB)** | **vypnuto** | Viz [RMOB a automatické programy](#rmob-a-automatické-programy) |

Oranžový řádek pod ovládacími prvky ukazuje pravidlo s aktuálními čísly, např. *N(144 MHz) = N(Collm 36,2 MHz) x (36,2/144)^3,00 x K = N x 0,01589 x 1,00*, přepočet délky a maximální ping podle IARU na dané frekvenci.

## Od radaru k radioamatérskému pásmu

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Zdroj:** SM6FHZ, *„432 MHz Meteorscatter, Challenges and Techniques“*, 45th Nordic VUSHF, květen 2025 – počet a intenzita odrazů se mění s **λ³**, délka s **λ²** (432 MHz je o 14–15 dB pod 144 MHz a trvá 1/9). **Ověření:** v McKinleyho rovnici je λ³ výkon jediné podhusté stopy, nikoli počet stop; pro hmotnostní index 2 se počet stop nad pevným prahem mění přibližně s λ^1,5 (IZ5TEK; OH5IY). Program ponechává k = 3, experimentální pravidlo SM6FHZ, a uvádí to; správné k pro vaši stanici vyplyne ze srovnání s RMOB. Při dopředném rozptylu roste délka také se sec²φ (McKinley; OH5IY): Collm měří ve zpětném rozptylu (φ = 0), proto předpověď násobí sec²φ ve středu trasy (×4 při 60°, ×8,5 při 70°, ×33 při 80°). S k = 3 se z 1000 meteorů/hodinu v Collmu stane asi **16 odrazů/hodinu na 144 MHz**; pozorovatelé RMOB poslouchající GRAVES na 143,050 MHz obvykle napočítají **20 až 140 ech/hodinu** (bulletin RMOB, červen 2018): řád velikosti je slučitelný a rozdíl tvoří faktor stanice K. (Manuál, rov. 44–45.)

## Příštích 24 hodin

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Perzistence:** přepočtená hodnota ze stejné hodiny předchozího dne (nebo dva dny zpět, pokud chybí), opravená změnou **indexu rojů trasy** I (Σ ZHR × účinnost, viz [Výpočet účinnosti](Efficiency-Calculation-cs#model)). Konstanta 10 představuje sporadické pozadí a omezuje korekci, když je index malý. *Volba programu (manuál, rov. 47).*

| Panel | Obsah |
|---|---|
| **Naměřeno v Collmu a přepočteno na f MHz – včera a dnes (UTC)** | Meteory/hodinu z radaru v Collmu; přepočtené hodnoty (oranžově, pravá stupnice); počty RMOB, pokud jsou načteny (zeleně, pravá stupnice) |
| **Experimentální předpověď na příštích 24 hodin na f MHz pro …** | Předpovídané odrazy/hodinu (sloupce) a index rojů trasy (pravá stupnice) |
| Tabulka | Čas UTC · Collm ve stejnou hodinu · Přepočteno · Index rojů trasy · Předpověď /hod · **Hodnocení** |

**Hodnocení:** *dobré*, když je předpověď alespoň 1,3 × průměr za 24 hodin, *ucházející* od 0,8 ×, *slabé* pod tím. Stejná předpověď se objevuje na přehledové kartě **EXPERIMENTÁLNÍ PŘEDPOVĚĎ** a v oranžovém řádku [Výpočtu účinnosti](Efficiency-Calculation-cs) a je základem očekávaných ech na kartě [Radar GRAVES](GRAVES-Radar-cs#očekávaná-echa-experimentální).

## Srovnání s RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) shromažďuje hodinové počty meteorů od radiových pozorovatelů; mnozí v Itálii poslouchají GRAVES na 143,050 MHz (planetárium v Benátkách, Faenza, Rovereto a další).

**Čtení souborů RMOB.** Přijímají se dva textové formáty:

| Formát | Vzhled | Poznámky |
|---|---|---|
| Měsíční soubor (Colorgramme / Spectrum Lab) | jeden řádek na den, `day| n| n| …` s 24 hodinovými hodnotami | obvyklý `NAME_MMYYYYrmob.TXT` |
| Tabulka z bulletinu | záhlaví ` UT |  1   2   3 …`, řádky `0h|175 166 …` | pokud soubor obsahuje více pozorovatelů, čtou se jeden po druhém: použijte soubor s jediným pozorovatelem |

Měsíc a rok se berou z názvu souboru (`…_MMYYYYrmob…`) nebo ze záhlaví; jinak se použije aktuální měsíc (a program to oznámí).

**Proložení exponentu.** S K = 1, z mediánu poměrů RMOB/Collm přes společné hodiny (alespoň 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Volba programu (manuál, rov. 46).* Dialog ukáže společné hodiny, medián poměru a k; **Ano** použije k (a nastaví K = 1), **Ne** ponechá k = 3 – pak upravte K ručně na hodnotu navrženou ve stejném dialogu.

## RMOB a automatické programy

RMOB žádá, aby **automatické programy jeho soubory nestahovaly**. Z toho důvodu je **automatické stahování** na začátku **vypnuté** a mělo by se zapnout **až po požádání RMOB o svolení**. Bez něj můžete vždy použít **Načíst soubor RMOB z disku...** nebo stisknout **Stáhnout RMOB nyní**, když to potřebujete.

Adresa pro stahování je šablona v `config.ini` (klíč `rmob_url`, výchozí `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kde `{NOME}` je pozorovatel a `{MMAAAA}` měsíc a rok); stažené soubory se uchovávají v `data/radar/`.
