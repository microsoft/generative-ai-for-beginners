[![Modelos de Código Abierto](../../../translated_images/es/17-lesson-banner.a5b918fb0920e4e6.webp)](https://youtu.be/yAXVW-lUINc?si=bOtW9nL6jc3XJgOM)

## Introducción

Los Agentes de IA representan un desarrollo emocionante en la IA Generativa, permitiendo que los Modelos de Lenguaje Grandes (LLMs) evolucionen de asistentes a agentes capaces de tomar acciones. Los marcos de trabajo de Agentes de IA permiten a los desarrolladores crear aplicaciones que brindan a los LLMs acceso a herramientas y gestión del estado. Estos marcos también mejoran la visibilidad, permitiendo a los usuarios y desarrolladores monitorear las acciones planificadas por los LLMs, mejorando así la gestión de la experiencia.

La lección cubrirá las siguientes áreas:

- Entender qué es un Agente de IA - ¿Qué es exactamente un Agente de IA?
- Explorar cinco diferentes marcos de trabajo para Agentes de IA - ¿Qué los hace únicos?
- Aplicar estos Agentes de IA a diferentes casos de uso - ¿Cuándo deberíamos usar Agentes de IA?

## Objetivos de aprendizaje

Después de tomar esta lección, podrás:

- Explicar qué son los Agentes de IA y cómo pueden ser usados.
- Tener comprensión de las diferencias entre algunos de los marcos de trabajo populares para Agentes de IA, y cómo difieren.
- Entender cómo funcionan los Agentes de IA para construir aplicaciones con ellos.

## ¿Qué Son los Agentes de IA?

Los Agentes de IA son un campo muy emocionante en el mundo de la IA Generativa. Con esta emoción a veces viene una confusión sobre términos y su aplicación. Para mantener las cosas simples e incluir la mayoría de las herramientas que se refieren a Agentes de IA, utilizaremos esta definición:

Los Agentes de IA permiten que los Modelos de Lenguaje Grandes (LLMs) realicen tareas dándoles acceso a un **estado** y **herramientas**.

![Modelo de Agente](../../../translated_images/es/what-agent.21f2893bdfd01e6a.webp)

Definamos estos términos:

**Modelos de Lenguaje Grandes** - Estos son los modelos mencionados a lo largo de este curso como GPT-5, GPT-4o, y Llama 3.3, etc.

**Estado** - Se refiere al contexto en el que el LLM está trabajando. El LLM utiliza el contexto de sus acciones pasadas y el contexto actual para guiar su toma de decisiones para las acciones subsecuentes. Los marcos de trabajo de Agentes de IA permiten a los desarrolladores mantener este contexto más fácilmente.

**Herramientas** - Para completar la tarea que el usuario ha solicitado y que el LLM ha planificado, el LLM necesita acceso a herramientas. Algunos ejemplos de herramientas pueden ser una base de datos, una API, una aplicación externa o incluso otro LLM.

Estas definiciones, esperamos, te darán una buena base para avanzar mientras exploramos cómo se implementan. Vamos a explorar algunos diferentes marcos de trabajo para Agentes de IA:

## Agentes LangChain

[Agentes LangChain](https://python.langchain.com/docs/how_to/#agents?WT.mc_id=academic-105485-koreyst) es una implementación de las definiciones que proporcionamos arriba.

Para gestionar el **estado** , utiliza una función incorporada llamada `AgentExecutor`. Esta acepta el `agent` definido y las `tools` disponibles para él.

El `Agent Executor` también almacena el historial de chat para proporcionar el contexto de la conversación.

![Agentes Langchain](../../../translated_images/es/langchain-agents.edcc55b5d5c43716.webp)

LangChain ofrece un [catálogo de herramientas](https://integrations.langchain.com/tools?WT.mc_id=academic-105485-koreyst) que pueden importarse a tu aplicación y a las que el LLM puede acceder. Estas son hechas por la comunidad y por el equipo de LangChain.

Luego puedes definir estas herramientas y pasarlas al `Agent Executor`.

La visibilidad es otro aspecto importante cuando hablamos de Agentes de IA. Es importante para los desarrolladores de aplicaciones entender qué herramienta está usando el LLM y por qué. Para eso, el equipo de LangChain ha desarrollado LangSmith.

## AutoGen

El siguiente marco de trabajo para Agentes de IA que discutiremos es [AutoGen](https://microsoft.github.io/autogen/?WT.mc_id=academic-105485-koreyst). El enfoque principal de AutoGen son las conversaciones. Los agentes son tanto **conversables** como **personalizables**.

**Conversable -** Los LLMs pueden iniciar y continuar una conversación con otro LLM para completar una tarea. Esto se hace creando `AssistantAgents` y dándoles un mensaje de sistema específico.

```python

autogen.AssistantAgent( name="Coder", llm_config=llm_config, ) pm = autogen.AssistantAgent( name="Product_manager", system_message="Creative in software product ideas.", llm_config=llm_config, )

```

**Personalizables** - Los agentes pueden definirse no solo como LLMs sino también como usuario o herramienta. Como desarrollador, puedes definir un `UserProxyAgent` que es responsable de interactuar con el usuario para obtener retroalimentación en la realización de una tarea. Esta retroalimentación puede continuar la ejecución de la tarea o detenerla.

```python
user_proxy = UserProxyAgent(name="user_proxy")
```

### Estado y Herramientas

Para cambiar y gestionar el estado, un Agente asistente genera código Python para completar la tarea.

Aquí hay un ejemplo del proceso:

![AutoGen](../../../translated_images/es/autogen.dee9a25a45fde584.webp)

#### LLM Definido con un Mensaje de Sistema

```python
system_message="For weather related tasks, only use the functions you have been provided with. Reply TERMINATE when the task is done."
```

Este mensaje de sistema dirige a este LLM específico cuáles funciones son relevantes para su tarea. Recuerda, con AutoGen puedes tener múltiples AssistantAgents definidos con diferentes mensajes de sistema.

#### Chat Iniciado por el Usuario

```python
user_proxy.initiate_chat( chatbot, message="I am planning a trip to NYC next week, can you help me pick out what to wear? ", )

```

Este mensaje del user_proxy (Humano) es lo que iniciará el proceso del Agente para explorar las posibles funciones que debe ejecutar.

#### Función Ejecutada

```bash
chatbot (to user_proxy):

***** Suggested tool Call: get_weather ***** Arguments: {"location":"New York City, NY","time_periond:"7","temperature_unit":"Celsius"} ******************************************************** --------------------------------------------------------------------------------

>>>>>>>> EXECUTING FUNCTION get_weather... user_proxy (to chatbot): ***** Response from calling function "get_weather" ***** 112.22727272727272 EUR ****************************************************************

```

Una vez que se procesa el chat inicial, el Agente enviará la herramienta sugerida para llamar. En este caso, es una función llamada `get_weather`. Dependiendo de tu configuración, esta función puede ejecutarse automáticamente y ser leída por el Agente o puede ejecutarse según la entrada del usuario.

Puedes encontrar una lista de [ejemplos de código de AutoGen](https://microsoft.github.io/autogen/docs/Examples/?WT.mc_id=academic-105485-koreyst) para explorar más cómo comenzar a construir.

## Microsoft Agent Framework

[Microsoft Agent Framework](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst) es el SDK de código abierto de Microsoft para construir Agentes de IA y sistemas multiagente en **Python** y **.NET**. Reúne las fortalezas de dos proyectos anteriores de Microsoft, las características empresariales de **Semantic Kernel** y la orquestación multiagente de **AutoGen**, en un solo marco de trabajo soportado. Si estás comenzando un nuevo proyecto de agente hoy, esta es la sucesora recomendada de AutoGen.

El marco escala desde un solo **agente de chat** hasta complejos **flujos de trabajo multiagente** y se integra directamente con Microsoft Foundry, Azure OpenAI y OpenAI. También proporciona observabilidad incorporada a través de OpenTelemetry para que puedas trazar exactamente lo que están haciendo tus agentes.

### Estado y Herramientas

**Estado** - El marco gestiona el contexto de la conversación por ti a través de **hilos**. Un agente mantiene el historial de mensajes (solicitudes de usuario, llamadas a herramientas y sus resultados), para que cada turno se construya sobre los anteriores. Los hilos también pueden persistirse, permitiendo pausar y reanudar la conversación después.

**Herramientas** - Le das herramientas a un agente pasando funciones Python simples. Los parámetros anotados con tipos se convierten automáticamente en un esquema, así el modelo sabe cómo y cuándo llamarlas (llamado de función). El marco también soporta servidores del Protocolo de Contexto de Modelo (MCP) y herramientas alojadas como un intérprete de código.

Aquí hay un ejemplo de un agente único con una herramienta personalizada:

```python
import asyncio
from typing import Annotated

from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient


def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    return f"The weather in {location} is sunny with a high of 22°C."


async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can answer weather questions.",
        tools=[get_weather],
    )

    response = await agent.run("What's the weather in Amsterdam?")
    print(response)


asyncio.run(main())
```

Para conectarte a Azure OpenAI en Microsoft Foundry en cambio, pasa tu endpoint y credenciales al cliente:

```python
from azure.identity.aio import AzureCliCredential
from agent_framework.openai import OpenAIChatClient

client = OpenAIChatClient(
    model="my-gpt-5-mini-deployment",
    azure_endpoint="https://my-resource.openai.azure.com",
    credential=AzureCliCredential(),
)
```

### Flujos de trabajo multiagente

Donde el marco realmente destaca es en la orquestación de varios agentes juntos. Por ejemplo, puedes ejecutar agentes uno tras otro (cada uno pasando su contexto al siguiente) o repartir a varios agentes en paralelo y agregar sus resultados:

```python
from agent_framework.orchestrations import SequentialBuilder, ConcurrentBuilder

# Ejecutar agentes en secuencia, pasando el contexto de la conversación a lo largo de la cadena
sequential = SequentialBuilder(participants=[researcher, writer, editor]).build()

# Expandir a agentes en paralelo, luego agregar sus respuestas
concurrent = ConcurrentBuilder(participants=[analyst_a, analyst_b, analyst_c]).build()
```

Para instalar el marco y comenzar:

```bash
pip install agent-framework-core
# Integraciones opcionales
pip install agent-framework-openai       # OpenAI y Azure OpenAI
pip install agent-framework-foundry      # Microsoft Foundry
```

Puedes explorar más en el [repositorio Microsoft Agent Framework](https://github.com/microsoft/agent-framework?WT.mc_id=academic-105485-koreyst) y la [documentación oficial](https://learn.microsoft.com/agent-framework/?WT.mc_id=academic-105485-koreyst).

## Taskweaver

El siguiente marco de agentes que exploraremos es [Taskweaver](https://microsoft.github.io/TaskWeaver/?WT.mc_id=academic-105485-koreyst). Es conocido como un agente "orientado al código" porque en lugar de trabajar estrictamente con `strings`, puede trabajar con DataFrames en Python. Esto se vuelve extremadamente útil para tareas de análisis y generación de datos. Esto puede incluir crear gráficos y tablas o generar números aleatorios.

### Estado y Herramientas

Para gestionar el estado de la conversación, TaskWeaver usa el concepto de un `Planner`. El `Planner` es un LLM que toma la solicitud de los usuarios y mapea las tareas que deben completarse para cumplir con esta solicitud.

Para completar las tareas, el `Planner` tiene acceso a la colección de herramientas llamadas `Plugins`. Esto pueden ser clases de Python o un intérprete de código general. Estos plugins se almacenan como embeddings para que el LLM pueda buscar mejor el plugin correcto.

![Taskweaver](../../../translated_images/es/taskweaver.da8559999267715a.webp)

Aquí hay un ejemplo de un plugin para manejar la detección de anomalías:

```python
class AnomalyDetectionPlugin(Plugin): def __call__(self, df: pd.DataFrame, time_col_name: str, value_col_name: str):
```

El código es verificado antes de ejecutarse. Otra característica para gestionar el contexto en Taskweaver es la `experiencia`. La experiencia permite que el contexto de una conversación se almacene a largo plazo en un archivo YAML. Esto puede configurarse para que el LLM mejore con el tiempo en ciertas tareas dado que se expone a conversaciones previas.

## JARVIS

El último marco de agentes que exploraremos es [JARVIS](https://github.com/microsoft/JARVIS?tab=readme-ov-file&WT.mc_id=academic-105485-koreyst). Lo que hace que JARVIS sea único es que usa un LLM para gestionar el `estado` de la conversación y las `herramientas` son otros modelos de IA. Cada uno de los modelos de IA son modelos especializados que realizan ciertas tareas como detección de objetos, transcripción o subtitulado de imágenes.

![JARVIS](../../../translated_images/es/jarvis.762ddbadbd1a3a33.webp)

El LLM, siendo un modelo de propósito general, recibe la solicitud del usuario y identifica la tarea específica y cualquier argumento/dato que se necesite para completar la tarea.

```python
[{"task": "object-detection", "id": 0, "dep": [-1], "args": {"image": "e1.jpg" }}]
```

Luego el LLM formatea la solicitud de una manera que el modelo de IA especializado pueda interpretar, como JSON. Una vez que el modelo de IA ha devuelto su predicción basada en la tarea, el LLM recibe la respuesta.

Si se requieren múltiples modelos para completar la tarea, también interpretará la respuesta de esos modelos antes de reunirlas para generar la respuesta al usuario.

El siguiente ejemplo muestra cómo funcionaría esto cuando un usuario solicita una descripción y conteo de objetos en una imagen:

## Tarea

Para continuar aprendiendo sobre Agentes de IA puedes construir con Microsoft Agent Framework:

- Una aplicación que simule una reunión de negocios con diferentes departamentos de una startup educativa.
- Crear mensajes de sistema que guíen a los LLMs a entender diferentes personas y prioridades, y permitir al usuario presentar una nueva idea de producto.
- El LLM debería luego generar preguntas de seguimiento de cada departamento para refinar y mejorar la presentación y la idea del producto.

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento en IA Generativa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->