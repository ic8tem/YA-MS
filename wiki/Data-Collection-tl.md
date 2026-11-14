[English](Data-Collection) · [Italiano](Data-Collection-it) · [Deutsch](Data-Collection-de) · [Nederlands](Data-Collection-nl) · [Français](Data-Collection-fr) · [Español](Data-Collection-es) · [Português](Data-Collection-pt) · [Português (Brasil)](Data-Collection-pt-br) · [Dansk](Data-Collection-da) · [Norsk](Data-Collection-nb) · [Svenska](Data-Collection-sv) · [Íslenska](Data-Collection-is) · [Eesti](Data-Collection-et) · [Lietuvių](Data-Collection-lt) · [Latviešu](Data-Collection-lv) · [Polski](Data-Collection-pl) · [Čeština](Data-Collection-cs) · [Magyar](Data-Collection-hu) · [Română](Data-Collection-ro) · [Ελληνικά](Data-Collection-el) · [Русский](Data-Collection-ru) · [Українська](Data-Collection-uk) · [Türkçe](Data-Collection-tr) · [Afrikaans](Data-Collection-af) · [العربية](Data-Collection-ar) · [עברית](Data-Collection-he) · [اردو](Data-Collection-ur) · [हिन्दी](Data-Collection-hi) · [বাংলা](Data-Collection-bn) · [ไทย](Data-Collection-th) · [Bahasa Indonesia](Data-Collection-id) · **Tagalog** · [日本語](Data-Collection-ja) · [한국어](Data-Collection-ko) · [中文](Data-Collection-zh) · [中文 (繁體)](Data-Collection-zh-tw)

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
| **5. WSJT-X / JTDX / MSHV sa UDP** | 127.0.0.1 : 2237 → 2238 | Gaya ng sa LIVETROPOVHF: nakikinig ang programa sa mga mensaheng UDP ng digital na programa (sa WSJT-X: Settings, Reporting, UDP Server 127.0.0.1 port 2237) at inuulit ang mga ito nang walang pagbabago sa forwarding port para sa ibang programa (GridTracker, JTAlert, log). Bawat na-decode na istasyon ay nagiging spot na narinig ng iyong istasyon; ang mga pansarang mensahe (RR73, 73, RRR) sa pagitan ng dalawang ibang istasyon ay nagiging ruta ng kanilang QSO. Dumaraan ang mga spot sa parehong mga filter gaya ng iba. |
| **Mga nakolektang MS spot** | – | Talahanayan ng mga tinanggap na spot, pinakabago muna. |

Bawat stream ay may host, port, mga command na ipinapadala pagkatapos ng login, *Kumonekta muli*, *Kumonekta sa pagsisimula*, isang console at isang linya para magpadala ng command. Isulat sa itaas ang iyong **callsign para sa login**. Ang pinagmulang MQTT ay may host, port, mga topic (isa bawat linya o pinaghihiwalay ng `;`), *Kumonekta muli* at *Kumonekta sa pagsisimula* (naka-off bilang default) at isang console na may mga natanggap na spot; dumaraan ang mga spot nito sa parehong filter. Ipinapakita ng isang strip ang katayuan ng apat na pinagmulan (berdeng tuldok = nakakonekta). Nananatiling bukas ang mga session kapag nagpalit ka ng wika o scheme ng kulay.

## Ang filter (40 % ng window)

- **Opsiyonal na lokal na filter:** agad na itinatapon ang mga linya ng cluster na mas mababa sa **27990.0 kHz** (hindi ipinapakita, hindi iniimbak).
- Agad na itinatapon ang mga spot na CW (CW o WPM sa komento, o 28000-28070 kHz): hindi lumalabas sa console at hindi sine-save, maliban kung may markang <MS>. Maaaring patayin ang kahon.

Database ng CALL3 na may mga patakaran ng LIVETROPOVHF. Dina-download ng "I-update ngayon" ang CALL3.TXT mula sa MMMonVHF (hindi bababa sa 100,000 wastong linya, nananatili ang nauna sa data/call3.bak); sa "Kusang mag-update tuwing 12 oras" ginagawa ito sa pagsisimula. Sa ibabaw ng file, ayon sa pagkakasunod: mano-manong entry (data/CALL3-MANUALE.TXT), pagwawasto mula sa cluster (ang 6-character na locator na idinedeklara ng nag-spot para sa sarili), idinagdag na file (data/CALL3-AGGIUNTE), saka ang CALL3.TXT at mga 6-character na locator na natutunan nang live (data/LOC6.TXT). Ang natanggap na 4-character na locator, o nagtatapos sa LL o MM, ay pinapalitan ng 6-character mula sa database; ang mga portable (may slash) sa eksaktong entry lamang.

Huling pinagmulan, gaya ng sa LIVETROPOVHF: para sa mga callsign na walang 6-character na locator sa anumang ibang pinagmulan, awtomatikong nagtatanong ang programa tuwing 30 minuto sa pampublikong API ng G7VRD (api.g7vrd.co.uk), nang tig-40 callsign; bawat callsign hanggang minsan sa isang araw. 6-character na locator lang ang tinatanggap, hindi ang gitna ng parisukat (LL o MM), sa parehong parisukat ng natanggap. Nasa data/CALL3-G7VRD.TXT ang mga resulta at, gaya ng lahat ng pagwawasto, isinusulat din sa data/call3.txt.

Kasunod ng G7VRD ang layer ng JTDX (data/grid_data.bin, mga 365,000 callsign): para lamang ito sa mga callsign na walang 6-character na locator sa lahat ng ibang pinagmulan, sa parehong square lamang ng natanggap, at hindi kailanman isinusulat sa data/call3.txt.
- Ang mga spot sa pagitan ng mga istasyong mas malapit sa 500 km ay agad na itinatapon, dahil sa layong iyon ang ugnayan ay direkta o troposperiko at hindi meteor scatter: hindi lumalabas sa console at hindi iniimbak. Kung kulang ang locator, nananatili ang spot. Ang layo ay napapalitan sa ilalim ng kahon.
- **Unang pamantayan – karaniwang frequency ng MS:** 50190–50300, 70100–70400, 144290–144399 kHz. Tinatanggap ang spot sa mga window na ito kahit walang pangalan ng mode, maliban kung nagdedeklara ang komento ng ibang propagasyon: `<TR> <AS> <ACS> <AU> <ES> <FAI> <F2>`. Maaaring i-edit ang mga window at tag.
- **Ikalawang pamantayan – mga mode ng MS:** sa labas ng mga window, o kung may isa sa mga tag na iyon, pinapanatili lamang ang spot kung naglalaman ito ng **MSK144, FSK441, FSK41, PSK2K, JTMS, JT6M** (mga digital mode na ginagamit lamang para sa MS) o **\<MS\>**, sa malaki, maliit o halong titik. Maaaring i-off, idagdag at alisin ang mga salita; may sariling counter ang bawat isa.
- **Mga banda** 28, 50, 70, 144, 222, 432 MHz; **subok ng filter** sa isang idinikit na linya; **mga counter**.

## Mga locator at imbakan

Ang mga nawawalang locator, o locator na 4 na character lamang, ay kinukuha mula sa archive na **CALL3** (`data/call3.txt`, file ng JTDX, mahigit isang milyong callsign), na laging nananaig sa locator na 4 na character. Sine-save ang mga tinanggap na spot sa `data/spot_ms`, isang CSV file bawat araw, at pinagkukunan ng mapang [Live na trapiko](Live-Traffic-tl).
