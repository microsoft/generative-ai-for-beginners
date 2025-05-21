<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "0bba96e53ab841d99db731892a51fab8",
  "translation_date": "2025-05-20T07:00:52+00:00",
  "source_file": "16-open-source-models/README.md",
  "language_code": "tl"
}
-->
## Panimula

Ang mundo ng open-source na LLMs ay kapanapanabik at patuloy na nagbabago. Ang araling ito ay naglalayong magbigay ng masusing pagtingin sa open source na mga modelo. Kung naghahanap ka ng impormasyon kung paano ikumpara ang proprietary models sa open source models, pumunta sa araling ["Exploring and Comparing Different LLMs"](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst). Tatalakayin din sa araling ito ang paksa ng fine-tuning ngunit ang mas detalyadong paliwanag ay matatagpuan sa araling ["Fine-Tuning LLMs"](../18-fine-tuning/README.md?WT.mc_id=academic-105485-koreyst).

## Mga Layunin sa Pagkatuto

- Magkaroon ng pag-unawa sa open source na mga Modelo
- Pag-unawa sa mga benepisyo ng pagtatrabaho gamit ang open source na mga Modelo
- Pagsusuri sa mga open models na makukuha sa Hugging Face at Azure AI Studio

## Ano ang Open Source na mga Modelo?

Ang open source na software ay may mahalagang papel sa paglago ng teknolohiya sa iba't ibang larangan. Ang Open Source Initiative (OSI) ay nagtakda ng [10 pamantayan para sa software](https://web.archive.org/web/20241126001143/https://opensource.org/osd?WT.mc_id=academic-105485-koreyst) upang maituring na open source. Ang source code ay dapat na bukas na ibinahagi sa ilalim ng lisensyang aprubado ng OSI.

Habang ang pag-develop ng LLMs ay may mga katulad na elemento sa pag-develop ng software, ang proseso ay hindi eksaktong pareho. Ito ay nagdala ng maraming talakayan sa komunidad tungkol sa depinisyon ng open source sa konteksto ng LLMs. Para maitugma ang isang modelo sa tradisyonal na depinisyon ng open source, ang sumusunod na impormasyon ay dapat na pampublikong magagamit:

- Mga dataset na ginamit sa pag-train ng modelo.
- Buong model weights bilang bahagi ng pag-train.
- Ang evaluation code.
- Ang fine-tuning code.
- Buong model weights at training metrics.

Sa kasalukuyan, iilan lamang ang mga modelo na tumutugma sa pamantayang ito. Ang [OLMo model na ginawa ng Allen Institute for Artificial Intelligence (AllenAI)](https://huggingface.co/allenai/OLMo-7B?WT.mc_id=academic-105485-koreyst) ay isa na pumapasok sa kategoryang ito.

Para sa araling ito, tatawagin natin ang mga modelo bilang "open models" sa mga susunod na bahagi dahil maaaring hindi sila tumutugma sa pamantayan sa itaas sa oras ng pagsulat.

## Mga Benepisyo ng Open Models

**Lubos na Naiaangkop** - Dahil ang open models ay inilalabas na may detalyadong impormasyon sa pag-train, maaaring baguhin ng mga mananaliksik at developer ang loob ng modelo. Ito ay nagbibigay-daan sa paglikha ng mga modelong lubos na espesyal na na-fine-tune para sa isang tiyak na gawain o larangan ng pag-aaral. Ilan sa mga halimbawa nito ay ang pag-generate ng code, mga operasyong matematikal, at biyolohiya.

**Gastos** - Ang gastos kada token para sa paggamit at pag-deploy ng mga modelong ito ay mas mababa kaysa sa proprietary models. Kapag bumubuo ng Generative AI applications, dapat na isaalang-alang ang performance kumpara sa presyo kapag nagtatrabaho gamit ang mga modelong ito sa iyong kaso ng paggamit.

**Kakayahang Umangkop** - Ang pagtatrabaho gamit ang open models ay nagbibigay-daan sa iyo na maging flexible sa paggamit ng iba't ibang mga modelo o pagsasama-sama ng mga ito. Isang halimbawa nito ay ang [HuggingChat Assistants](https://huggingface.co/chat?WT.mc_id=academic-105485-koreyst) kung saan maaaring piliin ng isang user ang modelong ginagamit direkta sa user interface.

## Pagsusuri sa Iba't ibang Open Models

### Llama 2

Ang [LLama2](https://huggingface.co/meta-llama?WT.mc_id=academic-105485-koreyst), na binuo ng Meta, ay isang open model na na-optimize para sa mga chat-based na aplikasyon. Ito ay dahil sa kanyang fine-tuning na paraan, na kinabibilangan ng malaking dami ng diyalogo at feedback mula sa tao. Sa pamamaraang ito, ang modelo ay naglalabas ng mas maraming resulta na naaayon sa inaasahan ng tao na nagbibigay ng mas mahusay na karanasan sa gumagamit.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Llama ay ang [Japanese Llama](https://huggingface.co/elyza/ELYZA-japanese-Llama-2-7b?WT.mc_id=academic-105485-koreyst), na nagdadalubhasa sa wikang Hapon at [Llama Pro](https://huggingface.co/TencentARC/LLaMA-Pro-8B?WT.mc_id=academic-105485-koreyst), na isang pinahusay na bersyon ng base model.

### Mistral

Ang [Mistral](https://huggingface.co/mistralai?WT.mc_id=academic-105485-koreyst) ay isang open model na may matinding pokus sa mataas na performance at kahusayan. Gumagamit ito ng Mixture-of-Experts na pamamaraan na pinagsasama ang isang grupo ng mga espesyal na expert models sa isang sistema kung saan depende sa input, ang ilang mga modelo ay pinipili na gamitin. Ito ay ginagawang mas epektibo ang computation dahil ang mga modelo ay tumutugon lamang sa mga input na kanilang ispesyalisasyon.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Mistral ay ang [BioMistral](https://huggingface.co/BioMistral/BioMistral-7B?text=Mon+nom+est+Thomas+et+mon+principal?WT.mc_id=academic-105485-koreyst), na nakatuon sa medikal na larangan at [OpenMath Mistral](https://huggingface.co/nvidia/OpenMath-Mistral-7B-v0.1-hf?WT.mc_id=academic-105485-koreyst), na gumaganap ng mga kalkulasyong matematikal.

### Falcon

Ang [Falcon](https://huggingface.co/tiiuae?WT.mc_id=academic-105485-koreyst) ay isang LLM na ginawa ng Technology Innovation Institute (**TII**). Ang Falcon-40B ay na-train gamit ang 40 bilyong mga parameter na napatunayang mas mahusay kaysa sa GPT-3 na may mas mababang compute budget. Ito ay dahil sa paggamit nito ng FlashAttention algorithm at multiquery attention na nagpapahintulot dito na mabawasan ang mga pangangailangan sa memorya sa oras ng inference. Sa mas maikling oras ng inference, ang Falcon-40B ay angkop para sa mga chat applications.

Ilan sa mga halimbawa ng fine-tuned na bersyon ng Falcon ay ang [OpenAssistant](https://huggingface.co/OpenAssistant/falcon-40b-sft-top1-560?WT.mc_id=academic-105485-koreyst), isang assistant na itinayo sa open models at [GPT4ALL](https://huggingface.co/nomic-ai/gpt4all-falcon?WT.mc_id=academic-105485-koreyst), na nagdudulot ng mas mataas na performance kaysa sa base model.

## Paano Pumili

Walang isang sagot para sa pagpili ng open model. Isang magandang simula ay ang paggamit ng Azure AI Studio's filter by task feature. Makakatulong ito sa iyo na maunawaan kung anong mga uri ng gawain ang na-train para sa modelo. Ang Hugging Face ay nagtataglay din ng LLM Leaderboard na nagpapakita ng mga pinakamahusay na gumaganap na modelo batay sa ilang mga sukatan.

Kapag naghahanap na ikumpara ang LLMs sa iba't ibang uri, ang [Artificial Analysis](https://artificialanalysis.ai/?WT.mc_id=academic-105485-koreyst) ay isa pang mahusay na mapagkukunan.

Kung nagtatrabaho sa isang tiyak na kaso ng paggamit, ang paghahanap ng mga fine-tuned na bersyon na nakatuon sa parehong larangan ay maaaring maging epektibo. Ang pagsubok sa maraming open models upang makita kung paano sila gumaganap ayon sa iyong at ng iyong mga gumagamit na inaasahan ay isa pang magandang kasanayan.

## Mga Susunod na Hakbang

Ang pinakamagandang bahagi tungkol sa open models ay maaari kang magsimula sa pagtatrabaho gamit ang mga ito nang mabilis. Tingnan ang [Azure AI Studio Model Catalog](https://ai.azure.com?WT.mc_id=academic-105485-koreyst), na nagtatampok ng isang tiyak na Hugging Face collection na may mga modelong tinalakay natin dito.

## Hindi Natatapos Dito ang Pag-aaral, Ipagpatuloy ang Paglalakbay

Pagkatapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Habang sinisikap naming maging tama, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang sanggunian. Para sa kritikal na impormasyon, inirerekomenda ang propesyonal na pagsasaling-wika ng tao. Hindi kami mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.