# Panimula sa Maliit na Mga Modelong Pangwika para sa Generative AI para sa mga Nagsisimula
Ang Generative AI ay isang kamangha-manghang larangan ng artipisyal na intelihensiya na nakatuon sa paglikha ng mga sistemang may kakayahang bumuo ng bagong nilalaman. Ang nilalaman na ito ay maaaring mula sa teksto at mga larawan hanggang sa musika at maging mga buong virtual na kapaligiran. Isa sa mga pinaka kapana-panabik na aplikasyon ng generative AI ay sa larangan ng mga modelong pangwika.

## Ano ang Maliit na Mga Modelong Pangwika?

Ang Maliit na Modelong Pangwika (Small Language Model o SLM) ay kumakatawan sa isang pinaikling bersyon ng isang malaking modelong pangwika (Large Language Model o LLM), na gumagamit ng marami sa mga prinsipyo ng arkitektura at mga teknik ng LLMs, habang nagpapakita ng mas mababang gamit sa komputasyon.

Ang mga SLM ay isang bahagi ng mga modelong pangwika na dinisenyo upang bumuo ng tekstong parang tao. Hindi tulad ng kanilang mas malalaking katapat, tulad ng GPT-4, ang mga SLM ay mas maliit at mas epektibo, kaya't mainam para sa mga aplikasyon kung saan limitado ang mga mapagkukunan ng komputasyon. Sa kabila ng kanilang mas maliit na sukat, kaya pa rin nilang magsagawa ng iba't ibang gawain. Karaniwang ginagawa ang mga SLM sa pamamagitan ng pag-compress o pag-distill ng mga LLM na may layuning mapanatili ang malaking bahagi ng orihinal na kakayahan at kasanayan sa wika ng modelo. Ang pagbawas sa laki ng modelo ay nagpapababa sa kabuuang kumplikasyon, kaya't mas epektibo ang mga SLM sa paggamit ng memorya at pangangailangang pampagkompyut. Sa kabila ng mga optimisasyon na ito, kaya pa ring gawin ng SLM ang malawak na hanay ng mga gawain sa pagproseso ng natural na wika (NLP):

- Pagbuo ng Teksto: Paglikha ng magkakaugnay at kontekstwal na mga pangungusap o talata.
- Pagtatapos ng Teksto: Pagtataya at pagtatapos ng mga pangungusap batay sa isang naibigay na simula.
- Pagsasalin: Paglilipat ng teksto mula sa isang wika patungo sa iba.
- Pagbubuod: Pagpapaikli ng mahahabang teksto upang maging mas madaling unawain na mga buod.

Bagaman may ilang pagkakaiba sa pagganap o lalim ng pag-unawa kumpara sa kanilang mas malalaking katapat.

## Paano Gumagana ang Maliit na Mga Modelong Pangwika?
Ang mga SLM ay sinasanay gamit ang napakaraming halaga ng datos ng teksto. Sa panahon ng pagsasanay, natututuhan nila ang mga pattern at estruktura ng wika, na nagpapahintulot sa kanila na makabuo ng teksto na tama sa gramatika at angkop sa konteksto. Ang proseso ng pagsasanay ay kinabibilangan ng:

- Pangongolekta ng Datos: Pangangalap ng malawak na mga dataset ng teksto mula sa iba't ibang pinagkukunan.
- Preprocessing: Paglilinis at pag-aayos ng datos upang maging angkop para sa pagsasanay.
- Pagsasanay: Paggamit ng mga algorithm ng machine learning para turuan ang modelo kung paano intindihin at bumuo ng teksto.
- Fine-Tuning: Pagsasaayos ng modelo upang mapabuti ang pagganap nito sa mga partikular na gawain.

Ang pagbuo ng mga SLM ay naaayon sa lumalaking pangangailangan para sa mga modelong maaaring gamitin sa mga kapaligirang may limitadong mapagkukunan, tulad ng mga mobile device o mga edge computing platform, kung saan ang buong LLM ay maaaring hindi praktikal dahil sa sobrang pangangailangan sa mapagkukunan. Sa pagtutok sa kahusayan, pinagsasama ng mga SLM ang pagganap at accessibility, na nagpapahintulot ng mas malawak na aplikasyon sa iba't ibang larangan.

![slm](../../../translated_images/tl/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Mga Layunin sa Pagkatuto

Sa araling ito, nais naming ipakilala ang kaalaman tungkol sa SLM at pagtambalin ito sa Microsoft Phi-3 upang matutunan ang iba't ibang senaryo sa nilalaman ng teksto, paningin, at MoE.

Sa pagtatapos ng araling ito, inaasahan mong masasagot ang mga sumusunod na tanong:

- Ano ang SLM?
- Ano ang pagkakaiba ng SLM at LLM?
- Ano ang Pamilya ng Microsoft Phi-3/3.5?
- Paano magpatakbo ng inference gamit ang Pamilya ng Microsoft Phi-3/3.5?

Handa ka na ba? Magsimula na tayo.

## Ang Mga Pagkakaiba sa pagitan ng Malalaking Modelong Pangwika (LLMs) at Maliit na Modelong Pangwika (SLMs)

Parehong nakabatay ang LLMs at SLMs sa mga pundamental na prinsipyo ng probabilistic machine learning, sumusunod sa magkatulad na mga pamamaraan sa kanilang disenyo ng arkitektura, metodolohiyang pang-pagsasanay, mga proseso ng pagbuo ng datos, at mga teknik sa pagsusuri ng modelo. Ngunit may ilang pangunahing mga aspeto na nagkakaiba sa dalawang uri ng mga modelo na ito.

## Mga Aplikasyon ng Maliit na Mga Modelong Pangwika

Malawak ang gamit ng mga SLM, kabilang ang:

- Chatbots: Pagsuporta sa mga customer at pakikipag-usap sa mga gumagamit sa isang panauhing paraan.
- Paglikha ng Nilalaman: Pagtulong sa mga manunulat sa pamamagitan ng pagbuo ng mga ideya o kahit pagsusulat ng buong artikulo.
- Edukasyon: Pagtulong sa mga estudyante sa mga asignaturang pagsulat o pag-aaral ng mga bagong wika.
- Accessibility: Paggawa ng mga kasangkapan para sa mga indibidwal na may kapansanan, tulad ng mga sistema ng teksto-sa-talata.

**Sukat**
  
Isang pangunahing pagkakaiba sa pagitan ng LLMs at SLMs ay nasa sukat ng mga modelo. Ang LLMs, tulad ng ChatGPT (GPT-4), ay maaaring magkaroon ng tinatayang 1.76 trilyong mga parameter, habang ang mga open-source na SLMs gaya ng Mistral 7B ay dinisenyo na may mas kaunting mga parameter—mga humigit-kumulang 7 bilyon. Ang pagkakaibang ito ay pangunahin dahil sa mga kaibahan sa arkitektura ng modelo at proseso ng pagsasanay. Halimbawa, gumagamit ang ChatGPT ng self-attention mechanism sa loob ng encoder-decoder framework, samantalang gumagamit ang Mistral 7B ng sliding window attention, na nagpapahintulot ng mas epektibong pagsasanay sa loob ng isang decoder-only model. Ang pagkakaibang arkitekturang ito ay may malalim na implikasyon para sa kumplikasyon at pagganap ng mga modelong ito.

**Pag-unawa**

Karaniwang naka-optimize ang mga SLM para sa pagganap sa mga partikular na larangan, kaya't sila ay sobrang espesyalisado ngunit maaaring limitado ang kanilang kakayahan na magbigay ng malawakang kontekstwal na pag-unawa sa iba't ibang larangan ng kaalaman. Sa kabaligtaran, nilalayon ng mga LLM na tularan ang intelihensiya ng tao sa mas malawak na antas. Sinanay sa malawak at magkakaibang mga dataset, ang mga LLM ay dinisenyo upang gumana nang mabuti sa iba't ibang larangan, na nagbibigay ng mas mataas na versatility at adaptability. Dahil dito, mas angkop ang mga LLM para sa mas malawak na hanay ng mga gawain tulad ng natural language processing at programming.

**Komputasyon**

Ang pagsasanay at paggamit ng mga LLM ay mga prosesong nangangailangan ng malaking mapagkukunan, madalas na nangangailangan ng malalaking pasilidad ng komputasyon, kabilang ang malawakang GPU clusters. Halimbawa, ang pagsasanay ng modelong tulad ng ChatGPT mula sa simula ay maaaring mangailangan ng libu-libong GPU sa mahabang panahon. Sa kabilang banda, ang mga SLM, dahil sa mas kaunting bilang ng mga parameter, ay mas madaling ma-access sa usapin ng mapagkukunang pangkompyut. Ang mga modelong tulad ng Mistral 7B ay maaaring sanayin at patakbuhin sa mga lokal na makina na may katamtamang GPU capabilities, bagaman nangangailangan pa rin ng ilang oras ang pagsasanay sa maraming GPUs.

**Pagkiling (Bias)**

Kilala ang bias sa mga LLM, pangunahing dahil sa kalikasan ng datos ng pagsasanay. Madalas silang umaasa sa mga hilaw at bukas na datos mula sa internet, na maaaring hindi ganap na kumakatawan o maling kumakatawan sa ilang mga grupo, nagdudulot ng maling label, o nagpapakita ng mga lingguwistikong pagkiling na naaapektuhan ng diyalekto, heograpikong pagkakaiba, at mga panuntunan sa gramatika. Bukod dito, maaaring hindi sinasadyang mapalala ng kumplikadong arkitektura ng LLM ang bias, na maaaring hindi mapansin nang walang maingat na fine-tuning. Sa kabilang banda, ang mga SLM, na sinasanay sa mas limitadong, espesipikong mga dataset, ay likas na mas mababa ang posibilidad na maapektuhan ng ganitong mga bias, kahit na hindi sila ganap na ligtas dito.

**Inference**

Ang mas maliit na sukat ng mga SLM ay nagbibigay sa kanila ng malaking kalamangan sa bilis ng inference, na nagpapahintulot na mabilis silang makapag-produce ng output sa lokal na hardware nang hindi nangangailangan ng malawakang parallel processing. Sa kabaligtaran, ang mga LLM ay dahil sa kanilang laki at kumplikasyon, ay madalas na nangangailangan ng malaking mga paralel na mapagkukunan ng komputasyon upang makamit ang katanggap-tanggap na oras ng inference. Ang pagdami ng mga sabay-sabay na gumagamit ay lalo pang nagpapabagal ng tugon ng LLM, lalo na kapag ginagamit sa malawakang sukat.

Sa kabuuan, habang parehong nakabase ang LLMs at SLMs sa pundasyon ng machine learning, malaki ang kanilang pagkakaiba sa sukat ng modelo, pangangailangan sa mapagkukunan, pampagkontextong pag-unawa, pagkasensitibo sa bias, at bilis ng inference. Ang mga pagkakaibang ito ay nagpapakita ng kani-kanilang angkop na gamit para sa iba’t ibang mga kaso, kung saan ang LLMs ay mas versatile ngunit mabigat sa mapagkukunan, at ang SLMs naman ay nag-aalok ng mas espesipikong kahusayan na may mas mababang pangangailangan sa komputasyon.

***Tandaan: Sa araling ito, ipakikilala namin ang SLM gamit ang Microsoft Phi-3 / 3.5 bilang halimbawa.***

## Ipakilala ang Pamilya ng Phi-3 / Phi-3.5

Pangunahing tinatarget ng Pamilya ng Phi-3 / 3.5 ang mga senaryo ng aplikasyon sa teksto, paningin, at Agent (MoE):

### Phi-3 / 3.5 Instruct

Pangunahing para sa pagbuo ng teksto, pagtatapos ng chat, at pagkuha ng impormasyon sa nilalaman, atbp.

**Phi-3-mini**

Ang 3.8B na modelong pangwika ay available sa Microsoft Foundry, Hugging Face, at Ollama. Malaki ang kalamangan ng mga modelo ng Phi-3 kumpara sa mga modelong pantay o mas malaki ang sukat sa mga pangunahing benchmark (tingnan ang mga numero ng benchmark sa ibaba, mas mataas ang numero ay mas maganda). Naipapasa ng Phi-3-mini ang mga modelong doble ang laki nito, habang ang Phi-3-small at Phi-3-medium ay lampas pa sa mga mas malalaking modelo, kabilang ang GPT-3.5.

**Phi-3-small at medium**

Sa 7B parameter lamang, nilalagpasan ng Phi-3-small ang GPT-3.5T sa iba't ibang mga benchmark sa wika, pangangatwiran, coding, at matematika.

Ang Phi-3-medium na may 14B na mga parameter ay nagpapatuloy sa trend na ito at nilalagpasan ang Gemini 1.0 Pro.

**Phi-3.5-mini**

Maaari natin itong isipin bilang isang upgrade ng Phi-3-mini. Habang nananatiling pareho ang mga parameter, pinabubuti nito ang kakayahan na suportahan ang maraming wika (sumusuporta sa 20+ na mga wika: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) at nagdaragdag ng mas malakas na suporta para sa mahahabang konteksto.

Ang Phi-3.5-mini na may 3.8B na mga parameter ay nilalampasan ang mga modelong may parehong laki at katumbas ng mga modelong doble ang laki.

### Phi-3 / 3.5 Vision

Maaari nating isipin ang Instruct model ng Phi-3/3.5 bilang kakayahan ng Phi na maintindihan, at ang Vision ay nagbibigay ng mga mata kay Phi upang maunawaan ang mundo.


**Phi-3-Vision**

Ang Phi-3-vision, na may 4.2B parameter lamang, ay nagpapatuloy sa trend na ito at nilalampasan ang mga mas malalaking modelo tulad ng Claude-3 Haiku at Gemini 1.0 Pro V sa mga pangkalahatang gawain sa visual reasoning, OCR, at pag-unawa sa mga talahanayan at diagram.


**Phi-3.5-Vision**

Ang Phi-3.5-Vision ay isang upgrade rin ng Phi-3-Vision, na nagdaragdag ng suporta para sa maraming mga larawan. Maaari mo itong isipin bilang isang pagpapabuti sa paningin, hindi lamang ikaw ay makakakita ng mga larawan, pati na rin mga video.

Nilalampasan ng Phi-3.5-vision ang mga mas malalaking modelo tulad ng Claude-3.5 Sonnet at Gemini 1.5 Flash sa OCR, pag-unawa ng talahanayan at tsart, at katumbas sa mga pangkalahatang gawain sa visual na kaalaman at pangangatwiran. Sinusuportahan ang multi-frame input, ibig sabihin ay gumagawa ng pangangatwiran sa maramihang input na mga larawan.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** ay nagpapahintulot sa mga modelo na ma-pretrain gamit ang mas kaunting compute, na nangangahulugang maaari mong taasan nang malaki ang laki ng modelo o dataset gamit ang parehong budget ng compute tulad ng isang dense na modelo. Sa partikular, ang isang MoE na modelo ay dapat makamit ang parehong kalidad ng dense counterpart nito nang mas mabilis sa panahon ng pretraining.

Ang Phi-3.5-MoE ay binubuo ng 16x3.8B na mga expert module. Ang Phi-3.5-MoE na may 6.6B lamang na aktibong parameter ay nakakamit ng katulad na antas ng pangangatwiran, pag-unawa sa wika, at matematika tulad ng mas malalaking mga modelo.

Maaari nating gamitin ang modelo ng Pamilya ng Phi-3/3.5 base sa iba't ibang mga senaryo. Hindi tulad ng LLM, maaari mong i-deploy ang Phi-3/3.5-mini o Phi-3/3.5-Vision sa mga edge device.


## Paano Gamitin ang mga Modelong Pamilya ng Phi-3/3.5

Nais naming gamitin ang Phi-3/3.5 sa iba't ibang mga senaryo. Susunod, gagamitin namin ang Phi-3/3.5 base sa iba’t ibang mga senaryo.

![phi3](../../../translated_images/tl/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Pagsusuri gamit ang Cloud API

**Mga Modelo ng Microsoft Foundry**

> **Tandaan:** Magwawakas na ang GitHub Models sa katapusan ng Hulyo 2026. Ang [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) ang direktang kapalit.

> **Tandaan:** Ang buong pamilya ng Phi-3/3.5 (Instruct, Vision, at MoE variant) ay inalis na mula sa katalogo ng Microsoft Foundry Models noong 2025-08-30. Gamitin ang `Phi-4` (Instruct) o `Phi-4-mini-instruct` bilang kapalit — ang mga halimbawa ng Phi-3/3.5 sa ibaba ay gumagana pa rin sa pamamagitan ng Hugging Face, Ollama, ONNX Runtime, at NVIDIA NIM.

Ngayon ay nagbibigay ang Microsoft Foundry Models ng mga kahalili na Phi-4. Gamitin ang `Phi-4` o `Phi-4-mini-instruct` bilang kapalit ng mga na-retiring na Phi-3/3.5 na modelo kapag sinusundan ang mga halimbawa ng cloud API.

- Demo: Paghahambing ng mga epekto ng Phi-3-mini at Phi-3.5-mini sa mga senaryo sa Chinese

![phi3](../../../translated_images/tl/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/tl/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

Kung nais mong gumamit ng vision (multimodal) na mga modelo sa cloud, gamitin ang kasalukuyang magagamit na `Phi-4-multimodal-instruct` sa pamamagitan ng Microsoft Foundry bilang kapalit ng na-retiring na Phi-3/3.5 Vision models; para sa mga gawain sa teksto, gamitin ang `Phi-4` o `Phi-4-mini-instruct`. Ang Phi-3.5 MoE modelo ay na-retire na mula sa Microsoft Foundry, kaya gamitin ang ibang mga opsyon na inilarawan sa araling ito (halimbawa Hugging Face) kung nais mong mag-eksperimento dito. Kung interesado ka, maaari mong basahin ang Phi Cookbook upang matutunan kung paano tawagan ang mga Phi models sa pamamagitan ng Microsoft Foundry [I-click ang link na ito](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Bilang karagdagan sa cloud-based na katalogo ng Microsoft Foundry Models, maaari mo ring gamitin ang [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) upang maisagawa ang mga kaugnay na tawag. Maaari mong bisitahin ang NVIDIA NIM upang kumpletuhin ang mga API calls ng Pamilya ng Phi-3/3.5. Ang NVIDIA NIM (NVIDIA Inference Microservices) ay isang set ng mga pinalakas na inference microservices na dinisenyo upang tulungan ang mga developer na epektibong i-deploy ang AI models sa iba't ibang mga kapaligiran, kabilang ang mga cloud, data centers, at workstations.

Narito ang ilang mga pangunahing tampok ng NVIDIA NIM:

- **Kadaling I-deploy:** Pinapayagan ng NIM ang deployment ng mga AI na modelo gamit ang isang utos lamang, na nagpapadali upang maisama sa mga umiiral na workflow.
- **Na-optimize na Pagganap:** Ginagamit nito ang mga pre-optimized inference engines ng NVIDIA, tulad ng TensorRT at TensorRT-LLM, upang matiyak ang mababang latency at mataas na throughput.
- **Scalability:** Sinusuportahan ng NIM ang autoscaling sa Kubernetes, na nagpapahintulot dito na mahusay na hawakan ang iba't ibang workload.
- **Seguridad at Kontrol:** Maaaring panatilihin ng mga organisasyon ang kontrol sa kanilang data at mga aplikasyon sa pamamagitan ng self-hosting ng mga microservices ng NIM sa kanilang sariling pinamamahalaang imprastraktura.
- **Standard APIs:** Nagbibigay ang NIM ng mga industry-standard na API, na nagpapadali upang bumuo at magsama ng mga AI na aplikasyon tulad ng mga chatbot, AI assistant, at iba pa.

Bahagi ang NIM ng NVIDIA AI Enterprise, na naglalayong gawing simple ang deployment at operationalization ng mga AI na modelo, na tinitiyak na tumatakbo nang mahusay sa NVIDIA GPUs.

- Demo: Paggamit ng NVIDIA NIM upang tawagan ang Phi-3.5-Vision-API  [[I-click ang link na ito](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Pagpapatakbo ng Phi-3/3.5 nang Lokal
Ang Inference kaugnay sa Phi-3, o anumang language model tulad ng GPT-3, ay tumutukoy sa proseso ng pagbuo ng mga tugon o prediksyon base sa input na natatanggap nito. Kapag nagbigay ka ng prompt o tanong sa Phi-3, ginagamit nito ang na-train na neural network upang mahinuha ang pinaka-malamang at may kaugnayang tugon sa pamamagitan ng pagsusuri sa mga pattern at ugnayan sa data na pinag-aralan nito.

**Hugging Face Transformer**
Ang Hugging Face Transformers ay isang makapangyarihang library na dinisenyo para sa natural language processing (NLP) at iba pang machine learning na gawain. Narito ang ilang mahahalagang punto tungkol dito:

1. **Pretrained Models**: Nagbibigay ito ng libu-libong pretrained models na maaaring gamitin para sa iba't ibang gawain tulad ng text classification, named entity recognition, question answering, summarization, translation, at text generation.

2. **Framework Interoperability**: Sinusuportahan ng library ang maraming deep learning frameworks, kabilang ang PyTorch, TensorFlow, at JAX. Pinapayagan ka nitong mag-train ng modelo sa isang framework at gamitin ito sa iba.

3. **Multimodal Capabilities**: Bukod sa NLP, sinusuportahan din ng Hugging Face Transformers ang mga gawain sa computer vision (hal., image classification, object detection) at audio processing (hal., speech recognition, audio classification).

4. **Kadaling Gamitin**: Nag-aalok ang library ng mga API at kagamitan upang madaling mag-download at mag-fine-tune ng mga modelo, kaya accessible ito sa parehong mga baguhan at eksperto.

5. **Komunidad at Mga Mapagkukunan**: May buhay na komunidad ang Hugging Face at malawak na dokumentasyon, tutorials, at mga gabay upang matulungan ang mga gumagamit na makapagsimula at magamit nang husto ang library.
[opisyal na dokumentasyon](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o ang kanilang [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Ito ang pinaka-karaniwang ginagamit na pamamaraan, ngunit kailangan din nito ng GPU acceleration. Sa katunayan, ang mga senaryo tulad ng Vision at MoE ay nangangailangan ng maraming kalkulasyon, kaya magiging napakabagal ito sa CPU kung hindi ito naka-quantize.


- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Instruct [I-click ang link na ito](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-Vision [I-click ang link na ito](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Paggamit ng Transformer upang tawagan ang Phi-3.5-MoE [I-click ang link na ito](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) ay isang plataporma na dinisenyo upang gawing mas madali ang pagpapatakbo ng malalaking language model (LLMs) nang lokal sa iyong makina. Sinusuportahan nito ang iba't ibang modelo tulad ng Llama 3.1, Phi 3, Mistral, at Gemma 2, bukod sa iba pa. Pinapasimple ng plataporma ang proseso sa pamamagitan ng pagbubuklod ng model weights, configuration, at data sa isang package, kaya mas madali para sa mga gumagamit na i-customize at gumawa ng sariling mga modelo. Available ang Ollama para sa macOS, Linux, at Windows. Ito ay isang mahusay na kasangkapan kung nais mong magsubok o mag-deploy ng LLMs nang hindi umaasa sa mga cloud service. Ang Ollama ang pinaka-direktang paraan, kailangan mo lamang patakbuhin ang sumusunod na command.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) ay offline, on-device runtime ng Microsoft para patakbuhin ang mga modelo tulad ng Phi nang buong lokal sa iyong sariling hardware - walang kailangan na Azure subscription, API key, o koneksyon sa network. Awtomatikong pinipili nito ang pinakamahusay na execution provider na available (NPU, GPU, o CPU) at nagpapakita ng OpenAI-compatible na endpoint, kaya ang umiiral na `openai`/Azure AI Inference SDK code ay maaaring ituro dito nang minimal lang ang mga pagbabago. Tingnan ang [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) upang makapagsimula.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

O gamitin ang SDK nang diretso sa Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime para sa GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) ay isang cross-platform inference at training machine-learning accelerator. ONNX Runtime para sa Generative AI (GENAI) ay isang makapangyarihang kasangkapan na tumutulong sa iyo na patakbuhin nang mahusay ang mga generative AI models sa iba't ibang mga platform.

## Ano ang ONNX Runtime?
Ang ONNX Runtime ay isang open-source na proyekto na nagpapagana ng high-performance inference ng mga machine learning models. Sinusuportahan nito ang mga modelo sa format na Open Neural Network Exchange (ONNX), na isang pamantayan para sa pagrepresenta ng mga machine learning models. Ang ONNX Runtime inference ay maaaring magpabilis ng karanasan ng customer at magpababa ng mga gastos, sinusuportahan ang mga modelo mula sa deep learning frameworks tulad ng PyTorch at TensorFlow/Keras pati na rin ang mga klasikong machine learning libraries tulad ng scikit-learn, LightGBM, XGBoost, atbp. Ang ONNX Runtime ay katugma sa iba't ibang hardware, driver, at operating system, at nagbibigay ng optimal na pagganap sa pamamagitan ng paggamit ng hardware accelerators kung saan maaari kasabay ng graph optimizations at transforms.

## Ano ang Generative AI?
Ang Generative AI ay tumutukoy sa mga AI system na makakagawa ng mga bagong nilalaman, tulad ng teksto, mga imahe, o musika, base sa data na kanilang pinag-aralan. Mga halimbawa nito ay ang mga language models gaya ng GPT-3 at mga image generation models tulad ng Stable Diffusion. Ang ONNX Runtime para sa GenAI library ay nagbibigay ng generative AI loop para sa mga ONNX models, kabilang na ang inference gamit ang ONNX Runtime, logits processing, search at sampling, at KV cache management.

## ONNX Runtime para sa GENAI
Pinalalawak ng ONNX Runtime para sa GENAI ang kakayahan ng ONNX Runtime upang suportahan ang mga generative AI models. Narito ang mga pangunahing katangian:

- **Malawak na Suporta sa Platform:** Gumagana ito sa iba't ibang platform, kabilang ang Windows, Linux, macOS, Android, at iOS.
- **Suporta sa Modelo:** Sinusuportahan nito ang maraming popular na generative AI models, tulad ng LLaMA, GPT-Neo, BLOOM, at iba pa.
- **Pag-optimize ng Pagganap:** Kasama rito ang mga optimisasyon para sa iba't ibang hardware accelerators tulad ng NVIDIA GPUs, AMD GPUs, at iba pa.
- **Kadalian ng Paggamit:** Nagbibigay ito ng mga API para sa madaling integrasyon sa mga aplikasyon, na nagpapahintulot sa iyo na gumawa ng teksto, mga imahe, at ibang nilalaman nang may minimal na code
- Maaaring tawagan ng mga gumagamit ang mataas na antas na generate() method, o patakbuhin ang bawat iteration ng modelo sa isang loop, na gumagawa ng isang token sa bawat pagkakataon, at opsyonal na ina-update ang mga generation parameters sa loob ng loop.
- May suporta rin ang ONNX runtime para sa greedy/beam search at TopP, TopK sampling upang makabuo ng mga token sequence at built-in logits processing tulad ng repetition penalties. Madali ring magdagdag ng custom scoring.

## Pagsisimula
Upang makapagsimula gamit ang ONNX Runtime para sa GENAI, maaari mong sundin ang mga hakbang na ito:

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
### Demo:Paggamit ng ONNX Runtime GenAI upang tawagin ang Phi-3.5-Vision


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

Bilang karagdagan sa ONNX Runtime, Ollama, at Foundry Local reference methods, maaari rin nating kumpletuhin ang reference ng quantitative models base sa model reference methods na ibinibigay ng iba't ibang manufacturer. Tulad ng Apple MLX framework gamit ang Apple Metal, Qualcomm QNN gamit ang NPU, Intel OpenVINO gamit ang CPU/GPU, atbp. Maaari ka ring makakuha ng karagdagang nilalaman mula sa [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Higit pa

Natutuhan na natin ang mga batayan ng Phi-3/3.5 Family, ngunit upang matuto pa tungkol sa SLM kailangan natin ng mas maraming kaalaman. Maaari mong matagpuan ang mga sagot sa Phi-3 Cookbook. Kung nais mong matuto pa, bisitahin ang [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->