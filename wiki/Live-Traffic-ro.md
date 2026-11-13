[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · **Română** · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafic live

*Filă: Date live și în timp real › Trafic live.*

[![Trafic live](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ce arată

O **hartă azimutală echidistantă** centrată pe stația dumneavoastră (distanța de la centru = distanța reală, unghiul = azimutul) cu **întregul trafic meteor-scatter** adunat de [Colectare date](Data-Collection-ro). Pentru fiecare legătură programul desenează:

- **traseul** dintre cele două stații, în culoarea benzii sale: 28 MHz maro, 50 MHz verde, 70 MHz cyan, 144 MHz portocaliu, 222 MHz roz, 432 MHz violet;
- cele două **stații** de la capetele traseului;
- **norul**: unde se concentrează cele mai probabile urme de meteori pentru acel traseu și acea oră.

Spoturile cu o stație **în afara hărții** sunt eliminate. Un spot **abia sosit** (nu mai vechi de 3 minute) **clipește timp de un minut**, astfel încât activitatea nouă iese în evidență dintr-o privire.

Arată cine ascultă: triunghiuri în culoarea benzii marchează stațiile care, după PSKReporter, recepționează MSK144, FSK441, PSK2K sau JTMS pe 28, 50, 70, 144 și 432 MHz în fereastra de timp aleasă. Un clic pe un triunghi arată indicativul, locatorul, modurile și ultimul spot. Fluxul MQTT din fila Colectare date trebuie să fie conectat.

Se văd spoturile tuturor benzilor, inclusiv ale celor nealese în Colectarea datelor (acestea nu se memorează). Spoturile CW și cele între stații prea apropiate nu se văd, dacă sunt eliminate în Colectarea datelor.

## Cum se calculează norul

Pentru fiecare spot, programul construiește traseul dintre cei doi locatori (aceeași geometrie ca pentru propriul traseu, vedeți [Geometrie și atenuare pe traseu](Geometry-and-Path-Loss-ro)) și, la ora spotului, adună punct cu punct al stratului E **contribuțiile de reflexie speculară ale fiecărui roi activ**, ponderate cu ZHR-ul său – același calcul ca pentru **zonele PREV** din [bolta cerească](Sky-View-ro). Pentru fiecare latură a traseului care deține cel puțin 15 % din total, norul este o **elipsă**: centrul în media ponderată a punctelor, semiaxele de 1,5 ori rădăcinile pătrate ale valorilor proprii ale dispersiei lor, axa mare de-a lungul vectorului propriu principal. Când niciun roi nu contribuie (doar meteori sporadici), norii sunt cele două **hot spot-uri** clasice, desenate punctat. Ecuațiile complete se află în capitolul 10 al manualului de calcul.

## Comenzi

| Comandă | Semnificație |
|---|---|
| **Raza hărții** | 600–3500 km de la stația dumneavoastră. |
| **Spoturi de afișat** | Ultimele 15 sau 30 de minute, ultima oră, ultimele 3 ore, ultimele 24 de ore. |
| **Tabel** | Legăturile de pe hartă, cele mai noi primele, în culoarea benzii; *Nor* dă ponderea reflexiilor pe latura principală sau *sporadici*. |
| **Clic** | Pe un traseu sau pe un rând din tabel: legătura este evidențiată, iar caseta arată locatorul centrului norului, ponderea, dimensiunea și axa sa. |
