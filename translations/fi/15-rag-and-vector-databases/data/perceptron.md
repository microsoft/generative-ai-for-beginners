<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T02:38:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "fi"
}
-->
# Johdatus neuroverkkoihin: Perceptron

Yksi ensimmäisistä yrityksistä toteuttaa jotain nykyaikaisen neuroverkon kaltaista tehtiin Frank Rosenblattin toimesta Cornell Aeronautical Laboratoryssa vuonna 1957. Se oli laitteistototeutus nimeltä "Mark-1", joka oli suunniteltu tunnistamaan yksinkertaisia geometrisia kuvioita, kuten kolmioita, neliöitä ja ympyröitä.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Kuvia Wikipediasta

Syöttökuva esitettiin 20x20 valokennorivistöllä, joten neuroverkossa oli 400 syötettä ja yksi binaarinen lähtö. Yksinkertainen verkko sisälsi yhden neuronin, jota kutsutaan myös **kynnyksen logiikkayksiköksi**. Neuroverkon painot toimivat kuin potentiometrit, jotka vaativat manuaalista säätämistä harjoitusvaiheen aikana.

> ✅ Potentiometri on laite, jonka avulla käyttäjä voi säätää piirin vastusta.

> New York Times kirjoitti tuolloin perceptronista: *sähköisen tietokoneen alkio, jonka [laivasto] odottaa voivan kävellä, puhua, nähdä, kirjoittaa, lisääntyä ja olla tietoinen olemassaolostaan.*

## Perceptron-malli

Oletetaan, että mallissamme on N ominaisuutta, jolloin syöttövektori olisi N:n kokoinen vektori. Perceptron on **binaarinen luokittelumalli**, eli se voi erottaa kahdenlaisia syöttödataa. Oletamme, että jokaiselle syöttövektorille x perceptronimme tuotos olisi joko +1 tai -1 riippuen luokasta. Tuotos lasketaan kaavalla:

y(x) = f(w<sup>T</sup>x)

missä f on askelaktivointifunktio

## Perceptronin opettaminen

Perceptronin opettamiseksi meidän täytyy löytää painojen vektori w, joka luokittelee suurimman osan arvoista oikein, eli tuottaa pienimmän **virheen**. Tämä virhe määritellään **perceptron-kriteerillä** seuraavalla tavalla:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

missä:

* summa otetaan niistä harjoitusdatan pisteistä i, jotka tuottavat väärän luokittelun
* x<sub>i</sub> on syöttödata ja t<sub>i</sub> on joko -1 tai +1 negatiivisille ja positiivisille esimerkeille vastaavasti.

Tätä kriteeriä pidetään painojen w funktiona, ja meidän täytyy minimoida se. Usein käytetään menetelmää nimeltä **gradienttilasku**, jossa aloitetaan joillakin alkuperäisillä painoilla w<sup>(0)</sup>, ja sitten jokaisessa vaiheessa päivitetään painot kaavan mukaan:

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

Tässä oppitunnissa opit perceptronista, joka on binaarinen luokittelumalli, ja kuinka opettaa sitä painojen vektorin avulla.

## 🚀 Haaste

Jos haluat kokeilla oman perceptronin rakentamista, kokeile tätä Microsoft Learn -laboratoriota, joka käyttää Azure ML designeria.

## Katsaus & Itseopiskelu

Jos haluat nähdä, kuinka voimme käyttää perceptronia lelumallin sekä todellisten ongelmien ratkaisemiseen, ja jatkaa oppimista - siirry Perceptron-muistikirjaan.

Tässä on myös mielenkiintoinen artikkeli perceptroneista.

## Tehtävä

Tässä oppitunnissa olemme toteuttaneet perceptronin binaarisen luokittelutehtävän suorittamiseen, ja olemme käyttäneet sitä kahden käsin kirjoitetun numeron luokitteluun. Tässä laboratoriossa sinua pyydetään ratkaisemaan numeron luokittelun ongelma kokonaan, eli määrittämään, mikä numero todennäköisimmin vastaa annettua kuvaa.

* Ohjeet
* Muistikirja

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa auktoritatiiviseksi lähteeksi. Kriittisen tiedon kohdalla suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.