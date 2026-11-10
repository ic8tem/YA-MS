[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · **Magyar** · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Közreműködés és kapcsolat

A YA-MS azoknak a jelzéseinek köszönhetően fejlődik, akik forgalom közben használják. Minden javítást a forrásának tulajdonítunk.

## Kapcsolat

| | |
|---|---|
| Szerző | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Hiba bejelentése

Nyisson egy **issue-t a GitHubon**, vagy írjon e-mailt a következőkkel:

- operációs rendszer és a YA-MS változatszáma (az ablak címsorában);
- a két lokátor, a sáv és az UTC idő;
- mire számított és mit látott (egy képernyőkép segít);
- radarproblémák esetén a [Radarfluxus](Radar-Flux-hu) fülön megjelenő üzenet.

## Mi különösen hasznos

- **Forgalmi beszámolók.** Órák és útvonalak, ahol a hatékonyság vagy az előrejelzés bevált – vagy nem. A modell kísérleti, és össze kell vetni valódi QSO-kkal, valamint az MCG_MS / MS-Soft eredményeivel.
- **RMOB-összehasonlítások.** A K állomástényező és a k kitevő azon értékei, amelyeket az [RMOB-összehasonlítással](Experimental-Forecasts-hu#rmob-összehasonlítás) kapott, a sávjával és az állomásával együtt.
- **Adatok forrással.** Pontosabb radiánselmozdulások, aktivitási profilok, új IMO-csúcsdátumok (`data/massimi_imo.csv`), antennaadatok: adja meg a forrást, és hivatkozni fogunk rá.
- **A radardiagramok változásai.** Ha a Collm-diagram formátuma megváltozik, a kép egy másolata (`data/radar/`) segít a beolvasás újrakalibrálásában.

## Fordítások

A kezelőfelület fordításai egyszerű szövegfájlok a **`data/lingue/<code>.txt`** helyen (UTF-8), és **bárki javíthatja őket**:

```
<Italian text><TAB><translation>
```

- Soronként egy bejegyzés; a `#` jellel kezdődő sorok megjegyzések.
- Mindkét oszlopban a `\n` két karakter sortörést jelent.
- Tartsa meg a `{0}`, `{1}`, … helyőrzőket a formátumukkal együtt (pl. `{0:F1}`, `{3:+0;-0}`), abban a sorrendben, amelyet az Ön nyelve megkövetel.
- A hiányzó vagy üres bejegyzések olaszul jelennek meg. Az összes kulcs listája a `data/lingue/chiavi.txt` (a `tools/estrai_chiavi.py` generálja, ne szerkessze).

Szerkessze a fájlt a telepítése `data/lingue` mappájában, és indítsa újra a YA-MS-t (vagy váltson nyelvet), hogy lássa az eredményt. Mivel ezeket a fájlokat **minden frissítéskor újabb változatok váltják fel**, kérjük, **küldje el a javításait** is – e-mailben vagy pull requestként a GitHubon (`data/lingue/`) –, hogy bekerüljenek a következő kiadásba.

Ez a wiki 36 nyelven érhető el (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); a wikioldalak javításait is szívesen fogadjuk.
