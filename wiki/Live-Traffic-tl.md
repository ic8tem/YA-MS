[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · [Íslenska](Live-Traffic-is) · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · **Tagalog** · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Live na trapiko

*Tab: Live at real-time na datos › Live na trapiko.*

[![Live na trapiko](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ano ang ipinapakita

Isang **azimuthal equidistant na mapa** na nakasentro sa iyong istasyon (distansiya mula sa gitna = totoong distansiya, anggulo = azimuth) na may **lahat ng trapikong meteor scatter** na nakolekta ng [Pangongolekta ng data](Data-Collection-tl). Para sa bawat contact, iginuguhit ng programa ang:

- ang **landas** sa pagitan ng dalawang istasyon, sa kulay ng banda nito: 28 MHz kayumanggi, 50 MHz berde, 70 MHz cyan, 144 MHz kahel, 222 MHz rosas, 432 MHz biyoleta;
- ang dalawang **istasyon** sa magkabilang dulo ng landas;
- ang **ulap**: kung saan nakatipon ang pinakamalamang na bakas ng meteor para sa landas na iyon at sa oras na iyon.

Itinatapon ang mga spot na may istasyong **nasa labas ng mapa**. Ang spot na **kararating lamang** (hindi lalampas sa 3 minuto) ay **kumikislap nang isang minuto**, kaya agad na napapansin ang bagong aktibidad.

Ipakita kung sino ang nakikinig: mga tatsulok na kulay ng banda ang nagmamarka sa mga istasyong, ayon sa PSKReporter, tumatanggap ng MSK144, FSK441, PSK2K o JTMS sa 28, 50, 70, 144 at 432 MHz sa napiling panahon. Ang pag-click sa tatsulok ay nagpapakita ng call sign, locator, mga mode at huling spot. Dapat nakakonekta ang daloy na MQTT sa tab na Pangongolekta ng data.

Pati ang mga aktibong monitor sa mapa ng PSKReporter: mga hungkag na tatsulok para sa mga istasyong lumalabas sa mapa ng pskreporter.info sa MSK144, FSK441, PSK2K o JTMS pero wala pang natatanggap na spot (ang MQTT ay nagpapadala lang ng mga istasyong may natatanggap). Tinatanong ng YA-MS ang serbisyong pang-query ng PSKReporter nang isang mode bawat pagkakataon, tuwing 3 minuto, kaya bawat mode ay naa-update tuwing 12 minuto, ayon sa patakaran ng serbisyo. Ang click sa tatsulok ay nagpapakita ng callsign, locator, programang pang-decode at oras na aktibo ang monitor. Naka-on mula sa simula.

Isinusulat sa mapa ang mga callsign ng dalawang istasyon ng bawat spot, isang beses bawat istasyon. Mapipili ang projection: azimuthal (nakasentro sa iyong istasyon) o Mercator. Ipinaliliwanag ng tooltip sa kolumnang Ulap ang kahulugan nito.

Ipinapakita ang mga spot ng lahat ng banda, pati ng mga bandang hindi pinili sa Pagkolekta ng data (hindi ito iniimbak). Hindi ipinapakita ang mga CW spot at ang mga spot sa pagitan ng mga istasyong masyadong malapit, kung itinatapon ang mga ito sa Pagkolekta ng data.

## Paano kinakalkula ang ulap

Para sa bawat spot, binubuo ng programa ang landas sa pagitan ng dalawang locator (parehong heometriya gaya ng sa sarili mong landas, tingnan ang [Heometriya at path loss](Geometry-and-Path-Loss-tl)) at, sa oras ng spot, pinagsasama-sama punto por punto ng E layer ang **mga kontribusyon ng specular na repleksiyon ng bawat aktibong shower**, na tinimbang ayon sa ZHR nito – parehong kalkulasyon ng **mga PREV na sona** ng [kalangitan](Sky-View-tl). Para sa bawat panig ng landas na may hindi bababa sa 15 % ng kabuuan, ang ulap ay isang **ellipse**: gitna sa tinimbang na mean ng mga punto, mga semi-axis na 1.5 ulit ng square root ng mga eigenvalue ng kanilang pagkakalat, pangunahing axis sa direksiyon ng pangunahing eigenvector. Kapag walang shower na nag-aambag (sporadic na meteor lamang), ang mga ulap ay ang dalawang klasikong **hot spot**, na iginuhit nang putol-putol. Nasa kabanata 10 ng manwal ng kalkulasyon ang buong mga ekwasyon.

## Mga kontrol

| Kontrol | Kahulugan |
|---|---|
| **Radius ng mapa** | 600–3500 km mula sa iyong istasyon. |
| **Mga spot na ipapakita** | Huling 15 o 30 minuto, huling oras, huling 3 oras, huling 24 oras. |
| **Talahanayan** | Mga contact sa mapa, pinakabago muna, sa kulay ng banda; ibinibigay ng *Ulap* ang bahagi ng mga repleksiyon sa pangunahing panig, o *sporadic*. |
| **Click** | Sa isang landas o sa isang hanay ng talahanayan: naha-highlight ang contact at ipinapakita ng kahon ang locator ng gitna ng ulap, ang bahagi nito, laki at axis. |
