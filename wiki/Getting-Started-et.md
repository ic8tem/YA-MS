[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · **Eesti** · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Alustamine

Esimesel käivitusel näitab YA-MS näidistrassi (JN70CN → JO62QM sagedusel 144 MHz). Oma jaama jaoks seadistamiseks piisab viiest minutist.

## 1. Kolm juhtnuppude rida

Sakkide kohal on kolm juhtnuppude rida, mis kehtivad kõigil sakkidel. Paremal üleval olev nupp **Juhtnupud** peidab ja näitab neid (kasulik suure fondi korral); valik jäetakse meelde.

**Rida 1 – jaamad ja sagedusala**

| Juhtnupp | Mida see teeb |
|---|---|
| **Minu lokaator** / **kõrgus m** | Sinu Maidenheadi lokaator (4, 6 või 8 märki; kasutatakse ruudu keskpunkti) ja jaama kõrgus merepinnast. |
| **Korrespondent** / **kõrgus m** | Jaama lokaator ja kõrgus, kellega soovid sidet pidada. |
| **Sagedusala MHz** | 28, 50, 70, 144, 222 või 432 MHz: kasutatakse antenni võimenduse ja peaharu, vooluhinnangu ja lingi eelarve jaoks. |
| **Arvuta** | Arvutab trassi uuesti (E-kihi proovivõtt: mõni sekund). |
| **Antenni az** | Sinu antenni asimuut: alati **DX-i suunas** (trassi asimuut). |
| **Font** | Kogu teksti suurus, 100–300 %. Vt [Seaded](Settings-and-Data-Folder-et#font-ja-juhtnupud). |

**Rida 2 – E-kiht ja antenn**

| Juhtnupp | Mida see teeb |
|---|---|
| **Jälgede kõrgus km** + **radarilt** | Meteoorijälgede kõrgus (vaikimisi 90 km). Kui *radarilt* on märgitud, kasutatakse Collmi radari mõõdetud sagedaseimat kõrgust (moodi); vt [Radari voog](Radar-Flux-et). |
| **Peaharu elevatsioon °** | Sinu antenni peaharu madalaim elevatsioon (0° = horisont). Kasutatakse ainult neid E-kihi punkte, mida mõlemad jaamad näevad sellest elevatsioonist kõrgemal. |
| **Yagi antenn: poom m** | Sinu Yagi poomi pikkus. Programm näitab pikkust λ-des, võimendust (DL6WU kõver) ja −3 dB peaharu horisontaalselt ja vertikaalselt; vt [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et#antenni-võimendus-ja-peaharu). Alla 2 λ on hinnang ebatäpne. |
| **Hot spot keskpunktist km** | Hot A ja Hot B kaugus keskpunktist, 30–400 km (vaikimisi 150 km, nagu AMS Bulletin 203 / W8WN / MSHV). |

**Rida 3 – aeg**

| Juhtnupp | Mida see teeb |
|---|---|
| **Aeg** | UTC kell. |
| **Taevavõlvi aeg (±36 h)** | Nihutab [Taevavõlvi](Sky-View-et) ja saki [GRAVESi radar](GRAVES-Radar-et) kuni 36 tundi tagasi või edasi, 15-minutiliste sammudega. |
| **Reaalaeg** | Tagasi praegusesse hetke. |
| **Päev 24 h tabeli jaoks (UTC)** | Päev, mida näidatakse sakil [Efektiivsuse arvutus](Efficiency-Calculation-et) ja GRAVESi ajateljel. |

## 2. Sinu jaam ja korrespondent

1. Sisesta **Minu lokaator** ja **kõrgus m**.
2. Sisesta **korrespondendi** lokaator ja kõrgus – või klõpsa kaardil [Taevavõlvis](Sky-View-et): **vasakklõps = korrespondendi lokaator**, **paremklõps = minu jaama lokaator**.
3. Vali **Sagedusala MHz** ja vajuta **Arvuta**.

Allosas olev olekuriba kinnitab: *Trass arvutatud: … km, … peegelduspunkti valimiga … s jooksul*.

## 3. Sinu antenn

Sisesta oma Yagi **poomi pikkus**. Programm tuletab võimenduse ja peaharu ning hoiatab, kui Hot A või Hot B jäävad juba **peaharu sisse**, kui antenn on suunatud korrespondendile (siis joonistatakse need halliga: antenni pole vaja keerata).

## 4. Tulemuste lugemine

| Küsimus | Kust vaadata |
|---|---|
| Milline meteoorivool aitab praegu minu trassi ja kummalt poolt? | [Taevavõlv](Sky-View-et): meteoorivoolude loetelu, soovitatud Hot punasega, PREV alad |
| Mis on täna parim tund? | [Efektiivsuse arvutus](Efficiency-Calculation-et): ülevaatekaardid ja tunnitabel |
| Mitu meteoori radar loendab? | [Radari voog](Radar-Flux-et) |
| Mitu pingi võin oodata 144 MHz-l? | [Eksperimentaalsed prognoosid](Experimental-Forecasts-et) (eksperimentaalne) |
| Kas mu jaam suudab trassi läbida? | [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et): sumbumine ja varu |
| Millal on järgmine maksimum? | [Meteoorivoolud](Showers-et) |
| Kas saan GRAVESiga katsetada? | [GRAVESi radar](GRAVES-Radar-et) |

## Praktilised reeglid (allikatest)

- **Suuna risti meteoorivooluga**: parim trass on radiandi asimuudiga risti; parim suund = radiandi asimuut ±90°, tolerants ±40–50° (SM6FHZ).
- **Külghajumine**: keera antenni 10–30° selle poole (A või B), kust tuleb enamik peegeldusi (Cerrotta–Sartori artikkel).
- **Liiga kõrge radiant** (üle 70°) või liiga madal (alla 20°) annab vähe kasulikke jälgi (DF5HC, DH9GCD).
- Sporaadiliste meteooride maksimum on umbes **06 UTC** (artikkel; Collmi voog kinnitab).
- Kasulikud kaugused 432 MHz-l: 800–2000 km, parim umbes 1400 km (SM6FHZ); parim kaugus üldiselt 1300–1500 km (DF5HC).

Edasi: [Taevavõlv](Sky-View-et).
