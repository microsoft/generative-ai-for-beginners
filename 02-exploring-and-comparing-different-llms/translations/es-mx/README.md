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

![Modelo Fundacional](../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

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

![Modelo Evaluation](../../images/Llama2.png?WT.mc_id=academic-105485-koreyst)

- Ajustar el modelo con datos de entrenamiento personalizados para mejorar el rendimiento del modelo en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure Machine Learning.

![Modelo Fine-tuning](../../images/Llama3.png?WT.mc_id=academic-105485-koreyst)

- Despliega el modelo pre-entrenado original o la versión ajustada a un punto final remoto de inferencia en tiempo real o por lotes, para permitir que las aplicaciones lo consuman.

![Modelo Deployment](../../images/Llama4.png?WT.mc_id=academic-105485-koreyst)

## Mejorando los resultados de LLM

Hemos explorado con nuestro equipo de inicio diferentes tipos de LLMs y una plataforma en la nube (Azure Machine Learning) que nos permite comparar diferentes modelos, evaluarlos con datos de prueba, mejorar el rendimiento y desplegarlos en puntos finales de inferencia.

Pero ¿Cuándo deberían considerar ajustar finamente un modelo en lugar de usar uno preentrenado? ¿Existen otros enfoques para mejorar el rendimiento del modelo en cargas de trabajo específicas?

Hay varios enfoques que una empresa puede usar para obtener los resultados que necesita de un LLM; puede seleccionar diferentes tipos de modelos con diferentes grados de entrenamiento.

desplegar un LLM en producción, con diferentes niveles de complejidad, coste y calidad. Aquí hay algunos enfoques diferentes:

- **Prompt engineering con texto**. La idea es proporcionar suficiente contexto al momento de formular la indicación para garantizar que obtengas las respuestas que necesitas.
  
- **Generación Aumentada por Recuperación (RAG)**. Sus datos podrían existir en una base de datos o en un punto final web, por ejemplo. Para asegurarse de que estos datos, o un subconjunto de los mismos, estén incluidos al momento de la indicación, puede recuperar los datos relevantes y hacer que formen parte de la indicación del usuario.

- **Modelo Fine-tuned**. Aquí, entrenaste el modelo aún más con tus propios datos, lo que hace que el modelo sea más preciso y receptivo a tus necesidades, pero podría resultar costoso.

![Despliegue de LLMs](../../images/Deploy.png?WT.mc_id=academic-105485-koreyst)

Img source: [Cuatro formas en que las empresas despliegan LLMs | Blog de Fiddler AI](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Ingeniería de Indicaciones con Contexto (Prompt Engineering)

Los LLM preentrenados funcionan muy bien en tareas generales del lenguaje natural, incluso al llamarlos con una indicación corta, como una oración por completar o una pregunta, lo que se conoce como aprendizaje "zero-shot"

Sin embargo, cuanto más el usuario pueda enmarcar su consulta con una solicitud detallada y ejemplos, es decir, el contexto, más precisa y cercana a las expectativas del usuario será la respuesta. En este caso, hablamos de "aprendizaje de un disparo" si la indicación incluye solo un ejemplo y "aprendizaje de unos pocos disparos" si incluye varios ejemplos. La ingeniería de indicaciones con contexto es el enfoque más rentable para comenzar.

### Generación Aumentada por Recuperación (RAG)

Los LLM tienen la limitación de que solo pueden utilizar los datos que se han utilizado durante su entrenamiento para generar una respuesta. Esto significa que no saben nada sobre los hechos que ocurrieron después de su proceso de entrenamiento y no pueden acceder a información no pública (como datos de la empresa).

Esto se puede superar a través de RAG, una técnica que aumenta la indicación con datos externos en forma de fragmentos de documentos, considerando los límites de longitud de la indicación. Esto es compatible con las herramientas de base de datos vectoriales. (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)) que recuperan los fragmentos útiles de diversas fuentes de datos predefinidas y los agregan al contexto de la indicación.

Esta técnica es muy útil cuando una empresa no tiene suficientes datos, tiempo o recursos para ajustar finamente un LLM, pero aún desea mejorar el rendimiento en una carga de trabajo específica y reducir los riesgos de fabricaciones, es decir, la mistificación de la realidad o contenido perjudicial.

### Modelo de ajuste fino (Fine-tuned)

El ajuste fino es un proceso que aprovecha el aprendizaje por transferencia para "adaptar" el modelo a una tarea descendente o para resolver un problema específico. A diferencia del aprendizaje de unos pocos disparos y de RAG, resulta en la generación de un nuevo modelo con pesos y sesgos actualizados. Requiere un conjunto de ejemplos de entrenamiento que consisten en una entrada única (la indicación) y su salida asociada (la completación). Este sería el enfoque preferido si:

- **Usando modelos ajustados finamente**. Una empresa preferiría utilizar modelos ajustados finamente menos capaces (como modelos de incrustación) en lugar de modelos de alto rendimiento, lo que resulta en una solución más económica y rápida.
  
- **Considerando la latencia**. La latencia es importante para un caso de uso específico, por lo que no es posible utilizar indicaciones muy largas o el número de ejemplos que deben ser aprendidos por el modelo no se ajusta al límite de longitud de la indicación.

- **Mantenerse actualizado**. Una empresa cuenta con una gran cantidad de datos de alta calidad y etiquetas de verdad básica, así como los recursos necesarios para mantener estos datos actualizados a lo largo del tiempo.
  
### Modelo entrenado

Entrenar un LLM desde cero es, sin duda, el enfoque más difícil y complejo de adoptar, requiriendo cantidades masivas de datos, recursos capacitados y la potencia informática adecuada. Esta opción solo debería considerarse en un escenario donde una empresa tenga un caso de uso específico del dominio y una gran cantidad de datos centrados en ese dominio.

## Verificación de conocimientos

¿Cuál podría ser un buen enfoque para mejorar los resultados de finalización del LLM?

1. Ingeniería de indicaciones con contexto.
1. RAG (Generación Aumentada por Recuperación).
1. Modelo ajustado finamente.

R:3, si tiene el tiempo, los recursos y los datos de alta calidad, realizar ajustes es la mejor opción para mantenerse actualizado. Sin embargo, si buscas mejorar las cosas y te falta tiempo, vale la pena considerar RAG primero.

## 🚀 Desafío

Lea más sobre cómo puede [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para su negocio.

## Gran trabajo, continúa aprendiendo

Después de completar esta lección, consulte nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos de IA generativa!

Dirígete a la Lección 3, donde veremos cómo [construir con IA generativa de manera responsable](../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst)!
