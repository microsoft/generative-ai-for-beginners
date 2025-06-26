<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:26:26+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin. Monikerroksinen perceptroni

Edellisessä osiossa opit yksinkertaisimmasta neuroverkkomallista - yksikerroksisesta perceptronista, lineaarisesta kaksiluokkaisesta luokittelumallista.

Tässä osiossa laajennamme tätä mallia joustavammaksi kehykseksi, jonka avulla voimme:

* suorittaa **moniluokkaluokittelua** kaksiluokkaisen lisäksi
* ratkaista **regressio-ongelmia** luokittelun lisäksi
* erottaa luokat, jotka eivät ole lineaarisesti erotettavissa

Kehitämme myös oman modulaarisen kehyksen Pythonissa, joka mahdollistaa erilaisten neuroverkkorakenteiden rakentamisen.

## Koneoppimisen muodollistaminen

Aloitetaan koneoppimisongelman muodollistamisella. Oletetaan, että meillä on harjoitusdatajoukko **X** ja etiketit **Y**, ja meidän on rakennettava malli *f*, joka tekee mahdollisimman tarkkoja ennusteita. Ennusteiden laatua mitataan **häviöfunktiolla** ℒ. Seuraavia häviöfunktioita käytetään usein:

* Regressio-ongelmassa, kun meidän on ennustettava luku, voimme käyttää **absoluuttista virhettä** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| tai **neliöllistä virhettä** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Luokittelussa käytämme **0-1-häviötä** (joka on olennaisesti sama kuin mallin **tarkkuus**) tai **logistista häviötä**.

Yksikerroksiselle perceptronille funktio *f* määriteltiin lineaarisena funktiona *f(x)=wx+b* (tässä *w* on painomatriisi, *x* on syöteominaisuuksien vektori ja *b* on harhavektori). Erilaisille neuroverkkorakenteille tämä funktio voi saada monimutkaisemman muodon.

> Luokittelun tapauksessa on usein toivottavaa saada verkon lähtönä vastaavien luokkien todennäköisyydet. Muuntaaksemme mielivaltaisia lukuja todennäköisyyksiksi (esim. normalisoidaksemme tuloksen), käytämme usein **softmax**-funktiota σ, ja funktiosta *f* tulee *f(x)=σ(wx+b)*

Yllä olevassa *f*:n määritelmässä *w* ja *b* kutsutaan **parametreiksi** θ=⟨*w,b*⟩. Kun annettu on datajoukko ⟨**X**,**Y**⟩, voimme laskea koko datajoukon kokonaisvirheen parametrien θ funktiona.

> ✅ **Neuroverkon koulutuksen tavoitteena on minimoida virhe vaihtelemalla parametreja θ**

## Gradienttilaskeuman optimointi

On olemassa tunnettu funktion optimointimenetelmä nimeltä **gradienttilaskeuma**. Ajatuksena on, että voimme laskea derivaatan (moniulotteisessa tapauksessa kutsutaan **gradientiksi**) häviöfunktion suhteen parametreihin ja vaihdella parametreja siten, että virhe pienenee. Tämä voidaan muodollistaa seuraavasti:

* Alusta parametrit joillakin satunnaisilla arvoilla w<sup>(0)</sup>, b<sup>(0)</sup>
* Toista seuraavaa vaihetta monta kertaa:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Koulutuksen aikana optimointivaiheiden oletetaan lasketun koko datajoukon huomioon ottaen (muista, että häviö lasketaan summana kaikkien harjoitusnäytteiden läpi). Kuitenkin todellisessa elämässä otamme pieniä osia datajoukosta, joita kutsutaan **minieriksi**, ja laskemme gradientit datan osajoukon perusteella. Koska osajoukko otetaan satunnaisesti joka kerta, tällaista menetelmää kutsutaan **stokastiseksi gradienttilaskeumaksi** (SGD).

## Monikerroksiset perceptronit ja takaisinsyöttö

Yksikerroksinen verkko, kuten olemme nähneet, pystyy luokittelemaan lineaarisesti erotettavia luokkia. Rikkaamman mallin rakentamiseksi voimme yhdistää useita verkon kerroksia. Matemaattisesti tämä tarkoittaisi, että funktiolla *f* olisi monimutkaisempi muoto, ja se laskettaisiin useassa vaiheessa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tässä α on **epälineaarinen aktivointifunktio**, σ on softmax-funktio ja parametrit θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradienttilaskeuma-algoritmi pysyisi samana, mutta gradienttien laskeminen olisi vaikeampaa. Ketjusäännön mukaan voimme laskea derivaatat seuraavasti:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ketjusääntöä käytetään laskemaan häviöfunktion derivaatat suhteessa parametreihin.

Huomaa, että kaikkien näiden lausekkeiden vasemmanpuoleinen osa on sama, ja siksi voimme tehokkaasti laskea derivaatat alkaen häviöfunktiosta ja kulkemalla "taaksepäin" laskentakaaviossa. Näin monikerroksisen perceptronin koulutusmenetelmää kutsutaan **takaisinsyötöksi**, tai 'backprop'iksi'.

> TODO: kuvan viite

> ✅ Käsittelemme takaisinsyöttöä paljon tarkemmin esimerkkivihossamme.

## Yhteenveto

Tässä oppitunnissa olemme rakentaneet oman neuroverkkokirjastomme, ja olemme käyttäneet sitä yksinkertaiseen kaksidimensionaaliseen luokittelutehtävään.

## 🚀 Haaste

Liitetyssä vihossa toteutat oman kehyksesi monikerroksisten perceptronien rakentamiseen ja kouluttamiseen. Pystyt näkemään yksityiskohtaisesti, miten modernit neuroverkot toimivat.

Siirry OwnFramework-vihkoon ja työskentele sen läpi.

## Kertaus & Itseopiskelu

Takaisinsyöttö on yleinen algoritmi AI:ssa ja ML:ssä, ja se kannattaa opiskella tarkemmin.

## Tehtävä

Tässä laboratoriossa sinun on käytettävä tässä oppitunnissa rakentamaasi kehystä MNIST-käsinkirjoitettujen numeroiden luokittelun ratkaisemiseen.

* Ohjeet
* Vihko

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttäen tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.