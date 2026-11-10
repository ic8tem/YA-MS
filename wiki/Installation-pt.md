[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · **Português** · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [ไทย](Installation-th) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalação

Todos os pacotes estão na página **[Releases](https://github.com/ic8tem/YA-MS/releases)** (nos nomes de ficheiro abaixo `x.y.z` é a versão, p. ex. `1.2.0`). Não é preciso compilar nada nem instalar mais nada: cada pacote contém o runtime do .NET 8.

| Sistema | Ficheiro | Instala-se em |
|---|---|---|
| Windows (64 bits) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalador) | `C:\YA-MS` |
| Windows (64 bits), portátil | `YA-MS-x.y.z-windows-x64-portatile.zip` | qualquer pasta onde possa escrever |
| Windows (32 bits, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ou `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bits) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bits) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bits) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**O programa e a sua pasta `data` ficam sempre juntos** na pasta YA-MS: todos os dados e definições estão lá (nada de AppData nem pastas do sistema). Ver [Definições e pasta de dados](Settings-and-Data-Folder-pt).

## Windows

### Instalador
1. Descarregue `YA-MS-x.y.z-windows-x64-setup.exe` e execute-o.
2. Se o **SmartScreen** mostrar "O Windows protegeu o seu PC": *Mais informações* → *Executar mesmo assim* (o programa não está assinado com um certificado comercial).
3. O YA-MS é instalado em **`C:\YA-MS`**, **sem direitos de administrador**, com um ícone no menu Iniciar e, se o assinalar, um ícone no ambiente de trabalho.

### Portátil
Extraia `YA-MS-x.y.z-windows-x64-portatile.zip` onde quiser (uma pasta onde possa escrever, não *Programas*) e execute `YA-MS.exe`. Pode copiar a pasta inteira para uma pen USB ou para outro computador.

## Linux

1. Extraia `YA-MS-x.y.z-linux-x64.tar.gz`.
2. A partir da pasta extraída execute:
   ```sh
   ./installa.sh
   ```
3. O script copia o YA-MS para **`~/YA-MS`** (não é preciso root) e acrescenta o **YA-MS** ao menu de aplicações (categoria *HamRadio*). Também o pode iniciar com `~/YA-MS/YA-MS`.

Para o texto japonês podem ser necessárias as fontes Noto CJK: ver [Problemas](Troubleshooting-FAQ-pt#linux-o-texto-japonês-aparece-como-quadradinhos).

## Raspberry Pi

Mesmo procedimento do Linux: extraia `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (ou `-32bit` no Raspberry Pi OS de 32 bits) e execute `./installa.sh` a partir da pasta extraída.

- Para saber que sistema tem, escreva `uname -m` num terminal: `aarch64` → pacote de 64 bits, `armv7l` → pacote de 32 bits.
- Suportados: Raspberry Pi 2 (só 32 bits), 3, 4, 5, 400 e 500, com a versão de ambiente de trabalho do Raspberry Pi OS. **Não suportados:** Pi Zero / Zero W e Pi 1 (processador ARMv6, o .NET não funciona aí); o Pi Zero 2 W funciona com o pacote de 64 bits, mas 512 MB de RAM são pouco.
- Recomenda-se um Pi 4 ou 5 com pelo menos 2 GB de RAM; o primeiro arranque demora alguns segundos mais do que num PC.

## macOS

1. Escolha o ficheiro certo: `-mac-apple-silicon.dmg` para processadores M1/M2/M3/M4, `-mac-intel.dmg` para Macs Intel.
2. Abra o `.dmg`, **clique direito em "Installa YA-MS.command" → Abrir** e confirme.
3. O script copia `YA-MS.app` para **`~/YA-MS`** e abre-o.

O programa não está assinado pela Apple, por isso na primeira vez o macOS pede confirmação; ver [Problemas](Troubleshooting-FAQ-pt#macos-não-é-possível-abrir-porque-é-de-um-programador-não-identificado).

## Primeiro arranque

- O **mapa da Europa** (costas e fronteiras do Natural Earth) é descarregado automaticamente para `data/mappa` na primeira vez: é necessária ligação à internet uma única vez.
- Os **dados de radar** (Collm, Sodankylä) são descarregados de imediato e depois verificados a cada 5 minutos.
- A interface arranca no idioma do sistema se for um dos seis disponíveis; caso contrário, em italiano; muda-se no canto superior direito (ver [Definições](Settings-and-Data-Folder-pt#idioma)).

## Atualização

Instale a nova versão **por cima da anterior** (mesmo instalador, mesma pasta). As definições (`config.ini`), os arquivos do fluxo e o mapa ficam em `data`. Os ficheiros de tradução em `data/lingue` são substituídos quando os novos são mais recentes.

## Compilar a partir do código-fonte (só para programadores)

Os instaladores são gerados pelo GitHub Actions (`.github/workflows/build.yml`) a cada atualização do ramo `release` (versão lida do ficheiro `VERSION`), que também cria a release `vX.Y.Z`. Localmente:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # ou linux-x64, linux-arm64, linux-arm, osx-arm64
```

Os documentos são regenerados com `tools/build_spiegazione.py data` e `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Seguinte: [Primeiros passos](Getting-Started-pt).
