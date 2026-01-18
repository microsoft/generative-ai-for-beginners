<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2210a0466c812d9defc4df2d9a709ff9",
  "translation_date": "2026-01-18T16:43:09+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "es"
}
-->
# Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales

[![Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales](../../../../../translated_images/es/15-lesson-banner.ac49e59506175d4f.webp)](https://youtu.be/4l8zhHUBeyI?si=BmvDmL1fnHtgQYkL)

En la lección de aplicaciones de búsqueda, aprendimos brevemente cómo integrar tus propios datos en Modelos de Lenguaje Grande (LLMs). En esta lección, profundizaremos en los conceptos de fundamentar tus datos en tu aplicación LLM, la mecánica del proceso y los métodos para almacenar datos, incluyendo tanto embeddings como texto.

> **Video Pronto Disponible**

## Introducción

En esta lección cubriremos lo siguiente:

- Una introducción a RAG, qué es y por qué se usa en IA (inteligencia artificial).

- Entender qué son las bases de datos vectoriales y crear una para nuestra aplicación.

- Un ejemplo práctico sobre cómo integrar RAG en una aplicación.

## Objetivos de aprendizaje

Después de completar esta lección, serás capaz de:

- Explicar la importancia de RAG en la recuperación y procesamiento de datos.

- Configurar una aplicación RAG y fundamentar tus datos en un LLM.

- Integrar efectivamente RAG y Bases de Datos Vectoriales en Aplicaciones LLM.

## Nuestro escenario: mejorando nuestros LLMs con nuestros propios datos

Para esta lección, queremos añadir nuestras propias notas a la startup educativa, lo que permite que el chatbot obtenga más información sobre las diferentes materias. Usando las notas que tenemos, los estudiantes podrán estudiar mejor y entender los distintos temas, facilitando la revisión para sus exámenes. Para crear nuestro escenario usaremos:

- `Azure OpenAI:` el LLM que usaremos para crear nuestro chatbot.

- `Lección AI para principiantes sobre Redes Neuronales:` estos serán los datos en los que fundamentaremos nuestro LLM.

- `Azure AI Search` y `Azure Cosmos DB:` base de datos vectorial para almacenar nuestros datos y crear un índice de búsqueda.

Los usuarios podrán crear cuestionarios de práctica a partir de sus notas, tarjetas de repaso y resumirlos en vistas concisas. Para comenzar, veamos qué es RAG y cómo funciona:

## Generación Aumentada por Recuperación (RAG)

Un chatbot potenciado por LLM procesa las indicaciones del usuario para generar respuestas. Está diseñado para ser interactivo y conversar con los usuarios sobre una amplia variedad de temas. Sin embargo, sus respuestas están limitadas al contexto proporcionado y sus datos de entrenamiento fundamentales. Por ejemplo, el conocimiento de GPT-4 se corta en septiembre de 2021, lo que significa que carece de conocimiento sobre eventos posteriores a ese periodo. Además, los datos usados para entrenar LLMs excluyen información confidencial como notas personales o el manual de productos de una empresa.

### Cómo funcionan los RAGs (Generación Aumentada por Recuperación)

![dibujo que muestra cómo funcionan los RAGs](../../../../../translated_images/es/how-rag-works.f5d0ff63942bd3a6.webp)

Supongamos que quieres desplegar un chatbot que crea cuestionarios a partir de tus notas, necesitarás una conexión a la base de conocimiento. Aquí es donde RAG viene al rescate. Los RAGs operan de la siguiente manera:

- **Base de conocimiento:** Antes de la recuperación, estos documentos necesitan ser ingeridos y preprocesados, normalmente dividiendo documentos grandes en trozos más pequeños, transformándolos en embeddings de texto y almacenándolos en una base de datos.

- **Consulta del usuario:** el usuario hace una pregunta.

- **Recuperación:** Cuando un usuario hace una pregunta, el modelo de embeddings recupera información relevante de nuestra base de conocimiento para proporcionar más contexto que se incorporará en la indicación.

- **Generación aumentada:** el LLM mejora su respuesta con base en los datos recuperados. Permite que la respuesta generada no solo se base en datos preentrenados sino también en información relevante del contexto añadido. Los datos recuperados se usan para aumentar las respuestas del LLM. Luego el LLM retorna una respuesta a la pregunta del usuario.

![dibujo que muestra la arquitectura de RAGs](../../../../../translated_images/es/encoder-decode.f2658c25d0eadee2.webp)

La arquitectura para RAGs se implementa usando transformadores que constan de dos partes: un codificador y un decodificador. Por ejemplo, cuando un usuario hace una pregunta, el texto de entrada es 'codificado' en vectores que capturan el significado de las palabras y los vectores son 'decodificados' en nuestro índice de documentos y genera texto nuevo basado en la consulta del usuario. El LLM usa un modelo codificador-decodificador para generar la salida.

Dos enfoques al implementar RAG según el artículo propuesto: [Retrieval-Augmented Generation for Knowledge intensive NLP (natural language processing software) Tasks](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) son:

- **_RAG-Sequence_** usando documentos recuperados para predecir la mejor respuesta posible a una consulta de usuario.

- **RAG-Token** usando documentos para generar el siguiente token, luego recuperarlos para responder a la consulta del usuario.

### ¿Por qué usarías RAGs? 

- **Riqueza de información:** asegura que las respuestas de texto estén actualizadas y sean actuales. Por lo tanto, mejora el rendimiento en tareas específicas del dominio accediendo a la base de conocimiento interna.

- Reduce la fabricación usando **datos verificables** en la base de conocimiento para proporcionar contexto a las consultas de los usuarios.

- Es **rentable** ya que es más económico que ajustar finamente un LLM.

## Creando una base de conocimiento

Nuestra aplicación está basada en nuestros datos personales, es decir, la lección de Redes Neuronales del currículo AI Para Principiantes.

### Bases de Datos Vectoriales

Una base de datos vectorial, a diferencia de bases de datos tradicionales, es una base de datos especializada diseñada para almacenar, gestionar y buscar vectores embebidos. Almacena representaciones numéricas de documentos. Descomponer los datos en embeddings numéricos facilita que nuestro sistema de IA entienda y procese los datos.

Almacenamos nuestros embeddings en bases de datos vectoriales ya que los LLMs tienen un límite en el número de tokens que aceptan como entrada. Como no puedes pasar todos los embeddings completos a un LLM, necesitaremos dividirlos en trozos y cuando un usuario haga una pregunta, se devolverán los embeddings más parecidos a la consulta junto con la indicación. Dividir también reduce costos en la cantidad de tokens que pasan por un LLM.

Algunas bases de datos vectoriales populares incluyen Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant y DeepLake. Puedes crear un modelo Azure Cosmos DB usando Azure CLI con el siguiente comando:

```bash
az login
az group create -n <resource-group-name> -l <location>
az cosmosdb create -n <cosmos-db-name> -r <resource-group-name>
az cosmosdb list-keys -n <cosmos-db-name> -g <resource-group-name>
```


### De texto a embeddings

Antes de almacenar nuestros datos, necesitaremos convertirlos en vectores embedding antes de almacenarlos en la base de datos. Si trabajas con documentos grandes o textos largos, puedes dividirlos en fragmentos basados en las consultas que esperas. La división puede hacerse a nivel de oraciones o párrafos. Como dividir extrae significados de las palabras alrededor, puedes añadir otro contexto a un fragmento, por ejemplo, añadiendo el título del documento o incluyendo algo de texto antes o después del fragmento. Puedes dividir los datos como sigue:

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

    # Si el último fragmento no alcanzó la longitud mínima, agréguelo de todos modos
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
```


Una vez divididos, podemos incrustar nuestro texto usando diferentes modelos de embeddings. Algunos modelos que puedes usar incluyen: word2vec, ada-002 de OpenAI, Azure Computer Vision y muchos más. La selección de un modelo dependerá de los idiomas que uses, el tipo de contenido codificado (texto/imágenes/audio), el tamaño de entrada que puede codificar y la longitud de salida del embedding.

Un ejemplo de texto embebido usando el modelo `text-embedding-ada-002` de OpenAI es:
![un embedding de la palabra gato](../../../../../translated_images/es/cat.74cbd7946bc9ca38.webp)

## Recuperación y búsqueda vectorial

Cuando un usuario hace una pregunta, el recuperador la transforma en un vector usando el codificador de consultas, luego busca en nuestro índice de búsqueda de documentos aquellos vectores relevantes en el documento relacionados con la entrada. Una vez hecho, convierte tanto el vector de entrada como los vectores del documento en texto y los pasa a través del LLM.

### Recuperación

La recuperación ocurre cuando el sistema intenta encontrar rápidamente los documentos del índice que cumplan con los criterios de búsqueda. El objetivo del recuperador es obtener documentos que se usarán para proporcionar contexto y fundamentar el LLM en tus datos.

Hay varias formas de realizar búsquedas dentro de nuestra base de datos tales como:

- **Búsqueda por palabra clave**: usada para búsquedas de texto.

- **Búsqueda vectorial**: convierte documentos de texto a representaciones vectoriales usando modelos de embeddings, permitiendo una **búsqueda semántica** basada en el significado de las palabras. La recuperación se hace consultando los documentos cuyas representaciones vectoriales estén más cerca de la pregunta del usuario.

- **Híbrida**: una combinación de búsqueda por palabra clave y vectorial.

Un desafío con la recuperación surge cuando no hay una respuesta similar a la consulta en la base de datos, el sistema entonces devolverá la mejor información que pueda obtener; sin embargo, puedes usar tácticas como establecer la distancia máxima para relevancia o usar búsqueda híbrida que combina ambas búsquedas: por palabras clave y vectoriales. En esta lección usaremos búsqueda híbrida, una combinación de ambas. Almacenaremos nuestros datos en un dataframe con columnas que contienen los fragmentos así como embeddings.

### Similitud Vectorial

El recuperador buscará en la base de conocimiento los embeddings que estén cercanos entre sí, el vecino más cercano, ya que son textos similares. En el escenario, cuando un usuario hace una consulta, primero se embebe y luego se empareja con embeddings similares. La medida comúnmente usada para encontrar cuán similares son diferentes vectores es la similitud coseno, que se basa en el ángulo entre dos vectores.

Podemos medir similitud usando otras alternativas como distancia euclidiana, que es la línea recta entre los puntos finales de vectores, y producto punto, que mide la suma de los productos de los elementos correspondientes de dos vectores.

### Índice de búsqueda

Al realizar recuperación, necesitaremos construir un índice de búsqueda para nuestra base de conocimiento antes de realizar la búsqueda. Un índice almacenará nuestros embeddings y podrá recuperar rápidamente los fragmentos más similares incluso en una base de datos grande. Podemos crear nuestro índice localmente usando:

```python
from sklearn.neighbors import NearestNeighbors

embeddings = flattened_df['embeddings'].to_list()

# Crear el índice de búsqueda
nbrs = NearestNeighbors(n_neighbors=5, algorithm='ball_tree').fit(embeddings)

# Para consultar el índice, puedes usar el método kneighbors
distances, indices = nbrs.kneighbors(embeddings)
```


### Reordenamiento

Una vez que has consultado la base de datos, podrías necesitar ordenar los resultados desde los más relevantes. Un LLM de reordenamiento utiliza aprendizaje automático para mejorar la relevancia de los resultados de búsqueda ordenándolos desde los más relevantes. Usando Azure AI Search, el reordenamiento se realiza automáticamente para ti usando un reranker semántico. Un ejemplo de cómo funciona el reordenamiento usando vecinos más cercanos:

```python
# Encuentra los documentos más similares
distances, indices = nbrs.kneighbors([query_vector])

index = []
# Imprime los documentos más similares
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

El último paso es agregar nuestro LLM a la mezcla para poder obtener respuestas fundamentadas en nuestros datos. Podemos implementarlo como sigue:

```python
user_input = "what is a perceptron?"

def chatbot(user_input):
    # Convertir la pregunta a un vector de consulta
    query_vector = create_embeddings(user_input)

    # Encontrar los documentos más similares
    distances, indices = nbrs.kneighbors([query_vector])

    # agregar documentos a la consulta para proporcionar contexto
    history = []
    for index in indices[0]:
        history.append(flattened_df['chunks'].iloc[index])

    # combinar el historial y la entrada del usuario
    history.append(user_input)

    # crear un objeto de mensaje
    messages=[
        {"role": "system", "content": "You are an AI assistant that helps with AI questions."},
        {"role": "user", "content": "\n\n".join(history) }
    ]

    # usar la finalización de chat para generar una respuesta
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

- Calidad de las respuestas suministradas asegurando que suene natural, fluido y humano.

- Fundamentación de los datos: evaluar si la respuesta proviene de los documentos suministrados.

- Relevancia: evaluar que la respuesta coincida y esté relacionada con la pregunta formulada.

- Fluidez: si la respuesta tiene sentido gramaticalmente.

## Casos de uso para usar RAG (Generación Aumentada por Recuperación) y bases de datos vectoriales

Hay muchos casos de uso diferentes donde las llamadas a funciones pueden mejorar tu app como:

- Preguntas y respuestas: fundamentar los datos de tu empresa para un chat que pueden usar los empleados para hacer preguntas.

- Sistemas de recomendación: donde puedes crear un sistema que coincida con los valores más similares, por ejemplo, películas, restaurantes y muchos más.

- Servicios de chatbot: puedes almacenar el historial de chat y personalizar la conversación basándote en los datos del usuario.

- Búsqueda de imágenes basada en embeddings vectoriales, útil para reconocimiento de imágenes y detección de anomalías.

## Resumen

Hemos cubierto las áreas fundamentales de RAG desde añadir nuestros datos a la aplicación, la consulta del usuario y la salida. Para simplificar la creación de RAG, puedes usar frameworks como Semantic Kernel, Langchain o Autogen.

## Tarea

Para continuar tu aprendizaje de Generación Aumentada por Recuperación (RAG) puedes construir:

- Construir un front-end para la aplicación usando el framework de tu elección.

- Utilizar un framework, ya sea LangChain o Semantic Kernel, y recrear tu aplicación.

Felicidades por completar la lección 👏.

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, echa un vistazo a nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir aumentando tus conocimientos en IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Si bien nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente oficial. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables por malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->