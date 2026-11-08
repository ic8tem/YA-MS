**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Mapa de cuadrículas

*Pestaña: Mapa de cuadrículas.*

[![Mapa de cuadrículas](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Las cuadrículas Maidenhead (4 caracteres) que has **trabajado** y **confirmado**, leídas del archivo ADIF de tu log, sobre un mapa de Europa, con **una subpestaña por banda: 50, 70, 144, 222 y 432 MHz**.

## Controles

| Control | Qué hace |
|---|---|
| **Cargar archivo ADIF...** | Lee un archivo `.adi` / `.adif`. Un ADIF nuevo **sustituye** los datos anteriores. |
| **Borrar memoria** | Borra todas las cuadrículas cargadas del ADIF (pide confirmación). |
| Ratón | **Rueda = zoom, arrastrar = mover, ratón sobre una cuadrícula = QSO** (hasta seis indicativos con fecha, *(confirmado)* cuando está confirmado) |

Tras la carga, el estado muestra *… QSO leídos, … cuadrículas-QSO en las bandas 50-432 MHz, … QSO descartados (otras bandas o sin cuadrícula)*. Cada mapa de banda lleva el rótulo *… cuadrículas trabajadas, … confirmadas*.

| Color | Significado |
|---|---|
| Naranja | trabajada |
| Verde | confirmada (QSL o LoTW) |

## Cómo se lee el ADIF

- Campos usados: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (especificación ADIF).
- Banda tomada de `BAND`, o de la frecuencia: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Una cuadrícula está **confirmada** si al menos un QSO en ella tiene `QSL_RCVD = Y` o `LOTW_QSL_RCVD = Y`.
- Las cuadrículas se conservan en `data/adif_quadrati.csv` hasta que cargues otro archivo o pulses **Borrar memoria**.

YA-MS **no** se conecta a LoTW: exporta el ADIF desde tu programa de log (o desde LoTW) y cárgalo aquí.
