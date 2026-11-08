[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · **한국어** · [中文](Troubleshooting-FAQ-zh)

# 문제 해결과 FAQ

## 설치와 시작

### Windows SmartScreen이 "Windows protected your PC"를 표시함
프로그램이 상용 인증서로 서명되어 있지 않기 때문입니다. *More info* → *Run anyway*를 클릭하세요. 프로그램은 [Releases](https://github.com/ic8tem/YA-MS/releases) 페이지에서만 다운로드하세요.

### macOS: 확인되지 않은 개발자의 앱이라 열 수 없음
YA-MS는 Apple 서명을 받지 않았으므로 처음에는 **Gatekeeper**가 차단합니다. `.dmg`에서 **"Installa YA-MS.command"를 오른쪽 클릭 → Open**을 선택하고 확인하세요. 스크립트가 `~/YA-MS/YA-MS.app`에서 "인터넷에서 다운로드됨" 격리 플래그를 제거하고 실행합니다. 그래도 macOS가 거부하면 *System Settings → Privacy & Security*를 열고 *Open Anyway*를 누르세요.

### macOS: 어떤 .dmg를 써야 하나?
M1/M2/M3/M4 프로세서는 `-mac-apple-silicon.dmg`, Intel Mac은 `-mac-intel.dmg`입니다(Apple 메뉴 → *About This Mac*에서 확인).

### Linux: 애플리케이션 메뉴에 YA-MS가 없음
압축 해제한 폴더에서 `./installa.sh`를 실행하세요(`~/YA-MS`에서가 아니라). 일부 데스크톱은 새 항목을 표시하려면 로그아웃/로그인이 필요합니다. 언제든 `~/YA-MS/YA-MS`로 실행할 수 있습니다.

### 유럽 지도가 없음
*유럽 지도를 사용할 수 없습니다 (첫 실행 시 네트워크 필요).* Natural Earth 지도는 첫 실행 시 `data/mappa`에 다운로드됩니다. 인터넷에 연결하고 YA-MS를 다시 시작하세요.

## 화면 표시

### Linux: 일본어 문자가 네모로 표시됨
시스템에 CJK 글꼴이 없습니다. **Noto CJK** 글꼴을 설치하고 YA-MS를 다시 시작하세요:

| 배포판 | 명령 |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### 글자가 너무 작거나 그래프 공간이 부족함
**글꼴** 슬라이더(100–300 %)를 사용하고 **조작**으로 조작 항목을 접으세요. [설정](Settings-and-Data-Folder-ko#글꼴과-조작)을 참조하세요.

### 밤에 화면이 너무 밝음
**테마** 목록에서 **야간** 또는 **검정**을 고르세요.

## 인터넷과 레이더 데이터

### "인터넷 연결이 없습니다" 메시지
어떤 소스에도 접속할 수 없을 때 YA-MS가 **한 번** 표시하며, 상태 표시줄이 빨간색이 됩니다. 프로그램은 **마지막으로 저장된 데이터**로 계속 동작하고 5분마다 자동으로 재시도합니다. 네트워크가 돌아오면 *연결이 복구되었습니다.*가 표시됩니다. 따로 할 일은 없습니다.

### 레이더 플럭스의 주황색 경고: "플럭스 세로 눈금을 읽을 수 없습니다 …"
Collm 레이더는 세로 눈금을 매일 바꾸고, YA-MS는 그래프 레이블에서 그 눈금을 읽습니다. 레이블을 읽지 못하면 보정된 눈금 0–1200 유성/시간을 사용하고 **값을 확인해야 한다**고 경고합니다. 보통 다음 시간의 그래프는 정상적으로 읽힙니다. 여러 시간 동안 *그래프 형식이 바뀌었습니다* 또는 *플럭스 축을 예상 위치에서 찾지 못했습니다*가 보이면 레이더가 그래프 형식을 바꾼 것이니 [알려 주세요](Contributing-and-Contacts-ko).

### "고도 그래프의 눈금이 바뀌었습니다"
고도 통계(최빈값, 평균, 중앙값)는 유효하며, 고도 히스토그램의 절대 계수만 유효하지 않습니다.

### "레이더 플럭스: 데이터 없음"
[레이더 플럭스](Radar-Flux-ko)에서 **지금 다운로드**를 누르고, `data/fonti_radar.csv`에서 Collm이 `attivo=1`인지 확인하세요.

### RMOB: 자동 다운로드가 왜 꺼져 있나?
RMOB는 **자동 프로그램이 파일을 가져가지 않도록** 요청합니다. RMOB에서 허가를 받은 뒤에만 *5분마다 자동 다운로드*를 켜세요. 그동안은 **지금 RMOB 다운로드** 또는 **디스크에서 RMOB 파일 불러오기...**를 사용하세요. [예보 실험 적용](Experimental-Forecasts-ko#rmob와-자동-프로그램)을 참조하세요.

### RMOB: "파일 형식을 인식하지 못했습니다" 또는 읽은 시간이 적음
관측자의 월간 텍스트 파일(`NAME_MMYYYYrmob.TXT`) 또는 관측자가 하나인 회보 표를 사용하세요. 지수 맞추기에는 Collm 데이터(어제와 오늘)와 겹치는 시간이 최소 3시간 필요합니다.

## 계산

### "내 국 로케이터가 잘못되었습니다" / "상대국 로케이터가 잘못되었습니다"
로케이터는 4, 6 또는 8자리여야 합니다(예: `JN70`, `JN70CN`, `JN70CN12`).

### "E층 공통 영역 없음"
경로가 흔적 고도에서의 도달 거리의 두 배보다 깁니다(로브 0°, 흔적 89.5 km에서 약 2 × 1062 km): 유성 산란 단일 홉으로는 커버할 수 없습니다. **로브 앙각**을 올리면 도달 거리가 더 짧아집니다.

### Hot A / Hot B가 회색임
DX를 향했을 때 이미 **안테나 로브 안**에 있습니다: 안테나를 돌릴 필요가 없습니다. [천구](Sky-View-ko#경고)를 참조하세요.

### 효율이 MCG_MS나 MS-Soft와 다름
YA-MS는 실제 경로와 자체 모델을 사용합니다. OH5IY와 MCG_MS의 눈금은 자세히 문서화되어 있지 않습니다. 절대 백분율보다 시간대와 경향을 비교하고, [모델](Efficiency-Calculation-ko#모델)을 참조하세요.

### GRAVES 빔 통과가 어긋나 보임
빔 시퀀스는 PC 시계로 계산하므로 NTP 서버와 동기화하세요. GRAVES 지휘소가 시퀀스를 몇 스텝 옮기는 경우도 있으므로 상세 표시는 수신으로 확인해야 하는 예측입니다.

## 기타 질문

**YA-MS는 무료인가요?** 네, 아마추어 무선사를 위한 무료 프로그램입니다.

**로테이터나 무전기를 제어하나요?** 아니요. YA-MS는 예보와 계획 도구입니다. QSO에는 디지털 모드 프로그램(예: MSHV, WSJT-X)을 사용하세요.

**432 MHz보다 높은 주파수에서도 동작하나요?** 밴드 목록은 432 MHz까지입니다(28, 50, 70, 144, 222, 432). 실험적 예보는 28–1300 MHz의 어떤 주파수든 받지만, 사용하는 SM6FHZ 규칙은 144 MHz와 432 MHz의 경험에서 나온 것입니다.

**문제가 생겼어요.** 운영 체제, YA-MS 버전, 수행한 작업을 적어 작성자에게 보내 주세요: [기여와 연락처](Contributing-and-Contacts-ko)를 참조하세요.
