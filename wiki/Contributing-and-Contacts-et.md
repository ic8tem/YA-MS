[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · **Eesti** · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Kaastöö ja kontaktid

YA-MS paraneb tänu inimestele, kes seda eetris kasutavad ja oma tähelepanekutest teatavad. Iga parandus omistatakse selle allikale.

## Kontaktid

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-post | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Probleemist teatamine

Ava **GitHubis issue** või kirjuta e-kiri, märkides:

- operatsioonisüsteemi ja YA-MS-i versiooni (akna tiitelribal);
- kaks lokaatorit, sagedusala ja UTC aja;
- mida ootasid ja mida nägid (ekraanipilt aitab);
- radariprobleemide korral sakil [Radari voog](Radar-Flux-et) näidatud teate.

## Mis on eriti kasulik

- **Eetrikogemused.** Tunnid ja trassid, kus efektiivsus või prognoos osutusid õigeks – või valeks. Mudel on eksperimentaalne ja vajab võrdlust tegelike QSO-dega ning MCG_MS-i / MS-Softiga.
- **RMOB-i võrdlused.** Jaama teguri K ja astendaja k väärtused, mille leidsid [võrdlusest RMOB-iga](Experimental-Forecasts-et#võrdlus-rmob-iga), koos oma sagedusala ja jaamaga.
- **Allikaga andmed.** Paremad radiantide nihked, aktiivsusprofiilid, uued IMO maksimumide kuupäevad (`data/massimi_imo.csv`), antenniandmed: lisa allikas ja sellele viidatakse.
- **Radarigraafikute muudatused.** Kui Collmi graafiku vorming muutub, aitab pildi koopia (`data/radar/`) lugemist uuesti kalibreerida.

## Tõlked

Kasutajaliidese tõlked on lihttekstifailid kaustas **`data/lingue/<code>.txt`** (UTF-8) ja **igaüks võib neid parandada**:

```
<Italian text><TAB><translation>
```

- Üks kirje rea kohta; märgiga `#` algavad read on kommentaarid.
- Mõlemas veerus tähendavad kaks märki `\n` reavahetust.
- Säilita kohatäited `{0}`, `{1}`, … koos nende vorminguga (nt `{0:F1}`, `{3:+0;-0}`), sinu keele nõutud järjekorras.
- Puuduvad või tühjad kirjed kuvatakse itaalia keeles. Kõigi võtmete loend on `data/lingue/chiavi.txt` (selle loob `tools/estrai_chiavi.py`, ära seda muuda).

Muuda faili oma paigalduse kaustas `data/lingue` ja käivita YA-MS uuesti (või vaheta keelt), et tulemust näha. Kuna need failid **asendatakse iga uuendusega uuematega**, saada palun oma parandused ka autorile – e-kirjaga või pull requestina GitHubis (`data/lingue/`) –, et need jõuaksid järgmisse väljalaskesse.

See wiki on olemas inglise, vene, saksa ja jaapani keeles; ka wiki lehtede parandused on teretulnud.
