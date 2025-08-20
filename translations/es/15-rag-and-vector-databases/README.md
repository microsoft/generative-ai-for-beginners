<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-07-09T16:01:44+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "es"
}
-->
# Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales

[![Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales](../../../translated_images/15-lesson-banner.ac49e59506175d4fc6ce521561dab2f9ccc6187410236376cfaed13cde371b90.es.png)](https://aka.ms/gen-ai-lesson15-gh?WT.mc_id=academic-105485-koreyst)

En la lección de aplicaciones de búsqueda, aprendimos brevemente cómo integrar tus propios datos en los Modelos de Lenguaje Grande (LLMs). En esta lección, profundizaremos en los conceptos de fundamentar tus datos en tu aplicación LLM, la mecánica del proceso y los métodos para almacenar datos, incluyendo tanto embeddings como texto.

> **Video próximamente**

## Introducción

En esta lección cubriremos lo siguiente:

- Una introducción a RAG, qué es y por qué se usa en IA (inteligencia artificial).

- Entender qué son las bases de datos vectoriales y cómo crear una para nuestra aplicación.

- Un ejemplo práctico de cómo integrar RAG en una aplicación.

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Explicar la importancia de RAG en la recuperación y procesamiento de datos.

- Configurar una aplicación RAG y fundamentar tus datos en un LLM.

- Integrar eficazmente RAG y bases de datos vectoriales en aplicaciones LLM.

## Nuestro escenario: mejorar nuestros LLMs con nuestros propios datos

Para esta lección, queremos añadir nuestras propias notas a la startup educativa, lo que permitirá que el chatbot obtenga más información sobre las diferentes materias. Usando las notas que tenemos, los estudiantes podrán estudiar mejor y comprender los distintos temas, facilitando la revisión para sus exámenes. Para crear nuestro escenario, usaremos:

- `Azure OpenAI:` el LLM que usaremos para crear nuestro chatbot

- `Lección AI para principiantes sobre Redes Neuronales:` estos serán los datos sobre los que fundamentaremos nuestro LLM

- `Azure AI Search` y `Azure Cosmos DB:` base de datos vectorial para almacenar nuestros datos y crear un índice de búsqueda

Los usuarios podrán crear cuestionarios de práctica a partir de sus notas, tarjetas de repaso y resumirlas en resúmenes concisos. Para comenzar, veamos qué es RAG y cómo funciona:

## Generación Aumentada por Recuperación (RAG)

Un chatbot impulsado por un LLM procesa las indicaciones del usuario para generar respuestas. Está diseñado para ser interactivo y participar con los usuarios en una amplia variedad de temas. Sin embargo, sus respuestas están limitadas al contexto proporcionado y a sus datos de entrenamiento base. Por ejemplo, el conocimiento de GPT-4 se corta en septiembre de 2021, lo que significa que no tiene información sobre eventos posteriores a esa fecha. Además, los datos usados para entrenar los LLMs excluyen información confidencial como notas personales o manuales de productos de una empresa.

### Cómo funcionan los RAGs (Generación Aumentada por Recuperación)

![dibujo que muestra cómo funcionan los RAGs](../../../translated_images/how-rag-works.f5d0ff63942bd3a638e7efee7a6fce7f0787f6d7a1fca4e43f2a7a4d03cde3e0.es.png)

Supongamos que quieres desplegar un chatbot que cree cuestionarios a partir de tus notas, necesitarás una conexión a la base de conocimiento. Aquí es donde RAG entra en acción. Los RAGs operan de la siguiente manera:

- **Base de conocimiento:** Antes de la recuperación, estos documentos deben ser ingeridos y preprocesados, normalmente dividiendo documentos grandes en fragmentos más pequeños, transformándolos en embeddings de texto y almacenándolos en una base de datos.

- **Consulta del usuario:** el usuario hace una pregunta

- **Recuperación:** Cuando un usuario hace una pregunta, el modelo de embedding recupera información relevante de nuestra base de conocimiento para proporcionar más contexto que se incorporará en la indicación.

- **Generación aumentada:** el LLM mejora su respuesta basándose en los datos recuperados. Esto permite que la respuesta generada no solo se base en datos preentrenados, sino también en información relevante del contexto añadido. Los datos recuperados se usan para aumentar las respuestas del LLM. Luego, el LLM devuelve una respuesta a la pregunta del usuario.

![dibujo que muestra la arquitectura de los RAGs](../../../translated_images/encoder-decode.f2658c25d0eadee2377bb28cf3aee8b67aa9249bf64d3d57bb9be077c4bc4e1a.es.png)

La arquitectura de los RAGs se implementa usando transformers que constan de dos partes: un codificador y un decodificador. Por ejemplo, cuando un usuario hace una pregunta, el texto de entrada se 'codifica' en vectores que capturan el significado de las palabras y los vectores se 'decodifican' en nuestro índice de documentos y generan nuevo texto basado en la consulta del usuario. El LLM usa un modelo codificador-decodificador para generar la salida.

Dos enfoques para implementar RAG según el artículo propuesto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) son:

- **_RAG-Sequence_** usa documentos recuperados para predecir la mejor respuesta posible a una consulta del usuario

- **RAG-Token** usa documentos para generar el siguiente token, luego los recupera para responder a la consulta del usuario

### ¿Por qué usarías RAGs?

- **Riqueza de información:** asegura que las respuestas de texto estén actualizadas y sean actuales. Por lo tanto, mejora el rendimiento en tareas específicas de dominio al acceder a la base de conocimiento interna.

- Reduce la fabricación de información utilizando **datos verificables** en la base de conocimiento para proporcionar contexto a las consultas del usuario.

- Es **rentable**, ya que son más económicos en comparación con el ajuste fino de un LLM.

## Creando una base de conocimiento

Nuestra aplicación se basa en nuestros datos personales, es decir, la lección de Redes Neuronales del currículo AI For Beginners.

### Bases de datos vectoriales

Una base de datos vectorial, a diferencia de las bases de datos tradicionales, es una base especializada diseñada para almacenar, gestionar y buscar vectores embebidos. Almacena representaciones numéricas de documentos. Descomponer los datos en embeddings numéricos facilita que nuestro sistema de IA entienda y procese la información.

Almacenamos nuestros embeddings en bases de datos vectoriales porque los LLMs tienen un límite en la cantidad de tokens que aceptan como entrada. Como no puedes pasar todos los embeddings a un LLM, necesitaremos dividirlos en fragmentos y cuando un usuario haga una pregunta, se devolverán los embeddings más relacionados junto con la indicación. Dividir en fragmentos también reduce los costos por la cantidad de tokens que se pasan a través de un LLM.

Algunas bases de datos vectoriales populares incluyen Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant y DeepLake. Puedes crear un modelo Azure Cosmos DB usando Azure CLI con el siguiente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```

### De texto a embeddings

Antes de almacenar nuestros datos, necesitaremos convertirlos en embeddings vectoriales antes de guardarlos en la base de datos. Si trabajas con documentos grandes o textos largos, puedes dividirlos en fragmentos basados en las consultas que esperas. La división puede hacerse a nivel de oración o párrafo. Como la división deriva significados de las palabras que la rodean, puedes añadir otro contexto a un fragmento, por ejemplo, añadiendo el título del documento o incluyendo algo de texto antes o después del fragmento. Puedes dividir los datos de la siguiente manera:

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

Una vez divididos, podemos incrustar nuestro texto usando diferentes modelos de embedding. Algunos modelos que puedes usar incluyen: word2vec, ada-002 de OpenAI, Azure Computer Vision y muchos más. La selección del modelo dependerá de los idiomas que uses, el tipo de contenido codificado (texto/imágenes/audio), el tamaño de entrada que puede codificar y la longitud de la salida del embedding.

Un ejemplo de texto embebido usando el modelo `text-embedding-ada-002` de OpenAI es:
![un embedding de la palabra cat](../../../translated_images/cat.74cbd7946bc9ca380a8894c4de0c706a4f85b16296ffabbf52d6175df6bf841e.es.png)

## Recuperación y búsqueda vectorial

Cuando un usuario hace una pregunta, el recuperador la transforma en un vector usando el codificador de consultas, luego busca en nuestro índice de búsqueda de documentos los vectores relevantes relacionados con la entrada. Una vez hecho esto, convierte tanto el vector de entrada como los vectores de documentos en texto y los pasa al LLM.

### Recuperación

La recuperación ocurre cuando el sistema intenta encontrar rápidamente los documentos del índice que cumplen con los criterios de búsqueda. El objetivo del recuperador es obtener documentos que se usarán para proporcionar contexto y fundamentar el LLM en tus datos.

Hay varias formas de realizar búsquedas dentro de nuestra base de datos, tales como:

- **Búsqueda por palabra clave** - usada para búsquedas de texto

- **Búsqueda semántica** - usa el significado semántico de las palabras

- **Búsqueda vectorial** - convierte documentos de texto a representaciones vectoriales usando modelos de embedding. La recuperación se realiza consultando los documentos cuyas representaciones vectoriales están más cercanas a la pregunta del usuario.

- **Híbrida** - combinación de búsqueda por palabra clave y búsqueda vectorial.

Un desafío con la recuperación surge cuando no hay una respuesta similar a la consulta en la base de datos, el sistema devolverá la mejor información que pueda obtener, sin embargo, puedes usar tácticas como establecer la distancia máxima para relevancia o usar búsqueda híbrida que combina palabras clave y búsqueda vectorial. En esta lección usaremos búsqueda híbrida, una combinación de búsqueda vectorial y por palabra clave. Almacenaremos nuestros datos en un dataframe con columnas que contienen los fragmentos así como los embeddings.

### Similitud vectorial

El recuperador buscará en la base de conocimiento embeddings que estén cerca entre sí, el vecino más cercano, ya que son textos similares. En el escenario, cuando un usuario hace una consulta, primero se embebe y luego se empareja con embeddings similares. La medida común que se usa para encontrar qué tan similares son diferentes vectores es la similitud coseno, que se basa en el ángulo entre dos vectores.

Podemos medir la similitud usando otras alternativas como la distancia euclidiana, que es la línea recta entre los extremos de los vectores, y el producto punto, que mide la suma de los productos de los elementos correspondientes de dos vectores.

### Índice de búsqueda

Al hacer la recuperación, necesitaremos construir un índice de búsqueda para nuestra base de conocimiento antes de realizar la búsqueda. Un índice almacenará nuestros embeddings y podrá recuperar rápidamente los fragmentos más similares incluso en una base de datos grande. Podemos crear nuestro índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Create the search index
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# To query the index, you can use the kneighbors method
distances, indices = nbrs.kneighbors(embeddings)
```

### Reordenamiento

Una vez que hayas consultado la base de datos, puede que necesites ordenar los resultados desde los más relevantes. Un LLM de reordenamiento utiliza Machine Learning para mejorar la relevancia de los resultados de búsqueda ordenándolos desde los más relevantes. Usando Azure AI Search, el reordenamiento se hace automáticamente para ti usando un reordenador semántico. Un ejemplo de cómo funciona el reordenamiento usando vecinos más cercanos:

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

## Integrándolo todo

El último paso es añadir nuestro LLM a la mezcla para poder obtener respuestas fundamentadas en nuestros datos. Podemos implementarlo de la siguiente manera:

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

### Métricas de evaluación

- Calidad de las respuestas proporcionadas, asegurando que suenen naturales, fluidas y humanas

- Fundamentación de los datos: evaluar si la respuesta proviene de los documentos suministrados

- Relevancia: evaluar si la respuesta coincide y está relacionada con la pregunta realizada

- Fluidez: si la respuesta tiene sentido gramaticalmente

## Casos de uso para RAG (Generación Aumentada por Recuperación) y bases de datos vectoriales

Existen muchos casos de uso donde las llamadas a funciones pueden mejorar tu aplicación, como:

- Preguntas y respuestas: fundamentar los datos de tu empresa en un chat que pueda ser usado por empleados para hacer preguntas.

- Sistemas de recomendación: donde puedes crear un sistema que empareje los valores más similares, por ejemplo, películas, restaurantes y muchos más.

- Servicios de chatbot: puedes almacenar el historial de chat y personalizar la conversación según los datos del usuario.

- Búsqueda de imágenes basada en embeddings vectoriales, útil para reconocimiento de imágenes y detección de anomalías.

## Resumen

Hemos cubierto las áreas fundamentales de RAG desde añadir nuestros datos a la aplicación, la consulta del usuario y la salida. Para simplificar la creación de RAG, puedes usar frameworks como Semantic Kernel, Langchain o Autogen.

## Tarea

Para continuar tu aprendizaje sobre Generación Aumentada por Recuperación (RAG) puedes construir:

- Crear un front-end para la aplicación usando el framework de tu elección

- Utilizar un framework, ya sea LangChain o Semantic Kernel, y recrear tu aplicación.

Felicidades por completar la lección 👏.

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos en IA Generativa.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.