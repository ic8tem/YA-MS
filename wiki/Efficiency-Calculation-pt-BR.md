[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · **Português (Brasil)** · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-TW)

# Cálculo da eficiência

*Aba: Cálculo de previsão › Cálculo da eficiência.*

[![Cálculo da eficiência](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

A **eficiência** de uma chuva indica, em porcentagem, quanto a posição do seu radiante permite reflexões no **seu** percurso. O conceito é de Ilkka **OH5IY** (MS-Soft) e é retomado no artigo Cerrotta–Sartori: o máximo de eficiência não coincide com o máximo visual (ZHR), porque depende de onde está o radiante em relação às duas estações. O MCG_MS de DL5MCG aplica a mesma ideia a quatro direções fixas; o YA-MS calcula-a para o **percurso real** entre os dois locators.

Esta aba a mostra hora a hora para o dia escolhido em *Dia para a tabela de 24 h (UTC)* (valores à meia hora de cada hora).

## Cartões de resumo

| Cartão | Conteúdo |
|---|---|
| **MELHOR HORA DO DIA** | Hora com o índice do percurso mais alto, o índice e o lado predominante (A/B com a sua %) |
| **CHUVA MAIS FAVORÁVEL** | A chuva com o maior ZHR × eficiência do dia, a sua eficiência, hora e lado, e o **melhor apontamento** (azimute do radiante +90° / −90°) |
| **AGORA** | Índice e lado predominante a esta hora, e o Hot recomendado (só quando o dia escolhido é hoje) |
| **PREVISÃO EXPERIMENTAL** | Reflexões/hora esperadas agora, dentro de 1 h e dentro de 2 h à frequência da previsão (Collm, regras SM6FHZ; veja [Previsões experimentais](Experimental-Forecasts-pt-BR)) |

Abaixo dos cartões, uma faixa explica as letras A e B (veja abaixo).

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
| `…↑` | o radiante está **acima de 70°** visto da sua estação a essa hora (alto demais) |
| texto amarelo | eficiência ≥ 50 % |

- **A** = **esquerda** olhando da sua estação para o correspondente (zona Hot A); **B** = **direita** (zona Hot B). Convém girar a antena **10–30° para esse lado** (side-scatter, artigo Cerrotta–Sartori).
- **Linhas azul-claras** (*DH9GCD %*, abaixo de cada chuva): a fórmula de DH9GCD, para comparação.
- **Linha Σ**: *Índice do percurso (ZHR×efic.)*.
- **Linha laranja** (*Previsão … MHz (refl./hora)*): a previsão experimental, para as horas em que existe (hoje e parte de amanhã).

## O modelo

Todos os passos estão no [manual de cálculo](Efficiency-Explanation-pt-BR) (`doc/YA-MS_manuale_calcoli.docx`, capítulo 5). Em resumo:

**1. Reflexão especular.** Um rastro envia o sinal de A para B só se for tangente a um elipsoide com A e B nos focos (McKinley 1961). Os rastros de uma chuva são paralelos à direção do radiante ŝ (artigo; McKinley). Para cada ponto P da camada E, com os vetores unitários em direção às estações:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

A mesma lei está na base do QTFGUI de DJ5HG e do seu texto *"Die Geometrie von Meteorscatterverbindungen"* (2004): o rastro difunde em um cone que tem o rastro como eixo, e só um receptor sobre o cone o ouve. Para um rastro ideal a parede do cone é muito fina (um radiador com milhares de comprimentos de onda); o programa aceita a condição com uma tolerância gaussiana σ = 0,05 rad (cerca de 3°), que representa o que o cone ideal não vê: a dispersão dos radiantes das chuvas (0,3–1,4° medidos pela GMN), os rastros curvados pelo vento e o seu comprimento finito – *escolha do programa*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Peso de cada ponto.** Potência de um rastro subdenso (McKinley; ITU-R P.843, eq. 3), φ = metade do ângulo de dispersão (limitado a 85°, *escolha*), β = ângulo entre o rastro e o plano de propagação A-P-B, p̂ = normal unitária a esse plano:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opção "Ângulo β entre rastro e percurso (McKinley completo)"** (ativada por padrão, configuração prudente). Ativada: os rastros que atravessam o plano de propagação valem 10–15 dB menos do que os que nele se encontram, de modo que nenhum rastro é superestimado. Desativada: cada rastro pesa como se estivesse no plano (β = 0, peso com cos²φ), como até a versão 1.6. *Verificação:* em um percurso de 1000 km, sem β o melhor azimute do radiante fica a 15°–90° do percurso conforme a elevação do radiante (30° com o radiante a 30°, perpendicular ao percurso com o radiante a 60°), e o radiante perpendicular vale 67 % a 30° de elevação; com β o melhor radiante fica sempre ao longo do percurso e o perpendicular desce para 15 %. Com β perde-se a regra da melhor direção de SM6FHZ / DH9GCD; β continua sendo uma opção, ativada por padrão porque dá os valores mais prudentes, e desativá-la restaura a regra.

O número de meteoros que chega a um ponto é proporcional ao seno da elevação do radiante nesse ponto (ŝ·û_P), a mesma correção que a IMO usa para o ZHR.

**Opção "Rastros mais longos com radiante baixo (DJ5HG)"** (caixa acima do gráfico, desativada por padrão, com tooltip): DJ5HG nota que com o radiante baixo caem menos meteoros por km², mas os rastros são mais longos (até 100 km úteis) e cumprem mais vezes a lei de reflexão. Com a opção ativada o peso passa a ser min(sin El, 15/100): a espessura útil da camada, 15 km, dividida pelo seno da elevação dá o comprimento do rastro, limitado a 100 km. Acima de cerca de 9° os dois efeitos anulam-se. Desativada, o cálculo continua prudente.

**Configuração do cálculo** (mesma linha, botões de opção): **Prudente** (padrão, os valores mais prudentes: altitude dos rastros do radar, rastros normais, β ativado), **Como DJ5HG** (102 km, rastros mais longos, β) e **Personalizada**, selecionada automaticamente quando você altera manualmente a altitude, a caixa *do radar*, a opção dos rastros mais longos ou β.

**3. Soma e porcentagem.** Pontos a cada 15 km à altitude dos rastros, só onde ambas as estações os veem acima da elevação do lóbulo (*escolha*). 100 % é a posição do radiante mais favorável para esse percurso:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F é calculado uma vez por percurso em uma grade de direções (azimute a cada 5°, elevação a cada 2,5°) e interpolado.

**Eficiência em dB (referência DJ5HG).** A porcentagem é relativa apenas à melhor posição do radiante para esse percurso. Para comparar percursos diferentes, o programa dá também a eficiência em dB em relação à referência fixa de DJ5HG: 0 dB é o máximo de um percurso norte–sul de 1000 km que atravessa o equador, com o radiante no equador celeste no equinócio, calculado com a mesma altitude e os mesmos pesos. DJ5HG indica os seus valores como melhores do que 6 dB.

**4. Lado e índice.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

A letra na tabela é o lado com a fração maior. *Escolhas do programa (eq. 32–33 do manual).*

## Comparação com DH9GCD

As fontes primárias para a melhor direção são Eshleman & Mlodnosky e Meeks & James (Proc. IRE, 1957), Hines (1955) e a sua verificação experimental por Forsyth, Hines & Vogan (1955): só são úteis os radiantes no semicírculo de céu perpendicular à bissetriz do ângulo de difusão, o número de rastros cresce com sin El e, perto do ponto médio, os rastros úteis caem a cerca de H·tan El para o lado, no lado oposto ao radiante. DJ5HG acrescenta uma reserva: com um radiante **baixo** mesmo ao longo do percurso, a fórmula de McKinley dá sinais fortes (Hamburgo–Narvik, Quadrântidas, por volta das 19 UTC), portanto "radiante alinhado com o percurso = quase zero" só vale para um radiante alto; o programa continua prudente e mostra o aviso *RADIANTE BAIXO AO LONGO DO PERCURSO*.

Uma verificação independente: a fórmula da melhor direção de **DH9GCD**, citada por **DF5HC** (conferência DARC, janeiro de 2018) – não tem fonte primária publicada –, com El e Az a elevação e o azimute do radiante vistos da sua estação e P o azimute do correspondente:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

É máxima com o radiante a 45° e de lado em relação ao percurso. DF5HC considera o radiante baixo demais abaixo de 20° e **alto demais acima de 70°**: essas horas levam ↑ na tabela e um aviso na [Abóbada celeste](Sky-View-pt-BR#avisos). A fórmula ignora a distância e as altitudes, mas é uma boa referência.

## Verificações

| Verificação | Resultado |
|---|---|
| Regra de SM6FHZ (VUSHF 2025): melhor percurso ortogonal ao azimute do radiante, apontamento = az do radiante ±90°, tolerância ±40–50° | Reproduzida pelo modelo; com o radiante alinhado com o percurso e alto no céu a eficiência é quase nula |
| QTFGUI de DJ5HG, Hamburgo JO53IM – Barcelona, Quadrântidas, 4 de janeiro (exemplo do seu manual) | QTFGUI: 07:00 apontamento 252°, −8 dB; 08:00 nenhuma zona de reflexão; 09:00 apontamento 168°, −4 dB. YA-MS (altitude 102 km como o QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Os três métodos veem o buraco das 08:00, com o radiante quase no zênite |
| Curvas de DJ5HG (*Die Geometrie…*, Bild 8–9: a partir de Hamburgo e Munique, Quadrântidas, 4 de janeiro; lidas do gráfico, cerca de ±0,5 dB e ±15 min) contra o teste automático `--prova-dj5hg` (um valor por hora) | Horários: o buraco com o radiante perto do zênite cai às mesmas horas (Barcelona 07:30–08:30 contra 07–09; Sófia 06:36–07:48 contra 07–08; Narvik 07–08:30 contra 07–09); Moscou está fechado das 03 às 10 em ambos, aberto a partir de Hamburgo até por volta das 02:30 e a partir de Munique até por volta das 00:30, como escreve DJ5HG. Rumos: 2–10° de diferença. Níveis e forma a 102 km (diferença média e RMS em relação às curvas): sem β nem rastros mais longos −1,6 / 4,0 dB; rastros mais longos +1,1 / 4,6 dB; β −5,4 / 6,2 dB, mas com a melhor forma (3,0 dB retirada a média, contra 3,6): surgem os mínimos profundos com radiante baixo (Barcelona −15,6 dB às 17 contra −16 dB às 19:36; Sófia −18,5 dB às 20 contra −14 dB). β e rastros mais longos (*Como DJ5HG*) −2,2 / 4,7 dB; a configuração prudente (altitude do radar 89,5 km, β ativado, sem rastros mais longos) −6,9 / 7,6 dB, forma 3,3 dB. Sem β o YA-MS mal mostra o mínimo com o radiante baixo e quase alinhado com o percurso (−8,6 e −10,4 dB): é a reserva do próprio DJ5HG, daí o aviso |
| Amostragem a cada 5 km em vez de 15 km | as porcentagens mudam menos de 0,3 pontos |

> A documentação do MS-Soft 5.2 define a eficiência de OH5IY como um índice relativo apenas para rastros subdensos, com dois fatores (elevação do radiante, melhor cerca de 45°, e ângulo com o percurso, melhor 90°) e um mínimo elevado manualmente para 20 % para os rastros sobredensos; a fórmula não está publicada. O MCG_MS calcula-a para quatro direções fixas e, com o locator do DX, para o percurso real. O modelo considera apenas rastros subdensos, com antenas isotrópicas; as rajadas sobredensas e o fundo esporádico não entram na eficiência (o fundo esporádico é representado pelo fluxo radar).
