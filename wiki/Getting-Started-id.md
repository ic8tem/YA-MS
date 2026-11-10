[English](Getting-Started) · [Italiano](Getting-Started-it) · [Deutsch](Getting-Started-de) · [Nederlands](Getting-Started-nl) · [Français](Getting-Started-fr) · [Español](Getting-Started-es) · [Português](Getting-Started-pt) · [Dansk](Getting-Started-da) · [Norsk](Getting-Started-nb) · [Svenska](Getting-Started-sv) · [Íslenska](Getting-Started-is) · [Eesti](Getting-Started-et) · [Lietuvių](Getting-Started-lt) · [Latviešu](Getting-Started-lv) · [Русский](Getting-Started-ru) · [Українська](Getting-Started-uk) · [Türkçe](Getting-Started-tr) · [Afrikaans](Getting-Started-af) · [العربية](Getting-Started-ar) · [עברית](Getting-Started-he) · [اردو](Getting-Started-ur) · [हिन्दी](Getting-Started-hi) · [বাংলা](Getting-Started-bn) · **Bahasa Indonesia** · [Tagalog](Getting-Started-tl) · [日本語](Getting-Started-ja) · [한국어](Getting-Started-ko) · [中文](Getting-Started-zh)

# Memulai

Pada start pertama YA-MS menampilkan lintasan contoh (JN70CN → JO62QM di 144 MHz). Lima menit cukup untuk menyesuaikannya dengan stasiun Anda.

## 1. Tiga baris kontrol

Di atas tab terdapat tiga baris kontrol yang berlaku untuk semua tab. Tombol **Kontrol** di kanan atas melipat dan membukanya (berguna dengan huruf besar); pilihan ini diingat.

**Baris 1 – stasiun dan band**

| Kontrol | Fungsinya |
|---|---|
| **Locator saya** / **ketinggian m** | Locator Maidenhead Anda (4, 6 atau 8 karakter; yang dipakai adalah pusat kotak) dan ketinggian stasiun di atas permukaan laut. |
| **Stasiun DX** / **ketinggian m** | Locator dan ketinggian stasiun yang ingin Anda kerjakan. |
| **Band MHz** | 28, 50, 70, 144, 222 atau 432 MHz: dipakai untuk penguatan dan lobus antena, perkiraan fluks dan anggaran link. |
| **Hitung** | Menghitung ulang lintasan (pengambilan sampel lapisan E: beberapa detik). |
| **Az antena** | Azimut antena Anda: selalu **ke arah DX** (azimut lintasan). |
| **Huruf** | Ukuran seluruh teks, 100–300 %. Lihat [Pengaturan](Settings-and-Data-Folder-id#huruf-dan-kontrol). |

**Baris 2 – lapisan E dan antena**

| Kontrol | Fungsinya |
|---|---|
| **Ketinggian jejak km** + **dari radar** | Ketinggian jejak meteor (bawaan 90 km). Jika *dari radar* dicentang, dipakai ketinggian yang paling sering (modus) yang diukur radar Collm; lihat [Fluks radar](Radar-Flux-id). |
| **Elevasi lobus °** | Elevasi terendah lobus antena Anda (0° = cakrawala). Hanya titik lapisan E yang terlihat oleh kedua stasiun di atas elevasi ini yang dipakai. |
| **Antena Yagi: boom m** | Panjang boom Yagi Anda. Program menampilkan panjangnya dalam λ, penguatan (kurva DL6WU) dan lobus −3 dB, horizontal dan vertikal; lihat [Geometri dan redaman](Geometry-and-Path-Loss-id#penguatan-dan-lobus-antena). Di bawah 2 λ perkiraannya kasar. |
| **Hot spot dari titik tengah km** | Jarak Hot A dan Hot B dari titik tengah, 30–400 km (bawaan 150 km, seperti AMS Bulletin 203 / W8WN / MSHV). |

**Baris 3 – waktu**

| Kontrol | Fungsinya |
|---|---|
| **Jam** | Jam UTC. |
| **Waktu perhitungan (±36 h)** | Menggeser saat perhitungan – [Perhitungan prakiraan](Sky-View-id) dan [Radar GRAVES](GRAVES-Radar-id) – hingga 36 jam ke belakang atau ke depan, dengan langkah 15 menit. Di sampingnya: *Perhitungan untuk: sekarang* atau *Perhitungan untuk: dd/mm hh:mm UTC*. |
| **Waktu nyata** | Kembali ke saat ini. |
| **Hari untuk tabel 24 jam (UTC)** | Hari yang ditampilkan di [Perhitungan efisiensi](Efficiency-Calculation-id) dan di kronologi GRAVES. |

## 2. Stasiun Anda dan DX

1. Isi **Locator saya** dan **ketinggian m**.
2. Isi locator dan ketinggian **Stasiun DX** – atau klik peta di [Kubah langit](Sky-View-id): **klik kiri = locator stasiun DX**, **klik kanan = locator stasiun saya**.
3. Pilih **Band MHz** lalu tekan **Hitung**.

Bilah status di bawah mengonfirmasi: *Lintasan dihitung: … km, … titik pantul disampel dalam … s*.

## 3. Antena Anda

Masukkan **panjang boom** Yagi Anda. Program menurunkan penguatan dan lobus, lalu memberi peringatan jika Hot A atau Hot B sudah jatuh **di dalam lobus** saat antena diarahkan ke DX (maka keduanya digambar abu-abu: antena tidak perlu diputar).

## 4. Membaca hasil

| Pertanyaan | Di mana melihatnya |
|---|---|
| Hujan meteor mana yang membantu lintasan saya sekarang, dan dari sisi mana? | [Kubah langit](Sky-View-id): daftar hujan meteor, Hot yang disarankan berwarna merah, zona PREV |
| Jam berapa yang terbaik hari ini? | [Perhitungan efisiensi](Efficiency-Calculation-id): kartu ringkas dan tabel per jam |
| Berapa meteor yang dihitung radar? | [Fluks radar](Radar-Flux-id) |
| Berapa ping yang bisa saya harapkan di 144 MHz? | [Prakiraan eksperimental](Experimental-Forecasts-id) (eksperimental) |
| Apakah stasiun saya sanggup menutup lintasan ini? | [Geometri dan redaman](Geometry-and-Path-Loss-id): redaman lintasan dan margin |
| Kapan puncak berikutnya? | [Hujan meteor](Showers-id) |
| Bisakah saya mencoba dengan GRAVES? | [Radar GRAVES](GRAVES-Radar-id) |

## Aturan praktis (dari sumber)

- **Arahkan tegak lurus terhadap hujan meteor**: lintasan terbaik tegak lurus terhadap azimut radian; arah terbaik = azimut radian ±90°, toleransi ±40–50° (SM6FHZ).
- **Side scatter**: putar antena 10–30° ke arah sisi (A atau B) dari mana sebagian besar pantulan datang (artikel Cerrotta–Sartori).
- **Radian terlalu tinggi** (di atas 70°) atau terlalu rendah (di bawah 20°) menghasilkan sedikit jejak yang berguna (DF5HC, DH9GCD).
- Meteor sporadis mencapai puncak sekitar **06 UTC** (artikel; dikonfirmasi oleh fluks Collm).
- Jarak berguna di 432 MHz: 800–2000 km, terbaik sekitar 1400 km (SM6FHZ); jarak terbaik secara umum 1300–1500 km (DF5HC).

Berikutnya: [Kubah langit](Sky-View-id).
