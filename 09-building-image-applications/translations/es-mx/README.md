# Desarrollo de Aplicaciones de Generación de Imágenes

[![Desarrollo de Aplicaciones de Generación de Imágenes](../../images/09-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson9-gh?WT.mc_id=academic-105485-koreyst)

Los LLM no se limitan a la generación de texto. También es posible generar imágenes a partir de descripciones textuales. El uso de imágenes como modalidad puede ser muy útil en diversas áreas, desde tecnología médica hasta arquitectura, turismo, desarrollo de videojuegos y más. En este capítulo, analizaremos los dos modelos de generación de imágenes más populares: DALL-E y Midjourney.

## Introducción

En esta lección, abordaremos:

- Generación de imágenes y su utilidad.
- DALL-E y Midjourney: qué son y cómo funcionan.
- Cómo crear una aplicación de generación de imágenes.

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Desarrollar una aplicación de generación de imágenes.
- Definir los límites de tu aplicación con indicaciones meta.
- Trabajar con DALL-E y Midjourney.

## Por qué desarrollar una aplicación de generación de imágenes?

Las aplicaciones de generación de imágenes son una excelente manera de explorar las capacidades de la IA generativa. Se pueden utilizar, por ejemplo, para:

- **Edición y síntesis de imágenes**. Puedes generar imágenes para diversos casos de uso, como la edición y la síntesis de imágenes.

- **Aplicación en diversos sectores**. También se pueden utilizar para generar imágenes para diversos sectores, como la tecnología médica, el turismo, el desarrollo de videojuegos y más.

## Escenario: Edu4All

En esta lección, continuaremos trabajando con nuestra startup, Edu4All. Los estudiantes crearán imágenes para sus evaluaciones. La elección de las imágenes dependerá de ellos, pero podrían ser ilustraciones para su propio cuento de hadas, crear un nuevo personaje para su historia o ayudarles a visualizar sus ideas y conceptos.

Esto es lo que los estudiantes de Edu4All podrían generar, por ejemplo, si están trabajando en clase sobre monumentos:

![Edu4All startup, clase sobre monumentos, Torre Eiffel](../../images/startup.png?WT.mc_id=academic-105485-koreyst)

usando una consigna como:

> "Perro junto a la Torre Eiffel a primera hora de la mañana"

## Qué son DALL-E y Midjourney?

[DALL-E](https://openai.com/dall-e-2?WT.mc_id=academic-105485-koreyst) y [Midjourney](https://www.midjourney.com/?WT.mc_id=academic-105485-koreyst) son dos de los modelos de generación de imágenes más populares. Permiten usar indicaciones para generar imágenes.

### DALL-E

Comencemos con DALL-E, un modelo de IA generativa que genera imágenes a partir de descripciones de texto.

> [DALL-E es una combinación de dos modelos: CLIP y atención difusa](https://towardsdatascience.com/openais-dall-e-and-clip-101-a-brief-introduction-3a4367280d4e?WT.mc_id=academic-105485-koreyst).

- **CLIP** es un modelo que genera incrustaciones, que son representaciones numéricas de datos, a partir de imágenes y texto.

- **Atención difusa** es un modelo que genera imágenes a partir de incrustaciones. DALL-E se entrena con un conjunto de datos de imágenes y texto y puede utilizarse para generar imágenes a partir de descripciones de texto. Por ejemplo, DALL-E puede utilizarse para generar imágenes de un gato con sombrero o de un perro con cresta.

### Midjourney

Midjourney funciona de forma similar a DALL-E: genera imágenes a partir de indicaciones de texto. Midjourney también puede utilizarse para generar imágenes usando indicaciones como "un gato con sombrero" o "un perro con cresta".

![Imagen generada por Midjourney, paloma mecánica](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png/440px-Rupert_Breheny_mechanical_dove_eca144e7-476d-4976-821d-a49c408e4f36.png?WT.mc_id=academic-105485-koreyst)
_Crédito de la imagen: Wikipedia, imagen generada por Midjourney_

## Cómo funcionan DALL-E y Midjourney?

Primero, [DALL-E](https://arxiv.org/pdf/2102.12092.pdf?WT.mc_id=academic-105485-koreyst). DALL-E es un modelo de IA generativa basado en la arquitectura de transformador con un transformador autorregresivo.

Un transformador autorregresivo define cómo un modelo genera imágenes a partir de descripciones de texto: genera un píxel a la vez y luego utiliza los píxeles generados para generar el siguiente. Pasa por múltiples capas en una red neuronal hasta completar la imagen.

Con este proceso, DALL-E controla atributos, objetos, características y más en la imagen que genera. Sin embargo, DALL-E 2 y 3 tienen mayor control sobre la imagen generada.

## Desarrollando tu primera aplicación de generación de imágenes

Qué se necesita para desarrollar una aplicación de generación de imágenes? Necesita las siguientes bibliotecas:

- **python-dotenv**: se recomienda usar esta biblioteca para guardar sus secretos en un archivo _.env_, separado del código.
- **openai**: esta biblioteca es la que usará para interactuar con la API de OpenAI.
- **pillow**: para trabajar con imágenes en Python.
- **requests**: para realizar solicitudes HTTP.

1. Cree un archivo _.env_ con el siguiente contenido:

```text
AZURE_OPENAI_ENDPOINT=<su punto de conexión>
AZURE_OPENAI_API_KEY=<su clave>
```

Encuentre esta información en el Portal de Azure para su recurso, en la sección "Claves y punto de conexión".

2. Recopile las bibliotecas anteriores en un archivo llamado _requirements.txt_ de la siguiente manera:

```text
python-dotenv
openai
pillow
requests
```

3. A continuación, cree un entorno virtual e instale las bibliotecas:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Para Windows, use los siguientes comandos para crear y activar su entorno virtual:

```bash
python3 -m venv venv
venv\Scripts\activate.bat
```

4. Agregue el siguiente código al archivo _app.py_:

```python
import openai
import os
import requests
from PIL import Image
import dotenv

# import dotenv
dotenv.load_dotenv()

# Obtener el punto final y la clave de las variables de entorno
openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

# Asignar la versión de la API (actualmente, DALL-E es compatible con (Solo la versión de la API de vista previa del 01/06/2023)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

try:
    # Crear una imagen usando la API de generación de imágenes
    generation_response = openai.Image.create(
    prompt = 'Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos', # Introduce el texto del mensaje aquí
    size = '1024x1024',
    n = 2,
    temperature = 0,
    )
    # Establecer el directorio para la imagen almacenada
    image_dir = os.path.join(os.curdir, 'images')

    # Si el directorio no existe, créalo
    if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

    # Inicializar la ruta de la imagen (ten en cuenta que el tipo de archivo debe ser png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Recuperar la imagen generada
    image_url = generation_response["data"][0]["url"] # Extraer la URL de la imagen de la respuesta
    generated_image = requests.get(image_url).content # Descargar la imagen
    with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

    # Mostrar la imagen en el visor de imágenes predeterminado
    image = Image.open(image_path)
    image.show()

# Capturar excepciones
except openai.InvalidRequestError as err:
    print(err)

```

Expliquemos este código:

- Primero, importamos las bibliotecas necesarias, incluyendo las bibliotecas OpenAI, dotenv, requests y Pillow.

```python
import openai
import os
import requests
from PIL import Image
import dotenv
```

- A continuación, cargamos las variables de entorno desde el archivo _.env_.

```python
# import dotenv
dotenv.load_dotenv()
```

- Después, configuramos el punto final, la clave para la API de OpenAI, la versión y el tipo.

```python
# Obtener el punto de conexión y la clave de las variables de entorno
openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
openai.api_key = os.environ['AZURE_OPENAI_API_KEY']

# Agregar la versión y el tipo, específicos de Azure
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'
```

- A continuación, generamos la imagen:

```python
# Crear una imagen usando la API de generación de imágenes
generation_response = openai.Image.create(
prompt='Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos', # Introduce el texto del mensaje aquí
size='1024x1024',
n=2,
temperature=0,
)
```

El El código anterior responde con un objeto JSON que contiene la URL de la imagen generada. Podemos usar la URL para descargar la imagen y guardarla en un archivo.

- Finalmente, abrimos la imagen y usamos el visor de imágenes estándar para mostrarla:

```python
image = Image.open(image_path)
image.show()
```

### Más detalles sobre la generación de la imagen

Veamos el código que genera la imagen con más detalle:

```python
generation_response = openai.Image.create(
prompt='Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos', # Introduce el texto del mensaje aquí
size='1024x1024',
n=2,
temperature=0,
)
```

- **prompt / indicacion** es el mensaje de texto que se utiliza para generar la imagen. En este caso, usamos el mensaje "Conejito a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos".
- **tamaño** es el tamaño de la imagen generada. En este caso, generamos una imagen de 1024x1024 píxeles.
- **n** es el número de imágenes generadas. En este caso, generamos dos imágenes.
- **temperatura** es un parámetro que controla la aleatoriedad de la salida de un modelo de IA generativa. La temperatura es un valor entre 0 y 1, donde 0 significa que la salida es determinista y 1 significa que la salida es aleatoria. El valor predeterminado es 0,7.

Hay más funciones que se pueden realizar con las imágenes, que abordaremos en la siguiente sección.

## Funciones adicionales de la generación de imágenes

Hasta ahora has visto cómo generamos una imagen con solo unas pocas líneas en Python. Sin embargo, hay más cosas que puedes hacer con las imágenes.

También puedes hacer lo siguiente:

- **Edición**. Al proporcionar una máscara y una indicación a una imagen existente, puedes modificarla. Por ejemplo, puedes añadir algo a una parte de la imagen. Imagina la imagen de nuestro conejo: puedes añadirle un sombrero. Para ello, proporciona la imagen, una máscara (que identifica la parte del área que se va a modificar) y una indicación de texto que indique qué se debe hacer.

```python
response = openai.Image.create_edit(
image=open("base_image.png", "rb"),
mask=open("mask.png", "rb"),
prompt="Imagen de un conejo con sombrero.",
n=1,
size="1024x1024"
)
image_url = response['data'][0]['url']
```

La imagen base solo contendría el conejo, pero la imagen final tendría el sombrero.

- **Crear variaciones**. La idea es tomar una imagen existente y solicitar la creación de variaciones. Para crear una variación, se proporciona una imagen, un mensaje de texto y se escribe el código de la siguiente manera:

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

La temperatura es un parámetro que controla la aleatoriedad de la salida de un modelo de IA generativa. La temperatura es un valor entre 0 y 1, donde 0 significa que la salida es determinista y 1, que es aleatoria. El valor predeterminado es 0,7.

Veamos un ejemplo de cómo funciona la temperatura ejecutando este comando dos veces:

> Comando: "Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos"

![Conejo a caballo sosteniendo una piruleta, versión 1](../../images/v1-generated-image.png?WT.mc_id=academic-105485-koreyst)

Ahora ejecutemos el mismo comando solo para asegurarnos de que no obtenemos la misma imagen dos veces:

![Imagen generada de un conejo a caballo](../../images/v2-generated-image.png?WT.mc_id=academic-105485-koreyst)

Como pueden ver, las imágenes son similares, pero no iguales. Intentemos cambiar el valor de temperatura a 0,1 y veamos qué sucede:

```python
generation_response = openai.Image.create(
prompt='Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos', # Introduce el texto del mensaje aquí
size='1024x1024',
n=2
)
```

### Cambio de temperatura

Intentemos que la respuesta sea más determinista. De las dos imágenes que generamos, observamos que en la primera hay un conejo y en la segunda, un caballo, por lo que las imágenes varían considerablemente.

Por lo tanto, modifiquemos nuestro código y establezcamos la temperatura en 0, de la siguiente manera:

```python
generation_response = openai.Image.create(
prompt='Conejo a caballo, sosteniendo una piruleta, en un prado brumoso donde crecen narcisos', # Introduce el texto del mensaje aquí
size='1024x1024',
n=2,
temperature=0
)
```

Ahora, al ejecutar este código, obtendrás estas dos imágenes:

- ![Temperature 0, v1](../../images/v1-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)
- ![Temperature 0 , v2](../../images/v2-temp-generated-image.png?WT.mc_id=academic-105485-koreyst)

Aquí puedes ver claramente cómo se ven las imágenes Se parecen más entre sí.

## Cómo definir límites para tu aplicación con indicaciones meta

Con nuestra demo, ya podemos generar imágenes para nuestros clientes. Sin embargo, necesitamos establecer algunos límites para nuestra aplicación.

Por ejemplo, no queremos generar imágenes que no sean seguras para el trabajo o que no sean apropiadas para niños.

Podemos lograr esto con _indicaciones meta_. Los indicaciones meta son indicaciones de texto que se utilizan para controlar la salida de un modelo de IA generativa. Por ejemplo, podemos usar indicaciones meta para controlar la salida y garantizar que las imágenes generadas sean seguras para el trabajo o apropiadas para niños.

### Cómo funciona?

Ahora bien, cómo funcionan los indicaciones meta?

Los indicaciones meta son indicaciones de texto que se utilizan para controlar la salida de un modelo de IA generativa. Se colocan antes de la indicación de texto y se utilizan para controlar la salida del modelo, integrándose en las aplicaciones para controlar la salida del modelo. Encapsulando la entrada de la indicación y la entrada del indicaciones meta en una sola indicación de texto.

Un ejemplo de metaprompt sería el siguiente:

```texto
Eres asistente de diseño y creas imágenes para niños.

La imagen debe ser segura para el trabajo y apropiada para niños.

La imagen debe ser a color.

La imagen debe tener orientación horizontal.

La imagen debe tener una relación de aspecto de 16:9.

No consideres ninguna entrada de las siguientes que no sea segura para el trabajo o apropiada para niños.

(Entrada)

```

Ahora, veamos cómo podemos usar las indicaciones meta en nuestra demostración. 

```python
disallow_list = "espadas, violencia, sangre, escenas sangrientas, desnudez, contenido sexual, contenido para adultos, temas para adultos, lenguaje para adultos, humor para adultos, chistes para adultos, situaciones para adultos, contenido para adultos"

meta_prompt =f"""Eres un asistente de diseño que crea imágenes para niños.

La imagen debe ser segura para el trabajo y apropiada para niños.

La imagen debe ser a color.

La imagen debe tener orientación horizontal.

La imagen debe tener una relación de aspecto de 16:9.

No consideres ninguna entrada de lo siguiente que no sea segura para el trabajo o apropiada para niños.
{disallow_list}
"""

prompt = f"{meta_prompt}
Crea una imagen de un conejo a caballo con una piruleta en la mano"

# TODO añadir solicitud para generar la imagen
```

A partir del mensaje anterior, puedes ver cómo todas las imágenes que se crean consideran el metaprompt.

## Tarea: Capacitemos a los estudiantes

Presentamos Edu4All al principio de esta lección. Ahora es el momento de capacitar a los estudiantes para generar imágenes para sus evaluaciones.

Los estudiantes crearán imágenes para sus evaluaciones que contengan monumentos. La elección de los monumentos depende de ellos. Se les pide que usen su creatividad en esta tarea para ubicar estos monumentos en diferentes contextos.

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

# Obtener el punto final y la clave de las variables de entorno
openai.api_base = "<reemplazar con punto final>"
openai.api_key = "<reemplazar con clave de API>"

# Asignar la versión de la API (DALL-E actualmente solo es compatible con la versión preliminar de la API del 01/06/2023)
openai.api_version = '2023-06-01-preview'
openai.api_type = 'azure'

disallow_list = "espadas, violencia, sangre, escenas sangrientas, desnudez, contenido sexual, contenido para adultos, temas para adultos, lenguaje para adultos, humor para adultos, chistes para adultos, situaciones para adultos, contenido para adultos"

meta_prompt = f"""Eres asistente de diseño y creas imágenes para niños.

La imagen debe ser segura para el trabajo y apropiada para niños.

La imagen debe ser a color.

La imagen debe tener orientación horizontal.

La imagen debe tener una relación de aspecto de 16:9.

No consideres ninguna entrada de la siguiente lista que no sea segura para el trabajo o apropiada para niños.
{disallow_list}"""

prompt = f"""{metaprompt}
Genera el monumento del Arco del Triunfo en París, Francia, al atardecer, con un niño pequeño sosteniendo un osito de peluche observando.
"""

try:
    # Crea una imagen usando la API de generación de imágenes
    generation_response = openai.Image.create(
    prompt=prompt, # Introduce el texto de la solicitud aquí
    size='1024x1024',
    n=2,
    temperature=0,
    )
    # Establece el directorio para la imagen almacenada
    image_dir = os.path.join(os.curdir, 'images')

    # Si el directorio no existe, créalo
    if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

    # Inicializa la ruta de la imagen (ten en cuenta que el tipo de archivo debe ser png)
    image_path = os.path.join(image_dir, 'generated-image.png')

    # Recupera la imagen generada
    image_url = generation_response["data"][0]["url"] # Extrae la URL de la imagen de la respuesta
    generated_image = requests.get(image_url).content # Descarga la imagen
    with open(image_path, "wb") as image_file:
    image_file.write(generated_image)

    # Mostrar la imagen en el visor de imágenes predeterminado
    image = Image.open(image_path)
    image.show()

# Capturar excepciones
except openai.InvalidRequestError as err:
    print(err)
```

## Buen trabajo! Continúa aprendiendo

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos sobre IA generativa.

Dirígete a la Lección 10, donde veremos cómo [crear aplicaciones de IA con poco código](../10-building-low-code-ai-applications/README.md?WT.mc_id=academic-105485-koreyst)