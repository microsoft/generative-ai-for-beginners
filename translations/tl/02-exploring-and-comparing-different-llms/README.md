# Pagsusuri at paghahambing ng iba't ibang LLMs

[![Pagsusuri at paghahambing ng iba't ibang LLMs](../../../translated_images/tl/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _I-click ang larawan sa itaas upang panoorin ang video ng leksyon na ito_

Sa nakaraang leksyon, nakita natin kung paano binabago ng Generative AI ang tanawin ng teknolohiya, kung paano gumagana ang Malalaking Modelo ng Wika (LLMs) at kung paano maaaring gamitin ng isang negosyo - tulad ng aming startup - ang mga ito sa kanilang mga kaso ng paggamit at magpalago! Sa kabanatang ito, titingnan natin ang paghahambing at pagbibigay-kaibahan sa iba't ibang uri ng malalaking modelo ng wika (LLMs) upang maunawaan ang kanilang mga kalamangan at kahinaan.

Ang susunod na hakbang sa paglalakbay ng aming startup ay ang pagsiyasat sa kasalukuyang tanawin ng LLMs at pag-unawa kung alin ang angkop para sa aming kaso ng paggamit.

## Panimula

Saklaw ng leksyong ito:

- Iba't ibang uri ng LLMs sa kasalukuyang tanawin.
- Pagsubok, pag-uulit, at paghahambing ng iba't ibang modelo para sa iyong kaso ng paggamit sa Azure.
- Paano mag-deploy ng isang LLM.

## Mga Layunin sa Pagkatuto

Pagkatapos makumpleto ang leksyong ito, magagawa mong:

- Piliin ang tamang modelo para sa iyong kaso ng paggamit.
- Maunawaan kung paano subukan, ulitin, at pabutihin ang performance ng iyong modelo.
- Malaman kung paano nagde-deploy ng mga modelo ang mga negosyo.

## Unawain ang iba't ibang uri ng LLMs

Maaaring magkaroon ng maraming kategorya ang LLMs batay sa kanilang arkitektura, training data, at kaso ng paggamit. Ang pag-unawa sa mga pagkakaibang ito ay makakatulong sa aming startup na pumili ng tamang modelo para sa sitwasyon, at maunawaan kung paano subukan, ulitin, at pahusayin ang performance.

Maraming iba't ibang uri ng mga modelo ng LLM, ang pagpili mo ng modelo ay depende sa layunin mong gamitin ito, sa iyong data, kung gaano ka handang magbayad, at iba pa.

Depende kung gagamitin mo ang mga modelo para sa teksto, audio, video, pagbuo ng larawan, at iba pa, maaari kang pumili ng ibang uri ng modelo.

- **Pagrekognisa ng audio at pagsasalita**. Ang mga Whisper-style na modelo ay kapaki-pakinabang pa rin bilang mga pangkalahatang modelo ng pagsasalita, ngunit maliban dito, mayroon ding mas bagong mga speech-to-text models tulad ng `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, at mga variant ng diarization. Suriin ang saklaw ng wika, diarization, suporta sa real-time, latency, at gastos para sa iyong sitwasyon. Matuto pa sa [OpenAI speech-to-text documentation](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Pagbuo ng larawan**. Kilala ang DALL-E at Midjourney bilang mga pagpipilian sa pagbuo ng larawan, ngunit ang kasalukuyang OpenAI image APIs ay nakatuon sa GPT Image models tulad ng `gpt-image-2`, habang ang Stable Diffusion, Imagen, Flux, at iba pang pamilya ng mga modelo ay karaniwan ding pinipili. Ihambing ang pagsunod sa mga prompt, suporta sa pag-edit, kontrol ng estilo, pangangailangan sa kaligtasan, at lisensya. Matuto pa sa [OpenAI image generation guide](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) at Kabanata 9 ng kurikulum na ito.

- **Pagbuo ng teksto**. Sumasaklaw ngayon ang mga modelo ng teksto ng mga frontier models, reasoning models, mas maliliit na low-latency models, at open-weight models. Mga kasalukuyang halimbawa ay ang OpenAI GPT-5.x models, Anthropic Claude 4.x models, Google Gemini 3.x models, Meta Llama 4 models, at Mistral models. Huwag pumili lamang batay sa petsa ng paglabas o presyo; ihambing ang kalidad ng gawain, latency, context window, paggamit ng tool, asal sa kaligtasan, availability sa rehiyon, at kabuuang halaga. Ang [Microsoft Foundry model catalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) ay isang magandang lugar upang ihambing ang mga modelo na available sa Azure.

- **Multi-modality**. Maraming kasalukuyang modelo ang kayang magproseso ng higit pa sa teksto. Ang ilan ay tumatanggap ng input na larawan, audio, o video; ang ilan ay kayang tumawag ng mga tool; at may mga espesyal na modelo na kayang gumawa ng mga larawan, audio, o video. Halimbawa, sinusuportahan ng mga kasalukuyang OpenAI models ang teksto at input na larawan, kayang suportahan ng Gemini models ang teksto, code, larawan, audio, at video depende sa variant, at ang Llama 4 Scout at Maverick ay open-weight native multimodal models. Palaging suriin ang bawat card ng modelo para sa suporta sa input at output modalities bago bumuo ng workflow sa paligid nito.

Ang pagpili ng modelo ay nangangahulugan ng pagkuha mo ng ilang mga pangunahing kakayahan, na maaaring hindi sapat. Madalas ay may data na partikular sa kompanya na kailangan mong ipabatid sa LLM. May ilang iba't ibang mga opsyon kung paano ito lapitan, na tatalakayin pa sa mga susunod na seksyon.

### Foundation Models kumpara sa LLMs

Ang terminong Foundation Model ay [nalikha ng mga mananaliksik sa Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) at tinukoy bilang isang modelo ng AI na sumusunod sa ilang kriteriya, tulad ng:

- **Sila ay sinasanay gamit ang unsupervised learning o self-supervised learning**, ibig sabihin sinasanay sila sa hindi naka-label na multi-modal data, at hindi kailangan ng human annotation o labeling ng data para sa proseso ng pagsasanay.
- **Sila ay napakalalaking modelo**, batay sa napakalalim na neural networks na sinanay sa bilyon-bilyong parameter.
- **Karaniwan silang nilalayong magsilbing ‘foundation’ para sa ibang mga modelo**, ibig sabihin maaari silang gamitin bilang panimulang punto para sa iba pang mga modelo na itatayo sa ibabaw nito, na maaaring gawin sa pamamagitan ng fine-tuning.

![Foundation Models versus LLMs](../../../translated_images/tl/FoundationModel.e4859dbb7a825c94.webp)

Pinagmulan ng larawan: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Upang higit pang linawin ang pagkakaibang ito, gamitin natin ang ChatGPT bilang isang makasaysayang halimbawa. Ang mga unang bersyon ng ChatGPT ay gumamit ng GPT-3.5 bilang foundation model. Pagkatapos, ginamit ng OpenAI ang chat-specific na data at alignment techniques upang lumikha ng na-tune na bersyon na mas mahusay sa mga conversational na senaryo, tulad ng mga chatbot. Madalas na nagriroute ang mga modernong AI services sa pagitan ng iba't ibang variant ng modelo, kaya't ang pangalan ng serbisyo at pangalan ng underlying na modelo ay hindi palaging pareho.

![Foundation Model](../../../translated_images/tl/Multimodal.2c389c6439e0fc51.webp)

Pinagmulan ng larawan: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source kumpara sa Proprietary Models

Isa pang paraan upang ikategorya ang LLMs ay kung sila ay open-weight, open-source, o proprietary.

Ang mga open-source at open-weight models ay nagpapahintulot na makita, ma-download, o mabago ang mga artifacts ng modelo, ngunit nagkakaiba ang mga lisensya nila. Ang ilan ay ganap na open source, habang ang iba ay open-weight models na may mga limitasyon sa paggamit. Maaari silang maging kapaki-pakinabang kapag kailangan ng negosyo ng mas kontrol sa pag-deploy, lokalisasyon ng data, gastos, o customisasyon. Gayunpaman, kailangang suriin ng mga team ang mga termino ng lisensya, gastos sa serbisyo, maintenance, update sa seguridad, at kalidad ng ebalwasyon bago gamitin sa produksyon. Kabilang dito ang [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), ilan sa mga [Mistral models](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), at maraming mga modelo sa [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Ang mga proprietary models ay pag-aari at hinahost ng isang provider. Karaniwan silang optimized para sa managed production use at maaaring mag-alok ng matibay na suporta, kaligtasan, integrasyon ng tool, at scale. Gayunpaman, karaniwang hindi maaaring suriin o baguhin ng mga customer ang timbang ng modelo, at kailangang suriin ang mga tuntunin ng provider para sa privacy, pag-retain, pagsunod, at katanggap-tanggap na paggamit. Kabilang dito ang [OpenAI models](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), at [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding kumpara sa Pagbuo ng Larawan kumpara sa Pagbuo ng Teksto at Code

Maaari ring ikategorya ang LLMs ayon sa output na kanilang nililikha.

Ang mga embedding ay isang set ng mga modelo na kayang gawing numerikal na anyo ang teksto, na tinatawag na embedding, isang numerikal na representasyon ng input na teksto. Pinapadali ng embeddings para sa mga makina na maintindihan ang mga relasyon ng mga salita o pangungusap at maaaring gamitin bilang inputs ng ibang mga modelo, tulad ng classification models, o clustering models na mas mahusay sa numerikal na data. Ginagamit ang mga embedding models para sa transfer learning, kung saan ang isang modelo ay ginawa para sa surrogate na gawain na may maraming datos, at pagkatapos ay ginagamit muli ang timbang ng modelo (embeddings) para sa ibang downstream na mga gawain. Halimbawa ay ang [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/tl/Embedding.c3708fe988ccf760.webp)

Ang mga modelo para sa pagbuo ng larawan ay mga modelo na lumilikha ng mga larawan. Madalas silang ginagamit para sa pag-eedit ng larawan, synthesis ng larawan, at pagsasalin ng larawan. Kadalasang sinasanay ang mga image generation models sa malalaking dataset ng mga larawan tulad ng [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), at maaaring gamitin upang gumawa ng mga bagong larawan o mag-edit ng mga umiiral na larawan gamit ang inpainting, super-resolution, at techniques sa colorization. Mga halimbawa ay ang [GPT Image models](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), at Imagen models.

![Image generation](../../../translated_images/tl/Image.349c080266a763fd.webp)

Ang mga modelo ng pagbuo ng teksto at code ay mga modelo na lumilikha ng teksto o code. Madalas silang ginagamit para sa pagbubuod ng teksto, pagsasalin, at pagsagot ng tanong. Sinasanay ang mga text generation models sa malalaking dataset ng teksto tulad ng [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), at maaaring gamitin upang makabuo ng bagong teksto o sumagot ng mga tanong. Ang mga code generation models, tulad ng [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), ay karaniwang sinasanay sa malalaking dataset ng code mula sa GitHub, at maaaring gamitin upang makabuo ng bagong code o ayusin ang mga bug sa umiiral na code.

![Text and code generation](../../../translated_images/tl/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder kumpara sa Decoder-only

Upang pag-usapan ang iba't ibang uri ng arkitektura ng LLMs, gamitin natin ang isang talinghaga.

Isipin na binigyan ka ng iyong manager ng gawain na gumawa ng quiz para sa mga estudyante. Mayroon kang dalawang kasamahan; ang isa ay namamahala sa paggawa ng nilalaman at ang isa ay namamahala sa pagrerebyu.

Ang tagagawa ng nilalaman ay parang decoder-only model: kaya nilang tingnan ang paksa, makita kung ano ang sinusulat mo na, at magpatuloy sa paggawa ng nilalaman batay sa kontekstong iyon. Magaling sila sa pagsulat ng nakaka-engganyo at impormatibong nilalaman, ngunit hindi palaging sila ang pinakamahusay na pagpipilian kapag ang gawain ay classify lamang, retrieve, o encode ng impormasyon. Halimbawa ng decoder-only model families ay ang GPT at Llama models.

Ang tagarebyu ay parang encoder-only model, tinitingnan nila ang isinusulat na kurso at ang mga sagot, napapansin ang relasyon sa pagitan nila at nauunawaan ang konteksto, ngunit hindi sila magaling sa paggawa ng nilalaman. Halimbawa ng encoder-only model ay ang BERT.

Isipin mo na mayroon ding isang tao na kayang gumawa at magrebyu ng quiz, ito ay isang Encoder-Decoder model. Ilan sa mga halimbawa nito ay ang BART at T5.

### Serbisyo kumpara sa Modelo

Ngayon, pag-usapan natin ang kaibahan ng serbisyo at modelo. Ang serbisyo ay isang produkto na inaalok ng isang Cloud Service Provider, at karaniwang kumbinasyon ng mga modelo, data, at iba pang bahagi. Ang modelo ay ang pangunahing bahagi ng serbisyo, at karaniwang isang foundation model, tulad ng isang LLM.

Karaniwan ang mga serbisyo ay optimized para sa paggamit sa produksyon at mas madali silang gamitin kaysa sa mga modelo, sa pamamagitan ng graphical user interface. Ngunit hindi palaging libre ang mga serbisyo at maaaring kailanganin ng subscription o bayad para gamitin, bilang kapalit ng paggamit ng kagamitan at resources ng may-ari ng serbisyo, upang mapamahalaan ang gastos at madaling pag-scale. Isang halimbawa ng serbisyo ay ang [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-foundry/openai/overview?WT.mc_id=academic-105485-koreyst), na nag-aalok ng pay-as-you-go rate plan, ibig sabihin sinisingil ang mga user batay sa totoong gamit nila ng serbisyo. Nagbibigay din ang Azure OpenAI Service ng enterprise-grade security at responsable na AI framework sa ibabaw ng kakayahan ng mga modelo.

Ang mga modelo ay neural network artifacts: parameters, weights, arkitektura, tokenizer, at mga sumusuportang configuration. Ang pagpapatakbo ng isang modelo nang lokal o sa pribadong kapaligiran ay nangangailangan ng angkop na hardware, serving infrastructure, monitoring, at alinman sa compatible na open-source/open-weight license o commercial license. Ang mga open-weight models tulad ng Llama 4 o Mistral models ay maaaring i-host sariling sarili, ngunit kailangan pa rin ng computational power at operational expertise.

## Paano subukan at ulitin gamit ang iba't ibang mga modelo upang maunawaan ang performance sa Azure


Kapag nasuri na ng aming koponan ang kasalukuyang tanawin ng LLMs at nakapili ng ilang magagandang kandidato para sa kanilang mga senaryo, ang susunod na hakbang ay subukan ang mga ito gamit ang kanilang datos at kanilang trabaho. Ito ay isang paulit-ulit na proseso, ginagawa sa pamamagitan ng mga eksperimento at pagsukat.
Karamihan sa mga modelong nabanggit namin sa mga naunang talata (OpenAI models, open-weight models tulad ng Llama 4 at Mistral, at Hugging Face models) ay makukuha sa [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), na dating Azure AI Studio/Azure AI Foundry, ay isang pinagsama-samang platform ng Azure para sa paggawa ng mga AI na app at ahente. Tinutulungan nito ang mga developer na pamahalaan ang lifecycle mula sa eksperimento at pagsusuri hanggang sa deployment, pagmamanman, at pamamahala. Pinapayagan ng katalogo ng modelo sa Microsoft Foundry ang gumagamit na:

- Hanapin ang pangunahing modelo na interesado sa katalogo, kabilang ang mga modelong ibinebenta ng Azure at mga modelo mula sa mga partner at mga tagapagbigay ng komunidad. Maaaring salain ng mga gumagamit ayon sa gawain, tagapagbigay, lisensya, opsyon sa deployment, o pangalan.

![Model catalog](../../../translated_images/tl/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Suriin ang modelo card, kabilang ang detalyadong paglalarawan ng inaasahang gamit at mga datos ng pagsasanay, mga halimbawa ng code at mga resulta ng pagsusuri sa internal evaluations library.

![Model card](../../../translated_images/tl/ModelCard.598051692c6e400d.webp)

- Ihambing ang mga benchmark sa pagitan ng mga modelo at dataset na available sa industriya upang matantiya kung alin ang akma sa senaryo ng negosyo, sa pamamagitan ng [Model Benchmarks](https://learn.microsoft.com/azure/ai-foundry/concepts/model-benchmarks?WT.mc_id=academic-105485-koreyst) pane.

![Model benchmarks](../../../translated_images/tl/ModelBenchmarks.254cb20fbd06c03a.webp)

- I-fine-tune ang mga suportadong modelo gamit ang custom training data upang mapabuti ang performance ng modelo sa isang tiyak na trabaho, gamit ang mga kakayahan sa eksperimento at pagsubaybay ng Microsoft Foundry.

![Model fine-tuning](../../../translated_images/tl/FineTuning.aac48f07142e36fd.webp)

- I-deploy ang orihinal na pre-trained na modelo o ang fine-tuned na bersyon sa isang remote real-time inference endpoint, gamit ang managed compute o serverless deployment options, upang magamit ito ng mga aplikasyon.

![Model deployment](../../../translated_images/tl/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> Hindi lahat ng modelo sa katalogo ay kasalukuyang available para sa fine-tuning at/o pay-as-you-go na deployment. Suriin ang modelo card para sa mga detalye ng kakayahan at limitasyon ng modelo.

## Pagpapahusay ng mga Resulta ng LLM

Nasuri na namin kasama ang aming startup team ang iba't ibang klase ng LLMs at isang cloud platform (Microsoft Foundry) na nagpapahintulot sa amin na ihambing ang iba't ibang modelo, suriin ang mga ito gamit ang test data, pagbutihin ang performance, at i-deploy ang mga ito sa inference endpoints.

Ngunit kailan nila dapat isaalang-alang ang pag-fine-tune ng isang modelo sa halip na gumamit ng pre-trained na isa? Mayroon bang ibang paraan upang mapabuti ang performance ng modelo sa mga partikular na gawain?

Mayroong ilang mga paraan na puwedeng gamitin ng isang negosyo upang makuha ang mga resulta na kailangan nila mula sa isang LLM. Maaari kang pumili ng iba't ibang uri ng mga modelo na may iba't ibang antas ng pagsasanay kapag nagde-deploy ng LLM sa produksyon, na may iba't ibang antas ng pagiging kumplikado, gastos, at kalidad. Narito ang ilang mga iba't ibang paraan:

- **Prompt engineering na may konteksto**. Ang ideya ay magbigay ng sapat na konteksto kapag ikaw ay nag-prompt upang matiyak na makukuha mo ang mga sagot na kailangan mo.

- **Retrieval Augmented Generation, RAG**. Maaring ang iyong data ay nasa database o web endpoint halimbawa, upang matiyak na ang data na ito, o isang bahagi nito, ay maisama sa oras ng prompting, maaari mong kunin ang kaugnay na datos at gawing bahagi iyon ng prompt ng gumagamit.

- **Fine-tuned na modelo**. Dito, inyong pinalalim ang pagsasanay ng modelo gamit ang sariling datos na nagresulta sa pagiging mas tumpak at tumutugon sa iyong mga pangangailangan ngunit maaaring maging magastos.

![LLMs deployment](../../../translated_images/tl/Deploy.18b2d27412ec8c02.webp)

Pinagmulan ng Imahe: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering na may Konteksto

Ang mga pre-trained na LLM ay mahusay sa mga pangkalahatang gawain gamit ang natural na wika, kahit na kapag tinawag lamang gamit ang isang maikling prompt, tulad ng isang pangungusap na kailangang tapusin o isang tanong – ang tinatawag na “zero-shot” na pagkatuto.

Gayunpaman, mas naipapakita ng gumagamit ang kanilang query, gamit ang detalyadong kahilingan at mga halimbawa – ang Konteksto – mas tumpak at malapit sa inaasahan ng gumagamit ang magiging sagot. Sa ganitong kaso, pinag-uusapan natin ang “one-shot” na pagkatuto kung ang prompt ay may lamang isang halimbawa lamang at “few shot learning” kung ito ay may maramihang mga halimbawa.
Ang prompt engineering na may konteksto ang pinakamatipid na paraan upang magsimula.

### Retrieval Augmented Generation (RAG)

May limitasyon ang mga LLM na maaari lamang nilang gamitin ang datos na ginamit sa kanilang pagsasanay upang makabuo ng sagot. Ibig sabihin nito ay wala silang kaalaman tungkol sa mga pangyayaring naganap pagkatapos ng kanilang proseso ng pagsasanay, at hindi nila ma-access ang mga impormasyong hindi publiko (tulad ng datos ng kumpanya).
Ito ay maaaring malampasan sa pamamagitan ng RAG, isang teknika na pinalalawak ang prompt gamit ang panlabas na datos sa anyo ng mga piraso ng mga dokumento, isinasaalang-alang ang mga limitasyon sa haba ng prompt. Ito ay sinusuportahan ng mga tool ng Vector database (tulad ng [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) na kumukuha ng mga kapaki-pakinabang na piraso mula sa iba't ibang pre-defined na mga pinagkukunan ng datos at idinadagdag ang mga ito sa Konteksto ng prompt.

Napaka-kapaki-pakinabang ng teknikang ito kapag ang negosyo ay walang sapat na datos, sapat na oras, o mga resources upang mag-fine-tune ng LLM, ngunit nais pa ring pagbutihin ang performance sa isang tiyak na trabaho at bawasan ang mga panganib ng mga hallucinated, lipas na, o hindi suportadong mga sagot.

### Fine-tuned na modelo

Ang fine-tuning ay isang proseso na gumagamit ng transfer learning upang ‘iaakma’ ang modelo sa isang downstream na gawain o upang malutas ang isang tiyak na problema. Naiiba mula sa few-shot learning at RAG, nagreresulta ito sa isang bagong modelong nabubuo, na may mga na-update na timbang at bias. Nangangailangan ito ng isang set ng mga halimbawa ng pagsasanay na binubuo ng isang input lamang (ang prompt) at ang katumbas nitong output (ang completion).
Ito ang magiging gustong-gusto na paraan kung:

- **Paggamit ng mas maliit na task-specific na mga modelo**. Nais ng negosyo na i-fine-tune ang mas maliit na modelo para sa isang makitid na gawain kaysa paulit-ulit na mag-prompt sa isang mas malaking frontier na modelo, na nagreresulta sa mas matipid at mas mabilis na solusyon.

- **Pagsasaalang-alang sa latency**. Mahalaga ang latency para sa isang partikular na use-case, kaya hindi puwedeng gumamit ng sobrang mahahabang prompt o ang bilang ng mga halimbawa na kailangang matutunan mula sa modelo ay hindi kasya sa limitasyon ng haba ng prompt.

- **Pag-aakma ng matatag na pag-uugali**. Mayroon ang negosyo ng maraming mataas na kalidad na mga halimbawa at nais na ang modelo ay sunud-sunurin nang tuloy-tuloy ang isang pattern ng gawain, format ng output, tono, o istilong nakatuon sa isang partikular na domain. Kung ang pangunahing problema ay mga bagong katotohanan o pribadong kaalaman na madalas nagbabago, gamitin ang RAG sa halip na umasa lamang sa fine-tuning.

### Sinanay na modelo

Ang pagsasanay ng isang LLM mula sa simula ay walang duda ang pinaka-mahirap at pinakakomplikadong paraan na pwedeng gawin, nangangailangan ng napakalaking dami ng datos, mahuhusay na resources, at angkop na kapangyarihang pangkompyut. Dapat lamang isaalang-alang ang opsyong ito sa isang senaryong may domain-specific na use case at malaking dami ng domain-centric na datos.

## Pag-susulit ng Kaalaman

Ano ang maaaring maging magandang paraan upang mapabuti ang mga resulta ng LLM completion?

1. Prompt engineering na may konteksto
1. RAG
1. Fine-tuned na modelo

A: Lahat ng tatlo ay makakatulong. Magsimula sa prompt engineering at konteksto para sa mabilisang pagpapabuti, at gamitin ang RAG kapag kailangan ng modelo ng kasalukuyang mga katotohanan o pribadong datos ng negosyo. Piliin ang fine-tuning kapag mayroon kang sapat na mataas na kalidad na mga halimbawa at kailangan ang modelo na consistent na sundin ang isang gawain, format, tono, o pattern ng domain.

## 🚀 Hamon

Magbasa pa tungkol sa kung paano mo maaaring [gamitin ang RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para sa iyong negosyo.

## Mahusay na Trabaho, Ipagpatuloy ang Iyong Pag-aaral

Pagkatapos tapusin ang leksyon na ito, tingnan ang aming [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) upang ipagpatuloy ang pag-level up ng iyong kaalaman sa Generative AI!

Pumunta sa Lesson 3 kung saan titingnan natin kung paano [bumuo gamit ang Generative AI nang Responsable](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->