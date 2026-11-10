[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · **Română** · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [ไทย](Radar-Flux-th) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Flux radar

*Fila: Live și date în timp real › Flux radar.*

[![Flux radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Această filă arată ce numără **acum** radarele meteorice profesionale: numărătorile orare de meteori și altitudinile urmelor de la radarul SKiYMET din **Collm** (Universitatea din Leipzig / IAP Kühlungsborn, Germania, 36,2 MHz) și cea mai recentă imagine a radarului din **Sodankylä** (SGO, Finlanda). Numărătorile Collm alimentează estimarea pentru banda ta și [Implementarea experimentală a prognozelor](Experimental-Forecasts-ro); altitudinea măsurată a urmelor alimentează întreaga geometrie.

## Comenzi

| Comandă | Ce face |
|---|---|
| **Descarcă acum** | Verifică imediat toate sursele externe. |
| **Actualizare automată a tuturor surselor la fiecare 5 minute** | Activată implicit. La fiecare 5 minute sunt verificate toate sursele și sunt descărcate din nou **doar cele care s-au schimbat** (*neschimbat (verificat la … UTC)* / *dată nouă la … UTC*). |
| **Exponent λ (SM6FHZ)** | Exponentul k al regulii de frecvență, implicit 3 (1–4). |

## Ce se afișează

| Panou | Conținut |
|---|---|
| **Meteori/oră – ieri și azi (UTC)** | Bare cyan = numărătorile Collm (valide), bare roșii = respinse, linie portocalie groasă = *estimare la … MHz* pe scara din dreapta |
| **Altitudinile urmelor (Collm)** | Meteori pe km de altitudine între 70 și 110 km, cu altitudinea cea mai frecventă (moda), media, mediana și abaterea standard |
| Imaginea Collm | Graficul SKiYMET original, așa cum a fost descărcat |
| Imaginea Sodankylä | Cea mai recentă imagine cu numărătorile de meteori a radarului din Sodankylä (doar afișată; formatul ei nu este citit) |

Linia de deasupra graficelor spune când a fost citit graficul Collm și ce scară verticală a fost găsită (*scara citită din grafic: 0-… meteori/oră*).

## Cum se citește graficul Collm

Graficul Collm (720 × 720 pixeli, culori pure) are pozițiile axelor fixe, dar radarul **își adaptează scara verticală în fiecare zi** la valorile măsurate (de ex. 0–1,2·10³ pe 5/11/2026 și 0–1,0·10³ pe 6/11/2026, cu gradațiile mutate). De aceea YA-MS:

1. găsește gradațiile lungi ale axei;
2. **citește etichetele** gradației celei mai de sus și ale lui zero, comparând fiecare caracter cu fontul cu matrice de puncte al graficului;
3. pentru fiecare oră i (0–47, ieri și azi) ia coloana centrală și primul pixel cyan de sus, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top și y0 sunt rândurile gradației celei mai de sus și ale lui zero, N_top valoarea citită pe eticheta cea mai de sus (×1000). Rezoluție: circa 7–8 meteori/oră pe pixel. *Alegere a programului (manual, ec. 42).*

Dacă o etichetă nu poate fi citită, programul revine la calibrarea din 5/11/2026 (**scară calibrată 0-1200 meteori/oră**) și o spune cu portocaliu: *Nu reușesc să citesc scara verticală a fluxului (eticheta de sus: …): valori de verificat.* Dacă se schimbă chiar formatul graficului (*Formatul graficului s-a schimbat (…x…): citirea nu este posibilă.* sau *Axele fluxului nu au fost găsite în poziția așteptată.*), citirea trebuie recalibrată: te rog semnalează (vezi [Contribuții](Contributing-and-Contacts-ro)).

### Altitudinile urmelor

Din histograma altitudinilor (n_k meteori în km-ul k, altitudinea medie h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Manual, ec. 43.* Cu **de la radar** bifat (rândul 2 al comenzilor), **moda** devine altitudinea urmelor pentru toate calculele. Verificare: graficul din 5/11/2026 – moda 89,5 km, media 88,6 km, abaterea standard 6,8 km, ceea ce confirmă cei ~90 km din articolul Cerrotta–Sartori (media SKiYMET).

Dacă scara graficului altitudinilor se schimbă, programul avertizează: *statisticile altitudinilor (moda, media, mediana) rămân valide, numărătorile absolute nu.*

## Estimarea pentru banda ta

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Reguli experimentale ale lui **SM6FHZ** (VUSHF 2025): numărul și intensitatea reflexiilor se scalează cu λ³, durata cu λ²; dependența de λ³ este aceeași ca în ecuația lui McKinley pentru urmele subdense. Este afișată și durata maximă a ping-ului conform IARU Regiunea 1 (1000 ms la 50 MHz, 500 ms la 70 MHz, 100 ms la 144 MHz, 13 ms la 432 MHz). Valorile sunt orientative, de comparat cu experiența din trafic. Factorul stației K și comparația cu RMOB se află în [Implementare experimentală a prognozelor](Experimental-Forecasts-ro).

## Fără conexiune

Dacă nicio sursă nu poate fi accesată, apare **o singură dată** un mesaj: *Fără conexiune la internet. Datele radarelor și RMOB nu pot fi actualizate: programul folosește ultimele date salvate și reîncearcă singur la fiecare 5 minute.* Bara de stare de jos devine roșie (*FĂRĂ CONEXIUNE LA INTERNET …*) până când conexiunea revine (*Conexiune restabilită.*).

## Arhive și surse

| Fișier (în `data/`) | Conținut |
|---|---|
| `flusso_collm.csv` | Arhiva orară a fluxului citit de la Collm (orele deja prezente sunt actualizate) |
| `quote_collm.csv` | Arhiva altitudinilor urmelor |
| `radar/` | Cele mai recente imagini descărcate (și fișierele RMOB) |
| `fonti_radar.csv` | Adresele surselor radar, `attivo=1/0` pentru a activa/dezactiva fiecare sursă |

| Sursă | Frecvență | Note |
|---|---|---|
| Radarul meteoric Collm, Universitatea din Leipzig (LIM) și IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | actualizat în fiecare oră la minutul 10 UTC; fluxul de ieri + azi, distribuția altitudinilor |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | doar imagine (radar în curs de modernizare, proiectul DECC) |
| swan.ms (copie a Collm) | 36,2 MHz | dezactivat implicit; folosește-l doar cu permisiunea lui DL1DBC |

> Datele radar aparțin instituțiilor lor (Universitatea din Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
