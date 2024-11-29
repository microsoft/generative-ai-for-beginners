[![Modelos de Código Abierto](../../../translated_images/17-lesson-banner.png?WT.d223296926e27d95f6b5a748e3f77ab9a1b669d4f9aebe608f926cbb44ea08a8.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson17-gh?WT.mc_id=academic-105485-koreyst)

## Introducción

Los Agentes de IA representan un desarrollo emocionante en la IA Generativa, permitiendo que los Modelos de Lenguaje Extenso (LLMs) evolucionen de asistentes a agentes capaces de tomar acciones. Los marcos de trabajo de Agentes de IA permiten a los desarrolladores crear aplicaciones que otorgan a los LLMs acceso a herramientas y gestión de estado. Estos marcos también mejoran la visibilidad, permitiendo a usuarios y desarrolladores monitorear las acciones planificadas por los LLMs, mejorando así la gestión de la experiencia.

La lección cubrirá las siguientes áreas:

- Comprender qué es un Agente de IA - ¿Qué es exactamente un Agente de IA?
- Explorar cuatro marcos de trabajo diferentes de Agentes de IA - ¿Qué los hace únicos?
- Aplicar estos Agentes de IA a diferentes casos de uso - ¿Cuándo deberíamos usar Agentes de IA?

## Objetivos de aprendizaje

Después de tomar esta lección, podrás:

- Explicar qué son los Agentes de IA y cómo se pueden usar.
- Tener una comprensión de las diferencias entre algunos de los marcos de trabajo populares de Agentes de IA, y cómo difieren.
- Entender cómo funcionan los Agentes de IA para construir aplicaciones con ellos.

## ¿Qué son los Agentes de IA?

Los Agentes de IA son un campo muy emocionante en el mundo de la IA Generativa. Con esta emoción a veces viene una confusión de términos y su aplicación. Para simplificar las cosas e incluir la mayoría de las herramientas que se refieren a Agentes de IA, vamos a usar esta definición:

Los Agentes de IA permiten que los Modelos de Lenguaje Extenso (LLMs) realicen tareas dándoles acceso a un **estado** y **herramientas**.

![Modelo de Agente](../../../translated_images/what-agent.png?WT.96b2eb171bd613cd0652fb5a2c1f488c80fde8d3405db76d780603041a415cb3.es.mc_id=academic-105485-koreyst)

Definamos estos términos:

**Modelos de Lenguaje Extenso** - Estos son los modelos mencionados a lo largo de este curso como GPT-3.5, GPT-4, Llama-2, etc.

**Estado** - Esto se refiere al contexto en el que el LLM está trabajando. El LLM utiliza el contexto de sus acciones pasadas y el contexto actual, guiando su toma de decisiones para acciones subsecuentes. Los marcos de trabajo de Agentes de IA permiten a los desarrolladores mantener este contexto más fácilmente.

**Herramientas** - Para completar la tarea que el usuario ha solicitado y que el LLM ha planificado, el LLM necesita acceso a herramientas. Algunos ejemplos de herramientas pueden ser una base de datos, una API, una aplicación externa o incluso otro LLM.

Estas definiciones, con suerte, te darán una buena base a medida que avanzamos en cómo se implementan. Vamos a explorar algunos marcos de trabajo de Agentes de IA diferentes:

## Agentes de LangChain

[Agentes de LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) es una implementación de las definiciones que proporcionamos anteriormente.

Para gestionar el **estado**, utiliza una función incorporada llamada `AgentExecutor`. Esta acepta el `agent` definido y el `tools` que están disponibles para ella.

El `Agent Executor` también almacena el historial de chat para proporcionar el contexto del chat.

![Agentes de Langchain](../../../translated_images/langchain-agents.png?WT.311575a86262a6e33490477b281688373d96e3392dbfe3094965470531a9f111.es.mc_id=academic-105485-koreyst)

LangChain ofrece un [catálogo de herramientas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que se pueden importar a tu aplicación en la que el LLM puede obtener acceso. Estas son creadas por la comunidad y por el equipo de LangChain.

Luego puedes definir estas herramientas y pasarlas al `Agent Executor`.

La visibilidad es otro aspecto importante cuando hablamos de Agentes de IA. Es importante para los desarrolladores de aplicaciones entender qué herramienta está usando el LLM y por qué. Para eso, el equipo de LangChain ha desarrollado LangSmith.

## AutoGen

El siguiente marco de trabajo de Agentes de IA que discutiremos es [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). El enfoque principal de AutoGen son las conversaciones. Los agentes son tanto **conversables** como **personalizables**.

**Conversable -** Los LLMs pueden iniciar y continuar una conversación con otro LLM para completar una tarea. Esto se hace creando `AssistantAgents` y dándoles un mensaje de sistema específico.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizable** - Los agentes pueden definirse no solo como LLMs, sino como un usuario o una herramienta. Como desarrollador, puedes definir un `UserProxyAgent` que es responsable de interactuar con el usuario para obtener retroalimentación en la realización de una tarea. Esta retroalimentación puede continuar la ejecución de la tarea o detenerla.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado y Herramientas

Para cambiar y gestionar el estado, un agente asistente genera código Python para completar la tarea.

Aquí hay un ejemplo del proceso:

![AutoGen](../../../translated_images/autogen.png?WT.45c9474fbd6109577f4363559f022554e796000ea2d677b80021b00e6ca0d869.es.mc_id=academic-105485-koreyst)

#### LLM Definido con un Mensaje de Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Este mensaje del sistema dirige a este LLM específico a qué funciones son relevantes para su tarea. Recuerda, con AutoGen puedes tener múltiples AssistantAgents definidos con diferentes mensajes del sistema.

#### El Chat es Iniciado por el Usuario

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Este mensaje del user_proxy (Humano) es lo que iniciará el proceso del Agente para explorar las posibles funciones que debería ejecutar.

#### La Función es Ejecutada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Una vez que el chat inicial es procesado, el Agente enviará la herramienta sugerida para llamar. En este caso, es una función llamada `get_weather`. Depending on your configuration, this function can be automatically executed and read by the Agent or can be executed based on user input.

You can find a list of [AutoGen code samples](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) to further explore how to get started building.

## Taskweaver

The next agent framework we will explore is [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). It is known as a "code-first" agent because instead of working strictly with `strings` , it can work with DataFrames in Python. This becomes extremely useful for data analysis and generation tasks. This can be things like creating graphs and charts or generating random numbers.

### State and Tools

To manage the state of the conversation, TaskWeaver uses the concept of a `Planner`. The `Planner` is a LLM that takes the request from the users and maps out the tasks that need to be completed to fulfill this request.

To complete the tasks the `Planner` is exposed to the collection of tools called `Plugins`. Esto puede ser clases de Python o un intérprete de código general. Estos plugins se almacenan como incrustaciones para que el LLM pueda buscar mejor el plugin correcto.

![Taskweaver](../../../translated_images/taskweaver.png?WT.c5d336793941a5af0d2489ad6d88a03f09557bd5ca68a954f1ddaa3d9f1ecc3b.es.mc_id=academic-105485-koreyst)

Aquí hay un ejemplo de un plugin para manejar la detección de anomalías:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

El código se verifica antes de ejecutarse. Otra característica para gestionar el contexto en Taskweaver es `experience`. Experience allows for the context of a conversation to be stored over to the long term in a YAML file. This can be configured so that the LLM improves over time on certain tasks given that it is exposed to prior conversations.

## JARVIS

The last agent framework we will explore is [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file?WT.mc_id=academic-105485-koreyst). What makes JARVIS unique is that it uses an LLM to manage the `state` de la conversación y el `tools` son otros modelos de IA. Cada uno de los modelos de IA son modelos especializados que realizan ciertas tareas como detección de objetos, transcripción o subtitulado de imágenes.

![JARVIS](../../../translated_images/jarvis.png?WT.f12468c52a0c4848aeed51606a0e53a36eb38c65cc6c821597ea4dcaad03d1a3.es.mc_id=academic-105485-koreyst)

El LLM, siendo un modelo de propósito general, recibe la solicitud del usuario e identifica la tarea específica y cualquier argumento/dato que se necesite para completar la tarea.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

El LLM luego formatea la solicitud de una manera que el modelo de IA especializado pueda interpretar, como JSON. Una vez que el modelo de IA ha devuelto su predicción basada en la tarea, el LLM recibe la respuesta.

Si se requieren múltiples modelos para completar la tarea, también interpretará la respuesta de esos modelos antes de reunirlos para generar la respuesta al usuario.

El ejemplo a continuación muestra cómo funcionaría esto cuando un usuario solicita una descripción y conteo de los objetos en una imagen:

## Tarea

Para continuar tu aprendizaje de Agentes de IA puedes construir con AutoGen:

- Una aplicación que simula una reunión de negocios con diferentes departamentos de una startup educativa.
- Crear mensajes de sistema que guíen a los LLMs en la comprensión de diferentes personalidades y prioridades, y permitan al usuario presentar una nueva idea de producto.
- El LLM debería entonces generar preguntas de seguimiento de cada departamento para refinar y mejorar la presentación y la idea del producto.

## El aprendizaje no se detiene aquí, continúa el viaje

Después de completar esta lección, revisa nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos de IA Generativa.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática por inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción humana profesional. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.