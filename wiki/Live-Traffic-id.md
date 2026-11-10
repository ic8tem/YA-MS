[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-BR) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · **Bahasa Indonesia** · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-TW)

# Lalu lintas langsung

*Tab: Langsung dan data waktu nyata › Lalu lintas langsung.*

[![Lalu lintas langsung](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Yang ditampilkan

Sebuah **peta azimutal ekuidistan** yang berpusat di stasiun Anda (jarak dari pusat = jarak sebenarnya, sudut = azimut) dengan **seluruh lalu lintas meteor scatter** yang dikumpulkan oleh [Pengumpulan data](Data-Collection-id). Untuk setiap kontak program menggambar:

- **lintasan** antara kedua stasiun, dalam warna band-nya: 28 MHz cokelat, 50 MHz hijau, 70 MHz sian, 144 MHz oranye, 222 MHz merah muda, 432 MHz ungu;
- kedua **stasiun** di ujung lintasan;
- **awan**: tempat jejak meteor paling mungkin untuk lintasan dan jam tersebut terkonsentrasi.

Spot dengan salah satu stasiun **di luar peta** dibuang. Spot yang **baru tiba** (tidak lebih tua dari 3 menit) **berkedip selama satu menit**, sehingga aktivitas baru langsung terlihat.

## Cara awan dihitung

Untuk setiap spot program membangun lintasan antara kedua locator (geometri yang sama seperti untuk lintasan Anda sendiri, lihat [Geometri dan redaman](Geometry-and-Path-Loss-id)) dan, pada waktu spot tersebut, menjumlahkan titik demi titik lapisan E **kontribusi pantulan spekular dari setiap hujan meteor aktif**, dibobot dengan ZHR-nya – perhitungan yang sama dengan **zona PREV** pada [kubah langit](Sky-View-id). Untuk setiap sisi lintasan yang memuat paling sedikit 15 % dari total, awan berupa **elips**: pusatnya di rata-rata berbobot titik-titik tersebut, setengah sumbunya 1,5 kali akar kuadrat nilai eigen sebarannya, sumbu panjangnya searah vektor eigen utama. Jika tidak ada hujan meteor yang berkontribusi (hanya meteor sporadis), awan berupa dua **hot spot** klasik yang digambar putus-putus. Persamaan lengkapnya ada di bab 10 manual perhitungan.

## Kontrol

| Kontrol | Arti |
|---|---|
| **Radius peta** | 600–3500 km dari stasiun Anda. |
| **Spot yang ditampilkan** | 15 atau 30 menit terakhir, satu jam terakhir, 3 jam terakhir, 24 jam terakhir. |
| **Tabel** | Kontak di peta, yang terbaru di atas, dalam warna band; *Awan* memberikan bagian pantulan di sisi utama, atau *sporadis*. |
| **Klik** | Pada lintasan atau baris tabel: kontak disorot dan kotak menampilkan locator pusat awan, bagiannya, ukuran dan sumbunya. |
