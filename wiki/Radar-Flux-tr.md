[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · **Türkçe** · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · [Bahasa Indonesia](Radar-Flux-id) · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Radar akısı

*Sekme: Canlı ve gerçek zamanlı veriler › Radar akısı.*

[![Radar akısı](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Bu sekme profesyonel meteor radarlarının **şu anda** ne saydığını gösterir: **Collm** SKiYMET radarının (Leipzig Üniversitesi / IAP Kühlungsborn, Almanya, 36,2 MHz) saatlik meteor sayıları ve iz yükseklikleri ile **Sodankylä** radarının (SGO, Finlandiya) en son görüntüsü. Collm sayımları sizin bandınız için tahmini ve [Deneysel tahminler](Experimental-Forecasts-tr) sekmesini besler; ölçülen iz yüksekliği ise bütün geometriyi besler.

## Kontroller

| Kontrol | Ne yapar |
|---|---|
| **Şimdi indir** | Tüm dış kaynakları bir kerede denetler. |
| **Tüm kaynakların 5 dakikada bir otomatik güncellenmesi** | Varsayılan olarak açık. Her 5 dakikada bir tüm kaynaklar denetlenir ve **yalnızca değişenler** yeniden indirilir (*değişmedi (… UTC'de denetlendi)* / *… UTC'de yeni veri*). |
| **λ üssü (SM6FHZ)** | Frekans kuralının k üssü, varsayılan 3 (1–4). |

## Gösterilenler

| Panel | İçerik |
|---|---|
| **Meteor/saat – dün ve bugün (UTC)** | Camgöbeği çubuklar = Collm sayımları (geçerli), kırmızı çubuklar = atılanlar, kalın turuncu çizgi = sağ ölçekte *… MHz'de tahmin* |
| **İz yükseklikleri (Collm)** | 70 ile 110 km arasında km yükseklik başına meteor; en sık yükseklik (mod), ortalama, medyan ve standart sapma ile |
| Collm görüntüsü | İndirildiği haliyle özgün SKiYMET grafiği |
| Sodankylä görüntüsü | Sodankylä radarının en son meteor sayımı görüntüsü (yalnızca gösterilir; biçimi okunmaz) |

Grafiklerin üstündeki satır, Collm grafiğinin ne zaman okunduğunu ve hangi dikey ölçeğin bulunduğunu söyler (*grafikten okunan ölçek: 0-… meteor/saat*).

## Collm grafiği nasıl okunur

Collm grafiğinin (720 × 720 piksel, saf renkler) eksen konumları sabittir, ama radar **dikey ölçeği her gün** ölçülen değerlere göre **uyarlar** (örn. 5/11/2026'da 0–1,2·10³ ve 6/11/2026'da 0–1,0·10³, kaymış çentiklerle). Bu yüzden YA-MS:

1. eksenin uzun çentiklerini bulur;
2. her karakteri grafiğin nokta matrisli yazı tipiyle karşılaştırarak en üst çentiğin ve sıfırın **etiketlerini okur**;
3. her i saati (0–47, dün ve bugün) için orta sütunu ve yukarıdan ilk camgöbeği pikseli, y'yi alır:

```math
x_i = 101 + (i+0{.}5)\,\frac{676-101}{48},\qquad N = (y_0-y)\,\frac{N_{top}}{y_0-y_{top}}
```

y_top ve y0 en üst çentiğin ve sıfırın satırları, N_top en üst etikette okunan değerdir (×1000). Çözünürlük: piksel başına yaklaşık 7–8 meteor/saat. *Programın seçimi (kılavuz denk. 42).*

Bir etiket okunamazsa program 5/11/2026 kalibrasyonuna döner (**kalibre ölçek 0-1200 meteor/saat**) ve bunu turuncuyla belirtir: *Akının dikey ölçeği okunamıyor (üst etiket: …): değerler denetlenmeli.* Grafik biçiminin kendisi değişirse (*Grafik biçimi değişti (…x…): okunamıyor.* ya da *Akı eksenleri beklenen konumda bulunamadı.*), okumanın yeniden kalibre edilmesi gerekir: lütfen bildirin (bkz. [Katkıda bulunma](Contributing-and-Contacts-tr)).

### İz yükseklikleri

Yükseklik histogramından (k km'de n_k meteor, ortalama yükseklik h_k):

```math
\hat{h} = h_{k^*},\ k^* = \arg\max_k n_k,\qquad \bar{h} = \frac{\sum_k n_k h_k}{\sum_k n_k},\qquad s = \sqrt{\frac{\sum_k n_k (h_k-\bar{h})^2}{\sum_k n_k}}
```

*Kılavuz denk. 43.* **radardan** işaretliyken (kontrollerin 2. sırası) **mod**, tüm hesapların iz yüksekliği olur. Doğrulama: 5/11/2026 grafiği – mod 89,5 km, ortalama 88,6 km, standart sapma 6,8 km; Cerrotta–Sartori makalesindeki ~90 km'yi (SKiYMET ortalaması) doğrular.

Yükseklik grafiğinin ölçeği değişirse program uyarır: *yükseklik istatistikleri (mod, ortalama, medyan) geçerli kalır, mutlak sayımlar geçerli değildir.*

## Bandınız için tahmin

```math
N(f) = N_{Collm}(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k},\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}
```

**SM6FHZ**'nin deneysel kuralları (VUSHF 2025): yansımaların sayısı ve şiddeti λ³ ile, süresi λ² ile ölçeklenir (McKinley'de λ³ tek bir izin gücüdür; iz sayısı yaklaşık λ^1,5 ile ölçeklenir ve ileri saçılmada süreler ayrıca sec²φ ile artar: bkz. [Deneysel tahminler](Experimental-Forecasts-tr)). IARU 1. Bölge en uzun ping süresi de gösterilir (50 MHz'de 1000 ms, 70 MHz'de 500 ms, 144 MHz'de 100 ms, 432 MHz'de 13 ms). Değerler yol göstericidir; havadaki deneyimle karşılaştırılmalıdır. İstasyon katsayısı K ve RMOB ile karşılaştırma [Deneysel tahminler](Experimental-Forecasts-tr) sayfasındadır.

## Bağlantı yokken

Hiçbir kaynağa ulaşılamazsa **bir kez** bir ileti çıkar: *İnternet bağlantısı yok. Radar ve RMOB verileri güncellenemiyor: program son kaydedilen verileri kullanır ve 5 dakikada bir kendiliğinden yeniden dener.* Alttaki durum çubuğu bağlantı geri gelene kadar (*Bağlantı yeniden kuruldu.*) kırmızı olur (*İNTERNET BAĞLANTISI YOK …*).

## Arşivler ve kaynaklar

| Dosya (`data/` içinde) | İçerik |
|---|---|
| `flusso_collm.csv` | Collm'dan okunan akının saatlik arşivi (zaten var olan saatler güncellenir) |
| `quote_collm.csv` | İz yüksekliklerinin arşivi |
| `radar/` | En son indirilen görüntüler (ve RMOB dosyaları) |
| `fonti_radar.csv` | Radar kaynaklarının adresleri; her birini açmak/kapatmak için `attivo=1/0` |

| Kaynak | Frekans | Notlar |
|---|---|---|
| Collm meteor radarı, Leipzig Üniversitesi (LIM) ve IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | her saat 10. dakikada (UTC) güncellenir; dün + bugün akısı, yükseklik dağılımı |
| Sodankylä Jeofizik Gözlemevi – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | yalnızca görüntü (radar yenileniyor, DECC projesi) |
| swan.ms (Collm kopyası) | 36,2 MHz | varsayılan olarak kapalı; yalnızca DL1DBC'nin izniyle kullanın |

> Radar verileri sahibi kurumlara aittir (Leipzig Üniversitesi / IAP Kühlungsborn, Sodankylä Jeofizik Gözlemevi).
