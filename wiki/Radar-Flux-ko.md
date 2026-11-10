[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Português (Brasil)](Radar-Flux-pt-br) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Polski](Radar-Flux-pl) · [Čeština](Radar-Flux-cs) · [Magyar](Radar-Flux-hu) · [Română](Radar-Flux-ro) · [Ελληνικά](Radar-Flux-el) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [ไทย](Radar-Flux-th) · [日本語](Radar-Flux-ja) · **한국어** · [中文](Radar-Flux-zh) · [中文 (繁體)](Radar-Flux-zh-tw)

# 레이더 플럭스

*탭: 라이브 및 실시간 데이터 › 레이더 플럭스.*

[![레이더 플럭스](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

이 탭은 전문 유성 레이더가 **지금** 세고 있는 값을 보여 줍니다: **Collm** SKiYMET 레이더(라이프치히 대학 / IAP Kühlungsborn, 독일, 36.2 MHz)의 시간별 유성 수와 흔적 고도, 그리고 **Sodankylä** 레이더(SGO, 핀란드)의 최신 이미지입니다. Collm 계수는 내 밴드의 추정값과 [예보 실험 적용](Experimental-Forecasts-ko)에 쓰이고, 측정된 흔적 고도는 전체 기하 계산에 쓰입니다.

## 조작

| 조작 항목 | 기능 |
|---|---|
| **지금 다운로드** | 모든 외부 소스를 한 번에 확인합니다. |
| **모든 소스를 5분마다 자동 업데이트** | 기본적으로 켜져 있습니다. 5분마다 모든 소스를 확인하고 **변경된 것만** 다시 다운로드합니다(*변화 없음 (… UTC 확인)* / *… UTC 새 데이터*). |
| **λ 지수 (SM6FHZ)** | 주파수 규칙의 지수 k, 기본값 3(1–4). |

## 표시 내용

| 패널 | 내용 |
|---|---|
| **시간당 유성 수 – 어제와 오늘 (UTC)** | 청록 막대 = Collm 계수(유효), 빨간 막대 = 제외됨, 굵은 주황 선 = 오른쪽 눈금의 *… MHz 추정* |
| **흔적 고도 (Collm)** | 70–110 km 사이 고도 km당 유성 수와 가장 빈번한 고도(최빈값), 평균, 중앙값, 표준편차 |
| Collm 이미지 | 다운로드한 원본 SKiYMET 그래프 |
| Sodankylä 이미지 | Sodankylä 레이더의 최신 유성 수 이미지(표시만 하며 형식은 읽지 않음) |

그래프 위의 줄에는 Collm 그래프를 언제 읽었는지와 어떤 세로 눈금을 찾았는지가 표시됩니다(*그래프에서 읽은 눈금: 0-… 유성/시간*).

## Collm 그래프 읽는 방법

Collm 그래프(720 × 720 픽셀, 단색)는 축 위치가 고정되어 있지만, 레이더가 측정값에 맞춰 **세로 눈금을 매일 바꿉니다**(예: 2026/11/5에는 0–1.2·10³, 2026/11/6에는 0–1.0·10³이며 눈금 표시 위치도 이동). 따라서 YA-MS는:

1. 축의 긴 눈금 표시를 찾고;
2. 각 문자를 그래프의 도트 매트릭스 글꼴과 비교하여 가장 높은 눈금과 0의 **레이블을 읽고**;
3. 각 시간 i(0–47, 어제와 오늘)에 대해 가운데 열과 위에서부터 첫 번째 청록 픽셀 y를 구합니다:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top과 y0은 가장 높은 눈금과 0의 행, N_top은 가장 높은 레이블에서 읽은 값(×1000)입니다. 분해능: 픽셀당 약 7–8 유성/시간. *프로그램의 선택 (매뉴얼 식 42).*

레이블을 읽지 못하면 프로그램은 2026/11/5의 보정값(**보정된 눈금 0-1200 유성/시간**)으로 돌아가고 주황색으로 알립니다: *플럭스 세로 눈금을 읽을 수 없습니다 (맨 위 레이블: …): 값을 확인해야 합니다.* 그래프 형식 자체가 바뀌면(*그래프 형식이 바뀌었습니다(…x…): 읽을 수 없습니다* 또는 *플럭스 축을 예상 위치에서 찾지 못했습니다*) 읽기를 다시 보정해야 하므로 알려 주세요([기여](Contributing-and-Contacts-ko) 참조).

### 흔적 고도

고도 히스토그램(km k에 n_k개의 유성, 평균 고도 h_k)에서:

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*매뉴얼 식 43.* **레이더에서**(조작 항목 2행)를 선택하면 **최빈값**이 모든 계산의 흔적 고도가 됩니다. 검증: 2026/11/5 그래프 – 최빈값 89.5 km, 평균 88.6 km, 표준편차 6.8 km로 Cerrotta–Sartori 논문의 약 90 km(SKiYMET 평균)와 일치합니다.

고도 그래프의 눈금이 바뀌면 프로그램은 경고합니다: *고도 통계(최빈값, 평균, 중앙값)는 유효하지만 절대 계수는 유효하지 않습니다.*

## 내 밴드에서의 추정

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

**SM6FHZ**의 경험 규칙(VUSHF 2025): 반사의 수와 세기는 λ³, 지속 시간은 λ²에 비례합니다. λ³ 의존성은 McKinley의 저밀도 흔적 식과 같습니다. IARU Region 1의 최대 핑 지속 시간도 표시됩니다(50 MHz 1000 ms, 70 MHz 500 ms, 144 MHz 100 ms, 432 MHz 13 ms). 값은 참고용이며 실제 운용 경험과 비교해야 합니다. 국 계수 K와 RMOB 비교는 [예보 실험 적용](Experimental-Forecasts-ko)에 있습니다.

## 오프라인

어떤 소스에도 접속할 수 없으면 메시지가 **한 번** 표시됩니다: *인터넷 연결이 없습니다. 레이더와 RMOB 데이터를 업데이트할 수 없습니다: 마지막으로 저장된 데이터를 사용하며 5분마다 자동으로 재시도합니다.* 연결이 돌아올 때까지(*연결이 복구되었습니다.*) 아래쪽 상태 표시줄이 빨간색(*인터넷 연결 없음 …*)이 됩니다.

## 아카이브와 소스

| 파일 (`data/` 안) | 내용 |
|---|---|
| `flusso_collm.csv` | Collm에서 읽은 플럭스의 시간별 아카이브(이미 있는 시간은 갱신) |
| `quote_collm.csv` | 흔적 고도 아카이브 |
| `radar/` | 최근 다운로드한 이미지(와 RMOB 파일) |
| `fonti_radar.csv` | 레이더 소스 주소. `attivo=1/0`으로 각각 사용/사용 안 함 |

| 소스 | 주파수 | 비고 |
|---|---|---|
| Collm meteor radar, Leipzig University (LIM) 및 IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36.2 MHz | 매시 10분(UTC)에 갱신. 어제 + 오늘 플럭스, 고도 분포 |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36.9 MHz | 이미지만(레이더 갱신 중, DECC 프로젝트) |
| swan.ms (Collm 사본) | 36.2 MHz | 기본적으로 사용 안 함. DL1DBC의 허가가 있을 때만 사용 |

> 레이더 데이터의 권리는 각 기관(라이프치히 대학 / IAP Kühlungsborn, Sodankylä Geophysical Observatory)에 있습니다.
