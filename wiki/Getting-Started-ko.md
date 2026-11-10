[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Português (Brasil)](Getting-Started-pt-br) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Polski](Getting-Started-pl) · [Čeština](Getting-Started-cs) · [Magyar](Getting-Started-hu) · [Română](Getting-Started-ro) · [Ελληνικά](Getting-Started-el) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [ไทย](Getting-Started-th) · [日本語](Getting-Started-ja) · **한국어** · [中文](Getting-Started-zh) · [中文 (繁體)](Getting-Started-zh-tw)

# 시작하기

처음 실행하면 YA-MS는 예제 경로(144 MHz에서 JN70CN → JO62QM)를 보여 줍니다. 내 국에 맞게 설정하는 데는 5분이면 충분합니다.

## 1. 세 줄의 조작 항목

탭 위에는 모든 탭에 공통으로 적용되는 세 줄의 조작 항목이 있습니다. 오른쪽 위의 **조작** 버튼으로 접거나 펼칠 수 있으며(큰 글꼴을 쓸 때 유용), 선택 상태는 기억됩니다.

**1행 – 국과 밴드**

| 조작 항목 | 기능 |
|---|---|
| **내 로케이터** / **고도 m** | 내 Maidenhead 로케이터(4, 6 또는 8자리. 그리드 중심을 사용)와 국의 해발 고도. |
| **상대국** / **고도 m** | 교신하려는 국의 로케이터와 고도. |
| **밴드 MHz** | 28, 50, 70, 144, 222 또는 432 MHz: 안테나 이득과 로브, 플럭스 추정, 링크 버짓에 사용합니다. |
| **계산** | 경로를 다시 계산합니다(E층 샘플링: 몇 초). |
| **안테나 방위** | 내 안테나의 방위: 항상 **DX 방향**(경로의 방위). |
| **글꼴** | 모든 텍스트의 크기, 100–300 %. [설정](Settings-and-Data-Folder-ko#글꼴과-조작)을 참조하세요. |

**2행 – E층과 안테나**

| 조작 항목 | 기능 |
|---|---|
| **흔적 고도 km** + **레이더에서** | 유성 흔적의 고도(기본값 90 km). *레이더에서*를 선택하면 Collm 레이더가 측정한 가장 빈번한 고도(최빈값)를 사용합니다. [레이더 플럭스](Radar-Flux-ko)를 참조하세요. |
| **로브 앙각 °** | 내 안테나 로브의 최저 앙각(0° = 수평선). 두 국 모두에서 이 앙각보다 위로 보이는 E층의 점만 사용합니다. |
| **야기 안테나: 붐 m** | 야기 안테나의 붐 길이. 프로그램은 λ 단위 길이, 이득(DL6WU 곡선), 수평·수직 −3 dB 로브를 표시합니다. [기하와 경로 손실](Geometry-and-Path-Loss-ko#안테나-이득과-로브)을 참조하세요. 2 λ 미만에서는 대략적인 추정입니다. |
| **중간점에서 핫스폿까지 km** | 중간점에서 Hot A와 Hot B까지의 거리, 30–400 km(기본값 150 km, AMS Bulletin 203 / W8WN / MSHV와 같음). |

**3행 – 시각**

| 조작 항목 | 기능 |
|---|---|
| **시각** | UTC 시계. |
| **천구 시각 (±36 h)** | [천구](Sky-View-ko)와 [GRAVES 레이더](GRAVES-Radar-ko) 탭을 15분 단위로 최대 36시간 앞뒤로 옮깁니다. |
| **실시간** | 현재 시각으로 돌아갑니다. |
| **24 h 표의 날짜 (UTC)** | [효율 계산](Efficiency-Calculation-ko)과 GRAVES 타임라인에 표시할 날짜. |

## 2. 내 국과 상대국

1. **내 로케이터**와 **고도 m**를 입력합니다.
2. **상대국**의 로케이터와 고도를 입력하거나, [천구](Sky-View-ko)의 지도를 클릭합니다: **왼쪽 클릭 = 상대국 로케이터**, **오른쪽 클릭 = 내 국 로케이터**.
3. **밴드 MHz**를 고르고 **계산**을 누릅니다.

아래쪽 상태 표시줄에 확인 메시지가 나타납니다: *경로 계산 완료: … km, 반사점 …개를 … s 동안 샘플링*.

## 3. 내 안테나

야기 안테나의 **붐 길이**를 입력합니다. 프로그램이 이득과 로브를 구하고, 안테나를 DX로 향했을 때 Hot A나 Hot B가 이미 **로브 안**에 들어가면 알려 줍니다(이때 회색으로 표시되며 안테나를 돌릴 필요가 없습니다).

## 4. 결과 읽기

| 질문 | 확인할 곳 |
|---|---|
| 지금 어떤 유성우가 내 경로에 도움이 되고, 어느 쪽에서 오는가? | [천구](Sky-View-ko): 유성우 목록, 빨간색 추천 Hot, PREV 영역 |
| 오늘 가장 좋은 시간은? | [효율 계산](Efficiency-Calculation-ko): 요약 카드와 시간별 표 |
| 레이더가 유성을 몇 개나 세고 있는가? | [레이더 플럭스](Radar-Flux-ko) |
| 144 MHz에서 핑을 몇 개나 기대할 수 있는가? | [예보 실험 적용](Experimental-Forecasts-ko) (실험적) |
| 내 국으로 이 경로를 완성할 수 있는가? | [기하와 경로 손실](Geometry-and-Path-Loss-ko): 경로 손실과 마진 |
| 다음 극대는 언제인가? | [유성우](Showers-ko) |
| GRAVES로 시험해 볼 수 있는가? | [GRAVES 레이더](GRAVES-Radar-ko) |

## 실전 규칙 (출처 기반)

- **유성우에 직각으로 향하기**: 가장 좋은 경로는 복사점 방위에 직교합니다. 최적 지향 = 복사점 방위 ±90°, 허용 범위 ±40–50°(SM6FHZ).
- **사이드 스캐터**: 반사가 가장 많이 오는 쪽(A 또는 B)으로 안테나를 10–30° 돌립니다(Cerrotta–Sartori 논문).
- 복사점이 **너무 높거나**(70° 이상) 너무 낮으면(20° 미만) 유효한 흔적이 적습니다(DF5HC, DH9GCD).
- 산발 유성은 **06 UTC** 무렵에 극대가 됩니다(논문; Collm 플럭스로 확인).
- 432 MHz의 유효 거리: 800–2000 km, 최적 약 1400 km(SM6FHZ). 일반적인 최적 거리 1300–1500 km(DF5HC).

다음: [천구](Sky-View-ko).
