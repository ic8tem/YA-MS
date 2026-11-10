[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · **Română** · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Contribuții și contacte

YA-MS se îmbunătățește prin rapoartele celor care îl folosesc în eter. Fiecare corecție este atribuită sursei sale.

## Contacte

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Raportarea unei probleme

Deschideți un **issue pe GitHub** sau scrieți un e-mail cu:

- sistemul de operare și versiunea YA-MS (în titlul ferestrei);
- cei doi locatori, banda și ora UTC;
- ce vă așteptați și ce ați văzut (o captură de ecran ajută);
- pentru problemele radar, mesajul afișat în fila [Flux radar](Radar-Flux-ro).

## Ce este deosebit de util

- **Rapoarte din eter.** Orele și traseele în care eficiența sau previziunea au fost corecte – sau greșite. Modelul este experimental și are nevoie de comparație cu QSO-uri reale și cu MCG_MS / MS-Soft.
- **Comparații RMOB.** Valorile factorului de stație K și ale exponentului k pe care le-ați găsit cu [comparația cu RMOB](Experimental-Forecasts-ro#comparația-cu-rmob), împreună cu banda și stația dumneavoastră.
- **Date cu sursă.** Derive mai bune ale radianților, profiluri de activitate, noi date de maxim IMO (`data/massimi_imo.csv`), date despre antene: includeți sursa și va fi citată.
- **Modificări ale graficelor radar.** Dacă formatul graficului de la Collm se schimbă, o copie a imaginii (`data/radar/`) ajută la recalibrarea citirii.

## Traduceri

Traducerile interfeței sunt fișiere text simplu în **`data/lingue/<code>.txt`** (UTF-8) și **oricine le poate corecta**:

```
<Italian text><TAB><translation>
```

- O intrare pe linie; liniile care încep cu `#` sunt comentarii.
- În ambele coloane, cele două caractere `\n` înseamnă o întrerupere de linie.
- Păstrați substituenții `{0}`, `{1}`, … cu formatul lor (de ex. `{0:F1}`, `{3:+0;-0}`), în ordinea de care are nevoie limba dumneavoastră.
- Intrările lipsă sau goale sunt afișate în italiană. Lista tuturor cheilor este `data/lingue/chiavi.txt` (generată de `tools/estrai_chiavi.py`, nu o editați).

Editați fișierul din dosarul `data/lingue` al instalației dumneavoastră și reporniți YA-MS (sau schimbați limba) pentru a vedea rezultatul. Deoarece aceste fișiere sunt **înlocuite cu versiuni mai noi la fiecare actualizare**, vă rugăm să **trimiteți și corecțiile dumneavoastră** – prin e-mail sau ca pull request pe GitHub (`data/lingue/`) – astfel încât să intre în următoarea versiune.

Acest wiki există în 28 de limbi (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文); corecturile paginilor wiki sunt de asemenea binevenite.
