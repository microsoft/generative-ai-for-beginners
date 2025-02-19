# Construyendo con Modelos Mistral 

## Introducción 

Esta lección cubrirá: 
- Exploración de los diferentes Modelos Mistral 
- Comprensión de los casos de uso y escenarios para cada modelo 
- Ejemplos de código que muestran las características únicas de cada modelo. 

## Los Modelos Mistral 

En esta lección, exploraremos 3 diferentes modelos de Mistral: 
**Mistral Large**, **Mistral Small** y **Mistral Nemo**. 

Cada uno de estos modelos está disponible de forma gratuita en el mercado de Modelos de Github. El código en este cuaderno usará estos modelos para ejecutar el código. Aquí hay más detalles sobre cómo usar los Modelos de Github para [prototipar con modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst). 

## Mistral Large 2 (2407)

Mistral Large 2 es actualmente el modelo insignia de Mistral y está diseñado para uso empresarial. 

El modelo es una mejora del Mistral Large original al ofrecer: 
- Ventana de Contexto Más Grande - 128k vs 32k 
- Mejor rendimiento en tareas de Matemáticas y Programación - 76.9% de precisión promedio vs 60.4% 
- Rendimiento multilingüe aumentado - los idiomas incluyen: inglés, francés, alemán, español, italiano, portugués, neerlandés, ruso, chino, japonés, coreano, árabe e hindi.

Con estas características, Mistral Large sobresale en: 
- *Generación Aumentada por Recuperación (RAG)* - debido a la mayor ventana de contexto
- *Llamada de Funciones* - este modelo tiene llamadas de funciones nativas que permiten la integración con herramientas externas y APIs. Estas llamadas se pueden hacer tanto en paralelo como una tras otra en orden secuencial. 
- *Generación de Código* - este modelo destaca en la generación de Python, Java, TypeScript y C++. 

### Ejemplo de RAG usando Mistral Large 2 

En este ejemplo, estamos usando Mistral Large 2 para ejecutar un patrón RAG sobre un documento de texto. La pregunta está escrita en coreano y pregunta sobre las actividades del autor antes de la universidad. 

Utiliza el modelo de Embeddings de Cohere para crear embeddings del documento de texto así como de la pregunta. Para este ejemplo, utiliza el paquete de Python faiss como un almacén de vectores. 

El mensaje enviado al modelo Mistral incluye tanto las preguntas como los fragmentos recuperados que son similares a la pregunta. El modelo luego proporciona una respuesta en lenguaje natural. 

```python 
pip install faiss-cpu
```

```python 
import requests
import numpy as np
import faiss
import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference import EmbeddingsClient

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = requests.get('https://raw.githubusercontent.com/run-llama/llama_index/main/docs/docs/examples/data/paul_graham/paul_graham_essay.txt')
text = response.text

chunk_size = 2048
chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
len(chunks)

embed_model_name = "cohere-embed-v3-multilingual" 

embed_client = EmbeddingsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(token)
)

embed_response = embed_client.embed(
    input=chunks,
    model=embed_model_name
)



text_embeddings = []
for item in embed_response.data:
    length = len(item.embedding)
    text_embeddings.append(item.embedding)
text_embeddings = np.array(text_embeddings)


d = text_embeddings.shape[1]
index = faiss.IndexFlatL2(d)
index.add(text_embeddings)

question = "저자가 대학에 오기 전에 주로 했던 두 가지 일은 무엇이었나요?？"

question_embedding = embed_client.embed(
    input=[question],
    model=embed_model_name
)

question_embeddings = np.array(question_embedding.data[0].embedding)


D, I = index.search(question_embeddings.reshape(1, -1), k=2) # distance, index
retrieved_chunks = [chunks[i] for i in I.tolist()[0]]

prompt = f"""
Context information is below.
---------------------
{retrieved_chunks}
---------------------
Given the context information and not prior knowledge, answer the query.
Query: {question}
Answer:
"""


chat_response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        UserMessage(content=prompt),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(chat_response.choices[0].message.content)
```

## Mistral Small 

Mistral Small es otro modelo en la familia de modelos Mistral dentro de la categoría premier/empresarial. Como su nombre lo indica, este modelo es un Modelo de Lenguaje Pequeño (SLM). Las ventajas de usar Mistral Small son que es: 
- Económico en comparación con los LLM de Mistral como Mistral Large y NeMo - reducción del 80% en el precio
- Baja latencia - respuesta más rápida en comparación con los LLM de Mistral
- Flexible - se puede desplegar en diferentes entornos con menos restricciones sobre los recursos requeridos. 

Mistral Small es excelente para: 
- Tareas basadas en texto como resumen, análisis de sentimientos y traducción. 
- Aplicaciones donde se realizan solicitudes frecuentes debido a su rentabilidad 
- Tareas de código de baja latencia como revisión y sugerencias de código 

## Comparación entre Mistral Small y Mistral Large 

Para mostrar las diferencias en latencia entre Mistral Small y Large, ejecuta las siguientes celdas. 

Deberías ver una diferencia en los tiempos de respuesta entre 3-5 segundos. También observa las longitudes y el estilo de respuesta sobre el mismo mensaje.  

```python 

import os 
endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-small"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

```python 

import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

endpoint = "https://models.inference.ai.azure.com"
model_name = "Mistral-large"
token = os.environ["GITHUB_TOKEN"]

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful coding assistant."),
        UserMessage(content="Can you write a Python function to the fizz buzz test?"),
    ],
    temperature=1.0,
    top_p=1.0,
    max_tokens=1000,
    model=model_name
)

print(response.choices[0].message.content)

```

## Mistral NeMo

En comparación con los otros dos modelos discutidos en esta lección, Mistral NeMo es el único modelo gratuito con una Licencia Apache2. 

Se considera una mejora del LLM de código abierto anterior de Mistral, Mistral 7B. 

Algunas otras características del modelo NeMo son: 

- *Tokenización más eficiente:* Este modelo usa el tokenizador Tekken en lugar del más comúnmente usado tiktoken. Esto permite un mejor rendimiento en más idiomas y código. 

- *Ajuste fino:* El modelo base está disponible para ajuste fino. Esto permite más flexibilidad para casos de uso donde se pueda necesitar ajuste fino. 

- *Llamada de Funciones Nativa* - Al igual que Mistral Large, este modelo ha sido entrenado en la llamada de funciones. Esto lo hace único al ser uno de los primeros modelos de código abierto en hacerlo. 

### Comparación de Tokenizadores 

En este ejemplo, veremos cómo Mistral NeMo maneja la tokenización en comparación con Mistral Large. 

Ambos ejemplos toman el mismo mensaje, pero deberías ver que NeMo devuelve menos tokens en comparación con Mistral Large. 

```bash
pip install mistral-common
```

```python 
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "open-mistral-nemo	"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

```python
# Import needed packages:
from mistral_common.protocol.instruct.messages import (
    UserMessage,
)
from mistral_common.protocol.instruct.request import ChatCompletionRequest
from mistral_common.protocol.instruct.tool_calls import (
    Function,
    Tool,
)
from mistral_common.tokens.tokenizers.mistral import MistralTokenizer

# Load Mistral tokenizer

model_name = "mistral-large-latest"

tokenizer = MistralTokenizer.from_model(model_name)

# Tokenize a list of messages
tokenized = tokenizer.encode_chat_completion(
    ChatCompletionRequest(
        tools=[
            Tool(
                function=Function(
                    name="get_current_weather",
                    description="Get the current weather",
                    parameters={
                        "type": "object",
                        "properties": {
                            "location": {
                                "type": "string",
                                "description": "The city and state, e.g. San Francisco, CA",
                            },
                            "format": {
                                "type": "string",
                                "enum": ["celsius", "fahrenheit"],
                                "description": "The temperature unit to use. Infer this from the users location.",
                            },
                        },
                        "required": ["location", "format"],
                    },
                )
            )
        ],
        messages=[
            UserMessage(content="What's the weather like today in Paris"),
        ],
        model=model_name,
    )
)
tokens, text = tokenized.tokens, tokenized.text

# Count the number of tokens
print(len(tokens))
```

## El aprendizaje no se detiene aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos en IA Generativa.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.