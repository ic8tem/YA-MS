[English](Home) · [Italiano](Home-it) · [Deutsch](Home-de) · [Nederlands](Home-nl) · [Français](Home-fr) · [Español](Home-es) · [Português](Home-pt) · [Português (Brasil)](Home-pt-br) · [Dansk](Home-da) · [Norsk](Home-nb) · [Svenska](Home-sv) · [Íslenska](Home-is) · [Eesti](Home-et) · [Lietuvių](Home-lt) · [Latviešu](Home-lv) · [Polski](Home-pl) · [Čeština](Home-cs) · [Magyar](Home-hu) · [Română](Home-ro) · [Ελληνικά](Home-el) · [Русский](Home-ru) · [Українська](Home-uk) · [Türkçe](Home-tr) · [Afrikaans](Home-af) · [العربية](Home-ar) · [עברית](Home-he) · [اردو](Home-ur) · [हिन्दी](Home-hi) · [বাংলা](Home-bn) · [ไทย](Home-th) · **Bahasa Indonesia** · [Tagalog](Home-tl) · [日本語](Home-ja) · [한국어](Home-ko) · [中文](Home-zh) · [中文 (繁體)](Home-zh-tw)

# YA-MS – prakiraan meteor scatter dan efisiensi hujan meteor secara langsung

*disusun oleh Costantino Cerrotta IC8TEM*

**YA-MS** adalah program gratis untuk radio amatir yang bekerja **meteor scatter (MS) di 50, 70, 144, 222 dan 432 MHz**. Untuk lintasan nyata antara locator Anda dan locator stasiun DX, program ini menghitung jam demi jam seberapa besar setiap hujan meteor aktif membantu lintasan (**efisiensi**-nya), dari sisi lintasan mana pantulan datang (**Hot A / Hot B**), ke mana antena diarahkan, serta prakiraan eksperimental jumlah pantulan per jam yang diturunkan dari **radar meteor langsung** (Collm, Jerman). Program berjalan di **Windows, Linux, Raspberry Pi dan macOS** (.NET 8 + Avalonia), dalam 36 bahasa antarmuka.

Sumber utamanya adalah artikel **C. Cerrotta IC8TEM dan G. Sartori IV3GTH**, *"METEOR-SCATTER. Ovvero come collegare l'Europa in VHF tutto l'anno senza tante pretese"* (versi 7). Setiap rumus dan data dalam program menyebutkan sumbernya; lihat [Sumber](Sources-id).

<table><tr>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png" alt="Kubah langit"></a><br><sub>Kubah langit</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png" alt="Perhitungan efisiensi"></a><br><sub>Perhitungan efisiensi</sub></td>
<td width="33%" align="center"><a href="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png"><img src="https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png" alt="Radar GRAVES"></a><br><sub>Radar GRAVES</sub></td>
</tr></table>

## Untuk siapa

- Operator yang ingin tahu **kapan** sebuah lintasan meteor scatter terbuka dan **ke mana** antena diarahkan, lebih dari sekadar "puncak hujan meteor nanti malam".
- Stasiun yang bekerja di **lintasan panjang pada 144 dan 432 MHz**, di mana posisi radian menentukan apakah sebuah hujan meteor berguna atau tidak.
- Siapa pun yang ingin **memeriksa angka-angkanya**: manual perhitungan dan penjelasan di dalam program memberikan setiap langkah beserta asalnya: sumber yang dipublikasikan, verifikasi yang dilakukan pada program, atau pilihan program.

## Tab-tab

Sejak versi 1.6 tab utama memiliki **sub-tab** (baris yang lebih terang di bawah baris utama). Saat mulai, layar pembuka selama 5 detik menampilkan Perseid di atas VLT milik ESO (foto ESO/S. Guisard, CC BY 4.0).

| Tab | Sub-tab | Yang ditampilkan |
|---|---|---|
| **Langsung dan data waktu nyata** | [Lalu lintas langsung](Live-Traffic-id) | Peta azimutal seluruh lalu lintas MS yang terkumpul, dengan awan jejak paling mungkin untuk setiap kontak, warna per band, berkedip saat koresponden membalas Anda |
| | [Fluks radar](Radar-Flux-id) | Hitungan meteor per jam dan ketinggian jejak yang dibaca dari radar SKiYMET Collm, gambar Sodankylä, perkiraan untuk band Anda |
| | [Radar GRAVES](GRAVES-Radar-id) | Lintasan forward scatter GRAVES → Anda: zona berguna dalam berkas, sektor dan langkah, lintasan berkas berikutnya, cara mendengarkan |
| | [Pengumpulan data](Data-Collection-id) | Tiga aliran cluster telnet (DX cluster, RBN, DM4X/PSKReporter) dan filter spot MS |
| **Perhitungan prakiraan** | [Perhitungan prakiraan](Sky-View-id) | Peta denah lintasan dengan Hot A / Hot B, lobus antena, zona PREV dan pergeseran hujan meteor; daftar hujan meteor; kubah langit kecil dengan radian dan arah antena yang tepat; penampang dilihat dari antena |
| | [Geometri dan redaman](Geometry-and-Path-Loss-id) | Jarak, titik tengah, elevasi, Hot A / Hot B, batas zona bersama, redaman lintasan 28–432 MHz, anggaran link, antena |
| | [Perhitungan efisiensi](Efficiency-Calculation-id) | Kartu ringkas, efisiensi per jam setiap hujan meteor dengan sisi A/B, indeks lintasan, perbandingan DH9GCD, grafik |
| | [Prakiraan eksperimental](Experimental-Forecasts-id) | Fluks Collm diskalakan ke 144 MHz (atau frekuensi apa pun) dengan λ^k dan faktor stasiun K, prakiraan 24 jam, perbandingan RMOB |
| [Hujan meteor langsung](Live-Showers-id) | – | ZHR terukur dari Global Meteor Network dan peta radian CMOR |
| [Hujan meteor](Showers-id) | – | Katalog IMO dengan puncak berikutnya (tanggal dan jam IMO atau hasil hitungan) |
| [Peta kotak](Grid-Square-Map-id) | – | Kotak Maidenhead yang sudah dikerjakan dan terkonfirmasi dari file ADIF, satu tab per band |
| **Dokumen teknis** | [Sumber](Sources-id) | Semua sumber; yang utama adalah artikel Cerrotta–Sartori |
| | [Peta radar Eropa](European-Radar-Map-id) | Letak Collm, Sodankylä, GRAVES dan CMOR relatif terhadap stasiun Anda |
| | [Penjelasan perhitungan efisiensi](Efficiency-Explanation-id) | Dokumen langkah demi langkah tentang cara efisiensi dihitung, dapat diekspor ke Word |

Di atas tab terdapat tiga baris kontrol (locator Anda, stasiun DX, band, antena, ketinggian jejak, waktu); lihat [Memulai](Getting-Started-id). Tombol **Kontrol** melipatnya, sedangkan bahasa dan skema warna dipilih di kanan atas; lihat [Pengaturan dan folder data](Settings-and-Data-Folder-id).

## Singkatnya

- **Lintasan nyata, bukan arah tetap**: efisiensi dihitung untuk lintasan lingkaran besar antara kedua locator (program lama memakai empat arah tetap).
- **Model pantulan spekular** (McKinley) pada titik-titik lapisan E setiap 15 km, dengan ketinggian jejak dibaca langsung dari radar Collm.
- **Hot A / Hot B** 150 km di kedua sisi titik tengah (dapat diatur 30–400 km); yang disarankan berwarna merah, yang sudah berada di dalam lobus antena Anda berwarna abu-abu.
- **Radar langsung**: Collm diperiksa setiap 5 menit, hanya sumber yang berubah yang diunduh ulang; tanpa koneksi program tetap bekerja dengan data terakhir yang tersimpan.
- Prakiraan **eksperimental** di 50/144/432 MHz dengan aturan λ³ dari SM6FHZ, dapat dibandingkan dengan pengamat RMOB.
- Semuanya ada di satu folder **`data`** di samping program: tanpa AppData, tanpa folder sistem.

> Efisiensi adalah model eksperimental (pantulan spekular + jejak underdense). Bandingkan dengan MCG_MS, MS-Soft dan pengalaman Anda sendiri di udara.

## Mulai dari mana

1. [Instalasi](Installation-id)
2. [Memulai](Getting-Started-id)
3. [Pemecahan masalah dan FAQ](Troubleshooting-FAQ-id) jika ada yang tidak berfungsi.

Unduhan: halaman **[Releases](https://github.com/ic8tem/YA-MS/releases)** di GitHub.
