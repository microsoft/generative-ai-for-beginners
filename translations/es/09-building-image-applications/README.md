<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "063a2ac57d6b71bea0eaa880c68770d2",
  "translation_date": "2025-09-29T21:26:21+00:00",
  "source_file": "09-building-image-applications/README.md",
  "language_code": "es"
}
-->
# Creando Aplicaciones de Generación de Imágenes

[![Creando Aplicaciones de Generación de Imágenes](../../../translated_images/09-lesson-banner.906e408c741f44112ff5da17492a30d3872abb52b8530d6506c2631e86e704d0.es.png)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Los LLMs no solo sirven para generar texto. También es posible generar imágenes a partir de descripciones textuales. Tener imágenes como modalidad puede ser muy útil en diversas áreas como MedTech, arquitectura, turismo, desarrollo de videojuegos y más. En este capítulo, exploraremos los dos modelos de generación de imágenes más populares: DALL-E y Midjourney.

## Introducción

En esta lección, cubriremos:

- La generación de imágenes y por qué es útil.
- DALL-E y Midjourney: qué son y cómo funcionan.
- Cómo construir una aplicación de generación de imágenes.

## Objetivos de Aprendizaje

Después de completar esta lección, podrás:

- Construir una aplicación de generación de imágenes.
- Definir límites para tu aplicación con meta-prompts.
- Trabajar con DALL-E y Midjourney.

## ¿Por qué construir una aplicación de generación de imágenes?

Las aplicaciones de generación de imágenes son una excelente manera de explorar las capacidades de la IA Generativa. Pueden ser utilizadas, por ejemplo:

- **Edición y síntesis de imágenes**. Puedes generar imágenes para una variedad de casos de uso, como edición y síntesis de imágenes.

- **Aplicación en diversas industrias**. También pueden ser utilizadas para generar imágenes en industrias como MedTech, Turismo, Desarrollo de videojuegos y más.

## Escenario: Edu4All

Como parte de esta lección, continuaremos trabajando con nuestra startup, Edu4All. Los estudiantes crearán imágenes para sus evaluaciones; qué imágenes crear depende de ellos, pero podrían ser ilustraciones para su propio cuento de hadas, crear un nuevo personaje para su historia o ayudarles a visualizar sus ideas y conceptos.

Por ejemplo, esto es lo que los estudiantes de Edu4All podrían generar si están trabajando en clase sobre monumentos:

![Startup Edu4All, clase sobre monumentos, Torre Eiffel](../../../translated_images/startup.94d6b79cc4bb3f5afbf6e2ddfcf309aa5d1e256b5f30cc41d252024eaa9cc5dc.es.png)

usando un prompt como:

> "Perro junto a la Torre Eiffel en la luz del sol de la mañana temprano"

## ¿Qué son DALL-E y Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) y [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) son dos de los modelos de generación de imágenes más populares, que permiten usar prompts para generar imágenes.

### DALL-E

Comencemos con DALL-E, que es un modelo de IA Generativa que genera imágenes a partir de descripciones textuales.

> [DALL-E es una combinación de dos modelos, CLIP y atención difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP**, es un modelo que genera embeddings, que son representaciones numéricas de datos, a partir de imágenes y texto.

- **Atención difusa**, es un modelo que genera imágenes a partir de embeddings. DALL-E está entrenado en un conjunto de datos de imágenes y texto y puede ser utilizado para generar imágenes a partir de descripciones textuales. Por ejemplo, DALL-E puede generar imágenes de un gato con sombrero o un perro con un mohawk.

### Midjourney

Midjourney funciona de manera similar a DALL-E, generando imágenes a partir de prompts textuales. Midjourney también puede ser utilizado para generar imágenes con prompts como "un gato con sombrero" o "un perro con un mohawk".

![Imagen generada por Midjourney, paloma mecánica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito de la imagen: Wikipedia, imagen generada por Midjourney_

## ¿Cómo funcionan DALL-E y Midjourney?

Primero, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E es un modelo de IA Generativa basado en la arquitectura transformer con un _transformer autorregresivo_.

Un _transformer autorregresivo_ define cómo un modelo genera imágenes a partir de descripciones textuales, generando un píxel a la vez y luego utilizando los píxeles generados para generar el siguiente píxel. Este proceso pasa por múltiples capas en una red neuronal hasta que la imagen está completa.

Con este proceso, DALL-E controla atributos, objetos, características y más en la imagen que genera. Sin embargo, DALL-E 2 y 3 tienen más control sobre la imagen generada.

## Construyendo tu primera aplicación de generación de imágenes

Entonces, ¿qué se necesita para construir una aplicación de generación de imágenes? Necesitas las siguientes bibliotecas:

- **python-dotenv**, se recomienda encarecidamente usar esta biblioteca para mantener tus secretos en un archivo _.env_ separado del código.
- **openai**, esta biblioteca es la que usarás para interactuar con la API de OpenAI.
- **pillow**, para trabajar con imágenes en Python.
- **requests**, para ayudarte a realizar solicitudes HTTP.

## Crear y desplegar un modelo de Azure OpenAI

Si aún no lo has hecho, sigue las instrucciones en la página de [Microsoft Learn](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal) para crear un recurso y modelo de Azure OpenAI. Selecciona DALL-E 3 como modelo.

## Crear la aplicación

1. Crea un archivo _.env_ con el siguiente contenido:

   ```text
   AZURE_OPENAI_ENDPOINT=<your endpoint>
   AZURE_OPENAI_API_KEY=<your key>
   AZURE_OPENAI_DEPLOYMENT="dall-e-3"
   ```

   Localiza esta información en el Portal de Azure OpenAI Foundry para tu recurso en la sección "Deployments".

1. Reúne las bibliotecas anteriores en un archivo llamado _requirements.txt_ de la siguiente manera:

   ```text
   python-dotenv
   openai
   pillow
   requests
   ```

1. Luego, crea un entorno virtual e instala las bibliotecas:

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
    from openai import OpenAI, AzureOpenAI
    
    # import dotenv
    dotenv.load_dotenv()
    
    # configure Azure OpenAI service client 
    client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
    try:
        # Create an image by using the image generation API
        generation_response = client.images.generate(
                                prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                                size='1024x1024', n=1,
                                model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                              )

        # Set the directory for the stored image
        image_dir = os.path.join(os.curdir, 'images')

        # If the directory doesn't exist, create it
        if not os.path.isdir(image_dir):
            os.mkdir(image_dir)

        # Initialize the image path (note the filetype should be png)
        image_path = os.path.join(image_dir, 'generated-image.png')

        # Retrieve the generated image
        image_url = generation_response.data[0].url  # extract image URL from response
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

Vamos a explicar este código:

- Primero, importamos las bibliotecas que necesitamos, incluyendo la biblioteca de OpenAI, la biblioteca dotenv, la biblioteca requests y la biblioteca Pillow.

  ```python
  import openai
  import os
  import requests
  from PIL import Image
  import dotenv
  ```

- Luego, cargamos las variables de entorno desde el archivo _.env_.

  ```python
  # import dotenv
  dotenv.load_dotenv()
  ```

- Después, configuramos el cliente del servicio Azure OpenAI.

  ```python
  # Get endpoint and key from environment variables
  client = AzureOpenAI(
      azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
      api_key=os.environ['AZURE_OPENAI_API_KEY'],
      api_version = "2024-02-01"
      )
  ```

- A continuación, generamos la imagen:

  ```python
  # Create an image by using the image generation API
  generation_response = client.images.generate(
                        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                        size='1024x1024', n=1,
                        model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                      )
  ```

  El código anterior responde con un objeto JSON que contiene la URL de la imagen generada. Podemos usar la URL para descargar la imagen y guardarla en un archivo.

- Finalmente, abrimos la imagen y usamos el visor de imágenes estándar para mostrarla:

  ```python
  image = Image.open(image_path)
  image.show()
  ```

### Más detalles sobre la generación de la imagen

Veamos el código que genera la imagen en más detalle:

   ```python
     generation_response = client.images.generate(
                               prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',
                               size='1024x1024', n=1,
                               model=os.environ['AZURE_OPENAI_DEPLOYMENT']
                           )
   ```

- **prompt**, es el prompt textual que se utiliza para generar la imagen. En este caso, estamos usando el prompt "Conejo en caballo, sosteniendo una piruleta, en un prado con niebla donde crecen narcisos".
- **size**, es el tamaño de la imagen que se genera. En este caso, estamos generando una imagen de 1024x1024 píxeles.
- **n**, es el número de imágenes que se generan. En este caso, estamos generando dos imágenes.
- **temperature**, es un parámetro que controla la aleatoriedad del resultado de un modelo de IA Generativa. La temperatura es un valor entre 0 y 1 donde 0 significa que el resultado es determinista y 1 significa que el resultado es aleatorio. El valor predeterminado es 0.7.

Hay más cosas que puedes hacer con imágenes que cubriremos en la siguiente sección.

## Capacidades adicionales de generación de imágenes

Hasta ahora has visto cómo pudimos generar una imagen usando unas pocas líneas en Python. Sin embargo, hay más cosas que puedes hacer con imágenes.

También puedes hacer lo siguiente:

- **Realizar ediciones**. Proporcionando una imagen existente, una máscara y un prompt, puedes alterar una imagen. Por ejemplo, puedes agregar algo a una parte de una imagen. Imagina nuestra imagen del conejo, puedes agregarle un sombrero. Para hacerlo, debes proporcionar la imagen, una máscara (identificando la parte del área para el cambio) y un prompt textual que indique qué debe hacerse. 
> Nota: esto no es compatible con DALL-E 3.

Aquí hay un ejemplo usando GPT Image:

   ```python
   response = client.images.edit(
       model="gpt-image-1",
       image=open("sunlit_lounge.png", "rb"),
       mask=open("mask.png", "rb"),
       prompt="A sunlit indoor lounge area with a pool containing a flamingo"
   )
   image_url = response.data[0].url
   ```

  La imagen base solo contendría el salón con piscina, pero la imagen final tendría un flamenco:

<div style="display: flex; justify-content: space-between; align-items: center; margin: 20px 0;">
  <img src="../../../translated_images/sunlit_lounge.a75a0cb61749db0eddc1820c30a5fa9a3a9f48518cd7c8df4c2073e8c793bbb7.es.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/mask.1b2976ccec9e011eaac6cd3697d804a22ae6debba7452da6ba3bebcaa9c54ff0.es.png" style="width: 30%; max-width: 200px; height: auto;">
  <img src="../../../translated_images/sunlit_lounge_result.76ae02957c0bbeb860f1efdb42dd7f450ea01c6ae6cd70ad5ade4bab1a545d51.es.png" style="width: 30%; max-width: 200px; height: auto;">
</div>

- **Crear variaciones**. La idea es que tomes una imagen existente y pidas que se creen variaciones. Para crear una variación, proporcionas una imagen y un prompt textual y código como este:

  ```python
  response = openai.Image.create_variation(
    image=open("bunny-lollipop.png", "rb"),
    n=1,
    size="1024x1024"
  )
  image_url = response['data'][0]['url']
  ```

  > Nota: esto solo es compatible con OpenAI.

## Temperatura

La temperatura es un parámetro que controla la aleatoriedad del resultado de un modelo de IA Generativa. La temperatura es un valor entre 0 y 1 donde 0 significa que el resultado es determinista y 1 significa que el resultado es aleatorio. El valor predeterminado es 0.7.

Veamos un ejemplo de cómo funciona la temperatura, ejecutando este prompt dos veces:

> Prompt: "Conejo en caballo, sosteniendo una piruleta, en un prado con niebla donde crecen narcisos"

![Conejo en un caballo sosteniendo una piruleta, versión 1](../../../translated_images/v1-generated-image.a295cfcffa3c13c2432eb1e41de7e49a78c814000fb1b462234be24b6e0db7ea.es.png)

Ahora ejecutemos el mismo prompt nuevamente para ver que no obtendremos la misma imagen dos veces:

![Imagen generada de conejo en caballo](../../../translated_images/v2-generated-image.33f55a3714efe61dc19622c869ba6cd7d6e6de562e26e95b5810486187aace39.es.png)

Como puedes ver, las imágenes son similares, pero no idénticas. Probemos cambiar el valor de temperatura a 0.1 y veamos qué sucede:

```python
 generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2
    )
```

### Cambiando la temperatura

Entonces, intentemos hacer que la respuesta sea más determinista. Pudimos observar en las dos imágenes generadas que en la primera imagen hay un conejo y en la segunda imagen hay un caballo, por lo que las imágenes varían mucho.

Por lo tanto, cambiemos nuestro código y establezcamos la temperatura en 0, así:

```python
generation_response = client.images.create(
        prompt='Bunny on horse, holding a lollipop, on a foggy meadow where it grows daffodils',    # Enter your prompt text here
        size='1024x1024',
        n=2,
        temperature=0
    )
```

Ahora, cuando ejecutes este código, obtendrás estas dos imágenes:

- ![Temperatura 0, v1](../../../translated_images/v1-temp-generated-image.a4346e1d2360a056d855ee3dfcedcce91211747967cb882e7d2eff2076f90e4a.es.png)
- ![Temperatura 0, v2](../../../translated_images/v2-temp-generated-image.871d0c920dbfb0f1cb5d9d80bffd52da9b41f83b386320d9a9998635630ec83d.es.png)

Aquí puedes ver claramente cómo las imágenes se parecen más entre sí.

## Cómo definir límites para tu aplicación con meta-prompts

Con nuestra demostración, ya podemos generar imágenes para nuestros clientes. Sin embargo, necesitamos crear algunos límites para nuestra aplicación.

Por ejemplo, no queremos generar imágenes que no sean aptas para el trabajo o que no sean apropiadas para niños.

Podemos hacer esto con _meta-prompts_. Los meta-prompts son prompts textuales que se utilizan para controlar el resultado de un modelo de IA Generativa. Por ejemplo, podemos usar meta-prompts para controlar el resultado y asegurarnos de que las imágenes generadas sean aptas para el trabajo o apropiadas para niños.

### ¿Cómo funciona?

Ahora, ¿cómo funcionan los meta-prompts?

Los meta-prompts son prompts textuales que se utilizan para controlar el resultado de un modelo de IA Generativa. Se posicionan antes del prompt textual y se utilizan para controlar el resultado del modelo, integrándose en aplicaciones para controlar el resultado del modelo. Encapsulan la entrada del prompt y la entrada del meta-prompt en un solo prompt textual.

Un ejemplo de un meta-prompt sería el siguiente:

```text
You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.

(Input)

```

Ahora, veamos cómo podemos usar meta-prompts en nuestra demostración.

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

En el prompt anterior, puedes ver cómo todas las imágenes creadas consideran el meta-prompt.

## Tarea - habilitemos a los estudiantes

Introdujimos Edu4All al inicio de esta lección. Ahora es momento de habilitar a los estudiantes para que generen imágenes para sus evaluaciones.

Los estudiantes crearán imágenes para sus evaluaciones que contengan monumentos; qué monumentos crear depende de ellos. Se les pide a los estudiantes que usen su creatividad en esta tarea para colocar estos monumentos en diferentes contextos.

## Solución

Aquí hay una posible solución:
```python
import openai
import os
import requests
from PIL import Image
import dotenv
from openai import AzureOpenAI
# import dotenv
dotenv.load_dotenv()

# Get endpoint and key from environment variables
client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"],
  api_key=os.environ['AZURE_OPENAI_API_KEY'],
  api_version = "2024-02-01"
  )


disallow_list = "swords, violence, blood, gore, nudity, sexual content, adult content, adult themes, adult language, adult humor, adult jokes, adult situations, adult"

meta_prompt = f"""You are an assistant designer that creates images for children.

The image needs to be safe for work and appropriate for children.

The image needs to be in color.

The image needs to be in landscape orientation.

The image needs to be in a 16:9 aspect ratio.

Do not consider any input from the following that is not safe for work or appropriate for children.
{disallow_list}
"""

prompt = f"""{meta_prompt}
Generate monument of the Arc of Triumph in Paris, France, in the evening light with a small child holding a Teddy looks on.
""""

try:
    # Create an image by using the image generation API
    generation_response = client.images.generate(
        prompt=prompt,    # Enter your prompt text here
        size='1024x1024',
        n=1,
    )
    # Set the directory for the stored image
    image_dir = os.path.join(os.curdir, 'images')

    # If the directory doesn't exist, create it
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # Initialize the image path (note the filetype should be png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Retrieve the generated image
    image_url = generation_response.data[0].url  # extract image URL from response
    generated_image = requests.get(image_url).content  # download the image
    with open(image_path, "wb") as image_file:
        image_file.write(generated_image)

    # Display the image in the default image viewer
    image = Image.open(image_path)
    image.show()

# catch exceptions
except openai.BadRequestError as err:
    print(err)
```

## ¡Buen trabajo! Continúa aprendiendo

Después de completar esta lección, visita nuestra [colección de aprendizaje sobre IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir ampliando tus conocimientos sobre IA generativa.

Dirígete a la Lección 10, donde exploraremos cómo [crear aplicaciones de IA con poco código](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por garantizar la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.