[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · **한국어** · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# 실시간 트래픽

*탭: 라이브 및 실시간 데이터 › 실시간 트래픽.*

[![실시간 트래픽](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## 표시 내용

내 국을 중심으로 한 **방위 등거리 지도**(중심에서의 거리 = 실제 거리, 각도 = 방위)에 [데이터 수집](Data-Collection-ko)이 모은 **모든 유성 산란 트래픽**을 표시합니다. 프로그램은 교신마다 다음을 그립니다:

- 두 국 사이의 **경로**를 밴드 색으로: 28 MHz 갈색, 50 MHz 초록, 70 MHz 청록, 144 MHz 주황, 222 MHz 분홍, 432 MHz 보라;
- 경로 양 끝의 두 **국**;
- **구름**: 그 경로와 그 시각에 가장 가능성 높은 유성 흔적이 모여 있는 곳.

국 하나가 **지도 밖**에 있는 스폿은 버립니다. **방금 도착한** 스폿(3분 이내)은 **1분 동안 깜빡이므로** 새로운 활동이 한눈에 들어옵니다.

수신 중인 국 표시: 밴드 색의 삼각형은 PSKReporter에 따르면 선택한 시간 동안 28, 50, 70, 144, 432 MHz에서 MSK144, FSK441, PSK2K 또는 JTMS를 수신하는 국입니다. 삼각형을 클릭하면 호출부호, 로케이터, 모드와 마지막 스폿이 표시됩니다. "데이터 수집" 탭의 MQTT 흐름이 연결되어 있어야 합니다.

## 구름 계산 방법

프로그램은 스폿마다 두 로케이터 사이의 경로를 만들고(내 경로와 같은 기하. [기하와 경로 손실](Geometry-and-Path-Loss-ko) 참조), 스폿 시각에서 E층의 점마다 **활동 중인 모든 유성우의 정반사 기여**를 ZHR로 가중하여 합산합니다. 이는 [천구](Sky-View-ko)의 **PREV 영역**과 같은 계산입니다. 전체의 15 % 이상을 차지하는 경로의 각 쪽에 대해 구름은 **타원**으로 그립니다: 중심은 점들의 가중 평균, 반축은 분산 고윳값의 제곱근의 1.5배, 장축은 주 고유벡터 방향입니다. 기여하는 유성우가 없으면(산발 유성만 있는 경우) 구름은 고전적인 두 **핫스폿**이며 파선으로 그립니다. 전체 수식은 계산 매뉴얼 10장에 있습니다.

## 조작

| 조작 항목 | 의미 |
|---|---|
| **지도 반경** | 내 국에서 600–3500 km. |
| **표시할 스폿** | 최근 15분 또는 30분, 최근 1시간, 최근 3시간, 최근 24시간. |
| **표** | 지도 위의 교신. 최신 순, 밴드 색으로 표시. *구름*은 주된 쪽의 반사 비율 또는 *산발 유성*을 보여 줍니다. |
| **클릭** | 경로나 표의 행을 클릭하면 해당 교신이 강조되고, 상자에 구름 중심의 로케이터, 비율, 크기, 축이 표시됩니다. |
