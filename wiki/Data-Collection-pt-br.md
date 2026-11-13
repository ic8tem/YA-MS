[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · **Português (Brasil)** · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Coleta de dados

*Aba: Ao vivo e dados em tempo real › Coleta de dados.*

[![Coleta de dados](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Quatro fontes

A aba coleta **spots de meteor scatter** de três fluxos telnet e do fluxo MQTT do PSKReporter, cada um em sua própria subaba:

| Subaba | Padrão | Notas |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Um cluster à escolha. No ON0DXK as bandas VHF estão filtradas: ative-as com `set/filter dxbm/pass 6` (depois 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Os skimmers raramente decodificam modos MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X que transporta os spots do **PSKReporter**: é aqui que chegam as decodificações MSK144 do WSJT-X e do MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spots do PSKReporter ao vivo por **MQTT** (serviço de M0LTE): sem login, cada spot já traz os locators da estação que transmite e da que recebe. Tópicos padrão: MSK144 em 6 m, 4 m, 2 m, 1,25 m, 70 cm e FSK441 em 2 m (`pskr/filter/v2/band/mode/#`); *Tópicos padrão* os restaura. |
| **Spots MS coletados** | – | Tabela dos spots aceitos, os mais recentes primeiro. |

Cada fluxo tem host, porta, comandos enviados após o login, *Reconectar*, *Conectar na inicialização*, um console e uma linha para enviar comandos. Escreva no topo o seu **indicativo para o login**. A fonte MQTT tem host, porta, tópicos (um por linha ou separados por `;`), *Reconectar* e *Conectar na inicialização* (desativado por padrão) e um console com os spots recebidos; os seus spots passam pelo mesmo filtro. Uma faixa mostra o estado das quatro fontes (ponto verde = conectada). As sessões ficam abertas quando você muda de idioma ou de esquema de cores.

## O filtro (40 % da janela)

- **Filtro local opcional:** as linhas do cluster abaixo de **27990,0 kHz** são descartadas imediatamente (não são mostradas nem salvas).
- Os spots CW são descartados na hora (CW ou WPM no comentário, ou 28000-28070 kHz): não aparecem no console e não são gravados, exceto os marcados <MS>. A caixa pode ser desligada.
- **1.º critério – frequências MS típicas:** 50190–50300, 70100–70400, 144290–144399 kHz. Um spot nestas janelas é aceito mesmo sem o nome do modo, a não ser que o comentário declare outra propagação: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Janelas e etiquetas podem ser editadas.
- **2.º critério – modos MS:** fora das janelas, ou com uma dessas etiquetas, um spot só é mantido se contiver **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modos digitais usados apenas em MS) ou **\<MS\>**, em maiúsculas, minúsculas ou mistas. As palavras podem ser desativadas, adicionadas e removidas; cada uma tem o seu contador.
- **Bandas** 28, 50, 70, 144, 222, 432 MHz; **teste do filtro** em uma linha colada; **contadores**.

## Locators e armazenamento

Os locators ausentes, ou só com 4 caracteres, são obtidos da base **CALL3** (`data/call3.txt`, arquivo do JTDX, mais de um milhão de indicativos), que prevalece sempre sobre um locator de 4 caracteres. Os spots aceitos são salvos em `data/spot_ms`, um arquivo CSV por dia, e alimentam o mapa de [Tráfego ao vivo](Live-Traffic-pt-br).
