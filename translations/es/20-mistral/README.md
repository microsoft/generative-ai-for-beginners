<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4bd0fafda5d66cd9d60f1ebc7820415e",
  "translation_date": "2025-07-09T18:55:20+00:00",
  "source_file": "20-mistral/README.md",
  "language_code": "es"
}
-->
# Construyendo con Modelos Mistral

## Introducción

Esta lección cubrirá:  
- Exploración de los diferentes Modelos Mistral  
- Comprensión de los casos de uso y escenarios para cada modelo  
- Ejemplos de código que muestran las características únicas de cada modelo.

## Los Modelos Mistral

En esta lección, exploraremos 3 modelos diferentes de Mistral:  
**Mistral Large**, **Mistral Small** y **Mistral Nemo**.

Cada uno de estos modelos está disponible de forma gratuita en el marketplace de Github Model. El código en este cuaderno usará estos modelos para ejecutar el código. Aquí tienes más detalles sobre cómo usar Github Models para [prototipar con modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

## Mistral Large 2 (2407)  
Mistral Large 2 es actualmente el modelo insignia de Mistral y está diseñado para uso empresarial.

El modelo es una mejora respecto al Mistral Large original, ofreciendo:  
- Ventana de contexto más amplia - 128k vs 32k  
- Mejor rendimiento en tareas de matemáticas y programación - 76.9% de precisión promedio vs 60.4%  
- Mayor rendimiento multilingüe - idiomas incluyen: inglés, francés, alemán, español, italiano, portugués, neerlandés, ruso, chino, japonés, coreano, árabe e hindi.

Con estas características, Mistral Large destaca en:  
- *Generación aumentada por recuperación (RAG)* - gracias a la ventana de contexto más amplia  
- *Llamadas a funciones* - este modelo tiene llamadas a funciones nativas que permiten la integración con herramientas y APIs externas. Estas llamadas pueden hacerse en paralelo o de forma secuencial.  
- *Generación de código* - este modelo sobresale en generación de Python, Java, TypeScript y C++.

### Ejemplo de RAG usando Mistral Large 2

En este ejemplo, usamos Mistral Large 2 para ejecutar un patrón RAG sobre un documento de texto. La pregunta está escrita en coreano y consulta sobre las actividades del autor antes de la universidad.

Se utiliza el modelo de embeddings Cohere para crear embeddings tanto del documento de texto como de la pregunta. Para este ejemplo, se usa el paquete faiss de Python como almacén vectorial.

El prompt enviado al modelo Mistral incluye tanto las preguntas como los fragmentos recuperados que son similares a la pregunta. El modelo luego proporciona una respuesta en lenguaje natural.

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
Mistral Small es otro modelo dentro de la familia Mistral en la categoría premier/empresarial. Como su nombre indica, este modelo es un Modelo de Lenguaje Pequeño (SLM). Las ventajas de usar Mistral Small son:  
- Ahorro de costos en comparación con los LLMs de Mistral como Mistral Large y NeMo - reducción del 80% en precio  
- Baja latencia - respuesta más rápida comparada con los LLMs de Mistral  
- Flexible - puede desplegarse en diferentes entornos con menos restricciones en los recursos requeridos.

Mistral Small es ideal para:  
- Tareas basadas en texto como resumen, análisis de sentimiento y traducción.  
- Aplicaciones con solicitudes frecuentes debido a su rentabilidad  
- Tareas de código con baja latencia como revisión y sugerencias de código

## Comparando Mistral Small y Mistral Large

Para mostrar las diferencias en latencia entre Mistral Small y Large, ejecuta las celdas a continuación.

Deberías notar una diferencia en los tiempos de respuesta de entre 3 y 5 segundos. También observa las diferencias en la longitud y estilo de la respuesta con el mismo prompt.

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

En comparación con los otros dos modelos tratados en esta lección, Mistral NeMo es el único modelo gratuito con licencia Apache2.

Se considera una mejora respecto al anterior LLM de código abierto de Mistral, Mistral 7B.

Algunas otras características del modelo NeMo son:

- *Tokenización más eficiente:* Este modelo usa el tokenizador Tekken en lugar del más común tiktoken. Esto permite un mejor rendimiento en más idiomas y código.

- *Ajuste fino (Finetuning):* El modelo base está disponible para ajuste fino, lo que brinda mayor flexibilidad para casos de uso donde se requiera.

- *Llamadas a funciones nativas* - Al igual que Mistral Large, este modelo ha sido entrenado para llamadas a funciones. Esto lo hace único como uno de los primeros modelos de código abierto en hacerlo.

### Comparando tokenizadores

En este ejemplo, veremos cómo Mistral NeMo maneja la tokenización en comparación con Mistral Large.

Ambos ejemplos usan el mismo prompt, pero deberías notar que NeMo devuelve menos tokens que Mistral Large.

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

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, visita nuestra [colección de aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos en IA Generativa.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.