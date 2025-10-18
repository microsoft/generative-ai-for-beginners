<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4d57fad773cbeb69c5dd62e65c34200d",
  "translation_date": "2025-10-17T22:47:15+00:00",
  "source_file": "03-using-generative-ai-responsibly/README.md",
  "language_code": "es"
}
-->
# Uso Responsable de la IA Generativa

[![Uso Responsable de la IA Generativa](../../../translated_images/03-lesson-banner.1ed56067a452d97709d51f6cc8b6953918b2287132f4909ade2008c936cd4af9.es.png)](https://youtu.be/YOp-e1GjZdA?si=7Wv4wu3x44L1DCVj)

> _Haz clic en la imagen de arriba para ver el video de esta lección_

Es fácil sentirse fascinado por la IA y, en particular, por la IA generativa, pero es importante considerar cómo usarla de manera responsable. Debes pensar en aspectos como garantizar que los resultados sean justos, no dañinos y más. Este capítulo tiene como objetivo proporcionarte el contexto mencionado, qué considerar y cómo tomar medidas activas para mejorar tu uso de la IA.

## Introducción

Esta lección cubrirá:

- Por qué deberías priorizar la IA Responsable al construir aplicaciones de IA Generativa.
- Principios fundamentales de la IA Responsable y cómo se relacionan con la IA Generativa.
- Cómo poner en práctica estos principios de IA Responsable mediante estrategias y herramientas.

## Objetivos de Aprendizaje

Después de completar esta lección, sabrás:

- La importancia de la IA Responsable al construir aplicaciones de IA Generativa.
- Cuándo pensar y aplicar los principios fundamentales de la IA Responsable al construir aplicaciones de IA Generativa.
- Qué herramientas y estrategias están disponibles para poner en práctica el concepto de IA Responsable.

## Principios de la IA Responsable

El entusiasmo por la IA Generativa nunca ha sido mayor. Este entusiasmo ha atraído a muchos nuevos desarrolladores, atención y financiamiento a este campo. Si bien esto es muy positivo para quienes buscan construir productos y empresas utilizando IA Generativa, también es importante proceder de manera responsable.

A lo largo de este curso, nos enfocaremos en construir nuestra startup y nuestro producto educativo basado en IA. Utilizaremos los principios de la IA Responsable: Justicia, Inclusión, Fiabilidad/Seguridad, Seguridad y Privacidad, Transparencia y Responsabilidad. Con estos principios, exploraremos cómo se relacionan con el uso de la IA Generativa en nuestros productos.

## Por qué Deberías Priorizar la IA Responsable

Al construir un producto, adoptar un enfoque centrado en el ser humano, teniendo en cuenta los mejores intereses de tus usuarios, conduce a los mejores resultados.

La singularidad de la IA Generativa radica en su capacidad para crear respuestas útiles, información, orientación y contenido para los usuarios. Esto se puede hacer sin muchos pasos manuales, lo que puede llevar a resultados muy impresionantes. Sin una planificación y estrategias adecuadas, también puede, lamentablemente, generar resultados perjudiciales para tus usuarios, tu producto y la sociedad en general.

Veamos algunos (pero no todos) de estos posibles resultados perjudiciales:

### Alucinaciones

Las alucinaciones son un término utilizado para describir cuando un LLM produce contenido que es completamente sin sentido o algo que sabemos que es incorrecto según otras fuentes de información.

Tomemos como ejemplo que construimos una función para nuestra startup que permite a los estudiantes hacer preguntas históricas a un modelo. Un estudiante hace la pregunta: `¿Quién fue el único sobreviviente del Titanic?`

El modelo produce una respuesta como la siguiente:

![Pregunta: "¿Quién fue el único sobreviviente del Titanic?"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Fuente: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Esta es una respuesta muy confiada y detallada. Desafortunadamente, es incorrecta. Incluso con una mínima cantidad de investigación, uno descubriría que hubo más de un sobreviviente del desastre del Titanic. Para un estudiante que recién comienza a investigar este tema, esta respuesta puede ser lo suficientemente persuasiva como para no ser cuestionada y tratarse como un hecho. Las consecuencias de esto pueden llevar a que el sistema de IA sea poco confiable y afectar negativamente la reputación de nuestra startup.

Con cada iteración de un LLM dado, hemos visto mejoras en el rendimiento para minimizar las alucinaciones. Incluso con esta mejora, nosotros, como desarrolladores de aplicaciones y usuarios, aún debemos ser conscientes de estas limitaciones.

### Contenido Dañino

En la sección anterior cubrimos el caso en que un LLM produce respuestas incorrectas o sin sentido. Otro riesgo que debemos tener en cuenta es cuando un modelo responde con contenido dañino.

El contenido dañino puede definirse como:

- Proporcionar instrucciones o fomentar el autodaño o el daño a ciertos grupos.
- Contenido odioso o degradante.
- Guiar la planificación de cualquier tipo de ataque o actos violentos.
- Proporcionar instrucciones sobre cómo encontrar contenido ilegal o cometer actos ilegales.
- Mostrar contenido sexualmente explícito.

Para nuestra startup, queremos asegurarnos de tener las herramientas y estrategias adecuadas para evitar que este tipo de contenido sea visto por los estudiantes.

### Falta de Justicia

La justicia se define como “asegurar que un sistema de IA esté libre de sesgos y discriminación y que trate a todos de manera justa e igualitaria”. En el mundo de la IA Generativa, queremos asegurarnos de que las visiones del mundo excluyentes hacia grupos marginados no sean reforzadas por los resultados del modelo.

Este tipo de resultados no solo son destructivos para construir experiencias de producto positivas para nuestros usuarios, sino que también causan un daño social mayor. Como desarrolladores de aplicaciones, siempre debemos tener en cuenta una base de usuarios amplia y diversa al construir soluciones con IA Generativa.

## Cómo Usar la IA Generativa de Manera Responsable

Ahora que hemos identificado la importancia de la IA Generativa Responsable, veamos 4 pasos que podemos tomar para construir nuestras soluciones de IA de manera responsable:

![Ciclo de Mitigación](../../../translated_images/mitigate-cycle.babcd5a5658e1775d5f2cb47f2ff305cca090400a72d98d0f9e57e9db5637c72.es.png)

### Medir los Posibles Daños

En las pruebas de software, probamos las acciones esperadas de un usuario en una aplicación. De manera similar, probar un conjunto diverso de indicaciones que los usuarios probablemente usarán es una buena manera de medir los posibles daños.

Dado que nuestra startup está construyendo un producto educativo, sería bueno preparar una lista de indicaciones relacionadas con la educación. Esto podría incluir cubrir ciertos temas, hechos históricos e indicaciones sobre la vida estudiantil.

### Mitigar los Posibles Daños

Es momento de encontrar formas de prevenir o limitar el daño potencial causado por el modelo y sus respuestas. Podemos analizar esto en 4 capas diferentes:

![Capas de Mitigación](../../../translated_images/mitigation-layers.377215120b9a1159a8c3982c6bbcf41b6adf8c8fa04ce35cbaeeb13b4979cdfc.es.png)

- **Modelo**. Elegir el modelo adecuado para el caso de uso adecuado. Modelos más grandes y complejos como GPT-4 pueden causar más riesgos de contenido dañino cuando se aplican a casos de uso más pequeños y específicos. Usar tus datos de entrenamiento para ajustar el modelo también reduce el riesgo de contenido dañino.

- **Sistema de Seguridad**. Un sistema de seguridad es un conjunto de herramientas y configuraciones en la plataforma que sirve al modelo y que ayuda a mitigar daños. Un ejemplo de esto es el sistema de filtrado de contenido en el servicio Azure OpenAI. Los sistemas también deben detectar ataques de jailbreak y actividades no deseadas como solicitudes de bots.

- **Metaprompt**. Los metaprompts y la contextualización son formas de dirigir o limitar el modelo en función de ciertos comportamientos e información. Esto podría incluir el uso de entradas del sistema para definir ciertos límites del modelo. Además, proporcionar resultados más relevantes al alcance o dominio del sistema.

También se pueden usar técnicas como la Generación Aumentada por Recuperación (RAG) para que el modelo solo extraiga información de una selección de fuentes confiables. Hay una lección más adelante en este curso sobre [cómo construir aplicaciones de búsqueda](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Experiencia del Usuario**. La última capa es donde el usuario interactúa directamente con el modelo a través de la interfaz de nuestra aplicación de alguna manera. De esta manera, podemos diseñar la interfaz de usuario/experiencia de usuario (UI/UX) para limitar al usuario en los tipos de entradas que puede enviar al modelo, así como el texto o las imágenes que se muestran al usuario. Al implementar la aplicación de IA, también debemos ser transparentes sobre lo que nuestra aplicación de IA Generativa puede y no puede hacer.

Tenemos una lección completa dedicada a [Diseñar la UX para Aplicaciones de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **Evaluar el modelo**. Trabajar con LLMs puede ser un desafío porque no siempre tenemos control sobre los datos con los que se entrenó el modelo. Sin embargo, siempre debemos evaluar el rendimiento y los resultados del modelo. Sigue siendo importante medir la precisión, similitud, fundamentación y relevancia de los resultados del modelo. Esto ayuda a proporcionar transparencia y confianza a las partes interesadas y a los usuarios.

### Operar una Solución de IA Generativa Responsable

Construir una práctica operativa en torno a tus aplicaciones de IA es la etapa final. Esto incluye asociarse con otras partes de nuestra startup, como los equipos legales y de seguridad, para garantizar el cumplimiento de todas las políticas regulatorias. Antes de lanzar, también queremos construir planes en torno a la entrega, manejo de incidentes y retrocesos para evitar cualquier daño a nuestros usuarios.

## Herramientas

Aunque el trabajo de desarrollar soluciones de IA Responsable puede parecer mucho, es un esfuerzo que vale la pena. A medida que el área de la IA Generativa crece, más herramientas para ayudar a los desarrolladores a integrar la responsabilidad en sus flujos de trabajo madurarán. Por ejemplo, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) puede ayudar a detectar contenido e imágenes dañinas a través de una solicitud de API.

## Comprobación de Conocimientos

¿Qué cosas debes tener en cuenta para garantizar el uso responsable de la IA?

1. Que la respuesta sea correcta.  
2. Uso dañino, que la IA no se utilice con fines delictivos.  
3. Garantizar que la IA esté libre de sesgos y discriminación.  

R: 2 y 3 son correctas. La IA Responsable te ayuda a considerar cómo mitigar efectos dañinos, sesgos y más.

## 🚀 Desafío

Lee sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) y analiza qué puedes adoptar para tu uso.

## ¡Gran Trabajo, Continúa Aprendiendo!

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA Generativa.

¡Dirígete a la Lección 4 donde exploraremos [Fundamentos de la Ingeniería de Prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.