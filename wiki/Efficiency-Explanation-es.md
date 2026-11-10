[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · **Español** · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# Eficiencia - explicación

*Pestaña: Documentos técnicos › Eficiencia - explicación.*

[![Eficiencia - explicación](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Un documento técnico, *"Come YA-MS calcola l'efficienza di uno sciame"* (Cómo calcula YA-MS la eficiencia de una lluvia), mostrado dentro del programa como una página clara. Explica **paso a paso** cómo se obtiene la eficiencia e indica para cada paso **de dónde procede**. Por ahora el documento está **en italiano**; esta wiki ofrece su contenido en español en [Cálculo de la eficiencia](Efficiency-Calculation-es#el-modelo) y [Geometría y atenuación](Geometry-and-Path-Loss-es).

## Etiquetas

Cada paso lleva una etiqueta de color:

| Etiqueta | Color | Significado |
|---|---|---|
| **FONTE** (fuente) | azul | el paso retoma una fuente citada; el número entre corchetes remite a la lista final |
| **RILIEVO** (verificación) | verde | comparación entre el programa y las fuentes, con el resultado |
| **SCELTA** (decisión) | naranja | una decisión del programa, no tomada de una fuente: hay que comprobarla con la experiencia en el aire |

## Capítulos

| Capítulo | Contenido |
|---|---|
| 1. Introducción | Objetivo, etiquetas, qué significa la eficiencia (OH5IY, MCG_MS; YA-MS usa el trayecto real) |
| 2. Dónde se producen las reflexiones: la capa E | Estelas a 80–120 km; altura de las estelas = moda del histograma de Collm (verificación: 89,5 km el 5/11/2026) |
| 3. Geometría del trayecto | Tierra y punto medio; elevación de la antena (fórmula del artículo); zona común y sus límites; Hot A / Hot B; lóbulo de la antena (DL6WU, Kraus, W4RNL) |
| 4. El radiante de la lluvia | Posición del radiante (IMO 2026/2027), fecha del máximo (IMO o longitud solar), perfil de actividad |
| 5. Condición de reflexión | Reflexión especular (McKinley), tolerancia gaussiana de 0,05 rad, mejor apuntamiento (SM6FHZ), fórmula de DH9GCD |
| 6. De un punto a la eficiencia | Puntos de reflexión cada 15 km, peso de cada punto, porcentaje; comparación con QTFGUI (DJ5HG) |
| 7. Lectura de los resultados | Lado A / B, índice del trayecto, colores de los radiantes, zonas PREV, sección vista desde la antena |
| 8. Frecuencia de trabajo y atenuación | Reglas λ³ / λ², del radar a la banda de radioaficionado, referencias de atenuación |
| 9. Límites conocidos | Solo estelas subdensas, antenas isótropas, valores de trabajo |
| 10. Fuentes | 17 fuentes numeradas |

## Botones

| Botón | Qué hace |
|---|---|
| **Exportar a Word (.docx)...** | Guarda una copia de `data/efficienza_spiegazione.docx` donde elijas (nombre propuesto *YA-MS - calcolo dell'efficienza.docx*) |
| **Abrir en Word** | Abre el mismo `.docx` con el programa predeterminado para documentos Word (Word, LibreOffice, …) |

## Archivos

| Archivo | Contenido |
|---|---|
| `data/efficienza_spiegazione.txt` | El texto mostrado en la pestaña, un bloque por línea (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | La versión Word |
| `doc/YA-MS_manuale_calcoli.docx` | El **manual de cálculo**: todas las ecuaciones (editor de ecuaciones de Word), numeradas, con sus fuentes |

Los dos documentos se regeneran a partir del código fuente con `tools/build_spiegazione.py data` y `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
