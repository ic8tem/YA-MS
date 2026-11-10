[English](Experimental-Forecasts) · [Italiano](Experimental-Forecasts-it) · [Deutsch](Experimental-Forecasts-de) · [Nederlands](Experimental-Forecasts-nl) · [Français](Experimental-Forecasts-fr) · [Español](Experimental-Forecasts-es) · [Português](Experimental-Forecasts-pt) · [Português (Brasil)](Experimental-Forecasts-pt-br) · [Dansk](Experimental-Forecasts-da) · [Norsk](Experimental-Forecasts-nb) · [Svenska](Experimental-Forecasts-sv) · [Íslenska](Experimental-Forecasts-is) · [Eesti](Experimental-Forecasts-et) · [Lietuvių](Experimental-Forecasts-lt) · [Latviešu](Experimental-Forecasts-lv) · [Polski](Experimental-Forecasts-pl) · [Čeština](Experimental-Forecasts-cs) · [Magyar](Experimental-Forecasts-hu) · [Română](Experimental-Forecasts-ro) · [Ελληνικά](Experimental-Forecasts-el) · [Русский](Experimental-Forecasts-ru) · [Українська](Experimental-Forecasts-uk) · [Türkçe](Experimental-Forecasts-tr) · [Afrikaans](Experimental-Forecasts-af) · [العربية](Experimental-Forecasts-ar) · [עברית](Experimental-Forecasts-he) · [اردو](Experimental-Forecasts-ur) · [हिन्दी](Experimental-Forecasts-hi) · [বাংলা](Experimental-Forecasts-bn) · [ไทย](Experimental-Forecasts-th) · **Bahasa Indonesia** · [Tagalog](Experimental-Forecasts-tl) · [日本語](Experimental-Forecasts-ja) · [한국어](Experimental-Forecasts-ko) · [中文](Experimental-Forecasts-zh) · [中文 (繁體)](Experimental-Forecasts-zh-tw)

# Prakiraan eksperimental

*Tab: Perhitungan prakiraan › Prakiraan eksperimental.*

[![Prakiraan eksperimental](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_4.png)

Tab ini mengubah hitungan meteor **radar Collm (36,2 MHz)** menjadi perkiraan **pantulan per jam pada band amatir** (bawaan 144 MHz, frekuensi apa pun dari 28 hingga 1300 MHz), memprakirakan **24 jam ke depan** untuk lintasan Anda, dan memungkinkan Anda **membandingkan** perkiraan itu dengan seorang pengamat **RMOB** – misalnya yang mendengarkan GRAVES di 143,050 MHz.

> Semua yang ada di sini bersifat **eksperimental**: aturan frekuensinya adalah aturan empiris, dan faktor stasiun bergantung pada stasiun Anda. Gunakan angka-angka ini untuk membandingkan jam dan hari, lalu periksa di udara.

## Kontrol

| Kontrol | Bawaan | Fungsinya |
|---|---|---|
| **Frekuensi tujuan MHz** | 144 | Frekuensi prakiraan (28–1300 MHz) |
| **Eksponen λ^k** | 3 | Eksponen k dari aturan frekuensi (SM6FHZ: 3) |
| **Faktor stasiun K** | 1 | Memperhitungkan stasiun penerima (daya, antena); diperoleh dengan membandingkan dengan pengamat RMOB pada band yang sama |
| **Muat file RMOB dari disk...** | | Membaca file teks RMOB bulanan (lihat di bawah) |
| **Turunkan eksponen dari file RMOB** | | Mencocokkan k dari jam-jam yang sama antara Collm dan RMOB |
| **Pengamat RMOB** | kosong | Nama pengamat seperti tertulis pada nama file (mis. `NAME_112026rmob.TXT` → `NAME`) |
| **Unduh RMOB sekarang** | | Mengunduh sekali file bulan berjalan dari pengamat tersebut |
| **pengambilan otomatis setiap 5 menit (aktifkan hanya dengan izin RMOB)** | **mati** | Lihat [RMOB dan program otomatis](#rmob-dan-program-otomatis) |

Baris oranye di bawah kontrol menampilkan aturan dengan angka saat ini, mis. *N(144 MHz) = N(Collm 36.2 MHz) x (36.2/144)^3.00 x K = N x 0.01589 x 1.00*, skala durasi dan ping maksimum IARU pada frekuensi tersebut.

## Dari radar ke band amatir

```math
N(f) = N(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{k} K,\quad k = 3,\qquad \tau(f) = \tau(36{.}2\ \mathrm{MHz})\left(\frac{36{.}2}{f}\right)^{2}\sec^2\varphi
```

**Sumber:** SM6FHZ, *"432 MHz Meteorscatter, Challenges and Techniques"*, Nordic VUSHF ke-45, Mei 2025 – jumlah dan intensitas pantulan berskala dengan **λ³**, durasinya dengan **λ²** (432 MHz berada 14–15 dB di bawah 144 MHz dan berlangsung 1/9-nya). **Verifikasi:** dalam persamaan McKinley, λ³ adalah daya satu jejak underdense, bukan jumlah jejak; untuk indeks massa 2, jumlah jejak di atas ambang tetap berskala kira-kira dengan λ^1,5 (IZ5TEK; OH5IY). Program mempertahankan k = 3, aturan eksperimental SM6FHZ, dan menyatakannya; k yang tepat untuk stasiun Anda diperoleh dari perbandingan dengan RMOB. Pada hamburan maju, durasi juga bertambah dengan sec²φ (McKinley; OH5IY): Collm mengukur dalam hamburan balik (φ = 0), sehingga prakiraan dikalikan dengan sec²φ di titik tengah lintasan (×4 pada 60°, ×8,5 pada 70°, ×33 pada 80°). Dengan k = 3, 1000 meteor/jam di Collm menjadi sekitar **16 pantulan/jam di 144 MHz**; pengamat RMOB untuk GRAVES di 143,050 MHz biasanya menghitung **20 sampai 140 gema/jam** (buletin RMOB, Juni 2018): orde besarnya cocok, dan selisihnya adalah faktor stasiun K. (Manual pers. 44–45.)

## 24 jam ke depan

```math
N_{prev}(t) = N(f,\ t-24\,\mathrm{h})\,\frac{I(t)+10}{I(t-24\,\mathrm{h})+10}
```

**Persistensi:** nilai terskala dari jam yang sama pada hari sebelumnya (atau dua hari sebelumnya jika tidak ada), dikoreksi dengan perubahan **indeks hujan meteor lintasan** I (Σ ZHR × efisiensi, lihat [Perhitungan efisiensi](Efficiency-Calculation-id#model)). Konstanta 10 mewakili latar sporadis dan membatasi koreksi saat indeksnya kecil. *Pilihan program (manual pers. 47).*

| Panel | Isi |
|---|---|
| **Diukur di Collm dan diskalakan ke f MHz – kemarin dan hari ini (UTC)** | Meteor/jam radar Collm; nilai terskala (oranye, skala kanan); hitungan RMOB jika dimuat (hijau, skala kanan) |
| **Prakiraan eksperimental 24 jam ke depan pada f MHz untuk …** | Prakiraan pantulan/jam (batang) dan indeks hujan meteor lintasan (skala kanan) |
| Tabel | Jam UTC · Collm jam yang sama · Diskalakan · Indeks hujan meteor lintasan · Prakiraan /jam · **Penilaian** |

**Penilaian:** *baik* jika prakiraan paling sedikit 1,3 × rata-rata 24 jam, *sedang* mulai 0,8 ×, *buruk* di bawahnya. Prakiraan yang sama muncul di kartu **PRAKIRAAN EKSPERIMENTAL** dan di baris oranye [Perhitungan efisiensi](Efficiency-Calculation-id), dan menjadi dasar gema yang diharapkan di tab [Radar GRAVES](GRAVES-Radar-id#gema-yang-diharapkan-eksperimental).

## Perbandingan RMOB

[RMOB](https://www.rmob.org) (Radio Meteor Observatories On Line, Pierre Terrier) mengumpulkan hitungan meteor per jam dari para pengamat radio; banyak di Italia yang mendengarkan GRAVES di 143,050 MHz (Planetarium Venesia, Faenza, Rovereto dan lainnya).

**Membaca file RMOB.** Dua format teks diterima:

| Format | Tampilan | Catatan |
|---|---|---|
| File bulanan (Colorgramme / Spectrum Lab) | satu baris per hari, `day| n| n| …` dengan 24 nilai per jam | `NAME_MMYYYYrmob.TXT` yang biasa |
| Tabel buletin | header ` UT |  1   2   3 …`, baris `0h|175 166 …` | jika file berisi beberapa pengamat, semuanya dibaca berurutan: gunakan file dengan satu pengamat saja |

Bulan dan tahun diambil dari nama file (`…_MMYYYYrmob…`) atau dari header; jika tidak, dipakai bulan berjalan (dan program menyatakannya).

**Mencocokkan eksponen.** Dengan K = 1, dari median rasio RMOB/Collm pada jam-jam yang sama (paling sedikit 3):

```math
k_{emp} = -\frac{\ln\left(\mathrm{median}\,(N_{RMOB}/N_{Collm})\right)}{\ln(f/36{.}2)}
```

*Pilihan program (manual pers. 46).* Dialog menampilkan jam-jam yang sama, rasio median dan k; **Ya** menerapkan k (dan menetapkan K = 1), **Tidak** mempertahankan k = 3 – lalu sesuaikan K secara manual ke nilai yang disarankan dalam dialog yang sama.

## RMOB dan program otomatis

RMOB meminta agar **program otomatis tidak mengambil file-filenya**. Karena itu **pengambilan otomatis mati** saat awal dan sebaiknya diaktifkan **hanya setelah meminta izin RMOB**. Tanpa izin itu Anda selalu dapat memakai **Muat file RMOB dari disk...** atau menekan **Unduh RMOB sekarang** saat diperlukan.

Alamat unduhan adalah templat di `config.ini` (kunci `rmob_url`, bawaan `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT`, dengan `{NOME}` nama pengamat dan `{MMAAAA}` bulan dan tahun); file yang diunduh disimpan di `data/radar/`.
