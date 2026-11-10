[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · **Norsk** · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [ไทย](Live-Traffic-th) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafikk direkte

*Fane: Direkte og sanntidsdata › Trafikk direkte.*

[![Trafikk direkte](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Hva den viser

Et **asimutalt ekvidistant kart** sentrert på stasjonen din (avstand fra sentrum = faktisk avstand, vinkel = asimut) med **all meteor scatter-trafikk** samlet inn av [Datainnsamling](Data-Collection-nb). For hver forbindelse tegner programmet:

- **strekningen** mellom de to stasjonene, i fargen til båndet: 28 MHz brun, 50 MHz grønn, 70 MHz cyan, 144 MHz oransje, 222 MHz rosa, 432 MHz fiolett;
- de to **stasjonene** i hver ende av strekningen;
- **skyen**: der de mest sannsynlige meteorsporene for den strekningen og det tidspunktet er samlet.

Spot med en stasjon **utenfor kartet** forkastes. Et spot som **nettopp har kommet** (ikke eldre enn 3 minutter), **blinker i ett minutt**, slik at ny aktivitet springer i øynene.

## Slik beregnes skyen

For hvert spot bygger programmet opp strekningen mellom de to lokatorene (samme geometri som for din egen strekning, se [Geometri og demping](Geometry-and-Path-Loss-nb)) og summerer, på tidspunktet for spottet, punkt for punkt i E-laget **bidragene fra speilrefleksjon for hver aktiv sverm**, vektet med dens ZHR – samme beregning som **PREV-sonene** i [himmelhvelvingen](Sky-View-nb). For hver side av strekningen som har minst 15 % av totalen, er skyen en **ellipse**: sentrum i punktenes vektede middel, halvakser 1,5 ganger kvadratrøttene av egenverdiene til spredningen, hovedakse langs hovedegenvektoren. Når ingen sverm bidrar (bare sporadiske meteorer), er skyene de to klassiske **hot spots**, tegnet stiplet. De fullstendige likningene står i kapittel 10 i beregningshåndboken.

## Kontroller

| Kontroll | Betydning |
|---|---|
| **Kartradius** | 600–3500 km fra stasjonen din. |
| **Spot som vises** | Siste 15 eller 30 minutter, siste time, siste 3 timer, siste 24 timer. |
| **Tabell** | Forbindelser på kartet, nyeste først, i båndfargen; *Sky* angir andelen refleksjoner på hovedsiden, eller *sporadiske*. |
| **Klikk** | På en strekning eller en rad i tabellen: forbindelsen utheves, og boksen viser lokatoren for skyens sentrum, andelen, størrelsen og aksen. |
