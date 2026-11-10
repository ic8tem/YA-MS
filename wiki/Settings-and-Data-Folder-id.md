[English](Settings-and-Data-Folder) · [Italiano](Settings-and-Data-Folder-it) · [Deutsch](Settings-and-Data-Folder-de) · [Nederlands](Settings-and-Data-Folder-nl) · [Français](Settings-and-Data-Folder-fr) · [Español](Settings-and-Data-Folder-es) · [Português](Settings-and-Data-Folder-pt) · [Português (Brasil)](Settings-and-Data-Folder-pt-br) · [Dansk](Settings-and-Data-Folder-da) · [Norsk](Settings-and-Data-Folder-nb) · [Svenska](Settings-and-Data-Folder-sv) · [Íslenska](Settings-and-Data-Folder-is) · [Eesti](Settings-and-Data-Folder-et) · [Lietuvių](Settings-and-Data-Folder-lt) · [Latviešu](Settings-and-Data-Folder-lv) · [Polski](Settings-and-Data-Folder-pl) · [Čeština](Settings-and-Data-Folder-cs) · [Română](Settings-and-Data-Folder-ro) · [Русский](Settings-and-Data-Folder-ru) · [Українська](Settings-and-Data-Folder-uk) · [Türkçe](Settings-and-Data-Folder-tr) · [Afrikaans](Settings-and-Data-Folder-af) · [العربية](Settings-and-Data-Folder-ar) · [עברית](Settings-and-Data-Folder-he) · [اردو](Settings-and-Data-Folder-ur) · [हिन्दी](Settings-and-Data-Folder-hi) · [বাংলা](Settings-and-Data-Folder-bn) · **Bahasa Indonesia** · [Tagalog](Settings-and-Data-Folder-tl) · [日本語](Settings-and-Data-Folder-ja) · [한국어](Settings-and-Data-Folder-ko) · [中文](Settings-and-Data-Folder-zh)

# Pengaturan dan folder data

## Bilah tab

Di ujung kanan bilah tab, dari kanan ke kiri:

| Kontrol | Fungsinya |
|---|---|
| **Bahasa** (daftar) | Bahasa antarmuka; lihat [Bahasa](#bahasa) |
| **Tema** (daftar) | Skema warna; lihat [Skema warna](#skema-warna) |
| **Kontrol ▴ / ▾** | Melipat atau membuka tiga baris kontrol di atas tab; lihat [Huruf dan Kontrol](#huruf-dan-kontrol) |

Mengganti bahasa atau tema akan menyimpan pengaturan dan **membangun ulang jendela** pada posisi dan ukuran yang sama, di tab yang sama: tidak perlu memulai ulang.

## Bahasa

Enam bahasa antarmuka:

| Bahasa | Kode | File |
|---|---|---|
| Italiano | `it` | tidak ada: bahasa Italia adalah bahasa dasar (kunci) |
| English | `en` | `data/lingue/en.txt` |
| Русский | `ru` | `data/lingue/ru.txt` |
| 日本語 | `ja` | `data/lingue/ja.txt` |
| Deutsch | `de` | `data/lingue/de.txt` |
| Nederlands | `nl` | `data/lingue/nl.txt` |

Pada start pertama YA-MS memakai **bahasa sistem** jika termasuk salah satu di atas, jika tidak bahasa Italia. Angka dan tanggal mengikuti bahasa yang dipilih (mis. titik desimal dalam bahasa Inggris, koma dalam bahasa Italia dan Jerman). Teks yang tidak ada dalam file terjemahan ditampilkan dalam bahasa Italia. Di Linux, bahasa Jepang memerlukan font yang sesuai: lihat [Pemecahan masalah](Troubleshooting-FAQ-id#linux-teks-jepang-tampil-sebagai-kotak).

Dokumen [Efisiensi - penjelasan](Efficiency-Explanation-id) dan manual perhitungan berbahasa Italia.

## Skema warna

Daftar **Tema** menyediakan 12 skema, sama dengan program EME karya penulis, YAEC, ditambah palet asli YA-MS:

| Skema | Keterangan |
|---|---|
| **Terang** | bawaan |
| **Malam** | nuansa biru gelap, untuk dipakai malam hari |
| **Hitam** | latar hitam, untuk ruangan gelap dan layar OLED |
| Pastel biru muda · Pastel oranye · Pastel aquamarine · Pastel hijau · Pastel merah muda · Pastel ungu muda · Pastel nila · Pastel cokelat | delapan skema pastel terang |
| **Jejak meteor** | gaya asli YA-MS (hingga versi 1.2.0): ungu malam dengan biru muda, ungu, hijau muda, kuning dan oranye |

Skema berlaku untuk semua tab dan disimpan di `config.ini` (kunci `tema`).

## Huruf dan Kontrol

- **Huruf** (di ujung baris kontrol pertama): memperbesar **seluruh teks** dari **100 hingga 300 %** dengan langkah 10 %; garis, lingkaran dan peta tetap berukuran sama. Dengan huruf besar, tab berpindah ke baris kedua dan kartu membesar.
- **Kontrol**: dengan huruf besar atau layar kecil, lipat ketiga baris kontrol untuk memberi ruang bagi peta dan grafik. Keadaannya diingat.

## Folder data

Semua data dan pengaturan berada di satu folder **`data`** **di samping program** – tanpa AppData, tanpa folder sistem:

| Sistem | Program | Data |
|---|---|---|
| Windows (installer) | `C:\YA-MS\YA-MS.exe` | `C:\YA-MS\data` |
| Windows (portabel) | di mana pun Anda mengekstraknya | `data` di samping `YA-MS.exe` |
| Linux | `~/YA-MS/YA-MS` | `~/YA-MS/data` |
| macOS | `~/YA-MS/YA-MS.app` | `~/YA-MS/data` (di samping aplikasi) |

Saat mulai, program membuat folder bila perlu dan hanya menyalin file awal yang **belum ada**: file yang sudah Anda ubah tidak pernah ditimpa. File terjemahan di `data/lingue` adalah file program dan diganti bila file dari versi baru lebih mutakhir.

### File yang dapat Anda edit

| File | Isi |
|---|---|
| `sciami.csv` | Katalog hujan meteor (nilai IMO dan nilai kerja); lihat [Hujan meteor](Showers-id#mengedit-katalog) |
| `massimi_imo.csv` | Tanggal dan jam puncak yang diterbitkan IMO (2026, 2027): **tambahkan tahun baru** di sini |
| `ant_radiante.csv` | Posisi Sumber Antihelion (tabel 6 IMO) |
| `fonti_radar.csv` | Alamat radar; `attivo=1` mengunduh, `0` mengabaikan |
| `regole_sperimentali.csv` | Konstanta dan aturan yang dipakai, masing-masing dengan sumbernya (referensi) |
| `lingue/<code>.txt` | Terjemahan antarmuka; lihat [Berkontribusi](Contributing-and-Contacts-id#terjemahan) |
| `config.ini` | Pengaturan (lihat di bawah) |

### File yang dibuat oleh program

| File / folder | Isi |
|---|---|
| `config.ini` | Pengaturan |
| `flusso_collm.csv` | Arsip per jam fluks Collm |
| `quote_collm.csv` | Arsip ketinggian jejak |
| `radar/` | Gambar radar terbaru dan file RMOB |
| `mappa/` | Garis pantai dan perbatasan Natural Earth (diunduh pada start pertama) |
| `adif_quadrati.csv` | Kotak dari ADIF terakhir yang dimuat |
| `efficienza_spiegazione.txt`, `.docx` | [Dokumen penjelasan](Efficiency-Explanation-id) |

## config.ini

Teks biasa, satu `key=value` per baris (baris yang diawali `#` atau `;` adalah komentar). Program menulis file ini saat ditutup, jadi **editlah saat YA-MS tertutup**. Kunci yang mungkin perlu Anda ketahui:

| Kunci | Bawaan | Arti |
|---|---|---|
| `mio_locator`, `mia_quota_m` | JN70CN, 62 | Locator dan ketinggian Anda (m) |
| `dx_locator`, `dx_quota_m` | JO62QM, 50 | Locator dan ketinggian stasiun DX (m) |
| `banda_MHz` | 144 | Band (28, 50, 70, 144, 222, 432) |
| `quota_scie_km`, `quota_da_radar` | 90, 1 | Ketinggian jejak (km); 1 = pakai modus Collm |
| `elevazione_lobo_gradi` | 0 | Elevasi lobus (°) |
| `boom_m` | 4.6 | Panjang boom Yagi (m) |
| `hot_spot_km` | 150 | Jarak Hot A / Hot B dari titik tengah (30–400 km) |
| `lingua` | sistem / `it` | Kode bahasa (`it`, `en`, `ru`, `ja`, `de`, `nl`) |
| `tema` | `chiaro` | Skema warna: `chiaro` (Terang), `scuro` (Malam), `nero` (Hitam), `pastello-azzurro`, `pastello-arancione`, `pastello-acquamarina`, `pastello-verde`, `pastello-rosa`, `pastello-lilla`, `pastello-indaco`, `pastello-marrone`, `scia` (Jejak meteor) |
| `carattere_pct` | 100 | Ukuran huruf (100–300 %) |
| `comandi_visibili` | 1 | 1 = baris kontrol ditampilkan, 0 = dilipat |
| `mostra_mappa`, `vista_alto` | 1, 1 | Peta Eropa, tampak atas pada Kubah langit |
| `aggiornamento_automatico` | 1 | Pemeriksaan otomatis sumber setiap 5 menit |
| `esponente_lambda` | 3 | Eksponen λ di tab Fluks radar |
| `potenza_W`, `guadagno_dBi`, `sensibilita_dBm`, `densita_esponente_q` | 400, 14, −130, 14 | Masukan anggaran link |
| `prev_frequenza_MHz`, `prev_esponente`, `prev_fattore_stazione` | 144, 3, 1 | Prakiraan eksperimental: frekuensi, k, K |
| `rmob_osservatore` | kosong | Nama pengamat RMOB |
| `rmob_automatico` | 0 | Pengambilan RMOB otomatis (aktifkan hanya dengan izin RMOB) |
| `rmob_url` | `https://rmob.org/index.php/livedata/live_datas/{NOME}_{MMAAAA}rmob.TXT` | Templat alamat RMOB |
| `graves_sequenza` | 0 | Urutan berkas GRAVES: 0 = 0,8 s (2021), 1 = 3,2 s (2007) |

## Privasi

YA-MS tidak mengumpulkan data dan tidak menampilkan iklan. Program hanya tersambung ke internet untuk mengunduh data publik: gambar radar Collm dan Sodankylä, peta Natural Earth (start pertama) dan, jika Anda memintanya, file RMOB.
