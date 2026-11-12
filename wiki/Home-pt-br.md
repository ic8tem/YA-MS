[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · **Português (Brasil)** · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – previsões de meteor scatter e eficiência das chuvas ao vivo

*por Costantino Cerrotta IC8TEM*

O **YA-MS** é um programa gratuito para radioamadores que trabalham em **meteor scatter (MS) nos 50, 70, 144, 222 e 432 MHz**. Para o percurso real entre o seu locator e o do correspondente, calcula hora a hora quanto cada chuva de meteoros ativa ajuda esse percurso (a sua **eficiência**), de que lado do percurso chegam as reflexões (**Hot A / Hot B**), para onde apontar a antena e uma previsão experimental das reflexões por hora obtida de um **radar meteórico ao vivo** (Collm, Alemanha). Funciona em **Windows, Linux, Raspberry Pi e macOS** (.NET 8 + Avalonia), com 36 idiomas de interface.

A fonte principal é o artigo de **C. Cerrotta IC8TEM e G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versão 7). Cada fórmula e cada dado do programa cita a sua fonte; veja [Fontes](Sources-pt-br).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Abóbada celeste"></a><br><sub>Abóbada celeste</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Cálculo da eficiência"></a><br><sub>Cálculo da eficiência</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Para quem é

- Operadores que querem saber **quando** um percurso de meteor scatter está aberto e **para onde** apontar, para além do genérico "esta noite é o máximo da chuva".
- Estações que trabalham **percursos longos nos 144 e 432 MHz**, onde a posição do radiante decide se uma chuva é útil ou inútil.
- Quem quiser **verificar os números**: o manual de cálculo e a explicação integrada no programa apresentam cada passo com a sua origem: uma fonte publicada, uma verificação feita no programa ou uma escolha do programa.

## As abas

Desde a versão 1.6 as abas principais têm **subabas** (uma linha mais clara abaixo da principal). Na inicialização, uma tela de abertura de 5 segundos mostra as Perseidas sobre o VLT do ESO (foto ESO/S. Guisard, CC BY 4.0).

| Aba | Subaba | O que mostra |
|---|---|---|
| **Ao vivo e dados em tempo real** | [Tráfego ao vivo](Live-Traffic-pt-br) | Mapa azimutal de todo o tráfego MS coletado, com uma nuvem dos rastros mais prováveis para cada contato, cores por banda e spots novos piscando |
| | [Fluxo radar](Radar-Flux-pt-br) | Contagens horárias de meteoros e altitudes dos rastros lidas do radar SKiYMET de Collm, imagem de Sodankylä, estimativa na sua banda |
| | [Radar GRAVES](GRAVES-Radar-pt-br) | O percurso de forward scatter GRAVES → você: zona útil no feixe, setor e passo, próxima passagem do feixe, como escutar |
| | [Coleta de dados](Data-Collection-pt-br) | Três fluxos de cluster telnet (DX cluster, RBN, DM4X/PSKReporter) e o filtro dos spots MS |
| **Cálculo de previsão** | [Cálculo de previsão](Sky-View-pt-br) | Mapa em planta do percurso com Hot A / Hot B, lóbulo da antena, zonas PREV e deslocamento das chuvas; lista de chuvas; pequena abóbada celeste com os radiantes e as direções de antena certas; seção vista a partir da antena |
| | [Geometria e atenuação](Geometry-and-Path-Loss-pt-br) | Distância, ponto médio, elevação, Hot A / Hot B, limites da zona comum, atenuação do percurso 28–432 MHz, balanço do enlace, antena |
| | [Cálculo da eficiência](Efficiency-Calculation-pt-br) | Cartões de resumo, eficiência horária de cada chuva com lado A/B, índice do percurso, comparação com DH9GCD, gráfico |
| | [Previsões experimentais](Experimental-Forecasts-pt-br) | Fluxo de Collm transposto para 144 MHz (ou qualquer frequência) com λ^k e fator de estação K, previsão a 24 horas, comparação com o RMOB |
| [Chuvas ao vivo](Live-Showers-pt-br) | – | ZHR medidos pela Global Meteor Network e mapas de radiantes do CMOR |
| [Chuvas](Showers-pt-br) | – | Catálogo IMO com o próximo máximo (data e hora IMO ou calculadas) |
| [Mapa de quadrados](Grid-Square-Map-pt-br) | – | Quadrados Maidenhead trabalhados e confirmados a partir de um arquivo ADIF, uma aba por banda |
| **Documentos técnicos** | [Fontes](Sources-pt-br) | Todas as fontes; a principal é o artigo Cerrotta–Sartori |
| | [Mapa dos radares europeus](European-Radar-Map-pt-br) | Onde estão Collm, Sodankylä, GRAVES e CMOR em relação à sua estação |
| | [Explicação do cálculo da eficiência](Efficiency-Explanation-pt-br) | Documento passo a passo sobre o cálculo da eficiência, exportável para Word |

Acima das abas há três linhas de comandos (o seu locator, correspondente, banda, antena, altitude dos rastros, hora); veja [Primeiros passos](Getting-Started-pt-br). O botão **Comandos** as oculta; o idioma e o esquema de cores são escolhidos no canto superior direito; veja [Configurações e pasta de dados](Settings-and-Data-Folder-pt-br).

## Em resumo

- **Percurso real, não direções fixas**: a eficiência é calculada para o percurso de círculo máximo entre os dois locators (os programas anteriores usavam quatro direções fixas).
- **Modelo de reflexão especular** (McKinley) em pontos da camada E a cada 15 km, com a altitude dos rastros lida ao vivo do radar de Collm.
- **Hot A / Hot B** a 150 km de cada lado do ponto médio (ajustável de 30 a 400 km), o recomendado em vermelho, os que já estão dentro do lóbulo da sua antena em cinza.
- **Radar ao vivo**: Collm é verificado a cada 5 minutos e só as fontes alteradas são baixadas de novo; sem conexão o programa continua funcionando com os últimos dados salvos.
- Previsão **experimental** a 50/144/432 MHz com a regra λ³ de SM6FHZ, comparável com os observadores RMOB.
- Tudo em uma única pasta **`data`** ao lado do programa: nada de AppData nem pastas do sistema.

> A eficiência é um modelo experimental (reflexão especular + rastros subdensos). Compare-a com o MCG_MS, o MS-Soft e a sua própria experiência no ar.

## Por onde começar

1. [Instalação](Installation-pt-br)
2. [Primeiros passos](Getting-Started-pt-br)
3. [Problemas e perguntas frequentes](Troubleshooting-FAQ-pt-br) se algo não funcionar.

Downloads: **[Releases](https://github.com/ic8tem/YA-MS/releases)** no GitHub.
