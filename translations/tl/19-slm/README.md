# Panimula sa Maliit na Modelo ng Wika para sa Generative AI para sa mga Nagsisimula
Ang Generative AI ay isang kahanga-hangang larangan ng artipisyal na intelihensiya na nakatuon sa paglikha ng mga sistema na may kakayahang lumikha ng bagong nilalaman. Ang nilalamang ito ay maaaring mula sa teksto at larawan hanggang sa musika at maging buong virtual na mga kapaligiran. Isa sa pinaka kapana-panabik na aplikasyon ng generative AI ay nasa larangan ng mga modelong pangwika.

## Ano ang Maliit na Mga Modelo ng Wika?

Ang Maliit na Modelo ng Wika (SLM) ay kumakatawan sa isang pinaikling bersyon ng malaking modelo ng wika (LLM), gamit ang maraming mga prinsipyo at teknolohiya ng LLM, habang nagpapakita ng malakiang pagbawas sa pangangailangang computational. 

Ang mga SLM ay isang bahagi ng mga modelo ng wika na idinisenyo upang makagawa ng teksto na kahalintulad ng tao. Hindi tulad ng kanilang mas malalaking katapat, tulad ng GPT-4, ang mga SLM ay mas compact at mahusay, kaya angkop sila para sa mga aplikasyon kung saan limitado ang mga computational na yaman. Sa kabila ng kanilang mas maliit na sukat, kaya pa rin nilang magsagawa ng iba't ibang gawain. Karaniwan, ang mga SLM ay binubuo sa pamamagitan ng pag-compress o pag-distila ng mga LLM, na naglalayong panatilihin ang malaking bahagi ng orihinal na kakayahan at lingguwistikong mga katangian ng modelo. Ang pagbawas na ito sa laki ng modelo ay nagpapababa sa kabuuang komplikasyon, na ginagawang mas mahusay ang mga SLM sa paggamit ng memorya at mga kinakailangang computational. Sa kabila ng mga optimisasyong ito, kaya pa rin ng mga SLM na magsagawa ng malawak na uri ng mga gawain sa natural na pagproseso ng wika (NLP):

- Pagbuo ng Teksto: Paglikha ng magkakaugnay at kontekstwalyang angkop na mga pangungusap o talata.
- Kumpletong Teksto: Paghula at pag-kompleto ng mga pangungusap batay sa ibinigay na prompt.
- Pagsasalin: Paglilipat ng teksto mula sa isang wika patungo sa iba.
- Pagbubuod: Pagpapaikli ng mahahabang piraso ng teksto sa mas maiikling buod na madaling maintindihan.

Bagaman may kaunting pagbabawas sa pagganap o lalim ng pag-unawa kumpara sa kanilang mas malalaking katapat. 

## Paano Gumagana ang Maliit na mga Modelo ng Wika?
Ang mga SLM ay sinasanay gamit ang napakalaking dami ng datos ng teksto. Sa panahon ng pagsasanay, natututuhan nila ang mga pattern at istruktura ng wika, na nagbibigay-daan sa kanila upang makabuo ng teksto na parehong gramatikal na tama at kontekstwalyang angkop. Ang proseso ng pagsasanay ay kinabibilangan ng:

- Pangangalap ng Datos: Pagtipon ng malalaking dataset ng teksto mula sa iba't ibang mga pinanggalingan.
- Preprocessing: Paglilinis at pag-oorganisa ng datos upang maging angkop para sa pagsasanay.
- Pagsasanay: Paggamit ng mga algorithm ng machine learning upang turuan ang modelo kung paano maunawaan at makabuo ng teksto.
- Fine-Tuning: Pag-aayos ng modelo upang mapabuti ang pagganap nito sa mga partikular na gawain.

Ang pag-develop ng SLM ay naaayon sa tumataas na pangangailangan para sa mga modelong maaaring i-deploy sa mga kapaligirang may limitadong yaman, tulad ng mga mobile device o mga plataporma ng edge computing, kung saan maaaring hindi praktikal ang buong saklaw na mga LLM dahil sa mabibigat nitong pangangailangan sa yaman. Sa pamamagitan ng pagtutok sa kahusayan, binabalanse ng mga SLM ang pagganap at accessibility, na nagpapahintulot sa mas malawak na aplikasyon sa iba't ibang larangan.

![slm](../../../translated_images/tl/slm.4058842744d0444a.webp)

## Mga Layunin sa Pagkatuto

Sa araling ito, nais naming ipakilala ang kaalaman tungkol sa SLM at pagsamahin ito sa Microsoft Phi-3 upang matutunan ang iba't ibang mga senaryo sa nilalaman ng teksto, pananaw, at MoE.

Sa pagtatapos ng araling ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang SLM?
- Ano ang pagkakaiba ng SLM at LLM?
- Ano ang Microsoft Phi-3/3.5 Family?
- Paano magpatakbo ng inference gamit ang Microsoft Phi-3/3.5 Family?

Handa ka na ba? Magsimula tayo.

## Ang Pagkakaiba sa pagitan ng Malaking Modelo ng Wika (LLMs) at Maliit na Modelo ng Wika (SLMs)

Ang parehong LLM at SLM ay itinayo gamit ang mga pundasyong prinsipyo ng probabilistic na machine learning, sumusunod sa magkakatulad na mga pamamaraan sa kanilang disenyo ng arkitektura, mga metodolohiya sa pagsasanay, mga proseso ng pagbuo ng datos, at mga pamamaraan ng ebalwasyon ng modelo. Gayunpaman, may ilang mahahalagang mga salik na nag-iiba sa dalawang uri ng mga modelong ito.

## Mga Aplikasyon ng Maliit na Modelo ng Wika

Ang mga SLM ay may malawak na hanay ng mga aplikasyon, kabilang ang:

- Chatbots: Pagbibigay ng suporta sa customer at pakikipag-ugnayan sa mga gumagamit sa paraang conversational.
- Paglikha ng Nilalaman: Pagtulong sa mga manunulat sa pamamagitan ng paglikha ng mga ideya o kahit pagbuo ng buong artikulo.
- Edukasyon: Pagtulong sa mga estudyante sa pagsulat ng mga takdang-aralin o pag-aaral ng mga bagong wika.
- Accessibility: Paglikha ng mga kasangkapan para sa mga indibidwal na may kapansanan, tulad ng mga sistema ng teksto-sa-pagsasalita.

**Sukat**
  
Isang pangunahing pagkakaiba sa pagitan ng LLM at SLM ay nasa sukat ng mga modelo. Ang mga LLM, tulad ng ChatGPT (GPT-4), ay maaaring magkaroon ng tinatayang 1.76 trilyong mga parameter, habang ang mga open-source na SLM tulad ng Mistral 7B ay dinisenyo na may mas kaunting mga parameter—mga 7 bilyon. Ang pagkakaibang ito ay pangunahing sanhi ng pagkakaiba sa arkitektura ng modelo at mga proseso ng pagsasanay. Halimbawa, ang ChatGPT ay gumagamit ng self-attention mechanism sa loob ng encoder-decoder na balangkas, samantalang ang Mistral 7B ay gumagamit ng sliding window attention, na nagpapahintulot sa mas epektibong pagsasanay sa isang decoder-only na modelo. Ang pagkakaibang arkitekturang ito ay may malalim na epekto sa komplikasyon at pagganap ng mga modelong ito.

**Pagkaunawa**

Ang mga SLM ay karaniwang optimized para sa pagganap sa mga partikular na domain, kaya sila ay lubhang espesyal pero maaaring limitado sa kanilang kakayahang magbigay ng malawak na kontekstuwal na pag-unawa sa maraming larangan ng kaalaman. Sa kabilang banda, ang LLM ay nagtuturing na mag-modelo ng katalinuhan na kahalintulad ng tao sa mas malawak na antas. Sinanay sa malawak at magkakaibang dataset, ang LLM ay idinisenyo upang mag-perform nang mahusay sa iba’t ibang domain, na nag-aalok ng mas malaking versatility at adaptability. Dahil dito, ang mga LLM ay mas angkop para sa mas malawak na saklaw ng mga downstream na gawain, tulad ng natural language processing at programming.

**Pagkompyut**

Ang pagsasanay at pag-deploy ng mga LLM ay mabigat na proseso sa yaman, madalas na nangangailangan ng malawakang imprastruktura sa kompyutasyon, kabilang ang malalaking GPU clusters. Halimbawa, ang pagsasanay sa isang modelong tulad ng ChatGPT mula sa simula ay maaaring mangailangan ng libu-libong GPU sa mahabang panahon. Sa kabilang banda, ang mga SLM, na may mas maliit na bilang ng mga parameter, ay mas accessible sa mga tuntunin ng mga yaman sa kompyutasyon. Ang mga modelong tulad ng Mistral 7B ay maaaring sanayin at patakbuhin sa mga lokal na makina na may katamtamang kapasidad ng GPU, bagaman ang pagsasanay ay nangangailangan pa rin ng ilang oras gamit ang maraming GPU.

**Bias**

Ang bias ay isang kilalang isyu sa LLM, pangunahing dahil sa kalikasan ng data ng pagsasanay. Madalas na umaasa ang mga modelong ito sa raw, malayang magagamit na datos mula sa internet, na maaaring hindi kabilang o mali ang pagrepresenta sa ilang mga grupo, magpakilala ng maling pag-label, o magpakita ng lingguwistikong mga bias na naiimpluwensiyahan ng diyalekto, heograpikal na pagkakaiba, at mga tuntunin sa gramatika. Bukod pa rito, ang komplikasyon ng mga arkitektura ng LLM ay maaaring hindi sinasadyang magpalala ng bias, na maaaring hindi mapansin nang walang maingat na fine-tuning. Sa kabilang banda, ang mga SLM, na sinanay sa mas limitadong, domain-specific na mga dataset, ay likas na hindi gaanong madaling maapektuhan ng ganitong mga bias, bagaman hindi sila ganap na immune dito.

**Inference**

Ang nabawasang sukat ng mga SLM ay nagbibigay ng malaking bentahe sa bilis ng inference, na nagpapahintulot sa kanila na makabuo ng mga output nang mahusay sa lokal na hardware nang hindi nangangailangan ng malawakang parallel na pagproseso. Sa kabilang banda, ang mga LLM, dahil sa kanilang laki at komplikasyon, ay madalas na nangangailangan ng malalaking parallel na mga yaman sa kompyutasyon upang makamit ang katanggap-tanggap na mga oras ng inference. Ang presensya ng maraming kasabay na gumagamit ay lalo pang nagpapabagal sa mga response time ng LLM, lalo na kapag inilalapat sa malawakang sukat.

Sa kabuuan, bagaman ang parehong LLM at SLM ay may pundasyong batayan sa machine learning, sila ay malaki ang pagkakaiba sa laki ng modelo, mga kinakailangan sa yaman, kontekstuwal na pag-unawa, pagiging bulnerable sa bias, at bilis ng inference. Ang mga pagkakaibang ito ay nagpapakita ng kani-kanilang angkop na paggamit, kung saan ang LLM ay mas versatile ngunit mabigat ang pangangailangan sa yaman, at ang SLM ay nag-aalok ng mas mabisang kahusayan sa tiyak na domain na may nabawasang pangangailangan sa kompyutasyon.

***Tandaan: Sa araling ito, ipakikilala namin ang SLM gamit ang Microsoft Phi-3 / 3.5 bilang halimbawa.***

## Ipakilala ang Phi-3 / Phi-3.5 Family

Pangunahing tinatarget ng Phi-3 / 3.5 Family ang mga senaryo ng aplikasyon sa teksto, pananaw, at Agent (MoE):

### Phi-3 / 3.5 Instruct

Pangunahing para sa pagbuo ng teksto, kumpletong chat, at pagkuha ng impormasyon sa nilalaman, atbp.

**Phi-3-mini**

Ang 3.8B na modelo ng wika ay available sa Microsoft Foundry, Hugging Face, at Ollama. Ang mga Phi-3 na modelo ay malaki ang nalalampasan sa pagganap kumpara sa mga modelong pareho at mas malaki ang sukat sa mga pangunahing benchmark (tingnan ang mga numero ng benchmark sa ibaba, mas mataas na numero ay mas maganda). Ang Phi-3-mini ay nalalampasan ang mga modelong doble ang laki nito, habang ang Phi-3-small at Phi-3-medium ay nalalampasan ang mas malalaking modelo, kabilang ang GPT-3.5.

**Phi-3-small at medium**

Sa 7B na mga parameter, tinatalo ng Phi-3-small ang GPT-3.5T sa iba't ibang mga benchmark sa wika, pangangatwiran, coding, at matematika.

Ang Phi-3-medium na may 14B na mga parameter ay nagpapatuloy ng trend na ito at nalalampasan ang Gemini 1.0 Pro.

**Phi-3.5-mini**

Maaari natin itong isipin bilang pag-upgrade ng Phi-3-mini. Habang nananatili ang bilang ng mga parameter, pinapabuti nito ang kakayahan na suportahan ang maraming wika (sumusuporta sa 20+ na wika: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​at nagdaragdag ng mas matibay na suporta para sa mahabang konteksto.

Ang Phi-3.5-mini na may 3.8B parameter ay nalalampasan ang mga modelong wika na may kaparehong laki at katumbas ng mga modelo ng doble ang laki nito.

### Phi-3 / 3.5 Vision

Maaari nating isipin ang Instruct na modelo ng Phi-3/3.5 bilang kakayahan ng Phi na umunawa, at ang Vision ay ang nagbibigay ng mga mata kay Phi para maintindihan ang mundo.


**Phi-3-Vision**

Ang Phi-3-vision, na may 4.2B lamang na parameter, ay nagpapatuloy ng trend na ito at nalalampasan ang mas malalaking modelo tulad ng Claude-3 Haiku at Gemini 1.0 Pro V sa mga pangkalahatang gawain sa pangangatwiran ng biswal, OCR, at pag-unawa sa mga talahanayan at diagram.


**Phi-3.5-Vision**

Ang Phi-3.5-Vision ay isang pag-upgrade rin ng Phi-3-Vision, na nagdaragdag ng suporta para sa maraming mga larawan. Maaari mo itong isipin bilang pagpapabuti sa pananaw; hindi lamang nakikita mo ang mga larawan, kundi pati na rin ang mga video.

Nalalampasan ng Phi-3.5-vision ang mas malalaking modelo tulad ng Claude-3.5 Sonnet at Gemini 1.5 Flash sa OCR, pag-unawa sa mga talahanayan at tsart, at pantay sa mga gawain sa pangkalahatang pangangatwiran ng biswal na kaalaman. Sumusuporta sa multi-frame input, ibig sabihin ay pagbibigay ng pangangatwiran sa maraming input na mga larawan


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ay nagpapahintulot sa mga modelong ma-pretrain gamit ang mas kaunting compute, na ibig sabihin ay maaari mong palakihin nang malaki ang laki ng modelo o dataset gamit ang parehong budget sa compute tulad ng dense model. Partikular, ang isang MoE na modelo ay dapat makamit ang parehong kalidad tulad ng dense counterpart nito nang mas mabilis sa panahon ng pretraining.

Binubuo ang Phi-3.5-MoE ng 16x3.8B expert modules. Ang Phi-3.5-MoE, na may 6.6B lamang na aktibong parameter, ay nakakamit ng katulad na antas ng pangangatwiran, pag-unawa sa wika, at matematika tulad ng mas malalaking mga modelo.

Maaari nating gamitin ang modelong Phi-3/3.5 Family base sa iba't ibang mga senaryo. Hindi tulad ng LLM, maaari mong i-deploy ang Phi-3/3.5-mini o Phi-3/3.5-Vision sa mga edge device.


## Paano Gamitin ang Mga Modelong Phi-3/3.5 Family

Nais naming gamitin ang Phi-3/3.5 sa iba't ibang mga senaryo. Susunod, gagamitin natin ang Phi-3/3.5 batay sa iba't ibang mga senaryo.

![phi3](../../../translated_images/tl/phi3.655208c3186ae381.webp)

### Inference sa pamamagitan ng Cloud APIs

**Microsoft Foundry Models**

> **Tandaan:** Ang GitHub Models ay magreretire sa katapusan ng Hulyo 2026. Ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ang direktang kapalit.

Ang Microsoft Foundry Models ang pinakadirektang paraan. Maaari kang mabilis na makakuha ng access sa Phi-3/3.5-Instruct model sa pamamagitan ng Foundry model catalog. Pinagsama sa Azure AI Inference SDK / OpenAI SDK, maaari mong i-access ang API sa pamamagitan ng code upang kumpletuhin ang tawag sa Phi-3/3.5-Instruct. Maaari mo ring subukan ang iba't ibang epekto sa pamamagitan ng Playground.

- Demo: Paghahambing ng epekto ng Phi-3-mini at Phi-3.5-mini sa mga senaryong Tsino

![phi3](../../../translated_images/tl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/tl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

O kung nais nating gamitin ang mga modelo sa vision at MoE, maaari mong gamitin ang Microsoft Foundry para kumpletuhin ang tawag. Kung interesado ka, maaari mong basahin ang Phi-3 Cookbook para matutunan kung paano tawagan ang Phi-3/3.5 Instruct, Vision, MoE sa pamamagitan ng Microsoft Foundry [Pindutin ang link na ito](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bilang karagdagan sa cloud-based na Microsoft Foundry Models catalog, maaari mo ring gamitin ang [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) upang makumpleto ang mga kaugnay na tawag. Maaari mong bisitahin ang NVIDIA NIM upang kumpletuhin ang mga tawag sa API ng Phi-3/3.5 Family. Ang NVIDIA NIM (NVIDIA Inference Microservices) ay isang set ng mga pabilisin na inference microservices na dinisenyo upang tulungan ang mga developer mag-deploy ng mga AI model nang mahusay sa iba't ibang mga kapaligiran, kabilang ang mga cloud, data centers, at workstations.

Narito ang ilan sa mga pangunahing tampok ng NVIDIA NIM:

- **Dali ng Pag-deploy:** Pinapayagan ng NIM ang pag-deploy ng mga AI model gamit ang isang utos lang, na ginagawang madali itong ipasok sa mga umiiral na workflow.

- **Pinahusay na Pagganap:** Ginagamit nito ang NVIDIA’s pre-optimized inference engines, tulad ng TensorRT at TensorRT-LLM, upang matiyak ang mababang latency at mataas na throughput.
- **Scalability:** Sinusuportahan ng NIM ang autoscaling sa Kubernetes, na nagpapahintulot dito na epektibong hawakan ang iba't ibang workload.
- **Seguridad at Kontrol:** Maaaring panatilihin ng mga organisasyon ang kontrol sa kanilang data at mga aplikasyon sa pamamagitan ng self-hosting ng NIM microservices sa kanilang sariling pinamamahalaang imprastruktura.
- **Standard APIs:** Nagbibigay ang NIM ng mga industry-standard na API, kaya madaling bumuo at mag-integrate ng mga aplikasyon ng AI tulad ng mga chatbot, AI assistants, at iba pa.

Bahagi ang NIM ng NVIDIA AI Enterprise, na naglalayong gawing mas simple ang pagpapatupad at operasyon ng mga modelo ng AI, na tinitiyak na tumatakbo sila nang mahusay sa NVIDIA GPUs.

- Demo: Paggamit ng NVIDIA NIM upang tawagan ang Phi-3.5-Vision-API  [[I-click ang link na ito](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pagpapatakbo ng Phi-3/3.5 Nang Lokal
Ang inference kaugnay ng Phi-3, o anumang language model tulad ng GPT-3, ay tumutukoy sa proseso ng paggawa ng mga tugon o prediksyon batay sa input na natatanggap nito. Kapag nagbigay ka ng prompt o tanong sa Phi-3, ginagamit nito ang kanyang sinanay na neural network upang mahinuha ang pinaka-posible at may kaugnayang sagot sa pamamagitan ng pagsusuri sa mga pattern at relasyon sa data na pinag-aralan nito.

**Hugging Face Transformer**
Ang Hugging Face Transformers ay isang makapangyarihang library na dinisenyo para sa natural language processing (NLP) at iba pang mga gawain sa machine learning. Narito ang ilang mahahalagang punto tungkol dito:

1. **Pretrained Models**: Nagbibigay ito ng libu-libong pretrained models na maaaring gamitin para sa iba't ibang gawain tulad ng text classification, named entity recognition, question answering, summarization, translation, at text generation.

2. **Framework Interoperability**: Sinusuportahan ng library ang maraming deep learning frameworks, kabilang ang PyTorch, TensorFlow, at JAX. Ito ay nagpapahintulot sa iyo na magsanay ng modelo sa isang framework at gamitin ito sa iba.

3. **Multimodal Capabilities**: Bukod sa NLP, sinusuportahan din ng Hugging Face Transformers ang mga gawain sa computer vision (hal., image classification, object detection) at audio processing (hal., speech recognition, audio classification).

4. **Kadalian ng Paggamit**: Nag-aalok ang library ng mga API at tool upang madaliang mag-download at mag-fine-tune ng mga modelo, na ginagawang accessible para sa mga baguhan at eksperto.

5. **Komunidad at Mga Mapagkukunan**: May buhay na komunidad ang Hugging Face at malawak na dokumentasyon, mga tutorial, at mga gabay upang matulungan ang mga gumagamit na makapagsimula at magamit nang husto ang library.
[opisyal na dokumentasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o ang kanilang [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ito ang pinaka-karaniwang paraan ng paggamit, ngunit nangangailangan din ito ng GPU acceleration. Pagkatapos ng lahat, ang mga senaryo tulad ng Vision at MoE ay nangangailangan ng maraming kalkulasyon, na magiging napakabagal kung CPU lang ang gagamitin kung hindi ito na-quantize.


- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Instruct [I-click ang link na ito](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Vision [I-click ang link na ito](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-MoE [I-click ang link na ito](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ay isang platform na dinisenyo upang gawing mas madali ang pagpapatakbo ng malalaking language model (LLMs) nang lokal sa iyong makina. Sinusuportahan nito ang iba't ibang modelo tulad ng Llama 3.1, Phi 3, Mistral, at Gemma 2, bukod sa iba pa. Pinapasimple ng platform ang proseso sa pamamagitan ng pagsasama-sama ng model weights, configuration, at data sa isang pakete, na ginagawang mas accessible para sa mga gumagamit na i-customize at gumawa ng kanilang sariling mga modelo. Available ang Ollama para sa macOS, Linux, at Windows. Ito ay isang mahusay na tool kung nais mong mag-eksperimento o mag-deploy ng LLMs nang hindi umaasa sa mga cloud service. Ang Ollama ang pinaka-direktang paraan, kailangan mo lang patakbuhin ang sumusunod na utos.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ay offline, on-device runtime ng Microsoft para sa pagpapatakbo ng mga modelo tulad ng Phi nang ganap sa sarili mong hardware - hindi kailangan ng Azure subscription, API key, o koneksyon sa network. Awtomatikong pinipili nito ang pinakamahusay na execution provider na available (NPU, GPU, o CPU) at nag-eexpose ng OpenAI-compatible endpoint, kaya ang umiiral na `openai`/Azure AI Inference SDK code ay maaaring tumuro dito nang may kaunting pagbabago lamang. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) upang makapagsimula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

O gamitin ang SDK nang direkta sa Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime para sa GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ay isang cross-platform inference at training machine-learning accelerator. Ang ONNX Runtime para sa Generative AI (GENAI) ay isang makapangyarihang tool na tumutulong sa iyo na patakbuhin nang mahusay ang mga generative AI models sa iba't ibang plataporma.

## Ano ang ONNX Runtime?
Ang ONNX Runtime ay isang open-source na proyekto na nagbibigay-daan sa mataas na performance na inference ng mga machine learning models. Sinusuportahan nito ang mga modelo sa Open Neural Network Exchange (ONNX) format, na isang standard para sa representasyon ng mga modelo sa machine learning. Ang ONNX Runtime inference ay maaaring magbigay ng mas mabilis na karanasan sa customer at mas mababang gastos, sinusuportahan ang mga modelo mula sa deep learning frameworks tulad ng PyTorch at TensorFlow/Keras pati na rin sa mga klasikong machine learning libraries tulad ng scikit-learn, LightGBM, XGBoost, atbp. Compatible ang ONNX Runtime sa iba't ibang hardware, drivers, at operating systems, at nagbibigay ng optimal na performance sa pamamagitan ng paggamit ng hardware accelerators kung saan angkop pati na rin ang graph optimizations at transforms.

## Ano ang Generative AI?
Ang Generative AI ay tumutukoy sa mga sistema ng AI na kayang gumawa ng bagong nilalaman, tulad ng teksto, mga larawan, o musika, batay sa mga data na pinag-aralan nila. Halimbawa nito ang mga language models tulad ng GPT-3 at mga image generation models tulad ng Stable Diffusion. Nagbibigay ang ONNX Runtime para sa GenAI library ng generative AI loop para sa ONNX models, kabilang ang inference gamit ang ONNX Runtime, logits processing, search at sampling, at KV cache management.

## ONNX Runtime para sa GENAI
Pinalalawak ng ONNX Runtime para sa GENAI ang mga kakayahan ng ONNX Runtime upang suportahan ang mga generative AI models. Narito ang ilang mahahalagang tampok:

- **Malawak na Suporta sa Platform:** Gumagana ito sa iba't ibang platform, kabilang ang Windows, Linux, macOS, Android, at iOS.
- **Suporta sa Modelo:** Sinusuportahan nito ang maraming tanyag na generative AI models, tulad ng LLaMA, GPT-Neo, BLOOM, at iba pa.
- **Pag-optimize ng Performance:** May kasamang optimizations para sa iba't ibang hardware accelerators tulad ng NVIDIA GPUs, AMD GPUs, at iba pa2.
- **Kadalian ng Paggamit:** Nagbibigay ito ng mga API para sa madaling integrasyon sa mga aplikasyon, na nagpapahintulot sa iyo na gumawa ng teksto, mga larawan, at iba pang nilalaman gamit ang kaunting code lang.
- Maaaring tawagan ng mga gumagamit ang mataas na antas na generate() method, o patakbuhin ang bawat iterasyon ng modelo sa isang loop, na bumubuo ng isang token sa bawat pagkakataon, at opsyonal na ina-update ang mga generation parameters sa loob ng loop.
- Ang ONNX runtime ay may suporta rin para sa greedy/beam search at TopP, TopK sampling upang gumawa ng mga token sequences at may built-in na logits processing tulad ng repetition penalties. Maaari ka ring madaling magdagdag ng custom scoring.

## Pagsisimula
Upang makapagsimula sa ONNX Runtime para sa GENAI, maaari mong sundin ang mga hakbang na ito:

### I-install ang ONNX Runtime:
```Python
pip install onnxruntime
```
### I-install ang Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Patakbuhin ang isang Modelo: Narito ang simpleng halimbawa sa Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo:Paggamit ng ONNX Runtime GenAI upang tawagan ang Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Iba pa**

Bukod sa ONNX Runtime, Ollama, at Foundry Local na mga reference methods, maaari rin nating kompletuhin ang reference ng quantitative models batay sa mga model reference methods na ibinigay ng iba't ibang mga tagagawa. Tulad ng Apple MLX framework na may Apple Metal, Qualcomm QNN na may NPU, Intel OpenVINO na may CPU/GPU, atbp. Maaari ka ring makakuha ng higit pang nilalaman mula sa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Higit Pa

Napag-aralan na natin ang mga batayan ng Phi-3/3.5 Family, ngunit upang matutunan pa ang tungkol sa SLM kailangan natin ng mas maraming kaalaman. Maaari mong makita ang mga sagot sa Phi-3 Cookbook. Kung nais mong matuto pa, mangyaring bisitahin ang [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->