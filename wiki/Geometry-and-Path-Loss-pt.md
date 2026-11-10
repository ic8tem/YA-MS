[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · **Português** · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometria e atenuação

*Separador: Cálculo de previsão › Geometria e atenuação.*

[![Geometria e atenuação](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Um relatório em texto do percurso (selecionável, para o poder copiar) e, à direita, o gráfico **Elevação da antena em função da distância ao scatter point**. Os números entre parênteses retos remetem para as equações do manual de cálculo (`doc/YA-MS_manuale_calcoli.docx`).

## Dados de entrada deste separador

| Campo | Por omissão | Utilização |
|---|---|---|
| **Potência W** | 400 | Potência do emissor para o balanço da ligação |
| **Ganho da antena dBi (tx = rx)** | 14 | A mesma antena em ambas as extremidades |
| **Sinal mínimo dBm** | −130 | Sinal mínimo detetável (artigo: Yagi de 8 elementos + pré-amplificador) |
| **Densidade do rasto q = 10^ … eletrões/m** | 14 | Densidade linear de eletrões do rasto subdenso |

As estações, a banda, a altitude dos rastos, a elevação do lóbulo, o boom e a distância dos hot spots vêm das [filas de comandos](Getting-Started-pt#1-as-três-filas-de-comandos).

## Secções do relatório

| Secção | Conteúdo |
|---|---|
| **GEOMETRIA DO PERCURSO (Terra esférica, R = 6372,7955 km)** | Estação e DX com as suas altitudes; distância, azimute e azimute inverso; ponto médio (locator e coordenadas); altitude dos rastos (*<- moda medida pelo radar de Collm* quando obtida do radar); elevação da antena em direção ao ponto médio |
| **HOT A / HOT B (hot spots clássicos, para o apontamento da antena)** | Para cada um: locator, azimute a partir da sua estação e desvio em relação ao percurso direto, azimute a partir do DX, distância, elevação |
| **LIMITES DA ZONA COMUM** | Alcance à altitude dos rastos com a elevação do lóbulo; Limite A / Limite B com os respetivos azimutes |
| Antena | Boom em λ, ganho, lóbulo horizontal / vertical; se Hot A e Hot B estão dentro ou fora do lóbulo |
| **ATENUAÇÃO DO PERCURSO (rasto subdenso, McKinley 1961; ganhos das antenas excluídos)** | Tabela para o ponto médio (forward), Hot A e Hot B a 28, 50, 70, 144, 222 e 432 MHz |
| **BALANÇO DA LIGAÇÃO A … MHz (ponto médio)** | Potência e PIRE, atenuação do percurso, sinal na antena, mínimo detetável, **margem**; a mesma margem com a atenuação média de OH5IY |
| **REGRAS EXPERIMENTAIS ENTRE AS BANDAS (SM6FHZ, VUSHF 2025)** | Número/intensidade e duração comparados com os 144 MHz; ping máximo IARU |

## Locator e percurso

Locator (4, 6 ou 8 caracteres; centro do quadrado, sistema Maidenhead da IARU) [14]. Distância, azimute e ponto médio com fórmulas de círculo máximo numa esfera de raio **r = 6372,7955 km** (artigo Cerrotta–Sartori) [15–16]. Os cálculos que dependem da hora referem-se ao **ponto médio**, porque a melhor hora pode diferir até 1,5 horas entre as duas extremidades (SM6FHZ).

## Elevação da antena

**Fonte:** fórmula do artigo Cerrotta–Sartori (Figura 7), com x = d/r, sendo d a distância ao solo até ao ponto de reflexão, H a altitude dos rastos e h a altitude da estação [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Verificação:** coincide com a geometria esférica exata dentro de 0,03°. O programa usa o arco-tangente de dois argumentos, que dá valores negativos para lá do horizonte e evita o problema de periodicidade referido no artigo. Uma elevação negativa em direção ao ponto médio significa *percurso para lá do alcance geométrico de um salto único*.

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

**Verificação:** são os **limites mais afastados** do céu visto por ambas as estações, **não pontos para onde apontar**. Em JN70CN–IN78UO (1710 km, azimute 308°) ficam a 1062 km da estação, 37° à esquerda e à direita do percurso direto, enquanto o MSHV sugere 10°. É por isso que se chamam *Limite A* / *Limite B* e são desenhados de forma ténue no mapa.

## Hot A e Hot B

**Fonte:** as reflexões concentram-se em duas zonas ("hot spots") a cerca de **50–150 km de cada lado do ponto médio**. É a base da tabela de desvio da antena do AMS Bulletin n.º 203, retomada por W8WN (desvio de 10° para percursos de 1500 e 1800 km); o MSHV de LZ2HV usa o mesmo critério.

**Escolha:** Hot A e Hot B são os pontos à distância s do ponto médio M, perpendiculares ao percurso (s = 150 km, ajustável de 30 a 400 km); A à esquerda olhando da sua estação para o DX, B à direita [21]. O desvio visto da estação é aproximadamente [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verificação:** JN70CN–IN78UO, D = 1710 km: 6,7° com s = 100 km, **10,0° com s = 150 km** (igual ao MSHV e a AMS/W8WN), 13,2° com s = 200 km.

## Atenuação subdensa

**Fonte:** equação de McKinley para rastos subdensos (β = 0, sen α = 1), ganhos das antenas excluídos; q = densidade linear de eletrões, r_e = raio clássico do eletrão = 2,818·10⁻¹⁵ m, R1, R2 distâncias ao rasto, φ metade do ângulo de dispersão [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\cos^2\varphi}{\lambda^3 q^2 r_e^2}\right]\ \mathrm{dB}
```

**Verificação:** com q = 10¹⁴ eletrões/m a 144 MHz: **181–192 dB** entre 600 e 2200 km, em linha com as referências do artigo a 144 MHz: **182 dB no mínimo** (GM8JBJ, de Kaiser & Closs 1952) e **200 dB em média** (OH5IY).

## Balanço da ligação

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - 2{.}15 - L + G_{rx} - 2{.}15,\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Os ganhos são introduzidos em dBi e usados em dBd (dBi − 2,15). O relatório dá também a margem com a **atenuação média de OH5IY** (200 dB a 144 MHz, transposta com λ³ para a banda escolhida). Referência do artigo: são necessários cerca de **70 dBm de PIRE** (−130 dBm + 200 dB, p. ex. cerca de 400 W em 14 dBi).

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

A antena é sempre considerada apontada para o DX. Um hot spot está **dentro do lóbulo** se |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: é então desenhado a cinzento na [Abóbada celeste](Sky-View-pt) e aparece um aviso. No cálculo da eficiência as antenas são isotrópicas; o lóbulo real só é usado para esta verificação.

## Regras experimentais entre as bandas

Em relação aos 144 MHz: número/intensidade × (144/f)³ (em dB), duração × (144/f)² (SM6FHZ, VUSHF 2025). Duração máxima dos pings segundo a IARU Região 1: 1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz (VHF Handbook, citado no artigo). Ver também [Previsões experimentais](Experimental-Forecasts-pt).
