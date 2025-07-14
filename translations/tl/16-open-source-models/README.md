<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-07-09T17:13:16+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tl"
}
-->
[![Open Source Models](../../../translated_images/16-lesson-banner.6b56555e8404fda1716382db4832cecbe616ccd764de381f0af6cfd694d05f74.tl.png)](https://aka.ms/gen-ai-lesson16-gh?WT.mc_id=academic-105485-koreyst)

## Panimula

Ang mundo ng open-source LLMs ay kapanapanabik at patuloy na umuunlad. Layunin ng araling ito na magbigay ng mas malalim na pagtingin sa mga open source na modelo. Kung naghahanap ka ng impormasyon kung paano ikinukumpara ang mga proprietary na modelo sa open source na mga modelo, pumunta sa ["Exploring and Comparing Different LLMs" lesson](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tatalakayin din sa araling ito ang tungkol sa fine-tuning ngunit mas detalyadong paliwanag ay matatagpuan sa ["Fine-Tuning LLMs" lesson](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Mga Layunin sa Pagkatuto

- Maunawaan ang mga open source na Modelo  
- Maunawaan ang mga benepisyo ng paggamit ng open source na mga Modelo  
- Tuklasin ang mga open models na makikita sa Hugging Face at Azure AI Studio  

## Ano ang mga Open Source Models?

Malaki ang naging papel ng open source software sa pag-unlad ng teknolohiya sa iba't ibang larangan. Itinakda ng Open Source Initiative (OSI) ang [10 pamantayan para sa software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) upang maituring itong open source. Ang source code ay kailangang bukas na ibinahagi sa ilalim ng lisensyang aprubado ng OSI.

Bagamat may pagkakatulad ang pagbuo ng LLMs sa pagbuo ng software, hindi ito eksaktong pareho ang proseso. Dahil dito, maraming diskusyon sa komunidad tungkol sa kahulugan ng open source sa konteksto ng LLMs. Para maituring na sumusunod sa tradisyunal na kahulugan ng open source, dapat na publiko ang mga sumusunod na impormasyon:

- Mga datasets na ginamit sa pagsasanay ng modelo.  
- Buong model weights bilang bahagi ng pagsasanay.  
- Ang evaluation code.  
- Ang fine-tuning code.  
- Buong model weights at mga training metrics.  

Sa kasalukuyan, iilan lamang ang mga modelong tumutugma sa pamantayang ito. Ang [OLMo model na ginawa ng Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ay isa sa mga kabilang sa kategoryang ito.

Para sa araling ito, tatawagin nating "open models" ang mga modelo dahil maaaring hindi pa nila natutugunan ang mga pamantayang ito sa oras ng pagsulat.

## Mga Benepisyo ng Open Models

**Napaka-Customizable** – Dahil inilalabas ang open models kasama ang detalyadong impormasyon sa pagsasanay, maaaring baguhin ng mga mananaliksik at developer ang mga internal ng modelo. Nagbibigay ito ng kakayahang gumawa ng mga modelong espesyal na naiaangkop para sa partikular na gawain o larangan ng pag-aaral. Ilan sa mga halimbawa nito ay code generation, mga operasyong matematika, at biology.

**Gastos** – Mas mababa ang gastos kada token sa paggamit at pag-deploy ng mga modelong ito kumpara sa mga proprietary na modelo. Kapag gumagawa ng Generative AI na mga aplikasyon, mahalagang isaalang-alang ang performance kumpara sa presyo sa paggamit ng mga modelong ito para sa iyong kaso.

![Model Cost](../../../translated_images/model-price.3f5a3e4d32ae00b465325159e1f4ebe7b5861e95117518c6bfc37fe842950687.tl.png)  
Pinagmulan: Artificial Analysis

**Kakayahang Magbago-bago** – Ang paggamit ng open models ay nagbibigay-daan sa iyo na maging flexible sa paggamit ng iba't ibang modelo o pagsasama-sama ng mga ito. Halimbawa nito ang [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) kung saan maaaring pumili ang user ng modelong gagamitin direkta sa user interface:

![Choose Model](../../../translated_images/choose-model.f095d15bbac922141591fd4fac586dc8d25e69b42abf305d441b84c238e293f2.tl.png)

## Pagtuklas sa Iba’t Ibang Open Models

### Llama 2

Ang [Llama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), na ginawa ng Meta, ay isang open model na na-optimize para sa mga chat-based na aplikasyon. Ito ay dahil sa paraan ng fine-tuning nito, na kinabibilangan ng malaking dami ng dayalogo at feedback mula sa tao. Sa pamamaraang ito, mas nagagawa ng modelo ang mga resulta na naaayon sa inaasahan ng tao na nagbibigay ng mas magandang karanasan sa user.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Llama ay ang [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), na espesyalisado sa wikang Hapon, at ang [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), na isang pinahusay na bersyon ng base model.

### Mistral

Ang [Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ay isang open model na nakatuon sa mataas na performance at kahusayan. Ginagamit nito ang Mixture-of-Experts na pamamaraan kung saan pinagsasama ang grupo ng mga espesyalistang modelo sa isang sistema kung saan, depende sa input, pinipili ang mga modelong gagamitin. Ginagawa nitong mas epektibo ang komputasyon dahil ang mga modelo ay tumutugon lamang sa mga input na kanilang espesyalisado.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Mistral ay ang [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), na nakatuon sa medikal na larangan, at ang [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), na gumagawa ng mga matematikal na kalkulasyon.

### Falcon

Ang [Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ay isang LLM na ginawa ng Technology Innovation Institute (**TII**). Ang Falcon-40B ay sinanay gamit ang 40 bilyong parameters na ipinakita na mas mahusay kaysa sa GPT-3 gamit ang mas kaunting compute budget. Ito ay dahil sa paggamit nito ng FlashAttention algorithm at multiquery attention na nagpapababa ng pangangailangan sa memorya sa oras ng inference. Dahil sa pinaikling oras ng inference, ang Falcon-40B ay angkop para sa mga chat application.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Falcon ay ang [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), isang assistant na ginawa gamit ang open models, at ang [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), na nagbibigay ng mas mataas na performance kaysa sa base model.

## Paano Pumili

Walang iisang sagot sa pagpili ng open model. Magandang simulan sa paggamit ng filter by task feature ng Azure AI Studio. Makakatulong ito upang maunawaan kung anong mga uri ng gawain ang sinanay sa modelo. Pinapanatili rin ng Hugging Face ang isang LLM Leaderboard na nagpapakita ng mga pinakamahusay na modelo base sa ilang mga sukatan.

Kapag naghahanap ng paghahambing ng LLMs sa iba't ibang uri, ang [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ay isa pang mahusay na mapagkukunan:

![Model Quality](../../../translated_images/model-quality.aaae1c22e00f7ee1cd9dc186c611ac6ca6627eabd19e5364dce9e216d25ae8a5.tl.png)  
Pinagmulan: Artificial Analysis

Kung nagtatrabaho sa isang partikular na kaso, ang paghahanap ng mga fine-tuned na bersyon na nakatuon sa parehong larangan ay maaaring maging epektibo. Ang pagsubok sa iba't ibang open models upang makita kung paano sila gumaganap ayon sa iyong at ng iyong mga user na inaasahan ay isa pang magandang gawain.

## Mga Susunod na Hakbang

Ang pinakamagandang bahagi ng open models ay maaari kang agad makapagsimula sa paggamit nito. Tingnan ang [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), na nagtatampok ng isang partikular na koleksyon ng Hugging Face na may mga modelong tinalakay dito.

## Hindi Dito Nagtatapos ang Pagkatuto, Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.