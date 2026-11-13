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
