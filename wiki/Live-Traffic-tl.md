**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Live na trapiko

*Tab: Live at real-time na datos › Live na trapiko.*

[![Live na trapiko](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Ano ang ipinapakita

Isang **azimuthal equidistant na mapa** na nakasentro sa iyong istasyon (distansiya mula sa gitna = totoong distansiya, anggulo = azimuth) na may **lahat ng trapikong meteor scatter** na nakolekta ng [Pangongolekta ng data](Data-Collection-tl). Para sa bawat contact, iginuguhit ng programa ang:

- ang **landas** sa pagitan ng dalawang istasyon, sa kulay ng banda nito: 28 MHz kayumanggi, 50 MHz berde, 70 MHz cyan, 144 MHz kahel, 222 MHz rosas, 432 MHz biyoleta;
- ang dalawang **istasyon** sa magkabilang dulo ng landas;
- ang **ulap**: kung saan nakatipon ang pinakamalamang na bakas ng meteor para sa landas na iyon at sa oras na iyon.

Itinatapon ang mga spot na may istasyong **nasa labas ng mapa**. Ang spot na **kararating lamang** (hindi lalampas sa 3 minuto) ay **kumikislap nang isang minuto**, kaya agad na napapansin ang bagong aktibidad.

## Paano kinakalkula ang ulap

Para sa bawat spot, binubuo ng programa ang landas sa pagitan ng dalawang locator (parehong heometriya gaya ng sa sarili mong landas, tingnan ang [Heometriya at path loss](Geometry-and-Path-Loss-tl)) at, sa oras ng spot, pinagsasama-sama punto por punto ng E layer ang **mga kontribusyon ng specular na repleksiyon ng bawat aktibong shower**, na tinimbang ayon sa ZHR nito – parehong kalkulasyon ng **mga PREV na sona** ng [kalangitan](Sky-View-tl). Para sa bawat panig ng landas na may hindi bababa sa 15 % ng kabuuan, ang ulap ay isang **ellipse**: gitna sa tinimbang na mean ng mga punto, mga semi-axis na 1.5 ulit ng square root ng mga eigenvalue ng kanilang pagkakalat, pangunahing axis sa direksiyon ng pangunahing eigenvector. Kapag walang shower na nag-aambag (sporadic na meteor lamang), ang mga ulap ay ang dalawang klasikong **hot spot**, na iginuhit nang putol-putol. Nasa kabanata 10 ng manwal ng kalkulasyon ang buong mga ekwasyon.

## Mga kontrol

| Kontrol | Kahulugan |
|---|---|
| **Radius ng mapa** | 600–3500 km mula sa iyong istasyon. |
| **Mga spot na ipapakita** | Huling 15 o 30 minuto, huling oras, huling 3 oras, huling 24 oras. |
| **Talahanayan** | Mga contact sa mapa, pinakabago muna, sa kulay ng banda; ibinibigay ng *Ulap* ang bahagi ng mga repleksiyon sa pangunahing panig, o *sporadic*. |
| **Click** | Sa isang landas o sa isang hanay ng talahanayan: naha-highlight ang contact at ipinapakita ng kahon ang locator ng gitna ng ulap, ang bahagi nito, laki at axis. |
