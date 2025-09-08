<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-07-09T16:49:41+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks. Multi-Layered Perceptron

Sa nakaraang bahagi, natutunan mo ang pinakasimpleng modelo ng neural network - ang one-layered perceptron, isang linear na modelo para sa dalawang klase ng klasipikasyon.

Sa bahaging ito, palalawakin natin ang modelong ito sa isang mas flexible na balangkas, na magbibigay-daan sa atin upang:

* magsagawa ng **multi-class classification** bukod sa dalawang klase lamang
* lutasin ang mga **regression problems** bukod sa klasipikasyon
* paghiwalayin ang mga klase na hindi linear na mapaghihiwalay

Bubuuin din natin ang sarili nating modular na balangkas sa Python na magpapahintulot sa atin na makabuo ng iba't ibang arkitektura ng neural network.

## Pormalisasyon ng Machine Learning

Magsimula tayo sa pag-pormalisa ng problema sa Machine Learning. Ipagpalagay natin na mayroon tayong training dataset na **X** na may mga label na **Y**, at kailangan nating bumuo ng modelong *f* na makakapagbigay ng pinakatumpak na prediksyon. Ang kalidad ng mga prediksyon ay sinusukat gamit ang **Loss function** ℒ. Ang mga sumusunod na loss function ay madalas gamitin:

* Para sa regression problem, kung kailangang hulaan ang isang numero, maaari nating gamitin ang **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o ang **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para sa klasipikasyon, ginagamit natin ang **0-1 loss** (na halos kapareho ng **accuracy** ng modelo), o ang **logistic loss**.

Para sa one-level perceptron, ang function *f* ay tinukoy bilang isang linear na function *f(x)=wx+b* (kung saan ang *w* ay ang weight matrix, *x* ang vector ng input features, at *b* ang bias vector). Sa iba't ibang arkitektura ng neural network, maaaring maging mas kumplikado ang anyo ng function na ito.

> Sa kaso ng klasipikasyon, madalas na nais makuha ang mga probabilidad ng mga kaukulang klase bilang output ng network. Para i-convert ang mga arbitraryong numero sa mga probabilidad (halimbawa, para i-normalize ang output), madalas nating ginagamit ang **softmax** function σ, kaya ang function *f* ay nagiging *f(x)=σ(wx+b)*

Sa depinisyon ng *f* sa itaas, ang *w* at *b* ay tinatawag na **parameters** θ=⟨*w,b*⟩. Sa dataset na ⟨**X**,**Y**⟩, maaari nating kalkulahin ang kabuuang error sa buong dataset bilang isang function ng parameters θ.

> ✅ **Ang layunin ng pagsasanay ng neural network ay pababain ang error sa pamamagitan ng pagbabago ng parameters θ**

## Gradient Descent Optimization

May kilalang paraan ng pag-optimize ng function na tinatawag na **gradient descent**. Ang ideya ay maaari nating kalkulahin ang derivative (sa multi-dimensional na kaso ay tinatawag na **gradient**) ng loss function kaugnay ng parameters, at baguhin ang parameters sa paraang bumababa ang error. Maaari itong ipormalisa sa mga sumusunod na hakbang:

* I-initialize ang parameters gamit ang ilang random na halaga w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulitin ang sumusunod na hakbang nang maraming beses:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Sa panahon ng pagsasanay, ang mga hakbang ng optimization ay karaniwang kinakalkula gamit ang buong dataset (tandaan na ang loss ay kinukwenta bilang kabuuan sa lahat ng training samples). Ngunit sa totoong buhay, kumukuha tayo ng maliliit na bahagi ng dataset na tinatawag na **minibatches**, at kinakalkula ang gradients base sa subset ng data. Dahil ang subset ay random na pinipili sa bawat pagkakataon, ang paraang ito ay tinatawag na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons at Backpropagation

Ang one-layer network, tulad ng nakita natin sa itaas, ay kayang magklasipika ng mga klase na linearly separable. Para makabuo ng mas mayamang modelo, maaari nating pagsamahin ang ilang mga layer ng network. Sa matematika, nangangahulugan ito na ang function *f* ay magkakaroon ng mas kumplikadong anyo, at kakalkulahin sa ilang hakbang:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Dito, ang α ay isang **non-linear activation function**, ang σ ay softmax function, at ang parameters ay θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Mananatili ang algorithm ng gradient descent, ngunit magiging mas mahirap kalkulahin ang gradients. Gamit ang chain differentiation rule, maaari nating kalkulahin ang mga derivatives bilang:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ginagamit ang chain differentiation rule para kalkulahin ang mga derivatives ng loss function kaugnay ng parameters.

Pansinin na ang pinakakaliwang bahagi ng lahat ng mga ekspresyon na ito ay pareho, kaya epektibo nating makakalkula ang mga derivatives simula sa loss function at paurong na dumadaan sa computational graph. Kaya ang paraan ng pagsasanay ng multi-layered perceptron ay tinatawag na **backpropagation**, o 'backprop'.



> TODO: image citation

> ✅ Tatalakayin natin nang mas detalyado ang backprop sa ating notebook na halimbawa.

## Konklusyon

Sa araling ito, nakabuo tayo ng sarili nating neural network library, at ginamit natin ito para sa isang simpleng two-dimensional na klasipikasyon.

## 🚀 Hamon

Sa kalakip na notebook, ipatutupad mo ang sarili mong framework para sa pagbuo at pagsasanay ng multi-layered perceptrons. Makikita mo nang detalyado kung paano gumagana ang mga modernong neural networks.

Magpatuloy sa OwnFramework notebook at pag-aralan ito.

## Review at Sariling Pag-aaral

Ang backpropagation ay isang karaniwang algorithm na ginagamit sa AI at ML, na sulit pag-aralan nang mas malalim.

## Takdang-Aralin

Sa lab na ito, hihilingin sa iyo na gamitin ang framework na binuo mo sa araling ito upang lutasin ang MNIST handwritten digit classification.

* Mga Tagubilin
* Notebook

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.