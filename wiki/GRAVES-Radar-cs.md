[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · **Čeština** · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [ไทย](GRAVES-Radar-th) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# Radar GRAVES

*Karta: Živá data a data v reálném čase › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Co je GRAVES

**GRAVES** je francouzský radar, který vysílá **CW na 143,050 MHz** z **Broye-lès-Pesmes** (47,348° s. š. 5,515° v. d., lokátor **JN27SI**, asi 200 m n. m.; Wikipedie). Meteorické stopy v zóně, kterou vidí GRAVES i vy, k vám jeho signál odrážejí **dopředným rozptylem** (forward scatter): slyšíte krátké *pingy* blízko nosné. Takto počítají meteory hodinu po hodině pozorovatelé **RMOB** na 143,050 MHz a je to bezplatný, stále zapnutý zkušební signál pro vaši stanici meteor scatter na 2 m.

Karta pracuje s trasou **GRAVES → vy** jako se samostatnou trasou meteor scatter: stejnými funkcemi jako u hlavní trasy (stejná výška stopy, elevace laloku a vzdálenost hot spotů) počítá účinnost rojů, doporučený Hot a zóny PREV a pak kontroluje, zda tato zóna leží **uvnitř svazku GRAVES** a **kdy** ji svazek osvětlí.

## Horní lišta

| Ovládací prvek | Co dělá |
|---|---|
| **Nyní** | Vrátí čas nebeské klenby na reálný čas (karta sleduje posuvník *Čas nebeské klenby*). |
| **Nastavit GRAVES jako DX** | Stanicí DX se stane GRAVES (JN27SI, výška 200 m) a hlavní trasa se přepočítá: všechny ostatní karty pak ukazují trasu ke GRAVES. |
| **Sekvence svazku** | *0,8 s na krok · cyklus 4,8 s (PE1ITR 2021)* (výchozí) nebo *3,2 s na krok · cyklus 19,2 s (PE1ITR 2007)*. |

## Čtyři karty

| Karta | Obsah |
|---|---|
| **UŽITEČNÁ ZÓNA VE SVAZKU GRAVES** | *Ano · sektor X* s azimutem a elevací doporučeného hot spotu viděného z GRAVES a krokem (1–6); nebo *Ne: mimo sektory* / *Ne: pod obzorem GRAVES* / *Ne: nad svazkem (asi 25°)* |
| **ÚČINNOST TRASY GRAVES → VY NYNÍ** | Index trasy Σ ZHR × účinnost, nejlepší roj, převládající strana A/B a *očekávaná echa ≈ …/hodinu* (experimentální, viz níže) |
| **TRASA** | Vzdálenost ke GRAVES; anténa směrem k doporučenému Hotu (azimut a elevace); přímý azimut na GRAVES |
| **PŘÍŠTÍ PRŮCHOD SVAZKU NAD ZÓNOU** | *nyní · zbývá … s* nebo *za … s*, krok (např. *B4*), příští tři časy (sekundy v rámci minuty) a podíl zachycených stop |

Pokud v danou chvíli není užitečný žádný roj, program ukáže hot spot **nejvhodnější pro svazek** (uvnitř sektorů, nejblíže k jihu) a oznámí to.

## Obloha viděná z GRAVES

Podle PE1ITR a wiki Bolidozor pokrývají jižní oblohu od azimutu **90° do 270°** **čtyři fázované soustavy** ve čtyřech **sektorech po 45°**:

| Sektor | Azimut od GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Každý sektor je rozdělen na **6 kroků po 7,5°**, číslovaných 1 až 6 od nejnižšího azimutu, které se rozsvěcují jeden po druhém, **ve stejném okamžiku ve všech čtyřech sektorech**. Svazek je **široký asi 25° v elevaci**: ve výšce stopy pokrývá barevný prstenec mezi dvěma čárkovanými kružnicemi (*obzor svazku*). Na obrázku: oranžové/růžové body = zóny PREV trasy GRAVES → vy, zelená čára = směr k vaší stanici, červená čára = od vaší stanice k doporučenému hot spotu; právě rozsvícený krok je zvýrazněn.

## Rekonstrukce časové osy

*REKONSTRUKCE ČASOVÉ OSY · datum UTC* (stejný den jako tabulka 24 h): pro každou hodinu účinnost trasy GRAVES → vy, nejpříznivější roj a užitečné okno (*hh:00 → hh:00 UTC · n h*), s maximem (*max Σ … v hh:30*) a červenou značkou *nyní*. Pod tím jsou **podrobnosti na příštích několik sekund**: šest kroků sektoru, krok, který osvětluje užitečnou zónu, a *možné echo (+0,3 s stopy)*.

### Časování svazku

Sekvence je svázána s časem **UTC** (PE1ITR): právě rozsvícený krok se počítá ze sekund od 00:00 UTC modulo cyklus (86 400 s je násobkem 4,8 s i 19,2 s). Řídicí stanice někdy sekvenci posune o několik kroků, takže podrobnosti jsou **předpovědí, kterou je třeba potvrdit poslechem**. Žlutý štítek **hodiny PC synchronizovány** to připomíná: synchronizujte svůj PC se serverem NTP (chyba nejvýše několik desetin sekundy).

### Faktor detekce

Stopa je slyšet jen tehdy, když ji svazek osvětlí, dokud trvá:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s je typické trvání podhusté stopy na 143 MHz – pevná hodnota, *volba programu* (pravidlo λ² od SM6FHZ přepočítává trvání mezi pásmy, ale nedává výchozí hodnotu).

### Očekávaná echa (experimentální)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Předpověď z [Experimentálních předpovědí](Experimental-Forecasts-cs) (která už obsahuje faktor stanice K) se přepočte z jejího kmitočtu f_fc na 143,050 MHz pravidlem SM6FHZ (stejný exponent k), opraví poměrem indexů rojů obou tras (konstanta 10 představuje sporadické pozadí, stejně jako v předpovědi) a vynásobí faktorem detekce. Jen orientační: porovnejte s pozorovateli RMOB.

## Jak slyšet pingy GRAVES

| Krok | Co dělat |
|---|---|
| Přijímač | **USB na 143,049 MHz** (tón asi 1 kHz) nebo 143,050 MHz, **pomalé nebo vypnuté AGC**, nf šířka pásma **alespoň 2,4 kHz** |
| Anténa | Směrem k **doporučenému hot spotu** trasy GRAVES → vy (karta *TRASA*), s **nízkou elevací** |
| Vodopád | Pingy jsou **krátké čáry blízko nosné**; dlouhé (nadhusté) stopy jsou širší a ukazují Dopplerův posun |
| Počítání | RMOB používá GRAVES pro hodinové počty meteorů: **porovnejte své pingy s pozorovateli na 143,050 MHz** ([Experimentální předpovědi](Experimental-Forecasts-cs#srovnání-s-rmob)) |

## Zdroje

1. Rob Hardenberg **PE1ITR**, *„The 143.050 MHz Graves Radar, a VHF Beacon“* (DUBUS 4/2007) a *„Graves Radar Update April 2021“* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, „Graves“ – soustavy, sektory a časování svazku
3. **Wikipedie**, „GRAVES (system)“ – vysílač v Broye-lès-Pesmes (47,348° s. š. 5,515° v. d.)
4. **RMOB** – pozorovatelé na 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** od IC8TEM – karta Radar GRAVES (návrh, ze kterého je tato karta odvozena)
