[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · **Português (Brasil)** · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-TW)

# Fluxo radar

*Aba: Ao vivo e dados em tempo real › Fluxo radar.*

[![Fluxo radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Esta aba mostra o que os radares meteóricos profissionais estão contando **agora**: as contagens horárias de meteoros e as altitudes dos rastros do radar SKiYMET de **Collm** (Universidade de Leipzig / IAP Kühlungsborn, Alemanha, 36,2 MHz) e a última imagem do radar de **Sodankylä** (SGO, Finlândia). As contagens de Collm alimentam a estimativa na sua banda e as [Previsões experimentais](Experimental-Forecasts-pt-BR); a altitude dos rastros medida alimenta toda a geometria.

## Comandos

| Comando | O que faz |
|---|---|
| **Baixar agora** | Verifica de uma só vez todas as fontes externas. |
| **Atualização automática de todas as fontes a cada 5 minutos** | Ativada por padrão. A cada 5 minutos todas as fontes são verificadas e **só as que mudaram** são baixadas de novo (*inalterado (verificado às … UTC)* / *novo dado às … UTC*). |
| **Expoente λ (SM6FHZ)** | Expoente k da regra de frequência, padrão 3 (1–4). |

## O que é mostrado

| Painel | Conteúdo |
|---|---|
| **Meteoros/hora - ontem e hoje (UTC)** | Barras ciano = contagens de Collm (válidas), barras vermelhas = descartadas, linha laranja grossa = *estimativa a … MHz* na escala da direita |
| **Altitudes dos rastros (Collm)** | Meteoros por km de altitude entre 70 e 110 km, com altitude mais frequente (moda), média, mediana e desvio-padrão |
| Imagem de Collm | O gráfico SKiYMET original, tal como é baixado |
| Imagem de Sodankylä | A última imagem de contagens de meteoros do radar de Sodankylä (apenas mostrada; o seu formato não é lido) |

A linha acima dos gráficos indica quando o gráfico de Collm foi lido e que escala vertical foi encontrada (*escala lida no gráfico: 0-… meteoros/hora*).

## Como é lido o gráfico de Collm

O gráfico de Collm (720 × 720 pixels, cores puras) tem os eixos em posições fixas, mas o radar **adapta a escala vertical todos os dias** aos valores medidos (p. ex. 0–1,2·10³ em 5/11/2026 e 0–1,0·10³ em 6/11/2026, com as marcas deslocadas). Por isso o YA-MS:

1. encontra as marcas longas do eixo;
2. **lê as etiquetas** da marca mais alta e do zero comparando cada caractere com a fonte de matriz de pontos do gráfico;
3. para cada hora i (0–47, ontem e hoje) toma a coluna central e o primeiro pixel ciano a partir de cima, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top e y0 são as linhas da marca mais alta e do zero, N_top o valor lido na etiqueta mais alta (×1000). Resolução: cerca de 7–8 meteoros/hora por pixel. *Escolha do programa (eq. 42 do manual).*

Se uma etiqueta não puder ser lida, o programa recorre à calibração de 5/11/2026 (**escala calibrada 0-1200 meteoros/hora**) e avisa em laranja: *Não consigo ler a escala vertical do fluxo (etiqueta no topo: …): valores a verificar.* Se o próprio formato do gráfico mudar (*Formato do gráfico alterado (…x…): leitura impossível* ou *Eixos do fluxo não encontrados na posição esperada*), a leitura precisa ser recalibrada: por favor, informe (veja [Contribuir](Contributing-and-Contacts-pt-BR)).

### Altitudes dos rastros

A partir do histograma das altitudes (n_k meteoros no km k, altitude média h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Eq. 43 do manual.* Com **do radar** marcado (linha 2 dos comandos) a **moda** torna-se a altitude dos rastros de todos os cálculos. Verificação: gráfico de 5/11/2026 – moda 89,5 km, média 88,6 km, desvio-padrão 6,8 km, o que confirma os ~90 km do artigo Cerrotta–Sartori (média SKiYMET).

Se a escala do gráfico das altitudes mudar, o programa avisa: *as estatísticas das altitudes (moda, média, mediana) continuam válidas, as contagens absolutas não.*

## Estimativa na sua banda

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Regras experimentais de **SM6FHZ** (VUSHF 2025): o número e a intensidade das reflexões escalam com λ³, a duração com λ² (em McKinley λ³ é a potência de um rastro; o número de rastros escala aproximadamente com λ^1,5, e em difusão para a frente as durações também crescem com sec²φ: veja [Previsões experimentais](Experimental-Forecasts-pt-BR)). É também mostrada a duração máxima dos pings segundo a IARU Região 1 (1000 ms a 50 MHz, 500 ms a 70 MHz, 100 ms a 144 MHz, 13 ms a 432 MHz). Os valores são indicativos, a serem comparados com a experiência no ar. O fator de estação K e a comparação com o RMOB estão em [Previsões experimentais](Experimental-Forecasts-pt-BR).

## Sem conexão

Se nenhuma fonte for alcançável, aparece **uma única vez** uma mensagem: *Sem conexão com a Internet. Os dados dos radares e do RMOB não podem ser atualizados: o programa usa os últimos dados salvos e tenta novamente sozinho a cada 5 minutos.* A barra de status embaixo fica vermelha (*SEM CONEXÃO COM A INTERNET …*) até a conexão voltar (*Conexão restabelecida.*).

## Arquivos e fontes

| Arquivo (em `data/`) | Conteúdo |
|---|---|
| `flusso_collm.csv` | Arquivo horário do fluxo lido de Collm (as horas já presentes são atualizadas) |
| `quote_collm.csv` | Arquivo das altitudes dos rastros |
| `radar/` | Últimas imagens baixadas (e arquivos RMOB) |
| `fonti_radar.csv` | Endereços das fontes de radar, `attivo=1/0` para ativar/desativar cada uma |

| Fonte | Frequência | Notas |
|---|---|---|
| Radar meteórico de Collm, Universidade de Leipzig (LIM) e IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | atualizado de hora em hora no minuto 10 UTC; fluxo de ontem + hoje, distribuição das altitudes |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | só imagem (radar em renovação, projeto DECC) |
| swan.ms (cópia de Collm) | 36,2 MHz | desativada por padrão; use-a só com autorização de DL1DBC |

> Os dados de radar pertencem às respectivas instituições (Universidade de Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
