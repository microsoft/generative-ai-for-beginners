<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8b3cb38518cf4fe7714d2f5e74dfa3eb",
  "translation_date": "2025-10-03T08:09:11+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "es"
}
-->
# Fundamentos de la Ingeniería de Prompts

[![Fundamentos de la Ingeniería de Prompts](../../../translated_images/04-lesson-banner.a2c90deba7fedacda69f35b41636a8951ec91c2e33f5420b1254534ac85bc18e.es.png)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear prompts efectivos en modelos de IA generativa. La forma en que redactes tu prompt para un LLM también es importante. Un prompt cuidadosamente diseñado puede lograr una mejor calidad de respuesta. Pero, ¿qué significan exactamente términos como _prompt_ e _ingeniería de prompts_? ¿Y cómo puedo mejorar el _input_ del prompt que envío al LLM? Estas son las preguntas que intentaremos responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes de los usuarios. Esto se logra utilizando _Modelos de Lenguaje Extenso_ como la serie GPT ("Generative Pre-trained Transformer") de OpenAI, que están entrenados para usar lenguaje natural y código.

Los usuarios ahora pueden interactuar con estos modelos utilizando paradigmas familiares como el chat, sin necesidad de experiencia técnica o formación previa. Los modelos están basados en _prompts_: los usuarios envían un texto de entrada (prompt) y reciben la respuesta de la IA (completion). Luego pueden "chatear con la IA" de manera iterativa, en conversaciones de múltiples turnos, refinando su prompt hasta que la respuesta cumpla con sus expectativas.

Los "prompts" se convierten ahora en la principal _interfaz de programación_ para aplicaciones de IA generativa, indicando a los modelos qué hacer e influyendo en la calidad de las respuestas generadas. La "Ingeniería de Prompts" es un campo de estudio en rápido crecimiento que se centra en el _diseño y optimización_ de prompts para ofrecer respuestas consistentes y de calidad a escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Prompts, por qué es importante y cómo podemos crear prompts más efectivos para un modelo y objetivo de aplicación específicos. Comprenderemos conceptos clave y mejores prácticas para la ingeniería de prompts, y aprenderemos sobre un entorno interactivo de "sandbox" en Jupyter Notebooks donde podemos aplicar estos conceptos a ejemplos reales.

Al final de esta lección, seremos capaces de:

1. Explicar qué es la ingeniería de prompts y por qué es importante.
2. Describir los componentes de un prompt y cómo se utilizan.
3. Aprender mejores prácticas y técnicas para la ingeniería de prompts.
4. Aplicar las técnicas aprendidas a ejemplos reales, utilizando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Prompts: La práctica de diseñar y refinar entradas para guiar a los modelos de IA hacia la producción de resultados deseados.  
Tokenización: El proceso de convertir texto en unidades más pequeñas, llamadas tokens, que un modelo puede entender y procesar.  
LLMs Ajustados por Instrucciones: Modelos de Lenguaje Extenso (LLMs) que han sido ajustados con instrucciones específicas para mejorar la precisión y relevancia de sus respuestas.

## Sandbox de Aprendizaje

La ingeniería de prompts es actualmente más arte que ciencia. La mejor manera de mejorar nuestra intuición al respecto es _practicar más_ y adoptar un enfoque de prueba y error que combine experiencia en el dominio de la aplicación con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña esta lección proporciona un entorno de _sandbox_ donde puedes probar lo que aprendes, ya sea mientras avanzas o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave de API de Azure OpenAI**: el endpoint del servicio para un LLM desplegado.  
2. **Un entorno de ejecución de Python**: en el que se pueda ejecutar el Notebook.  
3. **Variables de entorno locales**: _completa los pasos de [CONFIGURACIÓN](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ahora para estar listo_.  

El notebook incluye ejercicios _iniciales_, pero se te anima a agregar tus propias secciones de _Markdown_ (descripción) y _Código_ (solicitudes de prompts) para probar más ejemplos o ideas, y desarrollar tu intuición para el diseño de prompts.

## Guía Ilustrada

¿Quieres obtener una visión general de lo que cubre esta lección antes de profundizar? Consulta esta guía ilustrada, que te da una idea de los temas principales tratados y los puntos clave para reflexionar en cada uno. El mapa de la lección te lleva desde la comprensión de los conceptos y desafíos básicos hasta abordarlos con técnicas relevantes de ingeniería de prompts y mejores prácticas. Ten en cuenta que la sección "Técnicas Avanzadas" en esta guía se refiere a contenido cubierto en el _próximo_ capítulo de este currículo.

![Guía Ilustrada de Ingeniería de Prompts](../../../translated_images/04-prompt-engineering-sketchnote.d5f33336957a1e4f623b826195c2146ef4cc49974b72fa373de6929b474e8b70.es.png)

## Nuestra Startup

Ahora, hablemos de cómo _este tema_ se relaciona con nuestra misión de startup de [llevar la innovación de la IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicaciones impulsadas por IA para el _aprendizaje personalizado_, así que pensemos en cómo diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedir a la IA que _analice datos curriculares para identificar brechas en la cobertura_. La IA puede resumir los resultados o visualizarlos con código.  
- **Educadores** podrían pedir a la IA que _genere un plan de lección para una audiencia y tema específicos_. La IA puede crear el plan personalizado en un formato especificado.  
- **Estudiantes** podrían pedir a la IA que _les enseñe una materia difícil_. La IA ahora puede guiar a los estudiantes con lecciones, pistas y ejemplos adaptados a su nivel.  

Eso es solo la punta del iceberg. Consulta [Prompts para la Educación](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst), una biblioteca de prompts de código abierto curada por expertos en educación, para obtener una visión más amplia de las posibilidades. _¡Prueba algunos de esos prompts en el sandbox o usando el OpenAI Playground para ver qué sucede!_

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe cubrir el concepto clave #1.
Refuerza el concepto con ejemplos y referencias.

CONCEPTO #1:
Ingeniería de Prompts.
Defínelo y explica por qué es necesario.
-->

## ¿Qué es la Ingeniería de Prompts?

Comenzamos esta lección definiendo **Ingeniería de Prompts** como el proceso de _diseñar y optimizar_ entradas de texto (prompts) para ofrecer respuestas consistentes y de calidad (completions) para un objetivo de aplicación y modelo específicos. Podemos pensar en esto como un proceso de 2 pasos:

- _Diseñar_ el prompt inicial para un modelo y objetivo específicos.  
- _Refinar_ el prompt de manera iterativa para mejorar la calidad de la respuesta.  

Este es necesariamente un proceso de prueba y error que requiere intuición y esfuerzo por parte del usuario para obtener resultados óptimos. Entonces, ¿por qué es importante? Para responder a esa pregunta, primero necesitamos entender tres conceptos:

- _Tokenización_: cómo el modelo "ve" el prompt.  
- _LLMs Base_: cómo el modelo base "procesa" un prompt.  
- _LLMs Ajustados por Instrucciones_: cómo el modelo ahora puede ver "tareas".  

### Tokenización

Un LLM ve los prompts como una _secuencia de tokens_, donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Dado que los LLMs están entrenados en tokens (y no en texto sin procesar), la forma en que los prompts se tokenizan tiene un impacto directo en la calidad de la respuesta generada.

Para obtener una intuición sobre cómo funciona la tokenización, prueba herramientas como el [Tokenizador de OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) que se muestra a continuación. Copia tu prompt y observa cómo se convierte en tokens, prestando atención a cómo se manejan los caracteres de espacio y los signos de puntuación. Ten en cuenta que este ejemplo muestra un LLM más antiguo (GPT-3), por lo que probar esto con un modelo más reciente puede producir un resultado diferente.

![Tokenización](../../../translated_images/04-tokenizer-example.e71f0a0f70356c5c7d80b21e8753a28c18a7f6d4aaa1c4b08e65d17625e85642.es.png)

### Concepto: Modelos Base

Una vez que un prompt se tokeniza, la función principal del ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo base) es predecir el siguiente token en esa secuencia. Dado que los LLMs están entrenados con conjuntos de datos masivos de texto, tienen una buena comprensión de las relaciones estadísticas entre los tokens y pueden hacer esa predicción con cierta confianza. Ten en cuenta que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su próxima predicción. Pueden continuar prediciendo la secuencia hasta que el usuario intervenga o se cumpla alguna condición preestablecida.

¿Quieres ver cómo funciona la completación basada en prompts? Ingresa el prompt anterior en el [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) de Azure OpenAI Studio con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información, por lo que deberías ver una completación que satisfaga este contexto.

Pero, ¿qué pasa si el usuario quiere ver algo específico que cumpla con ciertos criterios u objetivos de tarea? Aquí es donde entran en juego los LLMs ajustados por instrucciones.

![Completación de Chat con LLM Base](../../../translated_images/04-playground-chat-base.65b76fcfde0caa6738e41d20f1a6123f9078219e6f91a88ee5ea8014f0469bdf.es.png)

### Concepto: LLMs Ajustados por Instrucciones

Un [LLM Ajustado por Instrucciones](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) comienza con el modelo base y lo ajusta con ejemplos o pares de entrada/salida (por ejemplo, "mensajes" de múltiples turnos) que pueden contener instrucciones claras, y la respuesta de la IA intenta seguir esa instrucción.

Esto utiliza técnicas como el Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo para _seguir instrucciones_ y _aprender de la retroalimentación_, de modo que produzca respuestas más adecuadas para aplicaciones prácticas y más relevantes para los objetivos del usuario.

Probémoslo: vuelve al prompt anterior, pero ahora cambia el _mensaje del sistema_ para proporcionar la siguiente instrucción como contexto:

> _Resume el contenido que se te proporcione para un estudiante de segundo grado. Limita el resultado a un párrafo con 3-5 puntos clave._

¿Ves cómo el resultado ahora está ajustado para reflejar el objetivo y formato deseados? Un educador ahora puede usar directamente esta respuesta en sus diapositivas para esa clase.

![Completación de Chat con LLM Ajustado por Instrucciones](../../../translated_images/04-playground-chat-instructions.b30bbfbdf92f2d051639c9bc23f74a0e2482f8dc7f0dafc6cc6fda81b2b00534.es.png)

## ¿Por qué necesitamos la Ingeniería de Prompts?

Ahora que sabemos cómo los prompts son procesados por los LLMs, hablemos de _por qué_ necesitamos la ingeniería de prompts. La respuesta radica en el hecho de que los LLMs actuales presentan una serie de desafíos que hacen que lograr _completaciones confiables y consistentes_ sea más difícil sin dedicar esfuerzo a la construcción y optimización de prompts. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ probablemente producirá respuestas diferentes con diferentes modelos o versiones de modelos. Y puede incluso producir resultados diferentes con el _mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de prompts pueden ayudarnos a minimizar estas variaciones proporcionando mejores límites_.  

1. **Los modelos pueden fabricar respuestas.** Los modelos están preentrenados con conjuntos de datos _grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese alcance de entrenamiento. Como resultado, pueden producir completaciones que son inexactas, imaginarias o directamente contradictorias a hechos conocidos. _Las técnicas de ingeniería de prompts ayudan a los usuarios a identificar y mitigar estas fabricaciones, por ejemplo, pidiendo a la IA citas o razonamientos_.  

1. **Las capacidades de los modelos varían.** Los modelos más nuevos o generaciones de modelos tendrán capacidades más ricas, pero también traerán peculiaridades únicas y compensaciones en costo y complejidad. _La ingeniería de prompts puede ayudarnos a desarrollar mejores prácticas y flujos de trabajo que abstraigan las diferencias y se adapten a los requisitos específicos del modelo de manera escalable y fluida_.  

Veamos esto en acción en el OpenAI o Azure OpenAI Playground:

- Usa el mismo prompt con diferentes despliegues de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face): ¿notaste las variaciones?  
- Usa el mismo prompt repetidamente con el _mismo_ despliegue de LLM (por ejemplo, el playground de Azure OpenAI): ¿cómo diferían estas variaciones?  

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno en el que los LLMs a veces generan información incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También puedes haber escuchado este término como _"alucinaciones"_ en artículos populares o trabajos de investigación. Sin embargo, recomendamos encarecidamente usar _"fabricación"_ como término para no atribuir accidentalmente un rasgo humano a un resultado impulsado por una máquina. Esto también refuerza las [directrices de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde una perspectiva terminológica, eliminando términos que también podrían considerarse ofensivos o no inclusivos en algunos contextos.

¿Quieres tener una idea de cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA a generar contenido sobre un tema inexistente (para asegurarte de que no se encuentre en el conjunto de datos de entrenamiento). Por ejemplo, intenté este prompt:

> **Prompt:** genera un plan de lección sobre la Guerra Marciana de 2076.
Una búsqueda en la web me mostró que existen relatos ficticios (por ejemplo, series de televisión o libros) sobre guerras marcianas, pero ninguno ambientado en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede estar asociado con un evento real.

Entonces, ¿qué sucede cuando probamos este mensaje con diferentes proveedores de modelos de lenguaje?

> **Respuesta 1**: OpenAI Playground (GPT-35)

![Respuesta 1](../../../translated_images/04-fabrication-oai.5818c4e0b2a2678c40e0793bf873ef4a425350dd0063a183fb8ae02cae63aa0c.es.png)

> **Respuesta 2**: Azure OpenAI Playground (GPT-35)

![Respuesta 2](../../../translated_images/04-fabrication-aoai.b14268e9ecf25caf613b7d424c16e2a0dc5b578f8f960c0c04d4fb3a68e6cf61.es.png)

> **Respuesta 3**: Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../../translated_images/04-fabrication-huggingchat.faf82a0a512789565e410568bce1ac911075b943dec59b1ef4080b61723b5bf4.es.png)

Como era de esperar, cada modelo (o versión del modelo) genera respuestas ligeramente diferentes debido al comportamiento estocástico y las variaciones en las capacidades del modelo. Por ejemplo, un modelo se dirige a una audiencia de octavo grado, mientras que otro asume un estudiante de secundaria. Sin embargo, los tres modelos generaron respuestas que podrían convencer a un usuario desinformado de que el evento fue real.

Técnicas de ingeniería de mensajes como _metaprompting_ y _configuración de temperatura_ pueden reducir las fabricaciones del modelo hasta cierto punto. Nuevas arquitecturas de ingeniería de mensajes también incorporan herramientas y técnicas nuevas de manera fluida en el flujo del mensaje, para mitigar o reducir algunos de estos efectos.

## Estudio de Caso: GitHub Copilot

Concluyamos esta sección obteniendo una idea de cómo se utiliza la ingeniería de mensajes en soluciones del mundo real, analizando un estudio de caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "programador asistente de IA": convierte mensajes de texto en sugerencias de código y está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario fluida. Como se documenta en la serie de blogs a continuación, la versión más temprana se basó en el modelo OpenAI Codex, y los ingenieros rápidamente se dieron cuenta de la necesidad de ajustar el modelo y desarrollar mejores técnicas de ingeniería de mensajes para mejorar la calidad del código. En julio, [presentaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugerencias aún más rápidas.

Lee las publicaciones en orden para seguir su proceso de aprendizaje.

- **Mayo 2023** | [GitHub Copilot está mejorando en la comprensión de tu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: Trabajando con los modelos de lenguaje detrás de GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junio 2023** | [Cómo escribir mejores mensajes para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julio 2023** | [GitHub Copilot va más allá de Codex con un modelo de IA mejorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Guía para desarrolladores sobre ingeniería de mensajes y modelos de lenguaje](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septiembre 2023** | [Cómo construir una aplicación empresarial con modelos de lenguaje: Lecciones de GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

También puedes explorar su [blog de ingeniería](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), que muestra cómo estos modelos y técnicas se _aplican_ para impulsar aplicaciones del mundo real.

---

## Construcción de Mensajes

Ya hemos visto por qué la ingeniería de mensajes es importante; ahora entendamos cómo se _construyen_ los mensajes para poder evaluar diferentes técnicas que permitan un diseño más efectivo.

### Mensaje Básico

Comencemos con el mensaje básico: una entrada de texto enviada al modelo sin ningún otro contexto. Aquí hay un ejemplo: cuando enviamos las primeras palabras del himno nacional de los Estados Unidos a la [API de Completion de OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), responde instantáneamente _completando_ con las siguientes líneas, ilustrando el comportamiento básico de predicción.

| Mensaje (Entrada) | Respuesta (Salida)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que estás comenzando la letra de "The Star-Spangled Banner", el himno nacional de los Estados Unidos. La letra completa es...      |

### Mensaje Complejo

Ahora agreguemos contexto e instrucciones a ese mensaje básico. La [API de Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir un mensaje complejo como una colección de _mensajes_ con:

- Pares de entrada/salida que reflejan la entrada del _usuario_ y la respuesta del _asistente_.
- Mensaje del sistema que establece el contexto para el comportamiento o personalidad del asistente.

La solicitud ahora tiene la forma que se muestra a continuación, donde la _tokenización_ captura de manera efectiva información relevante del contexto y la conversación. Cambiar el contexto del sistema puede ser tan impactante en la calidad de las respuestas como las entradas proporcionadas por el usuario.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```


### Mensaje de Instrucción

En los ejemplos anteriores, el mensaje del usuario era una consulta de texto simple que puede interpretarse como una solicitud de información. Con los mensajes de _instrucción_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando una mejor orientación a la IA. Aquí hay un ejemplo:

| Mensaje (Entrada)                                                                                                                                                                                                                         | Respuesta (Salida)                                                                                                        | Tipo de Instrucción |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escribe una descripción de la Guerra Civil                                                                                                                                                                                                   | _devuelve un párrafo simple_                                                                                              | Simple              |
| Escribe una descripción de la Guerra Civil. Proporciona fechas y eventos clave y describe su importancia                                                                                                                                     | _devuelve un párrafo seguido de una lista de fechas clave con descripciones_                                             | Complejo             |
| Escribe una descripción de la Guerra Civil en un párrafo. Proporciona 3 puntos clave con fechas y su importancia. Proporciona 3 puntos más con figuras históricas clave y sus contribuciones. Devuelve la salida como un archivo JSON | _devuelve detalles más extensos en un cuadro de texto, formateados como JSON que puedes copiar y pegar en un archivo para validar según sea necesario_ | Complejo. Formateado. |

## Contenido Principal

En los ejemplos anteriores, el mensaje seguía siendo bastante abierto, permitiendo que el modelo de lenguaje decidiera qué parte de su conjunto de datos preentrenado era relevante. Con el patrón de diseño de _contenido principal_, el texto de entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí hay un ejemplo donde la instrucción es "resume esto en 2 oraciones".

| Mensaje (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Respuesta (Salida)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. Lleva el nombre del dios romano Júpiter. Cuando se observa desde la Tierra, Júpiter puede ser lo suficientemente brillante como para que su luz reflejada proyecte sombras visibles, y es, en promedio, el tercer objeto natural más brillante en el cielo nocturno después de la Luna y Venus. <br/> **Resume esto en 2 oraciones cortas** | Júpiter, el quinto planeta desde el Sol, es el más grande del Sistema Solar y es conocido por ser uno de los objetos más brillantes en el cielo nocturno. Nombrado en honor al dios romano Júpiter, es un gigante gaseoso cuya masa es dos veces y media la de todos los demás planetas del Sistema Solar juntos. |

El segmento de contenido principal puede usarse de varias maneras para impulsar instrucciones más efectivas:

- **Ejemplos**: en lugar de decirle al modelo qué hacer con una instrucción explícita, dale ejemplos de lo que debe hacer y deja que infiera el patrón.
- **Indicadores**: sigue la instrucción con un "indicador" que prepara la respuesta, guiando al modelo hacia respuestas más relevantes.
- **Plantillas**: estas son "recetas" repetibles para mensajes con marcadores de posición (variables) que pueden personalizarse con datos para casos de uso específicos.

Exploremos estas técnicas en acción.

### Uso de Ejemplos

Este es un enfoque donde utilizas el contenido principal para "alimentar al modelo" con algunos ejemplos del resultado deseado para una instrucción dada y dejas que infiera el patrón para el resultado deseado. Según la cantidad de ejemplos proporcionados, podemos tener mensajes de cero ejemplos, un ejemplo, pocos ejemplos, etc.

El mensaje ahora consta de tres componentes:

- Una descripción de la tarea
- Algunos ejemplos del resultado deseado
- El inicio de un nuevo ejemplo (que se convierte en una descripción implícita de la tarea)

| Tipo de Aprendizaje | Mensaje (Entrada)                                                                                                                                        | Respuesta (Salida)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Cero ejemplos     | "The Sun is Shining". Traducir al español                                                                                                            | "El Sol está brillando".    |
| Un ejemplo      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Pocos ejemplos      | El jugador corrió las bases => Béisbol <br/> El jugador hizo un ace => Tenis <br/> El jugador hizo un seis => Cricket <br/> El jugador hizo un mate => | Baloncesto                  |
|               |                                                                                                                                                       |                             |

Observa cómo tuvimos que proporcionar una instrucción explícita ("Traducir al español") en el ejemplo de cero ejemplos, pero se infiere en el ejemplo de un ejemplo. El ejemplo de pocos ejemplos muestra cómo agregar más ejemplos permite que los modelos hagan inferencias más precisas sin instrucciones adicionales.

### Indicadores en el Mensaje

Otra técnica para usar contenido principal es proporcionar _indicadores_ en lugar de ejemplos. En este caso, estamos dando al modelo un empujón en la dirección correcta _comenzando_ con un fragmento que refleja el formato de respuesta deseado. El modelo luego "toma el indicador" para continuar en esa línea.

| Número de Indicadores | Mensaje (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Respuesta (Salida)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume Esto**                                       | Júpiter es el planeta más grande de nuestro Sistema Solar y el quinto desde el Sol. Es un gigante gaseoso con una masa 1/1000 de la del Sol, pero más pesado que todos los demás planetas juntos. Las civilizaciones antiguas han conocido Júpiter durante mucho tiempo, y es fácilmente visible en el cielo nocturno. |
| 1              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. <br/>**Resúmelo** <br/> Lo que aprendimos es que Júpiter | es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas combinados. Es fácilmente visible a simple vista y ha sido conocido desde tiempos antiguos.                        |
| 2              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. <br/>**Resúmelo** <br/> Los 3 datos principales que aprendimos:         | 1. Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. <br/> 2. Es un gigante gaseoso con una masa milésima parte de la del Sol...<br/> 3. Júpiter ha sido visible a simple vista desde tiempos antiguos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Plantillas de Prompts

Una plantilla de prompt es una _receta predefinida para un prompt_ que puede almacenarse y reutilizarse según sea necesario, para ofrecer experiencias de usuario más consistentes a gran escala. En su forma más simple, es simplemente una colección de ejemplos de prompts como [este de OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que proporciona tanto los componentes interactivos del prompt (mensajes de usuario y sistema) como el formato de solicitud impulsado por API, para apoyar la reutilización.

En su forma más compleja, como [este ejemplo de LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contiene _marcadores de posición_ que pueden reemplazarse con datos de diversas fuentes (entrada del usuario, contexto del sistema, fuentes de datos externas, etc.) para generar un prompt dinámicamente. Esto nos permite crear una biblioteca de prompts reutilizables que pueden usarse para ofrecer experiencias de usuario consistentes **programáticamente** a gran escala.

Finalmente, el verdadero valor de las plantillas radica en la capacidad de crear y publicar _bibliotecas de prompts_ para dominios de aplicación verticales, donde la plantilla de prompt ahora está _optimizada_ para reflejar contextos o ejemplos específicos de la aplicación que hacen que las respuestas sean más relevantes y precisas para la audiencia objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, curando una biblioteca de prompts para el ámbito educativo con énfasis en objetivos clave como planificación de lecciones, diseño curricular, tutoría estudiantil, etc.

## Contenido de Apoyo

Si pensamos en la construcción de prompts como una instrucción (tarea) y un objetivo (contenido principal), entonces el _contenido secundario_ es como contexto adicional que proporcionamos para **influir en el resultado de alguna manera**. Podría ser parámetros de ajuste, instrucciones de formato, taxonomías de temas, etc., que pueden ayudar al modelo a _adaptar_ su respuesta para cumplir con los objetivos o expectativas del usuario.

Por ejemplo: Dado un catálogo de cursos con metadatos extensos (nombre, descripción, nivel, etiquetas de metadatos, instructor, etc.) sobre todos los cursos disponibles en el currículo:

- podemos definir una instrucción para "resumir el catálogo de cursos para el otoño de 2023"
- podemos usar el contenido principal para proporcionar algunos ejemplos del resultado deseado
- podemos usar el contenido secundario para identificar las 5 "etiquetas" principales de interés.

Ahora, el modelo puede proporcionar un resumen en el formato mostrado por los ejemplos dados, pero si un resultado tiene múltiples etiquetas, puede priorizar las 5 etiquetas identificadas en el contenido secundario.

---

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe cubrir el concepto principal #1.
Refuerza el concepto con ejemplos y referencias.

CONCEPTO #3:
Técnicas de Ingeniería de Prompts.
¿Cuáles son algunas técnicas básicas para la ingeniería de prompts?
Ilústralo con algunos ejercicios.
-->

## Mejores Prácticas para Prompts

Ahora que sabemos cómo se pueden _construir_ los prompts, podemos empezar a pensar en cómo _diseñarlos_ para reflejar mejores prácticas. Podemos pensar en esto en dos partes: tener la _mentalidad_ adecuada y aplicar las _técnicas_ correctas.

### Mentalidad para la Ingeniería de Prompts

La Ingeniería de Prompts es un proceso de prueba y error, así que ten en cuenta tres factores generales:

1. **El conocimiento del dominio importa.** La precisión y relevancia de la respuesta es una función del _dominio_ en el que opera esa aplicación o usuario. Aplica tu intuición y experiencia en el dominio para **personalizar técnicas** aún más. Por ejemplo, define _personalidades específicas del dominio_ en tus prompts del sistema, o utiliza _plantillas específicas del dominio_ en tus prompts de usuario. Proporciona contenido secundario que refleje contextos específicos del dominio, o utiliza _pistas y ejemplos específicos del dominio_ para guiar al modelo hacia patrones de uso familiares.

2. **El conocimiento del modelo importa.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones de los modelos también pueden variar en términos del conjunto de datos de entrenamiento que utilizan (conocimiento preentrenado), las capacidades que proporcionan (por ejemplo, a través de API o SDK) y el tipo de contenido para el que están optimizados (por ejemplo, código vs. imágenes vs. texto). Comprende las fortalezas y limitaciones del modelo que estás utilizando y usa ese conocimiento para _priorizar tareas_ o construir _plantillas personalizadas_ optimizadas para las capacidades del modelo.

3. **La iteración y validación importan.** Los modelos están evolucionando rápidamente, al igual que las técnicas para la ingeniería de prompts. Como experto en el dominio, puedes tener otros contextos o criterios específicos de _tu_ aplicación que pueden no aplicarse a la comunidad en general. Utiliza herramientas y técnicas de ingeniería de prompts para "dar inicio" a la construcción de prompts, luego itera y valida los resultados utilizando tu propia intuición y experiencia en el dominio. Registra tus ideas y crea una **base de conocimiento** (por ejemplo, bibliotecas de prompts) que puedan usarse como una nueva línea base por otros, para iteraciones más rápidas en el futuro.

## Mejores Prácticas

Ahora veamos las mejores prácticas comunes recomendadas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y los practicantes de [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                               | Por qué                                                                                                                                                                                                                                               |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evalúa los modelos más recientes. | Las nuevas generaciones de modelos probablemente tengan características y calidad mejoradas, pero también pueden implicar costos más altos. Evalúalos para medir el impacto y luego toma decisiones de migración.                                        |
| Separa instrucciones y contexto   | Verifica si tu modelo/proveedor define _delimitadores_ para distinguir instrucciones, contenido principal y contenido secundario más claramente. Esto puede ayudar a los modelos a asignar pesos más precisos a los tokens.                             |
| Sé específico y claro             | Da más detalles sobre el contexto deseado, el resultado, la longitud, el formato, el estilo, etc. Esto mejorará tanto la calidad como la consistencia de las respuestas. Captura recetas en plantillas reutilizables.                                  |
| Sé descriptivo, usa ejemplos      | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un enfoque `zero-shot` donde le das una instrucción (pero sin ejemplos), luego prueba `few-shot` como refinamiento, proporcionando algunos ejemplos del resultado deseado. Usa analogías. |
| Usa pistas para iniciar completaciones | Guíalo hacia un resultado deseado dándole algunas palabras o frases iniciales que pueda usar como punto de partida para la respuesta.                                                                                                               |
| Repite                            | A veces puede ser necesario repetir las instrucciones al modelo. Da instrucciones antes y después de tu contenido principal, usa una instrucción y una pista, etc. Itera y valida para ver qué funciona.                                              |
| El orden importa                  | El orden en que presentas la información al modelo puede impactar el resultado, incluso en los ejemplos de aprendizaje, gracias al sesgo de recencia. Prueba diferentes opciones para ver qué funciona mejor.                                           |
| Dale al modelo una "salida"       | Proporciona al modelo una respuesta de _respaldo_ que pueda dar si no puede completar la tarea por alguna razón. Esto puede reducir las posibilidades de que los modelos generen respuestas falsas o fabricadas.                                       |
|                                   |                                                                                                                                                                                                                                                       |

Como con cualquier mejor práctica, recuerda que _tu experiencia puede variar_ según el modelo, la tarea y el dominio. Usa estas como punto de partida e itera para encontrar lo que funciona mejor para ti. Reevalúa constantemente tu proceso de ingeniería de prompts a medida que nuevos modelos y herramientas estén disponibles, con un enfoque en la escalabilidad del proceso y la calidad de las respuestas.

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe proporcionar un desafío de código si aplica.

DESAFÍO:
Enlace a un Jupyter Notebook con solo los comentarios en las instrucciones (las secciones de código están vacías).

SOLUCIÓN:
Enlace a una copia de ese Notebook con los prompts completados y ejecutados, mostrando un ejemplo.
-->

## Tarea

¡Felicidades! ¡Llegaste al final de la lección! Es hora de poner a prueba algunos de esos conceptos y técnicas con ejemplos reales.

Para nuestra tarea, utilizaremos un Jupyter Notebook con ejercicios que puedes completar de manera interactiva. También puedes extender el Notebook con tus propias celdas de Markdown y Código para explorar ideas y técnicas por tu cuenta.

### Para comenzar, haz un fork del repositorio, luego

- (Recomendado) Lanza GitHub Codespaces
- (Alternativamente) Clona el repositorio en tu dispositivo local y úsalo con Docker Desktop
- (Alternativamente) Abre el Notebook con tu entorno de ejecución de Notebook preferido.

### Luego, configura tus variables de entorno

- Copia el archivo `.env.copy` en la raíz del repositorio a `.env` y completa los valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT`. Regresa a la [sección de Sandbox de Aprendizaje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender cómo hacerlo.

### Luego, abre el Jupyter Notebook

- Selecciona el kernel de ejecución. Si usas las opciones 1 o 2, simplemente selecciona el kernel predeterminado de Python 3.10.x proporcionado por el contenedor de desarrollo.

Estás listo para ejecutar los ejercicios. Ten en cuenta que aquí no hay respuestas _correctas o incorrectas_, solo se trata de explorar opciones mediante prueba y error y construir intuición sobre lo que funciona para un modelo y dominio de aplicación dado.

_Por esta razón, no hay segmentos de Solución de Código en esta lección. En cambio, el Notebook tendrá celdas de Markdown tituladas "Mi Solución:" que muestran un ejemplo de salida como referencia._

 <!--
PLANTILLA DE LECCIÓN:
Cierra la sección con un resumen y recursos para aprendizaje autodirigido.
-->

## Verificación de conocimiento

¿Cuál de las siguientes es un buen prompt siguiendo algunas prácticas razonables?

1. Muéstrame una imagen de un coche rojo
2. Muéstrame una imagen de un coche rojo de la marca Volvo y modelo XC90 estacionado junto a un acantilado con el sol poniéndose
3. Muéstrame una imagen de un coche rojo de la marca Volvo y modelo XC90

R: 2, es el mejor prompt ya que proporciona detalles sobre "qué" y entra en especificaciones (no cualquier coche, sino una marca y modelo específicos) y también describe el entorno general. 3 es el siguiente mejor ya que también contiene mucha descripción.

## 🚀 Desafío

Intenta aprovechar la técnica de "pista" con el prompt: Completa la frase "Muéstrame una imagen de un coche rojo de la marca Volvo y ". ¿Qué responde, y cómo lo mejorarías?

## ¡Buen trabajo! Continúa tu aprendizaje

¿Quieres aprender más sobre diferentes conceptos de Ingeniería de Prompts? Ve a la [página de aprendizaje continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar otros recursos excelentes sobre este tema.

Dirígete a la Lección 5 donde veremos [técnicas avanzadas de prompts](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.