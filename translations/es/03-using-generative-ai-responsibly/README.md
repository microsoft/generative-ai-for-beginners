# Uso Responsable de la IA Generativa

[![Uso Responsable de la IA Generativa](../../../translated_images/03-lesson-banner.png?WT.b0b917735411b39a55748e827c5c3121004890110b27f306bfe685c450c81ff9.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Haz clic en la imagen de arriba para ver el video de esta lección_

Es fácil sentirse fascinado por la IA y la IA generativa en particular, pero es importante considerar cómo usarla de manera responsable. Debes considerar aspectos como asegurar que el resultado sea justo, no dañino y más. Este capítulo tiene como objetivo proporcionarte el contexto mencionado, qué considerar y cómo tomar medidas activas para mejorar tu uso de la IA.

## Introducción

Esta lección cubrirá:

- Por qué deberías priorizar la IA Responsable al construir aplicaciones de IA Generativa.
- Principios fundamentales de la IA Responsable y cómo se relacionan con la IA Generativa.
- Cómo poner en práctica estos principios de IA Responsable a través de estrategias y herramientas.

## Objetivos de Aprendizaje

Al completar esta lección, sabrás:

- La importancia de la IA Responsable al construir aplicaciones de IA Generativa.
- Cuándo pensar y aplicar los principios fundamentales de la IA Responsable al construir aplicaciones de IA Generativa.
- Qué herramientas y estrategias están disponibles para poner en práctica el concepto de IA Responsable.

## Principios de IA Responsable

La emoción por la IA Generativa nunca ha sido tan alta. Esta emoción ha atraído a muchos nuevos desarrolladores, atención y financiamiento a este espacio. Si bien esto es muy positivo para cualquiera que busque construir productos y empresas utilizando IA Generativa, también es importante proceder de manera responsable.

A lo largo de este curso, nos enfocamos en construir nuestra startup y nuestro producto educativo de IA. Usaremos los principios de la IA Responsable: Equidad, Inclusividad, Confiabilidad/Seguridad, Seguridad y Privacidad, Transparencia y Responsabilidad. Con estos principios, exploraremos cómo se relacionan con nuestro uso de la IA Generativa en nuestros productos.

## Por Qué Deberías Priorizar la IA Responsable

Al construir un producto, adoptar un enfoque centrado en el ser humano teniendo en cuenta el mejor interés de tus usuarios conduce a los mejores resultados.

La singularidad de la IA Generativa es su capacidad para crear respuestas útiles, información, orientación y contenido para los usuarios. Esto se puede hacer sin muchos pasos manuales, lo que puede llevar a resultados muy impresionantes. Sin una planificación y estrategias adecuadas, también puede, lamentablemente, conducir a algunos resultados dañinos para tus usuarios, tu producto y la sociedad en general.

Veamos algunos (pero no todos) de estos resultados potencialmente dañinos:

### Alucinaciones

Las alucinaciones son un término utilizado para describir cuando un LLM produce contenido que es completamente sin sentido o algo que sabemos que es incorrecto fácticamente basado en otras fuentes de información.

Tomemos, por ejemplo, que construimos una función para nuestra startup que permite a los estudiantes hacer preguntas históricas a un modelo. Un estudiante hace la pregunta `Who was the sole survivor of Titanic?`

El modelo produce una respuesta como la siguiente:

![Prompt diciendo "¿Quién fue el único sobreviviente del Titanic?"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp)

> _(Fuente: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Esta es una respuesta muy confiada y completa. Desafortunadamente, es incorrecta. Incluso con una cantidad mínima de investigación, uno descubriría que hubo más de un sobreviviente del desastre del Titanic. Para un estudiante que recién comienza a investigar este tema, esta respuesta puede ser lo suficientemente persuasiva como para no ser cuestionada y tratada como un hecho. Las consecuencias de esto pueden llevar a que el sistema de IA sea poco confiable y afecte negativamente la reputación de nuestra startup.

Con cada iteración de cualquier LLM dado, hemos visto mejoras en el rendimiento en torno a minimizar las alucinaciones. Incluso con esta mejora, nosotros como constructores y usuarios de aplicaciones todavía necesitamos ser conscientes de estas limitaciones.

### Contenido Dañino

En la sección anterior cubrimos cuando un LLM produce respuestas incorrectas o sin sentido. Otro riesgo del que debemos estar conscientes es cuando un modelo responde con contenido dañino.

El contenido dañino se puede definir como:

- Proporcionar instrucciones o alentar el autodaño o el daño a ciertos grupos.
- Contenido odioso o denigrante.
- Guiar la planificación de cualquier tipo de ataque o actos violentos.
- Proporcionar instrucciones sobre cómo encontrar contenido ilegal o cometer actos ilegales.
- Mostrar contenido sexualmente explícito.

Para nuestra startup, queremos asegurarnos de tener las herramientas y estrategias adecuadas para evitar que este tipo de contenido sea visto por los estudiantes.

### Falta de Equidad

La equidad se define como "asegurar que un sistema de IA esté libre de sesgos y discriminación y que trate a todos de manera justa e igualitaria". En el mundo de la IA Generativa, queremos asegurarnos de que las visiones del mundo excluyentes de los grupos marginados no sean reforzadas por la salida del modelo.

Estos tipos de salidas no solo son destructivos para construir experiencias de producto positivas para nuestros usuarios, sino que también causan un daño social adicional. Como constructores de aplicaciones, siempre debemos tener en mente una base de usuarios amplia y diversa al construir soluciones con IA Generativa.

## Cómo Usar la IA Generativa de Manera Responsable

Ahora que hemos identificado la importancia de la IA Generativa Responsable, veamos 4 pasos que podemos tomar para construir nuestras soluciones de IA de manera responsable:

![Ciclo de Mitigación](../../../translated_images/mitigate-cycle.png?WT.ffc987e1880649a302a311432b78f49faa64e46f65df6350c9c409b5ed79549b.es.mc_id=academic-105485-koreyst)

### Medir Daños Potenciales

En las pruebas de software, probamos las acciones esperadas de un usuario en una aplicación. De manera similar, probar un conjunto diverso de prompts que los usuarios probablemente usarán es una buena manera de medir el daño potencial.

Dado que nuestra startup está construyendo un producto educativo, sería bueno preparar una lista de prompts relacionados con la educación. Esto podría ser para cubrir un cierto tema, hechos históricos y prompts sobre la vida estudiantil.

### Mitigar Daños Potenciales

Ahora es el momento de encontrar formas en las que podamos prevenir o limitar el daño potencial causado por el modelo y sus respuestas. Podemos ver esto en 4 capas diferentes:

![Capas de Mitigación](../../../translated_images/mitigation-layers.png?WT.cb109f48e143f1ff4dee760b4b0c9477c7d11c2fe57f3efdd89f68c1109f2de6.es.mc_id=academic-105485-koreyst)

- **Modelo**. Elegir el modelo correcto para el caso de uso correcto. Modelos más grandes y complejos como GPT-4 pueden causar más riesgo de contenido dañino cuando se aplican a casos de uso más pequeños y específicos. Usar tus datos de entrenamiento para ajustar también reduce el riesgo de contenido dañino.

- **Sistema de Seguridad**. Un sistema de seguridad es un conjunto de herramientas y configuraciones en la plataforma que sirve al modelo que ayuda a mitigar el daño. Un ejemplo de esto es el sistema de filtrado de contenido en el servicio de Azure OpenAI. Los sistemas también deben detectar ataques de fuga y actividades no deseadas como solicitudes de bots.

- **Metaprompt**. Los metaprompts y la fundamentación son formas en que podemos dirigir o limitar el modelo basado en ciertos comportamientos e información. Esto podría ser usar entradas del sistema para definir ciertos límites del modelo. Además, proporcionar salidas que sean más relevantes para el alcance o dominio del sistema.

También puede ser usar técnicas como la Generación Aumentada por Recuperación (RAG) para que el modelo solo obtenga información de una selección de fuentes confiables. Hay una lección más adelante en este curso para [construir aplicaciones de búsqueda](../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiencia del Usuario**. La capa final es donde el usuario interactúa directamente con el modelo a través de la interfaz de nuestra aplicación de alguna manera. De esta manera, podemos diseñar la UI/UX para limitar al usuario en los tipos de entradas que pueden enviar al modelo, así como el texto o las imágenes mostradas al usuario. Al desplegar la aplicación de IA, también debemos ser transparentes sobre lo que nuestra aplicación de IA Generativa puede y no puede hacer.

Tenemos una lección completa dedicada a [Diseñar UX para Aplicaciones de IA](../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluar el modelo**. Trabajar con LLMs puede ser un desafío porque no siempre tenemos control sobre los datos con los que se entrenó el modelo. Independientemente, siempre debemos evaluar el rendimiento y las salidas del modelo. Aún es importante medir la precisión, similitud, fundamentación y relevancia de la salida del modelo. Esto ayuda a proporcionar transparencia y confianza a los interesados y usuarios.

### Operar una Solución de IA Generativa Responsable

Construir una práctica operacional alrededor de tus aplicaciones de IA es la etapa final. Esto incluye asociarse con otras partes de nuestra startup como Legal y Seguridad para asegurarnos de que cumplimos con todas las políticas regulatorias. Antes de lanzar, también queremos construir planes alrededor de la entrega, manejo de incidentes y retroceso para evitar cualquier daño a nuestros usuarios mientras crecemos.

## Herramientas

Si bien el trabajo de desarrollar soluciones de IA Responsable puede parecer mucho, es un esfuerzo que vale la pena. A medida que el área de la IA Generativa crece, más herramientas para ayudar a los desarrolladores a integrar la responsabilidad en sus flujos de trabajo de manera eficiente madurarán. Por ejemplo, el [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) puede ayudar a detectar contenido e imágenes dañinas a través de una solicitud de API.

## Verificación de Conocimientos

¿Cuáles son algunas cosas de las que necesitas preocuparte para asegurar un uso responsable de la IA?

1. Que la respuesta sea correcta.
1. Uso dañino, que la IA no se use para propósitos criminales.
1. Asegurar que la IA esté libre de sesgos y discriminación.

A: 2 y 3 son correctas. La IA Responsable te ayuda a considerar cómo mitigar efectos dañinos y sesgos y más.

## 🚀 Desafío

Lee sobre [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) y ve qué puedes adoptar para tu uso.

## Gran Trabajo, Continúa Tu Aprendizaje

Después de completar esta lección, consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tu conocimiento en IA Generativa.

Dirígete a la Lección 4 donde veremos [Fundamentos de Ingeniería de Prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.