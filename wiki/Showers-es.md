[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · **Español** · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Lluvias

*Pestaña: Lluvias.*

[![Lluvias](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

El catálogo de lluvias que usan todos los cálculos: **45 lluvias** del **IMO Meteor Shower Calendar 2026 y 2027** (tablas 5 y 7) más la **Fuente Antihelio** (tabla 6), cada una con su **próximo máximo**.

## Columnas

| Columna | Significado |
|---|---|
| Código | Código IMO (QUA, PER, GEM, …) |
| Lluvia | Nombre |
| Actividad | Periodo de actividad (día/mes – día/mes) |
| λ max | Longitud solar del máximo (J2000), de la IMO |
| **Próximo máximo (UTC)** | Fecha y hora del próximo máximo (ver abajo) |
| **Fuente del máximo** | *IMO 2026* / *IMO 2027* = fecha y hora publicadas por la IMO; *IMO 2026 (día)* = la IMO da solo el día, la hora mostrada es calculada (*~hh:mm calc.*); *calculado a partir de λ* = no hay valor IMO para ese año |
| A.R., Decl. | Radiante en el máximo (*móvil* para la Fuente Antihelio) |
| v km/s, r | Velocidad geocéntrica e índice de población |
| ZHR | ZHR en el máximo (*var.* = variable) |
| Tipo | *visual* o *radio, diurna* |
| Activa hoy | *sí* cuando la lluvia está activa ahora |

## Próximo máximo

El programa muestra siempre el **próximo** máximo. Cuando la IMO ha publicado el calendario de ese año usa la **fecha y hora IMO** de `data/massimi_imo.csv` (2026 y 2027 están incluidos); si no, calcula el instante en que el Sol alcanza la longitud solar del máximo (Meeus, *Astronomical Algorithms*, cap. 25, resuelto con el método de Newton).

**Verificación:** el cálculo coincide con los calendarios IMO 2026 y 2027 con pocos minutos de diferencia donde la IMO da la hora (p. ej. Cuadrántidas 3/1/2026 21:13 frente a 21:00; Gemínidas 14/12/2027 19:51 frente a 20:00). Excepciones: kappa-Leónidas diurnas 2026 un día más tarde (26/9 en lugar de 25/9) y la hora de las eta-Acuáridas 2027 (15:10 frente a 09:00 de la IMO); en estos casos se usa el valor IMO.

**Añadir un año:** cuando la IMO publique un nuevo calendario, añade sus filas a `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, hora vacía si la IMO da solo el día). Hasta entonces el máximo se calcula.

## Lluvias menores y diurnas

El catálogo incluye las **lluvias menores** de la lista IMO, por ejemplo las Camelopardálidas de octubre (OCT, ZHR 5, activas del 5 al 6 de octubre), las Andromédidas, las gamma-Úrsidas Menores, y las **lluvias radio diurnas** de abril a octubre (Píscidas de abril diurnas, Ariétidas diurnas, zeta-Perseidas diurnas, beta-Táuridas diurnas, kappa-Leónidas diurnas, Sextántidas diurnas, …). Aun con ZHR pequeñas contribuyen al [índice del trayecto](Efficiency-Calculation-es#el-modelo) y al [Hot recomendado](Sky-View-es#hot-recomendado). Para las lluvias radio diurnas la IMO no da ZHR: cuando no se indica ninguna, el programa usa un valor de trabajo de 5.

## Perfil de actividad y desplazamiento del radiante

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 y λ_max proceden del calendario IMO; las pendientes B (distintas antes y después del máximo) y los desplazamientos diarios dα/dλ, dδ/dλ son **valores de trabajo** escritos en `data/sciami.csv` (la tabla de desplazamientos de la IMO aún no se ha introducido). *Ec. 9 y 13 del manual.* La posición de la Fuente Antihelio se interpola linealmente entre las fechas de la tabla 6 de la IMO (`data/ant_radiante.csv`; activa del 10 de diciembre al 20 de septiembre, ZHR de unos 4).

## Editar el catálogo

`data/sciami.csv` es un archivo de texto plano (separador `;`) que puedes editar: código, nombre, inicio y fin (MM-DD), λ max, A.R., Decl., desplazamientos, v, r, ZHR, B antes/después, tipo (V visual, R radio diurna). Si una línea es errónea, el programa muestra un mensaje al arrancar y la ignora.

Fuentes: International Meteor Organization – Meteor Shower Calendar 2026 y 2027, [www.imo.net](https://www.imo.net) (tablas 5, 6 y 7); Philip G0ISW (tasas horarias radio máximas); Rossano IZ5TEK (scattertek).
