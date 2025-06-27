<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "68664f7e754a892ae1d8d5e2b7bd2081",
  "translation_date": "2025-06-26T00:29:40+00:00",
  "source_file": "18-fine-tuning/README.md",
  "language_code": "es"
}
-->
[![Modelos de Código Abierto](../../../translated_images/18-lesson-banner.f30176815b1a5074fce9cceba317720586caa99e24001231a92fd04eeb54a121.es.png)](https://aka.ms/gen-ai-lesson18-gh?WT.mc_id=academic-105485-koreyst)

# Ajuste Fino de Tu LLM

Usar modelos de lenguaje grande para construir aplicaciones de IA generativa presenta nuevos desafíos. Un problema clave es asegurar la calidad de las respuestas (precisión y relevancia) en el contenido generado por el modelo para una solicitud de usuario dada. En lecciones anteriores, discutimos técnicas como la ingeniería de prompts y la generación aumentada por recuperación que intentan resolver el problema _modificando la entrada del prompt_ al modelo existente.

En la lección de hoy, discutimos una tercera técnica, **ajuste fino**, que intenta abordar el desafío _reentrenando el modelo en sí_ con datos adicionales. Vamos a profundizar en los detalles.

## Objetivos de Aprendizaje

Esta lección introduce el concepto de ajuste fino para modelos de lenguaje preentrenados, explora los beneficios y desafíos de este enfoque, y ofrece orientación sobre cuándo y cómo usar el ajuste fino para mejorar el rendimiento de tus modelos de IA generativa.

Al final de esta lección, deberías poder responder las siguientes preguntas:

- ¿Qué es el ajuste fino para modelos de lenguaje?
- ¿Cuándo y por qué es útil el ajuste fino?
- ¿Cómo puedo ajustar fino un modelo preentrenado?
- ¿Cuáles son las limitaciones del ajuste fino?

¿Listo? Comencemos.

## Guía Ilustrada

¿Quieres obtener una visión general de lo que cubriremos antes de profundizar? Revisa esta guía ilustrada que describe el viaje de aprendizaje para esta lección: desde aprender los conceptos básicos y la motivación para el ajuste fino, hasta entender el proceso y las mejores prácticas para ejecutar la tarea de ajuste fino. Este es un tema fascinante para explorar, así que no olvides consultar la página de [Recursos](./RESOURCES.md?WT.mc_id=academic-105485-koreyst) para obtener enlaces adicionales que apoyen tu viaje de aprendizaje autodirigido.

![Guía Ilustrada para el Ajuste Fino de Modelos de Lenguaje](../../../translated_images/18-fine-tuning-sketchnote.11b21f9ec8a703467a120cb79a28b5ac1effc8d8d9d5b31bbbac6b8640432e14.es.png)

## ¿Qué es el ajuste fino para modelos de lenguaje?

Por definición, los modelos de lenguaje grande están _preentrenados_ en grandes cantidades de texto obtenido de diversas fuentes, incluyendo internet. Como hemos aprendido en lecciones anteriores, necesitamos técnicas como la _ingeniería de prompts_ y la _generación aumentada por recuperación_ para mejorar la calidad de las respuestas del modelo a las preguntas del usuario ("prompts").

Una técnica popular de ingeniería de prompts implica dar al modelo más orientación sobre lo que se espera en la respuesta, ya sea proporcionando _instrucciones_ (orientación explícita) o _dándole algunos ejemplos_ (orientación implícita). Esto se conoce como _aprendizaje de pocos disparos_ pero tiene dos limitaciones:

- Los límites de tokens del modelo pueden restringir el número de ejemplos que puedes dar y limitar la efectividad.
- Los costos de tokens del modelo pueden hacer costoso agregar ejemplos a cada prompt y limitar la flexibilidad.

El ajuste fino es una práctica común en sistemas de aprendizaje automático donde tomamos un modelo preentrenado y lo reentrenamos con nuevos datos para mejorar su rendimiento en una tarea específica. En el contexto de los modelos de lenguaje, podemos ajustar fino el modelo preentrenado _con un conjunto curado de ejemplos para una tarea o dominio de aplicación dado_ para crear un **modelo personalizado** que pueda ser más preciso y relevante para esa tarea o dominio específico. Un beneficio adicional del ajuste fino es que también puede reducir el número de ejemplos necesarios para el aprendizaje de pocos disparos, reduciendo el uso de tokens y los costos relacionados.

## ¿Cuándo y por qué deberíamos ajustar fino los modelos?

En _este_ contexto, cuando hablamos de ajuste fino, nos referimos a un ajuste fino **supervisado** donde el reentrenamiento se realiza **agregando nuevos datos** que no formaban parte del conjunto de datos de entrenamiento original. Esto es diferente de un enfoque de ajuste fino no supervisado donde el modelo se reentrena en los datos originales, pero con diferentes hiperparámetros.

Lo clave a recordar es que el ajuste fino es una técnica avanzada que requiere un cierto nivel de experiencia para obtener los resultados deseados. Si se hace incorrectamente, puede que no proporcione las mejoras esperadas e incluso puede degradar el rendimiento del modelo para tu dominio objetivo.

Por lo tanto, antes de aprender "cómo" ajustar fino los modelos de lenguaje, necesitas saber "por qué" deberías tomar este camino y "cuándo" comenzar el proceso de ajuste fino. Comienza haciéndote estas preguntas:

- **Caso de Uso**: ¿Cuál es tu _caso de uso_ para el ajuste fino? ¿Qué aspecto del modelo preentrenado actual quieres mejorar?
- **Alternativas**: ¿Has probado _otras técnicas_ para lograr los resultados deseados? Úsalas para crear una línea base para la comparación.
  - Ingeniería de prompts: Prueba técnicas como el prompting de pocos disparos con ejemplos de respuestas de prompts relevantes. Evalúa la calidad de las respuestas.
  - Generación Aumentada por Recuperación: Prueba aumentar los prompts con resultados de consultas recuperados al buscar en tus datos. Evalúa la calidad de las respuestas.
- **Costos**: ¿Has identificado los costos del ajuste fino?
  - Ajustabilidad: ¿está disponible el modelo preentrenado para el ajuste fino?
  - Esfuerzo: para preparar los datos de entrenamiento, evaluar y refinar el modelo.
  - Computación: para ejecutar trabajos de ajuste fino y desplegar el modelo ajustado fino.
  - Datos: acceso a suficientes ejemplos de calidad para el impacto del ajuste fino.
- **Beneficios**: ¿Has confirmado los beneficios del ajuste fino?
  - Calidad: ¿el modelo ajustado fino superó la línea base?
  - Costo: ¿reduce el uso de tokens simplificando los prompts?
  - Extensibilidad: ¿puedes reutilizar el modelo base para nuevos dominios?

Al responder estas preguntas, deberías poder decidir si el ajuste fino es el enfoque correcto para tu caso de uso. Idealmente, el enfoque es válido solo si los beneficios superan los costos. Una vez que decides proceder, es momento de pensar en _cómo_ puedes ajustar fino el modelo preentrenado.

¿Quieres obtener más información sobre el proceso de toma de decisiones? Mira [Ajustar fino o no ajustar fino](https://www.youtube.com/watch?v=0Jo-z-MFxJs)

## ¿Cómo podemos ajustar fino un modelo preentrenado?

Para ajustar fino un modelo preentrenado, necesitas tener:

- un modelo preentrenado para ajustar fino
- un conjunto de datos para usar en el ajuste fino
- un entorno de entrenamiento para ejecutar el trabajo de ajuste fino
- un entorno de alojamiento para desplegar el modelo ajustado fino

## Ajuste Fino en Acción

Los siguientes recursos proporcionan tutoriales paso a paso para guiarte a través de un ejemplo real utilizando un modelo seleccionado con un conjunto de datos curado. Para trabajar en estos tutoriales, necesitas una cuenta en el proveedor específico, junto con acceso al modelo y conjuntos de datos relevantes.

| Proveedor    | Tutorial                                                                                                                                                                       | Descripción                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OpenAI       | [Cómo ajustar fino modelos de chat](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_finetune_chat_models.ipynb?WT.mc_id=academic-105485-koreyst)            | Aprende a ajustar fino un `gpt-35-turbo` para un dominio específico ("asistente de recetas") preparando datos de entrenamiento, ejecutando el trabajo de ajuste fino y utilizando el modelo ajustado fino para inferencia.                                                                                                                                                                                                                                              |
| Azure OpenAI | [Tutorial de ajuste fino de GPT 3.5 Turbo](https://learn.microsoft.com/azure/ai-services/openai/tutorials/fine-tune?tabs=python-new%2Ccommand-line?WT.mc_id=academic-105485-koreyst) | Aprende a ajustar fino un modelo `gpt-35-turbo-0613` **en Azure** tomando pasos para crear y subir datos de entrenamiento, ejecutar el trabajo de ajuste fino. Desplegar y usar el nuevo modelo.                                                                                                                                                                                                                                                                             |
| Hugging Face | [Ajuste fino de LLMs con Hugging Face](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl?WT.mc_id=academic-105485-koreyst)                                             | Esta publicación de blog te guía en el ajuste fino de un _LLM abierto_ (ej: `CodeLlama 7B`) usando la biblioteca [transformers](https://huggingface.co/docs/transformers/index?WT.mc_id=academic-105485-koreyst) y [Transformer Reinforcement Learning (TRL)](https://huggingface.co/docs/trl/index?WT.mc_id=academic-105485-koreyst]) con [conjuntos de datos abiertos](https://huggingface.co/docs/datasets/index?WT.mc_id=academic-105485-koreyst) en Hugging Face. |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 🤗 AutoTrain | [Ajuste fino de LLMs con AutoTrain](https://github.com/huggingface/autotrain-advanced/?WT.mc_id=academic-105485-koreyst)                                                       | AutoTrain (o AutoTrain Advanced) es una biblioteca de Python desarrollada por Hugging Face que permite el ajuste fino para muchas tareas diferentes, incluido el ajuste fino de LLM. AutoTrain es una solución sin código y el ajuste fino se puede hacer en tu propia nube, en Hugging Face Spaces o localmente. Soporta tanto una GUI basada en web, CLI y entrenamiento a través de archivos de configuración yaml.                       |
|              |                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Tarea

Selecciona uno de los tutoriales anteriores y recórrelos. _Podríamos replicar una versión de estos tutoriales en Jupyter Notebooks en este repositorio solo para referencia. Por favor, utiliza las fuentes originales directamente para obtener las versiones más recientes_.

## ¡Buen Trabajo! Continúa Tu Aprendizaje.

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tu conocimiento de IA generativa.

¡Felicitaciones! Has completado la lección final de la serie v2 de este curso. No dejes de aprender y construir. \*\*Consulta la página de [RECURSOS](RESOURCES.md?WT.mc_id=academic-105485-koreyst) para obtener una lista de sugerencias adicionales solo para este tema.

Nuestra serie de lecciones v1 también ha sido actualizada con más tareas y conceptos. Así que tómate un minuto para refrescar tu conocimiento, y por favor [comparte tus preguntas y comentarios](https://github.com/microsoft/generative-ai-for-beginners/issues?WT.mc_id=academic-105485-koreyst) para ayudarnos a mejorar estas lecciones para la comunidad.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.