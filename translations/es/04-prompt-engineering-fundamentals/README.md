<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a45c318dc6ebc2604f35b8b829f93af2",
  "translation_date": "2025-05-19T09:31:46+00:00",
  "source_file": "04-prompt-engineering-fundamentals/README.md",
  "language_code": "es"
}
-->
# Fundamentos de la Ingeniería de Prompts

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear prompts efectivos en modelos de IA generativa. La manera en que redactes tu prompt para un LLM también importa. Un prompt cuidadosamente elaborado puede lograr una mejor calidad de respuesta. Pero, ¿qué significan exactamente términos como _prompt_ e _ingeniería de prompts_? ¿Y cómo puedo mejorar el _input_ del prompt que envío al LLM? Estas son las preguntas que intentaremos responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes de los usuarios. Lo logra utilizando _Modelos de Lenguaje Extensos_ como la serie GPT ("Generative Pre-trained Transformer") de OpenAI, que están entrenados para usar lenguaje natural y código.

Los usuarios ahora pueden interactuar con estos modelos usando paradigmas familiares como el chat, sin necesidad de tener experiencia técnica o entrenamiento. Los modelos son _basados en prompts_: los usuarios envían un input de texto (prompt) y reciben la respuesta de la IA (completación). Luego pueden "chatear con la IA" de manera iterativa, en conversaciones de múltiples turnos, refinando su prompt hasta que la respuesta cumpla con sus expectativas.

Los "prompts" se convierten ahora en la principal _interfaz de programación_ para aplicaciones de IA generativa, indicando a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. La "Ingeniería de Prompts" es un campo de estudio en rápido crecimiento que se centra en el _diseño y optimización_ de prompts para ofrecer respuestas consistentes y de calidad a escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Prompts, por qué es importante y cómo podemos elaborar prompts más efectivos para un modelo y objetivo de aplicación dados. Entenderemos conceptos clave y mejores prácticas para la ingeniería de prompts, y conoceremos un entorno de "sandbox" interactivo en Jupyter Notebooks donde podemos ver estos conceptos aplicados a ejemplos reales.

Al final de esta lección, seremos capaces de:

1. Explicar qué es la ingeniería de prompts y por qué es importante.
2. Describir los componentes de un prompt y cómo se utilizan.
3. Aprender mejores prácticas y técnicas para la ingeniería de prompts.
4. Aplicar técnicas aprendidas a ejemplos reales, utilizando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Prompts: La práctica de diseñar y refinar inputs para guiar a los modelos de IA hacia la producción de outputs deseados.
Tokenización: El proceso de convertir texto en unidades más pequeñas, llamadas tokens, que un modelo puede entender y procesar.
LLMs afinados por instrucciones: Modelos de Lenguaje Extensos (LLMs) que han sido afinados con instrucciones específicas para mejorar la precisión y relevancia de sus respuestas.

## Sandbox de Aprendizaje

La ingeniería de prompts es actualmente más un arte que una ciencia. La mejor manera de mejorar nuestra intuición es _practicar más_ y adoptar un enfoque de prueba y error que combine experiencia en el dominio de aplicación con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña esta lección proporciona un entorno de _sandbox_ donde puedes probar lo que aprendes, ya sea mientras avanzas o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave de API de Azure OpenAI**: el endpoint del servicio para un LLM desplegado.
2. **Un entorno de ejecución de Python**: en el cual se puede ejecutar el Notebook.
3. **Variables de entorno locales**: _completa los pasos del [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ahora para estar listo_.

El notebook viene con ejercicios _iniciales_, pero se te anima a añadir tus propias secciones de _Markdown_ (descripción) y _Código_ (solicitudes de prompt) para probar más ejemplos o ideas, y construir tu intuición para el diseño de prompts.

## Guía Ilustrada

¿Quieres obtener una visión general de lo que cubre esta lección antes de profundizar? Echa un vistazo a esta guía ilustrada, que te da una idea de los temas principales tratados y los puntos clave para que pienses en cada uno. El mapa de la lección te lleva desde la comprensión de los conceptos y desafíos fundamentales hasta abordarlos con técnicas de ingeniería de prompts relevantes y mejores prácticas. Ten en cuenta que la sección "Técnicas Avanzadas" en esta guía se refiere al contenido cubierto en el _siguiente_ capítulo de este currículo.

## Nuestra Startup

Ahora, hablemos de cómo _este tema_ se relaciona con nuestra misión de startup para [llevar la innovación de la IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicaciones impulsadas por IA de _aprendizaje personalizado_, así que pensemos en cómo los diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedirle a la IA que _analice datos del currículo para identificar brechas en la cobertura_. La IA puede resumir los resultados o visualizarlos con código.
- **Educadores** podrían pedirle a la IA que _genere un plan de lección para un público objetivo y tema_. La IA puede construir el plan personalizado en un formato especificado.
- **Estudiantes** podrían pedirle a la IA que _les enseñe una materia difícil_. La IA ahora puede guiar a los estudiantes con lecciones, pistas y ejemplos adaptados a su nivel.

Eso es solo la punta del iceberg. Echa un vistazo a [Prompts Para Educación](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst), una biblioteca de prompts de código abierto curada por expertos en educación, para obtener una idea más amplia de las posibilidades. ¡Intenta ejecutar algunos de esos prompts en el sandbox o usando el OpenAI Playground para ver qué sucede!

## ¿Qué es la Ingeniería de Prompts?

Comenzamos esta lección definiendo **Ingeniería de Prompts** como el proceso de _diseñar y optimizar_ inputs de texto (prompts) para ofrecer respuestas consistentes y de calidad (completaciones) para un objetivo de aplicación y modelo dado. Podemos pensar en esto como un proceso de 2 pasos:

- _diseñar_ el prompt inicial para un modelo y objetivo dados
- _refinar_ el prompt de manera iterativa para mejorar la calidad de la respuesta

Este es necesariamente un proceso de prueba y error que requiere intuición y esfuerzo del usuario para obtener resultados óptimos. Entonces, ¿por qué es importante? Para responder a esa pregunta, primero necesitamos entender tres conceptos:

- _Tokenización_ = cómo el modelo "ve" el prompt
- _Base LLMs_ = cómo el modelo base "procesa" un prompt
- _LLMs afinados por instrucciones_ = cómo el modelo ahora puede ver "tareas"

### Tokenización

Un LLM ve los prompts como una _secuencia de tokens_ donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Dado que los LLMs están entrenados en tokens (y no en texto sin procesar), la manera en que los prompts se tokenizan tiene un impacto directo en la calidad de la respuesta generada.

Para obtener una intuición de cómo funciona la tokenización, prueba herramientas como el [Tokenizador de OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) que se muestra a continuación. Copia tu prompt y observa cómo se convierte en tokens, prestando atención a cómo se manejan los caracteres de espacio en blanco y los signos de puntuación. Ten en cuenta que este ejemplo muestra un LLM más antiguo (GPT-3), por lo que probar esto con un modelo más reciente puede producir un resultado diferente.

### Concepto: Modelos Fundamentales

Una vez que un prompt se tokeniza, la función principal del ["Base LLM"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo fundamental) es predecir el token en esa secuencia. Dado que los LLMs están entrenados en conjuntos de datos de texto masivos, tienen un buen sentido de las relaciones estadísticas entre los tokens y pueden hacer esa predicción con cierta confianza. Ten en cuenta que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su próxima predicción. Pueden continuar prediciendo la secuencia hasta que sea terminada por la intervención del usuario o alguna condición preestablecida.

¿Quieres ver cómo funciona la completación basada en prompts? Ingresa el prompt anterior en el [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) de Azure OpenAI Studio con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información, por lo que deberías ver una completación que satisfaga este contexto.

Pero, ¿qué pasa si el usuario quería ver algo específico que cumpliera con algunos criterios u objetivos de tarea? Aquí es donde entran en juego los LLMs afinados por instrucciones.

### Concepto: LLMs Afinados por Instrucciones

Un [LLM Afinado por Instrucciones](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) comienza con el modelo fundamental y lo afina con ejemplos o pares de input/output (por ejemplo, "mensajes" de múltiples turnos) que pueden contener instrucciones claras, y la respuesta de la IA intenta seguir esa instrucción.

Esto utiliza técnicas como el Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo para _seguir instrucciones_ y _aprender de la retroalimentación_ para que produzca respuestas más adecuadas para aplicaciones prácticas y más relevantes para los objetivos del usuario.

Vamos a probarlo: revisa el prompt anterior, pero ahora cambia el _mensaje del sistema_ para proporcionar la siguiente instrucción como contexto:

> _Resume el contenido que se te proporcione para un estudiante de segundo grado. Mantén el resultado en un párrafo con 3-5 puntos destacados._

¿Ves cómo el resultado ahora está afinado para reflejar el objetivo y formato deseados? Un educador ahora puede usar directamente esta respuesta en sus diapositivas para esa clase.

## ¿Por qué necesitamos Ingeniería de Prompts?

Ahora que sabemos cómo los prompts son procesados por los LLMs, hablemos de _por qué_ necesitamos ingeniería de prompts. La respuesta radica en el hecho de que los LLMs actuales plantean una serie de desafíos que hacen que las _completaciones confiables y consistentes_ sean más difíciles de lograr sin poner esfuerzo en la construcción y optimización de prompts. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ probablemente producirá diferentes respuestas con diferentes modelos o versiones de modelo. Y puede incluso producir diferentes resultados con el _mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de prompts pueden ayudarnos a minimizar estas variaciones proporcionando mejores límites_.

2. **Los modelos pueden fabricar respuestas.** Los modelos están pre-entrenados con _conjuntos de datos grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese alcance de entrenamiento. Como resultado, pueden producir completaciones que son inexactas, imaginarias o directamente contradictorias con hechos conocidos. _Las técnicas de ingeniería de prompts ayudan a los usuarios a identificar y mitigar tales fabricaciones, por ejemplo, pidiendo a la IA citas o razonamiento_.

3. **Las capacidades de los modelos variarán.** Los modelos más nuevos o generaciones de modelos tendrán capacidades más ricas, pero también traerán peculiaridades únicas y compensaciones en costo y complejidad. _La ingeniería de prompts puede ayudarnos a desarrollar mejores prácticas y flujos de trabajo que abstraigan las diferencias y se adapten a los requisitos específicos del modelo de manera escalable y sin problemas_.

Veamos esto en acción en el OpenAI o Azure OpenAI Playground:

- Usa el mismo prompt con diferentes despliegues de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face) - ¿viste las variaciones?
- Usa el mismo prompt repetidamente con el _mismo_ despliegue de LLM (por ejemplo, el playground de Azure OpenAI) - ¿cómo difirieron estas variaciones?

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno donde los LLMs a veces generan información incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También puedes haber oído esto referido como _"alucinaciones"_ en artículos populares o trabajos de investigación. Sin embargo, recomendamos encarecidamente usar _"fabricación"_ como el término para que no antropomorficemos accidentalmente el comportamiento atribuyendo un rasgo humano a un resultado impulsado por máquina. Esto también refuerza las [directrices de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde una perspectiva de terminología, eliminando términos que también pueden considerarse ofensivos o no inclusivos en algunos contextos.

¿Quieres tener una idea de cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA a generar contenido para un tema inexistente (para asegurarte de que no se encuentra en el conjunto de datos de entrenamiento). Por ejemplo, intenté este prompt:

> **Prompt:** genera un plan de lección sobre la Guerra Marciana de 2076.

Una búsqueda en la web me mostró que había relatos ficticios (por ejemplo, series de televisión o libros) sobre guerras marcianas, pero ninguno en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede estar asociado con un evento real.

Entonces, ¿qué sucede cuando ejecutamos este prompt con diferentes proveedores de LLM?

Como era de esperar, cada modelo (o versión de modelo) produce respuestas ligeramente diferentes gracias al comportamiento estocástico y las variaciones de capacidad del modelo. Por ejemplo, un modelo se dirige a un público de octavo grado mientras que el otro asume un estudiante de secundaria. Pero los tres modelos generaron respuestas que podrían convencer a un usuario no informado de que el evento era real.

Las técnicas de ingeniería de prompts como _metaprompting_ y _configuración de temperatura_ pueden reducir las fabricaciones del modelo hasta cierto punto. Nuevas _arquitecturas_ de ingeniería de prompts también incorporan nuevas herramientas y técnicas de manera fluida en el flujo de prompts, para mitigar o reducir algunos de estos efectos.

## Estudio de Caso: GitHub Copilot

Vamos a cerrar esta sección obteniendo una idea de cómo se utiliza la ingeniería de prompts en soluciones del mundo real mirando un Estudio de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "Programador de Pareja de IA" - convierte prompts de texto en completaciones de código y está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario fluida. Como se documenta en la serie de blogs a continuación, la versión más temprana se basó en el modelo Codex de OpenAI, con los ingenieros dándose cuenta rápidamente de la necesidad de afinar el modelo y desarrollar mejores técnicas de ingeniería de prompts para mejorar la calidad del código. En julio, [debutaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugerencias aún más rápidas.

Lee las publicaciones en orden, para seguir su viaje de aprendizaje.

Puedes explorar su [blog de Ingeniería](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que muestra cómo estos modelos y técnicas se _aplican_ para impulsar aplicaciones del mundo real.

## Construcción de Prompts

Hemos visto por qué la ingeniería de prompts es importante, ahora entendamos cómo se _construyen_ los prompts para poder evaluar diferentes técnicas para un diseño de prompts más efectivo.

### Prompt Básico

Comencemos con el prompt básico: un input de texto enviado al modelo sin otro contexto. Aquí hay un ejemplo: cuando enviamos las primeras palabras del himno nacional de los Estados Unidos a la [API de Completación](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) de OpenAI, se _completa_ instantáneamente la respuesta con las siguientes líneas, ilustrando el comportamiento básico de predicción.

### Prompt Complejo

Ahora añadamos contexto e instrucciones a ese prompt básico. La [API de Completación de Chat](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir un prompt complejo como una colección de _mensajes_ con:

- Pares de input/output reflejando el input del _usuario_ y la respuesta del _asistente_.
- Mensaje del sistema estableciendo el contexto para el comportamiento o personalidad del asistente.

La solicitud ahora está en la forma que se muestra, donde la _tokenización_ captura efectivamente información relevante del contexto y la conversación. Ahora, cambiar el contexto del sistema puede tener tanto impacto en la calidad de las completaciones como los inputs de usuario proporcionados.

### Prompt de Instrucción

En los ejemplos anteriores, el prompt del usuario era una consulta de texto simple que puede interpretarse como una solicitud de información. Con los prompts de _instrucción_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando mejor orientación a la IA. Aquí hay un ejemplo:

### Contenido Principal

En los ejemplos anteriores, el prompt todavía era bastante abierto, permitiendo que el LLM decidiera qué parte de su conjunto de datos pre-entrenado era relevante. Con el diseño de _contenido principal_, el texto de entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí hay un ejemplo donde la instrucción es "resume esto en 2 oraciones".

El segmento de contenido principal se puede usar de varias maneras para impulsar instrucciones más efectivas:

-
Finalmente, el verdadero valor de las plantillas radica en la capacidad de crear y publicar _bibliotecas de instrucciones_ para dominios de aplicaciones verticales, donde la plantilla de instrucciones ahora está _optimizada_ para reflejar el contexto o ejemplos específicos de la aplicación que hacen que las respuestas sean más relevantes y precisas para la audiencia de usuarios objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, curando una biblioteca de instrucciones para el dominio educativo con énfasis en objetivos clave como la planificación de lecciones, el diseño curricular, la tutoría de estudiantes, etc.

## Contenido de Apoyo

Si pensamos en la construcción de instrucciones como tener una instrucción (tarea) y un objetivo (contenido principal), entonces el _contenido secundario_ es como el contexto adicional que proporcionamos para **influir en el resultado de alguna manera**. Podría ser parámetros de ajuste, instrucciones de formato, taxonomías de temas, etc., que pueden ayudar al modelo a _adaptar_ su respuesta para cumplir con los objetivos o expectativas del usuario deseados.

Por ejemplo: Dado un catálogo de cursos con metadatos extensos (nombre, descripción, nivel, etiquetas de metadatos, instructor, etc.) sobre todos los cursos disponibles en el currículo:

- podemos definir una instrucción para "resumir el catálogo de cursos para el otoño de 2023"
- podemos usar el contenido principal para proporcionar algunos ejemplos del resultado deseado
- podemos usar el contenido secundario para identificar las 5 principales "etiquetas" de interés.

Ahora, el modelo puede proporcionar un resumen en el formato mostrado por los pocos ejemplos, pero si un resultado tiene múltiples etiquetas, puede priorizar las 5 etiquetas identificadas en el contenido secundario.

---

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debe cubrir el concepto central #1.
Reforzar el concepto con ejemplos y referencias.

CONCEPTO #3:
Técnicas de Ingeniería de Instrucciones.
¿Cuáles son algunas técnicas básicas para la ingeniería de instrucciones?
Ilustrar con algunos ejercicios.
-->

## Mejores Prácticas de Instrucciones

Ahora que sabemos cómo se pueden _construir_ las instrucciones, podemos comenzar a pensar en cómo _diseñarlas_ para reflejar las mejores prácticas. Podemos pensar en esto en dos partes: tener la _mentalidad_ correcta y aplicar las _técnicas_ adecuadas.

### Mentalidad de Ingeniería de Instrucciones

La Ingeniería de Instrucciones es un proceso de prueba y error, así que ten en cuenta tres factores amplios:

1. **La comprensión del dominio importa.** La precisión y relevancia de la respuesta es una función del _dominio_ en el que opera esa aplicación o usuario. Aplica tu intuición y experiencia en el dominio para **personalizar técnicas** aún más. Por ejemplo, define _personalidades específicas del dominio_ en tus instrucciones del sistema, o usa _plantillas específicas del dominio_ en tus instrucciones de usuario. Proporciona contenido secundario que refleje contextos específicos del dominio, o utiliza _pistas y ejemplos específicos del dominio_ para guiar al modelo hacia patrones de uso familiares.

2. **La comprensión del modelo importa.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones de modelos también pueden variar en términos del conjunto de datos de entrenamiento que utilizan (conocimiento preentrenado), las capacidades que proporcionan (por ejemplo, a través de API o SDK) y el tipo de contenido para el que están optimizados (por ejemplo, código vs. imágenes vs. texto). Comprende las fortalezas y limitaciones del modelo que estás utilizando, y usa ese conocimiento para _priorizar tareas_ o construir _plantillas personalizadas_ que estén optimizadas para las capacidades del modelo.

3. **La iteración y validación importa.** Los modelos están evolucionando rápidamente, al igual que las técnicas para la ingeniería de instrucciones. Como experto en el dominio, puedes tener otro contexto o criterios para _tu_ aplicación específica, que puede no aplicarse a la comunidad en general. Utiliza herramientas y técnicas de ingeniería de instrucciones para "dar inicio" a la construcción de instrucciones, luego itera y valida los resultados utilizando tu propia intuición y experiencia en el dominio. Registra tus conocimientos y crea una **base de conocimientos** (por ejemplo, bibliotecas de instrucciones) que pueda ser utilizada como una nueva línea base por otros, para iteraciones más rápidas en el futuro.

## Mejores Prácticas

Ahora veamos las prácticas comunes recomendadas por los profesionales de [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                                | Por qué                                                                                                                                                                                                                                               |
| :--------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluar los modelos más recientes. | Es probable que las nuevas generaciones de modelos tengan características y calidad mejoradas, pero también pueden incurrir en costos más altos. Evalúalos por impacto, luego toma decisiones de migración.                                                                                    |
| Separar instrucciones y contexto   | Verifica si tu modelo/proveedor define _delimitadores_ para distinguir instrucciones, contenido principal y secundario más claramente. Esto puede ayudar a los modelos a asignar pesos más precisos a los tokens.                                                                            |
| Ser específico y claro             | Proporciona más detalles sobre el contexto deseado, resultado, longitud, formato, estilo, etc. Esto mejorará tanto la calidad como la consistencia de las respuestas. Captura recetas en plantillas reutilizables.                                                                          |
| Ser descriptivo, usar ejemplos     | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
| Use cues to jumpstart completions | Nudge it towards a desired outcome by giving it some leading words or phrases that it can use as a starting point for the response.                                                                                                               |
| Double Down                       | Sometimes you may need to repeat yourself to the model. Give instructions before and after your primary content, use an instruction and a cue, etc. Iterate & validate to see what works.                                                         |
| Order Matters                     | The order in which you present information to the model may impact the output, even in the learning examples, thanks to recency bias. Try different options to see what works best.                                                               |
| Give the model an “out”           | Give the model a _fallback_ completion response it can provide if it cannot complete the task for any reason. This can reduce chances of models generating false or fabricated responses.                                                         |
|                                   |                                                                                                                                                                                                                                                   |

As with any best practice, remember that _your mileage may vary_ based on the model, the task and the domain. Use these as a starting point, and iterate to find what works best for you. Constantly re-evaluate your prompt engineering process as new models and tools become available, with a focus on process scalability and response quality.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the prompts filled in and run, showing what one example could be.
-->

## Assignment

Congratulations! You made it to the end of the lesson! It's time to put some of those concepts and techniques to the test with real examples!

For our assignment, we'll be using a Jupyter Notebook with exercises you can complete interactively. You can also extend the Notebook with your own Markdown and Code cells to explore ideas and techniques on your own.

### To get started, fork the repo, then

- (Recommended) Launch GitHub Codespaces
- (Alternatively) Clone the repo to your local device and use it with Docker Desktop
- (Alternatively) Open the Notebook with your preferred Notebook runtime environment.

### Next, configure your environment variables

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valores. Vuelve a la [sección de Sandbox de Aprendizaje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender cómo.

### A continuación, abre el Jupyter Notebook

- Selecciona el kernel de tiempo de ejecución. Si usas las opciones 1 o 2, simplemente selecciona el kernel predeterminado de Python 3.10.x proporcionado por el contenedor de desarrollo.

Estás listo para ejecutar los ejercicios. Ten en cuenta que no hay respuestas _correctas o incorrectas_ aquí, solo explorar opciones mediante prueba y error y construir intuición sobre lo que funciona para un modelo y dominio de aplicación dado.

_Por esta razón no hay segmentos de Solución de Código en esta lección. En su lugar, el Notebook tendrá celdas de Markdown tituladas "Mi Solución:" que muestran un ejemplo de salida como referencia._

 <!--
PLANTILLA DE LECCIÓN:
Cierra la sección con un resumen y recursos para el aprendizaje autodirigido.
-->

## Comprobación de Conocimiento

¿Cuál de las siguientes es una buena instrucción siguiendo algunas prácticas razonables?

1. Muéstrame una imagen de un coche rojo
2. Muéstrame una imagen de un coche rojo de marca Volvo y modelo XC90 estacionado junto a un acantilado con el sol poniéndose
3. Muéstrame una imagen de un coche rojo de marca Volvo y modelo XC90

A: 2, es la mejor instrucción ya que proporciona detalles sobre "qué" y entra en especificaciones (no solo cualquier coche, sino una marca y modelo específicos) y también describe el entorno general. 3 es el siguiente mejor ya que también contiene mucha descripción.

## 🚀 Desafío

Ve si puedes aprovechar la técnica de "pista" con la instrucción: Completa la frase "Muéstrame una imagen de un coche rojo de marca Volvo y ". ¿Con qué responde, y cómo lo mejorarías?

## ¡Buen Trabajo! Continúa Tu Aprendizaje

¿Quieres aprender más sobre diferentes conceptos de Ingeniería de Instrucciones? Ve a la [página de aprendizaje continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar otros excelentes recursos sobre este tema.

Dirígete a la Lección 5 donde veremos [técnicas avanzadas de instrucciones](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.