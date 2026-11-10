[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · **Português** · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Abóbada celeste

*Separador: Cálculo de previsão › Cálculo de previsão.*

[![Abóbada celeste](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Este subseparador (a abóbada celeste das versões anteriores) reúne num só ecrã **onde** estão agora os rastos úteis e **para onde apontar**. À esquerda a **vista em planta** do percurso; à direita a lista de chuvas, uma pequena abóbada celeste com os radiantes, o texto do cálculo e o **corte** visto a partir da sua antena. Tudo se refere ao momento escolhido com *Data do cálculo (UTC)* e o controlo deslizante *Horas (de −12 a +36 h)* (tempo real por omissão, em passos de 15 minutos).

Uma **faixa por cima da vista em planta** resume o cálculo para esse momento: data e hora (*agora* ou horas em relação a agora), o **índice do percurso Σ ZHR×η**, a **chuva mais útil** com o seu ZHR e a sua eficiência (também em dB em relação à referência DJ5HG, ver [Cálculo da eficiência](Efficiency-Calculation-pt)), o número de chuvas acima do horizonte e o **Hot recomendado** com o seu azimute.

Na pequena abóbada celeste uma **linha laranja** que passa pelo zénite indica sempre as **direções de antena certas**, ortogonais à deslocação da chuva selecionada (ou da mais favorável): azimute do radiante ±90°, com a etiqueta *antena NNN°* em ambas as extremidades e a tolerância de ±45° em linhas finas. Pequenas marcas laranja no bordo indicam as direções ortogonais das outras chuvas úteis.

## Vista em planta (esquerda)

Um mapa da Europa visto de cima (**E à direita**) com uma escala de graus à volta. A legenda por baixo do mapa indica o seu raio (*Mapa: bordo = … km da estação*).

| Elemento | Desenho |
|---|---|
| Percurso / DX | Linha verde da sua estação até ao correspondente (sempre o percurso real de círculo máximo entre os locators) |
| **Hot A / Hot B** | Pontos de cada lado do ponto médio, perpendiculares ao percurso, à distância dada pela tabela de desvio AMS (ou introduzida à mão). **Vermelho = recomendado**, **rosa = fora do lóbulo da antena**, **cinzento = dentro do lóbulo** (com um aviso) |
| Lóbulo da antena | O lóbulo horizontal a −3 dB em torno do azimute da antena (antena sempre apontada para o DX), com a etiqueta *lóbulo …°* |
| Limites da zona comum | Pontos ténues *lim. A* / *lim. B* e os dois círculos onde o horizonte de cada estação encontra a camada E (ver [Geometria](Geometry-and-Path-Loss-pt#limites-da-zona-comum)) |
| Deslocação da chuva | **Linha amarela**: direção em que a chuva selecionada (ou a mais favorável) varre o céu, ou seja, o azimute do radiante |
| Melhores apontamentos | **Pontos laranja**: os dois apontamentos perpendiculares à deslocação (azimute do radiante ±90°, SM6FHZ) |
| **Zonas PREV** | Elipses claras: onde caem **agora** os rastos mais prováveis, uma de cada lado do percurso |

As etiquetas não se sobrepõem: Hot A e PREV A são escritos à esquerda do percurso, B à direita. A **Legenda** é uma coluna recolhível à direita do mapa.

**Rato no mapa:** **clique esquerdo = locator do correspondente**, **clique direito = locator da minha estação**. O percurso é recalculado de imediato.

Opções por cima da lista de chuvas: **Direções Hot A / Hot B**, **Mapa da Europa** (Natural Earth, descarregado para `data/mappa` no primeiro arranque), **Vista de cima (E à direita)**.

### Hot recomendado

Para a hora mostrada, o programa soma em todas as chuvas acima do horizonte o peso ZHR × eficiência, repartido entre o lado A (fração f_A) e o lado B. O lado com maior peso dá o Hot recomendado, desenhado a vermelho:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Escolha do programa (eq. 23 do manual).* Origem da ideia: DJ5HG, citado por DF5HC (conferência DARC 2018) – consoante a posição do radiante, um dos dois pontos, HOT-A ou HOT-B, é mais favorável. Rodar 10–30° para esse lado (side-scatter) vem do artigo Cerrotta–Sartori.

### Zonas PREV

Para cada ponto P da camada E somam-se as contribuições de todas as chuvas ativas para a eficiência (mesma condição especular da [eficiência](Efficiency-Calculation-pt#o-modelo)), ponderadas com o ZHR. Os pontos com pelo menos 3 % do máximo formam as zonas PREV; cada uma é desenhada como uma elipse com centro = média ponderada dos pontos e eixos = o dobro da sua dispersão.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Escolha do programa (eq. 34 do manual).* É a regra prática: se a chuva varre de norte para sul, os rastos úteis caem a leste e a oeste.

## Lista de chuvas (em cima à direita)

| Coluna | Significado |
|---|---|
| Chuva, Sigla | Nome e código IMO |
| ZHR agora | Atividade neste momento (ZHR máximo IMO com o perfil de atividade) |
| Azimute, Elev. | Posição do radiante vista da sua estação |
| Efic. % | Eficiência da chuva para este percurso |
| Lado | A ou B, o lado de onde chega a maioria das reflexões |
| Melhor apont. | Azimute do radiante ±90° |
| Nascer, Ocaso | Nascer e ocaso do radiante (UTC); *circumpolar* ou *sempre abaixo* quando se aplica |

Clique numa linha para selecionar a chuva: a linha amarela de deslocação e os pontos laranja acompanham-na.

## Pequena abóbada celeste (ao centro, à direita)

Os radiantes numa abóbada celeste vista da sua estação, com o seu **código IMO** e a **trajetória diária a ciano** (horas UTC). **Clique num radiante** para o selecionar. Cores:

| Cor | Significado |
|---|---|
| Amarelo | eficiência ≥ 50 % e ZHR ≥ 2 |
| Laranja | eficiência ≥ 20 % |
| Vermelho-escuro | eficiência < 20 % |
| Cinzento | quase inativa |

Ao lado, o texto do cálculo: comprimento e azimute do percurso, ponto médio e a sua elevação, azimutes e desvios de Hot A / Hot B, o Hot recomendado (*… recomendado agora: az. …° (…% das reflexões previstas)*), os limites da zona comum e o lembrete: *melhor apontamento para a chuva: PERPENDICULAR à direção de chegada (azimute do radiante ±90°, tolerância ±40–50°, SM6FHZ)*.

## Corte (em baixo à direita)

*CORTE - os rastos mais prováveis vistos da antena em direção ao correspondente.* Na horizontal o **azimute em relação ao correspondente** (← A esquerda, B → direita), na vertical a **elevação**. Para cada chuva tomam-se os 14 pontos de reflexão mais intensos; cada rasto é um segmento orientado para o radiante, de 10 km acima a 10 km abaixo da altitude dos rastos (no máximo 60 km por lado), mais grosso quanto mais provável. São também desenhados: o lóbulo da antena (círculo de −3 dB em torno da elevação do lóbulo), o correspondente e Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Escolha do programa (eq. 35 do manual).*

## Avisos

| Aviso | Quando |
|---|---|
| **ATENÇÃO: Hot A (e/ou Hot B) fica dentro do lóbulo da antena …** | O hot spot está dentro de ±θ/2 do azimute da antena (θ = lóbulo horizontal a −3 dB): com este apontamento já está coberto. É marcado a cinzento no mapa. O Hot recomendado continua a vermelho. |
| **RADIANTE DEMASIADO ALTO (acima de 70°)** | Um radiante útil está acima de 70° visto da sua estação: os rastos descem quase verticais e refletem pouco em direção ao percurso (DF5HC, DH9GCD). As mesmas horas são marcadas com ↑ na [tabela horária](Efficiency-Calculation-pt#tabela-horária). |
| **RADIANTE BAIXO AO LONGO DO PERCURSO** | Um radiante ativo está abaixo de 20° e a menos de 30° da direção do percurso. A eficiência calculada continua baixa (prudente), mas DJ5HG espera reflexões raras e fortes de rastos rasantes alinhados com o percurso (Hamburgo–Narvik, Quadrântidas, cerca das 19 UTC): vale a pena escutar. |
| **PERCURSO PARA ALÉM DO HORIZONTE DOS RASTOS** | À altitude dos rastos, o ponto médio do percurso está abaixo do horizonte de ambas as estações (cerca de 2120 km com rastos a 90 km). O aviso indica a altitude mínima dos rastos necessária (cerca de 96 km para 2200 km, 105 km para 2300 km): a ligação só é possível com os rastos mais altos, e as eficiências e atenuações estão no limite do modelo. |
| *Nenhuma zona comum da camada E* | O percurso é mais longo do que o dobro do alcance à altitude dos rastos: as duas estações não veem uma parte comum da camada E (salto único impossível). |
| *Nenhum Hot recomendado* | Chuvas ativas quase ausentes neste momento. |

Referência para o gráfico da abóbada celeste: Swan Meteor Skyview de DL1DBC (swan.ms); gráfico polar com a melhor direção: RadiantCalc de SM6FHZ.
