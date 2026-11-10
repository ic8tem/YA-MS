[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [Bahasa Indonesia](Grid-Square-Map-id) · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · **한국어** · [中文](Grid-Square-Map-zh)

# 그리드 지도

*탭: 그리드 지도.*

[![그리드 지도](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

로그의 ADIF 파일에서 읽은 **교신한** 그리드와 **확인된** Maidenhead 그리드(4자리)를 유럽 지도에 표시합니다 – **밴드마다 하위 탭 하나: 50, 70, 144, 222, 432 MHz**.

## 조작

| 조작 항목 | 기능 |
|---|---|
| **ADIF 파일 불러오기...** | `.adi` / `.adif` 파일을 읽습니다. 새 ADIF는 이전 데이터를 **대체**합니다. |
| **메모리 지우기** | ADIF에서 불러온 그리드를 모두 지웁니다(확인을 요청함). |
| 마우스 | **휠 = 확대/축소, 드래그 = 이동, 그리드 위 마우스 = QSO**(날짜와 함께 최대 6개 호출부호, 확인된 경우 *(확인됨)*) |

불러온 뒤 상태 표시에 *QSO …개 읽음, 50-432 MHz 밴드 QSO 그리드 …개, QSO …개 제외 (다른 밴드 또는 그리드 없음)*이 나타납니다. 각 밴드 지도에는 *교신한 그리드 …개, 확인 …개* 캡션이 붙습니다.

| 색 | 의미 |
|---|---|
| 주황 | 교신함 |
| 초록 | 확인됨 (QSL 또는 LoTW) |

## ADIF 읽는 방법

- 사용하는 필드: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD`(ADIF 사양).
- 밴드는 `BAND`에서, 또는 주파수에서 구합니다: 50–54 MHz = 6 m, 69.9–71.5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1.25 m, 420–450 MHz = 70 cm.
- 그리드 안의 QSO 중 하나라도 `QSL_RCVD = Y` 또는 `LOTW_QSL_RCVD = Y`이면 그 그리드는 **확인됨**입니다.
- 그리드는 다른 파일을 불러오거나 **메모리 지우기**를 누를 때까지 `data/adif_quadrati.csv`에 보관됩니다.

YA-MS는 LoTW에 접속하지 **않습니다**: 로깅 프로그램(또는 LoTW)에서 ADIF를 내보내 여기서 불러오세요.
