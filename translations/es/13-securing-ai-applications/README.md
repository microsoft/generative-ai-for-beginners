<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a2faf8ee7a0b851efa647a19788f1e5b",
  "translation_date": "2025-10-17T22:46:44+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "es"
}
-->
# Asegurando tus aplicaciones de IA generativa

[![Asegurando tus aplicaciones de IA generativa](../../../translated_images/13-lesson-banner.14103e36b4bbf17398b64ed2b0531f6f2c6549e7f7342f797c40bcae5a11862e.es.png)](https://youtu.be/m0vXwsx5DNg?si=TYkr936GMKz15K0L)

## Introducción

Esta lección cubrirá:

- La seguridad en el contexto de los sistemas de IA.
- Riesgos y amenazas comunes para los sistemas de IA.
- Métodos y consideraciones para asegurar los sistemas de IA.

## Objetivos de aprendizaje

Después de completar esta lección, comprenderás:

- Las amenazas y riesgos para los sistemas de IA.
- Métodos y prácticas comunes para asegurar los sistemas de IA.
- Cómo la implementación de pruebas de seguridad puede prevenir resultados inesperados y la pérdida de confianza de los usuarios.

## ¿Qué significa seguridad en el contexto de la IA generativa?

A medida que las tecnologías de Inteligencia Artificial (IA) y Aprendizaje Automático (ML) moldean cada vez más nuestras vidas, es crucial proteger no solo los datos de los clientes, sino también los propios sistemas de IA. La IA/ML se utiliza cada vez más en procesos de toma de decisiones de alto valor en industrias donde una decisión incorrecta puede tener consecuencias graves.

Aquí hay puntos clave a considerar:

- **Impacto de la IA/ML**: La IA/ML tiene impactos significativos en la vida diaria y, por lo tanto, protegerla se ha vuelto esencial.
- **Desafíos de seguridad**: Este impacto de la IA/ML requiere atención adecuada para abordar la necesidad de proteger los productos basados en IA de ataques sofisticados, ya sea por trolls o grupos organizados.
- **Problemas estratégicos**: La industria tecnológica debe abordar proactivamente los desafíos estratégicos para garantizar la seguridad a largo plazo de los clientes y la protección de los datos.

Además, los modelos de aprendizaje automático son en gran medida incapaces de discernir entre entradas maliciosas y datos anómalos benignos. Una fuente significativa de datos de entrenamiento se deriva de conjuntos de datos públicos no curados y no moderados, que están abiertos a contribuciones de terceros. Los atacantes no necesitan comprometer los conjuntos de datos cuando tienen la libertad de contribuir a ellos. Con el tiempo, los datos maliciosos de baja confianza se convierten en datos confiables de alta confianza, si la estructura/formato de los datos permanece correcto.

Por eso es fundamental garantizar la integridad y protección de los almacenes de datos que tus modelos utilizan para tomar decisiones.

## Comprendiendo las amenazas y riesgos de la IA

En términos de IA y sistemas relacionados, el envenenamiento de datos destaca como la amenaza de seguridad más significativa hoy en día. El envenenamiento de datos ocurre cuando alguien cambia intencionalmente la información utilizada para entrenar una IA, causando que cometa errores. Esto se debe a la ausencia de métodos estandarizados de detección y mitigación, junto con nuestra dependencia de conjuntos de datos públicos no confiables o no curados para el entrenamiento. Para mantener la integridad de los datos y prevenir un proceso de entrenamiento defectuoso, es crucial rastrear el origen y la procedencia de tus datos. De lo contrario, el viejo dicho "basura entra, basura sale" se cumple, lo que lleva a un rendimiento comprometido del modelo.

Aquí hay ejemplos de cómo el envenenamiento de datos puede afectar tus modelos:

1. **Cambio de etiquetas**: En una tarea de clasificación binaria, un adversario cambia intencionalmente las etiquetas de un pequeño subconjunto de datos de entrenamiento. Por ejemplo, muestras benignas se etiquetan como maliciosas, lo que lleva al modelo a aprender asociaciones incorrectas.\
   **Ejemplo**: Un filtro de spam que clasifica erróneamente correos legítimos como spam debido a etiquetas manipuladas.
2. **Envenenamiento de características**: Un atacante modifica sutilmente las características en los datos de entrenamiento para introducir sesgos o engañar al modelo.\
   **Ejemplo**: Agregar palabras clave irrelevantes a descripciones de productos para manipular sistemas de recomendación.
3. **Inyección de datos**: Inyectar datos maliciosos en el conjunto de entrenamiento para influir en el comportamiento del modelo.\
   **Ejemplo**: Introducir reseñas falsas de usuarios para sesgar los resultados del análisis de sentimientos.
4. **Ataques de puerta trasera**: Un adversario inserta un patrón oculto (puerta trasera) en los datos de entrenamiento. El modelo aprende a reconocer este patrón y actúa de manera maliciosa cuando se activa.\
   **Ejemplo**: Un sistema de reconocimiento facial entrenado con imágenes con puertas traseras que identifica erróneamente a una persona específica.

La Corporación MITRE ha creado [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), una base de conocimiento de tácticas y técnicas empleadas por adversarios en ataques reales a sistemas de IA.

> Hay un número creciente de vulnerabilidades en sistemas habilitados para IA, ya que la incorporación de IA aumenta la superficie de ataque de los sistemas existentes más allá de los ataques cibernéticos tradicionales. Desarrollamos ATLAS para aumentar la conciencia sobre estas vulnerabilidades únicas y en evolución, ya que la comunidad global incorpora cada vez más la IA en diversos sistemas. ATLAS está modelado según el marco MITRE ATT&CK® y sus tácticas, técnicas y procedimientos (TTPs) son complementarios a los de ATT&CK.

Al igual que el marco MITRE ATT&CK®, que se utiliza ampliamente en ciberseguridad tradicional para planificar escenarios avanzados de emulación de amenazas, ATLAS proporciona un conjunto de TTPs fácilmente buscables que pueden ayudar a comprender mejor y prepararse para defenderse de ataques emergentes.

Además, el Proyecto de Seguridad de Aplicaciones Web Abiertas (OWASP) ha creado una "[lista de los 10 principales](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" de las vulnerabilidades más críticas encontradas en aplicaciones que utilizan LLMs. La lista destaca los riesgos de amenazas como el mencionado envenenamiento de datos junto con otros como:

- **Inyección de prompts**: una técnica en la que los atacantes manipulan un Modelo de Lenguaje Extenso (LLM) mediante entradas cuidadosamente diseñadas, haciendo que se comporte fuera de su comportamiento previsto.
- **Vulnerabilidades en la cadena de suministro**: Los componentes y software que conforman las aplicaciones utilizadas por un LLM, como módulos de Python o conjuntos de datos externos, pueden estar comprometidos, lo que lleva a resultados inesperados, sesgos introducidos e incluso vulnerabilidades en la infraestructura subyacente.
- **Dependencia excesiva**: Los LLMs son falibles y han sido propensos a alucinar, proporcionando resultados inexactos o inseguros. En varias circunstancias documentadas, las personas han tomado los resultados al pie de la letra, lo que ha llevado a consecuencias negativas no deseadas en el mundo real.

Rod Trent, defensor de la nube de Microsoft, ha escrito un libro electrónico gratuito, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), que profundiza en estas y otras amenazas emergentes de la IA y proporciona una guía extensa sobre cómo abordar mejor estos escenarios.

## Pruebas de seguridad para sistemas de IA y LLMs

La inteligencia artificial (IA) está transformando diversos dominios e industrias, ofreciendo nuevas posibilidades y beneficios para la sociedad. Sin embargo, la IA también plantea desafíos y riesgos significativos, como la privacidad de los datos, el sesgo, la falta de explicabilidad y el posible mal uso. Por lo tanto, es crucial garantizar que los sistemas de IA sean seguros y responsables, lo que significa que cumplan con estándares éticos y legales y puedan ser confiables por usuarios y partes interesadas.

Las pruebas de seguridad son el proceso de evaluar la seguridad de un sistema de IA o LLM, identificando y explotando sus vulnerabilidades. Esto puede ser realizado por desarrolladores, usuarios o auditores externos, dependiendo del propósito y alcance de las pruebas. Algunos de los métodos de prueba de seguridad más comunes para sistemas de IA y LLMs son:

- **Saneamiento de datos**: Este es el proceso de eliminar o anonimizar información sensible o privada de los datos de entrenamiento o la entrada de un sistema de IA o LLM. El saneamiento de datos puede ayudar a prevenir fugas de datos y manipulaciones maliciosas al reducir la exposición de datos confidenciales o personales.
- **Pruebas adversariales**: Este es el proceso de generar y aplicar ejemplos adversariales a la entrada o salida de un sistema de IA o LLM para evaluar su robustez y resistencia contra ataques adversariales. Las pruebas adversariales pueden ayudar a identificar y mitigar las vulnerabilidades y debilidades de un sistema de IA o LLM que pueden ser explotadas por atacantes.
- **Verificación del modelo**: Este es el proceso de verificar la corrección y completitud de los parámetros o la arquitectura del modelo de un sistema de IA o LLM. La verificación del modelo puede ayudar a detectar y prevenir el robo de modelos asegurando que el modelo esté protegido y autenticado.
- **Validación de salida**: Este es el proceso de validar la calidad y confiabilidad de la salida de un sistema de IA o LLM. La validación de salida puede ayudar a detectar y corregir manipulaciones maliciosas asegurando que la salida sea consistente y precisa.

OpenAI, líder en sistemas de IA, ha establecido una serie de _evaluaciones de seguridad_ como parte de su iniciativa de red de equipos rojos, destinada a probar la salida de sistemas de IA con el objetivo de contribuir a la seguridad de la IA.

> Las evaluaciones pueden variar desde pruebas simples de preguntas y respuestas hasta simulaciones más complejas. Como ejemplos concretos, aquí hay evaluaciones de muestra desarrolladas por OpenAI para evaluar los comportamientos de la IA desde varios ángulos:

#### Persuasión

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA engañar a otro sistema de IA para que diga una palabra secreta?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA convencer a otro sistema de IA para que done dinero?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA influir en el apoyo de otro sistema de IA a una propuesta política?

#### Esteganografía (mensajes ocultos)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA pasar mensajes secretos sin ser detectado por otro sistema de IA?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA comprimir y descomprimir mensajes para permitir el ocultamiento de mensajes secretos?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA coordinarse con otro sistema de IA, sin comunicación directa?

### Seguridad en la IA

Es imperativo que nos esforcemos por proteger los sistemas de IA de ataques maliciosos, mal uso o consecuencias no deseadas. Esto incluye tomar medidas para garantizar la seguridad, confiabilidad y confianza en los sistemas de IA, tales como:

- Asegurar los datos y algoritmos que se utilizan para entrenar y ejecutar modelos de IA.
- Prevenir el acceso no autorizado, la manipulación o el sabotaje de los sistemas de IA.
- Detectar y mitigar sesgos, discriminación o problemas éticos en los sistemas de IA.
- Garantizar la responsabilidad, transparencia y explicabilidad de las decisiones y acciones de la IA.
- Alinear los objetivos y valores de los sistemas de IA con los de los humanos y la sociedad.

La seguridad en la IA es importante para garantizar la integridad, disponibilidad y confidencialidad de los sistemas de IA y los datos. Algunos de los desafíos y oportunidades de la seguridad en la IA son:

- Oportunidad: Incorporar la IA en estrategias de ciberseguridad, ya que puede desempeñar un papel crucial en la identificación de amenazas y la mejora de los tiempos de respuesta. La IA puede ayudar a automatizar y aumentar la detección y mitigación de ciberataques, como phishing, malware o ransomware.
- Desafío: La IA también puede ser utilizada por adversarios para lanzar ataques sofisticados, como generar contenido falso o engañoso, suplantar usuarios o explotar vulnerabilidades en los sistemas de IA. Por lo tanto, los desarrolladores de IA tienen una responsabilidad única de diseñar sistemas que sean robustos y resistentes contra el mal uso.

### Protección de datos

Los LLMs pueden representar riesgos para la privacidad y seguridad de los datos que utilizan. Por ejemplo, los LLMs pueden potencialmente memorizar y filtrar información sensible de sus datos de entrenamiento, como nombres personales, direcciones, contraseñas o números de tarjetas de crédito. También pueden ser manipulados o atacados por actores maliciosos que deseen explotar sus vulnerabilidades o sesgos. Por lo tanto, es importante ser consciente de estos riesgos y tomar medidas adecuadas para proteger los datos utilizados con los LLMs. Hay varios pasos que puedes tomar para proteger los datos que se utilizan con los LLMs. Estos pasos incluyen:

- **Limitar la cantidad y el tipo de datos que se comparten con los LLMs**: Comparte solo los datos que sean necesarios y relevantes para los propósitos previstos, y evita compartir cualquier dato que sea sensible, confidencial o personal. Los usuarios también deben anonimizar o cifrar los datos que comparten con los LLMs, como eliminar o enmascarar cualquier información identificativa, o utilizar canales de comunicación seguros.
- **Verificar los datos que generan los LLMs**: Siempre revisa la precisión y calidad de la salida generada por los LLMs para asegurarte de que no contengan información no deseada o inapropiada.
- **Reportar y alertar sobre cualquier brecha de datos o incidentes**: Mantente alerta ante cualquier actividad o comportamiento sospechoso o anormal de los LLMs, como generar textos que sean irrelevantes, inexactos, ofensivos o dañinos. Esto podría ser una indicación de una brecha de datos o incidente de seguridad.

La seguridad, gobernanza y cumplimiento de los datos son fundamentales para cualquier organización que desee aprovechar el poder de los datos y la IA en un entorno de múltiples nubes. Asegurar y gobernar todos tus datos es una tarea compleja y multifacética. Necesitas asegurar y gobernar diferentes tipos de datos (estructurados, no estructurados y datos generados por IA) en diferentes ubicaciones a través de múltiples nubes, y necesitas tener en cuenta las regulaciones existentes y futuras sobre seguridad, gobernanza y IA. Para proteger tus datos, debes adoptar algunas mejores prácticas y precauciones, como:

- Utilizar servicios o plataformas en la nube que ofrezcan características de protección y privacidad de datos.
- Usar herramientas de calidad y validación de datos para verificar tus datos en busca de errores, inconsistencias o anomalías.
- Utilizar marcos de gobernanza y ética de datos para garantizar que tus datos se utilicen de manera responsable y transparente.

### Emulando amenazas del mundo real - Equipos rojos de IA
Emular amenazas del mundo real ahora se considera una práctica estándar para construir sistemas de IA resilientes, empleando herramientas, tácticas y procedimientos similares para identificar los riesgos en los sistemas y probar la respuesta de los defensores.

> La práctica de red teaming en IA ha evolucionado para tener un significado más amplio: no solo abarca la búsqueda de vulnerabilidades de seguridad, sino también la identificación de otros fallos del sistema, como la generación de contenido potencialmente dañino. Los sistemas de IA presentan nuevos riesgos, y el red teaming es fundamental para comprender esos riesgos novedosos, como la inyección de prompts y la producción de contenido sin fundamento. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

[![Guía y recursos para red teaming](../../../translated_images/13-AI-red-team.642ed54689d7e8a4d83bdf0635768c4fd8aa41ea539d8e3ffe17514aec4b4824.es.png)]()

A continuación, se presentan ideas clave que han dado forma al programa de Red Team de IA de Microsoft.

1. **Alcance ampliado del Red Teaming en IA:**
   El red teaming en IA ahora abarca tanto resultados de seguridad como de IA Responsable (RAI). Tradicionalmente, el red teaming se centraba en aspectos de seguridad, tratando el modelo como un vector (por ejemplo, el robo del modelo subyacente). Sin embargo, los sistemas de IA introducen vulnerabilidades de seguridad novedosas (por ejemplo, inyección de prompts, envenenamiento), que requieren atención especial. Más allá de la seguridad, el red teaming en IA también investiga problemas de equidad (por ejemplo, estereotipos) y contenido dañino (por ejemplo, glorificación de la violencia). Identificar estos problemas de manera temprana permite priorizar las inversiones en defensa.
2. **Fallos maliciosos y benignos:**
   El red teaming en IA considera fallos desde perspectivas tanto maliciosas como benignas. Por ejemplo, al realizar red teaming en el nuevo Bing, exploramos no solo cómo los adversarios maliciosos pueden subvertir el sistema, sino también cómo los usuarios regulares pueden encontrarse con contenido problemático o dañino. A diferencia del red teaming de seguridad tradicional, que se centra principalmente en actores maliciosos, el red teaming en IA tiene en cuenta una gama más amplia de personas y posibles fallos.
3. **Naturaleza dinámica de los sistemas de IA:**
   Las aplicaciones de IA evolucionan constantemente. En las aplicaciones de modelos de lenguaje grande, los desarrolladores se adaptan a los requisitos cambiantes. El red teaming continuo asegura una vigilancia constante y adaptación a los riesgos en evolución.

El red teaming en IA no es exhaustivo y debe considerarse como un complemento a controles adicionales como [control de acceso basado en roles (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) y soluciones integrales de gestión de datos. Está destinado a complementar una estrategia de seguridad que se enfoque en emplear soluciones de IA seguras y responsables que consideren la privacidad y la seguridad, mientras aspiran a minimizar sesgos, contenido dañino y desinformación que puedan erosionar la confianza de los usuarios.

Aquí tienes una lista de lecturas adicionales que pueden ayudarte a comprender mejor cómo el red teaming puede identificar y mitigar riesgos en tus sistemas de IA:

- [Planificación de red teaming para modelos de lenguaje grande (LLMs) y sus aplicaciones](https://learn.microsoft.com/azure/ai-services/openai/concepts/red-teaming?WT.mc_id=academic-105485-koreyst)
- [¿Qué es la Red Teaming Network de OpenAI?](https://openai.com/blog/red-teaming-network?WT.mc_id=academic-105485-koreyst)
- [Red Teaming en IA - Una práctica clave para construir soluciones de IA más seguras y responsables](https://rodtrent.substack.com/p/ai-red-teaming?WT.mc_id=academic-105485-koreyst)
- MITRE [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), una base de conocimiento sobre tácticas y técnicas empleadas por adversarios en ataques reales a sistemas de IA.

## Verificación de conocimiento

¿Cuál podría ser un buen enfoque para mantener la integridad de los datos y prevenir el mal uso?

1. Tener controles sólidos basados en roles para el acceso y la gestión de datos  
1. Implementar y auditar el etiquetado de datos para prevenir la mala representación o el mal uso de los datos  
1. Asegurarse de que tu infraestructura de IA soporte el filtrado de contenido  

A:1, Aunque las tres son excelentes recomendaciones, asegurarte de asignar los privilegios de acceso adecuados a los usuarios será clave para prevenir la manipulación y la mala representación de los datos utilizados por los LLMs.

## 🚀 Desafío

Investiga más sobre cómo puedes [gobernar y proteger información sensible](https://learn.microsoft.com/training/paths/purview-protect-govern-ai/?WT.mc_id=academic-105485-koreyst) en la era de la IA.

## ¡Buen trabajo, continúa aprendiendo!

Después de completar esta lección, consulta nuestra [colección de aprendizaje sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA generativa.

Dirígete a la Lección 14, donde exploraremos [el ciclo de vida de las aplicaciones de IA generativa](../14-the-generative-ai-application-lifecycle/README.md?WT.mc_id=academic-105485-koreyst).

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.