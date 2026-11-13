[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · **Türkçe** · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Canlı trafik

*Sekme: Canlı ve gerçek zamanlı veriler › Canlı trafik.*

[![Canlı trafik](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ne gösterir

İstasyonunuzu merkez alan bir **azimutal eşuzaklık haritası** (merkeze uzaklık = gerçek mesafe, açı = azimut); üzerinde [Veri toplama](Data-Collection-tr) ile toplanan **tüm meteor scatter trafiği** bulunur. Program her bağlantı için şunları çizer:

- iki istasyon arasındaki **yol**, bandının renginde: 28 MHz kahverengi, 50 MHz yeşil, 70 MHz camgöbeği, 144 MHz turuncu, 222 MHz pembe, 432 MHz mor;
- yolun uçlarındaki iki **istasyon**;
- **bulut**: o yol ve o saat için en olası meteor izlerinin yoğunlaştığı yer.

İstasyonlarından biri **harita dışında** kalan spot'lar atılır. **Yeni gelmiş** (3 dakikadan eski olmayan) bir spot **bir dakika boyunca yanıp söner**, böylece yeni etkinlik ilk bakışta göze çarpar.

Kimin dinlediğini göster: bant renginde üçgenler, PSKReporter'a göre seçilen zaman aralığında 28, 50, 70, 144 ve 432 MHz'de MSK144, FSK441, PSK2K veya JTMS alan istasyonları gösterir. Bir üçgene tıklamak çağrı işaretini, lokatörü, modları ve son spotu gösterir. Veri toplama sekmesindeki MQTT akışı bağlı olmalıdır.

Haritada her spotun iki istasyonunun çağrı işareti yazılır, istasyon başına bir kez. İzdüşüm seçilebilir: azimutal (merkezde istasyonun) veya Mercator. Bulut sütunundaki ipucu anlamını açıklar.

Veri toplama'da seçilmemiş olanlar da dahil tüm bantların spotları gösterilir (bunlar kaydedilmez). CW spotları ve birbirine çok yakın istasyonlar arasındaki spotlar, Veri toplama'da atılıyorsa gösterilmez.

## Bulut nasıl hesaplanır

Program her spot için iki lokatör arasındaki yolu kurar (kendi yolunuzla aynı geometri, bkz. [Geometri ve yol kaybı](Geometry-and-Path-Loss-tr)) ve spot zamanında E katmanının noktaları üzerinde, ZHR ile ağırlıklandırılmış **her etkin yağmurun aynasal yansıma katkılarını** nokta nokta toplar – [gökyüzü kubbesindeki](Sky-View-tr) **PREV bölgeleriyle** aynı hesap. Toplamın en az %15'ini taşıyan her yol tarafı için bulut bir **elipstir**: merkezi noktaların ağırlıklı ortalamasında, yarı eksenleri dağılımlarının özdeğerlerinin kareköklerinin 1,5 katı, büyük ekseni ana özvektör boyunca. Hiçbir yağmur katkı vermiyorsa (yalnızca sporadik meteorlar) bulutlar kesikli çizilen iki klasik **hot spot**'tur. Denklemlerin tamamı hesap kılavuzunun 10. bölümündedir.

## Kontroller

| Kontrol | Anlamı |
|---|---|
| **Harita yarıçapı** | İstasyonunuzdan 600–3500 km. |
| **Gösterilecek spot'lar** | Son 15 ya da 30 dakika, son bir saat, son 3 saat, son 24 saat. |
| **Tablo** | Haritadaki bağlantılar, en yenisi başta, bant renginde; *Bulut* ana taraftaki yansıma payını ya da *sporadik* ibaresini verir. |
| **Tıklama** | Bir yola ya da tablo satırına: bağlantı vurgulanır ve kutu bulut merkezinin lokatörünü, payını, boyutunu ve eksenini gösterir. |
