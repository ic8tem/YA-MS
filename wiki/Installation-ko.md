[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · **한국어** · [中文](Installation-zh)

# 설치

모든 패키지는 **[Releases](https://github.com/ic8tem/YA-MS/releases)** 페이지에 있습니다(아래 파일 이름에서 `x.y.z`는 버전, 예: `1.2.0`). 컴파일할 것도, 따로 설치할 것도 없습니다. 각 패키지에 .NET 8 런타임이 포함되어 있습니다.

| 시스템 | 파일 | 설치 위치 |
|---|---|---|
| Windows (64비트) | `YA-MS-x.y.z-windows-x64-setup.exe` (설치 프로그램) | `C:\YA-MS` |
| Windows (64비트), 포터블 | `YA-MS-x.y.z-windows-x64-portatile.zip` | 쓰기 권한이 있는 아무 폴더 |
| Windows (32비트, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` 또는 `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64비트): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS`(처음 실행할 때 그곳으로 복사됨) |
| Linux (64비트), 모든 배포판 | `YA-MS-x.y.z-linux-x64.tar.gz`(포터블 또는 `./installa.sh` 사용) | `~/YA-MS` 또는 아무 폴더 |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64비트) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32비트) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian 패키지 | `ya-ms_x.y.z_arm64.deb`(64비트) 또는 `ya-ms_x.y.z_armhf.deb`(32비트) | `~/YA-MS`(처음 실행할 때 그곳으로 복사됨) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, 애플리케이션만 | `YA-MS-x.y.z-mac-apple-silicon-app.zip` 또는 `...-mac-intel-app.zip` | `YA-MS.app`을 압축 해제한 폴더 |

**프로그램과 `data` 폴더는 항상 YA-MS 폴더 안에 함께 있습니다**: 모든 데이터와 설정이 그곳에 있습니다(AppData도 시스템 폴더도 사용하지 않음). [설정과 데이터 폴더](Settings-and-Data-Folder-ko)를 참조하세요.

## Windows

### 설치 프로그램
1. `YA-MS-x.y.z-windows-x64-setup.exe`를 다운로드하여 실행합니다.
2. **SmartScreen**이 "Windows protected your PC"를 표시하면 *More info* → *Run anyway*를 누릅니다(프로그램이 상용 인증서로 서명되어 있지 않기 때문입니다).
3. YA-MS는 **관리자 권한 없이** **`C:\YA-MS`**에 설치되며, 시작 메뉴 아이콘과 (선택하면) 바탕 화면 아이콘이 만들어집니다.

### 포터블
`YA-MS-x.y.z-windows-x64-portatile.zip`을 원하는 곳(쓰기 권한이 있는 폴더, *Program Files*는 제외)에 압축 해제하고 `YA-MS.exe`를 실행합니다. 폴더 전체를 USB 메모리나 다른 컴퓨터로 복사할 수 있습니다.

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz`를 압축 해제합니다.
2. 압축 해제한 폴더에서 다음을 실행합니다:
   ```sh
   ./installa.sh
   ```
3. 스크립트가 YA-MS를 **`~/YA-MS`**에 복사하고(root 불필요) 애플리케이션 메뉴(*HamRadio* 범주)에 **YA-MS**를 추가합니다. `~/YA-MS/YA-MS`로 직접 실행할 수도 있습니다.

### Debian 패키지 (.deb)
Debian, Ubuntu, Mint, Raspberry Pi OS에서는 대신 `ya-ms_x.y.z_amd64.deb`(Raspberry Pi에서는 `_arm64.deb` / `_armhf.deb`)를 설치할 수도 있습니다:
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
패키지는 프로그램을 `/opt/ya-ms`에 설치하고 메뉴에 **YA-MS**를 추가합니다. 처음 실행할 때(그리고 새 버전이 설치될 때마다) 자신을 **`~/YA-MS`**에 복사하고 그곳에서 실행되므로, `data` 폴더가 프로그램 옆에 유지되고 설정도 보존됩니다.

### 포터블
`.tar.gz`는 설치하지 않고도 사용할 수 있습니다: 쓰기 권한이 있는 아무 곳에나 압축 해제하고 그 폴더에서 `./YA-MS`를 실행하세요.

일본어 텍스트를 표시하려면 Noto CJK 글꼴이 필요할 수 있습니다: [문제 해결](Troubleshooting-FAQ-ko#linux-일본어-문자가-네모로-표시됨)을 참조하세요.

## Raspberry Pi

Linux와 같은 절차입니다. `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz`(Raspberry Pi OS 32비트에서는 `-32bit`)를 압축 해제하고 압축 해제한 폴더에서 `./installa.sh`를 실행합니다.

- 시스템 종류는 터미널에서 `uname -m`을 입력하면 알 수 있습니다: `aarch64` → 64비트 패키지, `armv7l` → 32비트 패키지.
- 지원: Raspberry Pi 2(32비트만), 3, 4, 5, 400, 500. Raspberry Pi OS 데스크톱 버전이 필요합니다. **지원하지 않음:** Pi Zero / Zero W와 Pi 1(ARMv6 프로세서에서는 .NET이 동작하지 않음). Pi Zero 2 W는 64비트 패키지로 동작하지만 512 MB RAM은 빠듯합니다.
- RAM 2 GB 이상의 Pi 4 또는 5를 권장합니다. 첫 실행은 PC보다 몇 초 더 걸립니다.

## macOS

1. 알맞은 파일을 고릅니다: M1/M2/M3/M4 프로세서는 `-mac-apple-silicon.dmg`, Intel Mac은 `-mac-intel.dmg`.
2. `.dmg`를 열고 **"Installa YA-MS.command"를 오른쪽 클릭 → Open**을 선택한 뒤 확인합니다.
3. 스크립트가 `YA-MS.app`을 **`~/YA-MS`**에 복사하고 실행합니다.

또는 `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip`을 사용할 수 있습니다. 이 파일에는 `YA-MS.app`만 들어 있습니다: 원하는 폴더(쓰기 권한이 있는 곳)에 압축 해제하면 `data` 폴더가 `YA-MS.app` 옆에 만들어집니다. 처음에는 오른쪽 클릭 → **Open**을 선택하세요.

프로그램이 Apple 서명을 받지 않았으므로 처음에는 macOS가 확인을 요청합니다. [문제 해결](Troubleshooting-FAQ-ko#macos-확인되지-않은-개발자의-앱이라-열-수-없음)을 참조하세요.

## 첫 실행

- **유럽 지도**(Natural Earth 해안선과 국경)는 처음 실행할 때 `data/mappa`에 자동으로 다운로드됩니다. 인터넷 연결은 한 번만 필요합니다.
- **레이더 데이터**(Collm, Sodankylä)는 즉시 다운로드되고 이후 5분마다 확인됩니다.
- 인터페이스는 시스템 언어가 제공되는 6개 언어 중 하나이면 그 언어로, 아니면 이탈리아어로 시작합니다. 오른쪽 위에서 바꿀 수 있습니다([설정](Settings-and-Data-Folder-ko#언어) 참조).

## 업데이트

새 버전을 **기존 버전 위에** 설치합니다(같은 설치 프로그램, 같은 폴더). 설정(`config.ini`), 플럭스 아카이브, 지도는 `data`에 그대로 남습니다. `data/lingue`의 번역 파일은 새 파일이 더 최신이면 교체됩니다.

## 소스에서 빌드 (개발자 전용)

설치 프로그램은 `release` 브랜치가 업데이트될 때마다 GitHub Actions(`.github/workflows/build.yml`)가 만들며(버전은 `VERSION` 파일에서 읽음), 릴리스 `vX.Y.Z`도 함께 생성합니다. 로컬에서는:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # 또는 linux-x64, linux-arm64, linux-arm, osx-arm64
```

문서는 `tools/build_spiegazione.py data`와 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`로 다시 생성합니다.

다음: [시작하기](Getting-Started-ko).
