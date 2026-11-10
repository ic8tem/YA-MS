[English](Showers) · [Italiano](Showers-it) · [Deutsch](Showers-de) · [Nederlands](Showers-nl) · [Français](Showers-fr) · [Español](Showers-es) · [Português](Showers-pt) · [Português (Brasil)](Showers-pt-br) · [Dansk](Showers-da) · [Norsk](Showers-nb) · [Svenska](Showers-sv) · [Íslenska](Showers-is) · [Eesti](Showers-et) · [Lietuvių](Showers-lt) · [Latviešu](Showers-lv) · [Polski](Showers-pl) · [Čeština](Showers-cs) · [Magyar](Showers-hu) · [Română](Showers-ro) · [Русский](Showers-ru) · [Українська](Showers-uk) · [Türkçe](Showers-tr) · [Afrikaans](Showers-af) · [العربية](Showers-ar) · [עברית](Showers-he) · [اردو](Showers-ur) · [हिन्दी](Showers-hi) · [বাংলা](Showers-bn) · **Bahasa Indonesia** · [Tagalog](Showers-tl) · [日本語](Showers-ja) · [한국어](Showers-ko) · [中文](Showers-zh)

# Hujan meteor

*Tab: Hujan meteor.*

[![Hujan meteor](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-5.png)

Katalog hujan meteor yang dipakai oleh semua perhitungan: **45 hujan meteor** dari **IMO Meteor Shower Calendar 2026 dan 2027** (tabel 5 dan 7) ditambah **Sumber Antihelion** (tabel 6), masing-masing dengan **puncak berikutnya**.

## Kolom

| Kolom | Arti |
|---|---|
| Kode | Kode IMO (QUA, PER, GEM, …) |
| Hujan meteor | Nama |
| Aktivitas | Periode aktivitas (hari/bulan – hari/bulan) |
| λ max | Bujur matahari saat puncak (J2000), dari IMO |
| **Puncak berikutnya (UTC)** | Tanggal dan jam puncak berikutnya (lihat di bawah) |
| **Sumber puncak** | *IMO 2026* / *IMO 2027* = tanggal dan jam yang diterbitkan IMO; *IMO 2026 (hari)* = IMO hanya memberikan harinya, jam yang ditampilkan adalah hasil hitungan (*~hh:mm hit.*); *dihitung dari λ* = tidak ada nilai IMO untuk tahun tersebut |
| A.R., Dekl. | Radian saat puncak (*bergerak* untuk Sumber Antihelion) |
| v km/s, r | Kecepatan geosentris dan indeks populasi |
| ZHR | ZHR puncak (*var.* = variabel) |
| Jenis | *visual* atau *radio, siang hari* |
| Aktif hari ini | *ya* jika hujan meteor sedang aktif |

## Puncak berikutnya

Program selalu menampilkan puncak **berikutnya**. Jika IMO sudah menerbitkan kalender tahun itu, program memakai **tanggal dan jam IMO** dari `data/massimi_imo.csv` (2026 dan 2027 sudah disertakan); jika belum, program menghitung saat Matahari mencapai bujur matahari puncak (Meeus, *Astronomical Algorithms*, bab 25, diselesaikan dengan metode Newton).

**Verifikasi:** perhitungan sesuai dengan kalender IMO 2026 dan 2027 dalam selisih beberapa menit di mana IMO memberikan jamnya (mis. Quadrantid 3/1/2026 21:13 dibandingkan 21:00; Geminid 14/12/2027 19:51 dibandingkan 20:00). Pengecualian: kappa Leonid siang hari 2026 satu hari lebih lambat (26/9, bukan 25/9) dan jam eta Aquariid 2027 (15:10 dibandingkan 09:00 IMO) – dalam kasus ini nilai IMO yang dipakai.

**Menambah tahun:** saat IMO menerbitkan kalender baru, tambahkan barisnya ke `data/massimi_imo.csv` (`year;code;MM-DD;hh:mm`, jam dikosongkan jika IMO hanya memberikan harinya). Sampai saat itu puncaknya dihitung.

## Hujan meteor minor dan siang hari

Katalog ini memuat **hujan meteor minor** dari daftar IMO – misalnya Camelopardalid Oktober (OCT, ZHR 5, aktif 5–6 Oktober), Andromedid, gamma Ursae Minorid – dan **hujan meteor radio siang hari** bulan April–Oktober (Piscid April siang hari, Arietid siang hari, zeta Perseid siang hari, beta Taurid siang hari, kappa Leonid siang hari, Sextantid siang hari, …). Meskipun ZHR-nya kecil, semuanya berkontribusi pada [indeks lintasan](Efficiency-Calculation-id#model) dan [Hot yang disarankan](Sky-View-id#hot-yang-disarankan). Untuk hujan meteor radio siang hari IMO tidak memberikan ZHR: jika tidak ada, program memakai nilai kerja 5.

## Profil aktivitas dan pergeseran radian

```
ZHR(λ☉) = ZHR_max · 10^( −B± · |λ☉ − λ_max| )
α = α0 + (dα/dλ)·Δλ      δ = δ0 + (dδ/dλ)·Δλ      Δλ = λ☉ − λ_max
```

ZHR_max, α0, δ0 dan λ_max dari kalender IMO; kemiringan B (berbeda sebelum dan sesudah puncak) serta pergeseran harian dα/dλ, dδ/dλ adalah **nilai kerja** yang ditulis di `data/sciami.csv` (tabel pergeseran IMO belum dimasukkan). *Manual pers. 9 dan 13.* Posisi Sumber Antihelion diinterpolasi secara linear di antara tanggal-tanggal pada tabel 6 IMO (`data/ant_radiante.csv`; aktif 10 Desember – 20 September, ZHR sekitar 4).

## Mengedit katalog

`data/sciami.csv` adalah file teks biasa (pemisah `;`) yang dapat Anda edit: kode, nama, awal dan akhir (MM-DD), λ max, A.R., Dekl., pergeseran, v, r, ZHR, B sebelum/sesudah, jenis (V visual, R radio siang hari). Jika ada baris yang salah, program menampilkan pesan saat mulai dan mengabaikannya.

Sumber: International Meteor Organization – Meteor Shower Calendar 2026 dan 2027, [www.imo.net](https://www.imo.net) (tabel 5, 6 dan 7); Philip G0ISW (laju per jam radio maksimum); Rossano IZ5TEK (scattertek).
