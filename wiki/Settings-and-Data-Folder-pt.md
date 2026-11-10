[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · **Português** · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-tw)

# Definições e pasta de dados

## A barra de separadores

Na extremidade direita da barra de separadores, da direita para a esquerda:

| Comando | O que faz |
|---|---|
| **Idioma** (lista) | Idioma da interface; ver [Idioma](#idioma) |
| **Tema** (lista) | Esquema de cores; ver [Esquemas de cores](#esquemas-de-cores) |
| **Comandos ▴ / ▾** | Recolhe ou mostra as três filas de comandos por cima dos separadores; ver [Tipo de letra e Comandos](#tipo-de-letra-e-comandos) |

Ao mudar o idioma ou o tema as definições são guardadas e **a janela é reconstruída** na mesma posição e tamanho, no mesmo separador: não é preciso reiniciar.

## Idioma

36 idiomas de interface, os mesmos do YAEC e do E-LAYER ANALYZER (os termos comuns com o YAEC são traduzidos da mesma forma):

| Idioma | Código | Ficheiro |
|---|---|---|
| Italiano | `it` | nenhum: o italiano é o idioma base (as chaves) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português (Portugal) | `pt` | `data/lingue/pt.txt` |
| Português (Brasil) | `pt-br` | `data/lingue/pt-br.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |
| Svenska | `sv` | `data/lingue/sv.txt` |
| Norsk (bokmål) | `nb` | `data/lingue/nb.txt` |
| Dansk | `da` | `data/lingue/da.txt` |
| Íslenska | `is` | `data/lingue/is.txt` |
| Eesti | `et` | `data/lingue/et.txt` |
| Latviešu | `lv` | `data/lingue/lv.txt` |
| Lietuvių | `lt` | `data/lingue/lt.txt` |
| Polski | `pl` | `data/lingue/pl.txt` |
| Čeština | `cs` | `data/lingue/cs.txt` |
| Magyar | `hu` | `data/lingue/hu.txt` |
| Română | `ro` | `data/lingue/ro.txt` |
| Ελληνικά | `el` | `data/lingue/el.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| Українська | `uk` | `data/lingue/uk.txt` |
| Türkçe | `tr` | `data/lingue/tr.txt` |
| Afrikaans | `af` | `data/lingue/af.txt` |
| العربية | `ar` | `data/lingue/ar.txt` |
| עברית | `he` | `data/lingue/he.txt` |
| اردو | `ur` | `data/lingue/ur.txt` |
| हिन्दी | `hi` | `data/lingue/hi.txt` |
| বাংলা | `bn` | `data/lingue/bn.txt` |
| ไทย | `th` | `data/lingue/th.txt` |
| Bahasa Indonesia | `id` | `data/lingue/id.txt` |
| Tagalog | `tl` | `data/lingue/tl.txt` |
| 中文 (简体) | `zh` | `data/lingue/zh.txt` |
| 中文 (繁體) | `zh-tw` | `data/lingue/zh-tw.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

No primeiro arranque o YA-MS usa o **idioma do sistema** se for um destes; caso contrário, o italiano. Os números e as datas seguem o idioma escolhido (p. ex. ponto decimal em inglês, vírgula em italiano e alemão). Qualquer texto em falta num ficheiro de tradução é mostrado em italiano. No Linux, o chinês, o japonês, o coreano, o árabe, o hebraico, o urdu, o hindi e o bengali precisam de fontes adequadas (p. ex. as famílias Noto): ver [Problemas](Troubleshooting-FAQ-pt#linux-o-texto-japonês-aparece-como-quadradinhos).

O documento [Eficiência - explicação](Efficiency-Explanation-pt) segue o idioma da interface; o manual de cálculo está em `doc/` (italiano) e em `doc/manuali/` (os outros 35 idiomas).

## Esquemas de cores

A lista **Tema** oferece 12 esquemas, os mesmos do programa EME do autor, o YAEC, mais a paleta original do YA-MS:

| Esquema | Descrição |
|---|---|
| **Claro** | por omissão |
| **Noite** | tons de azul-escuro, para usar à noite |
| **Preto** | fundo preto, para o escuro e para ecrãs OLED |
| Pastel azul-claro · Pastel laranja · Pastel água-marinha · Pastel verde · Pastel rosa · Pastel lilás · Pastel índigo · Pastel castanho | oito esquemas pastel claros |
| **Rasto meteórico** | o estilo original do YA-MS (até à versão 1.2.0): violeta noturno com azul-claro, violeta, verde-claro, amarelo e laranja |

O esquema aplica-se a todos os separadores e é guardado em `config.ini` (chave `tema`).

## Tipo de letra e Comandos

- **Tipo de letra** (no fim da primeira fila de comandos): amplia **todo o texto** de **100 a 300 %** em passos de 10 %; linhas, círculos e mapas mantêm o tamanho. Com letra grande os separadores passam para uma segunda linha e os cartões crescem.
- **Comandos**: com letra grande ou um ecrã pequeno, recolha as três filas de comandos para deixar espaço a mapas e gráficos. O estado fica memorizado.

## Pasta de dados

Todos os dados e definições estão numa única pasta **`data`** **ao lado do programa**, sem AppData nem pastas do sistema:

| Sistema | Programa | Dados |
|---|---|---|
| Windows (instalador) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portátil) | onde o extraiu | `data` ao lado de `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (ao lado da app) |

No arranque, o programa cria a pasta se necessário e copia apenas os ficheiros iniciais **em falta**: os ficheiros que alterou nunca são substituídos. Os ficheiros de tradução em `data/lingue` são ficheiros do programa e são substituídos quando os da nova versão são mais recentes.

### Ficheiros que pode editar

| Ficheiro | Conteúdo |
|---|---|
| `sciami.csv` | Catálogo de chuvas (valores IMO e valores de trabalho); ver [Chuvas](Showers-pt#editar-o-catálogo) |
| `massimi_imo.csv` | Datas e horas dos máximos publicadas pela IMO (2026, 2027): **acrescente aqui os anos novos** |
| `ant_radiante.csv` | Posição da Fonte Anti-helion (tabela 6 da IMO) |
| `fonti_radar.csv` | Endereços dos radares; `attivo=1` descarrega, `0` ignora |
| `regole_sperimentali.csv` | Constantes e regras usadas, cada uma com a sua fonte (referência) |
| `lingue/<code>.txt` | Traduções da interface; ver [Contribuir](Contributing-and-Contacts-pt#traduções) |
| `config.ini` | Definições (ver abaixo) |

### Ficheiros criados pelo programa

| Ficheiro / pasta | Conteúdo |
|---|---|
| `config.ini` | Definições |
| `flusso_collm.csv` | Arquivo horário do fluxo de Collm |
| `quote_collm.csv` | Arquivo das altitudes dos rastos |
| `radar/` | Últimas imagens de radar e ficheiros RMOB |
| `mappa/` | Costas e fronteiras do Natural Earth (descarregadas no primeiro arranque) |
| `adif_quadrati.csv` | Quadrados do último ADIF carregado |
| `efficienza_spiegazione.txt`, `.docx` | O [documento de explicação](Efficiency-Explanation-pt) |

## config.ini

Texto simples, um `chave=valor` por linha (as linhas que começam por `#` ou `;` são comentários). O programa escreve-o ao fechar, por isso **edite-o com o YA-MS fechado**. As chaves que pode querer conhecer:

| Chave | Por omissão | Significado |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | O seu locator e altitude (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locator e altitude do correspondente (m) |
| `banda_MHz` | 144 | Banda (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Altitude dos rastos (km); 1 = usar a moda de Collm |
| `elevazione_lobo_gradi` | 0 | Elevação do lóbulo (°) |
| `boom_m` | 4.6 | Comprimento do boom da Yagi (m) |
| `hot_spot_km` | 150 | Distância de Hot A / Hot B ao ponto médio (30–400 km) |
| `lingua` | sistema / `it` | Código do idioma (um dos 36 códigos acima, p. ex. `it`, `en`, `de`) |
| `tema` | `chiaro` | Esquema de cores: `chiaro` (Claro), `scuro` (Noite), `nero` (Preto), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Rasto meteórico) |
| `carattere_pct` | 100 | Tamanho da letra (100–300 %) |
| `comandi_visibili` | 1 | 1 = filas de comandos visíveis, 0 = recolhidas |
| `mostra_mappa`, `vista_alto` | 1, 1 | Mapa da Europa, vista de cima na Abóbada celeste |
| `aggiornamento_automatico` | 1 | Verificação automática das fontes a cada 5 minutos |
| `esponente_lambda` | 3 | Expoente λ no separador Fluxo radar |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Dados de entrada do balanço da ligação |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Previsão experimental: frequência, k, K |
| `rmob_osservatore` | vazio | Nome do observador RMOB |
| `rmob_automatico` | 0 | Descarga automática do RMOB (ative-a só com autorização do RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Modelo de endereço do RMOB |
| `graves_sequenza` | 0 | Sequência do feixe do GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privacidade

O YA-MS não recolhe dados nem mostra publicidade. Liga-se à internet apenas para descarregar dados públicos: as imagens dos radares de Collm e Sodankylä, o mapa do Natural Earth (primeiro arranque) e, se o pedir, um ficheiro RMOB.
