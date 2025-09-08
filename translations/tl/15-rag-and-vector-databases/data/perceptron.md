<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-07-09T17:00:01+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks: Perceptron

Isa sa mga unang pagsubok na gumawa ng katulad ng modernong neural network ay ginawa ni Frank Rosenblatt mula sa Cornell Aeronautical Laboratory noong 1957. Isa itong hardware implementation na tinawag na "Mark-1", na idinisenyo upang makilala ang mga simpleng hugis tulad ng tatsulok, parisukat, at bilog.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Mga larawan mula sa Wikipedia

Ang input na imahe ay kinakatawan ng 20x20 na photocell array, kaya ang neural network ay may 400 inputs at isang binary output. Ang simpleng network ay may isang neuron, na tinatawag ding **threshold logic unit**. Ang mga timbang ng neural network ay kumikilos tulad ng mga potentiometer na kailangang mano-manong i-adjust sa panahon ng training.

> ✅ Ang potentiometer ay isang aparato na nagpapahintulot sa gumagamit na baguhin ang resistensya ng isang circuit.

> Sinulat ng The New York Times tungkol sa perceptron noong panahong iyon: *ang simula ng isang electronic computer na inaasahan ng Navy na kaya nang maglakad, magsalita, makakita, magsulat, magparami ng sarili, at maging mulat sa sariling pag-iral.*

## Modelo ng Perceptron

Ipagpalagay natin na mayroon tayong N na features sa ating modelo, kaya ang input vector ay isang vector na may sukat na N. Ang perceptron ay isang **binary classification** na modelo, ibig sabihin kaya nitong paghiwalayin ang dalawang klase ng input data. Ipagpalagay natin na para sa bawat input vector x, ang output ng ating perceptron ay +1 o -1, depende sa klase. Ang output ay kakalkulahin gamit ang pormula:

y(x) = f(w<sup>T</sup>x)

kung saan ang f ay isang step activation function

## Pagsasanay ng Perceptron

Para sanayin ang perceptron, kailangan nating hanapin ang weights vector w na tama ang pagklasipika sa karamihan ng mga halaga, ibig sabihin ay nagreresulta sa pinakamaliit na **error**. Ang error na ito ay tinutukoy ng **perceptron criterion** sa sumusunod na paraan:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kung saan:

* ang suma ay kinukuha sa mga training data points i na nagreresulta sa maling klasipikasyon
* ang x<sub>i</sub> ay input data, at ang t<sub>i</sub> ay -1 o +1 para sa mga negatibo at positibong halimbawa ayon sa pagkakasunod

Ang kriteriang ito ay itinuturing na isang function ng weights w, at kailangan natin itong i-minimize. Madalas, ginagamit ang isang paraan na tinatawag na **gradient descent**, kung saan nagsisimula tayo sa ilang initial weights w<sup>(0)</sup>, at sa bawat hakbang ay ina-update ang weights gamit ang pormula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Dito, ang η ay tinatawag na **learning rate**, at ang ∇E(w) ay ang **gradient** ng E. Pagkatapos makalkula ang gradient, nagiging:

w<sup>(t+1)</sup> = w<sup>(t)</sup> + ∑ηx<sub>i</sub>t<sub>i</sub>

Ganito ang hitsura ng algorithm sa Python:

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

## Konklusyon

Sa araling ito, natutunan mo ang tungkol sa perceptron, isang binary classification na modelo, at kung paano ito sanayin gamit ang weights vector.

## 🚀 Hamon

Kung gusto mong subukan gumawa ng sarili mong perceptron, subukan ang lab na ito sa Microsoft Learn na gumagamit ng Azure ML designer


## Review at Sariling Pag-aaral

Para makita kung paano natin magagamit ang perceptron sa paglutas ng mga simpleng problema pati na rin sa mga totoong buhay na problema, at para magpatuloy sa pag-aaral - pumunta sa Perceptron notebook.

Narito rin ang isang kawili-wiling artikulo tungkol sa mga perceptron.

## Takdang-Aralin

Sa araling ito, nakagawa tayo ng perceptron para sa binary classification na gawain, at ginamit natin ito para magklasipika sa pagitan ng dalawang handwritten digits. Sa lab na ito, hihilingin kang lutasin ang problema ng digit classification nang buo, ibig sabihin ay tukuyin kung aling digit ang pinaka-malamang na tumutugma sa isang ibinigay na imahe.

* Mga Tagubilin
* Notebook

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.