[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · **Español** · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Previsiones experimentales

*Pestaña: Cálculo de previsión › Previsiones experimentales.*

[![Previsiones experimentales](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Esta pestaña convierte los recuentos de meteoros del **radar de Collm (36,2 MHz)** en una estimación de las **reflexiones por hora en una banda de radioaficionado** (144 MHz por defecto, cualquier frecuencia de 28 a 1300 MHz), hace una previsión de las **próximas 24 horas** para tu trayecto y te permite **comparar** la estimación con un observador **RMOB**, por ejemplo uno que escucha GRAVES en 143,050 MHz.

> Todo lo que hay aquí es **experimental**: la regla de frecuencia es una regla empírica y el factor de estación depende de tu estación. Usa los números para comparar horas y días, y compruébalos en el aire.

## Controles

| Control | Por defecto | Qué hace |
|---|---|---|
| **Frecuencia de destino MHz** | 144 | Frecuencia de la previsión (28–1300 MHz) |
| **Exponente λ^k** | 3 | Exponente k de la regla de frecuencia (SM6FHZ: 3) |
| **Factor de estación K** | 1 | Tiene en cuenta la estación receptora (potencia, antenas); se obtiene por comparación con un observador RMOB en la misma banda |
| **Cargar archivo RMOB desde el disco...** | | Lee un archivo de texto mensual de RMOB (ver abajo) |
| **Obtener el exponente del archivo RMOB** | | Ajusta k a partir de las horas en común entre Collm y RMOB |
| **Observador RMOB** | vacío | Nombre del observador tal como aparece en el nombre del archivo (p. ej. `NAME_112026rmob.TXT` → `NAME`) |
| **Descargar RMOB ahora** | | Descarga una vez el archivo del mes en curso de ese observador |
| **descarga automática cada 5 minutos (activar solo con el permiso de RMOB)** | **desactivada** | Ver [RMOB y los programas automáticos](#rmob-y-los-programas-automáticos) |

La línea naranja bajo los controles muestra la regla con los números actuales, p. ej. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, el escalado de la duración y el ping máximo IARU a esa frecuencia.

## Del radar a la banda de radioaficionado

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Fuente:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, mayo de 2025: el número y la intensidad de las reflexiones escalan con **λ³**, la duración con **λ²** (432 MHz está 14–15 dB por debajo de 144 MHz y dura 1/9). **Verificación:** la dependencia de λ³ es la misma que en la ecuación subdensa de McKinley. Con k = 3, 1000 meteoros/hora en Collm se convierten en unas **16 reflexiones/hora en 144 MHz**; los observadores RMOB de GRAVES en 143,050 MHz suelen contar **de 20 a 140 ecos/hora** (boletín RMOB, junio de 2018): el orden de magnitud es compatible, y la diferencia es el factor de estación K. (Ec. 44–45 del manual.)

## Próximas 24 horas

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Persistencia:** el valor escalado de la misma hora del día anterior (o de dos días antes si falta), corregido por la variación del **índice de lluvias del trayecto** I (Σ ZHR × eficiencia, ver [Cálculo de la eficiencia](Efficiency-Calculation-es#el-modelo)). La constante 10 representa el fondo esporádico y limita la corrección cuando el índice es pequeño. *Decisión del programa (ec. 47 del manual).*

| Panel | Contenido |
|---|---|
| **Medido en Collm y escalado a f MHz - ayer y hoy (UTC)** | Meteoros/hora del radar de Collm; valores escalados (naranja, escala de la derecha); los recuentos RMOB si se han cargado (verde, escala de la derecha) |
| **Previsión experimental de las próximas 24 horas a f MHz para …** | Reflexiones/hora previstas (barras) y el índice de lluvias del trayecto (escala de la derecha) |
| Tabla | Hora UTC · Collm misma hora · Escalado · Índice lluvias trayecto · Previsión /hora · **Valoración** |

**Valoración:** *bueno* cuando la previsión es al menos 1,3 × la media de 24 horas, *regular* desde 0,8 ×, *escaso* por debajo. La misma previsión aparece en la tarjeta **PREVISIÓN EXPERIMENTAL** y en la fila naranja de [Cálculo de la eficiencia](Efficiency-Calculation-es), y es la base de los ecos esperados en la pestaña [Radar GRAVES](GRAVES-Radar-es#ecos-esperados-experimental).

## Comparación con RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) reúne los recuentos horarios de meteoros de los radioobservadores; muchos en Italia escuchan GRAVES en 143,050 MHz (Planetario de Venecia, Faenza, Rovereto y otros).

**Lectura de los archivos RMOB.** Se aceptan dos formatos de texto:

| Formato | Aspecto | Notas |
|---|---|---|
| Archivo mensual (Colorgramme / Spectrum Lab) | una fila por día, `day| n| n| …` con 24 valores horarios | el habitual `NAME_MMYYYYrmob.TXT` |
| Tabla del boletín | cabecera ` UT |  1   2   3 …`, filas `0h|175 166 …` | si el archivo contiene varios observadores se leen seguidos: usa un archivo con un solo observador |

Mes y año se toman del nombre del archivo (`…_MMYYYYrmob…`) o de la cabecera; si no, se usa el mes actual (y el programa lo indica).

**Ajuste del exponente.** Con K = 1, a partir de la mediana de las razones RMOB/Collm en las horas comunes (al menos 3):

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Decisión del programa (ec. 46 del manual).* El cuadro de diálogo muestra las horas comunes, la razón mediana y k; **Sí** aplica k (y pone K = 1), **No** mantiene k = 3; en ese caso ajusta K a mano al valor sugerido en el mismo cuadro de diálogo.

## RMOB y los programas automáticos

RMOB pide que **los programas automáticos no descarguen sus archivos**. Por eso la **descarga automática está desactivada** al principio y solo debe activarse **después de pedir permiso a RMOB**. Sin él siempre puedes usar **Cargar archivo RMOB desde el disco...** o pulsar **Descargar RMOB ahora** cuando lo necesites.

La dirección de descarga es una plantilla en `config.ini` (clave `rmob_url`, por defecto `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, donde `{NOME}` es el observador y `{MMAAAA}` mes y año); los archivos descargados se guardan en `data/radar/`.
