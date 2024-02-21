# **Creando Aplicaciones de Generación de Texto**

[![Creando Aplicaciones de Generación de Texto](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/5jKHzY6-4s8?WT.mc_id=academic-105485-koreyst)

> *(Haz clic en la imagen de arriba para ver el video de esta lección)*

Hasta ahora has visto a lo largo de este plan de estudios que hay conceptos básicos como prompts e incluso toda una disciplina llamada "prompt engineering". Muchas herramientas con las que puedes interactuar, como ChatGPT, Office 365, Microsoft Power Platform y más, te ayudan a utilizar prompts para lograr algo.

Para agregar dicha experiencia a una aplicación, debes comprender conceptos como prompts, finalizaciones y elegir una biblioteca con la que trabajar. Eso es exactamente lo que aprenderás en este capítulo.

## Introducción

En este capítulo tú vas a:

- Aprender sobre la biblioteca openai y sus conceptos básicos.
- Construir una aplicación de generación de texto usando openai.
- Comprender cómo utilizar conceptos como prompt, temperatura y tokens para crear una aplicación de generación de texto.

## Metas de Aprendizaje

Al final de esta lección, podrás:

- Explicar qué es una app de generación de texto.
- Construir una aplicación de generación de texto usando openai.
- Configurar tu aplicación para usar más o menos tokens y también cambiar la temperatura, para una salida variada.

## ¿Qué es una aplicación de generación de texto?

Normalmente, cuando creas una aplicación, tiene algún tipo de interfaz como la siguiente:

- Basada en comandos. Las aplicaciones de consola son aplicaciones típicas en las que escribes un comando y este realiza una tarea. Por ejemplo, `git` es una aplicación basada en comandos.
- Interfaz de usuario (UI). Algunas aplicaciones tienen interfaces gráficas de usuario (GUI) donde haces clic en botones, ingresas texto, seleccionas opciones y más.

### Las aplicaciones de Consola y UI son limitadas

Compáralo con una aplicación basada en comandos donde escribes un comando:

- **Es limitado**. No puedes simplemente escribir cualquier comando, solo los que admite la aplicación.
- **Idioma específico**. Algunas aplicaciones admiten muchos idiomas, pero de forma predeterminada, la aplicación está diseñada para un idioma específico, incluso si puedes agregar compatibilidad con más idiomas.

### Beneficios de las aplicaciones de generación de texto

Entonces, ¿en qué se diferencia una aplicación de generación de texto?

En una aplicación de generación de texto, tienes más flexibilidad, no estás limitado a un conjunto de comandos o a un idioma de entrada específico. En su lugar, puedes utilizar lenguaje natural para interactuar con la aplicación. Otro beneficio es que ya estás interactuando con una fuente de datos que ha sido entrenada con un vasto corpus de información, mientras que una aplicación tradicional puede estar limitada en cuanto a lo que hay en una base de datos.

### ¿Qué puedo crear con una aplicación de generación de texto?

Hay muchas cosas que puedes construir. Por ejemplo:

- **Un chatbot**. Un chatbot que responda preguntas sobre temas como tu empresa y tus productos podría ser una buena opción.
- **Ayudante**. Los LLMs son excelentes para cosas como resumir texto, obtener información a partir de texto, producir texto como currículums y más.
- **Asistente de código**. Dependiendo del modelo de lenguaje que utilices, puedes crear un asistente de código que te ayude a escribir código. Por ejemplo, puedes utilizar un producto como GitHub Copilot y ChatGPT para ayudarte a escribir código.

## ¿Cómo puedo comenzar?

Bueno, necesitas encontrar una manera de integrar un LLM, lo cual generalmente implica los dos enfoques siguientes:

- Utilizar una API. Aquí estás creando solicitudes web con tu mensaje y recuperando el texto generado.
- Utilizar una biblioteca. Las bibliotecas ayudan a encapsular las llamadas al API y hacerlas más fáciles de usar.

## Bibliotecas/SDKs

Existen algunas bibliotecas conocidas para trabajar con LLMs como:

- **openai**, esta biblioteca facilita conectarse a tu modelo y enviar prompts.

Luego están las bibliotecas que operan en un nivel superior como:

- **Langchain**. Langchain es bastante conocido y es compatible con Python.
- **Semantic Kernel**. Semantic Kernel es una biblioteca de Microsoft que admite los lenguajes C#, Python y Java.

## Primera app utilizando openai

Veamos cómo podemos crear nuestra primera aplicación, qué bibliotecas necesitamos, cuántas se necesitan, etc.

### Instala openai

Existen muchas bibliotecas para interactuar con OpenAI o Azure OpenAI. Es posible utilizar numerosos lenguajes de programación, como C#, Python, JavaScript, Java y más. Hemos elegido utilizar la biblioteca de Python `openai`, por lo que usaremos `pip` para instalarla.

```bash
pip install openai
```

### Crea un recurso

Necesitas realizar los siguientes pasos:

- Crear una cuenta en Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtener acceso a Azure Open AI. Visita [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) y solicita acceso.

  > [!NOTA]
  > Al momento de escribir este artículo, debes solicitar acceso a Azure Open AI.

- Instalar Python <https://www.python.org/>
- Haber creado un recurso de Azure OpenAI Service. Consulta esta guía para saber cómo [crear un recurso](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localiza clave API y punto de conexión

En este punto, debes indicarle a tu biblioteca `openai` qué clave API utilizar. Para encontrar tu clave API, ve a la sección "Claves y punto de conexión" de tu recurso Azure Open AI y copia el valor "Clave 1".

![Pestaña de Claves y punto de conexión del recurso en Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Ahora que has copiado esta información, indiquemos a las bibliotecas que la utilicen.

> [!NOTA]
> Vale la pena separar tu clave API de tu código. Puedes hacerlo utilizando variables de entorno.
>
> - Asigna tu clave API a la variable de entorno `OPENAI_API_KEY`.
>  `export OPENAI_API_KEY='sk-...'`

### Establece la configuración de Azure

Si estás usando Azure Open AI, así es como estableces la configuración:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Arriba estamos configurando lo siguiente:

- `api_type` en `azure`. Esto le indica a la biblioteca que use Azure Open AI y no OpenAI.
- `api_key`, esta es tu clave API que se encuentra en el Portal de Azure.
- `api_version`, esta es la versión de la API que deseas utilizar. En el momento de redactar este artículo, la última versión es `2023-05-15`.
- `api_base`, este es el punto de conexión de la API. Puedes encontrarlo en el Portal de Azure junto a tu clave API.

> [!NOTA]
> `os.getenv` es una función que lee variables de entorno. Puedes usarlo para leer variables de entorno como `OPENAI_API_KEY` y `API_BASE`. Configura estas variables de entorno en tu terminal o utilizando una biblioteca como `dotenv`.

## Genera texto

La forma de generar texto es utilizar la clase `Completion`. He aquí un ejemplo:

```python
prompt = "Completa lo siguiente: Érase una vez un"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

En el código anterior, creamos un objeto de finalización y le pasamos el modelo que queremos usar y el prompt. Luego imprimimos el texto generado.

### Finalizaciones de Chat

Hasta ahora, has visto cómo hemos estado usando `Completion` para generar texto. Pero hay otra clase llamada `ChatCompletion` que es más adecuada para chatbots. Aquí hay un ejemplo de su uso:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hola mundo"}])
print(completion.choices[0].message.content)
```

Más sobre esta funcionalidad en un próximo capítulo.

## Ejercicio - tu primera app de generación de texto

Ahora que aprendimos cómo instalar y configurar openai, es hora de crear tu primera aplicación de generación de texto. Para crear tu aplicación, sigue estos pasos:

1. Crea un entorno virtual e instala openai:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install openai
    ```

    > [!NOTA]
    > Si estás usando Windows escribe `venv\Scripts\activate` en lugar de `source venv/bin/activate`.

    > [!NOTA]
    > Ubica tu clave de Azure Open AI key yendo a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), busca `Open AI`, selecciona el `recurso Open AI`, elige `Claves y punto de conexión` y copia el valor `Clave 1`.

1. Crea un archivo *app.py* y asígnale el siguiente código:

    ```python
    import openai

    openai.api_key = "<reemplaza este valor con tu clave de Open AI o tu clave de Azure Open AI>"

    openai.api_type = 'azure' 
    openai.api_version = '2023-05-15'
    openai.api_base = "<punto de conexión localizado en Azure Portal donde está tu clave API>"
    deployment_name = "<nombre de la implementación>"

    # agrega tu código a finalizar
    prompt = "Completa lo siguiente: Érase una vez un"

    # realiza la finalización
    completion = openai.Completion.create(engine= deployment_name, model="davinci-002", prompt=prompt)
    
    # imprime la respuesta
    print(completion.choices[0].text)
    ```

    > [!NOTA]
    > Si estás usando Azure Open AI, debes establecer `api_type` a `azure` y asignar a `api_key` tu clave de Azure Open AI.

    Deberías ver un resultado como el siguiente:

    ```output
     muy infeliz _____.

    Érase una vez una sirena muy infeliz.
    ```

## Diferentes tipos de prompts para diferentes cosas

Ahora has visto cómo generar texto usando un prompt. Incluso tienes un programa en funcionamiento que puedes modificar y cambiar para generar diferentes tipos de texto.

Los prompts se pueden utilizar para todo tipo de tareas. Por ejemplo:

- **Generar un tipo de texto**. Por ejemplo, puedes generar un poema, preguntas para un cuestionario, etc.
- **Buscar información**. Puedes utilizar prompts para buscar información como en el siguiente ejemplo '¿Qué significa CORS en el desarrollo web?'.
- **Generar código**. Puedes utilizar prompts para generar código, por ejemplo desarrollando una expresión regular utilizada para validar correos electrónicos o ¿por qué no generar un programa completo, como una aplicación web?

## Un caso de uso más práctico: un generador de recetas

Imagina que tienes ingredientes en casa y quieres cocinar algo. Para eso, necesitas una receta. Una forma de encontrar recetas es utilizar un motor de búsqueda, o podrías utilizar un LLM para hacerlo.

Podrías escribir un prompt como este:

> "Muéstrame 5 recetas de un platillo con los siguientes ingredientes: pollo, patatas y zanahoria. Por receta, enumera todos los ingredientes utilizados"

Dado el prompt anterior, es posible que obtengas una respuesta similar a:

```output
1. Pollo Asado y Verduras:
Ingredientes:
- 4 muslos de pollo
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 2 cucharadas de aceite de oliva
- 2 dientes de ajo, picados
- 1 cucharadita de tomillo seco
- 1 cucharadita de orégano seco
- Sal y pimienta, al gusto

2. Estofado de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla, picada
- 2 dientes de ajo, picados
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta, al gusto

3. Pollo y Papas Al Horno:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cebolla, picada
- 2 dientes de ajo, picados
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta, al gusto

4. Sopa de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla, picada
- 2 dientes de ajo, picados
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 4 tazas de caldo de pollo
- Sal y pimienta, al gusto

5. Picadillo de pollo y papa:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cebolla, picada
- 2 dientes de ajo, picados
- 1 cucharadita de orégano seco
```

Este resultado es genial, ya sé qué cocinar. En este punto, las mejoras que podrían ser útiles son:

- Filtrar ingredientes que no me gustan o a los que no soy alérgico.
- Elaborar una lista de compras, en caso de que no tenga todos los ingredientes en casa.

Para los casos anteriores, agreguemos un prompt adicional:

> "Por favor elimina las recetas con ajo porque soy alérgico y reemplázalas con otra cosa. Además, haz una lista de compras para las recetas, considerando que ya tengo pollo, papas y zanahorias en casa".

Ahora tienes un nuevo resultado, a saber:

```output
1. Pollo Asado y Verduras:
Ingredientes:
- 4 muslos de pollo
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 2 cucharadas de aceite de oliva
- 1 cucharadita de tomillo seco
- 1 cucharadita de orégano seco
- Sal y pimienta, al gusto

2. Estofado de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla, picada
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta, al gusto

3. Pollo y Papas Al Horno:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cebolla, picada
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 1 taza de caldo de pollo
- Sal y pimienta, al gusto

4. Sopa de pollo y papas:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 1 cebolla, picada
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cucharadita de orégano seco
- 1 cucharadita de tomillo seco
- 4 tazas de caldo de pollo
- Sal y pimienta, al gusto

5. Picadillo de pollo y papa:
Ingredientes:
- 2 cucharadas de aceite de oliva
- 2 pechugas de pollo, cortadas en cubos
- 2 papas, cortadas en cubos
- 2 zanahorias, cortadas en cubos
- 1 cebolla, picada
- 1 cucharadita de orégano seco

Lista de Compras: 
- Aceite de oliva
- Cebolla
- Tomillo
- Orégano
- Sal
- Pimienta
```

Esas son tus cinco recetas, sin mencionar el ajo y además tienes una lista de compras teniendo en cuenta lo que ya tienes en casa.

## Ejercicio - crea un generador de recetas

Ahora que hemos representado un escenario, vamos a escribir código que se ajuste al escenario demostrado. Para ello, sigue estos pasos:

1. Utiliza el archivo *app.py* existente como punto de partida.
2. Localiza la variable `prompt` y cambia su código al siguiente:

    ```python
    prompt = "Muéstrame 5 recetas para un plato con los siguientes ingredientes: pollo, papas y zanahorias. Por receta, enumera todos los ingredientes utilizados"
    ```

    Si ahora ejecutas el código, deberías ver un resultado similar a:
   

    ```output
    -Estofado de Pollo con Papas y Zanahorias: 3 cucharadas de aceite, 1 cebolla picada, 2 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa pelada y picada, 1 hoja de laurel, 1 ramita de tomillo, 1/2 cucharadita de sal , 1/4 cucharadita de pimienta negra, 1 1/2 tazas de caldo de pollo, 1/2 taza de vino blanco seco, 2 cucharadas de perejil fresco picado, 2 cucharadas de mantequilla sin sal, 1 1/2 libras de muslos de pollo deshuesados y sin piel, cortados en piezas de 1 pulgada.

    -Pollo Asado al Horno con Papas y Zanahorias: 3 cucharadas de aceite de oliva extra virgen, 1 cucharada de mostaza Dijon, 1 cucharada de romero fresco picado, 1 cucharada de tomillo fresco picado, 4 dientes de ajo picados, 1 1/2 libras de papas rojas pequeñas, en cuartos, 1 1/2 libras de zanahorias, cortadas en cuartos a lo largo, 1/2 cucharadita de sal, 1/4 cucharadita de pimienta negra, 1 pollo entero (4 libras).

    -Cazuela de Pollo, Papa y Zanahoria: aceite en aerosol, 1 cebolla grande picada, 2 dientes de ajo picados, 1 zanahoria pelada y rallada, 1 papa pelada y rallada, 1/2 cucharadita de hojas secas de tomillo, 1/4 cucharadita sal, 1/4 cucharadita de pimienta negra, 2 tazas de caldo de pollo sin grasa y bajo en sodio, 1 taza de guisantes congelados, 1/4 taza de harina para todo uso, 1 taza de leche descremada al 2%, 1/4 taza de queso parmesano rallado.
        
    -Cena de Pollo y Papa en una Olla: 2 cucharadas de aceite de oliva, 1 libra de muslos de pollo deshuesados y sin piel, cortados en trozos de 1 pulgada, 1 cebolla grande picada, 3 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa, pelada y picada, 1 hoja de laurel, 1 ramita de tomillo, 1/2 cucharadita de sal, 1/4 cucharadita de pimienta negra, 2 tazas de caldo de pollo, 1/2 taza de vino blanco seco.

    -Curry de Pollo, Papas y Zanahoria: 1 cucharada de aceite vegetal, 1 cebolla grande picada, 2 dientes de ajo picados, 1 zanahoria pelada y picada, 1 papa pelada y picada, 1 cucharadita de cilantro molido, 1 cucharadita de comino molido, 1/2 cucharadita de cúrcuma molida, 1/2 cucharadita de jengibre molido, 1/4 cucharadita de pimienta de cayena, 2 tazas de caldo de pollo, 1/2 taza de vino blanco seco, 1 lata (15 onzas) de garbanzos, escurridos y enjuagados, 1/2 taza de pasas, 1/2 taza de cilantro fresco picado.
    ```

    > NOTA, tu LLM es no determinista, por lo que es posible que obtengas resultados diferentes cada vez que ejecutes el programa.

    Genial, veamos cómo podemos mejorar las cosas. Para mejorar las cosas, queremos asegurarnos de que el código sea flexible, de modo que se puedan mejorar y cambiar los ingredientes y la cantidad de recetas.

1. Cambiemos el código de la siguiente manera:

    ```python
    no_recipes = input("Número de recetas (por ejemplo, 5: ")

    ingredients = input("Lista de ingredientes (por ejemplo, pollo, papas y zanahorias: ")
    
    # interpola el número de recetas en el prompt de ingredientes
    prompt = f"Muéstrame {no_recipes} recetas para un platillo con los siguientes ingredientes: {ingredients}. Por receta, enumera todos los ingredientes utilizados"
    ```

    Tomando el código para una prueba de funcionamiento, podría tener este aspecto:

    ```output
    Número de recetas (por ejemplo, 5: 3
    Lista de ingredientes (por ejemplo, pollo, papas y zanahorias: leche,fresas

    -Batido de fresa: leche, fresas, azúcar, extracto de vainilla, cubitos de hielo
    -Tarta de fresas: leche, harina, levadura, azúcar, sal, mantequilla sin sal, fresas, nata montada
    -Leche de fresa: leche, fresas, azúcar, extracto de vainilla    
    ```

### Mejora agregando filtro y lista de compras

Ahora tenemos una aplicación funcional capaz de producir recetas y es flexible, ya que depende de las aportaciones del usuario, tanto en la cantidad de recetas como en los ingredientes utilizados.

Para mejorarlo aún más, queremos agregar lo siguiente:

- **Filtrar ingredientes**. Queremos poder filtrar los ingredientes que no nos gustan o a los que somos alérgicos. Para lograr este cambio, podemos editar nuestro prompt existente y agregar una condición de filtro al final de esta manera:

    ```python
    filter = input("Filtro (por ejemplo, vegetariano, vegano o sin gluten: ")

    prompt = f"Muéstrame {no_recipes} recetas para un platillo con los siguientes ingredientes: {ingredients}. Por receta, enumera todos los ingredientes utilizados, sin {filter}"
    ```

    Arriba, agregamos `{filter}` al final del prompt y también capturamos el valor del filtro del usuario.

    Un ejemplo de entrada para ejecutar el programa ahora puede verse así:

    ```output
    Número de recetas (por ejemplo, 5: 3
    Lista de ingredientes (por ejemplo, pollo, papas y zanahorias: cebolla,leche
    Filtro (por ejemplo, vegetariano, vegano o sin gluten: no leche

    1. Sopa De Cebolla Francesa

    Ingredientes:
    
    -1 cebolla grande, en rodajas
    -3 tazas de caldo de res
    -1 taza de leche
    -6 rebanadas de pan francés
    -1/4 taza de queso parmesano rallado
    -1 cucharada de mantequilla
    -1 cucharadita de tomillo seco
    -1/4 cucharadita de sal
    -1/4 cucharadita de pimienta negra    

    Instrucciones:
    
    1. En una olla grande, saltea las cebollas en mantequilla hasta que estén doradas.
    2. Agrega el caldo de res, la leche, el tomillo, la sal y la pimienta. Llevar a ebullición.
    3. Reduce el fuego y cocina a fuego lento durante 10 minutos.
    4. Coloca las rebanadas de pan francés en tazones de sopa.
    5. Sirve la sopa sobre el pan.
    6. Espolvorea con queso parmesano.
    
    2. Sopa De Cebolla Y Papa
    
    Ingredientes:
    
    -1 cebolla grande, picada
    -2 tazas de papas, cortadas en cubitos
    -3 tazas de caldo de verduras
    -1 taza de leche
    -1/4 cucharadita de pimienta negra
    
    Instrucciones:
    
    1. En una olla grande, saltea las cebollas en mantequilla hasta que estén doradas.
    2. Agrega las papas, el caldo de verduras, la leche y la pimienta. Llevar a ebullición.
    3. Reduce el fuego y cocina a fuego lento durante 10 minutos.
    4. Sirve caliente.
    
    3. Sopa Cremosa de Cebolla
    
    Ingredientes:
    
    -1 cebolla grande, picada
    -3 tazas de caldo de verduras
    -1 taza de leche
    -1/4 cucharadita de pimienta negra
    -1/4 taza de harina para todo uso
    -1/2 taza de queso parmesano rallado
    
    Instrucciones:
    
    1. En una olla grande, saltea las cebollas en mantequilla hasta que estén doradas.
    2. Agrega el caldo de verduras, la leche y la pimienta. Llevar a ebullición.
    3. Reduce el fuego y cocina a fuego lento durante 10 minutos.
    4. En un tazón pequeño, mezcla la harina y el queso parmesano hasta que quede suave.
    5. Agrega a la sopa y cocina a fuego lento durante 5 minutos más o hasta que la sopa se espese.
    ```

    Como puedes ver, se han filtrado todas las recetas que contienen leche. Pero, si eres intolerante a la lactosa, es posible que también desees filtrar las recetas que contienen queso, por lo que es necesario ser claro.


- **Elabora una lista de compras**. Queremos elaborar una lista de compras, teniendo en cuenta lo que ya tenemos en casa.

    Para esta funcionalidad, podríamos intentar resolver todo en un prompt o dividirlo en dos prompts. Probemos el último enfoque. Aquí sugerimos agregar un prompt adicional, pero para que eso funcione, necesitamos agregar el resultado del prompt anterior como contexto al último prompt.

    Localiza la parte en el código que imprime el resultado del primer prompt y agrega el siguiente código a continuación:

    ```python
    old_prompt_result = completion.choices[0].text
    prompt = "Elabora una lista de compras para las recetas generadas y por favor no incluyas ingredientes que ya tengo."
    
    new_prompt = f"{old_prompt_result} {prompt}"
    completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
    
    # imprime respuesta
    print("Lista de compras:")
    print(completion.choices[0].text)
    ```

    Considera lo siguiente:

    1. Estamos construyendo un nuevo prompt agregando el resultado del primer prompt al nuevo prompt:

        ```python
        new_prompt = f"{old_prompt_result} {prompt}"
        ```

    2. Hacemos una nueva solicitud, pero también tomamos en cuenta la cantidad de tokens que solicitamos en el primer prompt, por lo que esta vez decimos que `max_tokens` es 1200.

        ```python
        completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
        ```  

        Probando este código, ahora llegamos al siguiente resultado:

        ```output
        Número de recetas (por ejemplo, 5: 2
        Lista de ingredientes (por ejemplo, pollo, papas y zanahorias: manzana,harina
        Filtro (por ejemplo, vegetariano, vegano o sin gluten: azúcar

        
        -Panqueques de manzana y harina: 1 taza de harina, 1/2 cucharadita de levadura en polvo, 1/2 cucharadita de bicarbonato de sodio, 1/4 cucharadita de sal, 1 cucharada de azúcar, 1 huevo, 1 taza de suero de leche o leche agria, 1/4 taza de mantequilla derretida , 1 manzana Granny Smith, pelada y rallada
        -Buñuelos de manzana: 1-1/2 tazas de harina, 1 cucharadita de levadura en polvo, 1/4 cucharadita de sal, 1/4 cucharadita de bicarbonato de sodio, 1/4 cucharadita de nuez moscada, 1/4 cucharadita de canela, 1/4 cucharadita de pimienta de Jamaica, 1/4 taza de azúcar, 1/4 taza de manteca vegetal, 1/4 taza de leche, 1 huevo, 2 tazas de manzanas peladas y ralladas        
        Lista de compras:
        -Harina, levadura en polvo, bicarbonato de sodio, sal, azúcar, huevo, suero de leche, mantequilla, manzana, nuez moscada, canela, pimienta de Jamaica.
        ```

## Mejora tu configuración

Lo que tenemos hasta ahora es código que funciona, pero hay algunos ajustes que deberíamos hacer para mejorar aún más las cosas. Algunas cosas que deberíamos hacer son:

- **Separa los secretos del código**, como la clave API. Los secretos no pertenecen al código y deberían almacenarse en un lugar seguro. Para separar los secretos del código, podemos usar variables de entorno y bibliotecas como `python-dotenv` para cargarlos desde un archivo. Así es como se vería en código:

    1. Crea un archivo `.env` con el siguiente contenido:

        ```bash
        OPENAI_API_KEY=sk-...
        ```

        > Nota, para Azure, debes configurar las siguientes variables de entorno:

        ```bash
        OPENAI_API_TYPE=azure
        OPENAI_API_VERSION=2023-05-15
        OPENAI_API_BASE=<reemplaza>
        ```

        En el código, cargarías las variables de entorno de esta manera:

        ```python
        from dotenv import load_dotenv

        load_dotenv()

        openai.api_key = os.environ["OPENAI_API_KEY"]
        ```

- **Unas palabras sobre la longitud del token**. Deberíamos considerar cuántos tokens necesitamos para generar el texto que queremos. Los tokens cuestan dinero, por lo que, siempre que sea posible, deberíamos intentar ser económicos con la cantidad de tokens que utilizamos. Por ejemplo, ¿podemos formular el prompt de manera que podamos usar menos tokens?

   Para cambiar los tokens utilizados, puedes utilizar el parámetro `max_tokens`. Por ejemplo, si quieres usar 100 tokens, harías lo siguiente:

    ```python
    completion = openai.Completion.create(model="davinci-002", prompt=prompt, max_tokens=100)
    ```

- **Experimentando con la temperatura**. La temperatura es algo que no hemos mencionado hasta ahora, pero es un contexto importante del rendimiento de nuestro programa. Cuanto mayor sea el valor de la temperatura, más aleatoria será la salida. A la inversa, cuanto menor sea el valor de la temperatura, más predecible será la salida. Considera si deseas variación en tu salida o no.

   Para modificar la temperatura, puedes utilizar el parámetro `temperature`. Por ejemplo, si deseas utilizar una temperatura de 0.5, harías lo siguiente:

    ```python
    completion = openai.Completion.create(model="davinci-002", prompt=prompt, temperature=0.5)
    ```

   > Nota, cuanto más te acerques a 1.0, más variada será la salida.

## Tarea

Para esta tarea, puedes elegir qué construir.

Aquí hay algunas sugerencias:

- Modifica la aplicación generadora de recetas para mejorarla aún más. Experimenta con los valores de temperatura y los prompts para ver qué se te ocurre.
- Construye un "compañero de estudio". Esta aplicación debería poder responder preguntas sobre un tema, por ejemplo Python, podrías tener prompts como "¿Qué es un tema determinado en Python?", o podrías tener un prompt que diga, muéstrame el código para un tema determinado, etc.
- Bot de Historia, haz que la historia cobre vida, instruye al bot para que interprete a un determinado personaje histórico y hazle preguntas sobre su vida y su época.

## Solución

### Compañero de estudio

A continuación se muestra un prompt de inicio, observa cómo puedes usarlo y modifícalo a tu gusto.

```text
- "Eres un experto en el lenguaje Python.

    Sugiere una lección para principiantes de Python en el siguiente formato:

    Formato:
    - conceptos:
    - breve explicación de la lección:
    - ejercicio en código con soluciones"
```

### Bot de Historia

A continuación se muestran algunos prompts que podrías utilizar:

```text
- "Eres Abe Lincoln, cuéntame sobre ti en 3 oraciones y responde usando gramática y palabras como las que habría usado Abe"
- "Eres Abe Lincoln, responde usando gramática y palabras como las que hubiera usado Abe:

   Cuéntame tus mayores logros, en 300 palabras"
```

## Verificación de conocimientos

¿Qué hace el concepto de temperatura?

1. Controla qué tan aleatoria es la salida.
2. Controla el tamaño de la respuesta.
3. Controla cuántos tokens se utilizan.

## 🚀 Desafío

Cuando trabajes en la tarea, intenta variar la temperatura, intenta configurarla en 0, 0.5 y 1. Recuerda que 0 es el menos variado y 1 es el máximo, ¿qué valor funciona mejor para tu aplicación?

## ¡Buen trabajo! Continúa tu Aprendizaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!  

Dirígete a la Lección 7, donde veremos ¡cómo [construir aplicaciones de chat](../../../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!
