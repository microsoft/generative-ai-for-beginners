# Construyendo con los modelos de la familia Meta 

## Introducción 

Esta lección cubrirá: 

- Explorando los dos principales modelos de la familia Meta - Llama 3.1 y Llama 3.2, además de las alternativas actualmente disponibles utilizadas en los ejemplos de código (Llama 3.3 y Llama 4) 
- Comprendiendo los casos de uso y escenarios para cada modelo 
- Ejemplo de código para mostrar las características únicas de cada modelo 


## La familia de modelos Meta 

En esta lección, exploraremos 2 modelos de la familia Meta o "Llama Herd": Llama 3.1 y Llama 3.2. Los ejemplos de código ejecutables usan Llama 3.3 y Llama 4, que son alternativas actualmente disponibles en el catálogo de Microsoft Foundry Models.

Estos modelos vienen en diferentes variantes y están disponibles en el [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst).

> **Nota:** GitHub Models se retirará a finales de julio de 2026. Aquí hay más detalles sobre el uso de [Microsoft Foundry Models](https://learn.microsoft.com/azure/ai-foundry/model-inference/overview?WT.mc_id=academic-105485-koreyst) para prototipar con modelos de IA.

> **Nota:** Las versiones específicas del modelo para las que esta lección fue escrita originalmente (Llama 3.1 70B/405B Instruct, Llama 3.2 11B/90B Vision Instruct) han sido retiradas del catálogo de Modelos Foundry de Microsoft. Los ejemplos de código a continuación usan `Llama-3.3-70B-Instruct` y `Llama-4-Scout-17B-16E-Instruct` como alternativas actualmente disponibles en el catálogo de Modelos Foundry de Microsoft, por lo que aún funcionan hoy en día.

Variantes del modelo (como se cubrió originalmente en esta lección): 
- Llama 3.1 - 70B Instruct (retirado) 
- Llama 3.1 - 405B Instruct (retirado) 
- Llama 3.2 - 11B Vision Instruct (retirado) 
- Llama 3.2 - 90B Vision Instruct (retirado) 

Alternativas actualmente disponibles utilizadas en los ejemplos de código: 
- Llama 3.3 - 70B Instrucciones (`Llama-3.3-70B-Instruct`) 
- Llama 4 Scout - 17B 16E Instrucciones (`Llama-4-Scout-17B-16E-Instruct`) 

*Nota: Las variantes de Llama 3 mencionadas arriba se conservan para contexto histórico y ya no están disponibles en los Modelos Microsoft Foundry.*

## Llama 3.1 

Con 405 mil millones de parámetros, Llama 3.1 entra en la categoría de LLM de código abierto. 

El modelo es una mejora respecto al lanzamiento anterior Llama 3, ofreciendo: 

- Ventana de contexto más grande - 128k tokens vs 8k tokens 
- Máximo de tokens de salida más grande - 4096 vs 2048 
- Mejor soporte multilingüe - debido al aumento de tokens de entrenamiento 

Esto permite que Llama 3.1 maneje casos de uso más complejos al construir aplicaciones GenAI, incluyendo: 
- Llamadas nativas a funciones - la capacidad de llamar a herramientas y funciones externas fuera del flujo de trabajo del LLM 
- Mejor rendimiento RAG - debido a la ventana de contexto más amplia 
- Generación de datos sintéticos - la capacidad de crear datos efectivos para tareas como el fine-tuning 

### Llamadas nativas a funciones 

Llama 3.1 ha sido afinado para ser más efectivo al hacer llamadas a funciones o herramientas. También tiene dos herramientas incorporadas que el modelo puede identificar como necesarias de usar según el prompt del usuario. Estas herramientas son: 

- **Brave Search** - Se puede usar para obtener información actualizada como el clima realizando una búsqueda web 
- **Wolfram Alpha** - Se puede usar para cálculos matemáticos más complejos, por lo que no es necesario escribir tus propias funciones. 

También puedes crear tus propias herramientas personalizadas que el LLM puede llamar. 

En el ejemplo de código a continuación: 

- Definimos las herramientas disponibles (brave_search, wolfram_alpha) en el prompt del sistema. 
- Enviamos un prompt de usuario que pregunta sobre el clima en cierta ciudad. 
- El LLM responderá con una llamada a herramienta a Brave Search que se verá así `<|python_tag|>brave_search.call(query="Stockholm weather")` 

*Nota: Este ejemplo solo hace la llamada a la herramienta, si quieres obtener los resultados, necesitarás crear una cuenta gratuita en la página de la API de Brave y definir la función en sí.

```python 
import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import AssistantMessage, SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Meta-Llama-3.1-405B-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-3.3-70B-Instruct, a currently available alternative, instead
model_name = "Llama-3.3-70B-Instruct"

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

A pesar de ser un LLM, una limitación de Llama 3.1 es su falta de multimodalidad. Es decir, la incapacidad de usar distintos tipos de entrada como imágenes como prompts y proporcionar respuestas. Esta capacidad es una de las principales características de Llama 3.2. Estas características también incluyen: 

- Multimodalidad - tiene la capacidad de evaluar tanto prompts de texto como de imagen 
- Variantes de tamaño pequeño a mediano (11B y 90B) - esto proporciona opciones flexibles de despliegue, 
- Variantes solo de texto (1B y 3B) - esto permite que el modelo se despliegue en dispositivos edge / móviles y proporciona baja latencia 

El soporte multimodal representa un gran paso en el mundo de los modelos de código abierto. El siguiente ejemplo de código toma tanto una imagen como un texto de indicación para obtener un análisis de la imagen. Debido a que Llama 3.2 90B Vision Instruct ha sido retirado, el ejemplo utiliza `Llama-4-Scout-17B-16E-Instruct`, una alternativa multimodal nativa actualmente disponible. 


### Soporte multimodal con Llama 3.2

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

# Get these from your Microsoft Foundry project's "Overview" page
token = os.environ["AZURE_INFERENCE_CREDENTIAL"]
endpoint = os.environ["AZURE_INFERENCE_ENDPOINT"]
# Llama-3.2-90B-Vision-Instruct was retired from Microsoft Foundry on 2026-06-13 with no replacement listed;
# using Llama-4-Scout-17B-16E-Instruct, a currently available natively multimodal alternative, instead
model_name = "Llama-4-Scout-17B-16E-Instruct"

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

## El aprendizaje no se detiene aquí, continúa el viaje

Después de completar esta lección, revisa nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento en IA Generativa!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->