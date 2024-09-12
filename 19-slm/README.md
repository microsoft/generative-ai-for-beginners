# Introduce SLM

A small language model (SLM) represents a scaled-down variant of a large language model (LLM), leveraging many of the architectural principles and techniques of LLMs, while exhibiting a significantly reduced computational footprint. Typically, SLMs are constructed by compressing or distilling LLMs, aiming to retain a substantial portion of the original model's functionality and linguistic capabilities. This reduction in model size decreases the overall complexity, making SLMs more efficient in terms of both memory usage and computational requirements. Despite these optimizations, SLMs can still perform a wide range of natural language processing (NLP) tasks, such as text generation, summarization, and translation, albeit with some trade-offs in performance or depth of understanding compared to their larger counterparts. The development of SLMs aligns with the increasing need for models that can be deployed in resource-constrained environments, such as mobile devices or edge computing platforms, where full-scale LLMs may be impractical due to their heavy resource demands. By focusing on efficiency, SLMs balance performance with accessibility, enabling broader application across various domains.

![slm](./img/slm.png)

## Learning Objectives

In this lesson, we hope to introduce the knowledge of SLM and combine it with Microsoft Phi-3 to learn different scenarios in text content, vision and MoE.

By the end of this lesson, you should be able to answer the following questions:

- What is SLM
- What is the difference about SLM and LLM
- What is Microsoft Phi-3/3.5 Family
- How to inference Microsoft Phi-3/3.5 Family

Ready? Let's get started.

## The Distinctions between Large Language Models (LLMs) and Small Language Models (SLMs)

Both LLMs and SLMs are built upon foundational principles of probabilistic machine learning, following similar approaches in their architectural design, training methodologies, data generation processes, and model evaluation techniques. However, several key factors differentiate these two types of models.

**Size**
  
A primary distinction between LLMs and SLMs lies in the scale of the models. LLMs, such as ChatGPT (GPT-4), can comprise an estimated 1.76 trillion parameters, while open-source SLMs like Mistral 7B are designed with significantly fewer parameters—approximately 7 billion. This disparity is primarily due to differences in model architecture and training processes. For instance, ChatGPT employs a self-attention mechanism within an encoder-decoder framework, whereas Mistral 7B uses sliding window attention, which enables more efficient training within a decoder-only model. This architectural variance has profound implications for the complexity and performance of these models.

**Comprehension**

SLMs are typically optimized for performance within specific domains, making them highly specialized but potentially limited in their ability to provide broad contextual understanding across multiple fields of knowledge. In contrast, LLMs aim to simulate human-like intelligence on a more comprehensive level. Trained on vast, diverse datasets, LLMs are designed to perform well across a variety of domains, offering greater versatility and adaptability. Consequently, LLMs are more suitable for a wider range of downstream tasks, such as natural language processing and programming.

**Computing**

The training and deployment of LLMs are resource-intensive processes, often requiring significant computational infrastructure, including large-scale GPU clusters. For example, training a model like ChatGPT from scratch may necessitate thousands of GPUs over extended periods. In contrast, SLMs, with their smaller parameter counts, are more accessible in terms of computational resources. Models like Mistral 7B can be trained and run on local machines equipped with moderate GPU capabilities, although training still demands several hours across multiple GPUs.

**Bias**

Bias is a known issue in LLMs, primarily due to the nature of the training data. These models often rely on raw, openly available data from the internet, which may underrepresent or misrepresent certain groups, introduce erroneous labeling, or reflect linguistic biases influenced by dialect, geographic variations, and grammatical rules. Additionally, the complexity of LLM architectures can inadvertently exacerbate bias, which may go unnoticed without careful fine-tuning. On the other hand, SLMs, being trained on more constrained, domain-specific datasets, are inherently less susceptible to such biases, though they are not immune to them.

**Inference**

The reduced size of SLMs affords them a significant advantage in terms of inference speed, allowing them to generate outputs efficiently on local hardware without the need for extensive parallel processing. In contrast, LLMs, due to their size and complexity, often require substantial parallel computational resources to achieve acceptable inference times. The presence of multiple concurrent users further slows down LLMs' response times, especially when deployed at scale.

In summary, while both LLMs and SLMs share a foundational basis in machine learning, they differ significantly in terms of model size, resource requirements, contextual understanding, susceptibility to bias, and inference speed. These distinctions reflect their respective suitability for different use cases, with LLMs being more versatile but resource-heavy, and SLMs offering more domain-specific efficiency with reduced computational demands.

***Note：In this chapter, we will introduce SLM using Microsoft Phi-3 / 3.5 as an example.***

## Introduce Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family mainly targets text, vision, and Agent (MoE) application scenarios:

### Phi-3 / 3.5 Instruct

Mainly for text generation, chat completion, and content information extraction, etc.

**Phi-3-mini**

The 3.8B language model is available on Microsoft Azure AI Studio, Hugging Face, and Ollama. Phi-3 models significantly outperform language models of equal and larger sizes on key benchmarks (see benchmark numbers below, higher numbers are better). Phi-3-mini outperforms models twice its size, while Phi-3-small and Phi-3-medium outperform larger models, including GPT-3.5

**Phi-3-small & medium**

With just 7B parameters, Phi-3-small beats GPT-3.5T on a variety of language, reasoning, coding, and math benchmarks.

The Phi-3-medium with 14B parameters continues this trend and outperforms the Gemini 1.0 Pro.

**Phi-3.5-mini**

We can think of it as an upgrade of Phi-3-mini. While the parameters remain unchanged, it improves the ability to support multiple languages(
Support 20+ languages:Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​and adds stronger support for long context.

Phi-3.5-mini with 3.8B parameters outperforms language models of the same size and on par with models twice its size.

### Phi-3 / 3.5 Vision

We can think of the Instruct model of Phi-3/3.5 as Phi's ability to understand, and Vision is what gives Phi eyes to understand the world.


**Phi-3-Vision**

Phi-3-vision, with only 4.2B parameters, continues this trend and outperforms larger models such as Claude-3 Haiku and Gemini 1.0 Pro V on general visual reasoning tasks, OCR, and table and diagram comprehension tasks.


**Phi-3.5-Vision**

Phi-3.5-Vision is also an upgrade of Phi-3-Vision, adding support for multiple images. You can think of it as an improvement in vision, not only can you see pictures, but also videos.

Phi-3.5-vision outperforms larger models such as Claude-3.5 Sonnet and Gemini 1.5 Flash across OCR, table and chart understanding tasks and on par on general visual knowledge reasoning tasks.Support multi-frame input, i.e., perform reasoning on multiple input images


### Phi-3.5-MoE

***Mixture of Experts(MoE)*** enable models to be pretrained with far less compute, which means you can dramatically scale up the model or dataset size with the same compute budget as a dense model. In particular, a MoE model should achieve the same quality as its dense counterpart much faster during pretraining.

Phi-3.5-MoE comprises 16x3.8B expert modules.Phi-3.5-MoE with only 6.6B active parameters achieves a similar level of reasoning, language understanding, and math as much larger models

We can use the Phi-3/3.5 Family model based on different scenarios. Unlike LLM, you can deploy Phi-3/3.5-mini or Phi-3/3.5-Vision on edge devices.


## How to use Phi-3/3.5 Family models

We hope to use Phi-3/3.5 in different scenarios. Next, we will use Phi-3/3.5 based on different scenarios.

![phi3](./img/phi3.png)

### Inference difference Cloud's API

**GitHub Models**

GitHub Models is the most direct way. You can quickly access the Phi-3/3.5-Instruct model through GitHub Models. Combined with the Azure AI Inference SDK / OpenAI SDK, you can access the API through code to complete the Phi-3/3.5-Instruct call. You can also test different effects through Playground.

- Demo:Comparison of the effects of Phi-3-mini and Phi-3.5-mini in Chinese scenarios

![phi3](./img/gh1.png)

![phi35](./img/gh2.png)


**Azure AI Studio**

Or if we want to use the vision and MoE models, you can use Azure AI Studio to complete the call. If you are interested, you can read the Phi-3 Cookbook to learn how to call Phi-3/3.5 Instruct, Vision, MoE through Azure AI Studio [Click this link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md)


**NVIDIA NIM**

In addition to the cloud-based Model Catalog solutions provided by Azure and GitHub, you can also use Nivida NIM to complete related calls. You can visit NIVIDA NIM to complete the API calls of Phi-3/3.5 Family

- Demo: Using Nividia NIM to call Phi-3.5-Vision-API  [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb)]


### Inference Phi-3/3.5 in local env


**Hugging face Transformer**

This is the most commonly used method, but it also requires GPU acceleration. After all, scenes such as Vision and MoE require a lot of calculations, which will be very limited in the CPU if they are not quantized.


- Demo:Using Transformer to call Phi-3.5-Instuct [Click this link](./python/phi35-instruct-demo.ipynb)

- Demo:Using Transformer to call Phi-3.5-Vision[Click this link](./python/phi35-vision-demo.ipynb)

- Demo:Using Transformer to call Phi-3.5-MoE[Click this link](./python/phi35_moe_demo.ipynb)

**Ollama**

Ollama is the most direct way, you just need to execute the following statement


```bash

ollama run phi3.5

```


**ONNX Runtime for GenAI**

ONNX Runtime is a cross-platform inference and training machine-learning accelerator.

ONNX Runtime inference can enable faster customer experiences and lower costs, supporting models from deep learning frameworks such as PyTorch and TensorFlow/Keras as well as classical machine learning libraries such as scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime is compatible with different hardware, drivers, and operating systems, and provides optimal performance by leveraging hardware accelerators where applicable alongside graph optimizations and transforms

ONNX Runtime for GenAI library provides the generative AI loop for ONNX models, including inference with ONNX Runtime, logits processing, search and sampling, and KV cache management.

Users can call a high level generate() method, or run each iteration of the model in a loop, generating one token at a time, and optionally updating generation parameters inside the loop.

It has support for greedy/beam search and TopP, TopK sampling to generate token sequences and built-in logits processing like repetition penalties. You can also easily add custom scoring.

 
- Demo:Using ONNX Runtime GenAI to call Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    code += tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Others**

In addition to ONNX Runtime and Ollama reference methods, we can also complete the reference of quantitative models based on the model reference methods provided by different manufacturers. Such as Apple MLX framework with Apple Metal, Qualcomm QNN with NPU, Intel OpenVINO with CPU/GPU, etc. You can also get more content from [Phi-3 Cookbook](https://aka.ms/phi-3cookbook)


## More

We have learned the basics of Phi-3/3.5 Family, but to learn more about SLM we need more knowledge. You can find the answers in the Phi-3 Cookbook. If you want to learn more, please visit Phi-3 Cookbook













