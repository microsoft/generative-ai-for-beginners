# Fundamentos de la Ingeniería de Prompt

[![Fundamentos de la Ingeniería de Prompt](../../../translated_images/es/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear prompts efectivos en modelos generativos de IA. La forma en que escribes tu prompt para un LLM también importa. Un prompt cuidadosamente elaborado puede lograr una mejor calidad de respuesta. Pero, ¿qué significan exactamente términos como _prompt_ e _ingeniería de prompt_? ¿Y cómo mejoro el _input_ del prompt que envío al LLM? Estas son las preguntas que trataremos de responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes del usuario. Lo logra usando _Modelos de Lenguaje Grandes_ como la serie GPT de OpenAI ("Transformador Generativo Preentrenado") entrenados para usar lenguaje natural y código.

Los usuarios ahora pueden interactuar con estos modelos usando paradigmas familiares como chat, sin necesidad de experiencia técnica ni entrenamiento. Los modelos son _basados en prompts_: los usuarios envían un texto de entrada (prompt) y reciben la respuesta de la IA (completado). Luego pueden "chatear con la IA" de forma iterativa, en conversaciones multivueltas, refinando su prompt hasta que la respuesta coincida con sus expectativas.

Los "prompts" se convierten ahora en la principal _interfaz de programación_ para apps de IA generativa, diciendo a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. La "Ingeniería de Prompt" es un campo de estudio en rápido crecimiento que se centra en el _diseño y optimización_ de prompts para entregar respuestas consistentes y de calidad a escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Prompt, por qué es importante y cómo podemos elaborar prompts más efectivos para un modelo y objetivo de aplicación dados. Entenderemos conceptos clave y mejores prácticas para la ingeniería de prompts, y conoceremos un entorno interactivo de cuadernos Jupyter "sandbox" donde podemos ver estos conceptos aplicados a ejemplos reales.

Al final de esta lección podremos:

1. Explicar qué es la ingeniería de prompt y por qué importa.
2. Describir los componentes de un prompt y cómo se usan.
3. Aprender mejores prácticas y técnicas para la ingeniería de prompt.
4. Aplicar técnicas aprendidas a ejemplos reales, usando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Prompt: La práctica de diseñar y refinar entradas para guiar a los modelos de IA hacia la producción de resultados deseados.
Tokenización: El proceso de convertir texto en unidades más pequeñas llamadas tokens que un modelo puede entender y procesar.
LLMs Ajustados con Instrucciones: Modelos de Lenguaje Grandes (LLMs) que han sido afinados con instrucciones específicas para mejorar la precisión y relevancia de sus respuestas.

## Sandbox de Aprendizaje

La ingeniería de prompt es actualmente más arte que ciencia. La mejor forma de mejorar nuestra intuición para ello es _practicar más_ y adoptar un enfoque de prueba y error que combine experiencia en el dominio de aplicación con técnicas recomendadas y optimizaciones específicas al modelo.

El Cuaderno Jupyter que acompaña esta lección proporciona un entorno _sandbox_ donde puedes probar lo que aprendes, ya sea sobre la marcha o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave API de Azure OpenAI**: el endpoint del servicio para un LLM desplegado.
2. **Un entorno de ejecución Python**: donde el Cuaderno pueda ser ejecutado.
3. **Variables de entorno locales**: _completa los pasos del [SETUP](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ahora para estar listo_.

El cuaderno viene con ejercicios _de inicio_, pero se te anima a añadir tus propias secciones de _Markdown_ (descripción) y _Código_ (solicitudes prompt) para probar más ejemplos o ideas y desarrollar tu intuición para el diseño de prompts.

## Guía Ilustrada

¿Quieres tener una visión general de lo que cubre esta lección antes de sumergirte? Revisa esta guía ilustrada, que te da una idea de los temas principales y las conclusiones clave para que consideres en cada uno. La hoja de ruta de la lección te lleva desde entender los conceptos y desafíos centrales hasta abordarlos con técnicas relevantes de ingeniería de prompt y mejores prácticas. Nota que la sección de "Técnicas Avanzadas" en esta guía se refiere al contenido cubierto en el _próximo_ capítulo de este currículo.

![Guía Ilustrada de Ingeniería de Prompt](../../../translated_images/es/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nuestra Startup

Ahora, hablemos de cómo _este tema_ se relaciona con la misión de nuestra startup de [llevar la innovación de IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicaciones impulsadas por IA de _aprendizaje personalizado_, así que pensemos en cómo diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedir a la IA que _analice datos del currículo para identificar brechas en la cobertura_. La IA puede resumir resultados o visualizarlos con código.
- **Educadores** podrían pedir a la IA que _genere un plan de lección para una audiencia y tema específicos_. La IA puede construir el plan personalizado en un formato especificado.
- **Estudiantes** podrían pedir a la IA que _los tutoree en una materia difícil_. La IA ahora puede guiar a los estudiantes con lecciones, pistas y ejemplos adaptados a su nivel.

Eso es solo la punta del iceberg. Revisa [Prompts For Education](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) — una biblioteca open-source de prompts curada por expertos en educación — para obtener una perspectiva más amplia de las posibilidades. _¡Prueba ejecutar algunos de esos prompts en el sandbox o usando el OpenAI Playground para ver qué sucede!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## ¿Qué es la Ingeniería de Prompt?

Comenzamos esta lección definiendo la **Ingeniería de Prompt** como el proceso de _diseñar y optimizar_ entradas de texto (prompts) para entregar respuestas consistentes y de calidad (completados) para un objetivo de aplicación y modelo dados. Podemos pensar en esto como un proceso de 2 pasos:

- _diseñar_ el prompt inicial para un modelo y objetivo dado
- _refinar_ el prompt de manera iterativa para mejorar la calidad de la respuesta

Este proceso es necesariamente de prueba y error que requiere intuición y esfuerzo del usuario para obtener resultados óptimos. ¿Entonces por qué es importante? Para responder esa pregunta, primero necesitamos entender tres conceptos:

- _Tokenización_ = cómo el modelo "ve" el prompt
- _Base LLMs_ = cómo el modelo base "procesa" un prompt
- _LLMs Ajustados con Instrucciones_ = cómo el modelo ahora puede "ver tareas"

### Tokenización

Un LLM ve los prompts como una _secuencia de tokens_ donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Dado que los LLMs se entrenan con tokens (y no con texto en crudo), la forma en que los prompts se tokenizan afecta directamente la calidad de la respuesta generada.

Para tener una intuición de cómo funciona la tokenización, prueba herramientas como el [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) que se muestra abajo. Copia tu prompt y observa cómo se convierte en tokens, prestando atención a cómo se manejan los caracteres de espacio y signos de puntuación. Nota que este ejemplo muestra un LLM más antiguo (GPT-3), así que probar esto con un modelo más nuevo puede producir un resultado diferente.

![Tokenización](../../../translated_images/es/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concepto: Modelos Fundamentales

Una vez que un prompt está tokenizado, la función principal del ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo fundamental) es predecir el token siguiente en esa secuencia. Dado que los LLMs se entrenan con conjuntos masivos de texto, tienen un buen sentido de las relaciones estadísticas entre tokens y pueden hacer esa predicción con cierta confianza. Nota que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su próxima predicción. Pueden seguir prediciendo la secuencia hasta que se termine por intervención del usuario o alguna condición preestablecida.

¿Quieres ver cómo funciona el completado basado en prompts? Ingresa el prompt anterior en el Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información, así que deberías ver un completado que satisface ese contexto.

Pero, ¿qué pasa si el usuario quiere ver algo específico que cumpla algunos criterios u objetivo de tarea? Aquí es donde los LLMs _ajustados con instrucciones_ entran en escena.

![Completado Chat Base LLM](../../../translated_images/es/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concepto: LLM Ajustados con Instrucciones

Un [LLM Ajustado con Instrucciones](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) comienza con el modelo fundamental y lo afina con ejemplos o pares de entrada/salida (por ejemplo, "mensajes" multivueltas) que pueden contener instrucciones claras, e intenta que la respuesta de la IA siga esa instrucción.

Esto utiliza técnicas como el Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo para _seguir instrucciones_ y _aprender de la retroalimentación_ para producir respuestas que se ajusten mejor a aplicaciones prácticas y sean más relevantes a los objetivos del usuario.

Vamos a probarlo: revisa el prompt anterior, pero ahora cambia el _mensaje del sistema_ para proporcionar la siguiente instrucción como contexto:

> _Resume el contenido que se te proporcione para un estudiante de segundo grado. Mantén el resultado en un párrafo con 3 a 5 puntos clave._

¿Ves cómo el resultado ahora está ajustado para reflejar el objetivo y formato deseados? Un educador puede usar directamente esta respuesta en sus diapositivas para esa clase.

![Completado Chat LLM Ajustado con Instrucciones](../../../translated_images/es/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## ¿Por qué necesitamos la Ingeniería de Prompt?

Ahora que sabemos cómo los LLMs procesan los prompts, hablemos de _por qué_ necesitamos ingeniería de prompt. La respuesta radica en que los LLMs actuales presentan una serie de desafíos que hacen que lograr _completados fiables y consistentes_ sea más difícil sin poner esfuerzo en la construcción y optimización del prompt. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ probablemente producirá respuestas diferentes con distintos modelos o versiones del modelo. E incluso puede producir resultados diferentes con el _mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de prompt pueden ayudarnos a minimizar estas variaciones proporcionando mejores límites de control_.

1. **Los modelos pueden fabricar respuestas.** Los modelos se pre-entrenan con conjuntos de datos _grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese ámbito de entrenamiento. Como resultado, pueden producir completados que son inexactos, imaginarios o directamente contradictorios con hechos conocidos. _Las técnicas de ingeniería de prompt ayudan a los usuarios a identificar y mitigar tales fabricaciones, por ejemplo, pidiendo a la IA citas o razonamientos_.

1. **Las capacidades de los modelos varían.** Modelos más nuevos o generaciones posteriores tendrán capacidades más ricas pero también traen peculiaridades y compensaciones únicas en costo y complejidad. _La ingeniería de prompt puede ayudarnos a desarrollar mejores prácticas y flujos de trabajo que abstraigan las diferencias y se adapten a requisitos específicos del modelo de manera escalable y fluida_.

Veamos esto en acción en el Playground de OpenAI o Azure OpenAI:

- Usa el mismo prompt con diferentes despliegues de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face) — ¿viste las variaciones?
- Usa el mismo prompt repetidamente con el _mismo_ despliegue de LLM (por ejemplo, playground de Azure OpenAI) — ¿cómo difirieron estas variaciones?

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno en que los LLMs a veces generan información factualmente incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También puedes haber oído este fenómeno llamado _"alucinaciones"_ en artículos populares o documentos de investigación. Sin embargo, recomendamos firmemente usar el término _"fabricación"_ para no antropomorfizar accidentalmente el comportamiento atribuyéndole una cualidad humana a un resultado generado por máquina. Esto también refuerza las [directrices de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde la perspectiva terminológica, eliminando términos que pueden considerarse ofensivos o no inclusivos en algunos contextos.

¿Quieres tener una idea de cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA generar contenido sobre un tema inexistente (para asegurarte de que no se encuentre en los datos de entrenamiento). Por ejemplo, intenté este prompt:

> **Prompt:** genera un plan de lección sobre la Guerra Marciana de 2076.
Una búsqueda en la web me mostró que existían relatos ficticios (por ejemplo, series de televisión o libros) sobre guerras en Marte, pero ninguno en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede asociarse con un evento real.

Entonces, ¿qué sucede cuando ejecutamos este prompt con diferentes proveedores de LLM?

> **Respuesta 1**: OpenAI Playground (GPT-35)

![Respuesta 1](../../../translated_images/es/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respuesta 2**: Azure OpenAI Playground (GPT-35)

![Respuesta 2](../../../translated_images/es/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respuesta 3**: : Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../../translated_images/es/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como era de esperar, cada modelo (o versión del modelo) produce respuestas ligeramente diferentes gracias al comportamiento estocástico y a las variaciones en la capacidad del modelo. Por ejemplo, un modelo está orientado a un público de 8º grado mientras que otro asume un estudiante de secundaria. Pero los tres modelos generaron respuestas que podrían convencer a un usuario no informado de que el evento fue real.

Las técnicas de ingeniería de prompts como el _metaprompting_ y la _configuración de temperatura_ pueden reducir las fabricaciones del modelo hasta cierto punto. Nuevas _arquitecturas_ de ingeniería de prompts también incorporan nuevas herramientas y técnicas de forma fluida en el flujo del prompt, para mitigar o reducir algunos de estos efectos.

## Estudio de Caso: GitHub Copilot

Terminemos esta sección con una idea de cómo se utiliza la ingeniería de prompts en soluciones del mundo real, viendo un Estudio de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "Programador en Pareja con IA": convierte texto en sugerencias de código y está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario fluida. Como se documenta en la serie de blogs a continuación, la versión inicial se basó en el modelo OpenAI Codex, con ingenieros que rápidamente se dieron cuenta de la necesidad de afinar el modelo y desarrollar mejores técnicas de ingeniería de prompts para mejorar la calidad del código. En julio, [presentaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para generar sugerencias aún más rápidas.

Lee las publicaciones en orden para seguir su camino de aprendizaje.

- **Mayo 2023** | [GitHub Copilot está mejorando en la comprensión de tu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: Trabajando con los LLM detrás de GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Junio 2023** | [Cómo escribir mejores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [.. GitHub Copilot va más allá de Codex con un modelo de IA mejorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Guía para desarrolladores sobre ingeniería de prompts y LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septiembre 2023** | [Cómo construir una aplicación LLM empresarial: lecciones de GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

También puedes explorar su [blog de Ingeniería](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que muestra cómo estos modelos y técnicas se _aplican_ para impulsar aplicaciones del mundo real.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Construcción de Prompts

Hemos visto por qué la ingeniería de prompts es importante, ahora entendamos cómo se _construyen_ los prompts para poder evaluar diferentes técnicas para un diseño de prompts más efectivo.

### Prompt Básico

Comencemos con el prompt básico: una entrada de texto enviada al modelo sin otro contexto. Aquí hay un ejemplo: cuando enviamos las primeras palabras del himno nacional de EE. UU. a la API de [Completado de OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) se _completa_ instantáneamente la respuesta con las siguientes líneas, ilustrando el comportamiento básico de predicción.

| Prompt (Entrada)   | Completado (Salida)                                                                                                                       |
| :----------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que estás comenzando la letra de "The Star-Spangled Banner", el himno nacional de Estados Unidos. La letra completa es ...       |

### Prompt Complejo

Ahora añadamos contexto e instrucciones a ese prompt básico. La [API de Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir un prompt complejo como una colección de _mensajes_ con:

- Pares de entrada/salida que reflejan la entrada del _usuario_ y la respuesta del _asistente_.
- Mensaje de sistema definiendo el contexto para el comportamiento o personalidad del asistente.

La solicitud ahora está en la siguiente forma, donde la _tokenización_ captura efectivamente la información relevante del contexto y la conversación. Cambiar el contexto del sistema puede ser tan impactante en la calidad de las respuestas como las entradas del usuario proporcionadas.

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

### Prompt de Instrucción

En los ejemplos anteriores, el prompt del usuario era una consulta de texto simple que puede interpretarse como una solicitud de información. Con los prompts de _instrucción_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando una mejor guía a la IA. Aquí un ejemplo:

| Prompt (Entrada)                                                                                                                                                                                                              | Completado (Salida)                                                                                                    | Tipo de Instrucción  |
| :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :------------------- |
| Escribe una descripción de la Guerra Civil                                                                                                                                                                                    | _devolvió un párrafo simple_                                                                                           | Simple               |
| Escribe una descripción de la Guerra Civil. Proporciona fechas clave y eventos y describe su relevancia                                                                                                                      | _devolvió un párrafo seguido de una lista con fechas clave y descripciones de eventos_                                   | Complejo             |
| Escribe una descripción de la Guerra Civil en 1 párrafo. Proporciona 3 puntos clave con fechas y su relevancia. Proporciona 3 puntos clave con figuras históricas y sus contribuciones. Devuelve el resultado en formato JSON. | _devuelve detalles más extensos en un cuadro de texto, formateados como JSON que puedes copiar y validar en un archivo_ | Complejo. Formateado. |

## Contenido Primario

En los ejemplos anteriores, el prompt seguía siendo bastante abierto, permitiendo que el LLM decidiera qué parte de su conjunto de datos pre-entrenado era relevante. Con el patrón de diseño de _contenido primario_, el texto de entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí un ejemplo donde la instrucción es "resume esto en 2 frases".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Completado (Salida)                                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. Lleva el nombre del dios romano Júpiter.[19] Cuando se observa desde la Tierra, Júpiter puede ser lo suficientemente brillante para que su luz reflejada proyecte sombras visibles,[20] y es en promedio el tercer objeto natural más brillante en el cielo nocturno después de la Luna y Venus. <br/> **Resume esto en 2 frases cortas** | Júpiter, el quinto planeta desde el Sol, es el más grande del Sistema Solar y es conocido por ser uno de los objetos más brillantes en el cielo nocturno. Nombrado en honor al dios romano Júpiter, es un gigante gaseoso cuya masa es dos veces y media la de todos los demás planetas del Sistema Solar juntos. |

El segmento de contenido primario puede usarse de varias maneras para impulsar instrucciones más efectivas:

- **Ejemplos** – en lugar de decirle al modelo qué hacer con una instrucción explícita, dale ejemplos de qué hacer y que infiera el patrón.
- **Señales (Cues)** – sigue la instrucción con una "señal" que prepare el completado, guiando al modelo hacia respuestas más relevantes.
- **Plantillas** – son 'recetas' repetibles para prompts con espacios reservados (variables) que pueden personalizarse con datos para casos específicos.

Exploremos estos en acción.

### Usando Ejemplos

Esta es una aproximación donde usas contenido primario para "alimentar al modelo" con algunos ejemplos del resultado deseado para una instrucción dada, y que infiera el patrón para el resultado que buscas. Según el número de ejemplos proporcionados, podemos tener promptings zero-shot, one-shot, few-shot, etc.

El prompt ahora consta de tres componentes:

- Una descripción de la tarea
- Algunos ejemplos del resultado deseado
- El inicio de un nuevo ejemplo (que se convierte en una descripción implícita de la tarea)

| Tipo de Aprendizaje | Prompt (Entrada)                                                                                          | Completado (Salida)         |
| :------------------ | :------------------------------------------------------------------------------------------------------ | :-------------------------- |
| Zero-shot           | "The Sun is Shining". Traduce al español                                                                | "El Sol está brillando".    |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                    | "Es un día frío y ventoso". |
| Few-shot            | El jugador corrió las bases => Béisbol <br/> El jugador hizo un as => Tenis <br/> El jugador hizo un seis => Cricket <br/> El jugador hizo un mate =>   | Baloncesto                  |
|                     |                                                                                                        |                             |

Observa cómo tuvimos que proporcionar una instrucción explícita ("Traduce al español") en el prompting zero-shot, pero esta se infiere en el ejemplo one-shot. El ejemplo few-shot muestra cómo agregar más ejemplos permite que los modelos hagan inferencias más precisas sin instrucciones adicionales.

### Señales (Cues) en el Prompt

Otra técnica para usar contenido primario es proporcionar _señales_ en lugar de ejemplos. En este caso, le damos al modelo un pequeño empujón en la dirección correcta al _empezar_ con un fragmento que refleja el formato de respuesta deseado. El modelo entonces "toma la señal" para continuar en ese sentido.

| Número de Señales | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                       | Completado (Salida)                                                                                                                                                                                                                                                                                       |
| :---------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                 | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto**                                               | Júpiter es el planeta más grande de nuestro Sistema Solar y el quinto desde el Sol. Es un gigante gaseoso con una masa 1/1000 de la del Sol, pero es más pesado que todos los otros planetas juntos. Las civilizaciones antiguas han conocido Júpiter durante mucho tiempo y es fácilmente visible en el cielo nocturno.. |
| 1              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por las antiguas civilizaciones desde antes de la historia registrada. <br/>**Resume Esto** <br/> Lo que aprendimos es que Júpiter | es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas combinados. Es fácilmente visible a simple vista y ha sido conocido desde la antigüedad.                        |
| 2              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por las antiguas civilizaciones desde antes de la historia registrada. <br/>**Resume Esto** <br/> Las 3 principales cosas que aprendimos:         | 1. Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. <br/> 2. Es un gigante gaseoso con una masa de una milésima parte de la del Sol...<br/> 3. Júpiter ha sido visible a simple vista desde la antigüedad ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Plantillas de Prompt

Una plantilla de prompt es una _receta predefinida para un prompt_ que puede almacenarse y reutilizarse según sea necesario, para generar experiencias de usuario más consistentes a gran escala. En su forma más simple, es simplemente una colección de ejemplos de prompts como [este de OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que proporciona tanto los componentes interactivos del prompt (mensajes de usuario y sistema) como el formato de la solicitud basada en API, para soportar la reutilización.

En su forma más compleja, como [este ejemplo de LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contiene _marcadores de posición_ que pueden reemplazarse con datos de diversas fuentes (entrada del usuario, contexto del sistema, fuentes de datos externas, etc.) para generar un prompt dinámicamente. Esto nos permite crear una biblioteca de prompts reutilizables que pueden usarse para generar experiencias de usuario coherentes **programáticamente** a gran escala.

Finalmente, el verdadero valor de las plantillas radica en la capacidad de crear y publicar _bibliotecas de prompts_ para dominios de aplicación verticales, donde la plantilla de prompt está ahora _optimizadda_ para reflejar el contexto o ejemplos específicos de la aplicación que hacen las respuestas más relevantes y precisas para la audiencia objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, que selecciona una biblioteca de prompts para el dominio educativo con énfasis en objetivos clave como la planificación de lecciones, diseño curricular, tutoría estudiantil, etc.

## Contenido de Apoyo

Si pensamos en la construcción de un prompt como tener una instrucción (tarea) y un objetivo (contenido principal), entonces el _contenido secundario_ es como un contexto adicional que proporcionamos para **influir en el resultado de alguna manera**. Podría ser parámetros de ajuste, instrucciones de formato, taxonomías temáticas, etc., que pueden ayudar al modelo a _adaptar_ su respuesta para ajustarse a los objetivos o expectativas del usuario deseados.

Por ejemplo: Dado un catálogo de cursos con metadata extensa (nombre, descripción, nivel, etiquetas de metadata, instructor, etc.) sobre todos los cursos disponibles en el currículo:

- podemos definir una instrucción para "resumir el catálogo de cursos para otoño 2023"
- podemos usar el contenido principal para proporcionar algunos ejemplos del resultado deseado
- podemos usar el contenido secundario para identificar las 5 principales "etiquetas" de interés.

Ahora, el modelo puede proporcionar un resumen en el formato mostrado por los pocos ejemplos, pero si un resultado tiene múltiples etiquetas, puede priorizar las 5 etiquetas identificadas en el contenido secundario.

---

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe cubrir el concepto principal #1.
Refuerce el concepto con ejemplos y referencias.

CONCEPTO #3:
Técnicas de Ingeniería de Prompts.
¿Cuáles son algunas técnicas básicas para ingeniería de prompts?
Ilústralo con algunos ejercicios.
-->

## Buenas Prácticas para Prompts

Ahora que sabemos cómo se pueden _construir_ los prompts, podemos comenzar a pensar en cómo _diseñarlos_ para reflejar las mejores prácticas. Podemos verlo en dos partes: tener la _mentalidad_ correcta y aplicar las _técnicas_ adecuadas.

### Mentalidad para Ingeniería de Prompts

La ingeniería de prompts es un proceso de prueba y error, así que ten en cuenta tres factores orientativos generales:

1. **Entender el Dominio es importante.** La precisión y relevancia de la respuesta dependen del _dominio_ en el que esa aplicación o usuario opera. Aplica tu intuición y experiencia en el dominio para **personalizar aún más las técnicas**. Por ejemplo, define _personalidades específicas del dominio_ en tus prompts del sistema, o usa _plantillas específicas del dominio_ en tus prompts de usuario. Proporciona contenido secundario que refleje contextos específicos del dominio, o usa _señales y ejemplos específicos del dominio_ para guiar al modelo hacia patrones de uso conocidos.

2. **Entender el Modelo es importante.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones del modelo también pueden variar en cuanto al conjunto de datos de entrenamiento que usan (conocimiento preentrenado), las capacidades que proporcionan (por ejemplo, vía API o SDK) y el tipo de contenido para el que están optimizados (por ejemplo, código vs. imágenes vs. texto). Comprende las fortalezas y limitaciones del modelo que estás usando, y usa ese conocimiento para _priorizar tareas_ o construir _plantillas personalizadas_ optimizadas para las capacidades del modelo.

3. **La Iteración y Validación son importantes.** Los modelos evolucionan rápidamente, y también las técnicas para ingeniería de prompts. Como experto en el dominio, puedes tener otro contexto o criterios para _tu_ aplicación específica, que puede que no apliquen a la comunidad en general. Usa herramientas y técnicas de ingeniería de prompts para "arrancar" la construcción, luego itera y valida los resultados usando tu propia intuición y experiencia. Registra tus conocimientos y crea una **base de conocimiento** (por ejemplo, bibliotecas de prompts) que otros puedan usar como referencia para iterar más rápido en el futuro.

## Mejores Prácticas

Ahora veamos algunas buenas prácticas comunes recomendadas por los practicantes de [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                                | Por qué                                                                                                                                                                                                                                             |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluar los modelos más nuevos.    | Nuevas generaciones de modelos suelen tener características y calidad mejoradas, pero también pueden implicar costos más altos. Evalúalos para medir impacto, luego toma decisiones de migración.                                                     |
| Separar instrucciones y contexto   | Verifica si tu modelo/proveedor define _delimitadores_ para distinguir claramente instrucciones, contenido primario y secundario. Esto ayuda a que los modelos asignen pesos a tokens más precisamente.                                             |
| Sé específico y claro              | Da más detalles sobre el contexto deseado, resultado, longitud, formato, estilo, etc. Esto mejorará la calidad y consistencia de las respuestas. Captura recetas en plantillas reutilizables.                                                     |
| Sé descriptivo, usa ejemplos       | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un enfoque de `zero-shot` donde das la instrucción pero sin ejemplos, luego prueba `few-shot` como refinamiento, proporcionando algunos ejemplos del resultado deseado. Usa analogías. |
| Usa señales para iniciar respuestas| Impúlsalo hacia el resultado deseado dándole algunas palabras o frases iniciales que puede usar como punto de partida para la respuesta.                                                                                                           |
| Reforzar                         | A veces puede ser necesario repetir las instrucciones al modelo. Da instrucciones antes y después del contenido principal, usa una instrucción y una señal, etc. Itera y valida para ver qué funciona.                                               |
| El orden importa                  | El orden en que presentas la información al modelo puede impactar el resultado, incluso en ejemplos de aprendizaje, debido al sesgo de recencia. Prueba diferentes opciones para ver cuál es la mejor.                                               |
| Dale al modelo una “salida”       | Dale al modelo una respuesta de _respaldo_ que pueda usar si no puede completar la tarea por cualquier motivo. Esto puede reducir la generación de respuestas falsas o fabricadas.                                                                |
|                                  |                                                                                                                                                                                                                                                     |

Como con cualquier buena práctica, recuerda que _tu experiencia puede variar_ según el modelo, la tarea y el dominio. Usa estas como punto de partida e itera para encontrar lo que mejor te funcione. Reevalúa constantemente tu proceso de ingeniería de prompts a medida que nuevos modelos y herramientas estén disponibles, con foco en la escalabilidad del proceso y calidad de las respuestas.

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe proporcionar un reto de código si es aplicable

RETO:
Enlaza un Jupyter Notebook con solo comentarios de código en las instrucciones (las secciones de código están vacías).

SOLUCIÓN:
Enlaza una copia de ese Notebook con los prompts llenados y ejecutados, mostrando un ejemplo de salida como referencia.
-->

## Tarea

¡Felicidades! ¡Llegaste al final de la lección! Es hora de poner a prueba algunos de esos conceptos y técnicas con ejemplos reales.

Para nuestra tarea, usaremos un Jupyter Notebook con ejercicios que puedes completar de forma interactiva. También puedes extender el Notebook con tus propias celdas Markdown y de código para explorar ideas y técnicas por tu cuenta.

### Para comenzar, haz un fork del repositorio, luego

- (Recomendado) Lanza GitHub Codespaces
- (Alternativamente) Clona el repo en tu dispositivo local y úsalo con Docker Desktop
- (Alternativamente) Abre el Notebook con tu entorno de ejecución preferido.

### Luego, configura tus variables de entorno

- Copia el archivo `.env.copy` en la raíz del repo a `.env` y rellena los valores `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT`. Regresa a la sección de [Learning Sandbox](#sandbox-de-aprendizaje) para aprender cómo.

### Después, abre el Jupyter Notebook

- Selecciona el kernel de ejecución. Si usas la opción 1 o 2, simplemente selecciona el kernel Python 3.10.x por defecto que proporciona el contenedor de desarrollo.

Ya estás listo para correr los ejercicios. Ten en cuenta que no hay respuestas _correctas o incorrectas_ aquí, solo exploración mediante prueba y error y construcción de intuición para lo que funciona con un modelo y dominio de aplicación dados.

_Por esta razón no hay segmentos de Solución de Código en esta lección. En cambio, el Notebook tendrá celdas Markdown tituladas "Mi Solución:" que muestran un ejemplo de salida como referencia._

 <!--
PLANTILLA DE LECCIÓN:
Cierra la sección con un resumen y recursos para aprendizaje autodidacta.
-->

## Chequeo de Conocimientos

¿Cuál de los siguientes es un buen prompt siguiendo prácticas razonables?

1. Muéstrame una imagen de un coche rojo
2. Muéstrame una imagen de un coche rojo marca Volvo y modelo XC90 estacionado junto a un acantilado con el sol poniéndose
3. Muéstrame una imagen de un coche rojo marca Volvo y modelo XC90

R: 2, es el mejor prompt porque da detalles del "qué" y específico (no cualquier coche sino marca y modelo concretos) y también describe el escenario general. 3 es el siguiente mejor pues también contiene mucha descripción.

## 🚀 Reto

Intenta aprovechar la técnica de “señal” con el prompt: Completa la frase "Muéstrame una imagen de un coche rojo de marca Volvo y ". ¿Con qué responde? ¿Cómo la mejorarías?

## ¡Gran Trabajo! Continúa Tu Aprendizaje

¿Quieres aprender más sobre conceptos de Ingeniería de Prompts? Visita la [página de aprendizaje continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar más recursos excelentes sobre este tema.

¡Dirígete a la Lección 5 donde exploraremos [técnicas avanzadas de prompts](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->