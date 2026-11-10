LANGBAR

# Abóbada celeste

*Aba: Cálculo de previsão › Cálculo de previsão.*

[![Abóbada celeste](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Esta subaba (a abóbada celeste das versões anteriores) reúne em uma só tela **onde** estão agora os rastros úteis e **para onde apontar**. À esquerda, a **vista em planta** do percurso; à direita, a lista de chuvas, uma pequena abóbada celeste com os radiantes, o texto do cálculo e o **corte** visto a partir da sua antena. Tudo se refere à hora do controle deslizante *Hora da abóbada celeste* (tempo real por padrão; ±36 h em passos de 15 minutos).

Na pequena abóbada celeste, uma **linha laranja** que passa pelo zênite indica sempre as **direções de antena corretas**, ortogonais ao deslocamento da chuva selecionada (ou da mais favorável): azimute do radiante ±90°, com o rótulo *antena NNN°* nas duas extremidades e a tolerância de ±45° em linhas finas. Pequenas marcas laranja na borda indicam as direções ortogonais das outras chuvas úteis.

## Vista em planta (esquerda)

Um mapa da Europa visto de cima (**E à direita**) com uma escala de graus ao redor. A legenda embaixo do mapa indica o seu raio (*Mapa: borda = … km da estação*).

| Elemento | Desenho |
|---|---|
| Percurso / DX | Linha verde da sua estação até o correspondente (sempre o percurso real de círculo máximo entre os locators) |
| **Hot A / Hot B** | Pontos a 150 km (ajustável) de cada lado do ponto médio, perpendiculares ao percurso. **Vermelho = recomendado**, **rosa = fora do lóbulo da antena**, **cinza = dentro do lóbulo** (com um aviso) |
| Lóbulo da antena | O lóbulo horizontal a −3 dB em torno do azimute da antena (antena sempre apontada para o DX), com o rótulo *lóbulo …°* |
| Limites da zona comum | Pontos tênues *lim. A* / *lim. B* e os dois círculos onde o horizonte de cada estação encontra a camada E (veja [Geometria](Geometry-and-Path-Loss-pt-br#limites-da-zona-comum)) |
| Deslocamento da chuva | **Linha amarela**: direção em que a chuva selecionada (ou a mais favorável) varre o céu, ou seja, o azimute do radiante |
| Melhores apontamentos | **Pontos laranja**: os dois apontamentos perpendiculares ao deslocamento (azimute do radiante ±90°, SM6FHZ) |
| **Zonas PREV** | Elipses claras: onde caem **agora** os rastros mais prováveis, uma de cada lado do percurso |

Os rótulos não se sobrepõem: Hot A e PREV A são escritos à esquerda do percurso, B à direita. A **Legenda** é uma coluna recolhível à direita do mapa.

**Mouse no mapa:** **clique esquerdo = locator do correspondente**, **clique direito = locator da minha estação**. O percurso é recalculado imediatamente.

Opções acima da lista de chuvas: **Direções Hot A / Hot B**, **Mapa da Europa** (Natural Earth, baixado para `data/mappa` na primeira inicialização), **Vista de cima (E à direita)**.

### Hot recomendado

Para a hora mostrada, o programa soma, em todas as chuvas acima do horizonte, o peso ZHR × eficiência, dividido entre o lado A (fração f_A) e o lado B. O lado com maior peso dá o Hot recomendado, desenhado em vermelho:

```
W_A = Σ (ZHR·η/100)·f_A        W_B = Σ (ZHR·η/100)·(1 − f_A)        recommended = side with larger W
```

*Escolha do programa (eq. 23 do manual).* Origem da ideia: DJ5HG, citado por DF5HC (conferência DARC 2018) – dependendo da posição do radiante, um dos dois pontos, HOT-A ou HOT-B, é mais favorável. Girar 10–30° para esse lado (side-scatter) vem do artigo Cerrotta–Sartori.

### Zonas PREV

Para cada ponto P da camada E, somam-se as contribuições de todas as chuvas ativas para a eficiência (mesma condição especular da [eficiência](Efficiency-Calculation-pt-br#o-modelo)), ponderadas pela ZHR. Os pontos com pelo menos 3 % do máximo formam as zonas PREV; cada uma é desenhada como uma elipse com centro = média ponderada dos pontos e eixos = o dobro da sua dispersão.

```
W_P = Σ ZHR · c_P(ŝ)      c_P = 100 · w_P·S_P·max(0, ŝ·û_P) / max F      PREV: W_P ≥ 0.03 · max W
```

*Escolha do programa (eq. 34 do manual).* É a regra prática: se a chuva varre de norte para sul, os rastros úteis caem a leste e a oeste.

## Lista de chuvas (em cima à direita)

| Coluna | Significado |
|---|---|
| Chuva, Sigla | Nome e código IMO |
| ZHR agora | Atividade neste momento (ZHR máxima IMO com o perfil de atividade) |
| Azimute, Elev. | Posição do radiante vista da sua estação |
| Efic. % | Eficiência da chuva para este percurso |
| Lado | A ou B, o lado de onde chega a maioria das reflexões |
| Melhor apont. | Azimute do radiante ±90° |
| Nascer, Ocaso | Nascer e ocaso do radiante (UTC); *circumpolar* ou *sempre abaixo* quando se aplica |

Clique em uma linha para selecionar a chuva: a linha amarela de deslocamento e os pontos laranja passam a segui-la.

## Pequena abóbada celeste (no centro, à direita)

Os radiantes em uma abóbada celeste vista da sua estação, com o seu **código IMO** e a **trajetória diária em ciano** (horas UTC). **Clique em um radiante** para selecioná-lo. Cores:

| Cor | Significado |
|---|---|
| Amarelo | eficiência ≥ 50 % e ZHR ≥ 2 |
| Laranja | eficiência ≥ 20 % |
| Vermelho-escuro | eficiência < 20 % |
| Cinza | quase inativa |

Ao lado, o texto do cálculo: comprimento e azimute do percurso, ponto médio e a sua elevação, azimutes e desvios de Hot A / Hot B, o Hot recomendado (*… recomendado agora: az. …° (…% das reflexões previstas)*), os limites da zona comum e o lembrete: *melhor apontamento para a chuva: PERPENDICULAR à direção de chegada (azimute do radiante ±90°, tolerância ±40–50°, SM6FHZ)*.

## Corte (embaixo à direita)

*CORTE - os rastros mais prováveis vistos da antena em direção ao correspondente.* Na horizontal, o **azimute em relação ao correspondente** (← A esquerda, B → direita); na vertical, a **elevação**. Para cada chuva são tomados os 14 pontos de reflexão mais intensos; cada rastro é um segmento orientado para o radiante, de 10 km acima a 10 km abaixo da altitude dos rastros (no máximo 60 km por lado), mais grosso quanto mais provável. Também são desenhados: o lóbulo da antena (círculo de −3 dB em torno da elevação do lóbulo), o correspondente e Hot A / Hot B.

```
Q = P ± t½·ŝ        t½ = min(60 km, 10 km / max(0.17, |ŝ·û_P|))
```

*Escolha do programa (eq. 35 do manual).*

## Avisos

| Aviso | Quando |
|---|---|
| **ATENÇÃO: Hot A (e/ou Hot B) fica dentro do lóbulo da antena …** | O hot spot está dentro de ±θ/2 do azimute da antena (θ = lóbulo horizontal a −3 dB): com este apontamento ele já está coberto. É marcado em cinza no mapa. O Hot recomendado continua em vermelho. |
| **RADIANTE ALTO DEMAIS (acima de 70°)** | Um radiante útil está acima de 70° visto da sua estação: os rastros descem quase verticais e refletem pouco em direção ao percurso (DF5HC, DH9GCD). As mesmas horas são marcadas com ↑ na [tabela horária](Efficiency-Calculation-pt-br#tabela-horária). |
| *Nenhuma zona comum da camada E* | O percurso é mais longo do que o dobro do alcance à altitude dos rastros: as duas estações não veem uma parte comum da camada E (salto único impossível). |
| *Nenhum Hot recomendado* | Chuvas ativas quase ausentes neste momento. |

Referência para o gráfico da abóbada celeste: Swan Meteor Skyview de DL1DBC (swan.ms); gráfico polar com a melhor direção: RadiantCalc de SM6FHZ.
