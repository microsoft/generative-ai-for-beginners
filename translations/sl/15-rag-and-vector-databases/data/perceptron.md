<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-06-25T23:45:42+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže: Perceptron

Eden prvih poskusov za implementacijo nečesa podobnega moderni nevronski mreži je izvedel Frank Rosenblatt iz Cornell Aeronautical Laboratory leta 1957. Bila je to strojna implementacija imenovana "Mark-1", zasnovana za prepoznavanje primitivnih geometrijskih oblik, kot so trikotniki, kvadrati in krogi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike iz Wikipedije

Vhodna slika je bila predstavljena z 20x20 fotocelično matriko, tako da je imela nevronska mreža 400 vhodov in en binarni izhod. Enostavna mreža je vsebovala en nevron, imenovan tudi **pragovna logična enota**. Teže nevronske mreže so delovale kot potenciometri, ki so zahtevali ročno nastavitev med fazo učenja.

> ✅ Potenciometer je naprava, ki omogoča uporabniku prilagajanje upornosti v vezju.

> The New York Times je takrat pisal o perceptronu: *embrio elektronskega računalnika, ki [ga mornarica] pričakuje, da bo lahko hodil, govoril, videl, pisal, se razmnoževal in se zavedal svojega obstoja.*

## Model perceptrona

Predpostavimo, da imamo v našem modelu N značilnosti, v tem primeru bi bil vhodni vektor vektor velikosti N. Perceptron je model za **binarno klasifikacijo**, tj. lahko razlikuje med dvema razredoma vhodnih podatkov. Predpostavili bomo, da bi bil za vsak vhodni vektor x izhod našega perceptrona bodisi +1 bodisi -1, odvisno od razreda. Izhod bo izračunan z uporabo formule:

y(x) = f(w<sup>T</sup>x)

kjer je f stopničasta aktivacijska funkcija

## Učenje perceptrona

Za učenje perceptrona moramo najti vektorsko težo w, ki pravilno klasificira večino vrednosti, tj. povzroči najmanjšo **napako**. Ta napaka je definirana z **merilom perceptrona** na naslednji način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kjer:

* vsota je vzeta za tiste točke učnih podatkov i, ki povzročijo napačno klasifikacijo
* x<sub>i</sub> so vhodni podatki, in t<sub>i</sub> je bodisi -1 ali +1 za negativne oziroma pozitivne primere.

To merilo se obravnava kot funkcija teže w, in ga moramo minimizirati. Pogosto se uporablja metoda, imenovana **gradientni spust**, pri kateri začnemo z nekaterimi začetnimi težami w<sup>(0)</sup>, nato pa pri vsakem koraku posodobimo teže po formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tukaj je η tako imenovana **hitrost učenja**, in ∇E(w) označuje **gradient** E. Ko izračunamo gradient, dobimo

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritem v Pythonu izgleda takole:

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

## Zaključek

V tej lekciji ste se naučili o perceptronu, ki je model za binarno klasifikacijo, in kako ga usposobiti z uporabo vektorske teže.

## 🚀 Izziv

Če želite poskusiti zgraditi svoj perceptron, poskusite to delavnico na Microsoft Learn, ki uporablja Azure ML designer.

## Pregled in samostojno učenje

Če želite videti, kako lahko uporabimo perceptron za reševanje preprostih problemov in tudi realnih problemov ter nadaljevati z učenjem, pojdite na zvezek Perceptron.

Tukaj je tudi zanimiv članek o perceptronih.

## Naloga

V tej lekciji smo implementirali perceptron za nalogo binarne klasifikacije in ga uporabili za razvrščanje med dvema ročno napisanima številkama. V tej delavnici ste pozvani, da popolnoma rešite problem razvrščanja številk, tj. določite, katera številka najverjetneje ustreza dani sliki.

* Navodila
* Zvezek

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne razlage, ki izhajajo iz uporabe tega prevoda.