[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · **Türkçe** · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · [Bahasa Indonesia](Getting-Started-id) · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

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
| **Orta noktadan hot spot km** + **auto (AMS)** | Hot A ve Hot B'nin orta noktaya uzaklığı. *auto (AMS)* işaretliyken (varsayılan) DJ5HG'nin aktardığı J. Richardson (AMS) anten sapma tablosunu izler: 1000 km'de 13°, 1250 km'de 11°, 1500 ve 2000 km'de 10° (orta noktadan yaklaşık 115, 121, 132 ve 176 km). 30–400 km'yi elle girmek için işareti kaldırın (MSHV 150 km kullanır). |

**3. sıra – saat**

| Kontrol | Ne yapar |
|---|---|
| **Saat** | UTC saati. |
| **Hesap tarihi (UTC)** | [Tahmin hesabı](Sky-View-tr) ve [GRAVES radarı](GRAVES-Radar-tr) için hesap günü (varsayılan bugün), günün şu anki saatinde. |
| **Saatler (−12 ile +36 sa arası)** | Hesap anını 15 dakikalık adımlarla o saatin 12 saat öncesinden 36 saat sonrasına kadar kaydırır. Yanında: *Hesap zamanı: şimdi* ya da *Hesap zamanı: dd/mm hh:mm UTC*. |
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
