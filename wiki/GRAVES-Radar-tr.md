[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · **Türkçe** · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · [Bahasa Indonesia](GRAVES-Radar-id) · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# GRAVES radarı

*Sekme: Canlı ve gerçek zamanlı veriler › GRAVES radarı.*

[![GRAVES radarı](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## GRAVES nedir

**GRAVES**, **Broye-lès-Pesmes**'ten (47,348° K 5,515° D, lokatör **JN27SI**, deniz seviyesinden yaklaşık 200 m; Wikipedia) **143,050 MHz'de CW** yayın yapan bir Fransız radarıdır. Hem GRAVES'in hem de sizin görebildiğiniz bölgedeki meteor izleri sinyalini size **forward scatter** ile yansıtır: taşıyıcıya yakın kısa *pingler* duyarsınız. **RMOB** gözlemcileri 143,050 MHz'de meteorları saat saat bu yolla sayar; ayrıca 2 m meteor scatter istasyonunuz için ücretsiz, her zaman açık bir deneme sinyalidir.

Sekme **GRAVES → siz** yolunu başlı başına bir meteor scatter yolu olarak ele alır: ana yolla aynı işlevlerle (aynı iz yüksekliği, lob elevasyonu ve hot spot mesafesi) yağmur verimini, önerilen Hot'u ve PREV bölgelerini hesaplar, sonra bu bölgenin **GRAVES huzmesinin içinde** olup olmadığını ve huzmenin onu **ne zaman** aydınlattığını denetler.

## Üst çubuk

| Kontrol | Ne yapar |
|---|---|
| **Şimdi** | Gökyüzü kubbesi saatini gerçek zamana döndürür (sekme *Gökyüzü kubbesi saati* kaydırıcısını izler). |
| **GRAVES'i DX yap** | Karşı istasyon GRAVES olur (JN27SI, yükseklik 200 m) ve ana yol yeniden hesaplanır: bundan sonra diğer tüm sekmeler GRAVES yolunu gösterir. |
| **Huzme dizisi** | *adım başına 0,8 s · döngü 4,8 s (PE1ITR 2021)* (varsayılan) ya da *adım başına 3,2 s · döngü 19,2 s (PE1ITR 2007)*. |

## Dört kart

| Kart | İçerik |
|---|---|
| **GRAVES HUZMESİNDEKİ YARARLI BÖLGE** | GRAVES'ten görülen önerilen hot spot'un azimutu ve elevasyonu ile adım (1–6) birlikte *Evet · sektör X*; ya da *Hayır: sektörlerin dışında* / *Hayır: GRAVES ufkunun altında* / *Hayır: huzmenin üstünde (yaklaşık 25°)* |
| **GRAVES → SİZ YOLUNUN ŞU ANKİ VERİMİ** | Yol endeksi Σ ZHR × verim, en iyi yağmur, baskın taraf A/B ve *beklenen yankı ≈ …/saat* (deneysel, aşağıya bakın) |
| **YOL** | GRAVES'e mesafe; önerilen Hot'a doğru anten (azimut ve elevasyon); GRAVES doğrudan azimutu |
| **HUZMENİN BÖLGE ÜZERİNDEN SONRAKİ GEÇİŞİ** | *şimdi · … s kaldı* ya da *… s sonra*, adım (örn. *B4*), sonraki üç an (dakika içindeki saniyeler) ve yakalanan izlerin oranı |

O anda hiçbir yağmur yararlı değilse program **huzmeye en uygun** hot spot'u (sektörlerin içinde, güneye en yakın) gösterir ve bunu belirtir.

## GRAVES'ten görülen gökyüzü

PE1ITR ve Bolidozor wiki'sine göre **dört fazlı dizi**, güney gökyüzünü **90° ile 270°** azimut arasında dört adet **45°'lik sektörle** kaplar:

| Sektör | GRAVES'ten azimut |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Her sektör **7,5°'lik 6 adıma** bölünür; adımlar en düşük azimuttan başlayarak 1'den 6'ya numaralanır ve birbiri ardına, **dört sektörde aynı anda** aydınlatılır. Huzme **elevasyonda yaklaşık 25° geniştir**: iz yüksekliğinde iki kesikli daire (*huzme ufku*) arasındaki renkli halkayı kaplar. Çizimde: turuncu/pembe noktalar = GRAVES → siz yolunun PREV bölgeleri, yeşil çizgi = istasyonunuzun yönü, kırmızı çizgi = istasyonunuzdan önerilen hot spot'a; şu anda aydınlatılan adım vurgulanır.

## Zaman sıralı yeniden kurulum

*ZAMAN SIRALI YENİDEN KURULUM · tarih UTC* (24 saatlik tabloyla aynı gün): her saat için GRAVES → siz yolunun verimi, en elverişli yağmur ve yararlı pencere (*hh:00 → hh:00 UTC · n sa*); en yüksek değer (*en yüksek Σ …, saat hh:30*) ve kırmızı bir *şimdi* işaretiyle. Altta **sonraki saniyelerin ayrıntısı**: sektörün altı adımı, yararlı bölgeyi aydınlatan adım ve *olası yankı (+0,3 s iz)*.

### Huzme zamanlaması

Dizi **UTC**'ye bağlıdır (PE1ITR): şu anda aydınlatılan adım, 00:00 UTC'den beri geçen saniyelerin döngüye göre modundan hesaplanır (86 400 s hem 4,8 s'nin hem 19,2 s'nin katıdır). Komuta istasyonu diziyi zaman zaman birkaç adım kaydırır; bu yüzden ayrıntı **dinleyerek doğrulanacak bir öngörüdür**. Sarı **PC saati eşitlendi** etiketi bunu hatırlatır: PC'nizi bir NTP sunucusuyla eşitleyin (hata en fazla birkaç saniyenin onda biri).

### Algılama katsayısı

Bir iz, ancak sürdüğü sırada huzme onu aydınlatırsa duyulur:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s, 143 MHz'de tipik bir underdense iz süresidir – sabit bir değer, *programın seçimi* (SM6FHZ'nin λ² kuralı süreleri bantlar arasında ölçekler ama bir başlangıç değeri vermez).

### Beklenen yankılar (deneysel)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

[Deneysel tahminler](Experimental-Forecasts-tr) sekmesindeki tahmin (istasyon katsayısı K'yı zaten içerir) SM6FHZ kuralıyla (aynı k üssü) kendi frekansı f_fc'den 143,050 MHz'e ölçeklenir, iki yolun yağmur endekslerinin oranıyla düzeltilir (10 sabiti, tahmindeki gibi sporadik arka planı temsil eder) ve algılama katsayısıyla çarpılır. Yalnızca yol göstericidir: RMOB gözlemcileriyle karşılaştırın.

## GRAVES pingleri nasıl dinlenir

| Adım | Ne yapmalı |
|---|---|
| Alıcı | **143,049 MHz'de USB** (yaklaşık 1 kHz'lik ton) ya da 143,050 MHz, **yavaş ya da kapalı AGC**, **en az 2,4 kHz** ses bant genişliği |
| Anten | GRAVES → siz yolunun **önerilen hot spot**'una doğru (*YOL* kartı), **düşük elevasyonda** |
| Şelale | Pingler **taşıyıcıya yakın kısa çizgilerdir**; uzun (overdense) izler daha geniştir ve Doppler gösterir |
| Sayım | RMOB saatlik meteor sayımları için GRAVES'i kullanır: **pinglerinizi 143,050 MHz'deki gözlemcilerle karşılaştırın** ([Deneysel tahminler](Experimental-Forecasts-tr#rmob-karşılaştırması)) |

## Kaynaklar

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) ve *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. **Bolidozor** wiki'si, "Graves" – diziler, sektörler ve huzme zamanlaması
3. **Wikipedia**, "GRAVES (system)" – Broye-lès-Pesmes'teki verici (47,348° K 5,515° D)
4. **RMOB** – 143,050 MHz'deki gözlemciler ([rmob.org](https://www.rmob.org))
5. IC8TEM'in **YAEC** programı – GRAVES Radar sekmesi (bu sekmenin türetildiği taslak)
