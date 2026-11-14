[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · **Português** · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Recolha de dados

*Separador: Em direto e dados em tempo real › Recolha de dados.*

[![Recolha de dados](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Quatro fontes

O separador recolhe **spots de meteor scatter** de três fluxos telnet e do fluxo MQTT do PSKReporter, cada um no seu próprio subseparador:

| Subseparador | Por omissão | Notas |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Um cluster à escolha. No ON0DXK as bandas VHF estão filtradas: ative-as com `set/filter dxbm/pass 6` (depois 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Os skimmers raramente descodificam modos MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X que transporta os spots do **PSKReporter**: é aqui que chegam as descodificações MSK144 do WSJT-X e do MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spots do PSKReporter em direto por **MQTT** (serviço de M0LTE): sem login, cada spot já traz os locators da estação que transmite e da que recebe. Tópicos predefinidos: MSK144 em 6 m, 4 m, 2 m, 1,25 m, 70 cm e FSK441 em 2 m (`pskr/filter/v2/band/mode/#`); *Tópicos predefinidos* repõe-nos. |
| **Spots MS recolhidos** | – | Tabela dos spots aceites, os mais recentes primeiro. |

Cada fluxo tem host, porta, comandos enviados após o login, *Voltar a ligar*, *Ligar no arranque*, uma consola e uma linha para enviar comandos. Escreva no topo o seu **indicativo para o login**. A fonte MQTT tem host, porta, tópicos (um por linha ou separados por `;`), *Voltar a ligar* e *Ligar no arranque* (desligado por omissão) e uma consola com os spots recebidos; os seus spots passam pelo mesmo filtro. Uma faixa mostra o estado das quatro fontes (ponto verde = ligada). As sessões ficam abertas quando muda de idioma ou de esquema de cores.

## O filtro (40 % da janela)

- **Filtro local opcional:** as linhas do cluster abaixo de **27990,0 kHz** são descartadas de imediato (não são mostradas nem guardadas).
- Os spots CW são descartados logo (CW ou WPM no comentário, ou 28000-28070 kHz): não aparecem na consola e não se guardam, exceto os marcados <MS>. A caixa pode ser desativada.

Base CALL3 com as regras do LIVETROPOVHF. «Atualizar agora» descarrega o CALL3.TXT do MMMonVHF (pelo menos 100 000 linhas válidas, o anterior fica em data/call3.bak); com «Atualizar sozinho a cada 7 dias» fá-lo ao arrancar. Acima do ficheiro valem, por ordem: entradas manuais (data/CALL3-MANUALE.TXT), correções do cluster (o locator de 6 caracteres que quem faz o spot declara de si), ficheiros adicionados (data/CALL3-AGGIUNTE), depois o CALL3.TXT e os locators de 6 caracteres aprendidos ao vivo (data/LOC6.TXT). Um locator recebido com 4 caracteres, ou terminado em LL ou MM, é substituído pelo de 6 caracteres da base; os portáteis (com barra) só com a entrada exata.

Última fonte, como no LIVETROPOVHF: para os indicativos sem locator de 6 caracteres em nenhuma outra fonte, o programa consulta automaticamente a cada 6 horas a API pública do G7VRD (api.g7vrd.co.uk), em grupos de 40 indicativos; cada indicativo no máximo uma vez por dia. Só se aceita um locator de 6 caracteres, não o centro do quadrado (LL ou MM), no mesmo quadrado do recebido. Os resultados ficam em data/CALL3-G7VRD.TXT e, como todas as correções, são também escritos em data/call3.txt.
- Os spots entre estações a menos de 500 km são descartados de imediato, porque a essa distância a ligação é direta ou troposférica e não meteor scatter: não aparecem na consola e não são guardados. Se faltar um locator, o spot mantém-se. A distância altera-se por baixo da caixa.
- **1.º critério – frequências MS típicas:** 50190–50300, 70100–70400, 144290–144399 kHz. Um spot nestas janelas é aceite mesmo sem o nome do modo, a não ser que o comentário declare outra propagação: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Janelas e etiquetas podem ser editadas.
- **2.º critério – modos MS:** fora das janelas, ou com uma dessas etiquetas, um spot só é mantido se contiver **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modos digitais usados apenas em MS) ou **\<MS\>**, em maiúsculas, minúsculas ou mistas. As palavras podem ser desativadas, adicionadas e removidas; cada uma tem o seu contador.
- **Bandas** 28, 50, 70, 144, 222, 432 MHz; **teste do filtro** numa linha colada; **contadores**.

## Locators e armazenamento

Os locators em falta, ou só com 4 caracteres, são obtidos da base **CALL3** (`data/call3.txt`, ficheiro do JTDX, mais de um milhão de indicativos), que prevalece sempre sobre um locator de 4 caracteres. Os spots aceites são guardados em `data/spot_ms`, um ficheiro CSV por dia, e alimentam o mapa de [Tráfego em direto](Live-Traffic-pt).
