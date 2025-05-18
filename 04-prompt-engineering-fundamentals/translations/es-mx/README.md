# Fundamentos de la Ingeniería de Indicaciones

[![Fundamentos de la Ingeniería de Indicaciones](../../images/04-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson4-gh?WT.mc_id=academic-105485-koreyst)

## Introducción
Este módulo cubre conceptos y técnicas esenciales para crear indicaciones efectivos en modelos de IA generativa. La forma en que escribes tu prompt para un LLM también importa. Un prompt cuidadosamente diseñado puede lograr respuestas de mayor calidad. Pero qué significan exactamente términos como _prompt_ e _ingeniería de indicaciones_? Y cómo puedo mejorar el _input_ que envío al LLM? Estas son las preguntas que intentaremos responder en este capítulo y el siguiente.

La _IA generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a solicitudes de los usuarios. Lo logra utilizando _Modelos de Lenguaje Extenso_ (LLM, por sus siglas en inglés) como la serie GPT ("Transformador Generativo Preentrenado") de OpenAI, entrenados para comprender lenguaje natural y código.

Los usuarios pueden interactuar ahora con estos modelos usando paradigmas familiares como el chat, sin necesidad de conocimientos técnicos ni entrenamiento. Los modelos se basan en _indicaciones_ — los usuarios envían una entrada de texto (prompt) y reciben la respuesta de la IA (completado). Pueden "chatear con la IA" de forma iterativa, en conversaciones de varios turnos, refinando el prompt hasta que la respuesta cumpla sus expectativas.

Los "indicaciones" se convierten ahora en la principal _interfaz de programación_ para las aplicaciones de IA generativa, indicando a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. La _Ingeniería de indicaciones_ es un campo de estudio en rápido crecimiento que se enfoca en el _diseño y la optimización_ de indicaciones para ofrecer respuestas consistentes y de calidad a escala.

## Objetivos de Aprendizaje

En esta lección, aprenderemos qué es la Ingeniería de Indicaciones, por qué es importante y cómo podemos redactar indicaciones más efectivos para un modelo y objetivo específico. Comprenderemos los conceptos fundamentales y las buenas prácticas para la ingeniería de indicaciones, y conoceremos un entorno interactivo de Jupyter Notebooks donde veremos estos conceptos aplicados a ejemplos reales.

Al final de esta lección, serás capaz de:

1. Explicar qué es la ingeniería de indicaciones y por qué importa.
2. Describir los componentes de un prompt y cómo se usan.
3. Conocer buenas prácticas y técnicas para la ingeniería de indicaciones.
4. Aplicar técnicas aprendidas a ejemplos reales, usando un endpoint de OpenAI.

## Términos Clave

Ingeniería de Indicaciones: La práctica de diseñar y refinar entradas para guiar a los modelos de IA hacia la producción de salidas deseadas.  
Tokenización: El proceso de convertir texto en unidades más pequeñas, llamadas tokens, que un modelo puede entender y procesar.  
LLMs Afinados con Instrucciones: Modelos de Lenguaje Extenso (LLMs) que han sido afinados con instrucciones específicas para mejorar la precisión y relevancia de sus respuestas.

## Entorno de Práctica

La ingeniería de indicaciones es actualmente más un arte que una ciencia. La mejor forma de mejorar nuestra intuición es _practicar más_ y adoptar un enfoque de prueba y error que combine conocimiento del dominio con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña esta lección proporciona un entorno tipo _sandbox_ donde puedes probar lo que vas aprendiendo — a medida que avanzas o como parte del desafío de código al final. Para ejecutar los ejercicios, necesitarás:

1. **Una clave API de Azure OpenAI** – el endpoint del servicio para un LLM desplegado.
2. **Un entorno de ejecución de Python** – donde se pueda ejecutar el Notebook.
3. **Variables de entorno locales** – _completa los pasos del [SETUP](../../../00-course-setup/SETUP.md?WT.mc_id=academic-105485-koreyst) ahora para estar listo_.

El Notebook incluye ejercicios _iniciales_ — pero se te anima a añadir tus propias secciones de _Markdown_ (descripción) y _Código_ (solicitudes de indicaciones) para probar más ejemplos o ideas — y desarrollar tu intuición sobre el diseño de indicaciones.

## Guía Ilustrada

Quieres tener una idea general de lo que cubre esta lección antes de comenzar? Mira esta guía ilustrada, que te da una visión general de los temas principales y los puntos clave que debes tener en cuenta en cada uno. El recorrido de la lección te lleva desde la comprensión de los conceptos fundamentales y los desafíos, hasta cómo abordarlos con técnicas y buenas prácticas de ingeniería de indicaciones. Ten en cuenta que la sección de “Técnicas Avanzadas” en esta guía hace referencia al contenido del _próximo_ capítulo de este plan de estudios.

![Guía Ilustrada sobre Ingeniería de Indicaciones](../../images/04-prompt-engineering-sketchnote.png?WT.mc_id=academic-105485-koreyst)

## Nuestra Startup

Ahora hablemos de cómo _este tema_ se relaciona con nuestra misión como startup de [llevar la innovación en IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos construir aplicaciones impulsadas por IA para el _aprendizaje personalizado_, así que pensemos en cómo distintos usuarios de nuestra aplicación podrían "diseñar" indicaciones:

- **Administradores** podrían pedir a la IA que _analice datos curriculares para identificar vacíos en la cobertura_. La IA puede resumir los resultados o visualizarlos con código.
- **Educadores** podrían pedir a la IA que _genere un plan de lección para una audiencia y tema específicos_. La IA puede crear el plan personalizado en un formato definido.
- **Estudiantes** podrían pedir a la IA que _les enseñe un tema difícil_. La IA ahora puede guiarlos con lecciones, pistas y ejemplos adaptados a su nivel.

Y eso es solo la punta del iceberg. Revisa [Indicaciones para Educacion](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst), una biblioteca de indicaciones de código abierto curada por expertos en educación, para tener una visión más amplia de las posibilidades! _Prueba algunos de esos indicaciones en el sandbox o usando el OpenAI Playground para ver qué ocurre!_

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #1:
Prompt Engineering.
Define it and explain why it is needed.
-->

## Qué es la Ingeniería de Indicaciones?

Comenzamos esta lección definiendo la **Ingeniería de Indicaciones** como el proceso de _diseñar y optimizar_ entradas de texto (indicaciones) para generar respuestas (completions) consistentes y de calidad para un objetivo y modelo determinados. Podemos pensar en esto como un proceso de 2 pasos:

- _Diseñar_ el prompt inicial para un modelo y objetivo específicos
- _Refinar_ el prompt de forma iterativa para mejorar la calidad de la respuesta

Este proceso requiere necesariamente prueba y error, intuición del usuario y esfuerzo para obtener los mejores resultados. Entonces, por qué es importante? Para responder a esa pregunta, primero debemos entender tres conceptos:

- _Tokenización_ = cómo el modelo “ve” el prompt
- _Modelos base_ (Base LLMs) = cómo el modelo procesa el prompt
- _LLMs afinados con instrucciones_ = cómo el modelo puede ahora ver “tareas”

### Tokenización

Un LLM ve los indicaciones como una _secuencia de tokens_, y diferentes modelos (o versiones del mismo) pueden tokenizar el mismo prompt de distintas formas. Como los LLMs están entrenados con tokens (y no con texto en bruto), la forma en que un prompt se tokeniza impacta directamente en la calidad de la respuesta generada.

Para entender mejor cómo funciona la tokenización, prueba herramientas como el [Tokenizer de OpenAI](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst). Copia tu prompt y observa cómo se convierte en tokens, prestando atención a cómo se tratan los espacios y signos de puntuación. Este ejemplo usa un modelo antiguo (GPT-3), así que al usar un modelo más nuevo podrías obtener resultados diferentes.

![Tokenización](../../images/04-tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

### Concepto: Modelos Base

Una vez tokenizado el prompt, la función principal del ["LLM base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o modelo fundacional) es predecir el siguiente token en la secuencia. Como estos modelos están entrenados con grandes cantidades de texto, tienen una buena comprensión estadística de la relación entre tokens y pueden predecir con cierto nivel de confianza. Es importante notar que no entienden el _significado_ de las palabras; simplemente reconocen patrones que pueden “completar”.

Quieres ver cómo funciona esta predicción basada en indicaciones? Ingresa el prompt anterior en Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) con la configuración predeterminada. El sistema tratará el prompt como una solicitud de información y debería generar una respuesta que se ajuste al contexto.

Pero qué pasa si el usuario quiere algo más específico que cumpla con ciertos criterios o un objetivo de tarea? Aquí es donde entran los _LLMs afinados con instrucciones_.

![Chat completado con modelo base](../../images/04-playground-chat-base.png?WT.mc_id=academic-105485-koreyst)

### Concepto: LLMs Afinados con Instrucciones

Un [LLM afinado con instrucciones](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) parte del modelo fundacional y se entrena adicionalmente con ejemplos o pares de entrada/salida (por ejemplo, “mensajes” en conversaciones) que contienen instrucciones claras, y el modelo intenta seguirlas.

Esto se logra con técnicas como Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF), que entrena al modelo para _seguir instrucciones_ y _aprender del feedback_, generando respuestas más relevantes y útiles para casos de uso reales.

Probémoslo: vuelve al prompt anterior, pero ahora cambia el _mensaje del sistema_ para incluir la siguiente instrucción como contexto:

> _Resume el contenido que se te proporcione como si se lo explicaras a un estudiante de segundo grado. Limita la respuesta a un párrafo con 3–5 viñetas._

Observa cómo el resultado ahora se ajusta al objetivo y formato deseado. Un educador puede usar esta respuesta directamente en sus presentaciones para esa clase.

![Completado con modelo afinado](../../images/04-playground-chat-instructions.png?WT.mc_id=academic-105485-koreyst)

## Por qué necesitamos Ingeniería de Indicaciones?

Ahora que sabemos cómo los LLMs procesan los indicaciones, hablemos de _por qué_ necesitamos ingeniería de indicaciones. La respuesta está en el hecho de que los modelos actuales presentan varios desafíos que hacen más difícil obtener _respuestas confiables y consistentes_ sin dedicar esfuerzo a la construcción y optimización del prompt. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ puede producir respuestas distintas con diferentes modelos o versiones del modelo. Incluso puede generar resultados diferentes con el _mismo modelo_ en diferentes momentos. _Las técnicas de ingeniería de indicaciones pueden ayudarnos a minimizar estas variaciones proporcionando mejores estructuras de control_.

2. **Los modelos pueden inventar información.** Aunque los modelos fueron preentrenados con _grandes cantidades de datos_, estos siguen siendo limitados. Como resultado, pueden generar respuestas que son inexactas, inventadas o incluso contradictorias con hechos conocidos. _Las técnicas de ingeniería de indicaciones ayudan a mitigar estas invenciones, por ejemplo, pidiendo citas o razonamientos al modelo_.

3. **Las capacidades del modelo varían.** Los modelos más nuevos pueden tener mejores habilidades, pero también presentan desafíos únicos en cuanto a costo o complejidad. _La ingeniería de indicaciones puede ayudarnos a desarrollar prácticas y flujos de trabajo que se adapten a cada modelo, ocultando las diferencias y haciendo las soluciones más escalables y reutilizables_.

Veámoslo en acción en el OpenAI o Azure OpenAI Playground:

- Usa el mismo prompt con diferentes implementaciones de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face). Viste las diferencias?
- Usa el mismo prompt varias veces con la _misma_ implementación (por ejemplo, en Azure OpenAI Playground). Las respuestas fueron iguales o diferentes?

### Ejemplo de Fabricaciones

En este curso, usamos el término **"fabricación"** para referirnos al fenómeno en el cual los LLMs generan información incorrecta debido a limitaciones en su entrenamiento u otros factores. Puede que hayas visto este comportamiento llamado _“alucinaciones”_ en artículos o investigaciones, pero recomendamos usar “fabricación” para evitar atribuir características humanas a un modelo de IA. Esto también respeta las [guías de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst), que recomiendan evitar términos potencialmente ofensivos o no inclusivos.

Quieres ver un ejemplo de fabricación? Intenta un prompt que le pida a la IA generar contenido sobre un tema ficticio (que sabemos que no existe). Por ejemplo:

> **Prompt:** genera un plan de clase sobre la Guerra Marciana del 2076.

Una búsqueda web muestra que existen relatos ficticios (series o libros) sobre guerras marcianas, pero ninguna en 2076. Además, el sentido común nos dice que 2076 es _el futuro_, por lo tanto no puede referirse a un evento real.

Veamos qué ocurre al usar este prompt en distintos modelos:

> **Respuesta 1**: OpenAI Playground (GPT-3.5)

![Respuesta 1](../../images/04-fabrication-oai.png?WT.mc_id=academic-105485-koreyst)

> **Respuesta 2**: Azure OpenAI Playground (GPT-3.5)

![Respuesta 2](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **Respuesta 3**: Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../images/04-fabrication-huggingchat.png?WT.mc_id=academic-105485-koreyst)

Como era de esperarse, cada modelo (o versión) produce respuestas ligeramente distintas debido al comportamiento estocástico y a las variaciones entre modelos. Por ejemplo, un modelo puede adaptar la respuesta a un público de octavo grado, mientras otro la dirige a estudiantes de secundaria. Pero todos generan respuestas _aparentemente plausibles_ sobre un evento que no ocurrió.

Técnicas de ingeniería de indicaciones como _indicaciones meta_ o la configuración de _temperature_ pueden ayudar a reducir las fabricaciones. También existen nuevas _arquitecturas_ para ingeniería de indicaciones que integran herramientas y técnicas directamente en el flujo del prompt para mitigar estos efectos.

## Estudio de Caso: GitHub Copilot

Para cerrar esta sección, veamos cómo se aplica la ingeniería de indicaciones en soluciones del mundo real a través de un caso práctico: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "programador asistente con IA" — convierte indicaciones de texto en sugerencias de código y se integra directamente en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia fluida. Según documenta esta serie de publicaciones, la primera versión se basaba en el modelo OpenAI Codex, y los ingenieros rápidamente se dieron cuenta de la necesidad de afinar el modelo y desarrollar mejores técnicas de ingeniería de indicaciones para mejorar la calidad del código generado. En julio, [presentaron un modelo de IA mejorado que va más allá de Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para generar sugerencias más rápidas y eficientes.

Lee las siguientes publicaciones en orden cronológico para seguir su recorrido de aprendizaje:

- **Mayo 2023** | [GitHub Copilot mejora en la comprensión de tu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: cómo trabajan con los LLMs detrás de Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Junio 2023** | [Cómo escribir mejores indicaciones para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Copilot va más allá de Codex con un modelo de IA mejorado](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Guía para desarrolladores sobre ingeniería de indicaciones y LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septiembre 2023** | [Cómo construir una aplicación empresarial con LLMs: lecciones de GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

También puedes explorar el [blog de Ingeniería de GitHub](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para encontrar más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst), que muestra cómo estos modelos y técnicas se _aplican_ en aplicaciones del mundo real.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #2.
Reinforce the concept with examples and references.

CONCEPT #2:
Prompt Design.
Illustrated with examples.
-->

## Construcción de Indicaciones

Ya vimos por qué la ingeniería de indicaciones es importante — ahora entendamos cómo se _construyen_ los indicaciones para evaluar diferentes técnicas que permitan diseñarlos de manera más efectiva.

### Prompt Básico

Comencemos con el prompt más básico: una entrada de texto enviada al modelo sin ningún contexto adicional. Por ejemplo, cuando enviamos las primeras palabras del himno nacional de EE. UU. al [API de Completion de OpenAI](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst), el modelo completa la secuencia con las siguientes líneas, ilustrando el comportamiento básico de predicción.

| Prompt (Entrada)     | Completion (Salida)                                                                                                                                   |
| :------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see   | Parece que estás comenzando la letra de "The Star-Spangled Banner", el himno nacional de los Estados Unidos. La letra completa es...                |

### Prompt Complejo

Ahora agreguemos contexto e instrucciones al prompt básico. El [API de Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir indicaciones complejos como una colección de _mensajes_ que incluyen:

- Pares de entrada/salida que reflejan la interacción _usuario-asistente_.
- Un mensaje del sistema que establece el contexto o comportamiento deseado del asistente.

La solicitud ahora tiene este formato, donde la _tokenización_ captura la información relevante del contexto y de la conversación. Cambiar el mensaje del sistema puede impactar tanto como las entradas del usuario.

```python
response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "Quién ganó la Serie Mundial en 2020?"},
        {"role": "assistant", "content": "Los Dodgers de Los Ángeles ganaron la Serie Mundial en 2020."},
        {"role": "user", "content": "Dónde se jugó?"}
    ]
)
```

### Instrucción

En los ejemplos anteriores, la instrucción del usuario era una consulta de texto simple que puede interpretarse como una solicitud de información. Con las instrucciones _instruction_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando una mejor guía a la IA. Ejemplo:

| Instrucción (Entrada) | Finalización (Salida) | Tipo de instrucción |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| Escribir una descripción de la Guerra Civil | _devolvió un párrafo simple_ | Simple |
| Escribir una descripción de la Guerra Civil. Indique fechas y eventos clave y describa su importancia | _devolvió un párrafo seguido de una lista de fechas de eventos clave con descripciones_ | Complejo |
| Escribir una descripción de la Guerra Civil en un párrafo. Indique tres viñetas con fechas clave y su importancia. Indique tres viñetas más con figuras históricas clave y sus contribuciones. Devuelva el resultado como un archivo JSON | _devuelve detalles más extensos en un cuadro de texto, con formato JSON, que puedes copiar y pegar en un archivo y validar según sea necesario_ | Complejo. Formato. |

## Contenido Primario

En los ejemplos anteriores, el prompt era bastante abierto, lo que permitía al LLM decidir qué parte de su conjunto de entrenamiento era relevante. Con el diseño de _contenido primario_, la entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí tienes un ejemplo donde la instrucción es "resume esto en 2 oraciones":

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Completion (Salida)                                                                                                                                                                                                                                                                             |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa mil veces menor que la del Sol, pero dos veces y media la masa de todos los demás planetas juntos. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por las civilizaciones antiguas desde antes de la historia escrita. Lleva el nombre del dios romano Júpiter.[19] Cuando se observa desde la Tierra, Júpiter puede ser lo suficientemente brillante como para proyectar sombras visibles,[20] y es en promedio el tercer objeto natural más brillante en el cielo nocturno después de la Luna y Venus. <br/> **Resume esto en 2 oraciones.** | Júpiter, el quinto planeta desde el Sol, es el más grande del Sistema Solar y uno de los objetos más brillantes del cielo nocturno. Nombrado en honor al dios romano Júpiter, es un gigante gaseoso cuya masa supera la de todos los demás planetas combinados. |

El segmento de contenido primario se puede usar de varias formas para generar instrucciones más efectivas:

- **Ejemplos** – en lugar de decirle explícitamente al modelo qué hacer, le das ejemplos de lo que debe generar y permites que infiera el patrón.
- **Señales** – después de la instrucción, agregas una "señal" que inicia el tipo de respuesta deseada.
- **Plantillas** – recetas reutilizables para indicaciones con espacios reservados (variables) que se pueden personalizar para casos de uso específicos.

Exploremos estos enfoques en acción.

### Uso de Ejemplos

Este enfoque consiste en alimentar al modelo con algunos ejemplos del resultado deseado para una tarea, permitiéndole inferir el patrón. Según cuántos ejemplos proporciones, puedes tener prompting de tipo cero, uno o pocos disparos (zero-shot, one-shot, few-shot).

El prompt ahora tiene tres componentes:

- Una descripción de la tarea
- Unos pocos ejemplos del resultado deseado
- El comienzo de un nuevo ejemplo (que se convierte en una descripción implícita de la tarea)

| Tipo de Aprendizaje | Prompt (Entrada)                                                                                                                      | Completion (Salida)           |
| :------------------ | :------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------- |
| Zero-shot           | "The Sun is Shining". Tradúcelo al español                                                                                           | "El Sol está brillando".      |
| One-shot            | "The Sun is Shining" => "El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                 | "Es un día frío y ventoso".   |
| Few-shot            | The player ran the bases => Béisbol <br/> The player hit an ace => Tenis <br/> The player hit a six => Críquet <br/> The player made a slam-dunk => | Baloncesto                    |

Nota cómo en el ejemplo zero-shot tuvimos que dar una instrucción explícita ("Tradúcelo al español"), pero en el one-shot el modelo infirió el patrón. En el few-shot, al darle más ejemplos, el modelo puede inferir con más precisión sin necesidad de instrucciones adicionales.

### Cues en Indicaciones

Otra técnica es proporcionar _señales_ (cues) en lugar de ejemplos. En este caso, estamos dando al modelo una pista o "inicio" de cómo debe continuar la respuesta.

| Nº de Cues | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Completion (Salida)                                                                                                                                                                                                                                                                               |
| :--------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0          | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa mil veces menor que la del Sol, pero dos veces y media la de todos los demás planetas. Es visible a simple vista y conocido desde tiempos antiguos. <br/>**Resúmelo**                                                                                           | Júpiter es el planeta más grande del Sistema Solar y el quinto desde el Sol. Es un gigante gaseoso visible en el cielo nocturno desde la antigüedad.                                                                                                                                             |
| 1          | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa mil veces menor que la del Sol, pero dos veces y media la de todos los demás planetas. <br/>**Resúmelo** <br/> Lo que aprendimos es que Júpiter...                                                                     | es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es visible desde la Tierra y ha sido conocido desde la antigüedad.                                                                                                                                                         |
| 2          | Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa mil veces menor que la del Sol, pero dos veces y media la de todos los demás planetas. <br/>**Resúmelo** <br/> Top 3 datos que aprendimos:                                              | 1. Júpiter es el quinto planeta desde el Sol y el más grande del Sistema Solar. <br/> 2. Es un gigante gaseoso cuya masa supera la de todos los otros planetas combinados. <br/> 3. Ha sido conocido desde tiempos antiguos y es muy visible en el cielo nocturno.                               |

### Plantillas de Indicaciones

Una plantilla de prompt es una _receta predefinida_ que puede guardarse y reutilizarse para generar experiencias consistentes. En su forma más simple, es una colección de ejemplos como [este de OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst), que incluye tanto los componentes del prompt como el formato de solicitud por API.

En su forma más compleja, como [esta en LangChain](https://python.langchain.com/docs/concepts/prompt_templates/?WT.mc_id=academic-105485-koreyst), incluye _variables_ que pueden reemplazarse con datos de distintas fuentes (input del usuario, contexto del sistema, fuentes externas, etc.) para generar el prompt dinámicamente.

El verdadero valor de las plantillas está en la posibilidad de crear y publicar _bibliotecas de indicaciones_ para dominios específicos — donde cada plantilla está _optimizadamente diseñada_ para reflejar el contexto o ejemplos más relevantes para ese tipo de aplicación. El repositorio [Indicaciones para Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un excelente ejemplo, con una colección curada para educación centrada en planificación de lecciones, diseño curricular, tutoría estudiantil, etc.

## Contenido de Apoyo

Si pensamos en la construcción de indicaciones como una combinación de instrucción (tarea) y contenido principal (contenido base), entonces el _contenido secundario_ es información adicional que proporcionamos para **influenciar la salida de alguna manera**. Puede tratarse de parámetros de ajuste, instrucciones de formato, taxonomías temáticas, etc., que ayudan al modelo a _adaptar_ su respuesta para que se alinee con los objetivos o expectativas del usuario.

Por ejemplo: dado un catálogo de cursos con meta datos extensos (nombre, descripción, nivel, etiquetas, instructor, etc.) sobre todos los cursos disponibles en el plan de estudios:

- Podemos definir una instrucción como "resume el catálogo de cursos para el semestre de otoño 2023".
- Podemos usar contenido primario para proporcionar algunos ejemplos del formato de salida deseado.
- Podemos usar contenido secundario para indicar las 5 etiquetas temáticas más importantes.

Así, el modelo puede generar un resumen que siga el formato mostrado en los ejemplos, pero si hay múltiples etiquetas por curso, puede priorizar aquellas que coincidan con las 5 etiquetas destacadas en el contenido secundario.

---

<!--
LESSON TEMPLATE:
This unit should cover core concept #1.
Reinforce the concept with examples and references.

CONCEPT #3:
Prompt Engineering Techniques.
What are some basic techniques for prompt engineering?
Illustrate it with some exercises.
-->

## Buenas Prácticas para Indicaciones

Ahora que sabemos cómo se pueden _construir_ los indicaciones, podemos comenzar a pensar en cómo _diseñarlos_ siguiendo buenas prácticas. Podemos dividir esto en dos partes: tener la _mentalidad correcta_ y aplicar las _técnicas adecuadas_.

### Mentalidad para la Ingeniería de Indicaciones

La Ingeniería de Indicaciones es un proceso de prueba y error, por lo que debes tener en cuenta tres principios generales:

1. **Entender el dominio es importante.** La precisión y relevancia de la respuesta dependen del _dominio_ en el que opera la aplicación o el usuario. Usa tu intuición y experiencia para **personalizar las técnicas**. Por ejemplo, define _personalidades específicas del dominio_ en los mensajes del sistema, o usa _plantillas específicas del dominio_ en los indicaciones del usuario. Proporciona contenido secundario que refleje ese contexto o usa _cues y ejemplos del dominio_ para guiar al modelo.

2. **Comprender el modelo es importante.** Sabemos que los modelos son estocásticos por naturaleza. Pero además, cada implementación puede variar en el conjunto de datos de entrenamiento, en sus capacidades (por ejemplo, API o SDK) y en el tipo de contenido que mejor manejan (texto, código, imágenes, etc.). Conoce las fortalezas y limitaciones del modelo que estás usando y aplica ese conocimiento para _priorizar tareas_ o construir _plantillas optimizadas_.

3. **La iteración y validación importan.** Los modelos evolucionan rápidamente, al igual que las técnicas de prompting. Como experto en el dominio, puedes tener criterios únicos que no aplican a otros usuarios. Usa las herramientas de ingeniería de indicaciones para arrancar el proceso, luego itera y valida con tu intuición. Documenta tus hallazgos y crea una **base de conocimiento** (como bibliotecas de indicaciones) que sirva de punto de partida para otros.

### Buenas Prácticas

Estas son algunas recomendaciones comunes sugeridas por [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst):

| Qué hacer                          | Por qué                                                                                                                                                                                                                                       |
| :--------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Evalúa los modelos más recientes   | Las generaciones más nuevas suelen tener mejores resultados y características, aunque también pueden tener mayor costo. Evalúalos antes de hacer la migración.                                                                              |
| Separa instrucciones y contexto    | Algunos proveedores o modelos usan _delimitadores_ para distinguir claramente la instrucción, el contenido primario y el contenido secundario. Esto puede ayudar al modelo a asignar mejor el peso a los tokens.                            |
| Sé específico y claro              | Brinda más detalles sobre el contexto, resultado deseado, longitud, formato, estilo, etc. Esto mejora la calidad y coherencia de la respuesta. Captura estos formatos en plantillas reutilizables.                                         |
| Usa descripciones y ejemplos       | Los modelos responden mejor al enfoque de "mostrar y contar". Comienza con `zero-shot` (solo instrucciones) y luego mejora con `few-shot` (instrucciones + ejemplos). Usa analogías si es útil.                                           |
| Usa cues para iniciar respuestas   | Da al modelo un empujón con palabras o frases que inicien la salida deseada.                                                                                                                                                                 |
| Refuerza instrucciones importantes | A veces hay que repetir la instrucción. Puedes ponerla antes y después del contenido primario, o combinar una instrucción con un cue. Prueba diferentes formas.                                                                             |
| El orden importa                   | El orden de la información puede afectar la salida, incluso dentro de los ejemplos. La _recencia_ puede influir. Experimenta.                                                                                                                |
| Dale al modelo una “salida”        | Proporciona una respuesta alternativa si el modelo no puede completar la tarea. Esto reduce el riesgo de respuestas falsas o fabricadas.                                                                                                     |

Como toda buena práctica, recuerda que _tu experiencia puede variar_ según el modelo, la tarea y el dominio. Usa estas recomendaciones como punto de partida y ajusta según tus necesidades. Revisa constantemente tu proceso de prompting a medida que aparezcan nuevos modelos y herramientas, priorizando escalabilidad y calidad en las respuestas.

<!--
LESSON TEMPLATE:
This unit should provide a code challenge if applicable

CHALLENGE:
Link to a Jupyter Notebook with only the code comments in the instructions (code sections are empty).

SOLUTION:
Link to a copy of that Notebook with the indicaciones filled in and run, showing what one example could be.
-->

## Asignación

Felicidades! Llegaste al final de la lección. Es hora de poner en práctica algunos de los conceptos y técnicas con ejemplos reales.

Para esta actividad, usaremos un Jupyter Notebook con ejercicios que puedes completar de forma interactiva. También puedes extender el Notebook con tus propias celdas de Markdown y Código para explorar ideas y técnicas por tu cuenta.

### Para comenzar, haz un fork del repositorio y luego:

- (Recomendado) Lanza un GitHub Codespace
- (Alternativa) Clona el repositorio en tu dispositivo local y úsalo con Docker Desktop
- (Alternativa) Abre el Notebook con tu entorno de ejecución preferido

### Luego, configura tus variables de entorno

- Copia el archivo `.env.copy` ubicado en la raíz del repositorio y renómbralo a `.env`. Llena los valores de `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT`. Si no sabes cómo hacerlo, vuelve a la sección [Entorno de Práctica](./04-prompt-engineering-fundamentals#learning-sandbox).

### Por último, abre el Notebook

- Selecciona el kernel de ejecución. Si usas Codespaces o Docker, selecciona el kernel de Python 3.10.x proporcionado por el contenedor de desarrollo.

Ya estás listo para ejecutar los ejercicios. Nota que no hay respuestas “correctas o incorrectas” — solo estás explorando mediante prueba y error para desarrollar tu intuición según el modelo y el dominio de tu aplicación.

_Por esta razón, esta lección no incluye secciones de "Solución de Código". En su lugar, el Notebook tendrá celdas de Markdown tituladas "Mi solución:" que mostrarán un ejemplo de salida como referencia._

## Verificación de Conocimiento

Cuál de los siguientes es un buen prompt siguiendo buenas prácticas razonables?

1. Muéstrame una imagen de un carro rojo  
2. Muéstrame una imagen de un carro rojo, marca Volvo y modelo XC90, estacionado junto a un acantilado con el atardecer de fondo  
3. Muéstrame una imagen de un carro rojo, marca Volvo y modelo XC90

**Respuesta**: 2 — es el mejor prompt porque proporciona detalles sobre "qué" se desea y va más allá: no es cualquier carro, sino una marca y modelo específicos, además de describir el entorno. El número 3 también es bueno, ya que contiene una descripción detallada.

## 🚀 Desafío

Prueba la técnica de "cue" con el siguiente prompt:

> Completa la frase: "Muéstrame una imagen de un carro rojo, marca Volvo y "

Qué respuesta te da? Cómo la mejorarías?

## Buen trabajo! Continúa aprendiendo

Quieres seguir aprendiendo más sobre conceptos de Ingeniería de Indicaciones? Visita la [página de aprendizaje continuo](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para encontrar otros recursos sobre este tema.

Ve al capítulo 5, donde exploraremos [técnicas avanzadas de prompting](../../../05-advanced-prompts/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst).
