<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-08-25T12:47:50+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "lt"
}
-->
# Įvadas į neuroninius tinklus: perceptronas

Vienas pirmųjų bandymų sukurti kažką panašaus į šiuolaikinį neuroninį tinklą buvo atliktas Franko Rosenblatto iš Kornelio aeronautikos laboratorijos 1957 metais. Tai buvo aparatinis įgyvendinimas, pavadintas „Mark-1“, sukurtas atpažinti paprastas geometrines figūras, tokias kaip trikampiai, kvadratai ir apskritimai.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Paveikslėliai iš Vikipedijos

Įvesties vaizdas buvo vaizduojamas 20x20 fotoląstelių matrica, taigi neuroninis tinklas turėjo 400 įėjimų ir vieną dvejetainį išėjimą. Paprastas tinklas turėjo vieną neuroną, dar vadinamą **slenksčio logikos vienetu**. Neuroninio tinklo svoriai veikė kaip potenciometrai, kuriuos reikėjo rankiniu būdu reguliuoti mokymo metu.

> ✅ Potenciometras – tai prietaisas, leidžiantis vartotojui reguliuoti grandinės varžą.

> Tuo metu „The New York Times“ rašė apie perceptroną: *elektroninio kompiuterio embrionas, iš kurio [JAV karinis jūrų laivynas] tikisi, kad jis galės vaikščioti, kalbėti, matyti, rašyti, daugintis ir suvokti savo egzistavimą.*

## Perceptrono modelis

Tarkime, kad mūsų modelyje yra N požymių, tuomet įvesties vektorius bus N dydžio vektorius. Perceptronas yra **dvejetainės klasifikacijos** modelis, t.y. jis gali atskirti dvi įvesties duomenų klases. Tarkime, kad kiekvienam įvesties vektoriui x perceptrono išėjimas bus +1 arba -1, priklausomai nuo klasės. Išėjimas skaičiuojamas pagal formulę:

y(x) = f(w<sup>T</sup>x)

kur f yra slenksčio aktyvacijos funkcija

## Perceptrono mokymas

Norint apmokyti perceptroną, reikia rasti svorių vektorių w, kuris teisingai klasifikuotų kuo daugiau reikšmių, t.y. duotų mažiausią **klaidą**. Ši klaida apibrėžiama pagal **perceptrono kriterijų** taip:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kur:

* suma skaičiuojama tik tiems mokymo duomenų taškams i, kurie buvo neteisingai klasifikuoti
* x<sub>i</sub> – įvesties duomenys, o t<sub>i</sub> – -1 arba +1, atitinkamai neigiamiems ir teigiamiems pavyzdžiams.

Šis kriterijus laikomas svorių w funkcija, ir jį reikia minimizuoti. Dažnai naudojamas metodas, vadinamas **gradientiniu nusileidimu**, kai pradedama nuo pradinio svorių vektoriaus w<sup>(0)</sup>, o kiekviename žingsnyje svoriai atnaujinami pagal formulę:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Čia η – vadinamas **mokymosi greitis**, o ∇E(w) žymi E **gradientą**. Apskaičiavus gradientą, gauname

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Algoritmas Python kalba atrodo taip:

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

## Išvada

Šioje pamokoje sužinojote apie perceptroną – dvejetainės klasifikacijos modelį, ir kaip jį apmokyti naudojant svorių vektorių.

## 🚀 Iššūkis

Jei norite patys sukurti perceptroną, išbandykite šią laboratoriją Microsoft Learn, kurioje naudojamas Azure ML dizaineris


## Apžvalga ir savarankiškas mokymasis

Norėdami pamatyti, kaip perceptroną galima naudoti sprendžiant žaislinius ir realius uždavinius, ir tęsti mokymąsi – eikite į Perceptron užrašų knygą.

Taip pat štai įdomus straipsnis apie perceptronus.

## Užduotis

Šioje pamokoje įgyvendinome perceptroną dvejetainės klasifikacijos užduočiai ir panaudojome jį dviem ranka rašytiems skaitmenims klasifikuoti. Šioje laboratorijoje jūsų prašoma visiškai išspręsti skaitmenų klasifikavimo uždavinį, t.y. nustatyti, kuris skaitmuo greičiausiai atitinka pateiktą vaizdą.

* Instrukcijos
* Užrašų knyga

---

**Atsakomybės atsisakymas**:  
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Svarbios informacijos atveju rekomenduojame profesionalų žmogaus vertimą. Mes neatsakome už nesusipratimus ar neteisingą interpretavimą, kilusį dėl šio vertimo naudojimo.