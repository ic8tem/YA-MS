**English** · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh)

# Hibaelhárítás és GYIK

## Telepítés és indítás

### A Windows SmartScreen azt írja: „A Windows megvédte a számítógépet”
A program nincs kereskedelmi tanúsítvánnyal aláírva. Kattintson a *További információ* → *Futtatás mindenképp* lehetőségre. Csak a [Releases](https://github.com/ic8tem/YA-MS/releases) oldalról töltse le.

### macOS: nem nyitható meg, mert azonosítatlan fejlesztőtől származik
A YA-MS-t nem az Apple írta alá, ezért a **Gatekeeper** első alkalommal blokkolja. A `.dmg` fájlban **kattintson jobb gombbal az „Installa YA-MS.command” elemre → Megnyitás**, és erősítse meg. A szkript eltávolítja az „internetről letöltve” karanténjelzőt a `~/YA-MS/YA-MS.app` alkalmazásról, és megnyitja. Ha a macOS továbbra is elutasítja, nyissa meg a *Rendszerbeállítások → Adatvédelem és biztonság* panelt, és nyomja meg a *Megnyitás mindenképp* gombot.

### macOS: melyik .dmg kell?
`-mac-apple-silicon.dmg` M1/M2/M3/M4 processzorhoz, `-mac-intel.dmg` Intel-alapú Machez (Apple menü → *Erről a Macről* megmutatja, melyik).

### Linux: a YA-MS nem jelenik meg az alkalmazások menüjében
Futtassa a `./installa.sh` szkriptet a kibontott mappából (nem a `~/YA-MS` mappából). Egyes asztali környezetekben ki- és újra be kell jelentkezni, hogy az új bejegyzések megjelenjenek. A programot mindig elindíthatja a `~/YA-MS/YA-MS` paranccsal.

### Hiányzik az Európa-térkép
*Az Európa-térkép nem érhető el (első indításkor hálózat szükséges).* A Natural Earth térkép első indításkor töltődik le a `data/mappa` mappába. Csatlakozzon az internethez, és indítsa újra a YA-MS-t.

## Megjelenítés

### Linux: a japán szöveg helyén négyzetek jelennek meg
A rendszeréből hiányoznak a CJK (kínai, japán, koreai) betűtípusok. Telepítse a **Noto CJK** betűtípusokat, és indítsa újra a YA-MS-t. Ugyanez történik arab, héber, urdu, hindi és bengáli szövegnél is: Debian, Ubuntu és Raspberry Pi OS rendszeren telepítse a `fonts-noto-core` csomagot is.

| Disztribúció | Parancs |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### A szöveg túl kicsi, vagy a grafikonoknak nincs elég hely
Használja a **Betűméret** csúszkát (100–300 %), és csukja össze a sorokat a **Vezérlők** gombbal. Lásd: [Beállítások](Settings-and-Data-Folder-hu#betűméret-és-vezérlők).

### Éjszaka túl világos a képernyő
Válassza az **Éjszakai** vagy a **Fekete** sémát a **Téma** listában.

## Internet és radaradatok

### „Nincs internetkapcsolat” üzenet
A YA-MS **egyszer** jeleníti meg, ha egyik forrás sem érhető el; az állapotsor pirosra vált. A program az **utoljára mentett adatokkal** dolgozik tovább, és 5 percenként magától újrapróbálkozik; amikor a hálózat visszatér, megjelenik *A kapcsolat helyreállt.* üzenet. Semmi teendő nincs.

### Narancs figyelmeztetés a Radarfluxus fülön: „Nem olvasható a fluxus függőleges skálája …”
A collmi radar minden nap módosítja a függőleges skáláját, és a YA-MS ezt a grafikon feliratairól olvassa le. Ha egy felirat nem olvasható, a program a kalibrált 0–1200 meteor/óra skálát használja, és figyelmeztet, hogy **az értékeket ellenőrizni kell**. A következő óránkénti grafikont általában helyesen olvassa be. Ha sok órán át *A grafikon formátuma megváltozott* vagy *A fluxus tengelyei nem a várt helyen találhatók* üzenetet lát, a radar megváltoztatta a grafikon formátumát: kérjük, [jelezze](Contributing-and-Contacts-hu).

### „A magassággrafikon skálája megváltozott”
A magassági statisztikák (módusz, átlag, medián) érvényesek maradnak; csak a magasság-hisztogram abszolút számai nem.

### „Radarfluxus: nincs adat”
Nyomja meg a **Letöltés most** gombot a [Radarfluxus](Radar-Flux-hu) fülön, és ellenőrizze, hogy a `data/fonti_radar.csv` fájlban a Collmnál `attivo=1` szerepel.

### RMOB: miért van kikapcsolva az automatikus letöltés?
Az RMOB azt kéri, hogy **automatikus programok ne töltsék le a fájljait**. Az *automatikus letöltés 5 percenként* opciót csak akkor kapcsolja be, ha az RMOB engedélyt adott rá. Addig használja az **RMOB letöltése most** vagy az **RMOB-fájl betöltése lemezről...** gombot. Lásd: [Kísérleti előrejelzések](Experimental-Forecasts-hu#rmob-és-automatikus-programok).

### RMOB: „Ismeretlen fájlformátum” vagy kevés beolvasott óra
Használja a megfigyelő havi szövegfájlját (`NAME_MMYYYYrmob.TXT`) vagy egyetlen megfigyelőt tartalmazó közlönytáblázatot. A kitevő illesztéséhez legalább 3 közös óra kell a collmi adatokkal (tegnap és ma).

## Számítások

### „Érvénytelen állomáslokátor” / „Érvénytelen DX-állomás-lokátor”
A lokátornak 4, 6 vagy 8 karakteresnek kell lennie (pl. `JN70`, `JN70CN`, `JN70CN12`).

### „Nincs közös E-réteg-zóna”
Az útvonal hosszabb, mint a nyommagasságbeli hatótáv kétszerese (kb. 2 × 1062 km 0°-os nyalábnál és 89,5 km-es nyomoknál): egyetlen meteorszórásos ugrás nem hidalja át. A **Nyalábeleváció** növelése tovább csökkenti a hatótávot.

### Hot A / Hot B szürke
Ezek már **az antennanyalábon belül** vannak, amikor az antenna a DX felé néz: nem kell elfordítani. Lásd: [Égbolt-kupola](Sky-View-hu#figyelmeztetések).

### A hatékonyság eltér az MCG_MS vagy az MS-Soft értékeitől
A YA-MS a valós útvonalat és saját modelljét használja; OH5IY és az MCG_MS skálája nincs részletesen dokumentálva. Inkább az órákat és a trendeket hasonlítsa össze, mint az abszolút százalékokat, és nézze meg a [modellt](Efficiency-Calculation-hu#a-modell).

### A GRAVES-nyaláb áthaladása eltolódottnak tűnik
A nyalábsorrendet a PC órájából számítja: szinkronizálja egy NTP-szerverrel. A GRAVES vezérlőállomása időnként néhány lépéssel el is tolja a sorrendet; a részletezés előrejelzés, amelyet hallgatással kell megerősíteni.

## Egyéb kérdések

**Ingyenes a YA-MS?** Igen, ingyenes program rádióamatőröknek.

**Vezérli a rotátoromat vagy a rádiómat?** Nem. A YA-MS előrejelző és tervezőeszköz; a QSO-hoz használja digitális módú programját (pl. MSHV, WSJT-X).

**Működik 432 MHz felett?** A sávlista 432 MHz-nél véget ér (28, 50, 70, 144, 222, 432). A kísérleti előrejelzés bármely frekvenciát elfogad 28 és 1300 MHz között, de az általa használt SM6FHZ-szabályok 144 és 432 MHz-es tapasztalatokból származnak.

**Valami hiba történt.** Írjon a szerzőnek, megadva az operációs rendszert, a YA-MS változatszámát és azt, hogy mit csinált: lásd: [Közreműködés és kapcsolat](Contributing-and-Contacts-hu).
