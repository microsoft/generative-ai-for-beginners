# Introducción a los Modelos de Lenguaje Pequeños para IA Generativa para Principiantes
La IA generativa es un campo fascinante de la inteligencia artificial que se centra en crear sistemas capaces de generar contenido nuevo. Este contenido puede variar desde texto e imágenes hasta música e incluso entornos virtuales completos. Una de las aplicaciones más emocionantes de la IA generativa es en el ámbito de los modelos de lenguaje.

## ¿Qué son los Modelos de Lenguaje Pequeños?

Un Modelo de Lenguaje Pequeño (SLM) representa una variante reducida de un modelo de lenguaje grande (LLM), aprovechando muchos de los principios arquitectónicos y técnicas de los LLM, pero con una huella computacional significativamente reducida.

Los SLM son un subconjunto de modelos de lenguaje diseñados para generar texto similar al humano. A diferencia de sus contrapartes más grandes, como GPT-4, los SLM son más compactos y eficientes, lo que los hace ideales para aplicaciones donde los recursos computacionales son limitados. A pesar de su tamaño reducido, aún pueden realizar una variedad de tareas. Normalmente, los SLM se construyen comprimiendo o destilando LLM, con el objetivo de retener una porción sustancial de la funcionalidad y capacidades lingüísticas del modelo original. Esta reducción en el tamaño del modelo disminuye la complejidad general, haciendo a los SLM más eficientes tanto en el uso de memoria como en los requerimientos computacionales. A pesar de estas optimizaciones, los SLM aún pueden realizar una amplia gama de tareas de procesamiento de lenguaje natural (NLP):

- Generación de Texto: Crear oraciones o párrafos coherentes y contextualmente relevantes.
- Completado de Texto: Predecir y completar oraciones basándose en un estímulo dado.
- Traducción: Convertir texto de un idioma a otro.
- Resumen: Condensar textos largos en resúmenes más cortos y digeribles.

Aunque con algunos compromisos en rendimiento o profundidad de comprensión comparados con sus contrapartes más grandes.

## ¿Cómo Funcionan los Modelos de Lenguaje Pequeños?
Los SLM se entrenan con grandes cantidades de datos textuales. Durante el entrenamiento, aprenden los patrones y estructuras del lenguaje, permitiéndoles generar texto que es tanto gramaticalmente correcto como contextualmente apropiado. El proceso de entrenamiento incluye:

- Recolección de Datos: Recopilar grandes conjuntos de datos de texto de diversas fuentes.
- Preprocesamiento: Limpiar y organizar los datos para hacerlos adecuados para el entrenamiento.
- Entrenamiento: Utilizar algoritmos de aprendizaje automático para enseñar al modelo cómo entender y generar texto.
- Ajuste Fino: Ajustar el modelo para mejorar su rendimiento en tareas específicas.

El desarrollo de los SLM está alineado con la necesidad creciente de modelos que puedan desplegarse en entornos con recursos limitados, como dispositivos móviles o plataformas de computación en el borde, donde los LLM completos pueden ser poco prácticos debido a sus altas demandas de recursos. Al centrarse en la eficiencia, los SLM equilibran el desempeño con la accesibilidad, permitiendo una aplicación más amplia en varios dominios.

![slm](../../../translated_images/es/slm.4058842744d0444a.webp)

## Objetivos de Aprendizaje

En esta lección, esperamos introducir el conocimiento sobre SLM y combinarlo con Microsoft Phi-3 para aprender diferentes escenarios en contenido de texto, visión y MoE.

Al finalizar esta lección, deberías poder responder las siguientes preguntas:

- ¿Qué es un SLM?
- ¿Cuál es la diferencia entre SLM y LLM?
- ¿Qué es la Familia Microsoft Phi-3/3.5?
- ¿Cómo ejecutar inferencias con la Familia Microsoft Phi-3/3.5?

¿Listo? Comencemos.

## Las Diferencias entre Modelos de Lenguaje Grandes (LLMs) y Modelos de Lenguaje Pequeños (SLMs)

Tanto los LLM como los SLM se basan en principios fundamentales del aprendizaje automático probabilístico, siguiendo enfoques similares en su diseño arquitectónico, metodologías de entrenamiento, procesos de generación de datos y técnicas de evaluación de modelos. Sin embargo, varios factores clave diferencian estos dos tipos de modelos.

## Aplicaciones de los Modelos de Lenguaje Pequeños

Los SLM tienen una amplia gama de aplicaciones, incluyendo:

- Chatbots: Proporcionar soporte al cliente y relacionarse con usuarios de manera conversacional.
- Creación de Contenido: Asistir a escritores generando ideas o incluso redactando artículos completos.
- Educación: Ayudar a estudiantes con tareas de escritura o aprendizaje de nuevos idiomas.
- Accesibilidad: Crear herramientas para personas con discapacidades, como sistemas de texto a voz.

**Tamaño**
  
Una distinción principal entre LLM y SLM radica en la escala de los modelos. Los LLMs, como ChatGPT (GPT-4), pueden comprender un estimado de 1.76 billones de parámetros, mientras que los SLMs de código abierto como Mistral 7B están diseñados con parámetros significativamente menores—aproximadamente 7 mil millones. Esta disparidad se debe principalmente a las diferencias en la arquitectura del modelo y los procesos de entrenamiento. Por ejemplo, ChatGPT emplea un mecanismo de autoatención dentro de un marco encoder-decoder, mientras que Mistral 7B utiliza atención de ventana deslizante, que permite un entrenamiento más eficiente dentro de un modelo solo decoder. Esta variación arquitectónica tiene profundas implicaciones para la complejidad y el rendimiento de estos modelos.

**Comprensión**

Los SLMs se optimizan típicamente para el rendimiento dentro de dominios específicos, haciéndolos altamente especializados pero potencialmente limitados en su capacidad para proporcionar una comprensión contextual amplia en múltiples campos del conocimiento. En contraste, los LLMs buscan simular inteligencia similar a la humana en un nivel más comprensivo. Entrenados con grandes y diversos conjuntos de datos, los LLMs están diseñados para desempeñarse bien en una variedad de dominios, ofreciendo mayor versatilidad y adaptabilidad. En consecuencia, los LLMs son más adecuados para una variedad más amplia de tareas posteriores, como procesamiento de lenguaje natural y programación.

**Computación**

El entrenamiento y despliegue de LLMs son procesos que requieren muchos recursos, frecuentemente necesitando una infraestructura computacional significativa, incluyendo grandes clústeres de GPU. Por ejemplo, entrenar un modelo como ChatGPT desde cero puede requerir miles de GPUs durante periodos prolongados. En contraste, los SLMs, con sus menores cantidades de parámetros, son más accesibles en términos de recursos computacionales. Modelos como Mistral 7B pueden ser entrenados y ejecutados en máquinas locales equipadas con GPUs moderadas, aunque el entrenamiento aún demanda varias horas en múltiples GPUs.

**Sesgo**

El sesgo es un problema conocido en los LLMs, principalmente debido a la naturaleza de los datos de entrenamiento. Estos modelos a menudo dependen de datos crudos y abiertos disponibles en internet, que pueden subrepresentar o representar erróneamente ciertos grupos, introducir etiquetados erróneos o reflejar sesgos lingüísticos influenciados por dialectos, variaciones geográficas y reglas gramaticales. Además, la complejidad de las arquitecturas LLM puede, inadvertidamente, exacerbar el sesgo, el cual puede pasar desapercibido sin un ajuste fino cuidadoso. Por otro lado, los SLM, al estar entrenados en conjuntos de datos más restringidos y específicos por dominio, son inherentemente menos susceptibles a dichos sesgos, aunque no están exentos de ellos.

**Inferencia**

El tamaño reducido de los SLM les proporciona una ventaja significativa en términos de velocidad de inferencia, permitiéndoles generar salidas eficientemente en hardware local sin la necesidad de un procesamiento paralelo extenso. En contraste, los LLMs, debido a su tamaño y complejidad, suelen requerir recursos computacionales paralelos sustanciales para lograr tiempos de inferencia aceptables. La presencia de múltiples usuarios concurrentes además ralentiza los tiempos de respuesta de los LLMs, especialmente cuando se implementan a gran escala.

En resumen, aunque tanto los LLMs como los SLMs comparten una base fundamental en aprendizaje automático, difieren significativamente en términos de tamaño del modelo, requisitos de recursos, comprensión contextual, susceptibilidad a sesgos y velocidad de inferencia. Estas distinciones reflejan su idoneidad respectiva para diferentes casos de uso, siendo los LLMs más versátiles pero con altos requerimientos de recursos, y los SLMs ofreciendo una eficiencia más específica por dominio con demandas computacionales reducidas.

***Nota: En esta lección, presentaremos los SLM usando Microsoft Phi-3 / 3.5 como ejemplo.***

## Presentación de la Familia Phi-3 / Phi-3.5

La Familia Phi-3 / 3.5 se enfoca principalmente en escenarios de aplicación de texto, visión y Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para generación de texto, completado de chat y extracción de información de contenido, etc.

**Phi-3-mini**

El modelo de lenguaje de 3.8B está disponible en Microsoft Foundry, Hugging Face y Ollama. Los modelos Phi-3 superan significativamente a modelos de lenguaje de tamaños iguales y mayores en puntos de referencia clave (ver números de benchmark abajo, números más altos son mejores). Phi-3-mini supera modelos que tienen el doble de su tamaño, mientras que Phi-3-small y Phi-3-medium superan modelos más grandes, incluyendo GPT-3.5.

**Phi-3-small & medium**

Con solo 7B parámetros, Phi-3-small supera a GPT-3.5T en una variedad de benchmarks de lenguaje, razonamiento, codificación y matemáticas.

El Phi-3-medium con 14B parámetros continúa esta tendencia y supera al Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerarlo como una actualización de Phi-3-mini. Aunque los parámetros permanecen sin cambios, mejora la capacidad de soportar múltiples idiomas (soporta más de 20 idiomas: árabe, chino, checo, danés, holandés, inglés, finlandés, francés, alemán, hebreo, húngaro, italiano, japonés, coreano, noruego, polaco, portugués, ruso, español, sueco, tailandés, turco, ucraniano) y añade un soporte más fuerte para contexto largo.

Phi-3.5-mini con 3.8B parámetros supera a modelos de lenguaje de igual tamaño y está a la par con modelos del doble de tamaño.

### Phi-3 / 3.5 Visión

Podemos pensar en el modelo Instruct de Phi-3/3.5 como la capacidad de Phi para entender, y en Visión es lo que da a Phi ojos para comprender el mundo.


**Phi-3-Visión**

Phi-3-visión, con solo 4.2B parámetros, continúa esta tendencia y supera modelos más grandes como Claude-3 Haiku y Gemini 1.0 Pro V en tareas generales de razonamiento visual, OCR y comprensión de tablas y diagramas.


**Phi-3.5-Visión**

Phi-3.5-Visión es también una mejora de Phi-3-Visión, añadiendo soporte para múltiples imágenes. Se puede pensar como una mejora en visión, no solo puedes ver imágenes, sino también videos.

Phi-3.5-visión supera modelos más grandes como Claude-3.5 Sonnet y Gemini 1.5 Flash en tareas de OCR, comprensión de tablas y gráficos y está a la par en tareas generales de razonamiento visual de conocimiento. Soporta entrada de múltiples fotogramas, es decir, realizar razonamiento sobre múltiples imágenes de entrada.


### Phi-3.5-MoE

***Mezcla de Expertos (MoE)*** permite que los modelos se preentrenen con mucho menos cómputo, lo que significa que se puede escalar dramáticamente el tamaño del modelo o del conjunto de datos con el mismo presupuesto de cómputo que un modelo denso. En particular, un modelo MoE debería alcanzar la misma calidad que su contraparte densa mucho más rápido durante el preentrenamiento.

Phi-3.5-MoE comprende 16x módulos expertos de 3.8B. Phi-3.5-MoE con solo 6.6B parámetros activos logra un nivel similar de razonamiento, comprensión lingüística y matemáticas que modelos mucho más grandes.

Podemos usar el modelo de la familia Phi-3/3.5 basado en diferentes escenarios. A diferencia de LLM, puedes desplegar Phi-3/3.5-mini o Phi-3/3.5-Visión en dispositivos edge.


## Cómo utilizar los modelos de la familia Phi-3/3.5

Esperamos usar Phi-3/3.5 en diferentes escenarios. A continuación, usaremos Phi-3/3.5 basado en distintos escenarios.

![phi3](../../../translated_images/es/phi3.655208c3186ae381.webp)

### Inferencia mediante APIs en la nube

**Modelos Microsoft Foundry**

> **Nota:** GitHub Models se retirará a finales de julio de 2026. [Microsoft Foundry Models](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) es el reemplazo directo.

Microsoft Foundry Models es la forma más directa. Puedes acceder rápidamente al modelo Phi-3/3.5-Instruct a través del catálogo de modelos Foundry. Combinado con Azure AI Inference SDK / OpenAI SDK, puedes acceder a la API mediante código para completar la llamada Phi-3/3.5-Instruct. También puedes probar diferentes efectos a través del Playground.

- Demo: Comparación de los efectos de Phi-3-mini y Phi-3.5-mini en escenarios en chino

![phi3](../../../translated_images/es/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/es/gh2.07d7985af66f178d.webp)


**Microsoft Foundry**

O si deseas usar los modelos de visión y MoE, puedes usar Microsoft Foundry para completar la llamada. Si estás interesado, puedes leer el Phi-3 Cookbook para aprender a llamar a Phi-3/3.5 Instruct, Visión, MoE a través de Microsoft Foundry [Haz clic en este enlace](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)


**NVIDIA NIM**

Además del catálogo de modelos en la nube Microsoft Foundry Models, también puedes usar [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para completar las llamadas relacionadas. Puedes visitar NVIDIA NIM para completar las llamadas a la API de la Familia Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) es un conjunto de microservicios de inferencia acelerada diseñados para ayudar a los desarrolladores a desplegar modelos de IA eficientemente en varios entornos, incluyendo nubes, centros de datos y estaciones de trabajo.

Aquí algunas características clave de NVIDIA NIM:

- **Facilidad de Despliegue:** NIM permite despliegues de modelos de IA con un solo comando, facilitando su integración en flujos de trabajo existentes.

- **Rendimiento Optimizado:** Aprovecha los motores de inferencia preoptimizados de NVIDIA, como TensorRT y TensorRT-LLM, para garantizar baja latencia y alto rendimiento.
- **Escalabilidad:** NIM soporta escalado automático en Kubernetes, permitiéndole manejar cargas de trabajo variables de manera efectiva.
- **Seguridad y Control:** Las organizaciones pueden mantener el control sobre sus datos y aplicaciones al alojar los microservicios de NIM en su propia infraestructura gestionada.
- **APIs Estándar:** NIM proporciona APIs estándar de la industria, facilitando la creación e integración de aplicaciones de IA como chatbots, asistentes de IA y más.

NIM es parte de NVIDIA AI Enterprise, que tiene como objetivo simplificar el despliegue y la operacionalización de modelos de IA, asegurando que funcionen eficientemente en GPUs NVIDIA.

- Demo: Usando NVIDIA NIM para llamar a Phi-3.5-Vision-API  [[Haz clic en este enlace](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Ejecutando Phi-3/3.5 Localmente
La inferencia en relación con Phi-3, o cualquier modelo de lenguaje como GPT-3, se refiere al proceso de generar respuestas o predicciones basadas en la entrada que recibe. Cuando proporcionas un prompt o pregunta a Phi-3, este utiliza su red neuronal entrenada para inferir la respuesta más probable y relevante analizando patrones y relaciones en los datos en los que fue entrenado.

**Hugging Face Transformer**
Hugging Face Transformers es una poderosa biblioteca diseñada para procesamiento de lenguaje natural (NLP) y otras tareas de aprendizaje automático. Aquí algunos puntos clave sobre ella:

1. **Modelos Preentrenados**: Proporciona miles de modelos preentrenados que pueden usarse para diversas tareas como clasificación de texto, reconocimiento de entidades nombradas, respuesta a preguntas, resumen, traducción y generación de texto.

2. **Interoperabilidad de Frameworks**: La biblioteca soporta múltiples frameworks de aprendizaje profundo, incluyendo PyTorch, TensorFlow y JAX. Esto permite entrenar un modelo en un framework y usarlo en otro.

3. **Capacidades Multimodales:** Además de NLP, Hugging Face Transformers también soporta tareas en visión computarizada (p. ej., clasificación de imágenes, detección de objetos) y procesamiento de audio (p. ej., reconocimiento de voz, clasificación de audio).

4. **Facilidad de Uso:** La biblioteca ofrece APIs y herramientas para descargar y afinar modelos fácilmente, haciéndola accesible tanto para principiantes como expertos.

5. **Comunidad y Recursos:** Hugging Face tiene una comunidad vibrante y extensa documentación, tutoriales y guías para ayudar a los usuarios a comenzar y aprovechar al máximo la biblioteca.
[documentación oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o su [repositorio GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este es el método más comúnmente utilizado, pero también requiere aceleración GPU. Después de todo, escenarios como Visión y MoE requieren muchos cálculos, que serán muy lentos en CPU si no están cuantificados.


- Demo: Usando Transformer para llamar a Phi-3.5-Instruct [Haz clic en este enlace](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usando Transformer para llamar a Phi-3.5-Vision [Haz clic en este enlace](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demo: Usando Transformer para llamar a Phi-3.5-MoE [Haz clic en este enlace](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) es una plataforma diseñada para facilitar la ejecución de grandes modelos de lenguaje (LLMs) localmente en tu máquina. Soporta varios modelos como Llama 3.1, Phi 3, Mistral y Gemma 2, entre otros. La plataforma simplifica el proceso al empaquetar pesos del modelo, configuración y datos en un solo paquete, haciendo que sea más accesible para que los usuarios personalicen y creen sus propios modelos. Ollama está disponible para macOS, Linux y Windows. Es una excelente herramienta si buscas experimentar o desplegar LLMs sin depender de servicios en la nube. Ollama es la forma más directa, solo necesitas ejecutar el siguiente comando.


```bash

ollama run phi3.5

```

**Foundry Local**

[Foundry Local](https://foundrylocal.ai?WT.mc_id=academic-105485-koreyst) es el runtime offline y en dispositivo de Microsoft para ejecutar modelos como Phi totalmente en tu propio hardware — sin necesidad de suscripción a Azure, clave API o conexión de red. Automáticamente selecciona el mejor proveedor de ejecución disponible (NPU, GPU o CPU) y expone un endpoint compatible con OpenAI, para que el código existente del SDK `openai`/Azure AI Inference pueda apuntar a él con cambios mínimos. Consulta la [documentación de Foundry Local](https://learn.microsoft.com/azure/ai-foundry/foundry-local/get-started?WT.mc_id=academic-105485-koreyst) para comenzar.

```bash

winget install Microsoft.FoundryLocal
foundry model run phi-3.5-mini

```

O usa el SDK directamente en Python:

```bash

pip install foundry-local-sdk

```

```python

from foundry_local import FoundryLocalManager

manager = FoundryLocalManager("phi-3.5-mini")
print(manager.endpoint, manager.api_key)

```

**ONNX Runtime para GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) es un acelerador de aprendizaje automático multiplataforma para inferencia y entrenamiento. ONNX Runtime para Inteligencia Artificial Generativa (GENAI) es una herramienta poderosa que te ayuda a ejecutar modelos generativos de IA eficientemente en varias plataformas.

## ¿Qué es ONNX Runtime?
ONNX Runtime es un proyecto de código abierto que permite inferencia de alto rendimiento de modelos de aprendizaje automático. Soporta modelos en el formato Open Neural Network Exchange (ONNX), que es un estándar para representar modelos de aprendizaje automático. La inferencia con ONNX Runtime puede habilitar experiencias más rápidas para el usuario y costos más bajos, soportando modelos de frameworks de aprendizaje profundo como PyTorch y TensorFlow/Keras, así como bibliotecas clásicas de aprendizaje automático como scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime es compatible con diferentes hardware, drivers y sistemas operativos, y provee un rendimiento óptimo aprovechando aceleradores de hardware donde aplique junto con optimizaciones y transformaciones de grafo.

## ¿Qué es la Inteligencia Artificial Generativa?
La IA generativa se refiere a sistemas de IA que pueden generar contenido nuevo, como texto, imágenes o música, basándose en los datos con los que han sido entrenados. Ejemplos incluyen modelos de lenguaje como GPT-3 y modelos generadores de imágenes como Stable Diffusion. La biblioteca ONNX Runtime para GenAI provee el ciclo generativo de IA para modelos ONNX, incluyendo inferencia con ONNX Runtime, procesamiento de logits, búsqueda y muestreo, y gestión de caché KV.

## ONNX Runtime para GENAI
ONNX Runtime para GENAI extiende las capacidades de ONNX Runtime para soportar modelos generativos de IA. Aquí algunas características clave:

- **Amplio Soporte de Plataformas:** Funciona en varias plataformas, incluyendo Windows, Linux, macOS, Android e iOS.
- **Soporte de Modelos:** Soporta muchos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM, y más.
- **Optimización de Rendimiento:** Incluye optimizaciones para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD, y más2.
- **Facilidad de Uso:** Proporciona APIs para una fácil integración en aplicaciones, permitiéndote generar texto, imágenes y otros contenidos con código mínimo.
- Los usuarios pueden llamar al método de alto nivel generate(), o ejecutar cada iteración del modelo en un ciclo, generando un token a la vez y opcionalmente actualizando parámetros de generación dentro del ciclo.
- ONNX Runtime también soporta búsqueda codiciosa/beam search y muestreo TopP, TopK para generar secuencias de tokens y procesamiento integrado de logits como penalizaciones por repetición. También puedes agregar fácilmente puntuaciones personalizadas.

## Comenzando
Para comenzar con ONNX Runtime para GENAI, puedes seguir estos pasos:

### Instalar ONNX Runtime:
```Python
pip install onnxruntime
```
### Instalar las Extensiones de IA Generativa:
```Python
pip install onnxruntime-genai
```

### Ejecutar un Modelo: Aquí un ejemplo simple en Python:
```Python
import onnxruntime_genai as og

model = og.Model('path_to_your_model.onnx')

tokenizer = og.Tokenizer(model)

input_text = "Hello, how are you?"

input_tokens = tokenizer.encode(input_text)

output_tokens = model.generate(input_tokens)

output_text = tokenizer.decode(output_tokens)

print(output_text) 
```
### Demo: Usando ONNX Runtime GenAI para llamar a Phi-3.5-Vision


```python

import onnxruntime_genai as og

model_path = './Your Phi-3.5-vision-instruct ONNX Path'

img_path = './Your Image Path'

model = og.Model(model_path)

processor = model.create_multimodal_processor()

tokenizer_stream = processor.create_stream()

text = "Your Prompt"

prompt = "<|user|>\n"

prompt += "<|image_1|>\n"

prompt += f"{text}<|end|>\n"

prompt += "<|assistant|>\n"

image = og.Images.open(img_path)

inputs = processor(prompt, images=image)

params = og.GeneratorParams(model)

params.set_inputs(inputs)

params.set_search_options(max_length=3072)

generator = og.Generator(model, params)

while not generator.is_done():

    generator.compute_logits()
    
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    
    output = tokenizer_stream.decode(new_token)
    
    print(tokenizer_stream.decode(new_token), end='', flush=True)

```


**Otros**

Además de los métodos de referencia ONNX Runtime, Ollama y Foundry Local, también podemos completar la referencia de modelos cuantitativos basados en los métodos de referencia de modelos proporcionados por diferentes fabricantes. Como el framework Apple MLX con Apple Metal, Qualcomm QNN con NPU, Intel OpenVINO con CPU/GPU, etc. También puedes obtener más contenido de [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst)


## Más

Hemos aprendido lo básico de la familia Phi-3/3.5, pero para aprender más sobre SLM necesitamos más conocimiento. Puedes encontrar las respuestas en el Phi-3 Cookbook. Si deseas aprender más, por favor visita el [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->