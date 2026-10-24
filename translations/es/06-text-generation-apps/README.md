# Construyendo aplicaciones de generación de texto

[![Construyendo aplicaciones de generación de texto](../../../translated_images/es/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Haz clic en la imagen de arriba para ver el video de esta lección)_

Hasta ahora, has visto a través de este currículo que existen conceptos básicos como los prompts e incluso toda una disciplina llamada "ingeniería de prompts". Muchas herramientas con las que puedes interactuar como ChatGPT, Office 365, Microsoft Power Platform y más, te apoyan utilizando prompts para lograr algo.

Para que puedas agregar esa experiencia a una app, necesitas entender conceptos como prompts, completions y elegir una librería para trabajar. Eso es exactamente lo que aprenderás en este capítulo.

## Introducción

En este capítulo, usted:

- Aprenderá sobre la librería openai y sus conceptos básicos.
- Construirá una aplicación de generación de texto usando openai.
- Entenderá cómo usar conceptos como prompt, temperatura y tokens para construir una aplicación de generación de texto.

## Objetivos de aprendizaje

Al final de esta lección, será capaz de:

- Explicar qué es una aplicación de generación de texto.
- Construir una aplicación de generación de texto usando openai.
- Configurar su aplicación para usar más o menos tokens y también cambiar la temperatura, para un resultado variado.

## ¿Qué es una aplicación de generación de texto?

Normalmente, cuando construyes una aplicación, tiene algún tipo de interfaz como la siguiente:

- Basada en comandos. Las aplicaciones de consola son aplicaciones típicas donde escribes un comando y realiza una tarea. Por ejemplo, `git` es una aplicación basada en comandos.
- Interfaz de usuario (UI). Algunas aplicaciones tienen interfaces gráficas de usuario (GUI), donde haces clic en botones, ingresas texto, seleccionas opciones y más.

### Las aplicaciones de consola y UI son limitadas

Compáralo con una app basada en comandos donde escribes un comando:

- **Tiene limitaciones**. No puedes simplemente escribir cualquier comando, solo los que la app soporta.
- **Específica de idioma**. Algunas apps soportan muchos idiomas, pero por defecto la app está diseñada para un idioma específico, aunque puedes agregar soporte para más idiomas.

### Beneficios de las aplicaciones de generación de texto

¿Cómo es diferente una app de generación de texto?

En una app de generación de texto tienes más flexibilidad, no estás limitado a un conjunto de comandos o a un idioma de entrada específico. En su lugar, puedes usar lenguaje natural para interactuar con la aplicación. Otro beneficio es que ya estás interactuando con una fuente de datos que ha sido entrenada en un vasto corpus de información, mientras que una app tradicional podría estar limitada a lo que hay en una base de datos.

### ¿Qué puedo construir con una app de generación de texto?

Hay muchas cosas que puedes construir. Por ejemplo:

- **Un chatbot**. Un chatbot que responda preguntas sobre temas, como tu empresa y sus productos, podría ser una buena opción.
- **Asistente**. Los LLM son excelentes para cosas como resumir texto, obtener insights de texto, generar texto como currículos y más.
- **Asistente de código**. Dependiendo del modelo de lenguaje que uses, puedes construir un asistente de código que te ayude a escribir código. Por ejemplo, puedes usar un producto como GitHub Copilot así como ChatGPT para ayudarte a escribir código.

## ¿Cómo puedo empezar?

Bueno, necesitas encontrar una forma de integrarte con un LLM lo cual generalmente implica dos enfoques:

- Usar una API. Aquí construyes solicitudes web con tu prompt y recibes el texto generado.
- Usar una librería. Las librerías ayudan a encapsular las llamadas a la API y hacerlas más fáciles de usar.

## Librerías / SDKs

Hay algunas librerías bien conocidas para trabajar con LLMs como:

- **openai**, esta librería facilita conectarte a tu modelo y enviar prompts.

Luego hay librerías que operan a un nivel más alto como:

- **Langchain**. Langchain es muy conocida y soporta Python.
- **Semantic Kernel**. Semantic Kernel es una librería de Microsoft que soporta los lenguajes C#, Python y Java.

## Primera app usando openai

Veamos cómo podemos construir nuestra primera app, qué librerías necesitamos, cuánto es requerido y más.

### Instalar openai

Hay muchas librerías para interactuar con OpenAI o Azure OpenAI. Es posible usar numerosos lenguajes de programación también como C#, Python, JavaScript, Java y más. Hemos elegido usar la librería de Python `openai`, así que usaremos `pip` para instalarla.

```bash
pip install openai
```

### Crear un recurso

Necesitas realizar los siguientes pasos:

- Crear una cuenta en Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtener acceso a Azure OpenAI. Ve a [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) y solicita acceso.

  > [!NOTE]
  > Al momento de escribir, necesitas aplicar para acceso a Azure OpenAI.

- Instalar Python <https://www.python.org/>
- Haber creado un recurso de Azure OpenAI Service. Consulta esta guía para cómo [crear un recurso](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Ubicar la clave API y el endpoint

En este punto, debes indicarle a tu librería `openai` qué clave API usar. Para encontrar tu clave API, ve a la sección "Claves y Endpoint" de tu recurso Azure OpenAI y copia el valor "Clave 1".

![Panel de Claves y Endpoint en el Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ahora que tienes esta información copiada, vamos a indicar a las librerías que la usen.

> [!NOTE]
> Vale la pena separar tu clave API de tu código. Puedes hacerlo usando variables de entorno.
>
> - Establece la variable de entorno `OPENAI_API_KEY` con tu clave API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurar Azure

Si estás usando Azure OpenAI (ahora parte de Microsoft Foundry), así es cómo configuras. Usamos el cliente estándar `OpenAI` apuntado al endpoint Azure OpenAI `/openai/v1/`, que funciona con la API de Responses y no requiere `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Arriba configuramos lo siguiente:

- `api_key`, esta es tu clave API encontrada en el Portal Azure o portal Microsoft Foundry.
- `base_url`, este es el endpoint del recurso Foundry con `/openai/v1/` agregado. El endpoint estable v1 funciona para OpenAI y Azure OpenAI sin necesidad de gestión de `api_version`.

> [!NOTE] > `os.environ` lee variables de entorno. Puedes usarla para leer variables de entorno como `AZURE_OPENAI_API_KEY` y `AZURE_OPENAI_ENDPOINT`. Establece estas variables en tu terminal o usando una librería como `dotenv`.

## Generar texto

La forma de generar texto es usar la API Responses mediante el método `responses.create`. Aquí un ejemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

En el código arriba, creamos una respuesta y pasamos el modelo que queremos usar y el prompt. Luego imprimimos el texto generado mediante `response.output_text`.

### Conversaciones multi-turno

La API Responses es adecuada tanto para generación de texto de un solo turno como para chatbots multi-turno - proporcionas una lista de mensajes en `input` para construir la conversación:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Más sobre esta funcionalidad en un capítulo próximo.

## Ejercicio - tu primera app de generación de texto

Ahora que aprendimos a configurar y ajustar openai, es hora de construir tu primera app de generación de texto. Para construir tu app, sigue estos pasos:

1. Crea un entorno virtual e instala openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Si usas Windows escribe `venv\Scripts\activate` en lugar de `source venv/bin/activate`.

   > [!NOTE]
   > Ubica tu clave Azure OpenAI yendo a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) y busca `Open AI`, selecciona `Open AI resource`, luego selecciona `Keys and Endpoint` y copia el valor `Key 1`.

1. Crea un archivo _app.py_ y coloca el siguiente código:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Si usas OpenAI normal (no Azure), usa `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (sin `base_url`) y pasa un nombre de modelo como `gpt-5-mini` en lugar de un nombre de despliegue.

   Deberías ver una salida como la siguiente:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para diferentes cosas

Ahora viste cómo generar texto usando un prompt. Incluso tienes un programa funcionando que puedes modificar y cambiar para generar diferentes tipos de texto.

Los prompts pueden usarse para todo tipo de tareas. Por ejemplo:

- **Generar un tipo de texto**. Por ejemplo, puedes generar un poema, preguntas para un quiz, etc.
- **Buscar información**. Puedes usar prompts para buscar información como el siguiente ejemplo '¿Qué significa CORS en desarrollo web?'.
- **Generar código**. Puedes usar prompts para generar código, por ejemplo desarrollar una expresión regular para validar correos o ¿por qué no generar un programa completo, como una web app?

## Un caso de uso más práctico: un generador de recetas

Imagina que tienes ingredientes en casa y quieres cocinar algo. Para eso necesitas una receta. Una manera de encontrar recetas es usar un motor de búsqueda o podrías usar un LLM para ello.

Podrías escribir un prompt así:

> "Muéstrame 5 recetas para un plato con los siguientes ingredientes: pollo, papas y zanahorias. Por receta, lista todos los ingredientes usados"

Dado ese prompt, podrías obtener una respuesta similar a:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Este resultado es genial, ya sé qué cocinar. En este punto, mejoras útiles podrían ser:

- Filtrar ingredientes que no me gustan o a los que soy alérgico.
- Producir una lista de compras, en caso de no tener todos los ingredientes en casa.

Para esos casos, agreguemos un prompt adicional:

> "Por favor, elimina recetas con ajo porque soy alérgico y reemplázalo con otra cosa. Además, por favor produce una lista de compras para las recetas, considerando que ya tengo pollo, papas y zanahorias en casa."

Ahora tienes un nuevo resultado, que es:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

Esas son tus cinco recetas, sin ajo mencionado y también tienes una lista de compras considerando lo que ya tienes en casa.

## Ejercicio - construir un generador de recetas

Ahora que jugamos un escenario, escribamos código para coincidir con el escenario mostrado. Para hacerlo, sigue estos pasos:

1. Usa el archivo _app.py_ existente como punto de partida
1. Ubica la variable `prompt` y cambia su código al siguiente:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Si ahora ejecutas el código, deberías ver una salida similar a:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTA, tu LLM es no determinístico, por lo que podrías obtener resultados diferentes cada vez que ejecutes el programa.

   Excelente, veamos cómo podemos mejorar las cosas. Para mejorar queremos asegurarnos que el código es flexible, así los ingredientes y el número de recetas puedan ser ajustados y cambiados.

1. Cambiemos el código de la siguiente manera:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Tomando el código para una prueba, podría verse así:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Mejorar agregando filtro y lista de compras

Ahora tenemos una app funcional capaz de producir recetas y es flexible porque depende de las entradas del usuario, tanto en número de recetas como también en los ingredientes usados.

Para mejorarla aún más, queremos agregar lo siguiente:

- **Filtrar ingredientes**. Queremos poder filtrar ingredientes que no nos gustan o a los que somos alérgicos. Para lograr este cambio, podemos editar nuestro prompt existente y añadir una condición de filtro al final así:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Arriba, añadimos `{filter}` al final del prompt y también capturamos el valor del filtro del usuario.

  Un ejemplo de entrada del programa ahora podría ser:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Como puedes ver, cualquier receta con leche ha sido filtrada. Pero, si eres intolerante a la lactosa, quizás quieras filtrar recetas con queso también, por lo que es necesario ser claro.

- **Producir una lista de compras**. Queremos producir una lista de compras, considerando lo que ya tenemos en casa.

  Para esta funcionalidad, podríamos intentar resolver todo en un prompt o dividirlo en dos prompts. Probemos el segundo enfoque. Aquí sugerimos agregar un prompt adicional, pero para que funcione necesitamos añadir el resultado del prompt anterior como contexto para el siguiente prompt.

  Ubica la parte en el código que imprime el resultado del primer prompt y añade el siguiente código abajo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Nota lo siguiente:

  1. Estamos construyendo un nuevo prompt añadiendo el resultado del primer prompt al nuevo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Hacemos una nueva solicitud, pero también considerando el número de tokens que pedimos en el primer prompt, así que esta vez decimos que `max_output_tokens` es 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Probando este código, ahora llegamos a la siguiente salida:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Mejora tu configuración

Lo que tenemos hasta ahora es un código que funciona, pero hay algunos ajustes que deberíamos hacer para mejorar aún más las cosas. Algunas cosas que deberíamos hacer son:

- **Separar secretos del código**, como la clave API. Los secretos no pertenecen al código y deben almacenarse en un lugar seguro. Para separar los secretos del código, podemos usar variables de entorno y bibliotecas como `python-dotenv` para cargarlas desde un archivo. Así es como se vería eso en el código:

  1. Crear un archivo `.env` con el siguiente contenido:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, para Azure OpenAI en Microsoft Foundry, necesitas configurar las siguientes variables de entorno en su lugar:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     En el código, cargarías las variables de entorno así:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Una palabra sobre la longitud de tokens**. Deberíamos considerar cuántos tokens necesitamos para generar el texto que queremos. Los tokens cuestan dinero, así que cuando sea posible, debemos intentar ser económicos con la cantidad de tokens que usamos. Por ejemplo, ¿podemos expresar el prompt de modo que usemos menos tokens?

  Para cambiar la cantidad de tokens usados, puedes usar el parámetro `max_output_tokens`. Por ejemplo, si quieres usar 100 tokens, harías:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentar con la temperatura**. La temperatura es algo que no hemos mencionado hasta ahora pero es un contexto importante para cómo funciona nuestro programa. A mayor valor de temperatura, más aleatoria será la salida. Por el contrario, a menor valor de temperatura, más predecible será la salida. Considera si quieres variación en tu salida o no.

  Para modificar la temperatura, puedes usar el parámetro `temperature`. Por ejemplo, si quieres usar una temperatura de 0.5, harías:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, cuanto más cerca de 1.0, más variada será la salida.

- **Los modelos de razonamiento no usan `temperature`**. Este es un cambio importante para 2026. Los modelos actuales no obsoletos en Microsoft Foundry son **modelos de razonamiento** (la familia GPT-5, serie o) - y **no soportan `temperature` ni `top_p`** (ni `max_tokens`; usa `max_output_tokens`). Si envías `temperature` a `gpt-5-mini` obtendrás un error de "parámetro no soportado". Así que para probar el ejemplo de temperatura anterior, apúntalo a un modelo que aún soporte controles de muestreo - por ejemplo un modelo abierto **Llama** como `Llama-3.3-70B-Instruct` del [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), llamado a través del endpoint Foundry Models / Azure AI Inference (de la misma forma que las muestras `githubmodels-*`). Para modelos de razonamiento como GPT-5, se dirige la salida de forma diferente:
  - **Ingeniería de prompts** - instrucciones claras, ejemplos y salida estructurada (ver la lección [04 - Ingeniería de prompts](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) hacen el trabajo que antes hacían los controles de muestreo.
  - **Controles de razonamiento** - parámetros como esfuerzo de razonamiento/verborrea ponen en balance profundidad del razonamiento contra latencia y costo.

  En resumen: `temperature`/`top_p` siguen siendo válidos en muchos modelos (Llama, Mistral, Phi y la familia GPT-4.x - aunque GPT-4.x está siendo deprecado), pero la dirección es ingeniería de prompts + controles de razonamiento en modelos de razonamiento como GPT-5.

## Tarea

Para esta tarea, puedes elegir qué construir.

Aquí hay algunas sugerencias:

- Ajusta la aplicación generadora de recetas para mejorarla aún más. Juega con los valores de temperatura y los prompts para ver qué puedes crear.
- Construye un "compañero de estudio". Esta aplicación debería poder responder preguntas sobre un tema, por ejemplo Python, podrías tener prompts como "¿Qué es un cierto tema en Python?", o un prompt que diga, muéstrame código para cierto tema, etc.
- Bot de historia, haz que la historia cobre vida, instruye al bot para que interprete a un personaje histórico determinado y hazle preguntas sobre su vida y época.

## Solución

### Compañero de estudio

A continuación hay un prompt inicial, mira cómo puedes usarlo y ajustarlo a tu gusto.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de historia

Aquí hay algunos prompts que podrías usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificación de conocimiento

¿Qué hace el concepto de temperatura?

1. Controla cuán aleatoria es la salida.
1. Controla qué tan grande es la respuesta.
1. Controla cuántos tokens se usan.

## 🚀 Desafío

Al trabajar en la tarea, intenta variar la temperatura, intenta establecerla en 0, 0.5 y 1. Recuerda que 0 es lo menos variado y 1 es lo más. ¿Qué valor funciona mejor para tu app?

## ¡Buen trabajo! Continúa tu aprendizaje

Después de completar esta lección, revisa nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tu conocimiento en IA generativa.

Dirígete a la Lección 7 donde veremos cómo [construir aplicaciones de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Descargo de responsabilidad**:
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional humana. No somos responsables de cualquier malentendido o interpretación errónea que surja del uso de esta traducción.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->