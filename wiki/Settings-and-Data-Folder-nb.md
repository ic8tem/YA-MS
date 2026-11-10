[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · **Norsk** · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Innstillinger og datamappe

## Fanelinjen

I høyre ende av fanelinjen, fra høyre mot venstre:

| Kontroll | Hva den gjør |
|---|---|
| **Språk** (liste) | Grensesnittspråk; se [Språk](#språk) |
| **Tema** (liste) | Fargeskjema; se [Fargeskjemaer](#fargeskjemaer) |
| **Kontroller ▴ / ▾** | Felder sammen eller ut de tre radene med kontroller over fanene; se [Skrift og Kontroller](#skrift-og-kontroller) |

Når du bytter språk eller tema, lagres innstillingene, og **vinduet bygges opp på nytt** i samme posisjon og størrelse, på samme fane: ingen omstart trengs.

## Språk

Seks språk i grensesnittet:

| Språk | Kode | Fil |
|---|---|---|
| Italiano | `it` | ingen: italiensk er grunnspråket (nøklene) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Ved første oppstart bruker YA-MS **systemspråket** hvis det er ett av disse, ellers italiensk. Tall og datoer følger valgt språk (f.eks. desimalpunktum på engelsk, komma på italiensk og tysk). Tekst som mangler i en oversettelsesfil, vises på italiensk. På Linux krever japansk egnede skrifter: se [Feilsøking](Troubleshooting-FAQ-nb#linux-japansk-tekst-vises-som-firkanter).

Dokumentet [Effektivitet - forklaring](Efficiency-Explanation-nb) og beregningshåndboken er på italiensk.

## Fargeskjemaer

Listen **Tema** har 12 skjemaer, de samme som i forfatterens EME-program YAEC pluss den opprinnelige YA-MS-paletten:

| Skjema | Beskrivelse |
|---|---|
| **Lys** | standard |
| **Natt** | mørkeblå toner, for bruk om natten |
| **Svart** | svart bakgrunn, for mørke omgivelser og OLED-skjermer |
| Pastell lyseblå · Pastell oransje · Pastell akvamarin · Pastell grønn · Pastell rosa · Pastell lilla · Pastell indigo · Pastell brun | åtte lyse pastellskjemaer |
| **Meteorspor** | den opprinnelige YA-MS-stilen (til og med versjon 1.2.0): nattfiolett med lyseblått, fiolett, lysegrønt, gult og oransje |

Skjemaet gjelder alle faner og lagres i `config.ini` (nøkkelen `tema`).

## Skrift og Kontroller

- **Skrift** (på slutten av første rad med kontroller): forstørrer **all tekst** fra **100 til 300 %** i steg på 10 %; linjer, sirkler og kart beholder størrelsen. Med store skrifter brytes fanene over på en ekstra linje, og panelene vokser.
- **Kontroller**: med store skrifter eller en liten skjerm kan du felle sammen de tre radene med kontroller for å gi plass til kart og diagrammer. Tilstanden huskes.

## Datamappe

Alle data og innstillinger ligger i én enkelt **`data`**-mappe **ved siden av programmet** – ingen AppData, ingen systemmapper:

| System | Program | Data |
|---|---|---|
| Windows (installasjonsprogram) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabel) | der du pakket det ut | `data` ved siden av `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (ved siden av appen) |

Ved oppstart oppretter programmet mappen ved behov og kopierer bare de **manglende** startfilene: filer du har endret, overskrives aldri. Oversettelsesfilene i `data/lingue` er programfiler og erstattes når filene i den nye versjonen er nyere.

### Filer du kan redigere

| Fil | Innhold |
|---|---|
| `sciami.csv` | Svermkatalog (IMO-verdier og arbeidsverdier); se [Svermer](Showers-nb#redigere-katalogen) |
| `massimi_imo.csv` | Datoer og tidspunkter for maksima publisert av IMO (2026, 2027): **legg til nye år** her |
| `ant_radiante.csv` | Posisjonen til Antihelion-kilden (IMOs tabell 6) |
| `fonti_radar.csv` | Radaradresser; `attivo=1` laster ned, `0` ignorerer |
| `regole_sperimentali.csv` | Konstanter og regler som brukes, hver med sin kilde (referanse) |
| `lingue/<code>.txt` | Oversettelser av grensesnittet; se [Bidra](Contributing-and-Contacts-nb#oversettelser) |
| `config.ini` | Innstillinger (se nedenfor) |

### Filer som programmet oppretter

| Fil / mappe | Innhold |
|---|---|
| `config.ini` | Innstillinger |
| `flusso_collm.csv` | Timearkiv med Collm-fluksen |
| `quote_collm.csv` | Arkiv med sporhøydene |
| `radar/` | Siste radarbilder og RMOB-filer |
| `mappa/` | Kystlinjer og grenser fra Natural Earth (lastes ned ved første oppstart) |
| `adif_quadrati.csv` | Ruter fra sist innlastede ADIF |
| `efficienza_spiegazione.txt`, `.docx` | [Forklaringsdokumentet](Efficiency-Explanation-nb) |

## config.ini

Ren tekst, én `key=value` per linje (linjer som begynner med `#` eller `;`, er kommentarer). Programmet skriver filen når det lukkes, så **rediger den mens YA-MS er lukket**. Nøklene du kan ha nytte av å kjenne:

| Nøkkel | Standard | Betydning |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Din lokator og høyde (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Motstasjonens lokator og høyde (m) |
| `banda_MHz` | 144 | Bånd (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Sporhøyde (km); 1 = bruk Collm-typetallet |
| `elevazione_lobo_gradi` | 0 | Lobeelevasjon (°) |
| `boom_m` | 4.6 | Bomlengde for Yagien (m) |
| `hot_spot_km` | 150 | Avstand fra Hot A / Hot B til midtpunktet (30–400 km) |
| `lingua` | system / `it` | Språkkode (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Fargeskjema: `chiaro` (Lys), `scuro` (Natt), `nero` (Svart), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteorspor) |
| `carattere_pct` | 100 | Skriftstørrelse (100–300 %) |
| `comandi_visibili` | 1 | 1 = radene med kontroller vises, 0 = sammenfelt |
| `mostra_mappa`, `vista_alto` | 1, 1 | Europakart, sett ovenfra i himmelhvelvingen |
| `aggiornamento_automatico` | 1 | Automatisk sjekk av kildene hvert 5. minutt |
| `esponente_lambda` | 3 | λ-eksponent i fanen Radarfluks |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Inndata til linkbudsjettet |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Eksperimentell prognose: frekvens, k, K |
| `rmob_osservatore` | tom | Navnet på RMOB-observatøren |
| `rmob_automatico` | 0 | Automatisk nedlasting fra RMOB (aktiver bare med tillatelse fra RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Mal for RMOB-adressen |
| `graves_sequenza` | 0 | GRAVES-strålesekvens: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Personvern

YA-MS samler ikke inn data og viser ingen reklame. Programmet kobler seg til internett bare for å laste ned offentlige data: radarbildene fra Collm og Sodankylä, Natural Earth-kartet (første oppstart) og, hvis du ber om det, en RMOB-fil.
