<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ec385b41ee50579025d50cc03bfb3a25",
  "translation_date": "2025-06-25T20:08:50+00:00",
  "source_file": "12-designing-ux-for-ai-applications/README.md",
  "language_code": "es"
}
-->
# Diseñando UX para Aplicaciones de IA

[![Diseñando UX para Aplicaciones de IA](../../../translated_images/12-lesson-banner.c53c3c7c802e8f563953ce388f6a987ca493472c724d924b060be470951c53c8.es.png)](https://aka.ms/gen-ai-lesson12-gh?WT.mc_id=academic-105485-koreyst)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

La experiencia del usuario es un aspecto muy importante al construir aplicaciones. Los usuarios necesitan poder usar tu aplicación de manera eficiente para realizar tareas. Ser eficiente es una cosa, pero también necesitas diseñar aplicaciones para que puedan ser utilizadas por todos, haciéndolas _accesibles_. Este capítulo se centrará en esta área para que, con suerte, termines diseñando una aplicación que la gente pueda y quiera usar.

## Introducción

La experiencia del usuario es cómo un usuario interactúa con y utiliza un producto o servicio específico, ya sea un sistema, herramienta o diseño. Al desarrollar aplicaciones de IA, los desarrolladores no solo se enfocan en asegurar que la experiencia del usuario sea efectiva sino también ética. En esta lección, cubrimos cómo construir aplicaciones de Inteligencia Artificial (IA) que aborden las necesidades del usuario.

La lección cubrirá las siguientes áreas:

- Introducción a la Experiencia del Usuario y Comprensión de las Necesidades del Usuario
- Diseñando Aplicaciones de IA para la Confianza y Transparencia
- Diseñando Aplicaciones de IA para la Colaboración y Retroalimentación

## Objetivos de aprendizaje

Después de tomar esta lección, podrás:

- Comprender cómo construir aplicaciones de IA que satisfagan las necesidades del usuario.
- Diseñar aplicaciones de IA que promuevan la confianza y la colaboración.

### Prerrequisito

Tómate un tiempo y lee más sobre [experiencia del usuario y pensamiento de diseño.](https://learn.microsoft.com/training/modules/ux-design?WT.mc_id=academic-105485-koreyst)

## Introducción a la Experiencia del Usuario y Comprensión de las Necesidades del Usuario

En nuestra startup educativa ficticia, tenemos dos usuarios principales, profesores y estudiantes. Cada uno de los dos usuarios tiene necesidades únicas. Un diseño centrado en el usuario prioriza al usuario asegurando que los productos sean relevantes y beneficiosos para aquellos a los que están destinados.

La aplicación debe ser **útil, confiable, accesible y agradable** para proporcionar una buena experiencia de usuario.

### Usabilidad

Ser útil significa que la aplicación tiene funcionalidades que coinciden con su propósito previsto, como automatizar el proceso de calificación o generar tarjetas de estudio para la revisión. Una aplicación que automatiza el proceso de calificación debe poder asignar puntuaciones a los trabajos de los estudiantes de manera precisa y eficiente, basándose en criterios predefinidos. Del mismo modo, una aplicación que genera tarjetas de estudio debe poder crear preguntas relevantes y diversas basadas en sus datos.

### Fiabilidad

Ser confiable significa que la aplicación puede realizar su tarea de manera consistente y sin errores. Sin embargo, la IA, al igual que los humanos, no es perfecta y puede ser propensa a errores. Las aplicaciones pueden encontrar errores o situaciones inesperadas que requieren intervención o corrección humana. ¿Cómo manejas los errores? En la última sección de esta lección, cubriremos cómo los sistemas y aplicaciones de IA están diseñados para la colaboración y retroalimentación.

### Accesibilidad

Ser accesible significa extender la experiencia del usuario a usuarios con diversas habilidades, incluidas aquellas con discapacidades, asegurando que nadie quede excluido. Al seguir las pautas y principios de accesibilidad, las soluciones de IA se vuelven más inclusivas, utilizables y beneficiosas para todos los usuarios.

### Agradable

Ser agradable significa que la aplicación es disfrutable de usar. Una experiencia de usuario atractiva puede tener un impacto positivo en el usuario, alentándolo a regresar a la aplicación y aumentando los ingresos del negocio.

![imagen que ilustra consideraciones de UX en IA](../../../translated_images/uxinai.d5b4ed690f5cefff0c53ffcc01b480cdc1828402e1fdbc980490013a3c50935a.es.png)

No todos los desafíos pueden resolverse con IA. La IA entra para mejorar tu experiencia de usuario, ya sea automatizando tareas manuales o personalizando experiencias de usuario.

## Diseñando Aplicaciones de IA para la Confianza y Transparencia

Construir confianza es fundamental al diseñar aplicaciones de IA. La confianza asegura que un usuario esté seguro de que la aplicación hará el trabajo, entregará resultados de manera consistente y los resultados son lo que el usuario necesita. Un riesgo en esta área es la desconfianza y la confianza excesiva. La desconfianza ocurre cuando un usuario tiene poca o ninguna confianza en un sistema de IA, esto lleva al usuario a rechazar tu aplicación. La confianza excesiva ocurre cuando un usuario sobreestima la capacidad de un sistema de IA, llevando a los usuarios a confiar demasiado en el sistema de IA. Por ejemplo, un sistema de calificación automatizado en el caso de confianza excesiva podría llevar al profesor a no revisar algunos de los trabajos para asegurar que el sistema de calificación funcione bien. Esto podría resultar en calificaciones injustas o inexactas para los estudiantes, o oportunidades perdidas para retroalimentación y mejora.

Dos formas de asegurar que la confianza esté en el centro del diseño son la explicabilidad y el control.

### Explicabilidad

Cuando la IA ayuda a informar decisiones como impartir conocimiento a futuras generaciones, es fundamental para los profesores y padres entender cómo se toman las decisiones de IA. Esto es explicabilidad: entender cómo las aplicaciones de IA toman decisiones. Diseñar para la explicabilidad incluye agregar detalles de ejemplos de lo que una aplicación de IA puede hacer. Por ejemplo, en lugar de "Comienza con el profesor de IA", el sistema puede usar: "Resume tus notas para una revisión más fácil usando IA."

![una página de aterrizaje de aplicación con ilustración clara de explicabilidad en aplicaciones de IA](../../../translated_images/explanability-in-ai.134426a96b498fbfdc80c75ae0090aedc0fc97424ae0734fccf7fb00a59a20d9.es.png)

Otro ejemplo es cómo la IA usa datos de usuario y personales. Por ejemplo, un usuario con la persona estudiante puede tener limitaciones basadas en su persona. La IA puede no ser capaz de revelar respuestas a preguntas pero puede ayudar a guiar al usuario a pensar cómo puede resolver un problema.

![IA respondiendo a preguntas basadas en persona](../../../translated_images/solving-questions.b7dea1604de0cbd2e9c5fa00b1a68a0ed77178a035b94b9213196b9d125d0be8.es.png)

Una última parte clave de la explicabilidad es la simplificación de explicaciones. Los estudiantes y profesores pueden no ser expertos en IA, por lo tanto, las explicaciones de lo que la aplicación puede o no puede hacer deben ser simplificadas y fáciles de entender.

![explicaciones simplificadas sobre capacidades de IA](../../../translated_images/simplified-explanations.4679508a406c3621fa22bad4673e717fbff02f8b8d58afcab8cb6f1aa893a82f.es.png)

### Control

La IA generativa crea una colaboración entre la IA y el usuario, donde por ejemplo un usuario puede modificar los prompts para obtener diferentes resultados. Además, una vez que se genera un output, los usuarios deben poder modificar los resultados dándoles una sensación de control. Por ejemplo, al usar Bing, puedes adaptar tu prompt basado en formato, tono y longitud. Además, puedes realizar cambios en tu output y modificar el resultado como se muestra a continuación:

![Resultados de búsqueda de Bing con opciones para modificar el prompt y el output](../../../translated_images/bing1.293ae8527dbe2789b675c8591c9fb3cb1aa2ada75c2877f9aa9edc059f7a8b1c.es.png)

Otra característica en Bing que permite a un usuario tener control sobre la aplicación es la capacidad de optar por participar o no en los datos que utiliza la IA. Para una aplicación escolar, un estudiante podría querer usar sus notas así como los recursos del profesor como material de revisión.

![Resultados de búsqueda de Bing con opciones para modificar el prompt y el output](../../../translated_images/bing2.309f4845528a88c28c1c9739fb61d91fd993dc35ebe6fc92c66791fb04fceb4d.es.png)

> Al diseñar aplicaciones de IA, la intencionalidad es clave para asegurar que los usuarios no confíen demasiado estableciendo expectativas poco realistas de sus capacidades. Una forma de hacer esto es creando fricción entre los prompts y los resultados. Recordándole al usuario que esto es IA y no un ser humano

## Diseñando Aplicaciones de IA para la Colaboración y Retroalimentación

Como se mencionó anteriormente, la IA generativa crea una colaboración entre el usuario y la IA. La mayoría de los compromisos son con un usuario ingresando un prompt y la IA generando un output. ¿Qué pasa si el output es incorrecto? ¿Cómo maneja la aplicación los errores si ocurren? ¿La IA culpa al usuario o se toma el tiempo para explicar el error?

Las aplicaciones de IA deben estar construidas para recibir y dar retroalimentación. Esto no solo ayuda al sistema de IA a mejorar, sino que también construye confianza con los usuarios. Un ciclo de retroalimentación debe estar incluido en el diseño, un ejemplo puede ser un simple pulgar hacia arriba o hacia abajo en el output.

Otra forma de manejar esto es comunicar claramente las capacidades y limitaciones del sistema. Cuando un usuario comete un error al solicitar algo más allá de las capacidades de la IA, también debe haber una forma de manejar esto, como se muestra a continuación.

![Dando retroalimentación y manejando errores](../../../translated_images/feedback-loops.7955c134429a94663443ad74d59044f8dc4ce354577f5b79b4bd2533f2cafc6f.es.png)

Los errores del sistema son comunes con aplicaciones donde el usuario podría necesitar asistencia con información fuera del alcance de la IA o la aplicación puede tener un límite en cuántas preguntas/temas un usuario puede generar resúmenes. Por ejemplo, una aplicación de IA entrenada con datos sobre temas limitados, por ejemplo, Historia y Matemáticas, puede no ser capaz de manejar preguntas sobre Geografía. Para mitigar esto, el sistema de IA puede dar una respuesta como: "Lo siento, nuestro producto ha sido entrenado con datos en los siguientes temas....., no puedo responder a la pregunta que hiciste."

Las aplicaciones de IA no son perfectas, por lo tanto, están destinadas a cometer errores. Al diseñar tus aplicaciones, debes asegurarte de crear espacio para retroalimentación de los usuarios y manejo de errores de una manera que sea simple y fácilmente explicable.

## Tarea

Toma cualquier aplicación de IA que hayas construido hasta ahora, considera implementar los siguientes pasos en tu aplicación:

- **Agradable:** Considera cómo puedes hacer tu aplicación más agradable. ¿Estás agregando explicaciones en todas partes? ¿Estás alentando al usuario a explorar? ¿Cómo estás redactando tus mensajes de error?

- **Usabilidad:** Construyendo una aplicación web. Asegúrate de que tu aplicación sea navegable tanto por mouse como por teclado.

- **Confianza y transparencia:** No confíes completamente en la IA y su output, considera cómo agregarías un humano al proceso para verificar el output. También considera e implementa otras formas de lograr confianza y transparencia.

- **Control:** Dale al usuario control de los datos que proporciona a la aplicación. Implementa una forma en que un usuario pueda optar por participar o no en la recopilación de datos en la aplicación de IA.

## ¡Continúa tu aprendizaje!

Después de completar esta lección, revisa nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA generativa.

Dirígete a la Lección 13, donde veremos cómo [asegurar aplicaciones de IA](../13-securing-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.