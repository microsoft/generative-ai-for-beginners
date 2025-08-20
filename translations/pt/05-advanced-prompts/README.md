<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2b4c36be7d66b32e4fac47761718b4a9",
  "translation_date": "2025-07-09T11:30:36+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "pt"
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

Executar o prompt novamente dá-nos este resultado:

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

Há apenas uma pequena diferença entre estas duas saídas. Vamos fazer o contrário desta vez, definir a temperatura para 0.9:

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

e a segunda tentativa com o valor de temperatura 0.9:

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

Como podem ver, os resultados não podiam ser mais variados.

> Note que existem mais parâmetros que pode alterar para variar a saída, como top-k, top-p, penalização de repetição, penalização de comprimento e penalização de diversidade, mas estes estão fora do âmbito deste currículo.

## Boas práticas

Existem muitas práticas que pode aplicar para tentar obter o que deseja. Vai encontrar o seu próprio estilo à medida que usar prompting cada vez mais.

Além das técnicas que abordámos, há algumas boas práticas a considerar ao fazer prompting a um LLM.

Aqui estão algumas boas práticas a ter em conta:

- **Especifique o contexto**. O contexto é importante, quanto mais conseguir especificar, como domínio, tema, etc., melhor.
- Limite a saída. Se quiser um número específico de itens ou um comprimento específico, especifique-o.
- **Especifique tanto o quê como o como**. Lembre-se de mencionar tanto o que quer como a forma como quer, por exemplo "Crie uma API Web em Python com as rotas products e customers, divida-a em 3 ficheiros".
- **Use templates**. Muitas vezes, vai querer enriquecer os seus prompts com dados da sua empresa. Use templates para isso. Os templates podem ter variáveis que substitui por dados reais.
- **Escreva corretamente**. Os LLMs podem fornecer uma resposta correta, mas se escrever corretamente, obterá uma resposta melhor.

## Exercício

Aqui está um código em Python que mostra como construir uma API simples usando Flask:

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

Use um assistente de IA como o GitHub Copilot ou ChatGPT e aplique a técnica "self-refine" para melhorar o código.

## Solução

Tente resolver o exercício adicionando prompts adequados ao código.

> [!TIP]
> Formule um prompt para pedir melhorias, é uma boa ideia limitar quantas melhorias quer. Também pode pedir para melhorar de uma forma específica, por exemplo arquitetura, desempenho, segurança, etc.

[Solução](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificação de conhecimento

Por que razão usaria chain-of-thought prompting? Mostre-me 1 resposta correta e 2 respostas incorretas.

1. Para ensinar o LLM a resolver um problema.  
1. B, Para ensinar o LLM a encontrar erros no código.  
1. C, Para instruir o LLM a apresentar diferentes soluções.

A: 1, porque chain-of-thought consiste em mostrar ao LLM como resolver um problema fornecendo-lhe uma série de passos, problemas semelhantes e como foram resolvidos.

## 🚀 Desafio

Acabou de usar a técnica self-refine no exercício. Pegue em qualquer programa que tenha criado e pense nas melhorias que gostaria de aplicar. Agora use a técnica self-refine para aplicar as alterações propostas. O que achou do resultado, melhor ou pior?

## Excelente trabalho! Continue a aprender

Depois de completar esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos em IA Generativa!

Siga para a Lição 6 onde aplicaremos o nosso conhecimento de Prompt Engineering construindo [aplicações de geração de texto](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.