[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · **Magyar** · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Meteorrajok

*Fül: Meteorrajok.*

[![Meteorrajok](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Az összes számítás által használt rajkatalógus: **45 raj** az **IMO Meteor Shower Calendar 2026 és 2027** kiadványaiból (5. és 7. táblázat), valamint az **Antihelion-forrás** (6. táblázat), mindegyik a **következő csúccsal**.

## Oszlopok

| Oszlop | Jelentés |
|---|---|
| Kód | IMO-kód (QUA, PER, GEM, …) |
| Raj | Név |
| Aktivitás | Aktivitási időszak (nap/hónap – nap/hónap) |
| λ max | A csúcs napközépponti hosszúsága (J2000), az IMO-tól |
| **Következő csúcs (UTC)** | A következő csúcs dátuma és időpontja (lásd lent) |
| **A csúcs forrása** | *IMO 2026* / *IMO 2027* = az IMO által közzétett dátum és időpont; *IMO 2026 (nap)* = az IMO csak a napot adja meg, a megjelenített időpont számított (*~óó:pp szám.*); *λ-ból számítva* = arra az évre nincs IMO-érték |
| Rekt., Dekl. | A radiáns a csúcsnál (az Antihelion-forrásnál *mozgó*) |
| v km/s, r | Geocentrikus sebesség és populációindex |
| ZHR | Csúcs-ZHR (*vált.* = változó) |
| Típus | *vizuális* vagy *rádiós, nappali* |

A **ma (UTC) aktív** rajok sárga háttérrel és félkövér szöveggel ki vannak emelve.

## Következő csúcs

A program mindig a **következő** csúcsot mutatja. Ha az IMO már közzétette az adott év naptárát, a `data/massimi_imo.csv` fájlban lévő **IMO-dátumot és -időpontot** használja (2026 és 2027 benne van); ellenkező esetben kiszámítja azt a pillanatot, amikor a Nap eléri a csúcs napközépponti hosszúságát (Meeus, *Astronomical Algorithms*, 25. fejezet, Newton-módszerrel megoldva).

**Ellenőrzés:** a számítás néhány percen belül egyezik az IMO 2026-os és 2027-es naptárával ott, ahol az IMO megadja az időpontot (pl. Quadrantidák 2026. 1. 3. 21:13 a 21:00-val szemben; Geminidák 2027. 12. 14. 19:51 a 20:00-val szemben). Kivételek: a Daytime kappa Leonids 2026-ban egy nappal később (9. 26. a 9. 25. helyett) és az eta Aquariidák időpontja 2027-ben (15:10 az IMO 09:00-s értékével szemben) – ezekben az esetekben az IMO-értéket használja.

**Új év hozzáadása:** amikor az IMO új naptárat tesz közzé, vegye fel annak sorait a `data/massimi_imo.csv` fájlba (`year;code;MM-DD;hh:mm`, az időpont üres, ha az IMO csak a napot adja meg). Addig a csúcsot a program számítja.

## Kisebb és nappali rajok

A katalógus tartalmazza az IMO-lista **kisebb rajait** – például az Októberi Camelopardalidákat (OCT, ZHR 5, aktív október 5–6.), az Andromedidákat, a gamma Ursae Minoridákat – és az április–októberi **nappali rádiós rajokat** (Daytime April Piscids, Daytime Arietids, Daytime zeta Perseids, Daytime beta Taurids, Daytime kappa Leonids, Daytime Sextantids, …). Kis ZHR mellett is hozzájárulnak az [útvonalindexhez](Efficiency-Calculation-hu#a-modell) és az [ajánlott Hot](Sky-View-hu#ajánlott-hot) meghatározásához. A nappali rádiós rajokra az IMO nem ad ZHR-t: ahol nincs megadva, a program 5-ös üzemi értéket használ.

## Aktivitási profil és a radiáns vándorlása

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 és λ_max az IMO-naptárból; a B meredekségek (a csúcs előtt és után eltérőek) és a dα/dλ, dδ/dλ napi vándorlások a `data/sciami.csv` fájlba írt **üzemi értékek** (az IMO vándorlási táblázata még nincs felvéve). *Kézikönyv, 9. és 13. egyenlet.* Az Antihelion-forrás helyzetét lineáris interpolációval számítja az IMO 6. táblázatának dátumai között (`data/ant_radiante.csv`; aktív december 10. – szeptember 20., ZHR kb. 4).

## A katalógus szerkesztése

A `data/sciami.csv` egyszerű szövegfájl (elválasztó: `;`), amelyet szerkeszthet: kód, név, kezdet és vég (MM-DD), λ max, rekt., dekl., vándorlások, v, r, ZHR, B előtte/utána, típus (V vizuális, R nappali rádiós). Ha egy sor hibás, a program induláskor üzenetet jelenít meg, és figyelmen kívül hagyja.

Források: International Meteor Organization – Meteor Shower Calendar 2026 és 2027, [www.imo.net](https://www.imo.net) (5., 6. és 7. táblázat); Rossano IZ5TEK (scattertek).
