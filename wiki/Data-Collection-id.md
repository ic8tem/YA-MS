[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · **Bahasa Indonesia** · [Tagalog](Data-Collection-tl) · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh)

# Pengumpulan data

*Tab: Langsung dan data waktu nyata › Pengumpulan data.*

[![Pengumpulan data](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Tiga aliran cluster

Tab ini mengumpulkan **spot meteor scatter** dari tiga aliran telnet, masing-masing di sub-tab tersendiri:

| Sub-tab | Bawaan | Catatan |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Cluster pilihan Anda. Di ON0DXK band VHF difilter: aktifkan dengan `set/filter dxbm/pass 6` (lalu 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Skimmer jarang mendekode mode MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster DM4X yang membawa spot **PSKReporter**: dekode MSK144 dari WSJT-X dan MSHV tiba di sini. |
| **Spot MS terkumpul** | – | Tabel spot yang diterima, yang terbaru di atas. |

Setiap aliran memiliki host, port, perintah yang dikirim setelah login, *Sambung ulang*, *Sambung saat mulai*, sebuah konsol dan baris untuk mengirim perintah. Tulis **callsign untuk login** Anda di bagian atas. Sebuah strip menampilkan status ketiga sesi (titik hijau = tersambung). Sesi tetap terbuka saat Anda mengganti bahasa atau skema warna.

## Filter (40 % dari jendela)

- **Filter lokal opsional:** baris cluster di bawah **27990,0 kHz** langsung dibuang (tidak ditampilkan, tidak disimpan).
- **Kriteria ke-1 – frekuensi khas MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Spot dalam jendela ini diterima bahkan tanpa nama mode, kecuali komentarnya menyatakan propagasi lain: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Jendela dan tag dapat diubah.
- **Kriteria ke-2 – mode MS:** di luar jendela, atau dengan salah satu tag tersebut, spot hanya dipertahankan jika memuat **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (mode digital yang hanya dipakai untuk MS) atau **\<MS\>**, dalam huruf besar, kecil atau campuran. Kata-kata dapat dinonaktifkan, ditambah dan dihapus; masing-masing punya penghitungnya sendiri.
- **Band** 28, 50, 70, 144, 222, 432 MHz; **uji filter** pada baris yang ditempel; **penghitung**.

## Locator dan penyimpanan

Locator yang tidak ada, atau yang hanya 4 karakter, diambil dari arsip **CALL3** (`data/call3.txt`, file JTDX, lebih dari satu juta callsign), yang selalu didahulukan daripada locator 4 karakter. Spot yang diterima disimpan di `data/spot_ms`, satu file CSV per hari, dan menjadi masukan peta [Lalu lintas langsung](Live-Traffic-id).
