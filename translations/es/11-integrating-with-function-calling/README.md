<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f6f84f9ef2d066cd25850cab93580a50",
  "translation_date": "2025-10-17T22:46:21+00:00",
  "source_file": "11-integrating-with-function-calling/README.md",
  "language_code": "es"
}
-->
# Integración con llamadas a funciones

[![Integración con llamadas a funciones](../../../translated_images/11-lesson-banner.d78860d3e1f041e2c3426b1c052e1590738d2978db584a08efe1efbca299ed82.es.png)](https://youtu.be/DgUdCLX8qYQ?si=f1ouQU5HQx6F8Gl2)

Has aprendido bastante en las lecciones anteriores. Sin embargo, podemos mejorar aún más. Algunos aspectos que podemos abordar son cómo obtener un formato de respuesta más consistente para facilitar el trabajo con la respuesta en etapas posteriores. Además, podríamos querer agregar datos de otras fuentes para enriquecer aún más nuestra aplicación.

Los problemas mencionados anteriormente son los que este capítulo busca resolver.

## Introducción

Esta lección cubrirá:

- Explicar qué es la llamada a funciones y sus casos de uso.
- Crear una llamada a funciones utilizando Azure OpenAI.
- Cómo integrar una llamada a funciones en una aplicación.

## Objetivos de aprendizaje

Al final de esta lección, podrás:

- Explicar el propósito de usar llamadas a funciones.
- Configurar llamadas a funciones utilizando el servicio Azure OpenAI.
- Diseñar llamadas a funciones efectivas para el caso de uso de tu aplicación.

## Escenario: Mejorando nuestro chatbot con funciones

En esta lección, queremos construir una funcionalidad para nuestra startup educativa que permita a los usuarios usar un chatbot para encontrar cursos técnicos. Recomendaremos cursos que se ajusten a su nivel de habilidad, rol actual y tecnología de interés.

Para completar este escenario, utilizaremos una combinación de:

- `Azure OpenAI` para crear una experiencia de chat para el usuario.
- `Microsoft Learn Catalog API` para ayudar a los usuarios a encontrar cursos según su solicitud.
- `Llamadas a funciones` para tomar la consulta del usuario y enviarla a una función para realizar la solicitud a la API.

Para comenzar, veamos por qué querríamos usar llamadas a funciones en primer lugar:

## Por qué usar llamadas a funciones

Antes de las llamadas a funciones, las respuestas de un LLM eran no estructuradas e inconsistentes. Los desarrolladores tenían que escribir código de validación complejo para asegurarse de poder manejar cada variación de una respuesta. Los usuarios no podían obtener respuestas como "¿Cuál es el clima actual en Estocolmo?". Esto se debe a que los modelos estaban limitados al momento en que se entrenaron los datos.

Las llamadas a funciones son una característica del servicio Azure OpenAI para superar las siguientes limitaciones:

- **Formato de respuesta consistente**. Si podemos controlar mejor el formato de la respuesta, podemos integrar más fácilmente la respuesta en otros sistemas.
- **Datos externos**. Capacidad de usar datos de otras fuentes de una aplicación en un contexto de chat.

## Ilustrando el problema a través de un escenario

> Te recomendamos usar el [notebook incluido](./python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) si deseas ejecutar el siguiente escenario. También puedes simplemente leer mientras intentamos ilustrar un problema donde las funciones pueden ayudar a resolverlo.

Veamos un ejemplo que ilustra el problema del formato de respuesta:

Supongamos que queremos crear una base de datos de datos de estudiantes para poder sugerirles el curso adecuado. A continuación, tenemos dos descripciones de estudiantes que son muy similares en los datos que contienen.

1. Crear una conexión con nuestro recurso Azure OpenAI:

   ```python
   import os
   import json
   from openai import AzureOpenAI
   from dotenv import load_dotenv
   load_dotenv()

   client = AzureOpenAI(
   api_key=os.environ['AZURE_OPENAI_API_KEY'],  # this is also the default, it can be omitted
   api_version = "2023-07-01-preview"
   )

   deployment=os.environ['AZURE_OPENAI_DEPLOYMENT']
   ```

   A continuación, hay un código en Python para configurar nuestra conexión con Azure OpenAI donde configuramos `api_type`, `api_base`, `api_version` y `api_key`.

1. Crear dos descripciones de estudiantes utilizando las variables `student_1_description` y `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Queremos enviar las descripciones de estudiantes anteriores a un LLM para analizar los datos. Estos datos pueden usarse más tarde en nuestra aplicación y enviarse a una API o almacenarse en una base de datos.

1. Creemos dos indicaciones idénticas en las que instruimos al LLM sobre qué información nos interesa:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   Las indicaciones anteriores instruyen al LLM para extraer información y devolver la respuesta en formato JSON.

1. Después de configurar las indicaciones y la conexión con Azure OpenAI, ahora enviaremos las indicaciones al LLM utilizando `openai.ChatCompletion`. Almacenamos la indicación en la variable `messages` y asignamos el rol a `user`. Esto es para imitar un mensaje de un usuario escrito a un chatbot.

   ```python
   # response from prompt one
   openai_response1 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1.choices[0].message.content

   # response from prompt two
   openai_response2 = client.chat.completions.create(
   model=deployment,
   messages = [{'role': 'user', 'content': prompt2}]
   )
   openai_response2.choices[0].message.content
   ```

Ahora podemos enviar ambas solicitudes al LLM y examinar la respuesta que recibimos encontrándola así: `openai_response1['choices'][0]['message']['content']`.

1. Por último, podemos convertir la respuesta al formato JSON llamando a `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1.choices[0].message.content)
   json_response1
   ```

   Respuesta 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Respuesta 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Aunque las indicaciones son las mismas y las descripciones son similares, vemos valores de la propiedad `Grades` formateados de manera diferente, ya que a veces obtenemos el formato `3.7` o `3.7 GPA`, por ejemplo.

   Este resultado se debe a que el LLM toma datos no estructurados en forma de indicación escrita y también devuelve datos no estructurados. Necesitamos tener un formato estructurado para saber qué esperar al almacenar o usar estos datos.

Entonces, ¿cómo resolvemos el problema de formato? Usando llamadas a funciones, podemos asegurarnos de recibir datos estructurados. Al usar llamadas a funciones, el LLM no llama ni ejecuta realmente ninguna función. En su lugar, creamos una estructura para que el LLM la siga en sus respuestas. Luego usamos esas respuestas estructuradas para saber qué función ejecutar en nuestras aplicaciones.

![flujo de funciones](../../../translated_images/Function-Flow.083875364af4f4bb69bd6f6ed94096a836453183a71cf22388f50310ad6404de.es.png)

Luego podemos tomar lo que se devuelve de la función y enviarlo de vuelta al LLM. El LLM responderá utilizando lenguaje natural para responder a la consulta del usuario.

## Casos de uso para usar llamadas a funciones

Hay muchos casos de uso diferentes donde las llamadas a funciones pueden mejorar tu aplicación, como:

- **Llamar herramientas externas**. Los chatbots son excelentes para proporcionar respuestas a preguntas de los usuarios. Al usar llamadas a funciones, los chatbots pueden usar mensajes de los usuarios para completar ciertas tareas. Por ejemplo, un estudiante puede pedirle al chatbot: "Envía un correo electrónico a mi instructor diciendo que necesito más ayuda con este tema". Esto puede hacer una llamada a la función `send_email(to: string, body: string)`.

- **Crear consultas de API o base de datos**. Los usuarios pueden encontrar información utilizando lenguaje natural que se convierte en una consulta o solicitud de API formateada. Un ejemplo de esto podría ser un profesor que solicita: "¿Quiénes son los estudiantes que completaron la última tarea?", lo que podría llamar a una función llamada `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Crear datos estructurados**. Los usuarios pueden tomar un bloque de texto o CSV y usar el LLM para extraer información importante de él. Por ejemplo, un estudiante puede convertir un artículo de Wikipedia sobre acuerdos de paz para crear tarjetas de memoria AI. Esto se puede hacer utilizando una función llamada `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Creando tu primera llamada a funciones

El proceso de crear una llamada a funciones incluye 3 pasos principales:

1. **Llamar** a la API de Chat Completions con una lista de tus funciones y un mensaje del usuario.
2. **Leer** la respuesta del modelo para realizar una acción, es decir, ejecutar una función o llamada a API.
3. **Hacer** otra llamada a la API de Chat Completions con la respuesta de tu función para usar esa información y crear una respuesta para el usuario.

![Flujo LLM](../../../translated_images/LLM-Flow.3285ed8caf4796d7343c02927f52c9d32df59e790f6e440568e2e951f6ffa5fd.es.png)

### Paso 1 - Crear mensajes

El primer paso es crear un mensaje de usuario. Esto puede asignarse dinámicamente tomando el valor de una entrada de texto o puedes asignar un valor aquí. Si es tu primera vez trabajando con la API de Chat Completions, necesitamos definir el `role` y el `content` del mensaje.

El `role` puede ser `system` (creando reglas), `assistant` (el modelo) o `user` (el usuario final). Para llamadas a funciones, lo asignaremos como `user` y una pregunta de ejemplo.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Al asignar diferentes roles, queda claro para el LLM si es el sistema diciendo algo o el usuario, lo que ayuda a construir un historial de conversación que el LLM puede usar como base.

### Paso 2 - Crear funciones

A continuación, definiremos una función y los parámetros de esa función. Usaremos solo una función aquí llamada `search_courses`, pero puedes crear múltiples funciones.

> **Importante**: Las funciones se incluyen en el mensaje del sistema al LLM y se incluirán en la cantidad de tokens disponibles que tienes.

A continuación, creamos las funciones como un array de elementos. Cada elemento es una función y tiene las propiedades `name`, `description` y `parameters`:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Describamos cada instancia de función más en detalle:

- `name` - El nombre de la función que queremos que se llame.
- `description` - Esta es la descripción de cómo funciona la función. Aquí es importante ser específico y claro.
- `parameters` - Una lista de valores y formato que deseas que el modelo produzca en su respuesta. El array de parámetros consiste en elementos donde los elementos tienen las siguientes propiedades:
  1.  `type` - El tipo de datos en el que se almacenarán las propiedades.
  1.  `properties` - Lista de los valores específicos que el modelo usará para su respuesta.
      1. `name` - La clave es el nombre de la propiedad que el modelo usará en su respuesta formateada, por ejemplo, `product`.
      1. `type` - El tipo de datos de esta propiedad, por ejemplo, `string`.
      1. `description` - Descripción de la propiedad específica.

También hay una propiedad opcional `required` - propiedad requerida para que se complete la llamada a la función.

### Paso 3 - Hacer la llamada a la función

Después de definir una función, ahora necesitamos incluirla en la llamada a la API de Chat Completion. Hacemos esto agregando `functions` a la solicitud. En este caso `functions=functions`.

También hay una opción para configurar `function_call` como `auto`. Esto significa que dejaremos que el LLM decida qué función debe llamarse según el mensaje del usuario en lugar de asignarla nosotros mismos.

Aquí hay un código a continuación donde llamamos a `ChatCompletion.create`, observa cómo configuramos `functions=functions` y `function_call="auto"` y, por lo tanto, le damos al LLM la opción de cuándo llamar a las funciones que le proporcionamos:

```python
response = client.chat.completions.create(model=deployment,
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto")

print(response.choices[0].message)
```

La respuesta que regresa ahora se ve así:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Aquí podemos ver cómo se llamó a la función `search_courses` y con qué argumentos, como se indica en la propiedad `arguments` en la respuesta JSON.

La conclusión es que el LLM pudo encontrar los datos para ajustar los argumentos de la función mientras los extraía del valor proporcionado al parámetro `messages` en la llamada de chat completions. A continuación, se muestra un recordatorio del valor de `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Como puedes ver, `student`, `Azure` y `beginner` se extrajeron de `messages` y se configuraron como entrada para la función. Usar funciones de esta manera es una excelente forma de extraer información de una indicación, pero también de proporcionar estructura al LLM y tener funcionalidad reutilizable.

A continuación, necesitamos ver cómo podemos usar esto en nuestra aplicación.

## Integrando llamadas a funciones en una aplicación

Después de haber probado la respuesta formateada del LLM, ahora podemos integrar esto en una aplicación.

### Gestionando el flujo

Para integrar esto en nuestra aplicación, sigamos los siguientes pasos:

1. Primero, hagamos la llamada a los servicios de OpenAI y almacenemos el mensaje en una variable llamada `response_message`.

   ```python
   response_message = response.choices[0].message
   ```

1. Ahora definiremos la función que llamará a la API de Microsoft Learn para obtener una lista de cursos:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   Observa cómo ahora creamos una función de Python real que se corresponde con los nombres de función introducidos en la variable `functions`. También estamos haciendo llamadas reales a API externas para obtener los datos que necesitamos. En este caso, vamos contra la API de Microsoft Learn para buscar módulos de formación.

Ok, entonces creamos variables `functions` y una función de Python correspondiente, ¿cómo le decimos al LLM cómo mapear estas dos juntas para que se llame nuestra función de Python?

1. Para ver si necesitamos llamar a una función de Python, necesitamos mirar la respuesta del LLM y ver si `function_call` es parte de ella y llamar a la función señalada. Aquí está cómo puedes hacer la verificación mencionada a continuación:

   ```python
   # Check if the model wants to call a function
   if response_message.function_call.name:
    print("Recommended Function call:")
    print(response_message.function_call.name)
    print()

    # Call the function.
    function_name = response_message.function_call.name

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message.function_call.arguments)
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message.role,
            "function_call": {
                "name": function_name,
                "arguments": response_message.function_call.arguments,
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   Estas tres líneas aseguran que extraemos el nombre de la función, los argumentos y hacemos la llamada:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message.function_call.arguments)
   function_response = function_to_call(**function_args)
   ```

   A continuación se muestra la salida de ejecutar nuestro código:

   **Salida**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Ahora enviaremos el mensaje actualizado, `messages`, al LLM para que podamos recibir una respuesta en lenguaje natural en lugar de una respuesta formateada en JSON de la API.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = client.chat.completions.create(
      messages=messages,
      model=deployment,
      function_call="auto",
      functions=functions,
      temperature=0
         )  # get a new response from GPT where it can see the function response


   print(second_response.choices[0].message)
   ```

   **Salida**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Tarea

Para continuar tu aprendizaje sobre Azure OpenAI Function Calling puedes construir:

- Más parámetros de la función que puedan ayudar a los estudiantes a encontrar más cursos.
- Crear otra llamada a función que tome más información del estudiante, como su idioma nativo.
- Crea un manejo de errores cuando la llamada a la función y/o la llamada a la API no devuelva ningún curso adecuado.

Sugerencia: Consulta la página de [documentación de referencia de la API de Learn](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) para ver cómo y dónde está disponible esta información.

## ¡Buen trabajo! Continúa el viaje

Después de completar esta lección, revisa nuestra [colección de aprendizaje sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA generativa.

Dirígete a la Lección 12, donde exploraremos cómo [diseñar UX para aplicaciones de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.