[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · **Español** · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Cálculo de la eficiencia

*Pestaña: Cálculo de previsión › Cálculo de la eficiencia.*

[![Cálculo de la eficiencia](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

La **eficiencia** de una lluvia indica, en porcentaje, cuánto permite la posición de su radiante las reflexiones en **tu** trayecto. El concepto es de Ilkka **OH5IY** (MS-Soft) y lo retoma el artículo Cerrotta–Sartori: el máximo de eficiencia no coincide con el máximo visual (ZHR), porque depende de dónde está el radiante respecto a las dos estaciones. MCG_MS de DL5MCG aplica la misma idea a cuatro direcciones fijas; YA-MS la calcula para el **trayecto real** entre los dos locators.

Esta pestaña la muestra hora por hora para el día elegido en *Fecha del cálculo (UTC)* (valores a la media de cada hora).

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

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

La misma ley está en la base de QTFGUI de DJ5HG y de su texto *"Die Geometrie von Meteorscatterverbindungen"* (2004): la estela dispersa sobre un cono que tiene la estela como eje, y solo un receptor situado en el cono la oye. Para una estela ideal la pared del cono es muy delgada (un radiador de miles de longitudes de onda); el programa acepta la condición con una tolerancia gaussiana σ = 0,05 rad (unos 3°), que representa lo que el cono ideal no ve: la dispersión de los radiantes de las lluvias (0,3–1,4° medidos por GMN), las estelas curvadas por el viento y su longitud finita, *decisión del programa*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Peso de cada punto.** Potencia de una estela subdensa (McKinley; ITU-R P.843, ec. 3), φ = mitad del ángulo de dispersión (limitado a 85°, *decisión*), β = ángulo entre la estela y el plano de propagación A-P-B, p̂ = normal unitaria a ese plano:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opción "Ángulo β entre estela y trayecto (McKinley completo)"** (activada por defecto, ajuste prudente). Activada: las estelas que cruzan el plano de propagación valen 10–15 dB menos que las que están en él, de modo que ninguna estela se sobrestima. Desactivada: cada estela pesa como si estuviera en el plano (β = 0, peso con cos²φ), como hasta la versión 1.6. *Verificación:* en un trayecto de 1000 km, sin β el mejor acimut del radiante está a 15°–90° del trayecto según la elevación del radiante (30° con el radiante a 30°, perpendicular al trayecto con el radiante a 60°), y el radiante perpendicular vale el 67 % a 30° de elevación; con β el mejor radiante está siempre a lo largo del trayecto y el perpendicular baja al 15 %. Con β se pierde la regla de la mejor dirección de SM6FHZ / DH9GCD; β sigue siendo una opción, activada por defecto porque da los valores más prudentes, y al desactivarla vuelve la regla.

El número de meteoros que llega a un punto es proporcional al seno de la elevación del radiante en ese punto (ŝ·û_P), la misma corrección que usa la IMO para la ZHR.

**Opción "Estelas más largas con radiante bajo (DJ5HG)"** (casilla encima del gráfico, desactivada por defecto, con tooltip): DJ5HG observa que con el radiante bajo caen menos meteoros por km², pero las estelas son más largas (hasta 100 km útiles) y cumplen más a menudo la ley de reflexión. Con la opción activada el peso pasa a ser min(sin El, 15/100): el espesor útil de la capa, 15 km, dividido por el seno de la elevación da la longitud de la estela, limitada a 100 km. Por encima de unos 9° los dos efectos se compensan. Desactivada, el cálculo sigue siendo prudente.

**Ajuste del cálculo** (misma fila, botones de opción): **Prudente** (predeterminado, los valores más prudentes: altura de las estelas del radar, estelas normales, β activada), **Como DJ5HG** (102 km, estelas más largas, β) y **Personalizado**, que se selecciona automáticamente cuando cambias a mano la altura, la casilla *del radar*, la opción de estelas más largas o β.

**3. Suma y porcentaje.** Puntos cada 15 km a la altura de las estelas, vistos por ambas estaciones por encima del horizonte y ponderados con el diagrama vertical de las dos antenas (casilla *diagrama de antena*, activada por defecto; desactivada, solo los puntos por encima de la elevación del lóbulo) (*elección*). El 100 % es la posición del radiante más favorable para ese trayecto:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F se calcula una vez por trayecto sobre una malla de direcciones (azimut cada 5°, elevación cada 2,5°) y se interpola.

**Eficiencia en dB (referencia DJ5HG).** El porcentaje es relativo solo a la mejor posición del radiante para ese trayecto. Para comparar trayectos distintos, el programa da también la eficiencia en dB respecto a la referencia fija de DJ5HG: 0 dB es el máximo de un trayecto norte–sur de 1000 km que cruza el ecuador, con el radiante en el ecuador celeste en el equinoccio, calculado con la misma altura y los mismos pesos. DJ5HG da sus valores como mejores que 6 dB.

**4. Lado e índice.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

La letra de la tabla es el lado con la fracción mayor. *Decisiones del programa (ec. 32–33 del manual).*

## Comparación con DH9GCD

Las fuentes primarias para la mejor dirección son Eshleman & Mlodnosky y Meeks & James (Proc. IRE, 1957), Hines (1955) y su verificación experimental por Forsyth, Hines & Vogan (1955): solo son útiles los radiantes en el semicírculo de cielo perpendicular a la bisectriz del ángulo de dispersión, el número de estelas crece con sin El y, cerca del punto medio, las estelas útiles caen a unos H·tan El hacia un lado, en el lado opuesto al radiante. DJ5HG añade una reserva: con un radiante **bajo** justo a lo largo del trayecto, la fórmula de McKinley da señales fuertes (Hamburgo–Narvik, Cuadrántidas, hacia las 19 UTC), así que "radiante alineado con el trayecto = casi cero" solo vale para un radiante alto; el programa sigue siendo prudente y muestra el aviso *RADIANTE BAJO A LO LARGO DEL TRAYECTO*.

Una verificación independiente: la fórmula de la mejor dirección de **DH9GCD**, citada por **DF5HC** (conferencia DARC, enero de 2018) –no tiene fuente primaria publicada–, con El y Az la elevación y el azimut del radiante vistos desde tu estación y P el azimut del corresponsal:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Es máxima con el radiante a 45° y de costado respecto al trayecto. DF5HC considera el radiante demasiado bajo por debajo de 20° y **demasiado alto por encima de 70°**: esas horas llevan ↑ en la tabla y un aviso en la [Bóveda celeste](Sky-View-es#avisos). La fórmula ignora la distancia y las alturas, pero es una buena referencia.

## Verificaciones

| Verificación | Resultado |
|---|---|
| Regla de SM6FHZ (VUSHF 2025): mejor trayecto ortogonal al azimut del radiante, apuntamiento = az del radiante ±90°, tolerancia ±40–50° | Reproducida por el modelo; con el radiante alineado con el trayecto y alto en el cielo, la eficiencia es casi nula |
| QTFGUI de DJ5HG, Hamburgo JO53IM – Barcelona, Cuadrántidas, 4 de enero (ejemplo de su manual) | QTFGUI: 07:00 apuntamiento 252°, −8 dB; 08:00 ninguna zona de reflexión; 09:00 apuntamiento 168°, −4 dB. YA-MS (altura 102 km como QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Los tres métodos ven el hueco de las 08:00, con el radiante casi en el cenit |
| Curvas de DJ5HG (*Die Geometrie…*, Bild 8–9: desde Hamburgo y Múnich, Cuadrántidas, 4 de enero; leídas del gráfico, aprox. ±0,5 dB y ±15 min) frente a la prueba automática `--prova-dj5hg` (un valor por hora) | Horarios: el hueco con el radiante cerca del cenit cae en las mismas horas (Barcelona 07:30–08:30 frente a 07–09; Sofía 06:36–07:48 frente a 07–08; Narvik 07–08:30 frente a 07–09); Moscú está cerrado de 03 a 10 en ambos, abierto desde Hamburgo hasta las 02:30 aprox. y desde Múnich hasta las 00:30 aprox., como escribe DJ5HG. Rumbos: 2–10° de diferencia. Niveles y forma a 102 km (diferencia media y RMS respecto a las curvas): sin β ni estelas más largas −1,6 / 4,0 dB; estelas más largas +1,1 / 4,6 dB; β −5,4 / 6,2 dB, pero con la mejor forma (3,0 dB tras quitar la media, frente a 3,6): aparecen los mínimos profundos con radiante bajo (Barcelona −15,6 dB a las 17 frente a −16 dB a las 19:36; Sofía −18,5 dB a las 20 frente a −14 dB). β y estelas más largas (*Como DJ5HG*) −2,2 / 4,7 dB; el ajuste prudente (altura del radar 89,5 km, β activada, sin estelas más largas) −6,9 / 7,6 dB, forma 3,3 dB. Sin β, YA-MS apenas muestra el mínimo con el radiante bajo y casi alineado con el trayecto (−8,6 y −10,4 dB): es la reserva del propio DJ5HG, de ahí el aviso |
| Muestreo cada 5 km en lugar de 15 km | los porcentajes cambian menos de 0,3 puntos |

> La documentación de MS-Soft 5.2 define la eficiencia de OH5IY como un índice relativo solo para estelas subdensas, con dos factores (elevación del radiante, mejor hacia 45°, y ángulo con el trayecto, mejor a 90°) y un mínimo subido a mano al 20 % para las estelas sobredensas; la fórmula no está publicada. MCG_MS la calcula para cuatro direcciones fijas y, con el locator del DX, para el trayecto real. El modelo considera solo estelas subdensas, con antenas isótropas; las ráfagas sobredensas y el fondo esporádico no entran en la eficiencia (el fondo esporádico lo representa el flujo radar). Desde la 1.8.1, con la casilla «diagrama de antena» activada, se aplica el diagrama vertical de las antenas; en acimut siguen siendo isótropas.
