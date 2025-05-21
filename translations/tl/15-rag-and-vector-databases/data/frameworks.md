<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b5466bcedc3c75aa35476270362f626a",
  "translation_date": "2025-05-20T02:04:29+00:00",
  "source_file": "15-rag-and-vector-databases/data/frameworks.md",
  "language_code": "tl"
}
-->
# Mga Framework ng Neural Network

Tulad ng ating natutunan, para makapagsanay ng neural networks nang epektibo, kailangan nating gawin ang dalawang bagay:

* Mag-operate sa tensors, halimbawa, mag-multiply, mag-add, at mag-compute ng ilang mga function tulad ng sigmoid o softmax
* Mag-compute ng gradients ng lahat ng expressions, upang maisagawa ang gradient descent optimization

Habang ang `numpy` na library ay maaaring gawin ang unang bahagi, kailangan natin ng mekanismo para mag-compute ng gradients. Sa ating framework na ating dinevelop sa nakaraang seksyon, kailangan nating i-programa nang mano-mano ang lahat ng derivative functions sa loob ng `backward` na method, na gumagawa ng backpropagation. Ideal na ang isang framework ay dapat magbigay sa atin ng kakayahang mag-compute ng gradients ng *anumang expression* na maari nating idefine.

Isa pang mahalagang bagay ay ang kakayahang magpatupad ng computations sa GPU, o anumang iba pang espesyal na compute units, tulad ng TPU. Ang deep neural network training ay nangangailangan ng *napakaraming* computations, at ang kakayahang i-parallelize ang mga computations na ito sa GPUs ay napakahalaga.

> ✅ Ang terminong 'parallelize' ay nangangahulugang ipamahagi ang computations sa maraming devices.

Sa kasalukuyan, ang dalawang pinakasikat na neural frameworks ay: TensorFlow at PyTorch. Pareho silang nagbibigay ng low-level API upang mag-operate gamit ang tensors sa parehong CPU at GPU. Sa ibabaw ng low-level API, mayroon ding higher-level API, na tinatawag na Keras at PyTorch Lightning ayon sa pagkakabanggit.

Low-Level API | TensorFlow| PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras| Pytorch

**Low-level APIs** sa parehong frameworks ay nagpapahintulot sa iyo na bumuo ng tinatawag na **computational graphs**. Ang graph na ito ay nagde-define kung paano i-compute ang output (karaniwan ay ang loss function) gamit ang mga input parameters, at maaaring i-push para sa computation sa GPU, kung ito ay available. May mga function para i-differentiate ang computational graph na ito at mag-compute ng gradients, na maaaring gamitin para i-optimize ang mga model parameters.

**High-level APIs** ay halos itinuturing ang neural networks bilang isang **sequence ng layers**, at ginagawa nitong mas madali ang pagbuo ng karamihan sa mga neural networks. Ang pagsasanay sa model ay karaniwang nangangailangan ng paghahanda ng data at pagkatapos ay pagtawag sa isang `fit` na function upang gawin ang trabaho.

Ang high-level API ay nagpapahintulot sa iyo na bumuo ng karaniwang neural networks nang mabilis nang hindi kinakailangang mag-alala sa maraming detalye. Kasabay nito, ang low-level API ay nag-aalok ng mas maraming kontrol sa proseso ng pagsasanay, at sa gayon ay madalas na ginagamit sa pananaliksik, kapag nakikitungo ka sa mga bagong neural network architectures.

Mahalaga ring maunawaan na maaari mong gamitin ang parehong APIs nang magkasama, halimbawa, maaari kang bumuo ng sarili mong network layer architecture gamit ang low-level API, at pagkatapos ay gamitin ito sa loob ng mas malaking network na binuo at sinanay gamit ang high-level API. O maaari kang magdeklara ng network gamit ang high-level API bilang isang sequence ng layers, at pagkatapos ay gamitin ang sarili mong low-level training loop upang magsagawa ng optimization. Parehong APIs ay gumagamit ng parehong pangunahing mga konsepto, at sila ay dinisenyo upang magtrabaho nang maayos na magkasama.

## Pag-aaral

Sa kursong ito, nag-aalok kami ng karamihan ng nilalaman para sa parehong PyTorch at TensorFlow. Maaari mong piliin ang iyong nais na framework at dumaan lamang sa mga kaukulang notebooks. Kung hindi ka sigurado kung aling framework ang pipiliin, basahin ang ilang mga talakayan sa internet tungkol sa **PyTorch vs. TensorFlow**. Maaari mo ring tingnan ang parehong frameworks upang makakuha ng mas mahusay na pag-unawa.

Kung maaari, gagamitin namin ang High-Level APIs para sa kasimplihan. Gayunpaman, naniniwala kami na mahalaga ang maunawaan kung paano gumagana ang neural networks mula sa simula, kaya't sa simula ay magsisimula kami sa pagtatrabaho gamit ang low-level API at tensors. Gayunpaman, kung nais mong magsimula agad at ayaw mong maglaan ng maraming oras sa pag-aaral ng mga detalyeng ito, maaari mong laktawan ang mga iyon at dumiretso sa high-level API notebooks.

## ✍️ Mga Pagsasanay: Mga Framework

Ipagpatuloy ang iyong pag-aaral sa mga sumusunod na notebooks:

Low-Level API | TensorFlow+Keras Notebook | PyTorch
--------------|-------------------------------------|--------------------------------
High-level API| Keras | *PyTorch Lightning*

Matapos masanay ang mga frameworks, balikan natin ang konsepto ng overfitting.

# Overfitting

Ang overfitting ay isang napakahalagang konsepto sa machine learning, at napakahalaga na ito ay tama!

Isaalang-alang ang sumusunod na problema ng pag-aapproximate ng 5 dots (kinakatawan ng `x` sa mga graph sa ibaba):

!linear | overfit
-------------------------|--------------------------
**Linear model, 2 parameters** | **Non-linear model, 7 parameters**
Training error = 5.3 | Training error = 0
Validation error = 5.1 | Validation error = 20

* Sa kaliwa, makikita natin ang isang magandang tuwid na linya ng approximation. Dahil ang bilang ng mga parameters ay sapat, nakuha ng model ang ideya sa likod ng point distribution nang tama.
* Sa kanan, ang model ay masyadong makapangyarihan. Dahil mayroon lamang tayong 5 puntos at ang model ay may 7 parameters, maaari itong mag-adjust sa paraang dumaan sa lahat ng puntos, na nagiging sanhi ng training error na maging 0. Gayunpaman, pinipigilan nito ang model na maunawaan ang tamang pattern sa likod ng data, kaya't ang validation error ay napakataas.

Napakahalaga na makuha ang tamang balanse sa pagitan ng richness ng model (bilang ng parameters) at bilang ng mga training samples.

## Bakit nagaganap ang overfitting

  * Hindi sapat ang training data
  * Masyadong makapangyarihang model
  * Masyadong maraming ingay sa input data

## Paano matukoy ang overfitting

Tulad ng makikita mo mula sa graph sa itaas, ang overfitting ay maaaring matukoy sa pamamagitan ng napakababang training error, at mataas na validation error. Karaniwan sa panahon ng pagsasanay makikita natin ang parehong training at validation errors na nagsisimulang bumaba, at pagkatapos sa isang punto ang validation error ay maaaring huminto sa pagbaba at magsimulang tumaas. Ito ay magiging isang senyales ng overfitting, at ang indikasyon na dapat nating itigil ang pagsasanay sa puntong ito (o kahit man lang gumawa ng snapshot ng model).

## Paano maiwasan ang overfitting

Kung nakikita mo na nagaganap ang overfitting, maaari mong gawin ang isa sa mga sumusunod:

 * Dagdagan ang dami ng training data
 * Bawasan ang pagiging kumplikado ng model
 * Gumamit ng ilang regularization technique, tulad ng Dropout, na ating tatalakayin sa susunod.

## Overfitting at Bias-Variance Tradeoff

Ang overfitting ay talagang isang kaso ng mas generic na problema sa statistics na tinatawag na Bias-Variance Tradeoff. Kung isasaalang-alang natin ang mga posibleng pinagmumulan ng error sa ating model, makikita natin ang dalawang uri ng errors:

* **Bias errors** ay sanhi ng ating algorithm na hindi makuha ang relasyon sa pagitan ng training data nang tama. Maaari itong magresulta mula sa katotohanang ang ating model ay hindi sapat na makapangyarihan (**underfitting**).
* **Variance errors**, na sanhi ng model na nag-aapproximate ng ingay sa input data sa halip na makabuluhang relasyon (**overfitting**).

Sa panahon ng pagsasanay, ang bias error ay bumababa (habang natututo ang ating model na iapproximate ang data), at ang variance error ay tumataas. Mahalaga na itigil ang pagsasanay - alinman sa mano-mano (kapag natukoy natin ang overfitting) o awtomatiko (sa pamamagitan ng pagpapakilala ng regularization) - upang maiwasan ang overfitting.

## Konklusyon

Sa araling ito, natutunan mo ang mga pagkakaiba sa pagitan ng iba't ibang APIs para sa dalawang pinakasikat na AI frameworks, TensorFlow at PyTorch. Bukod dito, natutunan mo ang tungkol sa isang napakahalagang paksa, ang overfitting.

## 🚀 Hamon

Sa mga kalakip na notebooks, makikita mo ang mga 'tasks' sa ibaba; dumaan sa mga notebooks at kumpletuhin ang mga tasks.

## Pagsusuri at Pag-aaral sa Sarili

Gumawa ng ilang pananaliksik sa mga sumusunod na paksa:

- TensorFlow
- PyTorch
- Overfitting

Tanungin ang iyong sarili ng mga sumusunod na katanungan:

- Ano ang pagkakaiba ng TensorFlow at PyTorch?
- Ano ang pagkakaiba ng overfitting at underfitting?

## Takdang-Aralin

Sa laboratoryong ito, hinihiling kang lutasin ang dalawang problema sa pag-uuri gamit ang single- at multi-layered fully-connected networks gamit ang PyTorch o TensorFlow.

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat pinagsisikapan naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagiging tumpak. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang mapagkukunan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.