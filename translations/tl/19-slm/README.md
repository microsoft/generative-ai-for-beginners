# Panimula sa Maliit na Modelo ng Wika para sa Generative AI para sa mga Nagsisimula
Ang Generative AI ay isang nakakatuwang larangan ng artificial intelligence na nakatuon sa paglikha ng mga sistema na kayang bumuo ng bagong nilalaman. Ang nilalamang ito ay maaaring mula sa teksto at mga imahe hanggang sa musika at maging sa buong virtual na mga kapaligiran. Isa sa mga pinaka-kapanapanabik na aplikasyon ng generative AI ay nasa larangan ng mga modelo ng wika.

## Ano ang Maliit na Modelo ng Wika?

Ang Maliit na Modelo ng Wika (SLM) ay kumakatawan sa isang binawasang bersyon ng malaking modelo ng wika (LLM), na ginagamit ang maraming mga prinsipyo ng arkitektura at mga teknik ng LLM, habang nagpapakita ng makabuluhang nabawasang pangangailangan sa komputasyon.

Ang mga SLM ay isang bahagi ng mga modelo ng wika na dinisenyo upang bumuo ng tekstong katulad ng sa tao. Hindi tulad ng kanilang mas malalaking katapat, tulad ng GPT-4, ang mga SLM ay mas compact at episyente, kaya't ideal sila para sa mga aplikasyon kung saan limitado ang mga mapagkukunan sa komputasyon. Sa kabila ng kanilang mas maliit na sukat, kaya pa rin nilang magsagawa ng iba't ibang gawain. Karaniwang itinatayo ang mga SLM sa pamamagitan ng pag-compress o pag-distill ng LLMs, na naglalayong mapanatili ang malaking bahagi ng orihinal na functionality at kakayahan sa lingguwistika ng modelo. Ang pagbawas na ito sa laki ng modelo ay nagpapababa sa kabuuang komplikasyon, na ginagawang mas episyente ang mga SLM sa paggamit ng memorya at kinakailangang komputasyon. Sa kabila ng mga optimisasyong ito, kaya pa rin ng mga SLM na magsagawa ng malawak na hanay ng mga gawain sa natural language processing (NLP):

- Paggawa ng Teksto: Paglikha ng mga magkakasunod at kontekstuwal na makabuluhang mga pangungusap o talata.
- Pagkumpleto ng Teksto: Paghula at pagtapos ng mga pangungusap batay sa ibinigay na prompt.
- Pagsasalin: Pagsasalin ng teksto mula sa isang wika patungo sa isa pa.
- Pagsusuma: Pagbubuod ng mahahabang teksto sa mas maikli, mas madaling maintindihang mga buod.

Bagaman may ilang trade-off sa pagganap o lalim ng pag-unawa kumpara sa kanilang mas malalaking katapat.

## Paano Gumagana ang Maliit na Modelo ng Wika?
Ang mga SLM ay sinasanay sa napakalaking dami ng datos ng teksto. Sa panahon ng pagsasanay, natututo sila ng mga pattern at istruktura ng wika, na nagbibigay-daan sa kanila upang bumuo ng teksto na parehong gramatically tama at naaayon sa konteksto. Ang proseso ng pagsasanay ay kinabibilangan ng:

- Pangangalap ng Datos: Pagkuha ng malalaking dataset ng teksto mula sa iba't ibang pinagkukunan.
- Preprocessing: Paglilinis at pag-aayos ng datos upang maging angkop para sa pagsasanay.
- Pagsasanay: Paggamit ng mga algorithm ng machine learning upang turuan ang modelo kung paano intindihin at gumawa ng teksto.
- Fine-Tuning: Pagsasaayos ng modelo para mapabuti ang pagganap nito sa mga partikular na gawain.

Ang pag-develop ng mga SLM ay kaayon ng lumalaking pangangailangan para sa mga modelo na maaaring i-deploy sa mga kapaligirang may limitadong mapagkukunan, gaya ng mga mobile devices o edge computing platforms, kung saan ang full-scale na mga LLM ay maaaring maging hindi praktikal dahil sa kanilang mabigat na pangangailangan sa mapagkukunan. Sa pamamagitan ng pagtutok sa episyensya, nilalapatan ng SLM ang balanse ng pagganap at aksesibilidad, na nagpapahintulot ng mas malawak na aplikasyon sa iba't ibang larangan.

![slm](../../../translated_images/tl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mga Layunin sa Pagkatuto

Sa leksyong ito, inaasahan naming ipakilala ang kaalaman tungkol sa SLM at pagsamahin ito sa Microsoft Phi-3 upang pag-aralan ang iba't ibang senaryo sa tekstong nilalaman, paningin, at MoE.

Sa pagtatapos ng leksyong ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang SLM?
- Ano ang kaibahan ng SLM at LLM?
- Ano ang Pamilyang Microsoft Phi-3/3.5?
- Paano patakbuhin ang inference gamit ang Pamilyang Microsoft Phi-3/3.5?

Handa ka na ba? Magsimula na tayo.

## Ang Mga Pagkakaiba sa pagitan ng Malaking Modelo ng Wika (LLMs) at Maliit na Modelo ng Wika (SLMs)

Ang parehong LLM at SLM ay nakabatay sa mga pundamental na prinsipyo ng probabilistic machine learning, sumusunod sa magkakaparehong pamamaraan sa kanilang disenyo ng arkitektura, metodolohiya ng pagsasanay, proseso ng paglikha ng datos, at mga teknik sa pagsusuri ng modelo. Gayunpaman, may ilang susi na mga pagkakaiba na naghihiwalay sa dalawang uri ng mga modelong ito.

## Mga Aplikasyon ng Maliit na Modelo ng Wika

Ang mga SLM ay may malawak na hanay ng mga aplikasyon, kabilang ang:

- Mga Chatbot: Nagbibigay ng suporta sa mga kustomer at nakikipag-ugnayan sa mga gumagamit sa paraang pakikipag-usap.
- Paglikha ng Nilalaman: Tumutulong sa mga manunulat sa pagbuo ng mga ideya o kahit sa pag-draft ng buong mga artikulo.
- Edukasyon: Tinutulungan ang mga estudyante sa mga takdang-aralin sa pagsusulat o pag-aaral ng bagong mga wika.
- Aksesibilidad: Lumilikha ng mga kagamitan para sa mga indibidwal na may kapansanan, tulad ng mga sistema ng text-to-speech.

**Sukat**
  
Ang pangunahing pagkakaiba sa pagitan ng LLM at SLM ay ang sukat ng mga modelo. Ang mga LLM, tulad ng ChatGPT (GPT-4), ay maaaring magkaroon ng tinatayang 1.76 trilyong mga parameter, habang ang mga open-source na SLM tulad ng Mistral 7B ay dinisenyo na may mas kaunting bilang ng mga parameter—mga 7 bilyon. Ang diperensyang ito ay pangunahing sanhi ng pagkakaiba sa arkitektura ng modelo at mga proseso ng pagsasanay. Halimbawa, gumagamit ang ChatGPT ng self-attention mechanism sa loob ng isang encoder-decoder na balangkas, samantalang ang Mistral 7B ay gumagamit ng sliding window attention, na nagbibigay-daan sa mas episyenteng pagsasanay sa loob ng isang decoder-only na modelo. Ang pagkakaibang ito sa arkitektura ay may malalalim na epekto sa komplikasyon at pagganap ng mga modelong ito.

**Pag-unawa**

Karaniwang iniaangkop ang mga SLM para sa pagganap sa mga partikular na domain, kaya't sila ay lubos na espesyalisado ngunit maaaring limitado sa kanilang kakayahang magbigay ng malawak na kontekstong pag-unawa sa maraming larangan ng kaalaman. Sa kabilang banda, ang LLM ay nilalayon na gayahin ang katalinuhan ng tao sa mas malawak na antas. Sinanay sa malalawak at magkakaibang mga dataset, dinisenyo ang LLM na magsagawa nang mahusay sa iba't ibang larangan, na nagbibigay ng mas malaking versatility at adaptability. Dahil dito, mas angkop ang LLM para sa mas malawak na hanay ng mga downstream na gawain, gaya ng natural language processing at programming.

**Pagkompyut**

Ang pagsasanay at pag-deploy ng mga LLM ay mga proseso na matindi ang pangangailangan sa mga mapagkukunan, madalas na nangangailangan ng malaking imprastraktura ng kompyuter, kabilang ang mga malalaking GPU clusters. Halimbawa, ang pagsasanay sa isang modelo tulad ng ChatGPT mula sa simula ay maaaring mangailangan ng libu-libong GPU sa mahabang panahon. Sa kabilang banda, ang mga SLM, na may mas maliit na bilang ng mga parameter, ay mas madaling ma-access pagdating sa mapagkukunan ng kompyutasyon. Ang mga modelong gaya ng Mistral 7B ay maaaring sanayin at patakbuhin sa mga lokal na makina na may katamtamang GPU capabilities, bagaman ang pagsasanay ay nangangailangan pa rin ng ilang oras sa maraming GPU.

**Pagkiling (Bias)**

Ang pagkiling ay kilalang isyu sa mga LLM, pangunahing sanhi ng likas na katangian ng datos sa pagsasanay. Kadalasang umaasa ang mga modelong ito sa hilaw, bukas na datos mula sa internet, na maaaring kulang sa representasyon o maling representasyon ng ilang mga grupo, magdala ng maling tagging, o magpakita ng lingguwistikang pagkiling na naiimpluwensyahan ng diyalekto, heograpikong pagkakaiba, at mga panuntunang gramatikal. Bukod pa rito, ang kumplikado ng arkitektura ng LLM ay maaaring walang malay na palalain ang pagkiling, na maaaring hindi mapansin kung walang maingat na fine-tuning. Sa kabilang banda, ang mga SLM, na sinanay sa mas limitado at domain-specific na mga dataset, ay likas na mas kaunti ang pagiging sensitibo sa ganitong mga bias, bagaman hindi sila ganap na immune rito.

**Inference**

Ang mas nabawasang sukat ng mga SLM ay nagbibigay sa kanila ng malaking kalamangan pagdating sa bilis ng inference, na nagpapahintulot sa kanila na makabuo ng output nang episyente sa lokal na hardware nang hindi nangangailangan ng malawakang parallel processing. Sa kabilang banda, ang LLM dahil sa laki at kumplikasyon nito ay madalas na nangangailangan ng malulaking parallel na mapagkukunan ng kompyutasyon upang makamit ang katanggap-tanggap na oras ng inference. Ang presensya ng maraming sabay-sabay na gumagamit ay nagpabagal pa lalo sa oras ng tugon ng LLM, lalo na kapag na-deploy sa malawakang saklaw.

Sa kabuuan, habang parehong nakabatay ang LLM at SLM sa pundamental na batayan ng machine learning, malaki ang kanilang pagkakaiba sa sukat ng modelo, pangangailangan sa mapagkukunan, kontekstuwal na pag-unawa, pagiging sensitibo sa bias, at bilis ng inference. Ang mga pagkakaibang ito ay nagpapakita ng kanilang kani-kaniyang kahusayan para sa iba't ibang mga kaso ng paggamit, kung saan ang LLM ay mas versatile ngunit matindi ang pangangailangan sa mapagkukunan, at ang SLM ay nag-aalok ng mas espesyal na episyensya sa domain na may nabawasang pangangailangan sa komputasyon.

***Tandaan: Sa leksyong ito, ipakikilala natin ang SLM gamit ang Microsoft Phi-3 / 3.5 bilang halimbawa.***

## Ipakilala ang Pamilyang Phi-3 / Phi-3.5

Pangunahing tinatarget ng Pamilyang Phi-3 / 3.5 ang mga senaryo ng aplikasyon sa teksto, paningin, at Ahente (MoE):

### Phi-3 / 3.5 Instruct

Pangunahin para sa paggawa ng teksto, pag-kompleto ng chat, at pagkuha ng impormasyon mula sa nilalaman, atbp.

**Phi-3-mini**

Ang 3.8B na modelo ng wika ay makukuha sa Microsoft Foundry, Hugging Face, at Ollama. Malaki ang kalamangan ng mga Phi-3 na modelo kumpara sa mga modelo ng wika ng parehong laki o mas malaki sa mga pangunahing benchmark (tingnan ang mga numero ng benchmark sa ibaba, mas mataas na numero ay mas maganda). Ang Phi-3-mini ay mas mahusay kaysa sa mga modelong doble ang laki nito, habang ang Phi-3-small at Phi-3-medium ay nakahihigit sa mas malalaking modelo, kabilang ang GPT-3.5.

**Phi-3-small & medium**

Sa 7B parameters lamang, tinalo ng Phi-3-small ang GPT-3.5T sa iba't ibang benchmark sa wika, pangangatwiran, coding, at math.

Ang Phi-3-medium na may 14B parameters ay nagpapatuloy sa tendensiyang ito at nalalampasan ang Gemini 1.0 Pro.

**Phi-3.5-mini**

Maaari natin itong ituring bilang isang pag-upgrade ng Phi-3-mini. Habang nananatiling pareho ang bilang ng mga parameter, pinapabuti nito ang kakayahang suportahan ang maraming wika (sumusuporta sa higit sa 20 wika: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​at nagbibigay ng mas malakas na suporta para sa mahahabang konteksto.

Ang Phi-3.5-mini na may 3.8B parameters ay mas mahusay kaysa sa mga modelo ng parehong laki at kapantay ng mga modelo na doble ang laki nito.

### Phi-3 / 3.5 Vision

Maaari nating isipin ang Instruct na modelo ng Phi-3/3.5 bilang kakayahan ng Phi na umunawa, at ang Vision ay nagbibigay kay Phi ng mga mata upang maunawaan ang mundo.


**Phi-3-Vision**

Ang Phi-3-vision, na may 4.2B parameters lamang, ay nagpapatuloy sa tendensiyang ito at nalalampasan ang mga mas malalaking modelo tulad ng Claude-3 Haiku at Gemini 1.0 Pro V sa mga pangkalahatang gawain sa visual reasoning, OCR, at pag-unawa sa mga talahanayan at diagram.


**Phi-3.5-Vision**

Ang Phi-3.5-Vision ay isang pag-upgrade din ng Phi-3-Vision, na nagbibigay ng suporta para sa maraming mga imahe. Maaari mo itong isipin bilang isang pagpapabuti sa paningin, hindi lang kayang makita ang mga larawan, pati na rin ang mga video.

Nalalampasan ng Phi-3.5-vision ang mga mas malalaking modelo tulad ng Claude-3.5 Sonnet at Gemini 1.5 Flash sa OCR, pag-unawa sa mga talahanayan at tsart, at kapantay sa mga pangkalahatang gawain sa visual na pangangatwiran sa kaalaman. Sinusuportahan ang multi-frame input, ibig sabihin ay nagsasagawa ng pangangatwiran sa maraming input na mga imahe.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ay nagbibigay-daan sa mga modelo na ma-pretrain gamit ang mas kakaunting compute, na nangangahulugang maaari mong palakihin nang malaki ang laki ng modelo o dataset gamit ang parehong compute budget tulad ng isang dense na modelo. Partikular, ang isang MoE na modelo ay dapat makamit ang parehong kalidad tulad ng dense na katapat nito nang mas mabilis sa panahon ng pretraining.

Binubuo ang Phi-3.5-MoE ng 16x3.8B na mga expert modules. Ang Phi-3.5-MoE na may 6.6B active parameters lamang ay nakakamit ng katulad na antas ng pangangatwiran, pag-unawa sa wika, at math tulad ng mas malalaking mga modelo.

Maaari nating gamitin ang Pamilyang Phi-3/3.5 na modelo batay sa iba't ibang senaryo. Hindi tulad ng LLM, maaari mong i-deploy ang Phi-3/3.5-mini o Phi-3/3.5-Vision sa mga edge device.


## Paano Gamitin ang Mga Modelong Pamilya ng Phi-3/3.5

Inaasahan naming gamitin ang Phi-3/3.5 sa iba't ibang mga senaryo. Susunod, gagamitin natin ang Phi-3/3.5 batay sa iba't ibang mga senaryo.

![phi3](../../../translated_images/tl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inference sa pamamagitan ng Cloud APIs

**Microsoft Foundry Models**

> **Tandaan:** Ang GitHub Models ay aalisin sa katapusan ng Hulyo 2026. Ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ang direktang kapalit.

Ang Microsoft Foundry Models ang pinaka-direktang paraan. Maaari kang mabilis na maka-access sa Phi-3/3.5-Instruct na modelo sa pamamagitan ng Foundry model catalog. Kasama ang Azure AI Inference SDK / OpenAI SDK, maaari kang gamitin ang API sa pamamagitan ng code upang makumpleto ang Phi-3/3.5-Instruct na tawag. Maaari mo ring subukan ang iba't ibang epekto sa pamamagitan ng Playground.

- Demo: Paghahambing ng mga epekto ng Phi-3-mini at Phi-3.5-mini sa mga senaryong Tsino

![phi3](../../../translated_images/tl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/tl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

O kung nais nating gamitin ang vision at MoE na mga modelo, maaari mong gamitin ang Microsoft Foundry para kumpletuhin ang tawag. Kung interesado ka, maaari mong basahin ang Phi-3 Cookbook upang matutunan kung paano tawagin ang Phi-3/3.5 Instruct, Vision, MoE sa pamamagitan ng Microsoft Foundry [I-click ang link na ito](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bilang karagdagan sa Microsoft Foundry Models catalog na nakabase sa cloud, maaari mo ring gamitin ang [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) upang kumpletuhin ang mga kaugnay na tawag. Maaari mong bisitahin ang NVIDIA NIM upang gawin ang mga tawag sa API ng Pamilyang Phi-3/3.5. Ang NVIDIA NIM (NVIDIA Inference Microservices) ay isang hanay ng mga accelerated inference microservices na disenyo upang tulungan ang mga developer na i-deploy ang mga AI na modelo nang episyente sa iba't ibang mga kapaligiran, kabilang ang mga ulap, data center, at mga workstation.

Narito ang ilang mahahalagang katangian ng NVIDIA NIM:

- **Dali ng Deployment:** Pinapayagan ng NIM ang pag-deploy ng mga AI modelo gamit ang isang utos lamang, kaya madaling isa-integrate sa umiiral na mga workflow.
- **Optimized na Performance:** Ginagamit nito ang mga pre-optimized inference engines ng NVIDIA, tulad ng TensorRT at TensorRT-LLM, upang matiyak ang mababang latency at mataas na throughput.
- **Scalability:** Sinusuportahan ng NIM ang autoscaling sa Kubernetes, na nagbibigay-daan dito na mahusay na hawakan ang iba't ibang mga workload.
- **Seguridad at Kontrol:** Maaaring panatilihin ng mga organisasyon ang kontrol sa kanilang datos at mga aplikasyon sa pamamagitan ng self-hosting ng NIM microservices sa sariling pinamamahalaang imprastraktura.
- **Standard APIs:** Nagbibigay ang NIM ng mga standard na API sa industriya, na nagpapadali sa pagbuo at pag-integrate ng mga AI application tulad ng mga chatbot, AI assistant, at iba pa.

Bahagi ang NIM ng NVIDIA AI Enterprise, na naglalayong pasimplehin ang deployment at operasyonal ng mga AI models, na tinitiyak na tumatakbo ito nang mahusay sa NVIDIA GPUs.

- Demo: Paggamit ng NVIDIA NIM para tawagan ang Phi-3.5-Vision-API  [[I-click ang link na ito](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pagpapatakbo ng Phi-3/3.5 Locally
Ang inference kaugnay ng Phi-3, o anumang language model tulad ng GPT-3, ay tumutukoy sa proseso ng paggawa ng mga sagot o prediksyon batay sa input na natatanggap nito. Kapag nagbigay ka ng prompt o tanong sa Phi-3, ginagamit nito ang napag-aralang neural network upang ipahiwatig ang pinakamalamang at pinakaangkop na sagot sa pamamagitan ng pagsusuri ng mga pattern at relasyon sa data na pinag-aralan nito.

**Hugging Face Transformer**
Ang Hugging Face Transformers ay isang makapangyarihang library na dinisenyo para sa natural language processing (NLP) at iba pang mga gawain sa machine learning. Narito ang ilang mga pangunahing punto tungkol dito:

1. **Pretrained Models**: Nagbibigay ito ng libu-libong pretrained models na maaaring gamitin para sa iba't ibang gawain tulad ng text classification, named entity recognition, question answering, summarization, translation, at text generation.

2. **Framework Interoperability**: Sinusuportahan ng library ang maraming deep learning frameworks, kabilang ang PyTorch, TensorFlow, at JAX. Pinapayagan ka nitong mag-train ng modelo sa isang framework at gamitin ito sa iba.

3. **Multimodal Capabilities**: Bukod sa NLP, sinusuportahan ng Hugging Face Transformers ang mga gawain sa computer vision (hal. image classification, object detection) at audio processing (hal. speech recognition, audio classification).

4. **Ease of Use**: Nag-aalok ang library ng mga API at tools para madaling ma-download at ma-fine-tune ang mga modelo, na ginagawa itong accessible para sa parehong mga baguhan at eksperto.

5. **Community and Resources**: May buhay na komunidad ang Hugging Face at malawak na dokumentasyon, mga tutorial, at mga gabay upang tulungan ang mga gumagamit na makapagsimula at masulit ang library.
[opisyal na dokumentasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o kanilang [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ito ang pinaka-karaniwang ginagamit na paraan, ngunit nangangailangan din ito ng GPU acceleration. Sa katunayan, ang mga senaryo tulad ng Vision at MoE ay nangangailangan ng maraming kalkulasyon, na magiging mabagal sa CPU kung hindi ito na-quantize.


- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-Instruct [I-click ang link na ito](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-Vision [I-click ang link na ito](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-MoE [I-click ang link na ito](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ay isang platform na dinisenyo upang gawing mas madali ang pagpapatakbo ng malalaking language models (LLMs) nang lokal sa iyong makina. Sinasuportahan nito ang iba't ibang mga modelo tulad ng Llama 3.1, Phi 3, Mistral, at Gemma 2, bukod sa iba pa. Pinapasimple ng platform ang proseso sa pamamagitan ng pagsasama-sama ng mga timbang ng modelo, configuration, at data sa isang pakete, na ginagawa itong mas accessible para sa mga gumagamit na i-customize at gumawa ng sarili nilang mga modelo. Available ang Ollama para sa macOS, Linux, at Windows. Ito ay isang mahusay na tool kung nais mong mag-eksperimento o mag-deploy ng LLMs nang hindi umaasa sa mga cloud service. Ang Ollama ang pinaka-direktang paraan, kailangan mo lamang patakbuhin ang sumusunod na utos.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ay offline, on-device runtime ng Microsoft para patakbuhin ang mga modelo tulad ng Phi nang buong-buo sa iyong sariling hardware - hindi kailangan ng Azure subscription, API key, o koneksyon sa network. Awtomatikong pinipili nito ang pinakamahusay na execution provider na available (NPU, GPU, o CPU) at nag-eexpose ng OpenAI-compatible endpoint, kaya ang umiiral na `openai`/Azure AI Inference SDK code ay maaaring tumukoy dito nang may kaunting pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) upang makapagsimula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

O gamitin nang direkta ang SDK sa Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ay isang cross-platform na accelerator para sa inference at training ng machine-learning. Ang ONNX Runtime para sa Generative AI (GENAI) ay isang makapangyarihang tool na tumutulong sa iyo na patakbuhin nang mahusay ang mga generative AI models sa iba't ibang platform.

## Ano ang ONNX Runtime?
Ang ONNX Runtime ay isang open-source na proyekto na nagpapagana ng high-performance inference para sa mga machine learning models. Sinusuportahan nito ang mga modelo sa Open Neural Network Exchange (ONNX) format, na isang standard para sa pagre-representa ng mga machine learning models. Maaaring mag-enable ang ONNX Runtime inference ng mas mabilis na karanasan para sa customer at mas mababang gastos, sinusuportahan ang mga modelo mula sa mga deep learning frameworks gaya ng PyTorch at TensorFlow/Keras pati na rin ang mga klasikong machine learning libraries tulad ng scikit-learn, LightGBM, XGBoost, at iba pa. Compatible ang ONNX Runtime sa iba't ibang hardware, driver, at operating system, at nagbibigay ng pinakamainam na performance sa pamamagitan ng paggamit ng hardware accelerators kung saan angkop kasama ang graph optimizations at transforms.

## Ano ang Generative AI?
Ang Generative AI ay tumutukoy sa mga AI system na kayang lumikha ng bagong nilalaman, tulad ng teksto, mga imahe, o musika, batay sa data na pinag-aralan nila. Kabilang dito ang mga language models tulad ng GPT-3 at mga image generation models tulad ng Stable Diffusion. Nagbibigay ang ONNX Runtime para sa GenAI library ng generative AI loop para sa mga ONNX models, kabilang ang inference gamit ang ONNX Runtime, logits processing, search at sampling, at KV cache management.

## ONNX Runtime para sa GENAI
Pinalalawak ng ONNX Runtime para sa GENAI ang kakayahan ng ONNX Runtime upang suportahan ang mga generative AI models. Narito ang ilang pangunahing tampok:

- **Malawak na Suporta sa Platform:** Gumagana ito sa iba't ibang platform, kabilang ang Windows, Linux, macOS, Android, at iOS.
- **Suporta sa Modelo:** Sinuportahan nito ang maraming kilalang generative AI models, tulad ng LLaMA, GPT-Neo, BLOOM, at iba pa.
- **Optimization sa Performance:** May kasama itong mga optimization para sa iba’t ibang hardware accelerators tulad ng NVIDIA GPUs, AMD GPUs, at iba pa.
- **Dali ng Paggamit:** Nagbibigay ito ng mga API para madaling pag-integrate sa mga application, na nagpapahintulot sa iyo na gumawa ng teksto, mga imahe, at iba pang nilalaman gamit ang kaunting code.
- Maaaring tawagan ng mga user ang high level na generate() method, o patakbuhin ang bawat iteration ng modelo sa isang loop, na gumagawa ng isang token sa bawat oras, at opsyonal na ina-update ang mga generation parameters sa loob ng loop.
- May suporta rin ang ONNX runtime para sa greedy/beam search at TopP, TopK sampling upang makabuo ng mga token sequence at built-in logits processing tulad ng repetition penalties. Madali rin magdagdag ng custom scoring.

## Pagsisimula
Para makapagsimula gamit ang ONNX Runtime para sa GENAI, maaaring sundin ang mga hakbang na ito:

### I-install ang ONNX Runtime:
```Python
pip install onnxruntime
```
### I-install ang Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Patakbuhin ang Isang Modelo: Narito ang isang simpleng halimbawa sa Python:
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
### Demo:Paggamit ng ONNX Runtime GenAI para tawagan ang Phi-3.5-Vision


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

Bilang karagdagan sa mga reference methods ng ONNX Runtime, Ollama, at Foundry Local, maaari rin nating kumpletuhin ang reference ng quantitative models batay sa mga model reference methods na ibinigay ng iba't ibang tagagawa. Tulad ng Apple MLX framework gamit ang Apple Metal, Qualcomm QNN na may NPU, Intel OpenVINO sa CPU/GPU, atbp. Maaari ka ring kumuha ng higit pang nilalaman mula sa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Higit pa

Natutunan na natin ang mga batayan ng Phi-3/3.5 Family, ngunit para matuto pa tungkol sa SLM kailangan natin ng mas maraming kaalaman. Maaari mong makita ang mga sagot sa Phi-3 Cookbook. Kung nais mong matuto pa, bisitahin ang [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->