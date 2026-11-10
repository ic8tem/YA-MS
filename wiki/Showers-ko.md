[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · **한국어** · [中文](Showers-zh)

# 유성우

*탭: 유성우.*

[![유성우](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

모든 계산에 쓰이는 유성우 목록: **IMO Meteor Shower Calendar 2026 및 2027**(표 5와 7)의 **45개 유성우**와 **Antihelion Source**(표 6)이며, 각각 **다음 극대**가 표시됩니다.

## 열

| 열 | 의미 |
|---|---|
| 약칭 | IMO 약칭(QUA, PER, GEM, …) |
| 유성우 | 이름 |
| 활동 | 활동 기간(일/월 – 일/월) |
| λ max | 극대의 태양 황경(J2000), IMO 값 |
| **다음 극대 (UTC)** | 다음 극대의 날짜와 시각(아래 참조) |
| **극대 출처** | *IMO 2026* / *IMO 2027* = IMO가 발표한 날짜와 시각; *IMO 2026 (일)* = IMO가 날짜만 제공하며 표시된 시각은 계산값(*~hh:mm 계산*); *λ로 계산* = 그해의 IMO 값 없음 |
| 적경, 적위 | 극대 시의 복사점(Antihelion Source는 *이동 중*) |
| v km/s, r | 지심 속도와 집단 지수 |
| ZHR | 극대 ZHR(*변동* = 가변) |
| 유형 | *안시* 또는 *전파, 주간* |

**오늘(UTC) 활동 중인** 유성우는 노란 반투명 배경과 굵은 글씨로 강조 표시됩니다.

## 다음 극대

프로그램은 항상 **다음** 극대를 보여 줍니다. IMO가 그해 달력을 발표했으면 `data/massimi_imo.csv`의 **IMO 날짜와 시각**을 사용하고(2026년과 2027년 포함), 그렇지 않으면 태양이 극대의 태양 황경에 도달하는 순간을 계산합니다(Meeus, *Astronomical Algorithms*, 25장, 뉴턴법으로 풂).

**검증:** IMO가 시각을 제공하는 경우 계산값은 IMO 2026 및 2027 달력과 몇 분 이내로 일치합니다(예: 사분의자리 유성우 2026/1/3 21:13 대 21:00; 쌍둥이자리 유성우 2027/12/14 19:51 대 20:00). 예외: 2026년 주간 사자자리 카파 유성우는 하루 늦게(9/25 대신 9/26), 2027년 물병자리 에타 유성우의 시각(15:10 대 IMO 09:00) – 이 경우에는 IMO 값을 사용합니다.

**연도 추가:** IMO가 새 달력을 발표하면 그 행을 `data/massimi_imo.csv`에 추가하세요(`year;code;MM-DD;hh:mm`, IMO가 날짜만 주면 시각은 비워 둠). 그때까지는 극대를 계산합니다.

## 소규모 유성우와 주간 유성우

목록에는 IMO 목록의 **소규모 유성우**(예: 10월 기린자리 유성우(OCT, ZHR 5, 10월 5–6일 활동), 안드로메다자리 유성우, 작은곰자리 감마 유성우)와 4–10월의 **주간 전파 유성우**(주간 4월 물고기자리 유성우, 주간 양자리 유성우, 주간 페르세우스자리 제타 유성우, 주간 황소자리 베타 유성우, 주간 사자자리 카파 유성우, 주간 육분의자리 유성우 등)가 포함됩니다. ZHR이 작아도 [경로 지수](Efficiency-Calculation-ko#모델)와 [추천 Hot](Sky-View-ko#추천-hot)에 기여합니다. 주간 전파 유성우에 대해 IMO는 ZHR을 주지 않으므로, 값이 없으면 프로그램은 작업값 5를 사용합니다.

## 활동 프로필과 복사점 이동

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0, λ_max는 IMO 달력의 값이고, 기울기 B(극대 전후가 다름)와 일일 이동 dα/dλ, dδ/dλ는 `data/sciami.csv`에 적힌 **작업값**입니다(IMO 이동 표는 아직 입력되지 않음). *매뉴얼 식 9와 13.* Antihelion Source의 위치는 IMO 표 6의 날짜 사이에서 선형 보간합니다(`data/ant_radiante.csv`; 12월 10일 – 9월 20일 활동, ZHR 약 4).

## 목록 편집

`data/sciami.csv`는 편집할 수 있는 일반 텍스트 파일(구분자 `;`)입니다: 약칭, 이름, 시작과 끝(MM-DD), λ max, 적경, 적위, 이동, v, r, ZHR, 극대 전/후 B, 유형(V 안시, R 주간 전파). 잘못된 행이 있으면 프로그램이 시작할 때 메시지를 표시하고 그 행을 무시합니다.

출처: International Meteor Organization – Meteor Shower Calendar 2026 및 2027, [www.imo.net](https://www.imo.net)(표 5, 6, 7); Philip G0ISW(전파 관측 최대 시간율); Rossano IZ5TEK(scattertek).
