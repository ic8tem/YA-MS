[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · **Polski** · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [ไทย](Data-Collection-th) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Zbieranie danych

*Zakładka: Na żywo i dane w czasie rzeczywistym › Zbieranie danych.*

[![Zbieranie danych](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Trzy strumienie klastrów

Zakładka zbiera **spoty meteor scatter** z trzech strumieni telnet, każdy w osobnej podzakładce:

| Podzakładka | Domyślnie | Uwagi |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Klaster do wyboru. Na ON0DXK pasma VHF są filtrowane: włącz je poleceniem `set/filter dxbm/pass 6` (potem 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmery rzadko dekodują emisje MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Klaster DM4X przekazujący spoty **PSKReporter**: tu trafiają dekodowania MSK144 z WSJT-X i MSHV. |
| **Zebrane spoty MS** | – | Tabela przyjętych spotów, najnowsze na górze. |

Każdy strumień ma host, port, polecenia wysyłane po zalogowaniu, *Połącz ponownie*, *Połącz przy uruchomieniu*, konsolę i wiersz do wysyłania poleceń. Na górze wpisz swój **znak wywoławczy do logowania**. Pasek pokazuje stan trzech sesji (zielona kropka = połączono). Sesje pozostają otwarte, gdy zmieniasz język lub schemat kolorów.

## Filtr (40 % okna)

- **Opcjonalny filtr lokalny:** wiersze klastra poniżej **27990,0 kHz** są od razu odrzucane (nie są wyświetlane ani zapisywane).
- **1. kryterium – typowe częstotliwości MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot w tych oknach jest przyjmowany nawet bez nazwy emisji, chyba że komentarz deklaruje inną propagację: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Okna i znaczniki można edytować.
- **2. kryterium – emisje MS:** poza oknami albo z jednym z tych znaczników spot jest zachowywany tylko wtedy, gdy zawiera **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (emisje cyfrowe używane tylko do MS) lub **\<MS\>**, pisane wielkimi, małymi lub mieszanymi literami. Słowa można wyłączać, dodawać i usuwać; każde ma swój licznik.
- **Pasma** 28, 50, 70, 144, 222, 432 MHz; **test filtra** na wklejonym wierszu; **liczniki**.

## Lokatory i zapis

Brakujące lokatory albo lokatory tylko 4-znakowe są pobierane z archiwum **CALL3** (`data/call3.txt`, plik JTDX, ponad milion znaków wywoławczych), które zawsze ma pierwszeństwo przed lokatorem 4-znakowym. Przyjęte spoty są zapisywane w `data/spot_ms`, jeden plik CSV na dzień, i zasilają mapę [Ruch na żywo](Live-Traffic-pl).
