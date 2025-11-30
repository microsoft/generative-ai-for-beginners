<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b9d32511b27373a1b21b5789d4fda057",
  "translation_date": "2025-10-17T22:49:49+00:00",
  "source_file": "14-the-generative-ai-application-lifecycle/README.md",
  "language_code": "es"
}
-->
[![Integración con llamadas a funciones](../../../translated_images/14-lesson-banner.066d74a31727ac121eeac06376a068a397d8e335281e63ce94130d11f516e46b.es.png)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# El Ciclo de Vida de las Aplicaciones de IA Generativa

Una pregunta importante para todas las aplicaciones de IA es la relevancia de las características de la IA, ya que es un campo que evoluciona rápidamente. Para garantizar que tu aplicación siga siendo relevante, confiable y robusta, necesitas monitorearla, evaluarla y mejorarla continuamente. Aquí es donde entra en juego el ciclo de vida de la IA generativa.

El ciclo de vida de la IA generativa es un marco que te guía a través de las etapas de desarrollo, implementación y mantenimiento de una aplicación de IA generativa. Te ayuda a definir tus objetivos, medir tu rendimiento, identificar tus desafíos e implementar tus soluciones. También te ayuda a alinear tu aplicación con los estándares éticos y legales de tu dominio y tus partes interesadas. Al seguir el ciclo de vida de la IA generativa, puedes asegurarte de que tu aplicación siempre esté entregando valor y satisfaciendo a tus usuarios.

## Introducción

En este capítulo, aprenderás:

- Comprender el cambio de paradigma de MLOps a LLMOps
- El ciclo de vida de LLM
- Herramientas para el ciclo de vida
- Métricas y evaluación del ciclo de vida

## Comprender el cambio de paradigma de MLOps a LLMOps

Los LLMs son una nueva herramienta en el arsenal de la Inteligencia Artificial, increíblemente poderosos en tareas de análisis y generación para aplicaciones. Sin embargo, este poder tiene algunas consecuencias en cómo optimizamos las tareas de IA y aprendizaje automático clásico.

Por ello, necesitamos un nuevo paradigma para adaptar esta herramienta de manera dinámica, con los incentivos correctos. Podemos categorizar las aplicaciones de IA más antiguas como "Aplicaciones de ML" y las aplicaciones de IA más nuevas como "Aplicaciones de IA Generativa" o simplemente "Aplicaciones de IA", reflejando la tecnología y técnicas predominantes en ese momento. Esto cambia nuestra narrativa de varias maneras. Observa la siguiente comparación.

![Comparación entre LLMOps y MLOps](../../../translated_images/01-llmops-shift.29bc933cb3bb0080a562e1655c0c719b71a72c3be6252d5c564b7f598987e602.es.png)

Nota que en LLMOps nos enfocamos más en los desarrolladores de aplicaciones, utilizando integraciones como un punto clave, empleando "Modelos como Servicio" y considerando los siguientes puntos para las métricas:

- Calidad: Calidad de la respuesta
- Daño: IA responsable
- Honestidad: Fundamentación de la respuesta (¿Tiene sentido? ¿Es correcta?)
- Costo: Presupuesto de la solución
- Latencia: Tiempo promedio de respuesta por token

## El ciclo de vida de LLM

Primero, para entender el ciclo de vida y las modificaciones, observemos la siguiente infografía.

![Infografía de LLMOps](../../../translated_images/02-llmops.70a942ead05a7645db740f68727d90160cb438ab71f0fb20548bc7fe5cad83ff.es.png)

Como puedes notar, esto es diferente de los ciclos de vida habituales de MLOps. Los LLMs tienen muchos requisitos nuevos, como el diseño de prompts, diferentes técnicas para mejorar la calidad (Fine-Tuning, RAG, Meta-Prompts), evaluaciones distintas y responsabilidad con IA responsable, y finalmente, nuevas métricas de evaluación (Calidad, Daño, Honestidad, Costo y Latencia).

Por ejemplo, observa cómo ideamos. Usamos ingeniería de prompts para experimentar con varios LLMs y explorar posibilidades para probar si sus hipótesis podrían ser correctas.

Nota que esto no es lineal, sino bucles integrados, iterativos y con un ciclo general.

¿Cómo podríamos explorar esos pasos? Veamos en detalle cómo construir un ciclo de vida.

![Flujo de etapas de LLMOps](../../../translated_images/03-llm-stage-flows.3a1e1c401235a6cfa886ed6ba04aa52a096a545e1bc44fa54d7d5983a7201892.es.png)

Esto puede parecer un poco complicado, enfoquémonos primero en los tres grandes pasos.

1. Idear/Explorar: Exploración, aquí podemos explorar según nuestras necesidades empresariales. Prototipar, crear un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) y probar si es lo suficientemente eficiente para nuestra hipótesis.
1. Construir/Aumentar: Implementación, ahora comenzamos a evaluar con conjuntos de datos más grandes, implementamos técnicas como Fine-Tuning y RAG para verificar la robustez de nuestra solución. Si no funciona, reimplementarlo, agregar nuevos pasos en nuestro flujo o reestructurar los datos podría ayudar. Después de probar nuestro flujo y nuestra escala, si funciona y cumple con nuestras métricas, está listo para el siguiente paso.
1. Operacionalizar: Integración, ahora agregamos sistemas de monitoreo y alertas a nuestro sistema, implementación e integración de la aplicación en nuestra aplicación.

Luego, tenemos el ciclo general de Gestión, enfocado en seguridad, cumplimiento y gobernanza.

¡Felicidades! Ahora tienes tu aplicación de IA lista para funcionar y operativa. Para una experiencia práctica, echa un vistazo al [Demo de Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Ahora, ¿qué herramientas podríamos usar?

## Herramientas para el ciclo de vida

Para herramientas, Microsoft proporciona la [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) y [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) para facilitar y hacer que tu ciclo sea fácil de implementar y listo para usar.

La [Plataforma Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) te permite usar [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio es un portal web que te permite explorar modelos, ejemplos y herramientas. Gestionar tus recursos, flujos de desarrollo de interfaz de usuario y opciones de SDK/CLI para desarrollo orientado a código.

![Posibilidades de Azure AI](../../../translated_images/04-azure-ai-platform.80203baf03a12fa8b166e194928f057074843d1955177baf0f5b53d50d7b6153.es.png)

Azure AI te permite usar múltiples recursos para gestionar tus operaciones, servicios, proyectos, búsqueda vectorial y necesidades de bases de datos.

![LLMOps con Azure AI](../../../translated_images/05-llm-azure-ai-prompt.a5ce85cdbb494bdf95420668e3464aae70d8b22275a744254e941dd5e73ae0d2.es.png)

Construye desde pruebas de concepto (POC) hasta aplicaciones a gran escala con PromptFlow:

- Diseña y construye aplicaciones desde VS Code, con herramientas visuales y funcionales.
- Prueba y ajusta tus aplicaciones para obtener una IA de calidad, con facilidad.
- Usa Azure AI Studio para integrar e iterar con la nube, realizar implementaciones rápidas y despliegues.

![LLMOps con PromptFlow](../../../translated_images/06-llm-promptflow.a183eba07a3a7fdf4aa74db92a318b8cbbf4a608671f6b166216358d3203d8d4.es.png)

## ¡Genial! Continúa aprendiendo

Increíble, ahora aprende más sobre cómo estructuramos una aplicación para usar los conceptos con la [Aplicación Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), para ver cómo Cloud Advocacy incorpora esos conceptos en demostraciones. Para más contenido, revisa nuestra [sesión destacada de Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ahora, revisa la Lección 15 para entender cómo [Retrieval Augmented Generation y Bases de Datos Vectoriales](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactan la IA generativa y cómo crear aplicaciones más atractivas.

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.