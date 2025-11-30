<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-07-09T16:35:21+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tl"
}
-->
# Neural Network Frameworks

Tulad ng natutunan na natin, para maging epektibo ang pagsasanay ng neural networks, kailangan nating gawin ang dalawang bagay:

* Mag-operate sa tensors, halimbawa, mag-multiply, mag-add, at mag-compute ng ilang functions tulad ng sigmoid o softmax
* Mag-compute ng gradients ng lahat ng expressions, para magawa ang gradient descent optimization

Habang kaya ng `numpy` library ang unang bahagi, kailangan natin ng mekanismo para mag-compute ng gradients. Sa framework na ginawa natin sa nakaraang bahagi, kailangang mano-manong i-program ang lahat ng derivative functions sa loob ng `backward` method, na siyang gumagawa ng backpropagation. Sa ideal, dapat bigyan tayo ng framework ng pagkakataon na makapag-compute ng gradients ng *anumang expression* na kaya nating idefine.

Isa pang mahalagang bagay ay ang kakayahang magpatakbo ng computations sa GPU, o sa iba pang specialized compute units tulad ng TPU. Ang pagsasanay ng malalalim na neural networks ay nangangailangan ng *maraming* computations, kaya napakahalaga na maiparallelize ang mga computations na ito sa GPUs.

> ✅ Ang ibig sabihin ng 'parallelize' ay ang paghati-hati ng computations sa maraming devices.

Sa kasalukuyan, ang dalawang pinakasikat na neural frameworks ay: TensorFlow at PyTorch. Pareho silang nagbibigay ng low-level API para mag-operate sa tensors sa parehong CPU at GPU. Bukod sa low-level API, mayroon ding high-level API, na tinatawag na Keras at PyTorch Lightning, ayon sa pagkakasunod.

Low-Level API | TensorFlow | PyTorch  
--------------|-------------|---------  
High-level API| Keras       | PyTorch

**Ang Low-level APIs** sa parehong frameworks ay nagpapahintulot sa iyo na bumuo ng tinatawag na **computational graphs**. Ang graph na ito ang nagdedetalye kung paano makukuha ang output (karaniwan ay loss function) gamit ang mga input parameters, at maaaring ipasa para sa computation sa GPU kung available ito. May mga functions para i-differentiate ang computational graph na ito at mag-compute ng gradients, na magagamit para i-optimize ang mga model parameters.

**Ang High-level APIs** ay tinitingnan ang neural networks bilang isang **sunod-sunod na mga layers**, at pinapadali ang pagbuo ng karamihan sa mga neural networks. Karaniwan, ang pagsasanay ng modelo ay nangangailangan ng paghahanda ng data at pagkatapos ay pagtawag sa `fit` function para gawin ang trabaho.

Pinapahintulutan ka ng high-level API na mabilis makabuo ng mga karaniwang neural networks nang hindi iniintindi ang maraming detalye. Sa kabilang banda, ang low-level API ay nagbibigay ng mas malawak na kontrol sa proseso ng pagsasanay, kaya madalas itong ginagamit sa pananaliksik, lalo na kapag gumagawa ng mga bagong neural network architectures.

Mahalaga ring maintindihan na maaari mong gamitin ang parehong APIs nang sabay, halimbawa, maaari kang gumawa ng sarili mong network layer architecture gamit ang low-level API, at gamitin ito sa loob ng mas malaking network na binuo at sinanay gamit ang high-level API. O kaya naman, maaari kang mag-define ng network gamit ang high-level API bilang sunod-sunod na layers, at gamitin ang sarili mong low-level training loop para sa optimization. Parehong gumagamit ang dalawang API ng parehong mga pangunahing konsepto, at dinisenyo silang magtrabaho nang maayos nang magkasama.

## Learning

Sa kursong ito, inaalok namin ang karamihan ng nilalaman para sa parehong PyTorch at TensorFlow. Maaari mong piliin ang framework na gusto mo at sundan lamang ang mga kaukulang notebooks. Kung hindi ka sigurado kung alin ang pipiliin, basahin ang ilang mga diskusyon sa internet tungkol sa **PyTorch vs. TensorFlow**. Maaari mo ring tingnan ang parehong frameworks para mas maintindihan.

Kung maaari, gagamitin namin ang High-Level APIs para sa pagiging simple. Gayunpaman, naniniwala kami na mahalagang maintindihan kung paano gumagana ang neural networks mula sa pinaka-ugat, kaya sa simula ay magsisimula tayo sa low-level API at tensors. Ngunit kung gusto mong mabilis makapagsimula at ayaw mong maglaan ng maraming oras sa pag-aaral ng mga detalye, maaari mong laktawan ito at pumunta diretso sa high-level API notebooks.

## ✍️ Exercises: Frameworks

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch  
--------------|----------------------------|---------  
High-level API| Keras                      | *PyTorch Lightning*

Pagkatapos mong ma-master ang frameworks, balikan natin ang konsepto ng overfitting.

# Overfitting

Ang overfitting ay isang napakahalagang konsepto sa machine learning, at napakahalaga na maintindihan ito nang tama!

Isaalang-alang ang sumusunod na problema ng pag-approximate ng 5 puntos (na kinakatawan ng `x` sa mga graph sa ibaba):

!linear | overfit  
-------------------------|--------------------------  
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**  
Training error = 5.3 | Training error = 0  
Validation error = 5.1 | Validation error = 20

* Sa kaliwa, makikita natin ang magandang tuwid na linya ng approximation. Dahil ang bilang ng parameters ay sapat, naintindihan ng modelo ang pattern ng distribusyon ng mga puntos nang tama.
* Sa kanan, masyadong malakas ang modelo. Dahil mayroon lamang tayong 5 puntos at may 7 parameters ang modelo, kaya nitong i-adjust ang sarili para dumaan sa lahat ng puntos, kaya ang training error ay naging 0. Ngunit, pinipigilan nito ang modelo na maintindihan ang tamang pattern sa likod ng data, kaya mataas ang validation error.

Napakahalaga na magkaroon ng tamang balanse sa pagitan ng pagiging kumplikado ng modelo (bilang ng parameters) at dami ng training samples.

## Bakit nangyayari ang overfitting

  * Kulang sa training data
  * Masyadong malakas na modelo
  * Masyadong maraming ingay sa input data

## Paano matukoy ang overfitting

Tulad ng makikita sa graph sa itaas, ang overfitting ay matutukoy sa pamamagitan ng napakababang training error, at mataas na validation error. Karaniwan sa pagsasanay, makikita natin na parehong bumababa ang training at validation errors, ngunit sa isang punto, maaaring huminto ang pagbaba ng validation error at magsimulang tumaas. Ito ay senyales ng overfitting, at palatandaan na marahil ay dapat nang itigil ang pagsasanay sa puntong iyon (o kahit gumawa ng snapshot ng modelo).

overfitting

## Paano maiwasan ang overfitting

Kung mapapansin mong nangyayari ang overfitting, maaari mong gawin ang isa sa mga sumusunod:

 * Dagdagan ang dami ng training data
 * Bawasan ang pagiging kumplikado ng modelo
 * Gumamit ng regularization technique, tulad ng Dropout, na tatalakayin natin sa susunod.

## Overfitting at Bias-Variance Tradeoff

Ang overfitting ay isang kaso ng mas pangkalahatang problema sa statistics na tinatawag na Bias-Variance Tradeoff. Kung titingnan natin ang mga posibleng pinagmumulan ng error sa ating modelo, makikita natin ang dalawang uri ng error:

* **Bias errors** ay sanhi ng algorithm na hindi kayang maayos na hulihin ang relasyon sa pagitan ng training data. Maaaring ito ay dahil hindi sapat ang lakas ng modelo (**underfitting**).
* **Variance errors** ay sanhi ng modelo na ina-approximate ang ingay sa input data sa halip na ang makabuluhang relasyon (**overfitting**).

Sa pagsasanay, bumababa ang bias error (habang natututo ang modelo na i-approximate ang data), at tumataas ang variance error. Mahalaga na itigil ang pagsasanay - mano-mano (kapag na-detect ang overfitting) o awtomatiko (sa pamamagitan ng regularization) - upang maiwasan ang overfitting.

## Konklusyon

Sa araling ito, natutunan mo ang pagkakaiba ng iba't ibang APIs para sa dalawang pinakasikat na AI frameworks, TensorFlow at PyTorch. Bukod dito, natutunan mo rin ang isang napakahalagang paksa, ang overfitting.

## 🚀 Challenge

Sa mga kasamang notebooks, makikita mo ang mga 'tasks' sa ibaba; pag-aralan ang mga notebooks at tapusin ang mga tasks.

## Review & Self Study

Magsaliksik tungkol sa mga sumusunod na paksa:

- TensorFlow  
- PyTorch  
- Overfitting

Tanungin ang sarili ng mga sumusunod na tanong:

- Ano ang pagkakaiba ng TensorFlow at PyTorch?  
- Ano ang pagkakaiba ng overfitting at underfitting?

## Assignment

Sa lab na ito, hihilingin kang lutasin ang dalawang classification problems gamit ang single- at multi-layered fully-connected networks gamit ang PyTorch o TensorFlow.

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.