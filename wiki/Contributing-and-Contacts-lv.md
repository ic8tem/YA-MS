[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · **Latviešu** · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Līdzdalība un kontakti

YA-MS uzlabojas, pateicoties to cilvēku ziņojumiem, kas to izmanto ēterā. Katrs labojums tiek piedēvēts tā avotam.

## Kontakti

| | |
|---|---|
| Autors | Costantino Cerrotta **IC8TEM** |
| E-pasts | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Ziņošana par problēmu

Atver **issue vietnē GitHub** vai raksti e-pastu, norādot:

- operētājsistēmu un YA-MS versiju (loga virsrakstā);
- abus lokatorus, joslu un UTC laiku;
- ko gaidīji un ko redzēji (ekrānuzņēmums palīdz);
- radaru problēmu gadījumā – ziņojumu, kas parādīts cilnē [Radara meteoru skaits](Radar-Flux-lv).

## Kas ir īpaši noderīgi

- **Ziņojumi no ētera.** Stundas un trases, kurās efektivitāte vai prognoze bija pareiza – vai nepareiza. Modelis ir eksperimentāls, un to vajag salīdzināt ar reāliem QSO un ar MCG_MS / MS-Soft.
- **RMOB salīdzinājumi.** Stacijas koeficienta K un kāpinātāja k vērtības, ko atradi ar [salīdzinājumu ar RMOB](Experimental-Forecasts-lv#salīdzinājums-ar-rmob), norādot savu joslu un staciju.
- **Dati ar avotu.** Labāki radiantu pārvietojumi, aktivitātes profili, jauni IMO maksimumu datumi (`data/massimi_imo.csv`), antenu dati: norādi avotu, un tas tiks citēts.
- **Radaru grafiku izmaiņas.** Ja Collm grafika formāts mainās, attēla kopija (`data/radar/`) palīdz pārkalibrēt nolasīšanu.

## Tulkojumi

Saskarnes tulkojumi ir vienkārši teksta faili **`data/lingue/<code>.txt`** (UTF-8), un **ikviens tos var labot**:

```
<Italian text><TAB><translation>
```

- Viens ieraksts rindā; rindas, kas sākas ar `#`, ir komentāri.
- Abās kolonnās divas rakstzīmes `\n` nozīmē rindas pārnesumu.
- Saglabā vietturus `{0}`, `{1}`, … ar to formātu (piem. `{0:F1}`, `{3:+0;-0}`), tādā secībā, kāda vajadzīga tavai valodai.
- Trūkstošie vai tukšie ieraksti tiek rādīti itāliski. Visu atslēgu saraksts ir `data/lingue/chiavi.txt` (ģenerē `tools/estrai_chiavi.py`, to nerediģē).

Rediģē failu savas instalācijas mapē `data/lingue` un restartē YA-MS (vai pārslēdz valodu), lai redzētu rezultātu. Tā kā šie faili **katrā atjauninājumā tiek aizstāti ar jaunākiem**, lūdzu, arī **nosūti savus labojumus** – pa e-pastu vai kā pull request vietnē GitHub (`data/lingue/`) –, lai tie nonāktu nākamajā laidienā.

Šī wiki ir pieejama 36 valodās (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); laipni gaidīti arī wiki lapu labojumi.
