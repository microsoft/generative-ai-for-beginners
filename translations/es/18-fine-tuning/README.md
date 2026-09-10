[![Modelos de Código Abierto](../../../translated_images/es/18-lesson-banner.f30176815b1a5074.webp)](https://youtu.be/6UAwhL9Q-TQ?si=5jJd8yeQsCfJ97em)

# Ajuste Fino de Tu LLM

Usar modelos de lenguaje grandes para construir aplicaciones generativas de IA conlleva nuevos desafíos. Un tema clave es asegurar la calidad de la respuesta (precisión y relevancia) en el contenido generado por el modelo para una solicitud dada del usuario. En lecciones anteriores, discutimos técnicas como la ingeniería de indicaciones y la generación aumentada por recuperación que intentan resolver el problema _modificando la entrada de la indicación_ al modelo existente.

En la lección de hoy, discutimos una tercera técnica, el **ajuste fino**, que intenta abordar el desafío _reentrenando el propio modelo_ con datos adicionales. Vamos a profundizar en los detalles.

## Objetivos de Aprendizaje

Esta lección introduce el concepto de ajuste fino para modelos de lenguaje preentrenados, explora los beneficios y desafíos de este enfoque, y proporciona orientación sobre cuándo y cómo usar el ajuste fino para mejorar el rendimiento de tus modelos generativos de IA.

Al final de esta lección, deberías poder responder las siguientes preguntas:

- ¿Qué es el ajuste fino para modelos de lenguaje?
- ¿Cuándo y por qué es útil el ajuste fino?
- ¿Cómo puedo ajustar finamente un modelo preentrenado?
- ¿Cuáles son las limitaciones del ajuste fino?

¿Listo? Comencemos.

## Guía Ilustrada

¿Quieres tener una visión general de lo que cubriremos antes de profundizar? Revisa esta guía ilustrada que describe el recorrido de aprendizaje para esta lección, desde aprender los conceptos centrales y la motivación para el ajuste fino, hasta entender el proceso y las mejores prácticas para ejecutar la tarea de ajuste fino. Este es un tema fascinante para explorar, ¡así que no olvides visitar la página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para enlaces adicionales que apoyen tu aprendizaje autodirigido!

![Guía Ilustrada para el Ajuste Fino de Modelos de Lenguaje](../../../translated_images/es/18-fine-tuning-sketchnote.11b21f9ec8a70346.webp)

## ¿Qué es el ajuste fino para modelos de lenguaje?

Por definición, los grandes modelos de lenguaje están _preentrenados_ en grandes cantidades de texto provenientes de diversas fuentes, incluyendo internet. Como hemos aprendido en lecciones anteriores, necesitamos técnicas como la _ingeniería de indicaciones_ y la _generación aumentada por recuperación_ para mejorar la calidad de las respuestas del modelo a las preguntas del usuario ("indicaciones").

Una técnica popular de ingeniería de indicaciones implica darle al modelo más orientación sobre lo que se espera en la respuesta, ya sea proporcionando _instrucciones_ (orientación explícita) o _dándole algunos ejemplos_ (orientación implícita). Esto se conoce como _aprendizaje con pocos ejemplos_ pero tiene dos limitaciones:

- Los límites de tokens del modelo pueden restringir la cantidad de ejemplos que puedes proporcionar y limitar la efectividad.
- El costo de los tokens del modelo puede hacer que agregar ejemplos a cada indicación sea caro y limitar la flexibilidad.

El ajuste fino es una práctica común en sistemas de aprendizaje automático donde tomamos un modelo preentrenado y lo reentrenamos con nuevos datos para mejorar su rendimiento en una tarea específica. En el contexto de los modelos de lenguaje, podemos ajustar finamente el modelo preentrenado _con un conjunto curado de ejemplos para una tarea o dominio de aplicación dado_ para crear un **modelo personalizado** que puede ser más preciso y relevante para esa tarea o dominio específico. Un beneficio adicional del ajuste fino es que también puede reducir el número de ejemplos necesarios para el aprendizaje con pocos ejemplos, disminuyendo el uso de tokens y los costos relacionados.

## ¿Cuándo y por qué deberíamos ajustar finamente los modelos?

En _este_ contexto, cuando hablamos de ajuste fino, nos referimos al ajuste fino **supervisado** donde el reentrenamiento se realiza **añadiendo nuevos datos** que no formaban parte del conjunto de datos de entrenamiento original. Esto es diferente de un enfoque de ajuste fino no supervisado donde el modelo se reentrena con los datos originales, pero con hiperparámetros diferentes.

Lo importante es recordar que el ajuste fino es una técnica avanzada que requiere cierto nivel de experiencia para obtener los resultados deseados. Si se hace incorrectamente, puede no proporcionar las mejoras esperadas e incluso puede degradar el rendimiento del modelo para tu dominio objetivo.

Por lo tanto, antes de aprender "cómo" ajustar finamente modelos de lenguaje, necesitas saber "por qué" deberías tomar esta ruta y "cuándo" comenzar el proceso de ajuste fino. Comienza haciéndote estas preguntas:

- **Caso de uso**: ¿Cuál es tu _caso de uso_ para el ajuste fino? ¿Qué aspecto del modelo preentrenado actual quieres mejorar?
- **Alternativas**: ¿Has probado _otras técnicas_ para lograr los resultados deseados? Úsalas para crear una línea base para comparación.
  - Ingeniería de indicaciones: Prueba técnicas como indicaciones con pocos ejemplos con respuestas relevantes. Evalúa la calidad de las respuestas.
  - Generación Aumentada por Recuperación: Prueba aumentar las indicaciones con resultados de consultas recuperadas buscando en tus datos. Evalúa la calidad de las respuestas.
- **Costos**: ¿Has identificado los costos del ajuste fino?
  - Ajustabilidad - ¿está disponible el modelo preentrenado para ajuste fino?
  - Esfuerzo - para preparar datos de entrenamiento, evaluar y refinar el modelo.
  - Computación - para ejecutar trabajos de ajuste fino y desplegar el modelo ajustado.
  - Datos - acceso a ejemplos de calidad suficiente para impacto del ajuste fino.
- **Beneficios**: ¿Has confirmado los beneficios del ajuste fino?
  - Calidad - ¿superó el modelo ajustado finamente la línea base?
  - Costo - ¿reduce el uso de tokens simplificando las indicaciones?
  - Extensibilidad - ¿puedes reutilizar el modelo base para nuevos dominios?

Al responder estas preguntas, deberías poder decidir si el ajuste fino es el enfoque adecuado para tu caso de uso. Idealmente, el enfoque es válido solo si los beneficios superan los costos. Una vez que decidas continuar, es momento de pensar en _cómo_ puedes ajustar finamente el modelo preentrenado.

¿Quieres obtener más información sobre el proceso de toma de decisiones? Mira [Ajustar fino o no ajustar fino](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## ¿Cómo podemos ajustar finamente un modelo preentrenado?

Para ajustar finamente un modelo preentrenado, necesitas tener:

- un modelo preentrenado para ajustar
- un conjunto de datos para usar en el ajuste fino
- un entorno de entrenamiento para ejecutar el trabajo de ajuste fino
- un entorno de alojamiento para desplegar el modelo ajustado

## Ajuste Fino en Microsoft Foundry

[Microsoft Foundry](https://ai.azure.com?WT.mc_id=academic-105485-koreyst) es donde ajustas, despliegas y gestionas modelos personalizados en Azure hoy en día (reúne lo que antes era Azure OpenAI Studio y Azure AI Studio). Antes de iniciar un trabajo, es útil entender las opciones que Foundry te ofrece y las mejores prácticas que recomienda la plataforma. Internamente, Foundry usa **LoRA (adaptación de baja clasificación)** para ajustar los modelos de manera eficiente, lo que mantiene el entrenamiento más rápido y económico que reentrenar cada peso.

### Paso 1: Elige una técnica de entrenamiento

Foundry soporta tres técnicas de ajuste fino. **Comienza con SFT** - cubre el rango más amplio de escenarios.

| Técnica | Qué hace | Cuándo usarla |
| --- | --- | --- |
| **Ajuste fino supervisado (SFT)** | Entrena con pares de ejemplos entrada/salida para que el modelo aprenda a producir las respuestas que deseas. | Es el predeterminado para la mayoría de tareas: especialización de dominio, rendimiento en tareas, estilo y tono, seguimiento de instrucciones y adaptación lingüística. |
| **Optimización Directa de Preferencias (DPO)** | Aprende de pares de respuestas _preferidas vs. no preferidas_ para alinear salidas con preferencias humanas. | Para mejorar la calidad de las respuestas, seguridad y alineación cuando tienes retroalimentación comparativa. |
| **Ajuste fino por refuerzo (RFT)** | Usa señales de recompensa de _evaluadores_ para optimizar comportamientos complejos con aprendizaje por refuerzo. | Para dominios objetivos que requieren razonamiento intenso (matemáticas, química, física) con respuestas claramente correctas o incorrectas. Requiere mayor experiencia en ML. |

### Paso 2: Elige un nivel de entrenamiento

Foundry te permite elegir cómo y dónde se ejecuta el entrenamiento:

- **Estándar** - entrena en la región de tus recursos y garantiza residencia de datos. Úsalo cuando los datos deban permanecer en una región específica.
- **Global** - más económico y rápido al usar capacidad fuera de tu región (los datos y pesos se copian a la región de entrenamiento). Un buen valor predeterminado cuando la residencia de datos no es un requisito.
- **Desarrollador** - el costo más bajo, usando capacidad ociosa sin garantías de latencia/SLA (los trabajos pueden ser preemptados y reanudados). Ideal para experimentación.

### Paso 3: Elige un modelo base

Los modelos ajustables incluyen OpenAI `gpt-4o-mini`, `gpt-4o`, `gpt-4.1`, `gpt-4.1-mini` y `gpt-4.1-nano` (SFT; la familia 4o/4.1 también soporta DPO), los modelos de razonamiento `o4-mini` y `gpt-5` (RFT), además de modelos de código abierto como `Ministral-3B`, `Qwen-32B`, `Llama-3.3-70B-Instruct` y `gpt-oss-20b` (SFT en recursos Foundry). Siempre revisa la [lista actual de modelos para ajuste fino](https://learn.microsoft.com/azure/ai-foundry/foundry-models/concepts/models-sold-directly-by-azure?WT.mc_id=academic-105485-koreyst#fine-tuning-models) para métodos, regiones y disponibilidad soportados.

> Foundry ofrece dos modalidades: **serverless** (precios basados en consumo, sin cuota de GPU que gestionar, OpenAI y modelos seleccionados) y **cómputo gestionado** (trae tus propias VM a través de Azure Machine Learning para la gama más amplia de modelos). La mayoría debería comenzar con serverless.

### Mejores prácticas en Foundry

- **Primero la línea base.** Mide el modelo base con ingeniería de indicaciones y RAG _antes_ de ajustar fino, para poder demostrar la ganancia.
- **Comienza pequeño, luego escala.** Empieza con 50-100 ejemplos de alta calidad para validar el enfoque, luego crece a 500+ para producción. La calidad supera a la cantidad - elimina ejemplos de baja calidad.
- **Formato correcto de datos.** Los archivos de entrenamiento y validación deben ser JSONL, UTF-8 **con BOM**, menos de 512 MB, usando el formato de mensaje de chat completions. Siempre incluye un archivo de validación para vigilar el sobreajuste.
- **Mantén el prompt del sistema en la inferencia.** Usa el mismo mensaje del sistema cuando llames al modelo que usaste durante el entrenamiento.
- **Evalúa puntos de control - no despliegues ciegamente el último.** Foundry conserva las últimas tres épocas como puntos de control desplegables; elige el que generalice mejor observando `train_loss` / `valid_loss` y la precisión de tokens.
- **Mide el costo de tokens junto con la calidad** al comparar el modelo ajustado con la línea base.
- **Itera con ajuste fino continuo.** Puedes ajustar un modelo ya ajustado con nuevos datos (soportado para modelos OpenAI).
- **Cuida los costos de alojamiento.** Un modelo personalizado desplegado factura por hora y un despliegue inactivo se elimina después de 15 días: limpia lo que no necesites.

Sigue el recorrido completo en [Personalizar un modelo con ajuste fino](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning?WT.mc_id=academic-105485-koreyst), y consulta las guías para [DPO](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/fine-tuning-direct-preference-optimization?WT.mc_id=academic-105485-koreyst) y [RFT](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/reinforcement-fine-tuning?WT.mc_id=academic-105485-koreyst) cuando estés listo para las otras técnicas.

## Ajuste fino en acción

Los siguientes recursos proporcionan tutoriales paso a paso que te guían a través de un ejemplo real en un modelo actualmente soportado con un conjunto de datos curado. Para trabajar con ellos, necesitas una cuenta en el proveedor específico, junto con acceso al modelo y conjuntos de datos relevantes.

| Proveedor     | Tutorial                                                                                                                                                                       | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cómo ajustar modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)                | Aprende a ajustar finamente un modelo reciente de chat OpenAI para un dominio específico ("asistente de recetas") preparando datos de entrenamiento, ejecutando el trabajo de ajuste fino y usando el modelo ajustado para inferencia.                                                                                                                                                                                                                                              |
| Microsoft Foundry | [Personaliza un modelo con ajuste fino](https://learn.microsoft.com/azure/ai-foundry/openai/tutorials/fine-tune?WT.mc_id=academic-105485-koreyst) | Aprende a ajustar finamente un modelo actualmente soportado como `gpt-4.1-mini` **en Azure** con Microsoft Foundry: prepara y sube datos de entrenamiento y validación, ejecuta el trabajo de ajuste fino, luego despliega y usa el nuevo modelo.                                                                                                                                                                                                                                                                 |

| Hugging Face | [Entrenamiento fino de LLMs con Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                               | Esta publicación del blog te guía en el entrenamiento fino de un _LLM abierto_ (ej: `CodeLlama 7B`) usando la librería [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) y [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst) con [datasets](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) abiertos en Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Entrenamiento fino de LLMs con AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                         | AutoTrain (o AutoTrain Advanced) es una biblioteca de Python desarrollada por Hugging Face que permite el entrenamiento fino para muchas tareas diferentes, incluyendo el entrenamiento fino de LLM. AutoTrain es una solución sin código y el entrenamiento fino se puede hacer en tu propia nube, en Hugging Face Spaces o localmente. Soporta tanto una interfaz gráfica web, CLI y entrenamiento mediante archivos de configuración YAML.                                                                               |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🦥 Unsloth | [Entrenamiento fino de LLMs con Unsloth](https://github.com/unslothai/unsloth?WT.mc_id=academic-105485-koreyst)                                                         | Unsloth es un marco de trabajo de código abierto que soporta el entrenamiento fino de LLM y aprendizaje por refuerzo (RL). Unsloth simplifica el entrenamiento local, la evaluación y el despliegue con [notebooks](https://github.com/unslothai/notebooks?WT.mc_id=academic-105485-koreyst) listos para usar. También soporta texto a voz (TTS), modelos BERT y multimodales. Para empezar, lee su guía paso a paso [Fine-tuning LLMs Guide](https://docs.unsloth.ai/get-started/fine-tuning-llms-guide).                                                                          |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
## Tarea

Selecciona uno de los tutoriales anteriores y repásalos. _Podríamos replicar una versión de estos tutoriales en Jupyter Notebooks en este repositorio solo para referencia. Por favor, usa las fuentes originales directamente para obtener las versiones más recientes_.

## ¡Excelente trabajo! Continúa tu aprendizaje.

Después de completar esta lección, consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir aumentando tu conocimiento en IA Generativa.

¡¡Felicidades!! Has completado la lección final de la serie v2 de este curso. No dejes de aprender y construir. \*\*Consulta la página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para una lista de sugerencias adicionales sobre este tema.

Nuestra serie de lecciones v1 también ha sido actualizada con más tareas y conceptos. Así que tómate un minuto para refrescar tus conocimientos - y por favor [comparte tus preguntas y comentarios](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para ayudarnos a mejorar estas lecciones para la comunidad.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->