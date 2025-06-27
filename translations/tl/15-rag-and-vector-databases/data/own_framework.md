<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "df98b2c59f87d8543135301e87969f70",
  "translation_date": "2025-06-25T23:28:38+00:00",
  "source_file": "15-rag-and-vector-databases/data/own_framework.md",
  "language_code": "tl"
}
-->
# Panimula sa Neural Networks. Multi-Layered Perceptron

Sa nakaraang seksyon, natutunan mo ang tungkol sa pinakasimpleng neural network model - isang layered perceptron, isang linear na modelo para sa dalawang klase na klasipikasyon.

Sa seksyong ito, palalawakin natin ang modelong ito sa isang mas flexible na framework, na magpapahintulot sa atin na:

* magsagawa ng **multi-class classification** bukod sa dalawang klase
* lutasin ang **mga problema sa regression** bukod sa klasipikasyon
* paghiwalayin ang mga klase na hindi linear na nahahati

Bubuo rin tayo ng sarili nating modular framework sa Python na magpapahintulot sa atin na bumuo ng iba't ibang neural network architectures.

## Pormalisasyon ng Machine Learning

Magsimula tayo sa pormalisasyon ng problema sa Machine Learning. Ipagpalagay na mayroon tayong training dataset **X** na may mga label na **Y**, at kailangan nating bumuo ng modelong *f* na gagawa ng pinakatumpak na prediksyon. Ang kalidad ng prediksyon ay sinusukat ng **Loss function** ℒ. Ang mga sumusunod na loss functions ay kadalasang ginagamit:

* Para sa regression problem, kapag kailangan nating magpredikta ng numero, maaari nating gamitin ang **absolute error** ∑<sub>i</sub>|f(x<sup>(i)</sup>)-y<sup>(i)</sup>|, o **squared error** ∑<sub>i</sub>(f(x<sup>(i)</sup>)-y<sup>(i)</sup>)<sup>2</sup>
* Para sa klasipikasyon, ginagamit natin ang **0-1 loss** (na karaniwang kapareho ng **accuracy** ng modelo), o **logistic loss**.

Para sa one-level perceptron, ang function *f* ay itinukoy bilang isang linear function *f(x)=wx+b* (dito ang *w* ay ang weight matrix, *x* ay ang vector ng input features, at *b* ay bias vector). Para sa iba't ibang neural network architectures, ang function na ito ay maaaring kumuha ng mas kumplikadong anyo.

> Sa kaso ng klasipikasyon, madalas na kanais-nais na makuha ang mga probabilidad ng mga kaukulang klase bilang output ng network. Upang i-convert ang arbitraryong mga numero sa probabilidad (hal. upang i-normalize ang output), madalas nating ginagamit ang **softmax** function σ, at ang function *f* ay nagiging *f(x)=σ(wx+b)*

Sa kahulugan ng *f* sa itaas, ang *w* at *b* ay tinatawag na **parameters** θ=⟨*w,b*⟩. Sa ibinigay na dataset ⟨**X**,**Y**⟩, maaari nating kalkulahin ang kabuuang error sa buong dataset bilang isang function ng mga parameter θ.

> ✅ **Ang layunin ng neural network training ay i-minimize ang error sa pamamagitan ng pagbabago ng mga parameter θ**

## Gradient Descent Optimization

Mayroong isang kilalang paraan ng pag-optimize ng function na tinatawag na **gradient descent**. Ang ideya ay maaari nating kalkulahin ang derivative (sa multi-dimensional na kaso ay tinatawag na **gradient**) ng loss function ukol sa mga parameter, at baguhin ang mga parameter sa paraang ang error ay bababa. Ito ay maaaring i-pormalisasyon sa sumusunod na paraan:

* I-initialize ang mga parameter sa ilang random na halaga w<sup>(0)</sup>, b<sup>(0)</sup>
* Ulitin ang sumusunod na hakbang ng maraming beses:
    - w<sup>(i+1)</sup> = w<sup>(i)</sup>-η∂ℒ/∂w
    - b<sup>(i+1)</sup> = b<sup>(i)</sup>-η∂ℒ/∂b

Sa panahon ng training, ang mga optimization steps ay inaasahang kalkulahin na isinasaalang-alang ang buong dataset (tandaan na ang loss ay kinakalkula bilang kabuuan sa lahat ng training samples). Gayunpaman, sa tunay na buhay ay kumukuha tayo ng maliliit na bahagi ng dataset na tinatawag na **minibatches**, at kinakalkula ang mga gradients batay sa subset ng data. Dahil ang subset ay kinukuha nang random sa bawat pagkakataon, ang ganitong paraan ay tinatawag na **stochastic gradient descent** (SGD).

## Multi-Layered Perceptrons at Backpropagation

Ang one-layer network, tulad ng nakita natin sa itaas, ay may kakayahang mag-klasipika ng mga klase na linear na nahahati. Upang bumuo ng mas mayamang modelo, maaari nating pagsamahin ang ilang mga layer ng network. Matematika, nangangahulugan ito na ang function *f* ay magkakaroon ng mas kumplikadong anyo, at mako-compute sa ilang hakbang:
* z<sub>1</sub>=w<sub>1</sub>x+b<sub>1</sub>
* z<sub>2</sub>=w<sub>2</sub>α(z<sub>1</sub>)+b<sub>2</sub>
* f = σ(z<sub>2</sub>)

Dito, ang α ay isang **non-linear activation function**, ang σ ay isang softmax function, at ang mga parameter θ=<*w<sub>1</sub>,b<sub>1</sub>,w<sub>2</sub>,b<sub>2</sub>*>.

Ang gradient descent algorithm ay mananatiling pareho, ngunit magiging mas mahirap ang pagkalkula ng mga gradients. Ayon sa chain differentiation rule, maaari nating kalkulahin ang mga derivatives bilang:

* ∂ℒ/∂w<sub>2</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂w<sub>2</sub>)
* ∂ℒ/∂w<sub>1</sub> = (∂ℒ/∂σ)(∂σ/∂z<sub>2</sub>)(∂z<sub>2</sub>/∂α)(∂α/∂z<sub>1</sub>)(∂z<sub>1</sub>/∂w<sub>1</sub>)

> ✅ Ang chain differentiation rule ay ginagamit upang kalkulahin ang mga derivatives ng loss function ukol sa mga parameter.

Pansinin na ang kaliwang bahagi ng lahat ng mga ekspresyon na iyon ay pareho, kaya't maaari nating mabisang kalkulahin ang mga derivatives simula sa loss function at magpatuloy "pabalik" sa computational graph. Kaya't ang paraan ng pag-training ng multi-layered perceptron ay tinatawag na **backpropagation**, o 'backprop'.

> TODO: pagbanggit ng larawan

> ✅ Tatalakayin natin ang backprop nang mas detalyado sa ating notebook na halimbawa.

## Konklusyon

Sa araling ito, bumuo tayo ng sarili nating neural network library, at ginamit natin ito para sa isang simpleng dalawang-dimensional na klasipikasyon na gawain.

## 🚀 Hamon

Sa kasamang notebook, ipapatupad mo ang sarili mong framework para sa pagbuo at pag-training ng multi-layered perceptrons. Makikita mo nang detalyado kung paano gumagana ang modernong neural networks.

Magpatuloy sa OwnFramework notebook at isagawa ito.

## Review at Pag-aaral sa Sarili

Ang backpropagation ay isang karaniwang algorithm na ginagamit sa AI at ML, na karapat-dapat pag-aralan nang mas detalyado.

## Takdang Aralin

Sa laboratoryong ito, hinihiling kang gamitin ang framework na binuo mo sa araling ito upang lutasin ang MNIST handwritten digit classification.

* Mga Instruksyon
* Notebook

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o kamalian. Ang orihinal na dokumento sa sariling wika nito ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.