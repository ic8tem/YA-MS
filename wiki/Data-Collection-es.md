[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · **Español** · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Recogida de datos

*Pestaña: En directo y datos en tiempo real › Recogida de datos.*

[![Recogida de datos](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Cuatro fuentes

La pestaña recoge **spots de meteor scatter** de tres flujos telnet y del flujo MQTT de PSKReporter, cada uno en su propia subpestaña:

| Subpestaña | Por defecto | Notas |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Un cluster a elección. En ON0DXK las bandas VHF están filtradas: actívalas con `set/filter dxbm/pass 6` (luego 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Los skimmers raramente decodifican modos MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X que transporta los spots de **PSKReporter**: aquí llegan las decodificaciones MSK144 de WSJT-X y MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spots de PSKReporter en directo por **MQTT** (servicio de M0LTE): sin login, cada spot ya lleva los locators de la estación que transmite y de la que recibe. Temas predeterminados: MSK144 en 6 m, 4 m, 2 m, 1,25 m, 70 cm y FSK441 en 2 m (`pskr/filter/v2/band/mode/#`); *Temas predeterminados* los restablece. |
| **Spots MS recogidos** | – | Tabla de los spots aceptados, los más recientes primero. |

Cada flujo tiene host, puerto, comandos enviados tras el login, *Reconectar*, *Conectar al inicio*, una consola y una línea para enviar comandos. Escribe arriba tu **indicativo para el login**. La fuente MQTT tiene host, puerto, temas (uno por línea o separados por `;`), *Reconectar* y *Conectar al inicio* (desactivado por defecto) y una consola con los spots recibidos; sus spots pasan por el mismo filtro. Una franja muestra el estado de las cuatro fuentes (punto verde = conectada). Las sesiones permanecen abiertas cuando cambias de idioma o de esquema de colores.

## El filtro (40 % de la ventana)

- **Filtro local opcional:** las líneas del cluster por debajo de **27990,0 kHz** se descartan enseguida (no se muestran ni se guardan).
- **1.er criterio – frecuencias MS típicas:** 50190–50300, 70100–70400, 144290–144399 kHz. Un spot en estas ventanas se acepta aunque no lleve el nombre del modo, salvo que el comentario declare otra propagación: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Ventanas y etiquetas se pueden editar.
- **2.º criterio – modos MS:** fuera de las ventanas, o con una de esas etiquetas, un spot solo se conserva si contiene **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (modos digitales usados solo en MS) o **\<MS\>**, en mayúsculas, minúsculas o mezcladas. Las palabras se pueden desactivar, añadir y quitar; cada una tiene su contador.
- **Bandas** 28, 50, 70, 144, 222, 432 MHz; **prueba del filtro** sobre una línea pegada; **contadores**.

## Locators y almacenamiento

Los locators que faltan, o los que solo tienen 4 caracteres, se toman del archivo **CALL3** (`data/call3.txt`, archivo de JTDX, más de un millón de indicativos), que siempre prevalece sobre un locator de 4 caracteres. Los spots aceptados se guardan en `data/spot_ms`, un archivo CSV por día, y alimentan el mapa de [Tráfico en directo](Live-Traffic-es).
