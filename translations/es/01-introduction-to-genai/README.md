<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "bfb7901bdbece1ba3e9f35c400ca33e8",
  "translation_date": "2025-10-17T22:50:50+00:00",
  "source_file": "01-introduction-to-genai/README.md",
  "language_code": "es"
}
-->
# Introducción a la IA Generativa y los Modelos de Lenguaje Extensos

[![Introducción a la IA Generativa y los Modelos de Lenguaje Extensos](../../../translated_images/01-lesson-banner.2424cfd092f43366707ee2d15749f62f76f80ea3cb0816f4f31d0abd5ffd4dd1.es.png)](https://youtu.be/lFXQkBvEe0o?si=6ZBcQTwLJJDpnX0K)

_(Haz clic en la imagen de arriba para ver el video de esta lección)_

La IA generativa es una inteligencia artificial capaz de generar texto, imágenes y otros tipos de contenido. Lo que la hace una tecnología fantástica es que democratiza la IA; cualquiera puede usarla con tan solo un mensaje de texto, una frase escrita en lenguaje natural. No necesitas aprender un lenguaje como Java o SQL para lograr algo valioso, solo necesitas usar tu idioma, expresar lo que deseas y obtendrás una sugerencia de un modelo de IA. Las aplicaciones e impactos de esto son enormes: puedes escribir o entender informes, redactar aplicaciones y mucho más, todo en cuestión de segundos.

En este programa, exploraremos cómo nuestra startup aprovecha la IA generativa para desbloquear nuevos escenarios en el mundo de la educación y cómo abordamos los inevitables desafíos asociados con las implicaciones sociales de su aplicación y las limitaciones tecnológicas.

## Introducción

Esta lección cubrirá:

- Introducción al escenario empresarial: nuestra idea y misión como startup.
- IA generativa y cómo llegamos al panorama tecnológico actual.
- Funcionamiento interno de un modelo de lenguaje extenso.
- Principales capacidades y casos prácticos de uso de los Modelos de Lenguaje Extensos.

## Objetivos de aprendizaje

Después de completar esta lección, comprenderás:

- Qué es la IA generativa y cómo funcionan los Modelos de Lenguaje Extensos.
- Cómo puedes aprovechar los modelos de lenguaje extenso para diferentes casos de uso, con un enfoque en escenarios educativos.

## Escenario: nuestra startup educativa

La Inteligencia Artificial Generativa (IA) representa el pináculo de la tecnología de IA, empujando los límites de lo que antes se consideraba imposible. Los modelos de IA generativa tienen varias capacidades y aplicaciones, pero para este programa exploraremos cómo está revolucionando la educación a través de una startup ficticia. Nos referiremos a esta startup como _nuestra startup_. Nuestra startup trabaja en el ámbito educativo con la ambiciosa misión de:

> _mejorar la accesibilidad al aprendizaje a nivel global, asegurando un acceso equitativo a la educación y proporcionando experiencias de aprendizaje personalizadas a cada estudiante, según sus necesidades_.

El equipo de nuestra startup es consciente de que no podremos alcanzar este objetivo sin aprovechar una de las herramientas más poderosas de los tiempos modernos: los Modelos de Lenguaje Extensos (LLMs).

Se espera que la IA generativa revolucione la forma en que aprendemos y enseñamos hoy en día, con estudiantes que tendrán a su disposición profesores virtuales las 24 horas del día, que proporcionan vastas cantidades de información y ejemplos, y profesores que podrán aprovechar herramientas innovadoras para evaluar a sus estudiantes y brindar retroalimentación.

![Cinco estudiantes jóvenes mirando un monitor - imagen de DALLE2](../../../translated_images/students-by-DALLE2.b70fddaced1042ee47092320243050c4c9a7da78b31eeba515b09b2f0dca009b.es.png)

Para comenzar, definamos algunos conceptos básicos y terminología que utilizaremos a lo largo del programa.

## ¿Cómo llegamos a la IA Generativa?

A pesar del extraordinario _hype_ generado recientemente por el anuncio de los modelos de IA generativa, esta tecnología lleva décadas en desarrollo, con los primeros esfuerzos de investigación que datan de los años 60. Ahora estamos en un punto en el que la IA tiene capacidades cognitivas humanas, como la conversación, como lo demuestran, por ejemplo, [OpenAI ChatGPT](https://openai.com/chatgpt) o [Bing Chat](https://www.microsoft.com/edge/features/bing-chat?WT.mc_id=academic-105485-koreyst), que también utiliza un modelo GPT para las conversaciones de búsqueda en Bing.

Retrocediendo un poco, los primeros prototipos de IA consistían en chatbots escritos a máquina, que dependían de una base de conocimientos extraída de un grupo de expertos y representada en una computadora. Las respuestas en la base de conocimientos se activaban por palabras clave que aparecían en el texto de entrada. Sin embargo, pronto quedó claro que tal enfoque, utilizando chatbots escritos a máquina, no escalaba bien.

### Un enfoque estadístico para la IA: Aprendizaje Automático

Un punto de inflexión llegó durante los años 90, con la aplicación de un enfoque estadístico al análisis de texto. Esto llevó al desarrollo de nuevos algoritmos, conocidos como aprendizaje automático, capaces de aprender patrones a partir de datos sin ser programados explícitamente. Este enfoque permite a las máquinas simular la comprensión del lenguaje humano: un modelo estadístico se entrena con pares de texto y etiquetas, lo que permite al modelo clasificar texto de entrada desconocido con una etiqueta predefinida que representa la intención del mensaje.

### Redes neuronales y asistentes virtuales modernos

En los últimos años, la evolución tecnológica del hardware, capaz de manejar mayores cantidades de datos y cálculos más complejos, fomentó la investigación en IA, llevando al desarrollo de algoritmos avanzados de aprendizaje automático conocidos como redes neuronales o algoritmos de aprendizaje profundo.

Las redes neuronales (y en particular las Redes Neuronales Recurrentes – RNNs) mejoraron significativamente el procesamiento del lenguaje natural, permitiendo representar el significado del texto de una manera más significativa, valorando el contexto de una palabra en una oración.

Esta es la tecnología que impulsó los asistentes virtuales nacidos en la primera década del nuevo siglo, muy competentes en interpretar el lenguaje humano, identificar una necesidad y realizar una acción para satisfacerla, como responder con un guion predefinido o consumir un servicio de terceros.

### Hoy en día, IA Generativa

Así es como llegamos a la IA Generativa actual, que puede considerarse como un subconjunto del aprendizaje profundo.

![IA, ML, DL y IA Generativa](../../../translated_images/AI-diagram.c391fa518451a40de58d4f792c88adb8568d8cb4c48eed6e97b6b16e621eeb77.es.png)

Después de décadas de investigación en el campo de la IA, una nueva arquitectura de modelo, llamada _Transformer_, superó los límites de las RNNs, siendo capaz de recibir secuencias de texto mucho más largas como entrada. Los Transformers se basan en el mecanismo de atención, que permite al modelo asignar diferentes pesos a las entradas que recibe, ‘prestando más atención’ donde se concentra la información más relevante, independientemente de su orden en la secuencia de texto.

La mayoría de los modelos recientes de IA generativa – también conocidos como Modelos de Lenguaje Extensos (LLMs), ya que trabajan con entradas y salidas textuales – están basados en esta arquitectura. Lo interesante de estos modelos – entrenados con una enorme cantidad de datos no etiquetados de diversas fuentes como libros, artículos y sitios web – es que pueden adaptarse a una amplia variedad de tareas y generar texto gramaticalmente correcto con un semblante de creatividad. Así que, no solo han mejorado increíblemente la capacidad de una máquina para ‘entender’ un texto de entrada, sino que también han habilitado su capacidad para generar una respuesta original en lenguaje humano.

## ¿Cómo funcionan los modelos de lenguaje extenso?

En el próximo capítulo vamos a explorar diferentes tipos de modelos de IA Generativa, pero por ahora echemos un vistazo a cómo funcionan los modelos de lenguaje extenso, con un enfoque en los modelos de OpenAI GPT (Generative Pre-trained Transformer).

- **Tokenizador, texto a números**: Los Modelos de Lenguaje Extensos reciben un texto como entrada y generan un texto como salida. Sin embargo, al ser modelos estadísticos, funcionan mucho mejor con números que con secuencias de texto. Es por eso que cada entrada al modelo es procesada por un tokenizador antes de ser utilizada por el núcleo del modelo. Un token es un fragmento de texto – que consiste en un número variable de caracteres, por lo que la tarea principal del tokenizador es dividir la entrada en un arreglo de tokens. Luego, cada token se asigna a un índice de token, que es la codificación entera del fragmento de texto original.

![Ejemplo de tokenización](../../../translated_images/tokenizer-example.80a5c151ee7d1bd485eff5aca60ac3d2c1eaaff4c0746e09b98c696c959afbfa.es.png)

- **Predicción de tokens de salida**: Dado n tokens como entrada (con un máximo n que varía de un modelo a otro), el modelo es capaz de predecir un token como salida. Este token se incorpora a la entrada de la siguiente iteración, en un patrón de ventana expansiva, lo que permite una mejor experiencia de usuario al obtener una (o varias) oraciones como respuesta. Esto explica por qué, si alguna vez has jugado con ChatGPT, podrías haber notado que a veces parece que se detiene en medio de una oración.

- **Proceso de selección, distribución de probabilidad**: El token de salida es elegido por el modelo según su probabilidad de ocurrir después de la secuencia de texto actual. Esto se debe a que el modelo predice una distribución de probabilidad sobre todos los posibles ‘siguientes tokens’, calculada en base a su entrenamiento. Sin embargo, no siempre se elige el token con la mayor probabilidad de la distribución resultante. Se agrega un grado de aleatoriedad a esta elección, de manera que el modelo actúe de forma no determinista: no obtenemos exactamente la misma salida para la misma entrada. Este grado de aleatoriedad se agrega para simular el proceso de pensamiento creativo y se puede ajustar utilizando un parámetro del modelo llamado temperatura.

## ¿Cómo puede nuestra startup aprovechar los Modelos de Lenguaje Extensos?

Ahora que tenemos una mejor comprensión del funcionamiento interno de un modelo de lenguaje extenso, veamos algunos ejemplos prácticos de las tareas más comunes que pueden realizar bastante bien, con un enfoque en nuestro escenario empresarial. Dijimos que la principal capacidad de un Modelo de Lenguaje Extenso es _generar un texto desde cero, partiendo de una entrada textual escrita en lenguaje natural_.

¿Pero qué tipo de entrada y salida textual?
La entrada de un modelo de lenguaje extenso se conoce como un _prompt_, mientras que la salida se conoce como una _completion_, término que se refiere al mecanismo del modelo para generar el siguiente token para completar la entrada actual. Vamos a profundizar en qué es un prompt y cómo diseñarlo de manera que obtengamos el máximo provecho de nuestro modelo. Pero por ahora, digamos que un prompt puede incluir:

- Una **instrucción** especificando el tipo de salida que esperamos del modelo. Esta instrucción a veces puede incluir algunos ejemplos o datos adicionales.

  1. Resumen de un artículo, libro, reseñas de productos y más, junto con la extracción de ideas de datos no estructurados.
    
    ![Ejemplo de resumen](../../../translated_images/summarization-example.7b7ff97147b3d790477169f442b5e3f8f78079f152450e62c45dbdc23b1423c1.es.png)
  
  2. Ideación creativa y diseño de un artículo, ensayo, tarea o más.
      
     ![Ejemplo de escritura creativa](../../../translated_images/creative-writing-example.e24a685b5a543ad1287ad8f6c963019518920e92a1cf7510f354e85b0830fbe8.es.png)

- Una **pregunta**, formulada en forma de conversación con un agente.
  
  ![Ejemplo de conversación](../../../translated_images/conversation-example.60c2afc0f595fa599f367d36ccc3909ffc15e1d5265cb33b907d3560f3d03116.es.png)

- Un fragmento de **texto para completar**, que implícitamente es una solicitud de asistencia para escribir.
  
  ![Ejemplo de finalización de texto](../../../translated_images/text-completion-example.cbb0f28403d427524f8f8c935f84d084a9765b683a6bf37f977df3adb868b0e7.es.png)

- Un fragmento de **código** junto con la solicitud de explicarlo y documentarlo, o un comentario pidiendo generar un código que realice una tarea específica.
  
  ![Ejemplo de codificación](../../../translated_images/coding-example.50ebabe8a6afff20267c91f18aab1957ddd9561ee2988b2362b7365aa6796935.es.png)

Los ejemplos anteriores son bastante simples y no están destinados a ser una demostración exhaustiva de las capacidades de los Modelos de Lenguaje Extensos. Están diseñados para mostrar el potencial de usar IA generativa, en particular pero no limitado a contextos educativos.

Además, la salida de un modelo de IA generativa no es perfecta y, a veces, la creatividad del modelo puede jugar en su contra, resultando en una salida que es una combinación de palabras que el usuario humano puede interpretar como una distorsión de la realidad, o puede ser ofensiva. La IA generativa no es inteligente, al menos en la definición más completa de inteligencia, que incluye razonamiento crítico y creativo o inteligencia emocional; no es determinista, y no es confiable, ya que fabricaciones, como referencias erróneas, contenido y declaraciones, pueden combinarse con información correcta y presentarse de manera persuasiva y confiada. En las siguientes lecciones, abordaremos todas estas limitaciones y veremos qué podemos hacer para mitigarlas.

## Tarea

Tu tarea es leer más sobre [IA generativa](https://en.wikipedia.org/wiki/Generative_artificial_intelligence?WT.mc_id=academic-105485-koreyst) e intentar identificar un área donde agregarías IA generativa hoy en día que no la tenga. ¿Cómo sería diferente el impacto en comparación con hacerlo de la "forma antigua"? ¿Puedes hacer algo que antes no podías o eres más rápido? Escribe un resumen de 300 palabras sobre cómo sería tu startup de IA soñada e incluye encabezados como "Problema", "Cómo usaría la IA", "Impacto" y opcionalmente un plan de negocios.

Si realizaste esta tarea, podrías estar listo para aplicar al incubador de Microsoft, [Microsoft for Startups Founders Hub](https://www.microsoft.com/startups?WT.mc_id=academic-105485-koreyst), donde ofrecemos créditos para Azure, OpenAI, mentoría y mucho más. ¡Échale un vistazo!

## Verificación de conocimiento

¿Qué es cierto sobre los modelos de lenguaje extenso?

1. Obtienes exactamente la misma respuesta cada vez.
1. Hace las cosas perfectamente, es excelente sumando números, produciendo código funcional, etc.
1. La respuesta puede variar a pesar de usar el mismo prompt. También es excelente para darte un primer borrador de algo, ya sea texto o código. Pero necesitas mejorar los resultados.

R: 3, un LLM es no determinista, la respuesta varía, sin embargo, puedes controlar su variación mediante un ajuste de temperatura. Tampoco deberías esperar que haga las cosas perfectamente, está aquí para hacer el trabajo pesado por ti, lo que a menudo significa que obtienes un buen primer intento de algo que necesitas mejorar gradualmente.

## ¡Buen trabajo! Continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA generativa.
Dirígete a la Lección 2, donde veremos cómo [explorar y comparar diferentes tipos de LLM](../02-exploring-and-comparing-different-llms/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.