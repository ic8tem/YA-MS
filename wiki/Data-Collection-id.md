[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · **Bahasa Indonesia** · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

# Pengumpulan data

*Tab: Langsung dan data waktu nyata › Pengumpulan data.*

[![Pengumpulan data](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Empat sumber

Tab ini mengumpulkan **spot meteor scatter** dari tiga aliran telnet dan dari umpan MQTT PSKReporter, masing-masing di sub-tab tersendiri:

| Sub-tab | Bawaan | Catatan |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Cluster pilihan Anda. Di ON0DXK band VHF difilter: aktifkan dengan `set/filter dxbm/pass 6` (lalu 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmer jarang mendekode mode MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X yang membawa spot **PSKReporter**: dekode MSK144 dari WSJT-X dan MSHV tiba di sini. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Spot PSKReporter langsung melalui **MQTT** (layanan dari M0LTE): tanpa login, setiap spot sudah membawa locator stasiun pemancar dan stasiun penerima. Topik bawaan: MSK144 di 6 m, 4 m, 2 m, 1,25 m, 70 cm dan FSK441 di 2 m (`pskr/filter/v2/band/mode/#`); *Topik bawaan* memulihkannya. |
| **Spot MS terkumpul** | – | Tabel spot yang diterima, yang terbaru di atas. |

Setiap aliran memiliki host, port, perintah yang dikirim setelah login, *Sambung ulang*, *Sambung saat mulai*, sebuah konsol dan baris untuk mengirim perintah. Tulis **callsign untuk login** Anda di bagian atas. Sumber MQTT memiliki host, port, topik (satu per baris atau dipisahkan dengan `;`), *Sambung ulang* dan *Sambung saat mulai* (nonaktif secara bawaan) serta konsol berisi spot yang diterima; spotnya melewati filter yang sama. Sebuah strip menampilkan status keempat sumber (titik hijau = tersambung). Sesi tetap terbuka saat Anda mengganti bahasa atau skema warna.

## Filter (40 % dari jendela)

- **Filter lokal opsional:** baris cluster di bawah **27990,0 kHz** langsung dibuang (tidak ditampilkan, tidak disimpan).
- Spot CW langsung dibuang (CW atau WPM di komentar, atau 28000-28070 kHz): tidak muncul di konsol dan tidak disimpan, kecuali bertanda <MS>. Kotak ini dapat dimatikan.

Basis data CALL3 dengan aturan LIVETROPOVHF. "Perbarui sekarang" mengunduh CALL3.TXT dari MMMonVHF (minimal 100.000 baris valid, yang lama tetap di data/call3.bak); dengan "Perbarui sendiri setiap 7 hari" hal itu dilakukan saat mulai. Di atas berkas berlaku berurutan: entri manual (data/CALL3-MANUALE.TXT), koreksi dari cluster (lokator 6 karakter yang dinyatakan pelapor tentang dirinya), berkas tambahan (data/CALL3-AGGIUNTE), lalu CALL3.TXT dan lokator 6 karakter yang dipelajari langsung (data/LOC6.TXT). Lokator diterima 4 karakter, atau berakhiran LL atau MM, diganti dengan yang 6 karakter dari basis data; stasiun portabel (dengan garis miring) hanya dengan entri yang persis.

Sumber terakhir, seperti di LIVETROPOVHF: untuk callsign yang tidak punya lokator 6 karakter di sumber lain mana pun, program bertanya di latar belakang ke API publik G7VRD (api.g7vrd.co.uk). Hanya lokator 6 karakter yang diterima, bukan pusat kotak (LL atau MM), di kotak yang sama dengan yang diterima; paling banyak 40 callsign per menit, masing-masing sekali sehari. Hasilnya disimpan di data/CALL3-G7VRD.TXT.
- Spot antarstasiun yang berjarak kurang dari 500 km langsung dibuang, karena pada jarak itu hubungannya langsung atau troposferik, bukan meteor scatter: tidak muncul di konsol dan tidak disimpan. Jika lokator tidak ada, spot tetap disimpan. Jaraknya dapat diubah di bawah kotak centang.
- **Kriteria ke-1 – frekuensi khas MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot dalam jendela ini diterima bahkan tanpa nama mode, kecuali komentarnya menyatakan propagasi lain: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Jendela dan tag dapat diubah.
- **Kriteria ke-2 – mode MS:** di luar jendela, atau dengan salah satu tag tersebut, spot hanya dipertahankan jika memuat **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (mode digital yang hanya dipakai untuk MS) atau **\<MS\>**, dalam huruf besar, kecil atau campuran. Kata-kata dapat dinonaktifkan, ditambah dan dihapus; masing-masing punya penghitungnya sendiri.
- **Band** 28, 50, 70, 144, 222, 432 MHz; **uji filter** pada baris yang ditempel; **penghitung**.

## Locator dan penyimpanan

Locator yang tidak ada, atau yang hanya 4 karakter, diambil dari arsip **CALL3** (`data/call3.txt`, file JTDX, lebih dari satu juta callsign), yang selalu didahulukan daripada locator 4 karakter. Spot yang diterima disimpan di `data/spot_ms`, satu file CSV per hari, dan menjadi masukan peta [Lalu lintas langsung](Live-Traffic-id).
