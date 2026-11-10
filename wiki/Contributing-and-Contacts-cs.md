[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · **Čeština** · [Română](Contributing-and-Contacts-ro) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Přispívání a kontakty

YA-MS se zlepšuje díky hlášením lidí, kteří ho používají na pásmu. Každá oprava je připsána svému zdroji.

## Kontakty

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Nahlášení problému

Otevřete **issue na GitHubu** nebo napište e-mail s těmito údaji:

- operační systém a verze YA-MS (v titulku okna);
- oba lokátory, pásmo a čas UTC;
- co jste očekávali a co jste viděli (pomůže snímek obrazovky);
- u problémů s radarem zpráva zobrazená na kartě [Tok z radaru](Radar-Flux-cs).

## Co je zvlášť užitečné

- **Hlášení z pásma.** Hodiny a trasy, kde účinnost nebo předpověď vyšly – nebo nevyšly. Model je experimentální a potřebuje srovnání se skutečnými QSO a s MCG_MS / MS-Soft.
- **Srovnání s RMOB.** Hodnoty faktoru stanice K a exponentu k, které jste zjistili pomocí [srovnání s RMOB](Experimental-Forecasts-cs#srovnání-s-rmob), s vaším pásmem a stanicí.
- **Data se zdrojem.** Lepší posuny radiantů, profily aktivity, nová data maxim podle IMO (`data/massimi_imo.csv`), údaje o anténách: uveďte zdroj a bude citován.
- **Změny grafů radarů.** Pokud se změní formát grafu z Collmu, kopie snímku (`data/radar/`) pomůže čtení znovu zkalibrovat.

## Překlady

Překlady rozhraní jsou prosté textové soubory v **`data/lingue/<code>.txt`** (UTF-8) a **opravit je může kdokoli**:

```
<Italian text><TAB><translation>
```

- Jedna položka na řádek; řádky začínající `#` jsou komentáře.
- V obou sloupcích znamenají dva znaky `\n` zalomení řádku.
- Zachovejte zástupné symboly `{0}`, `{1}`, … s jejich formátem (např. `{0:F1}`, `{3:+0;-0}`), v pořadí, které váš jazyk potřebuje.
- Chybějící nebo prázdné položky se zobrazí italsky. Seznam všech klíčů je `data/lingue/chiavi.txt` (generuje ho `tools/estrai_chiavi.py`, neupravujte ho).

Upravte soubor ve složce `data/lingue` vaší instalace a restartujte YA-MS (nebo přepněte jazyk), abyste viděli výsledek. Protože se tyto soubory **při každé aktualizaci nahrazují novějšími verzemi**, **pošlete prosím své opravy** i autorovi – e-mailem nebo jako pull request na GitHubu (`data/lingue/`) – aby se dostaly do příštího vydání.

Tato wiki existuje v 36 jazycích (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); opravy stránek wiki jsou také vítány.
