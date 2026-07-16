[![Open Source Models](../../../translated_images/tl/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning Ng Iyong LLM

Ang paggamit ng malalaking modelo ng wika upang bumuo ng mga generative AI application ay may kalakip na mga bagong hamon. Isang mahalagang isyu ay ang pagtitiyak ng kalidad ng tugon (katumpakan at kaugnayan) sa nilalamang nililikha ng modelo para sa isang partikular na kahilingan ng gumagamit. Sa mga naunang aralin, tinalakay natin ang mga teknik katulad ng prompt engineering at retrieval-augmented generation na sinusubukan lutasin ang problema sa pamamagitan ng _pagbabago ng prompt input_ sa umiiral na modelo.

Sa aralin ngayon, tatalakayin natin ang isang ikatlong teknik, ang **fine-tuning**, na sinusubukang tugunan ang hamon sa pamamagitan ng _muling pagsasanay mismo ng modelo_ gamit ang karagdagang datos. Suriin natin ang mga detalye.

## Mga Layunin ng Pagkatuto

Inilalahad ng araling ito ang konsepto ng fine-tuning para sa mga pre-trained na modelo ng wika, sinusuri ang mga benepisyo at hamon ng pamamaraang ito, at nagbibigay ng gabay kung kailan at paano gagamitin ang fine-tuning upang mapabuti ang pagganap ng iyong mga generative AI na modelo.

Sa pagtatapos ng araling ito, inaasahan mong masagot ang mga sumusunod na tanong:

- Ano ang fine-tuning para sa mga modelo ng wika?
- Kailan, at bakit, kapaki-pakinabang ang fine-tuning?
- Paano ako makakapag-fine-tune ng isang pre-trained na modelo?
- Ano ang mga limitasyon ng fine-tuning?

Handa ka na ba? Magsimula na tayo.

## Gabay na May Larawan

Gusto mo bang makita ang kabuuang larawan ng tatalakayin natin bago magsimula? Tingnan ang gabay na ito na may mga larawan na naglalarawan ng paglalakbay sa pag-aaral para sa araling ito - mula sa pag-aaral ng mga pangunahing konsepto at motibasyon para sa fine-tuning, hanggang sa pag-unawa sa proseso at pinakamahuhusay na gawain sa pagsasagawa ng fine-tuning. Ito ay isang kaakit-akit na paksa para sa eksplorasyon, kaya huwag kalimutang tingnan ang [Mga Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para sa karagdagang mga link na susuporta sa iyong sariling paglalakbay sa pagkatuto!

![Illustrated Guide to Fine Tuning Language Models](../../../translated_images/tl/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Ano ang fine-tuning para sa mga modelo ng wika?

Sa kahulugan, ang malalaking modelo ng wika ay _pre-trained_ sa malaking dami ng teksto mula sa iba't ibang pinagmulan kabilang ang internet. Tulad ng natutunan natin sa mga naunang aralin, kailangan natin ng mga teknik tulad ng _prompt engineering_ at _retrieval-augmented generation_ upang mapabuti ang kalidad ng mga tugon ng modelo sa mga tanong ng gumagamit ("prompts").

Isang tanyag na teknik sa prompt-engineering ay ang pagbibigay sa modelo ng mas maraming gabay sa kung ano ang inaasahan sa tugon, alinman sa pamamagitan ng pagbibigay ng _mga tagubilin_ (hayagang gabay) o _pagbibigay ng ilang mga halimbawa_ (tahi-tahing gabay). Tinatawag itong _few-shot learning_ ngunit may dalawang limitasyon ito:

- Maaaring pigilan ng mga limitasyon sa token ng modelo ang dami ng mga halimbawang maibibigay mo, at mabawasan ang bisa.
- Ang gastos ng mga token ng modelo ay maaaring maging mahal upang magdagdag ng mga halimbawa sa bawat prompt, at limitahan ang kakayahang umangkop.

Ang fine-tuning ay isang karaniwang gawain sa mga sistema ng machine learning kung saan kinukuha natin ang isang pre-trained na modelo at muling sinasanay ito gamit ang bagong datos upang mapabuti ang pagganap nito sa isang partikular na gawain. Sa konteksto ng mga modelo ng wika, maaari nating i-fine-tune ang pre-trained na modelo _gamit ang isang maingat na napiling set ng mga halimbawa para sa isang partikular na gawain o aplikasyon_ upang lumikha ng isang **custom na modelo** na maaaring mas tumpak at mas kaugnay para sa partikular na gawain o larangan. Isang karagdagang benepisyo ng fine-tuning ay maaari rin nitong bawasan ang bilang ng mga halimbawang kailangan para sa few-shot learning - na nagpapababa ng paggamit ng token at mga kaugnay na gastos.

## Kailan at bakit dapat tayong mag-fine-tune ng mga modelo?

Sa _kontekstong ito_, kapag pinag-uusapan natin ang fine-tuning, tinutukoy natin ang **supervised** na fine-tuning kung saan ang muling pagsasanay ay ginagawa sa pamamagitan ng **pagdagdag ng bagong datos** na hindi kabilang sa orihinal na training dataset. Ito ay naiiba sa unsupervised na approach sa fine-tuning kung saan muling sinasanay ang modelo gamit ang orihinal na datos, ngunit may ibang hyperparameters.

Ang mahalagang tandaan ay ang fine-tuning ay isang advanced na teknik na nangangailangan ng isang antas ng kadalubhasaan upang makamit ang nais na resulta. Kung hindi ito isasagawa ng tama, maaaring hindi ito magbigay ng inaasahang pagbuti, at maaari pang mas lumala ang pagganap ng modelo para sa iyong target na larangan.

Kaya, bago mo matutunan ang "paano" i-fine-tune ang mga modelo ng wika, kailangan mong malaman ang "bakit" dapat mong piliin ang paraang ito, at "kailan" sisimulan ang proseso ng fine-tuning. Magsimula sa pagtatanong sa iyong sarili ng mga tanong na ito:

- **Gamit na Layunin**: Ano ang iyong _use case_ para sa fine-tuning? Anong aspeto ng kasalukuyang pre-trained na modelo ang nais mong pagbutihin?
- **Mga Alternatibo**: Nasubukan mo na ba ang _ibang mga teknik_ upang makamit ang nais na resulta? Gamitin ang mga ito bilang baseline para sa paghahambing.
  - Prompt engineering: Subukan ang mga teknik gaya ng few-shot prompting na may mga halimbawa ng kaugnay na mga tugon sa prompt. Suriin ang kalidad ng mga tugon.
  - Retrieval Augmented Generation: Subukan ang pagdagdag ng mga query result sa mga prompt sa pamamagitan ng paghahanap sa iyong datos. Suriin ang kalidad ng mga tugon.
- **Mga Gastos**: Natukoy mo na ba ang mga gastos para sa fine-tuning?
  - Tunability - available ba ang pre-trained na modelo para sa fine-tuning?
  - Pagsisikap - para sa paghahanda ng training data, pagsusuri at pag-aayos ng modelo.
  - Compute - para sa pagpapatakbo ng mga fine-tuning na trabaho, at pag-deploy ng fine-tuned na modelo
  - Datos - access sa sapat na kalidad ng mga halimbawa para sa epekto ng fine-tuning
- **Mga Benepisyo**: Nakumpirma mo na ba ang mga benepisyo ng fine-tuning?
  - Kalidad - nalampasan ba ng fine-tuned na modelo ang baseline?
  - Gastos - nabawasan ba nito ang paggamit ng token sa pamamagitan ng pagpapasimple ng mga prompt?
  - Kakayahang Palawakin - maaari mo bang gamitin muli ang base na modelo para sa mga bagong larangan?

Sa pagsagot sa mga tanong na ito, dapat mong masuri kung ang fine-tuning ay ang tamang paraan para sa iyong use case. Sa ideal na sitwasyon, ang pamamaraang ito ay katanggap-tanggap lamang kung ang mga benepisyo ay mas malaki kaysa sa mga gastos. Kapag nagpasya ka nang ituloy, panahon na para pag-isipan ang _paano_ mo maaaring i-fine tune ang pre-trained na modelo.

Nais mo bang magkaroon ng higit pang kaalaman sa proseso ng paggawa ng desisyon? Panoorin ang [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## Paano tayo makakapag-fine-tune ng isang pre-trained na modelo?

Upang makapag-fine-tune ng isang pre-trained na modelo, kailangan mo ng:

- isang pre-trained na modelo na ia-fine-tune
- isang dataset na gagamitin para sa fine-tuning
- isang training environment upang patakbuhin ang fine-tuning job
- isang hosting environment upang ideploy ang fine-tuned na modelo

## Fine-Tuning Sa Gawa

> **Tandaan:** Ang `gpt-35-turbo` / `gpt-3.5-turbo`, na binanggit sa ilang mga tutorial sa ibaba, ay hindi na ginagamit para sa parehong inference at fine-tuning. Kung magsisimula ka ng bagong fine-tuning na trabaho ngayon, piliin ang kasalukuyang suportadong modelo - halimbawa `gpt-4o-mini` o `gpt-4.1-mini`. Tingnan ang [Fine-tuning models list](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para sa kasalukuyang listahan ng mga fine-tunable na modelo. Nananatiling naaangkop ang mga konsepto at hakbang sa mga tutorial na ito.

Ang mga sumusunod na sanggunian ay nagbibigay ng hakbang-hakbang na mga tutorial upang gabayan ka sa isang totoong halimbawa gamit ang napiling modelo at maingat na napiling dataset. Upang pagdaanan ang mga tutorial na ito, kailangan mong magkaroon ng account sa partikular na provider, kasama ang access sa kaukulang modelo at dataset.

| Provider     | Tutorial                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Matutunan kung paano i-fine-tune ang `gpt-35-turbo` para sa isang partikular na larangan ("recipe assistant") sa pamamagitan ng paghahanda ng training data, pagpapatakbo ng fine-tuning job, at paggamit ng fine-tuned na modelo para sa inference.                                                                                                                                                                                                                  |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Matutunan kung paano i-fine-tune ang modelo `gpt-35-turbo-0613` **sa Azure** sa pamamagitan ng mga hakbang na lumikha at mag-upload ng training data, pagpapatakbo ng fine-tuning job. Idedeploy at gagamitin ang bagong modelo.                                                                                                                                                                                                                                              |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Ang blog na ito ay naglalakad sa iyo sa fine-tuning ng isang _open LLM_ (hal: `CodeLlama 7B`) gamit ang [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) na aklatan at [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) gamit ang mga open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) sa Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | Ang AutoTrain (o AutoTrain Advanced) ay isang python na aklatan na binuo ng Hugging Face na nagpapahintulot ng fine-tuning para sa maraming iba't ibang gawain kabilang ang LLM fine-tuning. Ang AutoTrain ay isang no-code na solusyon at maaaring gawin ang fine-tuning sa iyong sariling cloud, sa Hugging Face Spaces o lokal. Sinusuportahan nito ang web-based GUI, CLI at pagsasanay gamit ang yaml config files.                                        |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Ang Unsloth ay isang open-source framework na sumusuporta sa LLM fine-tuning at reinforcement learning (RL). Pinapasimple ng Unsloth ang lokal na pagsasanay, pagsusuri, at deployment gamit ang mga handang gamitin na [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). Sinusuportahan din nito ang text-to-speech (TTS), BERT at mga multimodal na modelo. Para magsimula, basahin ang step-by-step na [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Takdang-Aralin

Pumili ng isa sa mga tutorial sa itaas at pagdaanan ito. _Maaring gumawa kami ng bersyon ng mga tutorial na ito sa Jupyter Notebooks sa repo na ito para sa sanggunian lamang. Mangyaring gamitin ang orihinal na mga sanggunian nang direkta upang makuha ang pinakabagong mga bersyon_.

## Magaling na Trabaho! Ipagpatuloy ang Iyong Pagkatuto.

Pagkatapos matapos ang araling ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pagpapalawak ng iyong kaalaman sa Generative AI!

Congratulations!! Nakumpleto mo na ang huling aralin mula sa v2 series para sa kursong ito! Huwag tumigil sa pag-aaral at paggawa. \*\*Tingnan ang [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) na pahina para sa listahan ng karagdagang mga mungkahi para sa paksang ito lamang.

Na-update din ang aming v1 series ng mga aralin na may higit pang mga takdang-aralin at konsepto. Kaya maglaan ng isang minuto para sariwain ang iyong kaalaman - at mangyaring [ibahagi ang iyong mga tanong at puna](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) upang matulungan kaming pagbutihin ang mga araling ito para sa komunidad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->