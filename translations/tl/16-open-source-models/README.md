<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a8b2d4bb727c877ebf9edff8623d16b9",
  "translation_date": "2025-09-06T10:22:02+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.tl.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Panimula

Ang mundo ng open-source LLMs ay kapana-panabik at patuloy na nagbabago. Ang araling ito ay naglalayong magbigay ng mas malalim na pag-unawa sa mga open source na modelo. Kung naghahanap ka ng impormasyon tungkol sa pagkukumpara ng proprietary models sa open source models, pumunta sa ["Exploring and Comparing Different LLMs" lesson](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tatalakayin din sa araling ito ang paksa ng fine-tuning, ngunit mas detalyadong paliwanag ay matatagpuan sa ["Fine-Tuning LLMs" lesson](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Mga Layunin sa Pag-aaral

- Maunawaan ang open source na mga modelo
- Maunawaan ang mga benepisyo ng paggamit ng open source na mga modelo
- Tuklasin ang mga open models na makikita sa Hugging Face at Azure AI Studio

## Ano ang Open Source Models?

Ang open source software ay may mahalagang papel sa pag-unlad ng teknolohiya sa iba't ibang larangan. Ang Open Source Initiative (OSI) ay nagtakda ng [10 pamantayan para sa software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) upang maiklasipika bilang open source. Ang source code ay kailangang bukas na ibinabahagi sa ilalim ng lisensyang aprubado ng OSI.

Bagama't ang pagbuo ng LLMs ay may mga katulad na elemento sa pagbuo ng software, hindi eksaktong pareho ang proseso. Ito ang nagdala ng maraming talakayan sa komunidad tungkol sa kahulugan ng open source sa konteksto ng LLMs. Para maituring na naaayon sa tradisyunal na kahulugan ng open source, ang sumusunod na impormasyon ay dapat na pampublikong magagamit:

- Mga dataset na ginamit sa pag-train ng modelo.
- Buong model weights bilang bahagi ng training.
- Ang evaluation code.
- Ang fine-tuning code.
- Buong model weights at training metrics.

Sa kasalukuyan, iilan lamang ang mga modelo na tumutugma sa pamantayang ito. Ang [OLMo model na ginawa ng Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ay isa sa mga tumutugma sa kategoryang ito.

Para sa araling ito, tatawagin natin ang mga modelo bilang "open models" mula ngayon dahil maaaring hindi sila tumutugma sa pamantayan sa itaas sa oras ng pagsulat.

## Mga Benepisyo ng Open Models

**Lubos na Napapasadya** - Dahil ang open models ay inilalabas na may detalyadong impormasyon sa training, maaaring baguhin ng mga mananaliksik at developer ang mga internal ng modelo. Pinapahintulutan nito ang paglikha ng mga modelong lubos na espesyal para sa partikular na gawain o larangan ng pag-aaral. Ilang halimbawa nito ay ang code generation, mathematical operations, at biology.

**Gastos** - Ang gastos kada token sa paggamit at pag-deploy ng mga modelong ito ay mas mababa kumpara sa proprietary models. Kapag gumagawa ng Generative AI applications, mahalagang suriin ang performance kumpara sa presyo batay sa iyong use case.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.tl.png)  
Source: Artificial Analysis

**Kakayahang Mag-adjust** - Ang paggamit ng open models ay nagbibigay-daan sa kakayahang mag-adjust sa paggamit ng iba't ibang modelo o pagsasama-sama ng mga ito. Isang halimbawa nito ay ang [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) kung saan maaaring pumili ang user ng modelong gagamitin direkta sa user interface:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.tl.png)

## Pagtuklas sa Iba't Ibang Open Models

### Llama 2

[LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), na binuo ng Meta, ay isang open model na na-optimize para sa mga chat-based na aplikasyon. Ito ay dahil sa fine-tuning method nito, na kinabibilangan ng malaking dami ng dialogue at human feedback. Sa pamamaraang ito, ang modelo ay nagbibigay ng mas maraming resulta na naaayon sa inaasahan ng tao, na nagbibigay ng mas mahusay na karanasan sa user.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Llama ay ang [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), na espesyal para sa Japanese, at [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), na isang pinahusay na bersyon ng base model.

### Mistral

[Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ay isang open model na nakatuon sa mataas na performance at efficiency. Ginagamit nito ang Mixture-of-Experts approach na pinagsasama ang grupo ng mga espesyal na expert models sa isang sistema kung saan, depende sa input, ang mga partikular na modelo ay pinipili upang gamitin. Ginagawa nitong mas epektibo ang computation dahil ang mga modelo ay tumutugon lamang sa mga input na kanilang espesyalisasyon.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Mistral ay ang [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), na nakatuon sa medical domain, at [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), na gumagawa ng mathematical computation.

### Falcon

[Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ay isang LLM na ginawa ng Technology Innovation Institute (**TII**). Ang Falcon-40B ay na-train sa 40 bilyong parameters na napatunayang mas mahusay kaysa sa GPT-3 na may mas mababang compute budget. Ito ay dahil sa paggamit nito ng FlashAttention algorithm at multiquery attention na nagpapababa sa memory requirements sa inference time. Sa mas mabilis na inference time, ang Falcon-40B ay angkop para sa chat applications.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Falcon ay ang [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), isang assistant na binuo gamit ang open models, at [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), na nagbibigay ng mas mataas na performance kaysa sa base model.

## Paano Pumili

Walang iisang sagot sa pagpili ng open model. Isang magandang simula ay ang paggamit ng Azure AI Studio's filter by task feature. Makakatulong ito upang maunawaan kung anong uri ng mga gawain ang na-train para sa modelo. Ang Hugging Face ay mayroon ding LLM Leaderboard na nagpapakita ng pinakamahusay na mga modelo batay sa ilang metrics.

Kapag naghahanap ng pagkukumpara ng LLMs sa iba't ibang uri, ang [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ay isa pang mahusay na mapagkukunan:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.tl.png)  
Source: Artificial Analysis

Kung nagtatrabaho sa isang partikular na use case, ang paghahanap ng fine-tuned na bersyon na nakatuon sa parehong larangan ay maaaring maging epektibo. Ang pag-eeksperimento sa maraming open models upang makita kung paano sila gumagana ayon sa iyong at sa inaasahan ng iyong mga user ay isa pang magandang kasanayan.

## Mga Susunod na Hakbang

Ang pinakamagandang bahagi ng open models ay maaari kang magsimula sa paggamit ng mga ito nang mabilis. Tingnan ang [Azure AI Foundry Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), na nagtatampok ng isang partikular na Hugging Face collection na may mga modelong tinalakay natin dito.

## Hindi natatapos dito ang pag-aaral, ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang patuloy na paunlarin ang iyong kaalaman sa Generative AI!

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.