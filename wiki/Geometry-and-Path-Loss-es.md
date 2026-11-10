[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · **Español** · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometría y atenuación

*Pestaña: Cálculo de previsión › Geometría y atenuación.*

[![Geometría y atenuación](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Un informe de texto del trayecto (seleccionable, para poder copiarlo) y, a la derecha, el gráfico **Elevación de antena en función de la distancia al scatter point**. Los números entre corchetes remiten a las ecuaciones del manual de cálculo (`doc/YA-MS_manuale_calcoli.docx`).

## Datos de entrada de esta pestaña

| Campo | Por defecto | Uso |
|---|---|---|
| **Potencia W** | 400 | Potencia del transmisor para el balance del enlace |
| **Ganancia antena dBi (tx = rx)** | 14 | La misma antena en ambos extremos |
| **Señal mínima dBm** | −130 | Señal mínima detectable (artículo: Yagi de 8 elementos + preamplificador) |
| **Densidad estela q = 10^ … electrones/m** | 14 | Densidad lineal de electrones de la estela subdensa |

Las estaciones, la banda, la altura de las estelas, la elevación del lóbulo, el boom y la distancia de los hot spots vienen de las [filas de controles](Getting-Started-es#1-las-tres-filas-de-controles).

## Secciones del informe

| Sección | Contenido |
|---|---|
| **GEOMETRÍA DEL TRAYECTO (Tierra esférica, R = 6372,7955 km)** | Estación y DX con sus alturas; distancia, azimut y azimut inverso; punto medio (locator y coordenadas); altura de las estelas (*<- moda medida por el radar de Collm* cuando se toma del radar); elevación de la antena hacia el punto medio |
| **HOT A / HOT B (hot spots clásicos, para el apuntamiento de la antena)** | Para cada uno: locator, azimut desde tu estación y desplazamiento respecto al trayecto directo, azimut desde el DX, distancia, elevación |
| **LÍMITES DE LA ZONA COMÚN** | Alcance a la altura de las estelas con la elevación del lóbulo; Límite A / Límite B con sus azimuts |
| Antena | Boom en λ, ganancia, lóbulo horizontal / vertical; si Hot A y Hot B están dentro o fuera del lóbulo |
| **ATENUACIÓN DEL TRAYECTO (estela subdensa, McKinley 1961; ganancias de antena excluidas)** | Tabla para el punto medio (forward), Hot A y Hot B en 28, 50, 70, 144, 222 y 432 MHz |
| **BALANCE A … MHz (punto medio)** | Potencia y PIRE, atenuación del trayecto, señal en la antena, mínimo detectable, **margen**; el mismo margen con la atenuación media de OH5IY |
| **REGLAS EXPERIMENTALES ENTRE BANDAS (SM6FHZ, VUSHF 2025)** | Número/intensidad y duración comparados con 144 MHz; ping máximo IARU |

## Locator y trayecto

Locator (4, 6 u 8 caracteres; centro de la cuadrícula, sistema Maidenhead de la IARU) [14]. Distancia, azimut y punto medio con fórmulas de círculo máximo sobre una esfera de radio **r = 6372,7955 km** (artículo Cerrotta–Sartori) [15–16]. Los cálculos que dependen de la hora se refieren al **punto medio**, porque la mejor hora puede diferir hasta 1,5 horas entre los dos extremos (SM6FHZ).

## Elevación de la antena

**Fuente:** fórmula del artículo Cerrotta–Sartori (Figura 7), con x = d/r, siendo d la distancia sobre el suelo hasta el punto de reflexión, H la altura de las estelas y h la altura de la estación [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Verificación:** coincide con la geometría esférica exacta dentro de 0,03°. El programa usa el arcotangente de dos argumentos, que da valores negativos más allá del horizonte y evita el problema de periodicidad mencionado en el artículo. Una elevación negativa hacia el punto medio significa *trayecto más allá del alcance geométrico de un salto único*.

## Alcance del horizonte

Distancia sobre el suelo a la que un rayo con elevación e alcanza la altura H (inversa geométrica de la fórmula anterior) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Verificación:** H = 89,5 km, e = 0° → **1062 km**. En el ejemplo del artículo (JN44BB–IO53RT) el dibujo sitúa los cruces del horizonte a unos 870 km de las estaciones, lo que corresponde a un lóbulo elevado unos 2° (865 km).

## Límites de la zona común

**Fuente:** el artículo localiza los cruces de las curvas donde el horizonte de cada estación encuentra la capa E: los cruces de dos círculos de radio angular ρ = d_H/r centrados en A y B [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

Si 1 − |p0|² < 0, el trayecto es más largo que 2·d_H y las estaciones **no ven ninguna zona común de la capa E**.

**Verificación:** son los **bordes más lejanos** del cielo visto por ambas estaciones, **no puntos a los que apuntar**. En JN70CN–IN78UO (1710 km, azimut 308°) caen a 1062 km de la estación, 37° a la izquierda y a la derecha del trayecto directo, mientras que MSHV sugiere 10°. Por eso se llaman *Límite A* / *Límite B* y se dibujan tenues en el mapa.

## Hot A y Hot B

**Fuente:** las reflexiones se concentran en dos zonas ("hot spots") a unos **50–150 km a cada lado del punto medio**. Es la base de la tabla de desplazamiento de antena del AMS Bulletin n.º 203, retomada por W8WN (desplazamiento de 10° para trayectos de 1500 y 1800 km); MSHV de LZ2HV usa el mismo criterio.

**Decisión:** Hot A y Hot B son los puntos a distancia s del punto medio M, perpendiculares al trayecto (s = 150 km, ajustable de 30 a 400 km); A a la izquierda mirando desde tu estación hacia el DX, B a la derecha [21]. El desplazamiento visto desde la estación es aproximadamente [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verificación:** JN70CN–IN78UO, D = 1710 km: 6,7° con s = 100 km, **10,0° con s = 150 km** (igual que MSHV y AMS/W8WN), 13,2° con s = 200 km.

## Atenuación subdensa

**Fuente:** ecuación de McKinley para estelas subdensas (β = 0, sen α = 1), ganancias de antena excluidas; q = densidad lineal de electrones, r_e = radio clásico del electrón = 2,818·10⁻¹⁵ m, R1, R2 distancias a la estela, φ mitad del ángulo de dispersión [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\cos^2\varphi}{\lambda^3 q^2 r_e^2}\right]\ \mathrm{dB}
```

**Verificación:** con q = 10¹⁴ electrones/m en 144 MHz: **181–192 dB** entre 600 y 2200 km, en línea con las referencias del artículo en 144 MHz: **182 dB como mínimo** (GM8JBJ, de Kaiser & Closs 1952) y **200 dB de media** (OH5IY).

## Balance del enlace

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - 2{.}15 - L + G_{rx} - 2{.}15,\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Las ganancias se introducen en dBi y se usan en dBd (dBi − 2,15). El informe da también el margen con la **atenuación media de OH5IY** (200 dB en 144 MHz, escalada con λ³ a la banda elegida). Referencia del artículo: hacen falta unos **70 dBm de PIRE** (−130 dBm + 200 dB, p. ej. unos 400 W en 14 dBi).

## Ganancia y lóbulo de la antena

**Ganancia – fuente:** curva de Günter Hoch **DL6WU** para Yagis largas en función de la longitud del boom L, citada por W8IO (válida a partir de unas 2 λ) [39]:

```math
G = 7{.}773\,\log_{10}(L/\lambda) + 11{.}43\ \mathrm{dBi}
```

**Verificación con los modelos NEC de L.B. Cebik W4RNL en 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elementos | Boom (λ) | NEC W4RNL (dBi) | Fórmula (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

La diferencia nunca supera **0,1 dB**: la ganancia depende más de la longitud del boom que del diseño (las Yagis VK3AUU tienen un boom más corto con el mismo número de elementos). El Yagi Calculator de VK5DJ da también estimaciones para las variantes VK3AUU, WA2PHW y DJ9BV, cuyas fórmulas no están publicadas.

**Lóbulo – fuente:** regla de Kraus, con lóbulo circular θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Verificación:** los modelos NEC de W4RNL de Yagis DL6WU dan un **lóbulo horizontal un 5–10 % más estrecho** que Kraus: 33,8° / 26,4° / 22,6° para 12, 19 y 26 elementos, frente a 37,3° / 28,0° / 23,9°. Las fórmulas simples ignoran los lóbulos laterales delanteros (W4RNL, *Long-Boom Yagi Rules of Thumb*). En booms largos el lóbulo vertical es algo más ancho que el horizontal (14 λ: 18,4° / 18,8°).

**Decisión** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Ejemplo: Yagi de 14 λ en 432 MHz → 20,3 dBi, lóbulo de 18,1° en horizontal y 19,5° en vertical; los modelos de W4RNL dan 20,4 dBi y 18,4° / 18,8°. Son reglas aproximadas obtenidas de unas pocas antenas DL6WU.

La antena se considera siempre apuntada al DX. Un hot spot está **dentro del lóbulo** si |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: entonces se dibuja en gris en la [Bóveda celeste](Sky-View-es) y aparece un aviso. En el cálculo de la eficiencia las antenas son isótropas; el lóbulo real solo se usa para esta comprobación.

## Reglas experimentales entre bandas

Respecto a 144 MHz: número/intensidad × (144/f)³ (en dB), duración × (144/f)² (SM6FHZ, VUSHF 2025). Duración máxima de los pings según la IARU Región 1: 1000 ms en 50 MHz, 500 ms en 70 MHz, 100 ms en 144 MHz, 13 ms en 432 MHz (VHF Handbook, citado en el artículo). Ver también [Previsiones experimentales](Experimental-Forecasts-es).
