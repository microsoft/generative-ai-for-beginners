<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6b7629b8ee4d7d874a27213e903d86a7",
  "translation_date": "2025-10-17T22:48:15+00:00",
  "source_file": "02-exploring-and-comparing-different-llms/README.md",
  "language_code": "es"
}
-->
# Explorando y comparando diferentes LLMs

[![Explorando y comparando diferentes LLMs](../../../translated_images/02-lesson-banner.ef94c84979f97f60f07e27d905e708cbcbdf78707120553ccab27d91c947805b.es.png)](https://youtu.be/KIRUeDKscfI?si=8BHX1zvwzQBn-PlK)

> _Haz clic en la imagen de arriba para ver el video de esta lección_

En la lección anterior, vimos cómo la IA generativa está transformando el panorama tecnológico, cómo funcionan los Modelos de Lenguaje Extenso (LLMs) y cómo una empresa, como nuestra startup, puede aplicarlos a sus casos de uso y crecer. En este capítulo, vamos a comparar y contrastar diferentes tipos de modelos de lenguaje extenso (LLMs) para entender sus ventajas y desventajas.

El siguiente paso en el camino de nuestra startup es explorar el panorama actual de los LLMs y entender cuáles son adecuados para nuestro caso de uso.

## Introducción

Esta lección cubrirá:

- Diferentes tipos de LLMs en el panorama actual.
- Probar, iterar y comparar diferentes modelos para tu caso de uso en Azure.
- Cómo implementar un LLM.

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Seleccionar el modelo adecuado para tu caso de uso.
- Entender cómo probar, iterar y mejorar el rendimiento de tu modelo.
- Saber cómo las empresas implementan modelos.

## Entender los diferentes tipos de LLMs

Los LLMs pueden clasificarse de varias maneras según su arquitectura, datos de entrenamiento y caso de uso. Entender estas diferencias ayudará a nuestra startup a seleccionar el modelo adecuado para el escenario y a comprender cómo probar, iterar y mejorar el rendimiento.

Existen muchos tipos diferentes de modelos LLM, y tu elección depende de para qué planeas usarlos, tus datos, cuánto estás dispuesto a pagar y más.

Dependiendo de si planeas usar los modelos para texto, audio, video, generación de imágenes, etc., podrías optar por un tipo diferente de modelo.

- **Reconocimiento de audio y voz**. Para este propósito, los modelos tipo Whisper son una excelente opción, ya que son de propósito general y están orientados al reconocimiento de voz. Están entrenados en audio diverso y pueden realizar reconocimiento de voz multilingüe. Aprende más sobre [modelos tipo Whisper aquí](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Generación de imágenes**. Para la generación de imágenes, DALL-E y Midjourney son dos opciones muy conocidas. DALL-E es ofrecido por Azure OpenAI. [Lee más sobre DALL-E aquí](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) y también en el Capítulo 9 de este currículo.

- **Generación de texto**. La mayoría de los modelos están entrenados en generación de texto y tienes una gran variedad de opciones desde GPT-3.5 hasta GPT-4. Tienen diferentes costos, siendo GPT-4 el más caro. Vale la pena explorar el [Azure OpenAI playground](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para evaluar qué modelos se ajustan mejor a tus necesidades en términos de capacidad y costo.

- **Multimodalidad**. Si buscas manejar múltiples tipos de datos en entrada y salida, podrías considerar modelos como [gpt-4 turbo con visión o gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst), las últimas versiones de los modelos de OpenAI, que son capaces de combinar el procesamiento de lenguaje natural con la comprensión visual, permitiendo interacciones a través de interfaces multimodales.

Seleccionar un modelo significa obtener algunas capacidades básicas, que pueden no ser suficientes. A menudo tienes datos específicos de la empresa que de alguna manera necesitas comunicar al LLM. Hay varias opciones sobre cómo abordar esto, más sobre esto en las próximas secciones.

### Modelos Fundamentales versus LLMs

El término Modelo Fundamental fue [acuñado por investigadores de Stanford](https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) y se define como un modelo de IA que sigue ciertos criterios, como:

- **Están entrenados utilizando aprendizaje no supervisado o aprendizaje auto-supervisado**, lo que significa que están entrenados con datos multimodales no etiquetados y no requieren anotaciones o etiquetado humano de datos para su proceso de entrenamiento.
- **Son modelos muy grandes**, basados en redes neuronales muy profundas entrenadas con miles de millones de parámetros.
- **Normalmente están destinados a servir como una ‘base’ para otros modelos**, lo que significa que pueden usarse como punto de partida para construir otros modelos encima, lo cual puede hacerse mediante ajuste fino.

![Modelos Fundamentales versus LLMs](../../../translated_images/FoundationModel.e4859dbb7a825c94b284f17eae1c186aabc21d4d8644331f5b007d809cf8d0f2.es.png)

Fuente de la imagen: [Essential Guide to Foundation Models and Large Language Models | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para aclarar más esta distinción, tomemos ChatGPT como ejemplo. Para construir la primera versión de ChatGPT, se utilizó un modelo llamado GPT-3.5 como modelo fundamental. Esto significa que OpenAI utilizó algunos datos específicos de chat para crear una versión ajustada de GPT-3.5 que estaba especializada en desempeñarse bien en escenarios conversacionales, como los chatbots.

![Modelo Fundamental](../../../translated_images/Multimodal.2c389c6439e0fc51b0b7b226d95d7d900d372ae66902d71b8ce5ec4951b8efbe.es.png)

Fuente de la imagen: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de código abierto versus modelos propietarios

Otra forma de categorizar los LLMs es si son de código abierto o propietarios.

Los modelos de código abierto son modelos que están disponibles para el público y pueden ser utilizados por cualquier persona. A menudo son puestos a disposición por la empresa que los creó o por la comunidad investigadora. Estos modelos pueden ser inspeccionados, modificados y personalizados para los diversos casos de uso en LLMs. Sin embargo, no siempre están optimizados para uso en producción y pueden no ser tan eficientes como los modelos propietarios. Además, la financiación para los modelos de código abierto puede ser limitada y es posible que no se mantengan a largo plazo o que no se actualicen con las últimas investigaciones. Ejemplos de modelos populares de código abierto incluyen [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) y [LLaMA](https://llama.meta.com).

Los modelos propietarios son modelos que son propiedad de una empresa y no están disponibles para el público. Estos modelos suelen estar optimizados para uso en producción. Sin embargo, no se permite que sean inspeccionados, modificados o personalizados para diferentes casos de uso. Además, no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso. También, los usuarios no tienen control sobre los datos que se utilizan para entrenar el modelo, lo que significa que deben confiar en el propietario del modelo para garantizar el compromiso con la privacidad de los datos y el uso responsable de la IA. Ejemplos de modelos propietarios populares incluyen [modelos de OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) o [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embedding versus generación de imágenes versus generación de texto y código

Los LLMs también pueden categorizarse según el tipo de salida que generan.

Los embeddings son un conjunto de modelos que pueden convertir texto en una forma numérica, llamada embedding, que es una representación numérica del texto de entrada. Los embeddings facilitan que las máquinas entiendan las relaciones entre palabras o frases y pueden ser consumidos como entradas por otros modelos, como modelos de clasificación o modelos de agrupamiento que tienen mejor rendimiento con datos numéricos. Los modelos de embedding se utilizan a menudo para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la cual hay una abundancia de datos, y luego los pesos del modelo (embeddings) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría es [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../../translated_images/Embedding.c3708fe988ccf76073d348483dbb7569f622211104f073e22e43106075c04800.es.png)

Los modelos de generación de imágenes son modelos que generan imágenes. Estos modelos se utilizan a menudo para edición de imágenes, síntesis de imágenes y traducción de imágenes. Los modelos de generación de imágenes suelen estar entrenados en grandes conjuntos de datos de imágenes, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y pueden usarse para generar nuevas imágenes o para editar imágenes existentes con técnicas de inpainting, super-resolución y colorización. Ejemplos incluyen [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [modelos de Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../../translated_images/Image.349c080266a763fd255b840a921cd8fc526ed78dc58708fa569ff1873d302345.es.png)

Los modelos de generación de texto y código son modelos que generan texto o código. Estos modelos se utilizan a menudo para resumen de texto, traducción y respuesta a preguntas. Los modelos de generación de texto suelen estar entrenados en grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden usarse para generar nuevo texto o para responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), suelen estar entrenados en grandes conjuntos de datos de código, como GitHub, y pueden usarse para generar nuevo código o para corregir errores en código existente.

![Generación de texto y código](../../../translated_images/Text.a8c0cf139e5cc2a0cd3edaba8d675103774e6ddcb3c9fc5a98bb17c9a450e31d.es.png)

### Encoder-Decoder versus solo Decoder

Para hablar sobre los diferentes tipos de arquitecturas de LLMs, usemos una analogía.

Imagina que tu gerente te dio la tarea de escribir un cuestionario para los estudiantes. Tienes dos colegas; uno se encarga de crear el contenido y el otro de revisarlo.

El creador de contenido es como un modelo solo Decoder, puede mirar el tema y ver lo que ya escribiste y luego escribir un curso basado en eso. Son muy buenos escribiendo contenido atractivo e informativo, pero no son muy buenos entendiendo el tema y los objetivos de aprendizaje. Algunos ejemplos de modelos Decoder son los modelos de la familia GPT, como GPT-3.

El revisor es como un modelo solo Encoder, mira el curso escrito y las respuestas, notando la relación entre ellos y entendiendo el contexto, pero no es bueno generando contenido. Un ejemplo de modelo solo Encoder sería BERT.

Imagina que también podemos tener a alguien que pueda crear y revisar el cuestionario, este es un modelo Encoder-Decoder. Algunos ejemplos serían BART y T5.

### Servicio versus Modelo

Ahora, hablemos de la diferencia entre un servicio y un modelo. Un servicio es un producto que ofrece un proveedor de servicios en la nube y suele ser una combinación de modelos, datos y otros componentes. Un modelo es el componente central de un servicio y suele ser un modelo fundamental, como un LLM.

Los servicios suelen estar optimizados para uso en producción y son más fáciles de usar que los modelos, a través de una interfaz gráfica de usuario. Sin embargo, los servicios no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso, a cambio de aprovechar el equipo y los recursos del propietario del servicio, optimizando gastos y escalando fácilmente. Un ejemplo de servicio es [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que ofrece un plan de tarifas de pago por uso, lo que significa que los usuarios son cobrados proporcionalmente a cuánto usan el servicio. Además, Azure OpenAI Service ofrece seguridad de nivel empresarial y un marco de IA responsable sobre las capacidades de los modelos.

Los modelos son solo la red neuronal, con los parámetros, pesos y otros. Permiten a las empresas ejecutarlos localmente, aunque necesitarían comprar equipos, construir una estructura para escalar y comprar una licencia o usar un modelo de código abierto. Un modelo como LLaMA está disponible para ser usado, requiriendo poder computacional para ejecutar el modelo.

## Cómo probar e iterar con diferentes modelos para entender el rendimiento en Azure

Una vez que nuestro equipo ha explorado el panorama actual de los LLMs e identificado algunos buenos candidatos para sus escenarios, el siguiente paso es probarlos con sus datos y su carga de trabajo. Este es un proceso iterativo, realizado mediante experimentos y mediciones.
La mayoría de los modelos que mencionamos en los párrafos anteriores (modelos de OpenAI, modelos de código abierto como Llama2 y transformadores de Hugging Face) están disponibles en el [Catálogo de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) en [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) es una plataforma en la nube diseñada para que los desarrolladores construyan aplicaciones de IA generativa y gestionen todo el ciclo de desarrollo, desde la experimentación hasta la evaluación, combinando todos los servicios de Azure AI en un único centro con una interfaz gráfica fácil de usar. El Catálogo de Modelos en Azure AI Studio permite al usuario:

- Encontrar el modelo base de interés en el catálogo, ya sea propietario o de código abierto, filtrando por tarea, licencia o nombre. Para mejorar la búsqueda, los modelos están organizados en colecciones, como la colección Azure OpenAI, la colección Hugging Face y más.

![Catálogo de modelos](../../../translated_images/AzureAIStudioModelCatalog.3cf8a499aa8ba0314f2c73d4048b3225d324165f547525f5b7cfa5f6c9c68941.es.png)

- Revisar la tarjeta del modelo, que incluye una descripción detallada del uso previsto y los datos de entrenamiento, ejemplos de código y resultados de evaluación en la biblioteca interna de evaluaciones.

![Tarjeta del modelo](../../../translated_images/ModelCard.598051692c6e400d681a713ba7717e8b6e5e65f08d12131556fcec0f1789459b.es.png)

- Comparar benchmarks entre modelos y conjuntos de datos disponibles en la industria para evaluar cuál se adapta mejor al escenario empresarial, a través del panel de [Benchmarks de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Benchmarks de modelos](../../../translated_images/ModelBenchmarks.254cb20fbd06c03a4ca53994585c5ea4300a88bcec8eff0450f2866ee2ac5ff3.es.png)

- Ajustar el modelo con datos de entrenamiento personalizados para mejorar el rendimiento del modelo en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure AI Studio.

![Ajuste del modelo](../../../translated_images/FineTuning.aac48f07142e36fddc6571b1f43ea2e003325c9c6d8e3fc9d8834b771e308dbf.es.png)

- Desplegar el modelo preentrenado original o la versión ajustada para una inferencia en tiempo real en un entorno de cómputo gestionado o en un endpoint de API sin servidor - [pago por uso](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview#model-deployment-managed-compute-and-serverless-api-pay-as-you-go?WT.mc_id=academic-105485-koreyst) - para habilitar su consumo en aplicaciones.

![Despliegue del modelo](../../../translated_images/ModelDeploy.890da48cbd0bccdb4abfc9257f3d884831e5d41b723e7d1ceeac9d60c3c4f984.es.png)

> [!NOTE]
> No todos los modelos en el catálogo están disponibles actualmente para ajuste y/o despliegue bajo el modelo de pago por uso. Consulta la tarjeta del modelo para obtener detalles sobre las capacidades y limitaciones del modelo.

## Mejorando los resultados de los LLM

Hemos explorado con nuestro equipo de startups diferentes tipos de LLMs y una plataforma en la nube (Azure Machine Learning) que nos permite comparar diferentes modelos, evaluarlos con datos de prueba, mejorar su rendimiento y desplegarlos en endpoints de inferencia.

Pero, ¿cuándo deberían considerar ajustar un modelo en lugar de usar uno preentrenado? ¿Existen otros enfoques para mejorar el rendimiento del modelo en cargas de trabajo específicas?

Hay varios enfoques que una empresa puede utilizar para obtener los resultados que necesita de un LLM. Puedes seleccionar diferentes tipos de modelos con distintos grados de entrenamiento al desplegar un LLM en producción, con diferentes niveles de complejidad, costo y calidad. Aquí hay algunos enfoques diferentes:

- **Ingeniería de prompts con contexto**. La idea es proporcionar suficiente contexto al realizar el prompt para garantizar que obtengas las respuestas que necesitas.

- **Generación Aumentada por Recuperación, RAG**. Tus datos podrían estar en una base de datos o un endpoint web, por ejemplo. Para garantizar que estos datos, o un subconjunto de ellos, se incluyan al momento de realizar el prompt, puedes recuperar los datos relevantes y hacer que formen parte del prompt del usuario.

- **Modelo ajustado**. Aquí, entrenas el modelo adicionalmente con tus propios datos, lo que hace que el modelo sea más preciso y responda mejor a tus necesidades, aunque puede ser costoso.

![Despliegue de LLMs](../../../translated_images/Deploy.18b2d27412ec8c02871386cbe91097c7f2190a8c6e2be88f66392b411609a48c.es.png)

Fuente de la imagen: [Cuatro formas en que las empresas despliegan LLMs | Blog de Fiddler AI](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Ingeniería de Prompts con Contexto

Los LLM preentrenados funcionan muy bien en tareas generales de lenguaje natural, incluso llamándolos con un prompt corto, como una oración para completar o una pregunta: el llamado aprendizaje "zero-shot".

Sin embargo, cuanto más pueda el usuario enmarcar su consulta, con una solicitud detallada y ejemplos - el Contexto - más precisa y cercana a las expectativas del usuario será la respuesta. En este caso, hablamos de aprendizaje "one-shot" si el prompt incluye solo un ejemplo y de "few-shot learning" si incluye múltiples ejemplos. La ingeniería de prompts con contexto es el enfoque más rentable para comenzar.

### Generación Aumentada por Recuperación (RAG)

Los LLMs tienen la limitación de que solo pueden usar los datos que se han utilizado durante su entrenamiento para generar una respuesta. Esto significa que no saben nada sobre los hechos que ocurrieron después de su proceso de entrenamiento y no pueden acceder a información no pública (como datos de la empresa).  
Esto se puede superar mediante RAG, una técnica que aumenta el prompt con datos externos en forma de fragmentos de documentos, considerando los límites de longitud del prompt. Esto es compatible con herramientas de bases de datos vectoriales (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperan los fragmentos útiles de diversas fuentes de datos predefinidas y los agregan al Contexto del prompt.

Esta técnica es muy útil cuando una empresa no tiene suficientes datos, tiempo o recursos para ajustar un LLM, pero aún desea mejorar el rendimiento en una carga de trabajo específica y reducir los riesgos de fabricaciones, es decir, distorsión de la realidad o contenido dañino.

### Modelo ajustado

El ajuste es un proceso que aprovecha el aprendizaje por transferencia para "adaptar" el modelo a una tarea específica o resolver un problema concreto. A diferencia del aprendizaje de pocos ejemplos y RAG, resulta en la generación de un nuevo modelo, con pesos y sesgos actualizados. Requiere un conjunto de ejemplos de entrenamiento que consisten en una única entrada (el prompt) y su salida asociada (la respuesta).  
Este sería el enfoque preferido si:

- **Uso de modelos ajustados**. Una empresa desea utilizar modelos ajustados menos capaces (como modelos de embeddings) en lugar de modelos de alto rendimiento, lo que resulta en una solución más rentable y rápida.

- **Considerando la latencia**. La latencia es importante para un caso de uso específico, por lo que no es posible usar prompts muy largos o el número de ejemplos que deberían ser aprendidos por el modelo no encaja con el límite de longitud del prompt.

- **Mantenerse actualizado**. Una empresa tiene muchos datos de alta calidad y etiquetas de verdad base, así como los recursos necesarios para mantener estos datos actualizados con el tiempo.

### Modelo entrenado

Entrenar un LLM desde cero es, sin duda, el enfoque más difícil y complejo de adoptar, ya que requiere cantidades masivas de datos, recursos calificados y potencia computacional adecuada. Esta opción solo debería considerarse en un escenario donde una empresa tenga un caso de uso específico para un dominio y una gran cantidad de datos centrados en ese dominio.

## Comprobación de conocimientos

¿Cuál podría ser un buen enfoque para mejorar los resultados de las respuestas de un LLM?

1. Ingeniería de prompts con contexto  
1. RAG  
1. Modelo ajustado  

A:3, si tienes el tiempo, los recursos y datos de alta calidad, el ajuste es la mejor opción para mantenerse actualizado. Sin embargo, si estás buscando mejorar las cosas y te falta tiempo, vale la pena considerar primero RAG.

## 🚀 Desafío

Investiga más sobre cómo puedes [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para tu negocio.

## ¡Buen trabajo! Continúa aprendiendo

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA generativa.

Dirígete a la Lección 3, donde veremos cómo [construir con IA generativa de manera responsable](../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.