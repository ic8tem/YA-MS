[English](Grid-Square-Map) · [Italiano](Grid-Square-Map-it) · [Deutsch](Grid-Square-Map-de) · [Nederlands](Grid-Square-Map-nl) · [Français](Grid-Square-Map-fr) · [Español](Grid-Square-Map-es) · [Português](Grid-Square-Map-pt) · [Português (Brasil)](Grid-Square-Map-pt-br) · [Dansk](Grid-Square-Map-da) · [Norsk](Grid-Square-Map-nb) · [Svenska](Grid-Square-Map-sv) · [Íslenska](Grid-Square-Map-is) · [Eesti](Grid-Square-Map-et) · [Lietuvių](Grid-Square-Map-lt) · [Latviešu](Grid-Square-Map-lv) · [Polski](Grid-Square-Map-pl) · [Čeština](Grid-Square-Map-cs) · [Magyar](Grid-Square-Map-hu) · [Română](Grid-Square-Map-ro) · [Ελληνικά](Grid-Square-Map-el) · [Русский](Grid-Square-Map-ru) · [Українська](Grid-Square-Map-uk) · [Türkçe](Grid-Square-Map-tr) · [Afrikaans](Grid-Square-Map-af) · [العربية](Grid-Square-Map-ar) · [עברית](Grid-Square-Map-he) · [اردو](Grid-Square-Map-ur) · [हिन्दी](Grid-Square-Map-hi) · [বাংলা](Grid-Square-Map-bn) · [ไทย](Grid-Square-Map-th) · **Bahasa Indonesia** · [Tagalog](Grid-Square-Map-tl) · [日本語](Grid-Square-Map-ja) · [한국어](Grid-Square-Map-ko) · [中文](Grid-Square-Map-zh) · [中文 (繁體)](Grid-Square-Map-zh-tw)

# Peta kotak

*Tab: Peta kotak.*

[![Peta kotak](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-6.png)

Kotak Maidenhead (4 karakter) yang sudah Anda **kerjakan** dan yang **terkonfirmasi**, dibaca dari file ADIF log Anda, pada peta Eropa – **satu sub-tab per band: 50, 70, 144, 222 dan 432 MHz**.

## Kontrol

| Kontrol | Fungsinya |
|---|---|
| **Muat file ADIF...** | Membaca file `.adi` / `.adif`. ADIF baru **menggantikan** data sebelumnya. |
| **Hapus memori** | Menghapus semua kotak yang dimuat dari ADIF (meminta konfirmasi). |
| Mouse | **Roda = zoom, seret = geser, mouse di atas kotak = QSO** (hingga enam callsign dengan tanggal, *(terkonfirmasi)* bila sudah terkonfirmasi) |

Setelah dimuat, status menampilkan *… QSO dibaca, … kotak-QSO di band 50-432 MHz, … QSO dibuang (band lain atau tanpa kotak)*. Setiap peta band memiliki keterangan *… kotak dikerjakan, … terkonfirmasi*.

| Warna | Arti |
|---|---|
| Oranye | sudah dikerjakan |
| Hijau | terkonfirmasi (QSL atau LoTW) |

## Cara ADIF dibaca

- Field yang dipakai: `CALL`, `GRIDSQUARE`, `VUCC_GRIDS`, `BAND`, `FREQ`, `QSO_DATE`, `QSL_RCVD`, `LOTW_QSL_RCVD` (spesifikasi ADIF).
- Band dari `BAND`, atau dari frekuensi: 50–54 MHz = 6 m, 69,9–71,5 MHz = 4 m, 144–148 MHz = 2 m, 219–225 MHz = 1,25 m, 420–450 MHz = 70 cm.
- Sebuah kotak **terkonfirmasi** jika paling sedikit satu QSO di dalamnya memiliki `QSL_RCVD = Y` atau `LOTW_QSL_RCVD = Y`.
- Kotak-kotak disimpan di `data/adif_quadrati.csv` sampai Anda memuat file lain atau menekan **Hapus memori**.

YA-MS **tidak** tersambung ke LoTW: ekspor ADIF dari program log Anda (atau dari LoTW) lalu muat di sini.
