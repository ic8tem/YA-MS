**English** · [Русский](Home-ru) · [Deutsch](Home-de) · [日本語](Home-ja)

# YA-MS – meteor scatter tahminleri ve yağmurların canlı verimi

*hazırlayan: Costantino Cerrotta IC8TEM*

**YA-MS**, **50, 70, 144, 222 ve 432 MHz'de meteor scatter (MS)** çalışan radyo amatörleri için ücretsiz bir programdır. Sizin lokatörünüz ile karşı istasyonun lokatörü arasındaki gerçek yol için saat saat şunları hesaplar: her etkin meteor yağmurunun yola ne kadar yardım ettiği (**verimi**), yansımaların yolun hangi tarafından geldiği (**Hot A / Hot B**), antenin nereye çevrileceği ve bir **canlı meteor radarından** (Collm, Almanya) türetilen, saatlik yansıma sayısına ilişkin deneysel bir tahmin. **Windows, Linux ve macOS** üzerinde (.NET 8 + Avalonia), 6 arayüz dilinde çalışır.

Ana kaynak, **C. Cerrotta IC8TEM ve G. Sartori IV3GTH**'nin *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (sürüm 7) başlıklı makalesidir. Programdaki her formül ve her veri kaynağını belirtir; bkz. [Kaynaklar](Sources-tr).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Gökyüzü kubbesi"></a><br><sub>Gökyüzü kubbesi</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Verim hesabı"></a><br><sub>Verim hesabı</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="GRAVES radarı"></a><br><sub>GRAVES radarı</sub></td>
</tr></table>

## Kimin için

- Bir meteor scatter yolunun **ne zaman** açık olduğunu ve antenin **nereye** çevrileceğini, genel geçer "yağmur bu gece tepe yapıyor" bilgisinin ötesinde öğrenmek isteyen operatörler.
- **144 ve 432 MHz'de uzun yollar** çalışan istasyonlar; burada bir yağmurun yararlı mı yararsız mı olduğuna radyantın konumu karar verir.
- **Rakamları denetlemek** isteyen herkes: hesap kılavuzu ve program içindeki açıklama her adımı kökeniyle birlikte verir: yayımlanmış bir kaynak, program üzerinde yapılmış bir doğrulama ya da programın bir seçimi.

## Sekmeler

Sürüm 1.6'dan beri ana sekmelerin **alt sekmeleri** vardır (ana sıranın altında daha açık renkli bir sıra). Açılışta 5 saniyelik bir karşılama ekranı ESO'nun VLT teleskobu üzerindeki Perseidleri gösterir (fotoğraf ESO/S. Guisard, CC BY 4.0).

| Sekme | Alt sekme | Ne gösterir |
|---|---|---|
| **Canlı ve gerçek zamanlı veriler** | [Canlı trafik](Live-Traffic-tr) | Toplanan tüm MS trafiğinin azimutal haritası; her bağlantı için en olası izlerden oluşan bir bulut, bant renkleri, yanıp sönen yeni spot'lar |
| | [Radar akısı](Radar-Flux-tr) | Collm SKiYMET radarından okunan saatlik meteor sayıları ve iz yükseklikleri, Sodankylä görüntüsü, sizin bandınız için tahmin |
| | [GRAVES radarı](GRAVES-Radar-tr) | GRAVES → siz forward scatter yolu: huzmedeki yararlı bölge, sektör ve adım, huzmenin sonraki geçişi, nasıl dinlenir |
| | [Veri toplama](Data-Collection-tr) | Üç telnet cluster akışı (DX cluster, RBN, DM4X/PSKReporter) ve MS spot filtresi |
| **Tahmin hesabı** | [Tahmin hesabı](Sky-View-tr) | Hot A / Hot B, anten lobu, PREV bölgeleri ve yağmur kayması ile yolun plan haritası; yağmur listesi; radyantlar ve doğru anten yönleriyle küçük gökyüzü kubbesi; antenden görülen kesit |
| | [Geometri ve yol kaybı](Geometry-and-Path-Loss-tr) | Mesafe, orta nokta, elevasyon, Hot A / Hot B, ortak bölge sınırları, 28–432 MHz yol kaybı, bağlantı bütçesi, anten |
| | [Verim hesabı](Efficiency-Calculation-tr) | Bir bakışta kartlar, her yağmurun A/B taraflı saatlik verimi, yol endeksi, DH9GCD karşılaştırması, grafik |
| | [Deneysel tahminler](Experimental-Forecasts-tr) | λ^k ve istasyon katsayısı K ile 144 MHz'e (ya da herhangi bir frekansa) ölçeklenmiş Collm akısı, 24 saatlik tahmin, RMOB karşılaştırması |
| **Teknik belgeler** | [Kaynaklar](Sources-tr) | Tüm kaynaklar; ana kaynak Cerrotta–Sartori makalesidir |
| | [Avrupa radarları haritası](European-Radar-Map-tr) | Collm, Sodankylä, GRAVES ve CMOR'un istasyonunuza göre konumu |
| | [Verim - açıklama](Efficiency-Explanation-tr) | Verimin nasıl hesaplandığını adım adım anlatan, Word'e aktarılabilen belge |
| [Canlı yağmurlar](Live-Showers-tr) | – | Global Meteor Network'ün ölçtüğü ZHR ve CMOR radyant haritaları |
| [Yağmurlar](Showers-tr) | – | Sonraki tepeyle birlikte IMO kataloğu (IMO tarih ve saati ya da hesaplanmış) |
| [Kare haritası](Grid-Square-Map-tr) | – | Bir ADIF dosyasından çalışılmış ve onaylanmış Maidenhead kareleri, her bant için bir sekme |

Sekmelerin üstünde üç sıra kontrol vardır (lokatörünüz, karşı istasyon, bant, anten, iz yüksekliği, saat); bkz. [İlk adımlar](Getting-Started-tr). **Kontroller** düğmesi bunları katlar; dil ve renk şeması sağ üstten seçilir; bkz. [Ayarlar ve veri klasörü](Settings-and-Data-Folder-tr).

## Kısaca

- **Sabit yönler değil, gerçek yol**: verim, iki lokatör arasındaki büyük daire yolu için hesaplanır (eski programlar dört sabit yön kullanıyordu).
- E katmanında her 15 km'de bir alınan noktalar üzerinde **aynasal yansıma modeli** (McKinley); iz yüksekliği Collm radarından canlı okunur.
- Orta noktanın iki yanında 150 km'de (30–400 km arası ayarlanabilir) **Hot A / Hot B**; önerilen kırmızı, anten lobunuzun zaten içinde olanlar gri.
- **Canlı radar**: Collm her 5 dakikada bir denetlenir, yalnızca değişen kaynaklar yeniden indirilir; bağlantı yokken program son kaydedilen verilerle çalışmayı sürdürür.
- SM6FHZ'nin λ³ kuralıyla 50/144/432 MHz için **deneysel** tahmin; RMOB gözlemcileriyle karşılaştırılabilir.
- Her şey programın yanındaki tek bir **`data`** klasöründe: AppData yok, sistem klasörü yok.

> Verim deneysel bir modeldir (aynasal yansıma + underdense izler). MCG_MS, MS-Soft ve havadaki kendi deneyiminizle karşılaştırın.

## Nereden başlamalı

1. [Kurulum](Installation-tr)
2. [İlk adımlar](Getting-Started-tr)
3. Bir şey çalışmazsa [Sorun giderme ve SSS](Troubleshooting-FAQ-tr).

İndirmeler: GitHub'daki **[Releases](https://github.com/ic8tem/YA-MS/releases)** sayfası.
