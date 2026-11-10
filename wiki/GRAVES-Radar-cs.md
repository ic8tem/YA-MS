**English** · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Karta: Živá data a reálný čas › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Co je GRAVES

**GRAVES** je francouzský radar, který vysílá **CW na 143,050 MHz** z **Broye-lès-Pesmes** (47,348° s. š., 5,515° v. d., lokátor **JN27SI**, asi 200 m n. m.; Wikipedie). Meteorické stopy v zóně, kterou vidí GRAVES i vy, odrážejí jeho signál k vám **dopředným rozptylem** (forward scatter): slyšíte krátké *pingy* blízko nosné. Takto pozorovatelé **RMOB** na 143,050 MHz počítají meteory hodinu po hodině, a je to bezplatný, stále zapnutý zkušební signál pro vaši stanici meteor scatter na 2 m.

Karta zachází s trasou **GRAVES → vy** jako se samostatnou trasou meteor scatter: stejnými funkcemi jako u hlavní trasy (stejná výška stop, elevace laloku a vzdálenost hot spotu) počítá účinnost rojů, doporučený Hot a zóny PREV, a pak ověřuje, zda tato zóna leží **uvnitř svazku GRAVES** a **kdy** ji svazek osvětlí.

## Horní lišta

| Ovládací prvek | Co dělá |
|---|---|
| **Nyní** | Vrátí výpočet do reálného času: dnešní datum a posuvník hodin na nulu (karta se řídí *Datem výpočtu* a *Hodinami*). |
| **Nastavit GRAVES jako DX** | DX stanicí se stane GRAVES (JN27SI, výška 200 m) a hlavní trasa se přepočítá: všechny ostatní karty pak ukazují trasu GRAVES. |
| **Sekvence svazku** | *0,8 s na krok · cyklus 4,8 s (PE1ITR 2021)* (výchozí) nebo *3,2 s na krok · cyklus 19,2 s (PE1ITR 2007)*. |

## Čtyři přehledové karty

| Karta | Obsah |
|---|---|
| **UŽITEČNÁ ZÓNA VE SVAZKU GRAVES** | *Ano · sektor X* s azimutem a elevací doporučeného hot spotu viděného z GRAVES a krokem (1–6); nebo *Ne: mimo sektory* / *Ne: pod obzorem GRAVES* / *Ne: nad svazkem (asi 25°)* |
| **ÚČINNOST TRASY GRAVES → VY NYNÍ** | Index trasy Σ ZHR × účinnost, nejlepší roj, převažující strana A/B a *očekávaná echa ≈ …/hodinu* (experimentální, viz níže) |
| **TRASA** | Vzdálenost ke GRAVES; anténa směrem k doporučenému Hot (azimut a elevace); přímý azimut na GRAVES |
| **PŘÍŠTÍ PRŮCHOD SVAZKU NAD ZÓNOU** | *nyní · zbývá … s* nebo *za … s*, krok (např. *B4*), příští tři časy (sekundy v rámci minuty) a podíl zachycených stop |

Pokud v daném okamžiku není užitečný žádný roj, program ukáže hot spot **nejvhodnější pro svazek** (uvnitř sektorů, nejblíže jihu) a oznámí to.

## Obloha viděná z GRAVES

Podle PE1ITR a wiki Bolidozor pokrývají **čtyři fázovaná anténní pole** jižní oblohu od **90° do 270°** azimutu ve čtyřech **sektorech po 45°**:

| Sektor | Azimut od GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Každý sektor je rozdělen na **6 kroků po 7,5°**, číslovaných 1 až 6 od nejnižšího azimutu, které se rozsvěcují jeden po druhém, **ve stejném okamžiku ve všech čtyřech sektorech**. Svazek je **v elevaci široký asi 25°**: ve výšce stop pokrývá barevný prstenec mezi dvěma čárkovanými kružnicemi (*obzor svazku*). Na výkresu: oranžové/růžové tečky = zóny PREV trasy GRAVES → vy, zelená čára = směr k vaší stanici, červená čára = od vaší stanice k doporučenému hot spotu; právě osvětlený krok je zvýrazněn.

## Rekonstrukce časové osy

*REKONSTRUKCE ČASOVÉ OSY · datum UTC* (stejný den jako 24h tabulka): pro každou hodinu účinnost trasy GRAVES → vy, nejpříznivější roj a užitečné okno (*hh:00 → hh:00 UTC · n h*), s maximem (*max Σ … v hh:30*) a červenou značkou *nyní*. Pod tím **detail příštích sekund**: šest kroků sektoru, krok, který osvětluje užitečnou zónu, a *možné echo (+0,3 s stopy)*.

### Časování svazku

Sekvence je vázána na **UTC** (PE1ITR): právě osvětlený krok se počítá ze sekund od 00:00 UTC modulo cyklus (86 400 s je násobkem 4,8 s i 19,2 s). Řídicí stanice občas posune sekvenci o několik kroků, proto je detail **předpovědí, kterou je třeba potvrdit poslechem**. Žlutý štítek **Hodiny PC synchronizovány** vám to připomíná: synchronizujte PC se serverem NTP (chyba nejvýše několik desetin sekundy).

### Detekční faktor

Stopa je slyšet, jen pokud ji svazek osvětlí, dokud trvá:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s je typická délka podhusté stopy na 143 MHz – pevná hodnota, *volba programu* (pravidlo λ² od SM6FHZ přepočítává délky mezi pásmy, ale nedává výchozí hodnotu).

### Očekávaná echa (experimentální)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Předpověď z karty [Experimentální předpovědi](Experimental-Forecasts-cs) (která již obsahuje faktor stanice K) se přepočte z její frekvence f_fc na 143,050 MHz pravidlem SM6FHZ (stejný exponent k), opraví se poměrem indexů rojů obou tras (konstanta 10 představuje sporadické pozadí, stejně jako v předpovědi) a vynásobí se detekčním faktorem. Jen orientačně: porovnávejte s pozorovateli RMOB.

## Jak slyšet pingy GRAVES

| Krok | Co udělat |
|---|---|
| Přijímač | **USB na 143,049 MHz** (tón asi 1 kHz) nebo 143,050 MHz, **pomalé nebo vypnuté AGC**, nf šířka pásma **alespoň 2,4 kHz** |
| Anténa | Směrem k **doporučenému hot spotu** trasy GRAVES → vy (karta *TRASA*), s **nízkou elevací** |
| Waterfall | Pingy jsou **krátké čáry blízko nosné**; dlouhé (přehusté) stopy jsou širší a vykazují Dopplerův posuv |
| Počítání | RMOB používá GRAVES pro hodinové počty meteorů: **porovnejte své pingy s pozorovateli na 143,050 MHz** ([Experimentální předpovědi](Experimental-Forecasts-cs#srovnání-s-rmob)) |

## Zdroje

1. Rob Hardenberg **PE1ITR**, *„The 143.050 MHz Graves Radar, a VHF Beacon“* (DUBUS 4/2007) a *„Graves Radar Update April 2021“* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, „Graves“ – anténní pole, sektory a časování svazku
3. **Wikipedie**, „GRAVES (system)“ – vysílač v Broye-lès-Pesmes (47,348° s. š., 5,515° v. d.)
4. **RMOB** – pozorovatelé na 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** od IC8TEM – karta GRAVES Radar (předloha, ze které tato karta vychází)
