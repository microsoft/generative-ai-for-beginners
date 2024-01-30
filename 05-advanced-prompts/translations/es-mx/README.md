# Creando Prompts Avanzados

[![Creando Prompts Avanzados](../../images/05-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://youtu.be/32GBH6BTWZQ?WT.mc_id=academic-105485-koreyst)

Recapitulemos algunos aprendizajes del capítulo anterior:

> Prompt _engineering_ es el proceso mediante el cual **guiamos el modelo hacia respuestas más relevantes** proporcionando instrucciones o contexto más útiles.

También hay dos pasos para escribir prompts: construir el prompt, proporcionando un contexto relevante y la segunda parte es la _optimización_, cómo mejorar gradualmente el prompt.

En este punto, tenemos algunos conocimientos básicos sobre cómo escribir prompts, pero necesitamos profundizar más. En este capítulo, pasarás de probar varios prompts a comprender por qué un prompt es mejor que otro. Aprenderás a construir prompts siguiendo algunas técnicas básicas que se pueden aplicar a cualquier LLM.

## Introducción

En este capítulo, cubriremos los siguientes temas:

- Amplíar tus conocimientos de prompt engineering aplicando diferentes técnicas a tus prompts.
- Configurar tus prompts para variar la salida.

## Metas de Aprendizaje

Después de completar esta lección, podrás:

- Aplicar técnicas de prompt engineering que mejoren el resultado de tus prompts.
- Realizar prompting que sea variado o determinista.

## Prompt engineering

Prompt engineering es el proceso de creación de prompts que producirán el resultado deseado. Prompt engineering implica mucho más que simplemente escribir un prompt de texto. Prompt engineering no es una disciplina de ingeniería, es más bien un conjunto de técnicas que puedes aplicar para obtener el resultado deseado.

### Un ejemplo de un prompt

Tomemos un prompt básico como este:

> Genera 10 preguntas sobre geografía.

En este prompt, en realidad estás aplicando un conjunto de técnicas de prompt diferentes.

Analicemos esto.

- **Contexto**, especificas que debe ser sobre "geografía".
- **Limitando la salida**, no deseas más de 10 preguntas.

### Limitaciones del prompting simple

Puede que obtengas o no el resultado deseado. Se generarán tus preguntas, pero la geografía es un tema grande y es posible que no obtengas lo que deseas debido a las siguientes razones:

- **Tema grande**, no sabes si será sobre países, capitales, ríos y demás.
- **Formato**, ¿qué pasaría si quisieras que las preguntas tuvieran un formato determinado?

Como puedes ver, hay mucho que considerar al crear prompts.

Hasta ahora, hemos visto un ejemplo sencillo de prompt, pero la IA generativa es capaz de hacer mucho más para ayudar a las personas en una variedad de roles e industrias. Exploremos algunas técnicas básicas a continuación.

### Técnicas de prompting

Primero, debemos comprender que los prompts son una propiedad _emergente_ de un LLM, lo que significa que no es una característica integrada en el modelo, sino algo que descubrimos a medida que usamos el modelo.

Existen algunas técnicas básicas que podemos utilizar para hacer prompt a un LLM. Vamos a explorarlos.

- **Few shot prompting**, esta es la forma más básica de prompting. Es un único prompt con algunos ejemplos.
- **Cadena-de-pensamiento**, este tipo de prompting le indica al LLM cómo dividir un problema en pasos.
- **Conocimiento generado**, para mejorar la respuesta de un prompt, puedes proporcionar hechos o conocimientos generados adicionalmente a tu prompt.
- **De menos a más**, como chain-of-thought, esta técnica consiste en dividir un problema en una serie de pasos y luego pedir que estos pasos se realicen en orden.
- **Auto-refinar**, esta técnica consiste en criticar el resultado del LLM y luego pedirle que mejore.
- **Prompting mayéutico**. Lo que deseas aquí es asegurarse de que la respuesta del LLM sea correcta y pedirle que explique varias partes de la respuesta. Esta es una forma de autorefinamiento.

### Few-shot prompting

Este estilo de prompting es muy simple, puede consistir en una único prompt y posiblemente algunos ejemplos. Esta técnica es probablemente la que estés utilizando cuando comienzas a aprender sobre los LLM. He aquí un ejemplo:

- Prompt: "¿Qué es el Álgebra?"
- Respuesta: "El álgebra es una rama de las matemáticas que estudia los símbolos matemáticos y las reglas para manipularlos".

### Cadena-de-pensamiento

Cadena-de-pensamiento es una técnica muy interesante ya que consiste en llevar el LLM a través de una serie de pasos. La idea es instruir al LLM de tal manera que comprenda cómo hacer algo. Considere el siguiente ejemplo, con y sin cadena-de-pensamiento:

    - Prompt: "Alice tiene 5 manzanas, lanza 3 manzanas, le da 2 a Bob y Bob le devuelve una, ¿cuántas manzanas tiene Alice?"
    - Respuesta: 5

El LLM responde con 5, lo cual es incorrecto. La respuesta correcta es 1 manzana, dado el cálculo (5 -3 -2 + 1 = 1).

Entonces, ¿cómo podemos enseñarle al LLM a hacer esto correctamente?

Probemos con la cadena-de-pensamiento. Aplicar la cadena-de-pensamiento significa:

1. Proporciona al LLM un ejemplo similar.
2. Muestra el cálculo y cómo calcularlo correctamente.
3. Proporciona el prompt original.

Aquí está cómo:

- Prompt: "Lisa tiene 7 manzanas, lanza 1 manzana, le da 4 manzanas a Bart y Bart le devuelve una:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3
  Alice tiene 5 manzanas, lanza 3 manzanas, le da 2 a Bob y Bob le devuelve una, ¿cuántas manzanas tiene Alice?
  Respuesta: 1

Observa cómo escribimos sustancialmente prompts más largos con otro ejemplo, un cálculo y luego el prompt original y llegamos a la respuesta correcta 1.

Como puedes ver, la cadena-de-pensamiento es una técnica muy poderosa.

### Conocimiento generado

Muchas veces, cuando deseas crear un prompt, deseas hacerlo utilizando los datos de tu propia empresa. Deseas que parte del prompt provenga de la empresa y la otra parte debería ser el prompt real en el que estás interesado.

A modo de ejemplo, así es como puede verse tu prompt si estás en el negocio de seguros:

    ```text
    {{company}}: {{company_name}}
    {{products}}: 
    {{products_list}}
    Por favor sugiere un seguro dado el siguiente presupuesto y requisitos:
    Presupuesto: {{budget}}
    Requisitos: {{requirements}}
    ```

Arriba, puedes ver cómo se construye el prompt utilizando una plantilla. En la plantilla hay una serie de variables, indicadas por `{{variable}}`, que serán reemplazadas con valores reales de la API de una empresa.

A continuación se muestra un ejemplo de cómo podría verse el prompt una vez que las variables hayan sido reemplazadas por contenido de tu empresa:

    ```text
    Compañía de seguros: ACME Insurance
    Productos de seguros (costo por mes):
    - Auto, barato, 500 USD
    - Auto, caro, 1100 USD 
    - Casa, barato, 600 USD
    - Casa, caro, 1200 USD
    - Vida, barato, 100 USD
    
    Por favor sugiere un seguro dado el siguiente presupuesto y requisitos:
    Presupuesto: $1000
    Requisitos: Auto, Casa
    ```

Ejecutar este prompt a través de un LLM producirá una respuesta como esta:

    ```output
    , y seguro de Vida
    
    Dado el presupuesto y requisitos, sugerimos el siguiente paquete de seguros de ACME Insurance:
    - Auto, barato, 500 USD 
    - Casa, barato, 600 USD 
    - Vida, barato, 100 USD 
    Costo total: $1,200 USD
    ```

Como puedes observar, también te sugiere el seguro de Vida, cosa que no debería hacer. Este resultado es una indicación de que necesitamos optimizar el prompt cambiándolo para que sea más claro sobre lo que puede permitir. Después de algunas _pruebas y errores_, llegamos al siguiente prompt:

    ```text
    Compañía de seguros: ACME Insurance
    Productos de seguros (costo por mes): 
    - tipo: Auto, barato, costo: 500 USD
    - tipo: Auto, caro, costo: 1100 USD 
    - tipo: Casa, barato, costo: 600 USD
    - tipo: Casa, caro, costo: 1200 USD
    - tipo: Vida, barato, costo: 100 USD
    
    Por favor sugiere un seguro dado el siguiente presupuesto y requisitos:
    Presupuesto: $1000 restringe la elección a los tipos: Auto, Casa
    ```

Observa cómo agregar _tipo_ y _costo_ y también usar la palabra clave _restringir_ ayuda al LLM a comprender lo que queremos.

Ahora obtenemos la siguiente respuesta:

    ```output
    Dado el presupuesto y los requisitos, sugerimos el producto de seguro Auto, Barato que cuesta 500 USD al mes.
    ```

El objetivo de este ejemplo era mostrar que, aunque utilizamos una técnica básica como _conocimiento generado_, todavía necesitamos optimizar el prompt en la mayoría de los casos para obtener el resultado deseado.

### De menos-a-más

La idea con prompting de menos-a-más es dividir un problema mayor en subproblemas. De esa manera, ayudas a guiar al LLM sobre cómo "conquistar" el problema más grande. Un buen ejemplo podría ser para ciencia de datos, donde puedes pedirle al LLM que divida un problema de esta manera:

> Prompt: ¿Cómo realizar ciencia de datos en 5 pasos?

Con tu asistente de IA respondiendo con:

1. Recopila datos
2. Limpia datos
3. Analizar datos
4. Graficar datos
5. Presentar datos

### Auto-refinar, criticar los resultados

Con las IAs generativas y los LLM, no se puede confiar en el resultado. Necesitas verificarlo. Después de todo, el LLM solo te presenta la cosa más probable por decir, no la que es correcta. Por tanto, una buena idea es pedirle al LLM que se critique a sí mismo, lo que nos lleva a la técnica del autorrefinamiento.

El funcionamiento consiste en que sigas los siguientes pasos:

1. Prompt inicial pidiendo al LLM que resuelva un problema
2. El LLM responde
3. Criticas la respuesta y le pides a la IA que mejore
4. El LLM responde nuevamente, esta vez considerando la crítica y sugiriendo soluciones que se le ocurrieron.

Puedes repetir este proceso tantas veces como quieras.

A continuación se muestra un ejemplo utilizando esta técnica:

> Prompt: "Crea una API web de Python con rutas de productos y clientes"

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

> Prompt: sugiere 3 mejoras al código anterior

Respuesta de la IA:

    ```text
    Claro, aquí hay tres sugerencias para mejorar el código:
    
    Importa el módulo correcto: la primera línea debe importar Flask en lugar de flask. La declaración de importación correcta debe ser from flask import Flask.
    
    Agrega una función principal: agrega un bloque if __name__ == '__main__': al final del archivo para ejecutar la aplicación cuando el archivo es ejecutado.
    
    Utiliza f-strings: utiliza f-strings para formatear las declaraciones return en las funciones de ruta. Por ejemplo, return 'Products' puede ser cambiado a return f'This is the {request.path} page'.
    ```

    ```python
    from flask import Flask, request
    
    app = Flask(__name__)
    
    @app.route('/products')
    def products():
        return f'This is the {request.path} page'
    
    @app.route('/customers')
    def customers():
        return f'This is the {request.path} page'
    
    if __name__ == '__main__':
        app.run()
    ```

Como puedes observar, la respuesta anterior de la IA mejora el primer código sugerido gracias a haber criticado la primera respuesta.

### Prompting mayéutico

Prompting mayéutico es una técnica similar al autorrefinamiento, pero se trata más de pedirle al LLM que se explique. El objetivo es reducir las inconsistencias en el resultado del LLM para garantizar que llegue a la respuesta correcta. El flujo de trabajo a seguir es:

1. Pide al LLM que responda una pregunta.
2. Para cada parte de la respuesta, pide al LLM que la explique más en profundidad.
3. Si hay inconsistencias, descarta las partes que sean inconsistentes.

Repite 2 y 3 hasta que hayas repasado todas las partes y estés satisfecho con la respuesta.

A continuación se muestra un prompt de ejemplo:

> prompt: ¿Cómo puedo crear un plan de crisis para mitigar una pandemia en 5 pasos?
Respuesta del LLM:

    ```text
    1. Identifica los riesgos
    2. Identifica las partes interesadas
    3. Identifica los recursos
    4. Identifica las acciones
    5. Identifica los canales de comunicación
    ```

Se han identificado 5 pasos, pero ¿podemos determinar si esto es correcto? Pidamos al LLM que explique cada paso:

> prompt: Explica el primer paso con más detalle, ¿cuáles son los riesgos en detalle con una pandemia? 

    ```text
    Los riesgos son los siguientes:
    
    - Pérdida de vida
    - Pérdida de negocio
    - Pérdida de reputación
    - Pérdida de clientes
    - Pérdida de empleados
    ```

En este punto, queremos asegurarnos de que el LLM esté correcto, por lo que le pedimos que explique el primer riesgo con más detalle y esperamos que sea coherente con la respuesta anterior:

> prompt: En una Pandemia, ¿cuál es el mayor riesgo y por qué?

    ```text
    El mayor riesgo es la pérdida de vidas porque es lo más importante que hay que proteger.
    ```

> ¿Cuáles son los dos mayores riesgos en una pandemia?

    ```text
    Los dos mayores riesgos son la pérdida de vidas y la pérdida de negocios.
    ```

En este punto, el LLM es coherente y menciona "vida" y "negocios" como los dos riesgos principales. Ahora podemos continuar con el siguiente paso y sentirnos bastante seguros. Sin embargo, no deberíamos confiar ciegamente en el LLM, siempre deberíamos verificar el resultado.

## Varía tu salida

Los LLM son no deterministas por naturaleza, lo que significa que obtendrás resultados diferentes cada vez que ejecutes el mismo prompt. Prueba el siguiente prompt, por ejemplo:

> "Genera código para una API web de Python"

    ```text
    # Import necessary modules
    import flask
    from flask import request, jsonify
    
    # Create a Flask app
    app = flask.Flask(__name__)
    
    # Create a route for the API
    @app.route('/api', methods=['GET'])
    def api():
        # Get the data from the request
        data = request.args
    
        # Process the data
        result = process_data(data)
    
        # Return the result as JSON
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

Ejecutar el mismo prompt nuevamente genera una respuesta ligeramente diferente:

    ```text
    #import necessary packages
    import flask
    from flask import request, jsonify
    
    #create the Flask application
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    
    #create a list of books
    books = [
        {'id': 0,
         'title': 'A Fire Upon the Deep',
         'author': 'Vernor Vinge',
         'first_sentence': 'The coldsleep itself was dreamless.',
         'year_published': '1992'},
        {'id': 1,
         'title': 'The Ones Who Walk Away From Omelas',
         'author': 'Ursula K. Le Guin',
         'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
         'published': '1973'},
        {'id': 2,
         'title': 'Dhalgren',
         'author': 'Samuel R. Delany',
         'first_sentence': 'to wound the autumnal city.',
         'published': '1975'}
    ]
    
    #create an endpoint for the API
    @app.route('/', methods=['GET'])
    def home():
        return '''<h1>Books API</h1>
    <p>A prototype API for retrieving books.</p>'''
    
    #create an endpoint to return all books
    @app.route('/api/v1/resources/books/all', methods=['GET'])
    def api_all():
        return jsonify(books)
    
    #create an endpoint to return a single book
    @app.route('/api/v1/resources/books', methods=['GET'])
    def api_id():
        #check if an ID was provided as part of the URL
        #if ID is provided, assign it to a variable
        #if no ID is provided, display an error
        if 'id' in request.args:
            id = int(request.args['id'])
        else:
            return "Error: No id field provided. Please specify an id."
    
        #create an empty list for our results
        results = []
    
        #loop through the data and match results that fit the requested ID
        #IDs are unique, but other fields might return many results
        for book in books:
            if book['id'] == id:
                results.append(book)
    
        #use the jsonify function from Flask to convert our list of
        #Python dictionaries to the JSON format
        return jsonify(results)
    
    app.run()
    ```

> Entonces, ¿la salida variada es un problema?

Depende de lo que estés intentando hacer. Si quieres una respuesta específica, entonces es un problema. Si está de acuerdo con un resultado variado como "Genera 3 preguntas sobre geografía", entonces no es un problema.

### Usar la temperatura para variar tu salida

De acuerdo, entonces hemos decidido que queremos limitar la salida para que sea más predecible, es decir, más determinista. ¿Como hacemos eso?

La temperatura es un valor entre 0 y 1, donde 0 es el más determinista y 1 es el más variado. El valor predeterminado es 0.7. Veamos qué sucede con dos ejecuciones del mismo prompt con la temperatura establecida en 0.1:

> "Genera código para una API web de Python"

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

Sólo hay una pequeña diferencia entre estas dos salidas. Hagamos lo contrario esta vez, fijemos la temperatura en 0.9:

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

y el segundo intento con 0.9 como valor de temperatura:

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

> Ten en cuenta que hay más parámetros que puedes cambiar para variar la salida, como top-k, top-p, penalización de repetición, penalización de longitud y penalización de diversidad, pero estos están fuera del alcance de este plan de estudios.

## Buenas prácticas

Hay muchas prácticas que puedes aplicar para intentar conseguir lo que deseas. Encontrarás tu propio estilo a medida que utilices los prompts más y más veces.

Además de las técnicas que hemos cubierto, existen algunas buenas prácticas a considerar al hacer prompting a un LLM.

Aquí hay algunas buenas prácticas a considerar:

- **Especifica contexto**. El contexto importa, cuanto más puedas especificar, como por ejemplo dominio, tema, etc., mejor.
- Limita la salida. Si deseas una cantidad específica de elementos o una longitud específica, especifícalo.
- **Especifica qué y cómo**. Recuerda mencionar tanto lo que quieres como cómo lo quieres, por ejemplo "Crea una API web de Python con rutas de productos y clientes, divídela en 3 archivos".
- **Usa plantillas**. A menudo, querrás enriquecer tus prompts con datos de tu empresa. Utiliza plantillas para hacer esto. Las plantillas pueden tener variables que reemplazas con datos reales.
- **Escribe correctamente**. Los LLM pueden brindarte una respuesta correcta, pero si escribes correctamente, obtendrás una mejor respuesta.

## Tarea

Aquí hay un código en Python que muestra cómo construir una API simple usando Flask:

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

Utiliza un asistente de IA como GitHub Copilot o ChatGPT y aplique la técnica de "auto-refinamiento" para mejorar el código.

## Solución

Intenta resolver la tarea agregando prompts adecuados al código.

> [!TIP]
> Formula un prompt para pedirle que mejore, es una buena idea limitar cuántas mejoras. También puedes pedir mejorarlo de cierta manera, por ejemplo arquitectura, rendimiento, seguridad, etc.

[Solución](../../solution.py?WT.mc_id=academic-105485-koreyst)

## Verificación de conocimientos

¿Por qué debería utilizar prompting de cadena-de-pensamiento? Muéstrame 1 respuesta correcta y 2 respuestas incorrectas.

1. Para enseñar al LLM cómo resolver un problema.
2. B, Para enseñar al LLM a encontrar errores en el código.
3. C, Para instruir al LLM a que proponga diferentes soluciones. 

R: 1, porque la cadena-de-pensamiento consiste en mostrarle al LLM cómo resolver un problema proporcionándole una serie de pasos y problemas similares y cómo se resolvieron.

## 🚀 Desafío

Acabas de utilizar la técnica de autorrefinamiento en la tarea. Toma cualquier programa que hayas creado y considera qué mejoras te gustaría aplicarle. Ahora utiliza la técnica de autorrefinamiento para aplicar los cambios propuestos. ¿Qué te pareció el resultado, mejor o peor?

## ¡Buen trabajo! Continúa tu Aprendizaje

Después de completar esta lección, ¡consulta nuestra [colección de Aprendizaje de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar mejorando tu conocimiento de IA Generativa!

Dirígete a la Lección 6, donde aplicaremos nuestro conocimiento de Prompt Engineering [creando aplicaciones de generación de texto](../../../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)
