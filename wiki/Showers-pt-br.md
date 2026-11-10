[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · **Português (Brasil)** · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-tw)

# Chuvas

*Aba: Chuvas.*

[![Chuvas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

O catálogo de chuvas usado por todos os cálculos: **45 chuvas** do **IMO Meteor Shower Calendar 2026 e 2027** (tabelas 5 e 7) mais a **Fonte Anti-helion** (tabela 6), cada uma com o seu **próximo máximo**.

## Colunas

| Coluna | Significado |
|---|---|
| Sigla | Código IMO (QUA, PER, GEM, …) |
| Chuva | Nome |
| Atividade | Período de atividade (dia/mês – dia/mês) |
| λ max | Longitude solar do máximo (J2000), da IMO |
| **Próximo máximo (UTC)** | Data e hora do próximo máximo (veja abaixo) |
| **Fonte do máximo** | *IMO 2026* / *IMO 2027* = data e hora publicadas pela IMO; *IMO 2026 (dia)* = a IMO dá apenas o dia, a hora mostrada é calculada (*~hh:mm calc.*); *calculado a partir de λ* = não há valor IMO para esse ano |
| A.R., Decl. | Radiante no máximo (*móvel* para a Fonte Anti-helion) |
| v km/s, r | Velocidade geocêntrica e índice de população |
| ZHR | ZHR no máximo (*var.* = variável) |
| Tipo | *visual* ou *rádio, diurna* |

As chuvas **ativas hoje (UTC)** aparecem destacadas com um véu amarelo e texto em negrito.

## Próximo máximo

O programa mostra sempre o **próximo** máximo. Quando a IMO publicou o calendário desse ano, usa a **data e hora IMO** de `data/massimi_imo.csv` (2026 e 2027 estão incluídos); caso contrário calcula o instante em que o Sol atinge a longitude solar do máximo (Meeus, *Astronomical Algorithms*, cap. 25, resolvido pelo método de Newton).

**Verificação:** o cálculo concorda com os calendários IMO 2026 e 2027 dentro de poucos minutos onde a IMO dá a hora (p. ex. Quadrântidas 3/1/2026 21:13 contra 21:00; Geminídeas 14/12/2027 19:51 contra 20:00). Exceções: kappa-Leônidas diurnas 2026 um dia mais tarde (26/9 em vez de 25/9) e a hora das eta-Aquáridas 2027 (15:10 contra 09:00 da IMO) – nestes casos é usado o valor IMO.

**Acrescentar um ano:** quando a IMO publicar um novo calendário, acrescente as suas linhas a `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, hora vazia se a IMO der apenas o dia). Até lá o máximo é calculado.

## Chuvas menores e diurnas

O catálogo inclui as **chuvas menores** da lista IMO – por exemplo as Camelopardálidas de outubro (OCT, ZHR 5, ativas de 5 a 6 de outubro), as Andromédidas, as gama-Ursae Minóridas – e as **chuvas rádio diurnas** de abril a outubro (Piscídeas de abril diurnas, Arietídeas diurnas, zeta-Perseidas diurnas, beta-Táuridas diurnas, kappa-Leônidas diurnas, Sextântidas diurnas, …). Mesmo com ZHR pequenos contribuem para o [índice do percurso](Efficiency-Calculation-pt-br#o-modelo) e para o [Hot recomendado](Sky-View-pt-br#hot-recomendado). Para as chuvas rádio diurnas a IMO não dá ZHR: quando nenhum é indicado, o programa usa um valor de trabalho de 5.

## Perfil de atividade e deslocamento do radiante

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 e λ_max vêm do calendário IMO; as inclinações B (diferentes antes e depois do máximo) e os deslocamentos diários dα/dλ, dδ/dλ são **valores de trabalho** escritos em `data/sciami.csv` (a tabela de deslocamentos da IMO ainda não foi incorporada). *Eq. 9 e 13 do manual.* A posição da Fonte Anti-helion é interpolada linearmente entre as datas da tabela 6 da IMO (`data/ant_radiante.csv`; ativa de 10 de dezembro a 20 de setembro, ZHR cerca de 4).

## Editar o catálogo

`data/sciami.csv` é um arquivo de texto simples (separador `;`) que você pode editar: código, nome, início e fim (MM-DD), λ max, A.R., Decl., deslocamentos, v, r, ZHR, B antes/depois, tipo (V visual, R rádio diurna). Se uma linha estiver errada, o programa mostra uma mensagem na inicialização e ignora-a.

Fontes: International Meteor Organization – Meteor Shower Calendar 2026 e 2027, [www.imo.net](https://www.imo.net) (tabelas 5, 6 e 7); Rossano IZ5TEK (scattertek).
