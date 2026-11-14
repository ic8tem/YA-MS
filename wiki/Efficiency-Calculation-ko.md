[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · **한국어** · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# 효율 계산

*탭: 예보 계산 › 효율 계산.*

[![효율 계산](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

유성우의 **효율**은 그 복사점 위치가 **내** 경로에서의 반사를 얼마나 허용하는지를 백분율로 나타냅니다. 이 개념은 Ilkka **OH5IY**(MS-Soft)가 고안했고 Cerrotta–Sartori 논문에서도 다룹니다: 효율의 극대는 안시 극대(ZHR)와 일치하지 않는데, 두 국에 대한 복사점의 위치에 좌우되기 때문입니다. DL5MCG의 MCG_MS는 같은 아이디어를 네 개의 고정 방향에 적용하고, YA-MS는 두 로케이터 사이의 **실제 경로**에 대해 계산합니다.

이 탭은 *계산 날짜 (UTC)*에서 고른 날짜에 대해 시간별 효율을 보여 줍니다(매시 30분 값).

## 요약 카드

| 카드 | 내용 |
|---|---|
| **하루 중 최적 시각** | 경로 지수가 가장 높은 시각, 그 지수, 우세한 쪽(A/B와 %) |
| **가장 유리한 유성우** | 그날 ZHR × 효율이 가장 큰 유성우, 그 효율, 시각, 쪽, **최적 지향**(복사점 방위 +90° / −90°) |
| **지금 · 1, 3, 6, 12, 24시간 후** | 각 시점마다 그곳에서 시작하는 한 시간의 평균(표본 4개): 경로 지수, 우세한 쪽, 가장 크게 기여하는 유성우, 레이더 자료가 있으면 실험 예보의 시간당 반사 횟수. '지금'에서는 레이더 자료가 없으면 추천 Hot을 표시합니다. 매분 갱신됩니다. |

이 카드들은 시간 줄 아래, 탭 위의 띠에 있으며 명령 줄을 접어도 항상 보입니다: 왼쪽에 선택한 날의 카드 두 개, 이어서 지금부터 시작하는 예보 시점 여섯 개.

카드 아래의 띠는 A와 B의 의미를 설명합니다(아래 참조).

## 그래프

*… …의 시간별 효율 (UTC, 매시 30분 값).* 최대 다섯 개 유성우에 대해 효율 %를 실선으로, DH9GCD 공식을 같은 색의 점선으로 그리고, **경로 지수**를 오른쪽 눈금의 파란 막대로 표시합니다.

## 시간별 표

그날 활동하는 유성우마다 한 행(ZHR 순 정렬), 시간(UTC)마다 24개 열:

| 셀 | 의미 |
|---|---|
| `63A` | 효율 63 %, 반사 대부분이 **A**쪽에서 옴 |
| `41B` | 효율 41 %, **B**쪽 |
| 빈칸 | 효율 1 % 미만 |
| `…↑` | 그 시각 복사점이 내 국에서 **70° 이상**(너무 높음) |
| 노란 글자 | 효율 ≥ 50 % |

- **A** = 내 국에서 상대국을 바라볼 때 **왼쪽**(Hot A 영역), **B** = **오른쪽**(Hot B 영역). 안테나를 **그쪽으로 10–30°** 돌리는 것이 좋습니다(사이드 스캐터, Cerrotta–Sartori 논문).
- **하늘색 행**(*DH9GCD %*, 각 유성우 아래): 비교용 DH9GCD 공식.
- **Σ 행**: *경로 지수 (ZHR×효율)*.
- **주황 행**(*예보 … MHz (반사/시간)*): 값이 있는 시간대(오늘과 내일 일부)의 실험적 예보.

## 모델

모든 단계는 [계산 매뉴얼](Efficiency-Explanation-ko)(`doc/YA-MS_manuale_calcoli.docx`, 5장)에 있습니다. 요약하면:

**1. 정반사.** 흔적은 A와 B를 초점으로 하는 타원체에 접할 때만 A에서 B로 신호를 보냅니다(McKinley 1961). 한 유성우의 흔적들은 복사점 방향 ŝ에 평행합니다(논문; McKinley). E층의 각 점 P에 대해 국을 향한 단위 벡터로:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

같은 법칙이 DJ5HG의 QTFGUI와 그의 글 *"Die Geometrie von Meteorscatterverbindungen"*(2004)의 바탕입니다: 흔적은 흔적을 축으로 하는 원뿔 위로 산란하며, 원뿔 위에 있는 수신국만 그것을 듣습니다. 이상적인 흔적에서는 원뿔 벽이 매우 얇습니다(수천 파장 길이의 방사체). 프로그램은 가우스 허용 범위 σ = 0.05 rad(약 3°)로 조건을 받아들이며, 이는 이상적인 원뿔이 보지 못하는 것, 즉 유성우 복사점의 퍼짐(GMN 측정 0.3–1.4°), 바람에 휜 흔적, 흔적의 유한한 길이를 나타냅니다 – *프로그램의 선택*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. 각 점의 가중치.** 저밀도 흔적의 전력(McKinley; ITU-R P.843, 식 3), φ = 산란각의 절반(85°로 제한, *선택*), β = 흔적과 전파면 A-P-B 사이의 각, p̂ = 그 면의 단위 법선:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**옵션 "흔적과 경로 사이의 각 β (완전한 McKinley)"**(기본값 켜짐, 신중 설정). 켜면: 전파면을 가로지르는 흔적은 면 안에 놓인 흔적보다 10–15 dB 낮게 평가되므로 어떤 흔적도 과대평가되지 않습니다. 끄면: 모든 흔적을 면 안에 있는 것처럼 가중합니다(β = 0, cos²φ를 포함한 가중치). 버전 1.6까지와 같습니다. *검증:* 1000 km 경로에서 β가 없으면 최적의 복사점 방위각은 복사점 고도에 따라 경로에서 15°–90° 떨어져 있고(복사점이 30°이면 30°, 60°이면 경로에 직각), 직각 방향 복사점은 고도 30°에서 67 %입니다. β가 있으면 최적의 복사점은 항상 경로를 따라 있고 직각 방향 복사점은 15 %로 떨어집니다. β를 쓰면 SM6FHZ / DH9GCD의 최적 방향 규칙이 사라집니다. β는 옵션으로 남아 있으며, 가장 신중한 값을 주기 때문에 기본값으로 켜져 있고, 끄면 규칙이 돌아옵니다.

한 점에 도달하는 유성 수는 그곳에서의 복사점 고도의 사인(ŝ·û_P)에 비례하며, 이는 IMO가 ZHR에 사용하는 보정과 같습니다.

**옵션 "낮은 복사점에서 더 긴 흔적 (DJ5HG)"**(차트 위 체크박스, 기본값 꺼짐, 툴팁 있음): DJ5HG는 복사점이 낮으면 km²당 떨어지는 유성은 적지만 흔적이 더 길고(유효 길이 최대 100 km) 반사 법칙을 더 자주 만족한다고 지적합니다. 옵션을 켜면 가중치는 min(sin El, 15/100)이 됩니다: 유효 층 두께 15 km를 고도의 사인으로 나누면 흔적 길이가 되며, 100 km로 제한됩니다. 약 9° 이상에서는 두 효과가 상쇄됩니다. 끄면 계산은 신중하게 유지됩니다.

**계산 설정**(같은 줄, 라디오 버튼): **신중**(기본값, 가장 신중한 값: 레이더 흔적 고도, 일반 흔적, β 켜짐), **DJ5HG와 같이**(102 km, 더 긴 흔적, β), **사용자 지정**. 사용자 지정은 고도, *레이더에서* 상자, 더 긴 흔적 옵션 또는 β를 직접 바꾸면 자동으로 선택됩니다.

**3. 합과 백분율.** 유성흔 높이에서 15 km마다 잡은 점으로, 두 국 모두 지평선 위로 보며 두 안테나의 수직 패턴으로 가중치를 줍니다(*안테나 패턴* 상자, 기본 켬; 끄면 로브 앙각 위의 점만)(*선택*). 100 %는 그 경로에서 가장 유리한 복사점 위치입니다:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F는 경로마다 한 번, 방향 격자(방위 5° 간격, 고도 2.5° 간격)에서 계산하고 보간합니다.

**dB 단위 효율 (DJ5HG 기준).** 백분율은 그 경로에 대한 최적의 복사점 위치에 대해서만 상대적입니다. 서로 다른 경로를 비교할 수 있도록 프로그램은 DJ5HG의 고정 기준에 대한 dB 단위 효율도 제공합니다: 0 dB는 적도를 가로지르는 1000 km 남북 경로에서 분점에 복사점이 천구 적도에 있을 때의 최댓값이며, 같은 고도와 같은 가중치로 계산합니다. DJ5HG는 자신의 값이 6 dB보다 정확하다고 밝힙니다.

**4. 쪽과 지수.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

표의 문자는 비율이 더 큰 쪽입니다. *프로그램의 선택 (매뉴얼 식 32–33).*

## DH9GCD 비교

최적 방향에 대한 1차 자료는 Eshleman & Mlodnosky와 Meeks & James(Proc. IRE, 1957), Hines(1955), 그리고 Forsyth, Hines & Vogan(1955)의 실험적 검증입니다: 산란각 이등분선에 수직인 하늘의 반원 위에 있는 복사점만 유용하고, 흔적의 수는 sin El에 따라 늘어나며, 중간점 근처에서 유용한 흔적은 복사점 반대쪽 옆으로 약 H·tan El 떨어진 곳에 생깁니다. DJ5HG는 단서를 덧붙입니다: **낮은** 복사점이 경로를 따라 정확히 놓이면 McKinley의 식은 강한 신호를 줍니다(함부르크–나르비크, 사분의자리 유성우, 약 19 UTC). 따라서 "경로와 나란한 복사점 = 거의 0"은 높은 복사점에만 해당합니다. 프로그램은 신중한 계산을 유지하고 경고 *경로를 따라 낮은 복사점*을 표시합니다.

독립적인 검증: **DF5HC**가 소개한(DARC 컨퍼런스, 2018년 1월) **DH9GCD**의 최적 방향 공식 – 발표된 1차 자료는 없습니다. El과 Az는 내 국에서 본 복사점의 고도와 방위, P는 상대국의 방위입니다:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

복사점이 45°에 있고 경로에 대해 정측면일 때 최대입니다. DF5HC는 복사점이 20° 미만이면 너무 낮고 **70° 이상이면 너무 높다**고 봅니다: 이런 시간대는 표에 ↑가 붙고 [천구](Sky-View-ko#경고)에 경고가 표시됩니다. 이 공식은 거리와 고도를 무시하지만 좋은 기준이 됩니다.

## 검증

| 검증 | 결과 |
|---|---|
| SM6FHZ 규칙(VUSHF 2025): 최적 경로는 복사점 방위에 직교, 지향 = 복사점 방위 ±90°, 허용 범위 ±40–50° | 모델이 재현함. 복사점이 경로와 나란하고 하늘 높이 있으면 효율은 거의 0 |
| DJ5HG의 QTFGUI, 함부르크 JO53IM – 바르셀로나, 사분의자리 유성우, 1월 4일(매뉴얼의 예) | QTFGUI: 07:00 지향 252°, −8 dB; 08:00 반사 영역 없음; 09:00 지향 168°, −4 dB. YA-MS(QTFGUI와 같은 고도 102 km): 07:00 241°, −5.4 dB; 08:00 0.6 % (−22 dB); 09:00 161°, −4.0 dB. DH9GCD: 26 %, 2 %, 32 %. 세 방법 모두 복사점이 거의 천정에 있는 08:00의 공백을 보여 줌 |
| DJ5HG의 곡선(*Die Geometrie…*, Bild 8–9: 함부르크와 뮌헨에서, 사분의자리 유성우, 1월 4일; 그래프에서 읽은 값, 약 ±0.5 dB, ±15분)과 자동 테스트 `--prova-dj5hg`(시간당 1개 값)의 비교 | 시각: 복사점이 천정 가까이 있을 때의 구멍이 같은 시간대에 나타납니다(바르셀로나 07:30–08:30 대 07–09; 소피아 06:36–07:48 대 07–08; 나르비크 07–08:30 대 07–09). 모스크바는 양쪽 모두 03–10시에 닫혀 있고, DJ5HG가 쓴 대로 함부르크에서는 약 02:30까지, 뮌헨에서는 약 00:30까지 열려 있습니다. 방향: 2–10° 차이. 102 km에서의 레벨과 모양(곡선과의 평균 차이와 RMS 차이): β 없음, 더 긴 흔적 없음 −1.6 / 4.0 dB; 더 긴 흔적 +1.1 / 4.6 dB; β −5.4 / 6.2 dB이지만 모양은 가장 좋습니다(평균을 빼면 3.0 dB, 대 3.6). 낮은 복사점에서의 깊은 최솟값이 나타납니다(바르셀로나 17시 −15.6 dB 대 19:36에 −16 dB, 소피아 20시 −18.5 dB 대 −14 dB). β와 더 긴 흔적(*DJ5HG와 같이*) −2.2 / 4.7 dB; 신중 설정(레이더 고도 89.5 km, β 켜짐, 더 긴 흔적 없음) −6.9 / 7.6 dB, 모양 3.3 dB. β가 없으면 복사점이 낮고 경로와 거의 나란할 때의 최솟값이 YA-MS에서 거의 나타나지 않습니다(−8.6과 −10.4 dB): 이는 DJ5HG 자신의 단서이며, 그래서 경고를 표시합니다 |
| 15 km 대신 5 km 간격 샘플링 | 백분율 변화 0.3포인트 미만 |

> MS-Soft 5.2 문서는 OH5IY의 효율을 저밀도 흔적만을 위한 상대 지수로 정의하며, 두 가지 요인(복사점 고도, 약 45°가 최적, 그리고 경로와의 각도, 90°가 최적)과 고밀도 흔적을 위해 수동으로 20 %까지 올린 최솟값을 사용합니다. 공식은 발표되지 않았습니다. MCG_MS는 네 개의 고정 방향에 대해, 그리고 DX 로케이터가 있으면 실제 경로에 대해 계산합니다. 모델은 저밀도 흔적만, 등방성 안테나로 고려합니다. 고밀도 버스트와 산발 배경은 효율에 포함되지 않습니다(산발 배경은 레이더 플럭스로 나타냅니다). 1.8.1부터 「안테나 패턴」 상자를 켜면 안테나의 수직 패턴이 적용됩니다. 방위각에서는 안테나가 등방성으로 남습니다.
