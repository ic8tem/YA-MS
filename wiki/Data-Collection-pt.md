[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · **Português** · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Recolha de dados

*Separador: Em direto e dados em tempo real › Recolha de dados.*

[![Recolha de dados](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Três fluxos de cluster

O separador recolhe **spots de meteor scatter** de três fluxos telnet, cada um no seu próprio subseparador:

| Subseparador | Por omissão | Notas |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Um cluster à escolha. No ON0DXK as bandas VHF estão filtradas: ative-as com `set/filter dxbm/pass 6` (depois 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Os skimmers raramente descodificam modos MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X que transporta os spots do **PSKReporter**: é aqui que chegam as descodificações MSK144 do WSJT-X e do MSHV. |
| **Spots MS recolhidos** | – | Tabela dos spots aceites, os mais recentes primeiro. |

Cada fluxo tem host, porta, comandos enviados após o login, *Voltar a ligar*, *Ligar no arranque*, uma consola e uma linha para enviar comandos. Escreva no topo o seu **indicativo para o login**. Uma faixa mostra o estado das três sessões (ponto verde = ligada). As sessões ficam abertas quando muda de idioma ou de esquema de cores.

## O filtro (40 % da janela)

- **Filtro local opcional:** as linhas do cluster abaixo de **27990,0 kHz** são descartadas de imediato (não são mostradas nem guardadas).
- **1.º critério – frequências MS típicas:** 50190–50300, 70100–70400, 144290–144399 kHz. Um spot nestas janelas é aceite mesmo sem o nome do modo, a não ser que o comentário declare outra propagação: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Janelas e etiquetas podem ser editadas.
- **2.º critério – modos MS:** fora das janelas, ou com uma dessas etiquetas, um spot só é mantido se contiver **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modos digitais usados apenas em MS) ou **\<MS\>**, em maiúsculas, minúsculas ou mistas. As palavras podem ser desativadas, adicionadas e removidas; cada uma tem o seu contador.
- **Bandas** 28, 50, 70, 144, 222, 432 MHz; **teste do filtro** numa linha colada; **contadores**.

## Locators e armazenamento

Os locators em falta, ou só com 4 caracteres, são obtidos da base **CALL3** (`data/call3.txt`, ficheiro do JTDX, mais de um milhão de indicativos), que prevalece sempre sobre um locator de 4 caracteres. Os spots aceites são guardados em `data/spot_ms`, um ficheiro CSV por dia, e alimentam o mapa de [Tráfego em direto](Live-Traffic-pt).
