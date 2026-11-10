[English](GRAVES-Radar) · [Italiano](GRAVES-Radar-it) · [Deutsch](GRAVES-Radar-de) · [Nederlands](GRAVES-Radar-nl) · [Français](GRAVES-Radar-fr) · [Español](GRAVES-Radar-es) · [Português](GRAVES-Radar-pt) · [Dansk](GRAVES-Radar-da) · [Norsk](GRAVES-Radar-nb) · [Svenska](GRAVES-Radar-sv) · [Íslenska](GRAVES-Radar-is) · [Eesti](GRAVES-Radar-et) · [Lietuvių](GRAVES-Radar-lt) · [Latviešu](GRAVES-Radar-lv) · [Русский](GRAVES-Radar-ru) · [Українська](GRAVES-Radar-uk) · [Türkçe](GRAVES-Radar-tr) · [Afrikaans](GRAVES-Radar-af) · [العربية](GRAVES-Radar-ar) · [עברית](GRAVES-Radar-he) · [اردو](GRAVES-Radar-ur) · [हिन्दी](GRAVES-Radar-hi) · [বাংলা](GRAVES-Radar-bn) · **Bahasa Indonesia** · [Tagalog](GRAVES-Radar-tl) · [日本語](GRAVES-Radar-ja) · [한국어](GRAVES-Radar-ko) · [中文](GRAVES-Radar-zh)

# Radar GRAVES

*Tab: Langsung dan data waktu nyata › Radar GRAVES.*

[![Radar GRAVES](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_3.png)

## Apa itu GRAVES

**GRAVES** adalah radar Prancis yang memancarkan **CW di 143,050 MHz** dari **Broye-lès-Pesmes** (47,348° LU 5,515° BT, locator **JN27SI**, sekitar 200 m dpl; Wikipedia). Jejak meteor di zona yang terlihat baik oleh GRAVES maupun oleh Anda memantulkan sinyalnya kepada Anda melalui **forward scatter**: Anda mendengar *ping* pendek di dekat carrier. Dengan cara inilah para pengamat **RMOB** di 143,050 MHz menghitung meteor jam demi jam, dan ini adalah sinyal uji gratis yang selalu menyala untuk stasiun meteor scatter 2 m Anda.

Tab ini memperlakukan **GRAVES → Anda** sebagai lintasan meteor scatter tersendiri: dengan fungsi yang sama seperti lintasan utama (ketinggian jejak, elevasi lobus dan jarak hot spot yang sama) tab ini menghitung efisiensi hujan meteor, Hot yang disarankan dan zona PREV, lalu memeriksa apakah zona itu **berada di dalam berkas GRAVES** dan **kapan** berkas meneranginya.

## Bilah atas

| Kontrol | Fungsinya |
|---|---|
| **Sekarang** | Mengembalikan perhitungan ke waktu nyata: tanggal hari ini dan penggeser jam di nol (tab mengikuti *Tanggal perhitungan* dan *Jam*). |
| **Jadikan GRAVES sebagai DX** | Stasiun DX menjadi GRAVES (JN27SI, ketinggian 200 m) dan lintasan utama dihitung ulang: semua tab lain kemudian menampilkan lintasan GRAVES. |
| **Urutan berkas** | *0,8 s per langkah · siklus 4,8 s (PE1ITR 2021)* (bawaan) atau *3,2 s per langkah · siklus 19,2 s (PE1ITR 2007)*. |

## Empat kartu

| Kartu | Isi |
|---|---|
| **ZONA BERGUNA DALAM BERKAS GRAVES** | *Ya · sektor X* dengan azimut dan elevasi hot spot yang disarankan dilihat dari GRAVES serta langkahnya (1–6); atau *Tidak: di luar sektor* / *Tidak: di bawah cakrawala GRAVES* / *Tidak: di atas berkas (sekitar 25°)* |
| **EFISIENSI LINTASAN GRAVES → ANDA SEKARANG** | Indeks lintasan Σ ZHR × efisiensi, hujan meteor terbaik, sisi dominan A/B, dan *gema yang diharapkan ≈ …/jam* (eksperimental, lihat di bawah) |
| **LINTASAN** | Jarak ke GRAVES; antena ke arah Hot yang disarankan (azimut dan elevasi); azimut langsung GRAVES |
| **LINTASAN BERKAS BERIKUTNYA DI ATAS ZONA** | *sekarang · sisa … s* atau *dalam … s*, langkahnya (mis. *B4*), tiga waktu berikutnya (detik dalam menit) dan fraksi jejak yang tertangkap |

Jika tidak ada hujan meteor yang berguna pada saat itu, program menampilkan hot spot yang **paling cocok dengan berkas** (di dalam sektor, paling dekat ke selatan) dan menyatakannya.

## Langit dilihat dari GRAVES

Menurut PE1ITR dan wiki Bolidozor, **empat larik bertahap (phased array)** mencakup langit selatan dari azimut **90° hingga 270°** dalam empat **sektor 45°**:

| Sektor | Azimut dari GRAVES |
|---|---|
| D | 90°–135° |
| C | 135°–180° |
| B | 180°–225° |
| A | 225°–270° |

Setiap sektor dibagi menjadi **6 langkah 7,5°**, bernomor 1 sampai 6 dari azimut terendah, yang diterangi satu demi satu, **pada saat yang sama di keempat sektor**. Lebar berkas sekitar **25° dalam elevasi**: pada ketinggian jejak berkas mencakup cincin berwarna di antara kedua lingkaran putus-putus (*cakrawala berkas*). Pada gambar: titik oranye/merah muda = zona PREV lintasan GRAVES → Anda, garis hijau = arah stasiun Anda, garis merah = dari stasiun Anda ke hot spot yang disarankan; langkah yang sedang diterangi disorot.

## Rekonstruksi kronologis

*REKONSTRUKSI KRONOLOGIS · tanggal UTC* (hari yang sama dengan tabel 24 jam): untuk setiap jam, efisiensi lintasan GRAVES → Anda, hujan meteor paling menguntungkan dan jendela berguna (*hh:00 → hh:00 UTC · n h*), dengan nilai maksimum (*maks Σ … pada hh:30*) dan penanda merah *sekarang*. Di bawahnya, **rincian detik-detik berikutnya**: enam langkah sektor, langkah yang menerangi zona berguna, dan *gema mungkin (+0,3 s jejak)*.

### Pewaktuan berkas

Urutannya terikat pada **UTC** (PE1ITR): langkah yang sedang diterangi dihitung dari detik sejak 00:00 UTC modulo siklus (86 400 s adalah kelipatan 4,8 s maupun 19,2 s). Stasiun komando kadang menggeser urutan beberapa langkah, sehingga rincian ini adalah **prediksi yang harus dikonfirmasi dengan mendengarkan**. Label kuning **jam PC tersinkronisasi** mengingatkan Anda: sinkronkan PC Anda dengan server NTP (kesalahan paling banyak beberapa persepuluh detik).

### Faktor deteksi

Sebuah jejak hanya terdengar jika berkas meneranginya selama jejak itu ada:

```math
p \approx \min\left(1,\ \frac{t_{step} + \tau}{T_{cycle}}\right):\qquad 2021:\ \frac{0{.}8+0{.}3}{4{.}8} \approx 23\ \%,\qquad 2007:\ \frac{3{.}2+0{.}3}{19{.}2} \approx 18\ \%
```

0,3 s adalah durasi khas jejak underdense pada 143 MHz – nilai tetap, *pilihan program* (aturan λ² SM6FHZ menskalakan durasi antarband tetapi tidak memberikan nilai awal).

### Gema yang diharapkan (eksperimental)

```math
N_{GRAVES} \approx N_{prev}(f_{fc})\left(\frac{f_{fc}}{143{.}05}\right)^{k}\frac{I_{GRAVES}+10}{I_{DX}+10}\; p
```

Prakiraan dari [Prakiraan eksperimental](Experimental-Forecasts-id) (yang sudah memuat faktor stasiun K) diskalakan dari frekuensinya f_fc ke 143,050 MHz dengan aturan SM6FHZ (eksponen k yang sama), dikoreksi dengan rasio indeks hujan meteor kedua lintasan (konstanta 10 mewakili latar sporadis, seperti pada prakiraan) dan dikalikan dengan faktor deteksi. Hanya indikatif: bandingkan dengan pengamat RMOB.

## Cara mendengar ping GRAVES

| Langkah | Apa yang harus dilakukan |
|---|---|
| Penerima | **USB di 143,049 MHz** (nada sekitar 1 kHz) atau 143,050 MHz, **AGC lambat atau mati**, lebar pita audio **minimal 2,4 kHz** |
| Antena | Ke arah **hot spot yang disarankan** untuk lintasan GRAVES → Anda (kartu *LINTASAN*), pada **elevasi rendah** |
| Waterfall | Ping berupa **garis pendek di dekat carrier**; jejak panjang (overdense) lebih lebar dan menunjukkan Doppler |
| Penghitungan | RMOB memakai GRAVES untuk hitungan meteor per jam: **bandingkan ping Anda dengan pengamat di 143,050 MHz** ([Prakiraan eksperimental](Experimental-Forecasts-id#perbandingan-rmob)) |

## Sumber

1. Rob Hardenberg **PE1ITR**, *"The 143.050 MHz Graves Radar, a VHF Beacon"* (DUBUS 4/2007) dan *"Graves Radar Update April 2021"* – [pe1itr.com/graves](https://pe1itr.com/graves)
2. Wiki **Bolidozor**, "Graves" – larik, sektor dan pewaktuan berkas
3. **Wikipedia**, "GRAVES (system)" – pemancar di Broye-lès-Pesmes (47,348° LU 5,515° BT)
4. **RMOB** – pengamat di 143,050 MHz ([rmob.org](https://www.rmob.org))
5. **YAEC** karya IC8TEM – tab GRAVES Radar (rancangan awal yang menjadi asal tab ini)
