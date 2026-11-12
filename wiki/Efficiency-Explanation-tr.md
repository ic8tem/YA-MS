[English](Efficiency-Explanation) · [Italiano](Efficiency-Explanation-it) · [Deutsch](Efficiency-Explanation-de) · [Nederlands](Efficiency-Explanation-nl) · [Français](Efficiency-Explanation-fr) · [Español](Efficiency-Explanation-es) · [Português](Efficiency-Explanation-pt) · [Português (Brasil)](Efficiency-Explanation-pt-br) · [Dansk](Efficiency-Explanation-da) · [Norsk](Efficiency-Explanation-nb) · [Svenska](Efficiency-Explanation-sv) · [Íslenska](Efficiency-Explanation-is) · [Eesti](Efficiency-Explanation-et) · [Lietuvių](Efficiency-Explanation-lt) · [Latviešu](Efficiency-Explanation-lv) · [Polski](Efficiency-Explanation-pl) · [Čeština](Efficiency-Explanation-cs) · [Magyar](Efficiency-Explanation-hu) · [Română](Efficiency-Explanation-ro) · [Ελληνικά](Efficiency-Explanation-el) · [Русский](Efficiency-Explanation-ru) · [Українська](Efficiency-Explanation-uk) · **Türkçe** · [Afrikaans](Efficiency-Explanation-af) · [العربية](Efficiency-Explanation-ar) · [עברית](Efficiency-Explanation-he) · [اردو](Efficiency-Explanation-ur) · [हिन्दी](Efficiency-Explanation-hi) · [বাংলা](Efficiency-Explanation-bn) · [ไทย](Efficiency-Explanation-th) · [Bahasa Indonesia](Efficiency-Explanation-id) · [Tagalog](Efficiency-Explanation-tl) · [日本語](Efficiency-Explanation-ja) · [한국어](Efficiency-Explanation-ko) · [中文](Efficiency-Explanation-zh) · [中文 (繁體)](Efficiency-Explanation-zh-tw)

# Verim hesabının açıklaması

*Sekme: Teknik belgeler › Verim hesabının açıklaması.*

[![Verim hesabının açıklaması](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-3_3.png)

Program içinde açık renkli bir sayfa olarak gösterilen teknik bir belge: *"Come YA-MS calcola l'efficienza di uno sciame"* (YA-MS bir yağmurun verimini nasıl hesaplar). Verimin nasıl elde edildiğini **adım adım** açıklar ve her adım için **nereden geldiğini** belirtir. Program onu, hesap kılavuzu gibi, **arayüz dilinde** (36 dilin tümünde) gösterir; bu wiki içeriğini ayrıca [Verim hesabı](Efficiency-Calculation-tr#model) ve [Geometri ve yol kaybı](Geometry-and-Path-Loss-tr) sayfalarında verir.

## Etiketler

Her adım renkli bir etiket taşır:

| Etiket | Renk | Anlamı |
|---|---|---|
| **FONTE** (kaynak) | mavi | adım, alıntılanan bir kaynağı ele alır; parantez içindeki sayı sondaki listeye karşılık gelir |
| **RILIEVO** (doğrulama) | yeşil | program ile kaynaklar arasında karşılaştırma ve sonucu |
| **SCELTA** (seçim) | turuncu | programın bir kaynaktan alınmamış bir seçimi: havadaki deneyimle denetlenmeli |

## Bölümler

| Bölüm | İçerik |
|---|---|
| 1. Giriş | Amaç, etiketler, verimin anlamı (OH5IY, MCG_MS; YA-MS gerçek yolu kullanır) |
| 2. Yansımalar nerede olur: E katmanı | 80–120 km'deki izler; iz yüksekliği = Collm histogramının modu (doğrulama: 5/11/2026'da 89,5 km) |
| 3. Yol geometrisi | Dünya ve orta nokta; anten elevasyonu (makale formülü); ortak bölge ve sınırları; Hot A / Hot B; anten lobu (DL6WU, Kraus, W4RNL) |
| 4. Yağmurun radyantı | Radyant konumu (IMO 2026/2027), tepe tarihi (IMO ya da güneş boylamı), etkinlik profili |
| 5. Yansıma koşulu | Aynasal yansıma (McKinley), 0,05 rad Gauss toleransı, en iyi yön (SM6FHZ), DH9GCD formülü |
| 6. Tek bir noktadan verime | Her 15 km'de yansıma noktaları, her noktanın ağırlığı, yüzde; QTFGUI (DJ5HG) ile karşılaştırma |
| 7. Sonuçların okunması | A / B tarafı, yol endeksi, radyant renkleri, PREV bölgeleri, antenden görülen kesit |
| 8. Çalışma frekansı ve yol kaybı | λ³ / λ² kuralları, radardan amatör banda, yol kaybı referansları |
| 9. Bilinen sınırlar | Yalnızca underdense izler, izotropik antenler, çalışma değerleri |
| 10. Kaynaklar | 17 numaralı kaynak |

## Düğmeler

| Düğme | Ne yapar |
|---|---|
| **Word'e aktar (.docx)...** | `data/efficienza_spiegazione.docx` dosyasının bir kopyasını seçtiğiniz yere kaydeder (önerilen ad *YA-MS - calcolo dell'efficienza.docx*) |
| **Word'de aç** | Aynı `.docx` dosyasını Word belgeleri için varsayılan programla açar (Word, LibreOffice, …) |

## Dosyalar

| Dosya | İçerik |
|---|---|
| `data/efficienza_spiegazione.txt` | Sekmede gösterilen metin, her satırda bir blok (`TITLE`, `SUB`, `H1`, `H2`, `P`, `TAG|FONTE|…`, `TAG|RILIEVO|…`, `TAG|SCELTA|…`, `EQ`, `LI`, `SRC`) |
| `data/efficienza_spiegazione.docx` | Word sürümü |
| `data/spiegazione/efficienza_spiegazione_<code>.txt` / `.docx` | Aynı belge diğer 35 dilde (ör. `_en`, `_de`, `_pt-br`) |
| `doc/YA-MS_manuale_calcoli.docx` | **Hesap kılavuzu** (İtalyanca): tüm denklemler (Word denklem düzenleyicisi), numaralı, kaynaklarıyla |
| `doc/manuali/YA-MS_manuale_calcoli_<code>.docx` | Diğer 35 dilde hesap kılavuzu |

İki belge kaynak koddan `tools/build_spiegazione.py data [code]` ve `node tools/build_manuale.js <file.docx> [code]` ile yeniden üretilir. Çeviriler `tools/traduzioni_doc/` klasöründedir (`tools/build_documenti.sh` tüm dilleri yeniden üretir).
