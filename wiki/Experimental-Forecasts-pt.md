[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · **Português** · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh)

# Previsões experimentais

*Separador: Cálculo de previsão › Previsões experimentais.*

[![Previsões experimentais](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Este separador converte as contagens de meteoros do **radar de Collm (36,2 MHz)** numa estimativa das **reflexões por hora numa banda de radioamador** (144 MHz por omissão, qualquer frequência de 28 a 1300 MHz), faz a previsão das **próximas 24 horas** para o seu percurso e permite **comparar** a estimativa com um observador **RMOB** – por exemplo um que escuta o GRAVES em 143,050 MHz.

> Tudo aqui é **experimental**: a regra de frequência é uma regra empírica e o fator de estação depende da sua estação. Use os números para comparar horas e dias, e verifique-os no ar.

## Comandos

| Comando | Por omissão | O que faz |
|---|---|---|
| **Frequência de destino MHz** | 144 | Frequência da previsão (28–1300 MHz) |
| **Expoente λ^k** | 3 | Expoente k da regra de frequência (SM6FHZ: 3) |
| **Fator de estação K** | 1 | Tem em conta a estação recetora (potência, antenas); obtém-se por comparação com um observador RMOB na mesma banda |
| **Carregar ficheiro RMOB do disco...** | | Lê um ficheiro de texto mensal do RMOB (ver abaixo) |
| **Obter o expoente do ficheiro RMOB** | | Ajusta k a partir das horas em comum entre Collm e RMOB |
| **Observador RMOB** | vazio | Nome do observador tal como aparece no nome do ficheiro (p. ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Descarregar RMOB agora** | | Descarrega uma vez o ficheiro do mês corrente desse observador |
| **obtenção automática a cada 5 minutos (ativar só com autorização do RMOB)** | **desativada** | Ver [RMOB e os programas automáticos](#rmob-e-os-programas-automáticos) |

A linha laranja por baixo dos comandos mostra a regra com os números atuais, p. ex. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, a transposição da duração e o ping máximo IARU nessa frequência.

## Do radar à banda de radioamador

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Fonte:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maio de 2025 – o número e a intensidade das reflexões escalam com **λ³**, a duração com **λ²** (os 432 MHz estão 14–15 dB abaixo dos 144 MHz e duram 1/9). **Verificação:** a dependência de λ³ é a mesma da equação subdensa de McKinley. Com k = 3, 1000 meteoros/hora em Collm tornam-se cerca de **16 reflexões/hora a 144 MHz**; os observadores RMOB do GRAVES em 143,050 MHz contam normalmente **de 20 a 140 ecos/hora** (boletim RMOB, junho de 2018): a ordem de grandeza é compatível, e a diferença é o fator de estação K. (Eq. 44–45 do manual.)

## Próximas 24 horas

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistência:** o valor transposto da mesma hora do dia anterior (ou de dois dias antes, se faltar), corrigido pela variação do **índice de chuvas do percurso** I (Σ ZHR × eficiência, ver [Cálculo da eficiência](Efficiency-Calculation-pt#o-modelo)). A constante 10 representa o fundo esporádico e limita a correção quando o índice é pequeno. *Escolha do programa (eq. 47 do manual).*

| Painel | Conteúdo |
|---|---|
| **Medido em Collm e transposto para f MHz - ontem e hoje (UTC)** | Meteoros/hora do radar de Collm; valores transpostos (laranja, escala da direita); as contagens RMOB se carregadas (verde, escala da direita) |
| **Previsão experimental das próximas 24 horas a f MHz para …** | Reflexões/hora previstas (barras) e o índice de chuvas do percurso (escala da direita) |
| Tabela | Hora UTC · Collm mesma hora · Transposto · Índice de chuvas do percurso · Previsão /hora · **Avaliação** |

**Avaliação:** *bom* quando a previsão é pelo menos 1,3 × a média das 24 horas, *médio* a partir de 0,8 ×, *fraco* abaixo disso. A mesma previsão aparece no cartão **PREVISÃO EXPERIMENTAL** e na linha laranja do [Cálculo da eficiência](Efficiency-Calculation-pt), e é a base dos ecos esperados no separador [Radar GRAVES](GRAVES-Radar-pt#ecos-esperados-experimental).

## Comparação com o RMOB

O [RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) reúne as contagens horárias de meteoros dos radio-observadores; muitos em Itália escutam o GRAVES em 143,050 MHz (Planetário de Veneza, Faenza, Rovereto e outros).

**Leitura dos ficheiros RMOB.** São aceites dois formatos de texto:

| Formato | Aspeto | Notas |
|---|---|---|
| Ficheiro mensal (Colorgramme / Spectrum Lab) | uma linha por dia, `day| n| n| …` com 24 valores horários | o habitual `NAME_MMYYYYrmob.TXT` |
| Tabela do boletim | cabeçalho ` UT |  1   2   3 …`, linhas `0h|175 166 …` | se o ficheiro contiver vários observadores, são lidos em sequência: use um ficheiro com um só observador |

Mês e ano vêm do nome do ficheiro (`…_MMYYYYrmob…`) ou do cabeçalho; caso contrário é usado o mês atual (e o programa indica-o).

**Ajuste do expoente.** Com K = 1, a partir da mediana das razões RMOB/Collm nas horas comuns (pelo menos 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Escolha do programa (eq. 46 do manual).* A caixa de diálogo mostra as horas comuns, a razão mediana e k; **Sim** aplica k (e define K = 1), **Não** mantém k = 3 – então ajuste K à mão para o valor sugerido na mesma caixa de diálogo.

## RMOB e os programas automáticos

O RMOB pede que **os programas automáticos não descarreguem os seus ficheiros**. Por isso a **descarga automática está desativada** de início e só deve ser ativada **depois de pedir autorização ao RMOB**. Sem ela pode sempre usar **Carregar ficheiro RMOB do disco...** ou premir **Descarregar RMOB agora** quando precisar.

O endereço de descarga é um modelo em `config.ini` (chave `rmob_url`, por omissão `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, onde `{NOME}` é o observador e `{MMAAAA}` mês e ano); os ficheiros descarregados são guardados em `data/radar/`.
