[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [Bahasa Indonesia](Home-id) · [Tagalog](Home-tl) · [日本語](Home-ja) · **한국어** · [中文](Home-zh)

# YA-MS – 유성 산란 예보와 실시간 유성우 효율

*Costantino Cerrotta IC8TEM 작성*

**YA-MS**는 **50, 70, 144, 222, 432 MHz에서 유성 산란(MS)** 교신을 하는 아마추어 무선사를 위한 무료 프로그램입니다. 내 로케이터와 상대국 로케이터 사이의 실제 경로에 대해, 활동 중인 각 유성우가 경로에 얼마나 도움이 되는지(**효율**), 반사가 경로의 어느 쪽에서 오는지(**Hot A / Hot B**), 안테나를 어디로 향해야 하는지를 한 시간 단위로 계산하고, **실시간 유성 레이더**(독일 Collm)에서 얻은 시간당 반사 수의 실험적 예보를 제공합니다. **Windows, Linux, macOS**(.NET 8 + Avalonia)에서 동작하며 인터페이스 언어는 6가지입니다.

주요 출처는 **C. Cerrotta IC8TEM과 G. Sartori IV3GTH**의 논문 *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"*(제7판)입니다. 프로그램의 모든 공식과 데이터에는 출처가 명시되어 있습니다. [출처](Sources-ko)를 참조하세요.

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="천구"></a><br><sub>천구</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="효율 계산"></a><br><sub>효율 계산</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES 레이더"></a><br><sub>GRAVES 레이더</sub></td>
</tr></table>

## 누구를 위한 프로그램인가

- "오늘 밤 유성우가 극대"라는 일반적인 정보를 넘어, 유성 산란 경로가 **언제** 열리고 **어디로** 안테나를 향해야 하는지 알고 싶은 운용자.
- 복사점 위치에 따라 유성우가 쓸모 있는지 없는지가 갈리는 **144 MHz와 432 MHz의 장거리 경로**를 운용하는 국.
- **숫자를 직접 검증**하고 싶은 모든 분: 계산 매뉴얼과 프로그램 내 설명 문서는 모든 단계를 그 근거(발표된 출처, 프로그램에서 수행한 검증, 또는 프로그램의 선택)와 함께 제시합니다.

## 탭 구성

버전 1.6부터 주 탭에는 **하위 탭**(주 탭 아래의 더 밝은 줄)이 있습니다. 시작할 때 5초 동안 ESO VLT 위의 페르세우스자리 유성우를 담은 시작 화면이 표시됩니다(사진 ESO/S. Guisard, CC BY 4.0).

| 탭 | 하위 탭 | 표시 내용 |
|---|---|---|
| **라이브 및 실시간 데이터** | [실시간 트래픽](Live-Traffic-ko) | 수집된 모든 MS 트래픽의 방위 등거리 지도. 교신마다 가장 가능성 높은 흔적의 구름, 밴드별 색상, 새 스폿 깜빡임 |
| | [레이더 플럭스](Radar-Flux-ko) | Collm SKiYMET 레이더에서 읽은 시간별 유성 수와 흔적 고도, Sodankylä 이미지, 내 밴드에서의 추정값 |
| | [GRAVES 레이더](GRAVES-Radar-ko) | GRAVES → 나 전방 산란 경로: 빔 안의 유효 영역, 섹터와 스텝, 다음 빔 통과, 수신 방법 |
| | [데이터 수집](Data-Collection-ko) | 세 개의 텔넷 클러스터 스트림(DX cluster, RBN, DM4X/PSKReporter)과 MS 스폿 필터 |
| **예보 계산** | [예보 계산](Sky-View-ko) | Hot A / Hot B, 안테나 로브, PREV 영역, 유성우 이동이 표시된 경로 평면도; 유성우 목록; 복사점과 올바른 안테나 방향을 보여 주는 작은 천구; 안테나에서 본 단면 |
| | [기하와 경로 손실](Geometry-and-Path-Loss-ko) | 거리, 중간점, 앙각, Hot A / Hot B, 공통 영역 한계, 28–432 MHz 경로 손실, 링크 버짓, 안테나 |
| | [효율 계산](Efficiency-Calculation-ko) | 요약 카드, 유성우별 시간별 효율과 A/B쪽, 경로 지수, DH9GCD 비교, 그래프 |
| | [예보 실험 적용](Experimental-Forecasts-ko) | λ^k와 국 계수 K로 144 MHz(또는 임의 주파수)에 환산한 Collm 플럭스, 24시간 예보, RMOB 비교 |
| **기술 문서** | [출처](Sources-ko) | 모든 출처. 주요 출처는 Cerrotta–Sartori 논문 |
| | [유럽 레이더 지도](European-Radar-Map-ko) | 내 국을 기준으로 한 Collm, Sodankylä, GRAVES, CMOR의 위치 |
| | [효율 - 설명](Efficiency-Explanation-ko) | 효율 계산 방법을 단계별로 설명한 문서. Word로 내보내기 가능 |
| [실시간 유성우](Live-Showers-ko) | – | Global Meteor Network의 측정 ZHR과 CMOR 복사점 지도 |
| [유성우](Showers-ko) | – | 다음 극대(IMO 날짜와 시각 또는 계산값)가 포함된 IMO 목록 |
| [그리드 지도](Grid-Square-Map-ko) | – | ADIF 파일에서 읽은 교신·확인 Maidenhead 그리드. 밴드마다 탭 하나 |

탭 위에는 세 줄의 조작 항목(내 로케이터, 상대국, 밴드, 안테나, 흔적 고도, 시각)이 있습니다. [시작하기](Getting-Started-ko)를 참조하세요. **조작** 버튼으로 이를 접을 수 있고, 언어와 색 구성은 오른쪽 위에서 선택합니다. [설정과 데이터 폴더](Settings-and-Data-Folder-ko)를 참조하세요.

## 요약

- **고정 방향이 아닌 실제 경로**: 효율은 두 로케이터 사이의 대권 경로에 대해 계산합니다(이전 프로그램은 네 개의 고정 방향을 사용했습니다).
- E층 위 15 km 간격의 점에 대한 **정반사 모델**(McKinley). 흔적 고도는 Collm 레이더에서 실시간으로 읽습니다.
- 중간점 양쪽 150 km(30–400 km 조정 가능)의 **Hot A / Hot B**. 추천 쪽은 빨간색, 이미 안테나 로브 안에 있는 쪽은 회색으로 표시합니다.
- **실시간 레이더**: Collm을 5분마다 확인하고 변경된 소스만 다시 다운로드합니다. 오프라인에서도 마지막으로 저장된 데이터로 계속 동작합니다.
- SM6FHZ의 λ³ 규칙을 이용한 50/144/432 MHz **실험적** 예보. RMOB 관측자와 비교할 수 있습니다.
- 모든 것이 프로그램 옆의 **`data`** 폴더 하나에 있습니다. AppData도 시스템 폴더도 사용하지 않습니다.

> 효율은 실험적 모델(정반사 + 저밀도 흔적)입니다. MCG_MS, MS-Soft, 그리고 실제 운용 경험과 비교해 보세요.

## 어디서부터 시작할까

1. [설치](Installation-ko)
2. [시작하기](Getting-Started-ko)
3. 문제가 있으면 [문제 해결과 FAQ](Troubleshooting-FAQ-ko)

다운로드: GitHub의 **[Releases](https://github.com/ic8tem/YA-MS/releases)**.
