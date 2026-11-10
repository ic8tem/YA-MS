[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · **Polski** · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [ไทย](Live-Traffic-th) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Ruch na żywo

*Zakładka: Na żywo i dane w czasie rzeczywistym › Ruch na żywo.*

[![Ruch na żywo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Co pokazuje

**Mapa azymutalna równoodległościowa** wyśrodkowana na twojej stacji (odległość od środka = rzeczywista odległość, kąt = azymut) z **całym ruchem meteor scatter** zebranym przez [Zbieranie danych](Data-Collection-pl). Dla każdej łączności program rysuje:

- **trasę** między dwiema stacjami, w kolorze jej pasma: 28 MHz brązowy, 50 MHz zielony, 70 MHz cyjan, 144 MHz pomarańczowy, 222 MHz różowy, 432 MHz fioletowy;
- dwie **stacje** na końcach trasy;
- **obłok**: miejsce, w którym skupiają się najbardziej prawdopodobne ślady meteorów dla tej trasy i tego czasu.

Spoty ze stacją **poza mapą** są odrzucane. Spot, który **właśnie nadszedł** (nie starszy niż 3 minuty), **miga przez minutę**, dzięki czemu nowa aktywność od razu rzuca się w oczy.

## Jak obliczany jest obłok

Dla każdego spotu program buduje trasę między dwoma lokatorami (ta sama geometria co dla twojej trasy, zob. [Geometria i tłumienie](Geometry-and-Path-Loss-pl)) i w chwili spotu sumuje punkt po punkcie warstwy E **wkłady odbicia zwierciadlanego od każdego aktywnego roju**, ważone jego ZHR – to samo obliczenie co dla **stref PREV** na [sklepieniu niebieskim](Sky-View-pl). Dla każdej strony trasy, na którą przypada co najmniej 15 % całości, obłok jest **elipsą**: środek w średniej ważonej punktów, półosie równe 1,5 pierwiastka kwadratowego z wartości własnych ich rozrzutu, oś wielka wzdłuż głównego wektora własnego. Gdy żaden rój nie wnosi wkładu (tylko meteory sporadyczne), obłokami są dwa klasyczne **hot spoty**, rysowane linią przerywaną. Pełne równania są w rozdziale 10 podręcznika obliczeń.

## Elementy sterujące

| Element | Znaczenie |
|---|---|
| **Promień mapy** | 600–3500 km od twojej stacji. |
| **Spoty do wyświetlenia** | Ostatnie 15 lub 30 minut, ostatnia godzina, ostatnie 3 godziny, ostatnie 24 godziny. |
| **Tabela** | Łączności na mapie, najnowsze na górze, w kolorze pasma; *Obłok* podaje udział odbić po stronie głównej albo *sporadyczne*. |
| **Kliknięcie** | Na trasie lub wierszu tabeli: łączność zostaje wyróżniona, a ramka pokazuje lokator środka obłoku, jego udział, rozmiar i oś. |
