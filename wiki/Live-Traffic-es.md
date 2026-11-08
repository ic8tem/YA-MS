**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Tráfico en directo

*Pestaña: En directo y datos en tiempo real › Tráfico en directo.*

[![Tráfico en directo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Qué muestra

Un **mapa azimutal equidistante** centrado en tu estación (distancia desde el centro = distancia real, ángulo = azimut) con **todo el tráfico de meteor scatter** reunido por [Recogida de datos](Data-Collection-es). Para cada contacto el programa dibuja:

- el **trayecto** entre las dos estaciones, con el color de su banda: 28 MHz marrón, 50 MHz verde, 70 MHz cian, 144 MHz naranja, 222 MHz rosa, 432 MHz violeta;
- las dos **estaciones** en los extremos del trayecto;
- la **nube**: dónde se concentran las estelas meteóricas más probables para ese trayecto y esa hora.

Los spots con una estación **fuera del mapa** se descartan. Un spot **recién llegado** (de no más de 3 minutos) **parpadea durante un minuto**, de modo que la actividad nueva salta a la vista.

## Cómo se calcula la nube

Para cada spot el programa construye el trayecto entre los dos locators (la misma geometría que para tu propio trayecto, ver [Geometría y atenuación](Geometry-and-Path-Loss-es)) y, a la hora del spot, suma punto por punto de la capa E las **contribuciones de reflexión especular de cada lluvia activa**, ponderadas con su ZHR: el mismo cálculo que las **zonas PREV** de la [bóveda celeste](Sky-View-es). Para cada lado del trayecto que reúna al menos el 15 % del total, la nube es una **elipse**: centro en la media ponderada de los puntos, semiejes iguales a 1,5 veces las raíces cuadradas de los autovalores de su dispersión, eje mayor según el autovector principal. Cuando no contribuye ninguna lluvia (solo meteoros esporádicos), las nubes son los dos **hot spots** clásicos, dibujados con trazo discontinuo. Las ecuaciones completas están en el capítulo 10 del manual de cálculo.

## Controles

| Control | Significado |
|---|---|
| **Radio del mapa** | 600–3500 km desde tu estación. |
| **Spots a mostrar** | Últimos 15 o 30 minutos, última hora, últimas 3 horas, últimas 24 horas. |
| **Tabla** | Contactos del mapa, los más recientes primero, con el color de la banda; *Nube* da la proporción de reflexiones del lado principal, o *esporádicos*. |
| **Clic** | Sobre un trayecto o una fila de la tabla: el contacto se resalta y el recuadro muestra el locator del centro de la nube, su proporción, tamaño y eje. |
