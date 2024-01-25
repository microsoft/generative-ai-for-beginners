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

### Modelos Fundacionales versus Modelos Grandes de Lenguaje

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

Otra manera de categorizar los LLMs es si son de código abierto o propietarios.

Los modelos de código abierto son modelos que se ponen a disposición del público y pueden ser utilizados por cualquiera. A menudo son publicados por la empresa que los creó o por la comunidad investigadora. Estos modelos pueden ser inspeccionados, modificados y personalizados para diversos casos de uso en LLMs. Sin embargo, no siempre están optimizados para uso en producción y pueden no ser tan eficientes como los modelos propietarios. Además, la financiación para modelos de código abierto puede ser limitada, y es posible que no se mantengan a largo plazo o que no se actualicen con las últimas investigaciones. Algunos ejemplos de modelos de código abierto populares incluyen:  [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://sapling.ai/llm/bloom?WT.mc_id=academic-105485-koreyst) and [LLaMA](https://sapling.ai/llm/llama?WT.mc_id=academic-105485-koreyst).

Los modelos propietarios son modelos que son propiedad de una empresa y no se ponen a disposición del público. Estos modelos suelen estar optimizados para su uso en producción. Sin embargo, no se permite su inspección, modificación o personalización para diferentes casos de uso. Además, no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso. Asimismo, los usuarios no tienen control sobre los datos utilizados para entrenar el modelo, lo que significa que deben confiar en el propietario del modelo para garantizar el compromiso con la privacidad de los datos y el uso responsable de la IA. Algunos ejemplos de modelos propietarios populares incluyen [modelos de OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) o [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Embeddings versus Generación de Imágenes versus Generación de Texto y Código

Los LLMs también pueden ser categorizados por la salida que generan.

Los embeddings son un conjunto de modelos que pueden convertir texto en una forma numérica, llamada embedding, que es una representación numérica del texto de entrada. Los embeddings facilitan que las máquinas comprendan las relaciones entre palabras u oraciones y pueden ser utilizadas como entradas por otros modelos, como modelos de clasificación o modelos de agrupación que tienen un mejor rendimiento con los datos numéricos. Los modelos de embeddings usualmente se utilizan para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la cual hay gran cantidad de datos, y luego los pesos del modelo (embeddings) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría es [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Embedding](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de imágenes son modelos que crean imágenes. Estos modelos suelen utilizarse para la edición de imágenes, la síntesis de imágenes y la traducción de imágenes. Los modelos de generación de imágenes con regularidad son entrenados en grandes conjuntos de datos de imágenes, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar nuevas imágenes o para editar imágenes existentes con técnicas de inpainting, super-resolución y colorización. Ejemplos incluyen [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [modelos de Stable Diffusion](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de texto y código son modelos que generan texto o código. Estos modelos suelen utilizarse para resumir texto, traducir y responder preguntas. Los modelos de generación de texto suelen ser entrenados en grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar texto o responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), en muchas ocasiones se entrenan en grandes conjuntos de datos de código, como GitHub, y pueden utilizarse para crear código nuevo o para corregir errores en código existente.

 ![Generación de texto y código](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Codificador-Decodificador versus Solo-Decodificador

Para hablar sobre los diferentes tipos de arquitecturas de LLMs, utilicemos una analogía.

Imagina que tu jefe te asignó la tarea de escribir un cuestionario para los estudiantes. Tienes dos colegas; uno se encarga de crear el contenido y el otro se encarga de revisarlo.

El creador de contenido es como un modelo Solo-Decodificador, puede mirar el tema y ver lo que escribiste, y luego puede escribir un curso basado en eso. Son muy buenos escribiendo contenido atractivo e informativo, pero no son muy buenos entendiendo el tema y los objetivos de aprendizaje. Algunos ejemplos de modelos decodificadores son los modelos de la familia GPT, como GPT-3.

El revisor es como un modelo Solo-Codificador, observa el curso escrito y las respuestas, notando la relación entre ellos y comprendiendo el contexto, pero no es bueno generando contenido. Un ejemplo de modelo Solo-Codificador sería BERT.

Imagina que también podemos tener a alguien que pueda crear y revisar el cuestionario, esto sería un modelo Codificador-Decodificador. Algunos ejemplos como BART y T5.

### Servicio versus Modelo

Ahora, hablemos de la diferencia entre un servicio y un modelo. Un servicio es un producto ofrecido por un Proveedor de Servicios en la Nube y suele ser una combinación de modelos, datos y otros componentes. Un modelo es el componente central de un servicio y a veces es un modelo fundacional, como un LLM.

Los servicios suelen estar optimizados para su uso en producción y son más fáciles de utilizar que los modelos, a través de una interfaz gráfica de usuario. Sin embargo, los servicios no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso, a cambio de aprovechar la infraestructura y los recursos del propietario del servicio, optimizando gastos y escalando fácilmente. Un ejemplo de servicio es [el servicio de Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), el cual ofrece un plan de tarifas de pago por uso, lo que significa que los usuarios pagan en proporción a qué tanto utilizan el servicio. Además, el servicio Azure OpenAI brinda seguridad de nivel empresarial y un marco de IA responsable, complementando las capacidades de los modelos.

Los modelos son simplemente la Red Neuronal, con los parámetros, pesos y otros elementos. Sin embargo, permitir que las empresas los ejecuten localmente requeriría la compra de hardware, la construcción de una infraestructura para escalar y la adquisición de una licencia o el uso de un modelo de código abierto. Un modelo como LLaMA está disponible para su uso, requieriendo una potencia de computo para ejecutarlo.

## Cómo probar e iterar con diferentes modelos para entender el rendimiento en Azure

Una vez que nuestro equipo haya explorado el panorama actual de los LLMs e identificado algunos candidatos prometedores para sus escenarios, el siguiente paso es probarlos con sus datos y sus cargas de trabajo. Este es un proceso iterativo, realizado mediante experimentos y mediciones. La mayoría de los modelos que mencionamos en párrafos anteriores (modelos de OpenAI, modelos de código abierto como Llama2 y transformadores de Hugging Face) están disponibles en el catálogo de [Modelos Fundacionales](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) en [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst) es un Servicio en la Nube diseñado para científicos de datos e ingenieros de ML para gestionar todo el ciclo de vida de ML (entrenar, probar, implementar y gestionar MLOps) en una sola plataforma. Machine Learning studio ofrece una interfaz gráfica de usuario para este servicio y permite al usuario:

- Encontrar el Modelo Fundacional de interés en el catálogo, filtrando por tarea, licencia o nombre. También es posible importar nuevos modelos que aún no estén incluidos en el catálogo.
- Revisar la tarjeta del modelo, que incluye una descripción detallada y ejemplos de código, y probarlo con el widget de Inferencia de Muestra, proporcionando un ejemplo de prompt para evaluar el resultado.

![Tarjeta del modelo](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- Evaluar el rendimiento del modelo con métricas de evaluación objetivas en una carga de trabajo específica y un conjunto específico de datos proporcionados en la entrada.

![Evaluación del modelo](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Ajustar el modelo con datos de entrenamiento personalizados para mejorar el rendimiento del modelo en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure Machine Learning.

![Ajuste fino del modelo](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Desplegar el modelo original preentrenado o la versión afinada en un endpoint remoto de inferencia en tiempo real o por lotes, para que las aplicaciones puedan consumirlo.

![Despliegue del modelo.](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## Mejorar los resultados de los LLMs

Hemos explorado con nuestro equipo de startup diferentes tipos de LLMs y una Plataforma en la Nube (Azure Machine Learning) que nos permite comparar diferentes modelos, evaluarlos con datos de prueba, y mejorar el rendimiento y desplegarlos en endpoints de inferencia.

Pero, ¿cuándo deberían considerar ajustar un modelo en lugar de usar uno preentrenado? ¿Existen otras estrategias para mejorar el rendimiento del modelo en cargas de trabajo específicas?

Existen varios enfoques que una empresa puede utilizar para obtener los resultados que necesita de un LLM, puedes seleccionar diferentes tipos de modelos con diferentes niveles de entrenamiento.

Desplegar un LLM en producción, con diferentes niveles de complejidad, costos y calidad. Aquí hay algunas estrategias diferentes:

- **Prompt engineering con contexto**. La idea es proporcionar un prompt con suficiente contexto para asegurarse de obtener las respuestas que necesitas.

- **Generación Aumentada de Recuperación, RAG**. Por ejemplo, tus datos pueden existir en una base de datos o un endpoint web, y para garantizar que estos datos, o un subconjunto de ellos, se incluyan al realizar el prompting, puedes recuperar los datos relevantes y hacer que formen parte del prompt del usuario.

- **Modelo afinado**. En este caso, entrenaste el modelo con mayor detalle utilizando tus propios datos, lo que lo hace más preciso y capaz de responder a tus necesidades, aunque puede ser costoso.

![Implementación de LLMs](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [Cuatro Formas en que las Empresas Implementan LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering con contexto

Los LLMs preentrenados funcionan muy bien en tareas generalizadas de lenguaje natural, incluso al llamarlos con un prompt breve, como una oración por completar o una pregunta, lo que se conoce como aprendizaje de "zero-shot".

No obstante, cuanto más pueda el usuario formular su consulta, con una solicitud detallada y ejemplos - el Contexto - más precisa y acorde a las expectativas del usuario será la respuesta. En este, hablamos de aprendizaje de “one-shot” si el prompt incluye solo un ejemplo y de “few shot learning” si se proporcionan varios ejemplos. Prompt engineering con contexto es el enfoque más eficaz desde el punto de vista económico para comenzar.

### Generación Aumentada de Recuperación (RAG)

Los LLMs tienen la limitación de que solo pueden utilizar los datos que se utilizaron durante su entrenamiento para generar una respuesta. Esto significa que no saben nada acerca de los hechos que ocurrieron después de su proceso de entrenamiento y no pueden acceder a información no pública (como datos de la empresa).
Esto se puede superar mediante RAG, una técnica que amplía el prompt con datos externos en forma de fragmentos de documentos, teniendo en cuenta los límites de longitud del prompt. Esto es respaldado por las herramientas de base de datos vectoriales (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperan los fragmentos útiles de diversas fuentes de datos predefinidas y los añaden al contexto del prompt.

Esta técnica es muy útil cuando una empresa no dispone de suficientes datos, tiempo o recursos para ajustar un LLM, pero aún desea mejorar el rendimiento en una carga de trabajo específica y reducir los riesgos de generar fabricaciones, es decir, la distorsión de la realidad o contenido perjudicial.

### Modelo afinado

El ajuste fino es un proceso que utiliza el aprendizaje por transferencia para "adaptar" el modelo a una tarea posterior o para resolver un problema específico. A diferencia del aprendizaje few-shot y RAG, esto resulta en la generación de un nuevo modelo con pesos y sesgos actualizados. Requiere un conjunto de ejemplos de entrenamiento que consisten en una única entrada (el prompt) y su salida asociada (la finalización).

Este sería el enfoque preferido si:

- **Utilizando modelos ajustados**. Una empresa le gustaría utilizar modelos ajustados menos capaces (como modelos de embedding) en lugar de modelos de alto rendimiento, lo que resultaría en una solución más rentable y rápida.

- **Teniendo en cuenta la latencia**. La latencia es importante para un caso de uso específico, por lo que no es posible utilizar prompts extensos o el número de ejemplos que deberían ser aprendidos del modelo no se ajusta al límite de longitud del prompt.

- **Mantenerse actualizado**. Una empresa cuenta con una gran cantidad de datos de alta calidad y etiquetas de verdad fundamental, así como los recursos necesarios para mantener actualizados estos datos con el tiempo.

### Modelo entrenado

Entrenar un LLM desde cero es, sin lugar a dudas, el enfoque más difícil y complejo de adoptar, ya que requiere grandes cantidades de datos, recursos capacitados y la potencia computacional adecuada. Esta opción solo debe considerarse en un escenario en el que una empresa tenga un caso de uso específico para un dominio y una gran cantidad de datos centrados en ese dominio.

## Evaluación de conocimientos

¿Cuál podría ser un buen enfoque para mejorar los resultados de finalización de LLM?

1. Prompt engineering con contexto
1. RAG
1. Modelo afinado 

A:3, si tienes el tiempo y los recursos y datos de alta calidad, el ajuste fino es la mejor opción para mantenerse actualizado. Sin embargo, si estás buscando mejoras y tienes limitaciones de tiempo, vale la pena considerar RAG en primer lugar.

## 🚀 Desafío

Investiga más sobre cómo puedes [utilizar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para tu negocio.

## Gran Trabajo, Continúa Tu Aprendizaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 3, donde veremos ¡cómo [construir con IA Generativa de manera Responsable](../../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!
