**English** · [Русский](Live-Traffic-ru) · [Deutsch](Live-Traffic-de) · [日本語](Live-Traffic-ja)

# Umferð í beinni

*Flipi: Beint og rauntímagögn › Umferð í beinni.*

[![Umferð í beinni](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Hvað hann sýnir

**Jafnfjarlægðar-áttarhornskort** með þína stöð í miðju (fjarlægð frá miðju = raunveruleg fjarlægð, horn = áttarhorn) með **allri meteor scatter-umferð** sem [Gagnasöfnun](Data-Collection-is) hefur safnað. Fyrir hvert samband teiknar forritið:

- **leiðina** milli stöðvanna tveggja, í lit tíðnisviðsins: 28 MHz brún, 50 MHz græn, 70 MHz blágræn, 144 MHz appelsínugul, 222 MHz bleik, 432 MHz fjólublá;
- **stöðvarnar** tvær við enda leiðarinnar;
- **skýið**: þar sem líklegustu loftsteinaslóðirnar fyrir þessa leið á þessum tíma safnast saman.

Spotum þar sem stöð er **utan kortsins** er hent. Spot sem **var að berast** (ekki eldra en 3 mínútur) **blikkar í eina mínútu**, svo ný virkni sést strax.

## Hvernig skýið er reiknað

Fyrir hvert spot setur forritið upp leiðina milli locatoranna tveggja (sama rúmfræði og fyrir þína eigin leið, sjá [Rúmfræði og deyfing](Geometry-and-Path-Loss-is)) og leggur saman, á tíma spotsins, punkt fyrir punkt í E-laginu **framlög speglunarendurvarps frá hverri virkri drífu**, vegin með ZHR hennar – sami útreikningur og fyrir **PREV-svæðin** í [himinhvelfingunni](Sky-View-is). Fyrir hvora hlið leiðarinnar sem hefur a.m.k. 15 % af heildinni er skýið **sporbaugur**: miðja í vegnu meðaltali punktanna, hálfásar 1,5 sinnum kvaðratrætur eigingilda dreifingar þeirra, langás eftir aðaleiginvigrinum. Þegar engin drífa leggur neitt til (aðeins stopulir loftsteinar) eru skýin tveir hefðbundnu **heitu blettirnir**, teiknaðir með brotalínu. Jöfnurnar í heild eru í 10. kafla reiknihandbókarinnar.

## Stýringar

| Stýring | Merking |
|---|---|
| **Radíus korts** | 600–3500 km frá þinni stöð. |
| **Spot til að sýna** | Síðustu 15 eða 30 mínútur, síðasta klukkustund, síðustu 3 klukkustundir, síðustu 24 klukkustundir. |
| **Tafla** | Sambönd á kortinu, nýjustu fyrst, í lit tíðnisviðsins; *Ský* gefur hlutfall endurvarpa á aðalhliðinni, eða *stopulir*. |
| **Smellur** | Á leið eða línu í töflunni: sambandið er auðkennt og reiturinn sýnir locator miðju skýsins, hlutfall þess, stærð og ás. |
