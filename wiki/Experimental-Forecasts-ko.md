[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · **한국어** · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# 예보 실험 적용

*탭: 예보 계산 › 예보 실험 적용.*

[![예보 실험 적용](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

이 탭은 **Collm 레이더(36.2 MHz)**의 유성 계수를 **아마추어 밴드에서의 시간당 반사 수** 추정값(기본 144 MHz, 28–1300 MHz의 임의 주파수)으로 바꾸고, 내 경로에 대해 **향후 24시간**을 예보하며, 추정값을 **RMOB** 관측자(예: 143.050 MHz로 GRAVES를 듣는 관측자)와 **비교**할 수 있게 해 줍니다.

> 여기 있는 모든 것은 **실험적**입니다: 주파수 규칙은 경험 규칙이고 국 계수는 내 국에 따라 달라집니다. 숫자는 시간대와 날짜를 비교하는 데 사용하고, 실제 운용으로 확인하세요.

## 조작

| 조작 항목 | 기본값 | 기능 |
|---|---|---|
| **목표 주파수 MHz** | 144 | 예보 주파수(28–1300 MHz) |
| **λ^k 지수** | 3 | 주파수 규칙의 지수 k(SM6FHZ: 3) |
| **국 계수 K** | 1 | 수신국(출력, 안테나)을 반영. 같은 밴드의 RMOB 관측자와 비교하여 구함 |
| **디스크에서 RMOB 파일 불러오기...** | | 월간 RMOB 텍스트 파일을 읽음(아래 참조) |
| **RMOB 파일에서 지수 구하기** | | Collm과 RMOB의 공통 시간에서 k를 맞춤 |
| **RMOB 관측자** | 비어 있음 | 파일 이름에 나오는 관측자 이름(예: `NAME_112026rmob.TXT` → `NAME`) |
| **지금 RMOB 다운로드** | | 그 관측자의 이번 달 파일을 한 번 다운로드 |
| **5분마다 자동 다운로드 (RMOB의 허가가 있을 때만 사용)** | **꺼짐** | [RMOB와 자동 프로그램](#rmob와-자동-프로그램) 참조 |

조작 항목 아래의 주황색 줄은 현재 값으로 규칙을 보여 줍니다. 예: *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, 그리고 지속 시간 환산과 그 주파수에서의 IARU 최대 핑.

## 레이더에서 아마추어 밴드로

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**출처:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45th Nordic VUSHF, 2025년 5월 – 반사의 수와 세기는 **λ³**, 지속 시간은 **λ²**에 비례합니다(432 MHz는 144 MHz보다 14–15 dB 낮고 지속 시간은 1/9). **검증:** λ³ 의존성은 McKinley의 저밀도 흔적 식과 같습니다. k = 3이면 Collm의 1000 유성/시간은 **144 MHz에서 약 16 반사/시간**이 됩니다. 143.050 MHz로 GRAVES를 듣는 RMOB 관측자는 보통 **시간당 20–140 에코**를 셉니다(RMOB 회보, 2018년 6월): 자릿수는 맞으며, 그 차이가 국 계수 K입니다. (매뉴얼 식 44–45.)

## 향후 24시간

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**지속성(persistence):** 전날(없으면 이틀 전) 같은 시각의 환산값을 **경로 유성우 지수** I(Σ ZHR × 효율, [효율 계산](Efficiency-Calculation-ko#모델) 참조)의 변화로 보정합니다. 상수 10은 산발 배경을 나타내며 지수가 작을 때 보정을 제한합니다. *프로그램의 선택 (매뉴얼 식 47).*

| 패널 | 내용 |
|---|---|
| **Collm에서 측정하여 f MHz로 환산 – 어제와 오늘 (UTC)** | Collm 레이더 유성/시간; 환산값(주황, 오른쪽 눈금); 불러온 경우 RMOB 계수(초록, 오른쪽 눈금) |
| **…에 대한 f MHz 향후 24시간 실험적 예보** | 예보 반사/시간(막대)과 경로 유성우 지수(오른쪽 눈금) |
| 표 | UTC 시각 · Collm 같은 시각 · 환산 · 경로 유성우 지수 · 예보 /시간 · **평가** |

**평가:** 예보가 24시간 평균의 1.3배 이상이면 *좋음*, 0.8배 이상이면 *보통*, 그 미만이면 *나쁨*. 같은 예보가 **실험적 예보** 카드와 [효율 계산](Efficiency-Calculation-ko)의 주황 행에도 나타나며, [GRAVES 레이더](GRAVES-Radar-ko#예상-에코-실험적) 탭의 예상 에코의 기초가 됩니다.

## RMOB 비교

[RMOB](https://www.rmob.org)(Radio Meteor Observatories On Line, Pierre Terrier)는 전파 관측자들의 시간별 유성 계수를 모읍니다. 이탈리아에서는 많은 관측자가 143.050 MHz로 GRAVES를 듣습니다(베네치아 천문관, 파엔차, 로베레토 등).

**RMOB 파일 읽기.** 두 가지 텍스트 형식을 받습니다:

| 형식 | 모양 | 비고 |
|---|---|---|
| 월간 파일 (Colorgramme / Spectrum Lab) | 하루 한 행, 24개의 시간별 값이 있는 `day| n| n| …` | 일반적인 `NAME_MMYYYYrmob.TXT` |
| 회보 표 | 헤더 ` UT |  1   2   3 …`, 행 `0h|175 166 …` | 파일에 관측자가 여럿이면 차례로 읽히므로 관측자가 하나인 파일을 사용하세요 |

월과 연도는 파일 이름(`…_MMYYYYrmob…`)이나 헤더에서 읽습니다. 그렇지 않으면 이번 달을 사용합니다(프로그램이 알려 줌).

**지수 맞추기.** K = 1로 두고, 공통 시간(최소 3시간)에 대한 RMOB/Collm 비의 중앙값으로부터:

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*프로그램의 선택 (매뉴얼 식 46).* 대화 상자에 공통 시간, 비의 중앙값, k가 표시됩니다. **예**를 누르면 k를 적용(하고 K = 1로 설정)하고, **아니오**를 누르면 k = 3을 유지합니다. 이 경우 같은 대화 상자에 제시된 값으로 K를 직접 조정하세요.

## RMOB와 자동 프로그램

RMOB는 **자동 프로그램이 파일을 가져가지 않도록** 요청합니다. 그래서 **자동 다운로드는 처음에 꺼져 있으며**, **RMOB에 허가를 요청한 뒤에만** 켜야 합니다. 허가가 없어도 언제든 **디스크에서 RMOB 파일 불러오기...**를 사용하거나 필요할 때 **지금 RMOB 다운로드**를 누를 수 있습니다.

다운로드 주소는 `config.ini`의 템플릿입니다(키 `rmob_url`, 기본값 `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, `{NOME}`은 관측자, `{MMAAAA}`는 월과 연도). 다운로드한 파일은 `data/radar/`에 보관됩니다.
