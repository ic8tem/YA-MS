[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · **Português** · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Explicação do cálculo da eficiência

*Separador: Documentos técnicos › Explicação do cálculo da eficiência.*

[![Explicação do cálculo da eficiência](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Um documento técnico, *"Come YA-MS calcola l'efficienza di uno sciame"* (Como o YA-MS calcula a eficiência de uma chuva), mostrado dentro do programa como uma página clara. Explica **passo a passo** como se obtém a eficiência e indica, para cada passo, **de onde vem**. O programa mostra-o **no idioma da interface** (todos os 36 idiomas), tal como o manual de cálculo; esta wiki apresenta também o seu conteúdo em [Cálculo da eficiência](Efficiency-Calculation-pt#o-modelo) e [Geometria e atenuação](Geometry-and-Path-Loss-pt).

## Etiquetas

Cada passo tem uma etiqueta colorida:

| Etiqueta | Cor | Significado |
|---|---|---|
| **FONTE** (fonte) | azul | o passo retoma uma fonte citada; o número entre parênteses retos remete para a lista no fim |
| **RILIEVO** (verificação) | verde | comparação entre o programa e as fontes, com o resultado |
| **SCELTA** (escolha) | laranja | uma escolha do programa, não tirada de uma fonte: a verificar com a experiência no ar |

## Capítulos

| Capítulo | Conteúdo |
|---|---|
| 1. Introdução | Objetivo, etiquetas, o que significa eficiência (OH5IY, MCG_MS; o YA-MS usa o percurso real) |
| 2. Onde ocorrem as reflexões: a camada E | Rastos a 80–120 km; altitude dos rastos = moda do histograma de Collm (verificação: 89,5 km a 5/11/2026) |
| 3. Geometria do percurso | Terra e ponto médio; elevação da antena (fórmula do artigo); zona comum e os seus limites; Hot A / Hot B; lóbulo da antena (DL6WU, Kraus, W4RNL) |
| 4. O radiante da chuva | Posição do radiante (IMO 2026/2027), data do máximo (IMO ou longitude solar), perfil de atividade |
| 5. Condição de reflexão | Reflexão especular (McKinley), tolerância gaussiana de 0,05 rad, melhor apontamento (SM6FHZ), fórmula de DH9GCD |
| 6. De um ponto à eficiência | Pontos de reflexão a cada 15 km, peso de cada ponto, percentagem; comparação com o QTFGUI (DJ5HG) |
| 7. Leitura dos resultados | Lado A / B, índice do percurso, cores dos radiantes, zonas PREV, corte visto a partir da antena |
| 8. Frequência de trabalho e atenuação | Regras λ³ / λ², do radar à banda de radioamador, referências de atenuação |
| 9. Limites conhecidos | Apenas rastos subdensos, antenas isotrópicas (em azimute; diagrama vertical opcional), valores de trabalho |
| 10. Fontes | 17 fontes numeradas |

## Botões

| Botão | O que faz |
|---|---|
| **Exportar para Word (.docx)...** | Guarda uma cópia de `data/efficienza_spiegazione.docx` onde escolher (nome sugerido *YA-MS - calcolo dell'efficienza.docx*) |
| **Abrir no Word** | Abre o mesmo `.docx` com o programa predefinido para documentos Word (Word, LibreOffice, …) |

## Ficheiros

| Ficheiro | Conteúdo |
|---|---|
| `data/efficienza_spiegazione.txt` | O texto mostrado no separador, um bloco por linha (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | A versão Word |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | O mesmo documento nos outros 35 idiomas (p. ex. `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | O **manual de cálculo** (italiano): todas as equações (editor de equações do Word), numeradas, com as suas fontes |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | O manual de cálculo nos outros 35 idiomas |

Os dois documentos são regenerados a partir do código-fonte com `tools/build_spiegazione.py data [code]` e `node tools/build_manuale.js <file.docx> [code]`. As traduções estão em `tools/traduzioni_doc/` (`tools/build_documenti.sh` regenera todos os idiomas).
