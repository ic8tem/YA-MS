[English](Efficiency-Calculation) · [Italiano](Efficiency-Calculation-it) · [Deutsch](Efficiency-Calculation-de) · [Nederlands](Efficiency-Calculation-nl) · [Français](Efficiency-Calculation-fr) · [Español](Efficiency-Calculation-es) · [Português](Efficiency-Calculation-pt) · [Português (Brasil)](Efficiency-Calculation-pt-br) · [Dansk](Efficiency-Calculation-da) · [Norsk](Efficiency-Calculation-nb) · [Svenska](Efficiency-Calculation-sv) · [Íslenska](Efficiency-Calculation-is) · [Eesti](Efficiency-Calculation-et) · [Lietuvių](Efficiency-Calculation-lt) · [Latviešu](Efficiency-Calculation-lv) · [Polski](Efficiency-Calculation-pl) · [Čeština](Efficiency-Calculation-cs) · [Magyar](Efficiency-Calculation-hu) · [Română](Efficiency-Calculation-ro) · [Ελληνικά](Efficiency-Calculation-el) · [Русский](Efficiency-Calculation-ru) · [Українська](Efficiency-Calculation-uk) · [Türkçe](Efficiency-Calculation-tr) · [Afrikaans](Efficiency-Calculation-af) · [العربية](Efficiency-Calculation-ar) · [עברית](Efficiency-Calculation-he) · [اردو](Efficiency-Calculation-ur) · [हिन्दी](Efficiency-Calculation-hi) · [বাংলা](Efficiency-Calculation-bn) · **Bahasa Indonesia** · [Tagalog](Efficiency-Calculation-tl) · [ไทย](Efficiency-Calculation-th) · [日本語](Efficiency-Calculation-ja) · [한국어](Efficiency-Calculation-ko) · [中文](Efficiency-Calculation-zh) · [中文 (繁體)](Efficiency-Calculation-zh-tw)

# Perhitungan efisiensi

*Tab: Perhitungan prakiraan › Perhitungan efisiensi.*

[![Perhitungan efisiensi](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-2_3.png)

**Efisiensi** sebuah hujan meteor menyatakan, dalam persen, seberapa besar posisi radiannya memungkinkan pantulan pada lintasan **Anda**. Konsep ini berasal dari Ilkka **OH5IY** (MS-Soft) dan diangkat dalam artikel Cerrotta–Sartori: puncak efisiensi tidak bertepatan dengan puncak visual (ZHR), karena bergantung pada letak radian relatif terhadap kedua stasiun. MCG_MS karya DL5MCG menerapkan gagasan yang sama pada empat arah tetap; YA-MS menghitungnya untuk **lintasan nyata** antara kedua locator.

Tab ini menampilkannya jam demi jam untuk hari yang dipilih di *Hari untuk tabel 24 jam (UTC)* (nilai pada setengah jam setiap jam).

## Kartu ringkas

| Kartu | Isi |
|---|---|
| **JAM TERBAIK HARI INI** | Jam dengan indeks lintasan tertinggi, indeksnya dan sisi dominan (A/B dengan %-nya) |
| **HUJAN METEOR PALING MENGUNTUNGKAN** | Hujan meteor dengan ZHR × efisiensi terbesar hari itu, efisiensinya, jam dan sisinya, serta **arah terbaik** (azimut radian +90° / −90°) |
| **SEKARANG** | Indeks dan sisi dominan pada jam ini, serta Hot yang disarankan (hanya jika hari yang dipilih adalah hari ini) |
| **PRAKIRAAN EKSPERIMENTAL** | Pantulan/jam yang diharapkan sekarang, 1 jam lagi dan 2 jam lagi pada frekuensi prakiraan (Collm, aturan SM6FHZ; lihat [Prakiraan eksperimental](Experimental-Forecasts-id)) |

Di bawah kartu, sebuah pita menjelaskan huruf A dan B (lihat di bawah).

## Grafik

*Efisiensi per jam untuk … pada … (UTC, nilai pada setengah jam).* Untuk paling banyak lima hujan meteor: efisiensi % sebagai garis utuh dan rumus DH9GCD sebagai garis titik-titik dengan warna yang sama; **indeks lintasan** sebagai batang biru pada skala kanan.

## Tabel per jam

Satu baris untuk setiap hujan meteor yang aktif pada hari itu (diurutkan menurut ZHR), 24 kolom untuk jam (UTC):

| Sel | Arti |
|---|---|
| `63A` | efisiensi 63 %, sebagian besar pantulan dari sisi **A** |
| `41B` | efisiensi 41 %, sisi **B** |
| `3` | efisiensi di bawah 5 %: angka tanpa huruf sisi |
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

```
ê_A = (A − P)/|A − P|     ê_B = (B − P)/|B − P|     n̂ = (ê_A + ê_B)/|ê_A + ê_B|     specular condition: ŝ·n̂ = 0
```

Hukum yang sama mendasari QTFGUI karya DJ5HG (hamburan kerucut). Syarat ini diterima dengan toleransi Gauss σ = 0,05 rad (sekitar 3°) – *pilihan program*:

```
S_P = exp( −(ŝ·n̂)² / (2σ²) )
```

**2. Bobot setiap titik.** Daya jejak underdense (McKinley), φ = setengah sudut hambur (dibatasi 85°, *pilihan*):

```
φ = ½·arccos(ê_A·ê_B)        w_P = 1 / [ R1·R2·(R1 + R2)·cos²φ ]
```

Jumlah meteor yang mencapai sebuah titik sebanding dengan sinus elevasi radian di titik itu (ŝ·û_P), koreksi yang sama yang dipakai IMO untuk ZHR.

**3. Jumlah dan persentase.** Titik setiap 15 km pada ketinggian jejak, hanya di tempat yang terlihat oleh kedua stasiun di atas elevasi lobus (*pilihan*). 100 % adalah posisi radian paling menguntungkan untuk lintasan tersebut:

```
F(ŝ) = Σ_P w_P · S_P · max(0, ŝ·û_P)          η(ŝ) = 100 · F(ŝ) / max F   %
```

F dihitung sekali per lintasan pada kisi arah (azimut setiap 5°, elevasi setiap 2,5°) lalu diinterpolasi.

**4. Sisi dan indeks.**

```
f_A = Σ_{P∈A} w_P·S_P·(ŝ·û_P) / Σ_P w_P·S_P·(ŝ·û_P)          I(t) = Σ_showers ZHR(t)·η(t) / 100
```

Huruf di tabel adalah sisi dengan fraksi lebih besar. *Pilihan program (manual pers. 32–33).*

## Perbandingan DH9GCD

Pemeriksaan independen: rumus arah terbaik dari **DH9GCD**, dilaporkan oleh **DF5HC** (konferensi DARC, Januari 2018), dengan El dan Az elevasi dan azimut radian dilihat dari stasiun Anda dan P azimut stasiun DX:

```
E = sin El · cos El · sin(P − Az)          shown as  E% = 200 · sin El · cos El · |sin(P − Az)|
```

Nilainya maksimum saat radian berada di 45° dan menyamping terhadap lintasan. DF5HC menganggap radian terlalu rendah di bawah 20° dan **terlalu tinggi di atas 70°**: jam-jam ini diberi ↑ di tabel dan peringatan di [Kubah langit](Sky-View-id#peringatan). Rumus ini mengabaikan jarak dan ketinggian, tetapi merupakan acuan yang baik.

## Verifikasi

| Verifikasi | Hasil |
|---|---|
| Aturan SM6FHZ (VUSHF 2025): lintasan terbaik tegak lurus azimut radian, arah = az radian ±90°, toleransi ±40–50° | Direproduksi oleh model; dengan radian sejajar lintasan dan tinggi di langit, efisiensinya hampir nol |
| QTFGUI karya DJ5HG, Hamburg JO53IM – Barcelona, Quadrantid, 4 Januari (contoh dalam manualnya) | QTFGUI: 07:00 arah 252°, −8 dB; 08:00 tidak ada zona pantul; 09:00 arah 168°, −4 dB. YA-MS (ketinggian 102 km seperti QTFGUI): 07:00 241°, −5,4 dB; 08:00 0,6 % (−22 dB); 09:00 161°, −4,0 dB. DH9GCD: 26 %, 2 %, 32 %. Ketiga metode melihat lubang pukul 08:00, dengan radian hampir di zenit |
| Pengambilan sampel setiap 5 km, bukan 15 km | persentase berubah kurang dari 0,3 poin |

> Skala yang dipakai OH5IY dan MCG_MS tidak diketahui secara rinci (manual MS-Soft tidak tersedia): bandingkan persentasenya dengan program-program tersebut sebelum menganggapnya setara. Model hanya mempertimbangkan jejak underdense, dengan antena isotropik; ledakan overdense dan latar sporadis tidak termasuk dalam efisiensi (latar sporadis diwakili oleh fluks radar).
