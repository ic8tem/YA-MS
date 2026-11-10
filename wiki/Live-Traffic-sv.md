[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · **Svenska** · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafik live

*Flik: Live och realtidsdata › Trafik live.*

[![Trafik live](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Vad den visar

En **azimutal ekvidistant karta** centrerad på din station (avstånd från mitten = verkligt avstånd, vinkel = azimut) med **all meteorscattertrafik** som samlats in av [Datainsamling](Data-Collection-sv). För varje förbindelse ritar programmet:

- **sträckan** mellan de två stationerna, i bandets färg: 28 MHz brun, 50 MHz grön, 70 MHz cyan, 144 MHz orange, 222 MHz rosa, 432 MHz violett;
- de två **stationerna** i sträckans ändar;
- **molnet**: där de mest sannolika meteorspåren för den sträckan och den tidpunkten är koncentrerade.

Spots med en station **utanför kartan** kasseras. En spot som **just har kommit in** (högst 3 minuter gammal) **blinkar i en minut**, så att ny aktivitet syns med en gång.

## Hur molnet beräknas

För varje spot bygger programmet sträckan mellan de två lokatorerna (samma geometri som för din egen sträcka, se [Geometri och dämpning](Geometry-and-Path-Loss-sv)) och summerar, vid tidpunkten för spoten, punkt för punkt i E-skiktet **spegelreflexionsbidragen från varje aktiv svärm**, viktade med dess ZHR – samma beräkning som för **PREV-zonerna** i [himlavalvet](Sky-View-sv). För varje sida av sträckan som har minst 15 % av totalen är molnet en **ellips**: mittpunkt i punkternas viktade medelvärde, halvaxlar 1,5 gånger kvadratrötterna ur egenvärdena för deras spridning, storaxel längs den huvudsakliga egenvektorn. När ingen svärm bidrar (endast sporadiska meteorer) är molnen de två klassiska **hot spots**, ritade streckade. De fullständiga ekvationerna finns i kapitel 10 i beräkningshandboken.

## Reglage

| Reglage | Betydelse |
|---|---|
| **Kartradie** | 600–3500 km från din station. |
| **Spots att visa** | Senaste 15 eller 30 minuterna, senaste timmen, senaste 3 timmarna, senaste 24 timmarna. |
| **Tabell** | Förbindelserna på kartan, nyaste först, i bandets färg; *Moln* anger andelen reflexer på huvudsidan, eller *sporadiska*. |
| **Klick** | På en sträcka eller en tabellrad: förbindelsen markeras och rutan visar lokatorn för molnets mittpunkt, dess andel, storlek och axel. |
