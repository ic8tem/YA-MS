[English](Sky-View) · [Italiano](Sky-View-it) · [Deutsch](Sky-View-de) · [Nederlands](Sky-View-nl) · [Français](Sky-View-fr) · [Español](Sky-View-es) · [Português](Sky-View-pt) · [Dansk](Sky-View-da) · [Norsk](Sky-View-nb) · [Svenska](Sky-View-sv) · [Íslenska](Sky-View-is) · [Eesti](Sky-View-et) · [Lietuvių](Sky-View-lt) · [Latviešu](Sky-View-lv) · [Русский](Sky-View-ru) · [Українська](Sky-View-uk) · [Türkçe](Sky-View-tr) · [Afrikaans](Sky-View-af) · [العربية](Sky-View-ar) · [עברית](Sky-View-he) · [اردو](Sky-View-ur) · [हिन्दी](Sky-View-hi) · [বাংলা](Sky-View-bn) · **Bahasa Indonesia** · [Tagalog](Sky-View-tl) · [日本語](Sky-View-ja) · [한국어](Sky-View-ko) · [中文](Sky-View-zh)

# Kubah langit

*Tab: Perhitungan prakiraan › Perhitungan prakiraan.*

[![Kubah langit](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_1.png)

Sub-tab ini (kubah langit pada versi sebelumnya) menyatukan dalam satu layar **di mana** jejak yang berguna berada sekarang dan **ke mana** antena diarahkan. Di kiri **denah** lintasan; di kanan daftar hujan meteor, kubah langit kecil dengan radian, teks perhitungan, dan **penampang** dilihat dari antena Anda. Semuanya mengacu pada saat yang dipilih dengan *Tanggal perhitungan (UTC)* dan penggeser *Jam (−12 hingga +36 h)* (bawaan waktu nyata, dengan langkah 15 menit).

Sebuah **strip di atas denah** merangkum perhitungan untuk saat itu: tanggal dan waktu (*sekarang* atau berapa jam dari sekarang), **indeks lintasan Σ ZHR×η**, **hujan meteor paling berguna** beserta ZHR dan efisiensinya (juga dalam dB relatif terhadap acuan DJ5HG, lihat [Perhitungan efisiensi](Efficiency-Calculation-id)), jumlah hujan meteor di atas cakrawala, dan **Hot yang disarankan** beserta azimutnya.

Pada kubah langit kecil, sebuah **garis oranye** yang melewati zenit selalu memberikan **arah antena yang tepat**, tegak lurus terhadap pergeseran hujan meteor yang dipilih (atau yang paling menguntungkan): azimut radian ±90°, berlabel *antena NNN°* di kedua ujungnya, dengan toleransi ±45° sebagai garis tipis. Tanda oranye pendek di tepi memberikan arah tegak lurus untuk hujan meteor berguna lainnya.

## Denah (kiri)

Peta Eropa dilihat dari atas (**T di kanan**) dengan skala derajat di sekelilingnya. Keterangan di bawah peta memberikan radiusnya (*Peta: tepi = … km dari stasiun*).

| Elemen | Gambar |
|---|---|
| Lintasan / DX | Garis hijau dari stasiun Anda ke stasiun DX (selalu lintasan lingkaran besar yang nyata antara kedua locator) |
| **Hot A / Hot B** | Titik di kedua sisi titik tengah, tegak lurus terhadap lintasan, pada jarak yang diberikan tabel offset AMS (atau dimasukkan secara manual). **Merah = disarankan**, **merah muda = di luar lobus antena**, **abu-abu = di dalam lobus** (dengan peringatan) |
| Lobus antena | Lobus horizontal −3 dB di sekitar azimut antena (antena selalu diarahkan ke DX), berlabel *lobus …°* |
| Batas zona bersama | Titik samar *bts. A* / *bts. B* dan dua lingkaran tempat cakrawala tiap stasiun bertemu lapisan E (lihat [Geometri](Geometry-and-Path-Loss-id#batas-zona-bersama)) |
| Pergeseran hujan meteor | **Garis kuning**: arah hujan meteor yang dipilih (atau yang paling menguntungkan) menyapu langit, yaitu azimut radian |
| Arah terbaik | **Titik oranye**: dua arah yang tegak lurus terhadap pergeseran (azimut radian ±90°, SM6FHZ) |
| **Zona PREV** | Elips terang: tempat jatuhnya jejak paling mungkin **saat ini**, satu untuk tiap sisi lintasan |

Label tidak saling tumpang tindih: Hot A dan PREV A ditulis di kiri lintasan, B di kanan. **Keterangan** berupa kolom yang dapat dilipat di sebelah kanan peta.

**Mouse pada peta:** **klik kiri = locator stasiun DX**, **klik kanan = locator stasiun saya**. Lintasan langsung dihitung ulang.

Opsi di atas daftar hujan meteor: **Arah Hot A / Hot B**, **Peta Eropa** (Natural Earth, diunduh ke `data/mappa` pada start pertama), **Tampak atas (T di kanan)**.

### Hot yang disarankan

Untuk waktu yang ditampilkan, program menjumlahkan bobot ZHR × efisiensi untuk semua hujan meteor di atas cakrawala, dibagi antara sisi A (fraksi f_A) dan sisi B. Sisi dengan bobot lebih besar memberikan Hot yang disarankan, digambar merah:

```math
W_A = \sum \frac{ZHR\,\eta}{100}\,f_A,\qquad W_B = \sum \frac{ZHR\,\eta}{100}\,(1-f_A),\qquad \mathrm{Hot} = \arg\max(W_A,\ W_B)
```

*Pilihan program (manual pers. 23).* Asal gagasannya: DJ5HG, dilaporkan oleh DF5HC (konferensi DARC 2018) – bergantung pada posisi radian, salah satu dari dua titik, HOT-A atau HOT-B, lebih menguntungkan. Memutar 10–30° ke sisi itu (side scatter) berasal dari artikel Cerrotta–Sartori.

### Zona PREV

Untuk setiap titik P lapisan E, kontribusi semua hujan meteor aktif terhadap efisiensi (syarat spekular yang sama seperti pada [efisiensi](Efficiency-Calculation-id#model)) dijumlahkan dengan bobot ZHR. Titik dengan paling sedikit 3 % dari maksimum membentuk zona PREV; masing-masing digambar sebagai elips dengan pusat = rata-rata berbobot titik-titiknya dan sumbu = dua kali sebarannya.

```math
W_P = \sum ZHR\; c_P(\hat{s}),\qquad c_P = 100\,\frac{w_P S_P \max(0,\ \hat{s}\cdot\hat{u}_P)}{\max F},\qquad PREV:\ W_P \ge 0{.}03\,\max W
```

*Pilihan program (manual pers. 34).* Inilah aturan praktisnya: jika hujan meteor menyapu dari utara ke selatan, jejak yang berguna jatuh di timur dan barat.

## Daftar hujan meteor (kanan atas)

| Kolom | Arti |
|---|---|
| Hujan meteor, Kode | Nama dan kode IMO |
| ZHR sekarang | Aktivitas saat ini (ZHR puncak IMO dengan profil aktivitas) |
| Azimut, Elev. | Posisi radian dilihat dari stasiun Anda |
| Efis. % | Efisiensi hujan meteor untuk lintasan ini |
| Sisi | A atau B, sisi dari mana sebagian besar pantulan datang |
| Arah terbaik | Azimut radian ±90° |
| Terbit, Terbenam | Terbit dan terbenamnya radian (UTC); *sirkumpolar* atau *selalu di bawah* bila berlaku |

Klik sebuah baris untuk memilih hujan meteor: garis pergeseran kuning dan titik oranye mengikutinya.

## Kubah langit kecil (kanan tengah)

Radian-radian pada kubah langit dilihat dari stasiun Anda, dengan **kode IMO** dan **jalur hariannya berwarna sian** (jam UTC). **Klik sebuah radian** untuk memilihnya. Warna:

| Warna | Arti |
|---|---|
| Kuning | efisiensi ≥ 50 % dan ZHR ≥ 2 |
| Oranye | efisiensi ≥ 20 % |
| Merah tua | efisiensi < 20 % |
| Abu-abu | hampir tidak aktif |

Di sebelahnya, teks perhitungan: panjang dan azimut lintasan, titik tengah dan elevasinya, azimut dan offset Hot A / Hot B, Hot yang disarankan (*… disarankan sekarang: az. …° (…% pantulan yang diperkirakan)*), batas zona bersama, dan pengingat: *arah terbaik untuk hujan meteor: TEGAK LURUS terhadap arah kedatangan (azimut radian ±90°, toleransi ±40–50°, SM6FHZ)*.

## Penampang (kanan bawah)

*PENAMPANG – jejak paling mungkin dilihat dari antena ke arah stasiun DX.* Secara horizontal **azimut relatif terhadap stasiun DX** (← A kiri, B → kanan), secara vertikal **elevasi**. Untuk setiap hujan meteor diambil 14 titik pantul terkuat; setiap jejak berupa ruas yang mengarah ke radian, dari 10 km di atas hingga 10 km di bawah ketinggian jejak (paling banyak 60 km per sisi), lebih tebal bila lebih mungkin. Juga digambar: lobus antena (lingkaran −3 dB di sekitar elevasi lobus), stasiun DX serta Hot A / Hot B.

```math
Q = P \pm t_{1/2}\,\hat{s},\qquad t_{1/2} = \min\left(60\ \mathrm{km},\ \frac{10\ \mathrm{km}}{\max(0{.}17,\ |\hat{s}\cdot\hat{u}_P|)}\right)
```

*Pilihan program (manual pers. 35).*

## Peringatan

| Peringatan | Kapan |
|---|---|
| **PERHATIAN: Hot A (dan/atau Hot B) masuk ke lobus antena …** | Hot spot berada dalam ±θ/2 dari azimut antena (θ = lobus horizontal −3 dB): dengan arah ini sudah tercakup. Ditandai abu-abu pada peta. Hot yang disarankan tetap merah. |
| **RADIAN TERLALU TINGGI (di atas 70°)** | Sebuah radian yang berguna berada di atas 70° dari stasiun Anda: jejak jatuh hampir vertikal dan sedikit memantul ke arah lintasan (DF5HC, DH9GCD). Jam-jam yang sama ditandai ↑ di [tabel per jam](Efficiency-Calculation-id#tabel-per-jam). |
| **RADIAN RENDAH SEPANJANG LINTASAN** | Sebuah radian aktif berada di bawah 20° dan dalam 30° dari arah lintasan. Efisiensi yang dihitung tetap rendah (hati-hati), tetapi DJ5HG memperkirakan pantulan yang jarang namun kuat dari jejak menyapu yang searah lintasan (Hamburg–Narvik, Quadrantid, sekitar 19 UTC): layak didengarkan. |
| *Tidak ada zona bersama lapisan E* | Lintasan lebih panjang dari dua kali jangkauan pada ketinggian jejak: kedua stasiun tidak melihat bagian bersama dari lapisan E (satu lompatan tidak mungkin). |
| *Tidak ada Hot yang disarankan* | Hampir tidak ada hujan meteor aktif pada waktu ini. |

Referensi untuk grafik kubah langit: Swan Meteor Skyview oleh DL1DBC (swan.ms); plot polar dengan arah terbaik: RadiantCalc oleh SM6FHZ.
