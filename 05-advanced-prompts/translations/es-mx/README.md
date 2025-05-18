# Creación de Indicaciones Avanzados

[![Creación de Indicaciones Avanzados](../../images/05-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson5-gh?WT.mc_id=academic-105485-koreyst?WT.mc_id=academic-105485-koreyst)

Repasemos algunos aprendizajes del capítulo anterior:

> La _ingeniería de indicaciones_ es el proceso mediante el cual **guiamos al modelo hacia respuestas más relevantes** proporcionando instrucciones o contexto más útiles.

También hay dos pasos para escribir indicaciones: construir la indicacion proporcionando contexto relevante y la segunda parte es la _optimización_, cómo mejorar gradualmente el indicacion.

En este punto, tenemos una comprensión básica de cómo escribir indicaciones, pero necesitamos profundizar. En este capítulo, pasarás de probar varios indicaciones a entender por qué un indicacion es mejor que otro. Aprenderás a construir indicaciones siguiendo algunas técnicas básicas que se pueden aplicar a cualquier LLM.

## Introducción

En este capítulo, cubriremos los siguientes temas:

- Ampliar tu conocimiento de la ingeniería de indicaciones aplicando diferentes técnicas a tus indicaciones.
- Configurar tus indicaciones para variar la salida.

## Objetivos de aprendizaje

Después de completar esta lección, podrás:

- Aplicar técnicas de ingeniería de indicacion que mejoran el resultado de tus indicaciones.
- Realizar indicaciones que sea variado o determinista.

## Ingeniería de Indicaciones

La ingeniería de indicaciones es el proceso de crear indicaciones que produzcan el resultado deseado. Hay más en la ingeniería de indicaciones que simplemente escribir un texto. La ingeniería de indicaciones no es una disciplina de ingeniería, sino un conjunto de técnicas que puedes aplicar para obtener el resultado deseado.

### Un ejemplo de indicacion

Tomemos una indicacion básica como esta:

> Genera 10 preguntas sobre geografía.

En este indicacion, en realidad estás aplicando un conjunto de técnicas diferentes.

Analicemos esto por partes.

- **Contexto**: especificas que debe ser sobre "geografía".
- **Limitar la salida**: quieres no más de 10 preguntas.

### Limitaciones de la indicacion simple

Puede que obtengas o no el resultado deseado. Obtendrás preguntas generadas, pero la geografía es un tema amplio y puede que no consigas lo que deseas por las siguientes razones:

- **Tema amplio**: no sabes si será sobre países, capitales, ríos, etc.
- **Formato**: y si querías que las preguntas se formatearan de cierta manera?

Como puedes ver, hay mucho que considerar al crear indicaciones.

Hasta ahora, hemos visto un ejemplo de indicacion simple, pero la IA generativa es capaz de mucho más para ayudar a personas en una variedad de roles e industrias. Exploremos algunas técnicas básicas a continuación.

### Técnicas para indicaciones

Primero, debemos entender que el indicaciones es una propiedad _emergente_ de un LLM, lo que significa que no es una función integrada en el modelo, sino algo que descubrimos al usar el modelo.

Hay algunas técnicas básicas que podemos usar para hacer indicaciones a un LLM. Vamos a explorarlas.

- **Indicacion de cero ejemplos**: esta es la forma más básica de indicaciones. Es un solo indicacion que solicita una respuesta del LLM basada únicamente en sus datos de entrenamiento.
- **Indicacion de pocos ejemplos**: este tipo de indicaciones guía al LLM proporcionando 1 o más ejemplos en los que puede basarse para generar su respuesta.
- **Cadena de pensamiento**: este tipo de indicaciones le indica al LLM cómo descomponer un problema en pasos.
- **Conocimiento generado**: para mejorar la respuesta de un indicacion, puedes proporcionar hechos o conocimientos generados además de tu indicacion.
- **De lo mínimo a lo máximo**: al igual que la cadena de pensamiento, esta técnica consiste en dividir un problema en una serie de pasos y luego pedir que se ejecuten en orden.
- **Auto-mejora**: esta técnica consiste en criticar la salida del LLM y luego pedirle que la mejore.
- **Indicacion mayéutico**: lo que quieres aquí es asegurarte de que la respuesta del LLM sea correcta y le pides que explique varias partes de la respuesta. Esta es una forma de auto-mejora.

### Indicacion de cero ejemplos

Este estilo de indicaciones es muy simple, consiste en un solo indicacion. Esta técnica es probablemente la que estás usando cuando empiezas a aprender sobre LLMs. Aquí tienes un ejemplo:

- indicacion: "Qué es el Álgebra?"
- Respuesta: "El álgebra es una rama de las matemáticas que estudia los símbolos matemáticos y las reglas para manipular estos símbolos."

### indicacion de pocos ejemplos

Este estilo de indicaciones ayuda al modelo proporcionando algunos ejemplos junto con la solicitud. Consiste en un solo indicacion con datos adicionales específicos de la tarea. Aquí tienes un ejemplo:

- Indicacion: "Escribe un poema al estilo de Shakespeare. Aquí tienes algunos ejemplos de sonetos shakesperianos:
  Soneto 18: 'Compararte con un día de verano? Eres más hermoso y más templado...'
  Soneto 116: 'No admitiré impedimentos en la unión de almas verdaderas. El amor no es amor que cambia cuando encuentra cambios...'
  Soneto 132: 'Tus ojos amo, y ellos, como compadeciéndose de mí, sabiendo que tu corazón me atormenta con desdén,...'
  Ahora, escribe un soneto sobre la belleza de la luna."
- Respuesta: "Sobre el cielo, la luna suavemente brilla, En luz de plata que lanza su gracia gentil,..."

Los ejemplos le proporcionan al LLM el contexto, formato o estilo de la salida deseada. Ayudan al modelo a entender la tarea específica y a generar respuestas más precisas y relevantes.

### Cadena de pensamiento

La cadena de pensamiento es una técnica muy interesante ya que se trata de guiar al LLM a través de una serie de pasos. La idea es instruir al LLM de tal manera que entienda cómo hacer algo. Considera el siguiente ejemplo, con y sin cadena de pensamiento:

- Indicacion: "Alicia tiene 5 manzanas, lanza 3, da 2 a Bob y Bob le devuelve una. Cuántas manzanas tiene Alicia?"
- Respuesta: 5

El LLM responde con 5, lo cual es incorrecto. La respuesta correcta es 1 manzana, dado el cálculo (5 - 3 - 2 + 1 = 1).

Entonces, cómo podemos enseñarle al LLM a hacer esto correctamente?

Probemos con cadena de pensamiento. Aplicar esta técnica significa:

1. Dar al LLM un ejemplo similar.
2. Mostrar el cálculo y cómo se realiza correctamente.
3. Proporcionar el indicacion original.

Así sería:

- Indicacion: "Lisa tiene 7 manzanas, lanza 1 manzana, da 4 a Bart y Bart le devuelve una:
  7 - 1 = 6  
  6 - 4 = 2  
  2 + 1 = 3  
  Alicia tiene 5 manzanas, lanza 3, da 2 a Bob y Bob le devuelve una. Cuántas manzanas tiene Alicia?"
- Respuesta: 1

Nota cómo escribimos indicaciones sustancialmente más largos con otro ejemplo, un cálculo y luego el indicacion original, y llegamos a la respuesta correcta: 1.

Como puedes ver, la cadena de pensamiento es una técnica muy poderosa.

### Conocimiento generado

Muchas veces, cuando quieres construir un indicacion, deseas hacerlo usando los datos de tu propia empresa. Quieres que parte del indicacion provenga de la empresa y la otra parte sea el indicacion en sí.

Como ejemplo, así podría lucir tu indicacion si trabajas en el sector de seguros:

```text
{{empresa}}: {{nombre_empresa}}
{{productos}}:
{{lista_productos}}
Por favor sugiere un seguro dado el siguiente presupuesto y requisitos:
Presupuesto: {{presupuesto}}
Requisitos: {{requisitos}}
```

Arriba, puede ver cómo se construye la solicitud usando una plantilla. En la plantilla hay varias variables, denotadas por `{{variable}}`, que se reemplazarán con valores reales de la API de la empresa.

A continuación, se muestra un ejemplo de cómo se vería la solicitud una vez que las variables se hayan reemplazado con el contenido de su empresa:

```texto
Compañía de seguros: ACME Insurance
Productos de seguro (costo mensual):
- Auto, económico, 500 USD
- Auto, caro, 1100 USD
- Hogar, económico, 600 USD
- Hogar, caro, 1200 USD
- Vida, económico, 100 USD

Sugiera un seguro según el siguiente presupuesto y requisitos:
Presupuesto: $1000
Requisitos: Seguro de auto, hogar y vida
```

Al ejecutar esta solicitud en un LLM, se obtendrá una respuesta como esta:

```resultado
Dados el presupuesto y los requisitos, sugerimos el siguiente paquete de seguros de ACME Insurance:
- Auto, económico, $500 USD
- Hogar, económico, $600 USD
- Vida, económico, $100 USD
Costo total: $1,200 USD
```

Como puede ver, también sugiere el seguro de vida, lo cual no debería ocurrir. Este resultado indica que debemos optimizar la solicitud modificándola para que sea más clara sobre lo que permite. Tras varias pruebas, llegamos a la siguiente solicitud:

```texto
Compañía de seguros: ACME Insurance
Productos de seguro (costo mensual):
- Tipo: Auto, económico, costo: 500 USD
- Tipo: Auto, caro, costo: 1100 USD
- Tipo: Hogar, económico, costo: 600 USD
- Tipo: Hogar, caro, costo: 1200 USD
- Tipo: Vida, económico, costo: 100 USD

Por favor, sugiera un seguro según el siguiente presupuesto y requisitos:
Presupuesto: $1000. Limite la elección a los tipos: Auto, Hogar.
```

Observe cómo añadir _typo_ y _costo_, así como usar la palabra clave _restringir_, ayuda al LLM a comprender lo que queremos.

Ahora obtenemos la siguiente respuesta:

```output
Dados el presupuesto y los requisitos, sugerimos el seguro de coche económico, que cuesta 500 USD al mes.
```

El objetivo de este ejemplo era mostrar que, aunque utilizamos una técnica básica como el _conocimiento generado_, en la mayoría de los casos necesitamos optimizar la solicitud para obtener el resultado deseado.

### De menor a mayor

La idea de la incitación de menor a mayor es descomponer un problema mayor en subproblemas. De esta manera, se ayuda al estudiante de maestría en cómo abordar el problema principal. Un buen ejemplo podría ser la ciencia de datos, donde se le puede pedir al estudiante de maestría que divida un problema de la siguiente manera:

> Incitación: Cómo realizar ciencia de datos en 5 pasos?

Con la respuesta de tu asistente de IA:

1. Recopilar datos
2. Limpiar datos
3. Analizar datos
4. Graficar datos
5. Presentar datos

### Autorefinar, criticar los resultados

Con las IA generativas y los LLM, no se puede confiar en el resultado. Es necesario verificarlo. Después de todo, el LLM solo presenta lo que probablemente se diga a continuación, no lo que es correcto. Por lo tanto, es recomendable pedirle al LLM que se autocritique, lo que nos lleva a la técnica de autorefinar.

El proceso funciona de la siguiente manera:

1. Indicación inicial: pedirle al LLM que resuelva un problema
2. El LLM responde
3. Se critica la respuesta y se le pide a la IA que mejore
4. El LLM responde de nuevo, esta vez considerando la crítica y sugiriendo las soluciones que encontró

Puede repetir este proceso tantas veces como desee.

Aquí hay un ejemplo de esta técnica:

> Indicacion: "Crear una API web de Python con rutas de productos y clientes"

Respuesta de la IA:

```python
import flask
app = Flask(__name__)

@app.route('/products')
def products():
    return 'Products'

@app.route('/customers')
def customers():
    return 'Customers'
```

> Indicacion: Sugiera 3 mejoras al código anterior

Respuesta de la IA:

```texto
Claro, aquí tienes tres sugerencias para mejorar el código:

Importar el módulo correcto: La primera línea debería importar Flask en lugar de flask. La sentencia de importación correcta debería ser `from flask import Flask`.

Añadir una función principal: Añadir un bloque `if __name__ == '__main__':` al final del archivo para ejecutar la aplicación cuando se ejecute el archivo.

Usar cadenas f: Usar cadenas f para dar formato a las sentencias de retorno en las funciones de ruta. Por ejemplo, `return 'Products'` se puede cambiar a `return f'This is the {request.path} page'. 
```

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/products')
def products():
    return f'Esta es la página {request.path}'

@app.route('/customers')
def customers():
    return f'Esta es la página {request.path}'

if __name__ == '__main__':
    app.run()
```

Como puede ver, la respuesta de IA anterior mejora el primer código sugerido gracias a la crítica de la primera respuesta.

### Incitación mayéutica

La incitación mayéutica es una técnica similar al autorefinamiento, pero consiste más en pedirle al LLM que se explique. El objetivo es reducir las inconsistencias en la salida del LLM para garantizar que llegue a la respuesta correcta. El flujo de trabajo a seguir es:

1. Pedirle al LLM que responda una pregunta.
2. Para cada parte de la respuesta, pedirle al LLM que la explique con más detalle.
3. Si hay inconsistencias, descartar las partes inconsistentes.

Repetir los pasos 2 y 3 hasta que haya revisado todas las partes y esté satisfecho con la respuesta.

Aquí hay un ejemplo de incitación:

> Incitación: Cómo puedo crear un plan de crisis para mitigar una pandemia en 5 pasos?

Respuesta del LLM:

```texto
1. Identificar los riesgos
2. Identificar a las partes interesadas
3. Identificar los recursos
4. Identificar las acciones
5. Identificar los canales de comunicación
```

Se identifican 5 pasos, pero podemos determinar si es correcto? Pidamos al LLM que explique cada paso:

> Pregunta: Explique el primer paso con más detalle. Cuáles son los riesgos específicos de una pandemia?

```texto
Los riesgos son los siguientes:

- Pérdida de vidas
- Pérdida de negocios
- Pérdida de reputación
- Pérdida de clientes
- Pérdida de empleados
```

En este punto, queremos asegurarnos de que el LLM sea correcto, por lo que le solicitamos que explique el primer riesgo con más detalle y esperamos que sea coherente con la respuesta anterior:

> Pregunta: En una pandemia, cuál es el mayor riesgo y por qué?

``texto
El mayor riesgo es la pérdida de vidas, ya que es lo más importante que debemos proteger.
```

> Cuáles son los dos mayores riesgos en una pandemia?

``texto
Los dos mayores riesgos son la pérdida de vidas y la pérdida de negocios.
```

En este punto, el LLM es coherente y menciona "vida" y "negocios" como los dos riesgos principales. Ahora podemos continuar con el siguiente paso con bastante confianza. Sin embargo, no debemos confiar ciegamente en el LLM; siempre debemos verificar el resultado.

## Varía tu salida

Los LLM no son deterministas por naturaleza, lo que significa que obtendrá resultados diferentes cada vez que ejecute el mismo mensaje. Pruebe el siguiente mensaje, por ejemplo:

> "Generar código para una API web de Python"

```python
# Importar los módulos necesarios
import flask
from flask import request, jsonify

# Crear una aplicación Flask
app = flask.Flask(__name__)

# Crear una ruta para la API
@app.route('/api', methods=['GET'])
def api():
    # Obtener los datos de la solicitud
    data = request.args

    # Procesar los datos
    result = process_data(data)

    # Devolver el resultado como JSON
    return jsonify(result)

# Función para procesar los datos
def process_data(data):
    # Hacer algo con los datos
    result = data + 1

    # Devolver el resultado
    return result

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run()

```

Al ejecutar el mismo mensaje de nuevo, se genera un resultado ligeramente diferente. Respuesta:

```python
#importar paquetes necesarios
import flask
from flask import request, jsonify

#crear la aplicación Flask
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#crear una lista de libros
books = [
    {'id': 0,
        'title': 'Un fuego en las profundidades',
        'author': 'Vernor Vinge',
        'first_sentence': 'El criosueño en sí mismo no tuvo sueños.',
        'year_published': '1992'},
    {'id': 1,
        'title': 'Los que se alejan de Omelas',
        'author': 'Ursula K. Le Guin',
        'first_sentence': 'Con un clamor de campanas que hizo remontar el vuelo a las golondrinas, el Festival de Verano llegó a la ciudad de Omelas, con sus brillantes torres junto al mar.',
        'year_published': 1973},
    {'id': 2,
        'title': Dhalgren,
        'author': Samuel R. Delany,
        'first_sentence': herir la ciudad otoñal,
        'year_published': 1975},
]

#Crear un punto de conexión para la API
@app.route('/', methods=['GET'])
def home():
    return '''<h1>API de Libros</h1>
<p>Un prototipo de API para recuperar libros.</p>'''

#Crear un punto de conexión para devolver todos los libros
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

#Crear un punto de conexión para devolver un solo libro
@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    #Comprobar si se proporcionó un ID como parte de la URL
    #Si se proporciona un ID, asignarlo a una variable
    #Si no se proporciona un ID, mostrar un error
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No se proporcionó el campo id. Por favor, especifique un id."

    #crear una lista vacía para nuestros resultados
    results = []

    #recorrer los datos y encontrar los resultados que coincidan con el id solicitado
    #Los id son únicos, pero otros campos pueden devolver muchos resultados
    for book in books:
        if book['id'] == id:
            results.append(book)

    #usar la función jsonify de Flask para convertir nuestra lista de #diccionarios de Python al formato JSON
    return jsonify(results)

app.run()
```

> Entonces, la salida variada es un problema?

Depende de lo que intentes hacer. Si quieres una respuesta específica, es un problema. Si te parece bien una salida variada como "Generar 3 preguntas cualesquiera sobre geografía", entonces no es un problema.

### Uso de la temperatura para variar la salida

Bien, hemos decidido limitar la salida para que sea más predecible, es decir, más determinista. Cómo lo hacemos?

La temperatura es un valor entre 0 y 1, donde 0 es el más determinista y 1 el más variable. El valor predeterminado es 0,7. Veamos qué sucede con dos ejecuciones del mismo indicacion con la temperatura establecida en 0,1:

> "Generar código para una API web de Python"

```python
#importar bibliotecas necesarias
import flask
from flask import request, jsonify
#Crear una instancia de la clase Flask
app = flask.Flask(__name__)

#Crear un endpoint para la API
@app.route('/api/v1/endpoint', methods=['GET'])
def api_endpoint():
    #Obtener los datos de la solicitud
    data = request.get_json()

    #Procesar los datos
    result = process_data(data)

    #Devolver el resultado
    return jsonify(result)

#Función para procesar los datos
def process_data(data):
    #Procesar los datos
    result = {'result': 'success'}

    #Devolver el resultado
    return result

#Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run()

```

Al ejecutar el indicacion de nuevo, obtenemos este resultado:

```python
#Importar las bibliotecas necesarias
import flask
from flask import request, jsonify

#Crear una aplicación Flask
app = flask.Flask(__name__)

#Crear una ruta para la API
@app.route('/api', methods=['GET'])
def api_call():
    #Obtener los datos de la solicitud
    data = request.get_json()

    #Procesar los datos
    result = process_data(data)

    #Devolver el resultado
    return jsonify(result)

#Definir la función process_data
def process_data(data):
    #Hacer algo con los datos
    result = data + 1

    #Devolver el resultado
    return result

#Ejecutar la aplicación
if __name__ == '__main__':
    app.run()

```

Hay solo una pequeña diferencia entre estas dos salidas. Esta vez, hagamos lo contrario: establezcamos la temperatura en 0.9:

```python
# Importar las bibliotecas necesarias
import flask
from flask import request, jsonify

# Crear una aplicación Flask
app = flask.Flask(__name__)

# Crear una ruta para la API
@app.route('/api', methods=['GET'])
def api_call():
    # Obtener los datos de la solicitud
    data = request.args

    # Procesar los datos
    result = process_data(data)

    # Devolver el resultado
    return jsonify(result)

# Función para procesar los datos
def process_data(data):
    # Hacer algo con los datos
    result = data + 1
    # Devuelve el resultado
    return result

# Ejecuta la aplicación
if __name__ == '__main__':
    app.run()

```

y el segundo intento con 0.9 como valor de temperatura:

```python
import flask
from flask import request, jsonify

# Crea la aplicación Flask
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# Crea algunos datos de prueba
books = [
    {'id': 0, 'title': 'Un fuego en las profundidades', 'author': 'Vernor Vinge', 'first_sentence': 'El criosueño en sí no tenía sueños', 'year_published': '1992'},
    {'id': 1, 'title': 'Los que se alejan de Omelas', 'author': 'Ursula K. Le Guin', 'first_sentence': 'Con un El clamor de las campanas hizo remontar el vuelo a las golondrinas; el Festival de Verano llegó a la ciudad de Omelas, coronada de brillantes torres por el mar.', 'published': '1973'},
    {'id': 2, 'title': 'Dhalgren', 'author': 'Samuel R. Delany', 'first_sentence': 'para herir la ciudad otoñal.', 'published': '1975'}
]

# crear un punto final
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Bienvenido a nuestra API de libros!</h1>'''

@app.route('/api/v1/resources/books')

```

Como puede ver, los resultados son muy variados.

> Tenga en cuenta que hay más parámetros que puede cambiar para variar la salida, como top-k, top-p y repetición. Penalización por extensión, penalización por diversidad y penalización por incitación, pero estas quedan fuera del alcance de este programa.

## Buenas prácticas

Hay muchas prácticas que puedes aplicar para intentar conseguir lo que quieres. Encontrarás tu propio estilo a medida que uses más las indicaciones.

Además de las técnicas que hemos visto, hay algunas buenas prácticas que debes considerar al incitar a un LLM.

Aquí tienes algunas buenas prácticas:

- **Especificar el contexto**. El contexto es importante; cuanto más especifiques, como el dominio, el tema, etc., mejor.
- Limitar el resultado. Si deseas un número específico de elementos o una longitud específica, especifícalo.
- **Especificar qué y cómo**. Recuerda mencionar qué quieres y cómo lo quieres, por ejemplo, "Crear una API web de Python con rutas, productos y clientes, dividiéndola en 3 archivos".
- **Usar plantillas**. A menudo, querrás enriquecer tus indicaciones con datos de tu empresa. Usa plantillas para ello. Las plantillas pueden tener variables que puedes reemplazar con datos reales.
- **Escribir correctamente**. Los LLM pueden proporcionarte Una respuesta correcta, pero si escribes correctamente, obtendrás una mejor respuesta.

## Tarea
Aquí tienes un código en Python que muestra cómo crear una API sencilla con Flask:

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

Usa un asistente de IA como GitHub Copilot o ChatGPT y aplica la técnica de autorefinamiento para mejorar el código.

## Solución

Intenta resolver la tarea añadiendo indicaciones adecuadas al código.

> [!TIP]
> Crea una indicación para pedirle que mejore. Es recomendable limitar el número de mejoras. También puedes pedir que se mejore de alguna manera, por ejemplo, la arquitectura, el rendimiento, la seguridad, etc.

[Solución](../../python/aoai-solution.py?WT.mc_id=academic-105485-koreyst)

## Prueba de conocimientos

Por qué debería usar la técnica de cadena de pensamiento? Muéstrame una respuesta correcta y dos incorrectas.

1. Para enseñar al LLM a resolver un problema.
2. Para enseñar al LLM a encontrar errores en el código.
3. Para indicar al LLM que proponga diferentes soluciones.

R: 1. Porque la técnica de cadena de pensamiento consiste en mostrar al LLM cómo resolver un problema, proporcionándole una serie de pasos, problemas similares y cómo se resolvieron.

## 🚀 Desafío

Acabas de usar la técnica de autorefinamiento en la tarea. Considera cualquier programa que hayas creado y qué mejoras te gustaría aplicarle. Ahora usa la técnica de autorefinamiento para aplicar los cambios propuestos. Qué te pareció el resultado, mejor o peor?

## Buen trabajo! Continúa aprendiendo.

Después de completar esta lección, consulta nuestra [colección de aprendizaje de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para seguir mejorando tus conocimientos de IA generativa.

Dirígete a la Lección 6, donde aplicaremos nuestros conocimientos de Ingeniería de [indicacion creando aplicaciones de generación de texto](../../../06-text-generation-apps/translations/es-mx/README.md?WT.mc_id=academic-105485-koreyst)