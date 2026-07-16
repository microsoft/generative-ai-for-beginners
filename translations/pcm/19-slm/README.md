# Introdakshon to Small Language Models for Generative AI for Beginners
Generative AI na one kain interestin part of artificial intelligence wey dey focus on to create systems wey fit generate new content. Dis content fit range from text and images to music and even whole virtual environments. One of di most excitin applications of generative AI be for di area of language models.

## Wetin Be Small Language Models?

Small Language Model (SLM) na small version of large language model (LLM), e dey use plenty principles and techniques from LLMs, but e dey use beta small computational power.

SLMs na set of language models wey dem design to generate text wey resemble wetin human fit talk. E no be like their bigger counterparts, like GPT-4, SLMs small and efficient, so e good for applications wey dem no get plenty computational resources. Even though dem small, dem fit still do plenty tasks. Normally, dem dey build SLMs by to compress or distill LLMs, so that dem go still keep plenty function and language skills from di original model. This small size make the model simpler and use less memory and computing power. Even wit this optimization, SLMs fit still do plenty natural language processing (NLP) tasks:

- Text Generation: To create sentences or paragraphs wey make sense and relate to di context.
- Text Completion: To predict and finish sentences based on the prompt wey dem give am.
- Translation: To change text from one language go another.
- Summarization: To reduce long text to short, easy-to-understand summaries.

But dem fit get some trade-offs for performance or depth of understanding compared to the bigger models.

## How Small Language Models Dey Work?
SLMs dem train on plenty text data. As dem dey train, dem dey learn the patterns and structures of language, so dat dem fit generate text wey correct grammatically and also make sense for di context. Di training process get:

- Data Collection: To gather big text datasets from different sources.
- Preprocessing: To clean and organize di data to make am ready for training.
- Training: To use machine learning algorithms to teach di model how to understand and produce text.
- Fine-Tuning: To adjust di model and improve how e dey perform for specific tasks.

The creation of SLMs dey follow di increasing need for models we fit deploy for places wey resources limited, like mobile devices or edge computing platforms, where full LLMs no fit work well because dem get heavy resource demands. By focusing on efficiency, SLMs fit balance performance with ease of access, and e make dem possible to use for many different fields.

![slm](../../../translated_images/pcm/slm.4058842744d0444a.webp)

## Learning Objectives

For dis lesson, we wan introduce di knowledge about SLM and join am with Microsoft Phi-3 to learn how e fit work for text content, vision, and MoE.

By di end of dis lesson, you go fit answer dis questions:

- Wetin be SLM?
- Wetin be di difference between SLM and LLM?
- Wetin be Microsoft Phi-3/3.5 Family?
- How you fit run inference with Microsoft Phi-3/3.5 Family?

Ready? Make we start.

## Di Differences Between Large Language Models (LLMs) and Small Language Models (SLMs)

Both LLMs and SLMs dem base on di basic principles of probabilistic machine learning, dem follow similar ways on architecture design, training methods, data generation, and how dem dey evaluate model dem. But plenty key factors dey separate these two kinds of models.

## Applications of Small Language Models

SLMs get many uses, including:

- Chatbots: To help customers and take run conversation wit them.
- Content Creation: To help writers create ideas or draft whole articles.
- Education: To assist students with writing assignments or learn new languages.
- Accessibility: To make tools for people with disabilities, like text-to-speech systems.

**Size**
  
One main difference between LLMs and SLMs na di size of di model. LLMs like ChatGPT (GPT-4), get about 1.76 trillion parameters, but open-source SLMs like Mistral 7B get way less—about 7 billion. This difference dey caused mainly by architecture and training style. For example, ChatGPT use self-attention inside encoder-decoder structure, but Mistral 7B use sliding window attention wey fit train well for decoder-only model. Dis difference get strong impact on complexity and performance.

**Comprehension**

SLMs usually optimized for specific domains, so dem get special skills but sometimes limited for broad understanding across many knowledge areas. But LLMs dey try mimic human-like intelligence more wide. Dem train for huge, mixed datasets, so LLMs dey perform well for many domains, and dem versatile. So LLMs better for many types of downstream tasks like natural language processing and programming.

**Computing**

Training and running LLMs na heavy workload, often need plenty computational resources, like big GPU clusters. For example, to train ChatGPT from start, you fit need thousands of GPUs for long time. On the other hand, SLMs with smaller parameter count, fit dey easier to run with less resources. Models like Mistral 7B fit train and run for local machines wey get moderate GPU, though training still need many hours across several GPUs.

**Bias**

Bias na common wahala for LLMs because of di training data. Dem dey rely on raw, open internet data, wey fit no represent some groups well, or get wrong labels, or show linguistic biases from dialect, location differences, and grammar rules. Also, di complex architecture fit make bias worse if no proper fine-tuning. But SLMs, wey train with smaller, domain-specific datasets, dey less prone to bias, though e no mean dem no get any bias at all.

**Inference**

Because SLMs small, dem get big advantage for inference speed, so dem fit generate output fast for local hardware without need for big parallel processing. LLMs, because of their size and complexity, often need plenty parallel compute to get good inference time. Plus, many users at once fit slow down LLM response especially when dem dey deployed at scale.

To summarize, although LLMs and SLMs base on same machine learning principles, dem differ for model size, resource needs, understanding context, bias tendency, and inference speed. These differences show which use fit each, LLMs dey more flexible but heavy for resources, while SLMs dey more efficient for specific domains with less computational demand.

***Note: For this lesson, we go use Microsoft Phi-3 / 3.5 as example to talk about SLM.***

## Introduction to Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family mainly dey focus on text, vision, and Agent (MoE) applications:

### Phi-3 / 3.5 Instruct

Mainly for text generation, chat completion, and content info extraction, etc.

**Phi-3-mini**

The 3.8B language model dey available for Microsoft Foundry, Hugging Face, and Ollama. Phi-3 models dey perform way better pass language models of same or bigger size on important benchmarks (see benchmark numbers below, higher numbers mean better). Phi-3-mini beat models wey twice im size, while Phi-3-small and Phi-3-medium beat bigger models, including GPT-3.5.

**Phi-3-small & medium**

With just 7B parameters, Phi-3-small beat GPT-3.5T for plenty language, reasoning, coding, and math benchmarks.

Phi-3-medium with 14B parameters continue dis trend and beat Gemini 1.0 Pro.

**Phi-3.5-mini**

We fit see am like upgrade of Phi-3-mini. Parameters no change, but e beta support plenty languages (over 20 languages: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) and e fit handle longer context better.

Phi-3.5-mini with 3.8B parameters dey perform better than models of same size and fit compete with models twice im size.

### Phi-3 / 3.5 Vision

We fit call Phi-3/3.5 Instruct model Phi eyes to understand text, and Vision na wetin give Phi eyes to see and understand di world.


**Phi-3-Vision**

Phi-3-vision, with only 4.2B parameters, still dey perform well pass bigger models like Claude-3 Haiku and Gemini 1.0 Pro V for general visual reasoning tasks, OCR, and table and diagram understanding tasks.


**Phi-3.5-Vision**

Phi-3.5-Vision na upgrade of Phi-3-Vision, e fit handle multiple images. You fit see am like improvement for vision where e no only fit see pictures but also videos.

Phi-3.5-vision dey perform well pass bigger models like Claude-3.5 Sonnet and Gemini 1.5 Flash for OCR, table and chart understanding tasks, and still equal for general visual knowledge reasoning. E fit handle multi-frame input, meaning e fit reason on many images at once.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** let models train with less compute, so you fit scale model or dataset size big time with same compute budget like dense model. MoE model fit reach same quality as dense version much quicker during pretraining.

Phi-3.5-MoE get 16x3.8B expert modules. Phi-3.5-MoE with only 6.6B active parameters fit do reasoning, language understanding, and math well like bigger models.

You fit use Phi-3/3.5 Family model for different scenarios. Unlike LLMs, you fit deploy Phi-3/3.5-mini or Phi-3/3.5-Vision on edge devices.


## How to Use Phi-3/3.5 Family Models

We want use Phi-3/3.5 for different scenarios. Next, we go use Phi-3/3.5 for different cases.

![phi3](../../../translated_images/pcm/phi3.655208c3186ae381.webp)

### Inference via Cloud APIs

**Microsoft Foundry Models**

> **Note:** GitHub Models go retire for end of July 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) na di replacement.

Microsoft Foundry Models na di most direct way. You fit quick access the Phi-3/3.5-Instruct model from Foundry model catalog. Join am with Azure AI Inference SDK / OpenAI SDK, you fit call di API with code to complete Phi-3/3.5-Instruct calls. You fit also test different results for di Playground.

- Demo: Comparison of how Phi-3-mini and Phi-3.5-mini perform for Chinese scenarios

![phi3](../../../translated_images/pcm/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pcm/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

If you want use vision and MoE models, you fit use Microsoft Foundry for calls. If you get interest, you fit read Phi-3 Cookbook to learn how to call Phi-3/3.5 Instruct, Vision, MoE through Microsoft Foundry [Click this link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Besides cloud Microsoft Foundry Models catalog, you fit also use [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) to do related calls. You fit go NVIDIA NIM to do API calls for Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) na set of fast inference microservices wey help developers deploy AI models easy for many environments, including clouds, data centers, and workstations.

Here be some important features of NVIDIA NIM:

- **Ease of Deployment:** NIM make am easy to deploy AI models with one command, and e easy to join with existing workflows.

- **Optimized Performance:** E dey use NVIDIA pre-optimized inference engines dem, like TensorRT and TensorRT-LLM, to make sure say e get low latency and high throughput.
- **Scalability:** NIM dey support autoscaling for Kubernetes, wey dey enable am to handle different workloads well well.
- **Security and Control:** Organizations fit maintain control over their data and applications by self-hosting NIM microservices for their own managed infrastructure.
- **Standard APIs:** NIM dey provide industry-standard APIs, wey make am easy to build and integrate AI applications like chatbots, AI assistants, and more.

NIM na part of NVIDIA AI Enterprise, wey aim to simplify the deployment and operationalization of AI models, making sure say dem dey run well for NVIDIA GPUs.

- Demo: Using NVIDIA NIM to call Phi-3.5-Vision-API  [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Running Phi-3/3.5 Locally
Inference wey relate to Phi-3, or any language model like GPT-3, na the process of generating responses or predictions based on the input wey e receive. When you give prompt or question to Phi-3, e go use im trained neural network take infer the most likely and relevant response by analyzing patterns and relations for the data wey e train on.

**Hugging Face Transformer**
Hugging Face Transformers na powerfull library wey dem design for natural language processing (NLP) and other machine learning tasks. Below na some key points about am:

1. **Pretrained Models**: E get thousands pretrained models wey you fit use for different tasks like text classification, named entity recognition, question answering, summarization, translation, and text generation.

2. **Framework Interoperability**: The library dey support plenty deep learning frameworks, like PyTorch, TensorFlow, and JAX. This one mean sey you fit train model for one framework and use am for another.

3. **Multimodal Capabilities**: Besides NLP, Hugging Face Transformers dey support tasks for computer vision (for example, image classification, object detection) and audio processing (for example, speech recognition, audio classification).

4. **Ease of Use**: The library dey offer APIs and tools wey make am easy to download and fine-tune models, so e dey accessible for both beginners and experts.

5. **Community and Resources**: Hugging Face get active community and plenty documentation, tutorials, and guides to help users start and make the best use of the library.
[official documentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) or their [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

This na the method wey dem dey use most, but e still need GPU acceleration. After all, scenarios like Vision and MoE need plenty calculations, wey go slow well well for CPU if dem no quantify am.


- Demo: Using Transformer to call Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) na platform wey dem design to make am easier to run large language models (LLMs) locally for your machine. E dey support different models like Llama 3.1, Phi 3, Mistral, and Gemma 2, plus others. The platform dey simplify the process by bundling model weights, configuration, and data into one package, wey make am easy for users to customize and create their own models. Ollama dey available for macOS, Linux, and Windows. E be beta tool if you dey find to experiment with or deploy LLMs without to rely on cloud services. Ollama na the most direct way, you just need to run dis command below.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) na Microsoft's offline, on-device runtime to run models like Phi completely for your own hardware - no Azure subscription, API key, or network connection required. E automatic pick the best execution provider wey dey available (NPU, GPU, or CPU) and e expose OpenAI-compatible endpoint, so existing `openai`/Azure AI Inference SDK code fit point at am with small changes. See the [Foundry Local documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to start.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Or use the SDK directly inside Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) na cross-platform inference and training machine-learning accelerator. ONNX Runtime for Generative AI (GENAI) na powerfull tool wey dey help you run generative AI models well for different platforms.

## Wetin ONNX Runtime be?
ONNX Runtime na open-source project wey enable high-performance inference of machine learning models. E support models for Open Neural Network Exchange (ONNX) format, wey be standard for representing machine learning models. ONNX Runtime inference fit make customer experiences faster and costs lower, e support models from deep learning frameworks like PyTorch and TensorFlow/Keras plus classical machine learning libraries like scikit-learn, LightGBM, XGBoost, and others. ONNX Runtime dey work with different hardware, drivers, and operating systems, and e provide optimal performance by using hardware accelerators where e fit alongside graph optimizations and transforms.

## Wetin Generative AI be?
Generative AI mean AI systems wey fit generate new content, like text, images, or music, based on the data wey dem train am on. Examples na language models like GPT-3 and image generation models like Stable Diffusion. ONNX Runtime for GenAI library dey provide the generative AI loop for ONNX models, including inference with ONNX Runtime, logits processing, search and sampling, and KV cache management.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI dey extend the capabilities of ONNX Runtime to support generative AI models. Below na some key features:

- **Broad Platform Support:** E dey work for different platforms, including Windows, Linux, macOS, Android, and iOS.
- **Model Support:** E go support plenty popular generative AI models like LLaMA, GPT-Neo, BLOOM, and others.
- **Performance Optimization:** E get optimizations for different hardware accelerators like NVIDIA GPUs, AMD GPUs, and others.
- **Ease of Use:** E provide APIs to make am easy to integrate inside applications, wey allow you generate text, images, and other content with small code.
- Users fit call high level generate() method, or run each iteration of the model inside loop, generating one token at a time, and optionally update generation parameters inside the loop.
- ONNX runtime still get support for greedy/beam search and TopP, TopK sampling to generate token sequences plus built-in logits processing like repetition penalties. You fit also easily add custom scoring.

## How to Start
To start with ONNX Runtime for GENAI, you fit follow these steps:

### Install ONNX Runtime:
```Python
pip install onnxruntime
```
### Install the Generative AI Extensions:
```Python
pip install onnxruntime-genai
```

### Run Model: Here na simple example inside Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Using ONNX Runtime GenAI to call Phi-3.5-Vision


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
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Others**

Apart from ONNX Runtime, Ollama, and Foundry Local reference methods, we fit also complete the reference of quantitative models based on model reference methods wey different manufacturers provide. Like Apple MLX framework with Apple Metal, Qualcomm QNN with NPU, Intel OpenVINO with CPU/GPU, and others. You fit also get more content from [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## More

We don learn the basics of Phi-3/3.5 Family, but to learn more about SLM we need more knowledge. You fit find the answers inside the Phi-3 Cookbook. If you want learn more, abeg visit the [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->