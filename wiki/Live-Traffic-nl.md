**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Verkeer live

*Tabblad: Live en realtimegegevens › Verkeer live.*

[![Verkeer live](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/nl-1_1.png)

## Wat het toont

Een **azimutale equidistante kaart** gecentreerd op jouw station (afstand tot het midden = werkelijke afstand, hoek = azimut) met **al het meteorscatter-verkeer** dat door [Gegevensverzameling](Data-Collection-nl) is verzameld. Voor elk contact tekent het programma:

- het **traject** tussen de twee stations, in de kleur van zijn band: 28 MHz bruin, 50 MHz groen, 70 MHz cyaan, 144 MHz oranje, 222 MHz roze, 432 MHz violet;
- de twee **stations** aan de uiteinden van het traject;
- de **wolk**: waar de meest waarschijnlijke meteorensporen voor dat traject en dat tijdstip geconcentreerd zijn.

Spots met een station **buiten de kaart** worden genegeerd. Een spot die **net binnen is** (niet ouder dan 3 minuten) **knippert een minuut lang**, zodat nieuwe activiteit direct opvalt.

## Hoe de wolk wordt berekend

Voor elke spot bouwt het programma het traject tussen de twee locators op (dezelfde geometrie als voor je eigen traject, zie [Geometrie en demping](Geometry-and-Path-Loss-nl)) en telt op het tijdstip van de spot, punt voor punt in de E-laag, de **bijdragen van spiegelende reflectie van elke actieve zwerm** op, gewogen met zijn ZHR – dezelfde berekening als de **PREV-zones** van de [hemelkoepel](Sky-View-nl). Voor elke zijde van het traject die minstens 15 % van het totaal bevat, is de wolk een **ellips**: middelpunt in het gewogen gemiddelde van de punten, halve assen 1,5 keer de vierkantswortels van de eigenwaarden van hun spreiding, lange as langs de hoofdeigenvector. Als geen enkele zwerm bijdraagt (alleen sporadische meteoren), zijn de wolken de twee klassieke **hotspots**, gestippeld getekend. De volledige vergelijkingen staan in hoofdstuk 10 van de rekenhandleiding.

## Bediening

| Element | Betekenis |
|---|---|
| **Kaartstraal** | 600–3500 km vanaf jouw station. |
| **Te tonen spots** | Laatste 15 of 30 minuten, laatste uur, laatste 3 uur, laatste 24 uur. |
| **Tabel** | Contacten op de kaart, nieuwste bovenaan, in de kleur van de band; *Wolk* geeft het aandeel reflecties aan de hoofdzijde, of *sporadische*. |
| **Klik** | Op een traject of een tabelregel: het contact wordt gemarkeerd en het vak toont de locator van het midden van de wolk, het aandeel, de afmetingen en de as. |
