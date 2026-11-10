[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · **Română** · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Contribuții și contacte

YA-MS se îmbunătățește prin rapoartele celor care îl folosesc în trafic. Fiecare corectură este atribuită sursei sale.

## Contacte

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Semnalarea unei probleme

Deschide un **issue pe GitHub** sau scrie un e-mail cu:

- sistemul de operare și versiunea YA-MS (în titlul ferestrei);
- cei doi locatori, banda și ora UTC;
- ce te așteptai și ce ai văzut (o captură de ecran ajută);
- pentru problemele cu radarul, mesajul afișat în fila [Flux radar](Radar-Flux-ro).

## Ce este deosebit de util

- **Rapoarte din trafic.** Orele și traseele în care eficiența sau prognoza au fost corecte – sau greșite. Modelul este experimental și are nevoie de comparații cu QSO-uri reale și cu MCG_MS / MS-Soft.
- **Comparații RMOB.** Valorile factorului stației K și ale exponentului k pe care le-ai găsit cu [comparația RMOB](Experimental-Forecasts-ro#comparația-rmob), împreună cu banda și stația ta.
- **Date cu sursă.** Deplasări mai bune ale radianților, profiluri de activitate, noi date ale maximelor IMO (`data/massimi_imo.csv`), date despre antene: indică sursa și va fi citată.
- **Schimbări ale graficelor radar.** Dacă formatul graficului Collm se schimbă, o copie a imaginii (`data/radar/`) ajută la recalibrarea citirii.

## Traduceri

Traducerile interfeței sunt fișiere text simplu în **`data/lingue/<code>.txt`** (UTF-8) și **oricine le poate corecta**:

```
<Italian text><TAB><translation>
```

- O intrare pe rând; rândurile care încep cu `#` sunt comentarii.
- În ambele coloane, cele două caractere `\n` înseamnă un salt la rând nou.
- Păstrează substituenții `{0}`, `{1}`, … cu formatul lor (de ex. `{0:F1}`, `{3:+0;-0}`), în ordinea de care are nevoie limba ta.
- Intrările lipsă sau goale sunt afișate în italiană. Lista tuturor cheilor este `data/lingue/chiavi.txt` (generată de `tools/estrai_chiavi.py`, nu o edita).

Editează fișierul din dosarul `data/lingue` al instalării tale și repornește YA-MS (sau schimbă limba) ca să vezi rezultatul. Deoarece aceste fișiere sunt **înlocuite de versiunile mai noi la fiecare actualizare**, te rog **trimite și corecturile tale** – prin e-mail sau ca pull request pe GitHub (`data/lingue/`) – ca să intre în următoarea versiune.

Acest wiki există în 36 de limbi (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); corecturile paginilor wiki sunt de asemenea binevenite.
