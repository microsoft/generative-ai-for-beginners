[![Open Source Models](../../../translated_images/pcm/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Fine-Tuning Your LLM

Using large language models to build generative AI applications dey come wit new wahala dem. One important matter na to make sure say the answer quality (accuracy and relevance) for content wey the model create for one kain user request dey correct. For previous lesson dem, we talk about techniques like prompt engineering and retrieval-augmented generation wey try solve di problem by _modifying di prompt input_ to di model wey dey already.

For today lesson, we go talk about one oda technique, **fine-tuning**, wey try solve di matter by _retraining di model itsef_ wit more data. Make we waka inside di details.

## Learning Objectives

This lesson go introduce di idea of fine-tuning for pre-trained language models, talk about di benefits and wahala dem for dis approach, and give you guide on how and when to use fine tuning to make your generative AI models better.

After dis lesson finish, you suppose fit answer dis questions dem:

- Wetin be fine tuning for language models?
- When and why you go find fine tuning useful?
- How I fit fine-tune one pre-trained model?
- Wetin be di limitations of fine-tuning?

You ready? Make we begin.

## Illustrated Guide

You want sabi di big picture of wetin we go cover before you enter? Check dis illustrated guide wey dey show di learning journey for dis lesson - from learning the main concept and motivation for fine-tuning, to understanding the process and beta way dem to do di fine-tuning work. Dis na one interesting topic to explore, so no forget to check di [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) page for more links wey go support your self-guided learning journey!

![Illustrated Guide to Fine Tuning Language Models](../../../translated_images/pcm/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Wetin be fine-tuning for language models?

By definition, large language models dey _pre-trained_ on plenti text wey dem collect from everywhere including internet. As we don learn for previous lesson dem, we need techniques like _prompt engineering_ and _retrieval-augmented generation_ to make model response to user question ("prompts") better.

One popular prompt-engineering way na to give model more correct guidance about wetin the answer suppose be either by giving _instructions_ (clear guide) or _giving am small example_ (soft guide). Dis one dem dey call _few-shot learning_ but e get two wahala:

- Model token limits fit limit how many examples you fit give, and fit reduce how effective e go be.
- Model token costs fit make am expensive to add example to every prompt, and limit flexibility.

Fine-tuning na something wey machine learning systems dey do well, where you go take one pre-trained model and train am again with new data to make am better for one particular task. For language models, you fit fine-tune the pre-trained model _wit set of selected examples for one task or area_ to make one **custom model** wey fit dey more accurate and relevant for that specific task or area. One side benefit of fine-tuning be say e fit reduce how many examples you need for few-shot learning - so token usage and cost fit low.

## When and why we suppose fine-tune models?

For _dis_ matter, when we talk fine-tuning, na **supervised** fine-tuning we mean where you dey train am again by **adding new data** wey no dey the original training data set inside. Dis one different from unsupervised fine-tuning wey the model train again for the original data but with different hyperparameters.

The main thing to remember be say fine-tuning na advanced way wey need some level of skill to get correct results. If you do am wrong, e fit no give better improvement, and e fit even make model perform worse for your target area.

So before you learn "how" to fine-tune language models, you need know "why" you gats do am, and "when" to start fine-tuning. Start by asking yourself this questions:

- **Use Case**: Wetin be your _use case_ for fine-tuning? Which part of the current pre-trained model you want improve?
- **Alternatives**: You don try _other techniques_ to get di result wey you want? Use them to create one baseline for comparison.
  - Prompt engineering: Try things like few-shot prompting wit relevant prompt responses examples. Check how beta di responses be.
  - Retrieval Augmented Generation: Try add prompts with query results wey you find for your data search. Check how di responses perform.
- **Costs**: You don check di costs for fine-tuning?
  - Tunability - the pre-trained model dey available for fine-tuning?
  - Effort - to prepare training data, check & improve model.
  - Compute - to run fine-tuning jobs and deploy fine-tuned model
  - Data - get enough good-quality examples to fit the fine-tuning work well
- **Benefits**: You don confirm the benefits of fine-tuning?
  - Quality - the fine-tuned model perform pass the baseline?
  - Cost - e reduce token usage by making prompts simple?
  - Extensibility - you fit use the base model again for new areas?

If you fit answer this questions, you fit decide if fine-tuning be di correct method for your use case. Better still, make sure say the benefit pass the costs. When you don decide to go ahead, na time to think about _how_ you fit fine tune the pre-trained model.

You want know more for decision-making? Watch [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## How we fit fine-tune pre-trained model?

To fine-tune pre-trained model, you need get:

- pre-trained model wey you fit fine-tune
- dataset for fine-tuning
- training place to run fine-tuning task
- place to host fine-tuned model

## Fine-Tuning on Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) na where you go fine-tune, deploy, and manage custom models on Azure today (e join together di tins wey dem dey call Azure OpenAI Studio and Azure AI Studio befor). Before you start your job, e good to sabi the choices Foundry give you - and beta way dem recommend make you take. Inside, Foundry dey use **LoRA (low-rank adaptation)** to fine-tune models well, wey make training quick and cheap pass to re-train every single weight.

### Step 1: Choose training technique

Foundry get three fine-tuning techniques. **Start with SFT** - e cover many different situations.

| Technique | Wetin e do | Wen you go use am |
| --- | --- | --- |
| **Supervised Fine-Tuning (SFT)** | Train am on input/output example pairs so the model go learn how to give the answers wey you wan. | Na the normal one for most tasks: specialize for one domain, do tasks well, get style and tone, follow instructions, and language change. |
| **Direct Preference Optimization (DPO)** | Learn from _preferred vs. non-preferred_ response pairs to match output wit human taste. | To improve answer quality, safety, and alignment when you get comparison feedback. |
| **Reinforcement Fine-Tuning (RFT)** | Use reward signals from _graders_ to make complex behaviors better with reinforcement learning. | For heavy thinking tasks (math, chemistry, physics) where answer be either right or wrong. Need more machine learning skill. |

### Step 2: Choose training tier

Foundry allow you to choose how and where the training go run:

- **Standard** - train for your resource region and make sure data no leave there. Use am when data gats stay only for one region.
- **Global** - cheaper and faster to put job for queue by using capacity outside your region (data and weights dem go copy to training region). Good default if data no gats stay inside one place.
- **Developer** - cheapest of all, use idle capacity and no guarantee for speed (jobs fit stop and start again). Good for trying things.

### Step 3: Choose base model

Models wey fit fine-tune include OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini`, and `gpt-4.1-nano` (SFT; 4o/4.1 family still support DPO), reasoning models `o4-mini` and `gpt-5` (RFT), and open-source models like `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct`, and `gpt-oss-20b` (SFT on Foundry resources). Always check di latest [Fine-tuning models list](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) for how dem dey support am, where e dey, and availability.

> Foundry get two ways: **serverless** (pay for only wetin you use, no GPU quota to manage, OpenAI and some models) and **managed compute** (bring your own VMs via Azure Machine Learning for many models). Most people suppose start wit serverless.

### Foundry best practices

- **Baseline first.** Measure base model wit prompt engineering and RAG _before_ fine-tune, so you fit show di improvement.
- **Start small, then grow.** Start wit 50-100 good examples to test, then make am 500+ for production. Quality better pass quantity - remove bad examples.
- **Format data well.** Training and validation files gats be JSONL, UTF-8 **wit BOM**, under 512 MB, use chat-completions message format. Always add validation file to watch for overfitting.
- **Keep training system prompt for inference.** Use same system message when you call model as the one you use for training.
- **Check checkpoint - no just deploy last one.** Foundry save di last three epochs as deploy checkpoints; choose the one wey generalize well by looking at `train_loss` / `valid_loss` and token accuracy.
- **Measure token cost with quality** when you dey compare fine-tuned model wit baseline.
- **Keep improving wit continuous fine-tuning.** You fit fine-tune model wey don fine-tune before on new data (OpenAI models support dis).
- **Beware hosting costs.** Custom model wey you deploy go charge hourly, and deployment wey no dey active go delete after 15 days - clear wetin you no need.

Follow di complete walkthrough for [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), and di guides for [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) and [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) when you ready for other techniques.

## Fine-Tuning In Action

The resources below get step-by-step tutorials wey go guide you for real example wit model wey dey currently supported and one set of selected data. To fit use dem well, you need account for the provider, plus access to the model and datasets.

| Provider     | Tutorial                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Learn how to fine-tune recent OpenAI chat model for one specific domain ("recipe assistant") by preparing training data, running fine-tuning job, and use fine-tuned model to run inference.                                                                                                                                                                                                                                               |
| Microsoft Foundry | [Customize a model with fine-tuning](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Learn to fine-tune currently supported model like `gpt-4.1-mini` **on Azure** wit Microsoft Foundry: prepare & upload training and validation data, run fine-tuning job, then deploy & use new model.                                                                                                                                                                                                                                             |

| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Dis blog post go show yu how to fine-tune open LLM (ex: `CodeLlama 7B`) using di [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) library & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) wit open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) for Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (or AutoTrain Advanced) na python library wey Hugging Face build wey fit do fine-tuning for plenty kain task including LLM fine-tuning. AutoTrain no need code, and you fit do fine-tuning for your own cloud, for Hugging Face Spaces or locally. E dey support web GUI, CLI and training through yaml config files.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth na open-source framework wey support LLM fine-tuning and reinforcement learning (RL). Unsloth dey make local training, evaluation, and deployment easy wit ready to use [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). E still dey support text-to-speech (TTS), BERT and multimodal models. To start, read their step-by-step [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Assignment

Choose one of di tutorials wey dey up and go through am. _We fit replicate one version of these tutorials for Jupyter Notebooks for dis repo as reference only. Abeg use di original sources directly to get di latest versions_.

## Great Work! Continue Your Learning.

After you don finish dis lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to improve your Generative AI knowledge!

Congrats!! You don finish di final lesson for di v2 series for dis course! No stop to dey learn and build. \*\*Check out di [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) page for list of more suggestions about dis topic.

Our v1 series of lessons don also get update wit more assignments and concepts. So take small time to refresh your knowledge - and abeg [share your questions and feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) to help us improve these lessons for the community.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->