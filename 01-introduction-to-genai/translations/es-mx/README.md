# 📚 Introducción a la Inteligencia Artificial Generativa y a los Modelos de Lenguaje Grandes

[![Introducción a la Inteligencia Artificial Generativa y a los Modelos de Lenguaje Grandes](../../images/01-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=36c6795a-e63c-46dd-8d69-df8bbe6e7bc9?WT.mc_id=academic-105485-koreyst)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

La Inteligencia Artificial Generativa es una forma de inteligencia artificial capaz de generar texto, imágenes y otros tipos de contenido. Lo que la hace una tecnología fantástica es que democratiza la IA; cualquiera puede utilizarla con tan solo una indicación de texto, una oración escrita en un lenguaje natural. No es necesario que aprendas un lenguaje como Java o SQL para lograr algo valioso; todo lo que necesitas es usar tu propio lenguaje, expresar lo que deseas, y obtendrás sugerencias de un modelo de IA. Las aplicaciones e impacto de esto son enormes: puedes redactar o entender informes, escribir aplicaciones y mucho más, todo en cuestión de segundos.

En este plan de estudios, exploraremos cómo nuestra startup aprovecha la inteligencia artificial generativa para desbloquear nuevos escenarios en el mundo de la educación, y cómo abordamos los inevitables desafíos asociados con las implicaciones sociales de su aplicación y las limitaciones tecnológicas.

## Introducción

Esta lección cubrirá:

- Introducción al escenario empresarial: nuestra idea y misión como startup.
- Inteligencia Artificial Generativa y cómo llegamos al panorama tecnológico actual.
- Funcionamiento interno de un modelo de lenguaje grande.
- Principales capacidades y casos de uso prácticos de los Modelos de Lenguaje Grandes.

## Objetivos de Aprendizaje

Después de completar esta lección, comprenderás:

- Qué es la inteligencia artificial generativa y cómo funcionan los Modelos de Lenguaje Grandes.
- Cómo puedes aprovechar los modelos de lenguaje grandes para diferentes casos de uso, con un enfoque en escenarios educativos.

## Escenario: nuestra startup educativa

La Inteligencia Artificial Generativa (IA) representa la cúspide de la tecnología de la IA, empujando los límites de lo que antes se consideraba imposible. Los modelos de IA generativa tienen varias capacidades y aplicaciones, pero en este plan de estudios exploraremos cómo está revolucionando la educación a través de una startup ficticia. Nos referiremos a esta startup como nuestra startup. Nuestra startup opera en el ámbito educativo con la ambiciosa declaración de misión de:

> _mejorar la accesibilidad en el aprendizaje a escala global, garantizando un acceso equitativo a la educación y proporcionando experiencias de aprendizaje personalizadas a cada estudiante, según sus necesidades._.

Nuestro equipo de startup es consciente de que no podremos alcanzar este objetivo sin aprovechar una de las herramientas más poderosas de los tiempos modernos: los Modelos de Lenguaje Grandes (LLMs).

Se espera que la Inteligencia Artificial Generativa revolucione la forma en que aprendemos y enseñamos hoy en día, con estudiantes teniendo a su disposición profesores virtuales las 24 horas del día que proporcionan grandes cantidades de información y ejemplos, y profesores capaces de aprovechar herramientas innovadoras para evaluar a sus estudiantes y brindar retroalimentación.

![Cinco jóvenes estudiantes mirando un monitor. - image by DALLE2](../../images/students-by-DALLE2.png?WT.mc_id=academic-105485-koreyst)

Para empezar, definamos algunos conceptos y terminología básicos que utilizaremos a lo largo del plan de estudios.

## ¿Cómo llegamos a la Inteligencia Artificial Generativa?

A pesar del extraordinario _hype_ creado recientemente por el anuncio de modelos de IA generativa, esta tecnología lleva décadas en desarrollo, con los primeros esfuerzos de investigación remontándose a los años 60. Ahora estamos en un punto en el que la IA tiene capacidades cognitivas humanas, como la conversación, como se muestra, por ejemplo [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), que también utiliza un modelo GPT para las conversaciones de búsqueda web en Bing.

Volviendo un poco atrás, los primeros prototipos de IA consistían en chatbots mecanografiados, que dependían de una base de conocimientos extraída de un grupo de expertos y representada en una computadora. Las respuestas en la base de conocimientos eran activadas por palabras clave que aparecían en el texto de entrada. Sin embargo, pronto quedó claro que este enfoque, utilizando chatbots mecanografiados, no escalaba bien.

### Enfoque estadístico para la Inteligencia Artificial: Aprendizaje Automático

Un punto de inflexión llegó durante los años 90, con la aplicación de un enfoque estadístico para el análisis de texto. Esto llevó al desarrollo de nuevos algoritmos, conocidos con el nombre de aprendizaje automático, capaces de aprender patrones a partir de datos sin ser programados explícitamente. Este enfoque permite que una máquina simule la comprensión del lenguaje humano: un modelo estadístico se entrena en pares de texto y etiquetas, lo que permite al modelo clasificar texto de entrada desconocido con una etiqueta predefinida que representa la intención del mensaje.

### Redes neuronales y asistentes virtuales modernos

En tiempos más recientes, la evolución tecnológica del hardware, capaz de manejar mayores cantidades de datos y cálculos más complejos, estimuló la investigación en los campos de la inteligencia artificial, llevando al desarrollo de algoritmos avanzados de aprendizaje automático, llamados redes neuronales o algoritmos de aprendizaje profundo.

Las redes neuronales (y en particular las Redes Neuronales Recurrentes - RNN) mejoraron significativamente el procesamiento del lenguaje natural, permitiendo la representación del significado del texto de una manera más significativa, valorando el contexto de una palabra en una oración.

Esta es la tecnología que impulsó a los asistentes virtuales nacidos en la primera década del nuevo siglo, muy competentes en interpretar el lenguaje humano, identificar una necesidad y realizar una acción para satisfacerla, como responder con un guion predefinido o consumir un servicio de terceros.

### En la actualidad, la Inteligencia Artificial Generativa

Así es como llegamos a la Inteligencia Artificial Generativa hoy en día, que se puede considerar como un subconjunto del aprendizaje profundo.

![AI, ML, DL y IA Generativa](../../images/AI-diagram.png?WT.mc_id=academic-105485-koreyst)

Después de décadas de investigación en el campo de la inteligencia artificial, una nueva arquitectura de modelo, - llamada _Transformer_ – superó los límites de las RNN, siendo capaz de manejar secuencias de texto mucho más largas como entrada. Los Transformers se basan en el mecanismo de atención, lo que permite al modelo asignar diferentes pesos a las entradas que recibe, ‘prestando más atención’ donde se concentra la información más relevante, independientemente de su orden en la secuencia de texto.

La mayoría de los modelos recientes de Inteligencia Artificial Generativa, también conocidos como Modelos de Lenguaje Grandes (LLMs, por sus siglas en inglés), ya que trabajan con entradas y salidas de texto, están basados de hecho en esta arquitectura. Lo interesante de estos modelos, entrenados con una gran cantidad de datos no etiquetados de diversas fuentes como libros, artículos y sitios web, es que pueden adaptarse a una amplia variedad de tareas y generar texto gramaticalmente correcto con un atisbo de creatividad. Por lo tanto, no solo mejoraron de manera increíble la capacidad de una máquina para 'entender' un texto de entrada, sino que también habilitaron su capacidad para generar una respuesta original en lenguaje humano.

## ¿Cómo funcionan los grandes modelos de lenguaje?

En el próximo capítulo exploraremos diferentes tipos de modelos de Inteligencia Artificial Generativa, pero por ahora echemos un vistazo a cómo funcionan los grandes modelos de lenguaje, con un enfoque en los modelos de OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizador, texto a números**: Los grandes modelos de lenguaje reciben un texto como entrada y generan un texto como salida. Sin embargo, al ser modelos estadísticos, funcionan mucho mejor con números que con secuencias de texto. Es por eso que cada entrada al modelo se procesa mediante un tokenizador antes de ser utilizada por el modelo central. Un token es un fragmento de texto, que consiste en un número variable de caracteres. La tarea principal del tokenizador es dividir la entrada en un conjunto de tokens. Luego, cada token se asigna con un índice de token, que es la codificación entera del fragmento de texto original.

![Ejemplo de tokenización](../../images/tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

- **Predicción de tokens de salida**: Dado un conjunto de n tokens como entrada (con un máximo n que varía de un modelo a otro), el modelo es capaz de predecir un token como salida. Este token se incorpora luego a la entrada de la siguiente iteración, en un patrón de ventana expansiva, lo que permite una mejor experiencia del usuario al obtener una (o varias) oraciones como respuesta. Esto explica por qué, si alguna vez has interactuado con ChatGPT, es posible que hayas notado que a veces parece detenerse en medio de una oración.

- **Proceso de selección, distribución de probabilidad**: El token de salida es elegido por el modelo de acuerdo con su probabilidad de ocurrir después de la secuencia de texto actual. Esto se debe a que el modelo predice una distribución de probabilidad sobre todos los posibles 'próximos tokens', calculados en base a su entrenamiento. Sin embargo, no siempre se elige el token con la probabilidad más alta de la distribución resultante. Se añade un grado de aleatoriedad a esta elección, de manera que el modelo actúa de manera no determinista; no obtenemos la misma salida exacta para la misma entrada. Este grado de aleatoriedad se agrega para simular el proceso de pensamiento creativo y se puede ajustar utilizando un parámetro del modelo llamado temperatura.

## ¿Cómo puede nuestra startup aprovechar los grandes modelos de lenguaje?

Ahora que tenemos una mejor comprensión del funcionamiento interno de un modelo de lenguaje grande, veamos algunos ejemplos prácticos de las tareas más comunes que pueden realizar bastante bien, con atención a nuestro escenario empresarial. Dijimos que la capacidad principal de un Modelo de Lenguaje Grande es _generar texto desde cero, a partir de una entrada textual escrita en lenguaje natural_.

¿Pero qué tipo de entrada y salida textual?
La entrada de un gran modelo de lenguaje se conoce como "prompt" (indicación), mientras que la salida se conoce como "completion" (completado), término que se refiere al mecanismo del modelo de generar el próximo token para completar la entrada actual. Vamos a profundizar en lo que es un "prompt" y cómo diseñarlo de manera que aprovechemos al máximo nuestro modelo. Pero por ahora, simplemente diremos que un "prompt" puede incluir:

- Una **instrucción** especificando el tipo de salida que esperamos del modelo. Esta instrucción a veces puede incluir algunos ejemplos o datos adicionales.

  1. Resumen de un artículo, libro, reseñas de productos y más, junto con la extracción de información clave a partir de datos no estructurados.

  ![Ejemplo de resumen](../../images/summarization-example.png?WT.mc_id=academic-105485-koreyst)

    <br>
    
    2. Ideación creativa y diseño de un artículo, un ensayo, una tarea u otros.
    
    ![Ejemplo de escritura creativa](../../images/creative-writing-example.png?WT.mc_id=academic-105485-koreyst)

    <br>


- Una **pregunta**, preguntado en forma de conversación con un agente.

![Ejemplo de conversación](../../images/conversation-example.png?WT.mc_id=academic-105485-koreyst)

<br>

- Un fragmento de **texto por completar**, lo cual implícitamente es una solicitud de ayuda en la escritura.

![Ejemplo de finalización de texto](../../images/text-completion-example.png?WT.mc_id=academic-105485-koreyst)

<br>

- Un trozo de **código** junto con la petición de explicarlo y documentarlo, o un comentario pidiendo generar un fragmento de código que realice una tarea específica.

![Ejemplo de código](../../images/coding-example.png?WT.mc_id=academic-105485-koreyst)

<br>

Los ejemplos anteriores son bastante simples y no pretenden ser una demostración exhaustiva de las capacidades de los modelos de lenguaje grandes. Solo quieren mostrar el potencial del uso de la IA generativa, en particular, pero no limitado al contexto educativo.

Además, el resultado de un modelo de IA generativa no es perfecto y, a veces, la creatividad del modelo puede ir en su contra, dando como respuesta un resultado que es una combinación de palabras que el usuario humano puede interpretar como una mistificación de la realidad, o puede ser ofensivo. La IA generativa no es inteligente, al menos en la definición más amplia de inteligencia, que incluye el razonamiento crítico y creativo o la inteligencia emocional; no es determinista y no es confiable, ya que las mentiras, como referencias, contenidos y declaraciones erróneas, pueden combinarse con información correcta y presentarse de manera persuasiva y segura. En las siguientes lecciones, abordaremos todas estas limitaciones y veremos qué podemos hacer para mitigarlas.

## Asignación

Tu tarea es investigar más sobre [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e intentar identificar un área donde agregarías inteligencia artificial generativa hoy en día que aún no la tenga. ¿Cómo sería diferente el impacto de hacerlo de la "manera antigua"? ¿Puedes hacer algo que no podrías hacer antes o eres más rápido? Escribe un resumen de 300 palabras sobre cómo sería tu ideal startup de inteligencia artificial e incluye los encabezados como "Problema", "¿Cómo usaría la IA?", "Impacto" y opcionalmente un plan de negocios.

Si realizas esta tarea, incluso podrías estar listo para postularte al programa de incubación de Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst) Ofrecemos créditos para Azure, OpenAI, mentoría y mucho más, échale un vistazo.!

## Verificación de conocimientos

¿Qué es cierto acerca de los grandes modelos de lenguaje (LLM's, Large Language Models en ingles)?

1. Obtienes la misma respuesta exacta cada vez.
2. Realiza tareas de manera perfecta, es excelente sumando números, produciendo código funcional, etc.
3. La respuesta puede variar a pesar de usar el mismo prompt. También es excelente para ofrecerte un primer borrador de algo, ya sea texto o código. Sin embargo, necesitas mejorar los resultados.

A: 3. Un LLM (Large Language Model) es no determinista, las respuestas varían, sin embargo, puedes controlar su variabilidad mediante un ajuste de temperatura. Tampoco debes esperar que haga las cosas de manera perfecta; está aquí para hacer el trabajo pesado por ti, lo que a menudo significa que obtienes un buen primer intento en algo que necesitas mejorar gradualmente.

## ¡Gran trabajo! ¡Continúa el viaje!

Después de completar esta lección, echa un vistazo a nuestra [Colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) Para seguir mejorando tu conocimiento en IA Generativa!

Dirígete a la Lección 2 donde veremos cómo [explorar y comparar diferentes tipos de LLM](../../../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!
