[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · **한국어** · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# 실시간 트래픽

*탭: 라이브 및 실시간 데이터 › 실시간 트래픽.*

[![실시간 트래픽](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## 표시 내용

내 국을 중심으로 한 **방위 등거리 지도**(중심에서의 거리 = 실제 거리, 각도 = 방위)에 [데이터 수집](Data-Collection-ko)이 모은 **모든 유성 산란 트래픽**을 표시합니다. 프로그램은 교신마다 다음을 그립니다:

- 두 국 사이의 **경로**를 밴드 색으로: 28 MHz 갈색, 50 MHz 초록, 70 MHz 청록, 144 MHz 주황, 222 MHz 분홍, 432 MHz 보라;
- 경로 양 끝의 두 **국**;
- **유성우 구역**: 그 경로와 그 시각에 가장 가능성 높은 유성 흔적이 모여 있는 곳.

국 하나가 **지도 밖**에 있는 스폿은 버립니다. **방금 도착한** 스폿(3분 이내)은 **1분 동안 깜빡이므로** 새로운 활동이 한눈에 들어옵니다.

수신 중인 국 표시: 밴드 색의 삼각형은 PSKReporter에 따르면 선택한 시간 동안 28, 50, 70, 144, 432 MHz에서 MSK144, FSK441, PSK2K 또는 JTMS를 수신하는 국입니다. 삼각형을 클릭하면 호출부호, 로케이터, 모드와 마지막 스폿이 표시됩니다. "데이터 수집" 탭의 MQTT 흐름이 연결되어 있어야 합니다.

PSKReporter 지도의 활성 모니터도 표시: pskreporter.info 지도에 MSK144, FSK441, PSK2K 또는 JTMS로 나타나지만 아직 스팟을 받지 않은 국은 빈 삼각형으로 표시합니다 (MQTT는 무언가를 수신한 국만 보냅니다). YA-MS는 서비스 규칙에 따라 모든 모드에 대해 5분마다 한 번 PSKReporter 조회 서비스에 질의합니다. 모니터는 지도에 최소 11분간 남습니다. 삼각형을 클릭하면 호출부호, 로케이터, 디코딩 프로그램과 모니터가 활성이었던 시각이 표시됩니다. 기본으로 켜짐.

평행 경로가 없는 1100 km 초과 FT8: 1100 km 이상 떨어진 국 사이의 FT8 스팟(PSKReporter MQTT, 클러스터 또는 UDP를 통한 WSJT-X에서)으로, 앞뒤 3분 안에 평행 경로(같은 밴드, 중점 300 km 이내, 방향 15° 이내, 다른 국 쌍)가 없는 것은 연한 녹색으로 그려지고 오른쪽 아래 표의 해당 행은 항상 깜박입니다. 스포라딕 E와 대류권 전파는 가깝고 평행한 경로를 많이 만듭니다. 고립된 스팟은 유성 흔적일 수 있습니다. 이를 위해 YA-MS는 MQTT에서 6 m, 4 m, 2 m, 1.25 m, 70 cm의 FT8 스팟도 받습니다(28 MHz는 어떤 경우에도 제외). 이 스팟은 MS 보관소에 들어가지 않습니다. 기본으로 켜짐. PSKReporter MQTT를 이용한 추가 확인: 수신국이 MQTT에서 3분 안에 같은 밴드로 1100 km 넘는 다른 국을 듣고 있으면 그 스팟은 고립된 것이 아닙니다(밴드 열림). 클러스터와 RBN의 스팟은 같은 쌍이 MQTT로도 들어올 때만 인정됩니다. RBN 스키머(«-#» 호출부호)는 인정되지 않습니다.

UDP를 통한 WSJT-X 스팟 가운데 내 국과 관련된 것(디코드에 내 호출부호가 있음: 나를 부르거나 응답하는 국)은 모드와 거리에 관계없이 항상 깜박이는 점선으로 그려집니다.

YA-MS 사용자 간 교환: 다른 YA-MS 사용자가 UDP로 내 국에 보낸 메시지를 디코드하면(MSK144, FSK441, PSK2K, JTMS 또는 1100 km 초과 FT8), 그의 YA-MS가 세 개의 공개 MQTT 브로커(HiveMQ, Mosquitto, EMQX)를 통해 암호화하여 보내 줍니다. 항상 깜박이는 보라색 점선과 UDP 콘솔의 한 줄로 표시됩니다. 나만 읽을 수 있습니다(ECDH P-256 키, AES-256, HMAC-SHA256). FT8 스팟은 3분 안에 평행 경로가 없을 때만 표시합니다. 기본으로 켜짐, data/config.ini의 yams_scambio=0으로 끕니다.

지도에는 각 스팟의 양쪽 국 호출부호가 국마다 한 번씩 표시됩니다. 투영은 방위 정거(내 국이 중심)와 메르카토르 중에서 고를 수 있습니다. 유성우 구역 열의 도움말이 그 의미를 설명합니다.

데이터 수집에서 선택하지 않은 밴드를 포함해 모든 밴드의 스팟이 표시됩니다(이것들은 저장되지 않습니다). CW 스팟과 너무 가까운 국 사이의 스팟은 데이터 수집에서 버리도록 설정되어 있으면 표시되지 않습니다.

## 유성우 구역 계산 방법

프로그램은 스폿마다 두 로케이터 사이의 경로를 만들고(내 경로와 같은 기하. [기하와 경로 손실](Geometry-and-Path-Loss-ko) 참조), 스폿 시각에서 E층의 점마다 **활동 중인 모든 유성우의 정반사 기여**를 ZHR로 가중하여 합산합니다. 이는 [천구](Sky-View-ko)의 **PREV 영역**과 같은 계산입니다. 전체의 15 % 이상을 차지하는 경로의 각 쪽에 대해 유성우 구역은 **타원**으로 그립니다: 중심은 점들의 가중 평균, 반축은 분산 고윳값의 제곱근의 1.5배, 장축은 주 고유벡터 방향입니다. 기여하는 유성우가 없으면(산발 유성만 있는 경우) 유성우 구역은 고전적인 두 **핫스폿**이며 파선으로 그립니다. 전체 수식은 계산 매뉴얼 10장에 있습니다.

## 조작

| 조작 항목 | 의미 |
|---|---|
| **지도 반경** | 내 국에서 600–3500 km. |
| **표시할 스폿** | 최근 15분 또는 30분, 최근 1시간, 최근 3시간, 최근 24시간. |
| **표** | 지도 위의 교신. 최신 순, 밴드 색으로 표시. *% 유성우*은 주된 쪽의 반사 비율 또는 *산발 유성*을 보여 줍니다. |
| **클릭** | 경로나 표의 행을 클릭하면 해당 교신이 강조되고, 상자에 유성우 구역 중심의 로케이터, 비율, 크기, 축이 표시됩니다. |
