**English** · [Русский](Contributing-and-Contacts-ru) · [Deutsch](Contributing-and-Contacts-de) · [日本語](Contributing-and-Contacts-ja)

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

Bu wiki English, Русский, Deutsch ve 日本語 dillerinde mevcuttur; wiki sayfalarına yönelik düzeltmeler de memnuniyetle karşılanır.
