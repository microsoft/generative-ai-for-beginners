# Uso Responsable de la IA Generativa

[![Uso Responsable de la IA Generativa](../../images/03-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson3-gh?WT.mc_id=academic-105485-koreyst)

> _Haga click en la imagen de arriba para ver el video de esta lección_

Es fácil fascinarse con la IA, y en particular con la IA generativa, pero es necesario considerar cómo usarla responsablemente. Debe considerar aspectos como cómo garantizar que el resultado sea justo y no dañino, entre otros. Este capítulo busca brindarle el contexto mencionado, qué considerar y cómo tomar medidas activas para mejorar su uso de la IA.

## Introducción

Esta lección abordará:

- Por qué debería priorizar la IA Responsable al crear aplicaciones de IA Generativa.
- Principios fundamentales de la IA Responsable y su relación con la IA Generativa.
- Cómo poner en práctica estos principios de la IA Responsable mediante estrategias y herramientas.

## Objetivos de aprendizaje

Tras completar esta lección, sabrás:

- La importancia de la IA Responsable al crear aplicaciones de IA Generativa.
- Cuándo considerar y aplicar los principios fundamentales de la IA Responsable al crear aplicaciones de IA Generativa.
- Qué herramientas y estrategias tienes a tu disposición para poner en práctica el concepto de IA Responsable.

## Principios de la IA Responsable

El entusiasmo por la IA Generativa nunca ha sido tan grande. Este entusiasmo ha atraído a muchos nuevos desarrolladores, atención y financiación a este espacio. Si bien esto es muy positivo para quienes buscan crear productos y empresas utilizando IA Generativa, también es importante que procedamos con responsabilidad.

A lo largo de este curso, nos centraremos en el desarrollo de nuestra startup y nuestro producto educativo de IA. Utilizaremos los principios de la IA Responsable: Equidad, Inclusión, Fiabilidad/Seguridad, Seguridad y Privacidad, Transparencia y Responsabilidad. Con estos principios, exploraremos cómo se relacionan con el uso de la IA Generativa en nuestros productos.

## Por qué debería priorizar la IA responsable?

Al desarrollar un producto, adoptar un enfoque centrado en el usuario, priorizando el bienestar del usuario, genera los mejores resultados.

La singularidad de la IA generativa reside en su capacidad para crear respuestas, información, orientación y contenido útiles para los usuarios. Esto se puede lograr sin muchos pasos manuales, lo que puede generar resultados impresionantes. Sin una planificación y estrategias adecuadas, también puede, lamentablemente, tener consecuencias perjudiciales para los usuarios, el producto y la sociedad en su conjunto.

Analicemos algunos (pero no todos) de estos resultados potencialmente dañinos:

### Alucinaciones

El término alucinaciones se utiliza para describir cuando un Máster en Derecho (LLM) produce contenido completamente absurdo o algo que sabemos que es factualmente incorrecto según otras fuentes de información.

Por ejemplo, creamos una función para nuestra startup que permite a los estudiantes formular preguntas históricas a un modelo. Un estudiante pregunta: "Quién fue el único superviviente del Titanic?".

El modelo produce una respuesta como la siguiente:

![Indicación: "Quién fue el único superviviente del Titanic?"](../../../03-using-generative-ai-responsibly/images/ChatGPT-titanic-survivor-prompt.webp?WT.mc_id=academic-105485-koreyst)

> _(Fuente: [Flying bisons](https://flyingbisons.com?WT.mc_id=academic-105485-koreyst))_

Esta es una respuesta muy fiable y exhaustiva. Desafortunadamente, es incorrecta. Incluso con una investigación mínima, se descubriría que hubo más de un superviviente del desastre del Titanic. Para un estudiante que apenas comienza a investigar este tema, esta respuesta puede ser lo suficientemente convincente como para no ser cuestionada y considerada un hecho. Las consecuencias de esto pueden hacer que el sistema de IA sea poco fiable y afectar negativamente la reputación de nuestra startup.

Con cada iteración de cualquier LLM, hemos observado mejoras de rendimiento en la minimización de las alucinaciones. Aun con esta mejora, como desarrolladores de aplicaciones y usuarios, debemos ser conscientes de estas limitaciones.

### Contenido dañino

En la sección anterior, abordamos cuándo un LLM produce respuestas incorrectas o sin sentido. Otro riesgo que debemos tener en cuenta es cuando un modelo responde con contenido dañino.

El contenido dañino se puede definir como:

- Proporcionar instrucciones o incitar a la autolesión o a dañar a ciertos grupos.
- Contenido de odio o degradante.
- Orientar la planificación de cualquier tipo de ataque o acto violento.
- Proporcionar instrucciones sobre cómo encontrar contenido ilegal o cometer actos ilegales.
- Mostrar contenido sexualmente explícito.

En nuestra startup, queremos asegurarnos de contar con las herramientas y estrategias adecuadas para evitar que los estudiantes vean este tipo de contenido.

### Falta de imparcialidad

La imparcialidad se define como «garantizar que un sistema de IA esté libre de sesgos y discriminación, y que trate a todos de forma justa e igualitaria». En el ámbito de la IA generativa, queremos asegurarnos de que las visiones excluyentes de los grupos marginados no se vean reforzadas por los resultados del modelo.

Este tipo de resultados no solo perjudica la creación de experiencias positivas de producto para nuestros usuarios, sino que también causa un mayor daño social. Como desarrolladores de aplicaciones, siempre debemos tener en cuenta una base de usuarios amplia y diversa al crear soluciones con IA Generativa.

## Cómo usar la IA Generativa de forma responsable

Ahora que hemos identificado la importancia de la IA Generativa Responsable, veamos cuatro pasos que podemos seguir para desarrollar nuestras soluciones de IA de forma responsable:

![Mitigar el ciclo](../../images/mitigate-cycle.png?WT.mc_id=academic-105485-koreyst)

### Medir posibles daños

En las pruebas de software, evaluamos las acciones esperadas de un usuario en una aplicación. De igual forma, evaluar un conjunto diverso de indicaciones que los usuarios probablemente utilizarán es una buena manera de medir posibles daños.

Dado que nuestra startup está desarrollando un producto educativo, sería recomendable preparar una lista de indicaciones relacionadas con la educación. Esta podría abarcar un tema específico, hechos históricos e indicaciones sobre la vida estudiantil.

### Mitigar posibles daños

Ahora es el momento de encontrar maneras de prevenir o limitar los posibles daños causados ​​por el modelo y sus respuestas. Podemos analizar esto en cuatro niveles diferentes:

![Capas de mitigación](../../images/mitigation-layers.png?WT.mc_id=academic-105485-koreyst)

- **Modelo**. Elegir el modelo adecuado para el caso de uso adecuado. Los modelos más grandes y complejos, como GPT-4, pueden generar un mayor riesgo de contenido dañino al aplicarse a casos de uso más pequeños y específicos. Usar los datos de entrenamiento para ajustar el modelo también reduce el riesgo de contenido dañino.

- **Sistema de Seguridad**. Un sistema de seguridad es un conjunto de herramientas y configuraciones en la plataforma que sirve al modelo y que ayudan a mitigar los daños. Un ejemplo de esto es el sistema de filtrado de contenido del servicio Azure OpenAI. Los sistemas también deben detectar ataques de jailbreak y actividad no deseada, como solicitudes de bots.

- **Metaprompt**. Los metaprompts y la puesta a tierra son formas de dirigir o limitar el modelo en función de ciertos comportamientos e información. Esto podría implicar el uso de entradas del sistema para definir ciertos límites del modelo. Además, se pueden proporcionar salidas más relevantes para el alcance o dominio del sistema.

También se pueden utilizar técnicas como la Generación Aumentada por Recuperación (RAG) para que el modelo solo extraiga información de una selección de fuentes confiables. Más adelante en este curso, se incluye una lección sobre [desarrollo de aplicaciones de búsqueda](../../../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Experiencia de usuario**. La capa final es donde el usuario interactúa directamente con el modelo a través de la interfaz de nuestra aplicación. De esta manera, podemos diseñar la UI/UX para limitar los tipos de entradas que el usuario puede enviar al modelo, así como el texto o las imágenes que se le muestran. Al implementar la aplicación de IA, también debemos ser transparentes sobre lo que nuestra aplicación de IA generativa puede y no puede hacer.

Tenemos una lección completa dedicada a [Diseño de UX para Aplicaciones de IA](../../../12-designing-ux-for-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

- **Evaluar el modelo**. Trabajar con LLM puede ser un desafío porque no siempre tenemos control sobre los datos con los que se entrenó el modelo. En cualquier caso, siempre debemos evaluar el rendimiento y los resultados del modelo. Sigue siendo importante medir la precisión, la similitud, la solidez y la relevancia del resultado del modelo. Esto ayuda a brindar transparencia y confianza a las partes interesadas y a los usuarios.

### Operar una solución de IA Generativa Responsable

Desarrollar una práctica operativa en torno a sus aplicaciones de IA es la etapa final. Esto incluye la colaboración con otras áreas de nuestra startup, como los departamentos Legal y de Seguridad, para garantizar el cumplimiento de todas las políticas regulatorias. Antes del lanzamiento, también queremos desarrollar planes para la entrega, la gestión de incidentes y la reversión para evitar que los daños a nuestros usuarios se agraven.

## Herramientas

Aunque desarrollar soluciones de IA responsable pueda parecer una tarea ardua, vale la pena. A medida que crece el campo de la IA generativa, se desarrollarán más herramientas que ayuden a los desarrolladores a integrar la responsabilidad de forma eficiente en sus flujos de trabajo. Por ejemplo, la [Seguridad de contenido de IA de Azure](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) puede ayudar a detectar contenido e imágenes dañinos mediante una solicitud de API.

## Comprobación de conocimientos

Qué aspectos debes tener en cuenta para garantizar un uso responsable de la IA?

1. Que la respuesta sea correcta.
1. Uso perjudicial: que la IA no se utilice con fines delictivos.
1. Garantizar que la IA esté libre de sesgos y discriminación.

R: Las respuestas 2 y 3 son correctas. La IA responsable te ayuda a considerar cómo mitigar los efectos perjudiciales, los sesgos y mucho más.

## 🚀 Desafío

Infórmate sobre [Seguridad del contenido de la IA de Azure](https://learn.microsoft.com/azure/ai-services/content-safety/overview?WT.mc_id=academic-105485-koreyst) y descubre qué puedes adoptar para tu uso.

## ¡Buen trabajo! ¡Continúa aprendiendo!

Después de completar esta lección, consulta nuestra [Colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA generativa.

Dirígete a la Lección 4, donde veremos los [Fundamentos de ingeniería de indicaciones](../../../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst).