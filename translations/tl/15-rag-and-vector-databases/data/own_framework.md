<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-05-20T02:24:28+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks. Multi-Layered Perceptron

Sa nakaraang seksyon, natutunan mo ang tungkol sa pinakasimpleng modelo ng neural network - ang one-layered perceptron, isang linear na modelo para sa dalawang-klaseng klasipikasyon.

Sa seksyong ito, palalawakin natin ang modelong ito sa mas flexible na balangkas, na magbibigay-daan sa atin na:

* magsagawa ng **multi-class classification** bukod sa dalawang-klase
* lutasin ang mga **regression problems** bukod sa klasipikasyon
* paghiwalayin ang mga klase na hindi linear na maihihiwalay

Bubuo rin tayo ng sarili nating modular na balangkas sa Python na magpapahintulot sa atin na bumuo ng iba't ibang neural network architectures.

## Pagpormalisa ng Machine Learning

Magsimula tayo sa pagpormalisa ng problema sa Machine Learning. Ipagpalagay natin na mayroon tayong training dataset **X** na may mga label na **Y**, at kailangan nating bumuo ng modelong *f* na magbibigay ng pinaka-tumpak na prediksyon. Ang kalidad ng mga prediksyon ay sinusukat ng **Loss function** ℒ. Ang sumusunod na mga loss function ay madalas na ginagamit:

* Para sa regression problem, kapag kailangan nating magpredikta ng numero, maaari nating gamitin ang **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para sa klasipikasyon, ginagamit natin ang **0-1 loss** (na karaniwang kapareho ng **accuracy** ng modelo), o **logistic loss**.

Para sa one-level perceptron, ang function na *f* ay tinukoy bilang isang linear function *f(x)=wx+b* (dito ang *w* ay ang weight matrix, *x* ay ang vector ng input features, at *b* ay bias vector). Para sa iba't ibang neural network architectures, ang function na ito ay maaaring kumuha ng mas kumplikadong anyo.

> Sa kaso ng klasipikasyon, madalas na kanais-nais na makuha ang mga probabilidad ng kaukulang mga klase bilang output ng network. Upang i-convert ang arbitrary numbers sa probabilidad (hal. upang i-normalize ang output), madalas nating ginagamit ang **softmax** function σ, at ang function na *f* ay nagiging *f(x)=σ(wx+b)*

Sa depinisyon ng *f* sa itaas, ang *w* at *b* ay tinatawag na **parameters** θ=⟨*w,b*⟩. Ibinigay ang dataset ⟨**X**,**Y**⟩, maaari nating kalkulahin ang kabuuang error sa buong dataset bilang isang function ng mga parameters θ.

> ✅ **Ang layunin ng pagsasanay sa neural network ay upang mabawasan ang error sa pamamagitan ng pagbabago ng mga parameters θ**

## Gradient Descent Optimization

May isang kilalang paraan ng pag-optimize ng function na tinatawag na **gradient descent**. Ang ideya ay maaari nating kalkulahin ang derivative (sa multi-dimensional na kaso ay tinatawag na **gradient**) ng loss function kaugnay ng mga parameters, at baguhin ang mga parameters sa paraang ang error ay bababa. Ito ay maaaring pormalisahin tulad ng sumusunod:

* I-initialize ang mga parameters sa pamamagitan ng ilang random na halaga w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulitin ang sumusunod na hakbang nang maraming beses:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Sa panahon ng pagsasanay, ang mga hakbang sa pag-optimize ay dapat kalkulahin na isinasaalang-alang ang buong dataset (tandaan na ang loss ay kinakalkula bilang kabuuan sa lahat ng training samples). Gayunpaman, sa totoong buhay ay kumukuha tayo ng maliliit na bahagi ng dataset na tinatawag na **minibatches**, at kinakalkula ang gradients batay sa subset ng data. Dahil ang subset ay kinukuha nang random sa bawat oras, ang ganitong paraan ay tinatawag na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons at Backpropagation

Ang one-layer network, tulad ng nakita natin sa itaas, ay may kakayahang magklasipika ng mga linear na maihihiwalay na klase. Upang bumuo ng mas mayamang modelo, maaari nating pagsamahin ang ilang mga layer ng network. Sa matematika, nangangahulugan ito na ang function na *f* ay magkakaroon ng mas kumplikadong anyo, at kakalkulahin sa ilang mga hakbang:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Dito, ang α ay isang **non-linear activation function**, ang σ ay isang softmax function, at ang mga parameters θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Ang gradient descent algorithm ay mananatiling pareho, ngunit magiging mas mahirap kalkulahin ang mga gradients. Ayon sa chain differentiation rule, maaari nating kalkulahin ang derivatives bilang:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ang chain differentiation rule ay ginagamit upang kalkulahin ang derivatives ng loss function kaugnay ng mga parameters.

Tandaan na ang kaliwang bahagi ng lahat ng mga expression na iyon ay pareho, at sa gayon maaari nating mabisang kalkulahin ang derivatives simula sa loss function at pumunta "pabalik" sa computational graph. Kaya't ang paraan ng pagsasanay sa isang multi-layered perceptron ay tinatawag na **backpropagation**, o 'backprop'.

> ✅ Tatalakayin natin ang backprop nang mas detalyado sa ating halimbawa sa notebook.

## Konklusyon

Sa araling ito, nakabuo tayo ng sarili nating neural network library, at ginamit natin ito para sa isang simpleng dalawang-dimensional na klasipikasyon na gawain.

## 🚀 Hamon

Sa kasamang notebook, ipapatupad mo ang sarili mong balangkas para sa pagbuo at pagsasanay ng multi-layered perceptrons. Makikita mo nang detalyado kung paano gumagana ang modernong neural networks.

Magpatuloy sa OwnFramework notebook at pag-aralan ito.

## Pagsusuri at Pag-aaral sa Sarili

Ang backpropagation ay isang karaniwang algorithm na ginagamit sa AI at ML, karapat-dapat pag-aralan nang mas detalyado.

## Takdang Aralin

Sa laboratoryo na ito, hinihiling kang gamitin ang balangkas na ginawa mo sa araling ito upang lutasin ang klasipikasyon ng MNIST handwritten digit.

* Mga Instruksyon
* Notebook

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga error o hindi pagkaka-ayon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.