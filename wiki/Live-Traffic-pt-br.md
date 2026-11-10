[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · **Português (Brasil)** · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Tráfego ao vivo

*Aba: Ao vivo e dados em tempo real › Tráfego ao vivo.*

[![Tráfego ao vivo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## O que mostra

Um **mapa azimutal equidistante** centrado na sua estação (distância ao centro = distância real, ângulo = azimute) com **todo o tráfego de meteor scatter** reunido pela [Coleta de dados](Data-Collection-pt-br). Para cada contato o programa desenha:

- o **percurso** entre as duas estações, na cor da sua banda: 28 MHz marrom, 50 MHz verde, 70 MHz ciano, 144 MHz laranja, 222 MHz rosa, 432 MHz violeta;
- as duas **estações** nas extremidades do percurso;
- a **nuvem**: onde se concentram os rastros meteóricos mais prováveis para esse percurso e essa hora.

Os spots com uma estação **fora do mapa** são descartados. Um spot **recém-chegado** (com não mais de 3 minutos) **pisca durante um minuto**, para que a atividade nova seja vista imediatamente.

## Como é calculada a nuvem

Para cada spot o programa constrói o percurso entre os dois locators (a mesma geometria do seu próprio percurso, veja [Geometria e atenuação](Geometry-and-Path-Loss-pt-br)) e, à hora do spot, soma ponto a ponto da camada E as **contribuições de reflexão especular de cada chuva ativa**, ponderadas com o seu ZHR: o mesmo cálculo das **zonas PREV** da [abóbada celeste](Sky-View-pt-br). Para cada lado do percurso que reúna pelo menos 15 % do total, a nuvem é uma **elipse**: centro na média ponderada dos pontos, semieixos iguais a 1,5 vezes as raízes quadradas dos autovalores da sua dispersão, eixo maior ao longo do autovetor principal. Quando nenhuma chuva contribui (só meteoros esporádicos), as nuvens são os dois **hot spots** clássicos, desenhados em tracejado. As equações completas estão no capítulo 10 do manual de cálculo.

## Comandos

| Comando | Significado |
|---|---|
| **Raio do mapa** | 600–3500 km a partir da sua estação. |
| **Spots a mostrar** | Últimos 15 ou 30 minutos, última hora, últimas 3 horas, últimas 24 horas. |
| **Tabela** | Contatos no mapa, os mais recentes primeiro, na cor da banda; *Nuvem* indica a porcentagem de reflexões no lado principal, ou *esporádicos*. |
| **Clique** | Em um percurso ou em uma linha da tabela: o contato é destacado e a caixa mostra o locator do centro da nuvem, a sua porcentagem, tamanho e eixo. |
