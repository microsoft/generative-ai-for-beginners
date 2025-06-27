<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e2861bbca91c0567ef32bc77fe054f9e",
  "translation_date": "2025-06-25T22:15:43+00:00",
  "source_file": "15-rag-and-vector-databases/README.md",
  "language_code": "es"
}
-->
# Generación Aumentada por Recuperación (RAG) y Bases de Datos Vectoriales

En la lección de aplicaciones de búsqueda, aprendimos brevemente cómo integrar tus propios datos en Modelos de Lenguaje Grande (LLMs). En esta lección, profundizaremos en los conceptos de fundamentar tus datos en tu aplicación LLM, la mecánica del proceso y los métodos para almacenar datos, incluyendo tanto incrustaciones como texto.

> **Vídeo Próximamente**

## Introducción

En esta lección cubriremos lo siguiente:

- Una introducción a RAG, qué es y por qué se utiliza en IA (inteligencia artificial).

- Comprender qué son las bases de datos vectoriales y crear una para nuestra aplicación.

- Un ejemplo práctico sobre cómo integrar RAG en una aplicación.

## Objetivos de Aprendizaje

Después de completar esta lección, podrás:

- Explicar la importancia de RAG en la recuperación y procesamiento de datos.

- Configurar la aplicación RAG y fundamentar tus datos en un LLM.

- Integración efectiva de RAG y Bases de Datos Vectoriales en aplicaciones LLM.

## Nuestro Escenario: mejorando nuestros LLMs con nuestros propios datos

Para esta lección, queremos añadir nuestras propias notas en la startup educativa, lo que permite al chatbot obtener más información sobre los diferentes temas. Usando las notas que tenemos, los estudiantes podrán estudiar mejor y comprender los diferentes temas, facilitando la revisión para sus exámenes. Para crear nuestro escenario, utilizaremos:

- `Azure OpenAI:` el LLM que utilizaremos para crear nuestro chatbot

- `AI for beginners' lesson on Neural Networks`: estos serán los datos sobre los que fundamentaremos nuestro LLM

- `Azure AI Search` y `Azure Cosmos DB:` base de datos vectorial para almacenar nuestros datos y crear un índice de búsqueda

Los usuarios podrán crear cuestionarios de práctica a partir de sus notas, tarjetas de revisión y resumirlas en vistas generales concisas. Para comenzar, veamos qué es RAG y cómo funciona:

## Generación Aumentada por Recuperación (RAG)

Un chatbot potenciado por LLM procesa las solicitudes de los usuarios para generar respuestas. Está diseñado para ser interactivo y se involucra con los usuarios en una amplia gama de temas. Sin embargo, sus respuestas están limitadas al contexto proporcionado y a sus datos de entrenamiento fundamentales. Por ejemplo, el límite de conocimiento de GPT-4 es septiembre de 2021, lo que significa que carece de conocimiento de eventos que han ocurrido después de este período. Además, los datos utilizados para entrenar LLMs excluyen información confidencial como notas personales o el manual de productos de una empresa.

### Cómo funcionan los RAGs (Generación Aumentada por Recuperación)

Supongamos que deseas desplegar un chatbot que cree cuestionarios a partir de tus notas, necesitarás una conexión con la base de conocimiento. Aquí es donde RAG viene al rescate. Los RAGs operan de la siguiente manera:

- **Base de conocimiento:** Antes de la recuperación, estos documentos necesitan ser ingeridos y preprocesados, típicamente descomponiendo documentos grandes en fragmentos más pequeños, transformándolos en incrustaciones de texto y almacenándolos en una base de datos.

- **Consulta del usuario:** el usuario hace una pregunta

- **Recuperación:** Cuando un usuario hace una pregunta, el modelo de incrustación recupera información relevante de nuestra base de conocimiento para proporcionar más contexto que se incorporará en la solicitud.

- **Generación Aumentada:** el LLM mejora su respuesta basado en los datos recuperados. Permite que la respuesta generada no solo se base en datos preentrenados sino también en información relevante del contexto añadido. Los datos recuperados se utilizan para aumentar las respuestas del LLM. El LLM luego devuelve una respuesta a la pregunta del usuario.

La arquitectura para RAGs se implementa utilizando transformadores que constan de dos partes: un codificador y un decodificador. Por ejemplo, cuando un usuario hace una pregunta, el texto de entrada se 'codifica' en vectores que capturan el significado de las palabras y los vectores se 'decodifican' en nuestro índice de documentos y generan nuevo texto basado en la consulta del usuario. El LLM utiliza tanto un modelo codificador-decodificador para generar la salida.

Dos enfoques al implementar RAG según el documento propuesto: [Generación Aumentada por Recuperación para Tareas de NLP (procesamiento de lenguaje natural) intensivas en conocimiento](https://arxiv.org/pdf/2005.11401.pdf?WT.mc_id=academic-105485-koreyst) son:

- **_RAG-Secuencia_** usando documentos recuperados para predecir la mejor respuesta posible a una consulta del usuario

- **RAG-Token** usando documentos para generar el siguiente token, luego recuperarlos para responder a la consulta del usuario

### ¿Por qué usarías RAGs?

- **Riqueza de información:** asegura que las respuestas de texto estén actualizadas y sean actuales. Por lo tanto, mejora el rendimiento en tareas específicas de dominio al acceder a la base de conocimiento interna.

- Reduce la fabricación utilizando **datos verificables** en la base de conocimiento para proporcionar contexto a las consultas de los usuarios.

- Es **rentable** ya que son más económicos en comparación con el ajuste fino de un LLM.

## Creando una base de conocimiento

Nuestra aplicación se basa en nuestros datos personales, es decir, la lección de Redes Neuronales en el plan de estudios de IA para Principiantes.

### Bases de Datos Vectoriales

Una base de datos vectorial, a diferencia de las bases de datos tradicionales, es una base de datos especializada diseñada para almacenar, gestionar y buscar vectores incrustados. Almacena representaciones numéricas de documentos. Descomponer datos en incrustaciones numéricas facilita que nuestro sistema de IA comprenda y procese los datos.

Almacenamos nuestras incrustaciones en bases de datos vectoriales ya que los LLMs tienen un límite en la cantidad de tokens que aceptan como entrada. Como no puedes pasar todas las incrustaciones a un LLM, necesitaremos descomponerlas en fragmentos y cuando un usuario hace una pregunta, las incrustaciones más parecidas a la pregunta se devolverán junto con la solicitud. La fragmentación también reduce los costos en la cantidad de tokens pasados a través de un LLM.

Algunas bases de datos vectoriales populares incluyen Azure Cosmos DB, Clarifyai, Pinecone, Chromadb, ScaNN, Qdrant y DeepLake. Puedes crear un modelo de Azure Cosmos DB usando Azure CLI con el siguiente comando:

### De texto a incrustaciones

Antes de almacenar nuestros datos, necesitaremos convertirlos en incrustaciones vectoriales antes de que se almacenen en la base de datos. Si estás trabajando con documentos grandes o textos largos, puedes fragmentarlos según las consultas que esperas. La fragmentación se puede hacer a nivel de oración o a nivel de párrafo. Dado que la fragmentación deriva significados de las palabras que las rodean, puedes agregar algún otro contexto a un fragmento, por ejemplo, agregando el título del documento o incluyendo algún texto antes o después del fragmento. Puedes fragmentar los datos de la siguiente manera:

Una vez fragmentado, podemos incrustar nuestro texto utilizando diferentes modelos de incrustación. Algunos modelos que puedes usar incluyen: word2vec, ada-002 de OpenAI, Azure Computer Vision y muchos más. La selección de un modelo para usar dependerá de los idiomas que estés utilizando, el tipo de contenido codificado (texto/imágenes/audio), el tamaño de la entrada que puede codificar y la longitud de la salida de la incrustación.

Un ejemplo de texto incrustado usando el modelo `text-embedding-ada-002` de OpenAI es:

## Recuperación y Búsqueda Vectorial

Cuando un usuario hace una pregunta, el recuperador la transforma en un vector usando el codificador de consulta, luego busca en nuestro índice de búsqueda de documentos vectores relevantes en el documento que están relacionados con la entrada. Una vez hecho, convierte tanto el vector de entrada como los vectores de documentos en texto y los pasa a través del LLM.

### Recuperación

La recuperación ocurre cuando el sistema intenta encontrar rápidamente los documentos del índice que satisfacen los criterios de búsqueda. El objetivo del recuperador es obtener documentos que se utilizarán para proporcionar contexto y fundamentar el LLM en tus datos.

Hay varias formas de realizar búsquedas dentro de nuestra base de datos, tales como:

- **Búsqueda por palabra clave** - utilizada para búsquedas de texto

- **Búsqueda semántica** - utiliza el significado semántico de las palabras

- **Búsqueda vectorial** - convierte documentos de texto a representaciones vectoriales usando modelos de incrustación. La recuperación se realizará consultando los documentos cuyas representaciones vectoriales estén más cerca de la pregunta del usuario.

- **Híbrido** - una combinación de búsqueda por palabra clave y búsqueda vectorial.

Un desafío con la recuperación surge cuando no hay una respuesta similar a la consulta en la base de datos, el sistema entonces devolverá la mejor información que pueda obtener, sin embargo, puedes usar tácticas como establecer la distancia máxima para la relevancia o usar búsqueda híbrida que combina tanto palabras clave como búsqueda vectorial. En esta lección utilizaremos búsqueda híbrida, una combinación de búsqueda vectorial y por palabra clave. Almacenaremos nuestros datos en un marco de datos con columnas que contienen los fragmentos así como las incrustaciones.

### Similitud Vectorial

El recuperador buscará en la base de datos de conocimiento incrustaciones que estén cerca unas de otras, el vecino más cercano, ya que son textos similares. En el escenario en que un usuario hace una consulta, primero se incrusta y luego se empareja con incrustaciones similares. La medida común que se utiliza para encontrar cuán similares son diferentes vectores es la similitud de coseno, que se basa en el ángulo entre dos vectores.

Podemos medir la similitud usando otras alternativas como la distancia euclidiana, que es la línea recta entre los puntos finales de los vectores, y el producto punto, que mide la suma de los productos de los elementos correspondientes de dos vectores.

### Índice de búsqueda

Al realizar la recuperación, necesitaremos construir un índice de búsqueda para nuestra base de conocimiento antes de realizar la búsqueda. Un índice almacenará nuestras incrustaciones y podrá recuperar rápidamente los fragmentos más similares incluso en una base de datos grande. Podemos crear nuestro índice localmente usando:

### Reordenamiento

Una vez que hayas consultado la base de datos, es posible que necesites ordenar los resultados desde el más relevante. Un LLM de reordenamiento utiliza Aprendizaje Automático para mejorar la relevancia de los resultados de búsqueda ordenándolos desde el más relevante. Usando Azure AI Search, el reordenamiento se realiza automáticamente para ti utilizando un reordenador semántico. Un ejemplo de cómo funciona el reordenamiento usando vecinos más cercanos:

## Juntándolo todo

El último paso es añadir nuestro LLM a la mezcla para poder obtener respuestas que estén fundamentadas en nuestros datos. Podemos implementarlo de la siguiente manera:

## Evaluando nuestra aplicación

### Métricas de Evaluación

- Calidad de las respuestas suministradas asegurando que suenen naturales, fluidas y humanas.

- Fundamentación de los datos: evaluando si la respuesta proviene de los documentos suministrados.

- Relevancia: evaluando si la respuesta coincide y está relacionada con la pregunta realizada.

- Fluidez: si la respuesta tiene sentido gramaticalmente.

## Casos de Uso para usar RAG (Generación Aumentada por Recuperación) y bases de datos vectoriales

Hay muchos casos de uso diferentes donde las llamadas a funciones pueden mejorar tu aplicación como:

- Preguntas y Respuestas: fundamentando los datos de tu empresa a un chat que pueden usar los empleados para hacer preguntas.

- Sistemas de Recomendación: donde puedes crear un sistema que empareje los valores más similares, por ejemplo, películas, restaurantes y muchos más.

- Servicios de chatbot: puedes almacenar el historial de chat y personalizar la conversación basada en los datos del usuario.

- Búsqueda de imágenes basada en incrustaciones vectoriales, útil al realizar reconocimiento de imágenes y detección de anomalías.

## Resumen

Hemos cubierto las áreas fundamentales de RAG desde agregar nuestros datos a la aplicación, la consulta del usuario y la salida. Para simplificar la creación de RAG, puedes usar marcos como Semanti Kernel, Langchain o Autogen.

## Tarea

Para continuar tu aprendizaje de Generación Aumentada por Recuperación (RAG) puedes construir:

- Crear una interfaz para la aplicación utilizando el marco de tu elección.

- Utilizar un marco, ya sea LangChain o Semantic Kernel, y recrear tu aplicación.

Felicitaciones por completar la lección 👏.

## El aprendizaje no se detiene aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tus conocimientos de IA generativa.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción humana profesional. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.