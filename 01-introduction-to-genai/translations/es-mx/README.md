# Introducción a IA Generativa y Modelos de Lenguaje Grande

[![Introducción a IA Generativa y Modelos de Lenguaje Grande](../../images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/vf_mZrn8ibc?WT.mc_id=academic-105485-koreyst)

*(Haz clic en la imagen de arriba para ver el video de esta lección)*

La IA Generativa es la inteligencia artificial capaz de generar texto, imágenes y otros tipos de contenido. Lo que la convierte en una tecnología fantástica es que democratiza la IA: cualquiera puede usarla con tan solo un prompt de texto, una oración escrita en un lenguaje natural. No es necesario que aprendas un lenguaje como Java o SQL para lograr algo que valga la pena, todo lo que necesitas es usar tu lenguaje, indicar lo que quieres y obtendrás una sugerencia a partir de un modelo de IA. Las aplicaciones y el impacto de esto son enormes: escribes o entiendes reportes, escribes aplicaciones y mucho más, todo en segundos.

En este plan de estudios, exploraremos cómo nuestra startup aprovecha la IA generativa para desbloquear nuevos escenarios en el mundo de la educación y cómo abordamos los inevitables desafíos asociados con las implicaciones sociales de su aplicación y las limitaciones tecnológicas.

## Introducción

Esta lección cubrirá:

* Introducción al escenario de negocio: nuestra idea de startup y su misión.
* IA Generativa y cómo aterrizamos en el panorama tecnológico actual.
* Funcionamiento interno de un modelo de lenguaje grande.
* Principales capacidades y casos de uso práctico de los Modelos de Lenguaje Grande.

## Metas de Aprendizaje

Después de completar esta lección, comprenderás:

* Qué es la IA generativa y cómo funcionan los Modelos de Lenguaje Grande.
* Cómo aprovechar los Modelos de Lenguaje Grande para diferentes casos de uso, centrándose en escenarios educativos

## Escenario: nuestra startup educativa

La Inteligencia Artificial (IA) Generativa representa el pináculo de la tecnología de IA, superando los límites de lo que antes se consideraba imposible. Los modelos de IA Generativa tienen varias capacidades y aplicaciones, pero en este plan de estudios exploraremos cómo está revolucionando la educación a través de una startup ficticia. Nos referiremos a esta startup como *nuestra startup*. Nuestra startup trabaja en el ámbito educativo con la ambiciosa misión de

> *mejorar la accesibilidad al aprendizaje a nivel global, garantizando un acceso equitativo a la educación y proporcionando experiencias de aprendizaje personalizadas a cada alumno, de acuerdo a sus necesidades*.

Nuestro equipo de startup es consciente de que no podremos lograr este objetivo sin aprovechar una de las herramientas más poderosas de los tiempos modernos: los Modelos de Lenguaje Grande (LLMs).

Se espera que la IA Generativa revolucione la forma en que aprendemos y enseñamos hoy en día, ya que los estudiantes tendrán a su disposición profesores virtuales las 24 horas del día que proporcionan grandes cantidades de información y ejemplos, y profesores capaces de aprovechar herramientas innovadoras para evaluar a sus estudiantes y dar retroalimentación.

![Cinco jóvenes estudiantes mirando un monitor - imagen de DALLE2](../../images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

Para comenzar, definamos algunos conceptos y terminología básicos que usaremos a lo largo del plan de estudios.

## ¿Cómo obtuvimos la IA generativa?

A pesar del extraordinario *hype* creado últimamente por el anuncio de los modelos de IA generativa, esta tecnología lleva décadas en desarrollo, y los primeros esfuerzos de investigación se remontan a los años 60. Ahora estamos en un punto en el que la IA tiene capacidades cognitivas humanas, como la conversación, tal como se muestra, por ejemplo, en [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), el cual también utiliza un modelo GPT para las conversaciones de búsqueda web de Bing.

Retrocediendo un poco, los primeros prototipos de IA consistían en chatbots mecanografiados que se basaban en una base de conocimientos extraída a partir de un grupo de expertos y se representaba en una computadora. Las respuestas en la base de conocimientos eran generadas por palabras clave que aparecían en el texto de entrada.
Sin embargo, pronto quedó claro que tal enfoque, que utilizaba chatbots mecanografiados, no escalaba bien.

### Un enfoque estadístico a la IA: Machine Learning

Un punto de inflexión llegó durante los años 90, con la aplicación de un enfoque estadístico al análisis de texto. Esto llevó al desarrollo de nuevos algoritmos - conocidos con el nombre de machine learning - capaces de aprender patrones a partir de datos sin estar programados de manera explícita. Este enfoque permite que una máquina simule la comprensión del lenguaje humano: un modelo estadístico es entrenado en pares de texto y etiqueta, permitiendo al modelo clasificar texto de entrada desconocido con una etiqueta predefinida que representa la intención del mensaje.

### Redes neuronales y asistentes virtuales modernos

En tiempos más recientes, la evolución tecnológica del hardware, capaz de manejar mayores cantidades de datos y cálculos más complejos, impulsó la investigación en los campos de la IA, lo que llevó al desarrollo de algoritmos avanzados de machine learning, llamados redes neuronales o algoritmos de deep learning.

Las redes neuronales (y en particular las Redes Neuronales Recurrentes (RNN)) mejoraron significativamente el procesamiento del lenguaje natural, permitiendo la representación del significado del texto de una manera más significativa, valorando el contexto de una palabra en una oración.

Esta es la tecnología que impulsó a los asistentes virtuales nacidos en la primera década del nuevo siglo, muy hábiles para interpretar el lenguaje humano, identificar una necesidad y realizar una acción para satisfacerla - como responder con un guión predefinido o consumir un servicio de terceros.

### El presente, IA Generativa

Así es como llegamos hoy a la IA Generativa, que puede verse como un subconjunto de deep learning.

![IA, ML, DL e IA Generativa](../../images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

Después de décadas de investigación en el campo de la IA, una nueva arquitectura de modelo - llamada *Transformer* - superó los límites de las RNNs, siendo capaz de obtener secuencias de texto mucho más largas como entrada. Los transformadores están basados en el mecanismo de atención, permitiendo al modelo dar diferentes pesos a las entradas que recibe, ‘prestando más atención’ donde se concentra la información más relevante, independientemente de su orden en la secuencia del texto.

La mayoría de los modelos recientes de IA generativa, también conocidos como Modelos de Lenguaje Grande (LLMs) - debido a que funcionan con entradas y salidas textuales - están de hecho basados en esta arquitectura. Lo interesante de estos modelos - entrenados con una enorme cantidad de datos no etiquetados de diversas fuentes como libros, artículos y sitios web - es que pueden ser adaptados a una amplia variedad de tareas y generar texto gramaticalmente correcto con una apariencia de creatividad. Por lo tanto, no sólo mejoraron increíblemente la capacidad de una máquina para ‘entender’ un texto de entrada, sino que también permitieron su capacidad para generar una respuesta original en lenguaje humano.

## ¿Cómo funcionan los modelos de lenguaje grande?

En el próximo capítulo vamos a explorar diferentes tipos de modelos de IA Generativa, pero por ahora demos un vistazo a cómo funcionan los modelos de lenguaje grande, centrándonos en los modelos OpenAI GPT (Transformador Generativo Pre-entrenado).

* **Tokenizador, texto a números**: los Modelos de Lenguaje Grande reciben un texto como entrada y generan un texto como salida. Sin embargo, al ser modelos estadísticos, funcionan mucho mejor con números que con secuencias de texto. Es por eso que cada entrada al modelo es procesada por un tokenizador, antes de ser utilizada por el modelo central. Un token es un fragmento de texto - que consta de un número variable de caracteres, por lo que la tarea principal del tokenizador es dividir la entrada en un arreglo de tokens. Luego, cada token se asigna con un índice de token, el cual es la codificación entera del fragmento de texto original.

![Ejemplo de tokenización](../../images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

* **Predicción de tokens de salida**: Dados n tokens como entrada (con un máximo de n que varía de un modelo a otro), el modelo puede predecir un token como salida. Luego, este token es incorporado a la entrada de la siguiente iteración, en un patrón de ventana en expansión, lo que permite una mejor experiencia de usuario al obtener una (o múltiples) oraciones como respuesta. Esto explica por qué, si alguna vez jugaste con ChatGPT, habrás notado que a veces parece que se detiene en medio de una oración.

* **Proceso de selección, distribución de probabilidad**: el token de salida es elegido por el modelo de acuerdo a su probabilidad de ocurrir después de la secuencia de texto actual. Esto se debe a que el modelo predice una distribución de probabilidad sobre todos los ‘siguientes tokens’ posibles, calculada en función de su entrenamiento. Sin embargo, no siempre el token con la probabilidad más alta es seleccionado de la distribución resultante. Un grado de aleatoriedad es añadido a esta elección, en una forma que el modelo actúa de forma no determinista - no obtenemos exactamente la misma salida para la misma entrada. Este grado de aleatoriedad se agrega para simular el proceso de pensamiento creativo y se puede ajustar utilizando un parámetro del modelo llamado temperatura.

## ¿Cómo puede nuestra startup aprovechar los Modelos de Lenguajes Grande?

Ahora que tenemos un mejor entendimiento del funcionamiento interno de un modelo de lenguaje grande, veamos algunos ejemplos prácticos de las tareas más comunes que pueden realizar bastante bien, con la vista puesta en nuestro escenario empresarial.
Dijimos que la principal capacidad de un Modelo de Lenguaje Grande es *generar un texto desde cero, a partir de una entrada textual, escrita en lenguaje natural*.

Pero ¿qué tipo de entrada y salida textual?
La entrada de un modelo de lenguaje grande se conoce como 'prompt', mientras que la salida se conoce como resultado o 'completion', término que se refiere al mecanismo del modelo de generar el siguiente token para completar la entrada actual. Vamos a profundizar en qué es un prompt y cómo diseñarlo para aprovechar al máximo nuestro modelo. Pero por ahora, digamos que un prompt puede incluir:

* Una **instrucción** que especifica el tipo de resultado que esperamos del modelo. Esta instrucción en ocasiones puede incluir algunos ejemplos o algunos datos adicionales.

    1. Resumen de un artículo, libro, reseñas de productos y más, junto con la extracción de conocimientos a partir de datos no estructurados.
    
    ![Ejemplo de resumen](../../images/summarization-example.png?WT.mc_id=academic-105485-koreyst)

    <br>
    
    2. Ideación creativa y diseño de un artículo, un ensayo, una tarea o más. 
    
    ![Ejemplo de escritura creativa](../../images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

    <br>
    
* Una **pregunta**, formulada en forma de conversación con un agente.
  
![Ejemplo de conversación](../../images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

<br>

* Un fragmento de **texto para completar**, el cual implícitamente es una solicitud de ayuda para escribir.
   
![Ejemplo de finalización de texto](../../images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

<br>

* Un fragmento de **código** junto con la solicitud de explicarlo y documentarlo, o un comentario solicitando generar un fragmento de código que realice una tarea específica.

![Ejemplo de codificación](../../images/coding-example.png?WT.mc_id=academic-105485-koreyst)

<br>

Los ejemplos anteriores son bastante simples y no pretenden ser una demostración exhaustiva de las capacidades de los Modelos de Lenguaje Grande. Solo quieren mostrar el potencial del uso de la IA generativa, en particular pero no limitado al contexto educativo.

Además, el resultado de un modelo de IA generativa no es perfecto y a veces la creatividad del modelo puede ir en su contra, dando como resultado un resultado que es una combinación de palabras que el usuario humano puede interpretar como una mistificación de la realidad, o puede ser ofensivo. La IA Generativa no es inteligente - al menos en la definición más amplia de inteligencia, que incluye el razonamiento crítico y creativo o la inteligencia emocional; es no determinista y no es confiable, ya que las invenciones, tales como referencias, contenidos y declaraciones erróneas, podrían ser combinadas con información correcta y presentadas de manera persuasiva y segura. En las siguientes lecciones, estaremos abordando todas estas limitaciones y veremos qué podemos hacer para mitigarlas.

## Tarea

Tu tarea es leer más sobre [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) 
e intentar identificar un área donde agregarías IA generativa hoy que no la tiene. ¿En qué se diferenciaría el impacto de hacerlo a la "manera antigua", puedes hacer algo que antes no podías o eres más rápido? Escribe un resumen de 300 palabras sobre cómo sería la startup de IA de tus sueños e incluye encabezados como "Problema", "Cómo usaría la IA", "Impacto" y, opcionalmente, un plan de negocios.

Si realizaste esta tarea, puede que incluso estés listo para postularte a la incubadora de Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), ofrecemos créditos tanto para Azure como para OpenAI, mentoría y mucho más, ¡compruébalo!

## Verificación de conocimientos

¿Qué es cierto acerca de los modelos de lenguaje grande?

1. Obtienes exactamente la misma respuesta cada vez.
2. Hace las cosas perfectamente, excelente para sumar números, producir código funcional, etc.
3. La respuesta puede variar a pesar de utilizar el mismo prompt. También es genial para darte un primer borrador de algo, ya sea texto o código. Pero necesitas mejorar los resultados.

R: 3, un LLM es no determinista, la respuesta varía, sin embargo, puedes controlar su variación mediante un ajuste de temperatura. Tampoco deberías esperar que haga las cosas a la perfección, está aquí para hacer el trabajo pesado por ti, lo que a menudo significa que tendrás un buen primer intento en algo que necesitas mejorar gradualmente.

## ¡Buen trabajo! Continúa el viaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 2, donde veremos ¡cómo [explorar y comparar diferentes tipos de LLM](../../../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!
