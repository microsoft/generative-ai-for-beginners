[![Open Source Models](../../../translated_images/pcm/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# How to Fine-Tune Your LLM

Using big language models to build generative AI applications dey come wit new wahalas. One big problem na to make sure say the response quality (correctness and relevance) for the content wey the model generate for one user request dey beta. Noktin we discuss for before lessons be say we go use techniques like prompt engineering and retrieval-augmented generation wey dey try solve the problem by _changing the prompt input_ wey the model get.

For today's lesson, we go talk about one third technique wey be **fine-tuning**, wey dey try solve the challenge by _retraining the model itself_ wit extra data dem. Make we yan the koko.

## Wetin You Go Learn

This lesson go introduce fine-tuning concept for pre-trained language models, talk about the benefits and challenges of this method, and also give guide on when and how to fine-tune to make your generative AI model dey perform well.

By the time you finish this lesson, you go fit answer these questions:

- Wetin be fine-tuning for language models?
- When and why fine-tuning good to use?
- How I fit fine-tune pre-trained model?
- Wetin be the wahala wey dey fine-tuning?

Ready? Make we start.

## Illustrated Guide

Want see the koko of wetin we go cover before we start? Check this illustrated guide wey show the learning journey for this lesson - from knowing the main ideas and why fine-tuning matter, to understanding the process and best practices for to fine-tune well. This na serious topic wey good for exploration, so no forget check the [Resources](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) page for more links wey go help you learn on your own!

![Illustrated Guide to Fine Tuning Language Models](../../../translated_images/pcm/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## Wetin be fine-tuning for language models?

By definition, big language models be _pre-trained_ on plenty text wey come from different places for internet. As we don learn before, we need techniques like _prompt engineering_ and _retrieval-augmented generation_ to help improve how model go respond to user questions ("prompts").

One popular prompt technique na to give model beta guide on wetin e suppose respond by giving _instructions_ (explicit guide) or _give am some examples_ (implicit guide). Dem dey call this _few-shot learning_ but e get two wahala:

- Model token limits fit reduce how many examples you fit give, and e fit reduce how e go work well.
- Model token costs fit too high if you dey add examples to every prompt, and e fit reduce flexibility.

Fine-tuning na common method for machine learning where you take pre-trained model and train am again wit new data to make am better for one kain task. For language models, we fit fine-tune the pre-trained model _wit special examples for one specific task or area_ to make **custom model** wey fit better and more correct for that task. One plus point for fine-tuning be say e reduce the examples wey you need for few-shot learning - so e go reduce token use and cost.

## When and why we go fine-tune models?

For _this_ matter, fine-tuning mean **supervised** fine-tuning where you dey add **new data** wey no dey original training data. This different from unsupervised fine-tuning wey model just retrain on original data but with different settings.

The main thing to sabi be say fine-tuning na advanced work wey need skill to get beta result. If you no do am well, e fit no improve or e fit even spoil how model dey perform for your target area.

So before you learn "how" to fine-tune language models, you need to know "why" you go take this side, and "when" to start fine-tuning. Start by asking yourself these questions:

- **Use Case**: Wetin be your _use case_ for fine-tuning? Wetin you want improve for the pre-trained model?
- **Alternatives**: You don try _other methods_ to get wetin you want? Use them to get your baseline for comparison.
  - Prompt engineering: Try few-shot prompting wit examples wey related. Check how good the responses be.
  - Retrieval Augmented Generation: Try add query results wey you get from your data to prompts. Check how good the responses be.
- **Costs**: You don check the cost for fine-tuning?
  - Tunability - The pre-trained model dey available to fine-tune?
  - Effort - Work for preparing training data, checking & changing model.
  - Compute - For running fine-tuning job, and deploying fine-tuned model.
  - Data - Access to enough quality examples for fine-tuning effects.
- **Benefits**: You don check the benefits for fine-tuning?
  - Quality - The fine-tuned model pass the baseline?
  - Cost - E reduce token use by making prompts simple?
  - Extensibility - Fit use base model for new areas?

If you answer these questions well, you fit decide if fine-tuning na the best option for you. The right way be say benefits gatz pass the cost. If you ready, time reach to think about _how_ to fine-tune pre-trained model.

Want hear more about the decision process? Watch [To fine-tune or not to fine-tune](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## How we fit fine-tune pre-trained model?

To fine-tune pre-trained model, you need:

- Pre-trained model wey you go fine-tune
- Dataset wey you go use fine-tune
- Training environment to run fine-tuning job
- Hosting environment to deploy fine-tuned model

## Fine-Tuning for Real

> **Note:** `gpt-35-turbo` / `gpt-3.5-turbo`, wey some tutorials mention, dem don retire am for inference and fine-tuning. If you wan start new fine-tuning job today, try use model wey dem still support - like `gpt-4o-mini` or `gpt-4.1-mini`. Check [Fine-tuning models list](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) to see models wey you fit fine-tune now. The ideas and steps for the tutorials still dey valid.

Dis resources wey follow na step-by-step tutorials wey go guide you through example wit selected model and dataset. To use, you need account for specific provider plus access to model and dataset.

| Provider     | Tutorial                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [How to fine-tune chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Learn to fine-tune `gpt-35-turbo` for one specific area ("recipe assistant") by preparing training data, running fine-tuning, and using fine-tuned model for inference.                                                                                                                                                                                                                                                            |
| Azure OpenAI | [GPT 3.5 Turbo fine-tuning tutorial](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line&WT.mc_id=academic-105485-koreyst) | Learn to fine-tune `gpt-35-turbo-0613` model **on Azure** by creating & uploading training data, running fine-tuning job, deploying & using new model.                                                                                                                                                                                                                                                                           |
| Hugging Face | [Fine-tuning LLMs with Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | This blog talk about fine-tuning open LLM (like `CodeLlama 7B`) with [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) library & [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) wit open [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) on Hugging Face.                           |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Fine-tuning LLMs with AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (or AutoTrain Advanced) na python library wey Hugging Face develop wey fit fine-tune many kain tasks including LLMs. AutoTrain no need code and you fit do fine-tuning for your own cloud, Hugging Face Spaces or locally. E get web GUI, command line and training with yaml config files.                                                                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Fine-tuning LLMs with Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth na open-source framework wey support LLM fine-tuning and reinforcement learning (RL). E dey help local training, checking, and deployment wit ready to use [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst). E also support text-to-speech (TTS), BERT and multimodal models. To start, read their step-by-step [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                 |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Assignment

Choose one tutorial from the list and try am. _We fit do version of these tutorials for Jupyter Notebooks for this repo just to show, but use OG source to get beta versions_.

## Well Done! Carry On to Learn More.

After you finish lesson, check our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue to improve your Generative AI sense!

Congrats!! You don finish the last lesson from v2 series for this course! No stop to learn and build. \*\*Check the [RESOURCES](RESOURCES.md?WT.mc_id=academic-105485-koreyst) page for additional tips for this topic.

Our v1 lesson series don also update with more assignments and ideas. So take small time to refresh your mind - and pls [share your questions and feedback](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) to help us make these lessons better for the community.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->