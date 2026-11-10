[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · **Español** · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Bóveda celeste

*Pestaña: Cálculo de previsión › Cálculo de previsión.*

[![Bóveda celeste](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Esta subpestaña (la bóveda celeste de las versiones anteriores) reúne en una sola pantalla **dónde** están ahora las estelas útiles y **hacia dónde apuntar**. A la izquierda la **vista en planta** del trayecto; a la derecha la lista de lluvias, una pequeña bóveda celeste con los radiantes, el texto del cálculo y la **sección** vista desde tu antena. Todo se refiere a la hora del regulador *Hora de la bóveda celeste* (tiempo real por defecto; ±36 h en pasos de 15 minutos).

En la pequeña bóveda celeste una **línea naranja** que pasa por el cenit da siempre las **direcciones de antena adecuadas**, ortogonales al desplazamiento de la lluvia seleccionada (o de la más favorable): azimut del radiante ±90°, rotulada *antena NNN°* en ambos extremos, con la tolerancia de ±45° como líneas finas. Unas marcas naranjas cortas en el borde indican las direcciones ortogonales de las demás lluvias útiles.

## Vista en planta (izquierda)

Un mapa de Europa visto desde arriba (**E a la derecha**) con una escala de grados alrededor. El rótulo bajo el mapa indica su radio (*Mapa: borde = … km desde la estación*).

| Elemento | Dibujo |
|---|---|
| Trayecto / DX | Línea verde de tu estación al corresponsal (siempre el trayecto real de círculo máximo entre los locators) |
| **Hot A / Hot B** | Puntos a 150 km (ajustable) a cada lado del punto medio, perpendiculares al trayecto. **Rojo = recomendado**, **rosa = fuera del lóbulo de la antena**, **gris = dentro del lóbulo** (con un aviso) |
| Lóbulo de la antena | El lóbulo horizontal a −3 dB alrededor del azimut de la antena (antena siempre apuntada al DX), rotulado *lóbulo …°* |
| Límites de la zona común | Puntos tenues *lím. A* / *lím. B* y los dos círculos donde el horizonte de cada estación corta la capa E (ver [Geometría](Geometry-and-Path-Loss-es#límites-de-la-zona-común)) |
| Desplazamiento de la lluvia | **Línea amarilla**: dirección en la que la lluvia seleccionada (o la más favorable) barre el cielo, es decir, el azimut del radiante |
| Mejores apuntamientos | **Puntos naranjas**: los dos apuntamientos perpendiculares al desplazamiento (azimut del radiante ±90°, SM6FHZ) |
| **Zonas PREV** | Elipses claras: dónde caen **ahora** las estelas más probables, una por cada lado del trayecto |

Las etiquetas no se solapan: Hot A y PREV A se escriben a la izquierda del trayecto, B a la derecha. La **Leyenda** es una columna plegable a la derecha del mapa.

**Ratón sobre el mapa:** **clic izquierdo = locator del corresponsal**, **clic derecho = locator de mi estación**. El trayecto se recalcula al instante.

Opciones encima de la lista de lluvias: **Direcciones Hot A / Hot B**, **Mapa de Europa** (Natural Earth, descargado en `data/mappa` en el primer arranque), **Vista desde arriba (E a la derecha)**.

### Hot recomendado

Para la hora mostrada, el programa suma sobre todas las lluvias por encima del horizonte el peso ZHR × eficiencia, repartido entre el lado A (fracción f_A) y el lado B. El lado con mayor peso da el Hot recomendado, dibujado en rojo:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Decisión del programa (ec. 23 del manual).* Origen de la idea: DJ5HG, citado por DF5HC (conferencia DARC 2018): según la posición del radiante, uno de los dos puntos, HOT-A o HOT-B, es más favorable. Girar 10–30° hacia ese lado (side-scatter) procede del artículo Cerrotta–Sartori.

### Zonas PREV

Para cada punto P de la capa E se suman las contribuciones de todas las lluvias activas a la eficiencia (misma condición especular que en la [eficiencia](Efficiency-Calculation-es#el-modelo)), ponderadas con la ZHR. Los puntos con al menos el 3 % del máximo forman las zonas PREV; cada una se dibuja como una elipse con centro = media ponderada de los puntos y ejes = el doble de su dispersión.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Decisión del programa (ec. 34 del manual).* Es la regla práctica: si la lluvia barre de norte a sur, las estelas útiles caen al este y al oeste.

## Lista de lluvias (arriba a la derecha)

| Columna | Significado |
|---|---|
| Lluvia, Código | Nombre y código IMO |
| ZHR ahora | Actividad en este momento (ZHR máxima IMO con el perfil de actividad) |
| Azimut, Elev. | Posición del radiante vista desde tu estación |
| Efic. % | Eficiencia de la lluvia para este trayecto |
| Lado | A o B, el lado del que llega la mayoría de las reflexiones |
| Mejor apunt. | Azimut del radiante ±90° |
| Sale, Se pone | Salida y puesta del radiante (UTC); *circumpolar* o *siempre por debajo* cuando corresponde |

Haz clic en una fila para seleccionar la lluvia: la línea amarilla de desplazamiento y los puntos naranjas la siguen.

## Pequeña bóveda celeste (centro derecha)

Los radiantes en una bóveda celeste vista desde tu estación, con su **código IMO** y su **recorrido diario en cian** (horas UTC). **Haz clic en un radiante** para seleccionarlo. Colores:

| Color | Significado |
|---|---|
| Amarillo | eficiencia ≥ 50 % y ZHR ≥ 2 |
| Naranja | eficiencia ≥ 20 % |
| Rojo oscuro | eficiencia < 20 % |
| Gris | casi inactiva |

Al lado, el texto del cálculo: longitud y azimut del trayecto, punto medio y su elevación, azimuts y desplazamientos de Hot A / Hot B, el Hot recomendado (*… recomendado ahora: az. …° (…% de las reflexiones previstas)*), los límites de la zona común y el recordatorio: *mejor apuntamiento para la lluvia: PERPENDICULAR a la dirección de llegada (azimut del radiante ±90°, tolerancia ±40–50°, SM6FHZ)*.

## Sección (abajo a la derecha)

*SECCIÓN - las estelas más probables vistas desde la antena hacia el corresponsal.* En horizontal el **azimut respecto al corresponsal** (← A izquierda, B → derecha), en vertical la **elevación**. Para cada lluvia se toman los 14 puntos de reflexión más intensos; cada estela es un segmento orientado hacia el radiante, desde 10 km por encima hasta 10 km por debajo de la altura de las estelas (como máximo 60 km por lado), más grueso cuanto más probable. También se dibujan: el lóbulo de la antena (círculo de −3 dB alrededor de la elevación del lóbulo), el corresponsal y Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Decisión del programa (ec. 35 del manual).*

## Avisos

| Aviso | Cuándo |
|---|---|
| **ATENCIÓN: Hot A (y/o Hot B) entra en el lóbulo de la antena …** | El hot spot está dentro de ±θ/2 del azimut de la antena (θ = lóbulo horizontal a −3 dB): con este apuntamiento ya está cubierto. Se marca en gris en el mapa. El Hot recomendado sigue en rojo. |
| **RADIANTE DEMASIADO ALTO (por encima de 70°)** | Un radiante útil está a más de 70° de altura vista desde tu estación: las estelas caen casi verticales y reflejan poco hacia el trayecto (DF5HC, DH9GCD). Las mismas horas se marcan con ↑ en la [tabla horaria](Efficiency-Calculation-es#tabla-horaria). |
| *Ninguna zona común de la capa E* | El trayecto es más largo que el doble del alcance a la altura de las estelas: las dos estaciones no ven una parte común de la capa E (salto único imposible). |
| *Ningún Hot recomendado* | Casi no hay lluvias activas en este momento. |

Referencia para el gráfico de la bóveda celeste: Swan Meteor Skyview de DL1DBC (swan.ms); gráfico polar con la mejor dirección: RadiantCalc de SM6FHZ.
