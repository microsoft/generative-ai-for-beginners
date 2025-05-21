<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:22:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin. Monikerroksinen perceptron

Edellisessä osiossa opit yksinkertaisimmasta neuroverkkoyksiköstä - yksikerroksisesta perceptronista, lineaarisesta kaksiluokkaisesta luokittelumallista.

Tässä osiossa laajennamme tätä mallia joustavammaksi kehykseksi, joka mahdollistaa:

* suorittaa **moniluokkaluokittelua** kaksiluokkaisen lisäksi
* ratkaista **regressio-ongelmia** luokittelun lisäksi
* erottaa luokat, jotka eivät ole lineaarisesti erotettavissa

Kehitämme myös oman modulaarisen kehyksen Pythonilla, joka mahdollistaa erilaisten neuroverkkorakenteiden luomisen.

## Koneoppimisen muodollistaminen

Aloitetaan koneoppimisongelman muodollistamisella. Oletetaan, että meillä on opetusdatajoukko **X** ja tarrat **Y**, ja meidän on rakennettava malli *f*, joka tekee mahdollisimman tarkkoja ennusteita. Ennusteiden laatua mitataan **tappiofunktiolla** ℒ. Seuraavia tappiofunktioita käytetään usein:

* Regressio-ongelmassa, kun meidän on ennustettava luku, voimme käyttää **absoluuttista virhettä** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| tai **neliövirhettä** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Luokittelussa käytämme **0-1-tappiota** (joka on olennaisesti sama kuin mallin **tarkkuus**) tai **logistista tappiota**.

Yhden tason perceptronissa funktio *f* määriteltiin lineaarisena funktiona *f(x)=wx+b* (tässä *w* on painomatriisi, *x* on syötepiirteiden vektori ja *b* on bias-vektori). Eri neuroverkkorakenteissa tämä funktio voi olla monimutkaisempi.

> Luokittelussa on usein toivottavaa saada todennäköisyydet vastaaville luokille verkon tulosteena. Muuntaaksemme mielivaltaiset luvut todennäköisyyksiksi (esim. normalisoidaksemme tulosteen) käytämme usein **softmax**-funktiota σ, ja funktiosta *f* tulee *f(x)=σ(wx+b)*

Yllä olevassa *f*:n määritelmässä *w* ja *b* kutsutaan **parametreiksi** θ=⟨*w,b*⟩. Annetulla datajoukolla ⟨**X**,**Y**⟩ voimme laskea koko datajoukon kokonaisvirheen parametrien θ funktiona.

> ✅ **Neuroverkon koulutuksen tavoite on minimoida virhe muuttamalla parametreja θ**

## Gradienttimenetelmän optimointi

On olemassa tunnettu funktioiden optimointimenetelmä nimeltä **gradienttimenetelmä**. Ajatuksena on, että voimme laskea tappiofunktion derivaatan (moniulotteisessa tapauksessa kutsutaan **gradientiksi**) parametrien suhteen ja muuttaa parametreja siten, että virhe pienenee. Tämä voidaan muodollistaa seuraavasti:

* Alusta parametrit satunnaisilla arvoilla w<sup>(0)</sup>, b<sup>(0)</sup>
* Toista seuraava askel monta kertaa:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Koulutuksen aikana optimointiaskeleet lasketaan oletettavasti koko datajoukon huomioon ottaen (muista, että tappio lasketaan summana kaikkien opetusnäytteiden läpi). Kuitenkin todellisessa elämässä otamme pieniä osia datajoukosta, joita kutsutaan **minieriksi**, ja laskemme gradientit tietojoukon osajoukon perusteella. Koska osajoukko otetaan satunnaisesti joka kerta, tällaista menetelmää kutsutaan **stokastiseksi gradienttimenetelmäksi** (SGD).

## Monikerroksiset perceptronit ja takaisinkuljetus

Yksikerroksinen verkko, kuten edellä on nähty, pystyy luokittelemaan lineaarisesti erotettavia luokkia. Rikkaamman mallin rakentamiseksi voimme yhdistää useita kerroksia verkkoon. Matemaattisesti se tarkoittaisi, että funktio *f* olisi monimutkaisempi ja se laskettaisiin useassa vaiheessa:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tässä α on **epälineaarinen aktivointifunktio**, σ on softmax-funktio ja parametrit θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Gradienttimenetelmä pysyy samana, mutta gradienttien laskeminen on vaikeampaa. Ketjuerotussäännön avulla voimme laskea derivaatat seuraavasti:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ketjuerotussääntöä käytetään laskemaan tappiofunktion derivaatat parametrien suhteen.

Huomaa, että kaikkien näiden lausekkeiden vasemmanpuoleinen osa on sama, joten voimme tehokkaasti laskea derivaatat aloittamalla tappiofunktiosta ja menemällä "taaksepäin" laskentakaaviossa. Tästä syystä monikerroksisen perceptronin koulutusmenetelmää kutsutaan **takaisinkuljetukseksi** tai 'backpropiksi'.

> TODO: kuvan lähde

> ✅ Käsittelemme takaisinkuljetusta paljon yksityiskohtaisemmin muistikirjaesimerkissämme.

## Yhteenveto

Tässä oppitunnissa olemme rakentaneet oman neuroverkkokirjaston ja käyttäneet sitä yksinkertaiseen kaksiulotteiseen luokittelutehtävään.

## 🚀 Haaste

Mukana olevassa muistikirjassa toteutat oman kehyksen monikerroksisten perceptronien rakentamiseksi ja kouluttamiseksi. Näet yksityiskohtaisesti, miten modernit neuroverkot toimivat.

Siirry OwnFramework-muistikirjaan ja käy se läpi.

## Kertaus ja itseopiskelu

Takaisinkuljetus on yleinen algoritmi tekoälyssä ja koneoppimisessa, ja se on syytä opiskella tarkemmin.

## Tehtävä

Tässä laboratoriossa sinun tulee käyttää tämän oppitunnin aikana rakentamaasi kehystä MNIST-käsinkirjoitettujen numeroiden luokittelun ratkaisemiseksi.

* Ohjeet
* Muistikirja

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä AI-käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää auktoritatiivisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.