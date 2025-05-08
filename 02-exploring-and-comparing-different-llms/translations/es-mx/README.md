# Explorando y comparando diferentes LLM

[![Explorando y comparando diferentes LLM](../../images/02-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson2-gh?WT.mc_id=academic-105485-koreyst)

> _Haga click en la imagen de arriba para ver el video de esta lección_

En la lección anterior, vimos cómo la IA Generativa está cambiando el panorama tecnológico, cómo funcionan los Modelos de Lenguaje Largo (LLM) y cómo una empresa, como nuestra startup, puede aplicarlos a sus casos de uso y crecer. En este capítulo, buscamos comparar y contrastar diferentes tipos de Modelos de Lenguaje Largo (LLM) para comprender sus ventajas y desventajas.

El siguiente paso en la trayectoria de nuestra startup es explorar el panorama actual de los LLM y comprender cuáles son adecuados para nuestro caso de uso.

## Introducción

Esta lección cubrirá:

- Diferentes tipos de LLM en el panorama actual.
- Pruebas, iteraciones y comparación de diferentes modelos para su caso de uso en Azure.
- Cómo implementar un LLM.

## Objetivos de aprendizaje

Después de completar esta lección, podrá:

- Seleccionar el modelo adecuado para su caso de uso.
- Comprender cómo probar, iterar y mejorar el rendimiento de su modelo.
- Conocer cómo las empresas implementan los modelos.

## Comprender los diferentes tipos de LLM

Los LLM pueden tener múltiples categorizaciones según su arquitectura, datos de entrenamiento y caso de uso. Comprender estas diferencias ayudará a nuestra startup a seleccionar el modelo adecuado para cada escenario y a comprender cómo probar, iterar y mejorar el rendimiento.

Existen muchos tipos diferentes de modelos LLM; la elección del modelo depende de su uso previsto, sus datos, su presupuesto y otros factores.

Dependiendo de si desea utilizar los modelos para texto, audio, vídeo, generación de imágenes, etc., podría optar por un tipo de modelo diferente.

- **Reconocimiento de audio y voz**. Para este propósito, los modelos de tipo Whisper son una excelente opción, ya que son de propósito general y están orientados al reconocimiento de voz. Está entrenado con audio diverso y puede realizar reconocimiento de voz multilingüe. Obtenga más información sobre [modelos de typo Whisper aqui](https://platform.openai.com/docs/models/whisper?WT.mc_id=academic-105485-koreyst).

- **Generación de imágenes**. Para la generación de imágenes, DALL-E y Midjourney son dos opciones muy conocidas. Azure OpenAI ofrece DALL-E. [Más información sobre DALL-E aquí](https://platform.openai.com/docs/models/dall-e?WT.mc_id=academic-105485-koreyst) y también en el Capítulo 9 de este programa.

- **Generación de texto**. La mayoría de los modelos se entrenan en generación de texto y existen diversas opciones, desde GPT-3.5 hasta GPT-4. Tienen diferentes precios, siendo GPT-4 el más caro. Vale la pena consultar la [zona de juegos de Azure OpenAI](https://oai.azure.com/portal/playground?WT.mc_id=academic-105485-koreyst) para evaluar qué modelos se adaptan mejor a sus necesidades en términos de capacidad y costo.

- **Multimodalidad**. Si busca gestionar múltiples tipos de datos de entrada y salida, le recomendamos considerar modelos como [gpt-4 turbo con visión o gpt-4o](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#gpt-4-and-gpt-4-turbo-models?WT.mc_id=academic-105485-koreyst), las últimas versiones de los modelos de OpenAI, que combinan el procesamiento del lenguaje natural con la comprensión visual, lo que permite interacciones a través de interfaces multimodales.

Seleccionar un modelo implica obtener algunas capacidades básicas, pero esto podría no ser suficiente. A menudo, se tienen datos específicos de la empresa que, de alguna manera, es necesario comunicar al LLM. Existen diferentes opciones para abordar este tema; más información al respecto en las próximas secciones.

### Modelos Fundamentales versus LLMs

El término Modelo Fundamental fue [acuñado por investigadores de Stanford] (https://arxiv.org/abs/2108.07258?WT.mc_id=academic-105485-koreyst) y definido como un modelo de IA que sigue ciertos criterios, como:

- **Se entrenan mediante aprendizaje no supervisado o autosupervisado**, lo que significa que se entrenan con datos multimodales sin etiquetar y no requieren anotación ni etiquetado humano de los datos para su proceso de entrenamiento.
- **Son modelos muy grandes**, basados ​​en redes neuronales muy profundas entrenadas con miles de millones de parámetros.
- **Normalmente están pensados ​​para servir de base para otros modelos**, lo que significa que pueden utilizarse como punto de partida para la construcción de otros modelos, lo cual puede lograrse mediante ajustes finos.

![Modelos Fundamentales versus LLMs](../../images/FoundationModel.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [Guía Esencial de Modelos Fundamentales y Modelos de Lenguaje Grandes | por Babar M Bhatti | Medium
](https://thebabar.medium.com/essential-guide-to-foundation-models-and-large-language-models-27dab58f7404)

Para aclarar mejor esta distinción, tomemos ChatGPT como ejemplo. Para crear la primera versión de ChatGPT, se utilizó un modelo llamado GPT-3.5 como modelo fundamental. Esto significa que OpenAI utilizó datos específicos del chat para crear una versión optimizada de GPT-3.5, especializada en un buen rendimiento en escenarios conversacionales, como los chatbots.

![Modelo Fundamental](../../images/Multimodal.png?WT.mc_id=academic-105485-koreyst)

Fuente de la imagen: [2108.07258.pdf (arxiv.org)](https://arxiv.org/pdf/2108.07258.pdf?WT.mc_id=academic-105485-koreyst)

### Modelos de código abierto versus modelos propietarios

Otra forma de clasificar los LLM es si son de código abierto o propietarios.

Los modelos de código abierto son modelos disponibles para el público general y pueden ser utilizados por cualquier persona. Suelen ser puestos a disposición por la empresa que los creó o por la comunidad investigadora. Estos modelos pueden ser inspeccionados, modificados y personalizados para los diversos casos de uso de los LLM. Sin embargo, no siempre están optimizados para su uso en producción y pueden no ser tan eficientes como los modelos propietarios. Además, la financiación para los modelos de código abierto puede ser limitada y es posible que no se mantengan a largo plazo o que no se actualicen con las últimas investigaciones. Algunos ejemplos de modelos de código abierto populares son [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html?WT.mc_id=academic-105485-koreyst), [Bloom](https://huggingface.co/bigscience/bloom) y [LLaMA](https://llama.meta.com).

Los modelos propietarios son modelos propiedad de una empresa y no están disponibles públicamente. Estos modelos suelen estar optimizados para su uso en producción. Sin embargo, no se permite su inspección, modificación ni personalización para diferentes casos de uso. Además, no siempre son gratuitos y pueden requerir una suscripción o pago para su uso. Asimismo, los usuarios no tienen control sobre los datos utilizados para entrenar el modelo, por lo que deben confiar al propietario del modelo la responsabilidad de garantizar el compromiso con la privacidad de los datos y el uso responsable de la IA. Algunos ejemplos de modelos propietarios populares incluyen [modelos OpenAI](https://platform.openai.com/docs/models/overview?WT.mc_id=academic-105485-koreyst), [Google Bard](https://sapling.ai/llm/bard?WT.mc_id=academic-105485-koreyst) o [Claude 2](https://www.anthropic.com/index/claude-2?WT.mc_id=academic-105485-koreyst).

### Incrustaciones versus Generación de imágenes versus Generación de texto y código

Los LLM también se pueden clasificar por el resultado que generan.

Las incrustaciones son un conjunto de modelos que pueden convertir texto a una forma numérica, denominada incrustación, que es una representación numérica del texto de entrada. Las incrustaciones facilitan a las máquinas la comprensión de las relaciones entre palabras u oraciones y pueden ser utilizadas como entrada por otros modelos, como modelos de clasificación o modelos de agrupamiento, que ofrecen un mejor rendimiento con datos numéricos. Los modelos de incrustación se utilizan a menudo para el aprendizaje por transferencia, donde se construye un modelo para una tarea sustituta para la que existe una gran cantidad de datos, y luego las ponderaciones del modelo (incrustaciones) se reutilizan para otras tareas posteriores. Un ejemplo de esta categoría son las incrustaciones de OpenAI (https://platform.openai.com/docs/models/embeddings?WT.mc_id=academic-105485-koreyst).

![Incrustación](../../images/Embedding.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de imágenes son modelos que generan imágenes. Estos modelos se utilizan a menudo para la edición, síntesis y traducción de imágenes. Suelen entrenarse con grandes conjuntos de datos, como [LAION-5B](https://laion.ai/blog/laion-5b/?WT.mc_id=academic-105485-koreyst), y pueden utilizarse para generar nuevas imágenes o editar imágenes existentes con técnicas de relleno de imagen, superresolución y colorización. Algunos ejemplos son [DALL-E-3](https://openai.com/dall-e-3?WT.mc_id=academic-105485-koreyst) y [modelos de difusión estable](https://github.com/Stability-AI/StableDiffusion?WT.mc_id=academic-105485-koreyst).

![Generación de imágenes](../../images/Image.png?WT.mc_id=academic-105485-koreyst)

Los modelos de generación de texto y código generan texto o código. Estos modelos se utilizan a menudo para resumir textos, traducirlos y responder preguntas. Los modelos de generación de texto suelen entrenarse con grandes conjuntos de datos de texto, como [BookCorpus](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Zhu_Aligning_Books_and_ICCV_2015_paper.html?WT.mc_id=academic-105485-koreyst), y pueden utilizarse para generar texto nuevo o responder preguntas. Los modelos de generación de código, como [CodeParrot](https://huggingface.co/codeparrot?WT.mc_id=academic-105485-koreyst), suelen entrenarse con grandes conjuntos de datos de código, como GitHub, y pueden usarse para generar código nuevo o corregir errores en el código existente.

![Generación de texto y código](../../images/Text.png?WT.mc_id=academic-105485-koreyst)

### Codificador-Decodificador versus Solo Decodificador

Para hablar sobre los diferentes tipos de arquitecturas de los LLM, usemos una analogía.

Imagina que tu gerente te asigna la tarea de escribir un cuestionario para los estudiantes. Tienes dos colegas: uno supervisa la creación del contenido y el otro la revisión.

El creador de contenido es como un modelo solo decodificador: puede analizar el tema y ver lo que ya escribiste, y luego puede crear un curso basado en eso. Son muy buenos escribiendo contenido atractivo e informativo, pero no comprenden bien el tema ni los objetivos de aprendizaje. Algunos ejemplos de modelos decodificadores son los modelos de la familia GPT, como GPT-3.

El revisor es como un modelo solo de codificador: revisa el curso escrito y las respuestas, observa la relación entre ellos y comprende el contexto, pero no es bueno generando contenido. Un ejemplo de modelo solo de codificador sería BERT.

Imaginemos que también podemos contar con alguien que cree y revise el cuestionario. Este es un modelo de codificador-decodificador. Algunos ejemplos serían BART y T5.

### Servicio versus Modelo

Ahora, hablemos de la diferencia entre un servicio y un modelo. Un servicio es un producto ofrecido por un proveedor de servicios en la nube y suele ser una combinación de modelos, datos y otros componentes. Un modelo es el componente central de un servicio y suele ser un modelo base, como un LLM.

Los servicios suelen estar optimizados para producción y son más fáciles de usar que los modelos, gracias a una interfaz gráfica de usuario. Sin embargo, los servicios no siempre son gratuitos y pueden requerir una suscripción o pago para su uso, a cambio de aprovechar los equipos y recursos del propietario del servicio, optimizar los gastos y escalar fácilmente. Un ejemplo de servicio es [Azure OpenAI Service](https://learn.microsoft.com/azure/ai-services/openai/overview?WT.mc_id=academic-105485-koreyst), que ofrece un plan de pago por uso, lo que significa que los usuarios pagan proporcionalmente al uso del servicio. Además, Azure OpenAI Service ofrece seguridad de nivel empresarial y un marco de IA responsable, además de las capacidades de los modelos.

Los modelos son simplemente la red neuronal, con sus parámetros, ponderaciones y demás. Sin embargo, para que las empresas puedan operar localmente, se necesitaría comprar equipos, construir una estructura para escalar y adquirir una licencia o usar un modelo de código abierto. Un modelo como LLaMA está disponible, pero requiere potencia computacional para ejecutarlo.

## Cómo probar e iterar con diferentes modelos para comprender el rendimiento en Azure

Una vez que nuestro equipo haya explorado el panorama actual de los LLM e identificado algunos candidatos idóneos para sus escenarios, el siguiente paso es probarlos con sus datos y su carga de trabajo. Este es un proceso iterativo, realizado mediante experimentos y mediciones.
La mayoría de los modelos mencionados en párrafos anteriores (modelos de OpenAI, modelos de código abierto como Llama2 y transformadores Hugging Face) están disponibles en el [Catálogo de Modelos](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview?WT.mc_id=academic-105485-koreyst) de [Azure AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst).

[Azure AI Studio](https://learn.microsoft.com/azure/ai-studio/what-is-ai-studio?WT.mc_id=academic-105485-koreyst) es una plataforma en la nube diseñada para que los desarrolladores creen aplicaciones de IA generativa y gestionen todo el ciclo de vida del desarrollo, desde la experimentación hasta la evaluación, combinando todos los servicios de IA de Azure en un único centro con una práctica interfaz gráfica de usuario. El Catálogo de Modelos de Azure AI Studio permite al usuario:

- Encontrar el Modelo Fundacional de interés en el catálogo, ya sea propietario o de código abierto, filtrando por tarea, licencia o nombre. Para facilitar la búsqueda, los modelos se organizan en colecciones, como la colección Azure OpenAI, la colección Hugging Face y muchas más.

![Catálogo de modelos](../../images/AzureAIStudioModelCatalog.png?WT.mc_id=academic-105485-koreyst)

- Revise la tarjeta del modelo, que incluye una descripción detallada del uso previsto, los datos de entrenamiento, ejemplos de código y los resultados de la evaluación en la biblioteca de evaluaciones internas.

¡[Tarjeta del modelo](../../images/ModelCard.png?WT.mc_id=academic-105485-koreyst)

Compare los puntos de referencia de los modelos y conjuntos de datos disponibles en el sector para evaluar cuál se adapta mejor al escenario empresarial mediante el panel [Puntos de referencia del modelo](https://learn.microsoft.com/azure/ai-studio/how-to/model-benchmarks?WT.mc_id=academic-105485-koreyst).

![Puntos de referencia del modelo](../../images/ModelBenchmarks.png?WT.mc_id=academic-105485-koreyst)

- Ajuste el modelo con datos de entrenamiento personalizados para mejorar su rendimiento en una carga de trabajo específica, aprovechando las capacidades de experimentación y seguimiento de Azure AI Studio.

Ajuste del modelo

Implemente el modelo original preentrenado o la versión optimizada en un punto de conexión remoto de inferencia en tiempo real (computación administrada) o API sin servidor (pago por uso) para que las aplicaciones puedan utilizarlo.

![Implementación del modelo](../../images/ModelDeploy.png?WT.mc_id=academic-105485-koreyst)

> [!NOTA]
> No todos los modelos del catálogo están disponibles actualmente para ajustes o implementación con pago por uso. Consulte la ficha del modelo para obtener más información sobre sus capacidades y limitaciones.

## Mejorando los resultados del LLM

Con nuestro equipo de startups, hemos explorado diferentes tipos de LLM y una plataforma en la nube (Azure Machine Learning) que nos permite comparar diferentes modelos, evaluarlos con datos de prueba, mejorar el rendimiento e implementarlos en puntos finales de inferencia.

Pero cuándo deberían considerar ajustar un modelo en lugar de usar uno preentrenado? Existen otros enfoques para mejorar el rendimiento del modelo en cargas de trabajo específicas?

Existen varios enfoques que una empresa puede utilizar para obtener los resultados que necesita de un LLM. Se pueden seleccionar diferentes tipos de modelos con distintos grados de entrenamiento al implementar un LLM en producción, con distintos niveles de complejidad, coste y calidad. A continuación, se presentan algunos enfoques:

- **Ingeniería de indicaciones con contexto**. La idea es proporcionar suficiente contexto al solicitar para garantizar que se obtengan las respuestas necesarias.

- **Generación Aumentada de Recuperación (RAG)**. Sus datos podrían estar en una base de datos o un punto final web, por ejemplo. Para garantizar que estos datos, o un subconjunto de ellos, se incluyan al momento de la solicitud, puede obtener los datos relevantes e integrarlos en la solicitud del usuario.

- **Modelo optimizado**. En este caso, entrenó el modelo con sus propios datos, lo que lo hizo más preciso y adaptable a sus necesidades, aunque podría resultar costoso.

¡Implementación de LLM!

Fuente de la imagen: [Cuatro maneras en que las empresas implementan LLM | Blog de Fiddler AI](https://www.fiddler.ai/blog/four-ways-that-enterprises-deploy-llms?WT.mc_id=academic-105485-koreyst)

### Ingeniería de Propuestas con Contexto

Los LLM preentrenados funcionan muy bien en tareas de lenguaje natural generalizadas, incluso al solicitarles una proposición breve, como una oración para completar o una pregunta: el llamado aprendizaje "de disparo cero".

Sin embargo, cuanto más pueda el usuario estructurar su consulta con una solicitud detallada y ejemplos (el contexto), más precisa y cercana a sus expectativas será la respuesta. En este caso, hablamos de aprendizaje "de disparo único" si la proposición incluye solo un ejemplo y de "aprendizaje de disparos múltiples" si incluye varios. La ingeniería de propuestas con contexto es el enfoque más rentable para comenzar.

### Generación Aumentada de Recuperación (RAG)

Los LLM tienen la limitación de que solo pueden usar los datos utilizados durante su entrenamiento para generar una respuesta. Esto significa que desconocen los hechos ocurridos después del proceso de entrenamiento y no pueden acceder a información no pública (como datos de la empresa).
Esto se puede solucionar mediante RAG, una técnica que complementa la solicitud con datos externos en forma de fragmentos de documentos, teniendo en cuenta los límites de longitud de la solicitud. Esto es posible gracias a herramientas de bases de datos vectoriales (como [Azure Vector Search](https://learn.microsoft.com/azure/search/vector-search-overview?WT.mc_id=academic-105485-koreyst)), que recuperan los fragmentos útiles de diversas fuentes de datos predefinidas y los añaden al contexto de la solicitud.

Esta técnica es muy útil cuando una empresa no dispone de suficientes datos, tiempo ni recursos para perfeccionar un LLM, pero aun así desea mejorar el rendimiento en una carga de trabajo específica y reducir el riesgo de falsificaciones, es decir, la tergiversación de la realidad o el contenido dañino.

### Modelo perfeccionado

El ajuste fino es un proceso que aprovecha el aprendizaje por transferencia para adaptar el modelo a una tarea posterior o para resolver un problema específico. A diferencia del aprendizaje de pocos disparos y el RAG, genera un nuevo modelo con ponderaciones y sesgos actualizados. Requiere un conjunto de ejemplos de entrenamiento que consta de una única entrada (la indicación) y su salida asociada (la finalización).
Este sería el enfoque preferido si:

- **Uso de modelos ajustados**. Una empresa prefiere utilizar modelos ajustados con menor capacidad (como modelos de incrustación) en lugar de modelos de alto rendimiento, lo que resulta en una solución más rentable y rápida.

- **Consideración de la latencia**. La latencia es importante para un caso de uso específico, por lo que no es posible utilizar indicaciones muy largas o si el número de ejemplos que se deben aprender del modelo no se ajusta al límite de longitud de la indicación.

- **Mantenerse actualizado**. Una empresa cuenta con una gran cantidad de datos de alta calidad y etiquetas de datos reales, así como con los recursos necesarios para mantener estos datos actualizados a lo largo del tiempo.

### Modelo entrenado

Formar un LLM desde cero es, sin duda, el enfoque más difícil y complejo de adoptar, ya que requiere cantidades masivas de datos, recursos especializados y la capacidad computacional adecuada. Esta opción solo debe considerarse en un escenario donde una empresa tenga un caso de uso específico del dominio y una gran cantidad de datos centrados en el mismo.

## Comprobación de conocimientos

Cuál podría ser un buen enfoque para mejorar los resultados de la finalización del LLM?

1. Ingeniería rápida con contexto
1. RAG
1. Modelo optimizado

R:3, Si dispone del tiempo, los recursos y datos de alta calidad, optimizar es la mejor opción para mantenerse al día. Sin embargo, si busca mejorar y no dispone de tiempo, vale la pena considerar primero RAG.

## 🚀 Desafío

Lea más sobre cómo puede [usar RAG](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview?WT.mc_id=academic-105485-koreyst) para su negocio.

## ¡Buen trabajo! ¡Continúa aprendiendo!

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA generativa.

Dirígete a la Lección 3, donde veremos cómo [construir con IA generativa de forma responsable](../../../03-using-generative-ai-responsibly/README.md?WT.mc_id=academic-105485-koreyst).