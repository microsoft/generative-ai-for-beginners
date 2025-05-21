<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:01:27+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "fi"
}
-->
# Neuraaliverkkojen kehykset

Kuten olemme jo oppineet, tehokkaaseen neuraaliverkkojen kouluttamiseen tarvitaan kaksi asiaa:

* Operoida tensorien kanssa, esimerkiksi kertoa, lisätä ja laskea joitain funktioita kuten sigmoid tai softmax
* Laskea kaikkien lausekkeiden gradientit, jotta voidaan suorittaa gradienttilaskeutumisoptimointi

Vaikka `numpy`-kirjasto pystyy tekemään ensimmäisen osan, tarvitsemme jonkin mekanismin gradienttien laskemiseen. Kehyksessämme, jonka kehitimme edellisessä osassa, jouduimme ohjelmoimaan kaikki derivatiivifunktiot manuaalisesti `backward`-menetelmän sisällä, joka tekee takapropagoinnin. Ihanteellisesti kehyksen tulisi antaa meille mahdollisuus laskea *minkä tahansa lausekkeen* gradientit, joita voimme määritellä.

Toinen tärkeä asia on kyetä suorittamaan laskutoimituksia GPU:lla tai muilla erikoistuneilla laskentayksiköillä, kuten TPU:lla. Syvien neuraaliverkkojen kouluttaminen vaatii *paljon* laskutoimituksia, ja niiden laskutoimitusten rinnakkaistaminen GPU:illa on erittäin tärkeää.

> ✅ Termi 'rinnakkaistaminen' tarkoittaa laskutoimitusten jakamista useille laitteille.

Tällä hetkellä kaksi suosituinta neuraaliverkkojen kehystä ovat: TensorFlow ja PyTorch. Molemmat tarjoavat matalan tason API:n tensorien käsittelyyn sekä CPU:lla että GPU:lla. Matalan tason API:n lisäksi on myös korkean tason API, nimeltään vastaavasti Keras ja PyTorch Lightning.

Matalan tason API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
Korkean tason API| Keras| Pytorch

**Matalan tason API:t** molemmissa kehyksissä mahdollistavat niin kutsuttujen **laskentagraafien** rakentamisen. Tämä graafi määrittelee, miten lasketaan ulostulo (yleensä häviöfunktio) annettujen syöttöparametrien kanssa, ja se voidaan työntää laskettavaksi GPU:lle, jos se on saatavilla. On olemassa funktioita, jotka erottavat tämän laskentagraafin ja laskevat gradientit, joita voidaan sitten käyttää malliparametrien optimointiin.

**Korkean tason API:t** käsittelevät neuraaliverkkoja pääasiassa **kerrosten sarjana**, ja tekevät useimpien neuraaliverkkojen rakentamisesta paljon helpompaa. Mallin kouluttaminen vaatii yleensä datan valmistelua ja sitten `fit`-funktion kutsumista työn tekemiseksi.

Korkean tason API:n avulla voit rakentaa tyypillisiä neuraaliverkkoja erittäin nopeasti ilman huolta monista yksityiskohdista. Samalla matalan tason API tarjoaa paljon enemmän kontrollia koulutusprosessiin, ja siksi niitä käytetään paljon tutkimuksessa, kun käsitellään uusia neuraaliverkkoarkkitehtuureja.

On myös tärkeää ymmärtää, että voit käyttää molempia API:ta yhdessä, esimerkiksi voit kehittää oman verkon kerrosarkkitehtuurin matalan tason API:n avulla ja sitten käyttää sitä suuremmassa verkossa, joka on rakennettu ja koulutettu korkean tason API:lla. Tai voit määritellä verkon korkean tason API:n avulla kerrosten sarjana ja sitten käyttää omaa matalan tason koulutusloopia optimoinnin suorittamiseen. Molemmat API:t käyttävät samoja peruskäsitteitä, ja ne on suunniteltu toimimaan hyvin yhdessä.

## Oppiminen

Tässä kurssissa tarjoamme suurimman osan sisällöstä sekä PyTorchille että TensorFlow'lle. Voit valita mieluisan kehyksen ja käydä läpi vastaavat muistikirjat. Jos et ole varma, minkä kehyksen valitsisit, lue keskusteluja internetissä **PyTorch vs. TensorFlow**. Voit myös tutustua molempiin kehyksiin saadaksesi paremman ymmärryksen.

Missä mahdollista, käytämme korkean tason API:ta yksinkertaisuuden vuoksi. Uskomme kuitenkin, että on tärkeää ymmärtää, miten neuraaliverkot toimivat alusta alkaen, joten aluksi aloitamme työskentelemällä matalan tason API:n ja tensorien kanssa. Kuitenkin, jos haluat päästä nopeasti alkuun etkä halua käyttää paljon aikaa näiden yksityiskohtien oppimiseen, voit ohittaa ne ja siirtyä suoraan korkean tason API-muistikirjoihin.

## ✍️ Harjoitukset: Kehykset

Jatka oppimista seuraavissa muistikirjoissa:

Matalan tason API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
Korkean tason API| Keras | *PyTorch Lightning*

Kun olet hallinnut kehykset, kerrataan ylikapasitoinnin käsite.

# Ylikapasitointi

Ylikapasitointi on erittäin tärkeä käsite koneoppimisessa, ja on erittäin tärkeää saada se oikein!

Tarkastellaan seuraavaa ongelmaa, jossa pyritään arvioimaan 5 pistettä (edustettuna `x` alla olevissa graafeissa):

!lineaarinen | ylikapasitointi
-------------------------|--------------------------
**Lineaarinen malli, 2 parametria** | **Ei-lineaarinen malli, 7 parametria**
Koulutusvirhe = 5.3 | Koulutusvirhe = 0
Validointivirhe = 5.1 | Validointivirhe = 20

* Vasemmalla näemme hyvän suoran viivan arvioinnin. Koska parametrien määrä on riittävä, malli ymmärtää pistejakautuman oikein.
* Oikealla malli on liian voimakas. Koska meillä on vain 5 pistettä ja mallilla on 7 parametria, se voi säätää itsensä siten, että se kulkee kaikkien pisteiden läpi, mikä tekee koulutusvirheestä 0. Tämä estää mallia ymmärtämästä datan oikeaa mallia, ja siksi validointivirhe on erittäin korkea.

On erittäin tärkeää löytää oikea tasapaino mallin rikkauden (parametrien määrä) ja koulutusnäytteiden määrän välillä.

## Miksi ylikapasitointi tapahtuu

  * Ei tarpeeksi koulutusdataa
  * Liian voimakas malli
  * Liikaa kohinaa syöttödatoissa

## Kuinka havaita ylikapasitointi

Kuten yllä olevasta graafista näet, ylikapasitointi voidaan havaita erittäin alhaisella koulutusvirheellä ja korkealla validointivirheellä. Normaalisti koulutuksen aikana näemme sekä koulutus- että validointivirheiden alkavan pienentyä, ja sitten jossain vaiheessa validointivirhe saattaa lakata pienentymästä ja alkaa kasvaa. Tämä on merkki ylikapasitoinnista, ja indikaattori siitä, että meidän pitäisi luultavasti lopettaa koulutus tässä vaiheessa (tai ainakin tehdä mallista tilannekuva).

ylikapasitointi

## Kuinka estää ylikapasitointi

Jos huomaat, että ylikapasitointia tapahtuu, voit tehdä jonkin seuraavista:

 * Lisää koulutusdatan määrää
 * Vähennä mallin monimutkaisuutta
 * Käytä jotakin säännöllistämistekniikkaa, kuten Dropout, jota käsittelemme myöhemmin.

## Ylikapasitointi ja harha-varianssi kompromissi

Ylikapasitointi on itse asiassa tapaus yleisemmästä ongelmasta tilastotieteessä, nimeltään harha-varianssi kompromissi. Jos tarkastelemme mahdollisia virhelähteitä mallissamme, näemme kaksi tyyppistä virhettä:

* **Harhavirheet** johtuvat siitä, että algoritmimme ei pysty sieppaamaan koulutusdatan välistä suhdetta oikein. Se voi johtua siitä, että mallimme ei ole tarpeeksi voimakas (**alikapasitointi**).
* **Varianssivirheet**, jotka johtuvat siitä, että malli arvioi syöttödatan kohinaa merkityksellisen suhteen sijasta (**ylikapasitointi**).

Koulutuksen aikana harhavirhe vähenee (kun mallimme oppii arvioimaan dataa), ja varianssivirhe kasvaa. On tärkeää lopettaa koulutus - joko manuaalisesti (kun havaitsemme ylikapasitoinnin) tai automaattisesti (säännöllistämisen avulla) - estääksemme ylikapasitoinnin.

## Johtopäätös

Tässä oppitunnissa opit eroja kahden suosituimman AI-kehyksen, TensorFlow'n ja PyTorchin, eri API:iden välillä. Lisäksi opit erittäin tärkeästä aiheesta, ylikapasitoinnista.

## 🚀 Haaste

Liitetyissä muistikirjoissa löydät 'tehtäviä' alareunassa; käy läpi muistikirjat ja suorita tehtävät.

## Katsaus ja itseopiskelu

Tee tutkimusta seuraavista aiheista:

- TensorFlow
- PyTorch
- Ylikapasitointi

Kysy itseltäsi seuraavat kysymykset:

- Mikä on ero TensorFlow'n ja PyTorchin välillä?
- Mikä on ero ylikapasitoinnin ja alikapasitoinnin välillä?

## Tehtävä

Tässä laboratoriossa sinua pyydetään ratkaisemaan kaksi luokitteluongelmaa käyttäen yksikerroksisia ja monikerroksisia täysin kytkettyjä verkkoja PyTorchilla tai TensorFlow'lla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta ole tietoinen siitä, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää virallisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virheellisistä tulkinnoista.