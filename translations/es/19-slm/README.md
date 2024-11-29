```markdown
# Introducción a los Modelos de Lenguaje Pequeños para IA Generativa para Principiantes

La IA generativa es un campo fascinante de la inteligencia artificial que se centra en crear sistemas capaces de generar nuevo contenido. Este contenido puede variar desde texto e imágenes hasta música e incluso entornos virtuales completos. Una de las aplicaciones más emocionantes de la IA generativa es en el ámbito de los modelos de lenguaje.

## ¿Qué son los Modelos de Lenguaje Pequeños?

Un Modelo de Lenguaje Pequeño (SLM) representa una variante reducida de un modelo de lenguaje grande (LLM), aprovechando muchos de los principios arquitectónicos y técnicas de los LLM, mientras exhibe una huella computacional significativamente reducida. Los SLM son un subconjunto de modelos de lenguaje diseñados para generar texto similar al humano. A diferencia de sus contrapartes más grandes, como GPT-4, los SLM son más compactos y eficientes, lo que los hace ideales para aplicaciones donde los recursos computacionales son limitados. A pesar de su menor tamaño, aún pueden realizar una variedad de tareas. Típicamente, los SLM se construyen comprimiendo o destilando LLM, con el objetivo de retener una porción sustancial de la funcionalidad original del modelo y sus capacidades lingüísticas. Esta reducción en el tamaño del modelo disminuye la complejidad general, haciendo que los SLM sean más eficientes en términos de uso de memoria y requisitos computacionales. A pesar de estas optimizaciones, los SLM aún pueden realizar una amplia gama de tareas de procesamiento de lenguaje natural (NLP):

- Generación de Texto: Creación de oraciones o párrafos coherentes y contextualmente relevantes.
- Completación de Texto: Predicción y finalización de oraciones basadas en un estímulo dado.
- Traducción: Conversión de texto de un idioma a otro.
- Resumen: Condensación de textos largos en resúmenes más cortos y digeribles.

Aunque con algunos compromisos en el rendimiento o profundidad de comprensión en comparación con sus contrapartes más grandes.

## ¿Cómo Funcionan los Modelos de Lenguaje Pequeños?

Los SLM se entrenan con grandes cantidades de datos de texto. Durante el entrenamiento, aprenden los patrones y estructuras del lenguaje, lo que les permite generar texto que es tanto gramaticalmente correcto como contextualmente apropiado. El proceso de entrenamiento involucra:

- Recolección de Datos: Reunir grandes conjuntos de datos de texto de diversas fuentes.
- Preprocesamiento: Limpiar y organizar los datos para hacerlos adecuados para el entrenamiento.
- Entrenamiento: Utilizar algoritmos de aprendizaje automático para enseñar al modelo cómo entender y generar texto.
- Ajuste Fino: Ajustar el modelo para mejorar su rendimiento en tareas específicas.

El desarrollo de los SLM se alinea con la creciente necesidad de modelos que puedan ser desplegados en entornos con restricciones de recursos, como dispositivos móviles o plataformas de computación en el borde, donde los LLM a gran escala pueden ser poco prácticos debido a sus altas demandas de recursos. Al centrarse en la eficiencia, los SLM equilibran el rendimiento con la accesibilidad, permitiendo una aplicación más amplia en diversos dominios.

![slm](../../../translated_images/slm.png?WT.85221b66c3ce1b5e21e84c783c7ba31848501cd5c9557bb7fdf13173edafd675.es.mc_id=academic-105485-koreyst)

## Objetivos de Aprendizaje

En esta lección, esperamos introducir el conocimiento de los SLM y combinarlos con Microsoft Phi-3 para aprender diferentes escenarios en contenido de texto, visión y MoE. Al final de esta lección, deberías poder responder las siguientes preguntas:

- ¿Qué es un SLM?
- ¿Cuál es la diferencia entre SLM y LLM?
- ¿Qué es la Familia Microsoft Phi-3/3.5?
- ¿Cómo inferir la Familia Microsoft Phi-3/3.5?

¿Listo? Comencemos.

## Las Distinciones entre Modelos de Lenguaje Grandes (LLMs) y Modelos de Lenguaje Pequeños (SLMs)

Tanto los LLM como los SLM se construyen sobre principios fundamentales del aprendizaje automático probabilístico, siguiendo enfoques similares en su diseño arquitectónico, metodologías de entrenamiento, procesos de generación de datos y técnicas de evaluación de modelos. Sin embargo, varios factores clave diferencian estos dos tipos de modelos.

## Aplicaciones de los Modelos de Lenguaje Pequeños

Los SLM tienen una amplia gama de aplicaciones, incluyendo:

- Chatbots: Proporcionar soporte al cliente e interactuar con usuarios de manera conversacional.
- Creación de Contenido: Asistir a escritores generando ideas o incluso redactando artículos completos.
- Educación: Ayudar a estudiantes con tareas de escritura o en el aprendizaje de nuevos idiomas.
- Accesibilidad: Crear herramientas para individuos con discapacidades, como sistemas de texto a voz.

**Tamaño**

Una distinción principal entre LLM y SLM radica en la escala de los modelos. Los LLM, como ChatGPT (GPT-4), pueden comprender aproximadamente 1.76 billones de parámetros, mientras que los SLM de código abierto como Mistral 7B están diseñados con significativamente menos parámetros, aproximadamente 7 mil millones. Esta disparidad se debe principalmente a diferencias en la arquitectura del modelo y los procesos de entrenamiento. Por ejemplo, ChatGPT emplea un mecanismo de auto-atención dentro de un marco de codificador-decodificador, mientras que Mistral 7B utiliza atención de ventana deslizante, lo que permite un entrenamiento más eficiente dentro de un modelo solo de decodificador. Esta variación arquitectónica tiene implicaciones profundas para la complejidad y el rendimiento de estos modelos.

**Comprensión**

Los SLM están típicamente optimizados para el rendimiento dentro de dominios específicos, lo que los hace altamente especializados pero potencialmente limitados en su capacidad para proporcionar una comprensión contextual amplia en múltiples campos de conocimiento. En contraste, los LLM buscan simular la inteligencia similar a la humana a un nivel más integral. Entrenados en vastos y diversos conjuntos de datos, los LLM están diseñados para desempeñarse bien en una variedad de dominios, ofreciendo mayor versatilidad y adaptabilidad. En consecuencia, los LLM son más adecuados para una gama más amplia de tareas posteriores, como el procesamiento de lenguaje natural y la programación.

**Computación**

El entrenamiento y despliegue de los LLM son procesos intensivos en recursos, a menudo requiriendo una infraestructura computacional significativa, incluyendo grandes clústeres de GPU. Por ejemplo, entrenar un modelo como ChatGPT desde cero puede necesitar miles de GPUs durante períodos extendidos. En contraste, los SLM, con su menor cantidad de parámetros, son más accesibles en términos de recursos computacionales. Modelos como Mistral 7B pueden ser entrenados y ejecutados en máquinas locales equipadas con capacidades de GPU moderadas, aunque el entrenamiento aún demanda varias horas en múltiples GPUs.

**Sesgo**

El sesgo es un problema conocido en los LLM, principalmente debido a la naturaleza de los datos de entrenamiento. Estos modelos a menudo dependen de datos brutos, disponibles abiertamente en internet, que pueden subrepresentar o mal representar ciertos grupos, introducir etiquetado erróneo o reflejar sesgos lingüísticos influenciados por dialecto, variaciones geográficas y reglas gramaticales. Además, la complejidad de las arquitecturas de LLM puede inadvertidamente exacerbar el sesgo, lo que puede pasar desapercibido sin un ajuste fino cuidadoso. Por otro lado, los SLM, al ser entrenados en conjuntos de datos más restringidos y específicos de dominio, son inherentemente menos susceptibles a tales sesgos, aunque no son inmunes a ellos.

**Inferencia**

El tamaño reducido de los SLM les otorga una ventaja significativa en términos de velocidad de inferencia, permitiéndoles generar salidas de manera eficiente en hardware local sin la necesidad de procesamiento paralelo extenso. En contraste, los LLM, debido a su tamaño y complejidad, a menudo requieren recursos computacionales paralelos sustanciales para lograr tiempos de inferencia aceptables. La presencia de múltiples usuarios concurrentes ralentiza aún más los tiempos de respuesta de los LLM, especialmente cuando se despliegan a escala.

En resumen, aunque tanto los LLM como los SLM comparten una base fundamental en el aprendizaje automático, difieren significativamente en términos de tamaño del modelo, requisitos de recursos, comprensión contextual, susceptibilidad al sesgo y velocidad de inferencia. Estas distinciones reflejan su idoneidad respectiva para diferentes casos de uso, siendo los LLM más versátiles pero intensivos en recursos, y los SLM ofreciendo más eficiencia específica de dominio con demandas computacionales reducidas.

***Nota: En este capítulo, presentaremos SLM utilizando Microsoft Phi-3 / 3.5 como ejemplo.***

## Introducción a la Familia Phi-3 / Phi-3.5

La Familia Phi-3 / 3.5 se enfoca principalmente en escenarios de aplicación de texto, visión y Agente (MoE):

### Phi-3 / 3.5 Instruct

Principalmente para generación de texto, finalización de chat y extracción de información de contenido, etc.

**Phi-3-mini**

El modelo de lenguaje de 3.8B está disponible en Microsoft Azure AI Studio, Hugging Face y Ollama. Los modelos Phi-3 superan significativamente a los modelos de lenguaje de igual y mayor tamaño en puntos de referencia clave (ver números de referencia a continuación, números más altos son mejores). Phi-3-mini supera a modelos del doble de su tamaño, mientras que Phi-3-pequeño y Phi-3-mediano superan a modelos más grandes, incluyendo GPT-3.5

**Phi-3-pequeño y mediano**

Con solo 7B de parámetros, Phi-3-pequeño supera a GPT-3.5T en una variedad de puntos de referencia de lenguaje, razonamiento, codificación y matemáticas. El Phi-3-mediano con 14B de parámetros continúa esta tendencia y supera al Gemini 1.0 Pro.

**Phi-3.5-mini**

Podemos considerarlo como una actualización de Phi-3-mini. Mientras los parámetros permanecen sin cambios, mejora la capacidad de soportar múltiples idiomas (Soporta más de 20 idiomas: árabe, chino, checo, danés, holandés, inglés, finlandés, francés, alemán, hebreo, húngaro, italiano, japonés, coreano, noruego, polaco, portugués, ruso, español, sueco, tailandés, turco, ucraniano) y agrega un soporte más fuerte para contextos largos. Phi-3.5-mini con 3.8B de parámetros supera a los modelos de lenguaje del mismo tamaño y está a la par con modelos del doble de su tamaño.

### Phi-3 / 3.5 Visión

Podemos pensar en el modelo Instruct de Phi-3/3.5 como la capacidad de Phi para entender, y Visión es lo que le da a Phi ojos para entender el mundo.

**Phi-3-Vision**

Phi-3-vision, con solo 4.2B de parámetros, continúa esta tendencia y supera a modelos más grandes como Claude-3 Haiku y Gemini 1.0 Pro V en tareas generales de razonamiento visual, OCR y comprensión de tablas y diagramas.

**Phi-3.5-Vision**

Phi-3.5-Vision también es una actualización de Phi-3-Vision, agregando soporte para múltiples imágenes. Puedes pensar en ello como una mejora en la visión, no solo puede ver imágenes, sino también videos. Phi-3.5-vision supera a modelos más grandes como Claude-3.5 Sonnet y Gemini 1.5 Flash en tareas de OCR, comprensión de tablas y gráficos y está a la par en tareas generales de razonamiento de conocimiento visual. Soporta entrada de múltiples cuadros, es decir, realiza razonamiento en múltiples imágenes de entrada.

### Phi-3.5-MoE

***Mezcla de Expertos (MoE)*** permite que los modelos sean preentrenados con mucho menos cómputo, lo que significa que puedes escalar dramáticamente el tamaño del modelo o conjunto de datos con el mismo presupuesto de cómputo que un modelo denso. En particular, un modelo MoE debería lograr la misma calidad que su contraparte densa mucho más rápido durante el preentrenamiento. Phi-3.5-MoE comprende 16x3.8B módulos de expertos. Phi-3.5-MoE con solo 6.6B de parámetros activos logra un nivel similar de razonamiento, comprensión del lenguaje y matemáticas como modelos mucho más grandes.

Podemos usar el modelo de la Familia Phi-3/3.5 basado en diferentes escenarios. A diferencia de LLM, puedes desplegar Phi-3/3.5-mini o Phi-3/3.5-Vision en dispositivos de borde.

## Cómo usar los modelos de la Familia Phi-3/3.5

Esperamos usar Phi-3/3.5 en diferentes escenarios. A continuación, usaremos Phi-3/3.5 basado en diferentes escenarios.

![phi3](../../../translated_images/phi3.png?WT.0d1077c4470f7b6eef536aba4426fa8df26762844164cc3883d455ab5251bad1.es.mc_id=academic-105485-koreyst)

### Diferencia de inferencia

API de la Nube

**Modelos de GitHub**

Modelos de GitHub
```


**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.