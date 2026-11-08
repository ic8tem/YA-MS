[English](Radar-Flux) · [Italiano](Radar-Flux-it) · [Deutsch](Radar-Flux-de) · [Nederlands](Radar-Flux-nl) · [Français](Radar-Flux-fr) · [Español](Radar-Flux-es) · [Português](Radar-Flux-pt) · [Dansk](Radar-Flux-da) · [Norsk](Radar-Flux-nb) · [Svenska](Radar-Flux-sv) · [Íslenska](Radar-Flux-is) · [Eesti](Radar-Flux-et) · [Lietuvių](Radar-Flux-lt) · [Latviešu](Radar-Flux-lv) · [Русский](Radar-Flux-ru) · [Українська](Radar-Flux-uk) · [Türkçe](Radar-Flux-tr) · [Afrikaans](Radar-Flux-af) · [العربية](Radar-Flux-ar) · [עברית](Radar-Flux-he) · [اردو](Radar-Flux-ur) · [हिन्दी](Radar-Flux-hi) · [বাংলা](Radar-Flux-bn) · **Bahasa Indonesia** · [Tagalog](Radar-Flux-tl) · [日本語](Radar-Flux-ja) · [한국어](Radar-Flux-ko) · [中文](Radar-Flux-zh)

# Fluks radar

*Tab: Langsung dan data waktu nyata › Fluks radar.*

[![Fluks radar](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_2.png)

Tab ini menampilkan apa yang sedang dihitung radar meteor profesional **saat ini**: hitungan meteor per jam dan ketinggian jejak dari radar SKiYMET **Collm** (Universitas Leipzig / IAP Kühlungsborn, Jerman, 36,2 MHz), serta gambar terbaru radar **Sodankylä** (SGO, Finlandia). Hitungan Collm menjadi masukan bagi perkiraan untuk band Anda dan [Prakiraan eksperimental](Experimental-Forecasts-id); ketinggian jejak yang terukur menjadi masukan bagi seluruh geometri.

## Kontrol

| Kontrol | Fungsinya |
|---|---|
| **Unduh sekarang** | Memeriksa semua sumber eksternal sekaligus. |
| **Pembaruan otomatis semua sumber setiap 5 menit** | Aktif secara bawaan. Setiap 5 menit semua sumber diperiksa dan **hanya yang berubah** diunduh ulang (*tidak berubah (diperiksa pada … UTC)* / *data baru pada … UTC*). |
| **Eksponen λ (SM6FHZ)** | Eksponen k dari aturan frekuensi, bawaan 3 (1–4). |

## Yang ditampilkan

| Panel | Isi |
|---|---|
| **Meteor/jam – kemarin dan hari ini (UTC)** | Batang sian = hitungan Collm (valid), batang merah = dibuang, garis oranye tebal = *perkiraan pada … MHz* pada skala kanan |
| **Ketinggian jejak (Collm)** | Meteor per km ketinggian antara 70 dan 110 km, dengan ketinggian paling sering (modus), rata-rata, median dan simpangan baku |
| Gambar Collm | Grafik SKiYMET asli, sebagaimana diunduh |
| Gambar Sodankylä | Gambar hitungan meteor terbaru dari radar Sodankylä (hanya ditampilkan; formatnya tidak dibaca) |

Baris di atas grafik menyebutkan kapan grafik Collm dibaca dan skala vertikal mana yang ditemukan (*skala terbaca dari grafik: 0-… meteor/jam*).

## Cara grafik Collm dibaca

Grafik Collm (720 × 720 piksel, warna murni) memiliki posisi sumbu yang tetap, tetapi radar **menyesuaikan skala vertikal setiap hari** dengan nilai yang terukur (mis. 0–1,2·10³ pada 5/11/2026 dan 0–1,0·10³ pada 6/11/2026, dengan tanda skala yang bergeser). Karena itu YA-MS:

1. mencari tanda skala panjang pada sumbu;
2. **membaca label** tanda skala tertinggi dan nol dengan membandingkan setiap karakter dengan font dot-matrix grafik;
3. untuk setiap jam i (0–47, kemarin dan hari ini) mengambil kolom tengah dan piksel sian pertama dari atas, y:

```
x_i = 101 + (i + 0.5)·(676 − 101)/48        N = (y0 − y)·N_top / (y0 − y_top)   meteors/hour
```

y_top dan y0 adalah baris tanda skala tertinggi dan nol, N_top nilai yang terbaca pada label tertinggi (×1000). Resolusi: sekitar 7–8 meteor/jam per piksel. *Pilihan program (manual pers. 42).*

Jika sebuah label tidak dapat dibaca, program kembali ke kalibrasi 5/11/2026 (**skala terkalibrasi 0-1200 meteor/jam**) dan menyatakannya dengan warna oranye: *Tidak dapat membaca skala vertikal fluks (label atas: …): nilai perlu diperiksa.* Jika format grafiknya sendiri berubah (*Format grafik berubah (…x…): tidak dapat dibaca.* atau *Sumbu fluks tidak ditemukan pada posisi yang diharapkan.*), pembacaan harus dikalibrasi ulang: mohon laporkan (lihat [Berkontribusi](Contributing-and-Contacts-id)).

### Ketinggian jejak

Dari histogram ketinggian (n_k meteor pada km ke-k, ketinggian rata-rata h_k):

```
h_mode = h_k*  with k* = argmax n_k      mean = Σ n_k·h_k / Σ n_k      s = sqrt( Σ n_k·(h_k − mean)² / Σ n_k )
```

*Manual pers. 43.* Dengan **dari radar** dicentang (baris 2 kontrol), **modus** menjadi ketinggian jejak untuk semua perhitungan. Verifikasi: grafik 5/11/2026 – modus 89,5 km, rata-rata 88,6 km, simpangan baku 6,8 km, mengonfirmasi ~90 km dalam artikel Cerrotta–Sartori (rata-rata SKiYMET).

Jika skala grafik ketinggian berubah, program memperingatkan: *statistik ketinggian (modus, rata-rata, median) tetap valid, hitungan absolut tidak.*

## Perkiraan untuk band Anda

```
meteors/hour at f = Collm(36.2 MHz) · (36.2 / f)^k          ping duration · (36.2 / f)²          k = 3
```

Aturan eksperimental dari **SM6FHZ** (VUSHF 2025): jumlah dan intensitas pantulan berskala dengan λ³, durasinya dengan λ²; ketergantungan λ³ sama dengan pada persamaan underdense McKinley. Durasi ping maksimum IARU Region 1 juga ditampilkan (1000 ms di 50 MHz, 500 ms di 70 MHz, 100 ms di 144 MHz, 13 ms di 432 MHz). Nilai-nilai ini bersifat indikatif, untuk dibandingkan dengan pengalaman di udara. Faktor stasiun K dan perbandingan dengan RMOB ada di [Prakiraan eksperimental](Experimental-Forecasts-id).

## Tanpa koneksi

Jika tidak ada sumber yang dapat dijangkau, sebuah pesan muncul **sekali**: *Tidak ada koneksi internet. Data radar dan RMOB tidak dapat diperbarui: program memakai data terakhir yang tersimpan dan mencoba lagi sendiri setiap 5 menit.* Bilah status di bawah berubah merah (*TIDAK ADA KONEKSI INTERNET …*) sampai koneksi kembali (*Koneksi pulih.*).

## Arsip dan sumber

| File (di `data/`) | Isi |
|---|---|
| `flusso_collm.csv` | Arsip per jam fluks yang dibaca dari Collm (jam yang sudah ada diperbarui) |
| `quote_collm.csv` | Arsip ketinggian jejak |
| `radar/` | Gambar terakhir yang diunduh (dan file RMOB) |
| `fonti_radar.csv` | Alamat sumber radar, `attivo=1/0` untuk mengaktifkan/menonaktifkan masing-masing |

| Sumber | Frekuensi | Catatan |
|---|---|---|
| Radar meteor Collm, Universitas Leipzig (LIM) dan IAP Kühlungsborn – wetterdaten.meteo.uni-leipzig.de/radar_flux.php | 36,2 MHz | diperbarui setiap jam pada menit ke-10 UTC; fluks kemarin + hari ini, distribusi ketinggian |
| Sodankylä Geophysical Observatory – sgo.fi/Data/RealTime/meteorRadar.php | 36,9 MHz | hanya gambar (radar sedang diperbarui, proyek DECC) |
| swan.ms (salinan Collm) | 36,2 MHz | nonaktif secara bawaan; gunakan hanya dengan izin DL1DBC |

> Data radar adalah milik lembaga masing-masing (Universitas Leipzig / IAP Kühlungsborn, Sodankylä Geophysical Observatory).
