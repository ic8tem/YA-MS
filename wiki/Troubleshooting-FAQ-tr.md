[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · **Türkçe** · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · [Bahasa Indonesia](Troubleshooting-FAQ-id) · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# Sorun giderme ve SSS

## Kurulum ve açılış

### Windows SmartScreen "Windows bilgisayarınızı korudu" diyor
Program ticari bir sertifikayla imzalanmamıştır. *Ek bilgi* → *Yine de çalıştır*'a tıklayın. Programı yalnızca [Releases](https://github.com/ic8tem/YA-MS/releases) sayfasından indirin.

### macOS: tanımlanmamış bir geliştiriciden geldiği için açılamıyor
YA-MS Apple tarafından imzalanmamıştır, bu yüzden **Gatekeeper** ilk seferde onu engeller. `.dmg` içinde **"Installa YA-MS.command" üzerine sağ tıklayın → Aç** ve onaylayın. Betik, `~/YA-MS/YA-MS.app` üzerindeki "internetten indirildi" karantina işaretini kaldırır ve uygulamayı açar. macOS yine reddederse *Sistem Ayarları → Gizlilik ve Güvenlik*'i açın ve *Yine de Aç*'a basın.

### macOS: hangi .dmg?
M1/M2/M3/M4 işlemciler için `-mac-apple-silicon.dmg`, Intel Mac'ler için `-mac-intel.dmg` (hangisi olduğunu Apple menüsü → *Bu Mac Hakkında* söyler).

### Linux: YA-MS uygulamalar menüsünde yok
`./installa.sh` komutunu açılan klasörden çalıştırın (`~/YA-MS`'ten değil). Bazı masaüstü ortamları yeni girdileri göstermek için oturumu kapatıp yeniden açmayı gerektirir. Programı her zaman `~/YA-MS/YA-MS` ile başlatabilirsiniz.

### Avrupa haritası eksik
*Avrupa haritası yok (ilk açılışta ağ gerekir).* Natural Earth haritası ilk açılışta `data/mappa` içine indirilir. İnternete bağlanın ve YA-MS'i yeniden başlatın.

## Görüntü

### Linux: Japonca metin kutucuk olarak görünüyor
Sisteminizde CJK yazı tipleri (Çince, Japonca, Korece) yok. **Noto CJK** yazı tiplerini kurun ve YA-MS'i yeniden başlatın. Aynı durum Arapça, İbranice, Urduca, Hintçe ve Bengalce için de geçerlidir: Debian, Ubuntu ve Raspberry Pi OS'ta ayrıca `fonts-noto-core` paketini kurun.

| Dağıtım | Komut |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Metin çok küçük ya da grafiklere yer kalmıyor
**Yazı tipi** kaydırıcısını (%100–300) kullanın ve sıraları **Kontroller** ile katlayın. Bkz. [Ayarlar](Settings-and-Data-Folder-tr#yazı-tipi-ve-kontroller).

### Ekran gece çok parlak
**Tema** listesinden **Gece** ya da **Siyah**'ı seçin.

## İnternet ve radar verileri

### "İnternet bağlantısı yok" iletisi
YA-MS, hiçbir kaynağa ulaşılamadığında bunu **bir kez** gösterir; durum çubuğu kırmızıya döner. Program **son kaydedilen verilerle** çalışmayı sürdürür ve 5 dakikada bir kendiliğinden yeniden dener; ağ geri geldiğinde *Bağlantı yeniden kuruldu.* görünür. Yapmanız gereken bir şey yok.

### Radar akısında turuncu uyarı: "Akının dikey ölçeği okunamıyor …"
Collm radarı dikey ölçeğini her gün değiştirir ve YA-MS onu grafik etiketlerinden okur. Bir etiket okunamazsa program 0–1200 meteor/saat kalibre ölçeğini kullanır ve **değerlerin denetlenmesi gerektiği** uyarısını verir. Genellikle bir sonraki saatlik grafik doğru okunur. Saatlerce *Grafik biçimi değişti* ya da *Akı eksenleri beklenen konumda bulunamadı* görürseniz radar grafik biçimini değiştirmiştir: lütfen [bildirin](Contributing-and-Contacts-tr).

### "Yükseklik grafiğinin ölçeği değişti"
Yükseklik istatistikleri (mod, ortalama, medyan) geçerli kalır; yalnızca yükseklik histogramının mutlak sayımları geçerli değildir.

### "Radar akısı: veri yok"
[Radar akısı](Radar-Flux-tr) sekmesinde **Şimdi indir**'e basın ve `data/fonti_radar.csv` dosyasında Collm için `attivo=1` olduğunu denetleyin.

### RMOB: otomatik indirme neden kapalı?
RMOB, **otomatik programların dosyalarını çekmemesini** ister. *5 dakikada bir otomatik indirme* seçeneğini yalnızca RMOB size izin verdikten sonra etkinleştirin. O zamana kadar **RMOB'u şimdi indir** ya da **Diskten RMOB dosyası yükle...** seçeneğini kullanın. Bkz. [Deneysel tahminler](Experimental-Forecasts-tr#rmob-ve-otomatik-programlar).

### RMOB: "Dosya biçimi tanınmadı" ya da az saat okundu
Gözlemcinin aylık metin dosyasını (`NAME_MMYYYYrmob.TXT`) ya da tek gözlemcili bir bülten tablosunu kullanın. Üs uydurma işlemi, Collm verileriyle (dün ve bugün) en az 3 ortak saat gerektirir.

## Hesaplar

### "Geçersiz istasyon lokatörü" / "Geçersiz karşı istasyon lokatörü"
Lokatörler 4, 6 ya da 8 karakterli olmalıdır (örn. `JN70`, `JN70CN`, `JN70CN12`).

### "Ortak E katmanı bölgesi yok"
Yol, iz yüksekliğindeki menzilin iki katından uzundur (lob 0°'de ve izler 89,5 km'deyken yaklaşık 2 × 1062 km): tek bir meteor scatter atlaması onu kapsayamaz. **Lob elevasyonunu** yükseltmek menzili daha da kısaltır.

### Hot A / Hot B gri
Anten DX'e dönükken zaten **anten lobunuzun içindedirler**: çevirmeye gerek yok. Bkz. [Gökyüzü kubbesi](Sky-View-tr#uyarılar).

### Verim MCG_MS ya da MS-Soft'tan farklı
YA-MS gerçek yolu ve kendi modelini kullanır; OH5IY ve MCG_MS'nin ölçeği ayrıntılı olarak belgelenmemiştir. Mutlak yüzdeler yerine saatleri ve eğilimleri karşılaştırın ve [modele](Efficiency-Calculation-tr#model) bakın.

### GRAVES huzmesinin geçişi kaymış görünüyor
Huzme dizisi PC saatinden hesaplanır: saati bir NTP sunucusuyla eşitleyin. GRAVES komuta istasyonu da diziyi zaman zaman birkaç adım kaydırır; ayrıntı, dinleyerek doğrulanacak bir öngörüdür.

## Diğer sorular

**YA-MS ücretsiz mi?** Evet, radyo amatörleri için ücretsiz bir programdır.

**Rotatörümü ya da telsizimi kontrol ediyor mu?** Hayır. YA-MS bir tahmin ve planlama aracıdır; QSO için dijital mod programınızı (örn. MSHV, WSJT-X) kullanın.

**432 MHz'in üstünde çalışıyor mu?** Bant listesi 432 MHz'de biter (28, 50, 70, 144, 222, 432). Deneysel tahmin 28 ile 1300 MHz arasında her frekansı kabul eder, ama kullandığı SM6FHZ kuralları 144 ve 432 MHz'deki deneyimden gelir.

**Bir şeyler ters gitti.** İşletim sisteminizi, YA-MS sürümünü ve ne yaptığınızı belirterek yazara yazın: bkz. [Katkıda bulunma ve iletişim](Contributing-and-Contacts-tr).
