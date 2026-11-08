**English** · [Русский](Efficiency-Calculation-ru) · [Deutsch](Efficiency-Calculation-de) · [日本語](Efficiency-Calculation-ja)

# Verim hesabı

*Sekme: Tahmin hesabı › Verim hesabı.*

[![Verim hesabı](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

Bir yağmurun **verimi**, radyantının konumunun **sizin** yolunuzda yansımalara ne ölçüde izin verdiğini yüzde olarak söyler. Kavram Ilkka **OH5IY**'ye (MS-Soft) aittir ve Cerrotta–Sartori makalesinde ele alınmıştır: verim tepesi görsel tepeyle (ZHR) çakışmaz, çünkü radyantın iki istasyona göre nerede olduğuna bağlıdır. DL5MCG'nin MCG_MS programı aynı fikri dört sabit yöne uygular; YA-MS ise onu iki lokatör arasındaki **gerçek yol** için hesaplar.

Bu sekme, *24 saatlik tablo için gün (UTC)* alanında seçilen gün için verimi saat saat gösterir (değerler her saatin buçuğunda).

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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

DJ5HG'nin QTFGUI programı da aynı yasaya dayanır (koni saçılması). Koşul σ = 0,05 rad (yaklaşık 3°) Gauss toleransıyla kabul edilir – *programın seçimi*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Her noktanın ağırlığı.** Underdense bir izin gücü (McKinley), φ = saçılma açısının yarısı (85° ile sınırlı, *seçim*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Bir noktaya ulaşan meteor sayısı, oradaki radyant elevasyonunun sinüsüyle (ŝ·û_P) orantılıdır; IMO'nun ZHR için kullandığı düzeltmenin aynısı.

**3. Toplam ve yüzde.** İz yüksekliğinde her 15 km'de bir nokta, yalnızca iki istasyonun da onları lob elevasyonunun üstünde gördüğü yerlerde (*seçim*). %100, o yol için radyantın en elverişli konumudur:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F her yol için bir kez, bir yönler ızgarası üzerinde (azimut her 5°, elevasyon her 2,5°) hesaplanır ve enterpole edilir.

**4. Taraf ve endeks.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Tablodaki harf, oranı büyük olan taraftır. *Programın seçimleri (kılavuz denk. 32–33).*

## DH9GCD karşılaştırması

Bağımsız bir denetim: **DH9GCD**'nin en iyi yön formülü, **DF5HC**'nin aktarımıyla (DARC konferansı, Ocak 2018); El ve Az istasyonunuzdan görülen radyant elevasyonu ve azimutu, P karşı istasyonun azimutu:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Radyant 45°'de ve yola yandan baktığında en büyüktür. DF5HC radyantı 20°'nin altında çok alçak, **70°'nin üstünde çok yüksek** sayar: bu saatler tabloda ↑ alır ve [Gökyüzü kubbesinde](Sky-View-tr#uyarılar) bir uyarı çıkar. Formül mesafeyi ve yükseklikleri hesaba katmaz, ama iyi bir referanstır.

## Doğrulamalar

| Doğrulama | Sonuç |
|---|---|
| SM6FHZ kuralı (VUSHF 2025): en iyi yol radyant azimutuna diktir, yön = radyant az ±90°, tolerans ±40–50° | Model tarafından yeniden üretilir; radyant yolla aynı hizada ve gökyüzünde yüksekse verim neredeyse sıfırdır |
| DJ5HG'nin QTFGUI'si, Hamburg JO53IM – Barselona, Kuadrantidler, 4 Ocak (kılavuzundaki örnek) | QTFGUI: 07:00 yön 252°, −8 dB; 08:00 yansıma bölgesi yok; 09:00 yön 168°, −4 dB. YA-MS (QTFGUI gibi 102 km yükseklik): 07:00 241°, −5,4 dB; 08:00 %0,6 (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: %26, %2, %32. Üç yöntem de, radyant neredeyse zenitteyken 08:00 boşluğunu görür |
| 15 km yerine her 5 km'de örnekleme | yüzdeler 0,3 puandan az değişir |

> OH5IY ve MCG_MS'nin kullandığı ölçek ayrıntılı olarak bilinmiyor (MS-Soft kılavuzlarına erişilemiyor): yüzdeleri eşdeğer saymadan önce bu programlarınkilerle karşılaştırın. Model yalnızca underdense izleri, izotropik antenlerle dikkate alır; overdense patlamalar ve sporadik arka plan verimde yer almaz (sporadik arka plan radar akısıyla temsil edilir).
