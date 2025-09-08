<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T16:58:54+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin: Perceptroni

Yksi ensimmäisistä yrityksistä toteuttaa jotain nykyaikaisen neuroverkon kaltaista tehtiin vuonna 1957 Frank Rosenblattin toimesta Cornell Aeronautical Laboratoryssa. Se oli laitteistopohjainen toteutus nimeltä "Mark-1", joka oli suunniteltu tunnistamaan primitiivisiä geometrisia kuvioita, kuten kolmioita, neliöitä ja ympyröitä.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Kuvia Wikipediasta

Syötekuva esitettiin 20x20 valosolutaulukolla, joten neuroverkolla oli 400 syötettä ja yksi binäärinen lähtö. Yksinkertainen verkko sisälsi yhden neuronin, jota kutsutaan myös **kynnyslogiikkayksiköksi**. Neuroverkon painot toimivat kuin potentiometrit, joita säädettiin manuaalisesti harjoitteluvaiheessa.

> ✅ Potentiometri on laite, joka mahdollistaa piirin vastuksen säätämisen käyttäjän toimesta.

> The New York Times kirjoitti tuolloin perceptronista: *elektronisen tietokoneen alkio, jonka [laivasto] odottaa pystyvän kävelemään, puhumaan, näkemään, kirjoittamaan, lisääntymään ja tiedostamaan olemassaolonsa.*

## Perceptron-malli

Oletetaan, että mallissamme on N ominaisuutta, jolloin syötevektori on kooltaan N. Perceptron on **binääriluokittelumalli**, eli se pystyy erottamaan kaksi syöteluokkaa toisistaan. Oletamme, että jokaiselle syötevektorille x perceptronin lähtö on joko +1 tai -1 luokasta riippuen. Lähtö lasketaan kaavalla:

y(x) = f(w<sup>T</sup>x)

missä f on askelaktivaatiofunktio

## Perceptronin opettaminen

Perceptronin opettamiseksi meidän täytyy löytää painovektori w, joka luokittelee suurimman osan arvoista oikein, eli tuottaa pienimmän **virheen**. Tämä virhe määritellään **perceptronin kriteerinä** seuraavasti:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

missä:

* summa lasketaan niille harjoitusdatan pisteille i, jotka johtavat väärään luokitteluun
* x<sub>i</sub> on syötedata ja t<sub>i</sub> on joko -1 tai +1 negatiivisille ja positiivisille esimerkeille vastaavasti.

Tätä kriteeriä pidetään painojen w funktiona, ja meidän täytyy minimoida se. Usein käytetään menetelmää nimeltä **gradienttilasku**, jossa aloitetaan jollain alkuarvolla w<sup>(0)</sup> ja päivitetään painoja jokaisella askeleella kaavan mukaisesti:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tässä η on niin kutsuttu **oppimisnopeus** ja ∇E(w) tarkoittaa E:n **gradienttia**. Kun gradientti on laskettu, päädymme muotoon

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmi Pythonilla näyttää tältä:

```python
def train(positive_examples, negative_examples, num_iterations = 100, eta = 1):

    weights = [0,0,0] # Initialize weights (almost randomly :)
        
    for i in range(num_iterations):
        pos = random.choice(positive_examples)
        neg = random.choice(negative_examples)

        z = np.dot(pos, weights) # compute perceptron output
        if z < 0: # positive example classified as negative
            weights = weights + eta*weights.shape

        z  = np.dot(neg, weights)
        if z >= 0: # negative example classified as positive
            weights = weights - eta*weights.shape

    return weights
```

## Yhteenveto

Tässä oppitunnissa opit perceptronista, joka on binääriluokittelumalli, ja miten sitä opetetaan käyttämällä painovektoria.

## 🚀 Haaste

Jos haluat kokeilla oman perceptronin rakentamista, kokeile tätä Microsoft Learn -labraa, joka käyttää Azure ML designeria


## Kertaus & Itsenäinen opiskelu

Nähdäksesi, miten perceptronia voidaan käyttää leikkimielisen ongelman sekä todellisten ongelmien ratkaisuun ja jatkaaksesi oppimista - siirry Perceptron-muistikirjaan.

Tässä on myös mielenkiintoinen artikkeli perceptroneista.

## Tehtävä

Tässä oppitunnissa olemme toteuttaneet perceptronin binääriluokittelutehtävään ja käyttäneet sitä kahden käsinkirjoitetun numeron luokitteluun. Tässä labrassa sinun tulee ratkaista numeroluokittelun ongelma kokonaisuudessaan, eli määrittää, mikä numero todennäköisimmin vastaa annettua kuvaa.

* Ohjeet
* Muistikirja

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.