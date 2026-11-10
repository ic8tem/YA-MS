[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · **한국어** · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# 데이터 수집

*탭: 라이브 및 실시간 데이터 › 데이터 수집.*

[![데이터 수집](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## 네 가지 소스

이 탭은 세 개의 텔넷 스트림과 PSKReporter MQTT 피드에서 **유성 산란 스폿**을 수집하며, 각 소스는 별도의 하위 탭에 있습니다:

| 하위 탭 | 기본값 | 비고 |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | 사용자 지정 클러스터. ON0DXK에서는 VHF 밴드가 필터링되어 있으므로 `set/filter dxbm/pass 6`(이어서 4, 2…)으로 활성화하세요. |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network(7000 = CW/RTTY, 7001 = FT8). 스키머가 MS 모드를 디코드하는 일은 드뭅니다. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | **PSKReporter** 스폿을 전달하는 DM4X 클러스터: WSJT-X와 MSHV의 MSK144 디코드가 여기로 들어옵니다. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | **MQTT**를 통한 PSKReporter 실시간 스폿(M0LTE의 서비스): 로그인이 필요 없고, 각 스폿에는 송신국과 수신국의 로케이터가 이미 들어 있습니다. 기본 토픽: 6 m, 4 m, 2 m, 1.25 m, 70 cm의 MSK144와 2 m의 FSK441(`pskr/filter/v2/band/mode/#`). *기본 토픽*으로 복원합니다. |
| **수집된 MS 스폿** | – | 수락된 스폿의 표, 최신 항목이 위. |

각 스트림에는 호스트, 포트, 로그인 후 보낼 명령, *재연결*, *시작 시 연결*, 콘솔, 명령 입력 줄이 있습니다. 맨 위에 **로그인용 호출부호**를 입력하세요. MQTT 소스에는 호스트, 포트, 토픽(한 줄에 하나 또는 `;`로 구분), *재연결*과 *시작 시 연결*(기본값은 꺼짐), 수신한 스폿을 보여 주는 콘솔이 있으며, 그 스폿도 같은 필터를 거칩니다. 띠 표시줄이 네 소스의 상태(초록 점 = 연결됨)를 보여 줍니다. 언어나 색 구성을 바꿔도 세션은 열린 채로 유지됩니다.

## 필터 (창의 40 %)

- **선택적 로컬 필터:** **27990.0 kHz** 미만의 클러스터 줄은 즉시 버립니다(표시하지도 저장하지도 않음).
- **1차 기준 – MS 대표 주파수:** 50190–50300, 70100–70400, 144290–144399 kHz. 이 창 안의 스폿은 모드 이름이 없어도 수락합니다. 단, 코멘트에 다른 전파 모드가 표시된 경우는 예외입니다: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. 창과 태그는 편집할 수 있습니다.
- **2차 기준 – MS 모드:** 창 밖이거나 위 태그 중 하나가 있으면, **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M**(MS 전용 디지털 모드) 또는 **\<MS\>**를 대문자, 소문자, 혼합 어느 형태로든 포함할 때만 스폿을 유지합니다. 단어는 끄거나 추가·삭제할 수 있고 각각 카운터가 있습니다.
- **밴드** 28, 50, 70, 144, 222, 432 MHz; 붙여 넣은 줄에 대한 **필터 테스트**; **카운터**.

## 로케이터와 저장

로케이터가 없거나 4자리뿐인 경우 **CALL3** 아카이브(`data/call3.txt`, JTDX 파일, 호출부호 100만 개 이상)에서 가져오며, 이 값이 항상 4자리 로케이터보다 우선합니다. 수락된 스폿은 `data/spot_ms`에 하루 하나의 CSV 파일로 저장되고 [실시간 트래픽](Live-Traffic-ko) 지도에 쓰입니다.
