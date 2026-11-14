[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · [ไทย](Efficiency-Calculation-th) · **Bahasa Indonesia** · [Tagalog](Efficiency-Calculation-tl) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Perhitungan efisiensi

*Tab: Perhitungan prakiraan › Perhitungan efisiensi.*

[![Perhitungan efisiensi](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Efisiensi** sebuah hujan meteor menyatakan, dalam persen, seberapa besar posisi radiannya memungkinkan pantulan pada lintasan **Anda**. Konsep ini berasal dari Ilkka **OH5IY** (MS-Soft) dan diangkat dalam artikel Cerrotta–Sartori: puncak efisiensi tidak bertepatan dengan puncak visual (ZHR), karena bergantung pada letak radian relatif terhadap kedua stasiun. MCG_MS karya DL5MCG menerapkan gagasan yang sama pada empat arah tetap; YA-MS menghitungnya untuk **lintasan nyata** antara kedua locator.

Tab ini menampilkannya jam demi jam untuk hari yang dipilih di *Tanggal perhitungan (UTC)* (nilai pada setengah jam setiap jam).

## Kartu ringkas

| Kartu | Isi |
|---|---|
| **JAM TERBAIK HARI INI** | Jam dengan indeks lintasan tertinggi, indeksnya dan sisi dominan (A/B dengan %-nya) |
| **HUJAN METEOR PALING MENGUNTUNGKAN** | Hujan meteor dengan ZHR × efisiensi terbesar hari itu, efisiensinya, jam dan sisinya, serta **arah terbaik** (azimut radian +90° / −90°) |
| **SEKARANG · 1, 3, 6, 12 DAN 24 JAM LAGI** | untuk tiap cakrawala, rata-rata jam yang dimulai di sana (empat sampel): indeks lintasan, sisi dominan, hujan meteor yang paling berkontribusi dan, bila ada data radar, pantulan per jam dari prakiraan eksperimental. Di SEKARANG, tanpa data radar, muncul Hot yang disarankan. Diperbarui tiap menit. |

Kotak-kotak ini ada di pita di bawah baris waktu, di atas tab, selalu terlihat meski baris perintah dilipat: di kiri dua kotak hari yang dipilih, lalu enam cakrawala prakiraan yang dimulai dari sekarang.

Di bawah kartu, sebuah pita menjelaskan huruf A dan B (lihat di bawah).

## Grafik

*Efisiensi per jam untuk … pada … (UTC, nilai pada setengah jam).* Untuk paling banyak lima hujan meteor: efisiensi % sebagai garis utuh dan rumus DH9GCD sebagai garis titik-titik dengan warna yang sama; **indeks lintasan** sebagai batang biru pada skala kanan.

## Tabel per jam

Satu baris untuk setiap hujan meteor yang aktif pada hari itu (diurutkan menurut ZHR), 24 kolom untuk jam (UTC):

| Sel | Arti |
|---|---|
| `63A` | efisiensi 63 %, sebagian besar pantulan dari sisi **A** |
| `41B` | efisiensi 41 %, sisi **B** |
| kosong | efisiensi di bawah 1 % |
| `…↑` | radian berada **di atas 70°** dari stasiun Anda pada jam itu (terlalu tinggi) |
| teks kuning | efisiensi ≥ 50 % |

- **A** = **kiri** jika melihat dari stasiun Anda ke arah stasiun DX (zona Hot A); **B** = **kanan** (zona Hot B). Sebaiknya antena diputar **10–30° ke sisi tersebut** (side scatter, artikel Cerrotta–Sartori).
- **Baris biru muda** (*DH9GCD %*, di bawah setiap hujan meteor): rumus DH9GCD, sebagai pembanding.
- **Baris Σ**: *Indeks lintasan (ZHR×efis.)*.
- **Baris oranye** (*Prakiraan … MHz (pantulan/jam)*): prakiraan eksperimental, untuk jam-jam yang tersedia (hari ini dan sebagian besok).

## Model

Semua langkah ada di [manual perhitungan](Efficiency-Explanation-id) (`doc/YA-MS_manuale_calcoli.docx`, bab 5). Singkatnya:

**1. Pantulan spekular.** Sebuah jejak meneruskan sinyal dari A ke B hanya jika jejak itu menyinggung elipsoid dengan A dan B sebagai titik fokusnya (McKinley 1961). Jejak-jejak sebuah hujan meteor sejajar dengan arah radian ŝ (artikel; McKinley). Untuk setiap titik P lapisan E, dengan vektor satuan ke arah stasiun:

```math
\hat{e}_A = \frac{A-P}{|A-P|},\qquad \hat{e}_B = \frac{B-P}{|B-P|},\qquad \hat{n} = \frac{\hat{e}_A+\hat{e}_B}{|\hat{e}_A+\hat{e}_B|},\qquad \hat{s}\cdot\hat{n} = 0
```

Hukum yang sama mendasari QTFGUI karya DJ5HG dan tulisannya *"Die Geometrie von Meteorscatterverbindungen"* (2004): jejak menghamburkan pada sebuah kerucut yang porosnya adalah jejak itu sendiri, dan hanya penerima yang berada pada kerucut yang mendengarnya. Untuk jejak ideal, dinding kerucut sangat tipis (radiator sepanjang ribuan panjang gelombang); program menerima syarat ini dengan toleransi Gauss σ = 0,05 rad (sekitar 3°), yang mewakili hal-hal yang tidak dilihat kerucut ideal: sebaran radian hujan meteor (0,3–1,4° menurut pengukuran GMN), jejak yang dibengkokkan angin, dan panjang jejak yang terbatas – *pilihan program*:

```math
S_P = \exp\left(-\frac{(\hat{s}\cdot\hat{n})^2}{2\sigma^2}\right)
```

**2. Bobot setiap titik.** Daya jejak underdense (McKinley; ITU-R P.843, pers. 3), φ = setengah sudut hambur (dibatasi 85°, *pilihan*), β = sudut antara jejak dan bidang propagasi A-P-B, p̂ = normal satuan bidang tersebut:

```math
\varphi = \tfrac{1}{2}\arccos(\hat{e}_A\cdot\hat{e}_B),\qquad \hat{p} = \frac{\hat{e}_A\times\hat{e}_B}{|\hat{e}_A\times\hat{e}_B|},\qquad \sin\beta = |\hat{s}\cdot\hat{p}|,\qquad w_P(\hat{s}) = \frac{1}{R_1 R_2 (R_1+R_2)\,(1-\cos^2\beta\,\sin^2\varphi)}
```

**Opsi "Sudut β antara jejak dan lintasan (McKinley lengkap)"** (aktif secara bawaan, pengaturan hati-hati). Aktif: jejak yang memotong bidang propagasi bernilai 10–15 dB lebih rendah daripada yang terletak di dalamnya, sehingga tidak ada jejak yang ditaksir terlalu tinggi. Nonaktif: setiap jejak diberi bobot seolah-olah terletak di bidang tersebut (β = 0, bobot dengan cos²φ), seperti hingga versi 1.6. *Verifikasi:* pada lintasan 1000 km, tanpa β azimut radian terbaik berada 15°–90° dari lintasan tergantung elevasi radian (30° dengan radian pada 30°, tegak lurus lintasan dengan radian pada 60°), dan radian yang tegak lurus bernilai 67 % pada elevasi 30°; dengan β radian terbaik selalu searah lintasan dan yang tegak lurus turun ke 15 %. Dengan β aturan arah terbaik SM6FHZ / DH9GCD hilang; β tetap menjadi opsi, aktif secara bawaan karena memberikan nilai paling hati-hati, dan menonaktifkannya mengembalikan aturan tersebut.

Jumlah meteor yang mencapai sebuah titik sebanding dengan sinus elevasi radian di titik itu (ŝ·û_P), koreksi yang sama yang dipakai IMO untuk ZHR.

**Opsi "Jejak lebih panjang dengan radian rendah (DJ5HG)"** (kotak centang di atas grafik, nonaktif secara bawaan, dengan tooltip): DJ5HG mencatat bahwa dengan radian rendah lebih sedikit meteor jatuh per km², tetapi jejaknya lebih panjang (hingga 100 km berguna) dan lebih sering memenuhi hukum pantulan. Dengan opsi aktif, bobot menjadi min(sin El, 15/100): tebal lapisan yang berguna, 15 km, dibagi sinus elevasi memberikan panjang jejak, dibatasi 100 km. Di atas sekitar 9° kedua efek saling meniadakan. Jika nonaktif, perhitungan tetap hati-hati.

**Pengaturan perhitungan** (baris yang sama, tombol radio): **Hati-hati** (bawaan, nilai paling hati-hati: ketinggian jejak dari radar, jejak normal, β aktif), **Seperti DJ5HG** (102 km, jejak lebih panjang, β) dan **Kustom**, yang terpilih otomatis saat Anda mengubah secara manual ketinggian, kotak *dari radar*, opsi jejak lebih panjang, atau β.

**3. Jumlah dan persentase.** Titik setiap 15 km pada ketinggian jejak, dilihat kedua stasiun di atas cakrawala dan diberi bobot dengan pola vertikal kedua antena (kotak *pola antena*, aktif secara bawaan; nonaktif, hanya titik di atas elevasi lobus) (*pilihan*). 100 % adalah posisi radian paling menguntungkan untuk lintasan itu:

```math
F(\hat{s}) = \sum_P w_P\, S_P\, \max(0,\ \hat{s}\cdot\hat{u}_P),\qquad \eta(\hat{s}) = 100\,\frac{F(\hat{s})}{\max F}\ \%
```

F dihitung sekali per lintasan pada kisi arah (azimut setiap 5°, elevasi setiap 2,5°) lalu diinterpolasi.

**Efisiensi dalam dB (acuan DJ5HG).** Persentase hanya relatif terhadap posisi radian terbaik untuk lintasan itu. Untuk membandingkan lintasan yang berbeda, program juga memberikan efisiensi dalam dB relatif terhadap acuan tetap DJ5HG: 0 dB adalah maksimum lintasan utara–selatan 1000 km yang melintasi khatulistiwa dengan radian di ekuator langit saat ekuinoks, dihitung dengan ketinggian dan bobot yang sama. DJ5HG menyatakan nilainya lebih baik dari 6 dB.

**4. Sisi dan indeks.**

```math
f_A = \frac{\sum_{P\in A} w_P S_P\,(\hat{s}\cdot\hat{u}_P)}{\sum_P w_P S_P\,(\hat{s}\cdot\hat{u}_P)},\qquad I(t) = \sum \frac{ZHR(t)\,\eta(t)}{100}
```

Huruf di tabel adalah sisi dengan fraksi lebih besar. *Pilihan program (manual pers. 32–33).*

## Perbandingan DH9GCD

Sumber primer untuk arah terbaik adalah Eshleman & Mlodnosky dan Meeks & James (Proc. IRE, 1957), Hines (1955) serta pemeriksaan eksperimentalnya oleh Forsyth, Hines & Vogan (1955): hanya radian pada setengah lingkaran langit yang tegak lurus terhadap garis bagi sudut hamburan yang berguna, jumlah jejak bertambah dengan sin El, dan di dekat titik tengah jejak yang berguna jatuh sekitar H·tan El ke samping, di sisi yang berlawanan dengan radian. DJ5HG menambahkan catatan: dengan radian **rendah** tepat sepanjang lintasan, rumus McKinley memberikan sinyal kuat (Hamburg–Narvik, Quadrantid, sekitar 19 UTC), sehingga "radian searah lintasan = hampir nol" hanya berlaku untuk radian tinggi; program tetap hati-hati dan menampilkan peringatan *RADIAN RENDAH SEPANJANG LINTASAN*.

Pemeriksaan independen: rumus arah terbaik dari **DH9GCD**, dilaporkan oleh **DF5HC** (konferensi DARC, Januari 2018) – tidak memiliki sumber primer yang diterbitkan – dengan El dan Az elevasi dan azimut radian dilihat dari stasiun Anda dan P azimut stasiun DX:

```math
E = \sin El\,\cos El\,\sin(P-Az),\qquad E\% = 200\,\sin El\,\cos El\,|\sin(P-Az)|
```

Nilainya maksimum saat radian berada di 45° dan menyamping terhadap lintasan. DF5HC menganggap radian terlalu rendah di bawah 20° dan **terlalu tinggi di atas 70°**: jam-jam ini diberi ↑ di tabel dan peringatan di [Kubah langit](Sky-View-id#peringatan). Rumus ini mengabaikan jarak dan ketinggian, tetapi merupakan acuan yang baik.

## Verifikasi

| Verifikasi | Hasil |
|---|---|
| Aturan SM6FHZ (VUSHF 2025): lintasan terbaik tegak lurus azimut radian, arah = az radian ±90°, toleransi ±40–50° | Direproduksi oleh model; dengan radian sejajar lintasan dan tinggi di langit, efisiensinya hampir nol |
| QTFGUI karya DJ5HG, Hamburg JO53IM – Barcelona, Quadrantid, 4 Januari (contoh dalam manualnya) | QTFGUI: 07:00 arah 252°, −8 dB; 08:00 tidak ada zona pantul; 09:00 arah 168°, −4 dB. YA-MS (ketinggian 102 km seperti QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Ketiga metode melihat lubang pukul 08:00, dengan radian hampir di zenit |
| Kurva DJ5HG (*Die Geometrie…*, Bild 8–9: dari Hamburg dan München, Quadrantid, 4 Januari; dibaca dari grafik, sekitar ±0,5 dB dan ±15 menit) dibandingkan dengan uji otomatis `--prova-dj5hg` (satu nilai per jam) | Waktu: celah saat radian dekat zenit jatuh pada jam yang sama (Barcelona 07:30–08:30 vs 07–09; Sofia 06:36–07:48 vs 07–08; Narvik 07–08:30 vs 07–09); Moskow tertutup 03–10 pada keduanya, terbuka dari Hamburg hingga sekitar 02:30 dan dari München hingga sekitar 00:30, seperti ditulis DJ5HG. Arah: selisih 2–10°. Level dan bentuk pada 102 km (selisih rata-rata dan RMS terhadap kurva): tanpa β, tanpa jejak lebih panjang −1,6 / 4,0 dB; jejak lebih panjang +1,1 / 4,6 dB; β −5,4 / 6,2 dB tetapi dengan bentuk terbaik (3,0 dB setelah rata-rata dihilangkan, vs 3,6): minimum dalam dengan radian rendah muncul (Barcelona −15,6 dB pukul 17 vs −16 dB pukul 19:36; Sofia −18,5 dB pukul 20 vs −14 dB). β dan jejak lebih panjang (*Seperti DJ5HG*) −2,2 / 4,7 dB; pengaturan hati-hati (ketinggian radar 89,5 km, β aktif, tanpa jejak lebih panjang) −6,9 / 7,6 dB, bentuk 3,3 dB. Tanpa β, YA-MS hampir tidak menampilkan minimum saat radian rendah dan hampir searah lintasan (−8,6 dan −10,4 dB): inilah keberatan DJ5HG sendiri, karena itu ada peringatan |
| Pengambilan sampel setiap 5 km, bukan 15 km | persentase berubah kurang dari 0,3 poin |

> Dokumentasi MS-Soft 5.2 mendefinisikan efisiensi OH5IY sebagai indeks relatif hanya untuk jejak underdense, dengan dua faktor (elevasi radian, terbaik sekitar 45°, dan sudut terhadap lintasan, terbaik 90°) serta nilai minimum yang dinaikkan secara manual ke 20 % untuk jejak overdense; rumusnya tidak diterbitkan. MCG_MS menghitungnya untuk empat arah tetap dan, dengan lokator DX, untuk lintasan sebenarnya. Model hanya mempertimbangkan jejak underdense, dengan antena isotropik; ledakan overdense dan latar sporadis tidak termasuk dalam efisiensi (latar sporadis diwakili oleh fluks radar). Sejak 1.8.1, dengan kotak «pola antena» aktif, pola vertikal antena diterapkan; pada azimut antena tetap isotropik.
