[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · **Magyar** · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [ไทย](Troubleshooting-FAQ-th) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Hibaelhárítás és GYIK

## Telepítés és indítás

### A Windows SmartScreen azt írja: „A Windows megvédte a számítógépet”
A program nincs kereskedelmi tanúsítvánnyal aláírva. Kattintson a *További információ* → *Futtatás mindenképp* lehetőségre. Csak a [Releases](https://github.com/ic8tem/YA-MS/releases) oldalról töltse le.

### macOS: nem nyitható meg, mert azonosítatlan fejlesztőtől származik
A YA-MS-t nem írta alá az Apple, ezért a **Gatekeeper** első alkalommal blokkolja. A `.dmg`-ben **kattintson jobb gombbal az „Installa YA-MS.command” elemre → Megnyitás**, és erősítse meg. A szkript eltávolítja az „internetről letöltve” karantén-jelzőt a `~/YA-MS/YA-MS.app` alkalmazásról, és megnyitja. Ha a macOS továbbra is elutasítja, nyissa meg a *Rendszerbeállítások → Adatvédelem és biztonság* panelt, és nyomja meg a *Megnyitás mindenképp* gombot.

### macOS: melyik .dmg?
`-mac-apple-silicon.dmg` M1/M2/M3/M4 processzorokhoz, `-mac-intel.dmg` Intel alapú Macekhez (az Apple menü → *Erről a Macről* megmutatja, melyik van Önnek).

### Linux: a YA-MS nem szerepel az alkalmazásmenüben
Futtassa a `./installa.sh` szkriptet a kicsomagolt mappából (nem a `~/YA-MS` mappából). Egyes asztali környezetekben ki- és be kell jelentkezni, hogy az új bejegyzések megjelenjenek. A programot mindig elindíthatja a `~/YA-MS/YA-MS` paranccsal.

### Hiányzik az Európa-térkép
*Az Európa-térkép nem érhető el (az első indításhoz hálózat szükséges).* A Natural Earth térkép első indításkor töltődik le a `data/mappa` mappába. Csatlakozzon az internethez, és indítsa újra a YA-MS-t.

## Megjelenítés

### Linux: a japán szöveg helyén négyzetek jelennek meg
A rendszeréből hiányoznak a CJK betűtípusok. Telepítse a **Noto CJK** betűtípusokat, és indítsa újra a YA-MS-t:

| Disztribúció | Parancs |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### A szöveg túl kicsi, vagy a diagramoknak nincs elég helyük
Használja a **Betűtípus** csúszkát (100–300 %), és csukja össze a sorokat a **Vezérlők** gombbal. Lásd [Beállítások](Settings-and-Data-Folder-hu#betűtípus-és-vezérlők).

### Éjszaka túl világos a képernyő
Válassza az **Éjszaka** vagy a **Fekete** sémát a **Téma** listában.

## Internet és radaradatok

### „Nincs internetkapcsolat” üzenet
A YA-MS **egyszer** jeleníti meg, ha egyetlen forrás sem érhető el; az állapotsor pirosra vált. A program az **utoljára mentett adatokkal** dolgozik tovább, és 5 percenként magától újrapróbálkozik; amikor a hálózat visszatér, megjelenik *A kapcsolat helyreállt.* üzenet. Nincs teendő.

### Narancs figyelmeztetés a Radarfluxus fülön: „A függőleges fluxusskála nem olvasható …”
A Collm radar naponta változtatja a függőleges skáláját, és a YA-MS a diagram feliratairól olvassa le. Ha egy felirat nem olvasható, a program a kalibrált 0–1200 meteor/óra skálát használja, és figyelmeztet, hogy **az értékeket ellenőrizni kell**. Általában a következő órai diagramot már helyesen olvassa be. Ha sok órán át *A diagram formátuma megváltozott* vagy *A fluxustengelyek nem a várt helyen vannak* üzenetet lát, a radar megváltoztatta a diagram formátumát: kérjük, [jelezze](Contributing-and-Contacts-hu).

### „A magassági diagram skálája megváltozott”
A magassági statisztikák (módusz, átlag, medián) érvényesek maradnak; csak a magassági hisztogram abszolút számai nem.

### „Radarfluxus: nincs adat”
Nyomja meg a **Letöltés most** gombot a [Radarfluxus](Radar-Flux-hu) fülön, és ellenőrizze, hogy a `data/fonti_radar.csv` fájlban a Collm sorában `attivo=1` szerepel-e.

### RMOB: miért van kikapcsolva az automatikus letöltés?
Az RMOB azt kéri, hogy **automatikus programok ne töltsék le a fájljait**. Az *automatikus letöltés 5 percenként* lehetőséget csak azután kapcsolja be, hogy az RMOB engedélyt adott rá. Addig használja az **RMOB letöltése most** vagy az **RMOB-fájl betöltése lemezről...** lehetőséget. Lásd [Kísérleti előrejelzések](Experimental-Forecasts-hu#az-rmob-és-az-automatikus-programok).

### RMOB: „Ismeretlen fájlformátum” vagy kevés beolvasott óra
Használja a megfigyelő havi szövegfájlját (`NAME_MMYYYYrmob.TXT`) vagy egyetlen megfigyelőt tartalmazó közlöny-táblázatot. A kitevő illesztéséhez legalább 3 közös óra szükséges a Collm-adatokkal (tegnap és ma).

## Számítások

### „Érvénytelen állomáslokátor” / „Érvénytelen DX-állomás lokátor”
A lokátornak 4, 6 vagy 8 karakterből kell állnia (pl. `JN70`, `JN70CN`, `JN70CN12`).

### „Nincs közös E-réteg-zóna”
Az útvonal hosszabb, mint a nyommagasságban mért hatótávolság kétszerese (kb. 2 × 1062 km 0°-os lebenynél és 89,5 km-es nyomoknál): egyetlen meteor scatter ugrás nem tudja áthidalni. A **Lebeny elevációja** növelése tovább csökkenti a hatótávolságot.

### A Hot A / Hot B szürke
Már **az antennalebenyen belül** vannak, amikor az antenna a DX felé néz: nem kell elfordítani. Lásd [Égbolt-kupola](Sky-View-hu#figyelmeztetések).

### A hatékonyság eltér az MCG_MS vagy az MS-Soft eredményétől
A YA-MS a valódi útvonalat és saját modelljét használja; az OH5IY és az MCG_MS skálája nincs részletesen dokumentálva. Inkább az órákat és a tendenciákat hasonlítsa össze, ne az abszolút százalékokat, és nézze meg a [modellt](Efficiency-Calculation-hu#a-modell).

### A GRAVES nyaláb áthaladása eltolódottnak tűnik
A nyalábsorrendet a program a PC órájából számítja: szinkronizálja egy NTP-szerverrel. A GRAVES vezérlőállomása is időnként néhány lépéssel eltolja a sorrendet; a részletezés előrejelzés, amelyet hallgatással kell megerősíteni.

## Egyéb kérdések

**Ingyenes a YA-MS?** Igen, ingyenes program rádióamatőrök számára.

**Vezérli a rotoromat vagy a rádiómat?** Nem. A YA-MS előrejelző és tervező eszköz; az összeköttetéshez használja a digitális üzemmódú programját (pl. MSHV, WSJT-X).

**Működik 432 MHz felett?** A sávlista 432 MHz-nél véget ér (28, 50, 70, 144, 222, 432). A kísérleti előrejelzés bármilyen frekvenciát elfogad 28 és 1300 MHz között, de az általa használt SM6FHZ-szabályok a 144 és 432 MHz-es tapasztalatokból származnak.

**Valami nem sikerült.** Írjon a szerzőnek, megadva az operációs rendszerét, a YA-MS változatszámát és azt, amit tett: lásd [Közreműködés és kapcsolat](Contributing-and-Contacts-hu).
