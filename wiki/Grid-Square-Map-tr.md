**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

# Kare haritası

*Sekme: Kare haritası.*

[![Kare haritası](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Logunuzun ADIF dosyasından okunan, **çalıştığınız** ve **onaylanmış** Maidenhead kareleri (4 karakter), bir Avrupa haritası üzerinde – **her bant için bir alt sekme: 50, 70, 144, 222 ve 432 MHz**.

## Kontroller

| Kontrol | Ne yapar |
|---|---|
| **ADIF dosyası yükle...** | Bir `.adi` / `.adif` dosyası okur. Yeni bir ADIF önceki verilerin **yerini alır**. |
| **Belleği temizle** | ADIF'ten yüklenen tüm kareleri siler (onay ister). |
| Fare | **Tekerlek = yakınlaştırma, sürükleme = kaydırma, fare bir karenin üzerinde = QSO'lar** (tarihleriyle en çok altı çağrı işareti, onaylıysa *(onaylandı)*) |

Yüklemeden sonra durum satırı şunu gösterir: *… QSO okundu, 50-432 MHz bantlarında … QSO karesi, … QSO atıldı (diğer bantlar ya da karesiz)*. Her bant haritasının altında *… kare çalışıldı, … onaylandı* yazısı bulunur.

| Renk | Anlamı |
|---|---|
| Turuncu | çalışıldı |
| Yeşil | onaylandı (QSL ya da LoTW) |

## ADIF nasıl okunur

- Kullanılan alanlar: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (ADIF belirtimi).
- Bant `BAND` alanından ya da frekanstan: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Bir kare, içindeki en az bir QSO'da `QSL_RCVD = Y` ya da `LOTW_QSL_RCVD = Y` varsa **onaylanmıştır**.
- Kareler, başka bir dosya yükleyene ya da **Belleği temizle**'ye basana kadar `data/adif_quadrati.csv` içinde saklanır.

YA-MS LoTW'ye **bağlanmaz**: ADIF'i log programınızdan (ya da LoTW'den) dışa aktarın ve buraya yükleyin.
