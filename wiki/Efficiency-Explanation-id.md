[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · [Türkçe](Efficiency-Explanation-tr) · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · **Bahasa Indonesia** · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh)

# Efisiensi - penjelasan

*Tab: Dokumen teknis › Efisiensi - penjelasan.*

[![Efisiensi - penjelasan](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Sebuah dokumen teknis, *"Come YA-MS calcola l'efficienza di uno sciame"* (Cara YA-MS menghitung efisiensi sebuah hujan meteor), yang ditampilkan di dalam program sebagai halaman terang. Dokumen ini menjelaskan **langkah demi langkah** bagaimana efisiensi diperoleh, dan untuk setiap langkah menyebutkan **asal-usulnya**. Saat ini dokumen tersebut **berbahasa Italia**; wiki ini menyajikan isinya dalam bahasa Indonesia di [Perhitungan efisiensi](Efficiency-Calculation-id#model) dan [Geometri dan redaman](Geometry-and-Path-Loss-id).

## Label

Setiap langkah membawa label berwarna:

| Label | Warna | Arti |
|---|---|---|
| **FONTE** (sumber) | biru | langkah ini mengambil sumber yang dikutip; angka dalam kurung merujuk ke daftar di bagian akhir |
| **RILIEVO** (verifikasi) | hijau | perbandingan antara program dan sumber, beserta hasilnya |
| **SCELTA** (pilihan) | oranye | pilihan program, tidak diambil dari sumber: perlu diperiksa dengan pengalaman di udara |

## Bab

| Bab | Isi |
|---|---|
| 1. Pendahuluan | Tujuan, label, arti efisiensi (OH5IY, MCG_MS; YA-MS memakai lintasan nyata) |
| 2. Di mana pantulan terjadi: lapisan E | Jejak pada 80–120 km; ketinggian jejak = modus histogram Collm (verifikasi: 89,5 km pada 5/11/2026) |
| 3. Geometri lintasan | Bumi dan titik tengah; elevasi antena (rumus artikel); zona bersama dan batas-batasnya; Hot A / Hot B; lobus antena (DL6WU, Kraus, W4RNL) |
| 4. Radian hujan meteor | Posisi radian (IMO 2026/2027), tanggal puncak (IMO atau bujur matahari), profil aktivitas |
| 5. Syarat pantulan | Pantulan spekular (McKinley), toleransi Gauss 0,05 rad, arah terbaik (SM6FHZ), rumus DH9GCD |
| 6. Dari satu titik ke efisiensi | Titik pantul setiap 15 km, bobot setiap titik, persentase; perbandingan dengan QTFGUI (DJ5HG) |
| 7. Membaca hasil | Sisi A / B, indeks lintasan, warna radian, zona PREV, penampang dilihat dari antena |
| 8. Frekuensi kerja dan redaman lintasan | Aturan λ³ / λ², dari radar ke band amatir, referensi redaman lintasan |
| 9. Batasan yang diketahui | Hanya jejak underdense, antena isotropik, nilai kerja |
| 10. Sumber | 17 sumber bernomor |

## Tombol

| Tombol | Fungsinya |
|---|---|
| **Ekspor ke Word (.docx)...** | Menyimpan salinan `data/efficienza_spiegazione.docx` di tempat yang Anda pilih (nama yang disarankan *YA-MS - calcolo dell'efficienza.docx*) |
| **Buka di Word** | Membuka `.docx` yang sama dengan program bawaan untuk dokumen Word (Word, LibreOffice, …) |

## File

| File | Isi |
|---|---|
| `data/efficienza_spiegazione.txt` | Teks yang ditampilkan di tab, satu blok per baris (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Versi Word |
| `doc/YA-MS_manuale_calcoli.docx` | **Manual perhitungan**: semua persamaan (editor persamaan Word), bernomor, beserta sumbernya |

Kedua dokumen dibuat ulang dari kode sumber dengan `tools/build_spiegazione.py data` dan `node tools/build_manuale.js doc/YA-MS_manuale_calcoli.docx`.
