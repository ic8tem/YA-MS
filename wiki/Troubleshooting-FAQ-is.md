[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · **Íslenska** · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Úrræðaleit og algengar spurningar

## Uppsetning og ræsing

### Windows SmartScreen segir „Windows verndaði tölvuna þína“
Forritið er ekki undirritað með viðskiptavottorði. Smelltu á *Frekari upplýsingar* → *Keyra samt*. Sæktu það aðeins af síðunni [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: ekki hægt að opna því hann er frá óþekktum hönnuði
YA-MS er ekki undirritað af Apple, svo **Gatekeeper** stöðvar það í fyrsta skiptið. Í `.dmg`-skránni skaltu **hægrismella á "Installa YA-MS.command" → Opna** og staðfesta. Skriftan fjarlægir sóttkvíarmerkið „sótt af netinu“ af `~/YA-MS/YA-MS.app` og opnar það. Ef macOS neitar enn skaltu opna *Kerfisstillingar → Persónuvernd og öryggi* og ýta á *Opna samt*.

### macOS: hvaða .dmg?
`-mac-apple-silicon.dmg` fyrir M1/M2/M3/M4-örgjörva, `-mac-intel.dmg` fyrir Mac með Intel (Apple-valmyndin → *Um þennan Mac* segir þér hvort).

### Linux: YA-MS er ekki í forritavalmyndinni
Keyrðu `./installa.sh` í afþjöppuðu möppunni (ekki í `~/YA-MS`). Sum skjáborðsumhverfi þurfa útskráningu/innskráningu til að sýna nýjar færslur. Þú getur alltaf ræst það með `~/YA-MS/YA-MS`.

### Kortið af Evrópu vantar
*Kort af Evrópu ekki tiltækt (nettenging þarf við fyrstu ræsingu).* Kortið frá Natural Earth er sótt í `data/mappa` við fyrstu ræsingu. Tengstu netinu og endurræstu YA-MS.

## Skjámynd

### Linux: japanskur texti birtist sem kassar
Kerfið þitt vantar CJK-letur. Settu upp **Noto CJK**-letrið og endurræstu YA-MS:

| Dreifing | Skipun |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Textinn er of smár, eða gröfin hafa ekki pláss
Notaðu sleðann **Letur** (100–300 %) og felldu raðirnar saman með **Stýringar**. Sjá [Stillingar](Settings-and-Data-Folder-is#letur-og-stýringar).

### Skjárinn er of bjartur á nóttunni
Veldu **Nótt** eða **Svart** í listanum **Þema**.

## Netið og ratsjárgögn

### Skilaboðin „Engin nettenging“
YA-MS birtir þau **einu sinni** þegar engin lind næst; stöðustikan verður rauð. Forritið heldur áfram að vinna með **síðustu vistuðu gögnum** og reynir sjálft aftur á 5 mínútna fresti; *Tenging komin aftur.* birtist þegar netið er komið aftur. Þú þarft ekkert að gera.

### Appelsínugul viðvörun í Ratsjárflæði: „Get ekki lesið lóðréttan kvarða flæðisins …“
Collm-ratsjáin breytir lóðrétta kvarðanum sínum daglega og YA-MS les hann af merkimiðum grafsins. Ef ekki tekst að lesa merkimiða notar forritið kvarðaða skalann 0–1200 loftsteinar/klst. og varar við að **gildin þurfi að athuga**. Venjulega er næsta klukkustundargraf lesið rétt. Ef þú sérð *Snið grafsins hefur breyst* eða *Ásar flæðisins fundust ekki á væntanlegum stað* í margar klukkustundir hefur ratsjáin breytt sniði grafsins: vinsamlegast [tilkynntu það](Contributing-and-Contacts-is).

### „Kvarði hæðargrafsins hefur breyst“
Tölfræði hæða (tíðasta gildi, meðaltal, miðgildi) er enn gild; aðeins heildartalningar hæðarstuðlaritsins eru það ekki.

### „Ratsjárflæði: engin gögn“
Ýttu á **Sækja núna** í [Ratsjárflæði](Radar-Flux-is) og athugaðu að `data/fonti_radar.csv` hafi `attivo=1` fyrir Collm.

### RMOB: hvers vegna er sjálfvirk sókn óvirk?
RMOB biður um að **sjálfvirk forrit sæki ekki skrár þess**. Virkjaðu *sjálfvirk sókn á 5 mínútna fresti* aðeins eftir að RMOB hefur veitt þér leyfi. Notaðu á meðan **Sækja RMOB núna** eða **Hlaða RMOB-skrá af diski...**. Sjá [Tilraunaspár](Experimental-Forecasts-is#rmob-og-sjálfvirk-forrit).

### RMOB: „Skráarsnið þekktist ekki.“ eða fáar klukkustundir lesnar
Notaðu mánaðarlega textaskrá athugandans (`NAME_MMYYYYrmob.TXT`) eða töflu úr fréttabréfi með einum athuganda. Aðlögun veldisvísisins krefst a.m.k. 3 klukkustunda sameiginlegra með gögnum Collm (í gær og í dag).

## Útreikningar

### „Ógildur locator stöðvar“ / „Ógildur locator mótstöðvar“
Locatorar verða að hafa 4, 6 eða 8 stafi (t.d. `JN70`, `JN70CN`, `JN70CN12`).

### „Ekkert sameiginlegt svæði í E-laginu“
Leiðin er lengri en tvöföld drægnin í hæð slóðanna (um 2 × 1062 km með geislann í 0° og slóðir í 89,5 km): eitt meteor scatter-stökk getur ekki brúað hana. Að hækka **Hæðarhorn geisla** styttir drægnina enn frekar.

### Hot A / Hot B eru gráir
Þeir eru þegar **innan loftnetsgeislans** þegar þú beinir að DX: óþarfi að snúa. Sjá [Himinhvelfing](Sky-View-is#viðvaranir).

### Nýtnin er frábrugðin MCG_MS eða MS-Soft
YA-MS notar raunverulegu leiðina og eigið líkan; kvarði OH5IY og MCG_MS er ekki skjalfestur í smáatriðum. Berðu frekar saman klukkustundir og tilhneigingar en algildar prósentur, og sjá [líkanið](Efficiency-Calculation-is#líkanið).

### Yfirferð geisla GRAVES virðist hliðruð
Röð geislans er reiknuð út frá klukku tölvunnar: samstilltu hana við NTP-þjón. Stjórnstöð GRAVES hliðrar einnig stundum röðinni um nokkur skref; nánari sýnin er spá sem staðfesta þarf með hlustun.

## Aðrar spurningar

**Er YA-MS ókeypis?** Já, það er ókeypis forrit fyrir radíóamatöra.

**Stýrir það loftnetssnúningnum eða stöðinni minni?** Nei. YA-MS er verkfæri til spágerðar og skipulagningar; notaðu forritið þitt fyrir stafræna hætti (t.d. MSHV, WSJT-X) fyrir QSO-ið.

**Virkar það ofan 432 MHz?** Listinn yfir tíðnisvið endar við 432 MHz (28, 50, 70, 144, 222, 432). Tilraunaspáin tekur við hvaða tíðni sem er frá 28 til 1300 MHz, en reglur SM6FHZ sem hún notar byggja á reynslu á 144 og 432 MHz.

**Eitthvað fór úrskeiðis.** Skrifaðu höfundinum og tilgreindu stýrikerfi, útgáfu YA-MS og hvað þú gerðir: sjá [Framlög og tengiliðir](Contributing-and-Contacts-is).
