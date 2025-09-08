<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:23:12+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "es"
}
-->

# Generar código para una API web en Python

Este documento explica cómo crear una API web básica utilizando Python y frameworks populares.

## Requisitos previos

- Conocimientos básicos de Python
- Familiaridad con HTTP y APIs REST
- Instalación de Python 3.6 o superior

## Paso 1: Configurar el entorno

Primero, crea un entorno virtual para tu proyecto:

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
```

Luego, instala Flask, un microframework para crear APIs:

```bash
pip install Flask
```

## Paso 2: Crear la aplicación Flask

Crea un archivo llamado `app.py` y añade el siguiente código:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos de ejemplo
items = [
    {"id": 1, "nombre": "Item 1"},
    {"id": 2, "nombre": "Item 2"}
]

@app.route('/items', methods=['GET'])
def obtener_items():
    return jsonify(items)

@app.route('/items', methods=['POST'])
def crear_item():
    nuevo_item = request.get_json()
    items.append(nuevo_item)
    return jsonify(nuevo_item), 201

if __name__ == '__main__':
    app.run(debug=True)
```

## Paso 3: Ejecutar la aplicación

Para iniciar el servidor, ejecuta:

```bash
python app.py
```

La API estará disponible en `http://127.0.0.1:5000/items`.

## Paso 4: Probar la API

Puedes usar herramientas como `curl` o Postman para probar los endpoints.

Por ejemplo, para obtener la lista de items:

```bash
curl http://127.0.0.1:5000/items
```

Para crear un nuevo item:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"id":3,"nombre":"Item 3"}' http://127.0.0.1:5000/items
```

## Notas finales

Este es un ejemplo básico para comenzar. Para proyectos más complejos, considera usar frameworks como FastAPI o Django REST Framework.
```python
#import necessary libraries
import flask
from flask import request, jsonify

#create an instance of the Flask class
app = flask.Flask(__name__)

#create an endpoint for the API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #get the request data
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#function to process the data
def process_data(data):
    #process the data
    result = {'result': 'success'}

    #return the result
    return result

#run the Flask app
if __name__ == '__main__':
    app.run()

```

Ejecutar el prompt nuevamente nos da este resultado:

```python
#import necessary libraries
import flask
from flask import request, jsonify

#create a Flask app
app = flask.Flask(__name__)

#create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    #get the data from the request
    data = request.get_json()

    #process the data
    result = process_data(data)

    #return the result
    return jsonify(result)

#define the process_data function
def process_data(data):
    #do something with the data
    result = data + 1

    #return the result
    return result

#run the app
if __name__ == '__main__':
    app.run()

```

Solo hay una pequeña diferencia entre estas dos salidas. Hagamos lo contrario esta vez, establezcamos la temperatura en 0.9:

```python
# Import necessary libraries
import flask
from flask import request, jsonify

# Create a Flask app
app = flask.Flask(__name__)

# Create a route for the API
@app.route('/api', methods=['GET'])
def api_call():
    # Get the data from the request
    data = request.args

    # Process the data
    result = process_data(data)

    # Return the result
    return jsonify(result)

# Function to process the data
def process_data(data):
    # Do something with the data
    result = data + 1

    # Return the result
    return result

# Run the app
if __name__ == '__main__':
    app.run()

```

y el segundo intento con un valor de temperatura de 0.9:

```python
import flask
from flask import request, jsonify

# create the Flask app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# create some test data
books = [
    {'id': 0, 'title': 'A Fire Upon The Deep', 'author': 'Vernor Vinge', 'first_sentence': 'The coldsleep itself was dreamless.', 'year_published': '1992'},
    {'id': 1, 'title': 'The Ones Who Walk Away From Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'to wound the autumnal city.', 'published': '1975'}
]

# create an endpoint
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to our book API!</h1>'''

@app.route('/api/v1/resources/books

```

Como puedes ver, los resultados no podrían ser más variados.

> Note que hay más parámetros que puedes cambiar para variar la salida, como top-k, top-p, penalización por repetición, penalización de longitud y penalización de diversidad, pero estos están fuera del alcance de este currículo.

## Buenas prácticas

Hay muchas prácticas que puedes aplicar para intentar obtener lo que quieres. Encontrarás tu propio estilo a medida que uses el prompting cada vez más.

Además de las técnicas que hemos cubierto, hay algunas buenas prácticas a considerar al hacer prompts a un LLM.

Aquí algunas buenas prácticas a tener en cuenta:

- **Especifica el contexto**. El contexto importa, mientras más puedas especificar como dominio, tema, etc., mejor.
- Limita la salida. Si quieres un número específico de elementos o una longitud determinada, especifícalo.
- **Especifica tanto qué como cómo**. Recuerda mencionar tanto qué quieres como cómo lo quieres, por ejemplo: "Crea una API Web en Python con rutas products y customers, divídela en 3 archivos".
- **Usa plantillas**. A menudo querrás enriquecer tus prompts con datos de tu empresa. Usa plantillas para esto. Las plantillas pueden tener variables que reemplazas con datos reales.
- **Escribe correctamente**. Los LLM pueden darte una respuesta correcta, pero si escribes bien, obtendrás una mejor respuesta.

## Tarea

Aquí tienes un código en Python que muestra cómo construir una API simple usando Flask:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()
```

Usa un asistente de IA como GitHub Copilot o ChatGPT y aplica la técnica de "auto-mejora" para mejorar el código.

## Solución

Intenta resolver la tarea añadiendo prompts adecuados al código.

> [!TIP]
> Formula un prompt para pedir que lo mejore, es buena idea limitar cuántas mejoras quieres. También puedes pedir que lo mejore de una forma específica, por ejemplo arquitectura, rendimiento, seguridad, etc.

[Solución](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificación de conocimientos

¿Por qué usaría chain-of-thought prompting? Muéstrame 1 respuesta correcta y 2 respuestas incorrectas.

1. Para enseñar al LLM cómo resolver un problema.  
1. B, Para enseñar al LLM a encontrar errores en el código.  
1. C, Para instruir al LLM a proponer diferentes soluciones.

A: 1, porque chain-of-thought consiste en mostrar al LLM cómo resolver un problema proporcionándole una serie de pasos, y problemas similares y cómo se resolvieron.

## 🚀 Desafío

Acabas de usar la técnica de auto-mejora en la tarea. Toma cualquier programa que hayas creado y considera qué mejoras te gustaría aplicarle. Ahora usa la técnica de auto-mejora para aplicar los cambios propuestos. ¿Qué te pareció el resultado, mejor o peor?

## ¡Excelente trabajo! Continúa aprendiendo

Después de completar esta lección, revisa nuestra [colección de aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos en IA Generativa.

Dirígete a la Lección 6 donde aplicaremos nuestro conocimiento de Prompt Engineering construyendo [aplicaciones de generación de texto](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas derivadas del uso de esta traducción.