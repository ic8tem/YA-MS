[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Português (Brasil)](Sky-View-pt-BR) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Polski](Sky-View-pl) · [Čeština](Sky-View-cs) · [Magyar](Sky-View-hu) · [Română](Sky-View-ro) · [Ελληνικά](Sky-View-el) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · **Türkçe** · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · [ไทย](Sky-View-th) · [Bahasa Indonesia](Sky-View-id) · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh) · [中文 (繁體)](Sky-View-zh-TW)

# Gökyüzü kubbesi

*Sekme: Tahmin hesabı › Tahmin hesabı.*

[![Gökyüzü kubbesi](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Bu alt sekme (önceki sürümlerin gökyüzü kubbesi), yararlı izlerin şu anda **nerede** olduğunu ve antenin **nereye** çevrileceğini tek ekranda toplar. Solda yolun **plan görünümü**; sağda yağmur listesi, radyantlarla küçük bir gökyüzü kubbesi, hesabın metni ve anteninizden görülen **kesit**. Her şey *Hesap tarihi (UTC)* ve *Saatler (−12 ile +36 sa arası)* kaydırıcısıyla seçilen ana göredir (varsayılan gerçek zaman; 15 dakikalık adımlarla).

**Plan görünümünün üstündeki şerit** o anın hesabını özetler: tarih ve saat (*şimdi* ya da şimdiden itibaren saat), **yol endeksi Σ ZHR×η**, ZHR'si ve verimiyle (DJ5HG referansına göre dB cinsinden de, bkz. [Verim hesabı](Efficiency-Calculation-tr)) **en yararlı yağmur**, ufkun üstündeki yağmur sayısı ve azimutuyla **önerilen Hot**.

Küçük gökyüzü kubbesinde zenitten geçen bir **turuncu çizgi** her zaman **doğru anten yönlerini** verir; bu yönler seçili yağmurun (ya da en elverişli olanın) kaymasına diktir: radyant azimutu ±90°, iki ucunda *anten NNN°* etiketiyle, ±45°'lik tolerans ince çizgilerle. Kenardaki kısa turuncu çentikler diğer yararlı yağmurların dik yönlerini verir.

## Plan görünümü (sol)

Yukarıdan görülen bir Avrupa haritası (**D sağda**), çevresinde derece ölçeğiyle. Haritanın altındaki yazı yarıçapını verir (*Harita: kenar = istasyondan … km*).

| Öğe | Çizim |
|---|---|
| Yol / DX | İstasyonunuzdan karşı istasyona yeşil çizgi (her zaman lokatörler arasındaki gerçek büyük daire yolu) |
| **Hot A / Hot B** | Orta noktanın iki yanında, yola dik, AMS sapma tablosunun verdiği (ya da elle girilen) uzaklıktaki noktalar. **Kırmızı = önerilen**, **pembe = anten lobunun dışında**, **gri = lobun içinde** (uyarıyla) |
| Anten lobu | Anten azimutu çevresindeki −3 dB yatay lob (anten her zaman DX'e dönük), *lob …°* etiketiyle |
| Ortak bölge sınırları | Soluk *sın. A* / *sın. B* noktaları ve her istasyonun ufkunun E katmanıyla kesiştiği iki daire (bkz. [Geometri](Geometry-and-Path-Loss-tr#ortak-bölge-sınırları)) |
| Yağmur kayması | **Sarı çizgi**: seçili yağmurun (ya da en elverişlisinin) gökyüzünü taradığı yön, yani radyant azimutu |
| En iyi yönler | **Turuncu noktalar**: kaymaya dik iki yön (radyant azimutu ±90°, SM6FHZ) |
| **PREV bölgeleri** | Açık renkli elipsler: en olası izlerin **şu anda** düştüğü yer, yolun her tarafı için bir tane |

Etiketler üst üste binmez: Hot A ve PREV A yolun soluna, B sağına yazılır. **Açıklama**, haritanın sağında katlanabilir bir sütundur.

**Haritada fare:** **sol tık = karşı istasyon lokatörü**, **sağ tık = benim istasyonumun lokatörü**. Yol hemen yeniden hesaplanır.

Yağmur listesinin üstündeki seçenekler: **Hot A / Hot B yönleri**, **Avrupa haritası** (Natural Earth, ilk açılışta `data/mappa` içine indirilir), **Üstten görünüm (D sağda)**.

### Önerilen Hot

Gösterilen saat için program, ufkun üstündeki tüm yağmurlar üzerinden ZHR × verim ağırlığını toplar ve A tarafı (f_A oranı) ile B tarafı arasında böler. Ağırlığı büyük olan taraf önerilen Hot'u verir ve kırmızı çizilir:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Programın seçimi (kılavuz denk. 23).* Fikrin kaynağı: DJ5HG, DF5HC'nin aktarımıyla (DARC konferansı 2018) – radyantın konumuna göre iki noktadan biri, HOT-A ya da HOT-B, daha elverişlidir. O tarafa doğru 10–30° dönmek (side scatter) Cerrotta–Sartori makalesinden gelir.

### PREV bölgeleri

E katmanının her P noktası için tüm etkin yağmurların verime katkıları ([verimdeki](Efficiency-Calculation-tr#model) aynı aynasal koşul) ZHR ile ağırlıklandırılarak toplanır. Maksimumun en az %3'ünü taşıyan noktalar PREV bölgelerini oluşturur; her biri merkezi = noktaların ağırlıklı ortalaması ve eksenleri = dağılımlarının iki katı olan bir elips olarak çizilir.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Programın seçimi (kılavuz denk. 34).* Pratik kural budur: yağmur kuzeyden güneye tarıyorsa yararlı izler doğuya ve batıya düşer.

## Yağmur listesi (sağ üst)

| Sütun | Anlamı |
|---|---|
| Yağmur, Kod | Ad ve IMO kodu |
| ZHR şimdi | Bu andaki etkinlik (etkinlik profiliyle IMO tepe ZHR'si) |
| Azimut, Elev. | İstasyonunuzdan görülen radyant konumu |
| Verim % | Yağmurun bu yol için verimi |
| Taraf | A ya da B; yansımaların çoğunun geldiği taraf |
| En iyi yön | Radyant azimutu ±90° |
| Doğuş, Batış | Radyantın doğuşu ve batışı (UTC); uygun olduğunda *çevrekutupsal* ya da *hep altında* |

Yağmuru seçmek için bir satıra tıklayın: sarı kayma çizgisi ve turuncu noktalar onu izler.

## Küçük gökyüzü kubbesi (sağ orta)

İstasyonunuzdan görülen bir gökyüzü kubbesi üzerinde radyantlar, **IMO kodları** ve **camgöbeği renkli günlük rotaları** (UTC saatleri) ile. Seçmek için **bir radyanta tıklayın**. Renkler:

| Renk | Anlamı |
|---|---|
| Sarı | verim ≥ %50 ve ZHR ≥ 2 |
| Turuncu | verim ≥ %20 |
| Koyu kırmızı | verim < %20 |
| Gri | neredeyse etkin değil |

Yanında hesabın metni: yol uzunluğu ve azimutu, orta nokta ve elevasyonu, Hot A / Hot B azimutları ve sapmaları, önerilen Hot (*Şimdi önerilen …: az. …° (beklenen yansımaların %…'si)*), ortak bölge sınırları ve şu hatırlatma: *yağmur için en iyi yönlendirme: geliş yönüne DİK (radyant azimutu ±90°, tolerans ±40–50°, SM6FHZ)*.

## Kesit (sağ alt)

*KESİT – antenden karşı istasyona doğru görülen en olası izler.* Yatayda **karşı istasyona göre azimut** (← A sol, B → sağ), dikeyde **elevasyon**. Her yağmur için en güçlü 14 yansıma noktası alınır; her iz radyanta doğru yönelmiş bir doğru parçasıdır, iz yüksekliğinin 10 km üstünden 10 km altına kadar (her tarafta en çok 60 km), olasılığı yüksek olduğunda daha kalın. Ayrıca çizilenler: anten lobu (lob elevasyonu çevresinde −3 dB dairesi), karşı istasyon ve Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Programın seçimi (kılavuz denk. 35).*

## Uyarılar

| Uyarı | Ne zaman |
|---|---|
| **UYARI: Hot A (ve/veya Hot B) anten lobunun içinde …** | Hot spot anten azimutunun ±θ/2 içindedir (θ = yatay −3 dB lob): bu yönlendirmeyle zaten kapsanıyordur. Haritada gri gösterilir. Önerilen Hot kırmızı kalır. |
| **RADYANT ÇOK YÜKSEK (70° üstünde)** | Yararlı bir radyant istasyonunuzdan 70°'nin üstündedir: izler neredeyse dikey düşer ve yola doğru az yansıtır (DF5HC, DH9GCD). Aynı saatler [saatlik tabloda](Efficiency-Calculation-tr#saatlik-tablo) ↑ ile işaretlenir. |
| **YOL BOYUNCA ALÇAK RADYANT** | Etkin bir radyant 20°'nin altında ve yol doğrultusuna 30°'den yakın. Hesaplanan verim düşük (temkinli) kalır, ancak DJ5HG yolla aynı doğrultudaki sıyırma izlerinden seyrek ama güçlü yansımalar bekler (Hamburg–Narvik, Quadrantidler, yaklaşık 19 UTC): dinlemeye değer. |
| **YOL İZ UFKUNUN ÖTESİNDE** | İz yüksekliğinde yolun orta noktası her iki istasyonun da ufkunun altındadır (izler 90 km'deyken yaklaşık 2120 km). Uyarı, gereken en düşük iz yüksekliğini verir (2200 km için yaklaşık 96 km, 2300 km için 105 km): bağlantı yalnızca en yüksek izlerle mümkündür ve verimler ile kayıplar modelin sınırındadır. |
| *Ortak E katmanı bölgesi yok* | Yol, iz yüksekliğindeki menzilin iki katından uzundur: iki istasyon E katmanının ortak bir bölümünü görmez (tek atlama olanaksız). |
| *Önerilen Hot yok* | Bu saatte neredeyse hiç etkin yağmur yok. |

Gökyüzü kubbesi grafikleri için referans: DL1DBC'nin Swan Meteor Skyview'u (swan.ms); en iyi yönü gösteren kutupsal çizim: SM6FHZ'nin RadiantCalc'ı.
