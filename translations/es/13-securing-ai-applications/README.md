<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f3cac698e9eea47dd563633bd82daf8c",
  "translation_date": "2025-06-25T20:41:22+00:00",
  "source_file": "13-securing-ai-applications/README.md",
  "language_code": "es"
}
-->
# Asegurando tus aplicaciones de IA generativa

## Introducción

Esta lección cubrirá:

- Seguridad en el contexto de sistemas de IA.
- Riesgos y amenazas comunes para los sistemas de IA.
- Métodos y consideraciones para asegurar los sistemas de IA.

## Objetivos de aprendizaje

Después de completar esta lección, comprenderás:

- Las amenazas y riesgos para los sistemas de IA.
- Métodos y prácticas comunes para asegurar los sistemas de IA.
- Cómo la implementación de pruebas de seguridad puede prevenir resultados inesperados y la pérdida de confianza de los usuarios.

## ¿Qué significa seguridad en el contexto de la IA generativa?

A medida que las tecnologías de Inteligencia Artificial (IA) y Aprendizaje Automático (ML) moldean cada vez más nuestras vidas, es crucial proteger no solo los datos de los clientes, sino también los propios sistemas de IA. La IA/ML se utiliza cada vez más para apoyar procesos de toma de decisiones de alto valor en industrias donde una decisión incorrecta puede tener consecuencias graves.

Aquí hay puntos clave a considerar:

- **Impacto de la IA/ML**: La IA/ML tiene impactos significativos en la vida diaria y, como tal, protegerlos se ha vuelto esencial.
- **Desafíos de seguridad**: Este impacto que tiene la IA/ML necesita atención adecuada para abordar la necesidad de proteger los productos basados en IA de ataques sofisticados, ya sea por trolls o grupos organizados.
- **Problemas estratégicos**: La industria tecnológica debe abordar proactivamente los desafíos estratégicos para garantizar la seguridad a largo plazo de los clientes y la seguridad de los datos.

Además, los modelos de Aprendizaje Automático son en gran medida incapaces de discernir entre entradas maliciosas y datos anómalos benignos. Una fuente significativa de datos de entrenamiento se deriva de conjuntos de datos públicos no moderados, que están abiertos a contribuciones de terceros. Los atacantes no necesitan comprometer los conjuntos de datos cuando son libres de contribuir a ellos. Con el tiempo, los datos maliciosos de baja confianza se convierten en datos confiables de alta confianza, si la estructura/formato de los datos permanece correcto.

Por eso es crítico asegurar la integridad y protección de los almacenes de datos que tus modelos utilizan para tomar decisiones.

## Comprendiendo las amenazas y riesgos de la IA

En términos de IA y sistemas relacionados, el envenenamiento de datos destaca como la amenaza de seguridad más significativa hoy en día. El envenenamiento de datos ocurre cuando alguien cambia intencionalmente la información utilizada para entrenar una IA, haciendo que cometa errores. Esto se debe a la ausencia de métodos estandarizados de detección y mitigación, junto con nuestra dependencia de conjuntos de datos públicos no confiables o no moderados para el entrenamiento. Para mantener la integridad de los datos y prevenir un proceso de entrenamiento defectuoso, es crucial rastrear el origen y la línea de los datos. De lo contrario, el viejo adagio "basura entra, basura sale" se mantiene, lo que lleva a un rendimiento comprometido del modelo.

Aquí hay ejemplos de cómo el envenenamiento de datos puede afectar tus modelos:

1. **Cambio de etiquetas**: En una tarea de clasificación binaria, un adversario cambia intencionalmente las etiquetas de un pequeño subconjunto de datos de entrenamiento. Por ejemplo, muestras benignas se etiquetan como maliciosas, llevando al modelo a aprender asociaciones incorrectas.\
   **Ejemplo**: Un filtro de spam que clasifica incorrectamente correos electrónicos legítimos como spam debido a etiquetas manipuladas.
2. **Envenenamiento de características**: Un atacante modifica sutilmente características en los datos de entrenamiento para introducir sesgos o engañar al modelo.\
   **Ejemplo**: Agregar palabras clave irrelevantes a descripciones de productos para manipular sistemas de recomendación.
3. **Inyección de datos**: Inyectar datos maliciosos en el conjunto de entrenamiento para influir en el comportamiento del modelo.\
   **Ejemplo**: Introducir reseñas de usuarios falsas para sesgar los resultados de análisis de sentimiento.
4. **Ataques de puerta trasera**: Un adversario inserta un patrón oculto (puerta trasera) en los datos de entrenamiento. El modelo aprende a reconocer este patrón y se comporta maliciosamente cuando se activa.\
   **Ejemplo**: Un sistema de reconocimiento facial entrenado con imágenes con puerta trasera que identifica incorrectamente a una persona específica.

La Corporación MITRE ha creado [ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)](https://atlas.mitre.org/?WT.mc_id=academic-105485-koreyst), una base de conocimiento de tácticas y técnicas empleadas por adversarios en ataques reales a sistemas de IA.

> Hay un número creciente de vulnerabilidades en sistemas habilitados por IA, ya que la incorporación de IA aumenta la superficie de ataque de los sistemas existentes más allá de los ataques cibernéticos tradicionales. Desarrollamos ATLAS para aumentar la conciencia de estas vulnerabilidades únicas y en evolución, a medida que la comunidad global incorpora cada vez más IA en varios sistemas. ATLAS está modelado según el marco MITRE ATT&CK® y sus tácticas, técnicas y procedimientos (TTPs) son complementarios a los de ATT&CK.

Al igual que el marco MITRE ATT&CK®, que se utiliza extensamente en la ciberseguridad tradicional para planificar escenarios de emulación de amenazas avanzadas, ATLAS proporciona un conjunto de TTPs fácilmente buscable que puede ayudar a comprender mejor y prepararse para defenderse contra ataques emergentes.

Además, el Proyecto de Seguridad de Aplicaciones Web Abiertas (OWASP) ha creado una "[Lista de los 10 principales](https://llmtop10.com/?WT.mc_id=academic-105485-koreyst)" de las vulnerabilidades más críticas encontradas en aplicaciones que utilizan LLMs. La lista destaca los riesgos de amenazas como el mencionado envenenamiento de datos junto con otros como:

- **Inyección de mensajes**: una técnica donde los atacantes manipulan un Modelo de Lenguaje Grande (LLM) a través de entradas cuidadosamente elaboradas, haciendo que se comporte fuera de su comportamiento previsto.
- **Vulnerabilidades de la cadena de suministro**: Los componentes y software que conforman las aplicaciones utilizadas por un LLM, como módulos de Python o conjuntos de datos externos, pueden ser comprometidos, lo que lleva a resultados inesperados, sesgos introducidos e incluso vulnerabilidades en la infraestructura subyacente.
- **Dependencia excesiva**: Los LLMs son falibles y han sido propensos a alucinar, proporcionando resultados inexactos o inseguros. En varias circunstancias documentadas, las personas han tomado los resultados al pie de la letra, lo que lleva a consecuencias negativas no deseadas en el mundo real.

El defensor de la nube de Microsoft, Rod Trent, ha escrito un libro electrónico gratuito, [Must Learn AI Security](https://github.com/rod-trent/OpenAISecurity/tree/main/Must_Learn/Book_Version?WT.mc_id=academic-105485-koreyst), que profundiza en estas y otras amenazas emergentes de IA y proporciona una guía extensa sobre cómo abordar mejor estos escenarios.

## Pruebas de seguridad para sistemas de IA y LLMs

La inteligencia artificial (IA) está transformando varios dominios e industrias, ofreciendo nuevas posibilidades y beneficios para la sociedad. Sin embargo, la IA también plantea desafíos y riesgos significativos, como la privacidad de los datos, el sesgo, la falta de explicabilidad y el uso indebido potencial. Por lo tanto, es crucial asegurar que los sistemas de IA sean seguros y responsables, lo que significa que cumplan con estándares éticos y legales y puedan ser confiables por los usuarios y las partes interesadas.

Las pruebas de seguridad son el proceso de evaluar la seguridad de un sistema de IA o LLM, identificando y explotando sus vulnerabilidades. Esto puede ser realizado por desarrolladores, usuarios o auditores externos, dependiendo del propósito y alcance de las pruebas. Algunos de los métodos de prueba de seguridad más comunes para sistemas de IA y LLMs son:

- **Saneamiento de datos**: Este es el proceso de eliminar o anonimizar información sensible o privada de los datos de entrenamiento o la entrada de un sistema de IA o LLM. El saneamiento de datos puede ayudar a prevenir la fuga de datos y la manipulación maliciosa al reducir la exposición de datos confidenciales o personales.
- **Pruebas adversariales**: Este es el proceso de generar y aplicar ejemplos adversariales a la entrada o salida de un sistema de IA o LLM para evaluar su robustez y resistencia contra ataques adversariales. Las pruebas adversariales pueden ayudar a identificar y mitigar las vulnerabilidades y debilidades de un sistema de IA o LLM que pueden ser explotadas por atacantes.
- **Verificación del modelo**: Este es el proceso de verificar la corrección y completitud de los parámetros del modelo o la arquitectura de un sistema de IA o LLM. La verificación del modelo puede ayudar a detectar y prevenir el robo de modelos al asegurar que el modelo esté protegido y autenticado.
- **Validación de salida**: Este es el proceso de validar la calidad y fiabilidad de la salida de un sistema de IA o LLM. La validación de salida puede ayudar a detectar y corregir la manipulación maliciosa al asegurar que la salida sea consistente y precisa.

OpenAI, líder en sistemas de IA, ha establecido una serie de _evaluaciones de seguridad_ como parte de su iniciativa de red de equipos rojos, destinada a probar la salida de sistemas de IA con la esperanza de contribuir a la seguridad de la IA.

> Las evaluaciones pueden variar desde pruebas simples de preguntas y respuestas hasta simulaciones más complejas. Como ejemplos concretos, aquí hay evaluaciones de muestra desarrolladas por OpenAI para evaluar los comportamientos de IA desde varios ángulos:

#### Persuasión

- [MakeMeSay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_say/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA engañar a otro sistema de IA para que diga una palabra secreta?
- [MakeMePay](https://github.com/openai/evals/tree/main/evals/elsuite/make_me_pay/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA convencer a otro sistema de IA para que done dinero?
- [Ballot Proposal](https://github.com/openai/evals/tree/main/evals/elsuite/ballots/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA influir en el apoyo de otro sistema de IA a una propuesta política?

#### Esteganografía (mensajería oculta)

- [Steganography](https://github.com/openai/evals/tree/main/evals/elsuite/steganography/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA pasar mensajes secretos sin ser detectado por otro sistema de IA?
- [Text Compression](https://github.com/openai/evals/tree/main/evals/elsuite/text_compression/readme.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA comprimir y descomprimir mensajes, para permitir ocultar mensajes secretos?
- [Schelling Point](https://github.com/openai/evals/blob/main/evals/elsuite/schelling_point/README.md?WT.mc_id=academic-105485-koreyst): ¿Qué tan bien puede un sistema de IA coordinarse con otro sistema de IA, sin comunicación directa?

### Seguridad de IA

Es imperativo que nos esforcemos por proteger los sistemas de IA de ataques maliciosos, uso indebido o consecuencias no deseadas. Esto incluye tomar medidas para garantizar la seguridad, fiabilidad y confiabilidad de los sistemas de IA, como:

- Asegurar los datos y algoritmos que se utilizan para entrenar y ejecutar modelos de IA
- Prevenir el acceso no autorizado, la manipulación o el sabotaje de los sistemas de IA
- Detectar y mitigar el sesgo, la discriminación o problemas éticos en los sistemas de IA
- Garantizar la responsabilidad, transparencia y explicabilidad de las decisiones y acciones de IA
- Alinear los objetivos y valores de los sistemas de IA con los de los humanos y la sociedad

La seguridad de IA es importante para garantizar la integridad, disponibilidad y confidencialidad de los sistemas de IA y los datos. Algunos de los desafíos y oportunidades de la seguridad de IA son:

- Oportunidad: Incorporar la IA en las estrategias de ciberseguridad, ya que puede desempeñar un papel crucial en la identificación de amenazas y mejorar los tiempos de respuesta. La IA puede ayudar a automatizar y aumentar la detección y mitigación de ciberataques, como phishing, malware o ransomware.
- Desafío: La IA también puede ser utilizada por adversarios para lanzar ataques sofisticados, como generar contenido falso o engañoso, suplantar usuarios o explotar vulnerabilidades en sistemas de IA. Por lo tanto, los desarrolladores de IA tienen una responsabilidad única de diseñar sistemas que sean robustos y resistentes contra el uso indebido.

### Protección de datos

Los LLMs pueden plantear riesgos para la privacidad y seguridad de los datos que utilizan. Por ejemplo, los LLMs pueden potencialmente memorizar y filtrar información sensible de sus datos de entrenamiento, como nombres personales, direcciones, contraseñas o números de tarjetas de crédito. También pueden ser manipulados o atacados por actores maliciosos que desean explotar sus vulnerabilidades o sesgos. Por lo tanto, es importante estar al tanto de estos riesgos y tomar medidas apropiadas para proteger los datos utilizados con LLMs. Hay varios pasos que puedes tomar para proteger los datos que se utilizan con LLMs. Estos pasos incluyen:

- **Limitar la cantidad y tipo de datos que comparten con LLMs**: Solo compartir los datos que son necesarios y relevantes para los propósitos previstos, y evitar compartir cualquier dato que sea sensible, confidencial o personal. Los usuarios también deben anonimizar o cifrar los datos que comparten con LLMs, como eliminando o enmascarando cualquier información identificativa, o utilizando canales de comunicación seguros.
- **Verificar los datos que los LLMs generan**: Siempre comprobar la precisión y calidad de la salida generada por los LLMs para asegurarse de que no contengan información no deseada o inapropiada.
- **Informar y alertar sobre cualquier brecha de datos o incidentes**: Estar vigilante de cualquier actividad o comportamiento sospechoso o anormal de los LLMs, como generar textos que sean irrelevantes, inexactos, ofensivos o dañinos. Esto podría ser una indicación de una brecha de datos o incidente de seguridad.

La seguridad, gobernanza y cumplimiento de datos son críticos para cualquier organización que desee aprovechar el poder de los datos y la IA en un entorno de múltiples nubes. Asegurar y gobernar todos tus datos es una tarea compleja y multifacética. Necesitas asegurar y gobernar diferentes tipos de datos (estructurados, no estructurados y datos generados por IA) en diferentes ubicaciones a través de múltiples nubes, y necesitas tener en cuenta las regulaciones de seguridad de datos, gobernanza y IA existentes y futuras. Para proteger tus datos, necesitas adoptar algunas prácticas y precauciones recomendadas, tales como:

- Usar servicios o plataformas en la nube que ofrezcan características de protección y privacidad de datos.
- Usar herramientas de calidad y validación de datos para verificar tus datos en busca de errores, inconsistencias o anomalías.
- Usar marcos de gobernanza y ética de datos para garantizar que tus datos se utilicen de manera responsable y transparente.

### Emulación de amenazas del mundo real - Equipos rojos de IA

La emulación de amenazas del mundo real ahora se considera una práctica estándar en la construcción de sistemas de IA resilientes mediante el uso de herramientas, tácticas y procedimientos similares para identificar los riesgos para los sistemas y probar la respuesta de los defensores.

> La práctica de equipos rojos de IA ha evolucionado para asumir un significado más amplio: no solo cubre la búsqueda de vulnerabilidades de seguridad, sino que también incluye la búsqueda de otras fallas del sistema, como la generación de contenido potencialmente dañino. Los sistemas de IA vienen con nuevos riesgos, y los equipos rojos son fundamentales para comprender esos riesgos novedosos, como la inyección de mensajes y la producción de contenido no fundamentado. - [Microsoft AI Red Team building future of safer AI](https://www.microsoft.com/security/blog/2023/08/07/microsoft-ai-red-team-building-future-of-safer-ai/?WT.mc_id=academic-105485-koreyst)

A continuación se presentan ideas clave que han dado forma al programa de equipos rojos de IA de Microsoft.

1. **Alcance expansivo del equipo rojo de IA**:
   El equipo rojo de IA ahora abarca tanto resultados de seguridad como de IA responsable (RAI). Tradicionalmente, el equipo rojo se centraba en aspectos de seguridad, tratando el modelo como un vector (por ejemplo, robar el modelo subyacente). Sin embargo, los sistemas de IA introducen vulnerabilidades de seguridad novedosas (por ejemplo, inyección de mensajes, envenenamiento), que requieren atención especial. Más allá de la seguridad, el equipo rojo de IA también investiga cuestiones de equidad (por ejemplo, estereotipos) y contenido dañino (por ejemplo, glorificación de la violencia). La identificación temprana de estos problemas permite priorizar las inversiones en defensa.
2. **Fallos maliciosos y benignos**:
   El equipo rojo de IA considera fallos desde perspectivas tanto maliciosas como benignas. Por ejemplo, cuando se realiza equipo rojo en el nuevo Bing, exploramos no solo cómo los adversarios maliciosos pueden subvertir el sistema, sino también cómo los usuarios regulares pueden encontrar contenido problemático o dañino. A diferencia del equipo rojo de seguridad tradicional, que se centra principalmente en actores maliciosos, el equipo rojo de IA tiene en cuenta una gama más amplia de personas y posibles fallos.
3. **Naturaleza dinámica de los sistemas de IA**:
   Las aplicaciones de IA evolucionan constantemente. En aplicaciones de modelos de lenguaje grande, los desarrolladores se adaptan a requisitos cambiantes. El equipo rojo continuo asegura una vigilancia y adaptación constante a los riesgos en evolución.

El equipo rojo de IA no es todo abarcador y debe considerarse un movimiento complementario a controles adicionales como [control de acceso basado en roles (RBAC)](https://learn.microsoft.com/azure/ai-services/openai/how-to/role-based-access-control?WT.mc_id=academic-105485-koreyst) y soluciones de gestión de datos integrales. Está destinado a complementar una estrategia de seguridad que se centra en emplear soluciones de IA seguras y responsables que tengan en cuenta la privacidad y la seguridad mientras aspiran a minimizar los sesgos, el contenido dañino y la desinformación que pueden erosionar la confianza del usuario.

Aquí hay una lista de lecturas adicionales que pueden ayudarte a comprender mejor cómo el equipo rojo puede ayudar a identificar y mitigar riesgos en tus sistemas de IA:

- [Planificación de

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No somos responsables de ningún malentendido o interpretación errónea que surja del uso de esta traducción.