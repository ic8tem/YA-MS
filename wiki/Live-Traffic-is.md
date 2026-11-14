[English](Live-Traffic) · [Italiano](Live-Traffic-it) · [Deutsch](Live-Traffic-de) · [Nederlands](Live-Traffic-nl) · [Français](Live-Traffic-fr) · [Español](Live-Traffic-es) · [Português](Live-Traffic-pt) · [Português (Brasil)](Live-Traffic-pt-br) · [Dansk](Live-Traffic-da) · [Norsk](Live-Traffic-nb) · [Svenska](Live-Traffic-sv) · **Íslenska** · [Eesti](Live-Traffic-et) · [Lietuvių](Live-Traffic-lt) · [Latviešu](Live-Traffic-lv) · [Polski](Live-Traffic-pl) · [Čeština](Live-Traffic-cs) · [Magyar](Live-Traffic-hu) · [Română](Live-Traffic-ro) · [Ελληνικά](Live-Traffic-el) · [Русский](Live-Traffic-ru) · [Українська](Live-Traffic-uk) · [Türkçe](Live-Traffic-tr) · [Afrikaans](Live-Traffic-af) · [العربية](Live-Traffic-ar) · [עברית](Live-Traffic-he) · [اردو](Live-Traffic-ur) · [हिन्दी](Live-Traffic-hi) · [বাংলা](Live-Traffic-bn) · [ไทย](Live-Traffic-th) · [Bahasa Indonesia](Live-Traffic-id) · [Tagalog](Live-Traffic-tl) · [日本語](Live-Traffic-ja) · [한국어](Live-Traffic-ko) · [中文](Live-Traffic-zh) · [中文 (繁體)](Live-Traffic-zh-tw)

# Umferð í beinni

*Flipi: Beint og rauntímagögn › Umferð í beinni.*

[![Umferð í beinni](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)](https://raw.githubusercontent.com/ic8tem/YA-MS/main/docs/screenshots/en-1_1.png)

## Hvað hann sýnir

**Jafnfjarlægðar-áttarhornskort** með þína stöð í miðju (fjarlægð frá miðju = raunveruleg fjarlægð, horn = áttarhorn) með **allri meteor scatter-umferð** sem [Gagnasöfnun](Data-Collection-is) hefur safnað. Fyrir hvert samband teiknar forritið:

- **leiðina** milli stöðvanna tveggja, í lit tíðnisviðsins: 28 MHz brún, 50 MHz græn, 70 MHz blágræn, 144 MHz appelsínugul, 222 MHz bleik, 432 MHz fjólublá;
- **stöðvarnar** tvær við enda leiðarinnar;
- **skýið**: þar sem líklegustu loftsteinaslóðirnar fyrir þessa leið á þessum tíma safnast saman.

Spotum þar sem stöð er **utan kortsins** er hent. Spot sem **var að berast** (ekki eldra en 3 mínútur) **blikkar í eina mínútu**, svo ný virkni sést strax.

Sýna hverjir hlusta: þríhyrningar í lit bandsins merkja stöðvar sem samkvæmt PSKReporter taka á móti MSK144, FSK441, PSK2K eða JTMS á 28, 50, 70, 144 og 432 MHz í völdum tímaglugga. Smellur á þríhyrning sýnir kallmerki, staðsetningu, hætti og síðasta spot. MQTT-straumurinn í flipanum Gagnasöfnun verður að vera tengdur.

Einnig virkir hlustendur á korti PSKReporter: tómir þríhyrningar fyrir stöðvar sem birtast á korti pskreporter.info í MSK144, FSK441, PSK2K eða JTMS en hafa ekki enn tekið á móti neinu spotti (MQTT sendir aðeins stöðvar sem taka á móti einhverju). YA-MS spyr fyrirspurnaþjónustu PSKReporter einu sinni á 5 mínútna fresti fyrir alla hætti, eins og reglur þjónustunnar biðja um; hlustandi helst á kortinu í að minnsta kosti 11 mínútur. Smellur á þríhyrninginn sýnir kallmerki, staðsetningu, afkóðunarforrit og tímann sem hlustandinn var virkur. Kveikt sjálfgefið.

FT8 yfir 1100 km án samsíða leiða: FT8-spott (frá PSKReporter MQTT, klösum eða WSJT-X um UDP) milli stöðva sem eru meira en 1100 km hvor frá annarri og hefur engar samsíða leiðir á 3 mínútum fyrir og eftir (sama band, miðpunktur innan 300 km, stefna innan 20°, annað stöðvapar) er teiknað ljósgrænt og lína þess í töflunni neðst til hægri blikkar alltaf. Sporadískt E og tropo gefa margar nálægar, samsíða leiðir; stakt spott getur verið loftsteinaslóð. Þess vegna tekur YA-MS líka við FT8-spottum frá MQTT á 6 m, 4 m, 2 m, 1,25 m og 70 cm (ekki 10 m, of mörg). Þessi spott fara ekki í MS-safnið. Kveikt sjálfgefið.

WSJT-X-spott um UDP sem varða stöðina þína (afkóðunin inniheldur kallmerkið þitt: sá sem kallar á þig eða svarar þér) eru teiknuð með strikalínu sem blikkar alltaf, í öllum háttum og í hvaða fjarlægð sem er.

Kortið sýnir kallmerki beggja stöðva hvers spotts, einu sinni á hverja stöð. Vörpunin getur verið jafnfjarlæg (miðuð á þína stöð) eða Mercator. Ábendingin á dálknum Ský útskýrir merkingu hans.

Spott allra banda eru sýnd, líka banda sem ekki eru valin í Gagnasöfnun (þau eru ekki vistuð). CW-spott og spott milli stöðva sem eru of nálægt eru ekki sýnd ef þeim er hent í Gagnasöfnun.

## Hvernig skýið er reiknað

Fyrir hvert spot setur forritið upp leiðina milli locatoranna tveggja (sama rúmfræði og fyrir þína eigin leið, sjá [Rúmfræði og deyfing](Geometry-and-Path-Loss-is)) og leggur saman, á tíma spotsins, punkt fyrir punkt í E-laginu **framlög speglunarendurvarps frá hverri virkri drífu**, vegin með ZHR hennar – sami útreikningur og fyrir **PREV-svæðin** í [himinhvelfingunni](Sky-View-is). Fyrir hvora hlið leiðarinnar sem hefur a.m.k. 15 % af heildinni er skýið **sporbaugur**: miðja í vegnu meðaltali punktanna, hálfásar 1,5 sinnum kvaðratrætur eigingilda dreifingar þeirra, langás eftir aðaleiginvigrinum. Þegar engin drífa leggur neitt til (aðeins stopulir loftsteinar) eru skýin tveir hefðbundnu **heitu blettirnir**, teiknaðir með brotalínu. Jöfnurnar í heild eru í 10. kafla reiknihandbókarinnar.

## Stýringar

| Stýring | Merking |
|---|---|
| **Radíus korts** | 600–3500 km frá þinni stöð. |
| **Spot til að sýna** | Síðustu 15 eða 30 mínútur, síðasta klukkustund, síðustu 3 klukkustundir, síðustu 24 klukkustundir. |
| **Tafla** | Sambönd á kortinu, nýjustu fyrst, í lit tíðnisviðsins; *Ský* gefur hlutfall endurvarpa á aðalhliðinni, eða *stopulir*. |
| **Smellur** | Á leið eða línu í töflunni: sambandið er auðkennt og reiturinn sýnir locator miðju skýsins, hlutfall þess, stærð og ás. |
