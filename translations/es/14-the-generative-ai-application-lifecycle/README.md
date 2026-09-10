[![Integración con llamadas a funciones](../../../translated_images/es/14-lesson-banner.066d74a31727ac12.webp)](https://youtu.be/ewtQY_RJrzs?si=dyJ2bjiljH7UUHCh)

# El ciclo de vida de una aplicación de IA Generativa

Una pregunta importante para todas las aplicaciones de IA es la relevancia de las características de IA, ya que la IA es un campo que evoluciona rápidamente; para asegurar que tu aplicación siga siendo relevante, confiable y robusta, necesitas monitorearla, evaluarla y mejorarla continuamente. Aquí es donde entra en juego el ciclo de vida de la IA generativa.

El ciclo de vida de la IA generativa es un marco que te guía a través de las etapas de desarrollo, despliegue y mantenimiento de una aplicación de IA generativa. Te ayuda a definir tus objetivos, medir tu desempeño, identificar tus desafíos e implementar tus soluciones. También te ayuda a alinear tu aplicación con los estándares éticos y legales de tu dominio y tus partes interesadas. Siguiendo el ciclo de vida de la IA generativa, puedes asegurar que tu aplicación siempre aporte valor y satisfaga a tus usuarios.

## Introducción

En este capítulo, aprenderás:

- Entender el cambio de paradigma de MLOps a LLMOps
- El ciclo de vida de LLM
- Herramientas del ciclo de vida
- Medición y evaluación del ciclo de vida

## Entender el cambio de paradigma de MLOps a LLMOps

Los LLM son una nueva herramienta en el arsenal de la inteligencia artificial, son increíblemente poderosos en tareas de análisis y generación para aplicaciones, sin embargo, este poder tiene algunas consecuencias en cómo optimizamos las tareas de IA y Aprendizaje Automático Clásico.

Por esto, necesitamos un nuevo paradigma para adaptar esta herramienta de forma dinámica, con los incentivos correctos. Podemos categorizar las aplicaciones antiguas de IA como "Apps de ML" y las aplicaciones más nuevas como "Apps de GenAI" o simplemente "Apps de IA", reflejando la tecnología y técnicas predominantes en ese momento. Esto cambia nuestra narrativa en múltiples formas, observa la siguiente comparación.

![Comparación LLMOps vs. MLOps](../../../translated_images/es/01-llmops-shift.29bc933cb3bb0080.webp)

Nota que en LLMOps, nos enfocamos más en los desarrolladores de aplicaciones, usando integraciones como un punto clave, utilizando "Modelos como Servicio" y pensando en los siguientes puntos para métricas.

- Calidad: Calidad de la respuesta
- Daño: IA responsable
- Honestidad: Fundamentación de la respuesta (¿Tiene sentido? ¿Es correcta?)
- Costo: Presupuesto de la solución
- Latencia: Tiempo promedio para respuesta por token

## El ciclo de vida de LLM

Primero, para entender el ciclo de vida y sus modificaciones, observemos la siguiente infografía.

![Infografía LLMOps](../../../translated_images/es/02-llmops.70a942ead05a7645.webp)

Como puedes notar, esto es diferente de los ciclos de vida habituales de MLOps. Los LLMs tienen muchos requerimientos nuevos, como prompting, diferentes técnicas para mejorar la calidad (Fine-Tuning, RAG, Meta-Prompts), diferentes evaluaciones y responsabilidad con IA responsable, y finalmente, nuevas métricas de evaluación (Calidad, Daño, Honestidad, Costo y Latencia).

Por ejemplo, observa cómo ideamos. Usamos ingeniería de prompts para experimentar con varios LLMs y explorar posibilidades para probar si su hipótesis podría ser correcta.

Nota que esto no es lineal, sino bucles integrados, iterativos y con un ciclo generalizador.

¿Cómo podemos explorar esos pasos? Vamos a entrar en detalle sobre cómo podríamos construir un ciclo de vida.

![Flujo de trabajo LLMOps](../../../translated_images/es/03-llm-stage-flows.3a1e1c401235a6cf.webp)

Esto puede parecer un poco complicado, enfoquémonos primero en los tres grandes pasos.

1. Idear/Explorar: Exploración, aquí podemos explorar según las necesidades del negocio. Prototipado, creando un [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) y probar si es suficientemente eficiente para nuestra hipótesis.
1. Construir/Aumentar: Implementación, ahora comenzamos a evaluar con conjuntos de datos más grandes, implementando técnicas como Fine-tuning y RAG para verificar la robustez de nuestra solución. Si no funciona, reimplementarla, añadir nuevos pasos en nuestro flujo o reestructurar los datos puede ayudar. Después de probar nuestro flujo y escala, si funciona y cumple con nuestras métricas, está listo para el siguiente paso.
1. Operacionalizar: Integración, ahora añadiendo sistemas de monitoreo y alertas a nuestro sistema, despliegue e integración de la aplicación con nuestra aplicación.

Luego, tenemos el ciclo general de gestión, enfocado en seguridad, cumplimiento y gobernanza.

Felicidades, ahora tienes tu aplicación de IA lista para usar y operar. Para una experiencia práctica, echa un vistazo a la [Demostración de Contoso Chat.](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst)

Ahora, ¿qué herramientas podríamos usar?

## Herramientas del ciclo de vida

Para herramientas, Microsoft ofrece la [Plataforma AI de Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst) y [PromptFlow](https://microsoft.github.io/promptflow/index.html?WT.mc_id=academic-105485-koreyst) que facilitan y hacen que tu ciclo sea fácil de implementar y listo para usar.

La [Plataforma AI de Azure](https://azure.microsoft.com/solutions/ai/?WT.mc_id=academic-105485-koreyst), te permite usar [Microsoft Foundry](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst). Microsoft Foundry (antes Azure AI Studio) es un portal web que te permite explorar modelos, muestras y herramientas, administrar tus recursos y usar flujos de desarrollo UI así como opciones SDK/CLI para desarrollo Code-First.

![Posibilidades de Azure AI](../../../translated_images/es/04-azure-ai-platform.80203baf03a12fa8.webp)

Azure AI te permite usar múltiples recursos para gestionar tus operaciones, servicios, proyectos, búsqueda vectorial y necesidades de bases de datos.

![LLMOps con Azure AI](../../../translated_images/es/05-llm-azure-ai-prompt.a5ce85cdbb494bdf.webp)

Construye, desde pruebas de concepto (POC) hasta aplicaciones a gran escala con PromptFlow:

- Diseña y crea apps desde VS Code, con herramientas visuales y funcionales
- Prueba y ajusta finamente tus apps para IA de calidad, con facilidad.
- Usa Microsoft Foundry para integrar e iterar con la nube, Push y Deploy para una integración rápida.

![LLMOps con PromptFlow](../../../translated_images/es/06-llm-promptflow.a183eba07a3a7fdf.webp)

## ¡Genial! Continúa tu aprendizaje!

Asombroso, ahora aprende más sobre cómo estructuramos una aplicación para usar los conceptos con la [App Contoso Chat](https://nitya.github.io/contoso-chat/?WT.mc_id=academic-105485-koreyst), para ver cómo Cloud Advocacy añade esos conceptos en demostraciones. Para más contenido, mira nuestra [sesión del Ignite!
](https://www.youtube.com/watch?v=DdOylyrTOWg)

Ahora, revisa la Lección 15, para entender cómo [Retrieval Augmented Generation y Bases de Datos Vectoriales](../15-rag-and-vector-databases/README.md?WT.mc_id=academic-105485-koreyst) impactan la IA Generativa y hacer aplicaciones más atractivas!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->