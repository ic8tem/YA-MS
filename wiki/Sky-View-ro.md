[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · **Română** · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [ไทย](Sky-View-th) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Bolta cerească

*Fila: Calcul previzional › Calcul previzional.*

[![Bolta cerească](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Această sub-filă (bolta cerească din versiunile anterioare) pune pe un singur ecran **unde** se află acum urmele utile și **unde să orientezi antena**. În stânga, **vederea în plan** a traseului; în dreapta, lista roiurilor, o boltă cerească mică cu radianții, textul calculului și **secțiunea** văzută de antena ta. Totul se referă la ora cursorului *Ora bolții cerești* (implicit timpul real; ±36 h în pași de 15 minute).

În bolta cerească mică, o **linie portocalie** care trece prin zenit dă întotdeauna **direcțiile corecte ale antenei**, ortogonale pe deplasarea roiului selectat (sau a celui mai favorabil): azimutul radiantului ±90°, etichetat *antena NNN°* la ambele capete, cu toleranța de ±45° ca linii subțiri. Scurte gradații portocalii pe margine dau direcțiile ortogonale ale celorlalte roiuri utile.

## Vederea în plan (stânga)

O hartă a Europei văzută de sus (**E în dreapta**), cu o scară în grade de jur împrejur. Legenda de sub hartă îi dă raza (*Hartă: margine = … km de stație*).

| Element | Reprezentare |
|---|---|
| Traseu / DX | Linie verde de la stația ta la corespondent (întotdeauna traseul real pe cercul mare dintre locatori) |
| **Hot A / Hot B** | Puncte la 150 km (reglabil) de o parte și de alta a punctului median, perpendicular pe traseu. **Roșu = recomandat**, **roz = în afara lobului antenei**, **gri = în lob** (cu avertisment) |
| Lobul antenei | Lobul orizontal la −3 dB în jurul azimutului antenei (antena mereu orientată spre DX), etichetat *lob …°* |
| Limitele zonei comune | Punctele estompate *lim. A* / *lim. B* și cele două cercuri în care orizontul fiecărei stații întâlnește stratul E (vezi [Geometrie](Geometry-and-Path-Loss-ro#limitele-zonei-comune)) |
| Deplasarea roiului | **Linie galbenă**: direcția în care roiul selectat (sau cel mai favorabil) mătură cerul, adică azimutul radiantului |
| Orientări optime | **Puncte portocalii**: cele două orientări perpendiculare pe deplasare (azimutul radiantului ±90°, SM6FHZ) |
| **Zonele PREV** | Elipse deschise la culoare: unde cad **acum** urmele cele mai probabile, câte una pe fiecare latură a traseului |

Etichetele nu se suprapun: Hot A și PREV A sunt scrise în stânga traseului, B în dreapta. **Legenda** este o coloană pliabilă în dreapta hărții.

**Mouse-ul pe hartă:** **clic stânga = locatorul corespondentului**, **clic dreapta = locatorul stației mele**. Traseul se recalculează imediat.

Opțiunile de deasupra listei roiurilor: **Direcții Hot A / Hot B**, **Harta Europei** (Natural Earth, descărcată în `data/mappa` la prima pornire), **Vedere de sus (E în dreapta)**.

### Hot recomandat

Pentru ora afișată, programul adună pentru toate roiurile de deasupra orizontului ponderea ZHR × eficiență, împărțită între latura A (fracțiunea f_A) și latura B. Latura cu ponderea mai mare dă Hot-ul recomandat, desenat cu roșu:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*Alegere a programului (manual, ec. 23).* Sursa ideii: DJ5HG, citat de DF5HC (conferința DARC 2018) – în funcție de poziția radiantului, unul dintre cele două puncte, HOT-A sau HOT-B, este mai favorabil. Rotirea cu 10–30° spre acea latură (side-scatter) provine din articolul Cerrotta–Sartori.

### Zonele PREV

Pentru fiecare punct P al stratului E se adună contribuțiile tuturor roiurilor active la eficiență (aceeași condiție speculară ca la [eficiență](Efficiency-Calculation-ro#modelul)), ponderate cu ZHR. Punctele cu cel puțin 3 % din maxim formează zonele PREV; fiecare este desenată ca o elipsă cu centrul = media ponderată a punctelor și axele = dublul dispersiei lor.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Alegere a programului (manual, ec. 34).* Este regula practică: dacă roiul mătură cerul de la nord la sud, urmele utile cad la est și la vest.

## Lista roiurilor (dreapta sus)

| Coloană | Semnificație |
|---|---|
| Roi, Cod | Numele și codul IMO |
| ZHR acum | Activitatea în acest moment (ZHR de maxim IMO cu profilul de activitate) |
| Azimut, Elev. | Poziția radiantului văzută de la stația ta |
| Efic. % | Eficiența roiului pentru acest traseu |
| Latură | A sau B, latura din care sosesc cele mai multe reflexii |
| Orient. optimă | Azimutul radiantului ±90° |
| Răsare, Apune | Răsăritul și apusul radiantului (UTC); *circumpolar* sau *mereu sub orizont* când este cazul |

Fă clic pe un rând pentru a selecta roiul: linia galbenă a deplasării și punctele portocalii îl urmează.

## Bolta cerească mică (dreapta, la mijloc)

Radianții pe o boltă cerească văzută de la stația ta, cu **codul IMO** și **traiectoria zilnică în cyan** (orele UTC). **Fă clic pe un radiant** pentru a-l selecta. Culori:

| Culoare | Semnificație |
|---|---|
| Galben | eficiență ≥ 50 % și ZHR ≥ 2 |
| Portocaliu | eficiență ≥ 20 % |
| Roșu închis | eficiență < 20 % |
| Gri | aproape inactiv |

Alături, textul calculului: lungimea și azimutul traseului, punctul median și elevația lui, azimuturile și abaterile lui Hot A / Hot B, Hot-ul recomandat (*… recomandat acum: az. …° (…% din reflexiile prevăzute)*), limitele zonei comune și memento-ul: *orientarea optimă pentru roi: PERPENDICULAR pe direcția de sosire (azimutul radiantului ±90°, toleranță ±40–50°, SM6FHZ)*.

## Secțiunea (dreapta jos)

*SECȚIUNE – urmele cele mai probabile văzute de antenă spre corespondent.* Pe orizontală **azimutul față de corespondent** (← A stânga, B → dreapta), pe verticală **elevația**. Pentru fiecare roi se iau cele mai puternice 14 puncte de reflexie; fiecare urmă este un segment orientat spre radiant, de la 10 km deasupra până la 10 km sub altitudinea urmelor (cel mult 60 km de fiecare parte), mai gros când este mai probabil. Sunt desenate și: lobul antenei (cercul de −3 dB în jurul elevației lobului), corespondentul și Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Alegere a programului (manual, ec. 35).*

## Avertismente

| Avertisment | Când |
|---|---|
| **ATENȚIE: Hot A (și/sau Hot B) cade în lobul antenei …** | Hot spot-ul se află în ±θ/2 față de azimutul antenei (θ = lobul orizontal la −3 dB): cu această orientare este deja acoperit. Afișat cu gri pe hartă. Hot-ul recomandat rămâne roșu. |
| **RADIANT PREA SUS (peste 70°)** | Un radiant util este la peste 70° deasupra orizontului stației tale: urmele coboară aproape vertical și reflectă puțin spre traseu (DF5HC, DH9GCD). Aceleași ore sunt marcate cu ↑ în [tabelul orar](Efficiency-Calculation-ro#tabelul-orar). |
| *Nicio zonă comună a stratului E* | Traseul este mai lung decât dublul bătăii la altitudinea urmelor: cele două stații nu văd o parte comună a stratului E (salt unic imposibil). |
| *Niciun Hot recomandat* | Aproape niciun roi activ în acest moment. |

Referință pentru grafica bolții cerești: Swan Meteor Skyview de DL1DBC (swan.ms); grafic polar cu cea mai bună direcție: RadiantCalc de SM6FHZ.
