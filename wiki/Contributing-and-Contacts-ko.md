[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · **한국어** · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# 기여와 연락처

YA-MS는 실제 운용에서 사용하는 분들의 보고를 통해 발전합니다. 모든 수정 사항은 그 출처를 밝혀 반영합니다.

## 연락처

| | |
|---|---|
| 작성자 | Costantino Cerrotta **IC8TEM** |
| 이메일 | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## 문제 보고

**GitHub에 issue**를 열거나 다음 내용을 담아 이메일을 보내 주세요:

- 운영 체제와 YA-MS 버전(창 제목에 표시);
- 두 로케이터, 밴드, UTC 시각;
- 기대한 결과와 실제로 본 결과(스크린샷이 있으면 도움이 됨);
- 레이더 문제의 경우 [레이더 플럭스](Radar-Flux-ko) 탭에 표시된 메시지.

## 특히 도움이 되는 것

- **실제 운용 보고.** 효율이나 예보가 맞았던 – 또는 틀렸던 – 시간대와 경로. 모델은 실험적이므로 실제 QSO 및 MCG_MS / MS-Soft와의 비교가 필요합니다.
- **RMOB 비교.** [RMOB 비교](Experimental-Forecasts-ko#rmob-비교)로 구한 국 계수 K와 지수 k의 값을 밴드와 국 정보와 함께.
- **출처가 있는 데이터.** 더 나은 복사점 이동, 활동 프로필, 새 IMO 극대 날짜(`data/massimi_imo.csv`), 안테나 데이터: 출처를 함께 주시면 인용하겠습니다.
- **레이더 그래프의 변경.** Collm 그래프 형식이 바뀌면 이미지 사본(`data/radar/`)이 읽기 재보정에 도움이 됩니다.

## 번역

인터페이스 번역은 **`data/lingue/<code>.txt`**(UTF-8)의 일반 텍스트 파일이며 **누구나 수정할 수 있습니다**:

```
<Italian text><TAB><translation>
```

- 한 줄에 항목 하나. `#`로 시작하는 줄은 주석입니다.
- 두 열 모두에서 두 문자 `\n`은 줄바꿈을 뜻합니다.
- 자리 표시자 `{0}`, `{1}`, …는 형식(예: `{0:F1}`, `{3:+0;-0}`)을 유지한 채 언어에 맞는 순서로 두세요.
- 없거나 비어 있는 항목은 이탈리아어로 표시됩니다. 모든 키의 목록은 `data/lingue/chiavi.txt`입니다(`tools/estrai_chiavi.py`로 생성되므로 편집하지 마세요).

설치 폴더의 `data/lingue`에 있는 파일을 편집하고 YA-MS를 다시 시작(또는 언어를 전환)하면 결과를 볼 수 있습니다. 이 파일들은 **업데이트할 때마다 새 버전으로 교체되므로**, 수정 사항을 이메일이나 GitHub pull request(`data/lingue/`)로 **보내 주시면** 다음 릴리스에 반영됩니다.

이 위키는 36개 언어(English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體))로 제공되며, 위키 페이지에 대한 수정도 환영합니다.
