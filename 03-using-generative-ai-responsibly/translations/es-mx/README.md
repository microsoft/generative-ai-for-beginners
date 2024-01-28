# Usando IA Generativa de Forma Responsable

[![Usando IA Generativa de Forma Responsable](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)]() 

> **Video en Breve**

Es fácil sentirse fascinado por la IA y la IA generativa en particular, pero es necesario considerar cómo usarla de manera responsable. Debes considerar aspectos como cómo garantizar que la salida es justa, no dañina y más. Este capítulo tiene como objetivo proporcionarte el contexto mencionado, qué considerar y cómo tomar medidas activas para mejorar tu uso de la IA.

## Introducción

Esta lección cubrirá:

- Por qué deberías priorizar la IA Responsable al crear aplicaciones de IA Generativa.
- Principios básicos de la IA Responsable y cómo se relacionan con la IA Generativa.
- Cómo poner estos principios de IA Responsable en práctica a través de estrategias y herramientas.

## Metas de Aprendizaje

Después de completar esta lección sabrás: 

- La importancia de la IA Responsable al crear aplicaciones de IA Generativa.
- Cuándo pensar y aplicar los principios básicos de la IA Responsable al crear aplicaciones de IA Generativa.
- Qué herramientas y estrategias tienes a tu disposición para poner en práctica el concepto de IA Responsable.

## Principios de IA Responsable

El entusiasmo por la IA Generativa nunca ha sido tan grande. Este entusiasmo ha atraído a muchos nuevos desarrolladores, atención y financiación a este espacio. Si bien esto es muy positivo para cualquiera que busque crear productos y empresas que hacen uso de la IA Generativa, también es importante que procedamos de manera responsable.

A lo largo de este curso, nos centraremos en desarrollar nuestra startup y nuestro producto educativo de IA. Utilizaremos los principios de la IA Responsable: Equidad, Inclusión, Confiabilidad/Seguridad, Seguridad y Privacidad, Transparencia y Responsabilidad. Con estos principios, exploraremos cómo se relacionan con nuestro uso de IA Generativa en nuestros productos.

## ¿Por qué Deberías Priorizar la IA Responsable?

Al crear un producto, adoptar un enfoque centrado en el ser humano teniendo en mente los mejores intereses del usuario conduce a los mejores resultados.

La singularidad de la IA Generativa es su poder para crear respuestas, información, orientación y contenido útiles para los usuarios. Esto se puede hacer sin muchos pasos manuales que pueden conducir a resultados muy impresionantes. Sin una planificación y estrategias apropiadas, lamentablemente también puede producir resultados dañinos para tus usuarios, tu producto y la sociedad en su conjunto.

Veamos algunos (pero no todos) de estos resultados potencialmente dañinos:

### Alucinaciones

Las alucinaciones son un término utilizado para describir cuando un LLM produce contenido que es completamente absurdo o algo que sabemos que es incorrecto según otras fuentes de información.

Tomemos, por ejemplo, que creamos una función para nuestra startup que permite a los estudiantes hacer preguntas históricas a un modelo. Un estudiante hace la pregunta `¿Quién fue el único superviviente del Titanic?`

El modelo produce una respuesta como la siguiente:

![Prompt que dice "¿Quién fue el único superviviente del Titanic?"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> *(Fuente: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))*

Esta es una respuesta muy segura y completa. Lamentablemente, es incorrecta. Incluso con una mínima cantidad de investigación, uno descubriría que hubo más de un superviviente del desastre del Titanic. Para un estudiante que recién comienza a investigar este tema, esta respuesta puede ser lo suficientemente persuasiva como para no ser cuestionada y tratada como un hecho. Las consecuencias de esto pueden llevar a que el sistema de IA no sea confiable y afecte negativamente a la reputación de nuestra startup.

Con cada iteración de cualquier LLM determinado, hemos visto mejoras de rendimiento en torno a minimizar las alucinaciones. Incluso con esta mejora, nosotros, como creadores de aplicaciones y usuarios, aún necesitamos ser conscientes de estas limitaciones.

### Contenido Dañino

En la sección anterior cubrimos cuándo un LLM produce respuestas incorrectas o absurdas. Otro riesgo que debemos tener en cuenta es cuando un modelo responde con contenido dañino.

El contenido dañino puede ser definido como:

- Proporcionar instrucciones o fomentar la autolesión o el daño a ciertos grupos.
- Contenido odioso o denigrante.
- Orientar la planificación de cualquier tipo de ataque o actos violentos.
- Proporcionar instrucciones sobre cómo encontrar contenido ilegal o cometer actos ilegales.
- Mostrar contenido sexualmente explícito.

Para nuestra startup, queremos asegurarnos de contar con las herramientas y estrategias adecuadas para prevenir que este tipo de contenido sea visto por estudiantes.

### Falta de Equidad

La equidad se define como “garantizar que un sistema de IA esté libre de prejuicios y discriminación y que trate a todos de manera justa e igualitaria”. En el mundo de la IA Generativa, queremos asegurarnos de que las visiones del mundo excluyentes de los grupos marginados no sean reforzadas por la salida del modelo.

Estos tipos de salidas no sólo son destructivas para crear experiencias positivas de producto para nuestros usuarios, sino que también causan más daños a la sociedad. Como creadores de aplicaciones, siempre debemos tener en cuenta una base de usuarios amplia y diversa al crear soluciones con IA Generativa.

## Cómo Utilizar la IA Generativa de Manera Responsable

Ahora que hemos identificado la importancia de la IA Generativa Responsable, veamos 4 pasos que podemos tomar para construir nuestras soluciones de IA de forma responsable:

![Ciclo de Mitigación](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Medir Posibles Daños

En las pruebas de software, evaluamos las acciones esperadas de un usuario en una aplicación. De manera similar, probar un conjunto diverso de prompts que los usuarios muy probablemente utilizarán es una buena manera de medir el daño potencial.

Dado que nuestra startup está creando un producto educativo, sería bueno preparar una lista de sugerencias relacionadas con la educación. Esto podría ser para cubrir un tema determinado, hechos históricos y prompts sobre la vida estudiantil.

### Mitigar Posibles Daños

Ahora es el momento de encontrar formas de prevenir o limitar el daño potencial causado por el modelo y sus respuestas. Podemos observar esto en 4 capas diferentes:

![Capas de Mitigación](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Modelo**. Elegir el modelo adecuado para el caso de uso adecuado. Los modelos más grandes y complejos como GPT-4 pueden generar un mayor riesgo de contenido dañino cuando se aplican a casos de uso más pequeños y específicos. Usar tus datos de entrenamiento para afinar el modelo también reduce el riesgo de contenido dañino.

- **Sistema de Seguridad**. Un sistema de seguridad es un conjunto de herramientas y configuraciones en la plataforma que sirve al modelo que ayudan a mitigar el daño. Un ejemplo de esto es el sistema de filtrado de contenido del servicio Azure OpenAI. Los sistemas también deberían detectar ataques de jailbreak y actividades no deseadas, como solicitudes de bots.

- **Metaprompt**. Los metaprompts y la fundamentación son formas en que podemos dirigir o limitar el modelo de acuerdo a ciertos comportamientos e información. Esto podría ser utilizando de entradas de sistema para definir ciertos límites del modelo. Además, proporcionar salidas que sean más relevantes al alcance o dominio del sistema.

También se pueden utilizar técnicas como la Generación Aumentada de Recuperación (RAG) para que el modelo solo extraiga información de una selección de fuentes confiables. Hay una lección más adelante en este curso para [construir aplicaciones de búsqueda](../../../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst).

- **User Experience**. La capa final es donde el usuario interactúa directamente con el modelo a través de la interfaz de nuestra aplicación de alguna forma. De esta manera, podemos diseñar la UI/UX para limitar al usuario los tipos de entradas que puede enviar al modelo, así como el texto o las imágenes que se muestran al usuario. Al implementar la aplicación de IA, también debemos ser transparentes sobre lo que nuestra aplicación de IA Generativa puede y no puede hacer.

Tenemos una lección completa dedicada a [Diseñar UX para Aplicaciones de IA](../../../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluate model**. Trabajar con LLMs puede ser un desafío porque no siempre tenemos control sobre los datos con los que el modelo fue entrenado. De todos modos, siempre deberíamos evaluar el rendimiento y las salidas del modelo. Sigue siendo importante medir la precisión, la similaridad, la fundamentación y la relevancia de la salida del modelo. Esto ayuda a brindar transparencia y confianza a las partes interesadas y usuarios.

### Operar una solución de IA Generativa Responsable

Desarrollar una práctica operativa en torno a tus aplicaciones de IA es la etapa final. Esto incluye asociarnos con otras partes de nuestra startup, como Legal y Seguridad, para garantizar que cumplimos con todas las políticas regulatorias. Antes del lanzamiento, también queremos elaborar planes en torno a la entrega, el manejo de incidentes y la reversión para prevenir que aumente cualquier daño a nuestros usuarios.

## Herramientas

Si bien el trabajo de desarrollar soluciones de IA Responsable puede parecer mucho, vale la pena el esfuerzo. A medida que crece el área de la IA Generativa, más herramientas para ayudar a los desarrolladores a integrar eficientemente la responsabilidad en sus flujos de trabajo madurarán. Por ejemplo, [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) puede ayudar a detectar contenido e imágenes dañinos a través de una solicitud de API.

## Verificación de conocimientos

¿Cuáles son algunas de las cosas que debes tener en cuenta para garantizar un uso responsable de la IA?

1. Que la respuesta sea correcta.
2. Uso dañino, que la IA no se utilice con fines delictivos.
3. Garantizar que la IA esté libre de sesgos y discriminación.

R: 2 y 3 son correctas. La IA Responsable te ayuda a considerar cómo mitigar los efectos y sesgos dañinos y más.

## 🚀 Desafío

Lee sobre [Azure AI Content Saftey](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) y ve qué puedes adoptar para su uso.

## ¡Buen trabajo! Continúa tu Aprendizaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 4, donde veremos ¡[Fundamentos de Prompt Engineering](../../../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)!
