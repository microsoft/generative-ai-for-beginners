<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:01:52+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže: Perceptron

Eden prvih poskusov implementacije nečesa podobnega sodobni nevronski mreži je leta 1957 izvedel Frank Rosenblatt iz Cornell Aeronautical Laboratory. Šlo je za strojno implementacijo z imenom "Mark-1", zasnovano za prepoznavanje osnovnih geometrijskih likov, kot so trikotniki, kvadrati in krogi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Slike iz Wikipedije

Vhodna slika je bila predstavljena z mrežo 20x20 fotocelic, tako da je nevronska mreža imela 400 vhodov in en binarni izhod. Preprosta mreža je vsebovala en nevron, imenovan tudi **enota pragovne logike**. Teže v nevronski mreži so delovale kot potenciometri, ki so zahtevali ročno nastavitev med fazo učenja.

> ✅ Potenciometer je naprava, ki uporabniku omogoča prilagajanje upornosti v vezju.

> The New York Times je takrat o perceptronu zapisal: *zarodek elektronskega računalnika, za katerega [Navy] pričakuje, da bo lahko hodil, govoril, videl, pisal, se razmnoževal in bil zavedajoč svojega obstoja.*

## Model perceptrona

Predpostavimo, da imamo v našem modelu N značilnosti, v tem primeru je vhodni vektor velikosti N. Perceptron je model **binarne klasifikacije**, kar pomeni, da lahko razlikuje med dvema razredoma vhodnih podatkov. Predpostavili bomo, da je za vsak vhodni vektor x izhod našega perceptrona bodisi +1 ali -1, odvisno od razreda. Izhod se izračuna po formuli:

y(x) = f(w<sup>T</sup>x)

kjer je f stopničasta aktivacijska funkcija

## Učenje perceptrona

Za učenje perceptrona moramo najti vektor uteži w, ki pravilno klasificira večino vrednosti, torej povzroči najmanjšo **napako**. Ta napaka je definirana z **perceptronovim kriterijem** na naslednji način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kjer:

* se vsota izračuna za tiste učne podatke i, ki so napačno klasificirani
* x<sub>i</sub> so vhodni podatki, t<sub>i</sub> pa je bodisi -1 ali +1 za negativne oziroma pozitivne primere.

Ta kriterij obravnavamo kot funkcijo uteži w, ki jo želimo minimizirati. Pogosto se uporablja metoda, imenovana **gradientni spust**, pri kateri začnemo z začetnimi utežmi w<sup>(0)</sup> in nato pri vsakem koraku posodobimo uteži po formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tu je η t.i. **hitrost učenja**, ∇E(w) pa predstavlja **gradient** funkcije E. Ko izračunamo gradient, dobimo:

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

V tej lekciji ste spoznali perceptron, ki je model binarne klasifikacije, in kako ga naučiti z uporabo vektorja uteži.

## 🚀 Izziv

Če želite poskusiti zgraditi svoj perceptron, preizkusite ta laboratorij na Microsoft Learn, ki uporablja Azure ML designer.

## Pregled in samostojno učenje

Da vidite, kako lahko perceptron uporabimo za reševanje preprostih in tudi resničnih problemov ter nadaljujete z učenjem, pojdite na Perceptron zvezek.

Tukaj je tudi zanimiv članek o perceptronih.

## Naloga

V tej lekciji smo implementirali perceptron za nalogo binarne klasifikacije in ga uporabili za razvrščanje med dvema ročno napisanima številkama. V tej laboratorijski nalogi morate popolnoma rešiti problem klasifikacije številk, torej določiti, katera številka najbolj ustreza dani sliki.

* Navodila
* Zvezek

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.