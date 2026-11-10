[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · **한국어** · [中文](Settings-and-Data-Folder-zh)

# 설정과 데이터 폴더

## 탭 표시줄

탭 표시줄의 오른쪽 끝에 오른쪽에서 왼쪽 순으로:

| 조작 항목 | 기능 |
|---|---|
| **언어**(목록) | 인터페이스 언어; [언어](#언어) 참조 |
| **테마**(목록) | 색 구성; [색 구성](#색-구성) 참조 |
| **조작 ▴ / ▾** | 탭 위의 세 줄 조작 항목을 접거나 펼침; [글꼴과 조작](#글꼴과-조작) 참조 |

언어나 테마를 바꾸면 설정이 저장되고 같은 위치와 크기, 같은 탭으로 **창을 다시 구성합니다**: 재시작할 필요가 없습니다.

## 언어

인터페이스 언어 6가지:

| 언어 | 코드 | 파일 |
|---|---|---|
| Italiano | `it` | 없음: 이탈리아어가 기본 언어(키) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

처음 실행할 때 YA-MS는 **시스템 언어**가 이 중 하나이면 그 언어를, 아니면 이탈리아어를 사용합니다. 숫자와 날짜는 선택한 언어를 따릅니다(예: 영어는 소수점, 이탈리아어와 독일어는 쉼표). 번역 파일에 없는 텍스트는 이탈리아어로 표시됩니다. Linux에서 일본어를 표시하려면 알맞은 글꼴이 필요합니다: [문제 해결](Troubleshooting-FAQ-ko#linux-일본어-문자가-네모로-표시됨)을 참조하세요.

[효율 - 설명](Efficiency-Explanation-ko) 문서와 계산 매뉴얼은 이탈리아어로 되어 있습니다.

## 색 구성

**테마** 목록에는 12가지 구성이 있으며, 작성자의 EME 프로그램 YAEC와 같은 구성에 YA-MS 원래 팔레트를 더한 것입니다:

| 구성 | 설명 |
|---|---|
| **밝음** | 기본값 |
| **야간** | 어두운 파란 계열, 밤에 사용 |
| **검정** | 검은 배경, 어두운 곳과 OLED 화면용 |
| 파스텔 하늘색 · 파스텔 주황 · 파스텔 아쿠아마린 · 파스텔 초록 · 파스텔 분홍 · 파스텔 라일락 · 파스텔 남색 · 파스텔 갈색 | 밝은 파스텔 구성 8가지 |
| **유성 흔적** | YA-MS 원래 스타일(버전 1.2.0까지): 밤의 보라색 바탕에 하늘색, 보라, 연두, 노랑, 주황 |

구성은 모든 탭에 적용되며 `config.ini`(키 `tema`)에 저장됩니다.

## 글꼴과 조작

- **글꼴**(조작 항목 1행 끝): **모든 텍스트**를 10 % 단위로 **100–300 %**까지 키웁니다. 선, 원, 지도의 크기는 그대로입니다. 글꼴이 크면 탭이 두 번째 줄로 넘어가고 카드가 커집니다.
- **조작**: 글꼴이 크거나 화면이 작을 때 세 줄의 조작 항목을 접어 지도와 그래프의 공간을 확보합니다. 상태는 기억됩니다.

## 데이터 폴더

모든 데이터와 설정은 **프로그램 옆의** **`data`** 폴더 하나에 있습니다 – AppData도 시스템 폴더도 사용하지 않습니다:

| 시스템 | 프로그램 | 데이터 |
|---|---|---|
| Windows (설치 프로그램) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (포터블) | 압축 해제한 위치 | `YA-MS.exe` 옆의 `data` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data`(앱 옆) |

시작할 때 필요하면 폴더를 만들고 **없는** 초기 파일만 복사합니다: 사용자가 수정한 파일은 절대 덮어쓰지 않습니다. `data/lingue`의 번역 파일은 프로그램 파일이므로 새 버전의 파일이 더 최신이면 교체됩니다.

### 편집할 수 있는 파일

| 파일 | 내용 |
|---|---|
| `sciami.csv` | 유성우 목록(IMO 값과 작업값); [유성우](Showers-ko#목록-편집) 참조 |
| `massimi_imo.csv` | IMO가 발표한 극대 날짜와 시각(2026, 2027): 여기에 **새 연도를 추가** |
| `ant_radiante.csv` | Antihelion Source 위치(IMO 표 6) |
| `fonti_radar.csv` | 레이더 주소; `attivo=1`은 다운로드, `0`은 무시 |
| `regole_sperimentali.csv` | 사용하는 상수와 규칙, 각각의 출처(참고용) |
| `lingue/<code>.txt` | 인터페이스 번역; [기여](Contributing-and-Contacts-ko#번역) 참조 |
| `config.ini` | 설정(아래 참조) |

### 프로그램이 만드는 파일

| 파일 / 폴더 | 내용 |
|---|---|
| `config.ini` | 설정 |
| `flusso_collm.csv` | Collm 플럭스의 시간별 아카이브 |
| `quote_collm.csv` | 흔적 고도 아카이브 |
| `radar/` | 최신 레이더 이미지와 RMOB 파일 |
| `mappa/` | Natural Earth 해안선과 국경(첫 실행 시 다운로드) |
| `adif_quadrati.csv` | 마지막으로 불러온 ADIF의 그리드 |
| `efficienza_spiegazione.txt`, `.docx` | [설명 문서](Efficiency-Explanation-ko) |

## config.ini

일반 텍스트이며 한 줄에 `key=value` 하나(`#`나 `;`로 시작하는 줄은 주석). 프로그램이 종료할 때 기록하므로 **YA-MS를 닫은 상태에서 편집하세요**. 알아 둘 만한 키:

| 키 | 기본값 | 의미 |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | 내 로케이터와 고도(m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | 상대국 로케이터와 고도(m) |
| `banda_MHz` | 144 | 밴드(28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | 흔적 고도(km); 1 = Collm 최빈값 사용 |
| `elevazione_lobo_gradi` | 0 | 로브 앙각(°) |
| `boom_m` | 4.6 | 야기 붐 길이(m) |
| `hot_spot_km` | 150 | 중간점에서 Hot A / Hot B까지 거리(30–400 km) |
| `lingua` | 시스템 / `it` | 언어 코드(`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | 색 구성: `chiaro`(밝음), `scuro`(야간), `nero`(검정), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia`(유성 흔적) |
| `carattere_pct` | 100 | 글꼴 크기(100–300 %) |
| `comandi_visibili` | 1 | 1 = 조작 항목 표시, 0 = 접음 |
| `mostra_mappa`, `vista_alto` | 1, 1 | 유럽 지도, 천구의 위에서 본 모습 |
| `aggiornamento_automatico` | 1 | 5분마다 소스 자동 확인 |
| `esponente_lambda` | 3 | 레이더 플럭스 탭의 λ 지수 |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | 링크 버짓 입력값 |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | 실험적 예보: 주파수, k, K |
| `rmob_osservatore` | 비어 있음 | RMOB 관측자 이름 |
| `rmob_automatico` | 0 | RMOB 자동 다운로드(RMOB의 허가가 있을 때만 사용) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB 주소 템플릿 |
| `graves_sequenza` | 0 | GRAVES 빔 시퀀스: 0 = 0.8 s(2021), 1 = 3.2 s(2007) |

## 개인정보

YA-MS는 데이터를 수집하지 않고 광고도 표시하지 않습니다. 공개 데이터를 다운로드할 때만 인터넷에 접속합니다: Collm과 Sodankylä 레이더 이미지, Natural Earth 지도(첫 실행 시), 그리고 요청한 경우 RMOB 파일.
