[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · **Eesti** · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Alustamine

Esimesel käivitusel näitab YA-MS näidistrassi (JN70CN → JO62QM sagedusel 144 MHz). Oma jaama jaoks seadistamiseks piisab viiest minutist.

## 1. Kolm juhtnuppude rida

Sakkide kohal on kolm juhtnuppude rida, mis kehtivad kõigil sakkidel. Paremal üleval olev nupp **Juhtnupud** peidab ja näitab neid (kasulik suure fondi korral); valik jäetakse meelde.

**Rida 1 – jaamad ja sagedusala**

| Juhtnupp | Mida see teeb |
|---|---|
| **Minu lokaator** / **kõrgus m** | Sinu Maidenheadi lokaator (4, 6 või 8 märki; kasutatakse ruudu keskpunkti) ja jaama kõrgus merepinnast. |
| **Korrespondent** / **kõrgus m** | Kaardi kõrval paremal on vastasjaama kast: kirjuta kutsung ja vajuta Enter, lokaator võetakse CALL3 andmebaasist (nagu YAEC-is ja LIVETROPOVHF-is); all on lokaator ja kõrgus. Kutsungi võib kirjutada ka lokaatori kasti. |
| **Sagedusala MHz** | 28, 50, 70, 144, 222 või 432 MHz: kasutatakse antenni võimenduse ja peaharu, vooluhinnangu ja lingi eelarve jaoks. |
| **Arvuta** | Arvutab trassi uuesti (E-kihi proovivõtt: mõni sekund). |
| **Antenni az** | Vastasjaama kasti ülaosas, kaardi kõrval: sinu antenni asimuut, alati **DX-i poole** (trassi asimuut). Selle all, samas veerus, on kaardi legend. |
| **Font** | Kogu teksti suurus, 85–140 %. Vt [Seaded](Settings-and-Data-Folder-et#font-ja-juhtnupud). |

**Rida 2 – E-kiht ja antenn**

| Juhtnupp | Mida see teeb |
|---|---|
| **Jälgede kõrgus km** + **radarilt** | Meteoorijälgede kõrgus (vaikimisi 90 km). Kui *radarilt* on märgitud, kasutatakse Collmi radari mõõdetud sagedaseimat kõrgust (moodi); vt [Radari voog](Radar-Flux-et). |
| **Peaharu elevatsioon °** | Antenni vertikaalse keila maksimumi kõrgusnurk: 0° peale kinnitatud suunaantennil on maapinnalt peegeldumise tõttu keil siiski mõne kraadi võrra horisondist kõrgemal (tavaliselt 3-8°). Kui kast **antenni suunadiagramm** on sees (vaikimisi), kaalutakse E-kihi punkte mõlema antenni vertikaalse suunadiagrammiga; väljas kasutatakse ainult punkte, mida mõlemad jaamad näevad sellest kõrgusnurgast kõrgemal. |
| **Yagi antenn: poom m** | Sinu Yagi poomi pikkus. Programm näitab pikkust λ-des, võimendust (DL6WU kõver) ja −3 dB peaharu horisontaalselt ja vertikaalselt; vt [Geomeetria ja sumbumine](Geometry-and-Path-Loss-et#antenni-võimendus-ja-peaharu). Alla 2 λ on hinnang ebatäpne. |
| **Hot spot keskpunktist km** + **auto (AMS)** | Hot A ja Hot B kaugus keskpunktist. Kui *auto (AMS)* on märgitud (vaikimisi), järgib see J. Richardsoni (AMS) antennisuuna nihete tabelit, mida tsiteerib DJ5HG: 13° 1000 km juures, 11° 1250 km juures, 10° 1500 ja 2000 km juures (umbes 115, 121, 132 ja 176 km keskpunktist). Eemalda märge, et sisestada 30–400 km käsitsi (MSHV kasutab 150 km). |

**Rida 3 – aeg**

| Juhtnupp | Mida see teeb |
|---|---|
| **Aeg** | UTC kell. |
| **Arvutuse kuupäev (UTC)** | Päev, mille kohta tehakse arvutus sakkidel [Prognoosarvutus](Sky-View-et) ja [GRAVESi radar](GRAVES-Radar-et) (vaikimisi tänane), praegusel kellaajal. Samuti: päev, mida näidatakse sakil [Efektiivsuse arvutus](Efficiency-Calculation-et) ja GRAVESi ajateljel. |
| **Tunnid (−12 kuni +36 h)** | Nihutab arvutuse hetke vahemikus 12 tundi enne kuni 36 tundi pärast seda kellaaega, 15-minutiliste sammudega. Kõrval: *Arvutus ajale: praegu* või *Arvutus ajale: dd/mm hh:mm UTC*. |
| **Reaalaeg** | Tagasi praegusesse hetke. |

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
