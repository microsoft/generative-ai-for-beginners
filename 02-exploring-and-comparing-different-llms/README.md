# Exploring and Comparing Different LLMs

[![Exploring and Comparing Different LLMs](./images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Click the image above to view video of this lesson_

In the previous lesson, we learned how Generative AI is changing the technology landscape, how Large Language Models (LLMs) work, and how businesses—like our startup—can apply them to their use cases.

The next step in our startup's journey is to explore the current landscape of LLMs and understand which ones are suitable for our specific use case.

## Introduction

This lesson will cover:

- Different types of LLMs in the current landscape
- Testing, iterating, and comparing different models for your use case in Azure
- How to deploy an LLM

## Learning Goals

After completing this lesson, you will be able to:

- Select the right model for your use case
- Understand how to test, iterate, and improve your model's performance
- Know how businesses deploy models

## Understanding Different Types of LLMs

LLMs can be categorized in multiple ways based on their architecture, training data, and use case. Understanding these differences will help our startup select the right model for our scenario.

There are many different types of LLM models. Your choice of model depends on what you aim to use them for, your data, how much you're willing to pay, and more.

Depending on whether you aim to use the models for text, audio, video, image generation, and so on, you might opt for a different type of model.

- **Audio and speech recognition**. Whisper-style models remain useful general-purpose speech recognition models, but production choices now also include newer speech-to-text models such as `gpt-4o-transcribe`.

- **Image generation**. DALL-E and Midjourney are well-known image generation options, but current OpenAI image APIs center on GPT Image models such as `gpt-image-2`, while Stable Diffusion, Image Craft, and other models are also available.

- **Text generation**. Text models now span frontier models, reasoning models, smaller low-latency models, and open-weight models. Current examples include OpenAI GPT-5.x models, Anthropic Claude 3.5, and Meta's Llama 3.3.

- **Multi-modality**. Many current models can process more than just text. Some accept image, audio, or video inputs; some can call tools; and specialized models can generate images, audio, or video.

Selecting a model gives you some basic capabilities, but that might not be enough. Often you have company-specific data that you need to somehow communicate to the LLM. There are a few different approaches to accomplish this.

### Foundation Models versus LLMs

The term "Foundation Model" was [coined by Stanford researchers](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) and defined as an AI model that meets certain criteria, such as:

- **They are trained using unsupervised or self-supervised learning**, meaning they are trained on unlabeled multi-modal data and do not require human annotation or labeling of data.
- **They are very large models**, based on very deep neural networks trained on billions of parameters.
- **They are normally intended to serve as a 'foundation' for other models**, meaning they can be used as a starting point for other models to be built on top of, which can be done through fine-tuning.

![Foundation Models versus LLMs](./images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Image source: [Essential Guide to Foundation Models and Large Language Models | by Babar M Bhatti | Medium](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

To further clarify this distinction, let's use ChatGPT as a historical example. Early versions of ChatGPT used GPT-3.5 as a foundation model. OpenAI then used chat-specific data and alignment techniques to fine-tune the foundation model, resulting in a specialized LLM for conversational tasks.

![Foundation Model](./images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Image source: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Open-Weight/Open-Source versus Proprietary Models

Another way to categorize LLMs is whether they are open-weight, open-source, or proprietary.

Open-source and open-weight models make model artifacts available for inspection, download, or customization, but their licenses differ. Some are fully open source, while others are open-weight models with specific licensing restrictions.

Proprietary models are owned and hosted by a provider. These models are often optimized for managed production use and can offer strong support, safety systems, tool integration, and scalability. However, you have less control over the model itself.

### Embeddings versus Image Generation versus Text and Code Generation

LLMs can also be categorized by the type of output they generate.

Embeddings are a set of models that can convert text into a numerical form, called an embedding, which is a numerical representation of the input text. Embeddings make it easier for machines to understand the relationship between pieces of text.

![Embedding](./images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Image generation models are models that generate images. These models are often used for image editing, image synthesis, and image translation. Image generation models are often trained on large datasets of images and text.

![Image generation](./images/Image.png?WT.mc_id=academic-105485-koreyst)

Text and code generation models are models that generate text or code. These models are often used for text summarization, translation, and question answering. Text generation models are often trained on large datasets of text and code.

![Text and code generation](./images/Text.png?WT.mc_id=academic-105485-koreyst)

### Encoder-Decoder versus Decoder-only

To explain the different architectural types of LLMs, let's use an analogy.

Imagine your manager gave you a task to write a quiz for students. You have two colleagues: one oversees creating the content and the other oversees reviewing it.

The content creator is like a decoder-only model: they can look at the topic, see what you've already written, and then continue generating content based on that context. They are very good at writing and generating new content.

The reviewer is like an encoder-only model. They examine the written course and answers, notice the relationships between them, and understand context, but they are not good at generating new content.

Imagine that you also have someone who could both create and review the quiz. This is an encoder-decoder model. Some examples include BART and T5.

### Service versus Model
