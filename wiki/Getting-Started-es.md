**English** · [Русский](Getting-Started-ru) · [Deutsch](Getting-Started-de) · [日本語](Getting-Started-ja)

# Primeros pasos

En el primer arranque YA-MS muestra un trayecto de ejemplo (JN70CN → JO62QM en 144 MHz). Bastan cinco minutos para configurarlo para tu estación.

## 1. Las tres filas de controles

Encima de las pestañas hay tres filas de controles, válidas para todas las pestañas. El botón **Controles** arriba a la derecha las pliega y despliega (útil con fuentes grandes); la elección se recuerda.

**Fila 1 – estaciones y banda**

| Control | Qué hace |
|---|---|
| **Mi locator** / **altura m** | Tu locator Maidenhead (4, 6 u 8 caracteres; se usa el centro de la cuadrícula) y la altura de la estación sobre el nivel del mar. |
| **Corresponsal** / **altura m** | Locator y altura de la estación que quieres trabajar. |
| **Banda MHz** | 28, 50, 70, 144, 222 o 432 MHz: se usa para la ganancia y el lóbulo de la antena, la estimación del flujo y el balance del enlace. |
| **Calcular** | Recalcula el trayecto (muestreo de la capa E: unos segundos). |
| **Antena az** | Azimut de tu antena: siempre **hacia el DX** (azimut del trayecto). |
| **Fuente de letra** | Tamaño de todo el texto, 100–300 %. Ver [Ajustes](Settings-and-Data-Folder-es#fuente-de-letra-y-controles). |

**Fila 2 – capa E y antena**

| Control | Qué hace |
|---|---|
| **Altura estelas km** + **del radar** | Altura de las estelas meteóricas (por defecto 90 km). Con *del radar* marcado se usa la altura más frecuente (moda) medida por el radar de Collm; ver [Flujo radar](Radar-Flux-es). |
| **Elevación lóbulo °** | Elevación mínima del lóbulo de tu antena (0° = horizonte). Solo se usan los puntos de la capa E que ambas estaciones ven por encima de esta elevación. |
| **Antena Yagi: boom m** | Longitud del boom de tu Yagi. El programa muestra la longitud en λ, la ganancia (curva DL6WU) y el lóbulo a −3 dB, horizontal y vertical; ver [Geometría y atenuación](Geometry-and-Path-Loss-es#ganancia-y-lóbulo-de-la-antena). Por debajo de 2 λ la estimación es poco precisa. |
| **Hot spot desde punto medio km** | Distancia de Hot A y Hot B al punto medio, 30–400 km (por defecto 150 km, como AMS Bulletin 203 / W8WN / MSHV). |

**Fila 3 – hora**

| Control | Qué hace |
|---|---|
| **Hora** | Reloj UTC. |
| **Hora de la bóveda celeste (±36 h)** | Desplaza la [Bóveda celeste](Sky-View-es) y la pestaña [Radar GRAVES](GRAVES-Radar-es) hasta 36 horas atrás o adelante, en pasos de 15 minutos. |
| **Tiempo real** | Vuelve al momento actual. |
| **Día para la tabla 24 h (UTC)** | El día mostrado en [Cálculo de la eficiencia](Efficiency-Calculation-es) y en la cronología de GRAVES. |

## 2. Tu estación y el DX

1. Escribe **Mi locator** y **altura m**.
2. Escribe locator y altura del **Corresponsal**, o haz clic en el mapa de la [Bóveda celeste](Sky-View-es): **clic izquierdo = locator del corresponsal**, **clic derecho = locator de mi estación**.
3. Elige la **Banda MHz** y pulsa **Calcular**.

La barra de estado de abajo lo confirma: *Trayecto calculado: … km, … puntos de reflexión muestreados en … s*.

## 3. Tu antena

Introduce la **longitud del boom** de tu Yagi. El programa obtiene ganancia y lóbulo y te avisa si Hot A o Hot B ya caen **dentro del lóbulo** cuando la antena apunta al DX (entonces se dibujan en gris: no hace falta girar la antena).

## 4. Leer los resultados

| Pregunta | Dónde mirar |
|---|---|
| ¿Qué lluvia ayuda ahora a mi trayecto y desde qué lado? | [Bóveda celeste](Sky-View-es): lista de lluvias, Hot recomendado en rojo, zonas PREV |
| ¿Cuál es la mejor hora hoy? | [Cálculo de la eficiencia](Efficiency-Calculation-es): tarjetas de resumen y tabla horaria |
| ¿Cuántos meteoros está contando el radar? | [Flujo radar](Radar-Flux-es) |
| ¿Cuántos pings puedo esperar en 144 MHz? | [Previsiones experimentales](Experimental-Forecasts-es) (experimental) |
| ¿Puede mi estación cerrar el trayecto? | [Geometría y atenuación](Geometry-and-Path-Loss-es): atenuación del trayecto y margen |
| ¿Cuándo es el próximo máximo? | [Lluvias](Showers-es) |
| ¿Puedo hacer pruebas con GRAVES? | [Radar GRAVES](GRAVES-Radar-es) |

## Reglas prácticas (de las fuentes)

- **Apuntar perpendicularmente a la lluvia**: el mejor trayecto es ortogonal al azimut del radiante; mejor apuntamiento = azimut del radiante ±90°, tolerancia ±40–50° (SM6FHZ).
- **Side-scatter**: gira la antena 10–30° hacia el lado (A o B) del que llega la mayoría de las reflexiones (artículo Cerrotta–Sartori).
- Un **radiante demasiado alto** (por encima de 70°) o demasiado bajo (por debajo de 20°) da pocas estelas útiles (DF5HC, DH9GCD).
- Los meteoros esporádicos tienen su máximo hacia las **06 UTC** (artículo; confirmado por el flujo de Collm).
- Distancias útiles en 432 MHz: 800–2000 km, la mejor unos 1400 km (SM6FHZ); mejor distancia en general 1300–1500 km (DF5HC).

Siguiente: [Bóveda celeste](Sky-View-es).
