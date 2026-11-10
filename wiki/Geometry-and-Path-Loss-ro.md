[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · **Română** · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometrie și atenuare

*Fila: Calcul previzional › Geometrie și atenuare.*

[![Geometrie și atenuare](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Un raport text al traseului (selectabil, ca să-l poți copia) și, în dreapta, graficul **Elevația antenei în funcție de distanța până la scatter point**. Numerele dintre paranteze se referă la ecuațiile manualului de calcul (`doc/YA-MS_manuale_calcoli.docx`).

## Datele de intrare ale acestei file

| Câmp | Implicit | Folosire |
|---|---|---|
| **Putere W** | 400 | Puterea emițătorului pentru bilanțul legăturii |
| **Câștig antenă dBi (tx = rx)** | 14 | Aceeași antenă la ambele capete |
| **Semnal minim dBm** | −130 | Semnalul minim recepționabil (articol: Yagi cu 8 elemente + preamplificator) |
| **Densitate urmă q = 10^ … electroni/m** | 14 | Densitatea liniară de electroni a urmei subdense |

Stațiile, banda, altitudinea urmelor, elevația lobului, boom-ul și distanța hot spot-urilor provin din [rândurile de comenzi](Getting-Started-ro#1-cele-trei-rânduri-de-comenzi).

## Secțiunile raportului

| Secțiune | Conținut |
|---|---|
| **GEOMETRIA TRASEULUI (Pământ sferic, R = 6372,7955 km)** | Stația și corespondentul cu altitudinile lor; distanța, azimutul și azimutul invers; punctul median (locator și coordonate); altitudinea urmelor (*<- moda măsurată de radarul Collm* când este luată de la radar); elevația antenei spre punctul median |
| **HOT A / HOT B (hot spot clasice, pentru orientarea antenei)** | Pentru fiecare: locatorul, azimutul de la tine și abaterea față de traseul direct, azimutul de la corespondent, distanța, elevația |
| **LIMITELE ZONEI COMUNE** | Bătaia la altitudinea urmelor cu elevația lobului; Limita A / Limita B cu azimuturile |
| Antenă | Boom-ul în λ, câștigul, lobul orizontal / vertical; dacă Hot A și Hot B sunt în lob sau în afara lui |
| **ATENUAREA PE TRASEU (urmă subdensă, McKinley 1961; fără câștigurile antenelor)** | Tabel pentru punctul median (forward), Hot A și Hot B la 28, 50, 70, 144, 222 și 432 MHz |
| **BILANȚ LA … MHz (punct median)** | Puterea și EIRP, atenuarea, semnalul la antenă, minimul recepționabil, **marginea**; aceeași margine cu atenuarea medie a lui OH5IY |
| **REGULI EXPERIMENTALE ÎNTRE BENZI (SM6FHZ, VUSHF 2025)** | Numărul/intensitatea și durata comparate cu 144 MHz; ping-ul maxim IARU |

## Locator și traseu

Locator (4, 6 sau 8 caractere; centrul pătratului, sistemul IARU Maidenhead) [14]. Distanța, azimutul și punctul median cu formulele cercului mare pe o sferă cu raza **r = 6372,7955 km** (articolul Cerrotta–Sartori) [15–16]. Calculele dependente de timp se referă la **punctul median**, deoarece ora optimă poate diferi cu până la 1,5 ore între cele două capete (SM6FHZ).

## Elevația antenei

**Sursă:** formula din articolul Cerrotta–Sartori (Imaginea 7), cu x = d/r, d distanța la sol până la punctul de reflexie, H altitudinea urmelor și h altitudinea stației [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Verificare:** concordă cu geometria sferică exactă în limita a 0,03°. Programul folosește arctangenta cu două argumente, care dă valori negative dincolo de orizont și evită problema periodicității menționată în articol. O elevație negativă spre punctul median înseamnă *traseu dincolo de bătaia geometrică a unui singur salt*.

## Bătaia până la orizont

Distanța la sol la care o rază cu elevația e atinge altitudinea H (inversa geometrică a formulei de mai sus) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Verificare:** H = 89,5 km, e = 0° → **1062 km**. În exemplul din articol (JN44BB–IO53RT), desenul plasează intersecțiile cu orizontul la circa 870 km de stații, ceea ce corespunde unui lob ridicat cu circa 2° (865 km).

## Limitele zonei comune

**Sursă:** articolul localizează intersecțiile curbelor în care orizontul fiecărei stații întâlnește stratul E: intersecțiile a două cercuri cu raza unghiulară ρ = d_H/r centrate în A și B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Dacă 1 − |p0|² < 0, traseul este mai lung decât 2·d_H și stațiile nu văd **nicio zonă comună a stratului E**.

**Verificare:** acestea sunt **marginile cele mai îndepărtate** ale cerului văzut de ambele stații, **nu puncte spre care să orientezi antena**. Pe JN70CN–IN78UO (1710 km, azimut 308°) ele cad la 1062 km de stație, la 37° la stânga și la dreapta traseului direct, în timp ce MSHV sugerează 10°. De aceea se numesc *Limita A* / *Limita B* și sunt desenate estompat pe hartă.

## Hot A și Hot B

**Sursă:** reflexiile se concentrează în două zone („hot spot”) la circa **50–150 km de o parte și de alta a punctului median**. Aceasta este baza tabelului de abatere a antenei din AMS Bulletin No. 203, preluat de W8WN (abatere de 10° pentru trasee de 1500 și 1800 km); MSHV de LZ2HV folosește același criteriu.

**Alegere:** Hot A și Hot B sunt punctele aflate la distanța s de punctul median M, perpendicular pe traseu (s = 150 km, reglabil 30–400 km); A în stânga privind de la stația ta spre DX, B în dreapta [21]. Abaterea văzută de la stație este de circa [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Verificare:** JN70CN–IN78UO, D = 1710 km: 6,7° cu s = 100 km, **10,0° cu s = 150 km** (la fel ca MSHV și AMS/W8WN), 13,2° cu s = 200 km.

## Atenuarea pentru urme subdense

**Sursă:** ecuația lui McKinley pentru urmele subdense (β = 0, sin α = 1), fără câștigurile antenelor; q = densitatea liniară de electroni, r_e = raza clasică a electronului = 2,818·10⁻¹⁵ m, R1, R2 distanțele de la urmă, φ jumătate din unghiul de împrăștiere [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Verificare:** cu q = 10¹⁴ electroni/m la 144 MHz: **181–192 dB** între 600 și 2200 km, în acord cu referințele din articol la 144 MHz: **182 dB minim** (GM8JBJ, după Kaiser & Closs 1952) și **200 dB mediu** (OH5IY).

## Bilanțul legăturii

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Câștigurile se introduc în dBi și se folosesc în dBd (dBi − 2,15). Raportul dă și marginea cu **atenuarea medie a lui OH5IY** (200 dB la 144 MHz, transpusă cu λ³ la banda aleasă). Referința din articol: este nevoie de circa **70 dBm EIRP** (−130 dBm + 200 dB, de ex. circa 400 W într-o antenă de 14 dBi).

## Câștigul și lobul antenei

**Câștig – sursă:** curba lui Günter Hoch **DL6WU** pentru antenele Yagi lungi în funcție de lungimea boom-ului L, citată de W8IO (valabilă de la circa 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Verificare cu modelele NEC ale lui L.B. Cebik W4RNL la 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemente | Boom (λ) | W4RNL NEC (dBi) | Formulă (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Diferența nu depășește niciodată **0,1 dB**: câștigul depinde mai mult de lungimea boom-ului decât de proiect (antenele Yagi VK3AUU au un boom mai scurt la același număr de elemente). Yagi Calculator de VK5DJ dă și estimări pentru variantele VK3AUU, WA2PHW și DJ9BV, ale căror formule nu sunt publicate.

**Lob – sursă:** regula lui Kraus, cu un lob circular θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Verificare:** modelele NEC ale lui W4RNL pentru antenele Yagi DL6WU dau un **lob orizontal cu 5–10 % mai îngust** decât Kraus: 33,8° / 26,4° / 22,6° pentru 12, 19 și 26 de elemente, față de 37,3° / 28,0° / 23,9°. Formulele simple ignoră lobii laterali din față (W4RNL, *Long-Boom Yagi Rules of Thumb*). Pe boom-urile lungi, lobul vertical este puțin mai larg decât cel orizontal (14 λ: 18,4° / 18,8°).

**Alegere** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Exemplu: Yagi de 14 λ la 432 MHz → 20,3 dBi, lob de 18,1° orizontal și 19,5° vertical; modelele lui W4RNL dau 20,4 dBi și 18,4° / 18,8°. Acestea sunt reguli aproximative derivate din câteva antene DL6WU.

Antena este considerată întotdeauna orientată spre DX. Un hot spot este **în lob** dacă |Az(Hot) − Az(antenă)| ≤ θ_horizontal/2: atunci este desenat cu gri în [Bolta cerească](Sky-View-ro) și apare un avertisment. În calculul eficienței antenele sunt izotrope; lobul real este folosit doar pentru această verificare.

## Reguli experimentale între benzi

Față de 144 MHz: număr/intensitate × (144/f)³ (în dB), durată × (144/f)² (SM6FHZ, VUSHF 2025). Durata maximă a ping-ului conform IARU Regiunea 1: 1000 ms la 50 MHz, 500 ms la 70 MHz, 100 ms la 144 MHz, 13 ms la 432 MHz (VHF Handbook, citat în articol). Vezi și [Implementare experimentală a prognozelor](Experimental-Forecasts-ro).
