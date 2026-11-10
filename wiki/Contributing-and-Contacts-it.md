[English](Contributing-and-Contacts) · **Italiano** · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-BR) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [ไทย](Contributing-and-Contacts-th) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-TW)

# Contribuire e contatti

YA-MS migliora grazie alle segnalazioni di chi lo usa in aria. Ogni correzione viene attribuita alla sua fonte.

## Contatti

| | |
|---|---|
| Autore | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Segnalare un problema

Apri una **issue su GitHub** o scrivi un'e-mail con:

- sistema operativo e versione di YA-MS (nel titolo della finestra);
- i due locator, la banda e l'ora UTC;
- che cosa ti aspettavi e che cosa hai visto (una schermata aiuta);
- per i problemi con i radar, il messaggio mostrato nella linguetta [Flusso radar](Radar-Flux-it).

## Che cosa è particolarmente utile

- **Rapporti dall'aria.** Ore e tratte in cui l'efficienza o la previsione erano giuste – o sbagliate. Il modello è sperimentale e va confrontato con QSO reali e con MCG_MS / MS-Soft.
- **Confronti con RMOB.** I valori del fattore di stazione K e dell'esponente k che hai trovato con il [confronto con RMOB](Experimental-Forecasts-it#confronto-con-rmob), con la tua banda e la tua stazione.
- **Dati con una fonte.** Spostamenti dei radianti migliori, profili di attività, nuove date dei massimi IMO (`data/massimi_imo.csv`), dati d'antenna: indica la fonte e verrà citata.
- **Cambiamenti dei grafici radar.** Se cambia il formato del grafico di Collm, una copia dell'immagine (`data/radar/`) aiuta a ritarare la lettura.

## Traduzioni

Le traduzioni dell'interfaccia sono semplici file di testo in **`data/lingue/<codice>.txt`** (UTF-8) e **chiunque può correggerle**:

```
<testo italiano><TAB><traduzione>
```

- Una voce per riga; le righe che iniziano con `#` sono commenti.
- In entrambe le colonne i due caratteri `\n` indicano un a capo.
- Mantieni i segnaposto `{0}`, `{1}`, … con il loro formato (per esempio `{0:F1}`, `{3:+0;-0}`), nell'ordine che serve alla tua lingua.
- Le voci mancanti o vuote vengono mostrate in italiano. L'elenco di tutte le chiavi è `data/lingue/chiavi.txt` (generato da `tools/estrai_chiavi.py`, non modificarlo).

Modifica il file nella cartella `data/lingue` della tua installazione e riavvia YA-MS (o cambia lingua) per vedere il risultato. Poiché questi file vengono **sostituiti dalle versioni più recenti a ogni aggiornamento**, per favore **invia anche le tue correzioni** – per e-mail o come pull request su GitHub (`data/lingue/`) – così entrano nella release successiva.

Questa wiki esiste in 36 lingue (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, ไทย, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文, 中文 (繁體)); anche le correzioni alle pagine della wiki sono benvenute.
