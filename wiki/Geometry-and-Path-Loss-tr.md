[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Português (Brasil)](Geometry-and-Path-Loss-pt-br) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Polski](Geometry-and-Path-Loss-pl) · [Čeština](Geometry-and-Path-Loss-cs) · [Magyar](Geometry-and-Path-Loss-hu) · [Română](Geometry-and-Path-Loss-ro) · [Ελληνικά](Geometry-and-Path-Loss-el) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · **Türkçe** · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · [ไทย](Geometry-and-Path-Loss-th) · [Bahasa Indonesia](Geometry-and-Path-Loss-id) · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh) · [中文 (繁體)](Geometry-and-Path-Loss-zh-tw)

# Geometri ve yol kaybı

*Sekme: Tahmin hesabı › Geometri ve yol kaybı.*

[![Geometri ve yol kaybı](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Yolun metin raporu (seçilebilir, böylece kopyalayabilirsiniz) ve sağda **Scatter point'e uzaklığa göre anten elevasyonu** grafiği. Köşeli parantez içindeki sayılar hesap kılavuzunun (`doc/YA-MS_manuale_calcoli.docx`) denklemlerine karşılık gelir.

## Bu sekmenin girdileri

| Alan | Varsayılan | Kullanım |
|---|---|---|
| **Güç W** | 400 | Bağlantı bütçesi için verici gücü |
| **Anten kazancı dBi (tx = rx)** | 14 | İki uçta aynı anten |
| **En düşük sinyal dBm** | −130 | Alınabilir en düşük sinyal (makale: 8 elemanlı Yagi + preamp) |
| **İz yoğunluğu q = 10^ … elektron/m** | 14 | Underdense izin doğrusal elektron yoğunluğu |

İstasyonlar, bant, iz yüksekliği, lob elevasyonu, boom ve hot spot mesafesi [kontrol sıralarından](Getting-Started-tr#1-üç-sıra-kontrol) gelir.

## Raporun bölümleri

| Bölüm | İçerik |
|---|---|
| **YOL GEOMETRİSİ (küresel Dünya, R = 6372,7955 km)** | Yükseklikleriyle istasyon ve DX; mesafe, azimut ve ters azimut; orta nokta (lokatör ve koordinatlar); iz yüksekliği (radardan alındığında *<- Collm radarının ölçtüğü mod*); orta noktaya doğru anten elevasyonu |
| **HOT A / HOT B (klasik hot spot'lar, anten yönlendirmesi için)** | Her biri için: lokatör, sizden azimut ve doğrudan yoldan sapma, DX'ten azimut, mesafe, elevasyon |
| **ORTAK BÖLGE SINIRLARI** | Lob elevasyonuyla iz yüksekliğindeki menzil; azimutlarıyla A sınırı / B sınırı |
| Anten | λ cinsinden boom, kazanç, yatay / dikey lob; Hot A ve Hot B'nin lobun içinde mi dışında mı olduğu |
| **YOL KAYBI (düşük yoğunluklu iz, McKinley 1961; anten kazançları hariç)** | 28, 50, 70, 144, 222 ve 432 MHz'de orta nokta (forward), Hot A ve Hot B için tablo |
| **… MHz'DE BAĞLANTI BÜTÇESİ (orta nokta)** | Güç ve EIRP, yol kaybı, antendeki sinyal, alınabilir en düşük sinyal, **pay**; OH5IY'nin ortalama kaybıyla aynı pay |
| **BANTLAR ARASI DENEYSEL KURALLAR (SM6FHZ, VUSHF 2025)** | 144 MHz'e göre sayı/şiddet ve süre; IARU en uzun pingi |

## Lokatör ve yol

Lokatör (4, 6 ya da 8 karakter; karenin merkezi, IARU Maidenhead sistemi) [14]. Mesafe, azimut ve orta nokta, yarıçapı **r = 6372,7955 km** olan bir küre üzerinde büyük daire formülleriyle (Cerrotta–Sartori makalesi) [15–16]. Zamana bağlı hesaplar **orta noktaya** göredir, çünkü en iyi saat iki uç arasında 1,5 saate kadar farklı olabilir (SM6FHZ).

## Anten elevasyonu

**Kaynak:** Cerrotta–Sartori makalesinin formülü (Şekil 7); x = d/r, d yansıma noktasına yer mesafesi, H iz yüksekliği ve h istasyon yüksekliği [17]:

```math
e = 90^\circ - 57{.}3\,\arctan\left[\frac{r\tan x + \left(H - \frac{r(1-\cos x)}{\cos x}\right)\sin x}{H - \frac{r(1-\cos x)}{\cos x} - h\sin x}\right]
```

**Doğrulama:** kesin küresel geometriyle 0,03° içinde örtüşür. Program iki argümanlı arktanjantı kullanır; bu, ufkun ötesinde negatif değerler verir ve makalede değinilen periyodiklik sorununu ortadan kaldırır. Orta noktaya doğru negatif elevasyon *yolun tek atlamanın geometrik menzilinin ötesinde* olduğu anlamına gelir.

## Ufuk menzili

Elevasyonu e olan bir ışının H yüksekliğine ulaştığı yer mesafesi (yukarıdaki formülün geometrik tersi) [18]:

```math
d_H = r\left[\frac{\pi}{2} - e - \arcsin\left(\frac{(r+h)\cos e}{r+H}\right)\right]
```

**Doğrulama:** H = 89,5 km, e = 0° → **1062 km**. Makalenin örneğinde (JN44BB–IO53RT) çizim ufuk kesişimlerini istasyonlardan yaklaşık 870 km'ye koyar; bu da yaklaşık 2° yükseltilmiş bir loba (865 km) karşılık gelir.

## Troposferik kırılma (GFS)

Troposferik kırılma ("Troposferik kırılma (GFS)" kutusu, başlangıçta kapalı). Kutu işaretliyken program Open-Meteo'dan iki istasyonun üzerindeki GFS modeli profilini indirir (yüzeyde ve 1000-500 hPa seviyelerinde basınç, sıcaklık ve nem; 6 saat içindeki en yakın saat için), seviyelerin yüksekliklerini hipsometrik denklemle (sanal sıcaklık), kırınım indisini de ITU-R P.453 Tavsiyesi formülüyle hesaplar:

```math
N = \frac{77{.}6}{T}\left(P + \frac{4810\,e}{T}\right)
```

burada P ve e (buhar basıncı, Magnus formülünden) hPa, T kelvin cinsindendir. En üst seviyenin üzerinde N, 7,35 km ölçek yüksekliğiyle üstel olarak azalır. GFS yanıt vermezse P.453 referans atmosferi N = 315·exp(−h/7,35) kullanılır ve rapor bunu belirtir.

Işın, küresel biçimdeki Snell yasasıyla (n·r·cos e sabit) ince küresel kabuklar boyunca iz yüksekliğine kadar izlenir; buradan H yüksekliğindeki menzil ve yükselme açısı düzeltmesi elde edilir:

```math
\Delta\varphi = \frac{k\,\Delta r}{r_m\,\bar u},\quad u = \sqrt{n^2r^2-k^2},\quad k = n_0 r_0\cos e
```

Referans atmosfer ve 89,5 km'deki izlerle örnek: 0°'de menzil 1061,5'ten yaklaşık 1133 km'ye çıkar (+72 km) ve nokta 0,62° daha yüksek görünür; 4°'de menzil 14 km artar ve düzeltme 0,20°'dir; 10°'nin üzerinde etki ihmal edilebilir. Düzeltme orta noktaya doğru yükselme açısına, ortak bölgenin yarıçapına, sıcak noktalara ve verimlilik haritasının noktalarına uygulanır; kırılmış ufkun altındaki noktalar atılır. Rapor bunu "Kırılma" satırında verir.

Eşdeğer Dünya yarıçapı k = 4/3, troposferin ilk kilometrelerinde kalan ışınlar için geçerlidir; orada N km başına yaklaşık 40 birim azalır. 90 km'deki bir ize giden ışın tüm troposferi geçer ve N'nin neredeyse sıfır olduğu 10-15 km'nin üzerinde neredeyse düz ilerler: tüm yükseliş boyunca k = 4/3 ile 0°'deki menzil yaklaşık 1230 km olurdu, izlenen ışından neredeyse 100 km fazla. Bu yüzden program k = 4/3 kullanmak yerine, yazarın LIVETROPOVHF programının troposferik yayılım için yaptığı gibi, ışını GFS profilinde izler.

→ [Open-Meteo (GFS)](https://open-meteo.com/) · [ITU-R P.453](https://www.itu.int/rec/R-REC-P.453)

## Ortak bölge sınırları

**Kaynak:** makale, her istasyonun ufkunun E katmanıyla buluştuğu eğrilerin kesişimlerini bulur: merkezleri A ve B'de olan, açısal yarıçapı ρ = d_H/r iki dairenin kesişimleri [19–20]:

```math
p_0 = \frac{\cos\rho}{1+\hat{u}_A\cdot\hat{u}_B}\,(\hat{u}_A+\hat{u}_B),\qquad p_{A,B} = p_0 \pm \sqrt{\frac{1-|p_0|^2}{|\hat{u}_A\times\hat{u}_B|^2}}\,(\hat{u}_A\times\hat{u}_B)
```

1 − |p0|² < 0 ise yol 2·d_H'den uzundur ve istasyonlar **ortak bir E katmanı bölgesi görmez**.

**Doğrulama:** bunlar iki istasyonun da gördüğü gökyüzünün **en uzak kenarlarıdır**, **nişan alınacak noktalar değildir**. JN70CN–IN78UO'da (1710 km, azimut 308°) istasyondan 1062 km'ye, doğrudan yolun 37° solu ve sağına düşerler; MSHV ise 10° önerir. Bu yüzden *A sınırı* / *B sınırı* olarak adlandırılır ve haritada soluk çizilirler.

## Hot A ve Hot B

**Kaynak:** sporadik meteorların yansımaları orta noktanın iki yanındaki iki bölgede ("hot spot'lar") yoğunlaşır. J. Richardson (AMS), DJ5HG'nin aktardığı tabloda (*Die Geometrie von Meteorscatterverbindungen*, 2004), doğrudan yöne göre anten sapmasını verir: **1000 km'de 13°, 1250 km'de 11°, 1500 ve 2000 km'de 10°**. W8WN'nin de benimsediği AMS Bulletin No. 203, 1500 ve 1800 km'de 10° verir.

**Seçim:** Hot A ve Hot B, orta nokta M'den s uzaklığında, yola dik noktalardır. *auto (AMS)* işaretliyken (varsayılan) s, Richardson tablosundaki sapmadan doğrusal enterpolasyonla elde edilir (1000 km'nin altında 13°, 2000 km'nin üstünde 10°): s = (D/2)·tan(sapma). İşaretli değilse s elle girilir, 30–400 km (MSHV 150 km kullanır); A, istasyonunuzdan DX'e bakarken solda, B sağdadır [21]. İstasyondan görülen sapma yaklaşık olarak [22]:

```math
\Delta Az_{hot} \approx \arctan\frac{s}{D/2}
```

**Doğrulama:** AMS tablosuyla 1000 km → 13°, s ≈ 115 km; 1250 km → 11°, s ≈ 121 km; 1500 km → 10°, s ≈ 132 km; 2000 km → 10°, s ≈ 176 km. JN70CN–IN78UO (1710 km) → 10°, s ≈ 151 km; bu, daha önce ve MSHV'de kullanılan 150 km ile aynıdır; kısa yollarda tablo hot spot'ları orta noktaya yaklaştırır.

## Underdense yol kaybı

**Kaynak:** underdense izler için McKinley denklemi ve ITU-R P.843 Tavsiyesi (sin α = 1), anten kazançları hariç; q = doğrusal elektron yoğunluğu, r_e = klasik elektron yarıçapı = 2,818·10⁻¹⁵ m, R1, R2 ize olan mesafeler, φ saçılma açısının yarısı, β iz ile yol düzlemi arasındaki açı, a₁ başlangıç yarıçapı çarpanı, r₀ m ve h km cinsinden (P.843, denk. 4 ve 7) [36]:

```math
L = 10\log_{10}\left[\frac{16\pi^2 R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}{\lambda^3 q^2 r_e^2}\right] - 10\log_{10} a_1\ \mathrm{dB},\qquad a_1 = \exp\left(-\frac{8\pi^2 r_0^2}{\lambda^2\sec^2\varphi}\right),\qquad \log_{10} r_0 = 0{.}035\,h - 3{.}45
```

**Seçim:** bağlantı bütçesi ve kayıp tablosu β = 90° kullanır (iz yol düzlemini keser, en elverişsiz durum: temkinli değer) ve bütçe en iyi durumu, β = 0'ı da gösterir. r₀, frekans için ortalama yankı yüksekliğinde alınır, h = 124 − 17 log f (P.843, denk. 15): 50 MHz için 95 km'de 0,76 m, 144 MHz için 87 km'de 0,40 m, 432 MHz için 79 km'de 0,21 m. 1000 km'de a₁, 50 MHz'de 0,2 dB, 144 MHz'de 0,6 dB ve 432 MHz'de 1,4 dB'dir (600 km'de 2,9 dB); DJ5HG'nin sabit 102 km'sinde 432 MHz'de yaklaşık 70 dB olurdu, yani hiç yankı olmazdı.

**Doğrulama:** 144 MHz'de q = 10¹⁴ elektron/m, 89,5 km'de izler ve β = 0 ile: 600 ile 2100 km arasında **182–192 dB** (1000 km'de 185 dB); bu, GM8JBJ'nin aktardığı gibi John Worsnop **G4BAO**'nun doktora tezinde hesapladığı **172–190 dB** aralığının içindedir. β = 90° ile kayıp 600 km'de 10 dB, 1000 km'de 13 dB ve 2100 km'de 16 dB artar; OH5IY'nin **ortalama 200 dB** değeri iki durumun arasındadır. GM8JBJ'nin tablosundaki 182 dB bir doğrulama değildir: tablo frekans vermez, bacak başına 86,4 dB'si 1 MHz'de 500 km'lik serbest uzay kaybıdır (20 log f terimi eksiktir: 144 MHz'de 129,6 dB) ve kalemlerinin toplamı 182 değil 163,8 dB'dir; sayfada ne "en az" ne de "144 MHz" yazar.

## Bağlantı bütçesi

```math
P_{rx} = P_{tx}(\mathrm{dBm}) + G_{tx} - L + G_{rx},\qquad M = P_{rx} - P_{min},\quad P_{min} = -130\ \mathrm{dBm}
```

[37–38]. Kazançlar dBi olarak girilir ve kullanılır: McKinley'nin kaybı izotropik antenlere göredir, bu nedenle 2,15 dB'lik dipol düzeltmesi çıkarılmaz (EIRP = güç + kazanç). Rapor ayrıca **OH5IY'nin ortalama yol kaybıyla** (144 MHz'de 200 dB, λ³ ile seçilen banda ölçeklenmiş) payı da verir. Makaledeki referans: yaklaşık **70 dBm EIRP** gerekir (−130 dBm + 200 dB, örn. 14 dBi'ye yaklaşık 400 W).

## Anten kazancı ve lobu

**VE7BQH** – Bir Yagi'nin kazancı, bom uzunluğu L'nin fonksiyonu olarak: VE7BQH tablolarının bant başına ortalama doğrusu (bant başına yaklaşık 60 Yagi, NEC kazançları). Parantez içinde örneklem aralığı ve standart sapma:

```math
\begin{aligned}50\,\mathrm{MHz}:\ & G = 7{.}36\,\log_{10}(L/\lambda) + 11{.}67\ \mathrm{dBi} \\ 144\,\mathrm{MHz}:\ & G = 8{.}27\,\log_{10}(L/\lambda) + 11{.}31\ \mathrm{dBi} \\ 432\,\mathrm{MHz}:\ & G = 8{.}68\,\log_{10}(L/\lambda) + 11{.}03\ \mathrm{dBi}\end{aligned}
```

(50 MHz: 0,3–5 λ, 0,25 dB · 144 MHz: 0,75–8,9 λ, 0,15 dB · 432 MHz: 1,8–16 λ, 0,17 dB)

En yakın bandın doğrusu kullanılır: 100 MHz altında 50 MHz'inki, 100 ile 300 MHz arasında 144 MHz'inki, 300 MHz üstünde 432 MHz'inki (1296 MHz için bu bir dış değerlemedir). Örneklem aralığının dışında ana pencere tahminin kaba olduğunu bildirir.

DL6WU'nun tarihî eğrisi (VHF Communications 3/1982, şekil 1): 1981'de 432 ve 1296 MHz'de yapılan ölçümler, bom oktavı başına 2,35 dB, bildirilen doğruluk 0,5 dB; G ≈ 9,2 + 7,81 log10(L/λ) dBd. W8IO bunu 7,773 log10(L/λ) + 11,43 dBi olarak verir (fark 0,1 dB'den az). Program karşılaştırma için bunu rapora yazar:

```math
G = 7{.}81\,\log_{10}(L/\lambda) + 11{.}35\ \mathrm{dBi}
```

**L.B. Cebik W4RNL'nin 432 MHz'deki NEC modelleriyle doğrulama** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Eleman | Boom (λ) | W4RNL NEC (dBi) | Formül (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Fark hiçbir zaman **0,1 dB**'yi aşmaz: kazanç tasarımdan çok boom uzunluğuna bağlıdır (VK3AUU Yagi'lerinin aynı eleman sayısı için boom'u daha kısadır). VK5DJ'nin Yagi Calculator'ı, formülleri yayımlanmamış VK3AUU, WA2PHW ve DJ9BV çeşitleri için de tahminler verir.

VE7BQH ortalaması eksi DL6WU eğrisi: 50 MHz'de 2–16 λ arasında 0,25 dB içinde; 144 MHz'de 1 λ'da −0,04 dB'den 10 λ'da +0,42 dB'e; 432 MHz'de 2 λ'da −0,06 dB'den 10 λ'da +0,55 dB'e. W4RNL'nin 432 MHz'de benzettiği DL6WU ve VK3AUU Yagilerinde VE7BQH ortalaması NEC'in 0,15–0,55 dB üstündedir: uzun bomlarda tabloların bilgisayarla eniyilenmiş Yagileri özgün tasarımlardan daha fazla verir.

**Lob – kaynak:** Kraus kuralı, dairesel lobla θE = θH = θK [40]:

```math
G_{lin} = \frac{41253}{\theta_E\,\theta_H}\quad\Rightarrow\quad \theta_K = \sqrt{\frac{41253}{10^{G/10}}}
```

**Doğrulama:** W4RNL'nin DL6WU Yagi'lerine ait NEC modelleri, Kraus'a göre **%5–10 daha dar bir yatay lob** verir: 12, 19 ve 26 eleman için 33,8° / 26,4° / 22,6°, karşılığında 37,3° / 28,0° / 23,9°. Basit formüller öndeki yan lobları hesaba katmaz (W4RNL, *Long-Boom Yagi Rules of Thumb*). Uzun boom'larda dikey lob yataydan biraz daha geniştir (14 λ: 18,4° / 18,8°).

**Seçim** [41]:

```math
\theta_{horizontal} = 0{.}93\,\theta_K,\qquad \theta_{vertical} = \theta_K
```

Örnek: 432 MHz'de 14 λ'lık Yagi → 20,3 dBi, yatayda 18,1° ve dikeyde 19,5° lob; W4RNL'nin modelleri 20,4 dBi ve 18,4° / 18,8° verir. Bunlar birkaç DL6WU anteninden türetilmiş yaklaşık kurallardır.

VE7BQH ortalamasıyla aynı 14 λ Yagi 21,0 dBi ve 16,9° yatay, 18,1° dikey lob verir; yukarıdaki 20,3 dBi DL6WU eğrisinden gelir. Lob düzeltmeleri (0,93 · θK ve θK) DL6WU Yagilerinden türetilenler olarak kalır.

Anten her zaman DX'e çevrilmiş kabul edilir. Bir hot spot, |Az(Hot) − Az(anten)| ≤ θ_horizontal/2 ise **lobun içindedir**: bu durumda [Gökyüzü kubbesinde](Sky-View-tr) içinde gri çizilir ve bir uyarı görünür. Dikey lob verim hesabına da girer: *anten diyagramı* kutusu açıkken yansıma noktaları iki antenin dikey kazancıyla ağırlıklandırılır (genişlik θ_vertical, en yüksek nokta lob yükselmesinde, zemin çarpanı ufukta sıfıra kadar).

## Bantlar arası deneysel kurallar

144 MHz'e göre: sayı/şiddet × (144/f)³ (dB olarak), süre × (144/f)² (SM6FHZ, VUSHF 2025). IARU 1. Bölge en uzun ping süresi: 50 MHz'de 1000 ms, 70 MHz'de 500 ms, 144 MHz'de 100 ms, 432 MHz'de 13 ms (VHF Handbook, makalede aktarıldığı gibi). Ayrıca bkz. [Deneysel tahminler](Experimental-Forecasts-tr).
