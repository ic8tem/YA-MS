[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · **Português** · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh)

# Cálculo da eficiência

*Separador: Cálculo de previsão › Cálculo da eficiência.*

[![Cálculo da eficiência](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

A **eficiência** de uma chuva indica, em percentagem, quanto a posição do seu radiante permite reflexões no **seu** percurso. O conceito é de Ilkka **OH5IY** (MS-Soft) e é retomado no artigo Cerrotta–Sartori: o máximo de eficiência não coincide com o máximo visual (ZHR), porque depende de onde está o radiante em relação às duas estações. O MCG_MS de DL5MCG aplica a mesma ideia a quatro direções fixas; o YA-MS calcula-a para o **percurso real** entre os dois locators.

Este separador mostra-a hora a hora para o dia escolhido em *Dia para a tabela de 24 h (UTC)* (valores à meia hora de cada hora).

## Cartões de resumo

| Cartão | Conteúdo |
|---|---|
| **MELHOR HORA DO DIA** | Hora com o índice do percurso mais alto, o índice e o lado predominante (A/B com a sua %) |
| **CHUVA MAIS FAVORÁVEL** | A chuva com o maior ZHR × eficiência do dia, a sua eficiência, hora e lado, e o **melhor apontamento** (azimute do radiante +90° / −90°) |
| **AGORA** | Índice e lado predominante a esta hora, e o Hot recomendado (só quando o dia escolhido é hoje) |
| **PREVISÃO EXPERIMENTAL** | Reflexões/hora esperadas agora, dentro de 1 h e dentro de 2 h à frequência da previsão (Collm, regras SM6FHZ; ver [Previsões experimentais](Experimental-Forecasts-pt)) |

Por baixo dos cartões, uma faixa explica as letras A e B (ver abaixo).

## Gráfico

*Eficiência horária para … de … (UTC, valores à meia hora).* Para até cinco chuvas: eficiência % em linha contínua e a fórmula de DH9GCD em linha pontilhada da mesma cor; o **índice do percurso** em barras azuis na escala da direita.

## Tabela horária

Uma linha por cada chuva ativa nesse dia (ordenadas por ZHR), 24 colunas para as horas (UTC):

| Célula | Significado |
|---|---|
| `63A` | eficiência 63 %, a maioria das reflexões do lado **A** |
| `41B` | eficiência 41 %, lado **B** |
| `3` | eficiência inferior a 5 %: número sem letra de lado |
| vazia | eficiência inferior a 1 % |
| `…↑` | o radiante está **acima de 70°** visto da sua estação a essa hora (demasiado alto) |
| texto amarelo | eficiência ≥ 50 % |

- **A** = **esquerda** olhando da sua estação para o correspondente (zona Hot A); **B** = **direita** (zona Hot B). Convém rodar a antena **10–30° para esse lado** (side-scatter, artigo Cerrotta–Sartori).
- **Linhas azul-claras** (*DH9GCD %*, por baixo de cada chuva): a fórmula de DH9GCD, para comparação.
- **Linha Σ**: *Índice do percurso (ZHR×efic.)*.
- **Linha laranja** (*Previsão … MHz (refl./hora)*): a previsão experimental, para as horas em que existe (hoje e parte de amanhã).

## O modelo

Todos os passos estão no [manual de cálculo](Efficiency-Explanation-pt) (`doc/YA-MS_manuale_calcoli.docx`, capítulo 5). Em resumo:

**1. Reflexão especular.** Um rasto envia o sinal de A para B só se for tangente a um elipsoide com A e B nos focos (McKinley 1961). Os rastos de uma chuva são paralelos à direção do radiante ŝ (artigo; McKinley). Para cada ponto P da camada E, com os vetores unitários em direção às estações:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

A mesma lei está na base do QTFGUI de DJ5HG e do seu texto *"Die Geometrie von Meteorscatterverbindungen"* (2004): o rasto difunde num cone que tem o rasto como eixo, e só um recetor sobre o cone o ouve. Para um rasto ideal a parede do cone é muito fina (um radiador com milhares de comprimentos de onda); o programa aceita a condição com uma tolerância gaussiana σ = 0,05 rad (cerca de 3°), que representa o que o cone ideal não vê: a dispersão dos radiantes das chuvas (0,3–1,4° medidos pela GMN), os rastos curvados pelo vento e o seu comprimento finito – *escolha do programa*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Peso de cada ponto.** Potência de um rasto subdenso (McKinley), φ = metade do ângulo de dispersão (limitado a 85°, *escolha*):

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad w_P = \frac{1}{R_1 R_2 (R_1+R_2)\cos^2\varphi}
```

O número de meteoros que chega a um ponto é proporcional ao seno da elevação do radiante nesse ponto (ŝ·û_P), a mesma correção que a IMO usa para o ZHR.

**Opção "Rastos mais longos com radiante baixo (DJ5HG)"** (caixa por cima do gráfico, desligada por omissão, com tooltip): DJ5HG nota que com o radiante baixo caem menos meteoros por km², mas os rastos são mais longos (até 100 km úteis) e cumprem mais vezes a lei de reflexão. Com a opção ligada o peso passa a ser min(sin El, 15/100): a espessura útil da camada, 15 km, dividida pelo seno da elevação dá o comprimento do rasto, limitado a 100 km. Acima de cerca de 9° os dois efeitos anulam-se. Desligada, o cálculo continua prudente.

**3. Soma e percentagem.** Pontos a cada 15 km à altitude dos rastos, só onde ambas as estações os veem acima da elevação do lóbulo (*escolha*). 100 % é a posição do radiante mais favorável para esse percurso:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F é calculado uma vez por percurso numa grelha de direções (azimute a cada 5°, elevação a cada 2,5°) e interpolado.

**Eficiência em dB (referência DJ5HG).** A percentagem é relativa apenas à melhor posição do radiante para esse percurso. Para comparar percursos diferentes, o programa dá também a eficiência em dB em relação à referência fixa de DJ5HG: 0 dB é o máximo de um percurso norte–sul de 1000 km que atravessa o equador, com o radiante no equador celeste no equinócio, calculado com a mesma altitude e os mesmos pesos. DJ5HG indica os seus valores como melhores do que 6 dB.

**4. Lado e índice.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

A letra na tabela é o lado com a fração maior. *Escolhas do programa (eq. 32–33 do manual).*

## Comparação com DH9GCD

As fontes primárias para a melhor direção são Eshleman & Mlodnosky e Meeks & James (Proc. IRE, 1957), Hines (1955) e a sua verificação experimental por Forsyth, Hines & Vogan (1955): só são úteis os radiantes no semicírculo de céu perpendicular à bissetriz do ângulo de difusão, o número de rastos cresce com sin El e, perto do ponto médio, os rastos úteis caem a cerca de H·tan El para o lado, no lado oposto ao radiante. DJ5HG acrescenta uma reserva: com um radiante **baixo** mesmo ao longo do percurso, a fórmula de McKinley dá sinais fortes (Hamburgo–Narvik, Quadrântidas, cerca das 19 UTC), portanto "radiante alinhado com o percurso = quase zero" só vale para um radiante alto; o programa continua prudente e mostra o aviso *RADIANTE BAIXO AO LONGO DO PERCURSO*.

Uma verificação independente: a fórmula da melhor direção de **DH9GCD**, citada por **DF5HC** (conferência DARC, janeiro de 2018) – não tem fonte primária publicada –, com El e Az a elevação e o azimute do radiante vistos da sua estação e P o azimute do correspondente:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

É máxima com o radiante a 45° e de lado em relação ao percurso. DF5HC considera o radiante demasiado baixo abaixo de 20° e **demasiado alto acima de 70°**: essas horas levam ↑ na tabela e um aviso na [Abóbada celeste](Sky-View-pt#avisos). A fórmula ignora a distância e as altitudes, mas é uma boa referência.

## Verificações

| Verificação | Resultado |
|---|---|
| Regra de SM6FHZ (VUSHF 2025): melhor percurso ortogonal ao azimute do radiante, apontamento = az do radiante ±90°, tolerância ±40–50° | Reproduzida pelo modelo; com o radiante alinhado com o percurso e alto no céu a eficiência é quase nula |
| QTFGUI de DJ5HG, Hamburgo JO53IM – Barcelona, Quadrântidas, 4 de janeiro (exemplo do seu manual) | QTFGUI: 07:00 apontamento 252°, −8 dB; 08:00 nenhuma zona de reflexão; 09:00 apontamento 168°, −4 dB. YA-MS (altitude 102 km como o QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Os três métodos veem o buraco das 08:00, com o radiante quase no zénite |
| Amostragem a cada 5 km em vez de 15 km | as percentagens mudam menos de 0,3 pontos |

> A documentação do MS-Soft 5.2 define a eficiência de OH5IY como um índice relativo apenas para rastos subdensos, com dois fatores (elevação do radiante, melhor cerca de 45°, e ângulo com o percurso, melhor 90°) e um mínimo elevado à mão para 20 % para os rastos sobredensos; a fórmula não está publicada. O MCG_MS calcula-a para quatro direções fixas e, com o locator do DX, para o percurso real. O modelo considera apenas rastos subdensos, com antenas isotrópicas; as rajadas sobredensas e o fundo esporádico não entram na eficiência (o fundo esporádico é representado pelo fluxo radar).
