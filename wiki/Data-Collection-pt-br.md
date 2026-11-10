[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · **Português (Brasil)** · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Coleta de dados

*Aba: Ao vivo e dados em tempo real › Coleta de dados.*

[![Coleta de dados](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Três fluxos de cluster

A aba coleta **spots de meteor scatter** de três fluxos telnet, cada um na sua própria subaba:

| Subaba | Padrão | Notas |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Um cluster à sua escolha. No ON0DXK as bandas VHF estão filtradas: ative-as com `set/filter dxbm/pass 6` (depois 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Os skimmers raramente decodificam modos MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X que transporta os spots do **PSKReporter**: é aqui que chegam as decodificações MSK144 do WSJT-X e do MSHV. |
| **Spots MS coletados** | – | Tabela dos spots aceitos, os mais recentes primeiro. |

Cada fluxo tem host, porta, comandos enviados após o login, *Reconectar*, *Conectar na inicialização*, um console e uma linha para enviar comandos. Digite no topo o seu **indicativo para o login**. Uma faixa mostra o estado das três sessões (ponto verde = conectada). As sessões continuam abertas quando você muda o idioma ou o esquema de cores.

## O filtro (40 % da janela)

- **Filtro local opcional:** as linhas do cluster abaixo de **27990,0 kHz** são descartadas imediatamente (não são mostradas nem armazenadas).
- **1.º critério – frequências MS típicas:** 50190–50300, 70100–70400, 144290–144399 kHz. Um spot nessas janelas é aceito mesmo sem o nome do modo, a menos que o comentário declare outra propagação: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Janelas e tags podem ser editadas.
- **2.º critério – modos MS:** fora das janelas, ou com uma dessas tags, um spot só é mantido se contiver **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modos digitais usados apenas em MS) ou **\<MS\>**, em maiúsculas, minúsculas ou misturadas. As palavras podem ser desativadas, adicionadas e removidas; cada uma tem o seu contador.
- **Bandas** 28, 50, 70, 144, 222, 432 MHz; **teste do filtro** em uma linha colada; **contadores**.

## Locators e armazenamento

Os locators ausentes, ou com apenas 4 caracteres, são obtidos da base **CALL3** (`data/call3.txt`, arquivo do JTDX, mais de um milhão de indicativos), que sempre prevalece sobre um locator de 4 caracteres. Os spots aceitos são salvos em `data/spot_ms`, um arquivo CSV por dia, e alimentam o mapa de [Tráfego ao vivo](Live-Traffic-pt-br).
