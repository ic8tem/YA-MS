[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · **Português (Brasil)** · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [ไทย](Getting-Started-th) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# Primeiros passos

Na primeira inicialização o YA-MS mostra um percurso de exemplo (JN70CN → JO62QM nos 144 MHz). Bastam cinco minutos para configurá-lo para a sua estação.

## 1. As três linhas de comandos

Acima das abas há três linhas de comandos, válidas para todas as abas. O botão **Comandos** no canto superior direito as oculta e as mostra (útil com fonte grande); a escolha fica memorizada.

**Linha 1 – estações e banda**

| Comando | O que faz |
|---|---|
| **O meu locator** / **altitude m** | O seu locator Maidenhead (4, 6 ou 8 caracteres; é usado o centro do quadrado) e a altitude da estação acima do nível do mar. |
| **Correspondente** / **altitude m** | Locator e altitude da estação que você quer trabalhar. |
| **Banda MHz** | 28, 50, 70, 144, 222 ou 432 MHz: usada para o ganho e o lóbulo da antena, a estimativa do fluxo e o balanço do enlace. |
| **Calcular** | Recalcula o percurso (amostragem da camada E: alguns segundos). |
| **Antena az** | Azimute da sua antena: sempre **em direção ao DX** (azimute do percurso). |
| **Fonte** | Tamanho de todo o texto, 100–300 %. Veja [Configurações](Settings-and-Data-Folder-pt-br#fonte-e-comandos). |

**Linha 2 – camada E e antena**

| Comando | O que faz |
|---|---|
| **Altitude dos rastros km** + **do radar** | Altitude dos rastros meteóricos (padrão 90 km). Com *do radar* marcado, é usada a altitude mais frequente (moda) medida pelo radar de Collm; veja [Fluxo radar](Radar-Flux-pt-br). |
| **Elevação do lóbulo °** | Elevação do máximo do lóbulo vertical da sua antena: uma direcional fixa em 0° tem mesmo assim o lóbulo alguns graus acima do horizonte por causa da reflexão no solo (normalmente 3-8°). Com a caixa **diagrama da antena** ligada (padrão) os pontos da camada E são ponderados pelo diagrama vertical das duas antenas; desligada, só são usados os pontos que as duas estações veem acima dessa elevação. |
| **Antena Yagi: boom m** | Comprimento do boom da sua Yagi. O programa mostra o comprimento em λ, o ganho (curva DL6WU) e o lóbulo a −3 dB, horizontal e vertical; veja [Geometria e atenuação](Geometry-and-Path-Loss-pt-br#ganho-e-lóbulo-da-antena). Abaixo de 2 λ a estimativa é pouco precisa. |
| **Hot spot desde o ponto médio km** + **auto (AMS)** | Distância de Hot A e Hot B ao ponto médio. Com *auto (AMS)* marcado (padrão) segue a tabela de desvio da antena de J. Richardson (AMS) citada por DJ5HG: 13° a 1000 km, 11° a 1250 km, 10° a 1500 e 2000 km (cerca de 115, 121, 132 e 176 km do ponto médio). Desmarque-o para digitar 30–400 km manualmente (o MSHV usa 150 km). |

**Linha 3 – hora**

| Comando | O que faz |
|---|---|
| **Hora** | Relógio UTC. |
| **Data do cálculo (UTC)** | O dia do cálculo para [Cálculo de previsão](Sky-View-pt-br) e [Radar GRAVES](GRAVES-Radar-pt-br) (hoje por padrão), à hora atual do dia. Também: o dia mostrado em [Cálculo da eficiência](Efficiency-Calculation-pt-br) e na cronologia do GRAVES. |
| **Horas (de −12 a +36 h)** | Desloca o momento do cálculo desde 12 horas antes até 36 horas depois dessa hora, em passos de 15 minutos. Ao lado: *Cálculo para: agora* ou *Cálculo para: dd/mm hh:mm UTC*. |
| **Tempo real** | Volta ao momento atual. |

## 2. A sua estação e o DX

1. Escreva **O meu locator** e **altitude m**.
2. Escreva locator e altitude do **Correspondente**, ou clique no mapa da [Abóbada celeste](Sky-View-pt-br): **clique esquerdo = locator do correspondente**, **clique direito = locator da minha estação**.
3. Escolha a **Banda MHz** e clique em **Calcular**.

A barra de status embaixo confirma: *Percurso calculado: … km, … pontos de reflexão amostrados em … s*.

## 3. A sua antena

Insira o **comprimento do boom** da sua Yagi. O programa calcula ganho e lóbulo e avisa se Hot A ou Hot B já caem **dentro do lóbulo** quando a antena aponta para o DX (então são desenhados em cinza: não é preciso girar a antena).

## 4. Ler os resultados

| Pergunta | Onde ver |
|---|---|
| Que chuva ajuda agora o meu percurso, e de que lado? | [Abóbada celeste](Sky-View-pt-br): lista de chuvas, Hot recomendado em vermelho, zonas PREV |
| Qual é a melhor hora hoje? | [Cálculo da eficiência](Efficiency-Calculation-pt-br): cartões de resumo e tabela horária |
| Quantos meteoros o radar está contando? | [Fluxo radar](Radar-Flux-pt-br) |
| Quantos pings posso esperar nos 144 MHz? | [Previsões experimentais](Experimental-Forecasts-pt-br) (experimental) |
| A minha estação consegue fechar o percurso? | [Geometria e atenuação](Geometry-and-Path-Loss-pt-br): atenuação do percurso e margem |
| Quando é o próximo máximo? | [Chuvas](Showers-pt-br) |
| Posso fazer testes com o GRAVES? | [Radar GRAVES](GRAVES-Radar-pt-br) |

## Regras práticas (das fontes)

- **Apontar perpendicularmente à chuva**: o melhor percurso é ortogonal ao azimute do radiante; melhor apontamento = azimute do radiante ±90°, tolerância ±40–50° (SM6FHZ).
- **Side-scatter**: gire a antena 10–30° para o lado (A ou B) de onde chega a maioria das reflexões (artigo Cerrotta–Sartori).
- Um **radiante alto demais** (acima de 70°) ou baixo demais (abaixo de 20°) dá poucos rastros úteis (DF5HC, DH9GCD).
- Os meteoros esporádicos têm o máximo por volta das **06 UTC** (artigo; confirmado pelo fluxo de Collm).
- Distâncias úteis nos 432 MHz: 800–2000 km, a melhor cerca de 1400 km (SM6FHZ); melhor distância em geral 1300–1500 km (DF5HC).

Próximo: [Abóbada celeste](Sky-View-pt-br).
