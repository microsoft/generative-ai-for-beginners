<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:22:46+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "fr"
}
-->

> "Générer du code pour une API Web Python"
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

Relancer le prompt nous donne ce résultat :

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

Il n’y a qu’une toute petite différence entre ces deux sorties. Faisons l’inverse cette fois, réglons la température à 0,9 :

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

et la deuxième tentative avec une température à 0,9 :

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

Comme vous pouvez le voir, les résultats ne pourraient pas être plus variés.

> Notez qu’il existe d’autres paramètres que vous pouvez modifier pour varier la sortie, comme top-k, top-p, repetition penalty, length penalty et diversity penalty, mais ceux-ci dépassent le cadre de ce cours.

## Bonnes pratiques

Il existe de nombreuses pratiques que vous pouvez appliquer pour essayer d’obtenir ce que vous souhaitez. Vous trouverez votre propre style à mesure que vous utiliserez le prompting de plus en plus.

En plus des techniques que nous avons abordées, voici quelques bonnes pratiques à considérer lors du prompting d’un LLM.

Voici quelques bonnes pratiques à garder en tête :

- **Spécifiez le contexte**. Le contexte est important, plus vous pouvez préciser comme le domaine, le sujet, etc., mieux c’est.
- Limitez la sortie. Si vous voulez un nombre précis d’éléments ou une longueur spécifique, indiquez-le.
- **Précisez à la fois quoi et comment**. N’oubliez pas de mentionner à la fois ce que vous voulez et comment vous le voulez, par exemple « Créez une API Web Python avec les routes products et customers, divisez-la en 3 fichiers ».
- **Utilisez des modèles**. Souvent, vous voudrez enrichir vos prompts avec des données de votre entreprise. Utilisez des modèles pour cela. Les modèles peuvent contenir des variables que vous remplacez par des données réelles.
- **Orthographiez correctement**. Les LLM peuvent vous fournir une réponse correcte, mais si vous orthographiez bien, vous obtiendrez une meilleure réponse.

## Exercice

Voici un code en Python montrant comment construire une API simple avec Flask :

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

Utilisez un assistant IA comme GitHub Copilot ou ChatGPT et appliquez la technique de « self-refine » pour améliorer le code.

## Solution

Essayez de résoudre l’exercice en ajoutant des prompts appropriés au code.

> [!TIP]
> Formulez un prompt demandant une amélioration, il est judicieux de limiter le nombre d’améliorations. Vous pouvez aussi demander une amélioration dans un domaine précis, par exemple architecture, performance, sécurité, etc.

[Solution](../../../05-advanced-prompts/python/aoai-solution.py)

## Vérification des connaissances

Pourquoi utiliserais-je le chain-of-thought prompting ? Donnez-moi 1 réponse correcte et 2 réponses incorrectes.

1. Pour apprendre au LLM comment résoudre un problème.  
1. B, Pour apprendre au LLM à trouver des erreurs dans le code.  
1. C, Pour demander au LLM de proposer différentes solutions.

A : 1, car le chain-of-thought consiste à montrer au LLM comment résoudre un problème en lui fournissant une série d’étapes, ainsi que des problèmes similaires et leur résolution.

## 🚀 Défi

Vous venez d’utiliser la technique de self-refine dans l’exercice. Prenez n’importe quel programme que vous avez créé et réfléchissez aux améliorations que vous souhaiteriez y apporter. Utilisez maintenant la technique de self-refine pour appliquer les changements proposés. Quel est votre avis sur le résultat, meilleur ou pire ?

## Excellent travail ! Continuez à apprendre

Après avoir terminé cette leçon, consultez notre [collection d’apprentissage sur l’IA générative](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) pour continuer à approfondir vos connaissances en IA générative !

Rendez-vous à la Leçon 6 où nous appliquerons nos connaissances en Prompt Engineering en [créant des applications de génération de texte](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.