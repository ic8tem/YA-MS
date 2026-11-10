[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-BR) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · **한국어** · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-TW)

# 효율 - 설명

*탭: 기술 문서 › 효율 - 설명.*

[![효율 - 설명](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

기술 문서 *"Come YA-MS calcola l'efficienza di uno sciame"*(YA-MS가 유성우의 효율을 계산하는 방법)를 프로그램 안에서 밝은 페이지로 보여 줍니다. 효율을 구하는 과정을 **단계별로** 설명하고, 각 단계가 **어디에서 왔는지** 밝힙니다. 문서는 현재 **이탈리아어**로만 되어 있으며, 이 위키는 그 내용을 [효율 계산](Efficiency-Calculation-ko#모델)과 [기하와 경로 손실](Geometry-and-Path-Loss-ko)에서 한국어로 제공합니다.

## 레이블

각 단계에는 색 레이블이 붙어 있습니다:

| 레이블 | 색 | 의미 |
|---|---|---|
| **FONTE**(출처) | 파랑 | 인용한 출처를 그대로 따르는 단계. 괄호 안 숫자는 끝의 목록 번호 |
| **RILIEVO**(검증) | 초록 | 프로그램과 출처의 비교와 그 결과 |
| **SCELTA**(선택) | 주황 | 출처에서 가져오지 않은 프로그램의 선택: 실제 운용 경험으로 확인 필요 |

## 장 구성

| 장 | 내용 |
|---|---|
| 1. 서론 | 목적, 레이블, 효율의 의미(OH5IY, MCG_MS; YA-MS는 실제 경로를 사용) |
| 2. 반사가 일어나는 곳: E층 | 80–120 km의 흔적; 흔적 고도 = Collm 히스토그램의 최빈값(검증: 2026/11/5에 89.5 km) |
| 3. 경로 기하 | 지구와 중간점; 안테나 앙각(논문 공식); 공통 영역과 그 한계; Hot A / Hot B; 안테나 로브(DL6WU, Kraus, W4RNL) |
| 4. 유성우의 복사점 | 복사점 위치(IMO 2026/2027), 극대 날짜(IMO 또는 태양 황경), 활동 프로필 |
| 5. 반사 조건 | 정반사(McKinley), 가우스 허용 범위 0.05 rad, 최적 지향(SM6FHZ), DH9GCD 공식 |
| 6. 한 점에서 효율까지 | 15 km 간격의 반사점, 각 점의 가중치, 백분율; QTFGUI(DJ5HG)와 비교 |
| 7. 결과 읽기 | A / B쪽, 경로 지수, 복사점 색, PREV 영역, 안테나에서 본 단면 |
| 8. 운용 주파수와 경로 손실 | λ³ / λ² 규칙, 레이더에서 아마추어 밴드로, 경로 손실 기준값 |
| 9. 알려진 한계 | 저밀도 흔적만, 등방성 안테나, 작업값 |
| 10. 출처 | 번호가 붙은 17개 출처 |

## 버튼

| 버튼 | 기능 |
|---|---|
| **Word로 내보내기 (.docx)...** | `data/efficienza_spiegazione.docx`의 사본을 원하는 위치에 저장(제안 이름 *YA-MS - calcolo dell'efficienza.docx*) |
| **Word에서 열기** | 같은 `.docx`를 Word 문서의 기본 프로그램(Word, LibreOffice 등)으로 엽니다 |

## 파일

| 파일 | 내용 |
|---|---|
| `data/efficienza_spiegazione.txt` | 탭에 표시되는 텍스트, 한 줄에 한 블록(`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word 버전 |
| `doc/YA-MS_manuale_calcoli.docx` | **계산 매뉴얼**: 모든 식(Word 수식 편집기), 번호와 출처 포함 |

두 문서는 `tools/build_spiegazione.py data`와 `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`로 소스에서 다시 생성합니다.
