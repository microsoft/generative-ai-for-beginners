[![Integrating with function calling](../../../translated_images/14-lesson-banner.png?WT.833a8de2ff3806528caaf839db4385f00ff7c9f92ccdd38d886f4d662fc72f2a.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson14-gh?WT.mc_id=academic-105485-koreyst)

# El Ciclo de Vida de las Aplicaciones de IA Generativa

Una pregunta importante para todas las aplicaciones de IA es la relevancia de las características de IA, ya que es un campo que evoluciona rápidamente. Para asegurarte de que tu aplicación siga siendo relevante, confiable y robusta, necesitas monitorearla, evaluarla y mejorarla continuamente. Aquí es donde entra en juego el ciclo de vida de la IA generativa.

El ciclo de vida de la IA generativa es un marco que te guía a través de las etapas de desarrollo, implementación y mantenimiento de una aplicación de IA generativa. Te ayuda a definir tus objetivos, medir tu rendimiento, identificar tus desafíos e implementar tus soluciones. También te ayuda a alinear tu aplicación con los estándares éticos y legales de tu dominio y de tus partes interesadas. Siguiendo el ciclo de vida de la IA generativa, puedes asegurarte de que tu aplicación siempre esté ofreciendo valor y satisfaciendo a tus usuarios.

## Introducción

En este capítulo, aprenderás a:

- Comprender el Cambio de Paradigma de MLOps a LLMOps
- El Ciclo de Vida de LLM
- Herramientas del Ciclo de Vida
- Metrificación y Evaluación del Ciclo de Vida

## Comprender el Cambio de Paradigma de MLOps a LLMOps

Los LLMs son una nueva herramienta en el arsenal de la Inteligencia Artificial. Son increíblemente poderosos en tareas de análisis y generación para aplicaciones. Sin embargo, este poder tiene algunas consecuencias en cómo optimizamos las tareas de IA y Aprendizaje Automático Clásico.

Con esto, necesitamos un nuevo paradigma para adaptar esta herramienta de manera dinámica, con los incentivos correctos. Podemos categorizar las aplicaciones de IA más antiguas como "Apps de ML" y las aplicaciones de IA más nuevas como "Apps de GenAI" o simplemente "Apps de IA", reflejando la tecnología y técnicas predominantes en el momento. Esto cambia nuestra narrativa de múltiples maneras, observa la siguiente comparación.

![Comparación LLMOps vs. MLOps](../../../translated_images/01-llmops-shift.png?WT.38bc3eca81f659d83b17070d0a766bc3a9f13284b92c307e296915db4e683fcf.es.mc_id=academic-105485-koreys)

Nota que en LLMOps, estamos más enfocados en los Desarrolladores de Apps, usando integraciones como un punto clave, utilizando "Modelos-como-Servicio" y pensando en los siguientes puntos para las métricas.

- Calidad: Calidad de la respuesta
- Daño: IA Responsable
- Honestidad: Fundamentación de la respuesta (¿Tiene sentido? ¿Es correcta?)
- Costo: Presupuesto de la solución
- Latencia: Tiempo promedio para la respuesta de token

## El Ciclo de Vida de LLM

Primero, para entender el ciclo de vida y las modificaciones, observemos la siguiente infografía.

![Infografía de LLMOps](../../../translated_images/02-llmops.png?WT.32553adc9de4d89bb1d6a2f1f99d985457158a3be863e8e5dddc5e3dd074558a.es.mc_id=academic-105485-koreys)

Como puedes notar, esto es diferente de los ciclos de vida usuales de MLOps. Los LLMs tienen muchos nuevos requisitos, como la Elaboración de Prompts, diferentes técnicas para mejorar la calidad (Fine-Tuning, RAG, Meta-Prompts), diferentes evaluaciones y responsabilidades con IA responsable, y por último, nuevas métricas de evaluación (Calidad, Daño, Honestidad, Costo y Latencia).

Por ejemplo, observa cómo ideamos. Usando la ingeniería de prompts para experimentar con varios LLMs y explorar posibilidades para probar si su Hipótesis podría ser correcta.

Nota que esto no es lineal, sino bucles integrados, iterativos y con un ciclo general.

¿Cómo podríamos explorar esos pasos? Vamos a detallar cómo podríamos construir un ciclo de vida.

![Flujo de Trabajo de LLMOps](../../../translated_images/03-llm-stage-flows.png?WT.118920c8fd638f0879fe06c5e6eb9d91536e8b9c6bc56808ebed8706812f5391.es.mc_id=academic-105485-koreys)

Esto puede parecer un poco complicado, enfoquémonos en los tres grandes pasos primero.

1. Ideación/Exploración: Exploración, aquí podemos explorar de acuerdo a nuestras necesidades de negocio. Prototipado, creando un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) y probar si es lo suficientemente eficiente para nuestra Hipótesis.
2. Construcción/Aumento: Implementación, ahora, comenzamos a evaluar para conjuntos de datos más grandes, implementar técnicas como Fine-tuning y RAG, para verificar la robustez de nuestra solución. Si no lo es, reimplementarlo, añadiendo nuevos pasos en nuestro flujo o reestructurando los datos, podría ayudar. Después de probar nuestro flujo y nuestra escala, si funciona y verifica nuestras Métricas, está listo para el siguiente paso.
3. Operacionalización: Integración, ahora añadiendo Sistemas de Monitoreo y Alertas a nuestro sistema, implementación e integración de la aplicación a nuestra Aplicación.

Luego, tenemos el ciclo general de Gestión, enfocándonos en la seguridad, cumplimiento y gobernanza.

¡Felicidades! Ahora tienes tu App de IA lista para funcionar y operativa. Para una experiencia práctica, echa un vistazo a la [Demostración de Chat de Contoso.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreys)

Ahora, ¿qué herramientas podríamos usar?

## Herramientas del Ciclo de Vida

Para las herramientas, Microsoft ofrece la [Plataforma de Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) y [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) para facilitar y hacer que tu ciclo sea fácil de implementar y listo para funcionar.

La [Plataforma de Azure AI](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreys) te permite usar [AI Studio](https://ai.azure.com/?WT.mc_id=academic-105485-koreys). AI Studio es un portal web que te permite explorar modelos, muestras y herramientas. Gestionar tus recursos, flujos de desarrollo de UI y opciones de SDK/CLI para el desarrollo orientado a código.

![Posibilidades de Azure AI](../../../translated_images/04-azure-ai-platform.png?WT.a39053c2efd7670298a79282658a9f5bf903dec5c1938b1a08cf45f1284e6ac0.es.mc_id=academic-105485-koreys)

Azure AI te permite usar múltiples recursos, para gestionar tus operaciones, servicios, proyectos, búsqueda vectorial y necesidades de bases de datos.

![LLMOps con Azure AI](../../../translated_images/05-llm-azure-ai-prompt.png?WT.9189130ce4f2e7c8667fc7c83c6b89236ce5c6361150f47104c27c105f04b487.es.mc_id=academic-105485-koreys)

Construir, desde Pruebas de Concepto (POC) hasta aplicaciones a gran escala con PromptFlow:

- Diseñar y Construir apps desde VS Code, con herramientas visuales y funcionales
- Probar y ajustar tus apps para una IA de calidad, con facilidad.
- Usar Azure AI Studio para Integrar e Iterar con la nube, Empujar e Implementar para una integración rápida.

![LLMOps con PromptFlow](../../../translated_images/06-llm-promptflow.png?WT.e479dfedaa5f6ef7d36a11edbff74ac5579c3121ba0be0ee32eb5fc3eb17bd77.es.mc_id=academic-105485-koreys)

## ¡Genial! ¡Continúa tu Aprendizaje!

Increíble, ahora aprende más sobre cómo estructuramos una aplicación para usar los conceptos con la [App de Chat de Contoso](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), para ver cómo Cloud Advocacy añade esos conceptos en demostraciones. Para más contenido, consulta nuestra [sesión de Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ahora, revisa la Lección 15, para entender cómo [Generación Aumentada por Recuperación y Bases de Datos Vectoriales](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactan en la IA Generativa y para crear Aplicaciones más atractivas.

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.