# Introducción a los Modelos de Lenguaje Pequeños para IA Generativa para Principiantes
La IA generativa es un campo fascinante de la inteligencia artificial que se centra en crear sistemas capaces de generar contenido nuevo. Este contenido puede variar desde texto e imágenes hasta música e incluso entornos virtuales completos. Una de las aplicaciones más emocionantes de la IA generativa se encuentra en el ámbito de los modelos de lenguaje.

## ¿Qué Son los Modelos de Lenguaje Pequeños?

Un Modelo de Lenguaje Pequeño (SLM, por sus siglas en inglés) representa una variante reducida de un modelo de lenguaje grande (LLM), aprovechando muchos de los principios arquitectónicos y técnicas de los LLM, mientras exhibe una huella computacional significativamente reducida.

Los SLM son un subconjunto de modelos de lenguaje diseñados para generar texto similar al humano. A diferencia de sus contrapartes más grandes, como GPT-4, los SLM son más compactos y eficientes, lo que los hace ideales para aplicaciones donde los recursos computacionales son limitados. A pesar de su tamaño más pequeño, todavía pueden realizar una variedad de tareas. Típicamente, los SLM se construyen comprimiendo o destilando LLM, con el objetivo de retener una porción sustancial de la funcionalidad original y capacidades lingüísticas del modelo. Esta reducción en el tamaño del modelo disminuye la complejidad general, haciendo que los SLM sean más eficientes en términos de uso de memoria y requerimientos computacionales. A pesar de estas optimizaciones, los SLM aún pueden realizar una amplia gama de tareas de procesamiento de lenguaje natural (NLP):

- Generación de Texto: Crear oraciones o párrafos coherentes y contextualmente relevantes.
- Completado de Texto: Predecir y completar oraciones basadas en un prompt dado.
- Traducción: Convertir texto de un idioma a otro.
- Resumen: Condensar textos largos en resúmenes más cortos y digeribles.

Aunque con algunos sacrificios en el rendimiento o profundidad de comprensión en comparación con sus contrapartes más grandes.

## ¿Cómo Funcionan los Modelos de Lenguaje Pequeños?
Los SLM se entrenan con grandes cantidades de datos textuales. Durante el entrenamiento, aprenden los patrones y estructuras del lenguaje, lo que les permite generar texto que es gramaticalmente correcto y contextualmente apropiado. El proceso de entrenamiento incluye:

- Recolección de Datos: Recopilación de grandes conjuntos de datos de texto desde diversas fuentes.
- Preprocesamiento: Limpiar y organizar los datos para hacerlos adecuados para el entrenamiento.
- Entrenamiento: Usar algoritmos de aprendizaje automático para enseñar al modelo cómo entender y generar texto.
- Ajuste Fino: Ajustar el modelo para mejorar su desempeño en tareas específicas.

El desarrollo de los SLM se alinea con la creciente necesidad de modelos que puedan ser desplegados en entornos con recursos limitados, como dispositivos móviles o plataformas de computación en el borde, donde los LLM a gran escala pueden ser poco prácticos debido a sus exigencias de recursos. Al enfocarse en la eficiencia, los SLM equilibran el rendimiento con la accesibilidad, permitiendo una aplicación más amplia en diferentes dominios.

![slm](../../../translated_images/es/slm.4058842744d0444a.webp)

## Objetivos de Aprendizaje

En esta lección, esperamos introducir el conocimiento sobre SLM y combinarlo con Microsoft Phi-3 para aprender diferentes escenarios en contenido de texto, visión y MoE.

Al final de esta lección, deberías poder responder las siguientes preguntas:

- ¿Qué es un SLM?
- ¿Cuál es la diferencia entre SLM y LLM?
- ¿Qué es la familia Microsoft Phi-3/3.5?
- ¿Cómo hacer inferencia con la familia Microsoft Phi-3/3.5?

¿Listo? Comencemos.

## Las Distinciones entre Modelos de Lenguaje Grandes (LLMs) y Modelos de Lenguaje Pequeños (SLMs)

Tanto los LLM como los SLM están construidos sobre principios fundamentales del aprendizaje automático probabilístico, siguiendo enfoques similares en su diseño arquitectónico, metodologías de entrenamiento, procesos de generación de datos y técnicas de evaluación del modelo. Sin embargo, varios factores clave diferencian a estos dos tipos de modelos.

## Aplicaciones de Modelos de Lenguaje Pequeños

Los SLM tienen una amplia gama de aplicaciones, incluyendo:

- Chatbots: Proveer soporte al cliente y relacionarse con usuarios de manera conversacional.
- Creación de Contenido: Ayudar a escritores generando ideas o incluso redactando artículos completos.
- Educación: Asistir a estudiantes con tareas escritas o aprendizaje de nuevos idiomas.
- Accesibilidad: Crear herramientas para personas con discapacidades, como sistemas de texto a voz.

**Tamaño**

Una distinción principal entre LLM y SLM radica en la escala de los modelos. Los LLM, como ChatGPT (GPT-4), pueden contener un estimado de 1.76 billones de parámetros, mientras que SLM de código abierto como Mistral 7B están diseñados con significativamente menos parámetros—aproximadamente 7 mil millones. Esta disparidad se debe principalmente a diferencias en la arquitectura del modelo y los procesos de entrenamiento. Por ejemplo, ChatGPT emplea un mecanismo de autoatención dentro de un marco codificador-decodificador, mientras que Mistral 7B usa atención con ventana deslizante, lo que permite un entrenamiento más eficiente dentro de un modelo solo-decodificador. Esta variación arquitectónica tiene profundas implicaciones en la complejidad y rendimiento de estos modelos.

**Comprensión**

Los SLM suelen estar optimizados para un rendimiento dentro de dominios específicos, lo que los hace altamente especializados pero potencialmente limitados en su capacidad para proporcionar una comprensión contextual amplia en múltiples campos de conocimiento. En contraste, los LLM buscan simular inteligencia similar a la humana a un nivel más comprensivo. Entrenados en grandes y diversos conjuntos de datos, los LLM están diseñados para desempeñarse bien en una variedad de dominios, ofreciendo mayor versatilidad y adaptabilidad. En consecuencia, los LLM son más adecuados para una gama más amplia de tareas descendientes, como procesamiento de lenguaje natural y programación.

**Computación**

El entrenamiento y despliegue de los LLM son procesos intensivos en recursos, requiriendo a menudo una infraestructura computacional significativa, incluyendo clusters de GPU a gran escala. Por ejemplo, entrenar un modelo como ChatGPT desde cero puede necesitar miles de GPUs durante largos períodos. En contraste, los SLM, con su menor cantidad de parámetros, son más accesibles en términos de recursos computacionales. Modelos como Mistral 7B pueden ser entrenados y ejecutados en máquinas locales con capacidades GPU moderadas, aunque el entrenamiento aún demanda varias horas entre múltiples GPUs.

**Sesgo**

El sesgo es un problema conocido en los LLM, principalmente debido a la naturaleza de los datos de entrenamiento. Estos modelos suelen basarse en datos en bruto y disponibles abiertamente de Internet, que pueden subrepresentar o mal representar ciertos grupos, introducir etiquetado erróneo o reflejar sesgos lingüísticos influenciados por dialectos, variaciones geográficas y reglas gramaticales. Además, la complejidad de las arquitecturas LLM puede exacerbar inadvertidamente el sesgo, que podría pasar desapercibido sin un ajuste fino cuidadoso. Por otro lado, los SLM, al ser entrenados en conjuntos de datos más limitados y específicos de dominio, son inherentemente menos susceptibles a tales sesgos, aunque no están exentos de ellos.

**Inferencia**

El tamaño reducido de los SLM les otorga una ventaja significativa en términos de velocidad de inferencia, permitiéndoles generar resultados de manera eficiente en hardware local sin la necesidad de procesamiento paralelo extensivo. En contraste, los LLM, debido a su tamaño y complejidad, a menudo requieren recursos computacionales paralelos sustanciales para lograr tiempos de inferencia aceptables. La presencia de múltiples usuarios concurrentes ralentiza aún más los tiempos de respuesta de los LLM, especialmente cuando se despliegan a gran escala.

En resumen, aunque tanto los LLM como los SLM comparten una base fundamental en aprendizaje automático, difieren significativamente en términos de tamaño del modelo, requerimientos de recursos, comprensión contextual, susceptibilidad a sesgos y velocidad de inferencia. Estas distinciones reflejan su idoneidad respectiva para diferentes casos de uso, siendo los LLM más versátiles pero con un alto consumo de recursos, y los SLM ofreciendo eficiencia más específica para dominios con una demanda computacional reducida.

***Nota: En esta lección, presentaremos los SLM usando Microsoft Phi-3 / 3.5 como ejemplo.***

## Introducción a la familia Phi-3 / Phi-3.5

La familia Phi-3 / 3.5 está dirigida principalmente a escenarios de aplicación en texto, visión y Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para generación de texto, completado de chat y extracción de información de contenido, etc.

**Phi-3-mini**

El modelo de lenguaje de 3.8B parámetros está disponible en Microsoft Azure AI Studio, Hugging Face y Ollama. Los modelos Phi-3 superan significativamente a modelos de lenguaje de igual y mayor tamaño en benchmarks clave (ver números de benchmark más abajo, números más altos son mejores). Phi-3-mini supera a modelos del doble de tamaño, mientras que Phi-3-small y Phi-3-medium superan a modelos más grandes, incluido GPT-3.5.

**Phi-3-small y medium**

Con solo 7B parámetros, Phi-3-small supera a GPT-3.5T en una variedad de benchmarks de lenguaje, razonamiento, codificación y matemáticas.

El Phi-3-medium con 14B parámetros continúa esta tendencia y supera al Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerarlo una mejora de Phi-3-mini. Aunque los parámetros permanecen sin cambiar, mejora la capacidad de soportar múltiples idiomas (compatibilidad con más de 20 idiomas: árabe, chino, checo, danés, neerlandés, inglés, finés, francés, alemán, hebreo, húngaro, italiano, japonés, coreano, noruego, polaco, portugués, ruso, español, sueco, tailandés, turco, ucraniano) y añade un soporte más fuerte para contexto largo.

Phi-3.5-mini con 3.8B parámetros supera a modelos de lenguaje del mismo tamaño y está a la par con modelos del doble de tamaño.

### Phi-3 / 3.5 Visión

Podemos pensar en el modelo Instruct de Phi-3/3.5 como la capacidad de Phi para entender, y Visión es lo que le da ojos a Phi para comprender el mundo.

**Phi-3-Visión**

Phi-3-visión, con solo 4.2B parámetros, continúa esta tendencia y supera a modelos más grandes como Claude-3 Haiku y Gemini 1.0 Pro V en tareas generales de razonamiento visual, OCR, y en comprensión de tablas y diagramas.

**Phi-3.5-Visión**

Phi-3.5-Visión también es una mejora de Phi-3-Visión, añadiendo soporte para múltiples imágenes. Puedes considerarlo una mejora en visión, ya no solo puedes ver imágenes, sino también videos.

Phi-3.5-visión supera a modelos más grandes como Claude-3.5 Sonnet y Gemini 1.5 Flash en tareas de OCR, comprensión de tablas y gráficos y está a la par en tareas generales de razonamiento de conocimiento visual. Soporta entrada de múltiples cuadros, es decir, realizar razonamiento sobre múltiples imágenes de entrada.

### Phi-3.5-MoE

***Mixture of Experts (MoE)*** permite que los modelos se preentrenen con mucho menos cómputo, lo que significa que puedes escalar dramáticamente el tamaño del modelo o del conjunto de datos con el mismo presupuesto de cómputo que un modelo denso. En particular, un modelo MoE debería alcanzar la misma calidad que su contraparte densa mucho más rápido durante el preentrenamiento.

Phi-3.5-MoE comprende 16 módulos expertos de 3.8B cada uno. Phi-3.5-MoE con solo 6.6B parámetros activos logra un nivel similar de razonamiento, comprensión del lenguaje y matemáticas que modelos mucho más grandes.

Podemos usar los modelos de la familia Phi-3/3.5 según diferentes escenarios. A diferencia de los LLM, puedes desplegar Phi-3/3.5-mini o Phi-3/3.5-Visión en dispositivos edge.

## Cómo usar los modelos de la familia Phi-3/3.5

Esperamos utilizar Phi-3/3.5 en diferentes escenarios. A continuación, usaremos Phi-3/3.5 basado en diferentes escenarios.

![phi3](../../../translated_images/es/phi3.655208c3186ae381.webp)

### Inferencia mediante APIs en la nube

**GitHub Models**

GitHub Models es la forma más directa. Puedes acceder rápidamente al modelo Phi-3/3.5-Instruct a través de GitHub Models. Combinado con el SDK de Azure AI Inference / SDK de OpenAI, puedes acceder a la API mediante código para completar la llamada a Phi-3/3.5-Instruct. También puedes probar diferentes resultados a través de Playground.

- Demo: Comparación de los efectos de Phi-3-mini y Phi-3.5-mini en escenarios en chino

![phi3](../../../translated_images/es/gh1.126c6139713b622b.webp)

![phi35](../../../translated_images/es/gh2.07d7985af66f178d.webp)

**Azure AI Studio**

O si queremos usar los modelos de visión y MoE, puedes usar Azure AI Studio para completar la llamada. Si te interesa, puedes leer el Phi-3 Cookbook para aprender cómo llamar a Phi-3/3.5 Instruct, Visión, MoE a través de Azure AI Studio [Haz clic en este enlace](https://github.com/microsoft/Phi-3CookBook/blob/main/md/02.QuickStart/AzureAIStudio_QuickStart.md?WT.mc_id=academic-105485-koreyst)

**NVIDIA NIM**

Además de las soluciones del catálogo de modelos basadas en la nube proporcionadas por Azure y GitHub, también puedes usar [NVIDIA NIM](https://developer.nvidia.com/nim?WT.mc_id=academic-105485-koreyst) para completar llamadas relacionadas. Puedes visitar NVIDIA NIM para completar las llamadas a la API de la familia Phi-3/3.5. NVIDIA NIM (NVIDIA Inference Microservices) es un conjunto de microservicios acelerados de inferencia diseñados para ayudar a los desarrolladores a desplegar modelos de IA eficientemente en diversos entornos, incluyendo nubes, centros de datos y estaciones de trabajo.

Aquí hay algunas características clave de NVIDIA NIM:
- **Facilidad de Despliegue:** NIM permite el despliegue de modelos de IA con un solo comando, facilitando su integración en flujos de trabajo existentes.  
- **Rendimiento Optimizado:** Aprovecha los motores de inferencia preoptimizados de NVIDIA, como TensorRT y TensorRT-LLM, para garantizar baja latencia y alto rendimiento.  
- **Escalabilidad:** NIM soporta el autoescalado en Kubernetes, permitiendo manejar cargas de trabajo variables de forma eficiente.  
- **Seguridad y Control:** Las organizaciones pueden mantener el control sobre sus datos y aplicaciones alojando los microservicios NIM en su propia infraestructura gestionada.  
- **APIs Estándar:** NIM proporciona APIs estándar de la industria, facilitando la creación e integración de aplicaciones de IA como chatbots, asistentes de IA y más.  

NIM es parte de NVIDIA AI Enterprise, cuyo objetivo es simplificar el despliegue y la operacionalización de modelos de IA, asegurando que funcionen eficientemente en GPUs NVIDIA.

- Demostración: Usando NVIDIA NIM para llamar a Phi-3.5-Vision-API [[Haz clic en este enlace](./python/Phi-3-Vision-Nividia-NIM.ipynb?WT.mc_id=academic-105485-koreyst)]


### Ejecutando Phi-3/3.5 Localmente  
La inferencia en relación con Phi-3, o cualquier modelo de lenguaje como GPT-3, se refiere al proceso de generar respuestas o predicciones basadas en la entrada que recibe. Cuando proporcionas un prompt o pregunta a Phi-3, utiliza su red neuronal entrenada para inferir la respuesta más probable y relevante analizando patrones y relaciones en los datos con los que fue entrenado.

**Hugging Face Transformer**  
Hugging Face Transformers es una biblioteca poderosa diseñada para el procesamiento del lenguaje natural (NLP) y otras tareas de aprendizaje automático. Aquí algunos puntos clave:

1. **Modelos Preentrenados:** Ofrece miles de modelos preentrenados que se pueden usar para tareas como clasificación de texto, reconocimiento de entidades nombradas, respuesta a preguntas, resumen, traducción y generación de texto.

2. **Interoperabilidad de Frameworks:** La biblioteca soporta múltiples frameworks de aprendizaje profundo, incluyendo PyTorch, TensorFlow y JAX. Esto permite entrenar un modelo en un framework y usarlo en otro.

3. **Capacidades Multimodales:** Además de NLP, Hugging Face Transformers soporta tareas en visión computacional (por ejemplo, clasificación de imágenes, detección de objetos) y procesamiento de audio (por ejemplo, reconocimiento de voz, clasificación de audio).

4. **Facilidad de Uso:** La biblioteca ofrece APIs y herramientas para descargar y ajustar modelos fácilmente, haciéndola accesible para principiantes y expertos.

5. **Comunidad y Recursos:** Hugging Face cuenta con una comunidad vibrante y extensa documentación, tutoriales y guías para ayudar a los usuarios a comenzar y aprovechar al máximo la biblioteca.  
[documentación oficial](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) o su [repositorio de GitHub](https://github.com/huggingface/transformers?WT.mc_id=academic-105485-koreyst).

Este es el método más comúnmente usado, pero también requiere aceleración por GPU. Después de todo, escenarios como Vision y MoE requieren muchos cálculos, que serían muy lentos en CPU si no están cuantificados.


- Demostración: Usando Transformer para llamar a Phi-3.5-Instruct [Haz clic en este enlace](./python/phi35-instruct-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demostración: Usando Transformer para llamar a Phi-3.5-Vision [Haz clic en este enlace](./python/phi35-vision-demo.ipynb?WT.mc_id=academic-105485-koreyst)

- Demostración: Usando Transformer para llamar a Phi-3.5-MoE [Haz clic en este enlace](./python/phi35_moe_demo.ipynb?WT.mc_id=academic-105485-koreyst)

**Ollama**  
[Ollama](https://ollama.com/?WT.mc_id=academic-105485-koreyst) es una plataforma diseñada para facilitar la ejecución local de modelos de lenguaje grandes (LLMs) en tu equipo. Soporta varios modelos como Llama 3.1, Phi 3, Mistral y Gemma 2, entre otros. La plataforma simplifica el proceso al agrupar pesos de modelos, configuración y datos en un solo paquete, haciéndolo más accesible para que los usuarios personalicen y creen sus propios modelos. Ollama está disponible para macOS, Linux y Windows. Es una gran herramienta si quieres experimentar o desplegar LLMs sin depender de servicios en la nube. Ollama es la forma más directa, solo necesitas ejecutar el siguiente comando.


```bash

ollama run phi3.5

```


**ONNX Runtime para GenAI**

[ONNX Runtime](https://github.com/microsoft/onnxruntime-genai?WT.mc_id=academic-105485-koreyst) es un acelerador multiplataforma para inferencia y entrenamiento de machine learning. ONNX Runtime para Generative AI (GENAI) es una herramienta poderosa que ayuda a ejecutar modelos generativos de IA de manera eficiente en varias plataformas.

## ¿Qué es ONNX Runtime?  
ONNX Runtime es un proyecto open source que permite la inferencia de alto rendimiento de modelos de machine learning. Soporta modelos en formato Open Neural Network Exchange (ONNX), que es un estándar para representar modelos de machine learning. La inferencia con ONNX Runtime puede ofrecer experiencias de usuario más rápidas y reducir costos, soportando modelos de frameworks como PyTorch y TensorFlow/Keras, así como librerías clásicas de machine learning como scikit-learn, LightGBM, XGBoost, etc. ONNX Runtime es compatible con diferentes hardware, drivers y sistemas operativos, y proporciona rendimiento óptimo aprovechando aceleradores de hardware donde aplique junto con optimizaciones y transformaciones de grafo.

## ¿Qué es Generative AI?  
La IA generativa se refiere a sistemas de IA que pueden generar contenido nuevo, como texto, imágenes o música, basándose en los datos con los que fueron entrenados. Ejemplos incluyen modelos de lenguaje como GPT-3 y modelos de generación de imágenes como Stable Diffusion. La librería ONNX Runtime para GenAI proporciona el ciclo de IA generativa para modelos ONNX, incluyendo inferencia con ONNX Runtime, procesamiento de logits, búsqueda y muestreo, y gestión de caché KV.

## ONNX Runtime para GENAI  
ONNX Runtime para GENAI extiende las capacidades de ONNX Runtime para soportar modelos de IA generativa. Algunas características clave:

- **Amplio Soporte de Plataformas:** Funciona en varias plataformas, incluyendo Windows, Linux, macOS, Android e iOS.  
- **Soporte de Modelos:** Soporta muchos modelos populares de IA generativa, como LLaMA, GPT-Neo, BLOOM y más.  
- **Optimización de Rendimiento:** Incluye optimizaciones para diferentes aceleradores de hardware como GPUs NVIDIA, GPUs AMD y más.  
- **Facilidad de Uso:** Proporciona APIs para una integración sencilla en aplicaciones, permitiendo generar texto, imágenes y otros contenidos con código mínimo.  
- Los usuarios pueden llamar a un método de alto nivel generate() o ejecutar cada iteración del modelo en un bucle, generando un token a la vez, actualizando opcionalmente parámetros de generación dentro del bucle.  
- ONNX Runtime también soporta búsqueda greedy/beam y muestreo TopP, TopK para generar secuencias de tokens y procesamiento incorporado de logits como penalizaciones por repetición. También puedes agregar fácilmente puntuaciones personalizadas.

## Comenzando  
Para comenzar con ONNX Runtime para GENAI, sigue estos pasos:

### Instala ONNX Runtime:  
```Python
pip install onnxruntime
```
### Instala las Extensiones de IA Generativa:  
```Python
pip install onnxruntime-genai
```
  
### Ejecuta un Modelo: Aquí un ejemplo simple en Python:  
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
### Demostración: Usando ONNX Runtime GenAI para llamar Phi-3.5-Vision  


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

Además de ONNX Runtime y los métodos de referencia Ollama, también podemos completar la referencia de modelos cuantitativos basándonos en los métodos de referencia de los diferentes fabricantes. Tales como el framework Apple MLX con Apple Metal, Qualcomm QNN con NPU, Intel OpenVINO con CPU/GPU, etc. También puedes obtener más contenido en el [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).


## Más

Hemos aprendido los conceptos básicos de la familia Phi-3/3.5, pero para aprender más sobre SLM necesitamos más conocimientos. Puedes encontrar las respuestas en el Phi-3 Cookbook. Si quieres aprender más, por favor visita el [Phi-3 Cookbook](https://github.com/microsoft/phi-3cookbook?WT.mc_id=academic-105485-koreyst).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->