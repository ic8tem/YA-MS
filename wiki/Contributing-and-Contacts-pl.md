LANGBAR

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
