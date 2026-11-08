**English** · [Русский](Grid-Square-Map-ru) · [Deutsch](Grid-Square-Map-de) · [日本語](Grid-Square-Map-ja)

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
