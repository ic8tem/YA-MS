[English](Sources) · [Italiano](Sources-it) · [Deutsch](Sources-de) · [Nederlands](Sources-nl) · [Français](Sources-fr) · **Español** · [Português](Sources-pt) · [Português (Brasil)](Sources-pt-br) · [Dansk](Sources-da) · [Norsk](Sources-nb) · [Svenska](Sources-sv) · [Íslenska](Sources-is) · [Eesti](Sources-et) · [Lietuvių](Sources-lt) · [Latviešu](Sources-lv) · [Polski](Sources-pl) · [Čeština](Sources-cs) · [Magyar](Sources-hu) · [Română](Sources-ro) · [Ελληνικά](Sources-el) · [Русский](Sources-ru) · [Українська](Sources-uk) · [Türkçe](Sources-tr) · [Afrikaans](Sources-af) · [العربية](Sources-ar) · [עברית](Sources-he) · [اردو](Sources-ur) · [हिन्दी](Sources-hi) · [বাংলা](Sources-bn) · [ไทย](Sources-th) · [Bahasa Indonesia](Sources-id) · [Tagalog](Sources-tl) · [日本語](Sources-ja) · [한국어](Sources-ko) · [中文](Sources-zh) · [中文 (繁體)](Sources-zh-tw)

# Fuentes

*Pestaña: Documentos técnicos › Fuentes.*

[![Fuentes](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_1.png)

La pestaña **Fuentes** enumera todas las obras en las que se basa YA-MS, agrupadas como se ve abajo (el texto es seleccionable, para que puedas copiar las referencias). Las mismas fuentes, numeradas, cierran el manual de cálculo (`doc/YA-MS_manuale_calcoli.docx`) y el documento [Explicación del cálculo de la eficiencia](Efficiency-Explanation-es).

## FUENTE PRINCIPAL

| Fuente | Usada para |
|---|---|
| Costantino Cerrotta **IC8TEM**, Gianluigi "Gigi" Sartori **IV3GTH** – *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (artículo en italiano, versión 7) | Estelas en la capa E a unos 90 km (radar SKiYMET), radio terrestre 6372,7955 km, fórmula de la elevación, Hot A / Hot B, side-scatter 10–30°, atenuación del trayecto, señal mínima −130 dBm, duración de los pings IARU, máximo de esporádicos a las 06 UTC |

## CÁLCULO Y TEORÍA DE LA EFICIENCIA

| Fuente | Usada para |
|---|---|
| Ilkka Yrjölä **OH5IY** – MS-Soft, www.kolumbus.fi/oh5iy (sitio histórico) | Concepto de eficiencia de una lluvia; atenuación media del trayecto de 200 dB |
| Wilhelm Rauh **DL5MCG** – MCG_MS, MS Efficiency Calculator v1.61, qsl.net/dl5mcg | Eficiencia en cuatro direcciones fijas (comparación) |
| Ingolf **SM6FHZ** – *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, mayo de 2025 | Reglas λ³ y λ², punto medio, mejor dirección (az del radiante ±90°) |
| D.W.R. **McKinley** – *Meteor Science and Engineering*, McGraw-Hill, 1961 | Reflexión especular, ecuación de la estela subdensa |
| John **GM8JBJ** – Meteor scatter path loss, hamradio.engineering (de Kaiser & Closs 1952) | Atenuación del trayecto de 172–190 dB calculada por John Worsnop **G4BAO** (tesis doctoral), unos 6 dB menos para estelas alineadas con el trayecto; no se usa la tabla de 182 dB de la propia página (ver [Geometría y atenuación](Geometry-and-Path-Loss-es)) |
| Shelby **W8WN** – qsl.net/w8wn/hscw (tabla de desplazamientos del AMS Bulletin 203) | Elevación y desplazamiento óptimos, hot spots a 50–150 km |
| **LZ2HV** – MSHV | Hot A / Hot B (comparación; en el manual) |
| Klaus von der Heide **DJ5HG** – QTFGUI y el manual "QTFGUI Help" (2007) | Ley del cone scattering; caso de prueba Hamburgo – Barcelona con las Cuadrántidas usado para verificar el modelo |
| Jens **DF5HC** – *"Meteorscatter auf UKW"*, conferencia DARC, enero de 2018 | Fórmula de la mejor dirección de **DH9GCD**; cone scattering y elección HOT-A / HOT-B de DJ5HG; radiante útil entre 20 y 70°; mejor distancia 1300–1500 km; meteoros esporádicos según KB0VUK |
| Günter Hoch **DL6WU** – ganancia en función de la longitud del boom de las Yagis largas, citada por W8IO (w8io.com) | G(dBi) = 7.773 log(L/λ) + 11.43 |
| J.D. **Kraus** – *Antennas*, McGraw-Hill | G = 41253 / (θE·θH) |
| L.B. Cebik **W4RNL** – *Long-Boom Yagi Rules of Thumb: A Comparison with Modeling Data*; *Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2* (Yagis VK3AUU de David Tanner) | Simulaciones NEC usadas para verificar la curva de ganancia y corregir el lóbulo horizontal (0,93 × Kraus) |
| John Drew **VK5DJ** – Yagi Calculator | Estimaciones de ganancia para las variantes VK3AUU, WA2PHW y DJ9BV |
| J. **Meeus** – *Astronomical Algorithms*, 2.ª ed., Willmann-Bell, 1998 | Día juliano, tiempo sidéreo, longitud solar, azimut/elevación (en el manual) |

## DATOS DE LAS LLUVIAS

| Fuente | Usada para |
|---|---|
| International Meteor Organization – Meteor Shower Calendar 2026 (y 2027), www.imo.net, tablas 5, 6 y 7 | Radiantes, λ máx, v, r, ZHR, Fuente Antihelio, fechas y horas de los máximos |
| Rossano **IZ5TEK** – www.aripisa.it/images/pdf/scattertek.pdf | Datos de las lluvias |

## DATOS DE RADAR EN DIRECTO

| Fuente | Usada para |
|---|---|
| Radar meteórico de Collm, Universidad de Leipzig (LIM) e IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | Flujo horario de meteoros y alturas de las estelas ([Flujo radar](Radar-Flux-es)) |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | Imagen de los recuentos de meteoros |
| DL1DBC – Swan Meteor Skyview, swan.ms | Referencia para el gráfico de la bóveda celeste |
| SM6FHZ – RadiantCalc | Gráfico polar con la mejor dirección |
| Natural Earth – costas y fronteras a escala 1:50 millones, dominio público, www.naturalearthdata.com | Mapa de Europa |
| RMOB, Radio Meteor Observatories On Line (Pierre Terrier) – www.rmob.org; boletines mensuales rmob.org/rmobtext | Observadores de GRAVES en 143,050 MHz (Planetario de Venecia, Faenza, Rovereto y otros) para la comparación |

## RADAR GRAVES

| Fuente | Usada para |
|---|---|
| Rob Hardenberg **PE1ITR** – *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) y *"Graves Radar Update April 2021"* – pe1itr.com/graves | Sectores, pasos, temporización de los pasos de 0,8 s / 3,2 s |
| Wiki de Bolidozor, "Graves" | Agrupaciones, sectores y tiempos del haz |
| Wikipedia, "GRAVES (system)" | Transmisor en Broye-lès-Pesmes (47,348° N 5,515° E) |

Ver [Radar GRAVES](GRAVES-Radar-es).

## OTRAS REFERENCIAS DEL ARTÍCULO

G3WZT, DH8BQA, geekshed.co.uk, manual de WSJT-X, WB2FKO (pings), IU6GIR (actividad en 143,050 MHz), IARU Region 1 VHF Handbook.

## Constantes con su fuente

`data/regole_sperimentali.csv` enumera las constantes y reglas usadas por el programa, cada una con su fuente (altura típica de las estelas, intervalo de alturas, radio terrestre, reglas λ³ / λ², duración de los pings IARU, atenuaciones del trayecto, señal mínima, PIRE orientativa, máximo de esporádicos, distancias útiles en 432 MHz, mejor dirección, elevación máxima útil del radiante en 432 MHz, side-scatter).

> Los datos de radar pertenecen a sus instituciones. Hay que pedir permiso antes de descargarlos automáticamente desde un programa distribuido.
