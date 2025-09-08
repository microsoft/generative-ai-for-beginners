<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4c2a0b0c738b649ef049fb99a23be661",
  "translation_date": "2025-07-09T19:05:42+00:00",
  "source_file": "21-meta/README.md",
  "language_code": "es"
}
-->
# Construyendo con los Modelos de la Familia Meta

## Introducción

Esta lección cubrirá:

- Exploración de los dos principales modelos de la familia Meta: Llama 3.1 y Llama 3.2
- Comprender los casos de uso y escenarios para cada modelo
- Ejemplo de código para mostrar las características únicas de cada modelo

## La Familia de Modelos Meta

En esta lección, exploraremos 2 modelos de la familia Meta o "Llama Herd": Llama 3.1 y Llama 3.2

Estos modelos vienen en diferentes variantes y están disponibles en el marketplace de GitHub Model. Aquí tienes más detalles sobre cómo usar GitHub Models para [prototipar con modelos de IA](https://docs.github.com/en/github-models/prototyping-with-ai-models?WT.mc_id=academic-105485-koreyst).

Variantes del modelo:
- Llama 3.1 - 70B Instruct
- Llama 3.1 - 405B Instruct
- Llama 3.2 - 11B Vision Instruct
- Llama 3.2 - 90B Vision Instruct

*Nota: Llama 3 también está disponible en GitHub Models, pero no se cubrirá en esta lección*

## Llama 3.1

Con 405 mil millones de parámetros, Llama 3.1 se ubica en la categoría de LLM de código abierto.

Este modelo es una mejora respecto a la versión anterior Llama 3, ofreciendo:

- Ventana de contexto más amplia: 128k tokens vs 8k tokens
- Máximo de tokens de salida más grande: 4096 vs 2048
- Mejor soporte multilingüe, gracias al aumento en los tokens de entrenamiento

Esto permite que Llama 3.1 maneje casos de uso más complejos al construir aplicaciones GenAI, incluyendo:
- Llamadas nativas a funciones: la capacidad de llamar a herramientas y funciones externas fuera del flujo de trabajo del LLM
- Mejor rendimiento RAG, debido a la ventana de contexto más amplia
- Generación de datos sintéticos: la capacidad de crear datos efectivos para tareas como el fine-tuning

### Llamadas Nativas a Funciones

Llama 3.1 ha sido afinado para ser más efectivo al hacer llamadas a funciones o herramientas. También cuenta con dos herramientas integradas que el modelo puede identificar como necesarias según el prompt del usuario. Estas herramientas son:

- **Brave Search**: puede usarse para obtener información actualizada, como el clima, realizando una búsqueda web
- **Wolfram Alpha**: puede usarse para cálculos matemáticos más complejos, por lo que no es necesario escribir tus propias funciones

También puedes crear tus propias herramientas personalizadas que el LLM pueda llamar.

En el ejemplo de código a continuación:

- Definimos las herramientas disponibles (brave_search, wolfram_alpha) en el prompt del sistema.
- Enviamos un prompt del usuario que pregunta sobre el clima en una ciudad determinada.
- El LLM responderá con una llamada a la herramienta Brave Search que se verá así `<|python_tag|>brave_search.call(query="Stockholm weather")`

*Nota: Este ejemplo solo realiza la llamada a la herramienta; si quieres obtener los resultados, deberás crear una cuenta gratuita en la página de la API de Brave y definir la función en sí*

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "meta-llama-3.1-405b-instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)


tool_prompt=f"""
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Environment: ipython
Tools: brave_search, wolfram_alpha
Cutting Knowledge Date: December 2023
Today Date: 23 July 2024

You are a helpful assistant<|eot_id|>
"""

messages = [
    SystemMessage(content=tool_prompt),
    UserMessage(content="What is the weather in Stockholm?"),

]

response = client.complete(messages=messages, model=model_name)

print(response.choices[0].message.content)
```

## Llama 3.2

A pesar de ser un LLM, una limitación que tiene Llama 3.1 es la multimodalidad. Es decir, la capacidad de usar diferentes tipos de entrada, como imágenes, como prompts y proporcionar respuestas. Esta capacidad es una de las principales características de Llama 3.2. Estas características también incluyen:

- Multimodalidad: capacidad para evaluar tanto prompts de texto como de imagen
- Variantes de tamaño pequeño a mediano (11B y 90B): esto ofrece opciones flexibles de despliegue
- Variantes solo de texto (1B y 3B): permiten desplegar el modelo en dispositivos edge/móviles y ofrecen baja latencia

El soporte multimodal representa un gran avance en el mundo de los modelos de código abierto. El ejemplo de código a continuación toma tanto una imagen como un prompt de texto para obtener un análisis de la imagen con Llama 3.2 90B.

### Soporte Multimodal con Llama 3.2

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)
from azure.core.credentials import AzureKeyCredential

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "Llama-3.2-90B-Vision-Instruct"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

response = client.complete(
    messages=[
        SystemMessage(
            content="You are a helpful assistant that describes images in details."
        ),
        UserMessage(
            content=[
                TextContentItem(text="What's in this image?"),
                ImageContentItem(
                    image_url=ImageUrl.load(
                        image_file="sample.jpg",
                        image_format="jpg",
                        detail=ImageDetailLevel.LOW)
                ),
            ],
        ),
    ],
    model=model_name,
)

print(response.choices[0].message.content)
```

## El aprendizaje no termina aquí, continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de Generative AI](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos en Generative AI.

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.