[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · **Bahasa Indonesia** · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Lalu lintas langsung

*Tab: Langsung dan data waktu nyata › Lalu lintas langsung.*

[![Lalu lintas langsung](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Yang ditampilkan

Sebuah **peta azimutal ekuidistan** yang berpusat di stasiun Anda (jarak dari pusat = jarak sebenarnya, sudut = azimut) dengan **seluruh lalu lintas meteor scatter** yang dikumpulkan oleh [Pengumpulan data](Data-Collection-id). Untuk setiap kontak program menggambar:

- **lintasan** antara kedua stasiun, dalam warna band-nya: 28 MHz cokelat, 50 MHz hijau, 70 MHz sian, 144 MHz oranye, 222 MHz merah muda, 432 MHz ungu;
- kedua **stasiun** di ujung lintasan;
- **zona hujan meteor**: tempat jejak meteor paling mungkin untuk lintasan dan jam tersebut terkonsentrasi.

Spot dengan salah satu stasiun **di luar peta** dibuang. Hanya dekode WSJT-X Anda (UDP) yang berisi balasan koresponden kepada Anda yang berkedip.

Tampilkan siapa yang mendengarkan: segitiga berwarna pita menandai stasiun yang menurut PSKReporter menerima MSK144, FSK441, PSK2K, atau JTMS di 28, 50, 70, 144, dan 432 MHz dalam jendela waktu yang dipilih. Klik pada segitiga menampilkan callsign, locator, mode, dan spot terakhir. Aliran MQTT di tab Pengumpulan data harus terhubung.

Juga monitor aktif di peta PSKReporter: segitiga kosong untuk stasiun yang tampak di peta pskreporter.info dalam MSK144, FSK441, PSK2K atau JTMS tetapi belum menerima spot apa pun (MQTT hanya mengirim stasiun yang menerima sesuatu). YA-MS menanyai layanan kueri PSKReporter sekali setiap 5 menit untuk semua mode, sesuai aturan layanan; sebuah monitor tetap di peta setidaknya 11 menit. Klik pada segitiga menampilkan callsign, lokator, program dekode, dan waktu monitor aktif. Aktif sejak awal.

FT8 lebih dari 1100 km tanpa lintasan paralel: spot FT8 (dari PSKReporter MQTT, cluster, atau WSJT-X lewat UDP) antara stasiun yang berjarak lebih dari 1100 km yang tidak memiliki lintasan paralel dalam 3 menit sebelum dan sesudahnya (pita sama, titik tengah dalam 300 km, arah dalam 15°, pasangan stasiun lain) digambar hijau muda, begitu pula barisnya di tabel kanan bawah (tanpa berkedip). E sporadis dan tropo memberi banyak lintasan berdekatan dan paralel; spot yang terisolasi bisa jadi jejak meteor. Karena itu YA-MS juga menerima dari MQTT spot FT8 di 6 m, 4 m, 2 m, 1,25 m, dan 70 cm (tidak pernah 28 MHz). Spot ini tidak masuk arsip MS. Aktif sejak awal. Pemeriksaan tambahan dengan PSKReporter MQTT: spot tidak terisolasi jika stasiun penerima mendengar di MQTT stasiun lain lebih dari 1100 km di pita yang sama dalam 3 menit (pita terbuka); spot dari cluster dan RBN hanya dihitung jika pasangan yang sama juga datang dari MQTT; skimmer RBN (callsign dengan «-#») tidak pernah dihitung.

Dekode WSJT-X Anda melalui UDP yang berisi balasan koresponden kepada Anda (callsign pertama pesan adalah milik Anda) digambar dengan garis putus-putus yang berkedip, dalam mode apa pun dan pada jarak berapa pun, dan barisnya di tabel berkedip dengan latar kuning. Ini satu-satunya keadaan ketika sesuatu berkedip.

Pertukaran antarpengguna YA-MS: ketika pengguna YA-MS lain mendekode lewat UDP pesan yang ditujukan ke stasiun Anda (dalam MSK144, FSK441, PSK2K atau JTMS, atau FT8 lebih dari 1100 km), YA-MS-nya mengirimkannya kepada Anda secara terenkripsi melalui tiga broker MQTT publik (HiveMQ, Mosquitto, EMQX); Anda melihatnya sebagai garis putus-putus ungu yang tetap dan sebagai baris di konsol UDP. Hanya Anda yang dapat membacanya (kunci ECDH P-256, AES-256, dan HMAC-SHA256). Spot FT8 hanya ditampilkan jika tidak punya lintasan paralel dalam 3 menit. Aktif sejak awal; yams_scambio=0 di data/config.ini mematikannya.

Peta menuliskan callsign kedua stasiun pada setiap spot, sekali per stasiun. Proyeksi bisa dipilih: azimutal (berpusat di stasiunmu) atau Mercator. Tooltip pada kolom zona hujan meteor menjelaskan artinya.

Spot dari semua pita ditampilkan, termasuk pita yang tidak dipilih di Pengumpulan data (spot ini tidak disimpan). Spot CW dan spot antarstasiun yang terlalu dekat tidak ditampilkan, jika dibuang di Pengumpulan data.

## Cara zona hujan meteor dihitung

Untuk setiap spot program membangun lintasan antara kedua locator (geometri yang sama seperti untuk lintasan Anda sendiri, lihat [Geometri dan redaman](Geometry-and-Path-Loss-id)) dan, pada waktu spot tersebut, menjumlahkan titik demi titik lapisan E **kontribusi pantulan spekular dari setiap hujan meteor aktif**, dibobot dengan ZHR-nya – perhitungan yang sama dengan **zona PREV** pada [kubah langit](Sky-View-id). Untuk setiap sisi lintasan yang memuat paling sedikit 15 % dari total, zona hujan meteor berupa **elips**: pusatnya di rata-rata berbobot titik-titik tersebut, setengah sumbunya 1,5 kali akar kuadrat nilai eigen sebarannya, sumbu panjangnya searah vektor eigen utama. Jika tidak ada hujan meteor yang berkontribusi (hanya meteor sporadis), zona hujan meteor berupa dua **hot spot** klasik yang digambar putus-putus. Persamaan lengkapnya ada di bab 10 manual perhitungan.

## Kontrol

| Kontrol | Arti |
|---|---|
| **Radius peta** | 600–3500 km dari stasiun Anda. |
| **Spot yang ditampilkan** | 15 atau 30 menit terakhir, satu jam terakhir, 3 jam terakhir, 24 jam terakhir. |
| **Tabel** | Kontak di peta, yang terbaru di atas, dalam warna band; *% hujan* memberikan bagian pantulan di sisi utama, atau *sporadis*. |
| **Klik** | Pada lintasan atau baris tabel: kontak disorot dan kotak menampilkan locator pusat zona hujan meteor, bagiannya, ukuran dan sumbunya. |
