<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7a655f30d1dcbdfe6eff2558eff249af",
  "translation_date": "2025-05-19T10:27:57+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "es"
}
-->
# Construyendo Aplicaciones de Generación de Imágenes

[![Construyendo Aplicaciones de Generación de Imágenes](../../../translated_images/09-lesson-banner.d0229c79fda6596b8a678478e20301b74964cb8161e0c2e4a7c203655c623330.es.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Hay más en los LLMs que solo la generación de texto. También es posible generar imágenes a partir de descripciones de texto. Tener imágenes como una modalidad puede ser muy útil en varias áreas como MedTech, arquitectura, turismo, desarrollo de videojuegos y más. En este capítulo, exploraremos los dos modelos de generación de imágenes más populares, DALL-E y Midjourney.

## Introducción

En esta lección, cubriremos:

- Generación de imágenes y por qué es útil.
- DALL-E y Midjourney, qué son y cómo funcionan.
- Cómo construirías una aplicación de generación de imágenes.

## Objetivos de Aprendizaje

Después de completar esta lección, podrás:

- Construir una aplicación de generación de imágenes.
- Definir límites para tu aplicación con meta prompts.
- Trabajar con DALL-E y Midjourney.

## ¿Por qué construir una aplicación de generación de imágenes?

Las aplicaciones de generación de imágenes son una excelente manera de explorar las capacidades de la IA Generativa. Pueden ser utilizadas, por ejemplo:

- **Edición y síntesis de imágenes**. Puedes generar imágenes para una variedad de casos de uso, como edición de imágenes y síntesis de imágenes.

- **Aplicadas a una variedad de industrias**. También se pueden usar para generar imágenes para una variedad de industrias como Medtech, Turismo, Desarrollo de videojuegos y más.

## Escenario: Edu4All

Como parte de esta lección, continuaremos trabajando con nuestra startup, Edu4All. Los estudiantes crearán imágenes para sus evaluaciones, exactamente qué imágenes depende de los estudiantes, pero podrían ser ilustraciones para su propio cuento de hadas o crear un nuevo personaje para su historia o ayudarlos a visualizar sus ideas y conceptos.

Aquí está lo que los estudiantes de Edu4All podrían generar, por ejemplo, si están trabajando en clase sobre monumentos:

![Startup Edu4All, clase sobre monumentos, Torre Eiffel](../../../translated_images/startup.ec211d74fef9f4175010c3334942b715514230415744b9dd0a69a19f4ad68786.es.png)

usando un prompt como

> "Perro junto a la Torre Eiffel al amanecer"

## ¿Qué es DALL-E y Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) y [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) son dos de los modelos de generación de imágenes más populares, te permiten usar prompts para generar imágenes.

### DALL-E

Comencemos con DALL-E, que es un modelo de IA Generativa que genera imágenes a partir de descripciones de texto.

> [DALL-E es una combinación de dos modelos, CLIP y atención difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, es un modelo que genera embeddings, que son representaciones numéricas de datos, a partir de imágenes y texto.

- **Atención difusa**, es un modelo que genera imágenes a partir de embeddings. DALL-E está entrenado en un conjunto de datos de imágenes y texto y puede usarse para generar imágenes a partir de descripciones de texto. Por ejemplo, DALL-E puede usarse para generar imágenes de un gato con un sombrero, o un perro con una cresta.

### Midjourney

Midjourney funciona de manera similar a DALL-E, genera imágenes a partir de prompts de texto. Midjourney también puede usarse para generar imágenes usando prompts como "un gato con un sombrero" o "un perro con una cresta".

![Imagen generada por Midjourney, paloma mecánica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito de la imagen Wikipedia, imagen generada por Midjourney_

## ¿Cómo funcionan DALL-E y Midjourney?

Primero, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E es un modelo de IA Generativa basado en la arquitectura transformer con un _transformer autorregresivo_.

Un _transformer autorregresivo_ define cómo un modelo genera imágenes a partir de descripciones de texto, genera un píxel a la vez y luego usa los píxeles generados para generar el siguiente píxel. Pasando por múltiples capas en una red neuronal, hasta que la imagen está completa.

Con este proceso, DALL-E controla atributos, objetos, características y más en la imagen que genera. Sin embargo, DALL-E 2 y 3 tienen más control sobre la imagen generada.

## Construyendo tu primera aplicación de generación de imágenes

Entonces, ¿qué se necesita para construir una aplicación de generación de imágenes? Necesitas las siguientes bibliotecas:

- **python-dotenv**, se recomienda encarecidamente usar esta biblioteca para mantener tus secretos en un archivo _.env_ alejado del código.
- **openai**, esta biblioteca es la que usarás para interactuar con la API de OpenAI.
- **pillow**, para trabajar con imágenes en Python.
- **requests**, para ayudarte a hacer solicitudes HTTP.

1. Crea un archivo _.env_ con el siguiente contenido:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   ```

   Ubica esta información en el Portal de Azure para tu recurso en la sección "Claves y Punto de conexión".

1. Reúne las bibliotecas anteriores en un archivo llamado _requirements.txt_ de la siguiente manera:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. A continuación, crea un entorno virtual e instala las bibliotecas:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

   Para Windows, usa los siguientes comandos para crear y activar tu entorno virtual:

   ```bash
   python3 -m venv venv
   venv\Scripts\activate.bat
   ```

1. Agrega el siguiente código en un archivo llamado _app.py_:

   ```python
   import openai
   import os
   import requests
   from PIL import Image
   import dotenv

   # import dotenv
   dotenv.load_dotenv()

   # Get endpoint and key from environment variables
   openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
   openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

   # Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
   openai.api_version = '2023-06-01-preview'
   openai.api_type = 'azure'


   try:
       # Create an image by using the image generation API
       generation_response = openai.Image.create(
           prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
           size='1024x1024',
           n=2,
           temperature=0,
       )
       # Set the directory for the stored image
       image_dir = os.path.join(os.curdir, 'images')

       # If the directory doesn't exist, create it
       if not os.path.isdir(image_dir):
           os.mkdir(image_dir)

       # Initialize the image path (note the filetype should be png)
       image_path = os.path.join(image_dir, 'generated-image.png')

       # Retrieve the generated image
       image_url = generation_response["data"][0]["url"]  # extract image URL from response
       generated_image = requests.get(image_url).content  # download the image
       with open(image_path, "wb") as image_file:
           image_file.write(generated_image)

       # Display the image in the default image viewer
       image = Image.open(image_path)
       image.show()

   # catch exceptions
   except openai.InvalidRequestError as err:
       print(err)

   ```

Expliquemos este código:

- Primero, importamos las bibliotecas que necesitamos, incluida la biblioteca OpenAI, la biblioteca dotenv, la biblioteca requests y la biblioteca Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- A continuación, cargamos las variables de entorno del archivo _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Después de eso, configuramos el punto de conexión, clave para la API de OpenAI, versión y tipo.

  ```python
  # Get endpoint and key from environment variables
  openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
  openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

  # add version and type, Azure specific
  openai.api_version = '2023-06-01-preview'
  openai.api_type = 'azure'
  ```

- A continuación, generamos la imagen:

  ```python
  # Create an image by using the image generation API
  generation_response = openai.Image.create(
      prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
      size='1024x1024',
      n=2,
      temperature=0,
  )
  ```

  El código anterior responde con un objeto JSON que contiene la URL de la imagen generada. Podemos usar la URL para descargar la imagen y guardarla en un archivo.

- Por último, abrimos la imagen y usamos el visor de imágenes estándar para mostrarla:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Más detalles sobre la generación de la imagen

Veamos el código que genera la imagen con más detalle:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
```

- **prompt**, es el prompt de texto que se usa para generar la imagen. En este caso, estamos usando el prompt "Conejo en caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos".
- **size**, es el tamaño de la imagen que se genera. En este caso, estamos generando una imagen de 1024x1024 píxeles.
- **n**, es el número de imágenes que se generan. En este caso, estamos generando dos imágenes.
- **temperature**, es un parámetro que controla la aleatoriedad del resultado de un modelo de IA Generativa. La temperatura es un valor entre 0 y 1 donde 0 significa que el resultado es determinista y 1 significa que el resultado es aleatorio. El valor predeterminado es 0.7.

Hay más cosas que puedes hacer con imágenes que cubriremos en la siguiente sección.

## Capacidades adicionales de generación de imágenes

Has visto hasta ahora cómo pudimos generar una imagen usando unas pocas líneas en Python. Sin embargo, hay más cosas que puedes hacer con imágenes.

También puedes hacer lo siguiente:

- **Realizar ediciones**. Al proporcionar una imagen existente, una máscara y un prompt, puedes alterar una imagen. Por ejemplo, puedes agregar algo a una parte de una imagen. Imagina nuestra imagen de conejo, puedes agregar un sombrero al conejo. Cómo harías eso es proporcionando la imagen, una máscara (identificando la parte del área para el cambio) y un prompt de texto para decir qué se debe hacer.

  ```python
  response = openai.Image.create_edit(
    image=open("base_image.png", "rb"),
    mask=open("mask.png", "rb"),
    prompt="An image of a rabbit with a hat on its head.",
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  La imagen base solo contendría el conejo, pero la imagen final tendría el sombrero en el conejo.

- **Crear variaciones**. La idea es que tomas una imagen existente y pides que se creen variaciones. Para crear una variación, proporcionas una imagen y un prompt de texto y un código como este:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota, esto solo es compatible en OpenAI

## Temperatura

La temperatura es un parámetro que controla la aleatoriedad del resultado de un modelo de IA Generativa. La temperatura es un valor entre 0 y 1 donde 0 significa que el resultado es determinista y 1 significa que el resultado es aleatorio. El valor predeterminado es 0.7.

Veamos un ejemplo de cómo funciona la temperatura, ejecutando este prompt dos veces:

> Prompt: "Conejo en caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos"

![Conejo en un caballo sosteniendo una piruleta, versión 1](../../../translated_images/v1-generated-image.208ba0525ed6ae505504aa852e28d334c0440e9931b7c97f9508176a22d2dd54.es.png)

Ahora ejecutemos ese mismo prompt solo para ver que no obtendremos la misma imagen dos veces:

![Imagen generada de conejo en caballo](../../../translated_images/v2-generated-image.f0a88c05ef476e95f3682d4b21c9ba2f4807ae71cc29e9c05b42ebbf497cf61b.es.png)

Como puedes ver, las imágenes son similares, pero no iguales. Intentemos cambiar el valor de la temperatura a 0.1 y veamos qué sucede:

```python
 generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Cambiando la temperatura

Así que intentemos hacer la respuesta más determinista. Pudimos observar en las dos imágenes que generamos que en la primera imagen, hay un conejo y en la segunda imagen, hay un caballo, por lo que las imágenes varían mucho.

Por lo tanto, cambiemos nuestro código y establezcamos la temperatura a 0, así:

```python
generation_response = openai.Image.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ahora, cuando ejecutes este código, obtendrás estas dos imágenes:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.d8557be792b5c81c2c6d2804cb7b210fe8b340106fe4ffcadf9cf7de1cd7b991.es.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.bd412fcfbd43379312b1382212a332aa311ca1a80ea692dea50a8b876a487c61.es.png)

Aquí puedes ver claramente cómo las imágenes se parecen más entre sí.

## Cómo definir límites para tu aplicación con metaprompts

Con nuestra demostración, ya podemos generar imágenes para nuestros clientes. Sin embargo, necesitamos crear algunos límites para nuestra aplicación.

Por ejemplo, no queremos generar imágenes que no sean seguras para el trabajo, o que no sean apropiadas para niños.

Podemos hacer esto con _metaprompts_. Los metaprompts son prompts de texto que se utilizan para controlar el resultado de un modelo de IA Generativa. Por ejemplo, podemos usar metaprompts para controlar el resultado y asegurarnos de que las imágenes generadas sean seguras para el trabajo o apropiadas para niños.

### ¿Cómo funciona?

Ahora, ¿cómo funcionan los metaprompts?

Los metaprompts son prompts de texto que se utilizan para controlar el resultado de un modelo de IA Generativa, se posicionan antes del prompt de texto y se utilizan para controlar el resultado del modelo y se integran en aplicaciones para controlar el resultado del modelo. Encapsulando la entrada del prompt y la entrada del metaprompt en un solo prompt de texto.

Un ejemplo de un metaprompt sería el siguiente:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ahora, veamos cómo podemos usar metaprompts en nuestra demostración.

```python
disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt =f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"{meta_prompt}
Create an image of a bunny on a horse, holding a lollipop"

# TODO add request to generate image
```

En el prompt anterior, puedes ver cómo todas las imágenes creadas consideran el metaprompt.

## Asignación - vamos a habilitar a los estudiantes

Introdujimos Edu4All al comienzo de esta lección. Ahora es el momento de habilitar a los estudiantes para que generen imágenes para sus evaluaciones.

Los estudiantes crearán imágenes para sus evaluaciones que contengan monumentos, exactamente qué monumentos depende de los estudiantes. Se les pide a los estudiantes que usen su creatividad en esta tarea para colocar estos monumentos en diferentes contextos.

## Solución

Aquí hay una posible solución:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
openai.api_base = "<replace with endpoint>"
openai.api_key = "<replace with api key>"

# Assign the API version (DALL-E is currently supported for the 2023-06-01-preview API version only)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}"""

prompt = f"""{metaprompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = openai.Image.create(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response["data"][0]["url"]  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.InvalidRequestError as err:
    print(err)
```

## ¡Gran Trabajo! Continúa Tu Aprendizaje

Después de completar esta lección, consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA Generativa.

Dirígete a la Lección 10 donde veremos cómo [construir aplicaciones de IA con bajo código](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.