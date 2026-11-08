**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Mapa de quadrados

*Separador: Mapa de quadrados.*

[![Mapa de quadrados](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Os quadrados Maidenhead (4 caracteres) que **trabalhou** e **confirmou**, lidos do ficheiro ADIF do seu log, num mapa da Europa – **um subseparador por banda: 50, 70, 144, 222 e 432 MHz**.

## Comandos

| Comando | O que faz |
|---|---|
| **Carregar ficheiro ADIF...** | Lê um ficheiro `.adi` / `.adif`. Um ADIF novo **substitui** os dados anteriores. |
| **Limpar memória** | Apaga todos os quadrados carregados do ADIF (pede confirmação). |
| Rato | **Roda = zoom, arrastar = deslocar, rato sobre um quadrado = QSO** (até seis indicativos com data, *(confirmado)* quando confirmado) |

Depois do carregamento, o estado mostra *… QSO lidos, … quadrados-QSO nas bandas 50-432 MHz, … QSO descartados (outras bandas ou sem quadrado)*. Cada mapa de banda tem a legenda *… quadrados trabalhados, … confirmados*.

| Cor | Significado |
|---|---|
| Laranja | trabalhado |
| Verde | confirmado (QSL ou LoTW) |

## Como é lido o ADIF

- Campos usados: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (especificação ADIF).
- Banda obtida de `BAND`, ou da frequência: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Um quadrado está **confirmado** se pelo menos um QSO nele tiver `QSL_RCVD = Y` ou `LOTW_QSL_RCVD = Y`.
- Os quadrados ficam guardados em `data/adif_quadrati.csv` até carregar outro ficheiro ou premir **Limpar memória**.

O YA-MS **não** se liga ao LoTW: exporte o ADIF do seu programa de log (ou do LoTW) e carregue-o aqui.
