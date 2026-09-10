# Introdakshon to Small Language Models for Generative AI for Beginners
Generative AI na one kain interestin area for artificial intelligence wey dey focus on how to create systems wey fit generate new content. Dis content fit be anything from text and pictures go all di way to music and even whole virtual environments. One of di most excitin tins wey generative AI fit do na for language models.

## Wetin be Small Language Models?

Small Language Model (SLM) na smaller version of big language model (LLM), but e still dey use plenty architectural principles and techniques from LLMs, while e dey use less computational power.

SLMs na subset of language models wey dem design to generate human-like text. Dem no be as big as their bigger counterparts, like GPT-4; SLMs dey small and efficient, so dem dey perfect for where computational resources no too plenty. Even tho dem small, dem fit still do plenty work. Usually, dem dey build SLMs by compress or distill LLMs, to keep most of di original model functionality and language skill. Dis model size reduction dey make dem less complex, so SLMs fit use less memory and computational power. Even wit all these improvements, SLMs fit do plenty natural language processing (NLP) work:

- Text Generation: Make correct and context-appropriate sentences or paragraphs.
- Text Completion: Predict and finish sentences wey dem start.
- Translation: Change text from one language to another.
- Summarization: Make long text short and easy make sense summary.

But, e get some small sacrifice for performance or depth of understanding compared to bigger models dem.

## How Small Language Models Dem Dey Work?
SLMs dey learn from plenty text data. Dem go learn di language patterns and structure as dem dey train, so dem fit generate text wey dey grammatically correct and fit di context. Di training process dey include:

- Data Collection: Collect plenty text data from different places.
- Preprocessing: Clean and arrange di data well so e fit ready for training.
- Training: Use machine learning algorithms to teach di model how to understand and generate text.
- Fine-Tuning: Adjust di model for make e perform better for specific tasks.

SLMs development dey match di need for models wey fit work well for devices wey get limited resources, like mobile devices or edge computing platforms, where full big LLMs no fit run well because dem need too much resource. By focusing on efficiency, SLMs fit give better balance between performance and accessibility, so dem fit work for plenty areas.

![slm](../../../translated_images/pcm/slm.4058842744d0444a.webp)

## Wetin You Go Learn

For dis lesson, we wan introduce una to knowledge of SLM and join am with Microsoft Phi-3 to learn different text content, vision and MoE scenarios.

By di end of dis lesson, you suppose fit answer di following questions:

- Wetin be SLM?
- Wetin different SLM and LLM?
- Wetin be di Microsoft Phi-3/3.5 Family?
- How to run inference with di Microsoft Phi-3/3.5 Family?

You ready? Make we start.

## Differences Between Large Language Models (LLMs) and Small Language Models (SLMs)

Both LLMs and SLMs dey based on machine learning principles wey get chance calculations, and dem get similar design, training methods, data generation, and model evaluation. But some key differences make these two model types different.

## Uses for Small Language Models

SLMs get plenty uses, like:

- Chatbots: Help customers and chat with users like human.
- Content Creation: Help writers by generating ideas or even drafting whole articles.
- Education: Help students write assignments or learn new languages.
- Accessibility: Create tools for people with disabilities, like text-to-speech systems.

**Size**
  
Main difference between LLMs and SLMs na size of di model. LLMs like ChatGPT (GPT-4) get about 1.76 trillion parameters, but open-source SLMs like Mistral 7B get much less, about 7 billion parameters. Dis difference come from architecture and training methods. For example, ChatGPT dey use self-attention inside encoder-decoder design, but Mistral 7B dey use sliding window attention inside decoder-only design. Dis difference affect complexity and performance well well.

**Understanding**

SLMs dey best to perform well inside specific areas, so dem dey specialized but fit no understand plenty contexts across many fields well. But LLMs try mimic human intelligence for many areas. Dem dey train on big and diverse data, so dem fit work for many different domains. Because of this, LLMs dey more versatile and fit perform more tasks, like natural language processing and coding.

**Computing**

Training and using LLMs need plenty resources, like big GPU clusters. For example, to train model like ChatGPT from start, you need thousands of GPUs for long time. But SLMs get smaller parameters and fit run on local machines with moderate GPU, though training still fit take hours for multiple GPUs.

**Bias**

Bias dey common for LLMs because of training data nature. Dem dey use raw online data, wey fit no properly represent some groups, or get wrong labels, or get language bias because of dialect, location, grammar. Plus, LLMs complex architecture fit increase bias if people no fine-tune am well. But SLMs, because dem train for limited, specific data, normally get less bias, but bias fit still dey.

**Inference**

Small size of SLMs mean say dem fit generate result fast for local hardware without heavy parallel processing. But LLMs need plenty parallel compute power to run fast because of size and complexity. Plenty users using LLM at once fit also slow down dem more.

In summary, even as LLMs and SLMs both dey based on machine learning, dem differ well well for model size, resource needs, understanding context, bias problems, and inference speed. These differences make dem fit different uses, with LLMs more versatile but need plenty resources, and SLMs more efficient for specific areas with less resource use.

***Note: For dis lesson, we go use Microsoft Phi-3 / 3.5 as example to introduce SLM.***

## Introduce Phi-3 / Phi-3.5 Family

Phi-3 / 3.5 Family mainly dey focus on text, vision, and Agent (MoE) use cases:

### Phi-3 / 3.5 Instruct

Mainly for text generation, chat completion, and content extraction, and so on.

**Phi-3-mini**

Di 3.8B language model dey available for Microsoft Foundry, Hugging Face, and Ollama. Phi-3 models dey perform well pass language models wey get same or even bigger size for key benchmarks (see benchmark numbers below, higher better). Phi-3-mini fit perform pass models wey big reach twice di size, while Phi-3-small and Phi-3-medium fit perform pass bigger models like GPT-3.5.

**Phi-3-small & medium**

With only 7B parameters, Phi-3-small fit beat GPT-3.5T for plenty language, reasoning, coding, and math benchmarks.

Phi-3-medium get 14B parameters and e continue to perform well, even pass Gemini 1.0 Pro.

**Phi-3.5-mini**

You fit see am as upgrade of Phi-3-mini. Even tho parameters no change, e get better ability to support many languages (support 20+ languages: Arabic, Chinese, Czech, Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Korean, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian) ​​and e add strong support for long context.

Phi-3.5-mini with 3.8B parameters fit perform pass language models of same size and e fit compare well with models twice its size.

### Phi-3 / 3.5 Vision

You fit think of Phi-3/3.5 Instruct as how Phi fit understand tins, and Vision na wetin make Phi get eyes to see and understand world.


**Phi-3-Vision**

Phi-3-vision, wey only get 4.2B parameters, dey continue strong performance and e fit perform pass bigger models like Claude-3 Haiku and Gemini 1.0 Pro V for general visual reasoning, OCR, and table and diagram understanding.


**Phi-3.5-Vision**

Phi-3.5-Vision na upgrade for Phi-3-Vision, e fit handle many images. You fit see am as beta vision wey no just fit see picture but also videos.

Phi-3.5-vision fit perform pass bigger models like Claude-3.5 Sonnet and Gemini 1.5 Flash for OCR, table and chart understanding tasks, and e dey similar for general visual knowledge reasoning tasks. E support multi-frame input, mean say e fit reason many pictures at once


### Phi-3.5-MoE

***Mixture of Experts(MoE)*** mean say models fit train with less compute, so you fit scale model or dataset size well well but still use same compute budget as dense model. MoE model fit reach same quality as dense model faster during pretraining.

Phi-3.5-MoE get 16x3.8B expert modules. Phi-3.5-MoE with only 6.6B active parameters fit reason, understand language, and do math like big big models.

You fit use Phi-3/3.5 models for different use cases. Unlike LLM, you fit deploy Phi-3/3.5-mini or Phi-3/3.5-Vision for edge devices.


## How to use Phi-3/3.5 Family models

We want use Phi-3/3.5 for different situations. Next, we go use Phi-3/3.5 for different cases.

![phi3](../../../translated_images/pcm/phi3.655208c3186ae381.webp)

### Inference via Cloud APIs

**Microsoft Foundry Models**

> **Note:** GitHub Models go stop end July 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) na direct replacement.

Microsoft Foundry Models na di easiest way. You fit quick quick access Phi-3/3.5-Instruct model thru Foundry model catalog. Combine am with Azure AI Inference SDK / OpenAI SDK, you fit run API call through code to complete Phi-3/3.5-Instruct call. You fit also try different things for Playground.

- Demo: Comparison of Phi-3-mini and Phi-3.5-mini performance for Chinese scenarios

![phi3](../../../translated_images/pcm/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/pcm/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

If you want use vision and MoE models, you fit use Microsoft Foundry to make calls. If you like, you fit read Phi-3 Cookbook to learn how to use Phi-3/3.5 Instruct, Vision, MoE with Microsoft Foundry [Click dis link](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Besides Microsoft Foundry Models cloud catalog, you fit also use [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) to make related calls. You fit go NVIDIA NIM to make API calls for Phi-3/3.5 Family. NVIDIA NIM (NVIDIA Inference Microservices) na set of fast inference microservices wey help developers deploy AI models well for different environments like clouds, data centers, and workstations.

Here be some key features of NVIDIA NIM:

- **Ease of Deployment:** NIM make you fit deploy AI models with just one command, e make am easy to add to any workflow.

- **Optimized Performance:** E dey use NVIDIA pre-optimized inference engines dem, like TensorRT and TensorRT-LLM, to make sure say latency low and throughput high.
- **Scalability:** NIM dey support autoscaling for Kubernetes, wey fit handle different workload well well.
- **Security and Control:** Organizations fit maintain control over their data and applications by demself hosting NIM microservices for their own managed infrastructure.
- **Standard APIs:** NIM dey provide industry-standard APIs, wey make am easy to build and integrate AI applications like chatbots, AI assistants, and more.

NIM na part of NVIDIA AI Enterprise, wey dey try simplify how to deploy and make AI models work well, make sure dem dey run beta for NVIDIA GPUs.

- Demo: Using NVIDIA NIM to call Phi-3.5-Vision-API  [[Click this link](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Running Phi-3/3.5 Locally
Inference for Phi-3, or any language model like GPT-3, mean how e dey generate response or predictions based on wetin e receive as input. When you give Phi-3 prompt or question, e go use im trained neural network infer the most likely and relevant response by checking patterns and relationships for the data wey e don train on.

**Hugging Face Transformer**
Hugging Face Transformers na powerful library for natural language processing (NLP) and other machine learning work. Here na some main points about am:

1. **Pretrained Models**: E get thousands pretrained models wey fit do different work like text classification, named entity recognition, question answering, summarization, translation, and text generation.

2. **Framework Interoperability**: The library dey support many deep learning frameworks like PyTorch, TensorFlow, and JAX. This one allow you train model for one framework then use am for another.

3. **Multimodal Capabilities**: Besides NLP, Hugging Face Transformers fit also do tasks for computer vision (like image classification, object detection) and audio processing (like speech recognition, audio classification).

4. **Ease of Use**: The library get APIs and tools wey make am easy to download and fine-tune models, so e dey accessible for both beginners and experts.

5. **Community and Resources**: Hugging Face get active community and plenty documentation, tutorials, and guides to help users start and use the library well.
[official documentation](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) or their [GitHub repository](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

This na the most common way to use, but e need GPU acceleration. Because scenarios like Vision and MoE need plenty calculations, if dem no quantize am, e go dey very slow for CPU.


- Demo: Using Transformer to call Phi-3.5-Instruct [Click this link](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-Vision [Click this link](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Using Transformer to call Phi-3.5-MoE [Click this link](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) na platform wey dem design to make am easy to run big language models (LLMs) locally for your machine. E support different models like Llama 3.1, Phi 3, Mistral, and Gemma 2, and others. The platform simplify the process by bundling model weights, configuration, and data into one package, making e easier for users to customize and create their own models. Ollama dey available for macOS, Linux, and Windows. E beta tool if you wan try or deploy LLMs without needing cloud services. Ollama na the most direct way, you just gatz run this command.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) na Microsoft offline, on-device runtime wey fit run models like Phi for your own hardware - no need Azure subscription, API key, or network connection. E automatically choose the best execution provider available (NPU, GPU, or CPU) and e get OpenAI-compatible endpoint, so existing `openai`/Azure AI Inference SDK code fit use am with small changes. Check the [Foundry Local documentation](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) to start.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

Or use the SDK directly in Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime for GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) na cross-platform inference and training machine-learning accelerator. ONNX Runtime for Generative AI (GENAI) na powerful tool wey help you run generative AI models well well for different platforms. 

## Wetin be ONNX Runtime?
ONNX Runtime na open-source project wey dey enable high-performance inference of machine learning models. E support models for Open Neural Network Exchange (ONNX) format, wey be standard way to represent machine learning models. ONNX Runtime inference fit make customer experience faster and reduce cost, e support models from deep learning frameworks like PyTorch and TensorFlow/Keras as well as classical machine learning libraries like scikit-learn, LightGBM, XGBoost, and others. ONNX Runtime dey compatible with different hardware, drivers, and operating systems, and e give best performance by using hardware accelerators where e fit along with graph optimizations and transforms.

## Wetin be Generative AI?
Generative AI mean AI systems wey fit generate new content, like text, images, or music, based on the data dem train for before. Examples na language models like GPT-3 and image generation models like Stable Diffusion. ONNX Runtime for GenAI library dey provide generative AI loop for ONNX models, including inference with ONNX Runtime, logits processing, search and sampling, and KV cache management.

## ONNX Runtime for GENAI
ONNX Runtime for GENAI extend ONNX Runtime capacity to support generative AI models. Here na some key features:

- **Broad Platform Support:** E dey work for different platforms like Windows, Linux, macOS, Android, and iOS.
- **Model Support:** E dey support many popular generative AI models like LLaMA, GPT-Neo, BLOOM, and more.
- **Performance Optimization:** E get optimizations for different hardware accelerators like NVIDIA GPUs, AMD GPUs, and more.
- **Ease of Use:** E provide APIs wey make am easy to integrate am inside applications, so you fit generate text, images, and other content with little code
- Users fit call one high level generate() method, or run each iteration of the model for loop, generate one token at a time, and optionally update generation parameters inside the loop.
- ONNX runtime still dey support greedy/beam search and TopP, TopK sampling to generate token sequences and e get built-in logits processing like repetition penalties. You fit also easily add your own custom scoring.

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

### Run a Model: Here na simple example for Python:
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

Besides ONNX Runtime, Ollama, and Foundry Local reference methods, we fit also complete reference of quantitative models based on model reference ways provided by different manufacturers. Like Apple MLX framework with Apple Metal, Qualcomm QNN with NPU, Intel OpenVINO with CPU/GPU, etc. You fit get more content from [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## More

We don learn the basics of Phi-3/3.5 Family, but to learn more about SLM we need more knowledge. You fit find answers for the Phi-3 Cookbook. If you want learn more, abeg visit the [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dis document don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even tho we dey try make am correct, abeg make you know say automated translation fit get errors or mistakes. Di original document for dia own language na im be di correct source. For important info, make person wey sabi human translation do am. We no go responsible for any misunderstanding or wrong understanding wey fit happen because of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->