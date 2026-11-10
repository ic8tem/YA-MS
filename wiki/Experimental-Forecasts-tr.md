[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · **Türkçe** · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [Bahasa Indonesia](Experimental-Forecasts-id) · [Tagalog](Experimental-Forecasts-tl) · [ไทย](Experimental-Forecasts-th) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Deneysel tahminler

*Sekme: Tahmin hesabı › Deneysel tahminler.*

[![Deneysel tahminler](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Bu sekme **Collm radarının (36,2 MHz)** meteor sayımlarını **bir amatör bantta saatlik yansıma** tahminine dönüştürür (varsayılan 144 MHz, 28 ile 1300 MHz arasında herhangi bir frekans), yolunuz için **sonraki 24 saati** tahmin eder ve tahmini bir **RMOB** gözlemcisiyle – örneğin 143,050 MHz'de GRAVES'i dinleyen biriyle – **karşılaştırmanıza** olanak verir.

> Buradaki her şey **deneyseldir**: frekans kuralı ampirik bir kuraldır ve istasyon katsayısı istasyonunuza bağlıdır. Rakamları saatleri ve günleri karşılaştırmak için kullanın ve havada doğrulayın.

## Kontroller

| Kontrol | Varsayılan | Ne yapar |
|---|---|---|
| **Hedef frekans MHz** | 144 | Tahminin frekansı (28–1300 MHz) |
| **λ^k üssü** | 3 | Frekans kuralının k üssü (SM6FHZ: 3) |
| **İstasyon katsayısı K** | 1 | Alıcı istasyonu (güç, antenler) hesaba katar; aynı banttaki bir RMOB gözlemcisiyle karşılaştırılarak bulunur |
| **Diskten RMOB dosyası yükle...** | | Aylık bir RMOB metin dosyasını okur (aşağıya bakın) |
| **Üssü RMOB dosyasından çıkar** | | k'yı Collm ile RMOB'un ortak saatlerinden uydurur |
| **RMOB gözlemcisi** | boş | Gözlemcinin dosya adında göründüğü şekliyle adı (örn. `NAME_112026rmob.TXT` → `NAME`) |
| **RMOB'u şimdi indir** | | O gözlemcinin geçerli ay dosyasını bir kez indirir |
| **5 dakikada bir otomatik indirme (yalnızca RMOB'un izniyle etkinleştirin)** | **kapalı** | Bkz. [RMOB ve otomatik programlar](#rmob-ve-otomatik-programlar) |

Kontrollerin altındaki turuncu satır kuralı güncel rakamlarla gösterir, örn. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*; ayrıca süre ölçeklemesini ve o frekanstaki IARU en uzun pingini verir.

## Radardan amatör banda

```
N(f) = N(36.2 MHz) · (36.2 / f)^k · K        k = 3
τ(f) = τ(36.2 MHz) · (36.2 / f)²
```

**Kaynak:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, 45. Nordic VUSHF, Mayıs 2025 – yansımaların sayısı ve şiddeti **λ³** ile, süresi **λ²** ile ölçeklenir (432 MHz, 144 MHz'in 14–15 dB altındadır ve 1/9 kadar sürer). **Doğrulama:** λ³ bağımlılığı McKinley'in underdense denklemindekiyle aynıdır. k = 3 ile Collm'daki 1000 meteor/saat, **144 MHz'de yaklaşık 16 yansıma/saat** olur; 143,050 MHz'de GRAVES'i dinleyen RMOB gözlemcileri genellikle **saatte 20 ile 140 yankı** sayar (RMOB bülteni, Haziran 2018): büyüklük mertebesi uyumludur ve aradaki fark istasyon katsayısı K'dır. (Kılavuz denk. 44–45.)

## Sonraki 24 saat

```
N_forecast(t) = N(f, t − 24 h) · (I(t) + 10) / (I(t − 24 h) + 10)
```

**Kalıcılık:** bir önceki günün (yoksa iki gün öncesinin) aynı saatinin ölçeklenmiş değeri, **yol yağmur endeksi** I'nın değişimiyle düzeltilir (Σ ZHR × verim, bkz. [Verim hesabı](Efficiency-Calculation-tr#model)). 10 sabiti sporadik arka planı temsil eder ve endeks küçükken düzeltmeyi sınırlar. *Programın seçimi (kılavuz denk. 47).*

| Panel | İçerik |
|---|---|
| **Collm'da ölçülüp f MHz'e ölçeklendi – dün ve bugün (UTC)** | Collm radarının meteor/saat değerleri; ölçeklenmiş değerler (turuncu, sağ ölçek); yüklendiyse RMOB sayımları (yeşil, sağ ölçek) |
| **… için f MHz'de sonraki 24 saatin deneysel tahmini** | Tahmin edilen yansıma/saat (çubuklar) ve yol yağmur endeksi (sağ ölçek) |
| Tablo | UTC saati · Collm aynı saat · Ölçeklenmiş · Yol yağmur endeksi · Tahmin /saat · **Değerlendirme** |

**Değerlendirme:** tahmin 24 saatlik ortalamanın en az 1,3 katıysa *iyi*, 0,8 katından itibaren *orta*, altında *zayıf*. Aynı tahmin **DENEYSEL TAHMİN** kartında ve [Verim hesabı](Efficiency-Calculation-tr) sekmesinin turuncu satırında görünür; [GRAVES radarı](GRAVES-Radar-tr#beklenen-yankılar-deneysel) sekmesindeki beklenen yankıların da temelidir.

## RMOB karşılaştırması

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) radyo gözlemcilerinin saatlik meteor sayımlarını toplar; İtalya'da pek çoğu 143,050 MHz'de GRAVES'i dinler (Venedik Planetaryumu, Faenza, Rovereto ve diğerleri).

**RMOB dosyalarının okunması.** İki metin biçimi kabul edilir:

| Biçim | Görünüm | Notlar |
|---|---|---|
| Aylık dosya (Colorgramme / Spectrum Lab) | her gün için bir satır, 24 saatlik değerle `day| n| n| …` | alışılmış `NAME_MMYYYYrmob.TXT` |
| Bülten tablosu | başlık ` UT |  1   2   3 …`, satırlar `0h|175 166 …` | dosyada birden çok gözlemci varsa art arda okunur: tek gözlemcili bir dosya kullanın |

Ay ve yıl dosya adından (`…_MMYYYYrmob…`) ya da başlıktan alınır; aksi halde geçerli ay kullanılır (ve program bunu belirtir).

**Üssün uydurulması.** K = 1 ile, ortak saatlerdeki (en az 3) RMOB/Collm oranlarının medyanından:

```
k_emp = − ln( median(N_RMOB / N_Collm) ) / ln( f / 36.2 )
```

*Programın seçimi (kılavuz denk. 46).* İletişim kutusu ortak saatleri, medyan oranı ve k'yı gösterir; **Evet** k'yı uygular (ve K = 1 yapar), **Hayır** k = 3'ü korur – o zaman K'yı aynı iletişim kutusunda önerilen değere elle ayarlayın.

## RMOB ve otomatik programlar

RMOB, **otomatik programların dosyalarını çekmemesini** ister. Bu nedenle **otomatik indirme** başlangıçta **kapalıdır** ve **yalnızca RMOB'dan izin istedikten sonra** etkinleştirilmelidir. İzin olmadan da gerektiğinde her zaman **Diskten RMOB dosyası yükle...** seçeneğini kullanabilir ya da **RMOB'u şimdi indir** düğmesine basabilirsiniz.

İndirme adresi `config.ini` içinde bir şablondur (anahtar `rmob_url`, varsayılan `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`; burada `{NOME}` gözlemci, `{MMAAAA}` ay ve yıldır); indirilen dosyalar `data/radar/` içinde saklanır.
