[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Português (Brasil)](Installation-pt-br) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Polski](Installation-pl) · [Čeština](Installation-cs) · [Magyar](Installation-hu) · [Română](Installation-ro) · [Ελληνικά](Installation-el) · [Русский](Installation-ru) · [Українська](Installation-uk) · **Türkçe** · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · [ไทย](Installation-th) · [Bahasa Indonesia](Installation-id) · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh) · [中文 (繁體)](Installation-zh-tw)

# Kurulum

Tüm paketler **[Releases](https://github.com/ic8tem/YA-MS/releases)** sayfasındadır (aşağıdaki dosya adlarında `x.y.z` sürümdür, örn. `1.2.0`). Hiçbir şey derlemek ya da ayrıca kurmak gerekmez: her paket .NET 8 çalışma ortamını içerir.

| Sistem | Dosya | Kurulduğu yer |
|---|---|---|
| Windows (64 bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (kurulum programı) | `C:\YA-MS` |
| Windows (64 bit), taşınabilir | `YA-MS-x.y.z-windows-x64-portatile.zip` | yazma izniniz olan herhangi bir klasör |
| Windows (32 bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` ya da `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| ARM üzerinde Windows (64 bit, Snapdragon'lu PC'ler) | `YA-MS-x.y.z-windows-arm64-setup.exe` ya da `...-windows-arm64-portatile.zip` | `C:\YA-MS` |
| Linux (64 bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| Linux (64 bit), herhangi bir dağıtım | `YA-MS-x.y.z-linux-x64.tar.gz` (taşınabilir ya da `./installa.sh` ile) | `~/YA-MS` ya da herhangi bir klasör |
| Linux (64 bit): Fedora, openSUSE | `ya-ms-x.y.z.x86_64.rpm` (x86_64), `ya-ms-x.y.z.aarch64.rpm` (ARM64), `ya-ms-x.y.z.armv7hl.rpm` (ARM 32) | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| Arch, Manjaro, EndeavourOS, Arch Linux ARM | `ya-ms-x.y.z-1-x86_64.pkg.tar.zst`, `ya-ms-x.y.z-1-aarch64.pkg.tar.zst` | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| Slackware64, Slackware ARM64 | `ya-ms-x.y.z-x86_64-1_ic8tem.txz`, `ya-ms-x.y.z-aarch64-1_ic8tem.txz` | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| AppImage (x86_64, aarch64) | `YA-MS-x.y.z-x86_64.AppImage`, `YA-MS-x.y.z-aarch64.AppImage` | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| Alpine Linux (musl) | `YA-MS-x.y.z-alpine-x64.tar.gz`, `YA-MS-x.y.z-alpine-arm64.tar.gz` | `~/YA-MS` ya da herhangi bir klasör |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64 bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32 bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, Debian paketi | `ya-ms_x.y.z_arm64.deb` (64 bit) ya da `ya-ms_x.y.z_armhf.deb` (32 bit) | `~/YA-MS` (ilk açılışta oraya kopyalanır) |
| Linux ARM 64 bit, herhangi bir dağıtım (ör. Slackware ARM64) | `YA-MS-x.y.z-linux-arm64.tar.gz` (taşınabilir ya da `./installa.sh` ile) | `~/YA-MS` ya da herhangi bir klasör |
| Linux armv7l (ARM 32 bit), herhangi bir dağıtım | `YA-MS-x.y.z-linux-armv7l.tar.gz` (taşınabilir ya da `./installa.sh` ile) | `~/YA-MS` ya da herhangi bir klasör |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, yalnızca uygulama | `YA-MS-x.y.z-mac-apple-silicon-app.zip` ya da `...-mac-intel-app.zip` | `YA-MS.app`'i açtığınız klasör |

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

### Debian paketi (.deb)
Debian, Ubuntu, Mint ve Raspberry Pi OS'ta bunun yerine `ya-ms_x.y.z_amd64.deb` paketini (Raspberry Pi'de `_arm64.deb` / `_armhf.deb`) kurabilirsiniz:
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Paket programı `/opt/ya-ms` içine koyar ve **YA-MS**'i menüye ekler. İlk açılışta (ve her yeni sürümden sonra) program kendini **`~/YA-MS`** klasörüne kopyalar ve oradan çalışır; böylece `data` klasörü programın yanında kalır ve ayarlarınız korunur.

### Taşınabilir
`.tar.gz` kurulum yapmadan da çalışır: yazma izniniz olan herhangi bir yere açın ve o klasörden `./YA-MS`'i çalıştırın.

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

Alternatif olarak `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` yalnızca `YA-MS.app`'i içerir: seçtiğiniz bir klasöre (yazma izniniz olan) açın; `data` klasörü `YA-MS.app`'in yanında oluşturulur. İlk seferde sağ tıklayın → **Aç**.

Program Apple tarafından imzalanmamıştır, bu yüzden macOS ilk seferde onay ister; bkz. [Sorun giderme](Troubleshooting-FAQ-tr#macos-tanımlanmamış-bir-geliştiriciden-geldiği-için-açılamıyor).

## İlk açılış

- **Avrupa haritası** (Natural Earth kıyı çizgileri ve sınırları) ilk seferde otomatik olarak `data/mappa` klasörüne indirilir: bir kez internet bağlantısı gerekir.
- **Radar verileri** (Collm, Sodankylä) hemen indirilir, sonra her 5 dakikada bir denetlenir.
- Arayüz, mevcut 36 dilden biriyse sistem dilinizde, değilse İtalyanca açılır; sağ üstten değiştirin (bkz. [Ayarlar](Settings-and-Data-Folder-tr#dil)).

## Güncelleme

Yeni sürümü **eskisinin üzerine** kurun (aynı kurulum programı, aynı klasör). Ayarlar (`config.ini`), akı arşivleri ve harita `data` içinde kalır. `data/lingue` içindeki çeviri dosyaları, yenileri daha güncelse değiştirilir.

**1.8.0'dan itibaren YA-MS kendini günceller.** Açılışta günde bir kez GitHub'da yeni bir sürüm olup olmadığını denetler ve önerir; alt çubuktaki **Güncellemeler** düğmesi elle denetler. *Şimdi güncelle* sisteminiz için taşınabilir paketi indirir, program dosyalarını değiştirir, `data` klasörünü korur (değişen program dosyaları önce `data/backup/v<eski sürüm>` klasörüne kopyalanır) ve yeniden başlar; program klasörüne yazılabilmelidir. Açılışta program dosyaları eksikse (`data` veya `doc` içinde), bir pencere bunları listeler ve GitHub'dan yeniden indirmeyi önerir. Yeni sürümleri denetlememek için `config.ini` içinde `controlla_aggiornamenti=0` yapın.

## Kaynak koddan derleme (yalnızca geliştiriciler)

Kurulum paketleri, `release` dalının her güncellenmesinde GitHub Actions (`.github/workflows/build.yml`) tarafından üretilir (sürüm `VERSION` dosyasından alınır); aynı iş `vX.Y.Z` sürümünü de oluşturur. Yerel olarak:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # ya da linux-x64, linux-arm64, linux-arm, osx-arm64
```

Belgeler (tüm diller) `tools/build_documenti.sh` ile yeniden üretilir.

Sonraki: [İlk adımlar](Getting-Started-tr).
