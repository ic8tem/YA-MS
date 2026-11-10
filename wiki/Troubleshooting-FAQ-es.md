[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · **Español** · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-br) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-tw)

# Problemas y preguntas frecuentes

## Instalación y arranque

### Windows SmartScreen dice "Windows protegió su PC"
El programa no está firmado con un certificado comercial. Haz clic en *Más información* → *Ejecutar de todas formas*. Descárgalo solo de la página [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: no se puede abrir porque es de un desarrollador no identificado
YA-MS no está firmado por Apple, así que **Gatekeeper** lo bloquea la primera vez. En el `.dmg`, **clic derecho en "Installa YA-MS.command" → Abrir** y confirma. El script quita de `~/YA-MS/YA-MS.app` la marca de cuarentena "descargado de internet" y lo abre. Si macOS sigue negándose, abre *Ajustes del Sistema → Privacidad y seguridad* y pulsa *Abrir igualmente*.

### macOS: ¿qué .dmg?
`-mac-apple-silicon.dmg` para procesadores M1/M2/M3/M4, `-mac-intel.dmg` para Mac Intel (menú Apple → *Acerca de este Mac* te dice cuál tienes).

### Linux: YA-MS no aparece en el menú de aplicaciones
Ejecuta `./installa.sh` desde la carpeta descomprimida (no desde `~/YA-MS`). Algunos escritorios necesitan cerrar e iniciar sesión para mostrar las entradas nuevas. Siempre puedes iniciarlo con `~/YA-MS/YA-MS`.

### Falta el mapa de Europa
*Mapa de Europa no disponible (se necesita la red en el primer arranque).* El mapa de Natural Earth se descarga en `data/mappa` en el primer arranque. Conéctate a internet y reinicia YA-MS.

## Visualización

### Linux: el texto japonés aparece como cuadraditos
Al sistema le faltan fuentes CJK (chino, japonés, coreano). Instala las fuentes **Noto CJK** y reinicia YA-MS. Lo mismo ocurre con el árabe, el hebreo, el urdu, el hindi y el bengalí: en Debian, Ubuntu y Raspberry Pi OS instala también `fonts-noto-core`.

| Distribución | Comando |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### El texto es demasiado pequeño, o los gráficos no tienen sitio
Usa el regulador **Fuente de letra** (100–300 %) y pliega las filas con **Controles**. Ver [Ajustes](Settings-and-Data-Folder-es#fuente-de-letra-y-controles).

### La pantalla es demasiado luminosa de noche
Elige **Noche** o **Negro** en la lista **Tema**.

## Internet y datos de radar

### Mensaje "Sin conexión a internet"
YA-MS lo muestra **una sola vez** cuando no se puede alcanzar ninguna fuente; la barra de estado se vuelve roja. El programa sigue funcionando con los **últimos datos guardados** y lo vuelve a intentar solo cada 5 minutos; cuando vuelve la red aparece *Conexión restablecida.* No hay que hacer nada.

### Aviso naranja en Flujo radar: "No se puede leer la escala vertical del flujo …"
El radar de Collm cambia su escala vertical cada día y YA-MS la lee de las etiquetas del gráfico. Si una etiqueta no se puede leer, el programa usa la escala calibrada de 0–1200 meteoros/hora y avisa de que hay **valores por verificar**. Normalmente el siguiente gráfico horario se lee bien. Si durante muchas horas ves *Formato del gráfico cambiado* o *Ejes del flujo no encontrados en la posición esperada*, el radar ha cambiado el formato de su gráfico: por favor, [avísalo](Contributing-and-Contacts-es).

### "La escala del gráfico de alturas ha cambiado"
Las estadísticas de alturas (moda, media, mediana) siguen siendo válidas; solo los recuentos absolutos del histograma de alturas dejan de serlo.

### "Flujo radar: sin datos"
Pulsa **Descargar ahora** en [Flujo radar](Radar-Flux-es) y comprueba que `data/fonti_radar.csv` tiene `attivo=1` para Collm.

### RMOB: ¿por qué está desactivada la descarga automática?
RMOB pide que **los programas automáticos no descarguen sus archivos**. Activa la *descarga automática cada 5 minutos* solo después de que RMOB te haya dado permiso. Mientras tanto usa **Descargar RMOB ahora** o **Cargar archivo RMOB desde el disco...**. Ver [Previsiones experimentales](Experimental-Forecasts-es#rmob-y-los-programas-automáticos).

### RMOB: "Formato de archivo no reconocido" o pocas horas leídas
Usa el archivo de texto mensual del observador (`NAME_MMYYYYrmob.TXT`) o una tabla de boletín con un solo observador. El ajuste del exponente necesita al menos 3 horas en común con los datos de Collm (ayer y hoy).

## Cálculos

### "Locator de la estación no válido" / "Locator del corresponsal no válido"
Los locators deben tener 4, 6 u 8 caracteres (p. ej. `JN70`, `JN70CN`, `JN70CN12`).

### "Ninguna zona común de la capa E"
El trayecto es más largo que el doble del alcance a la altura de las estelas (unos 2 × 1062 km con el lóbulo a 0° y estelas a 89,5 km): un único salto de meteor scatter no puede cubrirlo. Subir la **Elevación lóbulo** acorta aún más el alcance.

### Hot A / Hot B aparecen en gris
Ya están **dentro del lóbulo de tu antena** cuando apuntas al DX: no hace falta girarla. Ver [Bóveda celeste](Sky-View-es#avisos).

### La eficiencia es distinta de la de MCG_MS o MS-Soft
YA-MS usa el trayecto real y su propio modelo; la escala de OH5IY y de MCG_MS no está documentada en detalle. Compara horas y tendencias más que porcentajes absolutos, y consulta el [modelo](Efficiency-Calculation-es#el-modelo).

### El paso del haz de GRAVES parece desplazado
La secuencia del haz se calcula con el reloj del PC: sincronízalo con un servidor NTP. Además, la estación de mando de GRAVES desplaza a veces la secuencia unos pasos; el detalle es una predicción que hay que confirmar escuchando.

## Otras preguntas

**¿YA-MS es gratuito?** Sí, es un programa gratuito para radioaficionados.

**¿Controla mi rotor o mi equipo?** No. YA-MS es una herramienta de previsión y planificación; para el QSO usa tu programa de modos digitales (p. ej. MSHV, WSJT-X).

**¿Funciona por encima de 432 MHz?** La lista de bandas llega hasta 432 MHz (28, 50, 70, 144, 222, 432). La previsión experimental acepta cualquier frecuencia de 28 a 1300 MHz, pero las reglas de SM6FHZ que usa proceden de la experiencia en 144 y 432 MHz.

**Algo ha ido mal.** Escribe al autor indicando tu sistema operativo, la versión de YA-MS y lo que hiciste: ver [Contribuir y contactos](Contributing-and-Contacts-es).
