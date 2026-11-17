# Panimula sa Maliit na Modelo ng Wika para sa Generative AI para sa mga Nagsisimula
Ang Generative AI ay isang kahanga-hangang larangan ng artipisyal na intelihensiya na nakatuon sa paglikha ng mga sistemang may kakayahang bumuo ng bagong nilalaman. Ang nilalamang ito ay maaaring mula sa teksto at mga larawan hanggang sa musika at maging buong virtual na mga kapaligiran. Isa sa mga pinaka-kapanapanabik na aplikasyon ng generative AI ay nasa larangan ng mga modelo ng wika.

## Ano ang Maliit na Modelo ng Wika?

Ang Maliit na Modelo ng Wika (SLM) ay kumakatawan sa isang pinasimpleng bersyon ng malaking modelo ng wika (LLM), gamit ang maraming mga prinsipyo ng arkitektura at mga teknik ng LLM, habang nagpapakita ng mas mababang pangangailangan sa komputasyon.

Ang mga SLM ay isang subset ng mga modelo ng wika na idinisenyo upang bumuo ng tekstong parang tao. Hindi tulad ng kanilang mas malalaking kapareha, tulad ng GPT-4, ang mga SLM ay mas compact at mahusay, na ginagawang angkop para sa mga aplikasyon kung saan limitado ang mga mapagkukunan sa komputasyon. Sa kabila ng kanilang mas maliit na sukat, maaari pa rin silang magsagawa ng iba't ibang mga gawain. Karaniwan, ang mga SLM ay binubuo sa pamamagitan ng pag-compress o pag-distill ng mga LLM, na layuning mapanatili ang malaking bahagi ng orihinal na kakayahan at lingguwistikong kapasidad ng modelo. Ang pagbawas na ito sa laki ng modelo ay nagpapababa sa pangkalahatang kumplikasyon, kaya mas epektibo ang mga SLM sa paggamit ng memorya at mga pangangailangan sa komputasyon. Sa kabila ng mga optimisasyong ito, ang mga SLM ay maaari pa ring magsagawa ng malawak na hanay ng mga gawain sa natural na pagproseso ng wika (NLP):

- Paggawa ng Teksto: Paglikha ng magkakaugnay at kontekstwal na may kaugnayang mga pangungusap o talata.
- Pagkumpleto ng Teksto: Pagtataya at pagkumpleto ng mga pangungusap batay sa ibinigay na prompt.
- Pagsasalin: Paglilipat ng teksto mula sa isang wika patungo sa iba.
- Pagbubuod: Pagpapaikli ng mahahabang teksto sa mas maiksi at madaling unawain na mga buod.

Bagaman may ilang kapalit sa pagganap o lalim ng pag-unawa kumpara sa kanilang mas malalaking kampeon.

## Paano Gumagana ang Maliit na Modelo ng Wika?
Ang mga SLM ay sinasanay gamit ang napakaraming datos na teksto. Sa panahon ng pagsasanay, natututuhan nila ang mga pattern at estruktura ng wika, na nagbibigay-daan sa kanila upang bumuo ng teksto na parehong tama sa gramatika at naaayon sa konteksto. Kasama sa proseso ng pagsasanay ang:

- Pangangalap ng Datos: Pagkuha ng malalaking dataset ng teksto mula sa iba't ibang pinagmulan.
- Preprocessing: Paglilinis at pag-aayos ng datos upang maging angkop para sa pagsasanay.
- Pagsasanay: Paggamit ng mga algorithm ng machine learning upang turuan ang modelo kung paano maunawaan at bumuo ng teksto.
- Fine-Tuning: Pag-aayos ng modelo upang mapabuti ang pagganap nito sa mga partikular na gawain.

Ang pag-unlad ng mga SLM ay naaayon sa tumataas na pangangailangan para sa mga modelo na maaaring i-deploy sa mga environment na may limitadong resources, tulad ng mga mobile device o edge computing platform, kung saan maaaring hindi praktikal ang buong sukat na LLM dahil sa kanilang mabigat na pangangailangan ng mapagkukunan. Sa pamamagitan ng pagtutok sa kahusayan, balansihin ng mga SLM ang pagganap at accessibility, na nagbibigay-daan sa mas malawak na aplikasyon sa iba't ibang larangan.

![slm](../../../translated_images/tl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mga Layunin sa Pag-aaral

Sa araling ito, nais naming ipakilala ang kaalaman tungkol sa SLM at pag-ugnayin ito sa Microsoft Phi-3 upang matutunan ang iba't ibang mga senaryo sa nilalaman ng teksto, bisyon, at MoE.

Sa pagtatapos ng araling ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang SLM?
- Ano ang pagkakaiba ng SLM at LLM?
- Ano ang Microsoft Phi-3/3.5 Family?
- Paano patakbuhin ang inference gamit ang Microsoft Phi-3/3.5 Family?

Handa ka na ba? Magsimula na tayo.

## Mga Pagkakaiba ng Malalaking Modelo ng Wika (LLMs) at Maliit na Modelo ng Wika (SLMs)

Ang parehong LLMs at SLMs ay itinayo sa mga pundamental na prinsipyo ng probabilistic machine learning, sumusunod sa magkatulad na mga pamamaraan sa kanilang arkitektural na disenyo, mga metodolohiya sa pagsasanay, proseso ng pagbuo ng datos, at mga teknik sa pagsusuri ng modelo. Gayunpaman, may ilang mahahalagang salik na naghihiwalay sa dalawang uri ng modelo.

## Mga Aplikasyon ng Maliit na Modelo ng Wika

May malawak na hanay ng mga aplikasyon ang mga SLM, kabilang ang:

- Chatbots: Pagbibigay ng suporta sa customer at pakikipag-ugnayan sa mga gumagamit sa paraan ng pag-uusap.
- Paglikha ng Nilalaman: Pagtulong sa mga manunulat sa pamamagitan ng pagbuo ng mga ideya o kahit pag-draft ng buong mga artikulo.
- Edukasyon: Pagtulong sa mga estudyante sa mga pagsusulat na gawain o pag-aaral ng mga bagong wika.
- Accessibility: Paglikha ng mga kagamitan para sa mga taong may kapansanan, tulad ng mga sistema ng text-to-speech.

**Laki**
  
Ang pangunahing pagkakaiba ng LLM at SLM ay nasa sukat ng mga modelo. Ang mga LLM, tulad ng ChatGPT (GPT-4), ay maaaring magkaroon ng tinatayang 1.76 trillion na mga parameter, habang ang mga open-source na SLM tulad ng Mistral 7B ay idinisenyo na may mas kaunting mga parameter—mga tinatayang 7 bilyon. Ang pagkakaibang ito ay pangunahing sanhi ng pagkakaiba sa arkitektura ng modelo at mga proseso ng pagsasanay. Halimbawa, ang ChatGPT ay gumagamit ng self-attention mechanism sa loob ng encoder-decoder framework, samantalang ang Mistral 7B ay gumagamit ng sliding window attention, na nagpapahintulot ng mas epektibong pagsasanay sa loob ng decoder-only na modelo. Ang pagkakaibang ito sa arkitektura ay may malalim na epekto sa kumplikasyon at pagganap ng mga modelong ito.

**Pag-unawa**

Karaniwang ina-optimize ang mga SLM para sa pagganap sa mga partikular na domain, kaya napaka-especialista nila ngunit maaaring limitado ang kakayahan sa pagbibigay ng malawak na kontekstuwal na pag-unawa sa iba't ibang larangan ng kaalaman. Sa kabilang banda, nilalayon ng LLM na gayahin ang intelihensiya ng tao sa mas malawak na antas. Sa pagsasanay gamit ang malalawak at magkakaibang dataset, ang LLM ay idinisenyo upang magganap ng mahusay sa iba't ibang larangan, na nag-aalok ng mas malaking versatility at adaptability. Dahil dito, mas angkop ang LLM para sa mas malawak na hanay ng mga downstream na gawain, tulad ng natural language processing at programming.

**Pagkompyut**

Ang pagsasanay at pag-deploy ng mga LLM ay mga prosesong nangangailangan ng malaking mga mapagkukunan, madalas na nangangailangan ng malaking pampamprosesong imprastraktura, kabilang ang mga malalaking GPU clusters. Halimbawa, ang pagsasanay ng isang modelo tulad ng ChatGPT mula sa simula ay maaaring mangailangan ng libu-libong GPUs sa loob ng mahabang panahon. Sa kabilang banda, ang mga SLM, na may mas maliit na bilang ng mga parameter, ay mas madaling ma-access sa mga mapagkukunan ng komputasyon. Ang mga modelong tulad ng Mistral 7B ay maaaring sanayin at patakbuhin sa mga lokal na makina na may katamtamang kakayahan sa GPU, kahit na ang pagsasanay ay nangangailangan pa rin ng ilang oras gamit ang maramihan na GPUs.

**Bias**

Ang bias ay isang kilalang isyu sa LLMs, pangunahing dahil sa uri ng datos na ginamit sa pagsasanay. Madalas na umaasa ang mga modelong ito sa hilaw, bukas na datos mula sa internet, na maaaring hindi sapat ang representasyon o hindi makatwiran ang paglalarawan sa ilang mga grupo, magpasok ng maling pag-label, o magpakita ng lingguwistikong bias na naapektuhan ng diyalekto, heograpikal na mga pagbabago, at mga patakaran sa gramatika. Bukod dito, ang komplikasyon ng arkitektura ng LLM ay maaaring hindi sinasadyang magpalala ng bias, na maaaring hindi mapansin nang walang masusing fine-tuning. Sa kabilang banda, ang mga SLM, bilang mga sinanay sa mas limitadong, domain-specific na dataset, ay likas na hindi gaanong madaling maapektuhan ng ganitong bias, bagaman hindi sila immune dito.

**Inference**

Ang mas maliit na sukat ng mga SLM ay nagbibigay sa kanila ng malaking kalamangan sa bilis ng inference, na nagpapahintulot sa kanila na bumuo ng output nang mabilis sa lokal na hardware nang hindi nangangailangan ng malawakang parallel processing. Sa kabilang banda, ang mga LLM, dahil sa kanilang laki at kumplikasyon, ay madalas na nangangailangan ng malaking mga parallel computational resources upang makamit ang katanggap-tanggap na mga oras ng inference. Ang pagdami ng sabay-sabay na mga gumagamit ay lalo pang nagpapabagal sa oras ng pagtugon ng LLM, lalo na kapag in-deploy sa malaking sukat.

Sa kabuuan, habang pareho ang LLMs at SLMs na may pundamental na batayan sa machine learning, malaki ang kanilang pagkakaiba sa laki ng modelo, pangangailangan sa mga mapagkukunan, kontekstwal na pag-unawa, pagiging sensitibo sa bias, at bilis ng inference. Ang mga pagkakaibang ito ay nagpapakita ng kanilang kani-kaniyang angkop na gamit, kung saan ang LLMs ay mas versatile ngunit mabigat sa resources, habang ang SLMs ay nag-aalok ng mas domain-specific na kahusayan na may pinababang mga pangangailangan sa komputasyon.

***Tandaan: Sa araling ito, ipapakilala namin ang SLM gamit ang Microsoft Phi-3 / 3.5 bilang halimbawa.***

## Ipakilala ang Phi-3 / Phi-3.5 Family

Ang Phi-3 / 3.5 Family ay pangunahing naglalayong mga senaryo ng aplikasyon sa teksto, bisyon, at Ahente (MoE):

### Phi-3 / 3.5 Instruct

Pangunahing para sa paggawa ng teksto, pagkumpleto ng chat, at pagkuha ng impormasyon sa nilalaman, at iba pa.

**Phi-3-mini**

Ang 3.8B na modelo ng wika ay available sa Microsoft Foundry, Hugging Face, at Ollama. Ang mga modelo ng Phi-3 ay malaki ang nalalampasan sa performance kumpara sa ibang mga modelo ng parehong laki at mas malalaki sa mga pangunahing benchmark (tingnan ang mga numero ng benchmark sa ibaba, mas mataas na numero ay mas maganda). Ang Phi-3-mini ay nalalampasan ang mga modelo na doble ang laki nito, habang ang Phi-3-small at Phi-3-medium ay nalalampasan ang mas malalaking modelo, kabilang ang GPT-3.5.

**Phi-3-small at medium**

Sa 7B parameters lamang, ang Phi-3-small ay nalalampasan ang GPT-3.5T sa iba't ibang benchmark sa wika, pangangatwiran, coding, at matematika.

Ang Phi-3-medium na may 14B parameters ay ipinagpapatuloy ang trend na ito at nalalampasan ang Gemini 1.0 Pro.

**Phi-3.5-mini**

Maaari natin itong isipin bilang upgrade ng Phi-3-mini. Habang nananatili ang mga parameter, pinapabuti nito ang kakayahang suportahan ang maraming wika (sumusuporta sa 20+ na mga wika: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​at nagdaragdag ng mas malakas na suporta para sa mahabang konteksto.

Ang Phi-3.5-mini na may 3.8B parameters ay nalalampasan ang mga modelo ng parehong laki at katumbas ng mga modelo na doble ang laki nito.

### Phi-3 / 3.5 Vision

Maaari nating isipin ang Instruct model ng Phi-3/3.5 bilang kakayahan ng Phi na umunawa, at ang Vision ang nagbibigay ng mga mata kay Phi para maintindihan ang mundo.


**Phi-3-Vision**

Ang Phi-3-vision, na may 4.2B parameters lamang, ay nagpapatuloy sa trend na ito at nalalampasan ang mas malalaking modelo tulad ng Claude-3 Haiku at Gemini 1.0 Pro V sa mga pangkalahatang gawain sa visual reasoning, OCR, at ang pag-unawa sa mga table at diagram.


**Phi-3.5-Vision**

Ang Phi-3.5-Vision ay isa ring upgrade ng Phi-3-Vision, na nagdaragdag ng suporta para sa maramihang mga imahe. Maaari mo itong isipin bilang pagpapabuti sa bisyon, hindi lang ito kakakita ng mga larawan kundi pati na rin ng mga video.

Ang Phi-3.5-vision ay nalalampasan ang mas malalaking modelo tulad ng Claude-3.5 Sonnet at Gemini 1.5 Flash sa OCR, pag-unawa sa mga table at chart na mga gawain at kapantay sa pangkalahatang mga gawain ng visual knowledge reasoning. Sinusuportahan nito ang multi-frame input, ibig sabihin ay maaaring magsagawa ng pangangatwiran sa maraming mga imahe bilang input.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ay nagbibigay-daan sa mga modelo na maisanay gamit ang mas kaunting compute, na nangangahulugang maaari mong malakiang pataasin ang laki ng modelo o dataset gamit ang parehong compute budget kumpara sa isang dense na modelo. Partikular, ang isang MoE na modelo ay dapat makamit ang parehong kalidad ng dense counterpart nito nang mas mabilis sa panahon ng pretraining.

Ang Phi-3.5-MoE ay binubuo ng 16x3.8B expert modules. Ang Phi-3.5-MoE na may 6.6B aktibong mga parameter ay nakakamit ng katulad na antas ng pangangatwiran, pag-unawa sa wika, at matematika tulad ng mas malalaking modelo.

Maaari nating gamitin ang modelo ng Phi-3/3.5 Family base sa iba't ibang mga senaryo. Hindi tulad ng LLM, maaari mong i-deploy ang Phi-3/3.5-mini o Phi-3/3.5-Vision sa mga edge device.


## Paano gamitin ang mga modelo ng Phi-3/3.5 Family

Nais naming gamitin ang Phi-3/3.5 sa iba't ibang mga senaryo. Susunod, gagamitin namin ang Phi-3/3.5 base sa iba't ibang mga senaryo.

![phi3](../../../translated_images/tl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inference gamit ang Cloud APIs

**Microsoft Foundry Models**

> **Tandaan:** Ang GitHub Models ay magtatapos sa katapusan ng Hulyo 2026. Ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ang direktang kapalit.

> **Tandaan:** Ang buong Phi-3/3.5 family (Instruct, Vision, at MoE variants) ay tinigilan mula sa katalogo ng Microsoft Foundry Models noong 2025-08-30. Gamitin ang `Phi-4` (Instruct) o `Phi-4-mini-instruct` doon bilang kapalit — ang mga halimbawa ng Phi-3/3.5 sa ibaba ay gumagana pa rin sa pamamagitan ng Hugging Face, Ollama, ONNX Runtime, at NVIDIA NIM.

Nagbibigay na ngayon ang Microsoft Foundry Models ng mga kahalili na Phi-4. Gamitin ang `Phi-4` o `Phi-4-mini-instruct` bilang kapalit ng mga retired na modelo ng Phi-3/3.5 kapag sumusunod sa mga halimbawa ng cloud API.

- Demo: Paghahambing ng mga epekto ng Phi-3-mini at Phi-3.5-mini sa mga senaryo sa Chinese

![phi3](../../../translated_images/tl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/tl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Kung nais mong gamitin ang mga vision (multimodal) na modelo sa cloud, gamitin ang kasalukuyang available na `Phi-4-multimodal-instruct` sa pamamagitan ng Microsoft Foundry sa halip na ang retired na Phi-3/3.5 Vision models; para sa mga gawain sa teksto, gamitin ang `Phi-4` o `Phi-4-mini-instruct`. Ang Phi-3.5 MoE na modelo ay tinigil na mula sa Microsoft Foundry, kaya gamitin ang iba pang mga opsyon na inilarawan sa araling ito (halimbawa Hugging Face) kung nais mong subukan ito. Kung interesado ka, maaari mong basahin ang Phi Cookbook upang matutunan kung paano tawagan ang mga Phi models sa pamamagitan ng Microsoft Foundry [I-click ang link na ito](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bukod sa cloud-based Microsoft Foundry Models catalog, maaari mo ring gamitin ang [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) upang kumpletuhin ang mga kaugnay na tawag. Maaari mong bisitahin ang NVIDIA NIM upang matapos ang mga API calls ng Phi-3/3.5 Family. Ang NVIDIA NIM (NVIDIA Inference Microservices) ay isang set ng mga pinalakas na inference microservices na dinisenyo upang tulungan ang mga developer na mag-deploy ng mga AI modelo nang mahusay sa iba't ibang environment, kabilang ang mga cloud, data centers, at workstations.

Narito ang ilang mga pangunahing tampok ng NVIDIA NIM:

- **Daliang Deployment:** Pinapayagan ng NIM ang deployment ng mga AI model sa iisang utos, na ginagawang madali itong isama sa mga umiiral na workflow.
- **Pinahusay na Performance:** Ginagamit nito ang NVIDIA’s pre-optimized inference engines, tulad ng TensorRT at TensorRT-LLM, upang matiyak ang mababang latency at mataas na throughput.
- **Scalability:** Sinusuportahan ng NIM ang autoscaling sa Kubernetes, na nagpapahintulot dito na mahusay na hawakan ang iba't ibang workload.
- **Seguridad at Kontrol:** Maaaring panatilihin ng mga organisasyon ang kontrol sa kanilang data at mga aplikasyon sa pamamagitan ng self-hosting ng NIM microservices sa kanilang sariling pinamamahalaang imprastraktura.
- **Standard APIs:** Nagbibigay ang NIM ng mga industry-standard na API, na nagpapadali sa pagbuo at pagsasama ng mga AI application tulad ng mga chatbot, AI assistant, at iba pa.

Bahagi ang NIM ng NVIDIA AI Enterprise, na naglalayong pasimplehin ang deployment at operationalization ng mga AI model, na tinitiyak na tumatakbo sila nang mahusay sa NVIDIA GPUs.

- Demo: Paggamit ng NVIDIA NIM para tawagan ang Phi-3.5-Vision-API  [[I-click ang link na ito](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pagpatakbo ng Phi-3/3.5 Nang Lokal
Ang inference kaugnay ng Phi-3, o anumang language model tulad ng GPT-3, ay tumutukoy sa proseso ng pagbuo ng mga tugon o prediksyon batay sa input na natanggap nito. Kapag nagbigay ka ng prompt o tanong sa Phi-3, ginagamit nito ang na-train na neural network nito upang mahinuha ang pinaka-posible at may kaugnayang tugon sa pamamagitan ng pagsusuri sa mga pattern at relasyon sa data na pinag-aralan nito.

**Hugging Face Transformer**
Ang Hugging Face Transformers ay isang makapangyarihang library na dinisenyo para sa natural language processing (NLP) at iba pang mga gawain sa machine learning. Narito ang ilang mahahalagang punto tungkol dito:

1. **Pretrained Models**: Nagbibigay ito ng libu-libong pretrained na mga modelo na maaaring gamitin para sa iba't ibang gawain gaya ng text classification, named entity recognition, question answering, summarization, translation, at text generation.

2. **Framework Interoperability**: Sinusuportahan ng library ang maraming deep learning framework, kabilang ang PyTorch, TensorFlow, at JAX. Pinapayagan ka nitong i-train ang isang modelo sa isang framework at gamitin ito sa iba.

3. **Multimodal Capabilities**: Bukod sa NLP, sinusuportahan din ng Hugging Face Transformers ang mga gawain sa computer vision (hal., image classification, object detection) at audio processing (hal., speech recognition, audio classification).

4. **Daliang Gamitin**: Nagbibigay ang library ng mga API at tool para madaliang i-download at i-fine-tune ang mga modelo, kaya ito ay naa-access para sa mga nagsisimula at eksperto.

5. **Komunidad at Mga Mapagkukunan**: May masiglang komunidad ang Hugging Face pati na rin malawak na dokumentasyon, mga tutorial, at gabay upang tulungan ang mga gumagamit na magsimula at magamit nang husto ang librarya.
[opisyal na dokumentasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o ang kanilang [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ito ang pinaka-karaniwang paraan, ngunit kailangan din ito ng GPU acceleration. Sa katunayan, ang mga scenario tulad ng Vision at MoE ay nangangailangan ng maraming kalkulasyon, na magiging napakabagal sa CPU kung hindi naka-quantize.


- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-Instruct [I-click ang link na ito](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-Vision [I-click ang link na ito](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer para tawagan ang Phi-3.5-MoE [I-click ang link na ito](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ay isang platform na nilikha upang gawing mas madali ang pagpapatakbo ng mga malalaking language models (LLMs) nang lokal sa iyong makina. Sinusuportahan nito ang iba't ibang modelo tulad ng Llama 3.1, Phi 3, Mistral, at Gemma 2, atbp. Pinapasimple ng platform ang proseso sa pamamagitan ng pag-bundle ng model weights, configuration, at data sa isang pakete, na ginagawang mas accessible para sa mga gumagamit na i-customize at lumikha ng kanilang sariling mga modelo. Available ang Ollama para sa macOS, Linux, at Windows. Isang mahusay na kagamitan ito kung nais mong mag-eksperimento o mag-deploy ng LLM nang hindi umaasa sa mga cloud service. Ang Ollama ang pinaka-direktang paraan, kailangan mo lang patakbuhin ang sumusunod na command.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ay offline, on-device runtime ng Microsoft para sa pagpapatakbo ng mga model tulad ng Phi nang buo sa iyong sariling hardware - hindi kailangan ng Azure subscription, API key, o koneksyon sa network. Awtomatikong pinipili nito ang pinakamainam na execution provider na magagamit (NPU, GPU, o CPU) at naglalabas ng OpenAI-compatible endpoint, kaya ang umiiral na `openai`/Azure AI Inference SDK code ay maaaring gumamit dito nang may minimal na pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) upang magsimula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

O kaya ay gamitin ang SDK nang direkta sa Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime para sa GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ay isang cross-platform inference at training machine-learning accelerator. Ang ONNX Runtime para sa Generative AI (GENAI) ay isang makapangyarihang tool na tumutulong na patakbuhin nang mahusay ang mga generative AI model sa iba't ibang platform.

## Ano ang ONNX Runtime?
Ang ONNX Runtime ay isang open-source na proyekto na nagbibigay-daan sa high-performance inference ng mga machine learning model. Sinusuportahan nito ang mga modelo sa Open Neural Network Exchange (ONNX) na format, na isang pamantayan para sa representasyon ng mga machine learning model. Ang ONNX Runtime inference ay maaaring mag-enable ng mas mabilis na karanasan ng customer at mas mababang gastos, sinusuportahan ang mga modelo mula sa deep learning framework tulad ng PyTorch at TensorFlow/Keras pati na rin sa mga klasikong machine learning library tulad ng scikit-learn, LightGBM, XGBoost, atbp. Compatible ang ONNX Runtime sa iba't ibang hardware, driver, at operating system, at nagbibigay ng optimal na performance sa pamamagitan ng paggamit ng hardware accelerators kung saan angkop kasabay ng graph optimizations at transforms.

## Ano ang Generative AI?
Ang Generative AI ay tumutukoy sa mga sistema ng AI na makakalikha ng bagong nilalaman, tulad ng teksto, larawan, o musika, batay sa data kung saan sila na-train. Mga halimbawa nito ay mga language model tulad ng GPT-3 at mga modelong naggagawa ng larawan tulad ng Stable Diffusion. Nagbibigay ang ONNX Runtime para sa GenAI library ng generative AI loop para sa ONNX models, kabilang ang inference gamit ang ONNX Runtime, logits processing, paghahanap at sampling, at KV cache management.

## ONNX Runtime para sa GENAI
Pinalalawak ng ONNX Runtime para sa GENAI ang kakayahan ng ONNX Runtime upang suportahan ang generative AI models. Narito ang ilang mahahalagang katangian:

- **Malawak na Suporta sa Platform:** Gumagana ito sa iba't ibang platform, kabilang ang Windows, Linux, macOS, Android, at iOS.
- **Suporta sa Modelo:** Sinusuportahan nito ang maraming sikat na generative AI models, tulad ng LLaMA, GPT-Neo, BLOOM, at iba pa.
- **Pag-optimize ng Performance:** Kabilang dito ang mga optimisasyon para sa iba't ibang hardware accelerators tulad ng NVIDIA GPUs, AMD GPUs, at iba pa.
- **Daliang Gamitin:** Nagbibigay ito ng mga API para sa madaling pagsasama sa mga aplikasyon, na nagpapahintulot sa iyo na bumuo ng teksto, larawan, at iba pang nilalaman nang may kaunting code.
- Maaaring tawagan ng mga user ang mataas na antas na generate() method, o patakbuhin ang bawat iterasyon ng modelo sa isang loop, na nag-generate ng isang token sa bawat pagkakataon, at opsyonal na ina-update ang mga generation parameters sa loob ng loop.
- Suportado rin ng ONNX runtime ang greedy/beam search at TopP, TopK sampling upang bumuo ng mga token sequence at may built-in na logits processing tulad ng repetition penalties. Maaari ka ring magdagdag ng custom scoring nang madali.

## Paano Magsimula
Upang magsimula sa ONNX Runtime para sa GENAI, maaari mong sundan ang mga hakbang na ito:

### I-install ang ONNX Runtime:
```Python
pip install onnxruntime
```
### I-install ang Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Patakbuhin ang isang Modelo: Narito ang isang simpleng halimbawa sa Python:
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


**Iba Pa**

Bukod sa ONNX Runtime, Ollama, at Foundry Local na mga reference method, maaari rin nating kumpletuhin ang listahan ng quantitative models batay sa mga model reference methods na ibinigay ng iba't ibang mga gumawa. Tulad ng Apple MLX framework gamit ang Apple Metal, Qualcomm QNN gamit ang NPU, Intel OpenVINO gamit ang CPU/GPU, at iba pa. Maaari ka ring makakuha ng karagdagang nilalaman mula sa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Higit Pa

Natutunan na natin ang mga batayan ng Phi-3/3.5 Family, ngunit upang matutunan pa ang SLM kailangan pa ng mas maraming kaalaman. Makikita mo ang mga sagot sa Phi-3 Cookbook. Kung nais mong matuto pa, bisitahin ang [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->