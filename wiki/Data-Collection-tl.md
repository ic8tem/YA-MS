[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-BR) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · **Tagalog** · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-TW)

# Pangongolekta ng data

*Tab: Live at real-time na datos › Pangongolekta ng data.*

[![Pangongolekta ng data](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_4.png)

## Apat na pinagmulan

Kinokolekta ng tab ang mga **spot na meteor scatter** mula sa tatlong telnet stream at mula sa MQTT feed ng PSKReporter, bawat isa sa sarili nitong sub-tab:

| Sub-tab | Default | Mga tala |
|---|---|---|
| **1. DX cluster** | on0dxk.dyndns.org : 8000 | Isang cluster na iyong pinili. Sa ON0DXK, naka-filter ang mga bandang VHF: i-enable ang mga ito gamit ang `set/filter dxbm/pass 6` (pagkatapos ay 4, 2…). |
| **2. RBN** | telnet.reversebeacon.net : 7001 | Reverse Beacon Network (7000 = CW/RTTY, 7001 = FT8). Bihirang mag-decode ang mga skimmer ng mga mode ng MS. |
| **3. DM4X (PSKReporter)** | dm4x.ddns.net : 8500 | Cluster ni DM4X na nagdadala ng mga spot ng **PSKReporter**: dito dumarating ang mga MSK144 decode ng WSJT-X at MSHV. |
| **4. PSKReporter MQTT** | mqtt.pskreporter.info : 1883 | Live na mga spot ng PSKReporter sa pamamagitan ng **MQTT** (serbisyo ni M0LTE): walang login, dala na ng bawat spot ang mga locator ng nagpapadala at ng tumatanggap na istasyon. Mga default na topic: MSK144 sa 6 m, 4 m, 2 m, 1.25 m, 70 cm at FSK441 sa 2 m (`pskr/filter/v2/band/mode/#`); ibinabalik ang mga ito ng *Mga default na topic*. |
| **Mga nakolektang MS spot** | – | Talahanayan ng mga tinanggap na spot, pinakabago muna. |

Bawat stream ay may host, port, mga command na ipinapadala pagkatapos ng login, *Kumonekta muli*, *Kumonekta sa pagsisimula*, isang console at isang linya para magpadala ng command. Isulat sa itaas ang iyong **callsign para sa login**. Ang pinagmulang MQTT ay may host, port, mga topic (isa bawat linya o pinaghihiwalay ng `;`), *Kumonekta muli* at *Kumonekta sa pagsisimula* (naka-off bilang default) at isang console na may mga natanggap na spot; dumaraan ang mga spot nito sa parehong filter. Ipinapakita ng isang strip ang katayuan ng apat na pinagmulan (berdeng tuldok = nakakonekta). Nananatiling bukas ang mga session kapag nagpalit ka ng wika o scheme ng kulay.

## Ang filter (40 % ng window)

- **Opsiyonal na lokal na filter:** agad na itinatapon ang mga linya ng cluster na mas mababa sa **27990.0 kHz** (hindi ipinapakita, hindi iniimbak).
- **Unang pamantayan – karaniwang frequency ng MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Tinatanggap ang spot sa mga window na ito kahit walang pangalan ng mode, maliban kung nagdedeklara ang komento ng ibang propagasyon: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Maaaring i-edit ang mga window at tag.
- **Ikalawang pamantayan – mga mode ng MS:** sa labas ng mga window, o kung may isa sa mga tag na iyon, pinapanatili lamang ang spot kung naglalaman ito ng **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (mga digital mode na ginagamit lamang para sa MS) o **\<MS\>**, sa malaki, maliit o halong titik. Maaaring i-off, idagdag at alisin ang mga salita; may sariling counter ang bawat isa.
- **Mga banda** 28, 50, 70, 144, 222, 432 MHz; **subok ng filter** sa isang idinikit na linya; **mga counter**.

## Mga locator at imbakan

Ang mga nawawalang locator, o locator na 4 na character lamang, ay kinukuha mula sa archive na **CALL3** (`data/call3.txt`, file ng JTDX, mahigit isang milyong callsign), na laging nananaig sa locator na 4 na character. Sine-save ang mga tinanggap na spot sa `data/spot_ms`, isang CSV file bawat araw, at pinagkukunan ng mapang [Live na trapiko](Live-Traffic-tl).
