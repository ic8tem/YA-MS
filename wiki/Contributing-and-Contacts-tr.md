[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · **Türkçe** · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · [Bahasa Indonesia](Contributing-and-Contacts-id) · [Tagalog](Contributing-and-Contacts-tl) · [ไทย](Contributing-and-Contacts-th) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Katkıda bulunma ve iletişim

YA-MS, onu havada kullananların bildirimleriyle gelişir. Her düzeltme kaynağıyla birlikte anılır.

## İletişim

| | |
|---|---|
| Yazar | Costantino Cerrotta **IC8TEM** |
| E-posta | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Sorun bildirme

**GitHub'da bir issue** açın ya da şu bilgilerle bir e-posta yazın:

- işletim sistemi ve YA-MS sürümü (pencere başlığında);
- iki lokatör, bant ve UTC saati;
- ne beklediğiniz ve ne gördüğünüz (bir ekran görüntüsü yardımcı olur);
- radar sorunları için [Radar akısı](Radar-Flux-tr) sekmesinde gösterilen ileti.

## Özellikle yararlı olanlar

- **Havadan raporlar.** Verimin ya da tahminin doğru – ya da yanlış – çıktığı saatler ve yollar. Model deneyseldir; gerçek QSO'larla ve MCG_MS / MS-Soft ile karşılaştırılması gerekir.
- **RMOB karşılaştırmaları.** [RMOB karşılaştırması](Experimental-Forecasts-tr#rmob-karşılaştırması) ile bulduğunuz istasyon katsayısı K ve k üssü değerleri, bandınız ve istasyonunuzla birlikte.
- **Kaynaklı veriler.** Daha iyi radyant kaymaları, etkinlik profilleri, yeni IMO tepe tarihleri (`data/massimi_imo.csv`), anten verileri: kaynağı ekleyin, alıntılanacaktır.
- **Radar grafiklerindeki değişiklikler.** Collm grafiğinin biçimi değişirse görüntünün bir kopyası (`data/radar/`) okumanın yeniden kalibre edilmesine yardımcı olur.

## Çeviriler

Arayüz çevirileri **`data/lingue/<code>.txt`** içindeki düz metin dosyalarıdır (UTF-8) ve **herkes düzeltebilir**:

```
<Italian text><TAB><translation>
```

- Her satırda bir girdi; `#` ile başlayan satırlar yorumdur.
- İki sütunda da `\n` iki karakteri satır sonu demektir.
- `{0}`, `{1}`, … yer tutucularını biçimleriyle (örn. `{0:F1}`, `{3:+0;-0}`) koruyun; dilinizin gerektirdiği sırada kullanın.
- Eksik ya da boş girdiler İtalyanca gösterilir. Tüm anahtarların listesi `data/lingue/chiavi.txt` dosyasıdır (`tools/estrai_chiavi.py` ile üretilir, düzenlemeyin).

Dosyayı kurulumunuzun `data/lingue` klasöründe düzenleyin ve sonucu görmek için YA-MS'i yeniden başlatın (ya da dili değiştirin). Bu dosyalar **her güncellemede daha yeni sürümlerle değiştirildiği** için lütfen **düzeltmelerinizi** de – e-postayla ya da GitHub'da bir pull request olarak (`data/lingue/`) – **gönderin**; böylece bir sonraki sürüme girerler.

Bu wiki 36 dilde mevcuttur (English, Italiano, Deutsch, Nederlands, Français, Español, Português, Português (Brasil), Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Polski, Čeština, Magyar, Română, Ελληνικά, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, ไทย, 日本語, 한국어, 中文, 中文 (繁體)); wiki sayfalarına yönelik düzeltmeler de memnuniyetle karşılanır.
