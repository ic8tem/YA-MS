[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · **Polski** · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# Rozwiązywanie problemów i FAQ

## Instalacja i uruchamianie

### Windows SmartScreen wyświetla „System Windows ochronił ten komputer”
Program nie jest podpisany komercyjnym certyfikatem. Kliknij *Więcej informacji* → *Uruchom mimo to*. Pobieraj go wyłącznie ze strony [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: nie można otworzyć, bo pochodzi od niezidentyfikowanego dewelopera
YA-MS nie jest podpisany przez Apple, więc **Gatekeeper** blokuje go za pierwszym razem. W pliku `.dmg` **kliknij prawym przyciskiem „Installa YA-MS.command” → Otwórz** i potwierdź. Skrypt usuwa z `~/YA-MS/YA-MS.app` flagę kwarantanny „pobrano z internetu” i otwiera aplikację. Jeśli macOS nadal odmawia, otwórz *Ustawienia systemowe → Prywatność i ochrona* i naciśnij *Otwórz mimo to*.

### macOS: który plik .dmg?
`-mac-apple-silicon.dmg` dla procesorów M1/M2/M3/M4, `-mac-intel.dmg` dla Maców z procesorem Intel (menu Apple → *Ten Mac* pokazuje, który masz).

### Linux: YA-MS nie ma w menu aplikacji
Uruchom `./installa.sh` z rozpakowanego folderu (nie z `~/YA-MS`). Niektóre środowiska graficzne wymagają wylogowania i ponownego zalogowania, aby pokazać nowe pozycje. Zawsze możesz uruchomić program poleceniem `~/YA-MS/YA-MS`.

### Brakuje mapy Europy
*Mapa Europy niedostępna (przy pierwszym uruchomieniu potrzebna jest sieć).* Mapa Natural Earth jest pobierana do `data/mappa` przy pierwszym uruchomieniu. Połącz się z internetem i uruchom YA-MS ponownie.

## Wyświetlanie

### Linux: tekst japoński wyświetla się jako prostokąty
W systemie brakuje czcionek CJK (chińskich, japońskich, koreańskich). Zainstaluj czcionki **Noto CJK** i uruchom YA-MS ponownie. To samo dotyczy arabskiego, hebrajskiego, urdu, hindi i bengalskiego: w systemach Debian, Ubuntu i Raspberry Pi OS zainstaluj także `fonts-noto-core`.

| Dystrybucja | Polecenie |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Tekst jest za mały lub wykresom brakuje miejsca
Użyj suwaka **Czcionka** (100–300 %) i zwiń wiersze przyciskiem **Sterowanie**. Zob. [Ustawienia](Settings-and-Data-Folder-pl#czcionka-i-sterowanie).

### Ekran jest w nocy za jasny
Wybierz **Noc** lub **Czarny** z listy **Motyw**.

## Internet i dane radarowe

### Komunikat „Brak połączenia z internetem”
YA-MS wyświetla go **jeden raz**, gdy żadne źródło nie jest osiągalne; pasek stanu zmienia kolor na czerwony. Program działa dalej z **ostatnio zapisanymi danymi** i sam ponawia próbę co 5 minut; gdy sieć wróci, pojawia się *Połączenie przywrócone.* Nie trzeba nic robić.

### Pomarańczowe ostrzeżenie w zakładce Strumień radarowy: „Nie można odczytać pionowej skali strumienia …”
Radar w Collm codziennie zmienia swoją skalę pionową, a YA-MS odczytuje ją z etykiet wykresu. Jeśli etykiety nie da się odczytać, program używa skalibrowanej skali 0–1200 meteorów/godzinę i ostrzega, że **wartości wymagają sprawdzenia**. Zwykle następny wykres godzinowy jest odczytywany poprawnie. Jeśli przez wiele godzin widzisz *Zmienił się format wykresu* lub *Nie znaleziono osi strumienia w oczekiwanym miejscu*, radar zmienił format swoich wykresów: prosimy, [zgłoś to](Contributing-and-Contacts-pl).

### „Zmieniła się skala wykresu wysokości”
Statystyki wysokości (dominanta, średnia, mediana) pozostają ważne; tylko bezwzględne liczebności histogramu wysokości już nie.

### „Strumień radarowy: brak danych”
Naciśnij **Pobierz teraz** w zakładce [Strumień radarowy](Radar-Flux-pl) i sprawdź, czy `data/fonti_radar.csv` ma `attivo=1` dla Collm.

### RMOB: dlaczego automatyczne pobieranie jest wyłączone?
RMOB prosi, aby **programy automatyczne nie pobierały jego plików**. Włącz *automatyczne pobieranie co 5 minut* dopiero wtedy, gdy RMOB udzieli ci zgody. Do tego czasu używaj **Pobierz RMOB teraz** lub **Wczytaj plik RMOB z dysku...**. Zob. [Prognozy eksperymentalne](Experimental-Forecasts-pl#rmob-a-programy-automatyczne).

### RMOB: „Nie rozpoznano formatu pliku” lub odczytano mało godzin
Użyj miesięcznego pliku tekstowego obserwatora (`NAME_MMYYYYrmob.TXT`) lub tabeli z biuletynu z jednym obserwatorem. Dopasowanie wykładnika wymaga co najmniej 3 godzin wspólnych z danymi z Collm (wczoraj i dziś).

## Obliczenia

### „Nieprawidłowy lokator stacji” / „Nieprawidłowy lokator stacji DX”
Lokatory muszą mieć 4, 6 lub 8 znaków (np. `JN70`, `JN70CN`, `JN70CN12`).

### „Brak wspólnej strefy warstwy E”
Trasa jest dłuższa niż dwukrotność zasięgu na wysokości śladu (około 2 × 1062 km przy listku na 0° i śladach na 89,5 km): pojedynczy skok meteor scatter nie jest w stanie jej pokryć. Podniesienie **Elewacji listka** jeszcze bardziej skraca zasięg.

### Hot A / Hot B są szare
Znajdują się już **wewnątrz listka twojej anteny**, gdy jest ona skierowana na DX: nie trzeba jej obracać. Zob. [Kopuła nieba](Sky-View-pl#ostrzeżenia).

### Efektywność różni się od MCG_MS lub MS-Soft
YA-MS używa rzeczywistej trasy i własnego modelu; skala OH5IY i MCG_MS nie jest szczegółowo udokumentowana. Porównuj godziny i tendencje, a nie bezwzględne procenty, i zapoznaj się z [modelem](Efficiency-Calculation-pl#model).

### Przejście wiązki GRAVES wydaje się przesunięte
Sekwencja wiązki jest obliczana na podstawie zegara komputera: zsynchronizuj go z serwerem NTP. Stacja sterująca GRAVES czasem też przesuwa sekwencję o kilka kroków; szczegóły są przewidywaniem do potwierdzenia nasłuchem.

## Inne pytania

**Czy YA-MS jest darmowy?** Tak, to darmowy program dla radioamatorów.

**Czy steruje moim rotatorem lub radiem?** Nie. YA-MS to narzędzie do prognozowania i planowania; do przeprowadzenia QSO używaj programu do emisji cyfrowych (np. MSHV, WSJT-X).

**Czy działa powyżej 432 MHz?** Lista pasm kończy się na 432 MHz (28, 50, 70, 144, 222, 432). Prognoza eksperymentalna przyjmuje dowolną częstotliwość od 28 do 1300 MHz, ale używane w niej reguły SM6FHZ wynikają z doświadczeń na 144 i 432 MHz.

**Coś poszło nie tak.** Napisz do autora, podając system operacyjny, wersję YA-MS i to, co robiłeś: zob. [Współpraca i kontakt](Contributing-and-Contacts-pl).
