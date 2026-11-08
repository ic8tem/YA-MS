[English](Geometry-and-Path-Loss) · [Italiano](Geometry-and-Path-Loss-it) · [Deutsch](Geometry-and-Path-Loss-de) · [Nederlands](Geometry-and-Path-Loss-nl) · [Français](Geometry-and-Path-Loss-fr) · [Español](Geometry-and-Path-Loss-es) · [Português](Geometry-and-Path-Loss-pt) · [Dansk](Geometry-and-Path-Loss-da) · [Norsk](Geometry-and-Path-Loss-nb) · [Svenska](Geometry-and-Path-Loss-sv) · [Íslenska](Geometry-and-Path-Loss-is) · [Eesti](Geometry-and-Path-Loss-et) · [Lietuvių](Geometry-and-Path-Loss-lt) · [Latviešu](Geometry-and-Path-Loss-lv) · [Русский](Geometry-and-Path-Loss-ru) · [Українська](Geometry-and-Path-Loss-uk) · [Türkçe](Geometry-and-Path-Loss-tr) · [Afrikaans](Geometry-and-Path-Loss-af) · [العربية](Geometry-and-Path-Loss-ar) · [עברית](Geometry-and-Path-Loss-he) · [اردو](Geometry-and-Path-Loss-ur) · [हिन्दी](Geometry-and-Path-Loss-hi) · [বাংলা](Geometry-and-Path-Loss-bn) · **Bahasa Indonesia** · [Tagalog](Geometry-and-Path-Loss-tl) · [日本語](Geometry-and-Path-Loss-ja) · [한국어](Geometry-and-Path-Loss-ko) · [中文](Geometry-and-Path-Loss-zh)

# Geometri dan redaman

*Tab: Perhitungan prakiraan › Geometri dan redaman.*

[![Geometri dan redaman](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_2.png)

Laporan teks tentang lintasan (dapat diseleksi, sehingga bisa Anda salin) dan, di sebelah kanan, grafik **Elevasi antena terhadap jarak dari scatter point**. Angka dalam kurung siku merujuk ke persamaan dalam manual perhitungan (`doc/YA-MS_manuale_calcoli.docx`).

## Masukan pada tab ini

| Isian | Bawaan | Kegunaan |
|---|---|---|
| **Daya W** | 400 | Daya pemancar untuk anggaran link |
| **Penguatan antena dBi (tx = rx)** | 14 | Antena yang sama di kedua ujung |
| **Sinyal minimum dBm** | −130 | Sinyal minimum yang dapat dideteksi (artikel: Yagi 8 elemen + preamp) |
| **Kerapatan jejak q = 10^ … elektron/m** | 14 | Kerapatan elektron linear jejak underdense |

Stasiun, band, ketinggian jejak, elevasi lobus, boom dan jarak hot spot diambil dari [baris kontrol](Getting-Started-id#1-tiga-baris-kontrol).

## Bagian-bagian laporan

| Bagian | Isi |
|---|---|
| **GEOMETRI LINTASAN (Bumi bulat, R = 6372,7955 km)** | Stasiun dan DX dengan ketinggiannya; jarak, azimut dan azimut balik; titik tengah (locator dan koordinat); ketinggian jejak (*<- modus terukur oleh radar Collm* bila diambil dari radar); elevasi antena ke arah titik tengah |
| **HOT A / HOT B (hot spot klasik, untuk mengarahkan antena)** | Untuk masing-masing: locator, azimut dari Anda dan offset dari lintasan langsung, azimut dari DX, jarak, elevasi |
| **BATAS ZONA BERSAMA** | Jangkauan pada ketinggian jejak dengan elevasi lobus; Batas A / Batas B dengan azimutnya |
| Antena | Boom dalam λ, penguatan, lobus horizontal / vertikal; apakah Hot A dan Hot B di dalam atau di luar lobus |
| **REDAMAN LINTASAN (jejak underdense, McKinley 1961; tanpa penguatan antena)** | Tabel untuk titik tengah (forward), Hot A dan Hot B pada 28, 50, 70, 144, 222 dan 432 MHz |
| **ANGGARAN LINK PADA … MHz (titik tengah)** | Daya dan EIRP, redaman lintasan, sinyal di antena, minimum terdeteksi, **margin**; margin yang sama dengan redaman rata-rata OH5IY |
| **ATURAN EKSPERIMENTAL ANTARBAND (SM6FHZ, VUSHF 2025)** | Jumlah/intensitas dan durasi dibandingkan dengan 144 MHz; ping maksimum IARU |

## Locator dan lintasan

Locator (4, 6 atau 8 karakter; pusat kotak, sistem Maidenhead IARU) [14]. Jarak, azimut dan titik tengah dengan rumus lingkaran besar pada bola berjari-jari **r = 6372,7955 km** (artikel Cerrotta–Sartori) [15–16]. Perhitungan yang bergantung waktu mengacu pada **titik tengah**, karena jam terbaik dapat berbeda hingga 1,5 jam antara kedua ujung (SM6FHZ).

## Elevasi antena

**Sumber:** rumus dari artikel Cerrotta–Sartori (Gambar 7), dengan x = d/r, d jarak permukaan ke titik pantul, H ketinggian jejak dan h ketinggian stasiun [17]:

```
e = 90° − 57.3 · arctan[ ( r·tan x + (H − r(1 − cos x)/cos x)·sin x ) / ( H − r(1 − cos x)/cos x − h·sin x ) ]
```

**Verifikasi:** cocok dengan geometri bola eksak dalam 0,03°. Program memakai arktangen dua argumen, yang memberikan nilai negatif di luar cakrawala dan menghindari masalah periodisitas yang disebut dalam artikel. Elevasi negatif ke arah titik tengah berarti *lintasan melebihi jangkauan geometris satu lompatan*.

## Jangkauan cakrawala

Jarak permukaan tempat sinar dengan elevasi e mencapai ketinggian H (invers geometris dari rumus di atas) [18]:

```
d_H = r · [ π/2 − e − arcsin( (r + h)·cos e / (r + H) ) ]
```

**Verifikasi:** H = 89,5 km, e = 0° → **1062 km**. Pada contoh dalam artikel (JN44BB–IO53RT) gambar menempatkan perpotongan cakrawala sekitar 870 km dari stasiun, yang sesuai dengan lobus yang dinaikkan sekitar 2° (865 km).

## Batas zona bersama

**Sumber:** artikel menentukan perpotongan kurva tempat cakrawala tiap stasiun bertemu lapisan E: perpotongan dua lingkaran berjari-jari sudut ρ = d_H/r yang berpusat di A dan B [19–20]:

```
p0 = cos ρ / (1 + û_A·û_B) · (û_A + û_B)
p_A,B = p0 ± sqrt( (1 − |p0|²) / |û_A × û_B|² ) · (û_A × û_B)
```

Jika 1 − |p0|² < 0, lintasan lebih panjang dari 2·d_H dan kedua stasiun **tidak melihat zona bersama lapisan E**.

**Verifikasi:** ini adalah **tepi terjauh** langit yang terlihat oleh kedua stasiun, **bukan titik untuk dibidik**. Pada JN70CN–IN78UO (1710 km, azimut 308°) titik-titik ini jatuh 1062 km dari stasiun, 37° di kiri dan kanan lintasan langsung, sedangkan MSHV menyarankan 10°. Karena itu keduanya disebut *Batas A* / *Batas B* dan digambar samar di peta.

## Hot A dan Hot B

**Sumber:** pantulan terkonsentrasi di dua zona ("hot spot") sekitar **50–150 km di kedua sisi titik tengah**. Inilah dasar tabel offset antena dalam AMS Bulletin No. 203, yang diambil oleh W8WN (offset 10° untuk lintasan 1500 dan 1800 km); MSHV karya LZ2HV memakai kriteria yang sama.

**Pilihan:** Hot A dan Hot B adalah titik pada jarak s dari titik tengah M, tegak lurus terhadap lintasan (s = 150 km, dapat diatur 30–400 km); A di kiri jika melihat dari stasiun Anda ke DX, B di kanan [21]. Offset yang terlihat dari stasiun kira-kira [22]:

```
ΔAz_hot ≈ arctan( s / (D/2) )
```

**Verifikasi:** JN70CN–IN78UO, D = 1710 km: 6,7° dengan s = 100 km, **10,0° dengan s = 150 km** (sama dengan MSHV dan AMS/W8WN), 13,2° dengan s = 200 km.

## Redaman lintasan underdense

**Sumber:** persamaan McKinley untuk jejak underdense (β = 0, sin α = 1), tanpa penguatan antena; q = kerapatan elektron linear, r_e = jari-jari elektron klasik = 2,818·10⁻¹⁵ m, R1, R2 jarak ke jejak, φ setengah sudut hambur [36]:

```
L = 10·log10[ 16·π²·R1·R2·(R1 + R2)·cos²φ / ( λ³·q²·r_e² ) ]   dB
```

**Verifikasi:** dengan q = 10¹⁴ elektron/m pada 144 MHz: **181–192 dB** antara 600 dan 2200 km, sejalan dengan referensi artikel pada 144 MHz: **minimum 182 dB** (GM8JBJ, dari Kaiser & Closs 1952) dan **rata-rata 200 dB** (OH5IY).

## Anggaran link

```
P_rx = P_tx(dBm) + G_tx − 2.15 − L + G_rx − 2.15        margin = P_rx − P_min,   P_min = −130 dBm
```

[37–38]. Penguatan dimasukkan dalam dBi dan dipakai dalam dBd (dBi − 2,15). Laporan juga memberikan margin dengan **redaman rata-rata OH5IY** (200 dB pada 144 MHz, diskalakan dengan λ³ ke band yang dipilih). Referensi artikel: diperlukan sekitar **70 dBm EIRP** (−130 dBm + 200 dB, mis. sekitar 400 W ke antena 14 dBi).

## Penguatan dan lobus antena

**Penguatan – sumber:** kurva Günter Hoch **DL6WU** untuk Yagi panjang sebagai fungsi panjang boom L, dilaporkan oleh W8IO (berlaku mulai sekitar 2 λ) [39]:

```
G = 7.773 · log10(L/λ) + 11.43   dBi
```

**Verifikasi terhadap model NEC L.B. Cebik W4RNL pada 432 MHz** (*Appreciating DL6WU Wide-Band Long-Boom Yagi Design*; *70-CM Yagi Stacks Part 2*):

| Yagi | Elemen | Boom (λ) | W4RNL NEC (dBi) | Rumus (dBi) |
|---|---|---|---|---|
| DL6WU | 13 / 22 / 31 | 3,23 / 6,82 / 10,42 | 15,28 / 17,82 / 19,35 | 15,38 / 17,91 / 19,34 |
| VK3AUU (David Tanner) | 16 / 28 / 40 | 3,12 / 6,88 / 10,79 | 15,17 / 17,91 / 19,46 | 15,27 / 17,94 / 19,45 |

Selisihnya tidak pernah melebihi **0,1 dB**: penguatan lebih bergantung pada panjang boom daripada desainnya (Yagi VK3AUU memiliki boom lebih pendek untuk jumlah elemen yang sama). Yagi Calculator karya VK5DJ juga memberikan perkiraan untuk varian VK3AUU, WA2PHW dan DJ9BV, yang rumusnya tidak dipublikasikan.

**Lobus – sumber:** aturan Kraus, dengan lobus melingkar θE = θH = θK [40]:

```
G_lin = 41253 / (θE · θH)   ⇒   θK = sqrt( 41253 / 10^(G/10) )
```

**Verifikasi:** model NEC W4RNL untuk Yagi DL6WU memberikan **lobus horizontal 5–10 % lebih sempit** daripada Kraus: 33,8° / 26,4° / 22,6° untuk 12, 19 dan 26 elemen, dibandingkan 37,3° / 28,0° / 23,9°. Rumus sederhana mengabaikan lobus samping depan (W4RNL, *Long-Boom Yagi Rules of Thumb*). Pada boom panjang lobus vertikal sedikit lebih lebar daripada horizontal (14 λ: 18,4° / 18,8°).

**Pilihan** [41]:

```
θ_horizontal = 0.93 · θK        θ_vertical = θK
```

Contoh: Yagi 14 λ pada 432 MHz → 20,3 dBi, lobus 18,1° horizontal dan 19,5° vertikal; model W4RNL memberikan 20,4 dBi dan 18,4° / 18,8°. Ini adalah aturan perkiraan yang diturunkan dari beberapa antena DL6WU.

Antena selalu dianggap diarahkan ke DX. Sebuah hot spot berada **di dalam lobus** jika |Az(Hot) − Az(antena)| ≤ θ_horizontal/2: maka hot spot itu digambar abu-abu pada [Kubah langit](Sky-View-id) dan muncul peringatan. Dalam perhitungan efisiensi antena dianggap isotropik; lobus nyata hanya dipakai untuk pemeriksaan ini.

## Aturan eksperimental antarband

Dibandingkan dengan 144 MHz: jumlah/intensitas × (144/f)³ (dalam dB), durasi × (144/f)² (SM6FHZ, VUSHF 2025). Durasi ping maksimum IARU Region 1: 1000 ms di 50 MHz, 500 ms di 70 MHz, 100 ms di 144 MHz, 13 ms di 432 MHz (VHF Handbook, dikutip dalam artikel). Lihat juga [Prakiraan eksperimental](Experimental-Forecasts-id).
