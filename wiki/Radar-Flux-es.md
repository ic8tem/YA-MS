[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · **Español** · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [ไทย](Radar-Flux-th) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# Flujo radar

*Pestaña: En directo y datos en tiempo real › Flujo radar.*

[![Flujo radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Esta pestaña muestra lo que están contando **ahora** los radares meteóricos profesionales: los recuentos horarios de meteoros y las alturas de las estelas del radar SKiYMET de **Collm** (Universidad de Leipzig / IAP Kühlungsborn, Alemania, 36,2 MHz) y la última imagen del radar de **Sodankylä** (SGO, Finlandia). Los recuentos de Collm alimentan la estimación en tu banda y las [Previsiones experimentales](Experimental-Forecasts-es); la altura de las estelas medida alimenta toda la geometría.

## Controles

| Control | Qué hace |
|---|---|
| **Descargar ahora** | Comprueba de una vez todas las fuentes externas. |
| **Actualización automática de todas las fuentes cada 5 minutos** | Activada por defecto. Cada 5 minutos se comprueban todas las fuentes y se vuelven a descargar **solo las que han cambiado** (*sin cambios (comprobado a las … UTC)* / *dato nuevo a las … UTC*). |
| **Exponente λ (SM6FHZ)** | Exponente k de la regla de frecuencia, por defecto 3 (1–4). |

## Qué se muestra

| Panel | Contenido |
|---|---|
| **Meteoros/hora - ayer y hoy (UTC)** | Barras cian = recuentos de Collm (válidos), barras rojas = descartados, línea naranja gruesa = *estimación a … MHz* en la escala de la derecha |
| **Alturas de las estelas (Collm)** | Meteoros por km de altura entre 70 y 110 km, con altura más frecuente (moda), media, mediana y desviación típica |
| Imagen de Collm | El gráfico SKiYMET original, tal como se descarga |
| Imagen de Sodankylä | La última imagen de recuentos de meteoros del radar de Sodankylä (solo se muestra; su formato no se lee) |

La línea sobre los gráficos indica cuándo se leyó el gráfico de Collm y qué escala vertical se encontró (*escala leída del gráfico: 0-… meteoros/hora*).

## Cómo se lee el gráfico de Collm

El gráfico de Collm (720 × 720 píxeles, colores puros) tiene los ejes en posiciones fijas, pero el radar **adapta la escala vertical cada día** a los valores medidos (p. ej. 0–1,2·10³ el 5/11/2026 y 0–1,0·10³ el 6/11/2026, con las marcas desplazadas). Por eso YA-MS:

1. localiza las marcas largas del eje;
2. **lee las etiquetas** de la marca más alta y del cero comparando cada carácter con la fuente de matriz de puntos del gráfico;
3. para cada hora i (0–47, ayer y hoy) toma la columna central y el primer píxel cian desde arriba, y:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top e y0 son las filas de la marca más alta y del cero, N_top el valor leído en la etiqueta más alta (×1000). Resolución: unos 7–8 meteoros/hora por píxel. *Decisión del programa (ec. 42 del manual).*

Si no se puede leer una etiqueta, el programa vuelve a la calibración del 5/11/2026 (**escala calibrada 0-1200 meteoros/hora**) y lo indica en naranja: *No se puede leer la escala vertical del flujo (etiqueta superior: …): valores por verificar.* Si cambia el propio formato del gráfico (*Formato del gráfico cambiado (…x…): lectura imposible* o *Ejes del flujo no encontrados en la posición esperada*), hay que recalibrar la lectura: por favor, avísalo (ver [Contribuir](Contributing-and-Contacts-es)).

### Alturas de las estelas

A partir del histograma de alturas (n_k meteoros en el km k, altura media h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Ec. 43 del manual.* Con **del radar** marcado (fila 2 de los controles) la **moda** pasa a ser la altura de las estelas en todos los cálculos. Verificación: gráfico del 5/11/2026 – moda 89,5 km, media 88,6 km, desviación típica 6,8 km, lo que confirma los ~90 km del artículo Cerrotta–Sartori (media SKiYMET).

Si cambia la escala del gráfico de alturas, el programa avisa: *las estadísticas de alturas (moda, media, mediana) siguen siendo válidas, los recuentos absolutos no.*

## Estimación en tu banda

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

Reglas experimentales de **SM6FHZ** (VUSHF 2025): el número y la intensidad de las reflexiones escalan con λ³, la duración con λ² (en McKinley λ³ es la potencia de una estela; el número de estelas escala aproximadamente como λ^1,5, y en dispersión hacia delante las duraciones crecen además con sec²φ: ver [Previsiones experimentales](Experimental-Forecasts-es)). También se muestra la duración máxima de los pings según la IARU Región 1 (1000 ms en 50 MHz, 500 ms en 70 MHz, 100 ms en 144 MHz, 13 ms en 432 MHz). Los valores son orientativos, a comparar con la experiencia en el aire. El factor de estación K y la comparación con RMOB están en [Previsiones experimentales](Experimental-Forecasts-es).

## Sin conexión

Si no se puede alcanzar ninguna fuente, aparece **una sola vez** un mensaje: *Sin conexión a internet. Los datos de los radares y de RMOB no se pueden actualizar: el programa usa los últimos datos guardados y lo vuelve a intentar solo cada 5 minutos.* La barra de estado de abajo se pone roja (*SIN CONEXIÓN A INTERNET …*) hasta que vuelve la conexión (*Conexión restablecida.*).

## Archivos históricos y fuentes

| Archivo (en `data/`) | Contenido |
|---|---|
| `flusso_collm.csv` | Archivo histórico horario del flujo leído de Collm (las horas ya presentes se actualizan) |
| `quote_collm.csv` | Archivo histórico de las alturas de las estelas |
| `radar/` | Últimas imágenes descargadas (y archivos RMOB) |
| `fonti_radar.csv` | Direcciones de las fuentes de radar, `attivo=1/0` para activar/desactivar cada una |

| Fuente | Frecuencia | Notas |
|---|---|---|
| Radar meteórico de Collm, Universidad de Leipzig (LIM) e IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | se actualiza cada hora en el minuto 10 UTC; flujo de ayer + hoy, distribución de alturas |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | solo imagen (radar en renovación, proyecto DECC) |
| swan.ms (copia de Collm) | 36,2 MHz | desactivada por defecto; úsala solo con el permiso de DL1DBC |

> Los datos de radar pertenecen a sus instituciones (Universidad de Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
