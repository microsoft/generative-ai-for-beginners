# Desarrollo de aplicaciones de búsqueda

[![Introducción a la IA generativa y los grandes modelos de lenguaje](../../images/08-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson8-gh?WT.mc_id=academic-105485-koreyst)

> > _Haga clic en la imagen de arriba para ver el video de esta lección_

Los LLM son mucho más que chatbots y generación de texto. También es posible crear aplicaciones de búsqueda mediante incrustaciones. Las incrustaciones son representaciones numéricas de datos, también conocidas como vectores, y pueden utilizarse para la búsqueda semántica de datos.

En esta lección, creará una aplicación de búsqueda para nuestra startup educativa. Nuestra startup es una organización sin fines de lucro que ofrece educación gratuita a estudiantes en países en desarrollo. Nuestra startup cuenta con una gran cantidad de videos de YouTube que los estudiantes pueden usar para aprender sobre IA. Nuestra startup quiere crear una aplicación de búsqueda que permita a los estudiantes buscar videos de YouTube escribiendo una pregunta.

Por ejemplo, un estudiante podría escribir "Qué son los Jupyter Notebooks?" o "Qué es Azure ML?" y la aplicación de búsqueda devolverá una lista de videos de YouTube relevantes para la pregunta. Mejor aún, la aplicación de búsqueda devolverá un enlace al lugar del video donde se encuentra la respuesta.

## Introducción

En esta lección, abordaremos:

- Búsqueda semántica vs. búsqueda por palabras clave.
- Qué son las incrustaciones de texto?
- Creación de un índice de incrustaciones de texto.
- Búsqueda en un índice de incrustaciones de texto.

## Objetivos de aprendizaje

Después de completar esta lección, podrá:

- Diferenciar entre la búsqueda semántica y la búsqueda por palabras clave.
- Explicar qué son las incrustaciones de texto.
- Crear una aplicación que utilice incrustaciones para buscar datos.

## Por qué crear una aplicación de búsqueda?

Crear una aplicación de búsqueda te ayudará a comprender cómo usar las incrustaciones para buscar datos. También aprenderás a crear una aplicación que los estudiantes puedan usar para encontrar información rápidamente.

La lección incluye un índice de incrustaciones de las transcripciones de YouTube del canal de YouTube de Microsoft [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). AI Show es un canal de YouTube que enseña sobre IA y aprendizaje automático. El índice de incrustaciones contiene las incrustaciones de cada una de las transcripciones de YouTube hasta octubre de 2023. Utilizarás el índice de incrustaciones para crear una aplicación de búsqueda para nuestra startup. La aplicación de búsqueda devuelve un enlace al lugar del video donde se encuentra la respuesta a la pregunta. Esta es una excelente manera para que los estudiantes encuentren la información que necesitan rápidamente.

El siguiente es un ejemplo de una consulta semántica para la pregunta "Se puede usar Rstudio con Azure ML?". Revisa la URL de YouTube; verás que contiene una marca de tiempo que te lleva al lugar del video donde se encuentra la respuesta a la pregunta.

![Consulta semántica para la pregunta "Se puede usar Rstudio con Azure ML?"](../../images/query-results.png?WT.mc_id=academic-105485-koreyst)

## Qué es la búsqueda semántica?

Quizás te preguntes qué es la búsqueda semántica. La búsqueda semántica es una técnica de búsqueda que utiliza la semántica, o el significado, de las palabras en una consulta para devolver resultados relevantes.

Aquí tienes un ejemplo de búsqueda semántica. Supongamos que quieres comprar un coche; podrías buscar "el coche de mis sueños". La búsqueda semántica entiende que no estás `soñando` con un coche, sino que buscas comprar tu coche `ideal`. La búsqueda semántica comprende tu intención y devuelve resultados relevantes. La alternativa es la búsqueda por `palabras clave`, que literalmente buscaría sueños sobre coches y, a menudo, arrojaría resultados irrelevantes.

## Qué son las incrustaciones de texto?

[Las incrustaciones de texto](https://en.wikipedia.org/wiki/Word_embedding?WT.mc_id=academic-105485-koreyst) son una técnica de representación de texto utilizada en el procesamiento del [lenguaje natural](https://en.wikipedia.org/wiki/Natural_language_processing?WT.mc_id=academic-105485-koreyst). Son representaciones numéricas semánticas del texto. Se utilizan para representar datos de forma que una máquina los comprenda fácilmente. Existen muchos modelos para crear incrustaciones de texto; en esta lección, nos centraremos en generarlas mediante el modelo de incrustación de OpenAI.

Aquí tienes un ejemplo: imagina que el siguiente texto forma parte de la transcripción de uno de los episodios del canal de YouTube AI Show:

```texto
Hoy aprenderemos sobre Azure Machine Learning. 
```

Pasaríamos el texto a la API de incrustación de OpenAI y esta devolvería la siguiente incrustación, compuesta por 1536 números, es decir, un vector. Cada número del vector representa un aspecto diferente del texto. Para abreviar, aquí están los primeros 10 números del vector.

```python
[-0.006655829958617687, 0.0026128944009542465, 0.008792596869170666, -0.02446001023054123, -0.008540431968867779, 0.022071078419685364, -0.010703742504119873, 0.003311325330287218, -0.011632772162556648, -0.02187200076878071, ...]
```

## Cómo se crea el índice de incrustación? 

El índice de incrustación de esta lección se creó con una serie de scripts de Python. Encontrará los scripts junto con las instrucciones en el archivo [README](../../scripts/README.md?WT.mc_id=academic-105485-koreyst), en la carpeta 'scripts' de esta lección. No necesita ejecutar estos scripts para completar la lección, ya que el índice de incrustación se proporciona automáticamente.

Los scripts realizan las siguientes operaciones:

1. Se descarga la transcripción de cada video de YouTube en la lista de reproducción [AI Show](https://www.youtube.com/playlist?list=PLlrxD0HtieHi0mwteKBOfEeOYf0LJU4O1). 2. Mediante [Funciones de OpenAI](https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling?WT.mc_id=academic-105485-koreyst), se intenta extraer el nombre del orador de los primeros 3 minutos de la transcripción de YouTube. El nombre del orador de cada vídeo se almacena en el índice de incrustación `embedding_index_3m.json`.
3. El texto de la transcripción se fragmenta en **segmentos de texto de 3 minutos**. Cada segmento incluye aproximadamente 20 palabras que se superponen con el siguiente para garantizar que la incrustación del segmento no se corte y para proporcionar un mejor contexto de búsqueda.
4. Cada segmento de texto se pasa a la API de OpenAI Chat para resumirlo en 60 palabras. El resumen también se almacena en el índice de incrustación `embedding_index_3m.json`.
5. Finalmente, el texto del segmento se pasa a la API de incrustación de OpenAI. La API de incrustación devuelve un vector de 1536 números que representan el significado semántico del segmento. El segmento, junto con el vector de incrustación de OpenAI, se almacena en un índice de incrustación `embedding_index_3m.json`.

### Bases de datos vectoriales

Para simplificar la lección, el índice de incrustación se almacena en un archivo JSON llamado `embedding_index_3m.json` y se carga en un DataFrame de Pandas. Sin embargo, en producción, el índice de incrustación se almacenaría en una base de datos vectorial como [Azure Cognitive Search](https://learn.microsoft.com/training/modules/improve-search-results-vector-search?WT.mc_id=academic-105485-koreyst), [Redis](https://cookbook.openai.com/examples/vector_databases/redis/readme?WT.mc_id=academic-105485-koreyst), [Pinecone](https://cookbook.openai.com/examples/vector_databases/pinecone/readme?WT.mc_id=academic-105485-koreyst) o [Weaviate](https://cookbook.openai.com/examples/vector_databases/weaviate/readme?WT.mc_id=academic-105485-koreyst), por nombrar solo algunas. ## Entendiendo la similitud de cosenos

Hemos aprendido sobre las incrustaciones de texto. El siguiente paso es aprender a usarlas para buscar datos y, en particular, encontrar las incrustaciones más similares a una consulta dada mediante la similitud de cosenos.

### Qué es la similitud de cosenos?

La similitud de coseno es una medida de similitud entre dos vectores; también se la conoce como "búsqueda del vecino más cercano". Para realizar una búsqueda de similitud de coseno, es necesario vectorizar el texto de la consulta mediante la API de incrustación de OpenAI. A continuación, calcule la similitud de coseno entre el vector de consulta y cada vector del índice de incrustación. Recuerde que el índice de incrustación tiene un vector para cada segmento de texto de la transcripción de YouTube. Finalmente, ordene los resultados por similitud de coseno; los segmentos de texto con la mayor similitud de coseno serán los más similares a la consulta.

Desde una perspectiva matemática, la similitud de coseno mide el coseno del ángulo entre dos vectores proyectados en un espacio multidimensional. Esta medida es beneficiosa, ya que si dos documentos están separados por una distancia euclidiana debido a su tamaño, podrían tener un ángulo menor entre ellos y, por lo tanto, una mayor similitud de coseno. Para más información sobre las ecuaciones de similitud de cosenos, consulte [Similitud de cosenos](https://en.wikipedia.org/wiki/Cosine_similarity?WT.mc_id=academic-105485-koreyst).

## Creación de su primera aplicación de búsqueda

A continuación, aprenderemos a crear una aplicación de búsqueda mediante incrustaciones. Esta aplicación permitirá a los estudiantes buscar un video escribiendo una pregunta. Devolverá una lista de videos relevantes para la pregunta. También mostrará un enlace a la parte del video donde se encuentra la respuesta.

Esta solución se creó y probó en Windows 11, macOS y Ubuntu 22.04 con Python 3.10 o posterior. Puede descargar Python desde [python.org](https://www.python.org/downloads/?WT.mc_id=academic-105485-koreyst).

## Tarea: Desarrollo de una aplicación de búsqueda para estudiantes

Presentamos nuestra startup al principio de esta lección. Ahora es el momento de que los estudiantes creen una aplicación de búsqueda para sus evaluaciones.

En esta tarea, crearán los servicios de Azure OpenAI que se usarán para crear la aplicación de búsqueda. Necesitarán una suscripción a Azure para completar esta tarea.

### Iniciar Azure Cloud Shell

1. Inicie sesión en el [portal de Azure](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst).
2. Seleccione el icono de Cloud Shell en la esquina superior derecha del portal de Azure.
3. Seleccione **Bash** como tipo de entorno.

#### Crear un grupo de recursos

> Para estas instrucciones, usamos el grupo de recursos "semantic-video-search" en el este de EE. UU.
> Puede cambiar el nombre del grupo de recursos, pero al cambiar la ubicación de los recursos, consulte la [tabla de disponibilidad de modelos](https://aka.ms/oai/models?WT.mc_id=academic-105485-koreyst).

```shell
az group create --name semantic-video-search --location eastus
```

#### Crear un recurso de Azure OpenAI Service

Desde Azure Cloud Shell, ejecute el siguiente comando para crear un recurso de Azure OpenAI Service.

```shell
az knowledgeful services account create --name semantic-video-openai --resource-group semantic-video-search \
--location eastus --kind OpenAI --sku s0
```

#### Obtener el punto de conexión y las claves para su uso en esta aplicación

Desde Azure Cloud Shell, ejecute los siguientes comandos para obtener el punto de conexión y las claves del recurso de Azure OpenAI Service.

```shell
az knowledgeful services account show --name semantic-video-openai \
--resource-group semantic-video-search | jq -r .properties.endpoint
az knowledgeful services account keys list --name semantic-video-openai \
--resource-group semantic-video-search | jq -r .key1
```

#### Implementar el modelo de incrustación de OpenAI

Desde Azure Cloud Shell, ejecute el siguiente comando para implementar el modelo de incrustación de OpenAI.

```shell
az knowledgeservices accountployment create \
--name semantic-video-openai \
--resource-group semantic-video-search \
--deployment-name text-embedding-ada-002 \
--model-name text-embedding-ada-002 \
--model-version "2" \
--model-format OpenAI \
--sku-capacity 100 --sku-name "Standard"
```

## Solución

Abra el cuaderno de soluciones en GitHub Codespaces y siga las instrucciones del cuaderno de Jupyter.

Al ejecutar el cuaderno, se le solicitará que introduzca una consulta. El cuadro de entrada se verá así:

![Cuadro de entrada para que el usuario introduzca una consulta](../../images/notebook-search.png?WT.mc_id=academic-105485-koreyst)

## Buen trabajo! Continúe aprendiendo!

Después de completar esta lección, consulte nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando sus conocimientos sobre IA generativa.

Vaya a la Lección 9, donde veremos cómo [crear aplicaciones de generación de imágenes](../../../09-building-image-applications/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst).