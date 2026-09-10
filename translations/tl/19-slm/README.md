# Panimula sa Maliit na Language Models para sa Generative AI para sa mga Baguhan
Ang Generative AI ay isang kahanga-hangang larangan ng artificial intelligence na nakatuon sa paggawa ng mga sistema na kayang lumikha ng bagong nilalaman. Ang nilalamang ito ay maaaring mula sa teksto at mga larawan hanggang sa musika at kahit buong virtual na mga kapaligiran. Isa sa mga pinaka kapana-panabik na aplikasyon ng generative AI ay nasa larangan ng mga language models.

## Ano ang Maliit na Language Models?

Ang Maliit na Language Model (SLM) ay kumakatawan sa pinaikling bersyon ng isang malaking language model (LLM), na ginagamit ang maraming prinsipyo at teknik ng arkitektura ng LLM, ngunit may mas maliit na computational footprint.

Ang mga SLM ay isang subset ng mga language models na dinisenyo upang lumikha ng tekstong katulad ng sa tao. Hindi tulad ng kanilang mas malalaking katapat, tulad ng GPT-4, ang mga SLM ay mas compact at mahusay, kaya't perpekto sila para sa mga aplikasyon kung saan limitado ang computational resources. Sa kabila ng kanilang maliit na sukat, kaya pa rin nilang gumanap ng iba't ibang mga gawain. Karaniwang ginagawa ang mga SLM sa pamamagitan ng pag-compress o pag-distill ng mga LLM, na layuning panatilihin ang malaking bahagi ng orihinal na kakayahan at kasanayan sa wika ng modelo. Ang pagbawas na ito sa laki ng modelo ay nagpapababa sa kabuuang pagiging kumplikado, kaya't mas mahusay ang mga SLM sa paggamit ng memorya at computational requirements. Sa kabila ng mga optimisasyong ito, ang mga SLM ay kayang magsagawa ng malawak na hanay ng mga gawain sa natural language processing (NLP):

- Pagbuo ng Teksto: Paggawa ng magkakaugnay at kontekstwal na mga pangungusap o talata.
- Pagkumpleto ng Teksto: Pagtataya at pagkompleto ng mga pangungusap batay sa ibinigay na prompt.
- Pagsasalin: Paglilipat ng teksto mula sa isang wika patungo sa iba.
- Pagbubuod: Pagbubuod ng mahahabang bahagi ng teksto sa mas maikli at madaling maintindihan na buod.

Bagaman may ilang kapalit sa pagganap o lalim ng pag-unawa kumpara sa kanilang mas malalaking katapat.

## Paano Gumagana ang Maliit na Language Models?
Ang mga SLM ay sinasanay gamit ang malaking dami ng data ng teksto. Sa panahon ng pagsasanay, natututuhan nila ang mga pattern at estruktura ng wika, na nagpapahintulot sa kanila na bumuo ng teksto na parehong tama sa gramatika at naaangkop sa konteksto. Ang proseso ng pagsasanay ay kinabibilangan ng:

- Pangangalap ng Data: Pangongolekta ng malalaking dataset ng teksto mula sa iba't ibang pinagkukunan.
- Preprocessing: Paglilinis at pag-aayos ng data upang maging angkop ito para sa pagsasanay.
- Pagsasanay: Paggamit ng mga machine learning algorithm upang turuan ang modelo kung paano unawain at bumuo ng teksto.
- Fine-Tuning: Pag-aayos ng modelo upang mapabuti ang pagganap nito sa mga espesipikong gawain.

Ang pagbuo ng mga SLM ay naaayon sa pagtaas ng pangangailangan para sa mga modelo na maaaring gamitin sa mga environment na may limitadong resources, tulad ng mga mobile na aparato o edge computing platforms, kung saan ang malalaking LLM ay maaaring hindi praktikal dahil sa kanilang matinding pangangailangan sa resources. Sa pamamagitan ng pagtutok sa kahusayan, pinagbabalanse ng mga SLM ang pagganap at accessibility, na nagpapahintulot ng mas malawak na aplikasyon sa iba't ibang larangan.

![slm](../../../translated_images/tl/slm.4058842744d0444a.webp)

## Mga Layunin sa Pagkatuto

Sa leksyon na ito, layunin naming ipakilala ang kaalaman tungkol sa SLM at pagsamahin ito sa Microsoft Phi-3 upang matutunan ang iba't ibang senaryo sa nilalaman ng teksto, bisyon, at MoE.

Sa pagtatapos ng leksyon na ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang SLM?
- Ano ang pagkakaiba ng SLM at LLM?
- Ano ang Microsoft Phi-3/3.5 Family?
- Paano magpatakbo ng inference gamit ang Microsoft Phi-3/3.5 Family?

Handa ka na ba? Magsimula tayo.

## Ang Pagkakaiba sa Pagitan ng Malalaking Language Models (LLMs) at Maliit na Language Models (SLMs)

Parehong ang LLMs at SLMs ay itinayo sa mga pangunahing prinsipyong probabilistic machine learning, sumusunod sa magkakatulad na pamamaraan sa arkitekturang disenyo, metodolohiya ng pagsasanay, proseso ng pagbuo ng data, at mga teknik sa pagsusuri ng modelo. Gayunpaman, may ilang mahahalagang salik na nagkakaiba sa dalawang uri ng mga modelong ito.

## Mga Aplikasyon ng Maliit na Language Models

Ang mga SLMs ay may malawak na hanay ng mga aplikasyon, kabilang ang:

- Mga Chatbots: Pagbibigay ng customer support at pakikipag-ugnayan sa mga user sa paraan ng pag-uusap.
- Paglikha ng Nilalaman: Pagtulong sa mga manunulat sa pagbuo ng mga ideya o kahit pagsulat ng buong artikulo.
- Edukasyon: Pagtulong sa mga estudyante sa mga sulatin o pag-aaral ng mga bagong wika.
- Accessibility: Paglikha ng mga kasangkapan para sa mga may kapansanan, tulad ng mga text-to-speech system.

**Sukat**
  
Isang pangunahing pagkakaiba sa pagitan ng LLMs at SLMs ay ang sukat ng mga modelo. Ang mga LLM tulad ng ChatGPT (GPT-4) ay maaaring magkaroon ng tinatayang 1.76 trilyong parameters, habang ang open-source na mga SLM tulad ng Mistral 7B ay dinisenyo na may makabuluhang mas kaunting parameters—mga humigit-kumulang 7 bilyon. Ang pagkakaibang ito ay pangunahing dulot ng kaibahan sa arkitektura ng modelo at mga proseso ng pagsasanay. Halimbawa, ang ChatGPT ay gumagamit ng self-attention mechanism sa loob ng encoder-decoder framework, samantalang ang Mistral 7B ay gumagamit ng sliding window attention, na nagpapahintulot ng mas mahusay na pagsasanay sa loob ng decoder-only na modelo. Ang pagkakaibang arkitekturang ito ay may malalim na epekto sa pagiging komplikado at pagganap ng mga modelong ito.

**Pag-unawa**

Kadalasan, ang mga SLM ay ini-optimize para sa pagganap sa espesipikong mga domain, kaya't sila ay lubos na espesyalista ngunit maaaring limitado sa kanilang kakayahang magbigay ng malawak na kontekstwal na pag-unawa sa maramihang larangan ng kaalaman. Sa kabilang banda, ang mga LLM ay naglalayong gayahin ang katalinuhan ng tao sa isang mas komprehensibong antas. Sinusubukan sa malalaking, magkakaibang dataset, ang mga LLM ay dinisenyo upang magpakita ng mahusay na pagganap sa iba't ibang larangan, na nag-aalok ng mas mataas na versatility at adaptability. Dahil dito, ang mga LLM ay mas angkop para sa mas malawak na hanay ng mga gawain, tulad ng natural language processing at programming.

**Pagpoproseso**

Ang pagsasanay at deployment ng mga LLM ay nangangailangan ng malaking resources, madalas na nangangailangan ng makabuluhang computational infrastructure, kabilang ang malalaking GPU cluster. Halimbawa, ang pagsasanay ng modelong tulad ng ChatGPT mula sa simula ay maaaring mangailangan ng libu-libong GPUs sa mahabang panahon. Sa kabilang banda, ang mga SLM, sa mas maliit nilang bilang ng parameters, ay mas madaling ma-access pagdating sa computational resources. Ang mga modelong tulad ng Mistral 7B ay maaaring sanayin at patakbuhin sa mga lokal na makina na may katamtamang kakayahan sa GPU, bagaman nangangailangan pa rin ang pagsasanay ng ilang oras gamit ang maramihang GPUs.

**Bias**

Ang bias ay isang kilalang isyu sa mga LLM, pangunahing dahil sa likas na katangian ng data sa pagsasanay. Madalas na umaasa ang mga modelong ito sa raw, bukas na data mula sa internet, na maaaring hindi kumakatawan nang maayos o nagkakaroon ng maling representasyon sa ilang grupo, naglalaman ng maling paglalarawan, o nagre-reflect ng lingguwistikong bias na naaapektuhan ng diyalekto, pagkakaiba-iba ng heograpiya, at mga patakaran sa gramatika. Bukod dito, ang pagiging komplikado ng arkitektura ng LLM ay maaaring hindi sinasadyang magpalala ng bias, na maaaring hindi mapansin nang hindi maingat na fine-tuning. Sa kabilang banda, ang mga SLM, na sinasanay sa mas limitadong, espesipikong datasets, ay likas na mas hindi madaling maapektuhan ng mga ganitong bias, bagaman hindi sila ganap na immune dito.

**Paghinuha (Inference)**

Ang maliit na sukat ng mga SLM ay nagbibigay sa kanila ng malaking kalamangan pagdating sa bilis ng inference, na nagpapahintulot na mabilis silang makabuo ng output sa lokal na hardware nang hindi nangangailangan ng malawakang parallel processing. Sa kabilang banda, ang mga LLM, dahil sa laki at pagiging komplikado, ay madalas na nangangailangan ng malalaking parallel computational resources upang makamit ang tinatanggap na oras ng inference. Ang pagkakaroon ng maraming sabay-sabay na gumagamit ay lalo pang nagpapabagal sa oras ng tugon ng mga LLM, lalo na kapag ginagamit sa malaking saklaw.

Sa kabuuan, habang parehong nakabase sa machine learning ang LLMs at SLMs, malaki ang pagkakaiba nila sa laki ng modelo, pangangailangan sa resources, antas ng pag-unawa sa konteksto, pagiging sensitibo sa bias, at bilis ng inference. Ang mga pagkakaibang ito ay nagpapakita ng angkop nilang paggamit sa iba't ibang sitwasyon, kung saan ang LLMs ay mas versatile ngunit mabigat sa resources, at ang SLMs ay nag-aalok ng mas episyenteng pagganap sa espesipikong domain na may mas mababang demand sa computational.

***Tandaan: Sa leksyong ito, ipakikilala natin ang SLM gamit ang Microsoft Phi-3 / 3.5 bilang halimbawa.***

## Ipinakikilala ang Phi-3 / Phi-3.5 Family

Ang Phi-3 / 3.5 Family ay pangunahing nakatuon sa mga senaryo ng aplikasyon sa teksto, bisyon, at Agent (MoE):

### Phi-3 / 3.5 Instruct

Pangunahing para sa pagbuo ng teksto, pagkompleto ng chat, at pagkuha ng impormasyon ng nilalaman, atbp.

**Phi-3-mini**

Ang 3.8B language model ay available sa Microsoft Foundry, Hugging Face, at Ollama. Ang mga Phi-3 na modelo ay malaki ang pag-ungos sa mga language model na may pantay at mas malalaking sukat sa mga pangunahing benchmark (tingnan ang mga numero sa benchmark sa ibaba, mas mataas ang numero mas maganda). Ang Phi-3-mini ay naihahambing ang pagganap sa mga modelo na doble ang laki nito, habang ang Phi-3-small at Phi-3-medium ay lumalampas sa mga mas malalaking modelo, kabilang ang GPT-3.5.

**Phi-3-small at medium**

Sa 7B na parameters lamang, ang Phi-3-small ay nalalampasan ang GPT-3.5T sa iba't ibang benchmarks sa wika, pangangatwiran, coding, at matematika.

Ang Phi-3-medium na may 14B na parameters ay nagpapatuloy sa trend na ito at nalalampasan ang Gemini 1.0 Pro.

**Phi-3.5-mini**

Maaaring isipin natin ito bilang upgrade ng Phi-3-mini. Bagama't hindi nagbago ang parameters, pinapabuti nito ang kakayahang suportahan ang maraming wika (sumusuporta sa 20+ na wika: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) at nagdaragdag ng mas malakas na suporta para sa mahabang konteksto.

Ang Phi-3.5-mini na may 3.8B parameters ay nalalampasan ang mga language model na may parehong laki at kapantay ng mga modelo na doble ang laki nito.

### Phi-3 / 3.5 Vision

Maaaring isipin natin ang Instruct na modelo ng Phi-3/3.5 bilang kakayahan ni Phi na unawain, at ang Vision ang nagbibigay kay Phi ng mga mata upang maintindihan ang mundo.


**Phi-3-Vision**

Ang Phi-3-vision, na may 4.2B parameters lamang, ay nagpapatuloy sa trend na ito at nalalampasan ang mas malalaking modelo tulad ng Claude-3 Haiku at Gemini 1.0 Pro V sa mga pangkalahatang gawain sa visual reasoning, OCR, at pag-unawa sa mga talahanayan at diagram.


**Phi-3.5-Vision**

Ang Phi-3.5-Vision ay isang upgrade din ng Phi-3-Vision, na nagdaragdag ng suporta para sa maraming mga larawan. Maaaring isipin ito bilang pagpapabuti sa vision; hindi lamang makakakita ka ng mga larawan, kundi pati ng mga video.

Ang Phi-3.5-vision ay nalalampasan ang mas malalaking modelo tulad ng Claude-3.5 Sonnet at Gemini 1.5 Flash sa OCR, pag-unawa sa mga talahanayan at tsart, at kapantay sa mga pangkalahatang gawain sa visual knowledge reasoning. Suportado ang multi-frame input, ibig sabihin, kayang magsagawa ng pangangatwiran sa maraming input na larawan.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ay nagpapahintulot sa mga modelo na ma-pretrain gamit ang mas kaunting compute, na ibig sabihin, maaari mong lubos na palakihin ang laki ng modelo o dataset gamit ang parehong compute budget tulad ng isang dense model. Partikular, ang isang MoE model ay dapat makamit ang parehong kalidad tulad ng dense counterpart nito nang mas mabilis sa panahon ng pretraining.

Ang Phi-3.5-MoE ay binubuo ng 16x3.8B expert modules. Ang Phi-3.5-MoE na may 6.6B active parameters lamang ay nakakamit ng katulad na antas ng pangangatwiran, pag-unawa sa wika, at matematika tulad ng mas malalaking modelo.

Maaari nating gamitin ang modelo ng Phi-3/3.5 Family batay sa iba't ibang senaryo. Hindi tulad ng LLM, maaari mong i-deploy ang Phi-3/3.5-mini o Phi-3/3.5-Vision sa mga edge device.


## Paano Gamitin ang Phi-3/3.5 Family models

Nais naming gamitin ang Phi-3/3.5 sa iba't ibang senaryo. Susunod, gagamit tayo ng Phi-3/3.5 batay sa iba't ibang senaryo.

![phi3](../../../translated_images/tl/phi3.655208c3186ae381.webp)

### Paghinuha gamit ang Cloud APIs

**Microsoft Foundry Models**

> **Tandaan:** Ang GitHub Models ay magtatapos sa katapusan ng Hulyo 2026. Ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ang direktang kapalit nito.

Ang Microsoft Foundry Models ang pinaka-direktang paraan. Maaari mong mabilis na ma-access ang Phi-3/3.5-Instruct model sa pamamagitan ng Foundry model catalog. Pinaghalo sa Azure AI Inference SDK / OpenAI SDK, maaari mong ma-access ang API sa pamamagitan ng code upang matapos ang tawag sa Phi-3/3.5-Instruct. Maaari ka ring mag-test ng iba't ibang epekto gamit ang Playground.

- Demo: Paghahambing ng mga epekto ng Phi-3-mini at Phi-3.5-mini sa mga senaryong Tsino

![phi3](../../../translated_images/tl/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/tl/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

O kung nais nating gamitin ang mga vision at MoE na modelo, maaari mong gamitin ang Microsoft Foundry upang matapos ang tawag. Kung interesado ka, maaari mong basahin ang Phi-3 Cookbook upang matutunan kung paano tawagan ang Phi-3/3.5 Instruct, Vision, MoE sa pamamagitan ng Microsoft Foundry [I-click ang link na ito](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bukod sa cloud-based na Microsoft Foundry Models catalog, maaari mo ring gamitin ang [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para matapos ang mga kaugnay na tawag. Maaari mong bisitahin ang NVIDIA NIM upang tapusin ang API calls ng Phi-3/3.5 Family. Ang NVIDIA NIM (NVIDIA Inference Microservices) ay isang set ng mga pinalakas na microservices na inference na nilikha upang tulungan ang mga developer na mag-deploy ng AI models nang episyente sa iba't ibang environment, kabilang ang mga cloud, data centers, at workstations.

Narito ang ilang mahahalagang tampok ng NVIDIA NIM:

- **Kadaling Deployment:** Pinapahintulutan ng NIM ang deployment ng mga AI model gamit ang isang utos lamang, na ginagawang madali itong isama sa umiiral na mga workflow.

- **Optimizadong Pagganap:** Ginagamit nito ang mga na-pre-optimize na inference engines ng NVIDIA, tulad ng TensorRT at TensorRT-LLM, upang matiyak ang mababang latency at mataas na throughput.
- **Scalability:** Sinusuportahan ng NIM ang autoscaling sa Kubernetes, na nagpapahintulot dito na mahusay na hawakan ang iba't ibang workload.
- **Seguridad at Kontrol:** Maaaring panatilihin ng mga organisasyon ang kontrol sa kanilang data at mga aplikasyon sa pamamagitan ng self-hosting ng mga NIM microservices sa kanilang sariling pinamamahalaang imprastruktura.
- **Standard APIs:** Nagbibigay ang NIM ng mga industry-standard na API, na nagpapadali sa paggawa at integrasyon ng mga AI application tulad ng chatbots, AI assistants, at iba pa.

Bahagi ang NIM ng NVIDIA AI Enterprise, na naglalayong gawing simple ang deployment at operationalization ng mga AI model, na tinitiyak na tumatakbo nang mahusay ang mga ito sa NVIDIA GPUs.

- Demo: Paggamit ng NVIDIA NIM upang tawagan ang Phi-3.5-Vision-API  [[I-click ang link na ito](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pagpapatakbo ng Phi-3/3.5 Nang Lokal
Ang inference kaugnay sa Phi-3, o anumang language model tulad ng GPT-3, ay tumutukoy sa proseso ng pagbuo ng mga tugon o prediksyon base sa input na natatanggap nito. Kapag nagbigay ka ng prompt o tanong sa Phi-3, ginagamit nito ang sinanay nitong neural network upang himayin ang mga pattern at relasyon sa data na pinag-aralan nito para mahulaan ang pinaka-malamang at nauugnay na sagot.

**Hugging Face Transformer**
Ang Hugging Face Transformers ay isang makapangyarihang library na idinisenyo para sa natural language processing (NLP) at iba pang mga gawain sa machine learning. Narito ang ilang mahahalagang punto tungkol dito:

1. **Mga Pretrained Model**: Nagbibigay ito ng libu-libong pretrained models na maaaring magamit sa iba't ibang gawain tulad ng text classification, named entity recognition, question answering, summarization, translation, at text generation.

2. **Interoperability ng Framework**: Sinusuportahan ng library ang maraming deep learning framework, kabilang ang PyTorch, TensorFlow, at JAX. Pinapayagan ka nitong mag-train ng model sa isang framework at gamitin ito sa iba.

3. **Multimodal na Kakayahan**: Bukod sa NLP, sinusuportahan din ng Hugging Face Transformers ang mga gawain sa computer vision (hal., image classification, object detection) at audio processing (hal., speech recognition, audio classification).

4. **Kadaling Gamitin**: Nagbibigay ang library ng mga API at tools upang madaling ma-download at ma-fine tune ang mga model, kaya't naa-access ito para sa mga baguhan at eksperto.

5. **Komunidad at Mga Mapagkukunan**: May buhay na komunidad ang Hugging Face at malawak na dokumentasyon, mga tutorial, at gabay para tulungan ang mga user na makapagsimula at magamit nang husto ang library.
[opisyal na dokumentasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o ang kanilang [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ito ang pinaka-karaniwang ginagamit na paraan, ngunit nangangailangan din ito ng GPU acceleration. Sa katunayan, ang mga senaryo tulad ng Vision at MoE ay nangangailangan ng maraming kalkulasyon, na magiging napakabagal sa CPU kung hindi ito naka-quantize.


- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Instruct [I-click ang link na ito](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Vision [I-click ang link na ito](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-MoE [I-click ang link na ito](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ay isang platform na idinisenyo upang gawing mas madali ang pagpapatakbo ng malalaking language model (LLMs) nang lokal sa iyong makina. Sinusuportahan nito ang iba't ibang modelo tulad ng Llama 3.1, Phi 3, Mistral, at Gemma 2, at iba pa. Pinadadali ng platform ang proseso sa pamamagitan ng pagsasama-sama ng model weights, configuration, at data sa isang package, kaya mas naa-access ito para sa mga user na i-customize at gumawa ng sarili nilang mga modelo. Available ang Ollama para sa macOS, Linux, at Windows. Ito ay isang mahusay na tool kung nais mong mag-eksperimento o mag-deploy ng LLM nang hindi umaasa sa mga cloud service. Ang Ollama ang pinaka-direktang paraan, kailangan mo lang patakbuhin ang sumusunod na utos.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ay ang offline, on-device runtime ng Microsoft para patakbuhin ang mga modelo tulad ng Phi nang buo sa iyong sariling hardware - hindi kailangan ang Azure subscription, API key, o koneksyon sa network. Awtomatikong pinipili nito ang pinakamahusay na execution provider na available (NPU, GPU, o CPU) at naglalabas ng OpenAI-compatible na endpoint, kaya ang umiiral na code ng `openai`/Azure AI Inference SDK ay pwedeng ituro dito nang may minimal na pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para magsimula.

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

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ay isang cross-platform inference at training machine-learning accelerator. Ang ONNX Runtime para sa Generative AI (GENAI) ay isang makapangyarihang tool na tumutulong sa'yo na patakbuhin nang mahusay ang mga generative AI model sa iba't ibang platform.

## Ano ang ONNX Runtime?
Ang ONNX Runtime ay isang open-source na proyekto na nagpapagana ng mataas na performance na inference ng mga machine learning model. Sinusuportahan nito ang mga model sa Open Neural Network Exchange (ONNX) format, na isang standard para sa representasyon ng mga machine learning model. Maaaring magbigay ang ONNX Runtime inference ng mas mabilis na karanasan para sa customer at mas mababang gastos, sinusuportahan ang mga model mula sa mga deep learning framework tulad ng PyTorch at TensorFlow/Keras pati na rin ang mga klasikal na machine learning library tulad ng scikit-learn, LightGBM, XGBoost, at iba pa. Ang ONNX Runtime ay compatible sa iba't ibang hardware, drivers, at mga operating system, at nagbibigay ng optimal na performance sa pamamagitan ng paggamit ng hardware accelerators kapag naaangkop kasabay ng mga graph optimizations at transforms.

## Ano ang Generative AI?
Ang Generative AI ay tumutukoy sa mga AI system na makakalikha ng bagong nilalaman, tulad ng teksto, mga larawan, o musika, base sa data na pinag-aralan nila. Mga halimbawa nito ang mga language model tulad ng GPT-3 at mga image generation model tulad ng Stable Diffusion. Nagbibigay ang ONNX Runtime para sa GenAI library ng generative AI loop para sa ONNX models, kabilang ang inference gamit ang ONNX Runtime, logits processing, search at sampling, at KV cache management.

## ONNX Runtime para sa GENAI
Pinalalawak ng ONNX Runtime para sa GENAI ang kakayahan ng ONNX Runtime upang suportahan ang mga generative AI model. Narito ang ilang pangunahing tampok:

- **Malawak na Suporta sa Platform:** Gumagana ito sa iba't ibang platform, kabilang ang Windows, Linux, macOS, Android, at iOS.
- **Suporta sa Model:** Sinusuportahan nito ang maraming kilalang generative AI model, tulad ng LLaMA, GPT-Neo, BLOOM, at iba pa.
- **Optimization sa Pagganap:** Kasama dito ang optimizations para sa iba't ibang hardware accelerators tulad ng NVIDIA GPUs, AMD GPUs, at iba pa.
- **Kadaling Gamitin:** Nagbibigay ito ng mga API para sa madaling integrasyon sa mga aplikasi, na nagpapahintulot sa iyo na gumawa ng teksto, larawan, at iba pang nilalaman gamit ang minimal na code.
- Maaaring tawagan ng mga user ang mataas na antas na generate() na method, o patakbuhin ang bawat pag-ikot ng model sa isang loop, na bumubuo ng isang token kada pagkakataon, at opsyonal na ina-update ang mga generation parameter sa loob ng loop.
- May suporta rin ang ONNX runtime para sa greedy/beam search at TopP, TopK sampling upang makalikha ng mga token sequence at built-in na logits processing tulad ng repetition penalties. Madali ka ring makakapagdagdag ng custom scoring.

## Pagsisimula
Para makapagsimula sa ONNX Runtime para sa GENAI, maaari mong sundan ang mga hakbang na ito:

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

Bilang karagdagan sa ONNX Runtime, Ollama, at Foundry Local na mga reference method, maaari rin nating kumpletuhin ang reference ng mga quantitative model base sa mga model reference method na ibinigay ng iba't ibang manufacturer. Tulad ng Apple MLX framework gamit ang Apple Metal, Qualcomm QNN gamit ang NPU, Intel OpenVINO gamit ang CPU/GPU, atbp. Maaari ka ring kumuha ng karagdagang nilalaman mula sa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Marami Pa

Natutunan na natin ang mga batayan ng Phi-3/3.5 Family, ngunit upang matuto pa tungkol sa SLM kailangan natin ng mas marami pang kaalaman. Makikita mo ang mga sagot sa Phi-3 Cookbook. Kung nais mong matuto pa, mangyaring bisitahin ang [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->