# Explorando y comparando diferentes Modelos Grandes de Lenguaje (LLMs)

[![Explorando y comparando diferentes LLMs](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/J1mWzw0P74c?WT.mc_id=academic-105485-koreyst)

> *Haz clic en la imagen de arriba para ver el video de esta lección*

Con la lección anterior, hemos visto cómo la IA Generativa está cambiando el panorama tecnológico, cómo funcionan los Modelos Grandes de Lenguaje (LLMs) y cómo un negocio - como nuestra startup - puede aplicarlos a sus casos de uso y expandirse. En este capítulo, buscamos comparar y contrastar diferentes tipos de Modelos Grandes de Lenguaje, LLMs, para entender sus pros y contras.

El siguiente paso en el viaje de nuestra startup es explorar el panorama actual de los Modelos Grandes de Lenguaje (LLMs) y entender cuáles son los apropiados para nuestro caso de uso.

## Introducción

En esta lección se cubrirá:

- Diferentes tipos de LLMs en el panorama actual.
- Pruebas, iteraciones y comparaciones de diferentes modelos para tu caso de uso en Azure.
- Cómo implementar un LLM.

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

- Seleccionar el modelo correcto para tu caso de uso.
- Entender cómo probar, iterar y mejorar el rendimiento de tu modelo.
- Saber cómo las empresas implementan modelos.

## Entender los diferentes tipos de LLMs

Los Modelos Grandes de Lenguaje (LLMs) pueden clasificarse de múltiples formas según su arquitectura, datos de entrenamiento y caso de uso. Comprender estas diferencias ayudará a nuestra startup a elegir el modelo más adecuado para el escenario en el que se utilizará, así como a entender cómo probar, iterar y mejorar su rendimiento.

Existen muchos tipos diferentes de modelos LLM. Tu elección de modelo dependerá de para qué planeas usarlos, los datos que tienes, cuánto estás dispuesto a pagar y más.

Según el propósito de uso de los modelos, ya sea para procesar texto, audio, vídeo, generar imágenes y otros, es posible que decidas elegir un tipo diferente de modelo.

- **Reconocimiento de audio y voz**. Para este propósito, los modelos tipo Whisper son una excelente elección, ya que son de propósito general y están orientados al reconocimiento de voz. Están entrenados con una amplia variedad de audios y pueden realizar reconocimiento de voz en múltiples idiomas. Aprende más sobre [modelos tipo Whisper aquí](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Generación de imágenes**. Para la generación de imágenes, DALL-E y Midjourney son dos opciones muy conocidas. DALL-E está disponible a través de Azure OpenAI. [Lee más sobre DALL-E aquí](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) y también en el Capítulo 9 de este currículo.

- **Generación de texto**. La mayoría de los modelos están entrenados en generación de texto y tienes una gran variedad de opciones, desde GPT-3.5 hasta GPT-4. Vienen con diferentes costos, siendo GPT-4 el más caro. Es recomendable revisar el [Azure Open AI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para determinar qué modelos se ajustan mejor a tus necesidades en cuanto a capacidad y costo.

Seleccionar un modelo significa que obtienes algunas capacidades básicas, que sin embargo podrían no ser suficientes. Frecuentemente tienes datos específicos de la empresa que de alguna manera necesitas comunicar al LLM. Hay varias opciones sobre cómo abordar eso, más sobre eso en las secciones siguientes.

### Modelos de Base versus Modelos Grandes de Lenguaje

El término Modelo Fundacional fue [creado por investigadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) y definido como un modelo de IA que sigue algunos criterios, tales como:

- **Se entrenan utilizando aprendizaje no supervisado o aprendizaje auto-supervisado**, lo que significa que se entrenan en datos multimodales no etiquetados, y no requieren anotación humana o etiquetado de datos para su proceso de entrenamiento.
- **Son modelos muy grandes**, basados en redes neuronales muy profundas entrenadas con miles de millones de parámetros.
- **Normalmente están destinados a servir como una 'fundación' para otros modelos**, lo que significa que pueden usarse como un punto de partida para que otros modelos se construyan sobre ellos, lo cual se puede hacer mediante ajustes finos.

![Modelos Fundacionales versus LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [Guía Esencial de Modelos Fundacionales y Modelos Grandes de Lenguaje | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para aclarar aún más esta distinción, tomemos ChatGPT como ejemplo. Para construir la primera versión de ChatGPT, un modelo llamado GPT-3.5 sirvió como el modelo fundacional. Esto significa que OpenAI utilizó algunos datos específicos de chat para crear una versión ajustada de GPT-3.5 que estaba especializada en desempeñarse bien en escenarios conversacionales, como los chatbots.

![Modelo Fundacional](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de Código Abierto versus Modelos Propietarios

Otra manera de categorizar los Modelos Grandes de Lenguaje es si son de código abierto (open source) o propietarios.

Los modelos de código abierto son modelos que se ponen a disposición del público y pueden ser utilizados por cualquiera. A menudo son publicados por la empresa que los creó o por la comunidad investigadora. Estos modelos pueden ser inspeccionados, modificados y personalizados para diversos casos de uso en Modelos Grandes de Lenguaje. Sin embargo, no siempre están optimizados para uso en producción y pueden no ser tan eficientes como los modelos propietarios. Además, la financiación para modelos de código abierto puede ser limitada, y es posible que no se mantengan a largo plazo o que no se actualicen con las últimas investigaciones. Algunos ejemplos de modelos de código abierto populares incluyen:  [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst) and [LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst).

Los modelos propietarios son modelos que son propiedad de una empresa y no se ponen a disposición del público. Estos modelos suelen estar optimizados para su uso en producción. Sin embargo, no se permite su inspección, modificación o personalización para diferentes casos de uso. Además, no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso. Asimismo, los usuarios no tienen control sobre los datos utilizados para entrenar el modelo, lo que significa que deben confiar en el propietario del modelo para garantizar el compromiso con la privacidad de los datos y el uso responsable de la inteligencia artificial. Algunos ejemplos de modelos propietarios populares: [OpenAI models](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) or [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Incrustaciones versus Generación de Imágenes versus Generación de Texto y Código

Los LLMs también pueden ser categorizados por la salida que generan.

Los embeddings son un conjunto de modelos que pueden convertir texto en una forma numérica, llamada incrustación, que es una representación numérica del texto de entrada. Las incrustaciones facilitan que las máquinas comprendan las relaciones entre palabras u oraciones y pueden ser utilizadas como entradas por otros modelos, como modelos de clasificación o modelos de agrupación que tienen un mejor rendimiento con los datos numéricos. Los modelos de incrustación usualmente se utilizan para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la cual hay gran cantidad de datos, y luego los pesos del modelo (incrustaciones) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría es [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Incrustación](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de imágenes son modelos que crean imágenes. Estos modelos suelen utilizarse para la edición de imágenes, la síntesis de imágenes y la traducción de imágenes. Los modelos de generación de imágenes con regularidad son entrenados en grandes conjuntos de datos de imágenes, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar nuevas imágenes o para editar imágenes existentes con técnicas de inpainting, super-resolución y colorización. Algunos ejemplos: [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de texto y código son modelos que generan texto o código. Estos modelos suelen utilizarse para resumir texto, traducir y responder preguntas. Los modelos de generación de texto suelen ser entrenados en grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar texto o responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), en muchas ocasiones se entrenan en grandes conjuntos de datos de código, como GitHub, y pueden utilizarse para crear código o para corregir errores en código existente.

 ![Generación de texto y código](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Encoder-Decoder versus Decoder-only

To talk about the different types of architectures of LLMs, let's use an analogy.

Imagine your manager gave you a task for writing a quiz for the students.  You have two colleagues; one oversees creating the content and the other oversees reviewing them.

The content creator is like a Decoder only model, they can look at the topic and see what you already wrote and then he can write a course based on that. They are very good at writing engaging and informative content, but they are not very good at understanding the topic and the learning objectives. Some examples of Decoder models are GPT family models, such as GPT-3.

The reviewer is like an Encoder only model, they look at the course written and the answers, noticing the relationship between them and understanding context, but they are not good at generating content. An example of Encoder only model would be BERT.

Imagine that we can have someone as well who could create and review the quiz, this is an Encoder-Decoder model. Some examples would be BART and T5.

### Service versus Model

Now, let's talk about the difference between a service and a model. A service is a product that is offered by a Cloud Service Provider, and is often a combination of models, data, and other components. A model is the core component of a service, and is often a foundation model, such as an LLM.

Services are often optimized for production use and are often easier to use than models, via a graphical user interface. However, services are not always available for free, and may require a subscription or payment to use, in exchange for leveraging the service owner’s equipment and resources, optimizing expenses and scaling easily. An example of service is [Azure OpenAI service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), which offers a pay-as-you-go rate plan,  meaning users are charged proportionally to how much they use the service Also, Azure OpenAI service offers enterprise-grade security and responsible AI framework on top of the models' capabilities.

Models are just the Neural Network, with the parameters, weights, and others. Allowing companies to run locally, however, would need to buy equipment, build structure to scale and buy a license or use an open-source model. A model like LLaMA is available to be used, requiring computational power to run the model.

## How to test and iterate with different models to understand performance on Azure

Once our team has explored the current LLMs landscape and identified some good candidates for their scenarios, the next step is testing them on their data and on their workload. This is an iterative process, done by experiments and measures.
Most of the models we mentioned in previous paragraphs (OpenAI models, open source models like Llama2, and Hugging Face transformers) are available in the [Foundation Models](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) catalog in [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst) is a Cloud Service designed for data scientists and ML engineers to manage the whole ML lifecycle (train, test, deploy and handle MLOps) in a single platform. The Machine Learning studio offers a graphical user interface to this service and enables the user to:

- Find the Foundation Model of interest in the catalog, filtering by task, license, or name. It’s also possible to import new models that are not yet included in the catalog.
- Review the model card, including a detailed description and code samples, and test it with the Sample Inference widget, by providing a sample prompt to test the result.

![Model card](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- Evaluate model performance with objective evaluation metrics on a specific workload and a specific set of data provided in input.

![Model evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Fine-tune the model on custom training data to improve model performance in a specific workload, leveraging the experimentation and tracking capabilities of Azure Machine Learning.

![Model fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Deploy the original pre-trained model or the fine-tuned version to a remote real time inference or batch endpoint, to enable applications to consume it.

![Model deployment](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## Improving LLM results

We’ve explored with our startup team different kinds of LLMs and a Cloud Platform (Azure Machine Learning) enabling us to compare different models, evaluate them on test data, improve performance and deploy them on inference endpoints.

But when shall they consider fine-tuning a model rather than using a pre-trained one? Are there other approaches to improve model performance on specific workloads?

There are several approaches a business can use to get the results they need from an LLM, you can select different types of models with different degrees of training

deploy an LLM in production, with different levels of complexity, cost, and quality. Here are some different approaches:

- **Prompt engineering with context**. The idea is to provide enough context when you prompt to ensure you get the responses you need.

- **Retrieval Augmented Generation, RAG**. Your data might exist in a database or web endpoint for example, to ensure this data, or a subset of it, is included at the time of prompting, you can fetch the relevant data and make that part of the user's prompt.

- **Fine-tuned model**. Here, you trained the model further on your own data which leads to the model being more exact and responsive to your needs but might be costly.

![LLMs deployment](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Img source: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering with Context

Pre-trained LLMs work very well on generalized natural language tasks, even by calling them with a short prompt, like a sentence to complete or a question – the so-called “zero-shot” learning.

However, the more the user can frame their query, with a detailed request and examples – the Context – the more accurate and closest to user’s expectations the answer will be. In this case, we talk about “one-shot” learning if the prompt includes only one example and “few shot learning” if it includes multiple examples.
Prompt engineering with context is the most cost-effective approach to kick-off with.

### Retrieval Augmented Generation (RAG)

LLMs have the limitation that they can use only the data that has been used during their training to generate an answer. This means that they don’t know anything about the facts that happened after their training process, and they cannot access non-public information (like company data).
This can be overcome through RAG, a technique that augments prompt with external data in the form of chunks of documents, considering prompt length limits. This is supported by Vector database tools (like [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) that retrieve the useful chunks from varied pre-defined data sources and add them to the prompt Context.

This technique is very helpful when a business doesn’t have enough data, enough time, or resources to fine-tune an LLM, but still wishes to improve performance on a specific workload and reduce risks of fabrications, i.e., mystification of reality or harmful content.  

### Fine-tuned model

Fine-tuning is a process that leverages transfer learning to ‘adapt’ the model to a downstream task or to solve a specific problem. Differently from few-shot learning and RAG, it results in a new model being generated, with updated weights and biases. It requires a set of training examples consisting of a single input (the prompt) and its associated output (the completion).
This would be the preferred approach if:

- **Using fine-tuned models**. A business would like to use fine-tuned less capable models (like embedding models) rather than high performance models, resulting in a more cost effective and fast solution.

- **Considering latency**. Latency is important for a specific use-case, so it’s not possible to use very long prompts or the number of examples that should be learned from the model doesn’t fit with the prompt length limit.

- **Staying up to date**. A business has a lot of high-quality data and ground truth labels and the resources required to maintain this data up to date over time.

### Trained model

Training an LLM from scratch is without a doubt the most difficult and the most complex approach to adopt, requiring massive amounts of data, skilled resources, and appropriate computational power. This option should be considered only in a scenario where a business has a domain-specific use case and a large amount of domain-centric data.

## Knowledge check

What could be a good approach to improve LLM completion results?

1. Prompt engineering with context
1. RAG
1. Fine-tuned model

A:3, if you have the time and resources and high quality data, fine-tuning is the better option to stay up to date. However, if you're looking at improving things and you're lacking time it's worth considering RAG first.

## 🚀 Challenge

Read up more on how you can [use RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) for your business.

## Great Work, Continue Your Learning

After completing this lesson, check out our [Generative AI Learning collection](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) to continue leveling up your Generative AI knowledge!

Head over to Lesson 3 where we will look at how to [build with Generative AI Responsibly](../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!
