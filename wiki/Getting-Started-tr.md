**English** · [Русский](Getting-Started-ru) · [Deutsch](Getting-Started-de) · [日本語](Getting-Started-ja)

# İlk adımlar

İlk açılışta YA-MS örnek bir yol gösterir (144 MHz'de JN70CN → JO62QM). Programı istasyonunuza göre ayarlamak için beş dakika yeterlidir.

## 1. Üç sıra kontrol

Sekmelerin üstünde, tüm sekmeler için geçerli üç sıra kontrol vardır. Sağ üstteki **Kontroller** düğmesi bunları katlar ve açar (büyük yazı tiplerinde işe yarar); seçim hatırlanır.

**1. sıra – istasyonlar ve bant**

| Kontrol | Ne yapar |
|---|---|
| **Benim lokatörüm** / **yükseklik m** | Maidenhead lokatörünüz (4, 6 ya da 8 karakter; karenin merkezi kullanılır) ve istasyonun deniz seviyesinden yüksekliği. |
| **Karşı istasyon** / **yükseklik m** | Çalışmak istediğiniz istasyonun lokatörü ve yüksekliği. |
| **Bant MHz** | 28, 50, 70, 144, 222 ya da 432 MHz: anten kazancı ve lobu, akı tahmini ve bağlantı bütçesi için kullanılır. |
| **Hesapla** | Yolu yeniden hesaplar (E katmanının örneklenmesi: birkaç saniye). |
| **Anten az** | Anteninizin azimutu: her zaman **DX'e doğru** (yolun azimutu). |
| **Yazı tipi** | Tüm metnin boyutu, %100–300. Bkz. [Ayarlar](Settings-and-Data-Folder-tr#yazı-tipi-ve-kontroller). |

**2. sıra – E katmanı ve anten**

| Kontrol | Ne yapar |
|---|---|
| **İz yüksekliği km** + **radardan** | Meteor izlerinin yüksekliği (varsayılan 90 km). *radardan* işaretliyse Collm radarının ölçtüğü en sık yükseklik (mod) kullanılır; bkz. [Radar akısı](Radar-Flux-tr). |
| **Lob elevasyonu °** | Anten lobunuzun en düşük elevasyonu (0° = ufuk). Yalnızca iki istasyonun da bu elevasyonun üstünde gördüğü E katmanı noktaları kullanılır. |
| **Yagi anten: boom m** | Yagi'nizin boom uzunluğu. Program uzunluğu λ cinsinden, kazancı (DL6WU eğrisi) ve yatay ile dikey −3 dB lobu gösterir; bkz. [Geometri ve yol kaybı](Geometry-and-Path-Loss-tr#anten-kazancı-ve-lobu). 2 λ'nın altında tahmin kabadır. |
| **Orta noktadan hot spot km** | Hot A ve Hot B'nin orta noktaya uzaklığı, 30–400 km (varsayılan 150 km; AMS Bulletin 203 / W8WN / MSHV'deki gibi). |

**3. sıra – saat**

| Kontrol | Ne yapar |
|---|---|
| **Saat** | UTC saati. |
| **Gökyüzü kubbesi saati (±36 sa)** | [Gökyüzü kubbesini](Sky-View-tr) ve [GRAVES radarı](GRAVES-Radar-tr) sekmesini 15 dakikalık adımlarla 36 saate kadar geri ya da ileri götürür. |
| **Gerçek zaman** | Şimdiye döner. |
| **24 saatlik tablo için gün (UTC)** | [Verim hesabı](Efficiency-Calculation-tr) sekmesinde ve GRAVES zaman çizelgesinde gösterilen gün. |

## 2. İstasyonunuz ve DX

1. **Benim lokatörüm** ve **yükseklik m** alanlarını doldurun.
2. **Karşı istasyon** lokatörünü ve yüksekliğini yazın – ya da [Gökyüzü kubbesindeki](Sky-View-tr) haritaya tıklayın: **sol tık = karşı istasyon lokatörü**, **sağ tık = benim istasyonumun lokatörü**.
3. **Bant MHz** değerini seçin ve **Hesapla**'ya basın.

Alttaki durum çubuğu şunu doğrular: *Yol hesaplandı: … km, … s içinde … yansıma noktası örneklendi*.

## 3. Anteniniz

Yagi'nizin **boom uzunluğunu** girin. Program kazancı ve lobu türetir ve anten DX'e dönükken Hot A ya da Hot B zaten **lobun içine** düşüyorsa sizi uyarır (o zaman gri çizilirler: anteni çevirmeye gerek yoktur).

## 4. Sonuçları okuyun

| Soru | Nereye bakmalı |
|---|---|
| Şu anda yoluma hangi yağmur yardım ediyor ve hangi taraftan? | [Gökyüzü kubbesi](Sky-View-tr): yağmur listesi, kırmızıyla önerilen Hot, PREV bölgeleri |
| Bugünün en iyi saati hangisi? | [Verim hesabı](Efficiency-Calculation-tr): bir bakışta kartlar ve saatlik tablo |
| Radar kaç meteor sayıyor? | [Radar akısı](Radar-Flux-tr) |
| 144 MHz'de kaç ping bekleyebilirim? | [Deneysel tahminler](Experimental-Forecasts-tr) (deneysel) |
| İstasyonum bu yolu kapatabilir mi? | [Geometri ve yol kaybı](Geometry-and-Path-Loss-tr): yol kaybı ve pay |
| Sonraki tepe ne zaman? | [Yağmurlar](Showers-tr) |
| GRAVES ile deneme yapabilir miyim? | [GRAVES radarı](GRAVES-Radar-tr) |

## Pratik kurallar (kaynaklardan)

- **Yağmura dik yönlendirin**: en iyi yol radyant azimutuna diktir; en iyi yön = radyant azimutu ±90°, tolerans ±40–50° (SM6FHZ).
- **Side scatter**: anteni, yansımaların çoğunun geldiği tarafa (A ya da B) doğru 10–30° çevirin (Cerrotta–Sartori makalesi).
- **Çok yüksek** (70°'nin üstünde) ya da çok alçak (20°'nin altında) **radyant** az sayıda yararlı iz verir (DF5HC, DH9GCD).
- Sporadik meteorlar **06 UTC** civarında tepe yapar (makale; Collm akısıyla doğrulanmıştır).
- 432 MHz'de yararlı mesafeler: 800–2000 km, en iyisi yaklaşık 1400 km (SM6FHZ); genel olarak en iyi mesafe 1300–1500 km (DF5HC).

Sonraki: [Gökyüzü kubbesi](Sky-View-tr).
