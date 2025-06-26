<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:05:33+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "fi"
}
-->
# Neuraaliverkkojen kehykset

Kuten olemme jo oppineet, jotta voimme kouluttaa neuraaliverkkoja tehokkaasti, meidän täytyy tehdä kaksi asiaa:

* Operoida tensoreilla, esim. kertoa, lisätä ja laskea joitakin funktioita kuten sigmoid tai softmax
* Laskea kaikkien lausekkeiden gradientit, jotta voimme suorittaa gradienttilaskeutumisoptimoinnin

Vaikka `numpy`-kirjasto voi tehdä ensimmäisen osan, tarvitsemme jonkin mekanismin gradienttien laskemiseen. Kehyksessämme, jonka kehitimme edellisessä osiossa, meidän piti manuaalisesti ohjelmoida kaikki derivaattafunktiot `backward`-metodin sisällä, joka tekee takaisinlevityksen. Ihanteellisesti kehyksen pitäisi antaa meille mahdollisuus laskea gradientit *mille tahansa lausekkeelle*, jonka voimme määritellä.

Toinen tärkeä asia on kyetä suorittamaan laskelmia GPU:lla tai muilla erikoistuneilla laskentayksiköillä, kuten TPU:lla. Syvien neuraaliverkkojen kouluttaminen vaatii *paljon* laskelmia, ja niiden laskelmien rinnakkaistaminen GPU:illa on erittäin tärkeää.

> ✅ Termi 'rinnakkaistaminen' tarkoittaa laskelmien jakamista useille laitteille.

Tällä hetkellä kaksi suosituinta neuraalikehystä ovat: TensorFlow ja PyTorch. Molemmat tarjoavat matalan tason API:n, jolla voi operoida tensoreilla sekä CPU:lla että GPU:lla. Matalan tason API:n lisäksi on myös korkeamman tason API, nimeltään vastaavasti Keras ja PyTorch Lightning.

Matalan tason API | TensorFlow | PyTorch
-----------------|-------------------------------------|--------------------------------
Korkean tason API | Keras | Pytorch

**Matalan tason API:t** molemmissa kehyksissä mahdollistavat ns. **laskentagrafien** rakentamisen. Tämä graafi määrittelee, miten laskea ulostulo (yleensä tappiofunktio) annetuilla syöteparametreilla, ja se voidaan työntää laskentaan GPU:lle, jos se on saatavilla. On olemassa funktioita, joilla voi erotella tämän laskentagraafin ja laskea gradientit, joita voidaan sitten käyttää mallin parametrien optimointiin.

**Korkean tason API:t** käsittelevät neuraaliverkkoja pitkälti **kerrosten sekvenssinä**, ja tekevät useimpien neuraaliverkkojen rakentamisesta paljon helpompaa. Mallin kouluttaminen vaatii yleensä datan valmistelua ja sitten `fit`-funktion kutsumista työn suorittamiseksi.

Korkean tason API mahdollistaa tyypillisten neuraaliverkkojen rakentamisen erittäin nopeasti ilman huolta monista yksityiskohdista. Samalla matalan tason API tarjoaa paljon enemmän kontrollia koulutusprosessiin, ja siksi niitä käytetään paljon tutkimuksessa, kun käsitellään uusia neuraaliverkkoarkkitehtuureja.

On myös tärkeää ymmärtää, että voit käyttää molempia API:ta yhdessä, esim. voit kehittää oman verkkokerrosarkkitehtuurin matalan tason API:lla, ja sitten käyttää sitä isommassa verkossa, joka on rakennettu ja koulutettu korkean tason API:lla. Tai voit määritellä verkon korkean tason API:lla kerrosten sekvenssinä, ja sitten käyttää omaa matalan tason koulutusloopia optimoinnin suorittamiseen. Molemmat API:t käyttävät samoja peruskäsitteitä, ja ne on suunniteltu toimimaan hyvin yhdessä.

## Oppiminen

Tässä kurssissa tarjoamme suurimman osan sisällöstä sekä PyTorchille että TensorFlowlle. Voit valita haluamasi kehyksen ja käydä läpi vastaavat muistiinpanot. Jos et ole varma, minkä kehyksen valita, lue joitakin keskusteluja internetissä aiheesta **PyTorch vs. TensorFlow**. Voit myös tutustua molempiin kehyksiin saadaksesi paremman ymmärryksen.

Mahdollisuuksien mukaan käytämme korkean tason API:ta yksinkertaisuuden vuoksi. Uskomme kuitenkin, että on tärkeää ymmärtää, miten neuraaliverkot toimivat alusta alkaen, joten aluksi aloitamme matalan tason API:n ja tensorien kanssa. Kuitenkin, jos haluat päästä nopeasti alkuun etkä halua käyttää paljon aikaa näiden yksityiskohtien oppimiseen, voit ohittaa ne ja siirtyä suoraan korkean tason API-muistiinpanoihin.

## ✍️ Harjoitukset: Kehykset

Jatka oppimistasi seuraavissa muistiinpanoissa:

Matalan tason API | TensorFlow+Keras Muistiinpanot | PyTorch
-----------------|-------------------------------------|--------------------------------
Korkean tason API | Keras | *PyTorch Lightning*

Kun olet hallinnut kehykset, kerrataan ylikouluttamisen käsitettä.

# Ylikouluttaminen

Ylikouluttaminen on erittäin tärkeä käsite koneoppimisessa, ja on erittäin tärkeää ymmärtää se oikein!

Pohdi seuraavaa ongelmaa, jossa approksimoidaan 5 pistettä (edustettuna `x` alla olevissa graafeissa):

!lineaarinen | ylikoulutus
-------------------------|--------------------------
**Lineaarinen malli, 2 parametria** | **Ei-lineaarinen malli, 7 parametria**
Koulutusvirhe = 5.3 | Koulutusvirhe = 0
Validointivirhe = 5.1 | Validointivirhe = 20

* Vasemmalla näemme hyvän suoran linjan approksimaation. Koska parametrien määrä on sopiva, malli ymmärtää oikein pisteiden jakautumisen taustalla olevan idean.
* Oikealla malli on liian voimakas. Koska meillä on vain 5 pistettä ja mallilla on 7 parametria, se voi säätyä siten, että se kulkee kaikkien pisteiden läpi, jolloin koulutusvirhe on 0. Tämä kuitenkin estää mallia ymmärtämästä datan taustalla olevaa oikeaa mallia, joten validointivirhe on erittäin korkea.

On erittäin tärkeää löytää oikea tasapaino mallin rikkauden (parametrien määrä) ja koulutusnäytteiden määrän välillä.

## Miksi ylikouluttaminen tapahtuu

  * Ei tarpeeksi koulutusdataa
  * Liian voimakas malli
  * Liikaa kohinaa syötteessä

## Miten ylikouluttaminen havaitaan

Kuten yllä olevasta graafista voi nähdä, ylikouluttaminen voidaan havaita erittäin alhaisesta koulutusvirheestä ja korkeasta validointivirheestä. Normaalisti koulutuksen aikana näemme sekä koulutus- että validointivirheiden alkavan laskea, ja sitten jossain vaiheessa validointivirhe saattaa lakata laskemasta ja alkaa nousta. Tämä on merkki ylikouluttamisesta ja indikaattori siitä, että meidän pitäisi todennäköisesti lopettaa koulutus tässä vaiheessa (tai ainakin tehdä mallista tilannekuva).

ylikouluttaminen

## Miten ylikouluttaminen estetään

Jos huomaat, että ylikouluttaminen tapahtuu, voit tehdä jonkin seuraavista:

 * Lisää koulutusdatan määrää
 * Vähennä mallin monimutkaisuutta
 * Käytä jotakin regularisointitekniikkaa, kuten Dropoutia, jota käsittelemme myöhemmin.

## Ylikouluttaminen ja harha-varianssi -kauppa

Ylikouluttaminen on itse asiassa tapaus tilastotieteessä tunnetusta yleisemmästä ongelmasta, nimeltään Harha-Varianssi -kauppa. Jos tarkastelemme mahdollisia virhelähteitä mallissamme, voimme nähdä kahdenlaisia virheitä:

* **Harhavirheet** johtuvat algoritmimme kyvyttömyydestä vangita suhdetta koulutusdatan välillä oikein. Se voi johtua siitä, että mallimme ei ole tarpeeksi voimakas (**alikouluttaminen**).
* **Varianssivirheet**, jotka johtuvat mallin kohinan approksimoinnista syöttödatassa merkityksellisen suhteen sijaan (**ylikouluttaminen**).

Koulutuksen aikana harhavirhe vähenee (kun mallimme oppii approksimoimaan dataa) ja varianssivirhe kasvaa. On tärkeää lopettaa koulutus - joko manuaalisesti (kun havaitsemme ylikouluttamisen) tai automaattisesti (ottamalla käyttöön regularisointi) - estääksemme ylikouluttamisen.

## Yhteenveto

Tässä oppitunnissa opit eroja kahden suosituimman AI-kehyksen, TensorFlow:n ja PyTorchin, eri API:den välillä. Lisäksi opit erittäin tärkeästä aiheesta, ylikouluttamisesta.

## 🚀 Haaste

Liitetyissä muistiinpanoissa löydät 'tehtäviä' alareunasta; käy muistiinpanot läpi ja suorita tehtävät.

## Katsaus ja itseopiskelu

Tee tutkimusta seuraavista aiheista:

- TensorFlow
- PyTorch
- Ylikouluttaminen

Kysy itseltäsi seuraavat kysymykset:

- Mikä on ero TensorFlow:n ja PyTorchin välillä?
- Mikä on ero ylikouluttamisen ja alikouluttamisen välillä?

## Tehtävä

Tässä laboratoriossa sinua pyydetään ratkaisemaan kaksi luokitteluongelmaa käyttäen yksi- ja monikerroksisia täysin kytkettyjä verkkoja PyTorchilla tai TensorFlowlla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa mahdollisista väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.