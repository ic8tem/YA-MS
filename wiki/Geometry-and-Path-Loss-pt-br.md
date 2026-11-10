[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · **Português (Brasil)** · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [ไทย](Geometry-and-Path-Loss-th) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometria e atenuação

*Aba: Cálculo de previsão › Geometria e atenuação.*

[![Geometria e atenuação](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Um relatório em texto do percurso (selecionável, para que você possa copiá-lo) e, à direita, o gráfico **Elevação da antena em função da distância ao scatter point**. Os números entre colchetes remetem às equações do manual de cálculo (`doc/YA-MS_manuale_calcoli.docx`).

## Dados de entrada desta aba

| Campo | Padrão | Uso |
|---|---|---|
| **Potência W** | 400 | Potência do transmissor para o balanço do enlace |
| **Ganho da antena dBi (tx = rx)** | 14 | A mesma antena nas duas pontas |
| **Sinal mínimo dBm** | −130 | Sinal mínimo detectável (artigo: Yagi de 8 elementos + pré-amplificador) |
| **Densidade do rastro q = 10^ … elétrons/m** | 14 | Densidade linear de elétrons do rastro subdenso |

As estações, a banda, a altitude dos rastros, a elevação do lóbulo, o boom e a distância dos hot spots vêm das [linhas de comandos](Getting-Started-pt-br#1-as-três-linhas-de-comandos).

## Seções do relatório

| Seção | Conteúdo |
|---|---|
| **GEOMETRIA DO PERCURSO (Terra esférica, R = 6372,7955 km)** | Estação e DX com as suas altitudes; distância, azimute e azimute reverso; ponto médio (locator e coordenadas); altitude dos rastros (*<- moda medida pelo radar de Collm* quando obtida do radar); elevação da antena em direção ao ponto médio |
| **HOT A / HOT B (hot spots clássicos, para o apontamento da antena)** | Para cada um: locator, azimute a partir da sua estação e desvio em relação ao percurso direto, azimute a partir do DX, distância, elevação |
| **LIMITES DA ZONA COMUM** | Alcance à altitude dos rastros com a elevação do lóbulo; Limite A / Limite B com os respectivos azimutes |
| Antena | Boom em λ, ganho, lóbulo horizontal / vertical; se Hot A e Hot B estão dentro ou fora do lóbulo |
| **ATENUAÇÃO DO PERCURSO (rastro subdenso, McKinley 1961; ganhos das antenas excluídos)** | Tabela para o ponto médio (forward), Hot A e Hot B em 28, 50, 70, 144, 222 e 432 MHz |
| **BALANÇO DO ENLACE A … MHz (ponto médio)** | Potência e EIRP, atenuação do percurso, sinal na antena, mínimo detectável, **margem**; a mesma margem com a atenuação média de OH5IY |
| **REGRAS EXPERIMENTAIS ENTRE AS BANDAS (SM6FHZ, VUSHF 2025)** | Número/intensidade e duração comparados com 144 MHz; ping máximo IARU |

## Locator e percurso

Locator (4, 6 ou 8 caracteres; centro do quadrado, sistema Maidenhead da IARU) [14]. Distância, azimute e ponto médio com fórmulas de círculo máximo em uma esfera de raio **r = 6372,7955 km** (artigo Cerrotta–Sartori) [15–16]. Os cálculos que dependem da hora referem-se ao **ponto médio**, porque a melhor hora pode diferir em até 1,5 hora entre as duas pontas (SM6FHZ).

## Elevação da antena

**Fonte:** fórmula do artigo Cerrotta–Sartori (Figura 7), com x = d/r, sendo d a distância no solo até o ponto de reflexão, H a altitude dos rastros e h a altitude da estação [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Verificação:** coincide com a geometria esférica exata dentro de 0,03°. O programa usa o arco tangente de dois argumentos, que dá valores negativos além do horizonte e evita o problema de periodicidade mencionado no artigo. Uma elevação negativa em direção ao ponto médio significa *percurso além do alcance geométrico de um salto único*.

## Alcance do horizonte

Distância no solo na qual um raio com elevação e atinge a altitude H (inversa geométrica da fórmula anterior) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Verificação:** H = 89,5 km, e = 0° → **1062 km**. No exemplo do artigo (JN44BB–IO53RT), o desenho coloca os cruzamentos do horizonte a cerca de 870 km das estações, o que corresponde a um lóbulo elevado cerca de 2° (865 km).

## Limites da zona comum

**Fonte:** o artigo localiza os cruzamentos das curvas onde o horizonte de cada estação encontra a camada E: os cruzamentos de dois círculos de raio angular ρ = d_H/r centrados em A e B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Se 1 − |p0|² < 0, o percurso é mais longo do que 2·d_H e as estações **não veem nenhuma zona comum da camada E**.

**Verificação:** são as **bordas mais distantes** do céu visto pelas duas estações, **não pontos para onde apontar**. Em JN70CN–IN78UO (1710 km, azimute 308°) elas ficam a 1062 km da estação, 37° à esquerda e à direita do percurso direto, enquanto o MSHV sugere 10°. É por isso que se chamam *Limite A* / *Limite B* e são desenhadas de forma tênue no mapa.

## Hot A e Hot B

**Fonte:** as reflexões se concentram em duas zonas ("hot spots") a cerca de **50–150 km de cada lado do ponto médio**. Essa é a base da tabela de desvio da antena do AMS Bulletin n.º 203, retomada por W8WN (desvio de 10° para percursos de 1500 e 1800 km); o MSHV de LZ2HV usa o mesmo critério.

**Escolha:** Hot A e Hot B são os pontos à distância s do ponto médio M, perpendiculares ao percurso (s = 150 km, ajustável de 30 a 400 km); A à esquerda olhando da sua estação para o DX, B à direita [21]. O desvio visto da estação é aproximadamente [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Verificação:** JN70CN–IN78UO, D = 1710 km: 6,7° com s = 100 km, **10,0° com s = 150 km** (igual ao MSHV e a AMS/W8WN), 13,2° com s = 200 km.

## Atenuação subdensa

**Fonte:** equação de McKinley para rastros subdensos (β = 0, sen α = 1), ganhos das antenas excluídos; q = densidade linear de elétrons, r_e = raio clássico do elétron = 2,818·10⁻¹⁵ m, R1, R2 distâncias ao rastro, φ metade do ângulo de espalhamento [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Verificação:** com q = 10¹⁴ elétrons/m em 144 MHz: **181–192 dB** entre 600 e 2200 km, em linha com as referências do artigo em 144 MHz: **182 dB no mínimo** (GM8JBJ, de Kaiser & Closs 1952) e **200 dB em média** (OH5IY).

## Balanço do enlace

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Os ganhos são informados em dBi e usados em dBd (dBi − 2,15). O relatório também dá a margem com a **atenuação média de OH5IY** (200 dB em 144 MHz, transposta com λ³ para a banda escolhida). Referência do artigo: são necessários cerca de **70 dBm de EIRP** (−130 dBm + 200 dB, p. ex. cerca de 400 W em 14 dBi).

## Ganho e lóbulo da antena

**Ganho – fonte:** curva de Günter Hoch **DL6WU** para Yagis longas em função do comprimento do boom L, citada por W8IO (válida a partir de cerca de 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Verificação com os modelos NEC de L.B. Cebik W4RNL em 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementos | Boom (λ) | NEC W4RNL (dBi) | Fórmula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

A diferença nunca passa de **0,1 dB**: o ganho depende mais do comprimento do boom do que do projeto (as Yagis VK3AUU têm um boom mais curto para o mesmo número de elementos). O Yagi Calculator de VK5DJ também dá estimativas para as variantes VK3AUU, WA2PHW e DJ9BV, cujas fórmulas não são publicadas.

**Lóbulo – fonte:** regra de Kraus, com lóbulo circular θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Verificação:** os modelos NEC de W4RNL de Yagis DL6WU dão um **lóbulo horizontal 5–10 % mais estreito** do que Kraus: 33,8° / 26,4° / 22,6° para 12, 19 e 26 elementos, contra 37,3° / 28,0° / 23,9°. As fórmulas simples ignoram os lóbulos laterais dianteiros (W4RNL, *Long-Boom Yagi Rules of Thumb*). Em booms longos o lóbulo vertical é ligeiramente mais largo do que o horizontal (14 λ: 18,4° / 18,8°).

**Escolha** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Exemplo: Yagi de 14 λ em 432 MHz → 20,3 dBi, lóbulo de 18,1° na horizontal e 19,5° na vertical; os modelos de W4RNL dão 20,4 dBi e 18,4° / 18,8°. São regras aproximadas obtidas a partir de algumas antenas DL6WU.

A antena é sempre considerada apontada para o DX. Um hot spot está **dentro do lóbulo** se |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: nesse caso ele é desenhado em cinza na [Abóbada celeste](Sky-View-pt-br) e aparece um aviso. No cálculo da eficiência as antenas são isotrópicas; o lóbulo real só é usado para essa verificação.

## Regras experimentais entre as bandas

Em relação a 144 MHz: número/intensidade × (144/f)³ (em dB), duração × (144/f)² (SM6FHZ, VUSHF 2025). Duração máxima dos pings segundo a IARU Região 1: 1000 ms em 50 MHz, 500 ms em 70 MHz, 100 ms em 144 MHz, 13 ms em 432 MHz (VHF Handbook, citado no artigo). Veja também [Previsões experimentais](Experimental-Forecasts-pt-br).
