[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · **Türkçe** · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Veri toplama

*Sekme: Canlı ve gerçek zamanlı veriler › Veri toplama.*

[![Veri toplama](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Dört kaynak

Sekme **meteor scatter spot'larını** üç telnet akışından ve PSKReporter MQTT akışından toplar; her biri kendi alt sekmesindedir:

| Alt sekme | Varsayılan | Notlar |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Seçtiğiniz bir cluster. ON0DXK'de VHF bantları filtrelenmiştir: `set/filter dxbm/pass 6` ile açın (sonra 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmer'lar MS modlarını nadiren çözer. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | **PSKReporter** spot'larını taşıyan DM4X cluster'ı: WSJT-X ve MSHV'nin MSK144 çözümleri buraya gelir. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | **MQTT** üzerinden canlı PSKReporter spot'ları (M0LTE hizmeti): oturum açmak gerekmez, her spot gönderen ve alan istasyonun lokatörlerini zaten içerir. Varsayılan konular: 6 m, 4 m, 2 m, 1,25 m, 70 cm'de MSK144 ve 2 m'de FSK441 (`pskr/filter/v2/band/mode/#`); *Varsayılan konular* bunları geri yükler. |
| **Toplanan MS spot'ları** | – | Kabul edilen spot'ların tablosu, en yenisi başta. |

Her akışın sunucusu, portu, oturum açıldıktan sonra gönderilen komutları, *Yeniden bağlan*, *Açılışta bağlan* seçenekleri, bir konsolu ve komut göndermek için bir satırı vardır. **Oturum için çağrı işaretinizi** en üste yazın. MQTT kaynağının sunucusu, portu, konuları (satır başına bir tane ya da `;` ile ayrılmış), *Yeniden bağlan* ve *Açılışta bağlan* seçenekleri (varsayılan olarak kapalı) ve alınan spot'ları gösteren bir konsolu vardır; spot'ları aynı filtreden geçer. Bir şerit dört kaynağın durumunu gösterir (yeşil nokta = bağlı). Dili ya da renk şemasını değiştirdiğinizde oturumlar açık kalır.

## Filtre (pencerenin %40'ı)

- **İsteğe bağlı yerel filtre:** **27990,0 kHz**'in altındaki cluster satırları hemen atılır (gösterilmez, saklanmaz).
- CW spotları hemen atılır (yorumda CW veya WPM, ya da 28000-28070 kHz): <MS> ile işaretlenmedikçe konsolda görünmez ve kaydedilmez. Kutu kapatılabilir.
- **1. kriter – tipik MS frekansları:** 50190–50300, 70100–70400, 144290–144399 kHz. Bu pencerelerdeki bir spot, mod adı olmasa bile kabul edilir; yorum başka bir yayılım bildirmiyorsa: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Pencereler ve etiketler düzenlenebilir.
- **2. kriter – MS modları:** pencerelerin dışında ya da bu etiketlerden biriyle gelen bir spot, ancak **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (yalnızca MS için kullanılan dijital modlar) ya da **\<MS\>** içeriyorsa tutulur; büyük, küçük ya da karışık harfle. Kelimeler kapatılabilir, eklenebilir ve kaldırılabilir; her birinin kendi sayacı vardır.
- **Bantlar** 28, 50, 70, 144, 222, 432 MHz; yapıştırılan bir satır üzerinde **filtre testi**; **sayaçlar**.

## Lokatörler ve saklama

Eksik lokatörler ya da yalnızca 4 karakterli lokatörler **CALL3** arşivinden (`data/call3.txt`, JTDX dosyası, bir milyondan fazla çağrı işareti) alınır; bu arşiv 4 karakterli bir lokatöre her zaman üstün gelir. Kabul edilen spot'lar `data/spot_ms` içinde, her gün için bir CSV dosyası olarak kaydedilir ve [Canlı trafik](Live-Traffic-tr) haritasını besler.
