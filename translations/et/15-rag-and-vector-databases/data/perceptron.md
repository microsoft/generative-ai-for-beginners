<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-10-11T11:16:45+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "et"
}
-->
# Sissejuhatus närvivõrkudesse: Perceptron

Üks esimesi katseid luua midagi tänapäevase närvivõrgu sarnast tehti 1957. aastal Frank Rosenblatti poolt Cornell Aeronautical Laboratory's. See oli riistvaraline lahendus nimega "Mark-1", mis oli loodud primitiivsete geomeetriliste kujundite, nagu kolmnurgad, ruudud ja ringid, äratundmiseks.

|      |      |
|--------------|-----------|
|<img src='../../../../translated_images/Rosenblatt-wikipedia.1d205667acda28c0f97ad594eb6dadfa0485605f3fb2155eca46a0255e98efac.et.jpg' alt='Frank Rosenblatt'/> | <img src='../../../../translated_images/Mark_I_perceptron_wikipedia.434e46ca39e2be801976110f8b1b75b13d1197f69e3a5f8b7537b43d35413e6f.et.jpg' alt='Mark 1 Perceptron' />|

> Pildid Wikipediast

Sisendpilt esitati 20x20 fototundliku elemendi maatriksina, seega oli närvivõrgul 400 sisendit ja üks binaarne väljund. Lihtne võrk koosnes ühest neuronist, mida nimetatakse ka **läve loogika üksuseks**. Närvivõrgu kaalu väärtused toimisid nagu potentsiomeetrid, mida tuli treeningfaasis käsitsi reguleerida.

> ✅ Potentsiomeeter on seade, mis võimaldab kasutajal reguleerida vooluringi takistust.

> The New York Times kirjutas tol ajal perceptroni kohta: *elektroonilise arvuti embrüo, millest [merevägi] loodab, et see suudab kõndida, rääkida, näha, kirjutada, end paljundada ja olla teadlik oma olemasolust.*

## Perceptroni mudel

Oletame, et meie mudelis on N tunnust, sel juhul oleks sisendvektor suurusega N. Perceptron on **binaarne klassifitseerimismudel**, st see suudab eristada kahte sisendandmete klassi. Eeldame, et iga sisendvektori x korral on meie perceptroni väljund kas +1 või -1, sõltuvalt klassist. Väljund arvutatakse järgmise valemi abil:

y(x) = f(w<sup>T</sup>x)

kus f on astmelise aktiveerimise funktsioon.

## Perceptroni treenimine

Perceptroni treenimiseks peame leidma kaaluvektori w, mis klassifitseerib enamik väärtusi õigesti, st mille tulemuseks on kõige väiksem **viga**. See viga määratletakse **perceptroni kriteeriumi** järgi järgmiselt:

E(w) = -&sum;w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kus:

* summa võetakse nende treeningandmepunktide i kohta, mis annavad vale klassifikatsiooni
* x<sub>i</sub> on sisendandmed ja t<sub>i</sub> on vastavalt -1 või +1 negatiivsete ja positiivsete näidete jaoks.

Seda kriteeriumi käsitletakse kaalu w funktsioonina ja me peame selle minimeerima. Sageli kasutatakse meetodit nimega **gradientlangus**, mille puhul alustame mõnest esialgsest kaalust w<sup>(0)</sup> ja seejärel igal sammul uuendame kaale järgmise valemi järgi:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - &eta;&nabla;E(w)

Siin on &eta; nn **õppemäär** ja &nabla;E(w) tähistab E **gradienti**. Pärast gradiendi arvutamist jõuame valemini:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + &sum;&eta;x<sub>i</sub>t<sub>i</sub>

Algoritm Pythonis näeb välja selline:

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

## Kokkuvõte

Selles õppetükis õppisite perceptroni kohta, mis on binaarne klassifitseerimismudel, ja kuidas seda treenida kaaluvektori abil.

## 🚀 Väljakutse

Kui soovite proovida ise perceptroni luua, proovige seda laborit Microsoft Learnis, mis kasutab Azure ML disainerit.

## Ülevaade ja iseseisev õppimine

Et näha, kuidas perceptronit saab kasutada nii mänguliste kui ka päriselu probleemide lahendamiseks, ja õppimist jätkata, minge Perceptroni märkmikusse.

Siin on ka huvitav artikkel perceptronite kohta.

## Ülesanne

Selles õppetükis rakendasime perceptroni binaarse klassifitseerimise ülesande jaoks ja kasutasime seda kahe käsitsi kirjutatud numbri eristamiseks. Selles laboris palutakse teil lahendada numbrite klassifitseerimise probleem täielikult, st määrata, milline number kõige tõenäolisemalt vastab antud pildile.

* Juhised
* Märkmik

---

**Lahtiütlus**:  
See dokument on tõlgitud, kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi püüame tagada täpsust, palume arvestada, et automaatsed tõlked võivad sisaldada vigu või ebatäpsusi. Algset dokumenti selle algses keeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitame kasutada professionaalset inimtõlget. Me ei vastuta selle tõlke kasutamisest tulenevate arusaamatuste või valede tõlgenduste eest.