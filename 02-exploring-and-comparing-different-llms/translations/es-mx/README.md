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

### Incrustaciones (embeddings) versus Generación de Imágenes versus Generación de Texto y Código

Los LLMs también pueden ser categorizados por la salida que generan.

Los embeddings son un conjunto de modelos que pueden convertir texto en una forma numérica, llamada incrustación, que es una representación numérica del texto de entrada. Las incrustaciones facilitan que las máquinas comprendan las relaciones entre palabras u oraciones y pueden ser utilizadas como entradas por otros modelos, como modelos de clasificación o modelos de agrupación que tienen un mejor rendimiento con los datos numéricos. Los modelos de incrustación usualmente se utilizan para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la cual hay gran cantidad de datos, y luego los pesos del modelo (incrustaciones) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría es [OpenAI embeddings](https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Incrustación](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de imágenes son modelos que crean imágenes. Estos modelos suelen utilizarse para la edición de imágenes, la síntesis de imágenes y la traducción de imágenes. Los modelos de generación de imágenes con regularidad son entrenados en grandes conjuntos de datos de imágenes, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar nuevas imágenes o para editar imágenes existentes con técnicas de inpainting, super-resolución y colorización. Algunos ejemplos: [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [Stable Diffusion models](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de texto y código son modelos que generan texto o código. Estos modelos suelen utilizarse para resumir texto, traducir y responder preguntas. Los modelos de generación de texto suelen ser entrenados en grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden ser utilizados para generar texto o responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), en muchas ocasiones se entrenan en grandes conjuntos de datos de código, como GitHub, y pueden utilizarse para crear código o para corregir errores en código existente.

 ![Generación de texto y código](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Codificador-Decodificador versus Solo-Decodificador

Para hablar sobre los diferentes tipos de arquitecturas de LLMs, utilicemos una analogía.

Imagina que tu jefe te asignó la tarea de escribir un cuestionario para los estudiantes. Tienes dos colegas; uno se encarga de crear el contenido y el otro se encarga de revisarlo.

El creador de contenido es como un modelo Decodificador o Decoder, puede mirar el tema y ver lo que escribiste, y luego puede escribir un curso basado en eso. Son muy buenos escribiendo contenido atractivo e informativo, pero no son muy buenos entendiendo el tema y los objetivos de aprendizaje. Algunos ejemplos de modelos decodificadores son los modelos de la familia GPT, como GPT-3.

El que revisa es como un modelo Codificador o Encoder, observa el curso escrito y las respuestas, notando la relación entre ellos y comprendiendo el contexto, pero no es bueno generando contenido. Un ejemplo de modelo Codificador sería BERT.

Imagina que también podemos tener a alguien que pueda crear y revisar el cuestionario, esto sería un modelo Codificador-Decodificador. Algunos ejemplos como BART y T5.

### Servicio versus Modelo

Ahora, hablemos de la diferencia entre un servicio y un modelo. Un servicio es un producto ofrecido por un proveedor de servicios en la nube y suele ser una combinación de modelos, datos y otros componentes. Un modelo es el componente central de un servicio y a veces es un modelo base, como un LLM.

Los servicios suelen estar optimizados para su uso en producción y son más fáciles de utilizar que los modelos, a través de una interfaz gráfica de usuario. Sin embargo, los servicios no siempre están disponibles de forma gratuita y pueden requerir una suscripción o pago para su uso, a cambio de aprovechar la infraestructura y los recursos del propietario del servicio, optimizando gastos y escalando fácilmente. Un ejemplo de servicio es [Azure OpenAI service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), este servicio ofrece un plan de tarifas de pago por uso (pay-as-you-go) , lo que implica que los usuarios pagan en proporción a su utilización del servicio. Además, el servicio Azure OpenAI brinda seguridad de nivel empresarial y un marco de inteligencia artificial responsable, complementando las capacidades de los modelos.

Los modelos son simplemente la red neuronal, con sus parámetros, pesos y otros elementos. Permitir que las empresas los ejecuten localmente requeriría la compra de hardware, la construcción de una infraestructura para escalar y la adquisición de una licencia o el uso de un modelo de código abierto. Un modelo como LLaMA está disponible para su uso, pero requiere una potencia de computo significativa para ejecutarlo.

## Cómo probar e iterar con diferentes modelos para entender el rendimiento en Azure

Una vez que nuestro equipo haya explorado el panorama actual de los LLMs y se haya identificado algunos candidatos prometedores para sus escenarios, el siguiente paso implica poner a prueba estos modelos con sus propios datos y cargas de trabajo. Este proceso es iterativo y se basa en experimentos y mediciones.
La mayoría de los modelos que mencionamos en párrafos anteriores (modelos de OpenAI, modelos de código abierto como Llama2 y transformers de Hugging Face) están disponibles en el siguiente enlace. [Modelos Base](https://learn.microsoft.com/azure/machine-learning/concept-foundation-models?WT.mc_id=academic-105485-koreyst) catálogo en [Azure Machine Learning studio](https://ml.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure Machine Learning](https://azure.microsoft.com/products/machine-learning/?WT.mc_id=academic-105485-koreyst) es un Servicio en la Nube diseñado para científicos de datos e ingenieros de aprendizaje automático (ML) para gestionar todo el ciclo de vida del aprendizaje automático (entrenar, probar, implementar y gestionar MLOps) en una sola plataforma. El estudio de aprendizaje automático ofrece una interfaz gráfica de usuario para este servicio y permite al usuario:

- Encontrar el Modelo Base de interés en el catálogo, filtrando por tarea, licencia o nombre. También es posible importar nuevos modelos que aún no estén incluidos en el catálogo
- Revisar la tarjeta del modelo, que incluye una descripción detallada y ejemplos de código, y probarlo con el widget de Inferencia de Muestra, proporcionando un ejemplo de prompt para evaluar el resultado.

![Tarjeta del modelo](../../images/Llama1.png?WT.mc_id=academic-105485-koreyst)

- Evaluar el rendimiento del modelo utilizando métricas objetivas de evaluación en una carga de trabajo específica y un conjunto de datos específico proporcionado como entrada o input.

![Evaluación del modelo](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Ajustar finamente (fine-tune) el modelo con datos de entrenamiento personalizados para mejorar el rendimiento del modelo en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure Machine Learning.

![Ajuste fino del modelo](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Desplegar el modelo original preentrenado o la versión afinada (fine-tuned) en un endpoint remoto de inferencia en tiempo real o por lotes, para que las aplicaciones puedan utilizarlo.

![Despliegue del modelo.](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## Mejorar los resultados de los LLMs

Nuestro equipo de startup ha explorado diferentes tipos de LLMs y la Plataforma en la Nube (Azure Machine Learning) para comparar diferentes modelos, evaluar su desempeño con datos de prueba, y mejorarlos antes de desplegarlos en endpoints de inferencia.

Pero, ¿cuándo deberían considerar ajustar finamente (fine-tuning) un modelo en lugar de usar uno preentrenado? ¿Existen otras estrategias para mejorar el rendimiento del modelo en cargas de trabajo específicas?

Existen varios enfoques que una empresa puede utilizar para obtener los resultados que necesita de un LLM. Pueden seleccionar diferentes tipos de modelos con diferentes niveles de entrenamiento.

Desplegar un LLM en producción, con diferentes niveles de complejidad, costos y calidad. Aquí hay algunas estrategias diferentes:

- **Prompt engineering con contexto**. La idea es proporcionar un prompt con suficiente contexto para asegurarse de obtener las respuestas que uno necesita.

- **Generación aumentada con recuperación (Retrieval Augmented Generation, RAG)**. Por ejemplo, tus datos pueden existir en una base de datos o un endpoint web, y para garantizar que estos datos, o una parte de ellos, se incluyan al realizar el prompting y puedas obtener respuestas precisas, puedes recuperar los datos relevantes y agregarlos como parte del prompt del usuario.

- **Ajuste Fino de Modelo (Fine-tuned)**. En este caso, has entrenado el modelo con mayor detalle utilizando tus propios datos, lo que lo hace más preciso y capaz de responder a tus necesidades específicas, aunque puede tener costos asociados.

![Implementación de LLMs](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [Four Ways that Enterprises Deploy LLMs | Fiddler AI Blog](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Prompt Engineering con contexto

Los LLMs preentrenados funcionan muy bien en tareas de lenguaje natural generalizadas, incluso al llamarlos con un breve prompt, como una oración por completar o una pregunta, se lo conoce como "aprendizaje de cero disparos" (zero-shot learning).

No obstante, cuanto más detallado sea el planteamiento de la consulta por parte del usuario, incluyendo solicitudes precisas y ejemplos concretos, es decir, proporcionando contexto, más precisa y acorde a las expectativas del usuario será la respuesta. En este, hablamos de aprendizaje de “one-shot” si el prompt incluye solo un ejemplo y de “few shot learning” si se proporcionan varios ejemplos. Prompt engineering con contexto es el enfoque más eficaz desde el punto de vista económico para comenzar.

### Retrieval Augmented Generation (RAG)

Los LLMs tienen la limitación de que solo pueden utilizar los datos que se utilizaron durante su entrenamiento para generar una respuesta. Esto significa que no saben nada acerca de los hechos que ocurrieron después de su proceso de entrenamiento y no pueden acceder a información no pública (como datos de la empresa).
Esto se puede superar mediante RAG, una técnica que amplía el prompt con datos externos en forma de fragmentos de documentos, teniendo en cuenta los límites de longitud del prompt. Esto es respaldado por las herramientas de base de datos vectoriales (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) estas herramientas de base de datos vectoriales recuperan los fragmentos (chunks) útiles de diversas fuentes de datos predefinidas y los añaden al contexto del prompt.

Esta técnica es muy útil cuando una empresa no dispone de suficientes datos, tiempo o recursos para ajustar finamente (fine-tune) un LLM, pero aún desea mejorar el rendimiento en una carga de trabajo específica y reducir los riesgos de generar información falsa, es decir, la distorsión de la realidad o contenido perjudicial.

### Modelo afinado (Fine-tuned)

El ajuste fino es un proceso que utiliza el aprendizaje por transferencia para "adaptar" el modelo a una tarea o para resolver un problema específico. A diferencia del aprendizaje few-shot y RAG, esto resulta en la generación de un nuevo modelo con pesos y sesgos actualizados. Requiere un conjunto de ejemplos de entrenamiento que consisten en una única entrada (prompt) y su salida asociada (respuesta).

Este sería el enfoque preferido si:

- **Utilizando modelos ajustados finamente**. Una empresa preferiría utilizar modelos ajustados finamente menos capaces (como modelos de embedding) en lugar de modelos de alto rendimiento, lo que resultaría en una solución más rentable y rápida.

- **Teniendo en cuenta la latencia**. La latencia es importante para un caso de uso específico, por lo que no es posible utilizar prompts extensos o un número de ejemplos que no se ajuste al límite de longitud del prompt del modelo.

- **Mantenerse actualizado**. Una empresa cuenta con una gran cantidad de datos de alta calidad y etiquetas reales, así como los recursos necesarios para mantener actualizados estos datos con el tiempo.

### Modelo entrenado

Entrenar un LLM desde cero es, sin lugar a dudas, es el enfoque más difícil y complejo de adoptar, ya que requiere grandes cantidades de datos, recursos capacitados y la potencia computacional adecuada. Esta opción solo debe considerarse en un escenario en el que una empresa tenga un caso de uso específico para un dominio y una gran cantidad de datos centrados en ese dominio.

## Evaluación de conocimientos

¿Cuál podría ser un buen enfoque para mejorar los resultados finalización de LLM?

1. Prompt engineering con contexto
1. RAG
1. Modelo Fine-tuned 

A:3, si tienes el tiempo y los recursos, y cuentas con datos de alta calidad, el ajuste fino (fine-tuning) es la mejor opción para mantenerte actualizado. Sin embargo, si estás buscando mejoras y tienes limitaciones de tiempo, vale la pena considerar RAG en primer lugar.

## 🚀 Desafío

Investiga más sobre cómo puedes [utilizar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para tu negocio.

## Gran trabajo, continúa aprendiendo

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 3, donde veremos ¡cómo  [Usar IA Generativa de manera Responsable](../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!
