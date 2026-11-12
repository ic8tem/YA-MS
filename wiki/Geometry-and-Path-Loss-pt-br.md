[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · **Português (Brasil)** · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometria e atenuação

*Aba: Cálculo de previsão › Geometria e atenuação.*

[![Geometria e atenuação](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Um relatório em texto do percurso (selecionável, para que você possa copiá-lo) e, à direita, o gráfico **Elevação da antena em função da distância ao scatter point**. Os números entre colchetes remetem às as equações do manual de cálculo (`doc/YA-MS_manuale_calcoli.docx`).

## Dados de entrada desta aba

| Campo | Padrão | Uso |
|---|---|---|
| **Potência W** | 400 | Potência do transmissor para o balanço do enlace |
| **Ganho da antena dBi (tx = rx)** | 14 | A mesma antena em ambas as extremidades |
| **Sinal mínimo dBm** | −130 | Sinal mínimo detectável (artigo: Yagi de 8 elementos + pré-amplificador) |
| **Densidade do rastro q = 10^ … elétrons/m** | 14 | Densidade linear de elétrons do rastro subdenso |

As estações, a banda, a altitude dos rastros, a elevação do lóbulo, o boom e a distância dos hot spots vêm das [linhas de comandos](Getting-Started-pt-br#1-as-três-linhas-de-comandos).

## Seções do relatório

| Seção | Conteúdo |
|---|---|
| **GEOMETRIA DO PERCURSO (Terra esférica, R = 6372,7955 km)** | Estação e DX com as suas altitudes; distância, azimute e azimute inverso; ponto médio (locator e coordenadas); altitude dos rastros (*<- moda medida pelo radar de Collm* quando obtida do radar); elevação da antena em direção ao ponto médio |
| **HOT A / HOT B (hot spots clássicos, para o apontamento da antena)** | Para cada um: locator, azimute a partir da sua estação e desvio em relação ao percurso direto, azimute a partir do DX, distância, elevação |
| **LIMITES DA ZONA COMUM** | Alcance à altitude dos rastros com a elevação do lóbulo; Limite A / Limite B com os respectivos azimutes |
| Antena | Boom em λ, ganho, lóbulo horizontal / vertical; se Hot A e Hot B estão dentro ou fora do lóbulo |
| **ATENUAÇÃO DO PERCURSO (rastro subdenso, McKinley 1961; ganhos das antenas excluídos)** | Tabela para o ponto médio (forward), Hot A e Hot B a 28, 50, 70, 144, 222 e 432 MHz |
| **BALANÇO DO ENLACE A … MHz (ponto médio)** | Potência e PIRE, atenuação do percurso, sinal na antena, mínimo detectável, **margem**; a mesma margem com a atenuação média de OH5IY |
| **REGRAS EXPERIMENTAIS ENTRE AS BANDAS (SM6FHZ, VUSHF 2025)** | Número/intensidade e duração comparados com os 144 MHz; ping máximo IARU |

## Locator e percurso

Locator (4, 6 ou 8 caracteres; centro do quadrado, sistema Maidenhead da IARU) [14]. Distância, azimute e ponto médio com fórmulas de círculo máximo em uma esfera de raio **r = 6372,7955 km** (artigo Cerrotta–Sartori) [15–16]. Os cálculos que dependem da hora referem-se ao **ponto médio**, porque a melhor hora pode diferir até 1,5 horas entre as duas extremidades (SM6FHZ).

## Elevação da antena

**Fonte:** fórmula do artigo Cerrotta–Sartori (Figura 7), com x = d/r, sendo d a distância ao solo até o ponto de reflexão, H a altitude dos rastros e h a altitude da estação [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Verificação:** coincide com a geometria esférica exata dentro de 0,03°. O programa usa o arco-tangente de dois argumentos, que dá valores negativos além do horizonte e evita o problema de periodicidade mencionado no artigo. Uma elevação negativa em direção ao ponto médio significa *percurso além do alcance geométrico de um salto único*.

## Alcance do horizonte

Distância ao solo à qual um raio com elevação e atinge a altitude H (inversa geométrica da fórmula anterior) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Verificação:** H = 89,5 km, e = 0° → **1062 km**. No exemplo do artigo (JN44BB–IO53RT) o desenho coloca os cruzamentos do horizonte a cerca de 870 km das estações, o que corresponde a um lóbulo elevado cerca de 2° (865 km).

## Limites da zona comum

**Fonte:** o artigo localiza os cruzamentos das curvas onde o horizonte de cada estação encontra a camada E: os cruzamentos de dois círculos de raio angular ρ = d_H/r centrados em A e B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Se 1 − |p0|² < 0, o percurso é mais longo do que 2·d_H e as estações **não veem nenhuma zona comum da camada E**.

**Verificação:** são os **limites mais afastados** do céu visto por ambas as estações, **não pontos para onde apontar**. Em JN70CN–IN78UO (1710 km, azimute 308°) ficam a 1062 km da estação, 37° à esquerda e à direita do percurso direto, enquanto o MSHV sugere 10°. É por isso que se chamam *Limite A* / *Limite B* e são desenhados de forma tênue no mapa.

## Hot A e Hot B

**Fonte:** as reflexões dos meteoros esporádicos concentram-se em duas zonas ("hot spots") de cada lado do ponto médio. J. Richardson (AMS), na tabela citada por DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), dá o desvio da antena em relação ao rumo direto: **13° a 1000 km, 11° a 1250 km, 10° a 1500 e 2000 km**. O AMS Bulletin n.º 203, retomado por W8WN, dá 10° a 1500 e 1800 km.

**Escolha:** Hot A e Hot B são os pontos à distância s do ponto médio M, perpendiculares ao percurso. Com *auto (AMS)* marcado (padrão), s vem do desvio da tabela de Richardson, interpolado linearmente (13° abaixo de 1000 km, 10° acima de 2000 km): s = (D/2)·tan(desvio). Desmarcado, s é inserido manualmente, de 30 a 400 km (o MSHV usa 150 km); A à esquerda olhando da sua estação para o DX, B à direita [21]. O desvio visto da estação é aproximadamente [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verificação:** com a tabela AMS, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, igual aos 150 km usados antes e pelo MSHV; nos percursos curtos a tabela aproxima os hot spots do ponto médio.

## Atenuação subdensa

**Fonte:** equação de McKinley e Recomendação ITU-R P.843 para rastros subdensos (sen α = 1), ganhos das antenas excluídos; q = densidade linear de elétrons, r_e = raio clássico do elétron = 2,818·10⁻¹⁵ m, R1, R2 distâncias ao rastro, φ metade do ângulo de dispersão, β ângulo entre o rastro e o plano do percurso, a₁ fator do raio inicial com r₀ em m e h em km (P.843, eq. 4 e 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Escolha:** o balanço e a tabela de atenuações usam β = 90° (rastro que atravessa o plano do percurso, o caso menos favorável: valor prudente) e o balanço mostra também o melhor caso, β = 0. r₀ é tomado à altitude média dos ecos para a frequência, h = 124 − 17 log f (P.843, eq. 15): 0,76 m a 95 km para 50 MHz, 0,40 m a 87 km para 144 MHz, 0,21 m a 79 km para 432 MHz. Em 1000 km a₁ vale 0,2 dB a 50 MHz, 0,6 dB a 144 MHz e 1,4 dB a 432 MHz (2,9 dB a 600 km); à altitude fixa de 102 km de DJ5HG seria cerca de 70 dB a 432 MHz, ou seja, nenhum eco.

**Verificação:** com q = 10¹⁴ elétrons/m, rastros a 89,5 km e β = 0, a 144 MHz: **182–192 dB** entre 600 e 2100 km (185 dB a 1000 km), dentro do intervalo de **172–190 dB** calculado por John Worsnop **G4BAO** na sua tese de doutorado, conforme citado por GM8JBJ. Com β = 90° a atenuação cresce 10 dB a 600 km, 13 dB a 1000 km e 16 dB a 2100 km; os **200 dB de média** de OH5IY ficam entre os dois casos. Os 182 dB da tabela de GM8JBJ não são uma confirmação: a tabela não indica frequência, os seus 86,4 dB por trecho são a atenuação em espaço livre sobre 500 km a 1 MHz (falta o termo 20 log f: 129,6 dB a 144 MHz) e as suas parcelas somam 163,8 dB, não 182; a página não diz nem "mínimo" nem "144 MHz".

## Balanço do enlace

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Os ganhos são inseridos e usados em dBi: a atenuação de McKinley refere-se a antenas isotrópicas, portanto não se subtrai a correção de dipolo de 2,15 dB (PIRE = potência + ganho). O relatório dá também a margem com a **atenuação média de OH5IY** (200 dB a 144 MHz, transposta com λ³ para a banda escolhida). Referência do artigo: são necessários cerca de **70 dBm de PIRE** (−130 dBm + 200 dB, p. ex. cerca de 400 W em 14 dBi).

## Ganho e lóbulo da antena

**Ganho – fonte:** curva de Günter Hoch **DL6WU** para Yagis longas em função do comprimento do boom L, citada por W8IO (válida a partir de cerca de 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Verificação com os modelos NEC de L.B. Cebik W4RNL a 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementos | Boom (λ) | NEC W4RNL (dBi) | Fórmula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

A diferença nunca ultrapassa **0,1 dB**: o ganho depende mais do comprimento do boom do que do projeto (as Yagis VK3AUU têm um boom mais curto para o mesmo número de elementos). O Yagi Calculator de VK5DJ dá também estimativas para as variantes VK3AUU, WA2PHW e DJ9BV, cujas fórmulas não estão publicadas.

**Lóbulo – fonte:** regra de Kraus, com lóbulo circular θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Verificação:** os modelos NEC de W4RNL de Yagis DL6WU dão um **lóbulo horizontal 5–10 % mais estreito** do que Kraus: 33,8° / 26,4° / 22,6° para 12, 19 e 26 elementos, contra 37,3° / 28,0° / 23,9°. As fórmulas simples ignoram os lóbulos laterais dianteiros (W4RNL, *Long-Boom Yagi Rules of Thumb*). Em booms longos o lóbulo vertical é ligeiramente mais largo do que o horizontal (14 λ: 18,4° / 18,8°).

**Escolha** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Exemplo: Yagi de 14 λ a 432 MHz → 20,3 dBi, lóbulo de 18,1° na horizontal e 19,5° na vertical; os modelos de W4RNL dão 20,4 dBi e 18,4° / 18,8°. São regras aproximadas obtidas a partir de algumas antenas DL6WU.

A antena é sempre considerada apontada para o DX. Um hot spot está **dentro do lóbulo** se |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: ele é então desenhado em cinza na [Abóbada celeste](Sky-View-pt-br) e aparece um aviso. O lóbulo vertical também entra no cálculo da eficiência: com a caixa *diagrama da antena* ligada, os pontos de reflexão são ponderados pelo ganho vertical das duas antenas (largura θ_vertical, máximo na elevação do lóbulo, fator do solo até zero no horizonte).

## Regras experimentais entre as bandas

Em relação aos 144 MHz: número/intensidade × (144/f)³ (em dB), duração × (144/f)² (SM6FHZ, VUSHF 2025). Duração máxima dos pings segundo a IARU Região 1: 1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz (VHF Handbook, citado no artigo). Ver também [Previsões experimentais](Experimental-Forecasts-pt-br).
