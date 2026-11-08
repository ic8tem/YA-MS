**English** · [Русский](GRAVES-Radar-ru) · [Deutsch](GRAVES-Radar-de) · [日本語](GRAVES-Radar-ja)

# Radar GRAVES

*Pestaña: En directo y datos en tiempo real › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Qué es GRAVES

**GRAVES** es un radar francés que transmite **CW en 143,050 MHz** desde **Broye-lès-Pesmes** (47,348° N 5,515° E, locator **JN27SI**, unos 200 m s. n. m.; Wikipedia). Las estelas meteóricas en la zona que ven tanto GRAVES como tú reflejan su señal hacia ti por **forward scatter**: oyes *pings* cortos cerca de la portadora. Así es como los observadores **RMOB** en 143,050 MHz cuentan los meteoros hora por hora, y es una señal de prueba gratuita y siempre activa para tu estación de meteor scatter en 2 m.

La pestaña trata **GRAVES → tú** como un trayecto de meteor scatter propio: con las mismas funciones que el trayecto principal (misma altura de las estelas, elevación del lóbulo y distancia de los hot spots) calcula la eficiencia de las lluvias, el Hot recomendado y las zonas PREV, y luego comprueba si esa zona está **dentro del haz de GRAVES** y **cuándo** la ilumina el haz.

## Barra superior

| Control | Qué hace |
|---|---|
| **Ahora** | Devuelve la hora de la bóveda celeste al tiempo real (la pestaña sigue al regulador *Hora de la bóveda celeste*). |
| **Poner GRAVES como DX** | El corresponsal pasa a ser GRAVES (JN27SI, altura 200 m) y el trayecto principal se recalcula: todas las demás pestañas muestran entonces el trayecto de GRAVES. |
| **Secuencia del haz** | *0,8 s por paso · ciclo 4,8 s (PE1ITR 2021)* (por defecto) o *3,2 s por paso · ciclo 19,2 s (PE1ITR 2007)*. |

## Las cuatro tarjetas

| Tarjeta | Contenido |
|---|---|
| **ZONA ÚTIL EN EL HAZ DE GRAVES** | *Sí · sector X* con el azimut y la elevación del hot spot recomendado vistos desde GRAVES y el paso (1–6); o *No: fuera de los sectores* / *No: bajo el horizonte de GRAVES* / *No: por encima del haz (unos 25°)* |
| **EFICIENCIA DEL TRAYECTO GRAVES → TÚ AHORA** | Índice del trayecto Σ ZHR × eficiencia, mejor lluvia, lado predominante A/B y *ecos esperados ≈ …/hora* (experimental, ver abajo) |
| **TRAYECTO** | Distancia a GRAVES; antena hacia el Hot recomendado (azimut y elevación); azimut directo de GRAVES |
| **PRÓXIMO PASO DEL HAZ SOBRE LA ZONA** | *ahora · quedan … s* o *en … s*, el paso (p. ej. *B4*), las tres próximas horas (segundos dentro del minuto) y la fracción de estelas captadas |

Si en ese momento no hay ninguna lluvia útil, el programa muestra el hot spot **más adecuado al haz** (dentro de los sectores, el más cercano al sur) y lo indica.

## El cielo visto desde GRAVES

Según PE1ITR y la wiki de Bolidozor, **cuatro agrupaciones en fase** cubren el cielo al sur de **90° a 270°** de azimut en cuatro **sectores de 45°**:

| Sector | Azimut desde GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Cada sector se divide en **6 pasos de 7,5°**, numerados de 1 a 6 a partir del azimut más bajo, iluminados uno tras otro, **en el mismo momento en los cuatro sectores**. El haz tiene unos **25° de anchura en elevación**: a la altura de las estelas cubre la corona coloreada entre los dos círculos discontinuos (*horizonte del haz*). En el dibujo: puntos naranja/rosa = zonas PREV del trayecto GRAVES → tú, línea verde = dirección de tu estación, línea roja = de tu estación al hot spot recomendado; se resalta el paso iluminado en ese momento.

## Reconstrucción cronológica

*RECONSTRUCCIÓN CRONOLÓGICA · fecha UTC* (el mismo día que la tabla de 24 h): para cada hora, la eficiencia del trayecto GRAVES → tú, la lluvia más favorable y la ventana útil (*hh:00 → hh:00 UTC · n h*), con el máximo (*máx Σ … a las hh:30*) y un marcador rojo de *ahora*. Debajo, el **detalle de los próximos segundos**: los seis pasos del sector, el paso que ilumina la zona útil y *eco posible (+0,3 s de estela)*.

### Temporización del haz

La secuencia está ligada a la hora **UTC** (PE1ITR): el paso iluminado ahora se calcula a partir de los segundos desde las 00:00 UTC módulo el ciclo (86 400 s es múltiplo tanto de 4,8 s como de 19,2 s). La estación de mando a veces desplaza la secuencia algunos pasos, así que el detalle es una **predicción que hay que confirmar escuchando**. La etiqueta amarilla **reloj del PC sincronizado** te lo recuerda: sincroniza tu PC con un servidor NTP (error de unas décimas de segundo como mucho).

### Factor de detección

Una estela solo se oye si el haz la ilumina mientras dura:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0,3 s es una duración típica de una estela subdensa a 143 MHz: un valor fijo, *decisión del programa* (la regla λ² de SM6FHZ escala las duraciones entre bandas, pero no da un valor de partida).

### Ecos esperados (experimental)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

La previsión de [Previsiones experimentales](Experimental-Forecasts-es) (que ya incluye el factor de estación K) se escala de su frecuencia f_fc a 143,050 MHz con la regla de SM6FHZ (mismo exponente k), se corrige con la razón entre los índices de lluvias de los dos trayectos (la constante 10 representa el fondo esporádico, como en la previsión) y se multiplica por el factor de detección. Solo orientativo: compáralo con los observadores RMOB.

## Cómo escuchar los pings de GRAVES

| Paso | Qué hacer |
|---|---|
| Receptor | **USB en 143,049 MHz** (tono de aproximadamente 1 kHz) o 143,050 MHz, **AGC lento o desactivado**, ancho de banda de audio de **al menos 2,4 kHz** |
| Antena | Hacia el **hot spot recomendado** del trayecto GRAVES → tú (tarjeta *TRAYECTO*), con **elevación baja** |
| Cascada | Los pings son **trazos cortos cerca de la portadora**; las estelas largas (sobredensas) son más anchas y muestran Doppler |
| Recuento | RMOB usa GRAVES para los recuentos horarios de meteoros: **compara tus pings con los observadores en 143,050 MHz** ([Previsiones experimentales](Experimental-Forecasts-es#comparación-con-rmob)) |

## Fuentes

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) y *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki de **Bolidozor**, "Graves" – agrupaciones, sectores y tiempos del haz
3. **Wikipedia**, "GRAVES (system)" – transmisor en Broye-lès-Pesmes (47,348° N 5,515° E)
4. **RMOB** – observadores en 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** de IC8TEM – pestaña Radar GRAVES (el boceto del que deriva esta pestaña)
