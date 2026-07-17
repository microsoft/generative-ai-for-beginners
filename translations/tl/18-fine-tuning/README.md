[![Open Source Models](../../../translated_images/tl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning ng Iyong LLM

Ang paggamit ng malalaking language model upang bumuo ng mga generative AI na aplikasyon ay may kasamang mga bagong hamon. Isang mahalagang isyu ay ang pagsigurado ng kalidad ng tugon (katumpakan at kaugnayan) sa nilalamang nililikha ng modelo para sa isang partikular na kahilingan ng gumagamit. Sa mga naunang aralin, tinalakay namin ang mga teknik tulad ng prompt engineering at retrieval-augmented generation na sinusubukang lutasin ang problema sa pamamagitan ng _pagbabago ng prompt input_ sa umiiral na modelo.

Sa aralin ngayon, tatalakayin natin ang pangatlong teknik, ang **fine-tuning**, na sumusubok tugunan ang hamon sa pamamagitan ng _muling pagsasanay sa modelo mismo_ gamit ang karagdagang datos. Suriin natin ang mga detalye.

## Mga Layunin sa Pagkatuto

Ipinapakilala ng araling ito ang konsepto ng fine-tuning para sa mga pre-trained language model, tinatalakay ang mga benepisyo at hamon ng pamamaraang ito, at nagbibigay ng gabay kung kailan at paano gagamitin ang fine tuning upang mapabuti ang pagganap ng iyong mga generative AI na modelo.

Sa pagtatapos ng araling ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang fine tuning para sa mga language model?
- Kailan, at bakit, kapaki-pakinabang ang fine tuning?
- Paano ako makakapag-fine-tune ng isang pre-trained na modelo?
- Ano ang mga limitasyon ng fine-tuning?

Handa ka na ba? Magsimula tayo.

## Pinakita na Gabay

Gusto mo bang makuha ang kabuuang larawan ng mga tatalakayin bago tayo magsimula? Tingnan ang pinakilutong gabay na ito na naglalarawan ng paglalakbay sa pagkatuto para sa araling ito - mula sa pagkatuto ng mga pangunahing konsepto at motibasyon para sa fine-tuning, hanggang sa pag-unawa sa proseso at mga pinakamahuhusay na gawi para sa pagsasagawa ng fine-tuning na gawain. Isang kawili-wiling paksa ito para tuklasin, kaya huwag kalimutang tingnan ang [Mga Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) na pahina para sa karagdagang mga link na susuporta sa iyong sariling paglalakbay sa pagkatuto!

![Illustrated Guide to Fine Tuning Language Models](../../../translated_images/tl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ano ang fine-tuning para sa mga language model?

Ayon sa depinisyon, ang malalaking language model ay _pre-trained_ gamit ang malaking dami ng teksto mula sa iba't ibang pinanggalingan kabilang ang internet. Tulad ng natutunan natin sa mga naunang aralin, kailangan natin ng mga teknik tulad ng _prompt engineering_ at _retrieval-augmented generation_ upang mapabuti ang kalidad ng mga tugon ng modelo sa mga tanong ("prompts") ng gumagamit.

Isang kilalang paraan sa prompt engineering ang pagbibigay sa modelo ng mas maraming gabay sa inaasahan sa tugon alinman sa pamamagitan ng pagbibigay ng _mga tagubilin_ (hayagang panuto) o _pagbibigay ng ilang halimbawa_ (implicit na gabay). Tinatawag ito na _few-shot learning_ ngunit may dalawang limitasyon:

- Ang mga limitasyon sa token ng modelo ay maaaring magpigil sa dami ng mga halimbawang maaaring ibigay, at magkaroon ng limitadong bisa.
- Ang mga gastos sa token ng modelo ay maaaring maging mahal upang magdagdag ng mga halimbawa sa bawat prompt, at magpigil sa kakayahang magbago.

Ang fine-tuning ay isang pangkaraniwang kasanayan sa mga sistema ng machine learning kung saan kinukuha natin ang isang pre-trained na modelo at muling sinasanay ito gamit ang bagong datos upang mapabuti ang pagganap nito sa isang partikular na gawain. Sa konteksto ng mga language model, maaari nating fine-tune ang pre-trained na modelo _gamit ang piniling mga halimbawa para sa isang partikular na gawain o domain ng aplikasyon_ upang makalikha ng isang **pasadyang modelo** na maaaring mas tumpak at kaugnay para sa partikular na gawain o domain. Isang dagdag na benepisyo ng fine-tuning ay maaari rin nitong bawasan ang dami ng mga halimbawa na kailangan sa few-shot learning - na nagpapababa ng paggamit ng token at mga kaugnay na gastusin.

## Kailan at bakit dapat mag-fine-tune ng mga modelo?

Sa _kontekstong ito_, kapag pinag-uusapan natin ang fine-tuning, tinutukoy natin ang **supervised** na fine-tuning kung saan ang muling pagsasanay ay ginagawa sa pamamagitan ng **pagdaragdag ng bagong datos** na hindi kabilang sa orihinal na training dataset. Ito ay naiiba sa unsupervised fine-tuning kung saan muling sinasanay ang modelo sa orihinal na datos, ngunit gamit ang iba't ibang hyperparameters.

Ang mahalagang tandaan ay ang fine-tuning ay isang advanced na teknik na nangangailangan ng tiyak na antas ng kasanayan upang makamit ang ninanais na resulta. Kapag ginawa nang mali, maaaring hindi ito magbigay ng inaasahang pagbuti, at maaaring magpababa pa ng pagganap ng modelo para sa iyong target na domain.

Kaya, bago mo matutunan "paano" mag-fine-tune ng mga language model, kailangan mong malaman "bakit" mo dapat piliin ang paraang ito, at "kailan" simulan ang proseso ng fine-tuning. Simulan sa pagtatanong sa iyong sarili ng mga sumusunod na tanong:

- **Use Case**: Ano ang iyong _use case_ para sa fine-tuning? Anong aspeto ng kasalukuyang pre-trained na modelo ang nais mong pagbutihin?
- **Alternatibo**: Nasubukan mo na ba ang _ibang teknik_ upang maabot ang nais na resulta? Gamitin ang mga ito upang makalikha ng baseline para sa paghahambing.
  - Prompt engineering: Subukan ang mga teknik tulad ng few-shot prompting gamit ang mga halimbawa ng mga kaugnay na tugon sa prompt. Suriin ang kalidad ng mga tugon.
  - Retrieval Augmented Generation: Subukan ang pagdagdag ng mga resulta ng query sa mga prompt sa pamamagitan ng paghahanap sa iyong datos. Suriin ang kalidad ng mga tugon.
- **Mga Gastos**: Natukoy mo na ba ang mga gastusin para sa fine-tuning?
  - Kakayahang i-tune - available ba ang pre-trained na modelo para sa fine-tuning?
  - Pagsisikap - para sa paghahanda ng training data, pagsusuri at pag-refine ng modelo.
  - Kompyutasyon - para sa pagpapatakbo ng mga trabaho sa fine-tuning, at pag-deploy ng fine-tuned na modelo.
  - Datos - access sa sapat na kalidad ng mga halimbawa para sa malaking epekto ng fine-tuning.
- **Mga Benepisyo**: Nakumpirma mo na ba ang mga benepisyo ng fine-tuning?
  - Kalidad - nalampasan ba ng fine-tuned na modelo ang baseline?
  - Gastos - nakababawas ba ito sa paggamit ng token sa pamamagitan ng pagpapasimple ng mga prompt?
  - Kakayahang palawakin - maaari mo bang gamitin muli ang base model para sa mga bagong domain?

Sa pagsagot ng mga tanong na ito, dapat ay makapagpasya ka kung tama ba ang fine-tuning para sa iyong use case. Sa ideal, balido lamang ang pamamaraang ito kung mas malaki ang benepisyo kaysa sa gastos. Kapag nagpasyang ituloy, oras na para pag-isipan kung _paano_ mo maaring i-fine tune ang pre-trained na modelo.

Gusto mo bang makakuha ng higit pang kaalaman sa proseso ng paggawa ng desisyon? Panoorin ang [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Paano tayo makakapag-fine-tune ng isang pre-trained na modelo?

Para mag-fine-tune ng isang pre-trained na modelo, kailangan mong magkaroon ng:

- isang pre-trained na modelo upang i-fine-tune
- isang dataset para gamitin sa fine-tuning
- isang training environment upang patakbuhin ang fine-tuning na trabaho
- isang hosting environment upang i-deploy ang fine-tuned na modelo

## Fine-Tuning sa Microsoft Foundry

Ang [Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) ang lugar kung saan ka mag-fine-tune, mag-deploy, at mamahala ng mga pasadyang modelo sa Azure ngayon (pinagsasama nito ang dating Azure OpenAI Studio at Azure AI Studio). Bago ka magsimula ng trabaho, makakatulong na maunawaan mo ang mga pagpipilian na ibinibigay ng Foundry - at ang mga pinakamahuhusay na gawi na inirerekomenda ng plataporma. Sa likod ng mga eksena, ginagamit ng Foundry ang **LoRA (low-rank adaptation)** upang mag-fine-tune ng mga modelo nang epektibo, na pinananatiling mas mabilis ang pagsasanay at mas abot-kaya kaysa sa muling pagsasanay ng bawat timbang.

### Hakbang 1: Piliin ang teknik ng pagsasanay

Sinusuportahan ng Foundry ang tatlong teknik ng fine-tuning. **Magsimula sa SFT** - ito ang sumasaklaw sa pinakamaraming uri ng senaryo.

| Teknik | Ano ang ginagawa nito | Kailan ito gamitin |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Nagsasanay sa input/output example pairs upang matutunan ng modelo ang paggawa ng mga tugon na gusto mo. | Ang default para sa karamihan ng mga gawain: espesyalisasyon ng domain, pagganap ng gawain, estilo at tono, pagsunod sa instruksyon, at pag-aangkop sa wika. |
| **Direct Preference Optimization (DPO)** | Natututo mula sa _preferred vs. non-preferred_ na pares ng tugon upang itugma ang mga output sa mga preferensiya ng tao. | Pagpapabuti ng kalidad ng tugon, kaligtasan, at pagkakatugma kapag may comparative na feedback. |
| **Reinforcement Fine-Tuning (RFT)** | Gumagamit ng mga reward signal mula sa _mga tagasuri_ upang i-optimize ang komplikadong pag-uugali gamit ang reinforcement learning. | Mga layunin na may matinding pangangatwiran tulad ng matematika, kimika, pisika na may malinaw na tama/maling sagot. Nangangailangan ng mas mataas na kasanayan sa ML. |

### Hakbang 2: Piliin ang training tier

Pinapayagan ng Foundry na pumili ka kung paano at saan tatakbo ang pagsasanay:

- **Standard** - nagsasanay sa rehiyon ng iyong resource at ginagarantiyahan ang kaligtasan ng datos sa region na iyon. Gamitin ito kapag kailangang manatili ang datos sa isang tiyak na rehiyon.
- **Global** - mas mura at mas mabilis mag-queue gamit ang kapasidad lampas sa iyong rehiyon (kinokopya ang datos at timbang sa training region). Isang magandang default kapag hindi requirement ang data residency.
- **Developer** - pinakamurang opsyon, ginagamit ang idle capacity na walang latency/SLA guarantee (puwedeng ma-preempt at ma-resume ang mga trabaho). Perpekto para sa eksperimento.

### Hakbang 3: Pumili ng base model

Kasama sa mga modelong maaaring i-fine-tune ang OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, at `gpt-4.1-nano` (SFT; sinusuportahan din ng pamilya ng 4o/4.1 ang DPO), ang mga reasoning model na `o4-mini` at `gpt-5` (RFT), pati na rin ang mga open-source na modelo tulad ng `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, at `gpt-oss-20b` (SFT sa Foundry resources). Palaging suriin ang kasalukuyang [Fine-tuning models list](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para sa suportadong mga metodo, rehiyon, at availability.

> Nag-aalok ang Foundry ng dalawang modality: **serverless** (consumption-based pricing, walang GPU quota na kailangang pamahalaan, OpenAI at mga piling modelo) at **managed compute** (magdala ng sariling VM gamit ang Azure Machine Learning para sa pinakamalawak na hanay ng modelo). Karamihan sa mga tao ay dapat magsimula sa serverless.

### Mga pinakamahusay na gawi sa Foundry

- **Baseline muna.** Sukatin ang base model gamit ang prompt engineering at RAG _bago_ ka mag-fine-tune, upang mapatunayan ang pag-usbong.
- **Magsimula maliit, pagkatapos ay palawakin.** Magsimula sa 50-100 na mataas ang kalidad na mga halimbawa upang mapatunayan ang pamamaraan, pagkatapos ay palakihin sa 500+ para sa produksyon. Mahalagang higit na mahalaga ang kalidad kaysa dami – alisin ang mga mababang kalidad na halimbawa.
- **Format ng datos ng tama.** Ang mga training at validation files ay kailangang JSONL, UTF-8 **na may BOM**, mas mababa sa 512 MB, gamit ang chat-completions message format. Laging isama ang validation file para mapanood ang overfitting.
- **Panatilihin ang training system prompt sa inference.** Gamitin ang parehong system message kapag tinawag ang modelo na ginamit mo noong training.
- **Suriin ang mga checkpoint – huwag basta i-deploy ang huling isa.** Pinananatili ng Foundry ang huling tatlong epochs bilang mga deployable checkpoint; piliin ang pinakamahusay na nagge-generalize sa pamamagitan ng pagmamasid sa `train_loss` / `valid_loss` at token accuracy.
- **Sukatin ang gastos ng token kasabay ng kalidad** kapag inihahambing ang fine-tuned na modelo sa baseline.
- **Ulitin gamit ang tuloy-tuloy na fine-tuning.** Maaari kang mag-fine-tune ng isang fine-tuned na modelo gamit ang bagong datos (sinusuportahan para sa OpenAI models).
- **Isaalang-alang ang gastos sa hosting.** Ang isang deployed custom model ay naniningil ng oras-oras, at ang hindi aktibong deployment ay tinatanggal pagkatapos ng 15 araw - linisin ang mga hindi mo kailangan.

Sundan ang buong gabay sa [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), at tingnan ang mga gabay para sa [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) at [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) kapag handa ka na sa iba pang mga teknik.

## Fine-Tuning Sa Gawa

Ang mga sumusunod na resources ay naglalaman ng mga step-by-step na tutorial na gumagabay sa iyo sa isang totoong halimbawa gamit ang kasalukuyang suportadong modelo at piniling dataset. Para magamit ang mga ito, kailangan mong magkaroon ng account sa partikular na provider, pati na rin access sa kaukulang modelo at mga dataset.

| Provider     | Tutorial                                                                                                                                                                       | Paglalarawan                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Paano mag-fine-tune ng chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Matutunan kung paano mag-fine-tune ng kamakailang OpenAI chat model para sa isang partikular na domain ("assistant ng recipe") sa pamamagitan ng paghahanda ng training data, pagpapatakbo ng fine-tuning na trabaho, at paggamit ng fine-tuned na modelo para sa inference.                                                                                                                                                                              |
| Microsoft Foundry | [I-customize ang modelo gamit ang fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Matutunan kung paano mag-fine-tune ng kasalukuyang suportadong modelo tulad ng `gpt-4.1-mini` **sa Azure** gamit ang Microsoft Foundry: ihanda at i-upload ang training at validation data, patakbuhin ang fine-tuning na trabaho, pagkatapos ay i-deploy at gamitin ang bagong modelo.                                                                                                                                                                                                         |

| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ang blog post na ito ay nagpapakita sa iyo kung paano mag-fine-tune ng _open LLM_ (halimbawa: `CodeLlama 7B`) gamit ang [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) library at [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) gamit ang bukas na [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) sa Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | Ang AutoTrain (o AutoTrain Advanced) ay isang python library na binuo ng Hugging Face na nagpapahintulot ng fine-tuning para sa maraming iba't ibang gawain kabilang ang LLM fine-tuning. Ang AutoTrain ay isang no-code na solusyon at maaaring gawin ang fine-tuning sa iyong sariling cloud, sa Hugging Face Spaces o lokal. Sinusuportahan nito ang web-based GUI, CLI at pagsasanay gamit ang yaml config files.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Ang Unsloth ay isang open-source na framework na sumusuporta sa LLM fine-tuning at reinforcement learning (RL). Pinapadali ng Unsloth ang lokal na pagsasanay, pagsusuri, at deployment gamit ang mga handang gamitin na [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Sinusuportahan rin nito ang text-to-speech (TTS), BERT at multimodal na mga modelo. Upang makapagsimula, basahin ang kanilang step-by-step na [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Assignment

Pumili ng isa sa mga tutorial sa itaas at sundan ang mga ito. _Maaring gumawa kami ng bersyon ng mga tutorial na ito sa Jupyter Notebooks sa repo na ito bilang sanggunian lamang. Mangyaring gamitin ang orihinal na mga pinagkukunan direkta upang makuha ang pinakabagong mga bersyon_.

## Mahusay na Gawa! Ipagpatuloy ang Iyong Pag-aaral.

Matapos makumpleto ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Binabati kita!! Nakumpleto mo na ang huling aralin mula sa v2 series para sa kursong ito! Huwag tumigil sa pag-aaral at pagbuo. \*\*Tingnan ang pahina ng [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para sa listahan ng iba pang mga suhestiyon para lamang sa paksang ito.

Ang aming v1 series ng mga aralin ay na-update din na may higit pang mga takdang-aralin at mga konsepto. Kaya maglaan ng sandali upang sariwain ang iyong kaalaman - at mangyaring [ibahagi ang iyong mga katanungan at puna](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) upang matulungan kaming mapabuti ang mga araling ito para sa komunidad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->