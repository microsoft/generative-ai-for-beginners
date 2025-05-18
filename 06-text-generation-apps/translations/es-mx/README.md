# Creación de Aplicaciones de Generación de Texto

[![Creación de Aplicaciones de Generación de Texto](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Haga clic en la imagen de arriba para ver el video de esta lección)_

Has visto hasta ahora en este programa que existen conceptos fundamentales como las indicaciones e incluso una disciplina llamada "ingeniería de indicaciones". Muchas herramientas con las que puedes interactuar, como ChatGPT, Office 365, Microsoft Power Platform y más, te ayudan a usar indicaciones para lograr algo.

Para añadir esta experiencia a una aplicación, necesitas comprender conceptos como las indicaciones, las finalizaciones y elegir una biblioteca con la que trabajar. Eso es precisamente lo que aprenderás en este capítulo.

## Introducción

En este capítulo, aprenderás:

- Aprenderás sobre la biblioteca OpenAI y sus conceptos fundamentales.
- Desarrollarás una aplicación de generación de texto con OpenAI.
- Comprenderás cómo usar conceptos como la indicacion, la temperatura y los tokens para desarrollar una aplicación de generación de texto.

## Objetivos de aprendizaje

Al finalizar esta lección, podrás:

- Explicar qué es una aplicación de generación de texto.
- Desarrollar una aplicación de generación de texto con OpenAI.
- Configurar tu aplicación para usar más o menos tokens y también cambiar la temperatura para obtener una salida variada.

## Qué es una aplicación de generación de texto?

Normalmente, al desarrollar una aplicación, esta tiene algún tipo de interfaz como la siguiente:

- Basada en comandos. Las aplicaciones de consola son aplicaciones típicas donde se escribe un comando y se ejecuta una tarea. Por ejemplo, `git` es una aplicación basada en comandos.
- Interfaz de usuario (UI). Algunas aplicaciones tienen interfaces gráficas de usuario (GUI) donde se hacen clic en botones, se introduce texto, se seleccionan opciones y más.

### Las aplicaciones de consola e interfaz de usuario son limitadas

Compáralas con una aplicación basada en comandos donde escribes un comando:

- **Es limitada**. No puedes escribir cualquier comando, solo los que la aplicación admite.
- **Específica del idioma**. Algunas aplicaciones admiten varios idiomas, pero por defecto están diseñadas para un idioma específico, incluso si puedes añadir más.

### Beneficios de las aplicaciones de generación de texto

En qué se diferencia una aplicación de generación de texto?

En una aplicación de generación de texto, tienes más flexibilidad; no estás limitado a un conjunto de comandos ni a un idioma de entrada específico. En cambio, puedes usar lenguaje natural para interactuar con la aplicación. Otra ventaja es que ya estás interactuando con una fuente de datos entrenada con un amplio corpus de información, mientras que una aplicación tradicional podría estar limitada por lo que hay en una base de datos.

### Qué puedo crear con una aplicación de generación de texto?

Hay muchas cosas que puedes crear. Por ejemplo:

- **Un chatbot**. Un chatbot que responda preguntas sobre temas como tu empresa y sus productos podría ser una buena opción.
- **Asistente**. Los LLM son excelentes para resumir texto, extraer información del texto, producir texto como currículums y más.
- **Asistente de código**. Dependiendo del modelo de lenguaje que uses, puedes crear un asistente de código que te ayude a escribir código. Por ejemplo, puedes usar un producto como GitHub Copilot y ChatGPT para ayudarte a escribir código.

## Cómo puedo empezar?

Bueno, necesitas encontrar una forma de integrarlo con un LLM, lo que generalmente implica los dos enfoques siguientes:

- Usar una API. Aquí construyes solicitudes web con tu solicitud y obtienes el texto generado.
- Usar una biblioteca. Las bibliotecas ayudan a encapsular las llamadas a la API y facilitan su uso.

## Bibliotecas/SDK

Existen algunas bibliotecas conocidas para trabajar con LLM, como:

- **OpenAI**: esta biblioteca facilita la conexión con el modelo y el envío de indicaciones.

También existen bibliotecas que operan a un nivel superior, como:

- **Langchain**: Langchain es muy conocida y compatible con Python.
- **Semantic Kernel**: Semantic Kernel es una biblioteca de Microsoft compatible con los lenguajes C#, Python y Java.

## Primera aplicación con openai

Veamos cómo podemos crear nuestra primera aplicación: qué bibliotecas necesitamos, cuántas se requieren, etc.

### Instalar openai

Existen muchas bibliotecas disponibles para interactuar con OpenAI o Azure OpenAI. Es posible usar numerosos lenguajes de programación, como C#, Python, JavaScript, Java y más. Hemos optado por usar la biblioteca de Python `openai`, así que usaremos `pip` para instalarla.

```bash
pip install openai
```

### Crear un recurso

Debe realizar los siguientes pasos:

- Crear una cuenta en Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtener acceso a Azure OpenAI. Vaya a [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) y solicite acceso.

> [!NOTA]
> Al momento de escribir este artículo, debe solicitar acceso a Azure OpenAI.

- Instalar Python <https://www.python.org/>
- Haber creado un recurso de Azure OpenAI Service. Consulta esta guía para saber cómo [crear un recurso](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizar la clave API y el punto de conexión

En este punto, debes indicar a tu biblioteca `openai` qué clave API usar. Para encontrarla, ve a la sección "Claves y punto de conexión" de tu recurso de Azure OpenAI y copia el valor "Clave 1".

Hoja de recursos Claves y puntos de conexión en Azure Portal (https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ahora que ha copiado esta información, instruyamos a las bibliotecas para que la usen.

> [!NOTA]
> Conviene separar la clave de API del código. Puede hacerlo mediante variables de entorno.
>
> - Establezca la variable de entorno `OPENAI_API_KEY` en su clave de API. > `export OPENAI_API_KEY='sk-...'`

### Configuración de Azure

Si usa Azure OpenAI, configure la configuración de la siguiente manera:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Arriba, configuramos lo siguiente:

- `api_type` a `azure`. Esto indica a la biblioteca que use Azure OpenAI y no OpenAI.
- `api_key`, su clave API, que se encuentra en el Portal de Azure.
- `api_version`, la versión de la API que desea usar. Al momento de escribir este artículo, la última versión es `2023-05-15`.
- `api_base`, este es el punto final de la API. Puede encontrarlo en el Portal de Azure junto a su clave de API.

> [!NOTA] > `os.getenv` es una función que lee variables de entorno. Puede usarla para leer variables de entorno como `OPENAI_API_KEY` y `API_BASE`. Establezca estas variables de entorno en su terminal o usando una biblioteca como `dotenv`.

## Generar texto

La forma de generar texto es usar la clase `Completion`. Aquí tienes un ejemplo:

```python
indicacion = "Complete the following: Érase una vez un"

completion = openai.Completion.create(model="davinci-002", indicacion=indicacion)
print(completion.choices[0].text)
```

En el código anterior, creamos un objeto de finalización y le pasamos el modelo que queremos usar y el mensaje. Luego, imprimimos el texto generado.

### Finalizaciones de chat

Hasta ahora, has visto cómo hemos usado `Completion` para generar texto. Pero existe otra clase llamada `ChatCompletion` que es más adecuada para chatbots. Aquí tienes un ejemplo de su uso:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Más información sobre esta funcionalidad en un próximo capítulo.

## Ejercicio: Tu primera aplicación de generación de texto

Ahora que hemos aprendido a configurar openai, es hora de crear tu primera aplicación de generación de texto. Para compilar tu aplicación, sigue estos pasos:

1. Crea un entorno virtual e instala OpenAI:

```bash
python -m venv venv
source venv/bin/activate
pip install openai
```

> [!NOTA]
> Si usas Windows, escribe `venv\Scripts\activate` en lugar de `source venv/bin/activate`.

> [!NOTA]
> Encuentra tu clave de Azure OpenAI en [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), busca `Open AI`, selecciona `Open AI resource` y luego `Keys and Endpoint`. Copia el valor `Key 1`.

1. Crea un archivo _app.py_ y asígnale el siguiente código:

```python
import openai

openai.api_key = "<reemplaza este valor con tu clave de OpenAI o la clave de Azure OpenAI>"

openai.api_type = 'azure'
openai.api_version = '2023-05-15'
openai.api_base = "<punto de conexión encontrado en Azure Portal donde está tu clave API>"
deployment_name = "<nombre de la implementación>"

# Agrega tu código de finalización
indicacion = "Completa lo siguiente: Érase una vez un"
messages = [{"role": "user", "content": indicacion}]

# Realizar la finalización
complete = openai.chat.completions.create(model=deployment_name, messages=messages)

# Imprimir respuesta
print(completion.choices[0].message.content)
```

> [!NOTA]
> Si usas Azure OpenAI, debes establecer `api_type` en `azure` y `api_key` en tu clave de Azure OpenAI.

Deberías ver un resultado como el siguiente:

```output
muy infeliz _____.

Había una vez una sirena muy infeliz.
```

## Diferentes tipos de indicaciones, para diferentes propósitos

Ahora has visto cómo generar texto usando una indicación. Incluso tienes un programa en ejecución que puedes modificar para generar diferentes tipos de texto.

Las indicaciones se pueden usar para todo tipo de tareas. Por ejemplo:

- **Generar un tipo de texto**. Por ejemplo, puedes generar un poema, preguntas para un cuestionario, etc.
- **Buscar información**. Puedes usar indicaciones para buscar información como en el siguiente ejemplo: "Qué significa CORS en el desarrollo web?".
- **Generar código**. Puedes usar indicaciones para generar código, por ejemplo, desarrollando una expresión regular para validar correos electrónicos, o por qué no generar un programa completo, como una aplicación web?

## Un caso práctico: un generador de recetas

Imagina que tienes ingredientes en casa y quieres cocinar algo. Para ello, necesitas una receta. Una forma de encontrar recetas es usar un buscador o un Máster en Derecho.

Podrías escribir una consigna como esta:

> "Muéstrame 5 recetas de un plato con los siguientes ingredientes: pollo, papas y zanahorias. Por receta, enumera todos los ingredientes utilizados".

Con la consigna anterior, podrías obtener una respuesta similar a esta:

```Resultado
1. Pollo asado con verduras:
Ingredientes:
- 4 muslos de pollo
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 2 cucharadas de aceite de oliva
- 2 dientes de ajo picados
- 1 cucharadita de tomillo seco
- 1 cucharadita de orégano seco
- Sal y pimienta al gusto

2. Guiso de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla picada
- 2 dientes de ajo picados
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cucharadita de Orégano
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta al gusto

3. Pollo y papa al horno:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cebolla picada
- 2 dientes de ajo picados
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta al gusto

4. Sopa de pollo y papa:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla picada
- 2 dientes de ajo picados
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 4 tazas de caldo de pollo
- Sal y pimienta Al gusto

5. Hash de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cebolla picada
- 2 dientes de ajo picados
- 1 cucharadita de orégano seco
```

Este resultado es genial, ya sé qué cocinar. En este punto, las mejoras que podrían ser útiles son:

- Filtrar los ingredientes que no me gustan o a los que soy alérgico.
- Hacer una lista de la compra, por si no tengo todos los ingredientes en casa.

Para los casos anteriores, agreguemos una indicación adicional:

> "Por favor, eliminen las recetas con ajo, ya que soy alérgico, y sustitúyanlo por otra cosa. También, por favor, hagan una lista de la compra de las recetas, considerando que ya tengo pollo, papas y zanahorias en casa".

Ahora tienes un nuevo resultado:

```Resultado
1. Pollo asado con verduras:
Ingredientes:
- 4 muslos de pollo
- 2 patatas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 2 cucharadas de aceite de oliva
- 1 cucharadita de tomillo seco
- 1 cucharadita de orégano seco
- Sal y pimienta al gusto

2. Guiso de pollo y patatas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla picada
- 2 pechugas de pollo cortadas en cubos
- 2 patatas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta al gusto

3. Pollo y patatas al horno:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo cortadas en cubos
- 2 patatas cortadas en Cubos
- 2 zanahorias cortadas en cubos
- 1 cebolla picada
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta al gusto

4. Sopa de pollo y papa:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla picada
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 4 tazas de caldo de pollo
- Sal y pimienta al gusto

5. Picadillo de pollo y papa:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo cortadas en cubos
- 2 papas cortadas en cubos
- 2 zanahorias cortadas en cubos
- 1 cebolla picada
- 1 cucharadita de orégano seco

Lista de compras:
- Aceite de oliva
- Cebolla
- Tomillo
- Orégano
- Sal
- Pimienta
```

Estas son tus cinco recetas, sin mencionar el ajo, y además tienes una lista de la compra considerando lo que ya tienes en casa.

## Ejercicio: crea un generador de recetas

Ahora que hemos desarrollado un escenario, escribamos código que coincida con el escenario demostrado. Para ello, siga estos pasos:

1. Use el archivo _app.py_ existente como punto de partida.
1. Localice la variable `indicacion` y cambie su código por el siguiente:

```python
indicacion = "Muéstrame 5 recetas de un plato con los siguientes ingredientes: pollo, papas y zanahorias. Por receta, enumere todos los ingredientes utilizados".
```

Si ahora ejecuta el código, debería ver un resultado similar a este:

```output
- Estofado de pollo con papas y zanahorias: 3 cucharadas de aceite, 1 cebolla picada, 2 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa pelada y picada, 1 hoja de laurel, 1 ramita de tomillo, 1/2 cucharadita de sal, 1/4 cucharadita de pimienta negra, 1 1/2 tazas de caldo de pollo, 1/2 taza de vino blanco seco, 2 cucharadas de perejil fresco picado, 2 cucharadas de mantequilla sin sal, 1 1/2 libras. Muslos de pollo deshuesados ​​y sin piel, cortados en trozos de 2,5 cm.
-Pollo asado al horno con patatas y zanahorias: 3 cucharadas de aceite de oliva virgen extra, 1 cucharada de mostaza Dijon, 1 cucharada de romero fresco picado, 1 cucharada de tomillo fresco picado, 4 dientes de ajo picados, 680 g de patatas rojas pequeñas cortadas en cuartos, 680 g de zanahorias cortadas en cuartos a lo largo, 1/2 cucharadita de sal, 1/4 de cucharadita de pimienta negra, 1 pollo entero (1,8 kg).
-Cazuela de pollo, patatas y zanahorias: aceite en aerosol, 1 cebolla grande picada, 2 dientes de ajo picados, 1 zanahoria pelada y rallada, 1 patata pelada y rallada, 1/2 cucharadita de hojas de tomillo seco, 1/4 de cucharadita de sal, 1/4 de cucharadita de pimienta negra, 500 ml de caldo de pollo sin grasa y bajo en sodio, 1 taza de guisantes congelados, 1/4 de taza. Harina para todo uso, 1 taza de leche descremada al 2%, 1/4 taza de queso parmesano rallado

- Cena de pollo y papas en una olla: 2 cucharadas de aceite de oliva, 450 g de muslos de pollo deshuesados ​​y sin piel, cortados en trozos de 2,5 cm, 1 cebolla grande picada, 3 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa pelada y picada, 1 hoja de laurel, 1 ramita de tomillo, 1/2 cucharadita de sal, 1/4 cucharadita de pimienta negra, 2 tazas de caldo de pollo, 1/2 taza de vino blanco seco

- Curry de pollo, papa y zanahoria: 1 cucharada de aceite vegetal, 1 cebolla grande picada, 2 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa pelada y picada, 1 cucharadita de cilantro molido, 1 cucharadita de comino molido, 1/2 cucharadita de cúrcuma molida, 1/2 cucharadita de jengibre molido, 1/4 cucharadita de pimienta de cayena, 2 tazas Caldo de pollo, 1/2 taza de vino blanco seco, 1 lata (15 onzas) de garbanzos escurridos y enjuagados, 1/2 taza de pasas, 1/2 taza de cilantro fresco picado
```

> NOTA: Su LLM no es determinista, por lo que podría obtener resultados diferentes cada vez que ejecute el programa.

Genial, veamos cómo podemos mejorar. Para mejorar, queremos asegurarnos de que el código sea flexible, de modo que se puedan mejorar y modificar los ingredientes y el número de recetas.

1. Modifiquemos el código de la siguiente manera:

```python
no_recipes = input("Número de recetas (por ejemplo, 5): ")

ingredientes = input("Lista de ingredientes (por ejemplo, pollo, papas y zanahorias): ")

# Interpolar el número de recetas en la solicitud an Ingredients
solicitud = f"Muéstrame {no_recipes} recetas de un plato con los siguientes ingredientes: {ingredientes}. Por receta, enumera todos los ingredientes utilizados"
```

Si tomamos el código para una prueba, podría verse así:

```salida
Número de recetas (por ejemplo, 5): 3
Lista de ingredientes (por ejemplo, pollo, papas y zanahorias): leche, fresas

-Batido de fresa: leche, fresas, azúcar, extracto de vainilla, cubitos de hielo
-Tarta de fresa: leche, harina, levadura química, azúcar, sal, mantequilla sin sal, fresas, crema batida
-Leche de fresa: leche, Fresas, azúcar, extracto de vainilla
```

### Mejora añadiendo un filtro y una lista de la compra

Ahora tenemos una aplicación funcional capaz de generar recetas y es flexible, ya que depende de la información del usuario, tanto en la cantidad de recetas como en los ingredientes utilizados.

Para mejorarla aún más, queremos añadir lo siguiente:

- **Filtrar ingredientes**. Queremos poder filtrar los ingredientes que no nos gustan o a los que somos alérgicos. Para lograr este cambio, podemos editar nuestra solicitud existente y añadir una condición de filtro al final, como se muestra a continuación:

```python
filter = input("Filtrar (por ejemplo, vegetariano, vegano o sin gluten): ")

solicitud = f"Muéstrame {no_recipes} recetas de un plato con los siguientes ingredientes: {ingredientes}. Por receta, enumera todos los ingredientes utilizados, sin {filter}"
```

Arriba, añadimos `{filtro}` al final de la solicitud y también capturamos el valor del filtro del usuario.

Un ejemplo de entrada para ejecutar el programa podría verse así:

```salida
Número de recetas (por ejemplo, 5): 3
Lista de ingredientes (por ejemplo, pollo, patatas y zanahorias): cebolla, leche
Filtro (por ejemplo, vegetariano, vegano o sin gluten): sin leche

1. Sopa de Cebolla Francesa

Ingredientes:

- 1 cebolla grande, rebanada
- 3 tazas de caldo de res
- 1 taza de leche
- 6 rebanadas de pan francés
- 1/4 taza de queso parmesano rallado
- 1 cucharada de mantequilla
- 1 cucharadita de tomillo seco
- 1/4 cucharadita de sal
- 1/4 cucharadita de pimienta negra

Instrucciones:

1. En una olla grande, sofría la cebolla en mantequilla hasta que esté dorada.
2. Añada el caldo de res, la leche, el tomillo, la sal y la pimienta. Deje hervir.
3. Reduzca el fuego y cocine a fuego lento durante 10 minutos.
4. Coloque las rebanadas de pan francés en platos hondos.
5. Sirva la sopa sobre el pan.
6. Espolvoree con queso parmesano.

2. Sopa de Cebolla y Papa

Ingredientes:

- 1 cebolla grande picada
- 2 tazas de papas picadas
- 3 tazas de caldo de verduras
- 1 taza de leche
- 1/4 cucharadita de pimienta negra

Instrucciones:

1. En una olla grande, sofría la cebolla en mantequilla hasta que esté dorada.
2. Añada las papas, el caldo de verduras, la leche y la pimienta. Deje hervir.
3. Reduzca el fuego y cocine a fuego lento durante 10 minutos.
4. Sirva caliente.

3. Sopa Cremosa de Cebolla

Ingredientes:

- 1 cebolla grande picada
- 3 tazas de caldo de verduras
- 1 taza de leche
- 1/4 cucharadita de pimienta negra
- 1/4 taza de harina para todo uso
- 1/2 taza de queso parmesano rallado

Instrucciones:

1. En una olla grande, sofría la cebolla en mantequilla hasta que esté dorada.
2. Añada el caldo de verduras, la leche y la pimienta. Deje hervir.
3. Reduzca el fuego y cocine a fuego lento durante 10 minutos.
4. En un tazón pequeño, bata la harina y el queso parmesano hasta que quede suave.
5. Añada a la sopa y cocine a fuego lento durante 5 minutos más, o hasta que espese.
```

Como puede ver, se han descartado las recetas con leche. Sin embargo, si tiene intolerancia a la lactosa, le recomendamos descartar también las recetas con queso, por lo que es importante aclararlo.

- **Elaborar una lista de la compra**. Queremos elaborar una lista de la compra teniendo en cuenta lo que ya tenemos en casa.

Para esta función, podríamos intentar resolver todo en una sola pregunta o dividirla en dos. Probemos este último enfoque. Aquí sugerimos agregar una pregunta adicional, pero para que funcione, necesitamos agregar el resultado de la primera pregunta como contexto a la segunda.

Localice la parte del código que imprime el resultado del primer mensaje y agregue el siguiente código:

```python
old_indicacion_result = completion.choices[0].message.content
indicacion = "Genere una lista de la compra para las recetas generadas y, por favor, no incluya ingredientes que ya tenga."

new_indicacion = f"{old_indicacion_result} {indicacion}"
messages = [{"role": "user", "content": new_indicacion}]
completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

# Imprimir respuesta
print("Lista de la compra:")
print(completion.choices[0].message.content)
```

Tenga en cuenta lo siguiente:

1. Construimos un nuevo mensaje añadiendo el resultado del primer mensaje al nuevo mensaje:

```python
new_indicacion = f"{old_indicacion_result} {indicacion}"
```

1. Realizamos una nueva solicitud, pero también consideramos la cantidad de tokens que solicitamos en el primer mensaje; por lo tanto, esta vez, `max_tokens` es 1200.

```python
complete = openai.Completion.create(engine=deployment_name, indicacion=new_indicacion, max_tokens=1200)
```

Probando este código, obtenemos la siguiente salida:

```output
Número de recetas (por ejemplo, 5): 2
Lista de ingredientes (por ejemplo, pollo, papas y zanahorias): manzana, harina
Filtro (por ejemplo, vegetariano, vegano o sin gluten): azúcar

- Panqueques de manzana y harina: 1 taza Harina, 1/2 cucharadita de levadura en polvo, 1/2 cucharadita de bicarbonato de sodio, 1/4 cucharadita de sal, 1 cucharada de azúcar, 1 huevo, 1 taza de suero de leche o leche agria, 1/4 taza de mantequilla derretida, 1 manzana Granny Smith pelada y rallada.

Buñuelos de manzana: 1 1/2 tazas de harina, 1 cucharadita de levadura en polvo, 1/4 cucharadita de sal, 1/4 cucharadita de bicarbonato de sodio, 1/4 cucharadita de nuez moscada, 1/4 cucharadita de canela, 1/4 cucharadita de pimienta de Jamaica, 1/4 taza de azúcar, 1/4 taza de manteca vegetal, 1/4 taza de leche, 1 huevo, 2 tazas de manzanas ralladas y peladas.

Lista de la compra:

Harina, levadura en polvo, bicarbonato de sodio, sal, azúcar, huevo, suero de leche, mantequilla, manzana, nuez moscada, canela, pimienta de Jamaica.

## Mejora tu Configuración

Hasta ahora, el código funciona, pero debemos realizar algunos ajustes para mejorarlo aún más. Algunas cosas que deberíamos hacer son:

- **Separar los secretos del código**, como la clave API. Los secretos no pertenecen al código y deben almacenarse en una ubicación segura. Para separar los secretos del código, podemos usar variables de entorno y bibliotecas como `python-dotenv` para cargarlos desde un archivo. Así se vería en código:

1. Cree un archivo `.env` con el siguiente contenido:

```bash
OPENAI_API_KEY=sk-...
```

> Nota: para Azure, debe configurar las siguientes variables de entorno:

```bash
OPENAI_API_TYPE=azure
OPENAI_API_VERSION=2023-05-15
OPENAI_API_BASE=<replace>
```

En código, las variables de entorno se cargarían así:

```python
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]
```

- **Aclaración sobre la longitud del token**. Debemos considerar cuántos tokens necesitamos para generar el texto deseado. Los tokens cuestan dinero, así que, siempre que sea posible, debemos intentar ahorrar en la cantidad de tokens que usamos. Por ejemplo, podemos redactar el mensaje de forma que podamos usar menos tokens?

Para cambiar los tokens utilizados, puede usar el parámetro `max_tokens`. Por ejemplo, si desea usar 100 tokens, debe hacer lo siguiente:

```python
completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
```

- **Experimentando con la temperatura**. La temperatura es algo que no hemos mencionado hasta ahora, pero es un contexto importante para el rendimiento de nuestro programa. Cuanto mayor sea el valor de la temperatura, más aleatoria será la salida. Por el contrario, cuanto menor sea el valor de la temperatura, más predecible será la salida. Considere si desea variación en la salida o no.

Para modificar la temperatura, puede usar el parámetro `temperature`. Por ejemplo, si desea usar una temperatura de 0.5, deberá hacer lo siguiente:

```python
completion = client.chat.completions.create(model=deployment, messages=messages, temperatures=0.5)
```

> Tenga en cuenta que cuanto más cerca de 1.0 esté el valor, más variada será la salida.

## Tarea

Para esta tarea, puedes elegir qué crear.

Sugerencias:

- Ajusta la aplicación generadora de recetas para mejorarla aún más. Experimenta con los valores de temperatura y las indicaciones para ver qué se te ocurre.

- Crea un "compañero de estudio". Esta aplicación debería poder responder preguntas sobre un tema, por ejemplo, Python. Podrías incluir indicaciones como "Qué es un tema específico en Python?", o una que diga "Muéstrame el código de un tema específico", etc.

- Bot de historia: haz que la historia cobre vida; pídele al bot que interprete a un personaje histórico y hazle preguntas sobre su vida y su época.

## Solución

### Compañero de estudio

A continuación, se muestra una indicación inicial: descubre cómo puedes usarla y modificarla a tu gusto.

```texto
- "Eres un experto en Python

Sugiere una lección para principiantes de Python con el siguiente formato:

Formato:
- Conceptos:
- Breve explicación de la lección:
- Ejercicio de código con soluciones"
```

### Bot de historial

Aquí tienes algunas sugerencias:

```texto
- "Eres Abe Lincoln, cuéntame sobre ti en 3 frases y responde usando la gramática y el vocabulario que Abe habría usado"
- "Eres Abe Lincoln, responde usando la gramática y el vocabulario que Abe habría usado:

Cuéntame sobre tus mayores logros, en 300 palabras"
```

## Comprobación de conocimientos

Qué hace el concepto "temperatura"?

1. Controla la aleatoriedad de la salida.
1. Controla el tamaño de la respuesta.
1. Controla la cantidad de tokens utilizados.

## 🚀 Desafío

Al trabajar en la tarea, intenta variar la temperatura; configúrala en 0, 0.5 y 1. Recuerda que 0 es el valor con menor variación y 1 el máximo. Qué valor funciona mejor para tu aplicación?

## Buen trabajo! Continúa aprendiendo!

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos de IA generativa.

Dirígete a la Lección 7, donde veremos cómo [crear aplicaciones de chat](../../../07-building-chat-applications/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst).