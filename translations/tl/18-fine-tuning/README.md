<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3772dcd23a98e2010f53ce8b9c583631",
  "translation_date": "2026-01-18T18:44:52+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "tl"
}
-->
[![Open Source Models](../../../../../translated_images/tl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning ng Iyong LLM

Ang paggamit ng malalaking modelo ng wika para gumawa ng mga generative AI na aplikasyon ay may kasamang mga bagong hamon. Isang susi na isyu ay ang pagtitiyak sa kalidad ng tugon (katumpakan at kaugnayan) sa nilalamang nilikha ng modelo para sa isang partikular na kahilingan ng gumagamit. Sa mga nakaraang leksyon, tinalakay natin ang mga teknika tulad ng prompt engineering at retrieval-augmented generation na sumusubok na lutasin ang problema sa pamamagitan ng _pagbabago ng prompt input_ sa umiiral na modelo.

Sa leksyon ngayon, tatalakayin natin ang ikatlong teknik, ang **fine-tuning**, na sumusubok na tugunan ang hamon sa pamamagitan ng _muling pagsasanay sa mismong modelo_ gamit ang karagdagang datos. Tara’t sumisid tayo sa mga detalye.

## Mga Layunin sa Pagkatuto

Ipinapakilala ng leksyon na ito ang konsepto ng fine-tuning para sa mga pre-trained na modelo ng wika, sinasaliksik ang mga benepisyo at hamon ng pamamaraang ito, at nagbibigay gabay kung kailan at paano gamitin ang fine-tuning upang mapabuti ang pagganap ng iyong mga generative AI na modelo.

Sa pagtatapos ng leksyon na ito, dapat mong masagot ang mga sumusunod na tanong:

- Ano ang fine-tuning para sa mga modelo ng wika?
- Kailan, at bakit, kapaki-pakinabang ang fine-tuning?
- Paano ako makakapag-fine-tune ng isang pre-trained na modelo?
- Ano ang mga limitasyon ng fine-tuning?

Handa ka na ba? Magsimula na tayo.

## Ilustradong Gabay

Gusto mo bang makita ang kabuuang larawan ng mga pag-uusapan natin bago tayo sumabak? Tingnan ang ilustradong gabay na ito na naglalarawan ng paglalakbay sa pagkatuto para sa leksyon na ito - mula sa pag-aaral ng mga pangunahing konsepto at motibasyon para sa fine-tuning, hanggang sa pag-unawa sa proseso at pinakamahuhusay na gawain para sa pagpapatupad ng gawain ng fine-tuning. Isang kapanapanabik na paksa ito para sa paggalugad, kaya huwag kalimutang bisitahin ang [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) na pahina para sa karagdagang mga link na susuporta sa iyong sariling paglalakbay sa pagkatuto!

![Illustrated Guide to Fine Tuning Language Models](../../../../../translated_images/tl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ano ang fine-tuning para sa mga modelo ng wika?

Ayon sa kahulugan, ang mga malalaking modelo ng wika ay _pre-trained_ sa malaking dami ng teksto na galing sa iba't ibang mga pinanggalingan kabilang na ang internet. Tulad ng natutunan natin sa mga nakaraang leksyon, kailangan natin ng mga teknik tulad ng _prompt engineering_ at _retrieval-augmented generation_ upang mapabuti ang kalidad ng mga tugon ng modelo sa mga tanong ("prompts") ng gumagamit.

Isang kilalang teknik sa prompt-engineering ay ang pagbibigay sa modelo ng mas maraming gabay kung ano ang inaasahan sa tugon sa pamamagitan ng pagbibigay ng _mga instruksyon_ (hayagang gabay) o _pagbibigay ng ilang halimbawa_ (di-hayagang gabay). Ito ay tinatawag na _few-shot learning_ ngunit may dalawang limitasyon:

- Ang mga limitasyon sa token ng modelo ay maaaring pumigil sa dami ng mga halimbawa na maaaring ibigay, at limitahan ang bisa nito.
- Ang gastos sa token ng modelo ay maaaring gawing mahal ang pagdagdag ng mga halimbawa sa bawat prompt, at limitahan ang pagkamalikhain.

Ang fine-tuning ay isang karaniwang gawain sa mga sistema ng machine learning kung saan kinukuha natin ang isang pre-trained na modelo at muling sinasanay ito gamit ang bagong datos upang mapabuti ang pagganap nito sa isang partikular na gawain. Sa konteksto ng mga modelo ng wika, maaari nating i-fine-tune ang pre-trained na modelo _gamit ang mas piling hanay ng mga halimbawa para sa isang tiyak na gawain o application domain_ upang lumikha ng isang **custom na modelo** na maaaring mas tumpak at kaugnay para sa partikular na gawain o domain. Isang karagdagang benepisyo ng fine-tuning ay maaari rin nitong bawasan ang bilang ng mga halimbawang kailangan para sa few-shot learning—na nagpapababa ng paggamit ng token at mga kaakibat na gastos.

## Kailan at bakit natin dapat i-fine-tune ang mga modelo?

Sa _kontekstong_ ito, kapag pinag-uusapan natin ang fine-tuning, tumutukoy tayo sa **supervised** fine-tuning kung saan ang muling pagsasanay ay ginagawa sa pamamagitan ng **pagdaragdag ng bagong datos** na hindi kabilang sa orihinal na dataset ng pagsasanay. Ito ay iba sa isang unsupervised na paraan ng fine-tuning kung saan ang modelo ay muling sinasanay sa orihinal na datos ngunit may ibang mga hyperparameters.

Ang mahalagang tandaan ay ang fine-tuning ay isang advanced na teknik na nangangailangan ng isang tiyak na lebel ng kasanayan upang makuha ang nais na resulta. Kung hindi ito magagawa nang tama, maaaring hindi nito maibigay ang inaasahang mga pagpapabuti, at maaaring mas lumala pa ang pagganap ng modelo para sa iyong target na domain.

Kaya, bago mo matutunan ang "paano" mag-fine-tune ng mga modelo ng wika, kailangan mong malaman "bakit" dapat mong tahakin ang landas na ito, at "kailan" simulan ang proseso ng fine-tuning. Magsimula sa pagtatanong sa iyong sarili ng mga tanong na ito:

- **Gamit**: Ano ang iyong _use case_ para sa fine-tuning? Anong aspeto ng kasalukuyang pre-trained na modelo ang gusto mong pagbutihin?
- **Mga Alternatibo**: Nasubukan mo na ba ang _ibang mga teknik_ para makamit ang nais na resulta? Gamitin ang mga ito upang gumawa ng baseline para sa paghahambing.
  - Prompt engineering: Subukan ang mga teknik tulad ng few-shot prompting gamit ang mga halimbawa ng kaugnay na tugon sa prompt. Suriin ang kalidad ng mga tugon.
  - Retrieval Augmented Generation: Subukan ang pag-augment ng mga prompt gamit ang resulta ng query na nakuha mula sa paghahanap sa iyong datos. Suriin ang kalidad ng mga tugon.
- **Gastos**: Napag-alaman mo na ba ang mga gastos para sa fine-tuning?
  - Tunability - available ba ang pre-trained modelo para sa fine-tuning?
  - Pagsisikap - para sa paghahanda ng training data, pagsusuri at pagpapabuti ng modelo.
  - Compute - para sa pagpapatakbo ng fine-tuning jobs at pag-deploy ng fine-tuned na modelo
  - Data - access sa sapat na kalidad ng mga halimbawa para sa epekto ng fine-tuning
- **Mga Benepisyo**: Nakumpirma mo na ba ang mga benepisyo ng fine-tuning?
  - Kalidad - naipasubok ba ng fine-tuned na modelo ang baseline?
  - Gastos - nakabawas ba ito sa paggamit ng token sa pamamagitan ng pagpapa-simple ng mga prompt?
  - Extensibility - maaari mo bang gamitin muli ang base na modelo para sa mga bagong domain?

Sa pagsagot sa mga tanong na ito, dapat kang makapagpasya kung tama ang fine-tuning para sa iyong use case. Ideyal na balidong pamamaraaan lamang ito kung ang mga benepisyo ay mas malaki kaysa gastusin. Kapag nagpasya kang ituloy, panahon na upang isipin _paano_ mo ma-fine-tune ang pre-trained na modelo.

Gusto mo bang makakuha ng higit na insight sa proseso ng paggawa ng desisyon? Panoorin ang [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Paano tayo makakapag-fine-tune ng isang pre-trained na modelo?

Upang mag-fine-tune ng pre-trained na modelo, kailangan mong magkaroon ng:

- isang pre-trained na modelo na i-fine-tune
- isang dataset na gagamitin para sa fine-tuning
- isang training environment para patakbuhin ang fine-tuning job
- isang hosting environment upang ideploy ang fine-tuned na modelo

## Fine-Tuning Na Gagamitin

Nagbibigay ang mga sumusunod na resources ng step-by-step tutorials para gabayan ka sa isang tunay na halimbawa gamit ang napiling modelo na may magandang dataset. Para sundan ang mga tutorial na ito, kailangan mong magkaroon ng account sa partikular na provider, pati na rin ng access sa kaugnay na modelo at mga dataset.

| Provider     | Tutorial                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Matutunan kung paano i-fine-tune ang `gpt-35-turbo` para sa isang partikular na domain ("recipe assistant") sa pamamagitan ng paghahanda ng training data, pagpapatakbo ng fine-tuning job, at paggamit ng fine-tuned na modelo para sa inference.                                                                                                                                                                                   |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Matutunan kung paano i-fine-tune ang `gpt-35-turbo-0613` na modelo **sa Azure** sa pamamagitan ng mga hakbang upang gumawa at mag-upload ng training data, patakbuhin ang fine-tuning job, ideploy, at gamitin ang bagong modelo.                                                                                                                                                                                                     |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Tinatalakay ng blog post na ito ang fine-tuning ng isang _open LLM_ (hal. `CodeLlama 7B`) gamit ang [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) library at [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) kasama ng mga bukas na [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) sa Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | Ang AutoTrain (o AutoTrain Advanced) ay isang python library na binuo ng Hugging Face na nagpapahintulot ng fine-tuning para sa iba't ibang gawain kabilang ang LLM fine-tuning. Ang AutoTrain ay isang no-code solution at maaaring gawin ang fine-tuning sa sarili mong cloud, sa Hugging Face Spaces o lokal. Sinusuportahan nito ang web-based GUI, CLI, at pagsasanay gamit ang yaml config files.                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth)                                                         | Ang Unsloth ay isang open-source framework na sumusuporta sa LLM fine-tuning at reinforcement learning (RL). Pinapadali ng Unsloth ang lokal na pagsasanay, pagsusuri, at deployment gamit ang mga handang gamitin na [notebooks](https://github.com/unslothai/notebooks). Sinusuportahan din nito ang text-to-speech (TTS), BERT, at multimodal na mga modelo. Para magsimula, basahin ang kanilang step-by-step na [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                    |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Takdang Aralin

Pumili ng isa sa mga tutorial sa itaas at sundan ito. _Maaaring gawin namin ang isang bersyon ng mga tutorial na ito sa Jupyter Notebooks sa repo na ito bilang sanggunian lamang. Mangyaring gamitin ang orihinal na mga pinanggalingan nang direkta upang makuha ang pinakabagong mga bersyon_.

## Mahusay na Gawain! Ipagpatuloy ang Iyong Pag-aaral.

Pagkatapos makumpleto ang leksyon na ito, bisitahin ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Binabati kita!! Nakumpleto mo na ang huling leksyon mula sa v2 na serye para sa kursong ito! Huwag tumigil sa pag-aaral at paggawa. \*\*Tingnan ang [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) na pahina para sa listahan ng mga karagdagang mungkahi para sa paksang ito lamang.

Ang aming v1 na serye ng mga leksyon ay na-update din na may higit pang mga takdang aralin at mga konsepto. Kaya maglaan ng isang minuto upang sariwain ang iyong kaalaman - at mangyaring [ibahagi ang iyong mga tanong at puna](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) upang matulungan kaming pagbutihin ang mga leksyon na ito para sa komunidad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagaman nagsusumikap kaming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na may ganap na awtoridad. Para sa mga mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling-tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->