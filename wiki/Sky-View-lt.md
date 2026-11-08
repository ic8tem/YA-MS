**English** · [Русский](Sky-View-ru) · [Deutsch](Sky-View-de) · [日本語](Sky-View-ja)

# Dangaus skliautas

*Kortelė: Prognozės skaičiavimas › Prognozės skaičiavimas.*

[![Dangaus skliautas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Ši vidinė kortelė (ankstesnių versijų dangaus skliautas) viename ekrane parodo, **kur** dabar yra naudingi pėdsakai ir **kur** nukreipti anteną. Kairėje – trasos **planas**; dešinėje – srautų sąrašas, mažas dangaus skliautas su radiantais, skaičiavimo tekstas ir iš jūsų antenos matomas **pjūvis**. Viskas susieta su slankiklio *Dangaus skliauto laikas* laiku (pagal nutylėjimą realus laikas; ±36 h 15 minučių žingsniais).

Mažame dangaus skliaute per zenitą einanti **oranžinė linija** visada rodo **tinkamas antenos kryptis**, statmenas pasirinkto (arba palankiausio) srauto slinkimui: radianto azimutas ±90°, abiejuose galuose pažymėta *antena NNN°*, ±45° tolerancija – plonomis linijomis. Trumpi oranžiniai brūkšneliai krašte rodo kitų naudingų srautų statmenas kryptis.

## Planas (kairėje)

Europos žemėlapis, matomas iš viršaus (**R dešinėje**), su laipsnių skale aplink. Užrašas po žemėlapiu nurodo jo spindulį (*Žemėlapis: kraštas = … km nuo stoties*).

| Elementas | Vaizdavimas |
|---|---|
| Trasa / DX | Žalia linija nuo jūsų stoties iki korespondento (visada reali didžiojo apskritimo trasa tarp lokatorių) |
| **Hot A / Hot B** | Taškai 150 km (reguliuojama) abipus vidurio taško, statmenai trasai. **Raudona = rekomenduojamas**, **rožinė = už antenos lapelio**, **pilka = lapelyje** (su įspėjimu) |
| Antenos lapelis | −3 dB horizontalusis lapelis aplink antenos azimutą (antena visada nukreipta į DX), pažymėtas *lapelis …°* |
| Bendrosios zonos ribos | Blankūs taškai *rib. A* / *rib. B* ir du apskritimai, kur kiekvienos stoties horizontas susitinka su E sluoksniu (žr. [Geometrija](Geometry-and-Path-Loss-lt#bendrosios-zonos-ribos)) |
| Srauto slinkimas | **Geltona linija**: kryptis, kuria pasirinktas (arba palankiausias) srautas brauko dangų, t. y. radianto azimutas |
| Geriausi nukreipimai | **Oranžiniai taškai**: dvi kryptys, statmenos slinkimui (radianto azimutas ±90°, SM6FHZ) |
| **PREV zonos** | Šviesios elipsės: kur **dabar** krenta labiausiai tikėtini pėdsakai, po vieną kiekvienoje trasos pusėje |

Užrašai nepersidengia: Hot A ir PREV A rašomi trasos kairėje, B – dešinėje. **Legenda** – suskleidžiamas stulpelis žemėlapio dešinėje.

**Pelė žemėlapyje:** **kairysis spustelėjimas = korespondento lokatorius**, **dešinysis spustelėjimas = mano stoties lokatorius**. Trasa iš karto perskaičiuojama.

Parinktys virš srautų sąrašo: **Hot A / Hot B kryptys**, **Europos žemėlapis** (Natural Earth, atsisiunčiamas į `data/mappa` pirmą kartą paleidžiant), **Vaizdas iš viršaus (R dešinėje)**.

### Rekomenduojamas Hot

Rodomam laikui programa susumuoja visų virš horizonto esančių srautų svorį ZHR × efektyvumas, padalytą tarp pusės A (dalis f_A) ir pusės B. Didesnio svorio pusė duoda rekomenduojamą Hot, piešiamą raudonai:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*Programos sprendimas (vadovo 23 lygtis).* Idėjos šaltinis: DJ5HG, pateikė DF5HC (DARC konferencija 2018) – priklausomai nuo radianto padėties vienas iš dviejų taškų, HOT-A arba HOT-B, yra palankesnis. Pasukimas 10–30° į tą pusę (šoninė sklaida) paimtas iš Cerrotta–Sartori straipsnio.

### PREV zonos

Kiekvienam E sluoksnio taškui P susumuojami visų aktyvių srautų indėliai į efektyvumą (ta pati veidrodinio atspindžio sąlyga kaip [efektyvumo](Efficiency-Calculation-lt#modelis) atveju), pasverti ZHR. Taškai, siekiantys bent 3 % maksimumo, sudaro PREV zonas; kiekviena piešiama kaip elipsė, kurios centras = svertinis taškų vidurkis, o ašys = dvigubas jų išsibarstymas.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Programos sprendimas (vadovo 34 lygtis).* Tai praktinė taisyklė: jei srautas brauko iš šiaurės į pietus, naudingi pėdsakai krenta rytuose ir vakaruose.

## Srautų sąrašas (viršuje dešinėje)

| Stulpelis | Reikšmė |
|---|---|
| Srautas, Kodas | Pavadinimas ir IMO kodas |
| ZHR dabar | Aktyvumas šiuo momentu (IMO maksimumo ZHR su aktyvumo profiliu) |
| Azimutas, Elev. | Radianto padėtis, matoma iš jūsų stoties |
| Efekt. % | Srauto efektyvumas šiai trasai |
| Pusė | A arba B – pusė, iš kurios ateina dauguma atspindžių |
| Geriausias nukr. | Radianto azimutas ±90° |
| Teka, Leidžiasi | Radianto patekėjimas ir nusileidimas (UTC); kai taikoma – *cirkumpoliarinis* arba *visada žemiau* |

Spustelėkite eilutę srautui pasirinkti: geltona slinkimo linija ir oranžiniai taškai seka jį.

## Mažas dangaus skliautas (dešinėje per vidurį)

Radiantai dangaus skliaute, matomame iš jūsų stoties, su **IMO kodu** ir **paros keliu žydra spalva** (UTC valandos). **Spustelėkite radiantą**, kad jį pasirinktumėte. Spalvos:

| Spalva | Reikšmė |
|---|---|
| Geltona | efektyvumas ≥ 50 % ir ZHR ≥ 2 |
| Oranžinė | efektyvumas ≥ 20 % |
| Tamsiai raudona | efektyvumas < 20 % |
| Pilka | beveik neaktyvus |

Šalia – skaičiavimo tekstas: trasos ilgis ir azimutas, vidurio taškas ir jo elevacija, Hot A / Hot B azimutai ir nuokrypiai, rekomenduojamas Hot (*… rekomenduojamas dabar: az. …° (…% numatomų atspindžių)*), bendrosios zonos ribos ir priminimas: *geriausias nukreipimas srautui: STATMENAI atėjimo krypčiai (radianto azimutas ±90°, tolerancija ±40–50°, SM6FHZ)*.

## Pjūvis (apačioje dešinėje)

*PJŪVIS – labiausiai tikėtini pėdsakai, matomi iš antenos korespondento kryptimi.* Horizontaliai – **azimutas korespondento atžvilgiu** (← A kairėje, B → dešinėje), vertikaliai – **elevacija**. Kiekvienam srautui imami 14 stipriausių atspindžio taškų; kiekvienas pėdsakas yra į radiantą orientuota atkarpa nuo 10 km virš iki 10 km žemiau pėdsakų aukščio (ne daugiau kaip 60 km į kiekvieną pusę), tuo storesnė, kuo labiau tikėtina. Taip pat piešiami antenos lapelis (−3 dB apskritimas aplink lapelio elevaciją), korespondentas ir Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Programos sprendimas (vadovo 35 lygtis).*

## Įspėjimai

| Įspėjimas | Kada |
|---|---|
| **DĖMESIO: Hot A (ir (arba) Hot B) patenka į antenos lapelį …** | Hot spot yra ±θ/2 ribose nuo antenos azimuto (θ = horizontalusis −3 dB lapelis): šiuo nukreipimu jis jau padengtas. Žemėlapyje rodomas pilkai. Rekomenduojamas Hot lieka raudonas. |
| **RADIANTAS PER AUKŠTAI (virš 70°)** | Naudingas radiantas yra aukščiau nei 70° iš jūsų stoties: pėdsakai krenta beveik vertikaliai ir mažai atspindi trasos kryptimi (DF5HC, DH9GCD). Tos pačios valandos [valandinėje lentelėje](Efficiency-Calculation-lt#valandinė-lentelė) pažymėtos ↑. |
| *Nėra bendrosios E sluoksnio zonos* | Trasa ilgesnė nei dvigubas nuotolis pėdsakų aukštyje: abi stotys nemato bendros E sluoksnio dalies (vienas šuolis neįmanomas). |
| *Nėra rekomenduojamo Hot* | Šiuo metu beveik nėra aktyvių srautų. |

Dangaus skliauto grafikos pavyzdys: DL1DBC Swan Meteor Skyview (swan.ms); polinė diagrama su geriausia kryptimi: SM6FHZ RadiantCalc.
