<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:30:58+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "br"
}
-->

> "Gerar código para uma API Web em Python"
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

Executar o prompt novamente nos dá este resultado:

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

Há apenas uma pequena diferença entre essas duas saídas. Vamos fazer o contrário desta vez, vamos definir a temperatura para 0,9:

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

e a segunda tentativa com o valor de temperatura 0,9:

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

Como você pode ver, os resultados não poderiam ser mais variados.

> Note que existem mais parâmetros que você pode alterar para variar a saída, como top-k, top-p, penalidade por repetição, penalidade de comprimento e penalidade de diversidade, mas esses estão fora do escopo deste currículo.

## Boas práticas

Existem muitas práticas que você pode aplicar para tentar obter o que deseja. Você encontrará seu próprio estilo à medida que usar prompting cada vez mais.

Além das técnicas que abordamos, há algumas boas práticas a considerar ao fazer prompting em um LLM.

Aqui estão algumas boas práticas para considerar:

- **Especifique o contexto**. O contexto importa, quanto mais você puder especificar, como domínio, tópico, etc., melhor.
- Limite a saída. Se você quiser um número específico de itens ou um comprimento específico, especifique isso.
- **Especifique tanto o que quanto o como**. Lembre-se de mencionar tanto o que você quer quanto como quer, por exemplo, "Crie uma API Web em Python com rotas products e customers, dividida em 3 arquivos".
- **Use templates**. Frequentemente, você vai querer enriquecer seus prompts com dados da sua empresa. Use templates para isso. Templates podem ter variáveis que você substitui pelos dados reais.
- **Escreva corretamente**. LLMs podem fornecer uma resposta correta, mas se você escrever corretamente, receberá uma resposta melhor.

## Exercício

Aqui está um código em Python mostrando como construir uma API simples usando Flask:

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

Use um assistente de IA como GitHub Copilot ou ChatGPT e aplique a técnica de "auto-refinamento" para melhorar o código.

## Solução

Tente resolver o exercício adicionando prompts adequados ao código.

> [!TIP]
> Formule um prompt pedindo para melhorar, é uma boa ideia limitar quantas melhorias. Você também pode pedir para melhorar de uma forma específica, por exemplo arquitetura, desempenho, segurança, etc.

[Solução](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificação de conhecimento

Por que eu usaria chain-of-thought prompting? Mostre 1 resposta correta e 2 respostas incorretas.

1. Para ensinar o LLM a resolver um problema.  
1. B, Para ensinar o LLM a encontrar erros no código.  
1. C, Para instruir o LLM a criar diferentes soluções.

A: 1, porque chain-of-thought é sobre mostrar ao LLM como resolver um problema fornecendo uma série de passos, problemas similares e como eles foram resolvidos.

## 🚀 Desafio

Você acabou de usar a técnica de auto-refinamento no exercício. Pegue qualquer programa que você tenha criado e pense nas melhorias que gostaria de aplicar. Agora use a técnica de auto-refinamento para aplicar as mudanças propostas. O que você achou do resultado, melhor ou pior?

## Excelente trabalho! Continue seu aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Siga para a Lição 6, onde aplicaremos nosso conhecimento de Engenharia de Prompt criando [aplicativos de geração de texto](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.