[English](Contributing-and-Contacts) · [Italiano](Contributing-and-Contacts-it) · [Deutsch](Contributing-and-Contacts-de) · [Nederlands](Contributing-and-Contacts-nl) · [Français](Contributing-and-Contacts-fr) · [Español](Contributing-and-Contacts-es) · [Português](Contributing-and-Contacts-pt) · [Português (Brasil)](Contributing-and-Contacts-pt-br) · [Dansk](Contributing-and-Contacts-da) · [Norsk](Contributing-and-Contacts-nb) · [Svenska](Contributing-and-Contacts-sv) · [Íslenska](Contributing-and-Contacts-is) · [Eesti](Contributing-and-Contacts-et) · [Lietuvių](Contributing-and-Contacts-lt) · [Latviešu](Contributing-and-Contacts-lv) · [Polski](Contributing-and-Contacts-pl) · [Čeština](Contributing-and-Contacts-cs) · [Magyar](Contributing-and-Contacts-hu) · [Română](Contributing-and-Contacts-ro) · [Ελληνικά](Contributing-and-Contacts-el) · [Русский](Contributing-and-Contacts-ru) · [Українська](Contributing-and-Contacts-uk) · [Türkçe](Contributing-and-Contacts-tr) · [Afrikaans](Contributing-and-Contacts-af) · [العربية](Contributing-and-Contacts-ar) · [עברית](Contributing-and-Contacts-he) · [اردو](Contributing-and-Contacts-ur) · [हिन्दी](Contributing-and-Contacts-hi) · [বাংলা](Contributing-and-Contacts-bn) · **Bahasa Indonesia** · [Tagalog](Contributing-and-Contacts-tl) · [日本語](Contributing-and-Contacts-ja) · [한국어](Contributing-and-Contacts-ko) · [中文](Contributing-and-Contacts-zh) · [中文 (繁體)](Contributing-and-Contacts-zh-tw)

# Berkontribusi dan kontak

YA-MS berkembang berkat laporan dari orang-orang yang memakainya di udara. Setiap koreksi dicantumkan beserta sumbernya.

## Kontak

| | |
|---|---|
| Penulis | Costantino Cerrotta **IC8TEM** |
| E-mail | **ccerrotta@gmail.com** · **ic8tem@gmail.com** |
| QRZ.com | [www.qrz.com/db/ic8tem](https://www.qrz.com/db/ic8tem) |
| GitHub | [github.com/ic8tem/YA-MS](https://github.com/ic8tem/YA-MS) – [Issues](https://github.com/ic8tem/YA-MS/issues) · [Releases](https://github.com/ic8tem/YA-MS/releases) |

## Melaporkan masalah

Buka **issue di GitHub** atau kirim e-mail dengan:

- sistem operasi dan versi YA-MS (di judul jendela);
- kedua locator, band dan jam UTC;
- apa yang Anda harapkan dan apa yang Anda lihat (tangkapan layar sangat membantu);
- untuk masalah radar, pesan yang ditampilkan di tab [Fluks radar](Radar-Flux-id).

## Yang paling berguna

- **Laporan dari udara.** Jam dan lintasan di mana efisiensi atau prakiraan terbukti benar – atau salah. Modelnya eksperimental dan perlu dibandingkan dengan QSO nyata serta dengan MCG_MS / MS-Soft.
- **Perbandingan RMOB.** Nilai faktor stasiun K dan eksponen k yang Anda temukan melalui [perbandingan RMOB](Experimental-Forecasts-id#perbandingan-rmob), beserta band dan stasiun Anda.
- **Data dengan sumber.** Pergeseran radian yang lebih baik, profil aktivitas, tanggal puncak IMO yang baru (`data/massimi_imo.csv`), data antena: sertakan sumbernya dan sumber itu akan dikutip.
- **Perubahan grafik radar.** Jika format grafik Collm berubah, salinan gambarnya (`data/radar/`) membantu mengkalibrasi ulang pembacaan.

## Terjemahan

Terjemahan antarmuka adalah file teks biasa di **`data/lingue/<code>.txt`** (UTF-8) dan **siapa pun dapat memperbaikinya**:

```
<Italian text><TAB><translation>
```

- Satu entri per baris; baris yang diawali `#` adalah komentar.
- Di kedua kolom, dua karakter `\n` berarti baris baru.
- Pertahankan placeholder `{0}`, `{1}`, … beserta formatnya (mis. `{0:F1}`, `{3:+0;-0}`), dalam urutan yang dibutuhkan bahasa Anda.
- Entri yang tidak ada atau kosong ditampilkan dalam bahasa Italia. Daftar semua kunci adalah `data/lingue/chiavi.txt` (dibuat oleh `tools/estrai_chiavi.py`, jangan diedit).

Edit file di folder `data/lingue` pada instalasi Anda lalu jalankan ulang YA-MS (atau ganti bahasa) untuk melihat hasilnya. Karena file-file ini **diganti oleh versi yang lebih baru pada setiap pembaruan**, mohon **kirimkan juga koreksi Anda** – lewat e-mail atau sebagai pull request di GitHub (`data/lingue/`) – agar masuk ke rilis berikutnya.

Wiki ini tersedia dalam English, Italiano, Deutsch, Nederlands, Français, Español, Português, Dansk, Norsk, Svenska, Íslenska, Eesti, Lietuvių, Latviešu, Русский, Українська, Türkçe, Afrikaans, العربية, עברית, اردو, हिन्दी, বাংলা, Bahasa Indonesia, Tagalog, 日本語, 한국어, 中文; koreksi untuk halaman wiki juga sangat disambut.
