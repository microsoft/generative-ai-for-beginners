<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "59021c5f419d3feda19075910a74280a",
  "translation_date": "2025-05-20T06:42:02+00:00",
  "source_file": "15-rag-and-vector-databases/data/perceptron.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks: Perceptron

Isa sa mga unang pagtatangka na ipatupad ang isang bagay na katulad ng modernong neural network ay ginawa ni Frank Rosenblatt mula sa Cornell Aeronautical Laboratory noong 1957. Ito ay isang hardware na implementasyon na tinawag na "Mark-1", na dinisenyo upang makilala ang mga primitibong hugis na geometric, tulad ng mga tatsulok, parisukat, at bilog.

|      |      |
|--------------|-----------|
|<img src='images/Rosenblatt-wikipedia.jpg' alt='Frank Rosenblatt'/> | <img src='images/Mark_I_perceptron_wikipedia.jpg' alt='The Mark 1 Perceptron' />|

> Mga imahe mula sa Wikipedia

Ang input na imahe ay kinakatawan ng 20x20 photocell array, kaya ang neural network ay may 400 na inputs at isang binary na output. Ang simpleng network ay naglalaman ng isang neuron, na tinatawag ding **threshold logic unit**. Ang mga bigat ng neural network ay kumikilos tulad ng mga potentiometer na nangangailangan ng manwal na pagsasaayos sa panahon ng pagsasanay.

> ✅ Ang potentiometer ay isang aparato na nagpapahintulot sa gumagamit na ayusin ang resistensya ng isang circuit.

> Sinulat ng The New York Times tungkol sa perceptron noong panahong iyon: *ang embryo ng isang electronic computer na [ang Navy] ay umaasa na makakalakad, makakapagsalita, makakakita, makakasulat, makakagawa ng sarili at magiging mulat sa kanyang pag-iral.*

## Modelo ng Perceptron

Ipagpalagay natin na mayroon tayong N na mga tampok sa ating modelo, kung saan ang input vector ay magiging isang vector ng laki N. Ang isang perceptron ay isang **binary classification** na modelo, ibig sabihin maaari itong makilala sa pagitan ng dalawang klase ng input na data. Ipagpalagay natin na para sa bawat input vector x ang output ng ating perceptron ay magiging alinman sa +1 o -1, depende sa klase. Ang output ay kakalkulahin gamit ang pormula:

y(x) = f(w<sup>T</sup>x)

kung saan ang f ay isang step activation function

## Pagsasanay sa Perceptron

Upang sanayin ang isang perceptron kailangan nating makahanap ng isang weights vector w na nag-uuri ng karamihan sa mga halaga nang tama, ibig sabihin nagreresulta sa pinakamaliit na **error**. Ang error na ito ay tinukoy ng **perceptron criterion** sa sumusunod na paraan:

E(w) = -∑w<sup>T</sup>x<sub>i</sub>t<sub>i</sub>

kung saan:

* ang kabuuan ay kinuha sa mga training data points i na nagreresulta sa maling klasipikasyon
* x<sub>i</sub> ay ang input data, at t<sub>i</sub> ay alinman sa -1 o +1 para sa mga negatibo at positibong halimbawa nang naaayon.

Ang pamantayang ito ay itinuturing bilang isang function ng weights w, at kailangan nating i-minimize ito. Madalas, isang paraan na tinatawag na **gradient descent** ang ginagamit, kung saan nagsisimula tayo sa ilang inisyal na weights w<sup>(0)</sup>, at pagkatapos sa bawat hakbang ay ina-update ang weights ayon sa pormula:

w<sup>(t+1)</sup> = w<sup>(t)</sup> - η∇E(w)

Dito ang η ay tinatawag na **learning rate**, at ang ∇E(w) ay nangangahulugang **gradient** ng E. Pagkatapos nating kalkulahin ang gradient, nagtatapos tayo sa

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

Sa araling ito, natutunan mo ang tungkol sa isang perceptron, na isang binary classification na modelo, at kung paano ito sanayin gamit ang isang weights vector.

## 🚀 Hamon

Kung gusto mong subukang bumuo ng iyong sariling perceptron, subukan ang lab na ito sa Microsoft Learn na gumagamit ng Azure ML designer

## Pagsusuri at Pag-aaral sa Sarili

Upang makita kung paano natin magagamit ang perceptron upang lutasin ang isang laruan na problema pati na rin ang mga totoong problema, at upang magpatuloy sa pag-aaral - pumunta sa Perceptron notebook.

Narito rin ang isang kawili-wiling artikulo tungkol sa mga perceptrons.

## Takdang Aralin

Sa araling ito, nagpatupad tayo ng isang perceptron para sa binary classification na gawain, at ginamit natin ito upang uriin sa pagitan ng dalawang manuskrito na numero. Sa lab na ito, ikaw ay hiniling na lutasin ang problema ng pagkilala sa numero nang buo, ibig sabihin tukuyin kung aling numero ang pinaka-malamang na tumutugma sa isang ibinigay na imahe.

* Mga Tagubilin
* Notebook

**Pagtatatuwa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.