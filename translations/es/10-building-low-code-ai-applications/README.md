# Construcción de Aplicaciones de IA de Bajo Código

[![Construcción de Aplicaciones de IA de Bajo Código](../../../translated_images/10-lesson-banner.png?WT.03212fed0693cf8837c727edc800942dbc5ef3a3036a8f7f399c6c08f6f59b92.es.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson10-gh?WT.mc_id=academic-105485-koreyst)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

## Introducción

Ahora que hemos aprendido a construir aplicaciones generadoras de imágenes, hablemos sobre el bajo código. La IA generativa se puede usar en varias áreas diferentes, incluyendo el bajo código, pero ¿qué es el bajo código y cómo podemos añadir IA a él?

La construcción de aplicaciones y soluciones se ha vuelto más fácil tanto para desarrolladores tradicionales como para no desarrolladores mediante el uso de Plataformas de Desarrollo de Bajo Código. Estas plataformas te permiten construir aplicaciones y soluciones con poco o ningún código, proporcionando un entorno de desarrollo visual que te permite arrastrar y soltar componentes. Esto te permite construir aplicaciones y soluciones más rápido y con menos recursos. En esta lección, profundizaremos en cómo usar el bajo código y cómo mejorar el desarrollo de bajo código con IA utilizando Power Platform.

Power Platform ofrece a las organizaciones la oportunidad de capacitar a sus equipos para construir sus propias soluciones a través de un entorno intuitivo de bajo código o sin código. Este entorno ayuda a simplificar el proceso de construcción de soluciones. Con Power Platform, las soluciones pueden construirse en días o semanas en lugar de meses o años. Power Platform consta de cinco productos clave: Power Apps, Power Automate, Power BI, Power Pages y Copilot Studio.

Esta lección cubre:

- Introducción a la IA Generativa en Power Platform
- Introducción a Copilot y cómo usarlo
- Uso de la IA Generativa para construir aplicaciones y flujos en Power Platform
- Comprensión de los Modelos de IA en Power Platform con AI Builder

## Objetivos de Aprendizaje

Al final de esta lección, podrás:

- Comprender cómo funciona Copilot en Power Platform.

- Construir una aplicación de seguimiento de tareas estudiantiles para nuestra startup educativa.

- Crear un flujo de procesamiento de facturas que use IA para extraer información de las facturas.

- Aplicar mejores prácticas al usar el modelo de IA para crear texto con GPT.

Las herramientas y tecnologías que usarás en esta lección son:

- **Power Apps**, para la aplicación de seguimiento de tareas estudiantiles, que proporciona un entorno de desarrollo de bajo código para construir aplicaciones que rastrean, gestionan e interactúan con datos.

- **Dataverse**, para almacenar los datos de la aplicación de seguimiento de tareas estudiantiles, donde Dataverse proporcionará una plataforma de datos de bajo código para almacenar los datos de la aplicación.

- **Power Automate**, para el flujo de procesamiento de facturas donde tendrás un entorno de desarrollo de bajo código para construir flujos de trabajo que automaticen el proceso de procesamiento de facturas.

- **AI Builder**, para el modelo de IA de procesamiento de facturas donde usarás modelos de IA preconstruidos para procesar las facturas de nuestra startup.

## IA Generativa en Power Platform

Mejorar el desarrollo y la aplicación de bajo código con IA generativa es un área clave de enfoque para Power Platform. El objetivo es permitir que todos construyan aplicaciones, sitios, paneles de control y procesos automatizados con IA, _sin requerir experiencia en ciencia de datos_. Este objetivo se logra integrando IA generativa en la experiencia de desarrollo de bajo código en Power Platform en forma de Copilot y AI Builder.

### ¿Cómo funciona esto?

Copilot es un asistente de IA que te permite construir soluciones de Power Platform describiendo tus requisitos en una serie de pasos conversacionales utilizando lenguaje natural. Por ejemplo, puedes instruir a tu asistente de IA para que indique qué campos usará tu aplicación y esta creará tanto la aplicación como el modelo de datos subyacente, o podrías especificar cómo configurar un flujo en Power Automate.

Puedes usar funcionalidades impulsadas por Copilot como una característica en las pantallas de tu aplicación para permitir a los usuarios descubrir información a través de interacciones conversacionales.

AI Builder es una capacidad de IA de bajo código disponible en Power Platform que te permite usar modelos de IA para ayudarte a automatizar procesos y predecir resultados. Con AI Builder puedes llevar IA a tus aplicaciones y flujos que se conectan a tus datos en Dataverse o en varias fuentes de datos en la nube, como SharePoint, OneDrive o Azure.

Copilot está disponible en todos los productos de Power Platform: Power Apps, Power Automate, Power BI, Power Pages y Power Virtual Agents. AI Builder está disponible en Power Apps y Power Automate. En esta lección, nos centraremos en cómo usar Copilot y AI Builder en Power Apps y Power Automate para construir una solución para nuestra startup educativa.

### Copilot en Power Apps

Como parte de Power Platform, Power Apps proporciona un entorno de desarrollo de bajo código para construir aplicaciones que rastrean, gestionan e interactúan con datos. Es un conjunto de servicios de desarrollo de aplicaciones con una plataforma de datos escalable y la capacidad de conectarse a servicios en la nube y datos locales. Power Apps te permite construir aplicaciones que funcionan en navegadores, tabletas y teléfonos, y pueden compartirse con compañeros de trabajo. Power Apps facilita a los usuarios el desarrollo de aplicaciones con una interfaz simple, para que cualquier usuario de negocios o desarrollador profesional pueda construir aplicaciones personalizadas. La experiencia de desarrollo de aplicaciones también se mejora con la IA Generativa a través de Copilot.

La función de asistente de IA Copilot en Power Apps te permite describir qué tipo de aplicación necesitas y qué información deseas que tu aplicación rastree, recopile o muestre. Copilot luego genera una aplicación Canvas receptiva basada en tu descripción. Luego puedes personalizar la aplicación para satisfacer tus necesidades. El asistente de IA Copilot también genera y sugiere una tabla de Dataverse con los campos que necesitas para almacenar los datos que deseas rastrear y algunos datos de muestra. Más adelante en esta lección, veremos qué es Dataverse y cómo puedes usarlo en Power Apps. Luego puedes personalizar la tabla para satisfacer tus necesidades usando la función de asistente de IA Copilot a través de pasos conversacionales. Esta función está disponible desde la pantalla de inicio de Power Apps.

### Copilot en Power Automate

Como parte de Power Platform, Power Automate permite a los usuarios crear flujos de trabajo automatizados entre aplicaciones y servicios. Ayuda a automatizar procesos comerciales repetitivos como la comunicación, la recopilación de datos y las aprobaciones de decisiones. Su interfaz simple permite a usuarios con diferentes niveles de competencia técnica (desde principiantes hasta desarrolladores experimentados) automatizar tareas laborales. La experiencia de desarrollo de flujos de trabajo también se mejora con la IA Generativa a través de Copilot.

La función de asistente de IA Copilot en Power Automate te permite describir qué tipo de flujo necesitas y qué acciones deseas que tu flujo realice. Copilot luego genera un flujo basado en tu descripción. Luego puedes personalizar el flujo para satisfacer tus necesidades. El asistente de IA Copilot también genera y sugiere las acciones que necesitas para realizar la tarea que deseas automatizar. Más adelante en esta lección, veremos qué son los flujos y cómo puedes usarlos en Power Automate. Luego puedes personalizar las acciones para satisfacer tus necesidades usando la función de asistente de IA Copilot a través de pasos conversacionales. Esta función está disponible desde la pantalla de inicio de Power Automate.

## Asignación: gestionar tareas estudiantiles y facturas para nuestra startup, usando Copilot

Nuestra startup ofrece cursos en línea a estudiantes. La startup ha crecido rápidamente y ahora tiene dificultades para mantenerse al día con la demanda de sus cursos. La startup te ha contratado como desarrollador de Power Platform para ayudarles a construir una solución de bajo código que les ayude a gestionar sus tareas estudiantiles y facturas. Su solución debería poder ayudarles a rastrear y gestionar las tareas estudiantiles a través de una aplicación y automatizar el proceso de procesamiento de facturas a través de un flujo de trabajo. Te han pedido que uses IA Generativa para desarrollar la solución.

Cuando comiences a usar Copilot, puedes usar la [Biblioteca de Prompts de Power Platform Copilot](https://github.com/pnp/powerplatform-prompts?WT.mc_id=academic-109639-somelezediko) para comenzar con los prompts. Esta biblioteca contiene una lista de prompts que puedes usar para construir aplicaciones y flujos con Copilot. También puedes usar los prompts en la biblioteca para obtener una idea de cómo describir tus requisitos a Copilot.

### Construir una Aplicación de Seguimiento de Tareas Estudiantiles para Nuestra Startup

Los educadores de nuestra startup han estado luchando para llevar un seguimiento de las tareas estudiantiles. Han estado usando una hoja de cálculo para rastrear las tareas, pero esto se ha vuelto difícil de gestionar a medida que ha aumentado el número de estudiantes. Te han pedido que construyas una aplicación que les ayude a rastrear y gestionar las tareas estudiantiles. La aplicación debería permitirles añadir nuevas tareas, ver tareas, actualizar tareas y eliminar tareas. La aplicación también debería permitir a los educadores y estudiantes ver las tareas que han sido calificadas y las que no.

Construirás la aplicación usando Copilot en Power Apps siguiendo los pasos a continuación:

1. Navega a la pantalla de inicio de [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

1. Usa el área de texto en la pantalla de inicio para describir la aplicación que deseas construir. Por ejemplo, **_Quiero construir una aplicación para rastrear y gestionar tareas estudiantiles_**. Haz clic en el botón **Enviar** para enviar el prompt al AI Copilot.

![Describe la aplicación que deseas construir](../../../translated_images/copilot-chat-prompt-powerapps.png?WT.30e5da1eee18fc179cbbe27b088aaa20d89624eaaed11a7750372ee8feb61af6.es.mc_id=academic-105485-koreyst)

1. El AI Copilot sugerirá una tabla de Dataverse con los campos que necesitas para almacenar los datos que deseas rastrear y algunos datos de muestra. Luego puedes personalizar la tabla para satisfacer tus necesidades usando la función de asistente de AI Copilot a través de pasos conversacionales.

   > **Importante**: Dataverse es la plataforma de datos subyacente para Power Platform. Es una plataforma de datos de bajo código para almacenar los datos de la aplicación. Es un servicio completamente gestionado que almacena datos de forma segura en la nube de Microsoft y se provisiona dentro de tu entorno de Power Platform. Viene con capacidades de gobernanza de datos integradas, como clasificación de datos, linaje de datos, control de acceso detallado y más. Puedes aprender más sobre Dataverse [aquí](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

   ![Campos sugeridos en tu nueva tabla](../../../translated_images/copilot-dataverse-table-powerapps.png?WT.d0158f12f6f02fdf31b4a056b0efbf5a64f49a2c2b6b9ea09b0f3a17d1189579.es.mc_id=academic-105485-koreyst)

1. Los educadores quieren enviar correos electrónicos a los estudiantes que han enviado sus tareas para mantenerlos actualizados sobre el progreso de sus tareas. Puedes usar Copilot para añadir un nuevo campo a la tabla para almacenar el correo electrónico del estudiante. Por ejemplo, puedes usar el siguiente prompt para añadir un nuevo campo a la tabla: **_Quiero añadir una columna para almacenar el correo electrónico del estudiante_**. Haz clic en el botón **Enviar** para enviar el prompt al AI Copilot.

![Añadiendo un nuevo campo](../../../translated_images/copilot-new-column.png?WT.18e16fce13f73236f484dc1b59e3d8e83a80c1cdf40854077a3dc800df76c560.es.mc_id=academic-105485-koreyst)

1. El AI Copilot generará un nuevo campo y luego puedes personalizar el campo para satisfacer tus necesidades.

1. Una vez que hayas terminado con la tabla, haz clic en el botón **Crear aplicación** para crear la aplicación.

1. El AI Copilot generará una aplicación Canvas receptiva basada en tu descripción. Luego puedes personalizar la aplicación para satisfacer tus necesidades.

1. Para que los educadores envíen correos electrónicos a los estudiantes, puedes usar Copilot para añadir una nueva pantalla a la aplicación. Por ejemplo, puedes usar el siguiente prompt para añadir una nueva pantalla a la aplicación: **_Quiero añadir una pantalla para enviar correos electrónicos a los estudiantes_**. Haz clic en el botón **Enviar** para enviar el prompt al AI Copilot.

![Añadiendo una nueva pantalla mediante una instrucción de prompt](../../../translated_images/copilot-new-screen.png?WT.afdf65429e4ef7b2eb58038fe91de6a3ebe7ca1d85e89c584efcb6da12abfdeb.es.mc_id=academic-105485-koreyst)

1. El AI Copilot generará una nueva pantalla y luego puedes personalizar la pantalla para satisfacer tus necesidades.

1. Una vez que hayas terminado con la aplicación, haz clic en el botón **Guardar** para guardar la aplicación.

1. Para compartir la aplicación con los educadores, haz clic en el botón **Compartir** y luego haz clic nuevamente en el botón **Compartir**. Luego puedes compartir la aplicación con los educadores ingresando sus direcciones de correo electrónico.

> **Tu tarea**: La aplicación que acabas de construir es un buen comienzo pero puede mejorarse. Con la función de correo electrónico, los educadores solo pueden enviar correos electrónicos a los estudiantes manualmente teniendo que escribir sus correos electrónicos. ¿Puedes usar Copilot para construir una automatización que permita a los educadores enviar correos electrónicos a los estudiantes automáticamente cuando envían sus tareas? Tu pista es que con el prompt adecuado puedes usar Copilot en Power Automate para construir esto.

### Construir una Tabla de Información de Facturas para Nuestra Startup

El equipo de finanzas de nuestra startup ha estado luchando para llevar un seguimiento de las facturas. Han estado usando una hoja de cálculo para rastrear las facturas, pero esto se ha vuelto difícil de gestionar a medida que ha aumentado el número de facturas. Te han pedido que construyas una tabla que les ayude a almacenar, rastrear y gestionar la información de las facturas que reciben. La tabla debería usarse para construir una automatización que extraiga toda la información de las facturas y la almacene en la tabla. La tabla también debería permitir al equipo de finanzas ver las facturas que han sido pagadas y las que no.

Power Platform tiene una plataforma de datos subyacente llamada Dataverse que te permite almacenar los datos para tus aplicaciones y soluciones. Dataverse proporciona una plataforma de datos de bajo código para almacenar los datos de la aplicación. Es un servicio completamente gestionado que almacena datos de forma segura en la nube de Microsoft y se provisiona dentro de tu entorno de Power Platform. Viene con capacidades de gobernanza de datos integradas, como clasificación de datos, linaje de datos, control de acceso detallado y más. Puedes aprender más [sobre Dataverse aquí](https://docs.microsoft.com/powerapps/maker/data-platform/data-platform-intro?WT.mc_id=academic-109639-somelezediko).

¿Por qué deberíamos usar Dataverse para nuestra startup? Las tablas estándar y personalizadas dentro de Dataverse proporcionan una opción de almacenamiento segura y basada en la nube para tus datos. Las tablas te permiten almacenar diferentes tipos de datos, similar a cómo podrías usar múltiples hojas de trabajo en un solo libro de Excel. Puedes usar tablas para almacenar datos que sean específicos para tu organización o necesidad empresarial. Algunos de los beneficios que nuestra startup obtendrá al usar Dataverse incluyen pero no se limitan a:

- **Fácil de gestionar**: Tanto los metadatos como los datos se almacenan en la nube, por lo que no tienes que preocuparte por los detalles de cómo se almacenan o gestionan. Puedes centrarte en construir tus aplicaciones y soluciones.

- **Seguro**: Dataverse proporciona una opción de almacenamiento segura y basada en la nube para tus datos. Puedes controlar quién tiene acceso a los datos en tus tablas y cómo pueden acceder a ellos utilizando seguridad basada en roles.

- **Ricos metadatos**: Los tipos de datos y las relaciones se usan directamente dentro de Power Apps.

- **Lógica y validación**: Puedes usar reglas de negocio, campos calculados y reglas de validación para aplicar lógica empresarial y mantener la precisión de los datos.

Ahora que sabes qué es Dataverse y por qué deberías usarlo, veamos cómo puedes usar Copilot para crear una tabla en Dataverse que cumpla con los requisitos de nuestro equipo de finanzas.

> **Nota**: Usarás esta tabla en la siguiente sección para construir una automatización que extraiga toda la información de las facturas y la almacene en la tabla.

Para crear una tabla en Dataverse usando Copilot, sigue los pasos a continuación:

1. Navega a la pantalla de inicio de [Power Apps](https://make.powerapps.com?WT.mc_id=academic-105485-koreyst).

2. En la barra de navegación izquierda, selecciona **Tablas** y luego haz clic en **Describir la nueva Tabla**.

   ![Seleccionar nueva tabla](../../../translated_images/describe-new-table.png?WT.1934e0de36f3fb613a023df3dcca89ba55f5d8d118e59b997d3f58e346f9e5db.es.mc_id=academic-105485-koreyst)

1. En la pantalla **Describir la nueva Tabla**, usa el área de texto para describir la tabla que deseas crear. Por ejemplo, **_Quiero crear una tabla para almacenar información de facturas_**. Haz clic en el botón **Enviar** para enviar el prompt al AI Copilot.

   ![Describe la tabla](../../../translated_images/copilot-chat-prompt-dataverse.png?WT.07979e2dd2a5c59cdd535f61e0dc2e0ce9d964189f70230e2a39ebb574a877cd.es.mc_id=academic-105485-koreyst)

1. El AI Copilot sugerirá una tabla de Dataverse con los campos que necesitas para almacenar los datos que deseas rastrear y algunos datos de muestra. Luego puedes personalizar la tabla para satisfacer tus necesidades usando la función de asistente de AI Copilot a través de pasos conversacionales.

   ![Tabla de Dataverse sugerida](../../../translated_images/copilot-dataverse-table.png?WT.45e9dc11cec7f53431fef3c849a45a5a0e52bdd3d621de57ff591f9af23aae38.es.mc_id=academic-105485-koreyst)

1. El equipo de finanzas quiere enviar un correo electrónico al proveedor para actualizarlos con el estado actual de su factura. Puedes usar Copilot para añadir un nuevo campo a la tabla para almacenar el correo electrónico del proveedor. Por ejemplo, puedes usar el siguiente prompt para añadir un nuevo campo a la tabla: **_Quiero añadir una columna para almacenar el correo electrónico del proveedor_**. Haz clic en el botón **Enviar** para enviar el prompt al AI Copilot.

1. El AI Copilot generará un nuevo campo y luego puedes personalizar el campo para satisfacer tus necesidades.

1. Una vez que hayas terminado con la tabla, haz clic en el botón **Crear** para crear la tabla.

## Modelos de IA en Power Platform con AI Builder

AI Builder es una capacidad de IA de bajo código disponible en Power Platform que te permite usar modelos de IA para ayudarte a automatizar procesos y predecir resultados. Con AI Builder puedes llevar IA a tus aplicaciones y flujos que se conectan a tus datos en Dataverse o en varias fuentes de datos en la nube, como SharePoint, OneDrive o Azure.

## Modelos de IA Preconstruidos vs Modelos de IA Personalizados

AI Builder proporciona dos tipos de modelos de IA: Modelos de IA Preconstruidos y Modelos de IA Personalizados. Los modelos de IA Preconstruidos son modelos de IA listos para usar que son entrenados por Microsoft y están disponibles en Power Platform. Estos te ayudan a añadir inteligencia a tus aplicaciones y flujos sin tener que recopilar datos y luego construir, entrenar y publicar tus propios modelos. Puedes usar
# Traducción del archivo Markdown

Este archivo está escrito en formato Markdown. Asegúrate de que la traducción no suene demasiado literal y de traducir los comentarios también. No traduzcas ningún [!NOTE], [!WARNING], [!TIP], [!IMPORTANT] o [!CAUTION]. No traduzcas entidades como nombres de variables, nombres de funciones, nombres de clases o marcadores de posición como @@INLINE_CODE_x@@ o @@CODE_BLOCK_x@@, pero mantenlos en el archivo. No traduzcas ninguna URL o ruta, pero mantenlas en el archivo. Escribe la salida de izquierda a derecha.

- **Análisis de Sentimientos**: Este modelo detecta sentimientos positivos, negativos, neutros o mixtos en el texto.
- **Lector de Tarjetas de Visita**: Este modelo extrae información de tarjetas de visita.
- **Reconocimiento de Texto**: Este modelo extrae texto de imágenes.
- **Detección de Objetos**: Este modelo detecta y extrae objetos de imágenes.
- **Procesamiento de Documentos**: Este modelo extrae información de formularios.
- **Procesamiento de Facturas**: Este modelo extrae información de facturas.

Con los Modelos de IA Personalizados puedes integrar tu propio modelo en AI Builder para que funcione como cualquier modelo personalizado de AI Builder, permitiéndote entrenar el modelo usando tus propios datos. Puedes usar estos modelos para automatizar procesos y predecir resultados tanto en Power Apps como en Power Automate. Al usar tu propio modelo, hay limitaciones que se aplican. Lee más sobre estas [limitaciones](https://learn.microsoft.com/ai-builder/byo-model#limitations?WT.mc_id=academic-105485-koreyst).

![Modelos de AI Builder](../../../translated_images/ai-builder-models.png?WT.6c2f6abc64cc07d27103364f2cd8c4689956e168da9f58cf75e6ca3fb459ec20.es.mc_id=academic-105485-koreyst)

## Asignación #2 - Construir un Flujo de Procesamiento de Facturas para Nuestra Startup

El equipo de finanzas ha estado teniendo dificultades para procesar facturas. Han estado usando una hoja de cálculo para rastrear las facturas, pero esto se ha vuelto difícil de manejar a medida que el número de facturas ha aumentado. Te han pedido que construyas un flujo de trabajo que les ayude a procesar facturas usando IA. El flujo de trabajo debe permitirles extraer información de las facturas y almacenar la información en una tabla de Dataverse. El flujo de trabajo también debe permitirles enviar un correo electrónico al equipo de finanzas con la información extraída.

Ahora que sabes qué es AI Builder y por qué deberías usarlo, veamos cómo puedes usar el Modelo de Procesamiento de Facturas de AI Builder, que cubrimos anteriormente, para construir un flujo de trabajo que ayude al equipo de finanzas a procesar facturas. Para construir un flujo de trabajo que ayude al equipo de finanzas a procesar facturas usando el Modelo de Procesamiento de Facturas de AI Builder, sigue los pasos a continuación:

1. Navega a la pantalla de inicio de [Power Automate](https://make.powerautomate.com?WT.mc_id=academic-105485-koreyst).
2. Usa el área de texto en la pantalla de inicio para describir el flujo de trabajo que deseas construir. Por ejemplo, **_Procesar una factura cuando llegue a mi buzón de correo_**. Haz clic en el botón **Enviar** para enviar el mensaje al AI Copilot.

![Copilot power automate](../../../translated_images/copilot-chat-prompt-powerautomate.png?WT.f6341b68d42f7c600e636c97f6874ec548ea3575906434e5caa9b7fbabd1c284.es.mc_id=academic-105485-koreyst)

3. El AI Copilot sugerirá las acciones que necesitas para realizar la tarea que deseas automatizar. Puedes hacer clic en el botón **Siguiente** para pasar a los siguientes pasos.
4. En el siguiente paso, Power Automate te pedirá que configures las conexiones requeridas para el flujo. Una vez que hayas terminado, haz clic en el botón **Crear flujo** para crear el flujo.
5. El AI Copilot generará un flujo y luego podrás personalizarlo para satisfacer tus necesidades.
6. Actualiza el disparador del flujo y establece la **Carpeta** en la carpeta donde se almacenarán las facturas. Por ejemplo, puedes establecer la carpeta en **Bandeja de entrada**. Haz clic en **Mostrar opciones avanzadas** y establece **Solo con Archivos Adjuntos** en **Sí**. Esto garantizará que el flujo solo se ejecute cuando se reciba un correo electrónico con un archivo adjunto en la carpeta.
7. Elimina las siguientes acciones del flujo: **HTML a texto**, **Componer**, **Componer 2**, **Componer 3** y **Componer 4** porque no las usarás.
8. Elimina la acción **Condición** del flujo porque no la usarás. Debería verse como la siguiente captura de pantalla:

![power automate, remove actions](../../../translated_images/powerautomate-remove-actions.png?WT.b7f06c5f7f24ed173de29f405e580c0bb414655560859cdbdf97b8c1803fe4c7.es.mc_id=academic-105485-koreyst)

9. Haz clic en el botón **Agregar una acción** y busca **Dataverse**. Selecciona la acción **Agregar una nueva fila**.
10. En la acción **Extraer Información de facturas**, actualiza el **Archivo de Factura** para apuntar al **Contenido del Archivo Adjunto** del correo electrónico. Esto garantizará que el flujo extraiga información del archivo adjunto de la factura.
11. Selecciona la **Tabla** que creaste anteriormente. Por ejemplo, puedes seleccionar la tabla **Información de Factura**. Elige el contenido dinámico de la acción anterior para llenar los siguientes campos:
    - ID
    - Monto
    - Fecha
    - Nombre
    - Estado
    - Establece el **Estado** en **Pendiente**.
    - Correo Electrónico del Proveedor
    - Usa el contenido dinámico **De** del disparador **Cuando llegue un nuevo correo electrónico**.

![power automate add row](../../../translated_images/powerautomate-add-row.png?WT.05f8f2c79ce95248eb173d6644436a1220f143991a5f0e647e15b922a0e1a290.es.mc_id=academic-105485-koreyst)

12. Una vez que hayas terminado con el flujo, haz clic en el botón **Guardar** para guardar el flujo. Luego puedes probar el flujo enviando un correo electrónico con una factura a la carpeta que especificaste en el disparador.

> **Tu tarea**: El flujo que acabas de construir es un buen comienzo, ahora necesitas pensar en cómo puedes construir una automatización que permita a nuestro equipo de finanzas enviar un correo electrónico al proveedor para actualizarlo con el estado actual de su factura. Tu pista: el flujo debe ejecutarse cuando el estado de la factura cambie.

## Usar un Modelo de IA de Generación de Texto en Power Automate

El Modelo de IA Crear Texto con GPT en AI Builder te permite generar texto basado en un mensaje y está impulsado por el Microsoft Azure OpenAI Service. Con esta capacidad, puedes incorporar la tecnología GPT (Transformador Generativo Pre-entrenado) en tus aplicaciones y flujos para construir una variedad de flujos automatizados y aplicaciones perspicaces.

Los modelos GPT se someten a un extenso entrenamiento con grandes cantidades de datos, lo que les permite producir texto que se asemeja mucho al lenguaje humano cuando se les proporciona un mensaje. Cuando se integran con la automatización de flujos de trabajo, los modelos de IA como GPT pueden aprovecharse para agilizar y automatizar una amplia gama de tareas.

Por ejemplo, puedes construir flujos para generar automáticamente texto para una variedad de casos de uso, como borradores de correos electrónicos, descripciones de productos y más. También puedes usar el modelo para generar texto para una variedad de aplicaciones, como chatbots y aplicaciones de servicio al cliente que permiten a los agentes de servicio al cliente responder de manera efectiva y eficiente a las consultas de los clientes.

![crear un mensaje](../../../translated_images/create-prompt-gpt.png?WT.7838e7bf32dee9636286569283c29f2a7cd58f2e2e093cee611dfa66db61a6ca.es.mc_id=academic-105485-koreyst)

Para aprender cómo usar este Modelo de IA en Power Automate, revisa el módulo [Agregar inteligencia con AI Builder y GPT](https://learn.microsoft.com/training/modules/ai-builder-text-generation/?WT.mc_id=academic-109639-somelezediko).

## ¡Buen Trabajo! Continúa con tu Aprendizaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA Generativa.

Dirígete a la Lección 11 donde veremos cómo [integrar IA Generativa con Llamadas a Funciones](../11-integrating-with-function-calling/README.md?WT.mc_id=academic-105485-koreyst).

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en IA. Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.