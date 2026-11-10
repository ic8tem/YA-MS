[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-BR) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Ελληνικά](Showers-el) · [Русский](Showers-ru) · [Українська](Showers-uk) · **Türkçe** · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · [ไทย](Showers-th) · [Bahasa Indonesia](Showers-id) · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh) · [中文 (繁體)](Showers-zh-TW)

# Yağmurlar

*Sekme: Yağmurlar.*

[![Yağmurlar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Tüm hesapların kullandığı yağmur kataloğu: **IMO Meteor Shower Calendar 2026 ve 2027**'den (tablo 5 ve 7) **45 yağmur** artı **Antihelion Kaynağı** (tablo 6), her biri **sonraki tepesiyle** birlikte.

## Sütunlar

| Sütun | Anlamı |
|---|---|
| Kod | IMO kodu (QUA, PER, GEM, …) |
| Yağmur | Ad |
| Etkinlik | Etkinlik dönemi (gün/ay – gün/ay) |
| λ max | Tepenin güneş boylamı (J2000), IMO'dan |
| **Sonraki tepe (UTC)** | Sonraki tepenin tarihi ve saati (aşağıya bakın) |
| **Tepe kaynağı** | *IMO 2026* / *IMO 2027* = IMO'nun yayımladığı tarih ve saat; *IMO 2026 (gün)* = IMO yalnızca günü verir, gösterilen saat hesaplanmıştır (*~hh:mm hes.*); *λ'dan hesaplandı* = o yıl için IMO değeri yok |
| S.A., Dek. | Tepedeki radyant (Antihelion Kaynağı için *hareketli*) |
| v km/s, r | Yer merkezli hız ve nüfus indeksi |
| ZHR | Tepe ZHR'si (*değ.* = değişken) |
| Tür | *görsel* ya da *radyo, gündüz* |

**Bugün (UTC) etkin olan** yağmurlar sarı bir örtü ve kalın yazıyla vurgulanır.

## Sonraki tepe

Program her zaman **sonraki** tepeyi gösterir. IMO o yılın takvimini yayımlamışsa `data/massimi_imo.csv` dosyasındaki **IMO tarih ve saatini** kullanır (2026 ve 2027 dahildir); aksi halde Güneş'in tepenin güneş boylamına ulaştığı anı hesaplar (Meeus, *Astronomical Algorithms*, bölüm 25, Newton yöntemiyle çözülerek).

**Doğrulama:** IMO'nun saati verdiği durumlarda hesap, IMO 2026 ve 2027 takvimleriyle birkaç dakika içinde uyuşur (örn. Kuadrantidler 3/1/2026 21:13, karşılığı 21:00; Geminidler 14/12/2027 19:51, karşılığı 20:00). İstisnalar: Gündüz kappa Leonidleri 2026 bir gün sonra (25/9 yerine 26/9) ve eta Akuaridler 2027'nin saati (15:10, IMO'da 09:00) – bu durumlarda IMO değeri kullanılır.

**Yıl ekleme:** IMO yeni bir takvim yayımladığında satırlarını `data/massimi_imo.csv` dosyasına ekleyin (`year;code;MM-DD;hh:mm`; IMO yalnızca günü veriyorsa saat boş). O zamana kadar tepe hesaplanır.

## Küçük ve gündüz yağmurları

Katalog, IMO listesinin **küçük yağmurlarını** içerir – örneğin Ekim Camelopardalidleri (OCT, ZHR 5, 5–6 Ekim'de etkin), Andromedidler, gamma Ursae Minoridler – ve Nisan–Ekim arasındaki **gündüz radyo yağmurlarını** (Gündüz Nisan Piscidleri, Gündüz Arietidleri, Gündüz zeta Perseidleri, Gündüz beta Tauridleri, Gündüz kappa Leonidleri, Gündüz Sextantidleri, …). ZHR'leri küçük olsa bile [yol endeksine](Efficiency-Calculation-tr#model) ve [önerilen Hot'a](Sky-View-tr#önerilen-hot) katkı verirler. Gündüz radyo yağmurları için IMO ZHR vermez: verilmediği yerde program 5 çalışma değerini kullanır.

## Etkinlik profili ve radyant kayması

```math
ZHR(\lambda_\odot) = ZHR_{max}\,10^{-B_\pm |\lambda_\odot - \lambda_{max}|},\qquad \alpha = \alpha_0 + \frac{d\alpha}{d\lambda}\Delta\lambda,\quad \delta = \delta_0 + \frac{d\delta}{d\lambda}\Delta\lambda,\quad \Delta\lambda = \lambda_\odot - \lambda_{max}
```

ZHR_max, α0, δ0 ve λ_max IMO takviminden; eğimler B (tepeden önce ve sonra farklı) ile günlük kaymalar dα/dλ, dδ/dλ ise `data/sciami.csv` dosyasına yazılmış **çalışma değerleridir** (IMO kayma tablosu henüz girilmedi). *Kılavuz denk. 9 ve 13.* Antihelion Kaynağının konumu IMO tablo 6'nın tarihleri arasında doğrusal olarak enterpole edilir (`data/ant_radiante.csv`; 10 Aralık – 20 Eylül arası etkin, ZHR yaklaşık 4).

## Kataloğun düzenlenmesi

`data/sciami.csv`, düzenleyebileceğiniz düz bir metin dosyasıdır (ayırıcı `;`): kod, ad, başlangıç ve bitiş (MM-DD), λ max, S.A., Dek., kaymalar, v, r, ZHR, önce/sonra B, tür (V görsel, R gündüz radyo). Bir satır hatalıysa program açılışta bir ileti gösterir ve o satırı yok sayar.

Kaynaklar: International Meteor Organization – Meteor Shower Calendar 2026 ve 2027, [www.imo.net](https://www.imo.net) (tablo 5, 6 ve 7); Rossano IZ5TEK (scattertek).
