# Desarrollo de aplicaciones de chat generativas con IA

[![Desarrollo de aplicaciones de chat generativas con IA](../../images/07-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lessons7-gh?WT.mc_id=academic-105485-koreyst)

> _(Haga clic en la imagen de arriba para ver el video de esta lección)_

Ahora que hemos visto cómo podemos crear aplicaciones de generación de texto, analicemos las aplicaciones de chat.

Las aplicaciones de chat se han integrado en nuestra vida diaria y ofrecen mucho más que una simple forma de conversar. Son parte integral de la atención al cliente, el soporte técnico e incluso de sistemas de asesoría sofisticados. Es probable que haya recibido ayuda de alguna aplicación de chat recientemente. A medida que integramos tecnologías más avanzadas, como la IA generativa, en estas plataformas, la complejidad aumenta, al igual que los desafíos.

Algunas preguntas que necesitamos responder son:

- **Desarrollo de la aplicación**. Cómo desarrollamos eficientemente e integramos fluidamente estas aplicaciones impulsadas por IA para casos de uso específicos?
- **Supervisión**. Una vez implementadas, cómo podemos supervisar y garantizar que las aplicaciones funcionen con la máxima calidad, tanto en términos de funcionalidad como de cumplimiento de los [seis principios de la IA responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst)?

A medida que avanzamos hacia una era definida por la automatización y las interacciones fluidas entre humanos y máquinas, comprender cómo la IA generativa transforma el alcance, la profundidad y la adaptabilidad de las aplicaciones de chat se vuelve esencial. Esta lección investigará los aspectos de la arquitectura que sustentan estos complejos sistemas, profundizará en las metodologías para optimizarlos para tareas específicas del dominio y evaluará las métricas y consideraciones pertinentes para garantizar una implementación responsable de la IA.

## Introducción

Esta lección abarca:

- Técnicas para desarrollar e integrar aplicaciones de chat de forma eficiente.
- Cómo aplicar la personalización y el ajuste preciso a las aplicaciones.
- Estrategias y consideraciones para supervisar eficazmente las aplicaciones de chat.

## Objetivos de aprendizaje

Al finalizar esta lección, podrá:

- Describir las consideraciones para desarrollar e integrar aplicaciones de chat en sistemas existentes.
- Personalizar las aplicaciones de chat para casos de uso específicos.
- Identificar las métricas y consideraciones clave para supervisar y mantener eficazmente la calidad de las aplicaciones de chat impulsadas por IA.
- Garantizar que las aplicaciones de chat utilicen la IA de forma responsable.

## Integración de la IA generativa en aplicaciones de chat

Mejorar las aplicaciones de chat mediante IA generativa no se centra solo en hacerlas más inteligentes, sino también en optimizar su arquitectura, rendimiento e interfaz de usuario para ofrecer una experiencia de usuario de calidad. Esto implica investigar los fundamentos arquitectónicos, las integraciones de API y las consideraciones de la interfaz de usuario. Esta sección tiene como objetivo ofrecerle una guía completa para navegar por estos entornos complejos, ya sea que las integre a sistemas existentes o las desarrolle como plataformas independientes.

Al finalizar esta sección, contará con la experiencia necesaria para construir e integrar aplicaciones de chat de forma eficiente.

### Chatbot o aplicación de chat?

Antes de profundizar en el desarrollo de aplicaciones de chat, comparemos los "chatbots" con las "aplicaciones de chat impulsadas por IA", que desempeñan funciones y roles distintos. El propósito principal de un chatbot es automatizar tareas conversacionales específicas, como responder preguntas frecuentes o hacer el seguimiento de un paquete. Generalmente se rige por lógica basada en reglas o algoritmos complejos de IA. En cambio, una aplicación de chat impulsada por IA es un entorno mucho más amplio, diseñado para facilitar diversas formas de comunicación digital, como chats de texto, voz y video entre usuarios. Su característica distintiva es la integración de un modelo de IA generativa que simula conversaciones con matices similares a las humanas, generando respuestas basadas en una amplia variedad de entradas y señales contextuales. Una aplicación de chat impulsada por IA generativa puede participar en debates de dominio abierto, adaptarse a contextos conversacionales cambiantes e incluso generar diálogos creativos o complejos.

La siguiente tabla describe las principales diferencias y similitudes para ayudarnos a comprender sus funciones únicas en la comunicación digital.

| Chatbot | Aplicación de chat generativa impulsada por IA |
| ------------------------------------- | -------------------------------------- |
| Centrado en tareas y basado en reglas | Consciente del contexto |
| A menudo integrado en sistemas más grandes | Puede albergar uno o varios chatbots |
| Limitado a funciones programadas | Incorpora modelos de IA generativa |
| Interacciones especializadas y estructuradas | Capaz de debates de dominio abierto |

### Aprovechar las funcionalidades predefinidas con SDK y API

Al crear una aplicación de chat, un buen primer paso es evaluar la disponibilidad. Usar SDK y API para crear aplicaciones de chat es una estrategia ventajosa por diversas razones. Al integrar SDK y API bien documentados, se posiciona estratégicamente la aplicación para el éxito a largo plazo, abordando las necesidades de escalabilidad y mantenimiento.

- **Acelera el proceso de desarrollo y reduce los gastos generales**: Confiar en funcionalidades predefinidas en lugar del costoso proceso de desarrollarlas uno mismo permite centrarse en otros aspectos de la aplicación que podrían ser más importantes, como la lógica de negocio.
- **Mejor rendimiento**: Al crear funcionalidades desde cero, con el tiempo se preguntará: "Cómo escala? Es esta aplicación capaz de gestionar una afluencia repentina de usuarios?". Los SDK y las API bien mantenidos suelen tener soluciones integradas para estos problemas. **Mantenimiento más sencillo**: Las actualizaciones y mejoras son más fáciles de gestionar, ya que la mayoría de las API y SDK simplemente requieren una actualización de una biblioteca cuando se lanza una versión más reciente.

**Acceso a tecnología de vanguardia**: Aprovechar modelos optimizados y entrenados con amplios conjuntos de datos proporciona a su aplicación capacidades de lenguaje natural.

Acceder a la funcionalidad de un SDK o API generalmente implica obtener permiso para usar los servicios proporcionados, lo que suele hacerse mediante una clave única o un token de autenticación. Usaremos la biblioteca de Python de OpenAI para explorar cómo funciona esto. También puede probarlo por su cuenta en el siguiente [notebook para OpenAI](../../python/oai-assignment.ipynb?WT.mc_id=academic-105485-koreyst) o [notebook para Azure OpenAI Services](../../python/aoai-assignment.ipynb?WT.mc_id=academic-105485-koreys) para esta lección.

```python
import os
from openai import OpenAI

API_KEY = os.getenv("OPENAI_API_KEY","")

client = OpenAI(
api_key=API_KEY
)

chat_completion = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Suggest two title for an instructive learning applications for generative IA."}])
```

El ejemplo anterior utiliza el modelo GPT-3.5 Turbo para completar la solicitud, pero tenga en cuenta que la clave API se configura antes de hacerlo. Recibirá un error si no la configura.

## Experiencia de usuario (UX)

Los principios generales de UX se aplican a las aplicaciones de chat, pero aquí hay algunas consideraciones adicionales que cobran especial importancia debido a los componentes de aprendizaje automático involucrados.

- **Mecanismo para abordar la ambigüedad**: Los modelos de IA generativa ocasionalmente generan respuestas ambiguas. Una función que permita a los usuarios solicitar aclaraciones puede ser útil si se encuentran con este problema.
- **Retención de contexto**: Los modelos de IA generativa avanzados tienen la capacidad de recordar el contexto dentro de una conversación, lo cual puede ser un activo esencial para la experiencia del usuario. Ofrecer a los usuarios la capacidad de controlar y gestionar el contexto mejora la experiencia del usuario, pero conlleva el riesgo de retener información confidencial. Considerar el tiempo que se almacena esta información, como implementar una política de retención, puede equilibrar la necesidad de contexto y la privacidad.
- **Personalización**: Gracias a su capacidad de aprendizaje y adaptación, los modelos de IA ofrecen una experiencia individualizada al usuario. Adaptar la experiencia del usuario mediante funciones como los perfiles de usuario no solo hace que el usuario se sienta comprendido, sino que también facilita su búsqueda de respuestas específicas, creando una interacción más eficiente y satisfactoria.

Un ejemplo de personalización es la configuración de "Instrucciones personalizadas" en ChatGPT de OpenAI. Te permite proporcionar información personal que puede ser un contexto importante para tus indicaciones. Aquí tienes un ejemplo de instrucción personalizada.

![Configuración de instrucciones personalizadas en ChatGPT](../../images/custom-instructions.png?WT.mc_id=academic-105485-koreyst)

Este "perfil" permite a ChatGPT crear un plan de lección en listas enlazadas. Ten en cuenta que ChatGPT tiene en cuenta que el usuario podría querer un plan de lección más detallado según su experiencia.

![Una solicitud en ChatGPT para un plan de lección sobre listas enlazadas](../../images/lesson-plan-prompt.png?WT.mc_id=academic-105485-koreyst)

### Marco de Mensajes del Sistema de Microsoft para Modelos de Lenguaje Grandes

[Microsoft ha proporcionado orientación](https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message#define-the-models-output-format?WT.mc_id=academic-105485-koreyst) para escribir mensajes del sistema eficaces al generar respuestas de LLM, divididas en 4 áreas:

1. Definir a quién va dirigido el modelo, así como sus capacidades y limitaciones.

2. Definir el formato de salida del modelo.

3. Proporcionar ejemplos específicos que demuestren el comportamiento previsto del modelo.

4. Proporcionar medidas de seguridad adicionales para el comportamiento.

### Accesibilidad

Independientemente de si un usuario tiene discapacidades visuales, auditivas, motoras o cognitivas, una aplicación de chat bien diseñada debe ser accesible para todos. La siguiente lista detalla características específicas diseñadas para mejorar la accesibilidad para diversas discapacidades.

- **Características para personas con discapacidad visual**: Temas de alto contraste y texto redimensionable, compatibilidad con lectores de pantalla.
- **Características para personas con discapacidad auditiva**: Funciones de texto a voz y de voz a texto, señales visuales para notificaciones de audio.
- **Características para personas con discapacidad motora**: Navegación con teclado, comandos de voz.
- **Características para personas con discapacidad cognitiva**: Opciones de idioma simplificadas.

## Personalización y ajuste para modelos de lenguaje específicos del dominio

Imagine una aplicación de chat que comprenda la jerga de su empresa y anticipe las consultas específicas que suelen tener sus usuarios. Hay un par de enfoques que vale la pena mencionar:

- **Aprovechamiento de modelos DSL**. DSL significa lenguaje específico de dominio. Puede aprovechar un modelo DSL entrenado en un dominio específico para comprender sus conceptos y escenarios.
- **Aplicar ajustes**. El ajuste es el proceso de entrenar aún más su modelo con datos específicos.

## Personalización: Uso de un DSL

Aprovechar un modelo de lenguaje específico de dominio (modelos DSL) puede mejorar la interacción del usuario al proporcionar interacciones especializadas y contextualmente relevantes. Se trata de un modelo entrenado o ajustado para comprender y generar texto relacionado con un campo, industria o tema específico. Las opciones para usar un modelo DSL pueden variar desde entrenarlo desde cero hasta usar modelos preexistentes mediante SDK y API. Otra opción es el ajuste, que implica adaptar un modelo preentrenado a un dominio específico.

## Personalización: Aplicar ajustes

A menudo se considera el ajuste cuando un modelo preentrenado presenta deficiencias en un dominio especializado o una tarea específica.

Por ejemplo, las consultas médicas son complejas y requieren mucho contexto. Cuando un profesional médico diagnostica a un paciente, se basa en diversos factores, como el estilo de vida o las condiciones preexistentes, e incluso puede basarse en publicaciones médicas recientes para validar su diagnóstico. En escenarios tan complejos, una aplicación de chat con IA de propósito general no puede ser una fuente confiable.

### Escenario: una aplicación médica
Considere una aplicación de chat diseñada para ayudar a los profesionales médicos, brindándoles referencias rápidas a guías de tratamiento, interacciones farmacológicas o hallazgos recientes de investigaciones.

Un modelo de propósito general podría ser adecuado para responder preguntas médicas básicas o brindar asesoramiento general, pero podría tener dificultades con lo siguiente:

- **Casos muy específicos o complejos**. Por ejemplo, un neurólogo podría preguntar a la aplicación: "Cuáles son las mejores prácticas actuales para el manejo de la epilepsia farmacorresistente en pacientes pediátricos?"
- **Falta de avances recientes**. Un modelo de propósito general podría tener dificultades para proporcionar una respuesta actualizada que incorpore los avances más recientes en neurología y farmacología.

En casos como estos, perfeccionar el modelo con un conjunto de datos médicos especializados puede mejorar significativamente su capacidad para gestionar estas complejas consultas médicas con mayor precisión y fiabilidad. Esto requiere acceso a un conjunto de datos amplio y relevante que represente los desafíos y las preguntas específicas del dominio que deben abordarse.

## Consideraciones para una experiencia de chat de alta calidad basada en IA

Esta sección describe los criterios para aplicaciones de chat de "alta calidad", que incluyen la captura de métricas prácticas y la adhesión a un marco que aprovecha responsablemente la tecnología de IA.

### Métricas Clave

Para mantener el rendimiento de alta calidad de una aplicación, es fundamental realizar un seguimiento de las métricas y consideraciones clave. Estas mediciones no solo garantizan la funcionalidad de la aplicación, sino que también evalúan la calidad del modelo de IA y la experiencia del usuario. A continuación, se incluye una lista que abarca las métricas básicas, de IA y de experiencia del usuario a considerar.

| Métrica | Definición | Consideraciones para el desarrollador de chat |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Tiempo de actividad** | Mide el tiempo que la aplicación está operativa y accesible para los usuarios. | Cómo se minimizará el tiempo de inactividad? |
| **Tiempo de respuesta** | El tiempo que tarda la aplicación en responder a la consulta de un usuario. | Cómo se puede optimizar el procesamiento de consultas para mejorar el tiempo de respuesta? |
| **Precisión** | La proporción de predicciones positivas verdaderas con respecto al número total de predicciones positivas | Cómo validará la precisión de su modelo? |
| **Recuperación (Sensibilidad)** | La proporción de predicciones positivas verdaderas con respecto al número real de positivas | Cómo medirá y mejorará la recuperación? |
| **Puntuación F1** | La media armónica de la precisión y la recuperación, que equilibra el equilibrio entre ambas. | Cuál es su puntuación F1 objetivo? Cómo equilibrará la precisión y la recuperación? |
| **Perplejidad** | Mide qué tan bien se alinea la distribución de probabilidad predicha por el modelo con la distribución real de los datos. | Cómo minimizará la perplejidad? |
| **Métricas de satisfacción del usuario** | Mide la percepción del usuario sobre la aplicación. A menudo se recopilan mediante encuestas. | Con qué frecuencia recopilará la opinión de los usuarios? Cómo se adaptará en función de ella? |
| **Tasa de error** | La tasa a la que el modelo comete errores de comprensión o de salida. | Qué estrategias implementas para reducir las tasas de error? |
| **Ciclos de reentrenamiento** | La frecuencia con la que se actualiza el modelo para incorporar nuevos datos e información. | Con qué frecuencia reentrenarás el modelo? Qué desencadena un ciclo de reentrenamiento? |
| **Detección de anomalías** | Herramientas y técnicas para identificar patrones inusuales que no se ajustan al comportamiento esperado. | Cómo responderás a las anomalías? |

### Implementación de prácticas responsables de IA en aplicaciones de chat

El enfoque de Microsoft para la IA Responsable ha identificado seis principios que deberían guiar el desarrollo y el uso de la IA. A continuación, se presentan los principios, su definición y los aspectos que un desarrollador de chat debe considerar y por qué debe tomarlos en serio.

| Principios | Definición de Microsoft | Consideraciones para el desarrollador de chat | Por qué es importante |
| ---------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Equidad | Los sistemas de IA deben tratar a todas las personas de forma justa. | Garantizar que la aplicación de chat no discrimine en función de los datos del usuario. | Generar confianza e inclusión entre los usuarios; evitar ramificaciones legales. |
| Fiabilidad y seguridad | Los sistemas de IA deben funcionar de forma fiable y segura. | Implementar pruebas y mecanismos de seguridad para minimizar errores y riesgos. | Garantizar la satisfacción del usuario y prevenir posibles daños. |
| Privacidad y seguridad | Los sistemas de IA deben ser seguros y respetar la privacidad. | Implementar medidas sólidas de cifrado y protección de datos. | Salvaguardar los datos confidenciales de los usuarios y cumplir con las leyes de privacidad. |
| Inclusión | Los sistemas de IA deben empoderar a todos e involucrar a las personas. | Diseñar una interfaz de usuario (UI)/experiencia de usuario (UX) accesible y fácil de usar para diversos públicos. | Garantiza que un mayor número de personas pueda usar la aplicación eficazmente. |
| Transparencia | Los sistemas de IA deben ser comprensibles. | Proporcionar documentación y razonamiento claros para las respuestas de la IA. | Es más probable que los usuarios confíen en un sistema si comprenden cómo se toman las decisiones. |
| Responsabilidad | Las personas deben ser responsables de los sistemas de IA. | Establecer un proceso claro para auditar y mejorar las decisiones de la IA. | Facilitar la mejora continua y las medidas correctivas en caso de errores. |

## Tarea

Consulta la [tarea](../../python?WT.mc_id=academic-105485-koreyst). Te guiará a través de una serie de ejercicios, desde la ejecución de tus primeras indicaciones de chat hasta la clasificación y resumen de texto, y más. Ten en cuenta que las tareas están disponibles en diferentes lenguajes de programación!

## Excelente trabajo! Continúa el viaje

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA generativa.

Dirígete a la Lección 8 para ver cómo puedes empezar a [crear aplicaciones de búsqueda](../../../08-building-search-applications/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst).