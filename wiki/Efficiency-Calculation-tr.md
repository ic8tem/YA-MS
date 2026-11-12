[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · **Türkçe** · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · [Bahasa Indonesia](Efficiency-Calculation-id) · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Verim hesabı

*Sekme: Tahmin hesabı › Verim hesabı.*

[![Verim hesabı](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Bir yağmurun **verimi**, radyantının konumunun **sizin** yolunuzda yansımalara ne ölçüde izin verdiğini yüzde olarak söyler. Kavram Ilkka **OH5IY**'ye (MS-Soft) aittir ve Cerrotta–Sartori makalesinde ele alınmıştır: verim tepesi görsel tepeyle (ZHR) çakışmaz, çünkü radyantın iki istasyona göre nerede olduğuna bağlıdır. DL5MCG'nin MCG_MS programı aynı fikri dört sabit yöne uygular; YA-MS ise onu iki lokatör arasındaki **gerçek yol** için hesaplar.

Bu sekme, *Hesap tarihi (UTC)* alanında seçilen gün için verimi saat saat gösterir (değerler her saatin buçuğunda).

## Bir bakışta kartlar

| Kart | İçerik |
|---|---|
| **GÜNÜN EN İYİ SAATİ** | En yüksek yol endeksine sahip saat, endeks ve baskın taraf (%'siyle A/B) |
| **EN ELVERİŞLİ YAĞMUR** | Günün en büyük ZHR × verimine sahip yağmuru, verimi, saati ve tarafı ile **en iyi yön** (radyant azimutu +90° / −90°) |
| **ŞİMDİ** | Bu saatteki endeks ve baskın taraf ile önerilen Hot (yalnızca seçilen gün bugünse) |
| **DENEYSEL TAHMİN** | Tahmin frekansında şimdi, 1 saat sonra ve 2 saat sonra beklenen yansıma/saat (Collm, SM6FHZ kuralları; bkz. [Deneysel tahminler](Experimental-Forecasts-tr)) |

Kartların altındaki bir şerit A ve B harflerini açıklar (aşağıya bakın).

## Grafik

*… tarihinde … için saatlik verim (UTC, saat buçuktaki değerler).* En çok beş yağmur için: düz çizgiyle verim % ve aynı renkte noktalı çizgiyle DH9GCD formülü; sağ ölçekte mavi çubuklarla **yol endeksi**.

## Saatlik tablo

O gün etkin olan her yağmur için bir satır (ZHR'ye göre sıralı), saatler için 24 sütun (UTC):

| Hücre | Anlamı |
|---|---|
| `63A` | verim %63, yansımaların çoğu **A** tarafından |
| `41B` | verim %41, **B** tarafı |
| `3` | verim %5'in altında: taraf harfi olmadan sayı |
| boş | verim %1'in altında |
| `…↑` | radyant o saatte istasyonunuzdan **70°'nin üstünde** (çok yüksek) |
| sarı metin | verim ≥ %50 |

- **A** = istasyonunuzdan karşı istasyona bakarken **solda** (Hot A bölgesi); **B** = **sağda** (Hot B bölgesi). Anteni **o tarafa 10–30° çevirmek** yararlıdır (side scatter, Cerrotta–Sartori makalesi).
- **Açık mavi satırlar** (*DH9GCD %*, her yağmurun altında): karşılaştırma için DH9GCD formülü.
- **Σ satırı**: *Yol endeksi (ZHR×verim)*.
- **Turuncu satır** (*Tahmin … MHz (yans./saat)*): deneysel tahmin, mevcut olduğu saatler için (bugün ve yarının bir kısmı).

## Model

Tüm adımlar [hesap kılavuzunda](Efficiency-Explanation-tr) (`doc/YA-MS_manuale_calcoli.docx`, 5. bölüm) yer alır. Kısaca:

**1. Aynasal yansıma.** Bir iz sinyali A'dan B'ye ancak odakları A ve B olan bir elipsoide teğetse gönderir (McKinley 1961). Bir yağmurun izleri radyant yönü ŝ'ye paraleldir (makale; McKinley). E katmanının her P noktası için, istasyonlara doğru birim vektörlerle:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

DJ5HG'nin QTFGUI programı ve *"Die Geometrie von Meteorscatterverbindungen"* (2004) başlıklı metni de aynı yasaya dayanır: iz, ekseni kendisi olan bir koni üzerine saçılır ve onu yalnızca koni üzerindeki bir alıcı duyar. İdeal bir iz için koninin duvarı çok incedir (binlerce dalga boyu uzunluğunda bir ışıyıcı); program koşulu σ = 0,05 rad (yaklaşık 3°) Gauss toleransıyla kabul eder; bu tolerans ideal koninin görmediklerini temsil eder: yağmur radyantlarının dağılımı (GMN ölçümlerine göre 0,3–1,4°), rüzgârın büktüğü izler ve izlerin sonlu uzunluğu – *programın seçimi*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Her noktanın ağırlığı.** Underdense bir izin gücü (McKinley; ITU-R P.843, denk. 3), φ = saçılma açısının yarısı (85° ile sınırlı, *seçim*), β = iz ile A-P-B yayılma düzlemi arasındaki açı, p̂ = bu düzlemin birim normali:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**"İz ile yol arasındaki β açısı (tam McKinley)" seçeneği** (varsayılan olarak açık, temkinli ayar). Açık: yayılma düzlemini kesen izler, düzlemde yatanlardan 10–15 dB daha az değerlidir; böylece hiçbir iz olduğundan fazla değerlendirilmez. Kapalı: her iz düzlemde bulunuyormuş gibi ağırlıklandırılır (β = 0, cos²φ ile ağırlık), sürüm 1.6'ya kadar olduğu gibi. *Doğrulama:* 1000 km'lik bir yolda β olmadan en iyi radyant azimutu, radyantın elevasyonuna bağlı olarak yoldan 15°–90° uzaktadır (radyant 30°'deyken 30°, radyant 60°'deyken yola dik) ve dik radyant 30° elevasyonda %67 değerindedir; β ile en iyi radyant her zaman yol boyuncadır ve dik olan %15'e düşer. β ile SM6FHZ / DH9GCD'nin en iyi yön kuralı kaybolur; β bir seçenek olarak kalır, en temkinli değerleri verdiği için varsayılan olarak açıktır ve kapatılması kuralı geri getirir.

Bir noktaya ulaşan meteor sayısı, oradaki radyant elevasyonunun sinüsüyle (ŝ·û_P) orantılıdır; IMO'nun ZHR için kullandığı düzeltmenin aynısı.

**"Alçak radyantla daha uzun izler (DJ5HG)" seçeneği** (grafiğin üstündeki onay kutusu, varsayılan olarak kapalı, araç ipucuyla): DJ5HG, radyant alçakken km² başına daha az meteor düştüğünü, ancak izlerin daha uzun olduğunu (100 km'ye kadar yararlı) ve yansıma yasasını daha sık sağladığını belirtir. Seçenek açıkken ağırlık min(sin El, 15/100) olur: yararlı katman kalınlığı olan 15 km, elevasyonun sinüsüne bölünerek iz uzunluğunu verir; üst sınır 100 km'dir. Yaklaşık 9°'nin üstünde iki etki birbirini dengeler. Kapalıyken hesap temkinli kalır.

**Hesap ayarı** (aynı satır, radyo düğmeleri): **Temkinli** (varsayılan, en temkinli değerler: iz yüksekliği radardan, normal izler, β açık), **DJ5HG gibi** (102 km, daha uzun izler, β) ve **Özel**; sonuncusu yüksekliği, *radardan* kutusunu, daha uzun izler seçeneğini veya β'yı elle değiştirdiğinizde otomatik olarak seçilir.

**3. Toplam ve yüzde.** İz yüksekliğinde her 15 km'de bir, iki istasyonun da ufkun üzerinde gördüğü ve iki antenin dikey diyagramıyla ağırlıklandırılan noktalar (*anten diyagramı* kutusu, varsayılan olarak açık; kapalıyken yalnızca lob yükselmesinin üstündeki noktalar) (*seçim*). %100, o yol için radyantın en elverişli konumudur:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F her yol için bir kez, bir yönler ızgarası üzerinde (azimut her 5°, elevasyon her 2,5°) hesaplanır ve enterpole edilir.

**dB cinsinden verim (DJ5HG referansı).** Yüzde yalnızca o yol için radyantın en iyi konumuna görelidir. Farklı yolları karşılaştırmak için program verimi DJ5HG'nin sabit referansına göre dB cinsinden de verir: 0 dB, ekvatoru kesen 1000 km'lik kuzey–güney yolunda, ekinoksta radyant gök ekvatorundayken elde edilen en yüksek değerdir; aynı yükseklik ve aynı ağırlıklarla hesaplanır. DJ5HG kendi değerlerinin 6 dB'den daha iyi olduğunu belirtir.

**4. Taraf ve endeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Tablodaki harf, oranı büyük olan taraftır. *Programın seçimleri (kılavuz denk. 32–33).*

## DH9GCD karşılaştırması

En iyi yön için birincil kaynaklar Eshleman & Mlodnosky ve Meeks & James (Proc. IRE, 1957), Hines (1955) ve onun Forsyth, Hines & Vogan (1955) tarafından yapılan deneysel doğrulamasıdır: yalnızca saçılma açısının açıortayına dik olan gökyüzü yarım çemberindeki radyantlar yararlıdır, iz sayısı sin El ile artar ve orta noktanın yakınında yararlı izler radyantın karşı tarafında, yana doğru yaklaşık H·tan El uzağa düşer. DJ5HG bir çekince ekler: **alçak** bir radyant tam yol boyunca olduğunda McKinley'in formülü güçlü sinyaller verir (Hamburg–Narvik, Quadrantidler, yaklaşık 19 UTC); dolayısıyla "yolla aynı doğrultudaki radyant = neredeyse sıfır" yalnızca yüksek bir radyant için geçerlidir; program temkinli kalır ve *YOL BOYUNCA ALÇAK RADYANT* uyarısını gösterir.

Bağımsız bir denetim: **DH9GCD**'nin en iyi yön formülü, **DF5HC**'nin aktarımıyla (DARC konferansı, Ocak 2018) – yayımlanmış bir birincil kaynağı yoktur –; El ve Az istasyonunuzdan görülen radyant elevasyonu ve azimutu, P karşı istasyonun azimutu:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Radyant 45°'de ve yola yandan baktığında en büyüktür. DF5HC radyantı 20°'nin altında çok alçak, **70°'nin üstünde çok yüksek** sayar: bu saatler tabloda ↑ alır ve [Gökyüzü kubbesinde](Sky-View-tr#uyarılar) bir uyarı çıkar. Formül mesafeyi ve yükseklikleri hesaba katmaz, ama iyi bir referanstır.

## Doğrulamalar

| Doğrulama | Sonuç |
|---|---|
| SM6FHZ kuralı (VUSHF 2025): en iyi yol radyant azimutuna diktir, yön = radyant az ±90°, tolerans ±40–50° | Model tarafından yeniden üretilir; radyant yolla aynı hizada ve gökyüzünde yüksekse verim neredeyse sıfırdır |
| DJ5HG'nin QTFGUI'si, Hamburg JO53IM – Barselona, Kuadrantidler, 4 Ocak (kılavuzundaki örnek) | QTFGUI: 07:00 yön 252°, −8 dB; 08:00 yansıma bölgesi yok; 09:00 yön 168°, −4 dB. YA-MS (QTFGUI gibi 102 km yükseklik): 07:00 241°, −5,4 dB; 08:00 %0,6 (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: %26, %2, %32. Üç yöntem de, radyant neredeyse zenitteyken 08:00 boşluğunu görür |
| DJ5HG eğrileri (*Die Geometrie…*, Bild 8–9: Hamburg ve Münih'ten, Quadrantidler, 4 Ocak; grafikten okunmuş, yaklaşık ±0,5 dB ve ±15 dk) ile otomatik test `--prova-dj5hg` (saatte bir değer) karşılaştırması | Zamanlama: radyant zenite yakınken oluşan boşluk aynı saatlere düşer (Barselona 07:30–08:30'a karşı 07–09; Sofya 06:36–07:48'e karşı 07–08; Narvik 07–08:30'a karşı 07–09); Moskova her ikisinde de 03–10 arası kapalıdır, DJ5HG'nin yazdığı gibi Hamburg'dan yaklaşık 02:30'a, Münih'ten yaklaşık 00:30'a kadar açıktır. Yönler: 2–10° fark. 102 km'de seviyeler ve biçim (eğrilerden ortalama ve RMS fark): β yok, daha uzun izler yok −1,6 / 4,0 dB; daha uzun izler +1,1 / 4,6 dB; β −5,4 / 6,2 dB ama en iyi biçimle (ortalama çıkarıldıktan sonra 3,0 dB, 3,6'ya karşı): alçak radyantla derin minimumlar ortaya çıkar (Barselona 17'de −15,6 dB, 19:36'da −16 dB'ye karşı; Sofya 20'de −18,5 dB, −14 dB'ye karşı). β ve daha uzun izler (*DJ5HG gibi*) −2,2 / 4,7 dB; temkinli ayar (radar yüksekliği 89,5 km, β açık, daha uzun izler yok) −6,9 / 7,6 dB, biçim 3,3 dB. β olmadan YA-MS, radyant alçakken ve yolla neredeyse aynı doğrultudayken oluşan minimumu zar zor gösterir (−8,6 ve −10,4 dB): bu, DJ5HG'nin kendi çekincesidir, uyarı bu yüzden vardır |
| 15 km yerine her 5 km'de örnekleme | yüzdeler 0,3 puandan az değişir |

> MS-Soft 5.2 belgeleri OH5IY'nin verimini yalnızca underdense izler için göreli bir endeks olarak tanımlar; iki çarpanı vardır (radyant elevasyonu, en iyisi yaklaşık 45°, ve yolla açı, en iyisi 90°) ve overdense izler için elle %20'ye yükseltilmiş bir minimumu vardır; formül yayımlanmamıştır. MCG_MS bunu dört sabit yön için ve DX lokatörü verildiğinde gerçek yol için hesaplar. Model yalnızca underdense izleri, izotropik antenlerle dikkate alır; overdense patlamalar ve sporadik arka plan verimde yer almaz (sporadik arka plan radar akısıyla temsil edilir). 1.8.1'den beri «anten diyagramı» kutusu açıkken antenlerin dikey diyagramı uygulanır; azimutta antenler izotropik kalır.
