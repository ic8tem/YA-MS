**English** · [Русский](Getting-Started-ru) · [Deutsch](Getting-Started-de) · [日本語](Getting-Started-ja)

# Primeiros passos

No primeiro arranque o YA-MS mostra um percurso de exemplo (JN70CN → JO62QM nos 144 MHz). Bastam cinco minutos para o configurar para a sua estação.

## 1. As três filas de comandos

Por cima dos separadores há três filas de comandos, válidas para todos os separadores. O botão **Comandos** no canto superior direito recolhe-as e mostra-as (útil com letra grande); a escolha fica memorizada.

**Fila 1 – estações e banda**

| Comando | O que faz |
|---|---|
| **O meu locator** / **altitude m** | O seu locator Maidenhead (4, 6 ou 8 caracteres; é usado o centro do quadrado) e a altitude da estação acima do nível do mar. |
| **Correspondente** / **altitude m** | Locator e altitude da estação que quer trabalhar. |
| **Banda MHz** | 28, 50, 70, 144, 222 ou 432 MHz: usada para o ganho e o lóbulo da antena, a estimativa do fluxo e o balanço da ligação. |
| **Calcular** | Recalcula o percurso (amostragem da camada E: alguns segundos). |
| **Antena az** | Azimute da sua antena: sempre **em direção ao DX** (azimute do percurso). |
| **Tipo de letra** | Tamanho de todo o texto, 100–300 %. Ver [Definições](Settings-and-Data-Folder-pt#tipo-de-letra-e-comandos). |

**Fila 2 – camada E e antena**

| Comando | O que faz |
|---|---|
| **Altitude dos rastos km** + **do radar** | Altitude dos rastos meteóricos (por omissão 90 km). Com *do radar* assinalado, é usada a altitude mais frequente (moda) medida pelo radar de Collm; ver [Fluxo radar](Radar-Flux-pt). |
| **Elevação do lóbulo °** | Elevação mínima do lóbulo da sua antena (0° = horizonte). Só são usados os pontos da camada E que ambas as estações veem acima desta elevação. |
| **Antena Yagi: boom m** | Comprimento do boom da sua Yagi. O programa mostra o comprimento em λ, o ganho (curva DL6WU) e o lóbulo a −3 dB, horizontal e vertical; ver [Geometria e atenuação](Geometry-and-Path-Loss-pt#ganho-e-lóbulo-da-antena). Abaixo de 2 λ a estimativa é pouco precisa. |
| **Hot spot desde o ponto médio km** | Distância de Hot A e Hot B ao ponto médio, 30–400 km (por omissão 150 km, como AMS Bulletin 203 / W8WN / MSHV). |

**Fila 3 – hora**

| Comando | O que faz |
|---|---|
| **Hora** | Relógio UTC. |
| **Hora da abóbada celeste (±36 h)** | Desloca a [Abóbada celeste](Sky-View-pt) e o separador [Radar GRAVES](GRAVES-Radar-pt) até 36 horas para trás ou para a frente, em passos de 15 minutos. |
| **Tempo real** | Volta ao momento atual. |
| **Dia para a tabela de 24 h (UTC)** | O dia mostrado em [Cálculo da eficiência](Efficiency-Calculation-pt) e na cronologia do GRAVES. |

## 2. A sua estação e o DX

1. Escreva **O meu locator** e **altitude m**.
2. Escreva locator e altitude do **Correspondente**, ou clique no mapa da [Abóbada celeste](Sky-View-pt): **clique esquerdo = locator do correspondente**, **clique direito = locator da minha estação**.
3. Escolha a **Banda MHz** e prima **Calcular**.

A barra de estado em baixo confirma: *Percurso calculado: … km, … pontos de reflexão amostrados em … s*.

## 3. A sua antena

Introduza o **comprimento do boom** da sua Yagi. O programa calcula ganho e lóbulo e avisa se Hot A ou Hot B já caem **dentro do lóbulo** quando a antena aponta para o DX (então são desenhados a cinzento: não é preciso rodar a antena).

## 4. Ler os resultados

| Pergunta | Onde ver |
|---|---|
| Que chuva ajuda agora o meu percurso, e de que lado? | [Abóbada celeste](Sky-View-pt): lista de chuvas, Hot recomendado a vermelho, zonas PREV |
| Qual é a melhor hora hoje? | [Cálculo da eficiência](Efficiency-Calculation-pt): cartões de resumo e tabela horária |
| Quantos meteoros está o radar a contar? | [Fluxo radar](Radar-Flux-pt) |
| Quantos pings posso esperar nos 144 MHz? | [Previsões experimentais](Experimental-Forecasts-pt) (experimental) |
| A minha estação consegue fechar o percurso? | [Geometria e atenuação](Geometry-and-Path-Loss-pt): atenuação do percurso e margem |
| Quando é o próximo máximo? | [Chuvas](Showers-pt) |
| Posso fazer testes com o GRAVES? | [Radar GRAVES](GRAVES-Radar-pt) |

## Regras práticas (das fontes)

- **Apontar perpendicularmente à chuva**: o melhor percurso é ortogonal ao azimute do radiante; melhor apontamento = azimute do radiante ±90°, tolerância ±40–50° (SM6FHZ).
- **Side-scatter**: rode a antena 10–30° para o lado (A ou B) de onde chega a maioria das reflexões (artigo Cerrotta–Sartori).
- Um **radiante demasiado alto** (acima de 70°) ou demasiado baixo (abaixo de 20°) dá poucos rastos úteis (DF5HC, DH9GCD).
- Os meteoros esporádicos têm o máximo por volta das **06 UTC** (artigo; confirmado pelo fluxo de Collm).
- Distâncias úteis nos 432 MHz: 800–2000 km, a melhor cerca de 1400 km (SM6FHZ); melhor distância em geral 1300–1500 km (DF5HC).

Seguinte: [Abóbada celeste](Sky-View-pt).
