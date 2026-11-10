[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · **Português** · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Separador: Em direto e dados em tempo real › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## O que é o GRAVES

O **GRAVES** é um radar francês que transmite **CW em 143,050 MHz** a partir de **Broye-lès-Pesmes** (47,348° N 5,515° E, locator **JN27SI**, cerca de 200 m de altitude; Wikipedia). Os rastos meteóricos na zona que tanto o GRAVES como a sua estação veem refletem o sinal até si por **forward scatter**: ouvem-se *pings* curtos perto da portadora. É assim que os observadores **RMOB** em 143,050 MHz contam os meteoros hora a hora, e é um sinal de teste gratuito e sempre ativo para a sua estação de meteor scatter nos 2 m.

O separador trata **GRAVES → si** como um percurso de meteor scatter próprio: com as mesmas funções do percurso principal (mesma altitude dos rastos, elevação do lóbulo e distância dos hot spots) calcula a eficiência das chuvas, o Hot recomendado e as zonas PREV, e depois verifica se essa zona está **dentro do feixe do GRAVES** e **quando** o feixe a ilumina.

## Barra superior

| Comando | O que faz |
|---|---|
| **Agora** | Repõe a hora da abóbada celeste no tempo real (o separador segue o controlo *Hora da abóbada celeste*). |
| **Pôr o GRAVES como DX** | O correspondente passa a ser o GRAVES (JN27SI, altitude 200 m) e o percurso principal é recalculado: todos os outros separadores mostram então o percurso do GRAVES. |
| **Sequência do feixe** | *0,8 s por passo · ciclo de 4,8 s (PE1ITR 2021)* (por omissão) ou *3,2 s por passo · ciclo de 19,2 s (PE1ITR 2007)*. |

## Os quatro cartões

| Cartão | Conteúdo |
|---|---|
| **ZONA ÚTIL NO FEIXE DO GRAVES** | *Sim · setor X* com o azimute e a elevação do hot spot recomendado vistos do GRAVES e o passo (1–6); ou *Não: fora dos setores* / *Não: abaixo do horizonte do GRAVES* / *Não: acima do feixe (cerca de 25°)* |
| **EFICIÊNCIA DO PERCURSO GRAVES → SI AGORA** | Índice do percurso Σ ZHR × eficiência, melhor chuva, lado predominante A/B e *ecos esperados ≈ …/hora* (experimental, ver abaixo) |
| **PERCURSO** | Distância ao GRAVES; antena em direção ao Hot recomendado (azimute e elevação); azimute direto do GRAVES |
| **PRÓXIMA PASSAGEM DO FEIXE SOBRE A ZONA** | *agora · faltam … s* ou *dentro de … s*, o passo (p. ex. *B4*), as três horas seguintes (segundos dentro do minuto) e a fração de rastos captados |

Se nesse momento nenhuma chuva for útil, o programa mostra o hot spot **mais adequado ao feixe** (dentro dos setores, o mais próximo do sul) e indica-o.

## O céu visto pelo GRAVES

Segundo PE1ITR e a wiki do Bolidozor, **quatro agrupamentos em fase** cobrem o céu a sul de **90° a 270°** de azimute em quatro **setores de 45°**:

| Setor | Azimute a partir do GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Cada setor está dividido em **6 passos de 7,5°**, numerados de 1 a 6 a partir do azimute mais baixo, iluminados um após o outro, **no mesmo instante em todos os quatro setores**. O feixe tem cerca de **25° de largura em elevação**: à altitude dos rastos cobre a coroa colorida entre os dois círculos tracejados (*horizonte do feixe*). No desenho: pontos laranja/rosa = zonas PREV do percurso GRAVES → si, linha verde = direção da sua estação, linha vermelha = da sua estação até ao hot spot recomendado; o passo iluminado nesse instante é realçado.

## Reconstrução cronológica

*RECONSTRUÇÃO CRONOLÓGICA · data UTC* (o mesmo dia da tabela de 24 h): para cada hora, a eficiência do percurso GRAVES → si, a chuva mais favorável e a janela útil (*hh:00 → hh:00 UTC · n h*), com o máximo (*máx Σ … às hh:30*) e um marcador vermelho de *agora*. Por baixo, o **detalhe dos segundos seguintes**: os seis passos do setor, o passo que ilumina a zona útil e *eco possível (+0,3 s de rasto)*.

### Temporização do feixe

A sequência está ligada à hora **UTC** (PE1ITR): o passo iluminado agora é calculado a partir dos segundos desde as 00:00 UTC módulo o ciclo (86 400 s é múltiplo tanto de 4,8 s como de 19,2 s). A estação de comando por vezes desloca a sequência alguns passos, por isso o detalhe é uma **previsão a confirmar à escuta**. A etiqueta amarela **relógio do PC sincronizado** lembra-o: sincronize o seu PC com um servidor NTP (erro de algumas décimas de segundo, no máximo).

### Fator de deteção

Um rasto só se ouve se o feixe o iluminar enquanto dura:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s é uma duração típica de um rasto subdenso a 143 MHz: um valor fixo, *escolha do programa* (a regra λ² de SM6FHZ transpõe as durações entre bandas, mas não dá um valor de partida).

### Ecos esperados (experimental)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

A previsão de [Previsões experimentais](Experimental-Forecasts-pt) (que já inclui o fator de estação K) é transposta da sua frequência f_fc para 143,050 MHz com a regra de SM6FHZ (mesmo expoente k), corrigida pela razão entre os índices de chuvas dos dois percursos (a constante 10 representa o fundo esporádico, como na previsão) e multiplicada pelo fator de deteção. Apenas indicativo: compare com os observadores RMOB.

## Como ouvir os pings do GRAVES

| Passo | O que fazer |
|---|---|
| Recetor | **USB em 143,049 MHz** (tom de cerca de 1 kHz) ou 143,050 MHz, **AGC lento ou desligado**, largura de banda de áudio de **pelo menos 2,4 kHz** |
| Antena | Em direção ao **hot spot recomendado** do percurso GRAVES → si (cartão *PERCURSO*), com **elevação baixa** |
| Waterfall | Os pings são **traços curtos perto da portadora**; os rastos longos (sobredensos) são mais largos e mostram Doppler |
| Contagem | O RMOB usa o GRAVES para as contagens horárias de meteoros: **compare os seus pings com os observadores em 143,050 MHz** ([Previsões experimentais](Experimental-Forecasts-pt#comparação-com-o-rmob)) |

## Fontes

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) e *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki do **Bolidozor**, "Graves" – agrupamentos, setores e tempos do feixe
3. **Wikipedia**, "GRAVES (system)" – transmissor em Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observadores em 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** de IC8TEM – separador Radar GRAVES (o esboço do qual deriva este separador)
