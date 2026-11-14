[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · **Polski** · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Zbieranie danych

*Zakładka: Dane na żywo i w czasie rzeczywistym › Zbieranie danych.*

[![Zbieranie danych](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Cztery źródła

Zakładka zbiera **spoty meteor scatter** z trzech strumieni telnet oraz z kanału MQTT PSKReporter, każdy w osobnej podzakładce:

| Podzakładka | Domyślnie | Uwagi |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Dowolny wybrany cluster. Na ON0DXK pasma VHF są filtrowane: włącz je poleceniem `set/filter dxbm/pass 6` (potem 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmery rzadko dekodują emisje MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X przekazujący spoty **PSKReporter**: tutaj trafiają dekody MSK144 z WSJT-X i MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spoty PSKReporter na żywo przez **MQTT** (usługa M0LTE): bez logowania, każdy spot zawiera już lokatory stacji nadającej i odbierającej. Domyślne tematy: MSK144 na 6 m, 4 m, 2 m, 1,25 m, 70 cm oraz FSK441 na 2 m (`pskr/filter/v2/band/mode/#`); *Domyślne tematy* je przywraca. |
| **5. WSJT-X / JTDX / MSHV przez UDP** | 127.0.0.1 : 2237 → 2238 | Jak w LIVETROPOVHF: program nasłuchuje komunikatów UDP programu cyfrowego (w WSJT-X: Ustawienia, Reporting, UDP Server 127.0.0.1 port 2237) i powtarza je bez zmian na porcie przekazywania dla innych programów (GridTracker, JTAlert, log). Każda zdekodowana stacja staje się spotem usłyszanym przez twoją stację; komunikaty kończące (RR73, 73, RRR) między dwiema innymi stacjami stają się trasą ich QSO. Spoty przechodzą przez te same filtry co pozostałe. |
| **Zebrane spoty MS** | – | Tabela zaakceptowanych spotów, od najnowszych. |

Każdy strumień ma host, port, polecenia wysyłane po zalogowaniu, *Połącz ponownie*, *Połącz przy starcie*, konsolę i wiersz do wysyłania poleceń. Na górze wpisz swój **znak do logowania**. Źródło MQTT ma host, port, tematy (po jednym w wierszu lub rozdzielone `;`), *Połącz ponownie* i *Połącz przy starcie* (domyślnie wyłączone) oraz konsolę z odebranymi spotami; jego spoty przechodzą przez ten sam filtr. Pasek pokazuje stan czterech źródeł (zielona kropka = połączono). Sesje pozostają otwarte, gdy zmieniasz język lub schemat kolorów.

## Filtr (40 % okna)

- **Opcjonalny filtr lokalny:** wiersze clustera poniżej **27990,0 kHz** są od razu odrzucane (nie są wyświetlane ani zapisywane).
- Spoty CW są od razu odrzucane (CW lub WPM w komentarzu albo 28000-28070 kHz): nie pojawiają się w konsoli i nie są zapisywane, chyba że są oznaczone <MS>. Pole można wyłączyć.

Baza CALL3 z regułami LIVETROPOVHF. „Aktualizuj teraz" pobiera CALL3.TXT z MMMonVHF (co najmniej 100 000 poprawnych wierszy, poprzedni zostaje w data/call3.bak); z opcją „Aktualizuj samo co 7 dni" dzieje się to przy uruchomieniu. Nad plikiem obowiązują kolejno: wpisy ręczne (data/CALL3-MANUALE.TXT), poprawki z klastra (6-znakowy lokator, który spotujący deklaruje o sobie), dodane pliki (data/CALL3-AGGIUNTE), potem CALL3.TXT i 6-znakowe lokatory nauczone na żywo (data/LOC6.TXT). Odebrany lokator 4-znakowy albo kończący się na LL lub MM zastępuje się 6-znakowym z bazy; stacje przenośne (z ukośnikiem) tylko dokładnym wpisem.

Ostatnie źródło, jak w LIVETROPOVHF: dla znaków bez 6-znakowego lokatora w żadnym innym źródle program automatycznie co 6 godzin pyta publiczne API G7VRD (api.g7vrd.co.uk), w grupach po 40 znaków; każdy znak najwyżej raz dziennie. Przyjmowany jest tylko lokator 6-znakowy, nie środek kwadratu (LL lub MM), w tym samym kwadracie co odebrany. Wyniki są w data/CALL3-G7VRD.TXT i, jak wszystkie poprawki, są też zapisywane w data/call3.txt.
- Spoty między stacjami oddalonymi o mniej niż 500 km są od razu odrzucane, bo na tej odległości łączność jest bezpośrednia lub troposferyczna, a nie meteor scatter: nie pojawiają się w konsoli i nie są zapisywane. Jeśli brakuje lokatora, spot zostaje. Odległość zmienia się pod polem wyboru.
- **1. kryterium – typowe częstotliwości MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot w tych oknach jest akceptowany nawet bez nazwy emisji, chyba że komentarz deklaruje inny rodzaj propagacji: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Okna i znaczniki można edytować.
- **2. kryterium – emisje MS:** poza oknami lub z jednym z tych znaczników spot jest zachowywany tylko wtedy, gdy zawiera **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (emisje cyfrowe używane wyłącznie do MS) lub **\<MS\>**, pisane wielkimi, małymi lub mieszanymi literami. Słowa można wyłączać, dodawać i usuwać; każde ma swój licznik.
- **Pasma** 28, 50, 70, 144, 222, 432 MHz; **test filtra** na wklejonym wierszu; **liczniki**.

## Lokatory i zapis

Brakujące lokatory lub lokatory mające tylko 4 znaki są pobierane z archiwum **CALL3** (`data/call3.txt`, plik JTDX, ponad milion znaków), które zawsze ma pierwszeństwo przed lokatorem 4-znakowym. Zaakceptowane spoty są zapisywane w `data/spot_ms`, po jednym pliku CSV na dzień, i zasilają mapę [Ruch na żywo](Live-Traffic-pl).
