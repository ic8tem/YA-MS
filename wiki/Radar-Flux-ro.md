[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-BR) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · **Română** · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-TW)

# Flux radar

*Filă: Date live și în timp real › Flux radar.*

[![Flux radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Această filă arată ce numără **acum** radarele profesionale de meteori: numărul orar de meteori și înălțimile urmelor de la radarul SKiYMET din **Collm** (Universitatea din Leipzig / IAP Kühlungsborn, Germania, 36,2 MHz) și cea mai recentă imagine a radarului din **Sodankylä** (SGO, Finlanda). Numărătorile de la Collm alimentează estimarea pe banda dumneavoastră și [Previziunile experimentale](Experimental-Forecasts-ro); înălțimea măsurată a urmelor alimentează întreaga geometrie.

## Comenzi

| Comandă | Ce face |
|---|---|
| **Descarcă acum** | Verifică imediat toate sursele externe. |
| **Actualizarea automată a tuturor surselor la fiecare 5 minute** | Activată implicit. La fiecare 5 minute sunt verificate toate sursele și sunt descărcate din nou **doar cele care s-au modificat** (*nemodificat (verificat la … UTC)* / *date noi la … UTC*). |
| **Exponentul λ (SM6FHZ)** | Exponentul k al regulii de frecvență, implicit 3 (1–4). |

## Ce se afișează

| Panou | Conținut |
|---|---|
| **Meteori/oră – ieri și astăzi (UTC)** | Bare cyan = numărătorile Collm (valide), bare roșii = eliminate, linie portocalie groasă = *estimare la … MHz* pe scala din dreapta |
| **Înălțimile urmelor (Collm)** | Meteori pe km de înălțime între 70 și 110 km, cu înălțimea cea mai frecventă (moda), media, mediana și abaterea standard |
| Imaginea Collm | Graficul SKiYMET original, așa cum a fost descărcat |
| Imaginea Sodankylä | Cea mai recentă imagine cu numărul de meteori a radarului din Sodankylä (doar afișată; formatul său nu este citit) |

Linia de deasupra graficelor spune când a fost citit graficul de la Collm și ce scală verticală a fost găsită (*scală citită din grafic: 0-… meteori/oră*).

## Cum se citește graficul de la Collm

Graficul de la Collm (720 × 720 pixeli, culori pure) are pozițiile axelor fixe, dar radarul **adaptează în fiecare zi scala verticală** la valorile măsurate (de ex. 0–1,2·10³ pe 5/11/2026 și 0–1,0·10³ pe 6/11/2026, cu gradațiile mutate). Prin urmare, YA-MS:

1. găsește gradațiile lungi ale axei;
2. **citește etichetele** gradației celei mai înalte și ale lui zero comparând fiecare caracter cu fontul în matrice de puncte al graficului;
3. pentru fiecare oră i (0–47, ieri și astăzi) ia coloana centrală și primul pixel cyan de sus, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top și y0 sunt rândurile gradației celei mai înalte și ale lui zero, N_top valoarea citită pe eticheta cea mai înaltă (×1000). Rezoluție: aproximativ 7–8 meteori/oră pe pixel. *Alegere a programului (ec. 42 din manual).*

Dacă o etichetă nu poate fi citită, programul revine la calibrarea din 5/11/2026 (**scală calibrată 0-1200 meteori/oră**) și o spune cu portocaliu: *Nu se poate citi scala verticală a fluxului (eticheta de sus: …): valorile trebuie verificate.* Dacă se schimbă chiar formatul graficului (*Formatul graficului s-a schimbat (…x…): nu poate fi citit* sau *Axele fluxului nu au fost găsite în poziția așteptată*), citirea trebuie recalibrată: vă rugăm să raportați (vedeți [Contribuții](Contributing-and-Contacts-ro)).

### Înălțimile urmelor

Din histograma înălțimilor (n_k meteori în km k, înălțimea medie h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Ec. 43 din manual.* Cu **de la radar** bifat (rândul 2 al comenzilor), **moda** devine înălțimea urmei pentru toate calculele. Verificare: graficul din 5/11/2026 – moda 89,5 km, media 88,6 km, abaterea standard 6,8 km, ceea ce confirmă cei ~90 km din articolul Cerrotta–Sartori (media SKiYMET).

Dacă scala graficului înălțimilor se schimbă, programul avertizează: *statisticile înălțimii (moda, media, mediana) rămân valabile, numărătorile absolute nu.*

## Estimarea pe banda dumneavoastră

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Reguli experimentale ale lui **SM6FHZ** (VUSHF 2025): numărul și intensitatea reflexiilor scalează cu λ³, durata cu λ² (la McKinley, λ³ este puterea unei singure urme; numărul de urme scalează aproximativ ca λ^1,5, iar în forward scatter duratele cresc și cu sec²φ: vedeți [Previziuni experimentale](Experimental-Forecasts-ro)). Este afișată și durata maximă a ping-ului în Regiunea 1 IARU (1000 ms la 50 MHz, 500 ms la 70 MHz, 100 ms la 144 MHz, 13 ms la 432 MHz). Valorile sunt orientative, de comparat cu experiența din eter. Factorul de stație K și comparația cu RMOB se află în [Previziuni experimentale](Experimental-Forecasts-ro).

## Fără conexiune

Dacă nicio sursă nu poate fi accesată, apare **o singură dată** un mesaj: *Nicio conexiune la internet. Datele radar și RMOB nu pot fi actualizate: programul folosește ultimele date salvate și reîncearcă singur la fiecare 5 minute.* Bara de stare de jos devine roșie (*NICIO CONEXIUNE LA INTERNET …*) până când conexiunea revine (*Conexiune restabilită.*).

## Arhive și surse

| Fișier (în `data/`) | Conținut |
|---|---|
| `flusso_collm.csv` | Arhiva orară a fluxului citit de la Collm (orele deja prezente sunt actualizate) |
| `quote_collm.csv` | Arhiva înălțimilor urmelor |
| `radar/` | Cele mai recente imagini descărcate (și fișierele RMOB) |
| `fonti_radar.csv` | Adresele surselor radar, `attivo=1/0` pentru a activa/dezactiva fiecare sursă |

| Sursă | Frecvență | Note |
|---|---|---|
| Radarul de meteori din Collm, Universitatea din Leipzig (LIM) și IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | actualizat în fiecare oră la minutul 10 UTC; fluxul de ieri + astăzi, distribuția înălțimilor |
| Observatorul Geofizic Sodankylä – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | doar imagine (radar în curs de modernizare, proiectul DECC) |
| swan.ms (copie a Collm) | 36,2 MHz | dezactivat implicit; folosiți-l doar cu permisiunea lui DL1DBC |

> Datele radar aparțin instituțiilor lor (Universitatea din Leipzig / IAP Kühlungsborn, Observatorul Geofizic Sodankylä).
