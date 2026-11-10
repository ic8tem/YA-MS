[English](Installation) · [Italiano](Installation-it) · [Deutsch](Installation-de) · [Nederlands](Installation-nl) · [Français](Installation-fr) · [Español](Installation-es) · [Português](Installation-pt) · [Dansk](Installation-da) · [Norsk](Installation-nb) · [Svenska](Installation-sv) · [Íslenska](Installation-is) · [Eesti](Installation-et) · [Lietuvių](Installation-lt) · [Latviešu](Installation-lv) · [Русский](Installation-ru) · [Українська](Installation-uk) · [Türkçe](Installation-tr) · [Afrikaans](Installation-af) · [العربية](Installation-ar) · [עברית](Installation-he) · [اردو](Installation-ur) · [हिन्दी](Installation-hi) · [বাংলা](Installation-bn) · **Bahasa Indonesia** · [Tagalog](Installation-tl) · [日本語](Installation-ja) · [한국어](Installation-ko) · [中文](Installation-zh)

# Instalasi

Semua paket ada di halaman **[Releases](https://github.com/ic8tem/YA-MS/releases)** (pada nama file di bawah, `x.y.z` adalah versinya, mis. `1.2.0`). Tidak ada yang perlu dikompilasi dan tidak ada yang perlu dipasang tambahan: setiap paket sudah berisi runtime .NET 8.

| Sistem | File | Dipasang di |
|---|---|---|
| Windows (64-bit) | `YA-MS-x.y.z-windows-x64-setup.exe` (installer) | `C:\YA-MS` |
| Windows (64-bit), portabel | `YA-MS-x.y.z-windows-x64-portatile.zip` | folder mana pun yang bisa Anda tulisi |
| Windows (32-bit, Windows 10/11) | `YA-MS-x.y.z-windows-x86-setup.exe` atau `...-windows-x86-portatile.zip` | `C:\YA-MS` |
| Linux (64-bit): Debian, Ubuntu, Mint | `ya-ms_x.y.z_amd64.deb` | `~/YA-MS` (disalin ke sana saat pertama kali dijalankan) |
| Linux (64-bit), distribusi apa pun | `YA-MS-x.y.z-linux-x64.tar.gz` (portabel atau dengan `./installa.sh`) | `~/YA-MS` atau folder mana pun |
| Raspberry Pi 3/4/5, 400/500 (Raspberry Pi OS 64-bit) | `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi 2/3/4 (Raspberry Pi OS 32-bit) | `YA-MS-x.y.z-raspberry-pi-32bit.tar.gz` | `~/YA-MS` |
| Raspberry Pi, paket Debian | `ya-ms_x.y.z_arm64.deb` (64-bit) atau `ya-ms_x.y.z_armhf.deb` (32-bit) | `~/YA-MS` (disalin ke sana saat pertama kali dijalankan) |
| macOS, Apple silicon (M1/M2/M3/M4) | `YA-MS-x.y.z-mac-apple-silicon.dmg` | `~/YA-MS` |
| macOS, Intel | `YA-MS-x.y.z-mac-intel.dmg` | `~/YA-MS` |
| macOS, hanya aplikasi | `YA-MS-x.y.z-mac-apple-silicon-app.zip` atau `...-mac-intel-app.zip` | folder tempat Anda mengekstrak `YA-MS.app` |

**Program dan folder `data`-nya selalu berada bersama** di folder YA-MS: semua data dan pengaturan ada di sana (tanpa AppData, tanpa folder sistem). Lihat [Pengaturan dan folder data](Settings-and-Data-Folder-id).

## Windows

### Installer
1. Unduh `YA-MS-x.y.z-windows-x64-setup.exe` lalu jalankan.
2. Jika **SmartScreen** menampilkan "Windows melindungi PC Anda": *Info selengkapnya* → *Tetap jalankan* (program tidak ditandatangani dengan sertifikat komersial).
3. YA-MS dipasang di **`C:\YA-MS`**, **tanpa hak administrator**, dengan ikon di menu Start dan, jika Anda mencentangnya, ikon di desktop.

### Portabel
Ekstrak `YA-MS-x.y.z-windows-x64-portatile.zip` di mana saja (folder yang bisa Anda tulisi, bukan *Program Files*) lalu jalankan `YA-MS.exe`. Seluruh folder dapat Anda salin ke flashdisk USB atau komputer lain.

## Linux

1. Ekstrak `YA-MS-x.y.z-linux-x64.tar.gz`.
2. Dari folder hasil ekstrak, jalankan:
   ```sh
   ./installa.sh
   ```
3. Skrip menyalin YA-MS ke **`~/YA-MS`** (tidak perlu root) dan menambahkan **YA-MS** ke menu aplikasi (kategori *HamRadio*). Anda juga bisa menjalankannya dengan `~/YA-MS/YA-MS`.

### Paket Debian (.deb)
Di Debian, Ubuntu, Mint, dan Raspberry Pi OS Anda juga dapat memasang `ya-ms_x.y.z_amd64.deb` sebagai gantinya (`_arm64.deb` / `_armhf.deb` di Raspberry Pi):
```sh
sudo apt install ./ya-ms_x.y.z_amd64.deb
```
Paket ini menempatkan program di `/opt/ya-ms` dan menambahkan **YA-MS** ke menu. Saat pertama kali dijalankan (dan setelah setiap versi baru) program menyalin dirinya ke **`~/YA-MS`** dan berjalan dari sana, sehingga folder `data` tetap berada di samping program dan pengaturan Anda tetap tersimpan.

### Portabel
File `.tar.gz` juga bisa dipakai tanpa dipasang: ekstrak di mana saja yang bisa Anda tulisi lalu jalankan `./YA-MS` dari folder tersebut.

Untuk teks bahasa Jepang Anda mungkin memerlukan font Noto CJK: lihat [Pemecahan masalah](Troubleshooting-FAQ-id#linux-teks-jepang-tampil-sebagai-kotak).

## Raspberry Pi

Prosedurnya sama dengan Linux: ekstrak `YA-MS-x.y.z-raspberry-pi-64bit.tar.gz` (atau `-32bit` pada Raspberry Pi OS 32-bit) lalu jalankan `./installa.sh` dari folder hasil ekstrak.

- Untuk melihat sistem yang Anda punya, ketik `uname -m` di terminal: `aarch64` → paket 64-bit, `armv7l` → paket 32-bit.
- Didukung: Raspberry Pi 2 (hanya 32-bit), 3, 4, 5, 400 dan 500, dengan versi desktop Raspberry Pi OS. **Tidak didukung:** Pi Zero / Zero W dan Pi 1 (prosesor ARMv6, .NET tidak berjalan di sana); Pi Zero 2 W bisa dengan paket 64-bit, tetapi RAM 512 MB terasa sempit.
- Disarankan Pi 4 atau 5 dengan RAM minimal 2 GB; start pertama beberapa detik lebih lama daripada di PC.

## macOS

1. Pilih file yang tepat: `-mac-apple-silicon.dmg` untuk prosesor M1/M2/M3/M4, `-mac-intel.dmg` untuk Mac Intel.
2. Buka `.dmg`, **klik kanan "Installa YA-MS.command" → Open** lalu konfirmasi.
3. Skrip menyalin `YA-MS.app` ke **`~/YA-MS`** dan membukanya.

Sebagai alternatif, `YA-MS-x.y.z-mac-apple-silicon-app.zip` / `-mac-intel-app.zip` hanya berisi `YA-MS.app`: ekstrak ke folder pilihan Anda (yang bisa Anda tulisi); folder `data` dibuat di samping `YA-MS.app`. Pada kali pertama: klik kanan → **Open**.

Program tidak ditandatangani oleh Apple, sehingga pada kali pertama macOS meminta konfirmasi; lihat [Pemecahan masalah](Troubleshooting-FAQ-id#macos-tidak-dapat-dibuka-karena-berasal-dari-pengembang-yang-tidak-dikenal).

## Start pertama

- **Peta Eropa** (garis pantai dan perbatasan Natural Earth) diunduh otomatis ke `data/mappa` pada kali pertama: koneksi internet diperlukan sekali.
- **Data radar** (Collm, Sodankylä) langsung diunduh, lalu diperiksa setiap 5 menit.
- Antarmuka dimulai dalam bahasa sistem Anda jika termasuk salah satu dari enam bahasa yang tersedia, jika tidak dalam bahasa Italia; ubah di kanan atas (lihat [Pengaturan](Settings-and-Data-Folder-id#bahasa)).

## Pembaruan

Pasang versi baru **di atas versi lama** (installer yang sama, folder yang sama). Pengaturan (`config.ini`), arsip fluks dan peta tetap berada di `data`. File terjemahan di `data/lingue` diganti bila yang baru lebih mutakhir.

## Membangun dari kode sumber (khusus pengembang)

Installer dibuat oleh GitHub Actions (`.github/workflows/build.yml`) setiap kali cabang `release` diperbarui (versi diambil dari file `VERSION`), yang sekaligus membuat rilis `vX.Y.Z`. Secara lokal:

```sh
dotnet publish YA-MS.csproj -c Release -r win-x64 --self-contained true     # atau linux-x64, linux-arm64, linux-arm, osx-arm64
```

Dokumen-dokumen dibuat ulang dengan `tools/build_spiegazione.py data` dan `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.

Berikutnya: [Memulai](Getting-Started-id).
