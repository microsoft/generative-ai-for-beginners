# Exploring and comparing different LLMs

[![Exploring and comparing different LLMs](../../../translated_images/pcm/02-lesson-banner.ef94c84979f97f60.webp)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Click the image above to view video of this lesson_

Wit di last lesson, we don see how Generative AI dey change technology land, how Large Language Models (LLMs) dey work and how business - like our startup - fit use dem for their own mata dem and flex! For dis chapter, we wan look compare and difference different kain big language models (LLMs) to sabi their better side and wetin no too better.

Di next step for our startup journey na to yarn di current LLMs dem and sabi which one go fit our own use.

## Introduction

Dis lesson go cover:

- Different kain LLMs wey dey for di current land.
- How to try am, change am small-small, and compare different models for your own use for Azure.
- How to run one LLM.

## Learning Goals

After you finish dis lesson, you go fit:

- Pick di correct model for your use.
- Sabi how to test, change, and improve your model work.
- Know how business dem dey run models.

## Understand different types of LLMs

LLMs fit get plenty kind based on how dem dem set up, data wey dem use learn, and wetin you wan use am do. If we sabi dis, e go help our startup pick di right model for di matter, and sabi how to test, change, and better am.

Plenty kain LLM models dey, how you go take choose model depend on wetin you wan use am for, your data, how much money you ready spend and more.

If na text, audio, video, image generation or whatever you wan use model for, you fit pick better model wey suit dat work.

- **Audio and speech recognition**. Whisper-style models still good for general speech recognition, but now production also get newer speech-to-text models like `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, and diarization versions. You suppose check language wey e fit cover, diarization, support for real-time, delay, and how e go cost you. Learn more for [OpenAI speech-to-text documentation](https://platform.openai.com/docs/guides/speech-to-text?WT.mc_id=academic-105485-koreyst).

- **Image generation**. DALL-E and Midjourney na popular options for image generation, but current OpenAI image APIs dey focus on GPT Image models like `gpt-image-2`, while Stable Diffusion, Imagen, Flux, and other families still dey common. Compare how prompt dem follow, editing support, style control, safety rules, and licenses. Learn more for [OpenAI image generation guide](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst) and Chapter 9 for dis course.

- **Text generation**. Text models now get frontier models, reasoning models, smaller low-latency models, and open-weight models. Examples na OpenAI GPT-5.x, Anthropic Claude 4.x, Google Gemini 3.x, Meta Llama 4, and Mistral. No just pick by release date or price; check task quality, delay time, context window, tool use, safety, place e dey, and total cost. [Microsoft Foundry model catalog](https://ai.azure.com/catalog?WT.mc_id=academic-105485-koreyst) good place to compare models wey dey for Azure.

- **Multi-modality**. Many models now fit handle more than text. Some fit use image, audio, or video for input; some fit call tools; and special models fit generate images, audio, or video. Example, current OpenAI models fit text and image input, Gemini models fit text, code, image, audio, video depending on which one, and Llama 4 Scout and Maverick na open-weight multimodal models. Always check model card for supported input and output before arrangement.

If you pick model, you go get some basic things, but sometimes e no go reach. Many times, you get company own data wey you go need talk for LLM about. Plenty ways dey to take do am, we go explain more for next sections.

### Foundation Models versus LLMs

Di term Foundation Model na [Stanford researchers coined am](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst), e mean AI model wey follow some rules like:

- **Dem dey train am with unsupervised learning or self-supervised learning**, so dem dey learn with multi-modal data wey no get labels, and dem no need human to mark or label data to teach am.
- **Dem big models**, dem get very deep neural network wey train for billions parameters.
- **Dem dey meant to be base for oda models**; dem fit be starting point for other models to build on, wey fit adjust with fine-tuning.

![Foundation Models versus LLMs](../../../translated_images/pcm/FoundationModel.e4859dbb7a825c94.webp)

Image source: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

To make am clear, make we take ChatGPT example. Early ChatGPT versions use GPT-3.5 as foundation model. OpenAI use chat-specific data and alignment way to make tuned version wey better for chat, like chatbot. Modern AI service fit use plenty model variants, so service name and model name no always be the same.

![Foundation Model](../../../translated_images/pcm/Multimodal.2c389c6439e0fc51.webp)

Image source: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus Proprietary Models

Another way to put LLMs different na to check if dem open-weight, open-source, or proprietary.

Open-source and open-weight models dey give model artifacts to check, download, or customize, but licenses different. Some full open source, others na open-weight but with use restrictions. Dem useful if business want control how dem run am, where dem keep data, cost, or customize. But team need check license terms, serving costs, maintenance, security updates, and eval quality before use for production. Examples na [Meta Llama 4](https://ai.meta.com/blog/llama-4-multimodal-intelligence/?WT.mc_id=academic-105485-koreyst), some [Mistral models](https://docs.mistral.ai/models/overview?WT.mc_id=academic-105485-koreyst), and many models for [Hugging Face](https://huggingface.co/models?WT.mc_id=academic-105485-koreyst).

Proprietary models belong to provider and dem host am. Dem usually optimize for managed production use and fit get strong support, safety system, tool integration, and scalable. But customer no fit check or change model weights, and dem need read provider terms for privacy, retention, compliance, and use rules. Examples na [OpenAI models](https://platform.openai.com/docs/models?WT.mc_id=academic-105485-koreyst), [Google Gemini](https://deepmind.google/models/gemini/pro/?WT.mc_id=academic-105485-koreyst), and [Anthropic Claude](https://platform.claude.com/docs/en/about-claude/models/overview?WT.mc_id=academic-105485-koreyst).

### Embedding versus Image generation versus Text and Code generation

LLMs fit also different based on their output.

Embeddings na models wey fit turn text to number, wey dem dey call embedding, dis na number way represent di input text. Embeddings help machine sabi how words or sentences take relate, and other models fit use am as input, like classification models or clustering models wey better for numbers. Embedding models usual for transfer learning, where model dey built for surrogate task where data plenty, then dem reuse model weights (embeddings) for other tasks. Example na [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/pcm/Embedding.c3708fe988ccf760.webp)

Image generation models na dem wey dey generate images. Dem dey use am for image editing, image synthesis, and image translation. Dem dey train these models on plenty image data, like [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), and fit use am generate new images or edit current images with inpainting, super-resolution, and colorize techniques. Examples na [GPT Image models](https://platform.openai.com/docs/guides/images?WT.mc_id=academic-105485-koreyst), [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst), and Imagen models.

![Image generation](../../../translated_images/pcm/Image.349c080266a763fd.webp)

Text and code generation models dey generate text or code. Dem dey use am for text summarization, translation, and question-answering. Text models dey train on plenty text data, like [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), and fit generate new text or answer questions. Code generation models, like [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), dey train on plenty code data like GitHub, fit generate new code or fix code bugs.

![Text and code generation](../../../translated_images/pcm/Text.a8c0cf139e5cc2a0.webp)

### Encoder-Decoder versus Decoder-only

To yarn about different architectures for LLMs, make we use example.

Imagine your manager give you task to write quiz for students. You get two colleagues; one dey create content, the other dey check am.

Content creator na like decoder-only model: fit look topic, see wetin you don write, then continue to write based on dat. Dem good for writing engaging and informative content, but no too fit for classification, retrieving, or encoding info. Example of decoder-only model na GPT and Llama models.

Reviewer na like Encoder-only model: dem dey look content and answers, dey notice relationship and context, but dem no too fit generate content. Example of Encoder-only model na BERT.

Imagine person fit dey create and review quiz, na Encoder-Decoder model. Examples na BART and T5.

### Service versus Model

Now, make we yarn difference between service and model. Service na product from Cloud Service Provider, usually arrangement of models, data, and other parts. Model na core part of service, often foundation model like LLM.

Services dey optimize for production and fit dey easier to use than models, with graphical user interface. But services no always free, fit need subscription or payment to use, so you fit use provider equipment and resources, save money and scale fast. Example na [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), wey dey pay-as-you-go, mean say user dey pay based on how much dem use the service. Azure OpenAI Service get enterprise-grade security and responsible AI framework on top of models.

Models na neural network artifacts: parameters, weights, architecture, tokenizer, and config. To run model locally or private place, you need correct hardware, server setup, monitoring, and open-source/open-weight license or commercial license. Open-weight models like Llama 4 or Mistral models fit self-host, but you still need machine power and know-how.

## How to test and iterate with different models to understand performance on Azure


Wen our team don explore di current LLMs landscape and identify some beta candidates for dia scenarios, di next step na to test dem on dia data and for dia workload. Dis na iterative process, wey dem dey do by experiments and measures.
Most of di models wey we mention for previous paragraphs (OpenAI models, open-weight models like Llama 4 and Mistral, and Hugging Face models) dey available for [Microsoft Foundry Models](https://learn.microsoft.com/azure/foundry/concepts/foundry-models-overview?WT.mc_id=academic-105485-koreyst).

[Microsoft Foundry](https://learn.microsoft.com/azure/foundry/what-is-foundry?WT.mc_id=academic-105485-koreyst), wey dem use to call am Azure AI Studio/Azure AI Foundry, na one single Azure platform for building AI apps and agents. E dey help developers manage di lifecycle from experimentation and evaluation to deployment, monitoring, and governance. Di model catalog for Microsoft Foundry dey allow di user to:

- Find di foundation model wey you get interest for inside di catalog, including models wey Azure sell and models from partners and community providers. Users fit filter by task, provider, license, deployment option, or name.

![Model catalog](../../../translated_images/pcm/AzureAIStudioModelCatalog.3cf8a499aa8ba031.webp)

- Review di model card, wey get detailed description of how dem intend to use am and training data, code samples and evaluation results for di internal evaluations library.

![Model card](../../../translated_images/pcm/ModelCard.598051692c6e400d.webp)

- Compare benchmarks across models and datasets wey dey inside di industry to sabi which one fit the business scenario, through di [Model Benchmarks](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst) pane.

![Model benchmarks](../../../translated_images/pcm/ModelBenchmarks.254cb20fbd06c03a.webp)

- Fine-tune supported models on custom training data to make di model perform beta for one kind workload, using di experimentation and tracking capabilities of Microsoft Foundry.

![Model fine-tuning](../../../translated_images/pcm/FineTuning.aac48f07142e36fd.webp)

- Deploy di original pre-trained model or di fine-tuned version go one remote real-time inference endpoint, using managed compute or serverless deployment option, so dat applications fit use am.

![Model deployment](../../../translated_images/pcm/ModelDeploy.890da48cbd0bccdb.webp)

> [!NOTE]
> No be all models for di catalog dey available now for fine-tuning and/or pay-as-you-go deployment. Check di model card for details on di model's capabilities and limitations.

## How to Make LLM Results Beta Pass

We don explore different kinds LLMs with our startup team and one cloud platform (Microsoft Foundry) wey help us compare different models, try dem on test data, improve performance, and deploy dem on inference endpoints.

But wen dem go consider to fine-tune model instead of just using pre-trained one? E get oda ways to make model perform beta on specific workloads?

Business get plenti ways to get the results wey dem need from LLM. You fit choose different types of models wey different level of training when you dey deploy LLM for production, with different levels of complexity, cost, and quality. Here na some different ways:

- **Prompt engineering wit context**. Di idea na to provide enough context wen you prompt to make sure say you go get di right answers wey you need.

- **Retrieval Augmented Generation, RAG**. Your data fit dey for database or web endpoint, for example, so to make sure say dis data or part of am dey included wen you dey prompt, you fit fetch di correct data and put am for user prompt.

- **Fine-tuned model**. Here, you go train di model again on your own data wey make di model dey more correct and responsive to your needs but e fit cost pass.

![LLMs deployment](../../../translated_images/pcm/Deploy.18b2d27412ec8c02.webp)

Img source: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering wit Context

Pre-trained LLMs dey work well for general natural language tasks, even if na only short prompt you give dem, like sentence wey dem go complete or question – dis na di “zero-shot” learning.

But wen user fit frame dia query well, with detailed request and examples – di Context – di answer go more correct and go meet wetin user expect. For dis case, we dey call am “one-shot” learning if prompt get only one example and “few shot learning” if e get many examples.
Prompt engineering wit context na di most cheap way to start.

### Retrieval Augmented Generation (RAG)

LLMs get one limit wey be say dem fit use only di data wey dem train on to generate answer. Dis mean say dem no sabi anything wey happen after dem finish to train, and dem no fit access private information (like company data).
Dis one you fit solve am wit RAG, wey be technique wey add external data as chunks of documents into di prompt, making sure say e no pass prompt length limit. Dis one dey supported by Vector database tools (like [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) wey dey find di important chunks from different data sources and add am to di prompt Context.

Dis technique beta wella wen business no get enough data, time, or resources to fine-tune their LLM, but dem still want to improve how e perform for one kind workload and reduce di chance of false, old, or unsupported answers.

### Fine-tuned model

Fine-tuning na process wey use transfer learning to ‘adapt’ di model to one downstream task or solve one specific problem. Different from few-shot learning and RAG, e go create new model with new weights and biases. E need training examples wey get input (di prompt) and its output (di completion).
Dis one na di way wey you go choose if:

- **You wan use smaller task-specific models**. Business go like fine-tune smaller model for one small task instead of dey always prompt larger model, so e go cost less and e go fast.

- **You dey consider latency**. Latency dey important for one specific use-case, so e no possible to use long prompts or too many examples inside prompt wey fit learn from model.

- **You want stable behavior**. Business get many high-quality examples and want di model to always follow one kind pattern, output format, tone, or style for domain. If di problem na fresh facts or private knowledge wey dey change, use RAG instead of just fine-tuning.

### Training model from scratch

To train LLM from scratch na di hardest and most complex way, e go need plenty data, skilled people and correct computational power. You go only reason am if business get domain-specific use case and plenty domain-centric data.

## Knowledge check

Wetin fit be correct way to improve LLM completion results?

1. Prompt engineering wit context
1. RAG
1. Fine-tuned model

A: All three fit help. Start with prompt engineering and context for quick improvements, and use RAG when model need current facts or private business data. Choose fine-tuning when you get plenty good examples and want model to always follow task, format, tone, or domain pattern.

## 🚀 Challenge

Read more about how you fit [use RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) for your business.

## Beta Work, Continue Your Learning

After you finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to sabi more about Generative AI!

Head go Lesson 3 where we go look how to [build with Generative AI Responsibly](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->