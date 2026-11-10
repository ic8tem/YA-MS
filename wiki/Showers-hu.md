[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · **Magyar** · [Română](Showers-ro) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Rajok

*Fül: Rajok.*

[![Rajok](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Az összes számításhoz használt rajkatalógus: **45 raj** az **IMO Meteor Shower Calendar 2026 és 2027** alapján (5. és 7. táblázat), valamint az **Antihelion-forrás** (6. táblázat), mindegyik a **következő csúcsával**.

## Oszlopok

| Oszlop | Jelentés |
|---|---|
| Kód | IMO-kód (QUA, PER, GEM, …) |
| Raj | Név |
| Aktivitás | Aktivitási időszak (nap/hónap – nap/hónap) |
| λ max | A csúcs napi hosszúsága (J2000), az IMO szerint |
| **Következő csúcs (UTC)** | A következő csúcs dátuma és időpontja (lásd alább) |
| **Csúcsforrás** | *IMO 2026* / *IMO 2027* = az IMO által közzétett dátum és időpont; *IMO 2026 (nap)* = az IMO csak a napot adja meg, a kijelzett időpont számított (*~óó:pp számított*); *λ-ból számítva* = arra az évre nincs IMO-érték |
| Rekt., Dekl. | A radiáns a csúcskor (*mozgó* az Antihelion-forrásnál) |
| v km/s, r | Geocentrikus sebesség és populációs index |
| ZHR | Csúcs-ZHR (*vált.* = változó) |
| Típus | *vizuális* vagy *rádió, nappali* |
| Ma aktív | *igen*, ha a raj most aktív |

## Következő csúcs

A program mindig a **következő** csúcsot mutatja. Ha az IMO közzétette az adott évi naptárt, a `data/massimi_imo.csv` fájlban szereplő **IMO dátumot és időpontot** használja (2026 és 2027 benne van); egyébként kiszámítja azt a pillanatot, amikor a Nap eléri a csúcs napi hosszúságát (Meeus, *Astronomical Algorithms*, 25. fejezet, Newton-módszerrel megoldva).

**Ellenőrzés:** a számítás néhány percen belül egyezik az IMO 2026-os és 2027-es naptárával ott, ahol az IMO megadja az időpontot (pl. Kvadrantidák 2026. 1. 3. 21:13, szemben a 21:00-val; Geminidák 2027. 12. 14. 19:51, szemben a 20:00-val). Kivételek: a Nappali kappa Leonidák 2026-ban egy nappal később (9. 26. a 9. 25. helyett) és az éta Aquariidák 2027-es időpontja (15:10, szemben az IMO 09:00-jával) – ezekben az esetekben az IMO-értéket használja.

**Új év hozzáadása:** amikor az IMO új naptárt tesz közzé, adja hozzá a sorait a `data/massimi_imo.csv` fájlhoz (`year;code;MM-DD;hh:mm`, az időpont üresen marad, ha az IMO csak a napot adja meg). Addig a csúcs számított.

## Kisebb és nappali rajok

A katalógus tartalmazza az IMO-lista **kisebb rajait** – például az Októberi Camelopardalidákat (OCT, ZHR 5, aktív október 5–6.), az Andromedidákat, a gamma Ursae Minoridákat –, valamint az április–október közötti **nappali rádiós rajokat** (Nappali áprilisi Piscidák, Nappali Arietidák, Nappali zéta Perseidák, Nappali béta Tauridák, Nappali kappa Leonidák, Nappali Sextantidák, …). Kis ZHR-rel is hozzájárulnak az [útvonalindexhez](Efficiency-Calculation-hu#a-modell) és az [ajánlott Hot](Sky-View-hu#ajánlott-hot) pont meghatározásához. A nappali rádiós rajokra az IMO nem ad meg ZHR-t: ahol nincs megadva, a program 5-ös munkaértéket használ.

## Aktivitási profil és a radiáns elmozdulása

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

A ZHR_max, α0, δ0 és λ_max az IMO-naptárból származik; a B meredekségek (a csúcs előtt és után eltérők) és a dα/dλ, dδ/dλ napi elmozdulások a `data/sciami.csv` fájlba írt **munkaértékek** (az IMO elmozdulási táblázatát még nem vitték fel). *Kézikönyv, 9. és 13. egyenlet.* Az Antihelion-forrás helyzetét a program lineárisan interpolálja az IMO 6. táblázatának dátumai között (`data/ant_radiante.csv`; aktív december 10. – szeptember 20., ZHR kb. 4).

## A katalógus szerkesztése

A `data/sciami.csv` egyszerű, szerkeszthető szövegfájl (elválasztó: `;`): kód, név, kezdet és vég (MM-DD), λ max, Rekt., Dekl., elmozdulások, v, r, ZHR, B előtte/utána, típus (V vizuális, R nappali rádiós). Ha egy sor hibás, a program induláskor üzenetet jelenít meg, és figyelmen kívül hagyja a sort.

Források: International Meteor Organization – Meteor Shower Calendar 2026 és 2027, [www.imo.net](https://www.imo.net) (5., 6. és 7. táblázat); Philip G0ISW (legnagyobb rádiós óránkénti gyakoriságok); Rossano IZ5TEK (scattertek).
