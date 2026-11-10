[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · **Português (Brasil)** · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh)

# Contribuir e contatos

O YA-MS melhora graças aos relatos de quem o usa no ar. Cada correção é creditada à sua fonte.

## Contatos

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Relatar um problema

Abra uma **issue no GitHub** ou escreva um e-mail com:

- sistema operacional e versão do YA-MS (no título da janela);
- os dois locators, a banda e a hora UTC;
- o que você esperava e o que viu (uma captura de tela ajuda);
- para problemas de radar, a mensagem mostrada na aba [Fluxo radar](Radar-Flux-pt-br).

## O que é especialmente útil

- **Relatos do ar.** Horas e percursos em que a eficiência ou a previsão acertaram – ou erraram. O modelo é experimental e precisa ser comparado com QSOs reais e com o MCG_MS / MS-Soft.
- **Comparações com o RMOB.** Valores do fator de estação K e do expoente k que você obteve com a [comparação com o RMOB](Experimental-Forecasts-pt-br#comparação-com-o-rmob), com a sua banda e a sua estação.
- **Dados com fonte.** Melhores deslocamentos dos radiantes, perfis de atividade, novas datas de máximos IMO (`data/massimi_imo.csv`), dados de antenas: indique a fonte e ela será citada.
- **Mudanças nos gráficos de radar.** Se o formato do gráfico de Collm mudar, uma cópia da imagem (`data/radar/`) ajuda a recalibrar a leitura.

## Traduções

As traduções da interface são arquivos de texto simples em **`data/lingue/<code>.txt`** (UTF-8) e **qualquer pessoa pode corrigi-las**:

```
<Italian text><TAB><translation>
```

- Uma entrada por linha; as linhas que começam com `#` são comentários.
- Nas duas colunas, os dois caracteres `\n` significam uma quebra de linha.
- Mantenha os marcadores `{0}`, `{1}`, … com o seu formato (p. ex. `{0:F1}`, `{3:+0;-0}`), na ordem de que o seu idioma precisar.
- As entradas ausentes ou vazias são mostradas em italiano. A lista de todas as chaves é `data/lingue/chiavi.txt` (gerada por `tools/estrai_chiavi.py`, não a edite).

Edite o arquivo na pasta `data/lingue` da sua instalação e reinicie o YA-MS (ou troque de idioma) para ver o resultado. Como esses arquivos **são substituídos por versões mais recentes a cada atualização**, por favor **envie também as suas correções** – por e-mail ou como pull request no GitHub (`data/lingue/`) – para que entrem na próxima versão.

Esta wiki existe em 36 idiomas (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文 (简体), 中文 (繁體)); correções nas páginas da wiki também são bem-vindas.
