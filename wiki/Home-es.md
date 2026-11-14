[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · **Español** · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – previsiones de meteor scatter y eficiencia de las lluvias en directo

*a cargo de Costantino Cerrotta IC8TEM*

**YA-MS** es un programa gratuito para radioaficionados que trabajan en **meteor scatter (MS) en 50, 70, 144, 222 y 432 MHz**. Para el trayecto real entre tu locator y el del corresponsal calcula, hora por hora, cuánto ayuda cada lluvia de meteoros activa a ese trayecto (su **eficiencia**), de qué lado del trayecto llegan las reflexiones (**Hot A / Hot B**), hacia dónde apuntar la antena y una previsión experimental de las reflexiones por hora obtenida de un **radar meteórico en directo** (Collm, Alemania). Funciona en **Windows, Linux, Raspberry Pi y macOS** (.NET 8 + Avalonia), con 36 idiomas de interfaz.

La fuente principal es el artículo de **C. Cerrotta IC8TEM y G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versión 7). Cada fórmula y cada dato del programa cita su fuente; ver [Fuentes](Sources-es).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Bóveda celeste"></a><br><sub>Bóveda celeste</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Cálculo de la eficiencia"></a><br><sub>Cálculo de la eficiencia</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Para quién es

- Operadores que quieren saber **cuándo** está abierto un trayecto de meteor scatter y **hacia dónde** apuntar, más allá del genérico "esta noche es el máximo de la lluvia".
- Estaciones que trabajan **trayectos largos en 144 y 432 MHz**, donde la posición del radiante decide si una lluvia es útil o inútil.
- Quien quiera **comprobar los números**: el manual de cálculo y la explicación integrada en el programa dan cada paso con su origen: una fuente publicada, una verificación hecha con el programa o una decisión del programa.

## Las pestañas

Desde la versión 1.6 las pestañas principales tienen **subpestañas** (una fila más clara bajo la principal). Al arrancar, una pantalla de bienvenida de 5 segundos muestra las Perseidas sobre el VLT de ESO (foto ESO/S. Guisard, CC BY 4.0).

| Pestaña | Subpestaña | Qué muestra |
|---|---|---|
| **En directo y datos en tiempo real** | [Tráfico en directo](Live-Traffic-es) | Mapa azimutal de todo el tráfico MS recogido, con una nube de las estelas más probables para cada contacto, colores por banda y parpadeo cuando un corresponsal le responde |
| | [Flujo radar](Radar-Flux-es) | Recuentos horarios de meteoros y alturas de las estelas leídos del radar SKiYMET de Collm, imagen de Sodankylä, estimación en tu banda |
| | [Radar GRAVES](GRAVES-Radar-es) | El trayecto de forward scatter GRAVES → tú: zona útil en el haz, sector y paso, próximo paso del haz, cómo escuchar |
| | [Recogida de datos](Data-Collection-es) | Tres flujos de cluster telnet (DX cluster, RBN, DM4X/PSKReporter) y el filtro de los spots MS |
| **Cálculo de previsión** | [Cálculo de previsión](Sky-View-es) | Mapa en planta del trayecto con Hot A / Hot B, lóbulo de la antena, zonas PREV y desplazamiento de las lluvias; lista de lluvias; pequeña bóveda celeste con los radiantes y las direcciones de antena adecuadas; sección vista desde la antena |
| | [Geometría y atenuación](Geometry-and-Path-Loss-es) | Distancia, punto medio, elevación, Hot A / Hot B, límites de la zona común, atenuación del trayecto 28–432 MHz, balance del enlace, antena |
| | [Cálculo de la eficiencia](Efficiency-Calculation-es) | Tarjetas de resumen, eficiencia horaria de cada lluvia con lado A/B, índice del trayecto, comparación con DH9GCD, gráfico |
| | [Previsiones experimentales](Experimental-Forecasts-es) | Flujo de Collm escalado a 144 MHz (o a cualquier frecuencia) con λ^k y factor de estación K, previsión de 24 horas, comparación con RMOB |
| [Lluvias en directo](Live-Showers-es) | – | ZHR medidas por la Global Meteor Network y mapas de radiantes de CMOR |
| [Lluvias](Showers-es) | – | Catálogo IMO con el próximo máximo (fecha y hora IMO o calculada) |
| [Mapa de cuadrículas](Grid-Square-Map-es) | – | Cuadrículas Maidenhead trabajadas y confirmadas a partir de un archivo ADIF, una pestaña por banda |
| **Documentos técnicos** | [Fuentes](Sources-es) | Todas las fuentes; la principal es el artículo Cerrotta–Sartori |
| | [Mapa de los radares europeos](European-Radar-Map-es) | Dónde están Collm, Sodankylä, GRAVES y CMOR respecto a tu estación |
| | [Explicación del cálculo de la eficiencia](Efficiency-Explanation-es) | Documento paso a paso sobre cómo se calcula la eficiencia, exportable a Word |

Encima de las pestañas hay tres filas de controles (tu locator, corresponsal, banda, antena, altura de las estelas, hora); ver [Primeros pasos](Getting-Started-es). El botón **Controles** las pliega; el idioma y el esquema de colores se eligen arriba a la derecha; ver [Ajustes y carpeta de datos](Settings-and-Data-Folder-es).

## En resumen

- **Trayecto real, no direcciones fijas**: la eficiencia se calcula para el trayecto de círculo máximo entre los dos locators (los programas anteriores usaban cuatro direcciones fijas).
- **Modelo de reflexión especular** (McKinley) sobre puntos de la capa E cada 15 km, con la altura de las estelas leída en directo del radar de Collm.
- **Hot A / Hot B** a 150 km a cada lado del punto medio (ajustable de 30 a 400 km), el recomendado en rojo, los que ya están dentro del lóbulo de tu antena en gris.
- **Radar en directo**: Collm se comprueba cada 5 minutos y solo se vuelven a descargar las fuentes que han cambiado; sin conexión el programa sigue funcionando con los últimos datos guardados.
- Previsión **experimental** en 50/144/432 MHz con la regla λ³ de SM6FHZ, comparable con los observadores RMOB.
- Todo en una única carpeta **`data`** junto al programa: nada de AppData ni carpetas del sistema.

> La eficiencia es un modelo experimental (reflexión especular + estelas subdensas). Compárala con MCG_MS, MS-Soft y tu propia experiencia en el aire.

## Por dónde empezar

1. [Instalación](Installation-es)
2. [Primeros pasos](Getting-Started-es)
3. [Problemas y preguntas frecuentes](Troubleshooting-FAQ-es) si algo no funciona.

Descargas: **[Releases](https://github.com/ic8tem/YA-MS/releases)** en GitHub.
