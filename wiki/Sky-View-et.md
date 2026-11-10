[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · **Eesti** · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Taevavõlv

*Sakk: Prognoosarvutus › Prognoosarvutus.*

[![Taevavõlv](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

See alamsakk (varasemate versioonide taevavõlv) näitab ühel ekraanil, **kus** kasulikud jäljed praegu on ja **kuhu** antenn suunata. Vasakul trassi **pealtvaade**; paremal meteoorivoolude loetelu, väike taevavõlv radiantidega, arvutuse tekst ja sinu antennist nähtav **lõige**. Kõik viitab hetkele, mis on valitud väljaga *Arvutuse kuupäev (UTC)* ja liuguriga *Tunnid (−12 kuni +36 h)* (vaikimisi reaalaeg, 15-minutiliste sammudega).

**Pealtvaate kohal olev riba** võtab selle hetke arvutuse kokku: kuupäev ja kellaaeg (*praegu* või tunnid praegusest), **trassi indeks Σ ZHR×η**, **kõige kasulikum meteoorivool** koos oma ZHR-i ja efektiivsusega (ka dB-des DJ5HG viite suhtes, vt [Efektiivsuse arvutus](Efficiency-Calculation-et)), horisondi kohal olevate meteoorivoolude arv ning **soovitatud Hot** koos asimuudiga.

Väikeses taevavõlvis näitab läbi seniidi kulgev **oranž joon** alati **õigeid antennisuundi**, mis on risti valitud (või kõige soodsama) meteoorivoolu nihkumisega: radiandi asimuut ±90°, mõlemas otsas silt *antenn NNN°*, ±45° tolerants peente joontena. Lühikesed oranžid kriipsud serval näitavad teiste kasulike meteoorivoolude ristsuundi.

## Pealtvaade (vasakul)

Ülalt vaadatud Euroopa kaart (**E paremal**), ümber kraadiskaala. Kaardi all olev allkiri annab selle raadiuse (*Kaart: serv = … km jaamast*).

| Element | Joonis |
|---|---|
| Trass / DX | Roheline joon sinu jaamast korrespondendini (alati lokaatorite vaheline tegelik suurringjoone trass) |
| **Hot A / Hot B** | Punktid mõlemal pool keskpunkti, trassiga risti, AMS-i nihketabeli antud (või käsitsi sisestatud) kaugusel. **Punane = soovitatud**, **roosa = väljaspool antenni peaharu**, **hall = peaharus** (koos hoiatusega) |
| Antenni peaharu | −3 dB horisontaalne peaharu antenni asimuudi ümber (antenn alati suunatud DX-ile), silt *peaharu …°* |
| Ühisala piirid | Kahvatud punktid *piir A* / *piir B* ja kaks ringi, kus kummagi jaama horisont kohtub E-kihiga (vt [Geomeetria](Geometry-and-Path-Loss-et#ühisala-piirid)) |
| Meteoorivoolu nihkumine | **Kollane joon**: suund, milles valitud (või kõige soodsam) meteoorivool taevast pühib, st radiandi asimuut |
| Parimad suunad | **Oranžid punktid**: kaks nihkumisega risti olevat suunda (radiandi asimuut ±90°, SM6FHZ) |
| **PREV alad** | Heledad ellipsid: kuhu **praegu** langevad kõige tõenäolisemad jäljed, üks kummalgi pool trassi |

Sildid ei kattu: Hot A ja PREV A kirjutatakse trassist vasakule, B paremale. **Legend** on kaardist paremal asuv kokkupandav veerg.

**Hiir kaardil:** **vasakklõps = korrespondendi lokaator**, **paremklõps = minu jaama lokaator**. Trass arvutatakse kohe uuesti.

Valikud meteoorivoolude loetelu kohal: **Hot A / Hot B suunad**, **Euroopa kaart** (Natural Earth, laaditakse esimesel käivitusel kausta `data/mappa`), **Pealtvaade (E paremal)**.

### Soovitatud Hot

Näidatud aja jaoks liidab programm kõigi horisondi kohal olevate meteoorivoolude kaalu ZHR × efektiivsus, jagatuna poole A (osa f_A) ja poole B vahel. Suurema kaaluga pool annab soovitatud Hoti, mis joonistatakse punasega:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Programmi valik (juhendi võrrand 23).* Idee allikas: DJ5HG, vahendanud DF5HC (DARC-i konverents 2018) – olenevalt radiandi asendist on üks kahest punktist, HOT-A või HOT-B, soodsam. 10–30° pööramine selle poole (külghajumine) pärineb Cerrotta–Sartori artiklist.

### PREV alad

Iga E-kihi punkti P jaoks liidetakse kõigi aktiivsete meteoorivoolude panused efektiivsusse (sama peegeltingimus nagu [efektiivsuse](Efficiency-Calculation-et#mudel) puhul), kaalutuna ZHR-iga. Punktid, mis on vähemalt 3 % maksimumist, moodustavad PREV alad; iga ala joonistatakse ellipsina, mille keskpunkt = punktide kaalutud keskmine ja teljed = kahekordne hajuvus.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Programmi valik (juhendi võrrand 34).* See on praktiline reegel: kui meteoorivool pühib põhjast lõunasse, langevad kasulikud jäljed itta ja läände.

## Meteoorivoolude loetelu (paremal üleval)

| Veerg | Tähendus |
|---|---|
| Meteoorivool, Lühend | Nimi ja IMO lühend |
| ZHR praegu | Aktiivsus sel hetkel (IMO maksimumi ZHR koos aktiivsusprofiiliga) |
| Asimuut, Elev. | Radiandi asend sinu jaamast vaadatuna |
| Efekt. % | Meteoorivoolu efektiivsus selle trassi jaoks |
| Pool | A või B, pool, kust tuleb enamik peegeldusi |
| Parim suund | Radiandi asimuut ±90° |
| Tõus, Loojang | Radiandi tõus ja loojang (UTC); vajaduse korral *tsirkumpolaarne* või *alati all* |

Meteoorivoolu valimiseks klõpsa real: kollane nihkumisjoon ja oranžid punktid järgivad seda.

## Väike taevavõlv (paremal keskel)

Radiandid sinu jaamast nähtaval taevavõlvil koos **IMO lühendi** ja **ööpäevase liikumisteega tsüaansinisena** (UTC tunnid). **Klõpsa radiandil**, et see valida. Värvid:

| Värv | Tähendus |
|---|---|
| Kollane | efektiivsus ≥ 50 % ja ZHR ≥ 2 |
| Oranž | efektiivsus ≥ 20 % |
| Tumepunane | efektiivsus < 20 % |
| Hall | peaaegu mitteaktiivne |

Selle kõrval arvutuse tekst: trassi pikkus ja asimuut, keskpunkt ja selle elevatsioon, Hot A / Hot B asimuudid ja nihked, soovitatud Hot (*… praegu soovitatud: az. …° (…% oodatud peegeldustest)*), ühisala piirid ja meeldetuletus: *parim suund meteoorivoolu jaoks: RISTI saabumissuunaga (radiandi asimuut ±90°, tolerants ±40–50°, SM6FHZ)*.

## Lõige (paremal all)

*LÕIGE – kõige tõenäolisemad jäljed antennist korrespondendi suunas vaadatuna.* Horisontaalteljel **asimuut korrespondendi suhtes** (← A vasakul, B → paremal), vertikaalteljel **elevatsioon**. Iga meteoorivoolu jaoks võetakse 14 tugevaimat peegelduspunkti; iga jälg on radiandi poole suunatud lõik 10 km kõrgemalt kuni 10 km madalamale jälgede kõrgusest (kuni 60 km kummalegi poole), seda jämedam, mida tõenäolisem. Joonistatakse ka antenni peaharu (−3 dB ring peaharu elevatsiooni ümber), korrespondent ja Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Programmi valik (juhendi võrrand 35).*

## Hoiatused

| Hoiatus | Millal |
|---|---|
| **HOIATUS: Hot A (ja/või Hot B) jääb antenni peaharusse …** | Hot spot on antenni asimuudist ±θ/2 piires (θ = horisontaalne −3 dB peaharu): selle suunaga on see juba kaetud. Kaardil hallina. Soovitatud Hot jääb punaseks. |
| **RADIANT LIIGA KÕRGEL (üle 70°)** | Kasulik radiant on sinu jaamast üle 70°: jäljed langevad peaaegu vertikaalselt ja peegeldavad trassi suunas vähe (DF5HC, DH9GCD). Samad tunnid on [tunnitabelis](Efficiency-Calculation-et#tunnitabel) märgitud ↑-ga. |
| **MADAL RADIANT PIKI TRASSI** | Aktiivne radiant on alla 20° ja trassi suunast vähem kui 30° kaugusel. Arvutatud efektiivsus jääb madalaks (ettevaatlik), kuid DJ5HG ootab harvu tugevaid peegeldusi trassiga joondatud riivavatelt jälgedelt (Hamburg–Narvik, kvadrantiidid, umbes 19 UTC): tasub kuulata. |
| **TRASS JÄLGEDE HORISONDIST KAUGEMAL** | Jälgede kõrgusel on trassi keskpunkt mõlema jaama horisondi all (umbes 2120 km, kui jäljed on 90 km kõrgusel). Hoiatus annab vajaliku minimaalse jälgede kõrguse (umbes 96 km 2200 km jaoks, 105 km 2300 km jaoks): side on võimalik ainult kõrgeimate jälgedega ning efektiivsused ja sumbumised on mudeli piiril. |
| *E-kihi ühisala puudub* | Trass on pikem kui kahekordne ulatus jälgede kõrgusel: kaks jaama ei näe E-kihi ühist osa (üks hüpe võimatu). |
| *Soovitatud Hot puudub* | Sel ajal pole peaaegu ühtegi aktiivset meteoorivoolu. |

Taevavõlvi graafika eeskuju: DL1DBC Swan Meteor Skyview (swan.ms); polaardiagramm parima suunaga: SM6FHZ RadiantCalc.
