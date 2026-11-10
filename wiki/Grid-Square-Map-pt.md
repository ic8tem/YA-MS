[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · **Português** · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh)

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
