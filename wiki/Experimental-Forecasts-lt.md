**English** · [Русский](Experimental-Forecasts-ru) · [Deutsch](Experimental-Forecasts-de) · [日本語](Experimental-Forecasts-ja)

# Eksperimentinės prognozės

*Kortelė: Prognozės skaičiavimas › Eksperimentinės prognozės.*

[![Eksperimentinės prognozės](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Ši kortelė **Collm radaro (36,2 MHz)** meteorų skaičius paverčia **atspindžių per valandą mėgėjų juostoje** įverčiu (pagal nutylėjimą 144 MHz, bet kuris dažnis nuo 28 iki 1300 MHz), prognozuoja jūsų trasai **kitas 24 valandas** ir leidžia įvertį **palyginti** su **RMOB** stebėtoju – pavyzdžiui, tokiu, kuris klausosi GRAVES 143,050 MHz dažniu.

> Viskas čia yra **eksperimentinis**: dažnio taisyklė yra empirinė, o stoties koeficientas priklauso nuo jūsų stoties. Naudokite skaičius valandoms ir dienoms palyginti ir tikrinkite juos eteryje.

## Valdikliai

| Valdiklis | Numatytasis | Ką daro |
|---|---|---|
| **Tikslinis dažnis MHz** | 144 | Prognozės dažnis (28–1300 MHz) |
| **λ^k rodiklis** | 3 | Dažnio taisyklės rodiklis k (SM6FHZ: 3) |
| **Stoties koeficientas K** | 1 | Įvertina priimančiąją stotį (galia, antenos); gaunamas palyginus su RMOB stebėtoju toje pačioje juostoje |
| **Įkelti RMOB failą iš disko...** | | Nuskaito mėnesio RMOB tekstinį failą (žr. toliau) |
| **Rodiklį gauti iš RMOB failo** | | Pritaiko k pagal bendras Collm ir RMOB valandas |
| **RMOB stebėtojas** | tuščia | Stebėtojo vardas, kaip jis užrašytas failo pavadinime (pvz., `NAME_112026rmob.TXT` → `NAME`) |
| **Atsisiųsti RMOB dabar** | | Vieną kartą atsisiunčia to stebėtojo einamojo mėnesio failą |
| **automatinis atsisiuntimas kas 5 minutes (įjungti tik gavus RMOB leidimą)** | **išjungta** | Žr. [RMOB ir automatinės programos](#rmob-ir-automatinės-programos) |

Oranžinė eilutė po valdikliais rodo taisyklę su dabartiniais skaičiais, pvz., *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, trukmės perskaičiavimą ir IARU didžiausią atspindžio trukmę tuo dažniu.

## Nuo radaro iki mėgėjų juostos

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Šaltinis:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45-asis Nordic VUSHF, 2025 m. gegužė – atspindžių skaičius ir intensyvumas kinta pagal **λ³**, trukmė – pagal **λ²** (432 MHz yra 14–15 dB žemiau nei 144 MHz ir trunka 1/9). **Patikra:** λ³ priklausomybė ta pati kaip McKinley retojo pėdsako lygtyje. Su k = 3 1000 meteorų/val. Collm virsta maždaug **16 atspindžių/val. ties 144 MHz**; GRAVES RMOB stebėtojai 143,050 MHz dažniu paprastai suskaičiuoja **nuo 20 iki 140 aidų/val.** (RMOB biuletenis, 2018 m. birželis): eilė suderinama, o skirtumas yra stoties koeficientas K. (Vadovo 44–45 lygtys.)

## Kitos 24 valandos

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Pastovumas:** perskaičiuota tos pačios valandos vertė praėjusią dieną (arba prieš dvi dienas, jei jos nėra), pataisyta pagal **trasos srautų indekso** I pokytį (Σ ZHR × efektyvumas, žr. [Efektyvumo skaičiavimas](Efficiency-Calculation-lt#modelis)). Konstanta 10 atspindi sporadinį foną ir riboja pataisą, kai indeksas mažas. *Programos sprendimas (vadovo 47 lygtis).*

| Skydelis | Turinys |
|---|---|
| **Išmatuota Collm ir perskaičiuota į f MHz – vakar ir šiandien (UTC)** | Collm radaro meteorai/val.; perskaičiuotos vertės (oranžinė, dešinė skalė); RMOB skaičiai, jei įkelti (žalia, dešinė skalė) |
| **Eksperimentinė kitų 24 valandų prognozė ties f MHz: …** | Prognozuojami atspindžiai/val. (stulpeliai) ir trasos srautų indeksas (dešinė skalė) |
| Lentelė | UTC laikas · Collm ta pačia valanda · Perskaičiuota · Trasos srautų indeksas · Prognozė /val. · **Įvertinimas** |

**Įvertinimas:** *geras*, kai prognozė yra bent 1,3 × 24 valandų vidurkio, *vidutinis* – nuo 0,8 ×, *silpnas* – mažiau. Ta pati prognozė rodoma skydelyje **EKSPERIMENTINĖ PROGNOZĖ** ir [Efektyvumo skaičiavimo](Efficiency-Calculation-lt) oranžinėje eilutėje, ji taip pat yra laukiamų aidų pagrindas kortelėje [GRAVES radaras](GRAVES-Radar-lt#laukiami-aidai-eksperimentiniai).

## Palyginimas su RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) renka radijo stebėtojų valandinius meteorų skaičius; daugelis Italijoje klausosi GRAVES 143,050 MHz dažniu (Venecijos planetariumas, Faenza, Rovereto ir kt.).

**RMOB failų skaitymas.** Priimami du tekstiniai formatai:

| Formatas | Išvaizda | Pastabos |
|---|---|---|
| Mėnesio failas (Colorgramme / Spectrum Lab) | po vieną eilutę dienai, `day| n| n| …` su 24 valandinėmis vertėmis | įprastas `NAME_MMYYYYrmob.TXT` |
| Biuletenio lentelė | antraštė ` UT |  1   2   3 …`, eilutės `0h|175 166 …` | jei faile yra keli stebėtojai, jie nuskaitomi iš eilės: naudokite failą su vienu stebėtoju |

Mėnuo ir metai imami iš failo pavadinimo (`…_MMYYYYrmob…`) arba iš antraštės; kitu atveju naudojamas einamasis mėnuo (ir programa apie tai praneša).

**Rodiklio pritaikymas.** Su K = 1, pagal RMOB/Collm santykių medianą bendromis valandomis (ne mažiau kaip 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Programos sprendimas (vadovo 46 lygtis).* Dialogo lange rodomos bendros valandos, santykio mediana ir k; **Taip** pritaiko k (ir nustato K = 1), **Ne** palieka k = 3 – tada ranka nustatykite K į tame pačiame dialoge siūlomą vertę.

## RMOB ir automatinės programos

RMOB prašo, kad **automatinės programos neatsisiųstų jo failų**. Todėl **automatinis atsisiuntimas** pradžioje yra **išjungtas** ir jį reikėtų įjungti **tik paprašius RMOB leidimo**. Be jo visada galite naudoti **Įkelti RMOB failą iš disko...** arba prireikus spausti **Atsisiųsti RMOB dabar**.

Atsisiuntimo adresas yra šablonas faile `config.ini` (raktas `rmob_url`, numatytasis `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, kur `{NOME}` – stebėtojas, o `{MMAAAA}` – mėnuo ir metai); atsisiųsti failai saugomi aplanke `data/radar/`.
