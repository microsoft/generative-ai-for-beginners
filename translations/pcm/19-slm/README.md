# Intro to Small Language Models for Generative AI for Beginners
Generative AI na one kain interesting artificial intelligence wey dey focus on how to create systems wey fit generate new content. Dis content fit include text, pictures, music, and even whole virtual environments. One of di most exciting way wey generative AI dey used na for language models.

## Wetin Small Language Models be?

Small Language Model (SLM) na small version of big language model (LLM), but e still use many of di design principles and techniques of LLMs, only say e dey use less computer power.

SLMs na small small language models wey dey generate text wey fit sound like human being talk. Dem no big reach things like GPT-4, SLMs small and efficient, so dem good well well for where computer resources no too dey. Even tho dem small, dem fit still do many kain work. Mostly, SLMs dey made by compress or distill LLMs to keep most of di original model powers and language skills. This kind small size make am easy to use, small for memory and computer handling. Even with these improvements, SLMs fit still do different NLP tasks:

- Text Generation: To create sentences or paragraphs wey go correct and dey make sense.
- Text Completion: To predict and finish sentences wey you start.
- Translation: To change text from one language go another one.
- Summarization: To make long text short and easy to understand.

Even tho dem get some small wahala for performance or deep understanding compared to big models.

## How Small Language Models dey Work?
SLMs dey train on plenty text data. When dem dey train dem, dem dey learn how language dey flow and konstructures so dem fit generate text wey correct grammar and fit for di context. Training process dey include:

- Data Collection: Gather plenty text from different places.
- Preprocessing: Clean and organize di text to make am ready for training.
- Training: Use machine learning algorithms to teach di model how to understand and produce text.
- Fine-Tuning: Adjust di model to do well for specific tasks.

Di way SLMs dey grow dey match di need to put models for places where resource no plenty, like mobile devices or edge computing, where full LLMs no too make sense because dem need plenty resources. By focusing on how to use resources well, SLMs dey balance performance and accessibility, so dem fit work for different things.

![slm](../../../translated_images/pcm/slm.4058842744d0444a.webp?WT.mc_id=academic-105485-koreyst)

## Wetin you go learn

For this lesson, we want make you sabi about SLM and join am with Microsoft Phi-3 so you fit sabi different scenarios for text content, vision and MoE.

By di end of dis lesson, you go fit answer these questions:

- Wetin be SLM?
- Wetin be difference between SLM and LLM?
- Wetin be Microsoft Phi-3/3.5 Family?
- How you fit run inference with Microsoft Phi-3/3.5 Family?

Ready? Make we start.

## Difference between Large Language Models (LLMs) and Small Language Models (SLMs)

Both LLMs and SLMs dey based on machine learning wey dey work with probability. Dem get similar design, how dem dey train am, how dem generate data, and how dem check their work. But some big factors dey wey make di two different.

## How Small Language Models dey used

SLMs fit do plenty work, for example:

- Chatbots: To support customers and talk with users like human beings.
- Content Creation: To help writers generate ideas or write articles.
- Education: To help students write and learn new languages.
- Accessibility: To create tools for people wey get disabilities, like text-to-speech.

**Size**
  
Di big difference between LLMs and SLMs na size. LLMs like ChatGPT (GPT-4) get about 1.76 trillion parameters, and open source SLMs like Mistral 7B get far less parameters, about 7 billion. Dis difference na because how dem design dem and how dem train am dey different. For example, ChatGPT get self-attention inside encoder-decoder style, but Mistral 7B use sliding window attention, so e fit train well for only decoder model. Dis kind design difference get big effect for how complex and how good di models be.

**Comprehension**

SLMs usually dey optimized for small areas, dem specialized but fit no understand many things well well. But LLMs dey try show human-like intelligence for many wide areas. Dem train on big assorted data, so dem fit work well for many different fields. This one make LLMs good for plenty different tasks, like natural language processing and computer programming.

**Computing**

Training and running LLMs na heavy work, dem need big computer set-ups, like many GPU clusters. Like if you wan train ChatGPT from zero, you go need thousands GPUs for long time. But SLMs want less because dem get smaller parameters. Models like Mistral 7B fit train and run for local computers with moderate GPUs, but training still need plenty hours and GPUs.

**Bias**

Bias na wahala for LLMs because of di training data dem use. Dem use raw internet data wey sometimes no represent all groups well, or get wrong labels, or show bias from dialect, place, grammar. LLM design fit also make bias worse if person no fine-tune well. But SLMs, wey dem train with focused and specific data, no get as much bias, but dem still get small chance of bias.

**Inference**

Because SLMs small, dem fit run inference quick quick on local machines without needing big parallel computing. But LLMs need strong parallel compute for fast inference. If many users dey use am at once, LLMs go slow more.

To sum am up, LLMs and SLMs both use machine learning principles but dem different for size, resource needs, understanding deepness, bias levels and speed of inference. These difference make LLMs fit use for many uses but need plenty resources, while SLMs good for focused tasks and less computing needs.

***Note: For this lesson, we go talk about SLM using Microsoft Phi-3 / 3.5 as example.***

## Talk about Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family mainly dey work for text, vision, and Agent (MoE) applications:

### Phi-3 / 3.5 Instruct

Mainly for text generation, chat completion, and content information extraction, etc.

**Phi-3-mini**

Di 3.8B language model dey available on Microsoft Foundry, Hugging Face, and Ollama. Phi-3 models dey perform well pass language models wey get same or bigger size for important benchmarks (see benchmark numbers below, higher better). Phi-3-mini better pass models wey get double im size, Phi-3-small and Phi-3-medium still better pass big models, including GPT-3.5.

**Phi-3-small & medium**

With only 7B parameters, Phi-3-small dey beat GPT-3.5T for different language, reasoning, coding, and math tests.

Phi-3-medium with 14B parameters dey continue dis better waka and e pass Gemini 1.0 Pro.

**Phi-3.5-mini**

We fit see am as upgrade of Phi-3-mini. Parameters no change, but e fit support many languages (support 20+ languages: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​and get stronger support for longer context.

Phi-3.5-mini with 3.8B parameters dey perform pass language models of same size and e dey equal models twice im size.

### Phi-3 / 3.5 Vision

We fit see di Instruct model of Phi-3/3.5 as Phi’s way to understand, and Vision na wetin give Phi eyes to understand di world.


**Phi-3-Vision**

Phi-3-vision wey get only 4.2B parameters dey continue dis trend and e dey better pass big models like Claude-3 Haiku and Gemini 1.0 Pro V for general visual reasoning, OCR, and table/diagram understanding tasks.


**Phi-3.5-Vision**

Phi-3.5-Vision upgrade Phi-3-Vision by adding support for multiple images. You fit see am as better vision, no be only pictures, but also videos.

Phi-3.5-vision better pass big models like Claude-3.5 Sonnet and Gemini 1.5 Flash for OCR, table and chart understanding and e equal them for general visual knowledge reasoning. E fit handle multi-frame input, mean e fit reason on many input images.


### Phi-3.5-MoE

***Mixture of Experts (MoE)*** dey make models fit pretrain with less compute, so you fit scale model or dataset size well well with same compute power like dense models. MoE model fit do same quality as dense model plenty faster during pretraining.

Phi-3.5-MoE get 16x3.8B expert modules. Phi-3.5-MoE with only 6.6B active parameters get similar reasoning, language understanding, and maths ability like models wey big well well.

You fit use Phi-3/3.5 Family model for different cases. Unlike LLM, you fit deploy Phi-3/3.5-mini or Phi-3/3.5-Vision for edge devices.


## How to use Phi-3/3.5 Family models

We hope say you go use Phi-3/3.5 for different cases. Next, we go show how to use Phi-3/3.5 according to different cases.

![phi3](../../../translated_images/pcm/phi3.655208c3186ae381.webp?WT.mc_id=academic-105485-koreyst)

### Inference via Cloud APIs

**Microsoft Foundry Models**

> **Note:** GitHub Models dey retire by end of July 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) na di correct replacement.

Microsoft Foundry Models na di quickest way. You fit quickly find Phi-3/3.5-Instruct model from Foundry catalog. Join am with Azure AI Inference SDK / OpenAI SDK, you fit use code access API to complete Phi-3/3.5-Instruct call. You fit also test different results for Playground.

- Demo: How Phi-3-mini and Phi-3.5-mini dey perform for Chinese situations

![phi3](../../../translated_images/pcm/gh1.126c6139713b622b.webp?WT.mc_id=academic-105485-koreyst)

![phi35](../../../translated_images/pcm/gh2.07d7985af66f178d.webp?WT.mc_id=academic-105485-koreyst)


**Microsoft Foundry**

If you want use vision and MoE models, you fit call am through Microsoft Foundry. If you like, you fit read Phi-3 Cookbook to learn how to call Phi-3/3.5 Instruct, Vision, MoE using Microsoft Foundry [Click this link](https://github.com/microsoft/PhiCookBook/blob/main/md/02.QuickStart/AzureAIFoundry_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Apart from cloud Microsoft Foundry Models catalog, you fit also use [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) to do calls. You fit visit NVIDIA NIM to run API calls for Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) na set of fast inference microservices wey help developers deploy AI models well for different environments like clouds, data centers, workstations.

Some main features of NVIDIA NIM be:

- **Easy Deploy:** NIM let you deploy AI models with one command, e easy to join with your current workflows.
- **Optimized Performance:** E use NVIDIA’s pre-optimized inference engines, like TensorRT and TensorRT-LLM, to get low delay and high output.
- **Scalability:** NIM fit do autoscaling on Kubernetes, so e fit handle different work loads well.
- **Security and Control:** Organizations fit control their data and app by self-hosting NIM microservices for their own infrastructure.
- **Standard APIs:** NIM dey provide industry-standard APIs, wey e make e easy to build and join AI apps like chatbot dem, AI assistant dem, and plenty more.

NIM na part of NVIDIA AI Enterprise, wey dem create to simplify how e be to deploy and run AI model dem, make sure say dem dey do well for NVIDIA GPU dem.

- Demo: Using NVIDIA NIM to call Phi-3.5-Vision-API  [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Running Phi-3/3.5 Locally
Inference about Phi-3, or any language model like GPT-3, na the process to make response or prediction based on wetin e receive. When you give Phi-3 prompt or question, e dey use e trained neural network to find the most likely and relevant answer by checking patterns and relationship for the data wey e train on.

**Hugging Face Transformer**
Hugging Face Transformers na strong library wey dem design for natural language processing (NLP) and other machine learning work. Here some important points about am:

1. **Pretrained Models**: E get thousands pretrained models wey fit do many work like text classification, named entity recognition, question answering, summarization, translation, and text generation.

2. **Framework Interoperability**: The library fit work with many deep learning frameworks, including PyTorch, TensorFlow, and JAX. This one mean say you fit train model for one framework then use am for another.

3. **Multimodal Capabilities**: Besides NLP, Hugging Face Transformers still dey support computer vision task dem (like image classification, object detection) and audio processing (like speech recognition, audio classification).

4. **Ease of Use**: The library get APIs and tools wey make am easy to download and fine-tune models, so both beginners and experts fit use am.

5. **Community and Resources**: Hugging Face get big community and plenty documentation, tutorials, and guides to help users start well and use the library better.
[official documentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) or their [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Na this method dey popular pass, but e still need GPU acceleration. For example, Vision and MoE need plenty calculation, if dem no quantize am, e go slow well well for CPU.


- Demo: Using Transformer to call Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) na platform wey dem design to make am easy to run large language models (LLMs) locally for your machine. E fit support plenti models like Llama 3.1, Phi 3, Mistral, and Gemma 2, plus others. The platform dey simplify everything by putting model weights, configuration, and data join as one package, so e easy for users to customize and create their own models. Ollama dey available for macOS, Linux, and Windows. E good tool if you wan try or deploy LLMs without use cloud services. Ollama na the most direct way, you just need run this command.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) na Microsoft's offline, on-device runtime to run models like Phi fully for your own hardware - no need Azure subscription, API key, or network connection. E go automatically choose the best execution provider wey dey (NPU, GPU, or CPU) and expose OpenAI-compatible endpoint, so the current `openai`/Azure AI Inference SDK code fit use am with small changes. Check the [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to start.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Or use the SDK directly for Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) na cross-platform inference and training machine-learning accelerator. ONNX Runtime for Generative AI (GENAI) na strong tool wey help you run generative AI models well well for different platforms. 

## Wetin be ONNX Runtime?
ONNX Runtime na open-source project wey dey enable high-performance inference of machine learning models. E support models for Open Neural Network Exchange (ONNX) format, wey be standard to represent machine learning models. ONNX Runtime inference fit make customer experience faster and costs reduce, e support models from deep learning frameworks like PyTorch and TensorFlow/Keras plus classical machine learning libraries like scikit-learn, LightGBM, XGBoost, and others. ONNX Runtime fit different hardware, drivers, and operating systems, and e dey provide correct performance by using hardware accelerators when e need am with graph optimizations and transforms.

## Wetin be Generative AI?
Generative AI mean AI system wey fit create new content like text, images, or music, based on the data dem train am on. Examples na language models like GPT-3 and image generation models like Stable Diffusion. ONNX Runtime for GenAI library dey provide the generative AI loop for ONNX models, wey include inference with ONNX Runtime, logits processing, search and sampling, plus KV cache management.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI extend the ONNX Runtime to support generative AI models. Here be some important features:

- **Broad Platform Support:** E dey work on different platforms, including Windows, Linux, macOS, Android, and iOS.
- **Model Support:** E support plenty popular generative AI models, like LLaMA, GPT-Neo, BLOOM, and more.
- **Performance Optimization:** E get optimizations for different hardware accelerators like NVIDIA GPUs, AMD GPUs, and more2.
- **Ease of Use:** E get APIs wey make am easy to join am with apps, so you fit generate text, images, and other content with small code
- Users fit call one high level generate() method, or run each iteration of the model in a loop, generating one token at a time, and fit also update generation parameters inside the loop.
- ONNX runtime still support greedy/beam search and TopP, TopK sampling to generate token sequences and e get built-in logits processing like repetition penalties. You fit also add custom scoring easily.

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

### Run a Model: Here na one simple example for Python:
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
### Demo:Using ONNX Runtime GenAI to call Phi-3.5-Vision


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

Besides ONNX Runtime, Ollama, and Foundry Local way dem use, we fit still finish the example of quantitative models based on the model example way different makers give. Like Apple MLX framework with Apple Metal, Qualcomm QNN with NPU, Intel OpenVINO with CPU/GPU, and others. You fit also find more info for [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## More

We don learn the basics of Phi-3/3.5 Family, but to sabi more about SLM, we need more knowledge. You fit find the answers inside the Phi-3 Cookbook. If you want sabi more, abeg visit the [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->