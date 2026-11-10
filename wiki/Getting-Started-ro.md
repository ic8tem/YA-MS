[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · **Română** · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [ไทย](Getting-Started-th) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Primii pași

La prima pornire YA-MS arată un traseu de exemplu (JN70CN → JO62QM pe 144 MHz). Cinci minute sunt suficiente pentru a-l configura pentru stația ta.

## 1. Cele trei rânduri de comenzi

Deasupra filelor sunt trei rânduri de comenzi, valabile pentru toate filele. Butonul **Comenzi** din dreapta sus le pliază și le depliază (util cu fonturi mari); alegerea este memorată.

**Rândul 1 – stații și bandă**

| Comandă | Ce face |
|---|---|
| **Locatorul meu** / **altitudine m** | Locatorul tău Maidenhead (4, 6 sau 8 caractere; se folosește centrul pătratului) și altitudinea stației deasupra nivelului mării. |
| **Corespondent** / **altitudine m** | Locatorul și altitudinea stației pe care vrei să o lucrezi. |
| **Bandă MHz** | 28, 50, 70, 144, 222 sau 432 MHz: folosită pentru câștigul și lobul antenei, estimarea fluxului și bilanțul legăturii. |
| **Calculează** | Recalculează traseul (eșantionarea stratului E: câteva secunde). |
| **Antenă az** | Azimutul antenei tale: întotdeauna **spre DX** (azimutul traseului). |
| **Font** | Mărimea întregului text, 100–300 %. Vezi [Setări](Settings-and-Data-Folder-ro#font-și-comenzi). |

**Rândul 2 – stratul E și antena**

| Comandă | Ce face |
|---|---|
| **Altitudine urme km** + **de la radar** | Altitudinea urmelor meteorice (implicit 90 km). Cu *de la radar* bifat, se folosește altitudinea cea mai frecventă (moda) măsurată de radarul Collm; vezi [Flux radar](Radar-Flux-ro). |
| **Elevație lob °** | Elevația cea mai joasă a lobului antenei tale (0° = orizont). Se folosesc doar punctele stratului E pe care ambele stații le văd deasupra acestei elevații. |
| **Antenă Yagi: boom m** | Lungimea boom-ului antenei tale Yagi. Programul arată lungimea în λ, câștigul (curba DL6WU) și lobul la −3 dB, orizontal și vertical; vezi [Geometrie și atenuare](Geometry-and-Path-Loss-ro#câștigul-și-lobul-antenei). Sub 2 λ estimarea este imprecisă. |
| **Hot spot de la punctul median km** | Distanța lui Hot A și Hot B de la punctul median, 30–400 km (implicit 150 km, ca în AMS Bulletin 203 / W8WN / MSHV). |

**Rândul 3 – ora**

| Comandă | Ce face |
|---|---|
| **Ora** | Ceas UTC. |
| **Ora bolții cerești (±36 h)** | Mută [Bolta cerească](Sky-View-ro) și fila [Radar GRAVES](GRAVES-Radar-ro) cu până la 36 de ore înapoi sau înainte, în pași de 15 minute. |
| **Timp real** | Revenire la momentul actual. |
| **Ziua pentru tabelul 24 h (UTC)** | Ziua afișată în [Calculul eficienței](Efficiency-Calculation-ro) și în cronologia GRAVES. |

## 2. Stația ta și corespondentul

1. Scrie **Locatorul meu** și **altitudine m**.
2. Scrie locatorul și altitudinea **corespondentului** – sau fă clic pe hartă în [Bolta cerească](Sky-View-ro): **clic stânga = locatorul corespondentului**, **clic dreapta = locatorul stației mele**.
3. Alege **Bandă MHz** și apasă **Calculează**.

Bara de stare de jos confirmă: *Traseu calculat: … km, … puncte de reflexie eșantionate în … s*.

## 3. Antena ta

Introdu **lungimea boom-ului** antenei tale Yagi. Programul deduce câștigul și lobul și te avertizează dacă Hot A sau Hot B cad deja **în lob** când antena este orientată spre DX (atunci sunt desenate cu gri: nu este nevoie să rotești antena).

## 4. Citește rezultatele

| Întrebare | Unde să te uiți |
|---|---|
| Ce roi ajută acum traseul meu și din ce parte? | [Bolta cerească](Sky-View-ro): lista roiurilor, Hot-ul recomandat cu roșu, zonele PREV |
| Care este cea mai bună oră azi? | [Calculul eficienței](Efficiency-Calculation-ro): casetele de sinteză și tabelul orar |
| Câți meteori numără radarul? | [Flux radar](Radar-Flux-ro) |
| Câte ping-uri pot aștepta pe 144 MHz? | [Implementare experimentală a prognozelor](Experimental-Forecasts-ro) (experimental) |
| Poate stația mea închide traseul? | [Geometrie și atenuare](Geometry-and-Path-Loss-ro): atenuarea și marginea |
| Când este următorul maxim? | [Roiuri](Showers-ro) |
| Pot face teste cu GRAVES? | [Radar GRAVES](GRAVES-Radar-ro) |

## Reguli practice (din surse)

- **Orientează perpendicular pe roi**: cel mai bun traseu este ortogonal pe azimutul radiantului; orientarea optimă = azimutul radiantului ±90°, toleranță ±40–50° (SM6FHZ).
- **Side-scatter**: rotește antena cu 10–30° spre latura (A sau B) din care sosesc cele mai multe reflexii (articolul Cerrotta–Sartori).
- Un **radiant prea sus** (peste 70°) sau prea jos (sub 20°) dă puține urme utile (DF5HC, DH9GCD).
- Meteorii sporadici au maximul în jurul orei **06 UTC** (articol; confirmat de fluxul Collm).
- Distanțe utile pe 432 MHz: 800–2000 km, optim circa 1400 km (SM6FHZ); distanța optimă în general 1300–1500 km (DF5HC).

Urmează: [Bolta cerească](Sky-View-ro).
