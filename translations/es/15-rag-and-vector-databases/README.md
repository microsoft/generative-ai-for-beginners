# Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales

[![Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales](../../../translated_images/15-lesson-banner.png?WT.ae1ec4b596c9c2b74121dd24c30143380d4789a9ef381276dbbc9fd5d7abc3d5.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

En la lección sobre aplicaciones de búsqueda, aprendimos brevemente cómo integrar tus propios datos en Modelos de Lenguaje de Gran Escala (LLMs). En esta lección, profundizaremos en los conceptos de fundamentar tus datos en tu aplicación LLM, la mecánica del proceso y los métodos para almacenar datos, incluyendo tanto incrustaciones como texto.

> **Video Próximamente**

## Introducción

En esta lección cubriremos lo siguiente:

- Una introducción a RAG, qué es y por qué se utiliza en la IA (inteligencia artificial).

- Comprender qué son las bases de datos vectoriales y crear una para nuestra aplicación.

- Un ejemplo práctico sobre cómo integrar RAG en una aplicación.

## Objetivos de Aprendizaje

Después de completar esta lección, serás capaz de:

- Explicar la importancia de RAG en la recuperación y procesamiento de datos.

- Configurar una aplicación RAG y fundamentar tus datos en un LLM.

- Integración efectiva de RAG y Bases de Datos Vectoriales en Aplicaciones LLM.

## Nuestro Escenario: mejorando nuestros LLMs con nuestros propios datos

Para esta lección, queremos agregar nuestras propias notas a la startup educativa, lo que permite al chatbot obtener más información sobre los diferentes temas. Usando las notas que tenemos, los estudiantes podrán estudiar mejor y comprender los diferentes temas, facilitando la revisión para sus exámenes. Para crear nuestro escenario, utilizaremos:

- `Azure OpenAI:` el LLM que usaremos para crear nuestro chatbot

- `AI for beginners' lesson on Neural Networks`: estos serán los datos en los que fundamentaremos nuestro LLM

- `Azure AI Search` y `Azure Cosmos DB:` base de datos vectorial para almacenar nuestros datos y crear un índice de búsqueda

Los usuarios podrán crear cuestionarios de práctica a partir de sus notas, tarjetas de revisión y resumirlas en visiones generales concisas. Para comenzar, veamos qué es RAG y cómo funciona:

## Generación Aumentada por Recuperación (RAG)

Un chatbot potenciado por LLM procesa las indicaciones del usuario para generar respuestas. Está diseñado para ser interactivo y relacionarse con los usuarios en una amplia gama de temas. Sin embargo, sus respuestas están limitadas al contexto proporcionado y sus datos de entrenamiento fundamentales. Por ejemplo, el límite de conocimiento de GPT-4 es septiembre de 2021, lo que significa que carece de conocimiento de eventos que han ocurrido después de este período. Además, los datos utilizados para entrenar LLMs excluyen información confidencial como notas personales o el manual de productos de una empresa.

### Cómo funcionan los RAGs (Generación Aumentada por Recuperación)

![dibujo que muestra cómo funcionan los RAGs](../../../translated_images/how-rag-works.png?WT.fde75879826c169b53e16dc0d0d6691172c75b314400f380d40a9f31244eba0e.es.mc_id=academic-105485-koreyst)

Supongamos que deseas implementar un chatbot que cree cuestionarios a partir de tus notas, necesitarás una conexión con la base de conocimiento. Aquí es donde RAG viene al rescate. Los RAGs operan de la siguiente manera:

- **Base de conocimiento:** Antes de la recuperación, estos documentos deben ser ingeridos y preprocesados, generalmente descomponiendo documentos grandes en fragmentos más pequeños, transformándolos en incrustaciones de texto y almacenándolos en una base de datos.

- **Consulta del Usuario:** el usuario hace una pregunta

- **Recuperación:** Cuando un usuario hace una pregunta, el modelo de incrustación recupera información relevante de nuestra base de conocimiento para proporcionar más contexto que se incorporará a la indicación.

- **Generación Aumentada:** el LLM mejora su respuesta en base a los datos recuperados. Permite que la respuesta generada no solo se base en datos preentrenados sino también en información relevante del contexto añadido. Los datos recuperados se utilizan para aumentar las respuestas del LLM. Luego, el LLM devuelve una respuesta a la pregunta del usuario.

![dibujo que muestra la arquitectura de los RAGs](../../../translated_images/encoder-decode.png?WT.80c3c9669a10e85d1f7e9dc7f7f0d416a71e16d2f8a6da93267e55cbfbddbf9f.es.mc_id=academic-105485-koreyst)

La arquitectura de los RAGs se implementa utilizando transformadores que constan de dos partes: un codificador y un decodificador. Por ejemplo, cuando un usuario hace una pregunta, el texto de entrada se 'codifica' en vectores que capturan el significado de las palabras y los vectores se 'decodifican' en nuestro índice de documentos y generan un nuevo texto basado en la consulta del usuario. El LLM utiliza tanto un modelo codificador-decodificador para generar la salida.

Dos enfoques al implementar RAG según el documento propuesto: [Generación Aumentada por Recuperación para Tareas de NLP (procesamiento de lenguaje natural) Intensivas en Conocimiento](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) son:

- **_RAG-Secuencia_** usando documentos recuperados para predecir la mejor respuesta posible a una consulta de usuario

- **RAG-Token** usando documentos para generar el siguiente token, luego recuperarlos para responder a la consulta del usuario

### ¿Por qué usarías RAGs?

- **Riqueza de información:** asegura que las respuestas de texto estén actualizadas y sean actuales. Por lo tanto, mejora el rendimiento en tareas específicas de dominio al acceder a la base de conocimiento interna.

- Reduce la fabricación utilizando **datos verificables** en la base de conocimiento para proporcionar contexto a las consultas de los usuarios.

- Es **rentable** ya que son más económicos en comparación con el ajuste fino de un LLM.

## Creación de una base de conocimiento

Nuestra aplicación se basa en nuestros datos personales, es decir, la lección de Redes Neuronales en el currículo de IA para Principiantes.

### Bases de Datos Vectoriales

Una base de datos vectorial, a diferencia de las bases de datos tradicionales, es una base de datos especializada diseñada para almacenar, gestionar y buscar vectores incrustados. Almacena representaciones numéricas de documentos. Descomponer datos en incrustaciones numéricas facilita que nuestro sistema de IA comprenda y procese los datos.

Almacenamos nuestras incrustaciones en bases de datos vectoriales ya que los LLMs tienen un límite en el número de tokens que aceptan como entrada. Como no puedes pasar todas las incrustaciones a un LLM, necesitaremos descomponerlas en fragmentos y cuando un usuario haga una pregunta, las incrustaciones más similares a la pregunta se devolverán junto con la indicación. La fragmentación también reduce los costos en el número de tokens que pasan por un LLM.

Algunas bases de datos vectoriales populares incluyen Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant y DeepLake. Puedes crear un modelo de Azure Cosmos DB usando Azure CLI con el siguiente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto a incrustaciones

Antes de almacenar nuestros datos, necesitaremos convertirlos en incrustaciones vectoriales antes de que se almacenen en la base de datos. Si estás trabajando con documentos grandes o textos largos, puedes fragmentarlos en función de las consultas que esperas. La fragmentación se puede hacer a nivel de oración o a nivel de párrafo. Como la fragmentación deriva significados de las palabras que los rodean, puedes agregar algún otro contexto a un fragmento, por ejemplo, agregando el título del documento o incluyendo algún texto antes o después del fragmento. Puedes fragmentar los datos de la siguiente manera:

```python
def split_text(text, max_length, min_length):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(' '.join(current_chunk)) < max_length and len(' '.join(current_chunk)) > min_length:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    # If the last chunk didn't reach the minimum length, add it anyway
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```

Una vez fragmentado, podemos incrustar nuestro texto usando diferentes modelos de incrustación. Algunos modelos que puedes usar incluyen: word2vec, ada-002 de OpenAI, Azure Computer Vision y muchos más. La selección de un modelo a usar dependerá de los idiomas que estés utilizando, el tipo de contenido codificado (texto/imágenes/audio), el tamaño de entrada que puede codificar y la longitud de la salida de incrustación.

Un ejemplo de texto incrustado usando el modelo `text-embedding-ada-002` de OpenAI es:
![una incrustación de la palabra gato](../../../translated_images/cat.png?WT.6f67a41409b2174c6f543273f4a9f8c38b227112a12831da3070e52f13e03818.es.mc_id=academic-105485-koreyst)

## Recuperación y Búsqueda Vectorial

Cuando un usuario hace una pregunta, el recuperador la transforma en un vector usando el codificador de consultas, luego busca en nuestro índice de búsqueda de documentos vectores relevantes en el documento que están relacionados con la entrada. Una vez hecho, convierte tanto el vector de entrada como los vectores de documentos en texto y lo pasa por el LLM.

### Recuperación

La recuperación ocurre cuando el sistema intenta encontrar rápidamente los documentos del índice que satisfacen los criterios de búsqueda. El objetivo del recuperador es obtener documentos que se utilizarán para proporcionar contexto y fundamentar el LLM en tus datos.

Hay varias maneras de realizar búsquedas dentro de nuestra base de datos, tales como:

- **Búsqueda por palabras clave** - utilizada para búsquedas de texto

- **Búsqueda semántica** - utiliza el significado semántico de las palabras

- **Búsqueda vectorial** - convierte documentos de texto a representaciones vectoriales usando modelos de incrustación. La recuperación se realizará consultando los documentos cuyas representaciones vectoriales están más cerca de la pregunta del usuario.

- **Híbrida** - una combinación de búsqueda por palabras clave y búsqueda vectorial.

Un desafío con la recuperación surge cuando no hay una respuesta similar a la consulta en la base de datos, el sistema entonces devolverá la mejor información que pueda obtener, sin embargo, puedes usar tácticas como establecer la distancia máxima para la relevancia o usar búsqueda híbrida que combine tanto palabras clave como búsqueda vectorial. En esta lección usaremos búsqueda híbrida, una combinación de búsqueda vectorial y por palabras clave. Almacenaremos nuestros datos en un marco de datos con columnas que contengan los fragmentos así como las incrustaciones.

### Similitud Vectorial

El recuperador buscará en la base de datos de conocimiento incrustaciones que estén cerca unas de otras, el vecino más cercano, ya que son textos que son similares. En el escenario en que un usuario hace una consulta, primero se incrusta y luego se empareja con incrustaciones similares. La medida común que se utiliza para encontrar cuán similares son diferentes vectores es la similitud del coseno, que se basa en el ángulo entre dos vectores.

Podemos medir la similitud usando otras alternativas que podemos usar son la distancia euclidiana, que es la línea recta entre los puntos finales de los vectores, y el producto punto, que mide la suma de los productos de los elementos correspondientes de dos vectores.

### Índice de Búsqueda

Al hacer la recuperación, necesitaremos construir un índice de búsqueda para nuestra base de conocimiento antes de realizar la búsqueda. Un índice almacenará nuestras incrustaciones y puede recuperar rápidamente los fragmentos más similares incluso en una base de datos grande. Podemos crear nuestro índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Reordenamiento

Una vez que hayas consultado la base de datos, es posible que necesites ordenar los resultados desde el más relevante. Un LLM de reordenamiento utiliza Aprendizaje Automático para mejorar la relevancia de los resultados de búsqueda ordenándolos desde el más relevante. Usando Azure AI Search, el reordenamiento se realiza automáticamente para ti usando un reordenador semántico. Un ejemplo de cómo funciona el reordenamiento usando vecinos más cercanos:

```python
# Find the most similar documents
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Print the most similar documents
for i in range(3):
    index = indices[0][i]
    for index in indices[0]:
        print(flattened_df['chunks'].iloc[index])
        print(flattened_df['path'].iloc[index])
        print(flattened_df['distances'].iloc[index])
    else:
        print(f"Index {index} not found in DataFrame")
```

## Uniendo todo

El último paso es agregar nuestro LLM a la mezcla para poder obtener respuestas que estén fundamentadas en nuestros datos. Podemos implementarlo de la siguiente manera:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convert the question to a query vector
    query_vector = create_embeddings(user_input)

    # Find the most similar documents
    distances, indices = nbrs.kneighbors([query_vector])

    # add documents to query  to provide context
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combine the history and the user input
    history.append(user_input)

    # create a message object
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": history[-1]}
    ]

    # use chat completion to generate a response
    response = openai.chat.completions.create(
        model="gpt-4",
        temperature=0.7,
        max_tokens=800,
        messages=messages
    )

    return response.choices[0].message

chatbot(user_input)
```

## Evaluando nuestra aplicación

### Métricas de Evaluación

- Calidad de las respuestas suministradas asegurando que suene natural, fluida y humana.

- Fundamentación de los datos: evaluar si la respuesta provino de los documentos suministrados.

- Relevancia: evaluar si la respuesta coincide y está relacionada con la pregunta realizada.

- Fluidez - si la respuesta tiene sentido gramaticalmente.

## Casos de Uso para usar RAG (Generación Aumentada por Recuperación) y bases de datos vectoriales

Existen muchos casos de uso diferentes donde las llamadas a funciones pueden mejorar tu aplicación como:

- Preguntas y Respuestas: fundamentar los datos de tu empresa a un chat que puede ser utilizado por empleados para hacer preguntas.

- Sistemas de Recomendación: donde puedes crear un sistema que empareje los valores más similares, por ejemplo, películas, restaurantes y muchos más.

- Servicios de Chatbot: puedes almacenar el historial de chat y personalizar la conversación en función de los datos del usuario.

- Búsqueda de imágenes basada en incrustaciones vectoriales, útil al hacer reconocimiento de imágenes y detección de anomalías.

## Resumen

Hemos cubierto las áreas fundamentales de RAG desde agregar nuestros datos a la aplicación, la consulta del usuario y la salida. Para simplificar la creación de RAG, puedes usar marcos como Semanti Kernel, Langchain o Autogen.

## Tarea

Para continuar tu aprendizaje de Generación Aumentada por Recuperación (RAG) puedes construir:

- Construir un front-end para la aplicación usando el marco de tu elección.

- Utilizar un marco, ya sea LangChain o Semantic Kernel, y recrear tu aplicación.

Felicidades por completar la lección 👏.

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tu conocimiento sobre IA Generativa.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.