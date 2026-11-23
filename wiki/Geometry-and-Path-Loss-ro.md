[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · **Română** · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometrie și atenuare pe traseu

*Filă: Calcul previzional › Geometrie și atenuare.*

[![Geometrie și atenuare pe traseu](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Un raport text al traseului (selectabil, astfel încât îl puteți copia) și, în dreapta, graficul **Elevația antenei în funcție de distanța față de punctul de împrăștiere**. Numerele dintre paranteze drepte se referă la ecuațiile manualului de calcul (`doc/YA-MS_manuale_calcoli.docx`).

## Datele de intrare ale acestei file

| Câmp | Implicit | Utilizare |
|---|---|---|
| **Putere W** | 400 | Puterea emițătorului pentru bilanțul legăturii |
| **Câștigul antenei dBi (tx = rx)** | 14 | Aceeași antenă la ambele capete |
| **Semnal minim dBm** | −130 | Semnalul minim detectabil (articolul: Yagi cu 8 elemente + preamplificator) |
| **Densitatea urmei q = 10^ … electroni/m** | 14 | Densitatea liniară de electroni a urmei subdense |

Stațiile, banda, înălțimea urmei, elevația lobului, boom-ul și distanța hot spot-ului provin din [rândurile de comenzi](Getting-Started-ro#1-cele-trei-rânduri-de-comenzi).

## Secțiunile raportului

| Secțiune | Conținut |
|---|---|
| **GEOMETRIA TRASEULUI (elipsoidul WGS84)** | Stația și DX-ul cu înălțimile lor; distanța, azimutul și azimutul invers; punctul median (locator și coordonate); înălțimea urmei (*← moda măsurată de radarul din Collm* când este luată de la radar); elevația antenei spre punctul median |
| **HOT A / HOT B (hot spot-uri clasice, pentru orientarea antenei)** | Pentru fiecare: locatorul, azimutul de la dumneavoastră și decalajul față de traseul direct, azimutul de la DX, distanța, elevația |
| **LIMITELE ZONEI COMUNE** | Raza la înălțimea urmei cu elevația lobului; Limita A / Limita B cu azimuturile |
| Antenă | Boom-ul în λ, câștigul, lobul orizontal / vertical; dacă Hot A și Hot B sunt în interiorul sau în afara lobului |
| **ATENUAREA PE TRASEU (urmă subdensă, McKinley 1961; fără câștigurile antenelor)** | Tabel pentru punctul median (înainte), Hot A și Hot B la 28, 50, 70, 144, 222 și 432 MHz |
| **BILANȚUL LEGĂTURII LA … MHz (punctul median)** | Puterea și EIRP, atenuarea pe traseu, semnalul la antenă, minimul detectabil, **marja**; aceeași marjă cu atenuarea medie a lui OH5IY |
| **REGULI EXPERIMENTALE ÎNTRE BENZI (SM6FHZ, VUSHF 2025)** | Număr/intensitate și durată comparate cu 144 MHz; ping-ul maxim IARU |

## Locator și traseu

Locator (4, 6 sau 8 caractere; centrul pătratului, sistemul IARU Maidenhead) [14]. Distanța, azimutul și punctul de mijloc pe geodezica elipsoidului **WGS84** cu metoda lui Karney (începând cu versiunea 1.8.24; înainte, sferă cu raza r = 6372,7955 km din articolul Cerrotta–Sartori [15–16]). Calculele care depind de timp se referă la **punctul median**, deoarece ora optimă poate diferi cu până la 1,5 ore între cele două capete (SM6FHZ).

## Elevația antenei

**Sursă:** formula din articolul Cerrotta–Sartori (Figura 7), cu x = d/r, d distanța la sol până la punctul de reflexie, H înălțimea urmei și h înălțimea stației [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Verificare:** corespunde geometriei sferice exacte în limita a 0,03°. Programul folosește arctangenta cu două argumente, care dă valori negative dincolo de orizont și evită problema de periodicitate menționată în articol. O elevație negativă spre punctul median înseamnă *traseu dincolo de raza geometrică a unui singur salt*.

## Raza orizontului

Distanța la sol la care o rază cu elevația e atinge înălțimea H (inversa geometrică a formulei de mai sus) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Verificare:** H = 89,5 km, e = 0° → **1062 km**. În exemplul din articol (JN44BB–IO53RT), desenul pune intersecțiile orizontului la aproximativ 870 km de stații, ceea ce corespunde unui lob ridicat cu aproximativ 2° (865 km).

## Refracție troposferică (GFS)

Refracție troposferică (căsuța "Refracție troposferică (GFS)", debifată la pornire). Cu căsuța bifată programul descarcă de la Open-Meteo profilul modelului GFS deasupra celor două stații (presiune, temperatură și umiditate la sol și la nivelurile de la 1000 la 500 hPa, la ora cea mai apropiată în limita a 6 ore), obține înălțimile nivelurilor cu ecuația hipsometrică (temperatură virtuală) și refractivitatea cu formula Recomandării ITU-R P.453:

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

cu P și e (presiunea vaporilor, din formula Magnus) în hPa și T în kelvini. Deasupra ultimului nivel N scade exponențial cu o înălțime de scară de 7,35 km. Dacă GFS nu răspunde, se folosește atmosfera de referință P.453, N = 315·exp(−h/7,35), iar raportul o spune.

Raza se urmărește prin straturi sferice subțiri cu legea lui Snell în formă sferică (n·r·cos e constant) până la înălțimea urmelor; rezultă raza de acțiune la înălțimea H și corecția elevației:

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

Exemplu cu atmosfera de referință și urme la 89,5 km: la 0° raza crește de la 1061,5 la circa 1133 km (+72 km) și punctul apare cu 0,62° mai sus; la 4° raza crește cu 14 km și corecția este 0,20°; peste 10° efectul este neglijabil. Corecția se aplică elevației spre punctul median, razei zonei comune, hot spot-urilor și punctelor hărții de eficiență; punctele sub orizontul refractat se elimină. Raportul o dă pe rândul "Refracție".

Raza terestră echivalentă k = 4/3 este valabilă pentru razele care rămân în primii kilometri ai troposferei, unde N scade cu circa 40 de unități pe km. Raza spre o urmă la 90 km străbate întreaga troposferă și peste 10-15 km, unde N este aproape nul, continuă aproape dreaptă: cu k = 4/3 pe toată urcarea, raza de acțiune la 0° ar fi de circa 1230 km, cu aproape 100 km mai mult decât raza urmărită. De aceea programul urmărește raza în profilul GFS, cum face LIVETROPOVHF al autorului pentru propagarea troposferică, în loc să folosească k = 4/3.

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

## Limitele zonei comune

**Sursă:** articolul localizează intersecțiile curbelor în care orizontul fiecărei stații întâlnește stratul E: intersecțiile a două cercuri cu raza unghiulară ρ = d_H/r centrate în A și B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Dacă 1 − |p0|² < 0, traseul este mai lung decât 2·d_H și stațiile nu văd **nicio zonă comună a stratului E**.

**Verificare:** acestea sunt **marginile cele mai îndepărtate** ale cerului văzut de ambele stații, **nu puncte spre care să orientați antena**. Pe JN70CN–IN78UO (1710 km, azimut 308°) ele cad la 1062 km de stație, la 37° la stânga și la dreapta traseului direct, în timp ce MSHV sugerează 10°. De aceea se numesc *Limita A* / *Limita B* și sunt desenate estompat pe hartă.

## Hot A și Hot B

**Sursă:** reflexiile meteorilor sporadici se concentrează în două zone („hot spot-uri”) de o parte și de alta a punctului median. J. Richardson (AMS), în tabelul citat de DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), dă decalajul antenei față de direcția directă: **13° la 1000 km, 11° la 1250 km, 10° la 1500 și 2000 km**. Buletinul AMS nr. 203, preluat de W8WN, dă 10° la 1500 și 1800 km.

**Alegere:** Hot A și Hot B sunt punctele aflate la distanța s de punctul median M, perpendicular pe traseu. Cu *auto (AMS)* bifat (implicit), s provine din decalajul din tabelul lui Richardson, interpolat liniar (13° sub 1000 km, 10° peste 2000 km): s = (D/2)·tan(decalaj). Debifat, s se introduce manual, 30–400 km (MSHV folosește 150 km); A la stânga privind de la stația dumneavoastră spre DX, B la dreapta [21]. Decalajul văzut de la stație este aproximativ [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verificare:** cu tabelul AMS, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, la fel ca cei 150 km folosiți anterior și de MSHV; pe trasee scurte, tabelul apropie hot spot-urile de punctul median.

## Atenuarea pe traseu subdensă

**Sursă:** ecuația lui McKinley și Recomandarea ITU-R P.843 pentru urme subdense (sin α = 1), fără câștigurile antenelor; q = densitatea liniară de electroni, r_e = raza clasică a electronului = 2,818·10⁻¹⁵ m, R1, R2 distanțele față de urmă, φ jumătate din unghiul de împrăștiere, β unghiul dintre urmă și planul traseului, a₁ factorul razei inițiale cu r₀ în m și h în km (P.843, ec. 4 și 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Alegere:** bilanțul și tabelul atenuărilor folosesc β = 90° (urmă care traversează planul traseului, cazul cel mai puțin favorabil: valoare prudentă), iar bilanțul arată și cazul cel mai bun, β = 0. r₀ se ia la înălțimea medie a ecoului pentru frecvența respectivă, h = 124 − 17 log f (P.843, ec. 15): 0,76 m la 95 km pentru 50 MHz, 0,40 m la 87 km pentru 144 MHz, 0,21 m la 79 km pentru 432 MHz. Pe 1000 km, a₁ este 0,2 dB la 50 MHz, 0,6 dB la 144 MHz și 1,4 dB la 432 MHz (2,9 dB la 600 km); la înălțimea fixă de 102 km a lui DJ5HG ar fi aproximativ 70 dB la 432 MHz, adică niciun ecou.

**Verificare:** cu q = 10¹⁴ electroni/m, urme la 89,5 km și β = 0, la 144 MHz: **182–192 dB** între 600 și 2100 km (185 dB la 1000 km), în intervalul **172–190 dB** calculat de John Worsnop **G4BAO** în teza sa de doctorat, după cum relatează GM8JBJ. Cu β = 90°, atenuarea crește cu 10 dB la 600 km, 13 dB la 1000 km și 16 dB la 2100 km; **media de 200 dB** a lui OH5IY se află între cele două cazuri. Cei 182 dB din tabelul lui GM8JBJ nu sunt o confirmare: tabelul nu dă nicio frecvență, cei 86,4 dB ai săi pe fiecare segment sunt atenuarea în spațiul liber pe 500 km la 1 MHz (lipsește termenul 20 log f: 129,6 dB la 144 MHz), iar elementele sale însumează 163,8 dB, nu 182; pagina nu spune nici „minim”, nici „144 MHz”.

## Bilanțul legăturii

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Câștigurile se introduc și se folosesc în dBi: atenuarea lui McKinley se referă la antene izotrope, deci nu se scade nicio corecție de dipol de 2,15 dB (EIRP = putere + câștig). Raportul dă și marja cu **atenuarea medie pe traseu a lui OH5IY** (200 dB la 144 MHz, scalată cu λ³ la banda aleasă). Referința articolului: este nevoie de aproximativ **70 dBm EIRP** (−130 dBm + 200 dB, de ex. aproximativ 400 W într-o antenă de 14 dBi).

## Câștigul și lobul antenei

**VE7BQH** – Câștigul unei antene Yagi în funcție de lungimea boomului L: dreapta medie a tabelelor VE7BQH pe bandă (circa 60 de antene pe bandă, câștiguri NEC). În paranteză intervalul eșantionului și abaterea standard:

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0,3–5 λ, 0,25 dB · 144 MHz: 0,75–8,9 λ, 0,15 dB · 432 MHz: 1,8–16 λ, 0,17 dB)

Se folosește dreapta benzii celei mai apropiate: sub 100 MHz cea de 50 MHz, între 100 și 300 MHz cea de 144 MHz, peste 300 MHz cea de 432 MHz (pentru 1296 MHz este o extrapolare). În afara intervalului eșantionului fereastra principală avertizează că estimarea este aproximativă.

Curba istorică DL6WU (VHF Communications 3/1982, fig. 1): măsurători la 432 și 1296 MHz din 1981, 2,35 dB pe octavă de boom, precizie declarată 0,5 dB; G ≈ 9,2 + 7,81 log10(L/λ) dBd. W8IO o dă ca 7,773 log10(L/λ) + 11,43 dBi (diferență sub 0,1 dB). Programul o scrie în raport pentru comparație:

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**Verificare față de modelele NEC ale lui L.B. Cebik W4RNL la 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemente | Boom (λ) | W4RNL NEC (dBi) | Formulă (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Diferența nu depășește niciodată **0,1 dB**: câștigul depinde mai mult de lungimea boom-ului decât de proiect (antenele Yagi VK3AUU au un boom mai scurt pentru același număr de elemente). Yagi Calculator de VK5DJ dă estimări și pentru variantele VK3AUU, WA2PHW și DJ9BV, ale căror formule nu sunt publicate.

Media VE7BQH minus curba DL6WU: la 50 MHz în limita a 0,25 dB între 2 și 16 λ; la 144 MHz de la −0,04 dB la 1 λ la +0,42 dB la 10 λ; la 432 MHz de la −0,06 dB la 2 λ la +0,55 dB la 10 λ. Pe antenele DL6WU și VK3AUU simulate de W4RNL la 432 MHz, media VE7BQH este cu 0,15–0,55 dB peste NEC: pe boomuri lungi antenele din tabele, optimizate pe calculator, rândesc mai mult decât proiectele originale.

**Lob – sursă:** regula lui Kraus, cu un lob circular θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Verificare:** modelele NEC ale lui W4RNL pentru antenele Yagi DL6WU dau un **lob orizontal cu 5–10 % mai îngust** decât Kraus: 33,8° / 26,4° / 22,6° pentru 12, 19 și 26 de elemente, față de 37,3° / 28,0° / 23,9°. Formulele simple ignoră lobii laterali din față (W4RNL, *Long-Boom Yagi Rules of Thumb*). Pe boom-uri lungi, lobul vertical este puțin mai larg decât cel orizontal (14 λ: 18,4° / 18,8°).

**Alegere** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Exemplu: Yagi de 14 λ la 432 MHz → 20,3 dBi, lob de 18,1° orizontal și 19,5° vertical; modelele lui W4RNL dau 20,4 dBi și 18,4° / 18,8°. Acestea sunt reguli aproximative deduse din câteva antene DL6WU.

Cu media VE7BQH aceeași antenă Yagi de 14 λ dă 21,0 dBi și un lob de 16,9° orizontal și 18,1° vertical; cei 20,3 dBi de mai sus provin din curba DL6WU. Corecțiile lobului (0,93 · θK și θK) rămân cele deduse din antenele DL6WU.

Antena este considerată mereu îndreptată spre DX. Un hot spot este **în interiorul lobului** dacă |Az(Hot) − Az(antenă)| ≤ θ_horizontal/2: atunci este desenat cu gri în [Bolta cerească](Sky-View-ro) și apare un avertisment. Lobul vertical intră și în calculul eficienței: cu căsuța *diagrama antenei* activată, punctele de reflexie sunt ponderate cu câștigul vertical al celor două antene (lățime θ_vertical, maxim la elevația lobului, factorul solului până la zero la orizont).

## Reguli experimentale între benzi

Comparat cu 144 MHz: număr/intensitate × (144/f)³ (în dB), durată × (144/f)² (SM6FHZ, VUSHF 2025). Durata maximă a ping-ului în Regiunea 1 IARU: 1000 ms la 50 MHz, 500 ms la 70 MHz, 100 ms la 144 MHz, 13 ms la 432 MHz (VHF Handbook, citat în articol). Vedeți și [Previziuni experimentale](Experimental-Forecasts-ro).
