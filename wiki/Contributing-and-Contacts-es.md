**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

# Contribuir y contactos

YA-MS mejora gracias a los informes de quienes lo usan en el aire. Cada corrección se atribuye a su fuente.

## Contactos

| | |
|---|---|
| Autor | Costantino Cerrotta **IC8TEM** |
| Correo electrónico | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Informar de un problema

Abre una **issue en GitHub** o escribe un correo indicando:

- sistema operativo y versión de YA-MS (en el título de la ventana);
- los dos locators, la banda y la hora UTC;
- qué esperabas y qué viste (una captura de pantalla ayuda);
- para los problemas de radar, el mensaje mostrado en la pestaña [Flujo radar](Radar-Flux-es).

## Lo que resulta especialmente útil

- **Informes desde el aire.** Horas y trayectos en los que la eficiencia o la previsión acertaron, o fallaron. El modelo es experimental y necesita compararse con QSO reales y con MCG_MS / MS-Soft.
- **Comparaciones con RMOB.** Valores del factor de estación K y del exponente k que hayas obtenido con la [comparación con RMOB](Experimental-Forecasts-es#comparación-con-rmob), con tu banda y tu estación.
- **Datos con fuente.** Mejores desplazamientos de los radiantes, perfiles de actividad, nuevas fechas de máximos IMO (`data/massimi_imo.csv`), datos de antenas: indica la fuente y se citará.
- **Cambios en los gráficos de radar.** Si cambia el formato del gráfico de Collm, una copia de la imagen (`data/radar/`) ayuda a recalibrar la lectura.

## Traducciones

Las traducciones de la interfaz son archivos de texto plano en **`data/lingue/<code>.txt`** (UTF-8) y **cualquiera puede corregirlas**:

```
<Italian text><TAB><translation>
```

- Una entrada por línea; las líneas que empiezan por `#` son comentarios.
- En ambas columnas los dos caracteres `\n` indican un salto de línea.
- Conserva los marcadores `{0}`, `{1}`, … con su formato (p. ej. `{0:F1}`, `{3:+0;-0}`), en el orden que necesite tu idioma.
- Las entradas que faltan o están vacías se muestran en italiano. La lista de todas las claves es `data/lingue/chiavi.txt` (generada por `tools/estrai_chiavi.py`, no la edites).

Edita el archivo en la carpeta `data/lingue` de tu instalación y reinicia YA-MS (o cambia de idioma) para ver el resultado. Como estos archivos **se sustituyen por versiones más recientes en cada actualización**, **envía también tus correcciones**, por correo o como pull request en GitHub (`data/lingue/`), para que entren en la próxima versión.

Esta wiki existe en English, Русский, Deutsch y 日本語; también son bienvenidas las correcciones a las páginas de la wiki.
