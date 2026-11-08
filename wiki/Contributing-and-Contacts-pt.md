**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

# Contribuir e contactos

O YA-MS melhora graças aos relatos de quem o usa no ar. Cada correção é atribuída à sua fonte.

## Contactos

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Comunicar um problema

Abra uma **issue no GitHub** ou escreva um e-mail com:

- sistema operativo e versão do YA-MS (no título da janela);
- os dois locators, a banda e a hora UTC;
- o que esperava e o que viu (uma captura de ecrã ajuda);
- para problemas de radar, a mensagem mostrada no separador [Fluxo radar](Radar-Flux-pt).

## O que é especialmente útil

- **Relatos do ar.** Horas e percursos em que a eficiência ou a previsão acertaram – ou falharam. O modelo é experimental e precisa de ser comparado com QSO reais e com o MCG_MS / MS-Soft.
- **Comparações com o RMOB.** Valores do fator de estação K e do expoente k que obteve com a [comparação com o RMOB](Experimental-Forecasts-pt#comparação-com-o-rmob), com a sua banda e a sua estação.
- **Dados com fonte.** Melhores deslocações dos radiantes, perfis de atividade, novas datas de máximos IMO (`data/massimi_imo.csv`), dados de antenas: indique a fonte e ela será citada.
- **Alterações nos gráficos de radar.** Se o formato do gráfico de Collm mudar, uma cópia da imagem (`data/radar/`) ajuda a recalibrar a leitura.

## Traduções

As traduções da interface são ficheiros de texto simples em **`data/lingue/<code>.txt`** (UTF-8) e **qualquer pessoa as pode corrigir**:

```
<Italian text><TAB><translation>
```

- Uma entrada por linha; as linhas que começam por `#` são comentários.
- Em ambas as colunas os dois caracteres `\n` indicam uma quebra de linha.
- Mantenha os marcadores `{0}`, `{1}`, … com o seu formato (p. ex. `{0:F1}`, `{3:+0;-0}`), pela ordem de que o seu idioma precisar.
- As entradas em falta ou vazias são mostradas em italiano. A lista de todas as chaves é `data/lingue/chiavi.txt` (gerada por `tools/estrai_chiavi.py`, não a edite).

Edite o ficheiro na pasta `data/lingue` da sua instalação e reinicie o YA-MS (ou mude de idioma) para ver o resultado. Como estes ficheiros **são substituídos por versões mais recentes a cada atualização**, **envie também as suas correções** – por e-mail ou como pull request no GitHub (`data/lingue/`) – para que entrem na próxima versão.

Esta wiki existe em English, Русский, Deutsch e 日本語; correções às páginas da wiki também são bem-vindas.
