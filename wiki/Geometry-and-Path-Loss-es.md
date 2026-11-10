[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · **Español** · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-BR) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-TW)

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

**Fuente:** las reflexiones de los meteoros esporádicos se concentran en dos zonas ("hot spots") a cada lado del punto medio. J. Richardson (AMS), en la tabla citada por DJ5HG (*Die Geometrie von Meteorscatterverbindungen*, 2004), da el desplazamiento de antena respecto al rumbo directo: **13° a 1000 km, 11° a 1250 km, 10° a 1500 y 2000 km**. El AMS Bulletin n.º 203, retomado por W8WN, da 10° a 1500 y 1800 km.

**Decisión:** Hot A y Hot B son los puntos a distancia s del punto medio M, perpendiculares al trayecto. Con *auto (AMS)* marcado (por defecto), s sale del desplazamiento de la tabla de Richardson, interpolado linealmente (13° por debajo de 1000 km, 10° por encima de 2000 km): s = (D/2)·tan(desplazamiento). Sin marcar, s se introduce a mano, de 30 a 400 km (MSHV usa 150 km); A a la izquierda mirando desde tu estación hacia el DX, B a la derecha [21]. El desplazamiento visto desde la estación es aproximadamente [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Verificación:** con la tabla AMS, 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km, igual que los 150 km usados antes y por MSHV; en los trayectos cortos la tabla acerca los hot spots al punto medio.

## Atenuación subdensa

**Fuente:** ecuación de McKinley y Recomendación ITU-R P.843 para estelas subdensas (sen α = 1), ganancias de antena excluidas; q = densidad lineal de electrones, r_e = radio clásico del electrón = 2,818·10⁻¹⁵ m, R1, R2 distancias a la estela, φ mitad del ángulo de dispersión, β ángulo entre la estela y el plano del trayecto, a₁ factor del radio inicial con r₀ en m y h en km (P.843, ec. 4 y 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Decisión:** el balance y la tabla de atenuaciones usan β = 90° (estela que cruza el plano del trayecto, el caso menos favorable: valor prudente) y el balance muestra también el mejor caso, β = 0. r₀ se toma a la altura media de los ecos para la frecuencia, h = 124 − 17 log f (P.843, ec. 15): 0,76 m a 95 km para 50 MHz, 0,40 m a 87 km para 144 MHz, 0,21 m a 79 km para 432 MHz. En 1000 km a₁ vale 0,2 dB en 50 MHz, 0,6 dB en 144 MHz y 1,4 dB en 432 MHz (2,9 dB a 600 km); con los 102 km fijos de DJ5HG serían unos 70 dB en 432 MHz, es decir, ningún eco.

**Verificación:** con q = 10¹⁴ electrones/m, estelas a 89,5 km y β = 0, en 144 MHz: **182–192 dB** entre 600 y 2100 km (185 dB a 1000 km), dentro del intervalo de **172–190 dB** calculado por John Worsnop **G4BAO** en su tesis doctoral, según recoge GM8JBJ. Con β = 90° la atenuación crece 10 dB a 600 km, 13 dB a 1000 km y 16 dB a 2100 km; los **200 dB de media** de OH5IY quedan entre los dos casos. Los 182 dB de la tabla de GM8JBJ no son una confirmación: la tabla no indica frecuencia, sus 86,4 dB por tramo son la pérdida en espacio libre sobre 500 km a 1 MHz (falta el término 20 log f: 129,6 dB en 144 MHz) y sus partidas suman 163,8 dB, no 182; la página no dice ni "mínimo" ni "144 MHz".

## Balance del enlace

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Las ganancias se introducen y se usan en dBi: la atenuación de McKinley se refiere a antenas isótropas, por lo que no se resta la corrección de dipolo de 2,15 dB (PIRE = potencia + ganancia). El informe da también el margen con la **atenuación media de OH5IY** (200 dB en 144 MHz, escalada con λ³ a la banda elegida). Referencia del artículo: hacen falta unos **70 dBm de PIRE** (−130 dBm + 200 dB, p. ej. unos 400 W en 14 dBi).

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
