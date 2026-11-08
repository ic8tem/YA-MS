**English** · [Русский](GRAVES-Radar-ru) · [Deutsch](GRAVES-Radar-de) · [日本語](GRAVES-Radar-ja)

# GRAVES radaras

*Kortelė: Tiesiogiai ir realiojo laiko duomenys › GRAVES radaras.*

[![GRAVES radaras](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Kas yra GRAVES

**GRAVES** – prancūzų radaras, transliuojantis **CW 143,050 MHz dažniu** iš **Broye-lès-Pesmes** (47,348° Š 5,515° R, lokatorius **JN27SI**, apie 200 m virš jūros lygio; Wikipedia). Meteorų pėdsakai zonoje, kurią mato ir GRAVES, ir jūs, atspindi jo signalą jums **forward scatter** būdu: girdite trumpus *ping* atspindžius šalia nešlio. Taip **RMOB** stebėtojai 143,050 MHz dažniu skaičiuoja meteorus kas valandą, ir tai nemokamas, visada veikiantis bandomasis signalas jūsų 2 m meteor scatter stočiai.

Kortelė traktuoja **GRAVES → jūs** kaip atskirą meteor scatter trasą: su tomis pačiomis funkcijomis kaip pagrindinei trasai (tas pats pėdsakų aukštis, lapelio elevacija ir hot spot atstumas) ji apskaičiuoja srautų efektyvumą, rekomenduojamą Hot ir PREV zonas, o tada patikrina, ar ta zona yra **GRAVES pluošte** ir **kada** pluoštas ją apšviečia.

## Viršutinė juosta

| Valdiklis | Ką daro |
|---|---|
| **Dabar** | Grąžina dangaus skliauto laiką į realų laiką (kortelė seka slankiklį *Dangaus skliauto laikas*). |
| **GRAVES kaip DX** | Korespondentu tampa GRAVES (JN27SI, aukštis 200 m), o pagrindinė trasa perskaičiuojama: visos kitos kortelės tada rodo GRAVES trasą. |
| **Pluošto seka** | *0,8 s žingsniui · ciklas 4,8 s (PE1ITR 2021)* (numatytoji) arba *3,2 s žingsniui · ciklas 19,2 s (PE1ITR 2007)*. |

## Keturi skydeliai

| Skydelis | Turinys |
|---|---|
| **NAUDINGOJI ZONA GRAVES PLUOŠTE** | *Taip · sektorius X* su rekomenduojamo hot spot azimutu ir elevacija, matomais iš GRAVES, ir žingsniu (1–6); arba *Ne: už sektorių ribų* / *Ne: žemiau GRAVES horizonto* / *Ne: virš pluošto (apie 25°)* |
| **GRAVES → JŪSŲ TRASOS EFEKTYVUMAS DABAR** | Trasos indeksas Σ ZHR × efektyvumas, geriausias srautas, vyraujanti pusė A/B ir *laukiami aidai ≈ …/val.* (eksperimentinis, žr. toliau) |
| **TRASA** | Atstumas iki GRAVES; antena į rekomenduojamą Hot (azimutas ir elevacija); tiesioginis GRAVES azimutas |
| **KITAS PLUOŠTO PRAĖJIMAS PER ZONĄ** | *dabar · liko … s* arba *po … s*, žingsnis (pvz., *B4*), trys kiti laikai (sekundės minutės viduje) ir pagautų pėdsakų dalis |

Jei tuo momentu nė vienas srautas nėra naudingas, programa rodo **pluoštui tinkamiausią** hot spot (sektorių viduje, arčiausiai pietų) ir apie tai praneša.

## Dangus, kurį mato GRAVES

Pagal PE1ITR ir Bolidozor wiki **keturios fazuotosios gardelės** dengia pietinę dangaus dalį nuo **90° iki 270°** azimuto keturiais **45° sektoriais**:

| Sektorius | Azimutas iš GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Kiekvienas sektorius padalytas į **6 žingsnius po 7,5°**, numeruojamus nuo 1 iki 6 pradedant mažiausiu azimutu, apšviečiamus vienas po kito, **tuo pačiu metu visuose keturiuose sektoriuose**. Pluoštas yra **apie 25° pločio pagal elevaciją**: pėdsakų aukštyje jis dengia spalvotą žiedą tarp dviejų brūkšninių apskritimų (*pluošto horizontas*). Brėžinyje: oranžiniai/rožiniai taškai = GRAVES → jūsų trasos PREV zonos, žalia linija = jūsų stoties kryptis, raudona linija = nuo jūsų stoties iki rekomenduojamo hot spot; dabar apšviestas žingsnis paryškintas.

## Chronologinė rekonstrukcija

*CHRONOLOGINĖ REKONSTRUKCIJA · data UTC* (ta pati diena kaip 24 h lentelėje): kiekvienai valandai GRAVES → jūsų trasos efektyvumas, palankiausias srautas ir naudingasis langas (*hh:00 → hh:00 UTC · n h*), su maksimumu (*maks. Σ … hh:30*) ir raudona žyma *dabar*. Apačioje – **kitų sekundžių detalės**: šeši sektoriaus žingsniai, naudingąją zoną apšviečiantis žingsnis ir *galimas aidas (+0,3 s pėdsako)*.

### Pluošto laikas

Seka susieta su **UTC** laiku (PE1ITR): dabar apšviestas žingsnis apskaičiuojamas iš sekundžių nuo 00:00 UTC moduliu ciklo trukmė (86 400 s yra ir 4,8 s, ir 19,2 s kartotinis). Valdymo stotis kartais paslenka seką keliais žingsniais, todėl detalės yra **prognozė, kurią reikia patvirtinti klausantis**. Geltona žyma **PC laikrodis sinchronizuotas** primena: sinchronizuokite savo PC su NTP serveriu (paklaida daugiausia kelios sekundės dešimtosios).

### Aptikimo koeficientas

Pėdsakas girdimas tik tada, jei pluoštas jį apšviečia, kol jis egzistuoja:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s – tipinė retojo pėdsako trukmė ties 143 MHz – fiksuota vertė, *programos sprendimas* (SM6FHZ λ² taisyklė perskaičiuoja trukmes tarp juostų, bet neduoda pradinės vertės).

### Laukiami aidai (eksperimentiniai)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

[Eksperimentinių prognozių](Experimental-Forecasts-lt) prognozė (kurioje jau yra stoties koeficientas K) perskaičiuojama iš jos dažnio f_fc į 143,050 MHz pagal SM6FHZ taisyklę (tas pats rodiklis k), pataisoma dviejų trasų srautų indeksų santykiu (konstanta 10 atspindi sporadinį foną, kaip prognozėje) ir padauginama iš aptikimo koeficiento. Tik orientacinė vertė: palyginkite su RMOB stebėtojais.

## Kaip išgirsti GRAVES atspindžius

| Žingsnis | Ką daryti |
|---|---|
| Imtuvas | **USB ties 143,049 MHz** (tonas apie 1 kHz) arba 143,050 MHz, **lėtas arba išjungtas AGC**, garso juosta **ne siauresnė nei 2,4 kHz** |
| Antena | Į GRAVES → jūsų trasos **rekomenduojamą hot spot** (skydelis *TRASA*), **maža elevacija** |
| Krioklys | Atspindžiai (ping) yra **trumpos linijos šalia nešlio**; ilgi (tankieji) pėdsakai platesni ir rodo Doplerį |
| Skaičiavimas | RMOB naudoja GRAVES valandiniams meteorų skaičiams: **palyginkite savo atspindžius su stebėtojais 143,050 MHz dažniu** ([Eksperimentinės prognozės](Experimental-Forecasts-lt#palyginimas-su-rmob)) |

## Šaltiniai

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) ir *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – gardelės, sektoriai ir pluošto laikas
3. **Wikipedia**, "GRAVES (system)" – siųstuvas Broye-lès-Pesmes (47,348° Š 5,515° R)
4. **RMOB** – stebėtojai 143,050 MHz dažniu ([rmob.org](https://www.rmob.org))
5. IC8TEM **YAEC** – kortelė GRAVES radaras (eskizas, iš kurio kilo ši kortelė)
