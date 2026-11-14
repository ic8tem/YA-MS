[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · **Română** · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Primii pași

La prima pornire, YA-MS arată un traseu de exemplu (JN70CN → JO62QM pe 144 MHz). Cinci minute sunt suficiente pentru a-l configura pentru stația dumneavoastră.

## 1. Cele două rânduri de comenzi

Deasupra filelor sunt două rânduri de comenzi, valabile pentru toate filele. Butonul **Comenzi** din dreapta sus le pliază și le desfășoară (util cu fonturi mari); alegerea este memorată. Stația dvs. (locator, altitudine, bandă și Calculează) este în dreapta sus în Trafic în direct.

**Stația mea – Trafic în direct**

| Comandă | Ce face |
|---|---|
| **Locatorul meu** / **înălțime m** | Locatorul dumneavoastră Maidenhead (4, 6 sau 8 caractere; se folosește centrul pătratului) și înălțimea stației deasupra nivelului mării. |
| **Stația DX** / **înălțime m** | Lângă hartă, în dreapta, este caseta corespondentului: scrie indicativul și apasă Enter, locatorul se ia din baza CALL3 (ca în YAEC și LIVETROPOVHF); dedesubt sunt locatorul și altitudinea. Indicativul se poate scrie și în căsuța locatorului. |
| **Bandă MHz** | 28, 50, 70, 144, 222 sau 432 MHz: folosită pentru câștigul și lobul antenei, estimarea fluxului și bilanțul legăturii. |
| **Calculează** | Recalculează traseul (eșantionarea stratului E: câteva secunde). |
| **Az antenă** | Sus în caseta corespondentului, lângă hartă: azimutul antenei dvs., mereu **spre DX** (azimutul traseului). Dedesubt, în aceeași coloană, este legenda hărții. |

**Rândul 1 – stratul E și antena**

| Comandă | Ce face |
|---|---|
| **Înălțimea urmei km** + **de la radar** | Înălțimea urmelor de meteori (implicit 90 km). Cu *de la radar* bifat, se folosește înălțimea cea mai frecventă (moda) măsurată de radarul din Collm; vedeți [Flux radar](Radar-Flux-ro). |
| **Elevația lobului °** | Elevația maximului lobului vertical al antenei tale: o directivă fixată la 0° are totuși lobul la câteva grade deasupra orizontului din cauza reflexiei pe sol (de obicei 3-8°). Cu căsuța **diagrama antenei** activată (implicit), punctele stratului E sunt ponderate cu diagrama verticală a celor două antene; dezactivată, se folosesc doar punctele pe care ambele stații le văd deasupra acestei elevații. |
| **Antenă Yagi: boom m** | Lungimea boom-ului antenei Yagi. Programul arată lungimea în λ, câștigul (curba DL6WU) și lobul la −3 dB, orizontal și vertical; vedeți [Geometrie și atenuare pe traseu](Geometry-and-Path-Loss-ro#câștigul-și-lobul-antenei). Sub 2 λ estimarea este aproximativă. |
| **Hot spot de la punctul median km** + **auto (AMS)** | Distanța lui Hot A și Hot B față de punctul median. Cu *auto (AMS)* bifat (implicit) urmează tabelul de decalare a antenei al lui J. Richardson (AMS) citat de DJ5HG: 13° la 1000 km, 11° la 1250 km, 10° la 1500 și 2000 km (aproximativ 115, 121, 132 și 176 km de la punctul median). Debifați-l pentru a introduce manual 30–400 km (MSHV folosește 150 km). |

**Rândul 2 – ora**

| Comandă | Ce face |
|---|---|
| **Ora** | Ceas UTC. |
| **Data calculului (UTC)** | Ziua calculului pentru [Calcul previzional](Sky-View-ro) și [Radar GRAVES](GRAVES-Radar-ro) (implicit astăzi), la ora curentă a zilei. De asemenea: ziua afișată în [Calculul eficienței](Efficiency-Calculation-ro) și în cronologia GRAVES. |
| **Ore (−12 până la +36 h)** | Mută momentul calculului de la 12 ore înainte până la 36 de ore după acea oră, în pași de 15 minute. Alături: *Calcul pentru: acum* sau *Calcul pentru: zz/ll hh:mm UTC*. |
| **Timp real** | Înapoi la momentul actual. |

Linia timpului («Ore (de la −12 la +36 h)» și «Timp real») este în partea de sus a filei Calcul de prognoză, pentru că se aplică doar acelui calcul.

## 2. Stația dumneavoastră și DX-ul

1. Introduceți **Locatorul meu** și **înălțime m**.
2. Introduceți locatorul și înălțimea **Stației DX** – sau faceți clic pe hartă în [Bolta cerească](Sky-View-ro): **clic stânga = locatorul stației DX**, **clic dreapta = locatorul stației mele**.
3. Alegeți **Bandă MHz** și apăsați **Calculează**.

Bara de stare de jos confirmă: *Traseu calculat: … km, … puncte de reflexie eșantionate în … s*.

## 3. Antena dumneavoastră

Introduceți **lungimea boom-ului** antenei Yagi. Programul deduce câștigul și lobul și vă avertizează dacă Hot A sau Hot B cad deja **în interiorul lobului** când antena este îndreptată spre DX (atunci sunt desenate în gri: nu este nevoie să rotiți antena).

## 4. Citiți rezultatele

| Întrebare | Unde să priviți |
|---|---|
| Ce roi îmi ajută traseul acum și din ce parte? | [Bolta cerească](Sky-View-ro): lista roiurilor, Hot-ul recomandat în roșu, zonele PREV |
| Care este cea mai bună oră astăzi? | [Calculul eficienței](Efficiency-Calculation-ro): cardurile de sinteză și tabelul orar |
| Câți meteori numără radarul? | [Flux radar](Radar-Flux-ro) |
| Câte ping-uri pot aștepta pe 144 MHz? | [Previziuni experimentale](Experimental-Forecasts-ro) (experimental) |
| Poate stația mea să închidă traseul? | [Geometrie și atenuare pe traseu](Geometry-and-Path-Loss-ro): atenuarea pe traseu și marja |
| Când este următorul maxim? | [Roiuri](Showers-ro) |
| Pot face teste cu GRAVES? | [Radar GRAVES](GRAVES-Radar-ro) |

## Reguli practice (din surse)

- **Orientați perpendicular pe roi**: cel mai bun traseu este ortogonal pe azimutul radiantului; direcția optimă = azimutul radiantului ±90°, toleranță ±40–50° (SM6FHZ).
- **Side-scatter**: rotiți antena cu 10–30° spre latura (A sau B) din care sosesc cele mai multe reflexii (articolul Cerrotta–Sartori).
- Un **radiant prea sus** (peste 70°) sau prea jos (sub 20°) dă puține urme utile (DF5HC, DH9GCD).
- Meteorii sporadici au maximul în jurul orei **06 UTC** (articolul; confirmat de fluxul de la Collm).
- Distanțe utile pe 432 MHz: 800–2000 km, optim aproximativ 1400 km (SM6FHZ); distanța optimă în general 1300–1500 km (DF5HC).

Mai departe: [Bolta cerească](Sky-View-ro).
