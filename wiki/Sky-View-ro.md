[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-br) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · **Română** · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-tw)

# Bolta cerească

*Filă: Calcul previzional › Calcul previzional.*

[![Bolta cerească](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Această subfilă (bolta cerească din versiunile anterioare) pune pe un singur ecran **unde** se află acum urmele utile și **unde să orientați antena**. În stânga, **vederea în plan** a traseului; în dreapta, lista roiurilor, o mică boltă cerească cu radianții, textul calculului și **secțiunea** văzută de la antena dumneavoastră. Totul se referă la momentul ales cu *Data calculului (UTC)* și cursorul *Ore (−12 până la +36 h)* (implicit timpul real, pași de 15 minute).

O **bandă deasupra vederii în plan** rezumă calculul pentru acel moment: data și ora (*acum* sau orele de acum încolo), **indicele traseului Σ ZHR×η**, **cel mai util roi** cu ZHR-ul și eficiența sa (și în dB față de referința DJ5HG, vedeți [Calculul eficienței](Efficiency-Calculation-ro)), numărul de roiuri deasupra orizontului și **Hot-ul recomandat** cu azimutul său.

În mica boltă cerească, o **linie portocalie** prin zenit arată întotdeauna **direcțiile corecte ale antenei**, ortogonale pe deriva roiului selectat (sau a celui mai favorabil): azimutul radiantului ±90°, etichetată *antenă NNN°* la ambele capete, cu toleranța de ±45° ca linii subțiri. Mici liniuțe portocalii pe margine dau direcțiile ortogonale ale celorlalte roiuri utile.

## Vederea în plan (stânga)

O hartă a Europei văzută de sus (**E la dreapta**) cu o scală în grade de jur împrejur. Legenda de sub hartă îi dă raza (*Hartă: margine = … km de la stație*).

| Element | Desen |
|---|---|
| Traseu / DX | Linie verde de la stația dumneavoastră la stația DX (întotdeauna traseul real pe cercul mare dintre locatori) |
| **Hot A / Hot B** | Puncte de o parte și de alta a punctului median, perpendiculare pe traseu, la distanța dată de tabelul de decalare AMS (sau introdusă manual). **Roșu = recomandat**, **roz = în afara lobului antenei**, **gri = în interiorul lobului** (cu avertisment) |
| Lobul antenei | Lobul orizontal la −3 dB în jurul azimutului antenei (antena întotdeauna îndreptată spre DX), etichetat *lob …°* |
| Limitele zonei comune | Puncte estompate *lim. A* / *lim. B* și cele două cercuri în care orizontul fiecărei stații întâlnește stratul E (vedeți [Geometrie](Geometry-and-Path-Loss-ro#limitele-zonei-comune)) |
| Deriva roiului | **Linie galbenă**: direcția în care roiul selectat (sau cel mai favorabil) mătură cerul, adică azimutul radiantului |
| Direcții optime | **Puncte portocalii**: cele două direcții perpendiculare pe derivă (azimutul radiantului ±90°, SM6FHZ) |
| **Zonele PREV** | Elipse deschise la culoare: unde cad **acum** cele mai probabile urme, câte una pe fiecare parte a traseului |

Etichetele nu se suprapun: Hot A și PREV A sunt scrise în stânga traseului, B în dreapta. **Legenda** este o coloană pliabilă în dreapta hărții.

**Mouse-ul pe hartă:** **clic stânga = locatorul stației DX**, **clic dreapta = locatorul stației mele**. Traseul este recalculat imediat.

Opțiuni deasupra listei roiurilor: **Direcțiile Hot A / Hot B**, **Harta Europei** (Natural Earth, descărcată în `data/mappa` la prima pornire), **Vedere de sus (E la dreapta)**.

### Hot recomandat

Pentru ora afișată, programul adună pentru toate roiurile de deasupra orizontului ponderea ZHR × eficiență, împărțită între latura A (fracția f_A) și latura B. Latura cu ponderea mai mare dă Hot-ul recomandat, desenat în roșu:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Alegere a programului (ec. 23 din manual).* Sursa ideii: DJ5HG, relatată de DF5HC (conferința DARC 2018) – în funcție de poziția radiantului, unul dintre cele două puncte, HOT-A sau HOT-B, este mai favorabil. Rotirea cu 10–30° spre acea latură (side-scatter) provine din articolul Cerrotta–Sartori.

### Zonele PREV

Pentru fiecare punct P al stratului E se adună contribuțiile tuturor roiurilor active la eficiență (aceeași condiție speculară ca la [eficiență](Efficiency-Calculation-ro#modelul)), ponderate cu ZHR. Punctele cu cel puțin 3 % din maxim formează zonele PREV; fiecare este desenată ca o elipsă cu centrul = media ponderată a punctelor și axele = de două ori dispersia lor.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Alegere a programului (ec. 34 din manual).* Este regula practică: dacă roiul mătură cerul de la nord la sud, urmele utile cad la est și la vest.

## Lista roiurilor (dreapta sus)

| Coloană | Semnificație |
|---|---|
| Roi, Cod | Numele și codul IMO |
| ZHR acum | Activitatea în acest moment (ZHR-ul de maxim IMO cu profilul de activitate) |
| Azimut, Elev. | Poziția radiantului văzută de la stația dumneavoastră |
| Efic. % | Eficiența roiului pentru acest traseu |
| Latură | A sau B, latura din care sosesc cele mai multe reflexii |
| Direcție optimă | Azimutul radiantului ±90° |
| Răsărit, Apus | Răsăritul și apusul radiantului (UTC); *circumpolar* sau *mereu sub orizont* când este cazul |

Faceți clic pe un rând pentru a selecta roiul: linia galbenă a derivei și punctele portocalii îl urmează.

## Mica boltă cerească (dreapta mijloc)

Radianții pe o boltă cerească văzută de la stația dumneavoastră, cu **codul IMO** și **traiectoria zilnică în cyan** (ore UTC). **Faceți clic pe un radiant** pentru a-l selecta. Culori:

| Culoare | Semnificație |
|---|---|
| Galben | eficiență ≥ 50 % și ZHR ≥ 2 |
| Portocaliu | eficiență ≥ 20 % |
| Roșu închis | eficiență < 20 % |
| Gri | aproape inactiv |

Alături, textul calculului: lungimea și azimutul traseului, punctul median și elevația sa, azimuturile și decalajele lui Hot A / Hot B, Hot-ul recomandat (*… recomandat acum: az. …° (…% din reflexiile așteptate)*), limitele zonei comune și memento-ul: *orientarea optimă pentru roi: PERPENDICULAR pe direcția de sosire (azimutul radiantului ±90°, toleranță ±40–50°, SM6FHZ)*.

## Secțiunea (dreapta jos)

*SECȚIUNE – cele mai probabile urme văzute de la antenă spre stația DX.* Pe orizontală, **azimutul relativ la stația DX** (← A stânga, B → dreapta), pe verticală **elevația**. Pentru fiecare roi se iau cele mai puternice 14 puncte de reflexie; fiecare urmă este un segment orientat spre radiant, de la 10 km deasupra până la 10 km sub înălțimea urmei (cel mult 60 km pe fiecare parte), mai gros când este mai probabil. Sunt desenate și: lobul antenei (cercul la −3 dB în jurul elevației lobului), stația DX și Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Alegere a programului (ec. 35 din manual).*

## Avertismente

| Avertisment | Când |
|---|---|
| **ATENȚIE: Hot A (și/sau Hot B) cade în interiorul lobului antenei …** | Hot spot-ul se află în ±θ/2 de azimutul antenei (θ = lobul orizontal la −3 dB): cu această orientare este deja acoperit. Afișat în gri pe hartă. Hot-ul recomandat rămâne roșu. |
| **RADIANT PREA SUS (peste 70°)** | Un radiant util este la peste 70° de la stația dumneavoastră: urmele cad aproape vertical și reflectă puțin spre traseu (DF5HC, DH9GCD). Aceleași ore sunt marcate cu ↑ în [tabelul orar](Efficiency-Calculation-ro#tabelul-orar). |
| **RADIANT JOS DE-A LUNGUL TRASEULUI** | Un radiant activ este sub 20° și la mai puțin de 30° de direcția traseului. Eficiența calculată rămâne mică (prudentă), dar DJ5HG se așteaptă la reflexii rare și puternice de la urme razante aliniate cu traseul (Hamburg–Narvik, Quadrantide, în jurul orei 19 UTC): merită ascultat. |
| **TRASEU DINCOLO DE ORIZONTUL URMELOR** | La înălțimea urmei, punctul median al traseului este sub orizontul ambelor stații (aproximativ 2120 km cu urme la 90 km). Avertismentul dă înălțimea minimă necesară a urmei (aproximativ 96 km pentru 2200 km, 105 km pentru 2300 km): legătura este posibilă doar cu cele mai înalte urme, iar eficiențele și atenuările sunt la limita modelului |
| *Nicio zonă comună a stratului E* | Traseul este mai lung decât dublul razei la înălțimea urmei: cele două stații nu văd o parte comună a stratului E (salt unic imposibil). |
| *Niciun Hot recomandat* | Aproape niciun roi activ la această oră. |

Referință pentru grafica bolții cerești: Swan Meteor Skyview de DL1DBC (swan.ms); diagrama polară cu direcția optimă: RadiantCalc de SM6FHZ.
