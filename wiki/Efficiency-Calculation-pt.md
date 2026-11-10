[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · **Português** · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

A mesma lei está na base do QTFGUI de DJ5HG (cone scattering). A condição é aceite com uma tolerância gaussiana σ = 0,05 rad (cerca de 3°) – *escolha do programa*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Peso de cada ponto.** Potência de um rasto subdenso (McKinley), φ = metade do ângulo de dispersão (limitado a 85°, *escolha*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

O número de meteoros que chega a um ponto é proporcional ao seno da elevação do radiante nesse ponto (ŝ·û_P), a mesma correção que a IMO usa para o ZHR.

**3. Soma e percentagem.** Pontos a cada 15 km à altitude dos rastos, só onde ambas as estações os veem acima da elevação do lóbulo (*escolha*). 100 % é a posição do radiante mais favorável para esse percurso:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F é calculado uma vez por percurso numa grelha de direções (azimute a cada 5°, elevação a cada 2,5°) e interpolado.

**4. Lado e índice.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

A letra na tabela é o lado com a fração maior. *Escolhas do programa (eq. 32–33 do manual).*

## Comparação com DH9GCD

Uma verificação independente: a fórmula da melhor direção de **DH9GCD**, citada por **DF5HC** (conferência DARC, janeiro de 2018), com El e Az a elevação e o azimute do radiante vistos da sua estação e P o azimute do correspondente:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

É máxima com o radiante a 45° e de lado em relação ao percurso. DF5HC considera o radiante demasiado baixo abaixo de 20° e **demasiado alto acima de 70°**: essas horas levam ↑ na tabela e um aviso na [Abóbada celeste](Sky-View-pt#avisos). A fórmula ignora a distância e as altitudes, mas é uma boa referência.

## Verificações

| Verificação | Resultado |
|---|---|
| Regra de SM6FHZ (VUSHF 2025): melhor percurso ortogonal ao azimute do radiante, apontamento = az do radiante ±90°, tolerância ±40–50° | Reproduzida pelo modelo; com o radiante alinhado com o percurso e alto no céu a eficiência é quase nula |
| QTFGUI de DJ5HG, Hamburgo JO53IM – Barcelona, Quadrântidas, 4 de janeiro (exemplo do seu manual) | QTFGUI: 07:00 apontamento 252°, −8 dB; 08:00 nenhuma zona de reflexão; 09:00 apontamento 168°, −4 dB. YA-MS (altitude 102 km como o QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Os três métodos veem o buraco das 08:00, com o radiante quase no zénite |
| Amostragem a cada 5 km em vez de 15 km | as percentagens mudam menos de 0,3 pontos |

> A escala usada por OH5IY e pelo MCG_MS não é conhecida em pormenor (os manuais do MS-Soft não estão disponíveis): compare as percentagens com esses programas antes de as considerar equivalentes. O modelo considera apenas rastos subdensos, com antenas isotrópicas; as rajadas sobredensas e o fundo esporádico não entram na eficiência (o fundo esporádico é representado pelo fluxo radar).
