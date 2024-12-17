# Fundamentos de la Ingeniería de Prompts

[![Fundamentos de la Ingeniería de Prompts](../../../translated_images/04-lesson-banner.png?WT.d904d510033d5f0283f2caff5f735050f929dd196a1fc25fefa18433347fe463.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear prompts efectivos en modelos de IA generativa. La forma en que escribes tu prompt a un LLM también importa. Un prompt cuidadosamente elaborado puede lograr una mejor calidad de respuesta. Pero, ¿qué significan exactamente términos como _prompt_ e _ingeniería de prompts_? ¿Y cómo puedo mejorar el _input_ del prompt que envío al LLM? Estas son las preguntas que intentaremos responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear nuevo contenido (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes de los usuarios. Lo logra utilizando _Modelos de Lenguaje Extensos_ como la serie GPT ("Generative Pre-trained Transformer") de OpenAI, que están entrenados para usar lenguaje natural y código.

Los usuarios ahora pueden interactuar con estos modelos usando paradigmas familiares como el chat, sin necesidad de conocimientos técnicos o capacitación. Los modelos están basados en _prompts_ - los usuarios envían una entrada de texto (prompt) y reciben la respuesta de la IA (completación). Luego pueden "chatear con la IA" de manera iterativa, en conversaciones de múltiples turnos, refinando su prompt hasta que la respuesta cumpla con sus expectativas.

Los "prompts" ahora se convierten en la principal _interfaz de programación_ para aplicaciones de IA generativa, indicando a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. La "Ingeniería de Prompts" es un campo de estudio de rápido crecimiento que se centra en el _diseño y optimización_ de prompts para ofrecer respuestas consistentes y de calidad a gran escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Prompts, por qué es importante y cómo podemos crear prompts más efectivos para un modelo y objetivo de aplicación dados. Entenderemos conceptos básicos y mejores prácticas para la ingeniería de prompts, y aprenderemos sobre un entorno interactivo de "sandbox" en Jupyter Notebooks donde podemos ver estos conceptos aplicados a ejemplos reales.

Al final de esta lección, seremos capaces de:

1. Explicar qué es la ingeniería de prompts y por qué es importante.
2. Describir los componentes de un prompt y cómo se utilizan.
3. Aprender mejores prácticas y técnicas para la ingeniería de prompts.
4. Aplicar las técnicas aprendidas a ejemplos reales, utilizando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Prompts: La práctica de diseñar y refinar entradas para guiar a los modelos de IA hacia la producción de salidas deseadas.
Tokenización: El proceso de convertir texto en unidades más pequeñas, llamadas tokens, que un modelo puede entender y procesar.
LLMs Ajustados por Instrucción: Modelos de Lenguaje Extensos (LLMs) que han sido ajustados con instrucciones específicas para mejorar la precisión y relevancia de sus respuestas.

## Sandbox de Aprendizaje

La ingeniería de prompts es actualmente más arte que ciencia. La mejor manera de mejorar nuestra intuición al respecto es _practicar más_ y adoptar un enfoque de prueba y error que combine la experiencia en el dominio de la aplicación con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña esta lección proporciona un entorno de _sandbox_ donde puedes probar lo que aprendes, ya sea mientras avanzas o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave API de Azure OpenAI** - el endpoint del servicio para un LLM desplegado.
2. **Un Entorno de Ejecución de Python** - en el cual se pueda ejecutar el Notebook.
3. **Variables de Entorno Local** - _completa los pasos de [SETUP](./../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ahora para prepararte_.

El notebook viene con ejercicios _iniciales_ - pero se te anima a agregar tus propias secciones de _Markdown_ (descripción) y _Código_ (solicitudes de prompts) para probar más ejemplos o ideas - y construir tu intuición para el diseño de prompts.

## Guía Ilustrada

¿Quieres obtener una visión general de lo que cubre esta lección antes de profundizar? Echa un vistazo a esta guía ilustrada, que te da una idea de los temas principales cubiertos y los puntos clave para que reflexiones en cada uno. El mapa de la lección te lleva desde la comprensión de los conceptos y desafíos básicos hasta abordarlos con técnicas de ingeniería de prompts relevantes y mejores prácticas. Ten en cuenta que la sección de "Técnicas Avanzadas" en esta guía se refiere a contenido cubierto en el _próximo_ capítulo de este currículo.

![Guía Ilustrada de Ingeniería de Prompts](../../../translated_images/04-prompt-engineering-sketchnote.png?WT.a936f69bc33c7a783015f6747ea56d0f0071349644cd9031f9b8d20a3eec8696.es.mc_id=academic-105485-koreyst)

## Nuestra Startup

Ahora, hablemos sobre cómo _este tema_ se relaciona con nuestra misión de startup para [llevar la innovación de IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicaciones de aprendizaje personalizado impulsadas por IA, así que pensemos en cómo los diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedir a la IA que _analice datos del currículo para identificar brechas en la cobertura_. La IA puede resumir resultados o visualizarlos con código.
- **Educadores** podrían pedir a la IA que _genere un plan de lección para una audiencia y tema específicos_. La IA puede construir el plan personalizado en un formato especificado.
- **Estudiantes** podrían pedir a la IA que _les enseñe una materia difícil_. La IA ahora puede guiar a los estudiantes con lecciones, pistas y ejemplos adaptados a su nivel.

Eso es solo la punta del iceberg. Echa un vistazo a [Prompts Para Educación](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una biblioteca de prompts de código abierto curada por expertos en educación - para obtener una visión más amplia de las posibilidades. _¡Intenta ejecutar algunos de esos prompts en el sandbox o utilizando el OpenAI Playground para ver qué sucede!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## ¿Qué es la Ingeniería de Prompts?

Comenzamos esta lección definiendo la **Ingeniería de Prompts** como el proceso de _diseñar y optimizar_ entradas de texto (prompts) para ofrecer respuestas consistentes y de calidad (completaciones) para un objetivo de aplicación y modelo dados. Podemos pensar en esto como un proceso de 2 pasos:

- _diseñar_ el prompt inicial para un modelo y objetivo dados
- _refinar_ el prompt de manera iterativa para mejorar la calidad de la respuesta

Este es necesariamente un proceso de prueba y error que requiere intuición y esfuerzo del usuario para obtener resultados óptimos. Entonces, ¿por qué es importante? Para responder a esa pregunta, primero necesitamos entender tres conceptos:

- _Tokenización_ = cómo el modelo "ve" el prompt
- _LLMs Base_ = cómo el modelo base "procesa" un prompt
- _LLMs Ajustados por Instrucción_ = cómo el modelo ahora puede ver "tareas"

### Tokenización

Un LLM ve los prompts como una _secuencia de tokens_ donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Dado que los LLMs están entrenados en tokens (y no en texto en bruto), la forma en que los prompts se tokenizan tiene un impacto directo en la calidad de la respuesta generada.

Para obtener una intuición de cómo funciona la tokenización, prueba herramientas como el [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) que se muestra a continuación. Copia tu prompt - y observa cómo se convierte en tokens, prestando atención a cómo se manejan los caracteres de espacio en blanco y los signos de puntuación. Ten en cuenta que este ejemplo muestra un LLM más antiguo (GPT-3) - por lo que probar esto con un modelo más nuevo puede producir un resultado diferente.

![Tokenización](../../../translated_images/04-tokenizer-example.png?WT.f5399316da400747ffe3af9c95e61dc1a85508d57378da23a77538270c4cabf1.es.mc_id=academic-105485-koreyst)

### Concepto: Modelos Base

Una vez que un prompt está tokenizado, la función principal del ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo base) es predecir el token en esa secuencia. Dado que los LLMs están entrenados en conjuntos de datos de texto masivos, tienen una buena noción de las relaciones estadísticas entre los tokens y pueden hacer esa predicción con cierta confianza. Ten en cuenta que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su próxima predicción. Pueden continuar prediciendo la secuencia hasta que el usuario intervenga o se alcance una condición preestablecida.

¿Quieres ver cómo funciona la completación basada en prompts? Ingresa el prompt anterior en el [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) de Azure OpenAI Studio con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información, por lo que deberías ver una completación que satisfaga este contexto.

Pero, ¿qué pasa si el usuario quiere ver algo específico que cumpla con algunos criterios u objetivo de tarea? Aquí es donde entran en juego los LLMs _ajustados por instrucción_.

![Completación de Chat de LLM Base](../../../translated_images/04-playground-chat-base.png?WT.7645a03d7989b1c410f2e9e6b503d18e4624f82d9cbf108dac999b8c8988f0ad.es.mc_id=academic-105485-koreyst)

### Concepto: LLMs Ajustados por Instrucción

Un [LLM Ajustado por Instrucción](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) comienza con el modelo base y lo ajusta con ejemplos o pares de entrada/salida (por ejemplo, "mensajes" de múltiples turnos) que pueden contener instrucciones claras, y la respuesta de la IA intenta seguir esa instrucción.

Esto utiliza técnicas como el Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo para _seguir instrucciones_ y _aprender de la retroalimentación_ de modo que produzca respuestas que estén mejor adaptadas a aplicaciones prácticas y sean más relevantes para los objetivos del usuario.

Vamos a probarlo - vuelve al prompt anterior, pero ahora cambia el _mensaje del sistema_ para proporcionar la siguiente instrucción como contexto:

> _Resume el contenido que se te proporcione para un estudiante de segundo grado. Mantén el resultado en un párrafo con 3-5 viñetas._

¿Ves cómo el resultado ahora está ajustado para reflejar el objetivo y formato deseados? Un educador ahora puede usar directamente esta respuesta en sus diapositivas para esa clase.

![Completación de Chat de LLM Ajustado por Instrucción](../../../translated_images/04-playground-chat-instructions.png?WT.d9c80b15e90815a83ce665bf4418e70205d30318a5a5bcf407b2c92769743593.es.mc_id=academic-105485-koreyst)

## ¿Por qué necesitamos la Ingeniería de Prompts?

Ahora que sabemos cómo los LLMs procesan los prompts, hablemos de _por qué_ necesitamos la ingeniería de prompts. La respuesta radica en el hecho de que los LLMs actuales presentan una serie de desafíos que hacen que lograr _completaciones confiables y consistentes_ sea más difícil sin dedicar esfuerzo a la construcción y optimización de prompts. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** Es probable que el _mismo prompt_ produzca diferentes respuestas con diferentes modelos o versiones de modelos. Y puede incluso producir diferentes resultados con el _mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de prompts pueden ayudarnos a minimizar estas variaciones proporcionando mejores límites_.

1. **Los modelos pueden fabricar respuestas.** Los modelos están preentrenados con _conjuntos de datos grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese ámbito de entrenamiento. Como resultado, pueden producir completaciones que son inexactas, imaginarias o directamente contradictorias a hechos conocidos. _Las técnicas de ingeniería de prompts ayudan a los usuarios a identificar y mitigar tales fabricaciones, por ejemplo, pidiendo a la IA citas o razonamientos_.

1. **Las capacidades de los modelos variarán.** Los modelos más nuevos o generaciones de modelos tendrán capacidades más ricas, pero también traerán peculiaridades únicas y compensaciones en costo y complejidad. _La ingeniería de prompts puede ayudarnos a desarrollar mejores prácticas y flujos de trabajo que abstraigan las diferencias y se adapten a los requisitos específicos del modelo de manera escalable y sin problemas_.

Veamos esto en acción en el OpenAI o Azure OpenAI Playground:

- Usa el mismo prompt con diferentes implementaciones de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face) - ¿viste las variaciones?
- Usa el mismo prompt repetidamente con la _misma_ implementación de LLM (por ejemplo, Azure OpenAI playground) - ¿cómo diferían estas variaciones?

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno en el que los LLMs a veces generan información incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También puedes haber oído esto referido como _"alucinaciones"_ en artículos populares o trabajos de investigación. Sin embargo, recomendamos encarecidamente usar _"fabricación"_ como término para no antropomorfizar accidentalmente el comportamiento al atribuir un rasgo humano a un resultado impulsado por una máquina. Esto también refuerza las [directrices de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde una perspectiva de terminología, eliminando términos que también pueden considerarse ofensivos o no inclusivos en algunos contextos.

¿Quieres tener una idea de cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA a generar contenido para un tema inexistente (para asegurarte de que no se encuentre en el conjunto de datos de entrenamiento). Por ejemplo, intenté este prompt:

> **Prompt:** genera un plan de lección sobre la Guerra Marciana de 2076.

Una búsqueda en la web me mostró que había relatos ficticios (por ejemplo, series de televisión o libros) sobre guerras marcianas, pero ninguno en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede asociarse con un evento real.

Entonces, ¿qué sucede cuando ejecutamos este prompt con diferentes proveedores de LLM?

> **Respuesta 1**: OpenAI Playground (GPT-35)

![Respuesta 1](../../../translated_images/04-fabrication-oai.png?WT.08cc3e01259a6b46725a800e67de50c37b7fdd6b1f932f027881cbe32f80bcf1.es.mc_id=academic-105485-koreyst)

> **Respuesta 2**: Azure OpenAI Playground (GPT-35)

![Respuesta 2](../../../translated_images/04-fabrication-aoai.png?WT.81e0d286a351c87c804aaca6e5f8251a6deed5105d11bca035f8cead8c52d299.es.mc_id=academic-105485-koreyst)

> **Respuesta 3**: : Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../../translated_images/04-fabrication-huggingchat.png?WT.992b3a675cc7ed0dbe53e308b93df8165048fb7c4516e6bb00611d05c92e8fd5.es.mc_id=academic-105485-koreyst)

Como era de esperar, cada modelo (o versión de modelo) produce respuestas ligeramente diferentes gracias al comportamiento estocástico y las variaciones en las capacidades del modelo. Por ejemplo, un modelo se dirige a una audiencia de octavo grado, mientras que el otro asume un estudiante de secundaria. Pero los tres modelos generaron respuestas que podrían convencer a un usuario desinformado de que el evento era real.

Las técnicas de ingeniería de prompts como _metaprompting_ y _configuración de temperatura_ pueden reducir las fabricaciones del modelo hasta cierto punto. Nuevas _arquitecturas_ de ingeniería de prompts también incorporan nuevas herramientas y técnicas de manera fluida en el flujo de prompts, para mitigar o reducir algunos de estos efectos.

## Estudio de Caso: GitHub Copilot

Concluyamos esta sección obteniendo una idea de cómo se utiliza la ingeniería de prompts en soluciones del mundo real al observar un Estudio de Caso: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "Programador de Pareja de IA" - convierte prompts de texto en completaciones de código y está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario fluida. Como se documenta en la serie de blogs a continuación, la versión más temprana se basó en el modelo OpenAI Codex, y los ingenieros rápidamente se dieron cuenta de la necesidad de ajustar el modelo y desarrollar mejores técnicas de ingeniería de prompts para mejorar la calidad del código. En julio, [debutaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugerencias aún más rápidas.

Lee las publicaciones en orden, para seguir su viaje de aprendizaje.

- **Mayo 2023** | [GitHub Copilot está Mejorando en Entender tu Código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: Trabajando con los LLMs detrás de GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junio 2023** | [Cómo escribir mejores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julio 2023** | [..
Finalmente, el verdadero valor de las plantillas radica en la capacidad de crear y publicar _bibliotecas de prompts_ para dominios de aplicaciones verticales, donde la plantilla de prompt ahora está _optimizada_ para reflejar un contexto o ejemplos específicos de la aplicación que hacen que las respuestas sean más relevantes y precisas para la audiencia de usuarios objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, curando una biblioteca de prompts para el dominio de la educación con énfasis en objetivos clave como la planificación de lecciones, el diseño curricular, la tutoría de estudiantes, etc.

## Contenido de Apoyo

Si pensamos en la construcción de prompts como tener una instrucción (tarea) y un objetivo (contenido principal), entonces el _contenido secundario_ es como el contexto adicional que proporcionamos para **influenciar la salida de alguna manera**. Podría ser la sintonización de parámetros, instrucciones de formato, taxonomías de temas, etc., que pueden ayudar al modelo a _adaptar_ su respuesta para adecuarse a los objetivos o expectativas deseadas por el usuario.

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
Técnicas de Ingeniería de Prompts.
¿Cuáles son algunas técnicas básicas para la ingeniería de prompts?
Ilústralo con algunos ejercicios.
-->

## Mejores Prácticas de Prompts

Ahora que sabemos cómo se pueden _construir_ los prompts, podemos comenzar a pensar en cómo _diseñarlos_ para reflejar las mejores prácticas. Podemos pensar en esto en dos partes: tener la _mentalidad_ correcta y aplicar las _técnicas_ adecuadas.

### Mentalidad de Ingeniería de Prompts

La Ingeniería de Prompts es un proceso de prueba y error, así que ten en cuenta tres factores amplios que guían:

1. **La Comprensión del Dominio Importa.** La precisión y relevancia de la respuesta es una función del _dominio_ en el que opera esa aplicación o usuario. Aplica tu intuición y experiencia en el dominio para **personalizar las técnicas** aún más. Por ejemplo, define _personalidades específicas del dominio_ en tus prompts del sistema, o usa _plantillas específicas del dominio_ en tus prompts de usuario. Proporciona contenido secundario que refleje contextos específicos del dominio, o utiliza _pistas y ejemplos específicos del dominio_ para guiar al modelo hacia patrones de uso familiares.

2. **La Comprensión del Modelo Importa.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones de modelos también pueden variar en términos del conjunto de datos de entrenamiento que utilizan (conocimiento preentrenado), las capacidades que proporcionan (por ejemplo, a través de API o SDK) y el tipo de contenido para el que están optimizados (por ejemplo, código vs. imágenes vs. texto). Comprende las fortalezas y limitaciones del modelo que estás utilizando y utiliza ese conocimiento para _priorizar tareas_ o construir _plantillas personalizadas_ que estén optimizadas para las capacidades del modelo.

3. **La Iteración y Validación Importa.** Los modelos están evolucionando rápidamente, al igual que las técnicas para la ingeniería de prompts. Como experto en el dominio, es posible que tengas otro contexto o criterios para _tu_ aplicación específica, que puede no aplicarse a la comunidad en general. Usa herramientas y técnicas de ingeniería de prompts para "dar un salto inicial" en la construcción de prompts, luego itera y valida los resultados utilizando tu propia intuición y experiencia en el dominio. Registra tus conocimientos y crea una **base de conocimientos** (por ejemplo, bibliotecas de prompts) que puedan ser utilizadas como una nueva línea base por otros, para iteraciones más rápidas en el futuro.

## Mejores Prácticas

Ahora veamos las prácticas comunes recomendadas por los profesionales de [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                               | Por qué                                                                                                                                                                                                                                             |
| :-------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evaluar los modelos más recientes. | Las nuevas generaciones de modelos probablemente tengan características y calidad mejoradas, pero también pueden tener costos más altos. Evalúalos por su impacto, luego toma decisiones de migración.                                               |
| Separar instrucciones y contexto  | Verifica si tu modelo/proveedor define _delimitadores_ para distinguir instrucciones, contenido principal y secundario de manera más clara. Esto puede ayudar a los modelos a asignar pesos más precisos a los tokens.                               |
| Ser específico y claro            | Da más detalles sobre el contexto deseado, resultado, longitud, formato, estilo, etc. Esto mejorará tanto la calidad como la consistencia de las respuestas. Captura recetas en plantillas reutilizables.                                            |
| Ser descriptivo, usar ejemplos    | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un `zero-shot` approach where you give it an instruction (but no examples) then try `few-shot` as a refinement, providing a few examples of the desired output. Use analogies. |
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

- Copy the `.env.copy` file in repo root to `.env` and fill in the `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_DEPLOYMENT` valores. Regresa a la [sección de Sandbox de Aprendizaje](../../../04-prompt-engineering-fundamentals/04-prompt-engineering-fundamentals) para aprender cómo.

### A continuación, abre el Jupyter Notebook

- Selecciona el núcleo de tiempo de ejecución. Si usas las opciones 1 o 2, simplemente selecciona el núcleo predeterminado de Python 3.10.x proporcionado por el contenedor de desarrollo.

Estás listo para ejecutar los ejercicios. Ten en cuenta que aquí no hay respuestas _correctas o incorrectas_, solo se exploran opciones mediante prueba y error y se construye intuición sobre lo que funciona para un modelo y dominio de aplicación dados.

_Por esta razón, no hay segmentos de Solución de Código en esta lección. En su lugar, el Notebook tendrá celdas de Markdown tituladas "Mi Solución:" que muestran un ejemplo de salida para referencia._

<!--
PLANTILLA DE LECCIÓN:
Cierra la sección con un resumen y recursos para el aprendizaje autodirigido.
-->

## Verificación de Conocimiento

¿Cuál de los siguientes es un buen prompt siguiendo algunas prácticas razonables?

1. Muéstrame una imagen de un coche rojo
2. Muéstrame una imagen de un coche rojo de la marca Volvo y modelo XC90 estacionado junto a un acantilado con el sol poniéndose
3. Muéstrame una imagen de un coche rojo de la marca Volvo y modelo XC90

A: 2, es el mejor prompt ya que proporciona detalles sobre "qué" y entra en especificaciones (no solo cualquier coche, sino una marca y modelo específicos) y también describe el entorno general. 3 es el siguiente mejor ya que también contiene mucha descripción.

## 🚀 Desafío

Ve si puedes aprovechar la técnica de "pista" con el prompt: Completa la oración "Muéstrame una imagen de un coche rojo de la marca Volvo y ". ¿Con qué responde, y cómo lo mejorarías?

## ¡Gran Trabajo! Continúa Tu Aprendizaje

¿Quieres aprender más sobre diferentes conceptos de Ingeniería de Prompts? Ve a la [página de aprendizaje continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar otros recursos excelentes sobre este tema.

Dirígete a la Lección 5 donde veremos [técnicas avanzadas de prompts](../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.