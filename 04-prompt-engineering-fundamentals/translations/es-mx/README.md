# Fundamentos de Prompt Engineering

[![Fundamentos de Prompt Engineering](../../images/04-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/r2ItK3UMVTk?WT.mc_id=academic-105485-koreyst)

La forma en que escribes tu prompt al LLM importa; un prompt cuidadosamente elaborado puede lograr un mejor resultado que uno que no lo sea. Pero, ¿qué son estos conceptos, prompt, prompt engineering y cómo puedo mejorar lo que envío al LLM? Preguntas como éstas son las que este capítulo y el próximo buscan responder.

La _IA Generativa_ es capaz de crear contenido nuevo (por ejemplo, texto, imágenes, audio, código, etc.) en respuesta a las solicitudes de los usuarios. Lo logra utilizando _Modelos de Lenguaje Grande_ (LLMs) como la serie GPT ("Transformador Generativo Pre-entrenado") de OpenAI que están entrenados para usar lenguaje y código natural.

Los usuarios ahora pueden interactuar con estos modelos utilizando paradigmas familiares como el chat, sin necesidad de experiencia técnica ni entrenamiento. Los modelos están _basados en prompts_- los usuarios envían una entrada de texto (prompt) y reciben la respuesta de la IA (finalización). Luego pueden "chatear con la IA" de forma iterativa, en conversaciones de varios turnos, refinando su prompt hasta que la respuesta coincida con sus expectativas.

Los "prompts" ahora se convierten en la principal _interfaz de programación_ para aplicaciones de IA generativa, indicando a los modelos qué hacer e influyendo en la calidad de las respuestas devueltas. "Prompt Engineering" es un campo de estudio de rápido crecimiento que se centra en el _diseño y optimización_ de prompts para ofrecer respuestas consistentes y de calidad a escala.

## Metas de Aprendizaje

En esta lección, aprenderemos qué es Prompt Engineering, por qué es importante y cómo podemos crear prompts más efectivos para un modelo y un objetivo de aplicación determinados. Comprenderemos los conceptos básicos y las mejores prácticas para prompt engineering y aprenderemos sobre un entorno "sandbox" interactivo de Jupyter Notebooks donde podemos ver estos conceptos aplicados a ejemplos reales.

Al final de esta lección seremos capaces de:

1. Explique qué es prompt engineering y por qué es importante.
2. Describir los componentes de un prompt y cómo se utilizan.
3. Aprender las mejores prácticas y técnicas para prompt engineering.
4. Aplicar las técnicas aprendidas a ejemplos reales, utilizando un punto de conexión de OpenAI.

## Sandbox de Aprendizaje

Prompt engineering es actualmente más un arte que una ciencia. La mejor manera de mejorar nuestra intuición es _practicar más_ y adoptar un enfoque de prueba y error que combine la experiencia en el dominio de la aplicación con técnicas recomendadas y optimizaciones específicas del modelo.

El Jupyter Notebook que acompaña a esta lección proporciona un entorno _sandbox_ donde puedes probar lo que aprendes - sobre la marcha, o como parte del desafío de código al final. Para ejecutar los ejercicios necesitarás:

1. Una clave API de Azure OpenAI - el punto de conexión de servicio para un LLM implementado.

2. Un runtime de Python - en el que se puede ejecutar el Notebook.

Hemos instrumentado este repositorio con un _contenedor de desarrollo_ que viene con un runtime de Python 3. Simplemente abre el repositorio en GitHub Codespaces o en tu Docker Desktop local para activar el runtime automáticamente. Luego abre el notebook y selecciona el kernel Python 3.x para preparar el Notebook para su ejecución.

El notebook predeterminado está configurado para usarse con un recurso del servicio Azure OpenAI. Simplemente copia el archivo `.env.copy` en la raíz de la carpeta a `.env` y actualiza las líneas `AZURE_OPENAI_API_KEY=` y `AZURE_OPENAI_API_ENDPOINT=` con tu clave API y punto de conexión. Puedes verificar tus credenciales en el [portal de Azure](https://portal.azure.com?WT.mc_id=academic-105485-koreyst), navegando a tu recurso Azure OpenAI y luego abriendo la pestaña _Claves y punto de conexión_ en el menú de la izquierda. Además, agrega el nombre que asignaste a tu modelo cuando creaste la implementación a la variable `AZURE_OPENAI_DEPLOYMENT`. El modelo recomendado para este ejercicio es 'gpt-35-turbo'.

El notebook viene con ejercicios _de inicio_ - pero te recomendamos que agregues tus propias secciones _Markdown_ (descripción) y _Código_ (solicitudes de prompts) para probar más ejemplos o ideas - y desarrollar tu intuición para diseñar de prompts.

## Nuestra Startup

Ahora, hablemos de cómo _este tema_ se relaciona con nuestra misión inicial de [llevar la innovación de la IA a la educación](https://educationblog.microsoft.com/2023/06/collaborating-to-bring-ai-innovation-to-education?WT.mc_id=academic-105485-koreyst). Queremos crear aplicaciones de _aprendizaje personalizado_ impulsadas por IA - así que pensemos en cómo los diferentes usuarios de nuestra aplicación podrían "diseñar" prompts:

- **Administradores** podrían pedirle a la IA que _analice los datos del plan de estudios para identificar brechas en la cobertura_. La IA puede resumir los resultados o visualizarlos con código.
- **Educadores** podrían pedirle a la IA que _genere un plan de lección para un público y un tema objetivo_. La IA puede crear el plan personalizado en un formato específico. 
- **Estudiantes** podrían pedirle a la IA que _les dé tutoría en un tema difícil_. La IA ahora puede guiar a los estudiantes con lecciones, consejos y ejemplos adaptados a su nivel.

Eso es sólo la punta del iceberg. Consulta [Prompts para la Educación](https://github.com/microsoft/prompts-for-edu/tree/main?WT.mc_id=academic-105485-koreyst) - una biblioteca de prompts de código abierto seleccionada por expertos en educación - para tener una idea más amplia de las posibilidades! _¡Intenta ejecutar algunos de esos prompts en el sandbox o usa OpenAI Playground para ver qué sucede!_

<!--
PLANTILLA DE LA LECCIÓN:
Esta unidad debería cubrir el concepto central #1.
Refuerza el concepto con ejemplos y referencias.

CONCEPTO #1:
Prompt Engineering.
Defínelo y explica por qué es necesario.
-->

## ¿Qué es Prompt Engineering?

Comenzamos esta lección definiendo **Prompt Engineering** como el proceso de _diseñar y optimizar_ entradas de texto (prompts) para ofrecer respuestas consistentes y de calidad (finalizaciones) para un objetivo y modelo de aplicación determinado. Podemos pensar en esto como un proceso de 2 pasos:

- _diseñar_ el prompt inicial para un modelo y objetivo determinado
- _refinar_ el prompt iterativamente para mejorar la calidad de la respuesta

Este es necesariamente un proceso de prueba y error que requiere la intuición del usuario y el esfuerzo para obtener resultados óptimos. Entonces, ¿por qué es importante? Para responder a esa pregunta, primero debemos entender tres conceptos:

- _Tokenización_ = cómo el modelo "ve" el prompt
- _LLMs base_ = cómo el modelo fundacional "procesa" un prompt
- _LLMs de Instrucciones Afinadas_ = cómo el modelo ahora puede ver "tareas"

### Tokenización

Un LLM considera a los prompts como una _sequencia de tokens_ donde diferentes modelos (o versiones de un modelo) pueden tokenizar el mismo prompt de diferentes maneras. Dado que los LLMs están entrenados en tokens (y no en texto sin procesar), la forma en que se tokenizan los prompts tiene un impacto directo en la calidad de la respuesta generada.

Para obtener una intuición sobre cómo funciona la tokenización, prueba herramientas como [OpenAI Tokenizer](https://platform.openai.com/tokenizer?WT.mc_id=academic-105485-koreyst) que se muestra a continuación. Copia tu prompt - y observa cómo eso se convierte en tokens, prestando atención a cómo se manejan los caracteres de espacios en blanco y los signos de puntuación. Ten en cuenta que este ejemplo muestra un LLM más antiguo (GPT-3), por lo que probar esto con un modelo más nuevo puede producir un resultado diferente.

![Tokenización](../../images/04-tokenizer-example.png?WT.mc_id=academic-105485-koreyst)

### Concepto: Modelos Fundacionales

Una vez que un prompt es tokenizado, la función principal del ["LLM Base"](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) (o Modelo Fundacional) es predecir el token en esa secuencia. Dado que los LLMs están entrenados en conjuntos de datos de texto masivos, tienen un buen sentido de las relaciones estadísticas entre los tokens y pueden hacer esa predicción con cierta confianza. Ten en cuenta que no entienden el _significado_ de las palabras en el prompt o token; solo ven un patrón que pueden "completar" con su próxima predicción. Pueden continuar prediciendo la secuencia hasta que se termine mediante la intervención del usuario o por alguna condición preestablecida.

¿Quieres ver cómo funciona la finalización basada en prompts? Ingresa el prompt anterior en Azure OpenAI Studio [_Chat Playground_](https://oai.azure.com/playground?WT.mc_id=academic-105485-koreyst) con la configuración predeterminada. El sistema está configurado para tratar los prompts como solicitudes de información - por lo que deberías ver una finalización que satisfaga este contexto.

Pero, ¿qué pasaría si el usuario quisiera ver algo específico que cumpliera algunos criterios u objetivos de la tarea? Aquí es donde los LLMS de _instrucciones afinadas_ entran en escena.

![Finalización de Chat de un LLM Base](../../images/04-playground-chat-base.png?WT.mc_id=academic-105485-koreyst)

### Concepto: LLMs de Instrucción Afinada

Un [LLM de Instrucción Afinada](https://blog.gopenai.com/an-introduction-to-base-and-instruction-tuned-large-language-models-8de102c785a6?WT.mc_id=academic-105485-koreyst) comienza con el modelo fundacional y lo afina con ejemplos o pares de entrada/salida (por ejemplo, "mensajes" de varios turnos) que pueden contener instrucciones claras - y la respuesta de la IA intenta seguir esa instrucción.

Esto utiliza técnicas como el Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF) que pueden entrenar al modelo a _seguir instrucciones_ y _aprender de la retroalimentación_ para que produzca respuestas que sean más adecuadas para aplicaciones prácticas y más relevantes para los objetivos del usuario.

Vamos a intentarlo - reutiliza el prompt anterior, pero ahora cambia el _mensaje de sistema_ para proporcionar la siguiente instrucción como contexto:

> _Summarize content you are provided with for a second-grade student. Keep the result to one paragraph with 3-5 bullet points._

¿Ves cómo ahora el resultado se ajusta para reflejar el objetivo y el formato deseados? Un educador ahora puede usar directamente esta respuesta en sus diapositivas para esa clase.

![Finalización de Chat de un LLM de Instrucción Afinada](../../images/04-playground-chat-instructions.png?WT.mc_id=academic-105485-koreyst)

## ¿Por qué necesitamos Prompt Engineering?

Ahora que sabemos cómo los prompts son procesados por los LLMs, hablemos de _por qué_ necesitamos prompt engineering. La respuesta radica en el hecho de que los LLMs actuales plantean una serie de desafíos que hacen que las _finalizaciones confiables y consistentes_ sean más difíciles de lograr sin esforzarse en una construcción y optimización del prompt. Por ejemplo:

1. **Las respuestas del modelo son estocásticas.** El _mismo prompt_ muy probablemente producirá diferentes respuestas con diferentes modelos o versiones de modelo. E incluso puede producir diferentes resultados con el _mismo_ modelo en diferentes momentos. _Las técnicas de Prompt engineering pueden ayudarnos a minimizar estas variaciones proporcionando mejores límites_.

2. **Los modelos pueden fabricar respuestas.** Los modelos son pre-entrenados con conjuntos de datos _grandes pero finitos_, lo que significa que carecen de conocimiento sobre conceptos fuera de ese alcance de entrenamiento. Como resultado, pueden producir finalizaciones que sean inexactas, imaginarias o directamente contradictorias con hechos conocidos. _Las técnicas de Prompt engineering ayudan a los usuarios a identificar y mitigar tales fabricaciones, por ejemplo, pidiendo a la IA citas o razonamiento_.

3. **Las capacidades de los modelos variarán.** Los modelos o generaciones de modelos más nuevas tendrán capacidades más enriquecidas, pero también traerán peculiaridades y compensaciones únicas en el costo y la complejidad. _Prompt engineering puede ayudarnos a desarrollar las mejores prácticas y flujos de trabajo que eliminen las diferencias y se adapten a los requisitos específicos del modelo en formas escalables y perfectas_.

Veamos esto en acción en el Playground de OpenAI o el de Azure OpenAI:

- Usa el mismo prompt con diferentes implementaciones de LLM (por ejemplo, OpenAI, Azure OpenAI, Hugging Face) - ¿Viste las variaciones?
- Usa el mismo prompt repetidamente con la _misma_ implementación de LLM (por ejemplo, Azure OpenAI Playground) - ¿Cómo diferían estas variaciones?

### Ejemplo de Fabricaciones

En este curso, utilizamos el término **"fabricación"** para hacer referencia al fenómeno donde los LLMs en ocasiones generan información factualmente incorrecta debido a limitaciones en su entrenamiento u otras restricciones. También puedes haber escuchado esto referido como _"alucinaciones"_ en artículos o trabajos de investigación populares. Sin embargo, recomendamos encarecidamente usar _"fabricación"_ como el término a fin de no antropomorfizar accidentalmente el comportamiento al atribuir un rasgo de un resultado humano a un resultado impulsado por una máquina. Esto también refuerza [las guías de IA Responsable](https://www.microsoft.com/ai/responsible-ai?WT.mc_id=academic-105485-koreyst) desde una perspectiva de terminología, eliminando términos que también pueden considerarse ofensivos o no inclusivos en algunos contextos.

¿Quieres tener una idea de cómo funcionan las fabricaciones? Piensa en un prompt que instruya a la IA a generar contenido para un tema inexistente (para asegurarse de que no se encuentre en el conjunto de datos de entrenamiento). Por ejemplo, probé este prompt:

> **Prompt:** generate a lesson plan on the Martian War of 2076.

Una búsqueda web me mostró que había cuentas ficticias (por ejemplo, series de televisión o libros) sobre guerras Marcianas - pero ninguna en 2076. El sentido común también nos dice que 2076 está _en el futuro_ y, por lo tanto, no puede ser asociado con un evento real.

Entonces, ¿qué sucede cuando ejecutamos este prompt con diferentes proveedores de LLM?

> **Respuesta 1**: OpenAI Playground (GPT-35)

![Respuesta 1](../../images/04-fabrication-oai.png?WT.mc_id=academic-105485-koreyst)

> **Respuesta 2**: Azure OpenAI Playground (GPT-35)

![Respuesta 2](../../images/04-fabrication-aoai.png?WT.mc_id=academic-105485-koreyst)

> **Respuesta 3**: : Hugging Face Chat Playground (LLama-2)

![Respuesta 3](../../images/04-fabrication-huggingchat.png?WT.mc_id=academic-105485-koreyst)

Como se esperaba, cada modelo (o versión del modelo) produce respuestas ligeramente diferentes gracias al comportamiento estocástico y las variaciones de capacidad del modelo. Por ejemplo, un modelo se dirige a una audiencia de 8º grado, mientras que el otro asume a un estudiante de bachillerato. Pero los tres modelos generaron respuestas que podrían convencer a un usuario desinformado de que el evento era real.

Las técnicas de Prompt engineering como _metaprompting_ y _configuración de temperatura_ pueden reducir las fabricaciones de modelos hasta cierto punto. Nuevas _arquitecturas_ de prompt engineering también incorporan nuevas herramientas y técnicas sin problemas en el flujo del prompt, para mitigar o reducir algunos de estos efectos.

## Caso de Estudio: GitHub Copilot

Concluyamos esta sección obteniendo una idea de cómo prompt engineering es usado en soluciones del mundo real observando un Caso de Estudio: [GitHub Copilot](https://github.com/features/copilot?WT.mc_id=academic-105485-koreyst).

GitHub Copilot es tu "Programador de Pares de IA" - convierte los prompts de texto en finalizaciones de código y está integrado en tu entorno de desarrollo (por ejemplo, Visual Studio Code) para una experiencia de usuario perfecta. Como se documenta en la serie de blogs mostrados a continuación, la primer versión se basó en el modelo OpenAI Codex - con los ingenieros dándose cuenta rápidamente de la necesidad de ajustar el modelo y desarrollar mejores técnicas de prompt engineering, para mejorar la calidad del código. En Julio, [debutaron un mejorado modelo de IA que va más allá del Codex](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst) para sugerencias aún más rápidas.

Lee las publicaciones en orden para seguir su viaje de aprendizaje.

- **Mayo 2023** | [GitHub Copilot se está Volviendo Mejor en Comprender Tu código](https://github.blog/2023-05-17-how-github-copilot-is-getting-better-at-understanding-your-code/?WT.mc_id=academic-105485-koreyst)
- **Mayo 2023** | [Dentro de GitHub: Trabajando con los LLMs detrás de GitHub Copilot](https://github.blog/2023-05-17-inside-github-working-with-the-llms-behind-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Junio 2023** | [Cómo escribir mejores prompts para GitHub Copilot](https://github.blog/2023-06-20-how-to-write-better-prompts-for-github-copilot/?WT.mc_id=academic-105485-koreyst).
- **Julio 2023** | [.. GitHub Copilot va más allá del Codex con un mejorado modelo de AI](https://github.blog/2023-07-28-smarter-more-efficient-coding-github-copilot-goes-beyond-codex-with-improved-ai-model/?WT.mc_id=academic-105485-koreyst)
- **Julio 2023** | [Una Guía del Desarrollador para Prompt Engineering y LLMs](https://github.blog/2023-07-17-prompt-engineering-guide-generative-ai-llms/?WT.mc_id=academic-105485-koreyst)
- **Septiembre 2023** | [Cómo crear una aplicación LLM empresarial: Lecciones de GitHub Copilot](https://github.blog/2023-09-06-how-to-build-an-enterprise-llm-application-lessons-from-github-copilot/?WT.mc_id=academic-105485-koreyst)

También puedes navegar por su [blog de Ingeniería](https://github.blog/category/engineering/?WT.mc_id=academic-105485-koreyst) para más publicaciones como [esta](https://github.blog/2023-09-27-how-i-used-github-copilot-chat-to-build-a-reactjs-gallery-prototype/?WT.mc_id=academic-105485-koreyst) que muestra cómo estos modelos y técnicas son _aplicados_ para dirigir aplicaciones del mundo real.

---

<!--
PLANTILLA DE LA LECCIÓN:
Esta unidad debería cubrir el concepto central #2.
Refuerza el concepto con ejemplos y referencias.

CONCEPTO #2:
Diseño de Prompts.
Ilustrado con ejemplos.
-->

## Construcción de Prompts

Hemos visto por qué prompt engineering es importante - ahora comprendamos cómo los prompts son _construidos_ a fin de poder evaluar diferentes técnicas para un diseño de prompts más efectivo.

### Prompt Básico

Comencemos con el prompt básico: una entrada de texto enviada al modelo sin ningún contexto. Aquí hay un ejemplo - cuando enviamos las primeras palabras del himno nacional de Estados Unidos al [API de Completions](https://platform.openai.com/docs/api-reference/completions?WT.mc_id=academic-105485-koreyst) de OpenAI, instantáneamente _completa_ la respuesta con las siguientes líneas, ilustrando el comportamiento básico de predicción.

| Prompt (Entrada)     | Finalización (Salida)                                                                                                                        |
| :------------------- | :------------------------------------------------------------------------------------------------------------------------------------------- |
| Oh say can you see   | It sounds like you're starting the lyrics to "The Star-Spangled Banner," the national anthem of the United States. The full lyrics are ...   |

### Prompt Complejo

Ahora agregemos contexto e instrucciones a ese prompt básico. El [API de Chat Completion](https://learn.microsoft.com/azure/ai-services/openai/how-to/chatgpt?WT.mc_id=academic-105485-koreyst) nos permite construir un prompt complejo como una colección de _mensajes_ com:

- Pares de entrada/salida que reflejan la entrada del _usuario_ y la respuesta del _asistente_.
- Mensaje del sistema que establece el contexto para el comportamiento o la personalidad del asistente.

La solicitud ahora está en el formulario mostrado a continuación, donde la _tokenización_ captura efectivamente información relevante del contexto y la conversación. Ahora, cambiar el contexto del sistema puede ser tan impactante en la calidad de las finalizaciones como las entradas del usuario proporcionadas.

```python
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Eres un asistente útil."},
        {"role": "user", "content": "¿Quién ganó la Serie Mundial en 2020?"},
        {"role": "assistant", "content": "Los Angeles Dodgers ganaron la Serie Mundial en 2020."},
        {"role": "user", "content": "¿Dónde se jugó?"}
    ]
)
```

### Prompt de Instrucción

En los ejemplos anteriores, el prompt del usuario era una consulta de texto simple que puede interpretarse como una solicitud de información. Con los prompts de _instrucción_, podemos usar ese texto para especificar una tarea con más detalle, proporcionando una mejor orientación a la IA. Aquí hay un ejemplo:

| Prompt (Entrada)                                                                                                                                                                                                                         | Finalización (Salida)                                                                                                        | Tipo de Instrucción    |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| Escribe una descripción de la Guerra Civil                                                                                                                                                                                                   | _devolvió un párrafo simple_                                                                                              | Simple              |
| Escribe una descripción de la Guerra Civil. Proporciona fechas y eventos clave y describe su importancia.                                                                                                                                      | _devolvió un párrafo seguido de una lista de fechas de eventos clave con descripciones_                                             | Complejo             |
| Escribe una descripción de la Guerra Civil en 1 párrafo. Proporciona 3 viñetas con fechas clave y su significado. Proporciona 3 viñetas más con figuras históricas clave y sus contribuciones. Devuelve el resultado como un archivo JSON. | _devolvió detalles más extensos en un cuadro de texto, formateado como JSON que puedes copiar y pegar a un archivo y validar según sea necesario_ | Complejo. Formateado. |

## Contenido Principal

En los ejemplos anteriores, el prompt todavía estaba bastante abierto, lo que permitió que el LLM decidiera qué parte de su conjunto de datos pre-entrenado era relevante. Con el patrón de diseño _contenido principal_, el texto de entrada se divide en dos partes:

- una instrucción (acción)
- contenido relevante (que influye en la acción)

Aquí hay un ejemplo en el que la instrucción es "resumir esto en 2 oraciones".

| Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Finalización (Salida)                                                                                                                                                                                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Júpiter es el quinto planeta a partir del Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del sol, pero dos veces y media más que la de todos los demás planetas en el Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. Recibe su nombre del dios romano Júpiter.[19] Cuando se observa desde la Tierra, Júpiter puede ser lo suficientemente brillante como para que su luz reflejada proyecte sombras visibles,[20] y es en promedio el tercer objeto natural más brillante en el cielo nocturno después de la Luna y Venus. <br/> **Resume esto en 2 oraciones cortas** | Júpiter, el quinto planeta a partir del Sol, es el más grande del Sistema Solar y es conocido por ser uno de los objetos más brillantes del cielo nocturno. Llamado así por el dios romano Júpiter, es un gigante gaseoso cuya masa es dos veces y media la de todos los demás planetas del Sistema Solar juntos. |

El segmento de contenido primario se puede utilizar de varias maneras para impulsar instrucciones más efectivas:

- **Ejemplos** - en lugar de decirle al modelo qué hacer con una instrucción explícita, dale ejemplos de qué hacer y déjalo que infiera el patrón.
- **Señales** - acompaña la instrucción con una "señal" que prepare la finalización, guiando el modelo hacia respuestas más relevantes.
- **Plantillas** - estas son 'recetas' repetibles para prompts con marcadores de posición (variables) que pueden personalizarse con datos para casos de uso específicos.

Veámoslos en acción.

### Usando Ejemplos

Este es un enfoque en el que usas el contenido principal para "alimentar el modelo" con algunos ejemplos de la salida deseada para una instrucción dada, dejando así que infiera el patrón para la salida deseada. Según el número de ejemplos proporcionados, podemos tener zero-shot prompting, one-shot prompting, few-shot prompting, etc.

El prompt ahora consta de tres componentes:

- La descripción de una tarea
- Unos cuantos ejemplos de la salida deseada
- El inicio de un nuevo ejemplo (el cual se convierte en una descripción implícita de la tarea) 

| Tipo de Aprendizaje | Prompt (Entrada)                                                                                                                                        | Finalización (Salida)         |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------- |
| Zero-shot     | "The Sun is Shining". Translate to Spanish                                                                                                            | "El Sol está brillando".    |
| One-shot      | "The Sun is Shining" => ""El Sol está brillando". <br> "It's a Cold and Windy Day" =>                                                                 | "Es un día frío y ventoso". |
| Few-shot      | The player ran the bases => Baseball <br/> The player hit an ace => Tennis <br/> The player hit a six => Cricket <br/> The player made a slam-dunk => | Basketball                  |
|               |                                                                                                                                                       |                             |

Observa cómo tuvimos que proporcionar instrucción explícita ("Translate to Spanish") en zero-shot prompting, pero dicha tarea es inferida en el ejemplo de one-shot prompting. El ejemplo de few-shot prompting muestra cómo agregar más ejemplos permite a los modelos hacer inferencias más precisas sin instrucciones adicionales.

### Señales de Prompt

Otra técnica para usar contenido primario es proporcionar _señales_ en lugar de ejemplos. En este caso, estamos dando al modelo un empujón en la dirección correcta al _inicializarlo_ con un fragmento que refleja el formato de respuesta deseado. El modelo luego "toma la señal" para continuar en esa línea.

| Número de Señales | Prompt (Entrada)                                                                                                                                                                                                                                                                                                                                                                                                                                               | Finalización (Salida)                                                                                                                                                                                                                                                                                       |
| :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0              | Júpiter es el quinto planeta a partir del Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del sol, pero dos veces y media más que la de todos los demás planetas en el Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto**                                       | Júpiter es el planeta más grande de nuestro Sistema Solar y el quinto a partir del Sol. Es un gigante gaseoso con una masa 1/1000 la del Sol, pero es más pesado que todos los demás planetas combinados. Las civilizaciones antiguas han sabido sobre Júpiter durante mucho tiempo, y es fácilmente visible en el cielo nocturno.. |
| 1              | Júpiter es el quinto planeta a partir del Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del sol, pero dos veces y media más que la de todos los demás planetas en el Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto** <br/> Lo que aprendimos es que Júpiter | es el quinto planeta a partir del Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa igual a la milésima parte del sol, pero dos veces y media más que la de todos los demás planetas combinados. Es fácilmente visible a simple vista y ha sido conocido desde la antigüedad.                        |
| 2              | Júpiter es el quinto planeta a partir del Sol y el más grande del Sistema Solar. Es un gigante gaseoso con una masa de una milésima parte del sol, pero dos veces y media más que la de todos los demás planetas en el Sistema Solar combinados. Júpiter es uno de los objetos más brillantes visibles a simple vista en el cielo nocturno, y ha sido conocido por las civilizaciones antiguas desde antes de la historia registrada. <br/>**Resume esto** <br/> Los 3 Hechos Principales Que Aprendimos:         | 1. Júpiter es el quinto planeta a partir del Sol y el más grande del Sistema Solar. <br/> 2. Es un gigante gaseoso con una masa de una milésima parte del Sol...<br/> 3. Júpiter ha sido visible a simple vista desde la antigüedad ...                                                                       |
|                |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                           |



### Plantillas de Prompt

Una plantilla de prompt es una _receta predefinida para un prompt_ que puede almacenarse y reutilizarse según sea necesario, para impulsar experiencias de usuario más consistentes a escala. En su forma más simple, es simplemente una colección de ejemplos de prompt como [este de OpenAI](https://platform.openai.com/examples?WT.mc_id=academic-105485-koreyst) que proporciona tanto los componentes interactivos de un prompt (mensajes de usuario y de sistema) como el formato de solicitud impulsado por la API - para admitir la reutilización.

En su forma más compleja como [este ejemplo de LangChain](https://python.langchain.com/docs/modules/model_io/prompts/prompt_templates/?WT.mc_id=academic-105485-koreyst) contiene _marcadores de posición_ que pueden ser reemplazados por datos de una variedad de fuentes (entrada del usuario, contexto del sistema, fuentes de datos externas, etc.) para generar un prompt de manera dinámica. Esto nos permite crear una biblioteca de prompts reutilizables que se pueden usar para impulsar experiencias de usuario consistentes **de forma programática** a escala.

Finalmente, el valor real de las plantillas radica en la capacidad de crear y publicar _bibliotecas de prompts_ para dominios de aplicaciones verticales - donde la plantilla de prompt ahora está _optimizada_ para reflejar el contexto o ejemplos específicos de la aplicación que hacen que las respuestas sean más relevantes y precisas para la audiencia de usuarios objetivo. El repositorio [Prompts For Edu](https://github.com/microsoft/prompts-for-edu?WT.mc_id=academic-105485-koreyst) es un gran ejemplo de este enfoque, ya que reúne una biblioteca de prompts para el ámbito educativo con énfasis en objetivos clave como la planificación de clases, el diseño de planes de estudios, la tutoría de estudiantes, etc.

## Contenido de Apoyo

Si pensamos en la construcción de prompts como algo que tiene una instrucción (tarea) y un objetivo (contenido primario), entonces el _contenido secundario_ es como un contexto adicional que proporcionamos para **influir en el resultado de alguna manera**. Podría tratarse de ajuste de parámetros, instrucciones de formato, taxonomías temáticas, etc., que pueden ayudar al modelo a _adaptar_ su respuesta de acuerdo a los objetivos o expectativas del usuario.

Por ejemplo: Dado un catálogo de cursos con metadatos extensos (nombre, descripción, nivel, etiquetas de metadatos, instructor, etc.) en todos los cursos disponibles en el plan de estudios:

- podemos definir una instrucción para "resumir el catálogo de cursos para el Otoño 2023"
- podemos usar el contenido principal para proporcionar algunos ejemplos de la salida deseada
- podemos usar el contenido secundario para identificar las 5 "etiquetas" principales de interés.

Ahora, el modelo puede proporcionar un resumen en el formato mostrado por los pocos ejemplos - pero si un resultado tiene varias etiquetas, puede priorizar las 5 etiquetas identificadas en el contenido secundario.

---

<!--
PLANTILLA DE LA LECCIÓN:
Esta unidad debería cubrir el concepto central #2.
Refuerza el concepto con ejemplos y referencias.

CONCEPT #3:
Técnicas de Prompt Engineering.
¿Cuáles son algunas técnicas básicas para prompt engineering?
Ilústralo con algunos ejercicios.
-->

## Mejores Prácticas de Prompting

Ahora que sabemos cómo se pueden _construir_ los prompts, podemos empezar a pensar en cómo _diseñarlos_ para que reflejen las mejores prácticas. Esto puede dividirse en dos partes - tener la _mentalidad_ adecuada y aplicar las _técnicas_ adecuadas.

### Mentalidad de Prompt Engineering

Prompt Engineering es un proceso de prueba-y-error, por lo que hay que tener en cuenta tres grandes factores orientativos:

1. **La Comprensión del Dominio Importa.** La precisión y relevancia de la respuesta es una función del _dominio_ en el que opera esa aplicación o usuario. Aplica tu intuición y experiencia en el campo para **personalizar técnicas** aún más. Por ejemplo, define _personalidades específicas del dominio_ en los prompts del sistema, o utiliza _plantillas específicas del dominio_ en los prompts del usuario. Proporciona contenido secundario que refleje contextos específicos del dominio o utiliza _señales y ejemplos específicos del dominio_ para guiar el modelo hacia patrones de uso familiares.

2. **La Comprensión del Modelo Importa.** Sabemos que los modelos son estocásticos por naturaleza. Pero las implementaciones de modelos también pueden variar en términos del conjunto de datos de entrenamiento que utilizan (conocimientos pre-entrenados), las capacidades que proporcionan (por ejemplo, a través de API o SDK) y el tipo de contenido para el que están optimizados (por ejemplo, código vs imágenes vs texto). Comprende las fortalezas y limitaciones del modelo que estás utilizando y utiliza ese conocimiento para _priorizar tareas_ o crear _plantillas personalizadas_ que estén optimizadas para las capacidades del modelo.

3. **La Iteración y la Validación Importan.** Los modelos están evolucionando rápidamente, al igual que las técnicas para prompt engineering. Como experto en un dominio, es posible que tengas otro contexto o criterio para _tu_ aplicación específica, que puede no aplicarse a la comunidad en general. Utiliza herramientas y técnicas de prompt engineering para "iniciar" la construcción de prompts, luego itera y valida los resultados utilizando tu propia intuición y experiencia en el dominio. Registra tus observaciones y crea una **base de conocimientos** (por ejemplo, bibliotecas de prompts) que otros puedan utilizar como nueva base de referencia para iteraciones más rápidas en el futuro.

## Mejores Prácticas

Ahora veamos las mejores prácticas comunes recomendadas por los profesionales de [Open AI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api?WT.mc_id=academic-105485-koreyst) y [Azure OpenAI](https://learn.microsoft.com/azure/ai-services/openai/concepts/prompt-engineering#best-practices?WT.mc_id=academic-105485-koreyst).

| Qué                              | Por Qué                                                                                                                                                                                                                                            |
| :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Evalúa los últimos modelos.       | Es probable que las nuevas generaciones de modelos tengan mejores características y calidad - pero también pueden incurrir en costos más elevados. Evalúa su impacto y luego toma decisiones sobre la migración.                                                                                    |
| Separa instrucciones y contexto.  | Comprueba si tu modelo/proveedor define _delimitadores_ para distinguir las instrucciones y el contenido primario y secundario con mayor claridad. Esto puede ayudar a los modelos a asignar pesos a los tokens con mayor precisión.                                                                |
| Sé específico y claro.            | Proporciona más detalles sobre el contexto deseado, el resultado, la longitud, el formato, el estilo, etc. Esto mejorará tanto la calidad como la coherencia de las respuestas. Captura recetas en plantillas reutilizables.                                                                         |
| Sé descriptivo, usa ejemplos.     | Los modelos pueden responder mejor a un enfoque de "mostrar y contar". Comienza con un enfoque "zero-shot" en el que le das una instrucción (pero sin ejemplos) y luego prueba con "few-shot" como refinamiento, proporcionando algunos ejemplos del resultado deseado. Utiliza analogías. |
| Utiliza señales para impulsar las finalizaciones.  | Empújalo hacia el resultado deseado dándole algunas palabras o frases clave que pueda usar como punto de partida para la respuesta.                                                                                                                                                 |
| Dobla la Apuesta.                 | A veces es posible que necesites repetir lo mismo que el modelo. Da instrucciones antes y después de tu contenido principal, usa una instrucción y una señal, etc. Itera y valida para ver qué funciona.                                                                                        |
| El Orden Importa.                 | El orden en el que presentas la información al modelo puede afectar el resultado, incluso en los ejemplos de aprendizaje, gracias al sesgo de actualidad. Prueba diferentes opciones para ver cuál funciona mejor.                                                                                    |
| Dale una "salida" al modelo.      | Proporciona al modelo una respuesta de finalización _alternativa_ que pueda proporcionar si no puede completar la tarea por algún motivo. Esto puede reducir las posibilidades de que los modelos generen respuestas falsas o fabricadas.                                                            |
|                                   |                                                                                                                                                                                                                                                   |

Como con cualquier otra mejor práctica, recuerda que _tu kilometraje puede variar_ en función del modelo, la tarea y el dominio. Utilízalos como punto de partida e itera para encontrar lo que funciona mejor para tí. Reevalúa constantemente tu proceso de prompt engineering a medida que dispongas de nuevos modelos y herramientas, centrándote en la escalabilidad del proceso y la calidad de la respuesta.

<!--
PLANTILLA DE LECCIÓN:
Esta unidad debería proporcionar un desafío de código si corresponde

DESAFÍO:
Enlace a un Jupyter Notebook con solo los comentarios de código en las instrucciones (las secciones de código están vacías).

SOLUCIÓN:
Enlace a una copia de ese Notebook con los prompts completados y ejecutados, mostrando lo que un ejemplo podría ser.
-->

## Tarea

¡Felicidades! ¡Llegaste al final de la lección! ¡Es hora de poner a prueba algunos de esos conceptos y técnicas con ejemplos reales!

Para nuestra tarea, utilizaremos un Jupyter Notebook con ejercicios que puedes completar de manera interactiva. También puedes extender el Notebook con tus propias celdas de Markdown y Código para explorar ideas y técnicas por tu cuenta.

### Para comenzar, haz fork al repo, luego

- (Recomendado) Inicia GitHub Codespaces
- (Alternativamente) Clona el repositorio a tu dispositivo local y úsalo con Docker Desktop
- (Alternativamente) Abre el Notebook con tu entorno de runtime de Notebook preferido.

### Siguiente, configura tus variables de entorno

- Copia el archivo `.env.copy` en la raiz del repositorio a `.env` y actualiza los valores de `AZURE_OPENAI_KEY`, `AZURE_OPENAI_ENDPOINT` y `AZURE_OPENAI_DEPLOYMENT`. Consulta la [sección de Sandbox de Aprendizaje](../../../04-prompt-engineering-fundamentals#learning-sandbox) para aprender cómo.

### Siguiente, abre el Jupyter Notebook

- Selecciona el runtime kernel. Si estás usando las opciones 1 o 2, simplemente selecciona el kernel predeterminado Python 3.10.x proporcionado por el contenedor de desarrollo.

Estás listo para realizar los ejercicios. Ten en cuenta que no hay respuestas _correctas o incorrectas_ aquí - sino que se trata de explorar opciones por prueba y error y de desarrollar la intuición de lo que funciona para un modelo y un dominio de aplicación determinados.

_Por esta razón, no hay segmento de Código de Solución en esta lección. En su lugar, el Notebook tendrá celdas de Markdown tituladas "Mi Solución:" que muestra una salida de ejemplo para referencia._

 <!--
PLANTILLA DE LA LECCIÓN:
Concluye la sección con un resumen y recursos para el aprendizaje autoguiado.
-->

## Verificación de Conocimientos

¿Cuál de los siguientes es un buen prompt que sigue algunas mejores prácticas razonables?

1. Muéstrame una imagen del auto rojo
2. Muéstrame una imagen del auto rojo de marca Volvo y modelo XC90 estacionado cerca de un acantilado con la puesta de sol
3. Muéstrame una imagen del auto rojo de marca Volvo y modelo XC90

R: 2, es el mejor prompt, ya que proporciona detalles sobre "qué" y entra en detalles (no cualquier automóvil sino una marca y modelo específicos) y también describe la configuración general. 3 es el siguiente mejor, ya que también contiene mucha descripción.

## 🚀 Desafío

Ve si puedes aprovechar la técnica de la "señal" con el siguiente prompt: Completa la oración "Muéstrame una imagen del auto rojo de la marca Volvo y ". ¿Con qué responde y cómo lo mejorarías?

## ¡Buen trabajo! Continúa tu Aprendizaje

¿Quieres obtener más información sobre los diferentes conceptos de Prompt Engineering? Ve a la [página de aprendizaje continuo](../../../13-continued-learning/README.md?WT.mc_id=academic-105485-koreyst) para encontrar otros grandes recursos sobre este tema.

Dirígete a la Lección 6 donde veremos ¡[técnicas avanzadas de prompting](../../../05-advanced-prompts/README.md?WT.mc_id=academic-105485-koreyst)!
