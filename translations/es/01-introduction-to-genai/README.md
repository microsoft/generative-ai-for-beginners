# Introducción a la IA Generativa y los Modelos de Lenguaje a Gran Escala

[![Introducción a la IA Generativa y los Modelos de Lenguaje a Gran Escala](../../../translated_images/01-lesson-banner.png?WT.e847a56bbd30dfd9341d21c4e957c3bcd9de94d06aa5bc91692a69cb1af2c994.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson-1-gh?WT.mc_id=academic-105485-koreyst)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

La IA generativa es una inteligencia artificial capaz de generar texto, imágenes y otros tipos de contenido. Lo que la convierte en una tecnología fantástica es que democratiza la IA, cualquiera puede usarla con tan solo un mensaje de texto, una frase escrita en lenguaje natural. No es necesario aprender un lenguaje como Java o SQL para lograr algo valioso, solo necesitas usar tu lenguaje, expresar lo que deseas y obtendrás una sugerencia de un modelo de IA. Las aplicaciones e impactos de esto son enormes, puedes redactar o entender informes, escribir aplicaciones y mucho más, todo en cuestión de segundos.

En este currículo, exploraremos cómo nuestra startup aprovecha la IA generativa para desbloquear nuevos escenarios en el mundo de la educación y cómo abordamos los inevitables desafíos asociados con las implicaciones sociales de su aplicación y las limitaciones tecnológicas.

## Introducción

Esta lección cubrirá:

- Introducción al escenario empresarial: nuestra idea y misión de startup.
- IA generativa y cómo llegamos al panorama tecnológico actual.
- Funcionamiento interno de un modelo de lenguaje a gran escala.
- Principales capacidades y casos de uso práctico de los Modelos de Lenguaje a Gran Escala.

## Objetivos de Aprendizaje

Después de completar esta lección, entenderás:

- Qué es la IA generativa y cómo funcionan los Modelos de Lenguaje a Gran Escala.
- Cómo puedes aprovechar los modelos de lenguaje a gran escala para diferentes casos de uso, con un enfoque en escenarios educativos.

## Escenario: nuestra startup educativa

La Inteligencia Artificial Generativa (IA) representa la cúspide de la tecnología de IA, empujando los límites de lo que una vez se pensó imposible. Los modelos de IA generativa tienen varias capacidades y aplicaciones, pero para este currículo exploraremos cómo está revolucionando la educación a través de una startup ficticia. Nos referiremos a esta startup como _nuestra startup_. Nuestra startup trabaja en el ámbito educativo con la ambiciosa misión de

> _mejorar la accesibilidad en el aprendizaje, a escala global, asegurando el acceso equitativo a la educación y proporcionando experiencias de aprendizaje personalizadas a cada estudiante, según sus necesidades_.

Nuestro equipo de startup es consciente de que no podremos lograr este objetivo sin aprovechar una de las herramientas más poderosas de los tiempos modernos: los Modelos de Lenguaje a Gran Escala (LLMs).

Se espera que la IA generativa revolucione la forma en que aprendemos y enseñamos hoy en día, con estudiantes que tienen a su disposición maestros virtuales las 24 horas del día que proporcionan grandes cantidades de información y ejemplos, y maestros que pueden aprovechar herramientas innovadoras para evaluar a sus estudiantes y dar retroalimentación.

![Cinco estudiantes jóvenes mirando un monitor - imagen de DALLE2](../../../translated_images/students-by-DALLE2.png?WT.540d623be2689660f18d0c126177502c651e2269597164cc09b60d7d90b830cf.es.mc_id=academic-105485-koreyst)

Para empezar, definamos algunos conceptos básicos y terminología que usaremos a lo largo del currículo.

## ¿Cómo obtuvimos la IA Generativa?

A pesar del extraordinario _hype_ creado últimamente por el anuncio de modelos de IA generativa, esta tecnología lleva décadas en desarrollo, con los primeros esfuerzos de investigación que datan de los años 60. Ahora estamos en un punto en el que la IA tiene capacidades cognitivas humanas, como la conversación, como lo demuestran, por ejemplo, [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), que también utiliza un modelo GPT para las conversaciones de búsqueda en la web de Bing.

Retrocediendo un poco, los primeros prototipos de IA consistían en chatbots escritos a máquina, que dependían de una base de conocimientos extraída de un grupo de expertos y representada en una computadora. Las respuestas en la base de conocimientos se activaban por palabras clave que aparecían en el texto de entrada.
Sin embargo, pronto quedó claro que tal enfoque, usando chatbots escritos a máquina, no escalaba bien.

### Un enfoque estadístico para la IA: Aprendizaje Automático

Un punto de inflexión llegó durante los años 90, con la aplicación de un enfoque estadístico al análisis de texto. Esto llevó al desarrollo de nuevos algoritmos, conocidos con el nombre de aprendizaje automático, capaces de aprender patrones a partir de datos, sin ser programados explícitamente. Este enfoque permite a una máquina simular la comprensión del lenguaje humano: un modelo estadístico se entrena en emparejamientos de texto y etiquetas, lo que permite al modelo clasificar texto de entrada desconocido con una etiqueta predefinida que representa la intención del mensaje.

### Redes neuronales y asistentes virtuales modernos

En tiempos más recientes, la evolución tecnológica del hardware, capaz de manejar mayores cantidades de datos y cálculos más complejos, fomentó la investigación en los campos de la IA, llevando al desarrollo de algoritmos avanzados de aprendizaje automático, llamados redes neuronales o algoritmos de aprendizaje profundo.

Las redes neuronales (y en particular las Redes Neuronales Recurrentes – RNNs) mejoraron significativamente el procesamiento del lenguaje natural, permitiendo la representación del significado del texto de una manera más significativa, valorando el contexto de una palabra en una oración.

Esta es la tecnología que impulsó a los asistentes virtuales nacidos en la primera década del nuevo siglo, muy competentes en interpretar el lenguaje humano, identificar una necesidad y realizar una acción para satisfacerla, como responder con un guion predefinido o consumir un servicio de terceros.

### Hoy en día, IA Generativa

Así es como llegamos a la IA Generativa hoy, que puede verse como un subconjunto del aprendizaje profundo.

![IA, ML, DL y IA Generativa](../../../translated_images/AI-diagram.png?WT.e126d57e1a443697cd851d5d04d66753225b4d910f4aff65f9f28215b528471a.es.mc_id=academic-105485-koreyst)

Después de décadas de investigación en el campo de la IA, una nueva arquitectura de modelos, llamada _Transformer_, superó los límites de las RNNs, siendo capaz de procesar secuencias de texto mucho más largas como entrada. Los Transformers se basan en el mecanismo de atención, que permite al modelo dar diferentes pesos a las entradas que recibe, 'prestando más atención' donde se concentra la información más relevante, independientemente de su orden en la secuencia de texto.

La mayoría de los modelos recientes de IA generativa, también conocidos como Modelos de Lenguaje a Gran Escala (LLMs), ya que trabajan con entradas y salidas textuales, están de hecho basados en esta arquitectura. Lo interesante de estos modelos, entrenados en una enorme cantidad de datos no etiquetados de diversas fuentes como libros, artículos y sitios web, es que pueden adaptarse a una amplia variedad de tareas y generar texto gramaticalmente correcto con una apariencia de creatividad. Así que, no solo mejoraron increíblemente la capacidad de una máquina para 'entender' un texto de entrada, sino que habilitaron su capacidad para generar una respuesta original en lenguaje humano.

## ¿Cómo funcionan los modelos de lenguaje a gran escala?

En el próximo capítulo vamos a explorar diferentes tipos de modelos de IA Generativa, pero por ahora echemos un vistazo a cómo funcionan los modelos de lenguaje a gran escala, con un enfoque en los modelos GPT (Generative Pre-trained Transformer) de OpenAI.

- **Tokenizador, texto a números**: Los Modelos de Lenguaje a Gran Escala reciben un texto como entrada y generan un texto como salida. Sin embargo, siendo modelos estadísticos, trabajan mucho mejor con números que con secuencias de texto. Por eso, cada entrada al modelo es procesada por un tokenizador, antes de ser utilizada por el modelo principal. Un token es un fragmento de texto, que consta de un número variable de caracteres, por lo que la tarea principal del tokenizador es dividir la entrada en una matriz de tokens. Luego, cada token se mapea con un índice de token, que es la codificación entera del fragmento de texto original.

![Ejemplo de tokenización](../../../translated_images/tokenizer-example.png?WT.3b4be927057ceb39216ffc617cde2fd4d843e0d7557fc81d08a0018831f601ed.es.mc_id=academic-105485-koreyst)

- **Predicción de tokens de salida**: Dados n tokens como entrada (con un máximo n que varía de un modelo a otro), el modelo es capaz de predecir un token como salida. Este token se incorpora luego en la entrada de la siguiente iteración, en un patrón de ventana expansiva, permitiendo una mejor experiencia de usuario al obtener una (o varias) oraciones como respuesta. Esto explica por qué, si alguna vez jugaste con ChatGPT, podrías haber notado que a veces parece que se detiene en medio de una oración.

- **Proceso de selección, distribución de probabilidad**: El token de salida es elegido por el modelo según su probabilidad de ocurrir después de la secuencia de texto actual. Esto se debe a que el modelo predice una distribución de probabilidad sobre todos los posibles 'siguientes tokens', calculada en base a su entrenamiento. Sin embargo, no siempre se elige el token con la mayor probabilidad de la distribución resultante. Se añade un grado de aleatoriedad a esta elección, de manera que el modelo actúa de manera no determinista, no obtenemos la misma salida exacta para la misma entrada. Este grado de aleatoriedad se añade para simular el proceso de pensamiento creativo y puede ajustarse usando un parámetro del modelo llamado temperatura.

## ¿Cómo puede nuestra startup aprovechar los Modelos de Lenguaje a Gran Escala?

Ahora que tenemos una mejor comprensión del funcionamiento interno de un modelo de lenguaje a gran escala, veamos algunos ejemplos prácticos de las tareas más comunes que pueden realizar bastante bien, con un ojo puesto en nuestro escenario empresarial.
Dijimos que la capacidad principal de un Modelo de Lenguaje a Gran Escala es _generar un texto desde cero, partiendo de una entrada textual, escrita en lenguaje natural_.

Pero, ¿qué tipo de entrada y salida textual?
La entrada de un modelo de lenguaje a gran escala se conoce como prompt, mientras que la salida se conoce como completion, término que se refiere al mecanismo del modelo de generar el siguiente token para completar la entrada actual. Vamos a profundizar en qué es un prompt y cómo diseñarlo de manera que saquemos el máximo provecho de nuestro modelo. Pero por ahora, digamos que un prompt puede incluir:

- Una **instrucción** que especifique el tipo de salida que esperamos del modelo. Esta instrucción a veces puede incluir algunos ejemplos o datos adicionales.

  1. Resumen de un artículo, libro, reseñas de productos y más, junto con la extracción de ideas de datos no estructurados.
    
    ![Ejemplo de resumen](../../../translated_images/summarization-example.png?WT.cf0bac4d43b9de29ec37e1b7707d9bd67e030f4e884a0ae778c6a3c36be77d79.es.mc_id=academic-105485-koreyst)
  
  2. Ideación creativa y diseño de un artículo, un ensayo, una tarea o más.
      
     ![Ejemplo de escritura creativa](../../../translated_images/creative-writing-example.png?WT.04b03c92f46ed96df1138828e37760ac81e06eaa8602de8c4b175a9c514c9a14.es.mc_id=academic-105485-koreyst)

- Una **pregunta**, formulada en forma de conversación con un agente.
  
  ![Ejemplo de conversación](../../../translated_images/conversation-example.png?WT.f904fd4c48fbf695b8e5d334e1ec02d66830bbc679ad4b5195f1c563e9bfbdc1.es.mc_id=academic-105485-koreyst)

- Un fragmento de **texto para completar**, que implícitamente es una solicitud de asistencia de escritura.
  
  ![Ejemplo de finalización de texto](../../../translated_images/text-completion-example.png?WT.9a641431b14ebbbcaa7d22def9729cf8cc7ab358b1dbc948653e43af47e41f73.es.mc_id=academic-105485-koreyst)

- Un fragmento de **código** junto con la solicitud de explicarlo y documentarlo, o un comentario pidiendo generar un fragmento de código que realice una tarea específica.
  
  ![Ejemplo de codificación](../../../translated_images/coding-example.png?WT.75933a45164ffb74ffbb4a72c8f77b0f76ebcdc676a58ad2871de5d32db63515.es.mc_id=academic-105485-koreyst)

Los ejemplos anteriores son bastante simples y no pretenden ser una demostración exhaustiva de las capacidades de los Modelos de Lenguaje a Gran Escala. Solo quieren mostrar el potencial de usar IA generativa, en particular pero no limitado al contexto educativo.

Además, la salida de un modelo de IA generativa no es perfecta y, a veces, la creatividad del modelo puede jugar en su contra, resultando en una salida que es una combinación de palabras que el usuario humano puede interpretar como una distorsión de la realidad, o puede ser ofensiva. La IA generativa no es inteligente, al menos en la definición más completa de inteligencia, que incluye razonamiento crítico y creativo o inteligencia emocional; no es determinista, y no es confiable, ya que fabricaciones, como referencias erróneas, contenido y declaraciones, pueden combinarse con información correcta y presentarse de manera persuasiva y confiada. En las lecciones siguientes, abordaremos todas estas limitaciones y veremos qué podemos hacer para mitigarlas.

## Tarea

Tu tarea es leer más sobre [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e intentar identificar un área donde agregarías IA generativa hoy que no la tenga. ¿Cómo sería el impacto diferente de hacerlo a la "vieja manera", puedes hacer algo que no podías antes, o eres más rápido? Escribe un resumen de 300 palabras sobre cómo sería tu startup de IA soñada e incluye encabezados como "Problema", "Cómo usaría la IA", "Impacto" y opcionalmente un plan de negocios.

Si realizaste esta tarea, incluso podrías estar listo para postularte al incubador de Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), ofrecemos créditos tanto para Azure, OpenAI, mentoría y mucho más, ¡échale un vistazo!

## Comprobación de conocimiento

¿Qué es cierto sobre los modelos de lenguaje a gran escala?

1. Obtienes la misma respuesta exacta cada vez.
1. Hace las cosas perfectamente, excelente en sumar números, producir código funcional, etc.
1. La respuesta puede variar a pesar de usar el mismo prompt. También es excelente para darte un primer borrador de algo, ya sea texto o código. Pero necesitas mejorar los resultados.

A: 3, un LLM es no determinista, la respuesta varía, sin embargo, puedes controlar su variación a través de un ajuste de temperatura. Tampoco deberías esperar que haga las cosas perfectamente, está aquí para hacer el trabajo pesado por ti, lo que a menudo significa que obtienes un buen primer intento en algo que necesitas mejorar gradualmente.

## ¡Gran trabajo! Continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tu conocimiento sobre IA Generativa.

Dirígete a la Lección 2 donde veremos cómo [explorar y comparar diferentes tipos de LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst)!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.