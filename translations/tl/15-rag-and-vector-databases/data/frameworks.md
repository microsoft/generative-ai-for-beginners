<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-06-25T23:08:06+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tl"
}
-->
# Neural Network Frameworks

Tulad ng natutunan na natin, upang masanay ang neural networks nang epektibo kailangan nating gawin ang dalawang bagay:

* Mag-operate sa tensors, halimbawa, mag-multiply, mag-add, at mag-compute ng ilang mga function tulad ng sigmoid o softmax
* Mag-compute ng gradients ng lahat ng expressions, upang maisagawa ang gradient descent optimization

Habang ang library ng `numpy` ay magagawa ang unang bahagi, kailangan natin ng mekanismo upang mag-compute ng gradients. Sa ating framework na nadevelop sa nakaraang seksyon, kinailangan nating manu-manong i-program ang lahat ng derivative functions sa loob ng `backward` method, na gumagawa ng backpropagation. Ideal na ang isang framework ay dapat magbigay sa atin ng oportunidad na mag-compute ng gradients ng *anumang expression* na maaari nating i-define.

Isa pang mahalagang bagay ay ang kakayahang magsagawa ng computations sa GPU, o anumang iba pang specialized compute units, tulad ng TPU. Ang pag-train ng deep neural network ay nangangailangan ng *maraming* computations, at ang kakayahang i-parallelize ang mga computations sa GPUs ay napakahalaga.

> ✅ Ang terminong 'parallelize' ay nangangahulugang ipamahagi ang computations sa maraming device.

Sa kasalukuyan, ang dalawang pinakasikat na neural frameworks ay: TensorFlow at PyTorch. Parehong nag-aalok ng low-level API upang mag-operate gamit ang tensors sa parehong CPU at GPU. Sa ibabaw ng low-level API, mayroon ding higher-level API, na tinatawag na Keras at PyTorch Lightning.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Low-level APIs** sa parehong frameworks ay nagpapahintulot sa iyo na bumuo ng tinatawag na **computational graphs**. Ang graph na ito ay nagde-define kung paano i-compute ang output (karaniwan ay ang loss function) gamit ang ibinigay na input parameters, at maaaring ipasa para sa computation sa GPU, kung available ito. Mayroong mga function upang i-differentiate ang computational graph na ito at mag-compute ng gradients, na maaaring gamitin para sa pag-optimize ng model parameters.

**High-level APIs** ay halos itinuturing ang neural networks bilang isang **sequence ng layers**, at ginagawa nitong mas madali ang pagbuo ng karamihan sa mga neural networks. Ang pag-train ng model ay karaniwang nangangailangan ng paghahanda ng data at pagkatapos ay pagtawag sa isang `fit` function upang gawin ang trabaho.

Ang high-level API ay nagbibigay-daan sa iyo na bumuo ng karaniwang neural networks nang mabilis nang hindi nababahala sa maraming detalye. Kasabay nito, ang low-level API ay nag-aalok ng mas maraming kontrol sa proseso ng pag-train, at sa gayon ay madalas na ginagamit sa pananaliksik, kapag ikaw ay nakikitungo sa mga bagong neural network architectures.

Mahalaga rin na maunawaan na maaari mong gamitin ang parehong APIs nang magkasama, halimbawa, maaari kang bumuo ng sarili mong network layer architecture gamit ang low-level API, at pagkatapos ay gamitin ito sa loob ng mas malaking network na binuo at na-train gamit ang high-level API. O maaari kang mag-define ng network gamit ang high-level API bilang isang sequence ng layers, at pagkatapos ay gamitin ang sarili mong low-level training loop upang magsagawa ng optimization. Parehong APIs ay gumagamit ng parehong pangunahing underlying concepts, at sila ay dinisenyo upang magtrabaho nang maayos nang magkasama.

## Learning

Sa kursong ito, nag-aalok kami ng karamihan ng nilalaman para sa PyTorch at TensorFlow. Maaari mong piliin ang iyong nais na framework at dumaan lamang sa kaukulang notebooks. Kung hindi ka sigurado kung aling framework ang pipiliin, basahin ang ilang talakayan sa internet tungkol sa **PyTorch vs. TensorFlow**. Maaari mo ring tingnan ang parehong frameworks upang magkaroon ng mas mahusay na pag-unawa.

Kung maaari, gagamitin namin ang High-Level APIs para sa pagiging simple. Gayunpaman, naniniwala kami na mahalaga na maunawaan kung paano gumagana ang neural networks mula sa simula, kaya sa simula ay nagsisimula kami sa pag-trabaho gamit ang low-level API at tensors. Gayunpaman, kung nais mong magsimula nang mabilis at hindi nais na gumugol ng maraming oras sa pag-aaral ng mga detalyeng ito, maaari mong laktawan ang mga ito at dumiretso sa high-level API notebooks.

## ✍️ Exercises: Frameworks

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Pagkatapos mag-master ng frameworks, balikan natin ang konsepto ng overfitting.

# Overfitting

Ang overfitting ay isang napakahalagang konsepto sa machine learning, at napakahalaga na makuha ito nang tama!

Isaalang-alang ang sumusunod na problema ng pag-aaproksima sa 5 tuldok (kinakatawan ng `x` sa mga graph sa ibaba):

!linear | overfit
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* Sa kaliwa, makikita natin ang isang mahusay na tuwid na linya na aproksimasyon. Dahil ang bilang ng mga parameters ay sapat, nakuha ng model ang ideya sa likod ng distribusyon ng tuldok.
* Sa kanan, masyadong makapangyarihan ang model. Dahil mayroon lamang tayong 5 puntos at ang model ay may 7 parameters, maaari itong mag-adjust sa paraang dumaan sa lahat ng puntos, na nagiging sanhi ng error sa training na maging 0. Gayunpaman, pinipigilan nito ang model sa pag-unawa sa tamang pattern sa likod ng data, kaya't napakataas ang validation error.

Napakahalaga na makuha ang tamang balanse sa pagitan ng richness ng model (bilang ng parameters) at bilang ng training samples.

## Bakit nagaganap ang overfitting

  * Hindi sapat ang training data
  * Masyadong makapangyarihan ang model
  * Masyadong maraming ingay sa input data

## Paano matukoy ang overfitting

Tulad ng makikita mo mula sa graph sa itaas, ang overfitting ay maaaring matukoy sa pamamagitan ng napakababang training error, at mataas na validation error. Karaniwang sa panahon ng training makikita natin ang parehong training at validation errors na nagsisimulang bumaba, at pagkatapos ay sa isang punto maaaring tumigil ang validation error sa pagbaba at magsimulang tumaas. Ito ay magiging senyales ng overfitting, at indikasyon na marahil dapat nating ihinto ang training sa puntong ito (o kahit papaano gumawa ng snapshot ng model).

overfitting

## Paano maiwasan ang overfitting

Kung nakikita mo na nagaganap ang overfitting, maaari mong gawin ang isa sa mga sumusunod:

 * Dagdagan ang dami ng training data
 * Bawasan ang pagiging kumplikado ng model
 * Gumamit ng ilang regularization technique, tulad ng Dropout, na isasaalang-alang natin mamaya.

## Overfitting at Bias-Variance Tradeoff

Ang overfitting ay talagang isang kaso ng mas generic na problema sa statistics na tinatawag na Bias-Variance Tradeoff. Kung isasaalang-alang natin ang posibleng mga pinagmumulan ng error sa ating model, makikita natin ang dalawang uri ng errors:

* **Bias errors** ay sanhi ng ating algorithm na hindi kayang makuha ang relasyon sa pagitan ng training data nang tama. Maaari itong magresulta mula sa katotohanan na ang ating model ay hindi sapat na makapangyarihan (**underfitting**).
* **Variance errors**, na sanhi ng model na inaaproksima ang ingay sa input data sa halip na makabuluhang relasyon (**overfitting**).

Sa panahon ng training, ang bias error ay bumababa (habang natututo ang ating model na aproksimahin ang data), at ang variance error ay tumataas. Mahalagang ihinto ang training - alinman sa manu-manong (kapag natukoy natin ang overfitting) o awtomatiko (sa pamamagitan ng pagpapakilala ng regularization) - upang maiwasan ang overfitting.

## Konklusyon

Sa leksyon na ito, natutunan mo ang tungkol sa mga pagkakaiba sa pagitan ng iba't ibang APIs para sa dalawang pinakasikat na AI frameworks, TensorFlow at PyTorch. Bukod dito, natutunan mo ang tungkol sa isang napakahalagang paksa, ang overfitting.

## 🚀 Hamon

Sa mga kasamang notebooks, makikita mo ang 'tasks' sa ibaba; dumaan sa mga notebooks at kumpletuhin ang mga tasks.

## Review & Self Study

Gumawa ng ilang pananaliksik sa mga sumusunod na paksa:

- TensorFlow
- PyTorch
- Overfitting

Tanungin ang iyong sarili ng mga sumusunod na katanungan:

- Ano ang pagkakaiba sa pagitan ng TensorFlow at PyTorch?
- Ano ang pagkakaiba sa pagitan ng overfitting at underfitting?

## Assignment

Sa lab na ito, hinihiling sa iyo na lutasin ang dalawang classification problems gamit ang single- at multi-layered fully-connected networks gamit ang PyTorch o TensorFlow.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI na serbisyo ng pagsasalin [Co-op Translator](https://github.com/Azure/co-op-translator). Habang nagsusumikap kami para sa katumpakan, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ay dapat ituring na mapagkakatiwalaang pinagmulan. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na nagmumula sa paggamit ng pagsasaling ito.