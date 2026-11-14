[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · **Español** · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Tráfico en directo

*Pestaña: En directo y datos en tiempo real › Tráfico en directo.*

[![Tráfico en directo](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Qué muestra

Un **mapa azimutal equidistante** centrado en tu estación (distancia desde el centro = distancia real, ángulo = azimut) con **todo el tráfico de meteor scatter** reunido por [Recogida de datos](Data-Collection-es). Para cada contacto el programa dibuja:

- el **trayecto** entre las dos estaciones, con el color de su banda: 28 MHz marrón, 50 MHz verde, 70 MHz cian, 144 MHz naranja, 222 MHz rosa, 432 MHz violeta;
- las dos **estaciones** en los extremos del trayecto;
- la **zona del enjambre**: dónde se concentran las estelas meteóricas más probables para ese trayecto y esa hora.

Los spots con una estación **fuera del mapa** se descartan. Un spot **recién llegado** (de no más de 3 minutos) **parpadea durante un minuto**, de modo que la actividad nueva salta a la vista.

Mostrar quién escucha: triángulos del color de la banda marcan las estaciones que, según PSKReporter, reciben en MSK144, FSK441, PSK2K o JTMS en 28, 50, 70, 144 y 432 MHz en la ventana de tiempo elegida. Un clic en un triángulo muestra indicativo, locator, modos y último spot. El flujo MQTT de la pestaña Recogida de datos debe estar conectado.

También los monitores activos del mapa de PSKReporter: triángulos vacíos para las estaciones que aparecen en el mapa de pskreporter.info en MSK144, FSK441, PSK2K o JTMS pero aún no han recibido ningún spot (MQTT solo envía las estaciones que reciben algo). YA-MS consulta el servicio de consulta de PSKReporter una vez cada 5 minutos para todos los modos, como piden las normas del servicio; un monitor permanece en el mapa al menos 11 minutos. Un clic en el triángulo muestra indicativo, locator, programa de decodificación y la hora en que el monitor estaba activo. Activado de serie.

FT8 a más de 1100 km sin trayectos paralelos: un spot FT8 (de PSKReporter MQTT, de los clusters o de WSJT-X vía UDP) entre estaciones separadas más de 1100 km que no tiene trayectos paralelos en los 3 minutos antes y después (misma banda, punto medio a menos de 300 km, dirección a menos de 15°, otro par de estaciones) se dibuja en verde claro y su fila en la tabla de abajo a la derecha parpadea siempre. La E esporádica y la tropo dan muchos trayectos cercanos y paralelos; un spot aislado puede ser una estela meteórica. Por eso YA-MS recibe de MQTT también los FT8 de 6 m, 4 m, 2 m, 1,25 m y 70 cm (nunca 28 MHz, en ningún caso). Estos spots no entran en el archivo MS. Activado de serie.

Los spots de WSJT-X vía UDP que conciernen a su estación (la decodificación contiene su indicativo: quien le llama o le responde) se dibujan con una línea discontinua que parpadea siempre, en cualquier modo y a cualquier distancia.

Intercambio entre usuarios de YA-MS: cuando otro usuario de YA-MS decodifica por UDP un mensaje dirigido a su estación (en MSK144, FSK441, PSK2K o JTMS, o en FT8 a más de 1100 km), su YA-MS se lo envía cifrado a través de tres brokers MQTT públicos (HiveMQ, Mosquitto, EMQX); lo ve como una línea discontinua violeta que parpadea siempre y como una línea en la consola UDP. Solo usted puede leerlo (claves ECDH P-256, AES-256 y HMAC-SHA256). Los spots FT8 solo se muestran si no tienen trayectos paralelos en 3 minutos. Activado de serie; yams_scambio=0 en data/config.ini lo apaga.

El mapa muestra los indicativos de las dos estaciones de cada spot, una sola vez por estación. La proyección puede ser azimutal (centrada en tu estación) o Mercator. La ayuda emergente de la columna zona del enjambre explica su significado.

Se muestran los spots de todas las bandas, también de las no elegidas en Recogida de datos (estos no se guardan). Los spots CW y los de estaciones demasiado cercanas no se muestran si se descartan en Recogida de datos.

## Cómo se calcula la zona del enjambre

Para cada spot el programa construye el trayecto entre los dos locators (la misma geometría que para tu propio trayecto, ver [Geometría y atenuación](Geometry-and-Path-Loss-es)) y, a la hora del spot, suma punto por punto de la capa E las **contribuciones de reflexión especular de cada lluvia activa**, ponderadas con su ZHR: el mismo cálculo que las **zonas PREV** de la [bóveda celeste](Sky-View-es). Para cada lado del trayecto que reúna al menos el 15 % del total, la zona del enjambre es una **elipse**: centro en la media ponderada de los puntos, semiejes iguales a 1,5 veces las raíces cuadradas de los autovalores de su dispersión, eje mayor según el autovector principal. Cuando no contribuye ninguna lluvia (solo meteoros esporádicos), las zona del enjambre son los dos **hot spots** clásicos, dibujados con trazo discontinuo. Las ecuaciones completas están en el capítulo 10 del manual de cálculo.

## Controles

| Control | Significado |
|---|---|
| **Radio del mapa** | 600–3500 km desde tu estación. |
| **Spots a mostrar** | Últimos 15 o 30 minutos, última hora, últimas 3 horas, últimas 24 horas. |
| **Tabla** | Contactos del mapa, los más recientes primero, con el color de la banda; *% enjambre* da la proporción de reflexiones del lado principal, o *esporádicos*. |
| **Clic** | Sobre un trayecto o una fila de la tabla: el contacto se resalta y el recuadro muestra el locator del centro de la zona del enjambre, su proporción, tamaño y eje. |
