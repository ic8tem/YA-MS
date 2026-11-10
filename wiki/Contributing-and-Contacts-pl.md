[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · **Polski** · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Współpraca i kontakt

YA-MS rozwija się dzięki zgłoszeniom osób, które używają go na paśmie. Każda poprawka jest przypisywana swojemu źródłu.

## Kontakt

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Zgłaszanie problemu

Otwórz **zgłoszenie (issue) na GitHubie** lub napisz e-mail, podając:

- system operacyjny i wersję YA-MS (widoczną w tytule okna);
- oba lokatory, pasmo i czas UTC;
- czego się spodziewałeś, a co zobaczyłeś (zrzut ekranu bardzo pomaga);
- w przypadku problemów z radarem – komunikat wyświetlany w zakładce [Strumień radarowy](Radar-Flux-pl).

## Co jest szczególnie przydatne

- **Raporty z pasma.** Godziny i trasy, dla których efektywność lub prognoza się sprawdziły – albo nie. Model jest eksperymentalny i wymaga porównania z rzeczywistymi QSO oraz z MCG_MS / MS-Soft.
- **Porównania z RMOB.** Wartości współczynnika stacji K i wykładnika k, które wyznaczyłeś za pomocą [porównania z RMOB](Experimental-Forecasts-pl#porównanie-z-rmob), wraz z twoim pasmem i stacją.
- **Dane ze źródłem.** Lepsze dryfy radiantów, profile aktywności, nowe daty maksimów IMO (`data/massimi_imo.csv`), dane anten: podaj źródło, a zostanie ono zacytowane.
- **Zmiany wykresów radarowych.** Jeśli zmieni się format wykresu z Collm, kopia obrazu (`data/radar/`) pomoże ponownie skalibrować odczyt.

## Tłumaczenia

Tłumaczenia interfejsu to zwykłe pliki tekstowe w **`data/lingue/<code>.txt`** (UTF-8) i **każdy może je poprawiać**:

```
<Italian text><TAB><translation>
```

- Jeden wpis w wierszu; wiersze zaczynające się od `#` są komentarzami.
- W obu kolumnach dwa znaki `\n` oznaczają przejście do nowego wiersza.
- Zachowaj symbole zastępcze `{0}`, `{1}`, … wraz z ich formatem (np. `{0:F1}`, `{3:+0;-0}`), w kolejności wymaganej przez twój język.
- Brakujące lub puste wpisy są wyświetlane po włosku. Lista wszystkich kluczy znajduje się w `data/lingue/chiavi.txt` (generowanym przez `tools/estrai_chiavi.py`, nie edytuj go).

Edytuj plik w folderze `data/lingue` swojej instalacji i uruchom YA-MS ponownie (albo przełącz język), aby zobaczyć efekt. Ponieważ te pliki są **zastępowane nowszymi wersjami przy każdej aktualizacji**, prosimy, **wyślij też swoje poprawki** – e-mailem lub jako pull request na GitHubie (`data/lingue/`) – aby trafiły do następnego wydania.

Ta wiki istnieje w 28 językach (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文); poprawki do stron wiki są również mile widziane.
