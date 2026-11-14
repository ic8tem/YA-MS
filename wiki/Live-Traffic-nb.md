[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · **Norsk** · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafikk direkte

*Fane: Direkte og sanntidsdata › Trafikk direkte.*

[![Trafikk direkte](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Hva den viser

Et **asimutalt ekvidistant kart** sentrert på stasjonen din (avstand fra sentrum = faktisk avstand, vinkel = asimut) med **all meteor scatter-trafikk** samlet inn av [Datainnsamling](Data-Collection-nb). For hver forbindelse tegner programmet:

- **strekningen** mellom de to stasjonene, i fargen til båndet: 28 MHz brun, 50 MHz grønn, 70 MHz cyan, 144 MHz oransje, 222 MHz rosa, 432 MHz fiolett;
- de to **stasjonene** i hver ende av strekningen;
- **skyen**: der de mest sannsynlige meteorsporene for den strekningen og det tidspunktet er samlet.

Spot med en stasjon **utenfor kartet** forkastes. Et spot som **nettopp har kommet** (ikke eldre enn 3 minutter), **blinker i ett minutt**, slik at ny aktivitet springer i øynene.

Vis hvem som lytter: trekanter i båndets farge markerer stasjonene som ifølge PSKReporter tar imot MSK144, FSK441, PSK2K eller JTMS på 28, 50, 70, 144 og 432 MHz i det valgte tidsvinduet. Et klikk på en trekant viser kallesignal, lokator, moduser og siste spot. MQTT-strømmen i fanen Datainnsamling må være tilkoblet.

Også de aktive monitorene på PSKReporter-kartet: tomme trekanter for stasjoner som vises på kartet til pskreporter.info i MSK144, FSK441, PSK2K eller JTMS, men som ennå ikke har mottatt noen spot (MQTT sender bare stasjoner som mottar noe). YA-MS spør PSKReporters oppslagstjeneste én modus om gangen, hvert 3. YA-MS spør PSKReporters oppslagstjeneste én gang hvert 5. minutt for alle moduser, slik tjenestens regler ber om; en monitor blir værende på kartet i minst 11 minutter. minutt, slik tjenestens regler ber om. Et klikk på trekanten viser kallesignal, lokator, dekodingsprogram og tidspunktet monitoren var aktiv. På fra start.

FT8 over 1100 km uten parallelle strekninger: en FT8-spot (fra PSKReporter MQTT, klustrene eller WSJT-X via UDP) mellom stasjoner mer enn 1100 km fra hverandre som ikke har parallelle strekninger i de 3 minuttene før og etter (samme bånd, midtpunkt innen 300 km, retning innen 20°, et annet stasjonspar) tegnes lysegrønn, og raden i tabellen nede til høyre blinker alltid. Sporadisk E og tropo gir mange nære, parallelle strekninger; en enslig spot kan være et meteorspor. Derfor mottar YA-MS også FT8-spotter fra MQTT på 6 m, 4 m, 2 m, 1,25 m og 70 cm (ikke 10 m, for mange). Disse spottene går ikke inn i MS-arkivet. På fra start.

WSJT-X-spotter via UDP som gjelder stasjonen din (dekodingen inneholder kallesignalet ditt: den som kaller deg eller svarer deg) tegnes med en stiplet linje som alltid blinker, i alle moduser og på alle avstander.

Kartet viser kallesignalene til begge stasjonene i hver spot, én gang per stasjon. Projeksjonen kan være asimutal (sentrert på din stasjon) eller Mercator. Verktøytipset på kolonnen Sky forklarer hva den betyr.

Spotter fra alle bånd vises, også fra bånd som ikke er valgt i Datainnsamling (de lagres ikke). CW-spotter og spotter mellom stasjoner som ligger for nær hverandre vises ikke, hvis de forkastes i Datainnsamling.

## Slik beregnes skyen

For hvert spot bygger programmet opp strekningen mellom de to lokatorene (samme geometri som for din egen strekning, se [Geometri og demping](Geometry-and-Path-Loss-nb)) og summerer, på tidspunktet for spottet, punkt for punkt i E-laget **bidragene fra speilrefleksjon for hver aktiv sverm**, vektet med dens ZHR – samme beregning som **PREV-sonene** i [himmelhvelvingen](Sky-View-nb). For hver side av strekningen som har minst 15 % av totalen, er skyen en **ellipse**: sentrum i punktenes vektede middel, halvakser 1,5 ganger kvadratrøttene av egenverdiene til spredningen, hovedakse langs hovedegenvektoren. Når ingen sverm bidrar (bare sporadiske meteorer), er skyene de to klassiske **hot spots**, tegnet stiplet. De fullstendige likningene står i kapittel 10 i beregningshåndboken.

## Kontroller

| Kontroll | Betydning |
|---|---|
| **Kartradius** | 600–3500 km fra stasjonen din. |
| **Spot som vises** | Siste 15 eller 30 minutter, siste time, siste 3 timer, siste 24 timer. |
| **Tabell** | Forbindelser på kartet, nyeste først, i båndfargen; *Sky* angir andelen refleksjoner på hovedsiden, eller *sporadiske*. |
| **Klikk** | På en strekning eller en rad i tabellen: forbindelsen utheves, og boksen viser lokatoren for skyens sentrum, andelen, størrelsen og aksen. |
