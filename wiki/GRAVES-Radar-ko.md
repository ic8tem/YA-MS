[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Português (Brasil)](GRAVES-Radar-pt-br) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Polski](GRAVES-Radar-pl) · [Čeština](GRAVES-Radar-cs) · [Magyar](GRAVES-Radar-hu) · [Română](GRAVES-Radar-ro) · [Ελληνικά](GRAVES-Radar-el) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [ไทย](GRAVES-Radar-th) · [日本語](GRAVES-Radar-ja) · **한국어** · [中文](GRAVES-Radar-zh) · [中文 (繁體)](GRAVES-Radar-zh-tw)

# GRAVES 레이더

*탭: 라이브 및 실시간 데이터 › GRAVES 레이더.*

[![GRAVES 레이더](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## GRAVES란

**GRAVES**는 **Broye-lès-Pesmes**(47.348° N 5.515° E, 로케이터 **JN27SI**, 해발 약 200 m; Wikipedia)에서 **143.050 MHz CW**를 송신하는 프랑스의 레이더입니다. GRAVES와 내 국이 모두 볼 수 있는 영역의 유성 흔적이 **전방 산란**으로 그 신호를 내게 반사합니다: 반송파 가까이에서 짧은 *핑*이 들립니다. 143.050 MHz의 **RMOB** 관측자들은 이렇게 유성을 시간별로 세며, 2 m 유성 산란 국에게는 언제나 켜져 있는 무료 시험 신호이기도 합니다.

이 탭은 **GRAVES → 나**를 독립된 유성 산란 경로로 다룹니다: 주 경로와 같은 함수(같은 흔적 고도, 로브 앙각, 핫스폿 거리)로 유성우 효율, 추천 Hot, PREV 영역을 계산한 다음, 그 영역이 **GRAVES 빔 안에** 있는지, 빔이 **언제** 그곳을 비추는지 확인합니다.

## 위쪽 막대

| 조작 항목 | 기능 |
|---|---|
| **지금** | 천구 시각을 실시간으로 되돌립니다(이 탭은 *천구 시각* 슬라이더를 따릅니다). |
| **GRAVES를 DX로 설정** | 상대국이 GRAVES(JN27SI, 고도 200 m)가 되고 주 경로를 다시 계산합니다: 이후 다른 모든 탭이 GRAVES 경로를 표시합니다. |
| **빔 시퀀스** | *스텝당 0.8 s · 주기 4.8 s (PE1ITR 2021)*(기본값) 또는 *스텝당 3.2 s · 주기 19.2 s (PE1ITR 2007)*. |

## 네 개의 카드

| 카드 | 내용 |
|---|---|
| **GRAVES 빔 안의 유효 영역** | *예 · 섹터 X*와 함께 GRAVES에서 본 추천 핫스폿의 방위와 앙각, 스텝(1–6); 또는 *아니오: 섹터 밖* / *아니오: GRAVES 수평선 아래* / *아니오: 빔 위쪽 (약 25°)* |
| **GRAVES → 내 경로의 현재 효율** | 경로 지수 Σ ZHR × 효율, 최적 유성우, 우세한 A/B쪽, *예상 에코 ≈ …/시간*(실험적, 아래 참조) |
| **경로** | GRAVES까지의 거리; 추천 Hot 방향의 안테나(방위와 앙각); GRAVES 직선 방위 |
| **해당 영역의 다음 빔 통과** | *지금 · … s 남음* 또는 *… s 후*, 스텝(예: *B4*), 다음 세 시각(분 안의 초)과 포착되는 흔적의 비율 |

그 순간 유효한 유성우가 없으면 프로그램은 **빔에 가장 알맞은** 핫스폿(섹터 안, 남쪽에 가장 가까운 것)을 표시하고 그렇다고 알립니다.

## GRAVES에서 본 하늘

PE1ITR와 Bolidozor wiki에 따르면 **네 개의 위상 배열 안테나**가 방위 **90°에서 270°**까지 남쪽 하늘을 네 개의 **45° 섹터**로 덮습니다:

| 섹터 | GRAVES 기준 방위 |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

각 섹터는 **7.5° 폭의 6개 스텝**으로 나뉘며, 가장 낮은 방위부터 1에서 6까지 번호가 매겨지고, **네 섹터 모두에서 같은 순간에** 차례로 비춰집니다. 빔의 **앙각 폭은 약 25°**입니다: 흔적 고도에서 두 파선 원 사이의 색칠된 고리(*빔 수평선*)를 덮습니다. 그림에서 주황/분홍 점 = GRAVES → 나 경로의 PREV 영역, 초록 선 = 내 국 방향, 빨간 선 = 내 국에서 추천 핫스폿까지이며, 지금 비춰지는 스텝이 강조됩니다.

## 시간순 재구성

*시간순 재구성 · 날짜 UTC*(24 h 표와 같은 날): 각 시간마다 GRAVES → 내 경로 효율, 가장 유리한 유성우, 유효 시간대(*hh:00 → hh:00 UTC · n h*)를 최대값(*최대 Σ … (hh:30)*)과 빨간 *지금* 표시와 함께 보여 줍니다. 아래에는 **다음 몇 초의 상세**: 섹터의 여섯 스텝, 유효 영역을 비추는 스텝, *에코 가능 (흔적 +0.3 s)*이 표시됩니다.

### 빔 타이밍

시퀀스는 **UTC**에 묶여 있습니다(PE1ITR): 지금 비춰지는 스텝은 00:00 UTC 이후의 초를 주기로 나눈 나머지로 계산합니다(86 400 s는 4.8 s와 19.2 s의 배수). 지휘소가 시퀀스를 몇 스텝 옮기는 경우가 있으므로 상세 표시는 **수신으로 확인해야 하는 예측**입니다. 노란 표시 **PC 시계 동기화됨**이 이를 상기시킵니다: PC를 NTP 서버와 동기화하세요(오차는 많아야 수십 분의 1초).

### 검출 계수

흔적은 지속되는 동안 빔이 비출 때만 들립니다:

```
probability ≈ min(1, (step + trail) / cycle)
2021 sequence:  (0.8 + 0.3) / 4.8  ≈ 23 %
2007 sequence:  (3.2 + 0.3) / 19.2 ≈ 18 %
```

0.3 s는 143 MHz에서 전형적인 저밀도 흔적의 지속 시간으로, *프로그램의 선택*인 고정값입니다(SM6FHZ의 λ² 규칙은 밴드 사이의 지속 시간을 환산하지만 출발값은 주지 않습니다).

### 예상 에코 (실험적)

```
echoes/hour ≈ forecast(main path, f_fc) · (f_fc / 143.05)^k · (I_GRAVES + 10) / (I_main + 10) · probability
```

[예보 실험 적용](Experimental-Forecasts-ko)의 예보(국 계수 K가 이미 포함됨)를 그 주파수 f_fc에서 143.050 MHz로 SM6FHZ 규칙(같은 지수 k)으로 환산하고, 두 경로의 유성우 지수 비로 보정한 뒤(상수 10은 예보에서와 마찬가지로 산발 배경을 나타냄) 검출 계수를 곱합니다. 참고용일 뿐이므로 RMOB 관측자와 비교하세요.

## GRAVES 핑 수신 방법

| 단계 | 해야 할 일 |
|---|---|
| 수신기 | **143.049 MHz USB**(약 1 kHz 톤) 또는 143.050 MHz, **AGC 느리게 또는 끔**, 오디오 대역폭 **2.4 kHz 이상** |
| 안테나 | GRAVES → 내 경로의 **추천 핫스폿** 방향(*경로* 카드), **낮은 앙각** |
| 워터폴 | 핑은 **반송파 가까이의 짧은 선**입니다. 긴(고밀도) 흔적은 더 넓고 도플러가 보입니다 |
| 계수 | RMOB는 시간별 유성 계수에 GRAVES를 사용합니다: **내 핑을 143.050 MHz 관측자와 비교하세요**([예보 실험 적용](Experimental-Forecasts-ko#rmob-비교)) |

## 출처

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"*(DUBUS 4/2007) 및 *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki, "Graves" – 어레이, 섹터, 빔 타이밍
3. **Wikipedia**, "GRAVES (system)" – Broye-lès-Pesmes의 송신기(47.348° N 5.515° E)
4. **RMOB** – 143.050 MHz 관측자([rmob.org](https://www.rmob.org))
5. IC8TEM의 **YAEC** – GRAVES 레이더 탭(이 탭의 원형이 된 시안)
