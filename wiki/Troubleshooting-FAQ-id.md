[English](Troubleshooting-FAQ) · [Italiano](Troubleshooting-FAQ-it) · [Deutsch](Troubleshooting-FAQ-de) · [Nederlands](Troubleshooting-FAQ-nl) · [Français](Troubleshooting-FAQ-fr) · [Español](Troubleshooting-FAQ-es) · [Português](Troubleshooting-FAQ-pt) · [Português (Brasil)](Troubleshooting-FAQ-pt-BR) · [Dansk](Troubleshooting-FAQ-da) · [Norsk](Troubleshooting-FAQ-nb) · [Svenska](Troubleshooting-FAQ-sv) · [Íslenska](Troubleshooting-FAQ-is) · [Eesti](Troubleshooting-FAQ-et) · [Lietuvių](Troubleshooting-FAQ-lt) · [Latviešu](Troubleshooting-FAQ-lv) · [Polski](Troubleshooting-FAQ-pl) · [Čeština](Troubleshooting-FAQ-cs) · [Magyar](Troubleshooting-FAQ-hu) · [Română](Troubleshooting-FAQ-ro) · [Ελληνικά](Troubleshooting-FAQ-el) · [Русский](Troubleshooting-FAQ-ru) · [Українська](Troubleshooting-FAQ-uk) · [Türkçe](Troubleshooting-FAQ-tr) · [Afrikaans](Troubleshooting-FAQ-af) · [العربية](Troubleshooting-FAQ-ar) · [עברית](Troubleshooting-FAQ-he) · [اردو](Troubleshooting-FAQ-ur) · [हिन्दी](Troubleshooting-FAQ-hi) · [বাংলা](Troubleshooting-FAQ-bn) · [ไทย](Troubleshooting-FAQ-th) · **Bahasa Indonesia** · [Tagalog](Troubleshooting-FAQ-tl) · [日本語](Troubleshooting-FAQ-ja) · [한국어](Troubleshooting-FAQ-ko) · [中文](Troubleshooting-FAQ-zh) · [中文 (繁體)](Troubleshooting-FAQ-zh-TW)

# Pemecahan masalah dan FAQ

## Instalasi dan start

### Windows SmartScreen menampilkan "Windows melindungi PC Anda"
Program tidak ditandatangani dengan sertifikat komersial. Klik *Info selengkapnya* → *Tetap jalankan*. Unduh hanya dari halaman [Releases](https://github.com/ic8tem/YA-MS/releases).

### macOS: tidak dapat dibuka karena berasal dari pengembang yang tidak dikenal
YA-MS tidak ditandatangani oleh Apple, sehingga **Gatekeeper** memblokirnya pada kali pertama. Di dalam `.dmg`, **klik kanan "Installa YA-MS.command" → Open** lalu konfirmasi. Skrip menghapus tanda karantina "diunduh dari internet" dari `~/YA-MS/YA-MS.app` dan membukanya. Jika macOS masih menolak, buka *System Settings → Privacy & Security* dan tekan *Open Anyway*.

### macOS: .dmg yang mana?
`-mac-apple-silicon.dmg` untuk prosesor M1/M2/M3/M4, `-mac-intel.dmg` untuk Mac Intel (menu Apple → *About This Mac* memberi tahu Anda yang mana).

### Linux: YA-MS tidak ada di menu aplikasi
Jalankan `./installa.sh` dari folder hasil ekstrak (bukan dari `~/YA-MS`). Beberapa desktop perlu log out/log in untuk menampilkan entri baru. Anda selalu bisa menjalankannya dengan `~/YA-MS/YA-MS`.

### Peta Eropa tidak muncul
*Peta Eropa tidak tersedia (perlu jaringan saat pertama kali dijalankan).* Peta Natural Earth diunduh ke `data/mappa` pada start pertama. Sambungkan ke internet lalu jalankan ulang YA-MS.

## Tampilan

### Linux: teks Jepang tampil sebagai kotak
Sistem Anda tidak memiliki font CJK (Tionghoa, Jepang, Korea). Pasang font **Noto CJK** lalu jalankan ulang YA-MS. Hal yang sama terjadi pada bahasa Arab, Ibrani, Urdu, Hindi, dan Bengali: di Debian, Ubuntu, dan Raspberry Pi OS pasang juga `fonts-noto-core`.

| Distribusi | Perintah |
|---|---|
| Debian, Ubuntu, Mint | `sudo apt install fonts-noto-cjk` |
| Fedora | `sudo dnf install google-noto-sans-cjk-fonts` |
| Arch | `sudo pacman -S noto-fonts-cjk` |
| openSUSE | `sudo zypper install noto-sans-cjk-fonts` |

### Teks terlalu kecil, atau grafik tidak punya ruang
Gunakan penggeser **Huruf** (100–300 %) dan lipat baris-baris dengan **Kontrol**. Lihat [Pengaturan](Settings-and-Data-Folder-id#huruf-dan-kontrol).

### Layar terlalu terang di malam hari
Pilih **Malam** atau **Hitam** pada daftar **Tema**.

## Internet dan data radar

### Pesan "Tidak ada koneksi internet"
YA-MS menampilkannya **sekali** saat tidak ada sumber yang dapat dijangkau; bilah status berubah merah. Program tetap bekerja dengan **data terakhir yang tersimpan** dan mencoba lagi sendiri setiap 5 menit; *Koneksi pulih.* muncul saat jaringan kembali. Tidak ada yang perlu dilakukan.

### Peringatan oranye di Fluks radar: "Tidak dapat membaca skala vertikal fluks …"
Radar Collm mengubah skala vertikalnya setiap hari dan YA-MS membacanya dari label grafik. Jika sebuah label tidak dapat dibaca, program memakai skala terkalibrasi 0–1200 meteor/jam dan memperingatkan bahwa **nilai perlu diperiksa**. Biasanya grafik per jam berikutnya terbaca dengan benar. Jika Anda melihat *Format grafik berubah* atau *Sumbu fluks tidak ditemukan pada posisi yang diharapkan* selama berjam-jam, radar telah mengubah format grafiknya: mohon [laporkan](Contributing-and-Contacts-id).

### "Skala grafik ketinggian telah berubah"
Statistik ketinggian (modus, rata-rata, median) tetap valid; hanya hitungan absolut pada histogram ketinggian yang tidak.

### "Fluks radar: tidak ada data"
Tekan **Unduh sekarang** di [Fluks radar](Radar-Flux-id), dan periksa bahwa `data/fonti_radar.csv` memiliki `attivo=1` untuk Collm.

### RMOB: mengapa pengambilan otomatis mati?
RMOB meminta agar **program otomatis tidak mengambil file-filenya**. Aktifkan *pengambilan otomatis setiap 5 menit* hanya setelah RMOB memberi Anda izin. Sementara itu gunakan **Unduh RMOB sekarang** atau **Muat file RMOB dari disk...**. Lihat [Prakiraan eksperimental](Experimental-Forecasts-id#rmob-dan-program-otomatis).

### RMOB: "Format file tidak dikenali" atau hanya sedikit jam yang terbaca
Gunakan file teks bulanan pengamat (`NAME_MMYYYYrmob.TXT`) atau tabel buletin dengan satu pengamat saja. Pencocokan eksponen memerlukan paling sedikit 3 jam yang sama dengan data Collm (kemarin dan hari ini).

## Perhitungan

### "Locator stasiun tidak valid" / "Locator stasiun DX tidak valid"
Locator harus terdiri dari 4, 6 atau 8 karakter (mis. `JN70`, `JN70CN`, `JN70CN12`).

### "Tidak ada zona bersama lapisan E"
Lintasan lebih panjang dari dua kali jangkauan pada ketinggian jejak (sekitar 2 × 1062 km dengan lobus pada 0° dan jejak pada 89,5 km): satu lompatan meteor scatter tidak dapat mencakupnya. Menaikkan **Elevasi lobus** makin memperpendek jangkauan.

### Hot A / Hot B berwarna abu-abu
Keduanya sudah **berada di dalam lobus antena Anda** saat diarahkan ke DX: tidak perlu memutar antena. Lihat [Kubah langit](Sky-View-id#peringatan).

### Efisiensinya berbeda dari MCG_MS atau MS-Soft
YA-MS memakai lintasan nyata dan modelnya sendiri; skala OH5IY dan MCG_MS tidak didokumentasikan secara rinci. Bandingkan jam dan tren alih-alih persentase absolut, dan lihat [modelnya](Efficiency-Calculation-id#model).

### Lintasan berkas GRAVES tampak bergeser
Urutan berkas dihitung dari jam PC: sinkronkan dengan server NTP. Stasiun komando GRAVES juga kadang menggeser urutan beberapa langkah; rinciannya adalah prediksi yang harus dikonfirmasi dengan mendengarkan.

## Pertanyaan lain

**Apakah YA-MS gratis?** Ya, ini program gratis untuk radio amatir.

**Apakah program ini mengendalikan rotator atau radio saya?** Tidak. YA-MS adalah alat prakiraan dan perencanaan; gunakan program mode digital Anda (mis. MSHV, WSJT-X) untuk QSO.

**Apakah berfungsi di atas 432 MHz?** Daftar band berhenti di 432 MHz (28, 50, 70, 144, 222, 432). Prakiraan eksperimental menerima frekuensi apa pun dari 28 hingga 1300 MHz, tetapi aturan SM6FHZ yang dipakainya berasal dari pengalaman di 144 dan 432 MHz.

**Ada yang tidak beres.** Tulis kepada penulis dengan menyebutkan sistem operasi Anda, versi YA-MS dan apa yang Anda lakukan: lihat [Berkontribusi dan kontak](Contributing-and-Contacts-id).
