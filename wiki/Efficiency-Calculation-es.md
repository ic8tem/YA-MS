[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · **Español** · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Cálculo de la eficiencia

*Pestaña: Cálculo de previsión › Cálculo de la eficiencia.*

[![Cálculo de la eficiencia](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

La **eficiencia** de una lluvia indica, en porcentaje, cuánto permite la posición de su radiante las reflexiones en **tu** trayecto. El concepto es de Ilkka **OH5IY** (MS-Soft) y lo retoma el artículo Cerrotta–Sartori: el máximo de eficiencia no coincide con el máximo visual (ZHR), porque depende de dónde está el radiante respecto a las dos estaciones. MCG_MS de DL5MCG aplica la misma idea a cuatro direcciones fijas; YA-MS la calcula para el **trayecto real** entre los dos locators.

Esta pestaña la muestra hora por hora para el día elegido en *Día para la tabla 24 h (UTC)* (valores a la media de cada hora).

## Tarjetas de resumen

| Tarjeta | Contenido |
|---|---|
| **MEJOR HORA DEL DÍA** | Hora con el índice del trayecto más alto, el índice y el lado predominante (A/B con su %) |
| **LLUVIA MÁS FAVORABLE** | La lluvia con el mayor ZHR × eficiencia del día, su eficiencia, hora y lado, y el **mejor apuntamiento** (azimut del radiante +90° / −90°) |
| **AHORA** | Índice y lado predominante a esta hora, y el Hot recomendado (solo cuando el día elegido es hoy) |
| **PREVISIÓN EXPERIMENTAL** | Reflexiones/hora esperadas ahora, dentro de 1 h y dentro de 2 h a la frecuencia de la previsión (Collm, reglas SM6FHZ; ver [Previsiones experimentales](Experimental-Forecasts-es)) |

Bajo las tarjetas, una franja explica las letras A y B (ver abajo).

## Gráfico

*Eficiencia horaria para … del … (UTC, valores a la media hora).* Para hasta cinco lluvias: eficiencia % como línea continua y la fórmula de DH9GCD como línea punteada del mismo color; el **índice del trayecto** como barras azules en la escala de la derecha.

## Tabla horaria

Una fila por cada lluvia activa ese día (ordenadas por ZHR), 24 columnas para las horas (UTC):

| Celda | Significado |
|---|---|
| `63A` | eficiencia 63 %, la mayoría de las reflexiones desde el lado **A** |
| `41B` | eficiencia 41 %, lado **B** |
| `3` | eficiencia inferior al 5 %: número sin letra de lado |
| vacía | eficiencia inferior al 1 % |
| `…↑` | el radiante está **por encima de 70°** visto desde tu estación a esa hora (demasiado alto) |
| texto amarillo | eficiencia ≥ 50 % |

- **A** = **izquierda** mirando desde tu estación hacia el corresponsal (zona Hot A); **B** = **derecha** (zona Hot B). Conviene girar la antena **10–30° hacia ese lado** (side-scatter, artículo Cerrotta–Sartori).
- **Filas celestes** (*DH9GCD %*, bajo cada lluvia): la fórmula de DH9GCD, como comparación.
- **Fila Σ**: *Índice trayecto (ZHR×efic.)*.
- **Fila naranja** (*Previsión … MHz (refl./hora)*): la previsión experimental, para las horas en que existe (hoy y parte de mañana).

## El modelo

Todos los pasos están en el [manual de cálculo](Efficiency-Explanation-es) (`doc/YA-MS_manuale_calcoli.docx`, capítulo 5). En resumen:

**1. Reflexión especular.** Una estela envía la señal de A a B solo si es tangente a un elipsoide con A y B en los focos (McKinley 1961). Las estelas de una lluvia son paralelas a la dirección del radiante ŝ (artículo; McKinley). Para cada punto P de la capa E, con los vectores unitarios hacia las estaciones:

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

La misma ley está en la base de QTFGUI de DJ5HG (cone scattering). La condición se acepta con una tolerancia gaussiana σ = 0,05 rad (unos 3°), *decisión del programa*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Peso de cada punto.** Potencia de una estela subdensa (McKinley), φ = mitad del ángulo de dispersión (limitado a 85°, *decisión*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

El número de meteoros que llega a un punto es proporcional al seno de la elevación del radiante en ese punto (ŝ·û_P), la misma corrección que usa la IMO para la ZHR.

**3. Suma y porcentaje.** Puntos cada 15 km a la altura de las estelas, solo donde ambas estaciones los ven por encima de la elevación del lóbulo (*decisión*). El 100 % es la posición del radiante más favorable para ese trayecto:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F se calcula una vez por trayecto sobre una malla de direcciones (azimut cada 5°, elevación cada 2,5°) y se interpola.

**4. Lado e índice.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

La letra de la tabla es el lado con la fracción mayor. *Decisiones del programa (ec. 32–33 del manual).*

## Comparación con DH9GCD

Una verificación independiente: la fórmula de la mejor dirección de **DH9GCD**, citada por **DF5HC** (conferencia DARC, enero de 2018), con El y Az la elevación y el azimut del radiante vistos desde tu estación y P el azimut del corresponsal:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Es máxima con el radiante a 45° y de costado respecto al trayecto. DF5HC considera el radiante demasiado bajo por debajo de 20° y **demasiado alto por encima de 70°**: esas horas llevan ↑ en la tabla y un aviso en la [Bóveda celeste](Sky-View-es#avisos). La fórmula ignora la distancia y las alturas, pero es una buena referencia.

## Verificaciones

| Verificación | Resultado |
|---|---|
| Regla de SM6FHZ (VUSHF 2025): mejor trayecto ortogonal al azimut del radiante, apuntamiento = az del radiante ±90°, tolerancia ±40–50° | Reproducida por el modelo; con el radiante alineado con el trayecto y alto en el cielo, la eficiencia es casi nula |
| QTFGUI de DJ5HG, Hamburgo JO53IM – Barcelona, Cuadrántidas, 4 de enero (ejemplo de su manual) | QTFGUI: 07:00 apuntamiento 252°, −8 dB; 08:00 ninguna zona de reflexión; 09:00 apuntamiento 168°, −4 dB. YA-MS (altura 102 km como QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Los tres métodos ven el hueco de las 08:00, con el radiante casi en el cenit |
| Muestreo cada 5 km en lugar de 15 km | los porcentajes cambian menos de 0,3 puntos |

> La escala usada por OH5IY y MCG_MS no se conoce en detalle (los manuales de MS-Soft no están disponibles): compara los porcentajes con esos programas antes de considerarlos equivalentes. El modelo considera solo estelas subdensas, con antenas isótropas; las ráfagas sobredensas y el fondo esporádico no entran en la eficiencia (el fondo esporádico lo representa el flujo radar).
