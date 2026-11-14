[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · **Português (Brasil)** · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Tráfego ao vivo

*Aba: Ao vivo e dados em tempo real › Tráfego ao vivo.*

[![Tráfego ao vivo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## O que mostra

Um **mapa azimutal equidistante** centrado na sua estação (distância ao centro = distância real, ângulo = azimute) com **todo o tráfego de meteor scatter** reunido pela [Coleta de dados](Data-Collection-pt-br). Para cada contato o programa desenha:

- o **percurso** entre as duas estações, na cor da sua banda: 28 MHz marrom, 50 MHz verde, 70 MHz ciano, 144 MHz laranja, 222 MHz rosa, 432 MHz violeta;
- as duas **estações** nas extremidades do percurso;
- a **zona da chuva**: onde se concentram os rastros meteóricos mais prováveis para esse percurso e essa hora.

Os spots com uma estação **fora do mapa** são descartados. Um spot **recém-chegado** (com não mais de 3 minutos) **pisca durante um minuto**, para que a atividade nova seja vista imediatamente.

Mostrar quem está ouvindo: triângulos na cor da banda marcam as estações que, segundo o PSKReporter, recebem em MSK144, FSK441, PSK2K ou JTMS em 28, 50, 70, 144 e 432 MHz na janela de tempo escolhida. Um clique em um triângulo mostra indicativo, locator, modos e último spot. O fluxo MQTT da aba Coleta de dados precisa estar conectado.

Também os monitores ativos do mapa do PSKReporter: triângulos vazios para as estações que aparecem no mapa de pskreporter.info em MSK144, FSK441, PSK2K ou JTMS mas ainda não receberam nenhum spot (o MQTT só envia estações que recebem algo). O YA-MS consulta o serviço de consulta do PSKReporter uma vez a cada 5 minutos para todos os modos, como pedem as regras do serviço; um monitor fica no mapa por pelo menos 11 minutos. Um clique no triângulo mostra indicativo, locator, programa de decodificação e o horário em que o monitor estava ativo. Ligado por padrão.

FT8 acima de 1100 km sem percursos paralelos: um spot FT8 (do PSKReporter MQTT, dos clusters ou do WSJT-X via UDP) entre estações a mais de 1100 km que não tem percursos paralelos nos 3 minutos antes e depois (mesma banda, ponto médio a menos de 300 km, direção a menos de 15°, outro par de estações) é desenhado em verde claro e sua linha na tabela embaixo à direita pisca sempre. A E esporádica e a tropo dão muitos percursos próximos e paralelos; um spot isolado pode ser um rastro meteórico. Por isso o YA-MS recebe do MQTT também os FT8 de 6 m, 4 m, 2 m, 1,25 m e 70 cm (nunca 28 MHz, em nenhum caso). Esses spots não entram no arquivo MS. Ligado por padrão. Verificações extras com o PSKReporter MQTT: o spot não é isolado se a estação receptora ouvir no MQTT outras estações a mais de 1100 km na mesma banda em 3 minutos (banda aberta); os spots dos clusters e do RBN só valem se o mesmo par chegar também pelo MQTT; os skimmers do RBN (indicativos com «-#») nunca valem.

Os spots do WSJT-X via UDP que dizem respeito à sua estação (a decodificação contém seu indicativo: quem chama você ou responde) são desenhados com tracejado que pisca sempre, em qualquer modo e a qualquer distância.

Troca entre usuários do YA-MS: quando outro usuário do YA-MS decodifica por UDP uma mensagem dirigida à sua estação (em MSK144, FSK441, PSK2K ou JTMS, ou em FT8 acima de 1100 km), o YA-MS dele envia a você cifrada por três brokers MQTT públicos (HiveMQ, Mosquitto, EMQX); você a vê como tracejado violeta que pisca sempre e numa linha do console UDP. Só você pode lê-la (chaves ECDH P-256, AES-256 e HMAC-SHA256). Os spots FT8 só aparecem se não tiverem percursos paralelos em 3 minutos. Ligado por padrão; yams_scambio=0 em data/config.ini desliga.

O mapa mostra os indicativos das duas estações de cada spot, uma só vez por estação. A projeção pode ser azimutal (centrada na sua estação) ou Mercator. A dica da coluna zona da chuva explica seu significado.

São mostrados os spots de todas as bandas, também das não escolhidas na Coleta de dados (esses não são salvos). Os spots CW e os entre estações próximas demais não são mostrados, se forem descartados na Coleta de dados.

## Como é calculada a zona da chuva

Para cada spot o programa constrói o percurso entre os dois locators (a mesma geometria do seu próprio percurso, veja [Geometria e atenuação](Geometry-and-Path-Loss-pt-br)) e, à hora do spot, soma ponto a ponto da camada E as **contribuições de reflexão especular de cada chuva ativa**, ponderadas com o seu ZHR: o mesmo cálculo das **zonas PREV** da [abóbada celeste](Sky-View-pt-br). Para cada lado do percurso que reúna pelo menos 15 % do total, a zona da chuva é uma **elipse**: centro na média ponderada dos pontos, semieixos iguais a 1,5 vezes as raízes quadradas dos autovalores da sua dispersão, eixo maior ao longo do autovetor principal. Quando nenhuma chuva contribui (só meteoros esporádicos), as zona da chuva são os dois **hot spots** clássicos, desenhados em tracejado. As equações completas estão no capítulo 10 do manual de cálculo.

## Comandos

| Comando | Significado |
|---|---|
| **Raio do mapa** | 600–3500 km a partir da sua estação. |
| **Spots a mostrar** | Últimos 15 ou 30 minutos, última hora, últimas 3 horas, últimas 24 horas. |
| **Tabela** | Contatos no mapa, os mais recentes primeiro, na cor da banda; *% chuva* indica a porcentagem de reflexões no lado principal, ou *esporádicos*. |
| **Clique** | Em um percurso ou em uma linha da tabela: o contato é destacado e a caixa mostra o locator do centro da zona da chuva, a sua porcentagem, tamanho e eixo. |
