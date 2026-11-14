[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · **Dansk** · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Live-trafik

*Fane: Live og realtidsdata › Live-trafik.*

[![Live-trafik](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Hvad den viser

Et **azimutalt ækvidistant kort** centreret på din station (afstand fra centrum = faktisk afstand, vinkel = azimut) med **al meteor scatter-trafik** indsamlet af [Dataindsamling](Data-Collection-da). For hver forbindelse tegner programmet:

- **strækningen** mellem de to stationer i sit bånds farve: 28 MHz brun, 50 MHz grøn, 70 MHz cyan, 144 MHz orange, 222 MHz lyserød, 432 MHz violet;
- de to **stationer** i strækningens ender;
- **skyen**: hvor de mest sandsynlige meteorspor for den strækning og det tidspunkt er samlet.

Spots med en station **uden for kortet** kasseres. Et spot, der **lige er ankommet** (højst 3 minutter gammelt), **blinker i ét minut**, så ny aktivitet springer i øjnene.

Vis hvem der lytter: trekanter i båndets farve markerer de stationer, der ifølge PSKReporter modtager MSK144, FSK441, PSK2K eller JTMS på 28, 50, 70, 144 og 432 MHz i det valgte tidsvindue. Et klik på en trekant viser kaldesignal, lokator, modes og sidste spot. MQTT-strømmen i fanen Dataindsamling skal være forbundet.

Også de aktive monitorer på PSKReporter-kortet: tomme trekanter for stationer, der ses på kortet hos pskreporter.info i MSK144, FSK441, PSK2K eller JTMS, men endnu ikke har modtaget noget spot (MQTT sender kun stationer, der modtager noget). YA-MS spørger PSKReporters opslagstjeneste én mode ad gangen, hvert 3. YA-MS spørger PSKReporters opslagstjeneste én gang hvert 5. minut for alle modes, som tjenestens regler beder om; en monitor bliver på kortet i mindst 11 minutter. minut, som tjenestens regler beder om. Et klik på trekanten viser kaldesignal, lokator, dekoderprogram og tidspunktet, hvor monitoren var aktiv. Tændt fra start.

FT8 over 1100 km uden parallelle strækninger: et FT8-spot (fra PSKReporter MQTT, klustrene eller WSJT-X via UDP) mellem stationer mere end 1100 km fra hinanden, som ikke har parallelle strækninger i de 3 minutter før og efter (samme bånd, midtpunkt inden for 300 km, retning inden for 15°, et andet stationspar), tegnes lysegrønt, og dets række i tabellen nederst til højre blinker altid. Sporadisk E og tropo giver mange nære, parallelle strækninger; et enligt spot kan være et meteorspor. Derfor modtager YA-MS også FT8-spots fra MQTT på 6 m, 4 m, 2 m, 1,25 m og 70 cm (ikke 10 m, for mange). Disse spots kommer ikke i MS-arkivet. Tændt fra start.

WSJT-X-spots via UDP, der vedrører din station (dekodningen indeholder dit kaldesignal: den, der kalder dig eller svarer dig), tegnes med en stiplet linje, der altid blinker, i alle modes og på alle afstande.

Kortet viser kaldesignalerne for begge stationer i hvert spot, én gang pr. station. Projektionen kan være azimutal (centreret på din station) eller Mercator. Værktøjstippet på kolonnen Sky forklarer betydningen.

Spots fra alle bånd vises, også fra bånd der ikke er valgt i Dataindsamling (de gemmes ikke). CW-spots og spots mellem stationer, der ligger for tæt, vises ikke, hvis de kasseres i Dataindsamling.

## Sådan beregnes skyen

For hvert spot opbygger programmet strækningen mellem de to lokatorer (samme geometri som for din egen strækning, se [Geometri og dæmpning](Geometry-and-Path-Loss-da)) og lægger, på spottets tidspunkt, punkt for punkt i E-laget **bidragene fra spejlende refleksion for hver aktiv sværm** sammen, vægtet med dens ZHR – samme beregning som **PREV-zonerne** i [himmelkuplen](Sky-View-da). For hver side af strækningen, der har mindst 15 % af det samlede, er skyen en **ellipse**: centrum i punkternes vægtede middelværdi, halvakser 1,5 gange kvadratrødderne af egenværdierne for deres spredning, storakse langs hovedegenvektoren. Når ingen sværm bidrager (kun sporadiske meteorer), er skyerne de to klassiske **hot spots**, tegnet stiplet. De fulde ligninger står i kapitel 10 i beregningsmanualen.

## Betjening

| Element | Betydning |
|---|---|
| **Kortradius** | 600–3500 km fra din station. |
| **Spots der vises** | Seneste 15 eller 30 minutter, seneste time, seneste 3 timer, seneste 24 timer. |
| **Tabel** | Forbindelser på kortet, nyeste først, i båndets farve; *Sky* angiver andelen af refleksioner på hovedsiden eller *sporadiske*. |
| **Klik** | På en strækning eller en række i tabellen: forbindelsen fremhæves, og boksen viser lokatoren for skyens centrum, dens andel, størrelse og akse. |
