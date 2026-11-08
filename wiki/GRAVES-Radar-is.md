**English** · [Русский](GRAVES-Radar-ru) · [Deutsch](GRAVES-Radar-de) · [日本語](GRAVES-Radar-ja)

# GRAVES-ratsjá

*Flipi: Beint og rauntímagögn › GRAVES-ratsjá.*

[![GRAVES-ratsjá](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Hvað GRAVES er

**GRAVES** er frönsk ratsjá sem sendir **CW á 143,050 MHz** frá **Broye-lès-Pesmes** (47.348° N 5.515° E, locator **JN27SI**, um 200 m y.s.; Wikipedia). Loftsteinaslóðir á svæðinu sem bæði GRAVES og þú sjáið endurvarpa merki hennar til þín með **forward scatter**: þú heyrir stutt *ping* nálægt burðarbylgjunni. Þannig telja **RMOB**-athugendur á 143,050 MHz loftsteina klukkustund fyrir klukkustund, og þetta er ókeypis prófunarmerki sem er alltaf í gangi fyrir meteor scatter-stöðina þína á 2 m.

Flipinn meðhöndlar **GRAVES → þú** sem sérstaka meteor scatter-leið: með sömu föllum og fyrir aðalleiðina (sama hæð slóða, hæðarhorn geisla og fjarlægð heitu blettanna) reiknar hann nýtni drífanna, ráðlagðan Hot og PREV-svæði, og athugar síðan hvort svæðið er **innan geisla GRAVES** og **hvenær** geislinn lýsir það upp.

## Efsta stikan

| Stýring | Hvað hún gerir |
|---|---|
| **Núna** | Færir tíma himinhvelfingarinnar aftur í rauntíma (flipinn fylgir sleðanum *Tími himinhvelfingar*). |
| **Setja GRAVES sem DX** | Mótstöðin verður GRAVES (JN27SI, hæð 200 m) og aðalleiðin er endurreiknuð: allir aðrir flipar sýna þá GRAVES-leiðina. |
| **Röð geislans** | *0,8 s á skref · lota 4,8 s (PE1ITR 2021)* (sjálfgefið) eða *3,2 s á skref · lota 19,2 s (PE1ITR 2007)*. |

## Spjöldin fjögur

| Spjald | Innihald |
|---|---|
| **NÝTILEGT SVÆÐI Í GEISLA GRAVES** | *Já · geiri X* með áttarhorni og hæðarhorni ráðlagða heita blettsins séð frá GRAVES og skrefinu (1–6); eða *Nei: utan geiranna* / *Nei: undir sjóndeildarhring GRAVES* / *Nei: fyrir ofan geislann (um 25°)* |
| **NÝTNI LEIÐARINNAR GRAVES → ÞÚ NÚNA** | Leiðarstuðull Σ ZHR × nýtni, besta drífan, ríkjandi hlið A/B og *væntanleg bergmál ≈ …/klst.* (tilraun, sjá hér fyrir neðan) |
| **LEIÐ** | Fjarlægð til GRAVES; loftnet að ráðlögðum Hot (áttarhorn og hæðarhorn); beint áttarhorn til GRAVES |
| **NÆSTA YFIRFERÐ GEISLANS YFIR SVÆÐIÐ** | *núna · … s eftir* eða *eftir … s*, skrefið (t.d. *B4*), næstu þrír tímar (sekúndur innan mínútunnar) og hlutfall slóða sem nást |

Ef engin drífa er nýtileg á þeirri stundu sýnir forritið þann heita blett sem **hentar geislanum best** (innan geiranna, næst suðri) og segir frá því.

## Himinninn séður frá GRAVES

Samkvæmt PE1ITR og wiki Bolidozor þekja **fjögur fasastýrð loftnetakerfi** suðurhimininn frá **90° til 270°** í áttarhorni í fjórum **45° geirum**:

| Geiri | Áttarhorn frá GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Hverjum geira er skipt í **6 skref á 7,5°**, númeruð 1 til 6 frá lægsta áttarhorni, sem lýst eru upp hvert á eftir öðru, **á sama augnabliki í öllum fjórum geirunum**. Geislinn er um **25° breiður í hæðarhorni**: í hæð slóðanna þekur hann litaða hringinn milli brotnu hringjanna tveggja (*sjóndeildarhringur geislans*). Á teikningunni: appelsínugulir/bleikir punktar = PREV-svæði leiðarinnar GRAVES → þú, græn lína = stefnan að þinni stöð, rauð lína = frá þinni stöð að ráðlagða heita blettinum; skrefið sem lýst er núna er auðkennt.

## Endurgerð tímalínu

*ENDURGERÐ TÍMALÍNU · dagsetning UTC* (sami dagur og í 24 klst. töflunni): fyrir hverja klukkustund nýtni leiðarinnar GRAVES → þú, hagstæðasta drífan og nýtilegi glugginn (*hh:00 → hh:00 UTC · n klst.*), með hámarkinu (*hám. Σ … kl. hh:30*) og rauðu merki fyrir *núna*. Fyrir neðan er **nánari sýn á næstu sekúndur**: sex skref geirans, skrefið sem lýsir upp nýtilega svæðið og *mögulegt bergmál (+0,3 s af slóð)*.

### Tímasetning geislans

Röðin er bundin **UTC** (PE1ITR): skrefið sem lýst er núna er reiknað út frá sekúndum frá 00:00 UTC, mátað við lotuna (86 400 s er margfeldi bæði af 4,8 s og 19,2 s). Stjórnstöðin hliðrar stundum röðinni um nokkur skref, svo nánari sýnin er **spá sem staðfesta þarf með hlustun**. Gula merkið **klukka tölvunnar samstillt** minnir þig á: samstilltu tölvuna þína við NTP-þjón (skekkja í mesta lagi nokkrir tíundu hlutar úr sekúndu).

### Greiningarstuðull

Slóð heyrist aðeins ef geislinn lýsir hana upp á meðan hún varir:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s er dæmigerð lengd undirþéttrar slóðar á 143 MHz – fast gildi, *val forritsins* (λ²-regla SM6FHZ kvarðar lengdir milli tíðnisviða en gefur ekkert upphafsgildi).

### Væntanleg bergmál (tilraun)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

Spáin úr [Tilraunaspám](Experimental-Forecasts-is) (sem inniheldur þegar stöðvarstuðulinn K) er kvörðuð frá tíðni sinni f_fc að 143,050 MHz með reglu SM6FHZ (sami veldisvísir k), leiðrétt með hlutfalli drífustuðla leiðanna tveggja (fastinn 10 táknar stopula bakgrunninn, eins og í spánni) og margfölduð með greiningarstuðlinum. Aðeins til viðmiðunar: berðu saman við RMOB-athugendur.

## Hvernig á að heyra GRAVES-pingin

| Skref | Hvað á að gera |
|---|---|
| Viðtæki | **USB á 143,049 MHz** (tónn um 1 kHz) eða 143,050 MHz, **hægt eða óvirkt AGC**, hljóðbandbreidd **a.m.k. 2,4 kHz** |
| Loftnet | Að **ráðlagða heita blettinum** fyrir leiðina GRAVES → þú (spjaldið *LEIÐ*), með **lágt hæðarhorn** |
| Foss (waterfall) | Ping eru **stutt strik nálægt burðarbylgjunni**; langar (yfirþéttar) slóðir eru breiðari og sýna Doppler-hliðrun |
| Talning | RMOB notar GRAVES til að telja loftsteina á klukkustund: **berðu pingin þín saman við athugendur á 143,050 MHz** ([Tilraunaspár](Experimental-Forecasts-is#samanburður-við-rmob)) |

## Heimildir

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) og *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, "Graves" – loftnetakerfi, geirar og tímasetning geislans
3. **Wikipedia**, "GRAVES (system)" – sendirinn í Broye-lès-Pesmes (47.348° N 5.515° E)
4. **RMOB** – athugendur á 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** eftir IC8TEM – flipinn GRAVES Radar (fyrirmyndin sem þessi flipi er dreginn af)
