LANGBAR

# Previsões experimentais

*Aba: Cálculo de previsão › Previsões experimentais.*

[![Previsões experimentais](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Esta aba converte as contagens de meteoros do **radar de Collm (36,2 MHz)** em uma estimativa das **reflexões por hora em uma banda de radioamador** (144 MHz por padrão, qualquer frequência de 28 a 1300 MHz), faz a previsão das **próximas 24 horas** para o seu percurso e permite **comparar** a estimativa com um observador **RMOB** – por exemplo, um que escuta o GRAVES em 143,050 MHz.

> Tudo aqui é **experimental**: a regra de frequência é uma regra empírica, e o fator de estação depende da sua estação. Use os números para comparar horas e dias, e confira-os no ar.

## Comandos

| Comando | Padrão | O que faz |
|---|---|---|
| **Frequência de destino MHz** | 144 | Frequência da previsão (28–1300 MHz) |
| **Expoente λ^k** | 3 | Expoente k da regra de frequência (SM6FHZ: 3) |
| **Fator de estação K** | 1 | Leva em conta a estação receptora (potência, antenas); é obtido por comparação com um observador RMOB na mesma banda |
| **Carregar arquivo RMOB do disco...** | | Lê um arquivo de texto mensal do RMOB (veja abaixo) |
| **Obter o expoente do arquivo RMOB** | | Ajusta k a partir das horas em comum entre Collm e RMOB |
| **Observador RMOB** | vazio | Nome do observador tal como aparece no nome do arquivo (p. ex. `NAME_112026rmob.TXT` → `NAME`) |
| **Baixar RMOB agora** | | Baixa uma vez o arquivo do mês corrente desse observador |
| **obtenção automática a cada 5 minutos (ativar só com autorização do RMOB)** | **desativada** | Veja [RMOB e os programas automáticos](#rmob-e-os-programas-automáticos) |

A linha laranja embaixo dos comandos mostra a regra com os números atuais, p. ex. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, a transposição da duração e o ping máximo IARU nessa frequência.

## Do radar à banda de radioamador

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Fonte:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, maio de 2025 – o número e a intensidade das reflexões variam com **λ³**, a duração com **λ²** (432 MHz fica 14–15 dB abaixo de 144 MHz e dura 1/9). **Verificação:** a dependência de λ³ é a mesma da equação subdensa de McKinley. Com k = 3, 1000 meteoros/hora em Collm tornam-se cerca de **16 reflexões/hora em 144 MHz**; os observadores RMOB do GRAVES em 143,050 MHz contam normalmente **de 20 a 140 ecos/hora** (boletim RMOB, junho de 2018): a ordem de grandeza é compatível, e a diferença é o fator de estação K. (Eq. 44–45 do manual.)

## Próximas 24 horas

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistência:** o valor transposto da mesma hora do dia anterior (ou de dois dias antes, se estiver faltando), corrigido pela variação do **índice de chuvas do percurso** I (Σ ZHR × eficiência, veja [Cálculo da eficiência](Efficiency-Calculation-pt-br#o-modelo)). A constante 10 representa o fundo esporádico e limita a correção quando o índice é pequeno. *Escolha do programa (eq. 47 do manual).*

| Painel | Conteúdo |
|---|---|
| **Medido em Collm e transposto para f MHz - ontem e hoje (UTC)** | Meteoros/hora do radar de Collm; valores transpostos (laranja, escala da direita); as contagens RMOB, se carregadas (verde, escala da direita) |
| **Previsão experimental das próximas 24 horas a f MHz para …** | Reflexões/hora previstas (barras) e o índice de chuvas do percurso (escala da direita) |
| Tabela | Hora UTC · Collm mesma hora · Transposto · Índice de chuvas do percurso · Previsão /hora · **Avaliação** |

**Avaliação:** *bom* quando a previsão é de pelo menos 1,3 × a média das 24 horas, *médio* a partir de 0,8 ×, *fraco* abaixo disso. A mesma previsão aparece no cartão **PREVISÃO EXPERIMENTAL** e na linha laranja do [Cálculo da eficiência](Efficiency-Calculation-pt-br), e é a base dos ecos esperados na aba [Radar GRAVES](GRAVES-Radar-pt-br#ecos-esperados-experimental).

## Comparação com o RMOB

O [RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) reúne as contagens horárias de meteoros dos radio-observadores; muitos na Itália escutam o GRAVES em 143,050 MHz (Planetário de Veneza, Faenza, Rovereto e outros).

**Leitura dos arquivos RMOB.** São aceitos dois formatos de texto:

| Formato | Aspecto | Notas |
|---|---|---|
| Arquivo mensal (Colorgramme / Spectrum Lab) | uma linha por dia, `day| n| n| …` com 24 valores horários | o habitual `NAME_MMYYYYrmob.TXT` |
| Tabela do boletim | cabeçalho ` UT |  1   2   3 …`, linhas `0h|175 166 …` | se o arquivo contiver vários observadores, eles são lidos em sequência: use um arquivo com um só observador |

Mês e ano vêm do nome do arquivo (`…_MMYYYYrmob…`) ou do cabeçalho; caso contrário, é usado o mês atual (e o programa avisa).

**Ajuste do expoente.** Com K = 1, a partir da mediana das razões RMOB/Collm nas horas em comum (pelo menos 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Escolha do programa (eq. 46 do manual).* A caixa de diálogo mostra as horas em comum, a razão mediana e k; **Sim** aplica k (e define K = 1), **Não** mantém k = 3 – nesse caso, ajuste K manualmente para o valor sugerido na mesma caixa de diálogo.

## RMOB e os programas automáticos

O RMOB pede que **programas automáticos não baixem os seus arquivos**. Por isso o **download automático vem desativado** e só deve ser ativado **depois de pedir autorização ao RMOB**. Sem ele, você sempre pode usar **Carregar arquivo RMOB do disco...** ou pressionar **Baixar RMOB agora** quando precisar.

O endereço de download é um modelo em `config.ini` (chave `rmob_url`, padrão `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, onde `{NOME}` é o observador e `{MMAAAA}` mês e ano); os arquivos baixados são armazenados em `data/radar/`.
