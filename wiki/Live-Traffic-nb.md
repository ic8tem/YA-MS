**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

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
