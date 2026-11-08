**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Tráfego em direto

*Separador: Em direto e dados em tempo real › Tráfego em direto.*

[![Tráfego em direto](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## O que mostra

Um **mapa azimutal equidistante** centrado na sua estação (distância ao centro = distância real, ângulo = azimute) com **todo o tráfego de meteor scatter** reunido pela [Recolha de dados](Data-Collection-pt). Para cada contacto o programa desenha:

- o **percurso** entre as duas estações, na cor da sua banda: 28 MHz castanho, 50 MHz verde, 70 MHz ciano, 144 MHz laranja, 222 MHz rosa, 432 MHz violeta;
- as duas **estações** nas extremidades do percurso;
- a **nuvem**: onde se concentram os rastos meteóricos mais prováveis para esse percurso e essa hora.

Os spots com uma estação **fora do mapa** são descartados. Um spot **acabado de chegar** (com não mais de 3 minutos) **pisca durante um minuto**, para que a atividade nova se veja logo.

## Como é calculada a nuvem

Para cada spot o programa constrói o percurso entre os dois locators (a mesma geometria do seu próprio percurso, ver [Geometria e atenuação](Geometry-and-Path-Loss-pt)) e, à hora do spot, soma ponto a ponto da camada E as **contribuições de reflexão especular de cada chuva ativa**, ponderadas com o seu ZHR: o mesmo cálculo das **zonas PREV** da [abóbada celeste](Sky-View-pt). Para cada lado do percurso que reúna pelo menos 15 % do total, a nuvem é uma **elipse**: centro na média ponderada dos pontos, semieixos iguais a 1,5 vezes as raízes quadradas dos valores próprios da sua dispersão, eixo maior segundo o vetor próprio principal. Quando nenhuma chuva contribui (só meteoros esporádicos), as nuvens são os dois **hot spots** clássicos, desenhados a tracejado. As equações completas estão no capítulo 10 do manual de cálculo.

## Comandos

| Comando | Significado |
|---|---|
| **Raio do mapa** | 600–3500 km a partir da sua estação. |
| **Spots a mostrar** | Últimos 15 ou 30 minutos, última hora, últimas 3 horas, últimas 24 horas. |
| **Tabela** | Contactos no mapa, os mais recentes primeiro, na cor da banda; *Nuvem* indica a percentagem de reflexões no lado principal, ou *esporádicos*. |
| **Clique** | Num percurso ou numa linha da tabela: o contacto é realçado e a caixa mostra o locator do centro da nuvem, a sua percentagem, tamanho e eixo. |
