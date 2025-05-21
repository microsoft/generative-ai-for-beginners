<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:44:43+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "sl"
}
-->
# Uvod v nevronske mreže: Perceptron

Eden prvih poskusov za izvedbo nečesa podobnega sodobni nevronski mreži je izvedel Frank Rosenblatt iz Cornell Aeronautical Laboratory leta 1957. Šlo je za strojno izvedbo, imenovano "Mark-1", ki je bila zasnovana za prepoznavanje primitivnih geometrijskih likov, kot so trikotniki, kvadrati in krogi.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='Perceptron Mark 1' />|

> Slike iz Wikipedije

Vhodna slika je bila predstavljena z 20x20 matriko fotocelic, zato je imela nevronska mreža 400 vhodov in en binarni izhod. Enostavna mreža je vsebovala en nevron, imenovan tudi **enota logičnega praga**. Teže nevronske mreže so delovale kot potenciometri, ki so zahtevali ročno nastavitev med fazo učenja.

> ✅ Potenciometer je naprava, ki omogoča uporabniku nastavitev upornosti vezja.

> New York Times je takrat pisal o perceptronu: *zarodek elektronskega računalnika, ki [morje] pričakuje, da bo lahko hodil, govoril, videl, pisal, se reproduciral in bil zavesten svoje eksistence.*

## Model perceptrona

Predpostavimo, da imamo v našem modelu N značilnosti, v tem primeru bi bil vhodni vektor vektor velikosti N. Perceptron je model **binarne klasifikacije**, kar pomeni, da lahko razlikuje med dvema razredoma vhodnih podatkov. Predpostavili bomo, da bi bil za vsak vhodni vektor x izhod našega perceptrona bodisi +1 ali -1, odvisno od razreda. Izhod se bo izračunal po formuli:

y(x) = f(w<sup>T</sup>x)

kjer je f stopničasta aktivacijska funkcija

## Učenje perceptrona

Za učenje perceptrona moramo najti vektorsko težo w, ki večino vrednosti pravilno klasificira, torej rezultira v najmanjši **napaki**. Ta napaka je opredeljena z **perceptronskim kriterijem** na naslednji način:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kjer:

* se vsota vzame na tistih točkah učnih podatkov i, ki rezultirajo v napačni klasifikaciji
* x<sub>i</sub> so vhodni podatki, in t<sub>i</sub> je bodisi -1 ali +1 za negativne in pozitivne primere ustrezno.

Ta kriterij se šteje kot funkcija teže w, ki jo moramo minimizirati. Pogosto se uporablja metoda, imenovana **gradientni spust**, pri kateri začnemo z začetnimi težami w<sup>(0)</sup>, in nato v vsakem koraku posodobimo teže po formuli:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Tu je η tako imenovana **hitrost učenja**, in ∇E(w) označuje **gradient** E. Ko izračunamo gradient, dobimo

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

V tej lekciji ste se naučili o perceptronu, ki je model binarne klasifikacije, in kako ga trenirati z uporabo vektorske teže.

## 🚀 Izziv

Če želite poskusiti zgraditi svoj perceptron, poskusite ta laboratorij na Microsoft Learn, ki uporablja Azure ML designer.

## Pregled in samostojno učenje

Da vidite, kako lahko uporabimo perceptron za reševanje enostavnih problemov kot tudi realnih problemov, in da nadaljujete z učenjem - pojdite na zvezek Perceptron.

Tukaj je zanimiv članek o perceptronih.

## Naloga

V tej lekciji smo izvedli perceptron za nalogo binarne klasifikacije, in uporabili smo ga za klasifikacijo med dvema ročno napisanima številkama. V tem laboratoriju ste pozvani, da popolnoma rešite problem klasifikacije številk, torej določite, katera številka najverjetneje ustreza dani sliki.

* Navodila
* Zvezek

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za strojno prevajanje [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku je treba obravnavati kot verodostojen vir. Za ključne informacije priporočamo strokovno človeško prevajanje. Ne odgovarjamo za morebitna nesporazumevanja ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.