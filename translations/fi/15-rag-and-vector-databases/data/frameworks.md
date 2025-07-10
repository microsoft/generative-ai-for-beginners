<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:33:34+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "fi"
}
-->
# Neuroverkkojen kehykset

Kuten olemme jo oppineet, neuroverkkojen tehokkaaseen kouluttamiseen tarvitsemme kaksi asiaa:

* Kyvyn käsitellä tensoreita, esimerkiksi kertoa, laskea yhteen ja suorittaa funktioita kuten sigmoid tai softmax
* Kyvyn laskea kaikkien lausekkeiden gradientit gradienttilaskennan suorittamiseksi

Vaikka `numpy`-kirjasto pystyy hoitamaan ensimmäisen osan, tarvitsemme mekanismin gradienttien laskemiseen. Kehyksessämme, jonka kehitimme edellisessä osassa, jouduimme ohjelmoimaan kaikki derivaatat manuaalisesti `backward`-metodiin, joka suorittaa takaisinkytkennän. Ihanteellisesti kehys antaisi mahdollisuuden laskea gradientit *mille tahansa lausekkeelle*, jonka voimme määritellä.

Toinen tärkeä asia on kyky suorittaa laskutoimituksia GPU:lla tai muilla erikoistuneilla laskentayksiköillä, kuten TPU:lla. Syvien neuroverkkojen koulutus vaatii *paljon* laskentaa, ja laskentojen rinnakkaistaminen GPU:illa on erittäin tärkeää.

> ✅ Termi 'rinnakkaistaa' tarkoittaa laskentojen jakamista useille laitteille.

Tällä hetkellä kaksi suosituimpaa neuroverkkokehystä ovat TensorFlow ja PyTorch. Molemmat tarjoavat matalan tason API:n tensorien käsittelyyn sekä CPU:lla että GPU:lla. Matalan tason API:n päällä on myös korkean tason API, nimeltään vastaavasti Keras ja PyTorch Lightning.

Matalan tason API | TensorFlow | PyTorch
-----------------|------------|---------
Korkean tason API| Keras      | PyTorch

**Matalan tason API:t** molemmissa kehyksissä mahdollistavat ns. **laskentakaavioiden** rakentamisen. Tämä kaavio määrittelee, miten lasketaan lähtöarvo (yleensä häviöfunktio) annetuilla syöteparametreilla, ja se voidaan suorittaa GPU:lla, jos sellainen on käytettävissä. On olemassa funktioita, joilla tätä laskentakaaviota voidaan derivoida ja laskea gradientit, joita voidaan käyttää mallin parametrien optimointiin.

**Korkean tason API:t** käsittelevät neuroverkkoja käytännössä **kerrosten sarjana**, mikä helpottaa useimpien neuroverkkojen rakentamista huomattavasti. Mallin koulutus vaatii yleensä datan valmistelun ja sitten `fit`-funktion kutsumisen työn suorittamiseksi.

Korkean tason API:n avulla voit rakentaa tyypillisiä neuroverkkoja nopeasti ilman, että sinun tarvitsee huolehtia monista yksityiskohdista. Samaan aikaan matalan tason API tarjoaa paljon enemmän kontrollia koulutusprosessiin, ja siksi sitä käytetään paljon tutkimuksessa, kun työskennellään uusien neuroverkkorakenteiden parissa.

On myös tärkeää ymmärtää, että molempia API:ita voi käyttää yhdessä, esimerkiksi voit kehittää oman verkon kerrosarkkitehtuurin matalan tason API:lla ja käyttää sitä sitten suuremmassa verkossa, joka on rakennettu ja koulutettu korkean tason API:lla. Tai voit määritellä verkon korkean tason API:lla kerrosten sarjana ja käyttää omaa matalan tason koulutussilmukkaasi optimointiin. Molemmat API:t perustuvat samoihin peruskäsitteisiin ja on suunniteltu toimimaan hyvin yhdessä.

## Oppiminen

Tässä kurssissa tarjoamme suurimman osan sisällöstä sekä PyTorchille että TensorFlow:lle. Voit valita mieluisimman kehyksen ja käydä läpi vain siihen liittyvät muistikirjat. Jos et ole varma, kumpaa kehystä valita, lue netistä keskusteluja aiheesta **PyTorch vs. TensorFlow**. Voit myös tutustua molempiin kehyksiin saadaksesi paremman käsityksen.

Missä mahdollista, käytämme yksinkertaisuuden vuoksi korkean tason API:ita. Uskomme kuitenkin, että on tärkeää ymmärtää neuroverkkojen toiminta alusta alkaen, joten aluksi työskentelemme matalan tason API:n ja tensorien kanssa. Jos haluat kuitenkin päästä nopeasti alkuun etkä halua käyttää paljon aikaa näiden yksityiskohtien oppimiseen, voit hypätä suoraan korkean tason API:n muistikirjoihin.

## ✍️ Harjoitukset: Kehykset

Jatka oppimista seuraavissa muistikirjoissa:

Matalan tason API | TensorFlow+Keras -muistikirja | PyTorch
-----------------|-------------------------------|---------
Korkean tason API| Keras                         | *PyTorch Lightning*

Kun olet hallinnut kehykset, kerrataan vielä ylisovittamisen käsite.

# Ylisovittaminen

Ylisovittaminen on erittäin tärkeä käsite koneoppimisessa, ja sen ymmärtäminen oikein on ratkaisevan tärkeää!

Tarkastellaan seuraavaa ongelmaa, jossa pyritään approksimoimaan 5 pistettä (joita on merkitty `x` alla olevissa kaavioissa):

!linear | overfit
-------------------------|--------------------------
**Lineaarinen malli, 2 parametria** | **Ei-lineaarinen malli, 7 parametria**
Koulutuksen virhe = 5.3 | Koulutuksen virhe = 0
Validointivirhe = 5.1 | Validointivirhe = 20

* Vasemmalla näemme hyvän suoran viivan approksimaation. Koska parametrien määrä on sopiva, malli ymmärtää pisteiden jakauman oikein.
* Oikealla malli on liian voimakas. Koska meillä on vain 5 pistettä ja mallilla on 7 parametria, se voi sovittaa kaikki pisteet tarkasti, jolloin koulutuksen virhe on 0. Tämä estää mallia ymmärtämästä datan oikeaa kaavaa, minkä vuoksi validointivirhe on hyvin korkea.

On erittäin tärkeää löytää oikea tasapaino mallin rikkauden (parametrien määrä) ja koulutusnäytteiden määrän välillä.

## Miksi ylisovittaminen tapahtuu

  * Liian vähän koulutusdataa
  * Liian voimakas malli
  * Liikaa kohinaa syötteessä

## Miten havaita ylisovittaminen

Kuten yllä olevasta kaaviosta näkyy, ylisovittaminen voidaan havaita hyvin matalasta koulutusvirheestä ja korkeasta validointivirheestä. Tavallisesti koulutuksen aikana sekä koulutus- että validointivirheet alkavat pienentyä, mutta jossain vaiheessa validointivirhe saattaa lakata pienentymästä ja alkaa kasvaa. Tämä on merkki ylisovittamisesta ja osoitus siitä, että koulutus kannattaa todennäköisesti lopettaa tässä vaiheessa (tai ainakin tallentaa mallin tilanne).

ylisovittaminen

## Miten estää ylisovittamista

Jos huomaat ylisovittamista, voit tehdä seuraavia asioita:

 * Lisätä koulutusdatan määrää
 * Vähentää mallin monimutkaisuutta
 * Käyttää jonkinlaista regularisointitekniikkaa, kuten Dropoutia, jota käsittelemme myöhemmin.

## Ylisovittaminen ja bias-varianssi-vaihtokauppa

Ylisovittaminen on itse asiassa osa laajempaa tilastotieteellistä ongelmaa, jota kutsutaan bias-varianssi-vaihtokaupaksi. Kun tarkastelemme mallin virhelähteitä, voimme erottaa kaksi virhetyyppiä:

* **Bias-virheet** johtuvat siitä, että algoritmimme ei pysty mallintamaan koulutusdatan ja mallin välistä suhdetta oikein. Tämä voi johtua siitä, että mallimme ei ole tarpeeksi voimakas (**alisovittaminen**).
* **Varianssivirheet** johtuvat siitä, että malli sovittaa kohinaa syötteessä merkityksellisen suhteen sijaan (**ylisovittaminen**).

Koulutuksen aikana bias-virhe pienenee (kun malli oppii approksimoimaan dataa), mutta varianssivirhe kasvaa. On tärkeää lopettaa koulutus joko manuaalisesti (kun havaitsemme ylisovittamisen) tai automaattisesti (ottamalla käyttöön regularisointi) ylisovittamisen estämiseksi.

## Yhteenveto

Tässä oppitunnissa opit eroja kahden suosituimman tekoälykehyksen, TensorFlow:n ja PyTorchin, eri API:iden välillä. Lisäksi opit erittäin tärkeästä aiheesta, ylisovittamisesta.

## 🚀 Haaste

Mukana olevissa muistikirjoissa löydät tehtäviä sivun alareunasta; käy muistikirjat läpi ja suorita tehtävät.

## Kertaus & Itsenäinen opiskelu

Tutki seuraavia aiheita:

- TensorFlow
- PyTorch
- Ylisovittaminen

Kysy itseltäsi seuraavat kysymykset:

- Mikä on ero TensorFlow:n ja PyTorchin välillä?
- Mikä on ero ylisovittamisen ja alisovittamisen välillä?

## Tehtävä

Tässä laboratoriossa sinun tulee ratkaista kaksi luokitteluongelmaa käyttäen yksikerroksisia ja monikerroksisia täysin yhdistettyjä verkkoja PyTorchilla tai TensorFlow:lla.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.