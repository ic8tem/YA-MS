[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-BR) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Magyar](Settings-and-Data-Folder-hu) · [Română](Settings-and-Data-Folder-ro) · [Ελληνικά](Settings-and-Data-Folder-el) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · **Türkçe** · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · [ไทย](Settings-and-Data-Folder-th) · [Bahasa Indonesia](Settings-and-Data-Folder-id) · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh) · [中文 (繁體)](Settings-and-Data-Folder-zh-TW)

# Ayarlar ve veri klasörü

## Sekme çubuğu

Sekme çubuğunun sağ ucunda, sağdan sola:

| Kontrol | Ne yapar |
|---|---|
| **Dil** (liste) | Arayüz dili; bkz. [Dil](#dil) |
| **Tema** (liste) | Renk şeması; bkz. [Renk şemaları](#renk-şemaları) |
| **Kontroller ▴ / ▾** | Sekmelerin üstündeki üç sıra kontrolü katlar ya da açar; bkz. [Yazı tipi ve Kontroller](#yazı-tipi-ve-kontroller) |

Dili ya da temayı değiştirmek ayarları kaydeder ve **pencereyi** aynı konum ve boyutta, aynı sekmede **yeniden kurar**: yeniden başlatmak gerekmez.

## Dil

28 arayüz dili; YAEC ve E-LAYER ANALYZER ile aynı (YAEC ile ortak terimler aynı şekilde çevrilmiştir):

| Dil | Kod | Dosya |
|---|---|---|
| Italiano | `it` | yok: İtalyanca temel dildir (anahtarlar) |
| English | `en` | `data/lingue/en.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Français | `fr` | `data/lingue/fr.txt` |
| Español | `es` | `data/lingue/es.txt` |
| Português | `pt` | `data/lingue/pt.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |
| Svenska | `sv` | `data/lingue/sv.txt` |
| Norsk (bokmål) | `nb` | `data/lingue/nb.txt` |
| Dansk | `da` | `data/lingue/da.txt` |
| Íslenska | `is` | `data/lingue/is.txt` |
| Eesti | `et` | `data/lingue/et.txt` |
| Latviešu | `lv` | `data/lingue/lv.txt` |
| Lietuvių | `lt` | `data/lingue/lt.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| Українська | `uk` | `data/lingue/uk.txt` |
| Türkçe | `tr` | `data/lingue/tr.txt` |
| Afrikaans | `af` | `data/lingue/af.txt` |
| العربية | `ar` | `data/lingue/ar.txt` |
| עברית | `he` | `data/lingue/he.txt` |
| اردو | `ur` | `data/lingue/ur.txt` |
| हिन्दी | `hi` | `data/lingue/hi.txt` |
| বাংলা | `bn` | `data/lingue/bn.txt` |
| Bahasa Indonesia | `id` | `data/lingue/id.txt` |
| Tagalog | `tl` | `data/lingue/tl.txt` |
| 中文 (简体) | `zh` | `data/lingue/zh.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| 한국어 | `ko` | `data/lingue/ko.txt` |

İlk açılışta YA-MS, bunlardan biriyse **sistem dilini**, değilse İtalyancayı kullanır. Sayılar ve tarihler seçilen dili izler (örn. İngilizcede ondalık nokta, İtalyanca ve Almancada virgül). Bir çeviri dosyasında eksik olan her metin İtalyanca gösterilir. Linux'ta Çince, Japonca, Korece, Arapça, İbranice, Urduca, Hintçe ve Bengalce için uygun yazı tipleri gerekir (örn. Noto aileleri): bkz. [Sorun giderme](Troubleshooting-FAQ-tr#linux-japonca-metin-kutucuk-olarak-görünüyor).

[Verim - açıklama](Efficiency-Explanation-tr) belgesi ve hesap kılavuzu İtalyancadır.

## Renk şemaları

**Tema** listesi 12 şema sunar; yazarın EME programı YAEC'dekilerle aynı, artı özgün YA-MS paleti:

| Şema | Açıklama |
|---|---|
| **Açık** | varsayılan |
| **Gece** | koyu mavi tonlar, gece kullanımı için |
| **Siyah** | siyah arka plan, karanlık ortam ve OLED ekranlar için |
| Pastel açık mavi · Pastel turuncu · Pastel akuamarin · Pastel yeşil · Pastel pembe · Pastel leylak · Pastel çivit · Pastel kahverengi | sekiz açık pastel şema |
| **Meteor izi** | özgün YA-MS tarzı (1.2.0 sürümüne kadar): açık mavi, mor, açık yeşil, sarı ve turuncuyla gece moru |

Şema tüm sekmelere uygulanır ve `config.ini` içinde kaydedilir (anahtar `tema`).

## Yazı tipi ve Kontroller

- **Yazı tipi** (birinci kontrol sırasının sonunda): **tüm metni** %10'luk adımlarla **%100'den %300'e** büyütür; çizgiler, daireler ve haritalar boyutlarını korur. Büyük yazı tiplerinde sekmeler ikinci bir satıra kayar ve kartlar büyür.
- **Kontroller**: büyük yazı tiplerinde ya da küçük bir ekranda, haritalara ve grafiklere yer açmak için üç sıra kontrolü katlayın. Durum hatırlanır.

## Veri klasörü

Tüm veriler ve ayarlar **programın yanındaki** tek bir **`data`** klasöründedir – AppData yok, sistem klasörü yok:

| Sistem | Program | Veriler |
|---|---|---|
| Windows (kurulum programı) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (taşınabilir) | nereye açtıysanız | `YA-MS.exe`'nin yanındaki `data` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (uygulamanın yanında) |

Açılışta program gerekirse klasörü oluşturur ve yalnızca **eksik** başlangıç dosyalarını kopyalar: değiştirdiğiniz dosyaların üzerine asla yazılmaz. `data/lingue` içindeki çeviri dosyaları program dosyalarıdır ve yeni sürümün dosyaları daha güncelse değiştirilir.

### Düzenleyebileceğiniz dosyalar

| Dosya | İçerik |
|---|---|
| `sciami.csv` | Yağmur kataloğu (IMO değerleri ve çalışma değerleri); bkz. [Yağmurlar](Showers-tr#kataloğun-düzenlenmesi) |
| `massimi_imo.csv` | IMO'nun yayımladığı tepe tarihleri ve saatleri (2026, 2027): **yeni yılları** buraya ekleyin |
| `ant_radiante.csv` | Antihelion Kaynağının konumu (IMO tablo 6) |
| `fonti_radar.csv` | Radar adresleri; `attivo=1` indirir, `0` yok sayar |
| `regole_sperimentali.csv` | Kullanılan sabitler ve kurallar, her biri kaynağıyla (başvuru için) |
| `lingue/<code>.txt` | Arayüz çevirileri; bkz. [Katkıda bulunma](Contributing-and-Contacts-tr#çeviriler) |
| `config.ini` | Ayarlar (aşağıya bakın) |

### Programın oluşturduğu dosyalar

| Dosya / klasör | İçerik |
|---|---|
| `config.ini` | Ayarlar |
| `flusso_collm.csv` | Collm akısının saatlik arşivi |
| `quote_collm.csv` | İz yüksekliklerinin arşivi |
| `radar/` | En son radar görüntüleri ve RMOB dosyaları |
| `mappa/` | Natural Earth kıyı çizgileri ve sınırları (ilk açılışta indirilir) |
| `adif_quadrati.csv` | Son yüklenen ADIF'ten kareler |
| `efficienza_spiegazione.txt`, `.docx` | [Açıklama belgesi](Efficiency-Explanation-tr) |

## config.ini

Düz metin, her satırda bir `key=value` (`#` ya da `;` ile başlayan satırlar yorumdur). Program dosyayı kapanırken yazar, bu yüzden **YA-MS kapalıyken düzenleyin**. Bilmek isteyebileceğiniz anahtarlar:

| Anahtar | Varsayılan | Anlamı |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Lokatörünüz ve yüksekliğiniz (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Karşı istasyonun lokatörü ve yüksekliği (m) |
| `banda_MHz` | 144 | Bant (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | İz yüksekliği (km); 1 = Collm modunu kullan |
| `elevazione_lobo_gradi` | 0 | Lob elevasyonu (°) |
| `boom_m` | 4.6 | Yagi boom uzunluğu (m) |
| `hot_spot_km` | 150 | Hot A / Hot B'nin orta noktaya uzaklığı (30–400 km) |
| `lingua` | sistem / `it` | Dil kodu (yukarıdaki 28 koddan biri, örn. `it`, `en`, `de`) |
| `tema` | `chiaro` | Renk şeması: `chiaro` (Açık), `scuro` (Gece), `nero` (Siyah), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Meteor izi) |
| `carattere_pct` | 100 | Yazı tipi boyutu (%100–300) |
| `comandi_visibili` | 1 | 1 = kontrol sıraları görünür, 0 = katlı |
| `mostra_mappa`, `vista_alto` | 1, 1 | Gökyüzü kubbesinde Avrupa haritası, üstten görünüm |
| `aggiornamento_automatico` | 1 | Kaynakların 5 dakikada bir otomatik denetimi |
| `esponente_lambda` | 3 | Radar akısı sekmesindeki λ üssü |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Bağlantı bütçesi girdileri |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Deneysel tahmin: frekans, k, K |
| `rmob_osservatore` | boş | RMOB gözlemcisinin adı |
| `rmob_automatico` | 0 | Otomatik RMOB indirmesi (yalnızca RMOB'un izniyle etkinleştirin) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | RMOB adres şablonu |
| `graves_sequenza` | 0 | GRAVES huzme dizisi: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Gizlilik

YA-MS hiçbir veri toplamaz ve reklam göstermez. İnternete yalnızca kamuya açık verileri indirmek için bağlanır: Collm ve Sodankylä radar görüntüleri, Natural Earth haritası (ilk açılış) ve isterseniz bir RMOB dosyası.
