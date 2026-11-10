[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · **Português** · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [ไทย](Home-th) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – previsões de meteor scatter e eficiência das chuvas em direto

*por Costantino Cerrotta IC8TEM*

O **YA-MS** é um programa gratuito para radioamadores que trabalham em **meteor scatter (MS) nos 50, 70, 144, 222 e 432 MHz**. Para o percurso real entre o seu locator e o do correspondente, calcula hora a hora quanto cada chuva de meteoros ativa ajuda esse percurso (a sua **eficiência**), de que lado do percurso chegam as reflexões (**Hot A / Hot B**), para onde apontar a antena e uma previsão experimental das reflexões por hora obtida de um **radar meteórico em direto** (Collm, Alemanha). Funciona em **Windows, Linux e macOS** (.NET 8 + Avalonia), com 6 idiomas de interface.

A fonte principal é o artigo de **C. Cerrotta IC8TEM e G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versão 7). Cada fórmula e cada dado do programa cita a sua fonte; ver [Fontes](Sources-pt).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Abóbada celeste"></a><br><sub>Abóbada celeste</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Cálculo da eficiência"></a><br><sub>Cálculo da eficiência</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Para quem é

- Operadores que querem saber **quando** um percurso de meteor scatter está aberto e **para onde** apontar, para além do genérico "esta noite é o máximo da chuva".
- Estações que trabalham **percursos longos nos 144 e 432 MHz**, onde a posição do radiante decide se uma chuva é útil ou inútil.
- Quem quiser **verificar os números**: o manual de cálculo e a explicação integrada no programa apresentam cada passo com a sua origem: uma fonte publicada, uma verificação feita no programa ou uma escolha do programa.

## Os separadores

Desde a versão 1.6 os separadores principais têm **subseparadores** (uma fila mais clara por baixo da principal). No arranque, um ecrã de abertura de 5 segundos mostra as Perseidas sobre o VLT do ESO (foto ESO/S. Guisard, CC BY 4.0).

| Separador | Subseparador | O que mostra |
|---|---|---|
| **Em direto e dados em tempo real** | [Tráfego em direto](Live-Traffic-pt) | Mapa azimutal de todo o tráfego MS recolhido, com uma nuvem dos rastos mais prováveis para cada contacto, cores por banda e spots novos a piscar |
| | [Fluxo radar](Radar-Flux-pt) | Contagens horárias de meteoros e altitudes dos rastos lidas do radar SKiYMET de Collm, imagem de Sodankylä, estimativa na sua banda |
| | [Radar GRAVES](GRAVES-Radar-pt) | O percurso de forward scatter GRAVES → si: zona útil no feixe, setor e passo, próxima passagem do feixe, como escutar |
| | [Recolha de dados](Data-Collection-pt) | Três fluxos de cluster telnet (DX cluster, RBN, DM4X/PSKReporter) e o filtro dos spots MS |
| **Cálculo de previsão** | [Cálculo de previsão](Sky-View-pt) | Mapa em planta do percurso com Hot A / Hot B, lóbulo da antena, zonas PREV e deslocação das chuvas; lista de chuvas; pequena abóbada celeste com os radiantes e as direções de antena certas; secção vista a partir da antena |
| | [Geometria e atenuação](Geometry-and-Path-Loss-pt) | Distância, ponto médio, elevação, Hot A / Hot B, limites da zona comum, atenuação do percurso 28–432 MHz, balanço da ligação, antena |
| | [Cálculo da eficiência](Efficiency-Calculation-pt) | Cartões de resumo, eficiência horária de cada chuva com lado A/B, índice do percurso, comparação com DH9GCD, gráfico |
| | [Previsões experimentais](Experimental-Forecasts-pt) | Fluxo de Collm transposto para 144 MHz (ou qualquer frequência) com λ^k e fator de estação K, previsão a 24 horas, comparação com o RMOB |
| **Documentos técnicos** | [Fontes](Sources-pt) | Todas as fontes; a principal é o artigo Cerrotta–Sartori |
| | [Mapa dos radares europeus](European-Radar-Map-pt) | Onde estão Collm, Sodankylä, GRAVES e CMOR em relação à sua estação |
| | [Eficiência - explicação](Efficiency-Explanation-pt) | Documento passo a passo sobre o cálculo da eficiência, exportável para Word |
| [Chuvas em direto](Live-Showers-pt) | – | ZHR medidos pela Global Meteor Network e mapas de radiantes do CMOR |
| [Chuvas](Showers-pt) | – | Catálogo IMO com o próximo máximo (data e hora IMO ou calculadas) |
| [Mapa de quadrados](Grid-Square-Map-pt) | – | Quadrados Maidenhead trabalhados e confirmados a partir de um ficheiro ADIF, um separador por banda |

Por cima dos separadores há três filas de comandos (o seu locator, correspondente, banda, antena, altitude dos rastos, hora); ver [Primeiros passos](Getting-Started-pt). O botão **Comandos** recolhe-as; o idioma e o esquema de cores escolhem-se no canto superior direito; ver [Definições e pasta de dados](Settings-and-Data-Folder-pt).

## Em resumo

- **Percurso real, não direções fixas**: a eficiência é calculada para o percurso de círculo máximo entre os dois locators (os programas anteriores usavam quatro direções fixas).
- **Modelo de reflexão especular** (McKinley) em pontos da camada E a cada 15 km, com a altitude dos rastos lida em direto do radar de Collm.
- **Hot A / Hot B** a 150 km de cada lado do ponto médio (ajustável de 30 a 400 km), o recomendado a vermelho, os que já estão dentro do lóbulo da sua antena a cinzento.
- **Radar em direto**: Collm é verificado a cada 5 minutos e só as fontes alteradas são descarregadas de novo; sem ligação o programa continua a funcionar com os últimos dados guardados.
- Previsão **experimental** a 50/144/432 MHz com a regra λ³ de SM6FHZ, comparável com os observadores RMOB.
- Tudo numa única pasta **`data`** ao lado do programa: nada de AppData nem pastas do sistema.

> A eficiência é um modelo experimental (reflexão especular + rastos subdensos). Compare-a com o MCG_MS, o MS-Soft e a sua própria experiência no ar.

## Por onde começar

1. [Instalação](Installation-pt)
2. [Primeiros passos](Getting-Started-pt)
3. [Problemas e perguntas frequentes](Troubleshooting-FAQ-pt) se algo não funcionar.

Transferências: **[Releases](https://github.com/ic8tem/YA-MS/releases)** no GitHub.
