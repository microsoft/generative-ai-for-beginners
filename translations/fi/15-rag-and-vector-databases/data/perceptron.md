<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:41:36+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "fi"
}
-->
# Johdanto neuroverkkoihin: Perceptron

Yksi ensimmäisistä yrityksistä toteuttaa jotain modernin neuroverkon kaltaista tehtiin Frank Rosenblattin toimesta Cornellin Aeronautical Laboratoryssä vuonna 1957. Se oli laitteistototeutus nimeltä "Mark-1", joka suunniteltiin tunnistamaan yksinkertaisia geometrisia kuvioita, kuten kolmioita, neliöitä ja ympyröitä.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Kuvat Wikipediasta

Syötekuva esitettiin 20x20 valokennojen matriisina, joten neuroverkolla oli 400 syötettä ja yksi binäärinen lähtö. Yksinkertainen verkko sisälsi yhden neuronin, jota kutsuttiin myös **kynnyksen logiikkayksiköksi**. Neuroverkon painot toimivat kuin potentiometrit, jotka vaativat manuaalista säätämistä harjoitteluvaiheen aikana.

> ✅ Potentiometri on laite, joka mahdollistaa käyttäjän säätää piirin vastusta.

> New York Times kirjoitti tuolloin perceptronista: *sähkötietokoneen alkio, jonka [laivasto] odottaa pystyvän kävelemään, puhumaan, näkemään, kirjoittamaan, lisääntymään ja olemaan tietoinen olemassaolostaan.*

## Perceptron-malli

Oletetaan, että mallissamme on N ominaisuutta, jolloin syötevektori olisi kooltaan N. Perceptron on **binääriluokittelumalli**, eli se voi erottaa kaksi syötedatan luokkaa. Oletamme, että jokaiselle syötevektorille x perceptronimme tuotos olisi joko +1 tai -1 riippuen luokasta. Tuotos lasketaan kaavalla:

y(x) = f(w<sup>T</sup>x)

missä f on porrasaktivointifunktio

## Perceptronin kouluttaminen

Perceptronin kouluttamiseksi meidän täytyy löytää painovektori w, joka luokittelee suurimman osan arvoista oikein, eli tuottaa pienimmän **virheen**. Tämä virhe määritellään **perceptronin kriteerin** avulla seuraavasti:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

missä:

* summa otetaan niistä harjoitusdatapisteistä i, jotka johtavat väärään luokitteluun
* x<sub>i</sub> on syötedata, ja t<sub>i</sub> on joko -1 tai +1 negatiivisille ja positiivisille esimerkeille vastaavasti.

Tätä kriteeriä pidetään painojen w funktiona, ja meidän täytyy minimoida se. Usein käytetään menetelmää nimeltä **gradienttilasku**, jossa aloitetaan jollain alkuperäisillä painoilla w<sup>(0)</sup>, ja sitten jokaisessa vaiheessa päivitetään painoja kaavan mukaisesti:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tässä η on niin sanottu **oppimisnopeus**, ja ∇E(w) tarkoittaa E:n **gradienttia**. Kun olemme laskeneet gradientin, päädymme seuraavaan:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmi Pythonissa näyttää tältä:

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

Tässä oppitunnissa opit perceptronista, joka on binääriluokittelumalli, ja kuinka kouluttaa sitä käyttämällä painovektoria.

## 🚀 Haaste

Jos haluat kokeilla rakentaa oman perceptronin, kokeile tätä Microsoft Learnin laboratoriota, joka käyttää Azure ML -suunnittelijaa.

## Katsaus & Itseopiskelu

Jos haluat nähdä, kuinka voimme käyttää perceptronia ratkaisemaan leikkiongelmia sekä tosielämän ongelmia, ja jatkaa oppimista - siirry Perceptron-muistikirjaan.

Tässä on myös mielenkiintoinen artikkeli perceptroneista.

## Tehtävä

Tässä oppitunnissa olemme toteuttaneet perceptronin binääriluokittelutehtävää varten, ja olemme käyttäneet sitä luokittelemaan kahta käsinkirjoitettua numeroa. Tässä laboratoriossa sinua pyydetään ratkaisemaan numeroluokittelun ongelma kokonaan, eli määrittämään, mikä numero todennäköisesti vastaa annettua kuvaa.

* Ohjeet
* Muistikirja

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.