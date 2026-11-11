[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · **Português (Brasil)** · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Instalação

Todos os pacotes estão na página **[Releases](https://github.com/ic8tem/YA-MS/releases)** (nos nomes de arquivo abaixo `x.y.z` é a versão, p. ex. `1.2.0`). Não é preciso compilar nada nem instalar mais nada: cada pacote contém o runtime do .NET 8.

| Sistema | Arquivo | Instala-se em |
|---|---|---|
| Windows (64 bits) | `YA-MS-x.y.z-windows-x64-setup.exe` (instalador) | `C:\YA-MS` |
| Windows (64 bits), portátil | `YA-MS-x.y.z-windows-x64-portatile.zip` | qualquer pasta onde você tenha permissão de escrita |
| Windows (32 bits, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ou `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bits): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (copiado para lá na primeira inicialização) |
| Linux (64 bits), qualquer distribuição | `YA-MS-x.y.z-linux-x64.tar.gz` (portátil ou com `./installa.sh`) | `~/YA-MS` ou qualquer pasta |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bits) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bits) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, pacote Debian | `ya-ms_x.y.z_arm64.deb` (64 bits) ou `ya-ms_x.y.z_armhf.deb` (32 bits) | `~/YA-MS` (copiado para lá na primeira inicialização) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, só a aplicação | `YA-MS-x.y.z-mac-apple-silicon-app.zip` ou `...-mac-intel-app.zip` | a pasta para onde extrair `YA-MS.app` |

**O programa e a sua pasta `data` ficam sempre juntos** na pasta YA-MS: todos os dados e configurações estão lá (nada de AppData nem pastas do sistema). Veja [Configurações e pasta de dados](Settings-and-Data-Folder-pt-br).

## Windows

### Instalador
1. Baixe `YA-MS-x.y.z-windows-x64-setup.exe` e execute-o.
2. Se o **SmartScreen** mostrar "O Windows protegeu o seu PC": *Mais informações* → *Executar mesmo assim* (o programa não está assinado com um certificado comercial).
3. O YA-MS é instalado em **`C:\YA-MS`**, **sem direitos de administrador**, com um ícone no menu Iniciar e, se você marcar a opção, um ícone na área de trabalho.

### Portátil
Extraia `YA-MS-x.y.z-windows-x64-portatile.zip` onde quiser (uma pasta onde você tenha permissão de escrita, não *Arquivos de Programas*) e execute `YA-MS.exe`. Você pode copiar a pasta inteira para um pendrive ou para outro computador.

## Linux

1. Extraia `YA-MS-x.y.z-linux-x64.tar.gz`.
2. A partir da pasta extraída execute:
   ```sh
   ./installa.sh
   ```
3. O script copia o YA-MS para **`~/YA-MS`** (não é preciso root) e acrescenta o **YA-MS** ao menu de aplicações (categoria *HamRadio*). Você também pode iniciá-lo com `~/YA-MS/YA-MS`.

### Pacote Debian (.deb)
No Debian, Ubuntu, Mint e Raspberry Pi OS você também pode instalar `ya-ms_x.y.z_amd64.deb` (`_arm64.deb` / `_armhf.deb` no Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
O pacote coloca o programa em `/opt/ya-ms` e acrescenta o **YA-MS** ao menu. Na primeira inicialização (e após cada nova versão) ele se copia para **`~/YA-MS`** e roda a partir daí, para que a pasta `data` fique ao lado do programa e as suas configurações sejam mantidas.

### Portátil
O `.tar.gz` também funciona sem instalação: extraia-o para qualquer local onde você tenha permissão de escrita e execute `./YA-MS` a partir dessa pasta.

Para o texto japonês podem ser necessárias as fontes Noto CJK: veja [Problemas](Troubleshooting-FAQ-pt-br#linux-o-texto-japonês-aparece-como-quadradinhos).

## Raspberry Pi

Mesmo procedimento do Linux: extraia `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (ou `-32bit` no Raspberry Pi OS de 32 bits) e execute `./installa.sh` a partir da pasta extraída.

- Para saber qual sistema você tem, digite `uname -m` em um terminal: `aarch64` → pacote de 64 bits, `armv7l` → pacote de 32 bits.
- Suportados: Raspberry Pi 2 (só 32 bits), 3, 4, 5, 400 e 500, com a versão desktop do Raspberry Pi OS. **Não suportados:** Pi Zero / Zero W e Pi 1 (processador ARMv6, o .NET não funciona aí); o Pi Zero 2 W funciona com o pacote de 64 bits, mas 512 MB de RAM é pouco.
- Recomenda-se um Pi 4 ou 5 com pelo menos 2 GB de RAM; a primeira inicialização demora alguns segundos mais do que em um PC.

## macOS

1. Escolha o arquivo certo: `-mac-apple-silicon.dmg` para processadores M1/M2/M3/M4, `-mac-intel.dmg` para Macs Intel.
2. Abra o `.dmg`, **clique com o botão direito em "Installa YA-MS.command" → Abrir** e confirme.
3. O script copia `YA-MS.app` para **`~/YA-MS`** e o abre.

Como alternativa, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` contém apenas `YA-MS.app`: extraia-o para uma pasta à sua escolha (onde você tenha permissão de escrita); a pasta `data` é criada ao lado de `YA-MS.app`. Na primeira vez, clique com o botão direito → **Abrir**.

O programa não está assinado pela Apple, por isso na primeira vez o macOS pede confirmação; veja [Problemas](Troubleshooting-FAQ-pt-br#macos-não-é-possível-abrir-porque-é-de-um-desenvolvedor-não-identificado).

## Primeira inicialização

- O **mapa da Europa** (costas e fronteiras do Natural Earth) é baixado automaticamente para `data/mappa` na primeira vez: é necessária conexão com a internet uma única vez.
- Os **dados de radar** (Collm, Sodankylä) são baixados imediatamente e depois verificados a cada 5 minutos.
- A interface inicia no idioma do sistema se for um dos 36 disponíveis; caso contrário, em italiano; ele pode ser alterado no canto superior direito (veja [Configurações](Settings-and-Data-Folder-pt-br#idioma)).

## Atualização

Instale a nova versão **sobre a anterior** (mesmo instalador, mesma pasta). As configurações (`config.ini`), os arquivos do fluxo e o mapa ficam em `data`. Os arquivos de tradução em `data/lingue` são substituídos quando os novos são mais recentes.

**A partir da 1.8.0, o YA-MS se atualiza sozinho.** Ao iniciar, uma vez por dia, verifica no GitHub se há uma versão nova e a oferece; o botão **Atualizações** na barra inferior faz a verificação manualmente. *Atualizar agora* baixa o pacote portátil do seu sistema, substitui os arquivos do programa, mantém a pasta `data` (os arquivos do programa que mudam são antes copiados para `data/backup/v<versão antiga>`) e reinicia; é preciso poder gravar na pasta do programa. Se ao iniciar faltarem arquivos do programa (em `data` ou `doc`), uma janela os lista e oferece baixá-los de novo do GitHub. Para não procurar versões novas coloque `controlla_aggiornamenti=0` em `config.ini`.

## Compilar a partir do código-fonte (só para desenvolvedores)

Os instaladores são gerados pelo GitHub Actions (`.github/workflows/build.yml`) a cada atualização do branch `release` (versão lida do arquivo `VERSION`), que também cria a release `vX.Y.Z`. Localmente:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # ou linux-x64, linux-arm64, linux-arm, osx-arm64
```

Os documentos (todos os idiomas) são regenerados com `tools/build_documenti.sh`.

Próximo: [Primeiros passos](Getting-Started-pt-br).
