[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · **Polski** · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Ruch na żywo

*Zakładka: Dane na żywo i w czasie rzeczywistym › Ruch na żywo.*

[![Ruch na żywo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Co pokazuje

**Mapa azymutalna równoodległościowa** wyśrodkowana na twojej stacji (odległość od środka = rzeczywista odległość, kąt = azymut) z **całym ruchem meteor scatter** zebranym przez zakładkę [Zbieranie danych](Data-Collection-pl). Dla każdej łączności program rysuje:

- **trasę** między dwiema stacjami, w kolorze jej pasma: 28 MHz brązowy, 50 MHz zielony, 70 MHz cyjan, 144 MHz pomarańczowy, 222 MHz różowy, 432 MHz fioletowy;
- obie **stacje** na końcach trasy;
- **chmurę**: miejsce, w którym koncentrują się najbardziej prawdopodobne ślady meteorów dla tej trasy i tej pory.

Spoty ze stacją **poza mapą** są odrzucane. Spot, który **właśnie nadszedł** (nie starszy niż 3 minuty), **miga przez minutę**, dzięki czemu nowa aktywność od razu rzuca się w oczy.

Pokaż, kto nasłuchuje: trójkąty w kolorze pasma oznaczają stacje, które według PSKReportera odbierają MSK144, FSK441, PSK2K lub JTMS na 28, 50, 70, 144 i 432 MHz w wybranym oknie czasu. Kliknięcie trójkąta pokazuje znak, lokator, emisje i ostatni spot. Strumień MQTT z zakładki Zbieranie danych musi być połączony.

Również aktywne monitory z mapy PSKReporter: puste trójkąty dla stacji widocznych na mapie pskreporter.info w MSK144, FSK441, PSK2K lub JTMS, które nie odebrały jeszcze żadnego spotu (MQTT wysyła tylko stacje, które coś odbierają). YA-MS odpytuje usługę wyszukiwania PSKReporter raz na 5 minut dla wszystkich emisji, jak wymagają zasady usługi; monitor pozostaje na mapie co najmniej 11 minut. Kliknięcie trójkąta pokazuje znak, lokator, program dekodujący i godzinę, o której monitor był aktywny. Domyślnie włączone.

FT8 powyżej 1100 km bez równoległych tras: spot FT8 (z PSKReporter MQTT, z clusterów lub z WSJT-X przez UDP) między stacjami oddalonymi o ponad 1100 km, który w ciągu 3 minut przed i po nie ma równoległych tras (to samo pasmo, punkt środkowy w promieniu 300 km, kierunek w granicach 15°, inna para stacji), rysuje się na jasnozielono, a jego wiersz w tabeli w prawym dolnym rogu zawsze miga. Sporadyczne E i tropo dają wiele bliskich, równoległych tras; pojedynczy spot może być śladem meteoru. Dlatego YA-MS odbiera z MQTT także spoty FT8 z 6 m, 4 m, 2 m, 1,25 m i 70 cm (nie z 10 m, jest ich za dużo). Te spoty nie trafiają do archiwum MS. Domyślnie włączone.

Spoty WSJT-X przez UDP dotyczące twojej stacji (dekodowanie zawiera twój znak: kto cię woła lub ci odpowiada) rysuje się zawsze migającą linią przerywaną, w każdej emisji i na każdą odległość.

Na mapie pisane są znaki obu stacji każdego spotu, raz dla każdej stacji. Odwzorowanie można wybrać: azymutalne (w środku twoja stacja) lub Mercatora. Podpowiedź na kolumnie Chmura wyjaśnia jej znaczenie.

Pokazywane są spoty ze wszystkich pasm, także z tych niewybranych w Zbieraniu danych (tych się nie zapisuje). Spoty CW i spoty między zbyt bliskimi stacjami nie są pokazywane, jeśli są odrzucane w Zbieraniu danych.

## Jak obliczana jest chmura

Dla każdego spotu program tworzy trasę między dwoma lokatorami (ta sama geometria co dla twojej trasy, zob. [Geometria i tłumienie trasy](Geometry-and-Path-Loss-pl)) i dla momentu spotu sumuje, punkt po punkcie warstwy E, **przyczynki odbicia zwierciadlanego od każdego aktywnego roju**, ważone jego ZHR – to te same obliczenia co dla **stref PREV** na [kopule nieba](Sky-View-pl). Dla każdej strony trasy, na którą przypada co najmniej 15 % całości, chmura jest **elipsą**: środek w średniej ważonej punktów, półosie równe 1,5-krotności pierwiastków kwadratowych wartości własnych ich rozrzutu, oś wielka wzdłuż głównego wektora własnego. Gdy żaden rój nie wnosi wkładu (tylko meteory sporadyczne), chmurami są dwa klasyczne **hot spoty**, rysowane linią przerywaną. Pełne równania znajdują się w rozdziale 10 podręcznika obliczeń.

## Elementy sterujące

| Element | Znaczenie |
|---|---|
| **Promień mapy** | 600–3500 km od twojej stacji. |
| **Wyświetlane spoty** | Ostatnie 15 lub 30 minut, ostatnia godzina, ostatnie 3 godziny, ostatnie 24 godziny. |
| **Tabela** | Łączności na mapie, od najnowszych, w kolorze pasma; *Chmura* podaje udział odbić po stronie głównej albo *sporadyczne*. |
| **Kliknięcie** | Na trasie lub wierszu tabeli: łączność zostaje wyróżniona, a ramka pokazuje lokator środka chmury, jej udział, rozmiar i oś. |
