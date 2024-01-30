# Explorando y comparando diferentes LLM (Grandes modelos de lenguaje)

[![Explorando y comparando diferentes LLMs](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/J1mWzw0P74c?WT.mc_id=academic-105485-koreyst)

> *Haz clic en la imagen de arriba para ver el video de esta lección*

Con la lección anterior, hemos visto cómo la Inteligencia Artificial Generativa está cambiando el panorama tecnológico, cómo funcionan los Grandes Modelos del Lenguaje (LLMs) y cómo una empresa, como nuestra startup, puede aplicarlos a sus casos de uso y crecer. En este capítulo, estamos buscando comparar y contrastar diferentes tipos de modelos de lenguaje grandes, LLMs, para entender sus ventajas y desventajas.

El siguiente paso en la trayectoria de nuestra startup es explorar el panorama actual de los Grandes Modelos del Lenguaje (LLMs) y comprender cuáles son adecuados para nuestro caso de uso.

## Introducción

Esta lección abordará:

-Diferentes tipos de Modelos de Lenguaje Grandes (LLMs) en el panorama actual.
-Pruebas, iteraciones y comparaciones de diferentes modelos para tu caso de uso en Azure.
-Cómo implementar un LLM.

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

-Seleccionar el modelo adecuado para tu caso de uso.
-Comprender cómo probar, iterar y mejorar el rendimiento de tu modelo.
-Conocer cómo las empresas implementan modelos.

## Comprender diferentes tipos LLMs.

Los Grandes Modelos del Lenguaje (LLMs) pueden tener múltiples categorizaciones basadas en su arquitectura, datos de entrenamiento y caso de uso. Comprender estas diferencias ayudará a nuestra startup a seleccionar el modelo adecuado para el escenario y entender cómo probar, iterar y mejorar el rendimiento.

Existen muchos tipos diferentes de modelos de LLM, la elección del modelo depende de para qué planeas utilizarlos, tus datos, cuánto estás dispuesto a pagar y otros factores más.

Dependiendo de si planeas utilizar los modelos para generación de texto, audio, video, imágenes, entre otros, es posible que optes por un tipo de modelo diferente.

- **Reconocimiento de audio y voz**. Para este propósito, los modelos tipo Whisper son una excelente elección, ya que son de propósito general y están diseñados para el reconocimiento de voz. Están entrenados en audio diverso y pueden realizar reconocimiento de voz multilingüe. Obtén más información sobre ellos en: [Modelos tipo Whisper aquí](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Generación de imágenes**. Para la generación de imágenes, DALL-E y Midjourney son dos opciones muy conocidas. DALL-E es ofrecido por Azure OpenAI. [Lee más sobre DALL-E aquí](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) y también en el Capítulo 9 de este curso.

- **Generación de texto**. La mayoría de los modelos están entrenados en generación de texto y tienes una amplia variedad de opciones, desde GPT-3.5 hasta GPT-4. Tienen diferentes costos, siendo GPT-4 el más caro. Vale la pena investigar más al respecto. [Azure Open AI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para evaluar cuáles modelos se ajustan mejor a tus necesidades en términos de capacidad y costo.

Seleccionar un modelo te brinda algunas capacidades básicas, que podrían no ser suficientes. A menudo, tienes datos específicos de la empresa que necesitas de alguna manera transmitir al LLM. Hay algunas opciones diferentes sobre cómo abordar eso, más detalles en las secciones próximas.

### Modelos Fundacionales versus grandes modelos del Lenguaje (LLMs).

El término "Modelo Fundacional" [fue acuñado por investigadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) y se define como un modelo de inteligencia artificial que sigue ciertos criterios, tales como:

- **Son entrenados utilizando aprendizaje no supervisado o aprendizaje auto-supervisado**, Lo que significa que se entrenan con datos multimodales no etiquetados y no requieren anotación humana o etiquetado de datos para su proceso de entrenamiento.
- **Son modelos muy grandes**, Basados en redes neuronales muy profundas entrenadas con miles de millones de parámetros.
- **Normalmente están destinados a servir como una "base" para otros modelos**, Lo que significa que pueden usarse como punto de partida para que otros modelos se construyan sobre ellos, lo cual se puede hacer mediante el ajuste fino (fine-tuning).

![Modelos fundqacionales vs Grandes Modelos del Lenguaje](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [Guía Esencial sobre Modelos Fundacionales y Grandes Modelos del Lenguaje | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para aclarar aún más esta distinción, tomemos ChatGPT como ejemplo. Para construir la primera versión de ChatGPT, se utilizó un modelo llamado GPT-3.5 como modelo base. Esto significa que OpenAI utilizó datos específicos de conversación para crear una versión ajustada de GPT-3.5 especializada en rendir bien en escenarios conversacionales, como chatbots.

![Modelo Fundacional](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de Código Abierto versus Modelos Propios

Otra forma de categorizar los LLMs es si son de código abierto o propietarios.

Los modelos de código abierto son modelos que se ponen a disposición del público y pueden ser utilizados por cualquier persona. A menudo son proporcionados por la empresa que los creó o por la comunidad de investigación. Estos modelos pueden ser inspeccionados, modificados y personalizados para diversos casos de uso en los LLMs. Sin embargo, no siempre están optimizados para su uso en producción y pueden no ser tan eficientes como los modelos propietarios. Además, la financiación para modelos de código abierto puede ser limitada y es posible que no se mantengan a largo plazo o no se actualicen con las últimas investigaciones. Ejemplos de modelos de código abierto populares incluyen [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst) y [LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst).

Los modelos propios son modelos que pertenecen a una empresa y no se ponen a disposición del público. Estos modelos suelen estar optimizados para su uso en producción. Sin embargo, no se permite inspeccionar, modificar o personalizar estos modelos para diferentes casos de uso. Además, no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso. También, los usuarios no tienen control sobre los datos utilizados para entrenar el modelo, lo que significa que deben confiar en el propietario del modelo para garantizar el compromiso con la privacidad de los datos y el uso responsable de la inteligencia artificial. Ejemplos de modelos propietarios populares incluyen [Modelos de OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) or [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Incrustación (Embedding) versus Generación de Imágenes versus Generación de Texto y Código.

Los LLMs también pueden categorizarse según la salida que generan.

Las incrustaciones (Embeddings) son un conjunto de modelos que pueden convertir el texto en una forma numérica, llamada incrustación, que es una representación numérica del texto de entrada. Las incrustaciones facilitan que las máquinas comprendan las relaciones entre palabras o oraciones y pueden ser consumidas como entradas por otros modelos, como modelos de clasificación o modelos de agrupamiento que tienen un mejor rendimiento en datos numéricos. Los modelos de incrustación a menudo se utilizan para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la cual hay abundancia de datos, y luego los pesos del modelo (incrustaciones) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría es [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de imágenes son modelos que generan imágenes. Estos modelos se utilizan a menudo para la edición de imágenes, síntesis de imágenes y traducción de imágenes. Los modelos de generación de imágenes a menudo se entrenan en grandes conjuntos de datos de imágenes, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y se pueden utilizar para generar nuevas imágenes o editar imágenes existentes con técnicas de rellenado, súper resolución y colorización. Ejemplos incluyen [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de texto y código son modelos que generan texto o código. Estos modelos se utilizan a menudo para la sumarización de texto, la traducción y la respuesta a preguntas. Los modelos de generación de texto a menudo se entrenan en grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar nuevo texto o responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), a menudo se entrenan en grandes conjuntos de datos de código, como GitHub, y se pueden utilizar para generar nuevo código o corregir errores en el código existente.

 ![Generación de texto y código](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Codificador-Decodificador versus Solo Decodificador

Para hablar sobre los diferentes tipos de arquitecturas de LLMs, usemos una analogía.

Imagina que tu jefe te asignó la tarea de escribir un cuestionario para los estudiantes. Tienes dos colegas; uno se encarga de crear el contenido y el otro se encarga de revisarlo.

El creador de contenido es como un modelo solo de decodificación, pueden mirar el tema y ver lo que ya escribiste y luego pueden escribir un curso basado en eso. Son muy buenos escribiendo contenido atractivo e informativo, pero no son muy buenos entendiendo el tema y los objetivos de aprendizaje. Algunos ejemplos de modelos de decodificación son los modelos de la familia GPT, como GPT-3.

El revisor es como un modelo solo de codificación, ellos miran el curso escrito y las respuestas, notando la relación entre ellos y entendiendo el contexto, pero no son buenos generando contenido. Un ejemplo de modelo solo de codificación sería BERT.

Imagina que también podemos tener a alguien que pueda crear y revisar el cuestionario, este es un modelo codificador-decodificador. Algunos ejemplos serían BART y T5.

### Servicio versus modelo

Ahora, hablemos sobre la diferencia entre un servicio y un modelo. Un servicio es un producto que ofrece un proveedor de servicios en la nube y a menudo es una combinación de modelos, datos y otros componentes. Un modelo es el componente central de un servicio y a menudo es un modelo base, como un LLM.

Los servicios a menudo están optimizados para su uso en producción y suelen ser más fáciles de usar que los modelos, a través de una interfaz gráfica de usuario. Sin embargo, los servicios no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso, a cambio de aprovechar el equipo y los recursos del propietario del servicio, optimizando gastos y escalando fácilmente. Un ejemplo de servicio es un servicio de almacenamiento en la nube como Dropbox o Google Drive.[Servicio de Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), el cual ofrece un plan de tarifas de pago por uso, lo que significa que los usuarios son cobrados de manera proporcional a la cantidad que utilicen el servicio. Además, el servicio proporciona seguridad de nivel empresarial y un marco de inteligencia artificial responsable que se suma a las capacidades de los modelos.

Los modelos son simplemente la red neuronal, con sus parámetros, pesos y otros atributos. Permiten a las empresas ejecutarlos localmente; sin embargo, esto requeriría la compra de equipos, la construcción de una estructura escalable y la adquisición de una licencia o el uso de un modelo de código abierto. Un modelo como LLaMA está disponible para su uso, pero requiere potencia computacional para ejecutar el modelo.

## Cómo probar e iterar con diferentes modelos para entender el rendimiento en Azure

Una vez que nuestro equipo ha explorado el panorama actual de los Modelos de Lenguaje de Gran Escala (LLMs, por sus siglas en inglés) e identificado algunos buenos candidatos para sus escenarios, el siguiente paso es probarlos con sus datos y su carga de trabajo. Este es un proceso iterativo, realizado mediante experimentos y medidas. La mayoría de los modelos que mencionamos en los párrafos anteriores (modelos de OpenAI, modelos de código abierto como Llama2 y transformadores de Hugging Face) están disponibles en los [Modelos Base](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) catalogo en [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst)es un servicio en la nube diseñado para científicos de datos e ingenieros de aprendizaje automático para gestionar todo el ciclo de vida del aprendizaje automático (entrenamiento, prueba, implementación y manejo de MLOps) en una sola plataforma. El estudio de aprendizaje automático ofrece una interfaz gráfica de usuario para este servicio y permite al usuario:

- Encontrar el Modelo Base de interés en el catálogo, filtrando por tarea, licencia o nombre. También es posible importar nuevos modelos que aún no estén incluidos en el catálogo.
- Revisar la ficha del modelo, que incluye una descripción detallada y ejemplos de código, y probarlo con el widget de Inferencia de Muestra, proporcionando un ejemplo de indicación para probar el resultado.
![Model card](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- Evaluar el rendimiento del modelo con métricas de evaluación objetiva en una carga de trabajo específica y un conjunto de datos específico proporcionado como entrada.

![Model evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Ajustar el modelo con datos de entrenamiento personalizados para mejorar el rendimiento del modelo en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure Machine Learning.

![Model fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Despliega el modelo pre-entrenado original o la versión ajustada a un punto final remoto de inferencia en tiempo real o por lotes, para permitir que las aplicaciones lo consuman.

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

Head over to Lesson 3 where we will look at how to [build with Generative AI Responsibly](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!
