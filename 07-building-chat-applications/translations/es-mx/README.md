# Creando Aplicaciones de Chat Generativas Impulsadas por IA

[![Creando Aplicaciones de Chat Generativas Impulsadas por IA](../../images/07-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/Kw4i-tlKMrQ?WT.mc_id=academic-105485-koreyst)

> *(Haz clic en la imagen de arriba para ver el video de esta lección)*

Ahora que hemos visto cómo podemos crear aplicaciones de generación de texto, veamos las aplicaciones de chat.

Las aplicaciones de chat se han integrado en nuestra vida diaria, ofreciendo algo más que un medio para mantener una conversación informal. Son partes integrales del servicio al cliente, soporte técnico e incluso sistemas de consulta sofisticados. Es probable que hayas recibido ayuda de una aplicación de chat no hace mucho. A medida que integramos tecnologías más avanzadas como la IA generativa en estas plataformas, la complejidad aumenta y también los desafíos.

Algunas preguntas que necesitamos tener una respuesta son:

- **Construyendo la aplicación**. ¿Cómo construimos eficientemente e integramos sin problemas estas aplicaciones impulsadas por IA para casos de uso específicos?
- **Monitoreo**. Una vez implementadas, ¿cómo podemos monitorear y garantizar que las aplicaciones funcionen con el más alto nivel de calidad, tanto en términos de funcionalidad como de cumplimiento de los [seis principios de IA responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

A medida que avanzamos hacia una era definida por la automatización y las interacciones fluidas entre humanos y máquinas, comprender cómo la IA generativa transforma el alcance, la profundidad y la adaptabilidad de las aplicaciones de chat se vuelve esencial. Esta lección investigará los aspectos de la arquitectura que respaldan estos intrincados sistemas, profundizará en las metodologías para ajustarlos para tareas específicas de dominio y evaluará las métricas y consideraciones pertinentes para garantizar una implementación responsable de la IA.

## Introducción

Esta lección cubre:

- Técnicas para construir e integrar eficientemente aplicaciones de chat.
- Cómo aplicar personalización y fine-tuning a las aplicaciones.
- Estrategias y consideraciones para monitorear efectivamente las aplicaciones de chat.

## Metas de Aprendizaje

Al final de esta lección, serás capaz de:

- Describir consideraciones para construir e integrar aplicaciones de chat en sistemas existentes.
- Personalizar aplicaciones de chat para casos de uso específicos.
- Identificar métricas y consideraciones clave para monitorear y mantener de manera efectiva la calidad de las aplicaciones de chat impulsadas por IA.
- Garantizar que las aplicaciones de chat aprovechen la IA de forma responsable.

## Integrando la IA Generativa en Aplicaciones de Chat

Mejorar las aplicaciones de chat a través de la IA generativa no se centra solo en hacerlas más inteligentes; se trata de optimizar su arquitectura, rendimiento e interfaz de usuario para ofrecer una experiencia de usuario de calidad. Esto implica investigar los fundamentos arquitectónicos, las integraciones de API y las consideraciones de la interfaz de usuario. Esta sección tiene como objetivo ofrecerte una hoja de ruta integral para navegar por estos paisajes complejos, ya sea que los estés conectando a sistemas existentes o construyéndolos como plataformas independientes.

Al final de esta sección, estarás equipado con la experiencia necesaria para construir e incorporar aplicaciones de chat de manera eficiente.

### ¿Chatbot o Aplicación de Chat?

Antes de sumergirnos en la creación de aplicaciones de chat, comparemos los 'chatbots' contra las 'aplicaciones de chat impulsadas por IA', las cuales cumplen distintos roles y funcionalidades. El objetivo principal de un chatbot es automatizar tareas conversacionales específicas, tales como responder preguntas frecuentes o rastrear un paquete. Por lo general, se rige por una lógica basada en reglas o complejos algoritmos de IA. Por el contrario, una aplicación de chat impulsada por IA es un entorno mucho más amplio diseñado para facilitar diversas formas de comunicación digital, tales como chats de texto, voz y vídeo entre usuarios humanos. Su característica definitoria es la integración de un modelo de IA generativa que simula conversaciones matizadas y similares a las humanas, generando respuestas basadas en una amplia variedad de entradas y señales contextuales. Una aplicación de chat generativa impulsada por IA puede participar en debates de dominio abierto, adaptarse a contextos conversacionales en evolución e incluso producir diálogos creativos o complejos.

La siguiente tabla describe las diferencias y similitudes clave para ayudarnos a comprender sus funciones únicas en la comunicación digital.

| Chatbot                                      | Aplicación de Chat Generativa Impulsada por IA |
| -------------------------------------------- | ---------------------------------------------- |
| Centrado en tareas y basado en reglas        | Consciente del contexto                        |
| A menudo integrado en sistemas más grandes   | Puede alojar uno o varios chatbots             |
| Limitado a funciones programadas             | Incorpora modelos de IA generativa             |
| Interacciones especializadas y estructuradas | Capaz de mantener debates en dominio abierto   |

### Aprovechando las funcionalidades prediseñadas con SDKs y APIs

Al crear una aplicación de chat, un gran primer paso es evaluar lo que ya existe. El uso de SDKs y APIs para crear aplicaciones de chat es una estrategia ventajosa por diversas razones. Al integrar SDKs y APIs bien documentados, estás posicionando estratégicamente tu aplicación para el éxito a largo plazo, abordando los problemas de escalabilidad y mantenimiento.

- **Acelera el proceso de desarrollo y reduce los gastos generales**: Confiar en funcionalidades prediseñadas en lugar del costoso proceso de crearlas por tí mismo te permite centrarte en otros aspectos de tu aplicación que pueden resultarte más importantes, como la lógica empresarial.
- **Mejor rendimiento**: Al crear una funcionalidad desde cero, eventualmente te preguntarás "¿Cómo se escala? ¿Es esta aplicación capaz de manejar una afluencia repentina de usuarios?" Los SDKs y APIs bien mantenidos con frecuencia tienen soluciones integradas para estos problemas.
- **Mantenimiento más sencillo**: Las actualizaciones y mejoras son más fáciles de administrar ya que la mayoría de las APIs y SDKs simplemente requieren una actualización de una biblioteca cuando se lanza una versión más nueva.
- **Acceso a tecnología de vanguardia**: Aprovechar los modelos que han sido ajustados y entrenados en conjuntos de datos extensos proporciona a tu aplicación capacidades de lenguaje natural.

Acceder a la funcionalidad de un SDK o API generalmente implica obtener permiso para utilizar los servicios proporcionados, lo que a menudo se realiza mediante el uso de una clave única o un token de autenticación. Usaremos la Biblioteca OpenAI Python para explorar cómo se ve esto. También puedes probarlo por tu cuenta en el siguiente [notebook para OpenAI](../../notebook-openai.ipynb?WT.mc_id=academic-105485-koreyst) o [notebook para Servicios de Azure OpenAI](../../notebook-azure-openai.ipynb?WT.mc_id=academic-105485-koreys) para esta lección.

```python
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two titles for an instructional lesson on chat applications for generative AI."}])
```

El ejemplo anterior utiliza el modelo GPT-3.5 Turbo para completar el prompt, pero observa que la clave API está configurada antes de hacerlo. Recibirás el siguiente error si no configuró la clave.

```output
AuthenticationError: No API key provided. You can set your API key in code using 'openai.api_key = <API-KEY>', or you can set the environment variable OPENAI_API_KEY=<API-KEY>). If your API key is stored in a file, you can point the openai module at it with 'openai.api_key_path = <PATH>'. You can generate API keys in the OpenAI web interface. See https://platform.openai.com/account/api-keys for details.
```

## Experiencia de Usuario (UX)

Los principios generales de UX se aplican a las aplicaciones de chat, pero aquí hay algunas consideraciones adicionales que se vuelven particularmente importantes debido a los componentes de machine learning involucrados.

- **Mecanismo para abordar la ambigüedad**: Los modelos de IA Generativa ocasionalmente generan respuestas ambiguas. Una función que permite a los usuarios solicitar aclaraciones puede resultar útil si se encuentran con este problema.
- **Retención de contexto**: Los modelos avanzados de IA generativa tienen la capacidad de recordar el contexto dentro de una conversación, lo cual puede ser un activo necesario para la experiencia del usuario. Dar a los usuarios la capacidad de controlar y gestionar el contexto mejora la experiencia del usuario, pero introduce el riesgo de retener información confidencial del usuario. Las consideraciones sobre cuánto tiempo se almacena esta información, tales como la introducción de una política de retención, pueden equilibrar la necesidad de contexto contra la privacidad.
- **Personalización**: Con la capacidad de aprender y adaptarse, los modelos de IA ofrecen una experiencia individualizada para un usuario. Adaptar la experiencia del usuario a través de funciones como perfiles de usuario no solo hace que el usuario se sienta comprendido, sino que también le ayuda a encontrar respuestas específicas, creando una interacción más eficiente y satisfactoria.

Un ejemplo de personalización es la configuración de "Instrucciones Personalizadas" en ChatGPT de OpenAI. Te permite proporcionar información sobre tí que puede ser un contexto importante para tus prompts. A continuación se muestra un ejemplo de una instrucción personalizada.

![Configuración de Instrucciones Personalizadas en ChatGPT](../../images/custom-instructions.png?WT.mc_id=academic-105485-koreyst)

Este "perfil" solicita a ChatGPT crear un plan de lección en listas vinculadas. Nota que ChatGPT tiene en cuenta que el usuario puede querer un plan de lección más profundo basado en su experiencia.

![Un prompt en ChatGPT para un plan de lección sobre listas vinculadas](../../images/lesson-plan-prompt.png?WT.mc_id=academic-105485-koreyst)

### Marco de Trabajo de Mensajes de Sistema de Microsoft para Grandes Modelos de Lenguaje

[Microsoft ha proporcionado orientación](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para escribir mensajes de sistema eficaces al generar respuestas de LLMs, divididos en 4 áreas:

1. Definir a quién va dirigido el modelo, así como sus capacidades y limitaciones.
2. Definir el formato de salida del modelo.
3. Proporcionar ejemplos específicos que demuestren el comportamiento previsto del modelo.
4. Proporcionar barreras de comportamiento adicionales.

### Accesibilidad
 
 Ya sea que un usuario tenga discapacidades visuales, auditivas, motoras o cognitivas, una aplicación de chat bien diseñada debería poder ser utilizada por todos. La siguiente lista desglosa características específicas destinadas a mejorar la accesibilidad para diversas discapacidades de los usuarios.

- **Funciones para Discapacidad Visual**: Temas de alto contraste y texto redimensionable, compatibilidad con lectores de pantalla.
- **Funciones para Discapacidad Auditiva**: Funciones de texto a voz y de voz a texto, señales visuales para notificaciones de audio.
- **Funciones para Discapacidad Motora**: Soporte de navegación con teclado, comandos de voz.
- **Funciones para Deterioro Cognitivo**: Opciones de lenguaje simplificadas.

## Personalización y Fine-Tuning de Modelos de Lenguaje Específicos de Dominio

Imagina una aplicación de chat que comprenda la jerga de tu empresa y anticipe las consultas específicas que tu base de usuarios suele tener. Hay un par de enfoques que vale la pena mencionar:

- **Aprovechar modelos DSL**. DSL significa Lenguaje Específico de Dominio. Puedes aprovechar el llamado modelo DSL entrenado en un dominio específico para comprender sus conceptos y escenarios.
- **Aplicar fine-tuning**. Fine-tuning es el proceso de entrenar aún más tu modelo con datos específicos.

## Personalización: Uso de un DSL

Aprovechar los modelos de lenguaje de dominio específico (Modelos DSL) puede mejorar la participación del usuario y proporcionar interacciones especializadas y contextualmente relevantes. Es un modelo que está entrenado o afinado para comprender y generar texto relacionado con un campo, industria o tema específico. Las opciones para usar un modelo DSL pueden variar desde entrenar uno desde cero hasta usar modelos preexistentes a través de SDKs y APIs. Otra opción es el fine-tuning, que implica tomar un modelo pre-entrenado existente y adaptarlo a un dominio específico.

## Personalización: Aplicar fine-tuning

A menudo fine-tuning es considerado cuando un modelo pre-entrenado se queda corto en un dominio especializado o una tarea específica.

Por ejemplo, las consultas médicas son complejas y requieren mucho contexto. Cuando un profesional médico diagnostica a un paciente, se basa en una variedad de factores, tales como el estilo de vida o condiciones preexistentes, e incluso puede basarse en revistas médicas recientes para validar su diagnóstico. En escenarios tan matizados, una aplicación de chat de IA de propósito general no puede ser una fuente confiable.

### Escenario: una aplicación médica**

Considera una aplicación de chat diseñada para ayudar a los médicos practicantes brindándoles referencias rápidas a guías de tratamiento, interacciones con medicamentos o hallazgos de investigaciones recientes.

Un modelo de propósito general puede ser adecuado para responder preguntas médicas básicas o brindar consejos generales, pero puede tener dificultades con lo siguiente:

- **Casos muy específicos o complejos**. Por ejemplo, un neurólogo podría preguntar a la aplicación, "¿Cuáles son las mejores prácticas actuales para el tratamiento de la epilepsia farmacorresistente en pacientes pediátricos?"
- **Falta de avances recientes**. Un modelo de propósito general podría tener dificultades para proporcionar una respuesta actualizada que incorpore los avances más recientes en neurología y farmacología.

En casos como estos, afinar el modelo con un conjunto de datos médicos especializados puede mejorar significativamente su capacidad para manejar estas complejas consultas médicas de manera más precisa y confiable. Esto requiere acceso a un conjunto de datos grande y relevante que represente los desafíos y preguntas específicos del dominio que necesitan ser abordadas.

## Consideraciones para una Experiencia de Chat Impulsada por IA de Alta Calidad

Esta sección describe los criterios para aplicaciones de chat de "alta calidad", los cuales incluyen la captura de métricas procesables y el cumplimiento de un marco de trabajo que aproveche responsablemente la tecnología de IA.

### Métricas Clave

Para mantener el rendimiento de alta calidad de una aplicación, es esencial realizar un seguimiento de las métricas y consideraciones clave. Estas mediciones no sólo garantizan la funcionalidad de la aplicación, sino que también evalúan la calidad del modelo de IA y la experiencia del usuario. A continuación se muestra una lista que cubre métricas básicas, de IA y de experiencia del usuario a considerar.

| Métrica                        | Definición                                                                                                             | Consideraciones para el Desarrollador de Chat                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| **Tiempo de Actividad**        | Mide el tiempo que la aplicación está operativa y accesible por los usuarios.                                          | ¿Cómo minimizarás el tiempo de inactividad?                       |
| **Tiempo de Respuesta**        | El tiempo que tarda la aplicación en responder a la consulta de un usuario.                                            | ¿Cómo puedes optimizar el procesamiento de consultas para mejorar el tiempo de respuesta?           |
| **Precisión**                  | La proporción de predicciones positivas verdaderas con respecto al número total de predicciones positivas.             | ¿Cómo validarás la precisión de tu modelo?                        |
| **Exhaustividad (Sensibilidad)**    | La proporción de predicciones positivas verdaderas con respecto al número real de positivos.                     | ¿Cómo medirás y mejorarás la exhaustividad?                        |
| **Puntuación F1**                  | La media armónica de precisión y exhaustividad, que equilibra la compensación entre ambas.                        | ¿Cuál es tu Puntuación F1 objetivo? ¿Cómo equilibrarás la precisión y la exhaustividad?            |
| **Perplejidad**               | Mide qué tan bien se alinea la distribución de probabilidad predicha por el modelo con la distribución real de los datos. | ¿Cómo minimizarás la perplejidad?                               |
| **Métricas de Satisfacción del Usuario** | Mide la percepción del usuario de la aplicación. Con frecuencia se captura mediante encuestas.              | ¿Con qué frecuencia recopilarás la retroalimentación de los usuarios? ¿Cómo te adaptarás en base a ello? |
| **Tasa de Error**                | La tasa a la que el modelo comete errores de comprensión o de salida.                                               | ¿Qué estrategias tienes implementadas para reducir las tasas de error?                             |
| **Ciclos de Reentrenamiento**   | La frecuencia con la que el modelo es actualizado para incorporar nuevos datos y conocimientos                       | ¿Con qué frecuencia volverás a entrenar el modelo? ¿Qué desencadena un ciclo de reentrenamiento?   |
| **Detección de Anomalías**         | Herramientas y técnicas para identificar patrones inusuales que no se ajustan al comportamiento esperado.         | ¿Cómo responderás a las anomalías?                                 |

### Implementación de Prácticas de IA Responsable en Aplicaciones de Chat

El enfoque de Microsoft hacia la IA responsable ha identificado seis principios que deberían guiar el desarrollo y el uso de la IA. A continuación se detallan los principios, su definición y las cosas que un desarrollador de chat debería considerar y por qué deberían ser tomados en serio.

| Principios                | Definición de Microsoft                                                             | Consideraciones para el Desarrollador de Chat                                            | Por Qué Es Importante                                                               |
| ------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Equidad                   | Los sistemas de IA deberían tratar a todas las personas de manera justa.            | Asegúrate de que la aplicación de chat no discrimine según los datos del usuario.      | Generar confianza e inclusión entre los usuarios; evita ramificaciones legales.     |
| Confiabilidad y Seguridad | Los sistemas de IA deberían funcionar de forma confiable y segura.                  | Implementa pruebas y mecanismos de seguridad para minimizar errores y riesgos.          | Garantiza la satisfacción del usuario y previene posibles daños.                    |
| Privacidad y Seguridad    | Los sistemas de IA deberían ser seguros y respetar la privacidad.                   | Implementar fuertes medidas de encriptación y protección de datos.                      | Para salvaguardar los datos confidenciales de los usuarios y cumplir con las leyes de privacidad.         |
| Inclusión                 | Los sistemas de IA deberían empoderar a todos e involucrar a las personas.          | Diseña UI/UX que sea accesible y fácil de usar para audiencias diversas.        | Garantiza que una gama más amplia de personas pueda utilizar la aplicación de forma efectiva.             |
| Transparencia             | Los sistemas de IA deben ser comprensibles.                                         | Proporciona documentación y razonamiento claros para las respuestas de la IA.        | Es más probable que los usuarios confíen en un sistema si pueden comprender cómo se toman las decisiones. |
| Rendición de Cuentas      | Las personas deberían ser responsables de los sistemas de IA.                       | Establecer un proceso claro para auditar y mejorar las decisiones de IA.           | Permite la mejora continua y medidas correctivas en caso de errores.                |

## Tarea
 
Consulta la [tarea](../../notebook-azure-openai.ipynb?WT.mc_id=academic-105485-koreyst) que te llevará a través de una serie de ejercicios, desde ejecutar tus primeros prompts de chat hasta clasificar y resumir texto y más.

## Gran Trabajo, Continúa el Viaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 8 para ver cómo puedes comenzar a [construir aplicaciones de búsqueda](../../../08-building-search-applications/README.md?WT.mc_id=academic-105485-koreyst)!
