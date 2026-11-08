[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · **한국어** · [中文](Geometry-and-Path-Loss-zh)

# 기하와 경로 손실

*탭: 예보 계산 › 기하와 경로 손실.*

[![기하와 경로 손실](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

경로에 대한 텍스트 보고서(선택 가능하므로 복사할 수 있음)와, 오른쪽에 **스캐터 포인트까지 거리에 따른 안테나 앙각** 그래프가 있습니다. 대괄호 안의 숫자는 계산 매뉴얼(`doc/YA-MS_manuale_calcoli.docx`)의 식 번호입니다.

## 이 탭의 입력값

| 항목 | 기본값 | 용도 |
|---|---|---|
| **출력 W** | 400 | 링크 버짓용 송신 출력 |
| **안테나 이득 dBi (송신 = 수신)** | 14 | 양쪽이 같은 안테나 |
| **최소 신호 dBm** | −130 | 최소 검출 가능 신호(논문: 8소자 야기 + 프리앰프) |
| **흔적 밀도 q = 10^ … 전자/m** | 14 | 저밀도 흔적의 전자 선밀도 |

국, 밴드, 흔적 고도, 로브 앙각, 붐, 핫스폿 거리는 [조작 항목](Getting-Started-ko#1-세-줄의-조작-항목)에서 가져옵니다.

## 보고서 구성

| 섹션 | 내용 |
|---|---|
| **경로 기하 (구형 지구, R = 6372.7955 km)** | 내 국과 DX의 고도; 거리, 방위와 역방위; 중간점(로케이터와 좌표); 흔적 고도(레이더에서 가져왔으면 *<- Collm 레이더로 측정한 최빈값*); 중간점 방향 안테나 앙각 |
| **HOT A / HOT B (안테나 지향용 고전적 핫스폿)** | 각각에 대해: 로케이터, 내 국 기준 방위와 직선 경로로부터의 오프셋, DX 기준 방위, 거리, 앙각 |
| **공통 영역 한계** | 로브 앙각에서의 흔적 고도 도달 거리; 한계 A / 한계 B와 방위 |
| 안테나 | λ 단위 붐, 이득, 수평 / 수직 로브; Hot A와 Hot B가 로브 안인지 밖인지 |
| **경로 손실 (저밀도 흔적, McKinley 1961; 안테나 이득 제외)** | 중간점(전방), Hot A, Hot B에 대한 28, 50, 70, 144, 222, 432 MHz 표 |
| **… MHz 링크 버짓 (중간점)** | 출력과 EIRP, 경로 손실, 안테나 신호, 최소 수신 가능, **마진**; OH5IY 평균 손실로 계산한 같은 마진 |
| **밴드 간 경험 규칙 (SM6FHZ, VUSHF 2025)** | 144 MHz 대비 수/세기와 지속 시간; IARU 최대 핑 |

## 로케이터와 경로

로케이터(4, 6 또는 8자리; 그리드 중심, IARU Maidenhead 체계) [14]. 거리, 방위, 중간점은 반경 **r = 6372.7955 km**(Cerrotta–Sartori 논문)인 구 위의 대권 공식으로 계산합니다 [15–16]. 시각에 따라 달라지는 계산은 **중간점**을 기준으로 합니다. 두 끝에서 최적 시각이 최대 1.5시간까지 차이 날 수 있기 때문입니다(SM6FHZ).

## 안테나 앙각

**출처:** Cerrotta–Sartori 논문의 공식(그림 7). x = d/r, d는 반사점까지의 지상 거리, H는 흔적 고도, h는 국의 고도 [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**검증:** 정확한 구면 기하와 0.03° 이내로 일치합니다. 프로그램은 2인수 아크탄젠트를 사용하여 수평선 너머에서는 음수 값을 주고, 논문에서 언급한 주기성 문제를 피합니다. 중간점 방향의 앙각이 음수이면 *단일 홉의 기하학적 도달 거리를 넘는 경로*라는 뜻입니다.

## 수평선 도달 거리

앙각 e의 전파가 고도 H에 닿는 지상 거리(위 공식의 기하학적 역) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**검증:** H = 89.5 km, e = 0° → **1062 km**. 논문의 예(JN44BB–IO53RT)에서는 그림상 수평선 교차점이 국에서 약 870 km에 있으며, 이는 로브를 약 2° 올린 경우(865 km)에 해당합니다.

## 공통 영역 한계

**출처:** 논문은 각 국의 수평선이 E층과 만나는 곡선들의 교점을 구합니다. 즉 A와 B를 중심으로 각반경 ρ = d_H/r인 두 원의 교점입니다 [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

1 − |p0|² < 0이면 경로가 2·d_H보다 길어 두 국이 **E층 공통 영역을 볼 수 없습니다**.

**검증:** 이 점들은 두 국이 함께 보는 하늘의 **가장 먼 가장자리**이지 **겨냥할 점이 아닙니다**. JN70CN–IN78UO(1710 km, 방위 308°)에서는 국에서 1062 km, 직선 경로의 좌우 37°에 위치하지만 MSHV는 10°를 제시합니다. 그래서 *한계 A* / *한계 B*라고 부르고 지도에 흐리게 그립니다.

## Hot A와 Hot B

**출처:** 반사는 **중간점 양쪽 약 50–150 km**의 두 영역("핫스폿")에 집중됩니다. 이는 AMS Bulletin No. 203의 안테나 오프셋 표의 바탕이며, W8WN이 이를 이어받았습니다(1500 km와 1800 km 경로에 10° 오프셋). LZ2HV의 MSHV도 같은 기준을 사용합니다.

**선택:** Hot A와 Hot B는 중간점 M에서 경로에 수직으로 거리 s만큼 떨어진 점입니다(s = 150 km, 30–400 km 조정 가능). 내 국에서 DX를 바라볼 때 A는 왼쪽, B는 오른쪽입니다 [21]. 국에서 본 오프셋은 대략 다음과 같습니다 [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**검증:** JN70CN–IN78UO, D = 1710 km: s = 100 km이면 6.7°, **s = 150 km이면 10.0°**(MSHV 및 AMS/W8WN과 같음), s = 200 km이면 13.2°.

## 저밀도 흔적 경로 손실

**출처:** 저밀도 흔적에 대한 McKinley의 식(β = 0, sin α = 1), 안테나 이득 제외. q = 전자 선밀도, r_e = 고전 전자 반경 = 2.818·10⁻¹⁵ m, R1, R2는 흔적까지의 거리, φ는 산란각의 절반 [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**검증:** 144 MHz에서 q = 10¹⁴ 전자/m이면 600–2200 km 사이에서 **181–192 dB**로, 논문이 인용한 144 MHz 기준값 **최소 182 dB**(GM8JBJ, Kaiser & Closs 1952 기반)와 **평균 200 dB**(OH5IY)에 부합합니다.

## 링크 버짓

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. 이득은 dBi로 입력하고 dBd(dBi − 2.15)로 사용합니다. 보고서는 **OH5IY의 평균 경로 손실**(144 MHz에서 200 dB, 선택한 밴드로 λ³ 환산)을 쓴 마진도 제시합니다. 논문의 기준: 약 **70 dBm EIRP**가 필요합니다(−130 dBm + 200 dB, 예: 14 dBi 안테나에 약 400 W).

## 안테나 이득과 로브

**이득 – 출처:** 붐 길이 L의 함수로 나타낸 긴 야기 안테나에 대한 Günter Hoch **DL6WU**의 곡선, W8IO 소개(약 2 λ부터 유효) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**432 MHz에서 L.B. Cebik W4RNL의 NEC 모델과 비교한 검증**(*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| 야기 | 소자 수 | 붐 (λ) | W4RNL NEC (dBi) | 공식 (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3.23 / 6.82 / 10.42 | 15.28 / 17.82 / 19.35 | 15.38 / 17.91 / 19.34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3.12 / 6.88 / 10.79 | 15.17 / 17.91 / 19.46 | 15.27 / 17.94 / 19.45 |

차이는 **0.1 dB**를 넘지 않습니다: 이득은 설계보다 붐 길이에 더 좌우됩니다(VK3AUU 야기는 같은 소자 수에서 붐이 더 짧습니다). VK5DJ의 Yagi Calculator도 VK3AUU, WA2PHW, DJ9BV 변형에 대한 추정값을 주지만 그 공식은 공개되어 있지 않습니다.

**로브 – 출처:** Kraus 규칙, 원형 로브 θE = θH = θK로 가정 [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**검증:** W4RNL의 DL6WU 야기 NEC 모델은 Kraus보다 **수평 로브가 5–10 % 좁습니다**: 12, 19, 26소자에서 33.8° / 26.4° / 22.6°, Kraus는 37.3° / 28.0° / 23.9°. 단순 공식은 전방 사이드로브를 무시합니다(W4RNL, *Long-Boom Yagi Rules of Thumb*). 긴 붐에서는 수직 로브가 수평보다 약간 넓습니다(14 λ: 18.4° / 18.8°).

**선택** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

예: 432 MHz의 14 λ 야기 → 20.3 dBi, 로브 수평 18.1°, 수직 19.5°. W4RNL 모델은 20.4 dBi, 18.4° / 18.8°입니다. 이는 몇몇 DL6WU 안테나에서 얻은 근사 규칙입니다.

안테나는 항상 DX를 향한다고 간주합니다. |Az(Hot) − Az(안테나)| ≤ θ_horizontal/2이면 핫스폿이 **로브 안**에 있는 것으로 보고 [천구](Sky-View-ko)에 회색으로 그리며 경고를 표시합니다. 효율 계산에서는 안테나를 등방성으로 취급하며, 실제 로브는 이 확인에만 사용합니다.

## 밴드 간 경험 규칙

144 MHz 대비: 수/세기 × (144/f)³(dB), 지속 시간 × (144/f)²(SM6FHZ, VUSHF 2025). IARU Region 1 최대 핑 지속 시간: 50 MHz 1000 ms, 70 MHz 500 ms, 144 MHz 100 ms, 432 MHz 13 ms(VHF Handbook, 논문에서 인용). [예보 실험 적용](Experimental-Forecasts-ko)도 참조하세요.
