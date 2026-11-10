[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · **Polski** · [Čeština](Contributing-and-Contacts-cs) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Współpraca i kontakt

YA-MS rozwija się dzięki zgłoszeniom osób, które używają go w eterze. Każda poprawka jest przypisywana jej źródłu.

## Kontakt

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Zgłaszanie problemu

Otwórz **zgłoszenie (issue) na GitHubie** lub napisz e-mail, podając:

- system operacyjny i wersję YA-MS (w tytule okna);
- oba lokatory, pasmo i godzinę UTC;
- czego się spodziewałeś i co zobaczyłeś (zrzut ekranu pomaga);
- w przypadku problemów z radarem: komunikat wyświetlony w zakładce [Strumień radarowy](Radar-Flux-pl).

## Co jest szczególnie przydatne

- **Raporty z eteru.** Godziny i trasy, dla których efektywność lub prognoza się sprawdziły – albo nie. Model jest eksperymentalny i wymaga porównania z rzeczywistymi QSO oraz z MCG_MS / MS-Soft.
- **Porównania z RMOB.** Wartości współczynnika stacji K i wykładnika k, które uzyskałeś dzięki [porównaniu z RMOB](Experimental-Forecasts-pl#porównanie-z-rmob), wraz z pasmem i opisem stacji.
- **Dane ze źródłem.** Lepsze przesunięcia radiantów, profile aktywności, nowe daty maksimów IMO (`data/massimi_imo.csv`), dane anten: podaj źródło, a zostanie zacytowane.
- **Zmiany wykresów radarowych.** Jeśli zmieni się format wykresu z Collm, kopia obrazu (`data/radar/`) pomaga ponownie skalibrować odczyt.

## Tłumaczenia

Tłumaczenia interfejsu to zwykłe pliki tekstowe w **`data/lingue/<code>.txt`** (UTF-8) i **każdy może je poprawiać**:

```
<Italian text><TAB><translation>
```

- Jeden wpis na wiersz; wiersze zaczynające się od `#` to komentarze.
- W obu kolumnach dwa znaki `\n` oznaczają podział wiersza.
- Zachowaj symbole zastępcze `{0}`, `{1}`, … wraz z ich formatem (np. `{0:F1}`, `{3:+0;-0}`), w kolejności, jakiej wymaga twój język.
- Brakujące lub puste wpisy są wyświetlane po włosku. Lista wszystkich kluczy to `data/lingue/chiavi.txt` (generowana przez `tools/estrai_chiavi.py`, nie edytuj jej).

Edytuj plik w folderze `data/lingue` swojej instalacji i uruchom YA-MS ponownie (lub zmień język), aby zobaczyć wynik. Ponieważ te pliki są **zastępowane nowszymi wersjami przy każdej aktualizacji**, prosimy też o **przesłanie poprawek** – e-mailem lub jako pull request na GitHubie (`data/lingue/`) – aby trafiły do następnego wydania.

Ta wiki istnieje w 36 językach (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文 (简体), 中文 (繁體)); poprawki do stron wiki również są mile widziane.
