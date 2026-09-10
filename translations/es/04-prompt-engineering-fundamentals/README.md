# Fundamentos de la Ingeniería de Prompts

[![Fundamentos de la Ingeniería de Prompts](../../../translated_images/es/04-lesson-banner.a2c90deba7fedacd.webp)](https://youtu.be/GElCu2kUlRs?si=qrXsBvXnCW12epb8)

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear prompts efectivos en modelos de IA generativa. La forma en que escribes tu prompt para un LLM también importa. Un prompt cuidadosamente elaborado puede lograr una mejor calidad de respuesta. Pero ¿qué significan exactamente términos como _prompt_ e _ingeniería de prompts_? ¿Y cómo mejoro el _input_ del prompt que envío al LLM? Estas son las preguntas que intentaremos responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes del usuario. Lo logra usando _Modelos de Lenguaje Grande_ como la serie GPT de OpenAI ("Transformador Generativo Preentrenado") que están entrenados para usar lenguaje natural y código.

Los usuarios ahora pueden interactuar con estos modelos usando paradigmas familiares como el chat, sin necesidad de conocimientos técnicos o entrenamiento. Los modelos son _basados en prompts_: los usuarios envían un texto (prompt) y reciben la respuesta de la IA (completado). Luego pueden "chatear con la IA" iterativamente, en conversaciones de varios turnos, refinando su prompt hasta que la respuesta coincida con sus expectativas.

Los "prompts" se convierten ahora en la principal _interfaz de programación_ para aplicaciones de IA generativa, indicándoles a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. La "Ingeniería de Prompts" es un campo de estudio en rápido crecimiento que se enfoca en el _diseño y optimización_ de prompts para entregar respuestas consistentes y de calidad a escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Prompts, por qué es importante y cómo podemos crear prompts más efectivos para un modelo y objetivo de aplicación dados. Entenderemos conceptos clave y buenas prácticas para la ingeniería de prompts, y conoceremos un entorno interactivo tipo Jupyter Notebooks "sandbox" donde podemos ver estos conceptos aplicados a ejemplos reales.

Al final de esta lección podremos:

1. Explicar qué es la ingeniería de prompts y por qué es importante.
2. Describir los componentes de un prompt y cómo se usan.
3. Aprender buenas prácticas y técnicas para la ingeniería de prompts.
4. Aplicar las técnicas aprendidas a ejemplos reales, usando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Prompts: La práctica de diseñar y refinar entradas para guiar a los modelos de IA hacia la producción de salidas deseadas.
Tokenización: El proceso de convertir texto en unidades más pequeñas, llamadas tokens, que un modelo pueda entender y procesar.
LLMs Ajustados por Instrucción: Modelos de Lenguaje Grande que han sido ajustados con instrucciones específicas para mejorar su precisión y relevancia en las respuestas.

## Sandbox de Aprendizaje

La ingeniería de prompts actualmente es más arte que ciencia. La mejor manera de mejorar nuestra intuición es _practicar más_ y adoptar un enfoque de prueba y error que combine experiencia en el dominio de la aplicación con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña esta lección brinda un entorno _sandbox_ donde puedes probar lo que aprendes, ya sea en el momento o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave API de Azure OpenAI** - el endpoint de servicio para un LLM desplegado.
2. **Un entorno de Python Runtime** - en el que se pueda ejecutar el Notebook.
3. **Variables de Entorno Locales** - _completa los pasos de [CONFIGURACIÓN](./../00-course-setup/02-setup-local.md?WT.mc_id=academic-105485-koreyst) ahora para estar listo_.

El notebook incluye ejercicios _iniciales_, pero se recomienda agregar tus propias secciones de _Markdown_ (descripción) y _Código_ (peticiones de prompts) para probar más ejemplos o ideas y construir tu intuición en el diseño de prompts.

## Guía Ilustrada

¿Quieres tener una visión general de lo que cubre esta lección antes de profundizar? Revisa esta guía ilustrada, que te presenta los temas principales y los puntos clave que deberías considerar en cada uno. La hoja de ruta de la lección te lleva desde entender los conceptos y desafíos fundamentales hasta abordarlos con técnicas relevantes de ingeniería de prompts y buenas prácticas. Nota que la sección "Técnicas Avanzadas" en esta guía se refiere a contenido cubierto en el _próximo_ capítulo del currículo.

![Guía Ilustrada de Ingeniería de Prompts](../../../translated_images/es/04-prompt-engineering-sketchnote.d5f33336957a1e4f.webp)

## Nuestra Startup

Ahora, hablemos de cómo _este tema_ se relaciona con la misión de nuestra startup de [llevar innovación en IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos crear aplicaciones con IA para _aprendizaje personalizado_, así que pensemos en cómo diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedir a la IA que _analice datos curriculares para identificar vacíos en la cobertura_. La IA puede resumir resultados o visualizarlos con código.
- **Educadores** podrían pedir a la IA que _genere un plan de lección para una audiencia objetivo y tema específico_. La IA puede construir el plan personalizado en un formato especificado.
- **Estudiantes** podrían pedir a la IA que _los tutorice en una materia difícil_. La IA puede ahora guiar a los estudiantes con lecciones, pistas y ejemplos adaptados a su nivel.

Eso es solo la punta del iceberg. Revisa [Prompts Para Educación](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst), una biblioteca de prompts de código abierto curada por expertos en educación, para tener una idea más amplia de las posibilidades. _¡Prueba ejecutar algunos de esos prompts en el sandbox o usando el OpenAI Playground para ver qué ocurre!_

<!--
PLANTILLA DE LA LECCIÓN:
Esta unidad debería cubrir el concepto central #1.
Reforzar el concepto con ejemplos y referencias.

CONCEPTO #1:
Ingeniería de Prompts.
Definirlo y explicar por qué es necesario.
-->

## ¿Qué es la Ingeniería de Prompts?

Empezamos esta lección definiendo la **Ingeniería de Prompts** como el proceso de _diseñar y optimizar_ entradas de texto (prompts) para entregar respuestas (completados) consistentes y de calidad para un objetivo de aplicación y modelo dados. Podemos pensar en esto como un proceso en 2 pasos:

- _diseñar_ el prompt inicial para un modelo y objetivo dados
- _refinar_ el prompt iterativamente para mejorar la calidad de la respuesta

Esto es necesariamente un proceso de prueba y error que requiere intuición y esfuerzo del usuario para obtener resultados óptimos. Entonces, ¿por qué es importante? Para responder a esa pregunta, primero necesitamos entender tres conceptos:

- _Tokenización_ = cómo el modelo "ve" el prompt
- _LLMs Base_ = cómo el modelo base "procesa" un prompt
- _LLMs Ajustados por Instrucción_ = cómo el modelo ahora puede ver "tareas"

### Tokenización

Un LLM ve los prompts como una _secuencia de tokens_, donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Puesto que los LLM están entrenados en tokens (y no en texto sin procesar), la forma en que los prompts se tokenizan impacta directamente en la calidad de la respuesta generada.

Para tener una intuición de cómo funciona la tokenización, prueba herramientas como el [Tokenizador de OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) mostrado abajo. Copia tu prompt y observa cómo se convierte en tokens, prestando atención a cómo se manejan los espacios en blanco y signos de puntuación. Nota que este ejemplo muestra un LLM más antiguo (GPT-3), así que probar con un modelo más nuevo puede producir un resultado diferente.

![Tokenización](../../../translated_images/es/04-tokenizer-example.e71f0a0f70356c5c.webp)

### Concepto: Modelos Foundation

Una vez tokenizado un prompt, la función principal del ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo Foundation) es predecir el token en esa secuencia. Puesto que los LLM están entrenados con grandes datasets de texto, tienen un buen sentido de las relaciones estadísticas entre tokens y pueden hacer esa predicción con cierta confianza. Nota que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su siguiente predicción. Pueden continuar prediciendo la secuencia hasta que el usuario la detenga o se cumpla alguna condición preestablecida.

¿Quieres ver cómo funciona el completado basado en prompts? Introduce el prompt anterior en el [playground de Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información, por lo que deberías ver un completado que satisfaga ese contexto.

Pero, ¿qué pasa si el usuario quiere ver algo específico que cumpla ciertos criterios o un objetivo de tarea? Aquí es donde entran los LLMs _ajustados por instrucción_.

![Chat de completado con LLM Base](../../../translated_images/es/04-playground-chat-base.65b76fcfde0caa67.webp)

### Concepto: LLMs Ajustados por Instrucción

Un [LLM Ajustado por Instrucción](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte del modelo foundation y lo ajusta con ejemplos o pares entrada/salida (por ejemplo, "mensajes" de varios turnos) que pueden contener instrucciones claras, y la respuesta de la IA intenta seguir esa instrucción.

Esto utiliza técnicas como Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo para _seguir instrucciones_ y _aprender de retroalimentación_ de modo que produzca respuestas mejor adaptadas a aplicaciones prácticas y más relevantes para los objetivos del usuario.

Probémoslo: revisa el prompt anterior, pero ahora cambia el _mensaje del sistema_ para proporcionar la siguiente instrucción como contexto:

> _Resume el contenido que te proporcionen para un estudiante de segundo grado. Mantén el resultado en un párrafo con 3-5 viñetas._

¿Ves cómo el resultado ahora está ajustado para reflejar el objetivo y formato deseado? Un educador puede usar directamente esta respuesta en sus diapositivas para esa clase.

![Chat de completado con LLM Ajustado por Instrucción](../../../translated_images/es/04-playground-chat-instructions.b30bbfbdf92f2d05.webp)

## ¿Por qué necesitamos la Ingeniería de Prompts?

Ahora que sabemos cómo los LLM procesan los prompts, hablemos de _por qué_ necesitamos la ingeniería de prompts. La respuesta radica en que los LLM actuales presentan varios desafíos que hacen que lograr _completados confiables y consistentes_ sea más difícil sin poner esfuerzo en la construcción y optimización del prompt. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ probablemente producirá respuestas diferentes con modelos o versiones distintas. E incluso puede producir resultados distintos con _el mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de prompts nos ayudan a minimizar estas variaciones proporcionando mejores límites de control_.

1. **Los modelos pueden fabricar respuestas.** Los modelos están preentrenados con datasets _grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese ámbito de entrenamiento. Como resultado, pueden producir completados que son inexactos, imaginarios o directamente contradictorios a hechos conocidos. _Las técnicas de ingeniería de prompts ayudan a los usuarios a identificar y mitigar tales fabricaciones, por ejemplo, pidiendo a la IA citas o razonamientos_.

1. **Las capacidades de los modelos varían.** Los modelos más nuevos o nuevas generaciones traerán capacidades más ricas pero también peculiaridades y compensaciones únicas en costo y complejidad. _La ingeniería de prompts puede ayudarnos a desarrollar buenas prácticas y flujos de trabajo que abstraigan diferencias y se adapten a requisitos específicos del modelo de manera escalable y fluida_.

Veamos esto en acción en OpenAI o en el Playground de Azure OpenAI:

- Usa el mismo prompt con diferentes despliegues de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face) - ¿viste las variaciones?
- Usa el mismo prompt repetidamente con el _mismo_ despliegue de LLM (por ejemplo, playground de Azure OpenAI) - ¿cómo difirieron estas variaciones?

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno donde los LLM a veces generan información factualmente incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También podrías haber escuchado esto referido como _"alucinaciones"_ en artículos populares o investigaciones. Sin embargo, recomendamos usar _"fabricación"_ para no antropomorfizar accidentalmente el comportamiento, atribuyendo un rasgo humano a un resultado generado por una máquina. Esto también refuerza las [directrices de IA responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde la perspectiva terminológica, eliminando términos que también pueden ser considerados ofensivos o no inclusivos en algunos contextos.

¿Quieres entender cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA a generar contenido sobre un tema inexistente (para asegurar que no esté en el dataset de entrenamiento). Por ejemplo, probé este prompt:

> **Prompt:** genera un plan de lección sobre la Guerra Marciana de 2076.

Una búsqueda en la web me mostró que hay relatos de ficción (por ejemplo, series de televisión o libros) sobre guerras marcianas, pero ninguno en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede asociarse con un evento real.


¿Qué sucede cuando ejecutamos este prompt con diferentes proveedores de LLM?

> **Respuesta 1**: OpenAI Playground (GPT-35)

![Respuesta 1](../../../translated_images/es/04-fabrication-oai.5818c4e0b2a2678c.webp)

> **Respuesta 2**: Azure OpenAI Playground (GPT-35)

![Respuesta 2](../../../translated_images/es/04-fabrication-aoai.b14268e9ecf25caf.webp)

> **Respuesta 3**: : Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../../translated_images/es/04-fabrication-huggingchat.faf82a0a51278956.webp)

Como se esperaba, cada modelo (o versión del modelo) produce respuestas ligeramente diferentes gracias al comportamiento estocástico y a las variaciones en la capacidad del modelo. Por ejemplo, un modelo se dirige a una audiencia de octavo grado mientras que otro asume un estudiante de secundaria. Pero los tres modelos generaron respuestas que podrían convencer a un usuario no informado de que el evento fue real.

Técnicas de ingeniería de prompts como el _metaprompting_ y la _configuración de la temperatura_ pueden reducir las fabricaciones del modelo hasta cierto punto. Nuevas _arquitecturas_ de ingeniería de prompts también incorporan nuevas herramientas y técnicas sin problemas en el flujo de prompts para mitigar o reducir algunos de estos efectos.

## Estudio de caso: GitHub Copilot

Cerremos esta sección con una idea de cómo se utiliza la ingeniería de prompts en soluciones del mundo real viendo un estudio de caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "Programador en pareja con IA": convierte prompts de texto en completaciones de código e está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario fluida. Como se documenta en la serie de blogs abajo, la primera versión se basaba en el modelo OpenAI Codex, con ingenieros que rápidamente se dieron cuenta de la necesidad de afinar el modelo y desarrollar mejores técnicas de ingeniería de prompts para mejorar la calidad del código. En julio, [presentaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugerencias aún más rápidas.

Lee las publicaciones en orden para seguir su proceso de aprendizaje.

- **Mayo 2023** | [GitHub Copilot mejora en la comprensión de tu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: Trabajando con los LLM detrás de GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junio 2023** | [Cómo escribir mejores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julio 2023** | [.. GitHub Copilot va más allá de Codex con un modelo de IA mejorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Guía para desarrolladores sobre ingeniería de prompts y LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septiembre 2023** | [Cómo construir una app empresarial con LLM: Lecciones desde GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

También puedes explorar su [blog de Ingeniería](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que muestra cómo estos modelos y técnicas se _aplican_ para impulsar aplicaciones del mundo real.

---

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debería cubrir el concepto principal #2.
Reforzar el concepto con ejemplos y referencias.

CONCEPTO #2:
Diseño de Prompts.
Ilustrado con ejemplos.
-->

## Construcción de Prompts

Hemos visto por qué la ingeniería de prompts es importante; ahora vamos a entender cómo se _construyen_ los prompts para poder evaluar diferentes técnicas para un diseño más efectivo de prompts.

### Prompt Básico

Empecemos con el prompt básico: una entrada de texto enviada al modelo sin otro contexto. Aquí hay un ejemplo: cuando enviamos las primeras palabras del himno nacional de EE.UU. a la [API de completado](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) de OpenAI, inmediatamente _completa_ la respuesta con las siguientes líneas, ilustrando el comportamiento básico de predicción.

| Prompt (Entrada)    | Completado (Salida)                                                                                                                        |
| :----------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see | Parece que estás comenzando la letra de "The Star-Spangled Banner", el himno nacional de los Estados Unidos. La letra completa es ...        |

### Prompt Complejo

Ahora añadamos contexto e instrucciones a ese prompt básico. La [API de Chat completions](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir un prompt complejo como una colección de _mensajes_ con:

- Pares de entrada/salida que reflejan la entrada del _usuario_ y la respuesta del _asistente_.
- Mensaje del sistema estableciendo el contexto para el comportamiento o personalidad del asistente.

La solicitud ahora tiene la forma siguiente, donde la _tokenización_ captura efectivamente información relevante del contexto y la conversación. Ahora, cambiar el contexto del sistema puede ser tan impactante en la calidad de las completaciones como las entradas proporcionadas por el usuario.

```python
response = client.responses.create(
    model="gpt-5-mini",
    input=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)
```

### Prompt de Instrucción

En los ejemplos anteriores, el prompt del usuario era una simple consulta de texto que puede interpretarse como una solicitud de información. Con prompts de _instrucción_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando mejor orientación a la IA. Aquí hay un ejemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Completado (Salida)                                                                                                        | Tipo de Instrucción |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escribe una descripción de la Guerra Civil                                                                                                                                                                                               | _devuelve un párrafo simple_                                                                                               | Simple              |
| Escribe una descripción de la Guerra Civil. Proporciona fechas clave y eventos y describe su importancia                                                                                                                                 | _devuelve un párrafo seguido de una lista de fechas clave con descripciones_                                              | Complejo            |
| Escribe una descripción de la Guerra Civil en 1 párrafo. Proporciona 3 viñetas con fechas clave y su importancia. Proporciona 3 viñetas adicionales con figuras históricas clave y sus contribuciones. Devuelve el resultado en un archivo JSON | _devuelve detalles más extensos en un cuadro de texto, formateados como JSON que puedes copiar y pegar a un archivo y validar según sea necesario_ | Complejo. Formateado. |

## Contenido Primario

En los ejemplos anteriores, el prompt todavía era bastante abierto, permitiendo que el LLM decida qué parte de su conjunto de datos preentrenado era relevante. Con el patrón de diseño de _contenido primario_, el texto de entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí hay un ejemplo donde la instrucción es "resume esto en 2 oraciones".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Completado (Salida)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del Sol, pero dos veces y media la de todos los otros planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. Lleva el nombre del dios romano Júpiter.[19] Cuando se ve desde la Tierra, Júpiter puede ser lo suficientemente brillante para que su luz reflejada proyecte sombras visibles,[20] y es en promedio el tercer objeto natural más brillante en el cielo nocturno después de la Luna y Venus. <br/> **Resume esto en 2 oraciones cortas** | Júpiter, el quinto planeta desde el Sol, es el más grande del Sistema Solar y es conocido por ser uno de los objetos más brillantes en el cielo nocturno. Llamado así por el dios romano Júpiter, es un gigante gaseoso cuya masa es dos veces y media la de todos los otros planetas del Sistema Solar juntos. |

El segmento de contenido primario puede usarse de varias maneras para impulsar instrucciones más efectivas:

- **Ejemplos** - en lugar de decirle al modelo qué hacer con una instrucción explícita, dale ejemplos de qué hacer y deja que infiera el patrón.
- **Señales** - sigue la instrucción con una "señal" que prepara la completación, guiando al modelo hacia respuestas más relevantes.
- **Plantillas** - estas son 'recetas' repetibles para prompts con marcadores de posición (variables) que pueden personalizarse con datos para casos de uso específicos.

Exploremos esto en acción.

### Uso de Ejemplos

Esta es una aproximación donde usas el contenido primario para "alimentar al modelo" con algunos ejemplos del resultado deseado para una instrucción dada, y dejar que infiera el patrón para el resultado deseado. Según el número de ejemplos proporcionados, podemos tener prompting zero-shot, one-shot, few-shot, etc.

El prompt ahora consiste en tres componentes:

- Una descripción de la tarea
- Algunos ejemplos del resultado deseado
- El inicio de un nuevo ejemplo (que se convierte en una descripción implícita de la tarea)

| Tipo de Aprendizaje | Prompt (Entrada)                                                                                                                                        | Completado (Salida)        |
| :------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot           | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot            | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot            | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|                     |                                                                                                                                                       |                            |

Nota cómo tuvimos que proporcionar una instrucción explícita ("Translate to Spanish") en prompting zero-shot, pero se infiere en el ejemplo one-shot. El ejemplo few-shot muestra cómo añadir más ejemplos permite a los modelos hacer inferencias más precisas sin instrucciones adicionales.

### Señales en Prompt

Otra técnica para usar contenido primario es proporcionar _señales_ en lugar de ejemplos. En este caso, damos al modelo un empujón en la dirección correcta empezando con un fragmento que refleja el formato de respuesta deseado. El modelo entonces "toma la señal" para continuar en esa línea.

| Número de Señales | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Completado (Salida)                                                                                                                                                                                                                                                                                       |
| :---------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0                 | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del Sol, pero dos veces y media la de todos los otros planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto**                                         | Júpiter es el planeta más grande de nuestro Sistema Solar y el quinto desde el Sol. Es un gigante gaseoso con una masa de 1/1000 de la del Sol, pero es más pesado que todos los otros planetas combinados. Las civilizaciones antiguas conocen a Júpiter desde hace mucho tiempo, y es fácilmente visible en el cielo nocturno. |
| 1                 | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del Sol, pero dos veces y media la de todos los otros planetas del Sistema Solar juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto** <br/> Lo que aprendimos es que Júpiter | es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del Sol, pero dos veces y media la de todos los otros planetas combinados. Es fácilmente visible a simple vista y es conocido desde tiempos antiguos.                      |

| 2              | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte de la del Sol, pero dos veces y media la de todos los demás planetas del Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por civilizaciones antiguas desde antes de la historia registrada. <br/>**Resumen** <br/> Las 3 principales cosas que aprendimos:         | 1. Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. <br/> 2. Es un gigante gaseoso con una masa de una milésima parte de la del Sol...<br/> 3. Júpiter ha sido visible a simple vista desde tiempos antiguos ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |

### Plantillas de Prompt

Una plantilla de prompt es una _receta predefinida para un prompt_ que puede almacenarse y reutilizarse según sea necesario, para impulsar experiencias de usuario más consistentes a gran escala. En su forma más simple, es simplemente una colección de ejemplos de prompt como [este de OpenAI](https://cookbook.openai.com/examples/gpt4-1_prompting_guide?WT.mc_id=academic-105485-koreyst) que proporciona tanto los componentes interactivos del prompt (mensajes del usuario y sistema) como el formato de solicitud impulsado por API - para soportar la reutilización.

En su forma más compleja, como [este ejemplo de LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), contiene _marcadores de posición_ que pueden ser reemplazados con datos de diversas fuentes (entrada del usuario, contexto del sistema, fuentes de datos externas, etc.) para generar un prompt dinámicamente. Esto nos permite crear una biblioteca de prompts reutilizables que pueden usarse para impulsar experiencias de usuario consistentes **programáticamente** a gran escala.

Finalmente, el valor real de las plantillas reside en la capacidad de crear y publicar _bibliotecas de prompts_ para dominios de aplicación verticales, donde la plantilla de prompt ahora está _optimizida_ para reflejar el contexto o ejemplos específicos de la aplicación que hacen que las respuestas sean más relevantes y precisas para el público usuario objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, curando una biblioteca de prompts para el dominio educativo con énfasis en objetivos clave como planificación de lecciones, diseño curricular, tutoría estudiantil, etc.

## Contenido de Apoyo

Si pensamos en la construcción de prompts como tener una instrucción (tarea) y un objetivo (contenido principal), entonces el _contenido secundario_ es como contexto adicional que proporcionamos para **influir en la salida de alguna manera**. Puede ser parámetros de ajuste, instrucciones de formato, taxonomías temáticas, etc., que pueden ayudar al modelo a _personalizar_ su respuesta para que se ajuste a los objetivos o expectativas del usuario deseados.

Por ejemplo: Dado un catálogo de cursos con metadatos extensos (nombre, descripción, nivel, etiquetas de metadatos, instructor, etc.) de todos los cursos disponibles en el plan de estudios:

- podemos definir una instrucción para "resumir el catálogo de cursos para el Otoño 2023"
- podemos usar el contenido principal para proporcionar algunos ejemplos de la salida deseada
- podemos usar el contenido secundario para identificar las 5 principales "etiquetas" de interés.

Ahora, el modelo puede proporcionar un resumen en el formato mostrado por los pocos ejemplos, pero si un resultado tiene múltiples etiquetas, puede priorizar las 5 etiquetas identificadas en el contenido secundario.

---

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe cubrir el concepto central #1.
Reforzar el concepto con ejemplos y referencias.

CONCEPTO #3:
Técnicas de Ingeniería de Prompts.
¿Cuáles son algunas técnicas básicas para ingeniería de prompts?
Ilústralo con algunos ejercicios.
-->

## Mejores Prácticas para Prompts

Ahora que sabemos cómo se pueden _construir_ los prompts, podemos empezar a pensar en cómo _diseñarlos_ para reflejar las mejores prácticas. Podemos pensar en esto en dos partes: tener la _mentalidad_ correcta y aplicar las _técnicas_ adecuadas.

### Mentalidad para Ingeniería de Prompts

La ingeniería de prompts es un proceso de prueba y error, así que ten en cuenta tres factores guía generales:

1. **Entender el dominio importa.** La precisión y relevancia de la respuesta es función del _dominio_ en el que opera esa aplicación o usuario. Aplica tu intuición y experiencia en el dominio para **personalizar aún más las técnicas**. Por ejemplo, define _personalidades específicas del dominio_ en tus prompts de sistema o usa _plantillas específicas del dominio_ en tus prompts de usuario. Proporciona contenido secundario que refleje contextos específicos del dominio, o usa _señales y ejemplos específicos del dominio_ para guiar al modelo hacia patrones de uso familiares.

2. **Entender el modelo importa.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones de modelo también pueden variar en términos del conjunto de datos de entrenamiento que usan (conocimiento preentrenado), las capacidades que proporcionan (e.g., vía API o SDK) y el tipo de contenido para el que están optimizados (e.g., código vs imágenes vs texto). Entiende las fortalezas y limitaciones del modelo que estás usando y usa ese conocimiento para _priorizar tareas_ o crear _plantillas personalizadas_ optimizadas para las capacidades del modelo.

3. **Iterar y validar importa.** Los modelos están evolucionando rápidamente, y también las técnicas para ingeniería de prompts. Como experto en el dominio, puedes tener otro contexto o criterios para _tu_ aplicación específica, que tal vez no aplican para la comunidad general. Usa herramientas y técnicas de ingeniería de prompts para "activar" la construcción de prompts, luego itera y valida los resultados usando tu propia intuición y experiencia en el dominio. Registra tus aprendizajes y crea una **base de conocimiento** (e.g., bibliotecas de prompts) que puedan ser usados como nueva línea base por otros para iteraciones más rápidas en el futuro.

## Mejores Prácticas

Ahora veamos las mejores prácticas comunes que recomiendan los practicantes de [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-foundry/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                              | Por qué                                                                                                                                                                                                                                              |
| :-------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluar los modelos más recientes.       | Las nuevas generaciones de modelos probablemente tengan características y calidad mejoradas, pero también pueden implicar costos más altos. Evalúalos por su impacto, luego toma decisiones de migración.                                               |
| Separar instrucciones y contexto   | Verifica si tu modelo/proveedor define _delimitadores_ para distinguir instrucciones, contenido principal y secundario más claramente. Esto puede ayudar a los modelos a asignar pesos más precisos a los tokens.                                       |
| Ser específico y claro             | Proporciona más detalles sobre el contexto deseado, resultado, longitud, formato, estilo, etc. Esto mejorará tanto la calidad como la consistencia de las respuestas. Captura recetas en plantillas reutilizables.                                     |
| Ser descriptivo, usar ejemplos      | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un enfoque de `zero-shot` donde das una instrucción (pero sin ejemplos), luego prueba `few-shot` como refinamiento, proporcionando algunos ejemplos de la salida deseada. Usa analogías. |
| Usar señales para iniciar completaciones | Guíalo hacia un resultado deseado dándole algunas palabras o frases iniciales que pueda usar como punto de partida para la respuesta.                                                                                                            |
| Repetir                         | A veces puede ser necesario repetir la instrucción al modelo. Da instrucciones antes y después de tu contenido principal, usa una instrucción y una señal, etc. Itera y valida para ver qué funciona.                                              |
| El orden importa                     | El orden en que presentas la información al modelo puede impactar la salida, incluso en los ejemplos de aprendizaje, gracias al sesgo de recencia. Prueba opciones diferentes para ver qué funciona mejor.                                         |
| Darle al modelo una “salida”           | Dale al modelo una respuesta de _respaldo_ que pueda proporcionar si no puede completar la tarea por cualquier motivo. Esto puede reducir las probabilidades de que los modelos generen respuestas falsas o fabricadas.                             |
|                                   |                                                                                                                                                                                                                                                   |

Como con cualquier mejor práctica, recuerda que _tu experiencia puede variar_ según el modelo, la tarea y el dominio. Usa estas como punto de partida y itera para encontrar lo que mejor funciona para ti. Reevalúa constantemente tu proceso de ingeniería de prompts conforme se disponen nuevos modelos y herramientas, con enfoque en la escalabilidad del proceso y calidad de la respuesta.

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe proporcionar un desafío de codificación si procede

DESAFÍO:
Enlace a un cuaderno Jupyter con solo los comentarios de código en las instrucciones (las secciones de código están vacías).

SOLUCIÓN:
Enlace a una copia de ese cuaderno con los prompts completados y ejecutados, mostrando lo que podría ser un ejemplo.
-->

## Tarea

¡Felicidades! ¡Has llegado al final de la lección! ¡Es momento de poner a prueba algunos de esos conceptos y técnicas con ejemplos reales!

Para nuestra tarea, usaremos un cuaderno Jupyter con ejercicios que puedes completar de forma interactiva. También puedes extender el cuaderno con tus propias celdas de Markdown y código para explorar ideas y técnicas por tu cuenta.

### Para comenzar, bifurca el repositorio, luego

- (Recomendado) Lanza GitHub Codespaces
- (Alternativamente) Clona el repositorio en tu dispositivo local y úsalo con Docker Desktop
- (Alternativamente) Abre el cuaderno con tu entorno preferido para ejecutar cuadernos.

### Después, configura tus variables de entorno

- Copia el archivo `.env.copy` que está en la raíz del repositorio a `.env` y completa los valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT`. Regresa a la [sección de Learning Sandbox](#sandbox-de-aprendizaje) para aprender cómo hacerlo.

### Luego, abre el cuaderno Jupyter

- Selecciona el kernel de ejecución. Si usas la opción 1 o 2, simplemente selecciona el kernel por defecto Python 3.10.x que provee el contenedor de desarrollo.

Ya estás listo para correr los ejercicios. Nota que aquí no hay respuestas _correctas o incorrectas_ – es solo explorar opciones mediante prueba y error y construir intuición sobre qué funciona para un modelo y dominio de aplicación dado.

_Por esta razón no hay segmentos de Solución de Código en esta lección. En cambio, el cuaderno tendrá celdas de Markdown tituladas "Mi solución:" que muestran un ejemplo de salida para referencia._

 <!--
PLANTILLA DE LECCIÓN:
Cierra la sección con un resumen y recursos para aprendizaje autodirigido.
-->

## Verificación de conocimiento

¿Cuál de los siguientes es un buen prompt siguiendo algunas prácticas recomendables razonables?

1. Muéstrame una imagen de un coche rojo
2. Muéstrame una imagen de un coche rojo de marca Volvo y modelo XC90 estacionado junto a un acantilado con el sol poniéndose
3. Muéstrame una imagen de un coche rojo de marca Volvo y modelo XC90

A: 2, es el mejor prompt porque proporciona detalles sobre "qué" y entra en específicos (no cualquier coche sino una marca y modelo específicos) y también describe el entorno general. El 3 es el siguiente mejor ya que también contiene mucha descripción.

## 🚀 Desafío

Ve si puedes aprovechar la técnica de "señal" con el prompt: Completa la frase "Muéstrame una imagen de coche rojo de marca Volvo y ". ¿Con qué responde y cómo lo mejorarías?

## ¡Gran trabajo! Continúa tu aprendizaje

¿Quieres aprender más sobre diferentes conceptos de Ingeniería de Prompts? Visita la [página de aprendizaje continuado](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar otros grandes recursos sobre este tema.

Dirígete a la Lección 5 donde veremos [técnicas avanzadas de prompting](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->