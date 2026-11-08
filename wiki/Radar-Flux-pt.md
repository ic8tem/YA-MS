[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · **Português** · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Fluxo radar

*Separador: Em direto e dados em tempo real › Fluxo radar.*

[![Fluxo radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Este separador mostra o que os radares meteóricos profissionais estão a contar **agora**: as contagens horárias de meteoros e as altitudes dos rastos do radar SKiYMET de **Collm** (Universidade de Leipzig / IAP Kühlungsborn, Alemanha, 36,2 MHz) e a última imagem do radar de **Sodankylä** (SGO, Finlândia). As contagens de Collm alimentam a estimativa na sua banda e as [Previsões experimentais](Experimental-Forecasts-pt); a altitude dos rastos medida alimenta toda a geometria.

## Comandos

| Comando | O que faz |
|---|---|
| **Descarregar agora** | Verifica de uma só vez todas as fontes externas. |
| **Atualização automática de todas as fontes a cada 5 minutos** | Ativa por omissão. A cada 5 minutos todas as fontes são verificadas e **só as que mudaram** são descarregadas de novo (*inalterado (verificado às … UTC)* / *novo dado às … UTC*). |
| **Expoente λ (SM6FHZ)** | Expoente k da regra de frequência, por omissão 3 (1–4). |

## O que é mostrado

| Painel | Conteúdo |
|---|---|
| **Meteoros/hora - ontem e hoje (UTC)** | Barras ciano = contagens de Collm (válidas), barras vermelhas = descartadas, linha laranja grossa = *estimativa a … MHz* na escala da direita |
| **Altitudes dos rastos (Collm)** | Meteoros por km de altitude entre 70 e 110 km, com altitude mais frequente (moda), média, mediana e desvio-padrão |
| Imagem de Collm | O gráfico SKiYMET original, tal como é descarregado |
| Imagem de Sodankylä | A última imagem de contagens de meteoros do radar de Sodankylä (apenas mostrada; o seu formato não é lido) |

A linha por cima dos gráficos indica quando o gráfico de Collm foi lido e que escala vertical foi encontrada (*escala lida no gráfico: 0-… meteoros/hora*).

## Como é lido o gráfico de Collm

O gráfico de Collm (720 × 720 píxeis, cores puras) tem os eixos em posições fixas, mas o radar **adapta a escala vertical todos os dias** aos valores medidos (p. ex. 0–1,2·10³ a 5/11/2026 e 0–1,0·10³ a 6/11/2026, com as marcas deslocadas). Por isso o YA-MS:

1. encontra as marcas longas do eixo;
2. **lê as etiquetas** da marca mais alta e do zero comparando cada carácter com a fonte de matriz de pontos do gráfico;
3. para cada hora i (0–47, ontem e hoje) toma a coluna central e o primeiro píxel ciano a partir de cima, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top e y0 são as linhas da marca mais alta e do zero, N_top o valor lido na etiqueta mais alta (×1000). Resolução: cerca de 7–8 meteoros/hora por píxel. *Escolha do programa (eq. 42 do manual).*

Se uma etiqueta não puder ser lida, o programa recorre à calibração de 5/11/2026 (**escala calibrada 0-1200 meteoros/hora**) e indica-o a laranja: *Não consigo ler a escala vertical do fluxo (etiqueta no topo: …): valores a verificar.* Se o próprio formato do gráfico mudar (*Formato do gráfico alterado (…x…): leitura impossível* ou *Eixos do fluxo não encontrados na posição esperada*), a leitura tem de ser recalibrada: por favor, comunique-o (ver [Contribuir](Contributing-and-Contacts-pt)).

### Altitudes dos rastos

A partir do histograma das altitudes (n_k meteoros no km k, altitude média h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Eq. 43 do manual.* Com **do radar** assinalado (fila 2 dos comandos) a **moda** torna-se a altitude dos rastos de todos os cálculos. Verificação: gráfico de 5/11/2026 – moda 89,5 km, média 88,6 km, desvio-padrão 6,8 km, o que confirma os ~90 km do artigo Cerrotta–Sartori (média SKiYMET).

Se a escala do gráfico das altitudes mudar, o programa avisa: *as estatísticas das altitudes (moda, média, mediana) continuam válidas, as contagens absolutas não.*

## Estimativa na sua banda

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Regras experimentais de **SM6FHZ** (VUSHF 2025): o número e a intensidade das reflexões escalam com λ³, a duração com λ²; a dependência de λ³ é a mesma da equação subdensa de McKinley. É também mostrada a duração máxima dos pings segundo a IARU Região 1 (1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz). Os valores são indicativos, a comparar com a experiência no ar. O fator de estação K e a comparação com o RMOB estão em [Previsões experimentais](Experimental-Forecasts-pt).

## Sem ligação

Se nenhuma fonte for alcançável, aparece **uma única vez** uma mensagem: *Sem ligação à Internet. Os dados dos radares e do RMOB não podem ser atualizados: o programa usa os últimos dados guardados e volta a tentar sozinho a cada 5 minutos.* A barra de estado em baixo fica vermelha (*SEM LIGAÇÃO À INTERNET …*) até a ligação voltar (*Ligação restabelecida.*).

## Arquivos e fontes

| Ficheiro (em `data/`) | Conteúdo |
|---|---|
| `flusso_collm.csv` | Arquivo horário do fluxo lido de Collm (as horas já presentes são atualizadas) |
| `quote_collm.csv` | Arquivo das altitudes dos rastos |
| `radar/` | Últimas imagens descarregadas (e ficheiros RMOB) |
| `fonti_radar.csv` | Endereços das fontes de radar, `attivo=1/0` para ativar/desativar cada uma |

| Fonte | Frequência | Notas |
|---|---|---|
| Radar meteórico de Collm, Universidade de Leipzig (LIM) e IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | atualizado de hora a hora ao minuto 10 UTC; fluxo de ontem + hoje, distribuição das altitudes |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | só imagem (radar em renovação, projeto DECC) |
| swan.ms (cópia de Collm) | 36,2 MHz | desativada por omissão; use-a só com autorização de DL1DBC |

> Os dados de radar pertencem às respetivas instituições (Universidade de Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
