[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · **Türkçe** · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Kurulum

Tüm paketler **[Releases](https://github.com/ic8tem/YA-MS/releases)** sayfasındadır (aşağıdaki dosya adlarında `x.y.z` sürümdür, örn. `1.2.0`). Hiçbir şey derlemek ya da ayrıca kurmak gerekmez: her paket .NET 8 çalışma ortamını içerir.

| Sistem | Dosya | Kurulduğu yer |
|---|---|---|
| Windows (64 bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (kurulum programı) | `C:\YA-MS` |
| Windows (64 bit), taşınabilir | `YA-MS-x.y.z-windows-x64-portatile.zip` | yazma izniniz olan herhangi bir klasör |
| Windows (32 bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ya da `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64 bit) | `YA-MS-x.y.z-linux-x64.tar.gz` | `~/YA-MS` |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |

**Program ve `data` klasörü her zaman birlikte durur**, YA-MS klasöründe: tüm veriler ve ayarlar oradadır (AppData yok, sistem klasörü yok). Bkz. [Ayarlar ve veri klasörü](Settings-and-Data-Folder-tr).

## Windows

### Kurulum programı
1. `YA-MS-x.y.z-windows-x64-setup.exe` dosyasını indirip çalıştırın.
2. **SmartScreen** "Windows bilgisayarınızı korudu" uyarısını gösterirse: *Ek bilgi* → *Yine de çalıştır* (program ticari bir sertifikayla imzalanmamıştır).
3. YA-MS, **yönetici hakları olmadan**, Başlat menüsü simgesiyle ve işaretlerseniz bir masaüstü simgesiyle **`C:\YA-MS`** klasörüne kurulur.

### Taşınabilir
`YA-MS-x.y.z-windows-x64-portatile.zip` dosyasını istediğiniz yere açın (yazma izniniz olan bir klasöre, *Program Files*'a değil) ve `YA-MS.exe`'yi çalıştırın. Klasörün tamamını bir USB belleğe ya da başka bir bilgisayara kopyalayabilirsiniz.

## Linux

1. `YA-MS-x.y.z-linux-x64.tar.gz` dosyasını açın.
2. Açılan klasörden şunu çalıştırın:
   ```sh
   ./installa.sh
   ```
3. Betik YA-MS'i **`~/YA-MS`** klasörüne kopyalar (root gerekmez) ve uygulamalar menüsüne **YA-MS**'i ekler (*HamRadio* kategorisi). Programı `~/YA-MS/YA-MS` ile de başlatabilirsiniz.

Japonca metin için Noto CJK yazı tipleri gerekebilir: bkz. [Sorun giderme](Troubleshooting-FAQ-tr#linux-japonca-metin-kutucuk-olarak-görünüyor).

## Raspberry Pi

Linux ile aynı yöntem: `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` dosyasını (Raspberry Pi OS 32 bit'te `-32bit` olanı) açın ve açılan klasörden `./installa.sh` komutunu çalıştırın.

- Hangi sisteme sahip olduğunuzu görmek için bir terminalde `uname -m` yazın: `aarch64` → 64 bit paket, `armv7l` → 32 bit paket.
- Desteklenenler: Raspberry Pi 2 (yalnızca 32 bit), 3, 4, 5, 400 ve 500, Raspberry Pi OS'un masaüstü sürümüyle. **Desteklenmeyenler:** Pi Zero / Zero W ve Pi 1 (ARMv6 işlemci, .NET orada çalışmaz); Pi Zero 2 W 64 bit paketle çalışır ama 512 MB RAM sıkışıktır.
- En az 2 GB RAM'li bir Pi 4 ya da 5 önerilir; ilk açılış bir PC'ye göre birkaç saniye daha uzun sürer.

## macOS

1. Doğru dosyayı seçin: M1/M2/M3/M4 işlemciler için `-mac-apple-silicon.dmg`, Intel Mac'ler için `-mac-intel.dmg`.
2. `.dmg` dosyasını açın, **"Installa YA-MS.command" üzerine sağ tıklayın → Aç** ve onaylayın.
3. Betik `YA-MS.app`'i **`~/YA-MS`** klasörüne kopyalar ve açar.

Program Apple tarafından imzalanmamıştır, bu yüzden macOS ilk seferde onay ister; bkz. [Sorun giderme](Troubleshooting-FAQ-tr#macos-tanımlanmamış-bir-geliştiriciden-geldiği-için-açılamıyor).

## İlk açılış

- **Avrupa haritası** (Natural Earth kıyı çizgileri ve sınırları) ilk seferde otomatik olarak `data/mappa` klasörüne indirilir: bir kez internet bağlantısı gerekir.
- **Radar verileri** (Collm, Sodankylä) hemen indirilir, sonra her 5 dakikada bir denetlenir.
- Arayüz, mevcut altı dilden biriyse sistem dilinizde, değilse İtalyanca açılır; sağ üstten değiştirin (bkz. [Ayarlar](Settings-and-Data-Folder-tr#dil)).

## Güncelleme

Yeni sürümü **eskisinin üzerine** kurun (aynı kurulum programı, aynı klasör). Ayarlar (`config.ini`), akı arşivleri ve harita `data` içinde kalır. `data/lingue` içindeki çeviri dosyaları, yenileri daha güncelse değiştirilir.

## Kaynak koddan derleme (yalnızca geliştiriciler)

Kurulum paketleri, `release` dalının her güncellenmesinde GitHub Actions (`.github/workflows/build.yml`) tarafından üretilir (sürüm `VERSION` dosyasından alınır); aynı iş `vX.Y.Z` sürümünü de oluşturur. Yerel olarak:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # ya da linux-x64, linux-arm64, linux-arm, osx-arm64
```

Belgeler `tools/build_spiegazione.py data` ve `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx` ile yeniden üretilir.

Sonraki: [İlk adımlar](Getting-Started-tr).
