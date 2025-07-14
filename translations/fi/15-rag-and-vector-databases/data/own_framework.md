<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:48:09+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin. Monikerroksinen perceptroni

Edellisessä osassa opit yksinkertaisimmasta neuroverkkomallista – yksikerroksisesta perceptronista, joka on lineaarinen kahden luokan luokittelumalli.

Tässä osassa laajennamme tätä mallia joustavammaksi rakenteeksi, joka mahdollistaa:

* **moniluokkaluokittelun** kahden luokan lisäksi
* **regressio-ongelmien** ratkaisemisen luokittelun lisäksi
* luokkien erottamisen, jotka eivät ole lineaarisesti erotettavissa

Kehitämme myös oman modulaarisen kehyksen Pythonilla, jonka avulla voimme rakentaa erilaisia neuroverkkorakenteita.

## Koneoppimisen formalisaatio

Aloitetaan koneoppimisongelman formalisoimisesta. Oletetaan, että meillä on opetusdatajoukko **X** ja siihen liittyvät tunnisteet **Y**, ja meidän täytyy rakentaa malli *f*, joka tekee mahdollisimman tarkkoja ennusteita. Ennusteiden laatua mitataan **häviöfunktiolla** ℒ. Seuraavia häviöfunktioita käytetään usein:

* Regressio-ongelmassa, jossa ennustetaan lukuarvoa, voimme käyttää **absoluuttista virhettä** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>| tai **neliövirhettä** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Luokittelussa käytämme **0-1 häviötä** (joka vastaa mallin **tarkkuutta**) tai **logistista häviötä**.

Yksikerroksisessa perceptronissa funktio *f* määriteltiin lineaarisena funktiona *f(x)=wx+b* (tässä *w* on painomatriisi, *x* on syöteominaisuuksien vektori ja *b* on bias-vektori). Eri neuroverkkorakenteissa tämä funktio voi olla monimutkaisempi.

> Luokittelussa on usein toivottavaa saada verkon ulostulona luokkien todennäköisyydet. Muuttaaksemme mielivaltaiset luvut todennäköisyyksiksi (esim. normalisoidaksemme ulostulon), käytämme usein **softmax**-funktiota σ, jolloin funktio *f* muuttuu muotoon *f(x)=σ(wx+b)*

Edellä määritellyssä funktiossa *f* parametreja *w* ja *b* kutsutaan **parametreiksi** θ=⟨*w,b*⟩. Kun datasetti ⟨**X**,**Y**⟩ on annettu, voimme laskea kokonaisvirheen koko datasetille parametrien θ funktiona.

> ✅ **Neuroverkon koulutuksen tavoitteena on minimoida virhe muuttamalla parametreja θ**

## Gradienttilaskun optimointi

Tunnettu funktioiden optimointimenetelmä on **gradienttilasku**. Ajatus on, että voimme laskea häviöfunktion derivaatan (moniulotteisessa tapauksessa **gradientin**) parametreihin nähden ja muuttaa parametreja siten, että virhe pienenee. Tämä voidaan formalisoida seuraavasti:

* Alustetaan parametrit satunnaisilla arvoilla w<sup>(0)</sup>, b<sup>(0)</sup>
* Toistetaan seuraava askel monta kertaa:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup> - η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup> - η∂ℒ/∂b

Koulutuksen aikana optimointiaskeleet lasketaan yleensä koko datasetin perusteella (muista, että häviö lasketaan kaikkien opetusnäytteiden summana). Käytännössä otamme kuitenkin pieniä osajoukkoja datasta, joita kutsutaan **minieräjoukoiksi** (minibatches), ja laskemme gradientit näiden osajoukkojen perusteella. Koska osajoukko valitaan satunnaisesti joka kerta, tätä menetelmää kutsutaan **stokastiseksi gradienttilaskuksi** (SGD).

## Monikerroksiset perceptronit ja takaisinkytkentä (backpropagation)

Yksikerroksinen verkko, kuten yllä nähtiin, pystyy luokittelemaan lineaarisesti erotettavat luokat. Rakentaaksemme monipuolisemman mallin voimme yhdistää useita verkon kerroksia. Matemaattisesti tämä tarkoittaa, että funktio *f* saa monimutkaisemman muodon ja lasketaan useassa vaiheessa:
* z<sub>1</sub> = w<sub>1</sub>x + b<sub>1</sub>
* z<sub>2</sub> = w<sub>2</sub>α(z<sub>1</sub>) + b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Tässä α on **ei-lineaarinen aktivointifunktio**, σ on softmax-funktio ja parametrit θ = ⟨*w<sub>1</sub>, b<sub>1</sub>, w<sub>2</sub>, b<sub>2</sub>*⟩.

Gradienttilasku pysyy samana, mutta gradienttien laskeminen on monimutkaisempaa. Ketjusäännön avulla voimme laskea derivaatat seuraavasti:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ketjusääntöä käytetään häviöfunktion derivaattojen laskemiseen parametrien suhteen.

Huomaa, että kaikkien näiden lausekkeiden vasemmanpuoleinen osa on sama, joten voimme tehokkaasti laskea derivaatat aloittaen häviöfunktiosta ja kulkemalla "taaksepäin" laskentakaavion läpi. Tätä monikerroksisen perceptronin koulutusmenetelmää kutsutaan **takaisinkytkennäksi** eli backpropagationiksi.

> TODO: kuvan lähde

> ✅ Käymme backpropagationin tarkemmin läpi esimerkkimuistiossa.

## Yhteenveto

Tässä oppitunnissa rakensimme oman neuroverkkokirjaston ja käytimme sitä yksinkertaisen kaksidimensioisen luokittelutehtävän ratkaisemiseen.

## 🚀 Haaste

Mukana olevassa muistiossa toteutat oman kehyksesi monikerroksisten perceptronien rakentamiseen ja kouluttamiseen. Näet yksityiskohtaisesti, miten nykyaikaiset neuroverkot toimivat.

Siirry OwnFramework-muistioon ja käy se läpi.

## Kertaus & Itsenäinen opiskelu

Takaisinkytkentä on yleinen algoritmi tekoälyssä ja koneoppimisessa, jota kannattaa opiskella tarkemmin.

## Tehtävä

Tässä laboratoriossa sinun tulee käyttää tässä oppitunnissa rakentamaasi kehystä ratkaistaksesi MNIST-käsinkirjoitettujen numeroiden luokittelutehtävä.

* Ohjeet
* Muistio

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.