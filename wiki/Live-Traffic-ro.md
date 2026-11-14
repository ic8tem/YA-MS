[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · **Română** · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Trafic live

*Filă: Date live și în timp real › Trafic live.*

[![Trafic live](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ce arată

O **hartă azimutală echidistantă** centrată pe stația dumneavoastră (distanța de la centru = distanța reală, unghiul = azimutul) cu **întregul trafic meteor-scatter** adunat de [Colectare date](Data-Collection-ro). Pentru fiecare legătură programul desenează:

- **traseul** dintre cele două stații, în culoarea benzii sale: 28 MHz maro, 50 MHz verde, 70 MHz cyan, 144 MHz portocaliu, 222 MHz roz, 432 MHz violet;
- cele două **stații** de la capetele traseului;
- **zona roiului**: unde se concentrează cele mai probabile urme de meteori pentru acel traseu și acea oră.

Spoturile cu o stație **în afara hărții** sunt eliminate. Un spot **abia sosit** (nu mai vechi de 3 minute) **clipește timp de un minut**, astfel încât activitatea nouă iese în evidență dintr-o privire.

Arată cine ascultă: triunghiuri în culoarea benzii marchează stațiile care, după PSKReporter, recepționează MSK144, FSK441, PSK2K sau JTMS pe 28, 50, 70, 144 și 432 MHz în fereastra de timp aleasă. Un clic pe un triunghi arată indicativul, locatorul, modurile și ultimul spot. Fluxul MQTT din fila Colectare date trebuie să fie conectat.

Și monitoarele active de pe harta PSKReporter: triunghiuri goale pentru stațiile care apar pe harta pskreporter.info în MSK144, FSK441, PSK2K sau JTMS dar nu au recepționat încă niciun spot (MQTT trimite doar stațiile care recepționează ceva). YA-MS interoghează serviciul de consultare PSKReporter o dată la 5 minute pentru toate modurile, cum cer regulile serviciului; un monitor rămâne pe hartă cel puțin 11 minute. Un clic pe triunghi arată indicativul, locatorul, programul de decodare și ora la care monitorul era activ. Activat implicit.

FT8 peste 1100 km fără trasee paralele: un spot FT8 (din PSKReporter MQTT, din clustere sau din WSJT-X prin UDP) între stații aflate la peste 1100 km care nu are trasee paralele în cele 3 minute dinainte și de după (aceeași bandă, punct de mijloc la cel mult 300 km, direcție în 15°, altă pereche de stații) se desenează în verde deschis, iar rândul său din tabelul din dreapta jos clipește mereu. E sporadic și tropo dau multe trasee apropiate și paralele; un spot izolat poate fi o urmă meteorică. De aceea YA-MS primește prin MQTT și spoturile FT8 de pe 6 m, 4 m, 2 m, 1,25 m și 70 cm (niciodată 28 MHz, în niciun caz). Aceste spoturi nu intră în arhiva MS. Activat implicit. Verificări suplimentare cu PSKReporter MQTT: spotul nu este izolat dacă stația receptoare aude în MQTT alte stații de peste 1100 km pe aceeași bandă în 3 minute (bandă deschisă); spoturile din clustere și RBN contează doar dacă aceeași pereche vine și din MQTT; skimmerele RBN (indicative cu «-#») nu contează niciodată.

Spoturile WSJT-X prin UDP care privesc stația dvs. (decodarea conține indicativul dvs.: cine vă cheamă sau vă răspunde) se desenează cu o linie întreruptă care clipește mereu, în orice mod și la orice distanță.

Schimb între utilizatorii YA-MS: când un alt utilizator YA-MS decodează prin UDP un mesaj adresat stației dvs. (în MSK144, FSK441, PSK2K sau JTMS, ori în FT8 peste 1100 km), YA-MS-ul lui vi-l trimite criptat prin trei brokeri MQTT publici (HiveMQ, Mosquitto, EMQX); îl vedeți ca linie întreruptă violet care clipește mereu și ca rând în consola UDP. Doar dvs. îl puteți citi (chei ECDH P-256, AES-256 și HMAC-SHA256). Spoturile FT8 apar doar dacă nu au trasee paralele în 3 minute. Activat implicit; yams_scambio=0 în data/config.ini îl oprește.

Harta scrie indicativele ambelor stații ale fiecărui spot, o singură dată pe stație. Proiecția se alege între azimutală (centrată pe stația ta) și Mercator. Indiciul de pe coloana zona roiului îi explică semnificația.

Se văd spoturile tuturor benzilor, inclusiv ale celor nealese în Colectarea datelor (acestea nu se memorează). Spoturile CW și cele între stații prea apropiate nu se văd, dacă sunt eliminate în Colectarea datelor.

## Cum se calculează zona roiului

Pentru fiecare spot, programul construiește traseul dintre cei doi locatori (aceeași geometrie ca pentru propriul traseu, vedeți [Geometrie și atenuare pe traseu](Geometry-and-Path-Loss-ro)) și, la ora spotului, adună punct cu punct al stratului E **contribuțiile de reflexie speculară ale fiecărui roi activ**, ponderate cu ZHR-ul său – același calcul ca pentru **zonele PREV** din [bolta cerească](Sky-View-ro). Pentru fiecare latură a traseului care deține cel puțin 15 % din total, zona roiului este o **elipsă**: centrul în media ponderată a punctelor, semiaxele de 1,5 ori rădăcinile pătrate ale valorilor proprii ale dispersiei lor, axa mare de-a lungul vectorului propriu principal. Când niciun roi nu contribuie (doar meteori sporadici), zona roiului sunt cele două **hot spot-uri** clasice, desenate punctat. Ecuațiile complete se află în capitolul 10 al manualului de calcul.

## Comenzi

| Comandă | Semnificație |
|---|---|
| **Raza hărții** | 600–3500 km de la stația dumneavoastră. |
| **Spoturi de afișat** | Ultimele 15 sau 30 de minute, ultima oră, ultimele 3 ore, ultimele 24 de ore. |
| **Tabel** | Legăturile de pe hartă, cele mai noi primele, în culoarea benzii; *% roi* dă ponderea reflexiilor pe latura principală sau *sporadici*. |
| **Clic** | Pe un traseu sau pe un rând din tabel: legătura este evidențiată, iar caseta arată locatorul centrului norului, ponderea, dimensiunea și axa sa. |
