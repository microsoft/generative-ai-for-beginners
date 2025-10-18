<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "b2651fb16bcfbc62b8e518751ed90fdb",
  "translation_date": "2025-10-18T00:36:50+00:00",
  "source_file": "05-advanced-prompts/README.md",
  "language_code": "pt"
}
-->
# Criando Prompts Avançados

[![Criando Prompts Avançados](../../../translated_images/05-lesson-banner.522610fd4a2cd82dbed66bb7e6fe104ed6da172e085dbb4d9100b28dc73ed435.pt.png)](https://youtu.be/BAjzkaCdRok?si=NmUIyRf7-cDgbjtt)

Vamos recapitular alguns aprendizados do capítulo anterior:

> A _engenharia de prompts_ é o processo pelo qual **orientamos o modelo para respostas mais relevantes** fornecendo instruções ou contexto mais úteis.

Existem também dois passos para escrever prompts: construir o prompt, fornecendo contexto relevante, e _otimização_, que é como melhorar gradualmente o prompt.

Neste ponto, temos uma compreensão básica de como escrever prompts, mas precisamos ir mais fundo. Neste capítulo, você passará de experimentar vários prompts para entender por que um prompt é melhor que outro. Você aprenderá a construir prompts seguindo algumas técnicas básicas que podem ser aplicadas a qualquer LLM.

## Introdução

Neste capítulo, abordaremos os seguintes tópicos:

- Ampliar seu conhecimento sobre engenharia de prompts aplicando diferentes técnicas aos seus prompts.
- Configurar seus prompts para variar o resultado.

## Objetivos de aprendizagem

Após concluir esta lição, você será capaz de:

- Aplicar técnicas de engenharia de prompts que melhoram o resultado dos seus prompts.
- Realizar prompts que sejam variados ou determinísticos.

## Engenharia de prompts

Engenharia de prompts é o processo de criar prompts que produzam o resultado desejado. Há mais na engenharia de prompts do que apenas escrever um texto. Engenharia de prompts não é uma disciplina de engenharia, mas sim um conjunto de técnicas que você pode aplicar para obter o resultado desejado.

### Um exemplo de prompt

Vamos pegar um prompt básico como este:

> Gere 10 perguntas sobre geografia.

Neste prompt, você está aplicando, na verdade, um conjunto de diferentes técnicas de prompts.

Vamos analisar isso.

- **Contexto**, você especifica que deve ser sobre "geografia".
- **Limitação do resultado**, você quer no máximo 10 perguntas.

### Limitações de prompts simples

Você pode ou não obter o resultado desejado. Suas perguntas serão geradas, mas geografia é um tema amplo e você pode não obter o que deseja devido aos seguintes motivos:

- **Tema amplo**, você não sabe se será sobre países, capitais, rios e assim por diante.
- **Formato**, e se você quisesse que as perguntas fossem formatadas de uma determinada maneira?

Como pode ver, há muito a considerar ao criar prompts.

Até agora, vimos um exemplo de prompt simples, mas a IA generativa é capaz de muito mais para ajudar pessoas em uma variedade de funções e indústrias. Vamos explorar algumas técnicas básicas a seguir.

### Técnicas para criar prompts

Primeiro, precisamos entender que criar prompts é uma propriedade _emergente_ de um LLM, o que significa que isso não é uma funcionalidade embutida no modelo, mas algo que descobrimos ao usar o modelo.

Existem algumas técnicas básicas que podemos usar para criar prompts em um LLM. Vamos explorá-las.

- **Prompt sem exemplos (Zero-shot prompting)**, esta é a forma mais básica de criar prompts. É um único prompt solicitando uma resposta do LLM com base apenas nos seus dados de treinamento.
- **Prompt com poucos exemplos (Few-shot prompting)**, este tipo de prompt orienta o LLM fornecendo 1 ou mais exemplos nos quais ele pode se basear para gerar sua resposta.
- **Cadeia de raciocínio (Chain-of-thought)**, este tipo de prompt instrui o LLM sobre como dividir um problema em etapas.
- **Conhecimento gerado**, para melhorar a resposta de um prompt, você pode fornecer fatos ou conhecimentos gerados adicionalmente ao seu prompt.
- **Do mais simples ao mais complexo (Least to most)**, como a cadeia de raciocínio, esta técnica trata de dividir um problema em uma série de etapas e pedir que essas etapas sejam realizadas em ordem.
- **Auto-refinamento**, esta técnica trata de criticar a saída do LLM e depois pedir que ele melhore.
- **Prompt maiêutico (Maieutic prompting)**. Aqui, você quer garantir que a resposta do LLM esteja correta e pede que ele explique várias partes da resposta. Esta é uma forma de auto-refinamento.

### Prompt sem exemplos (Zero-shot prompting)

Este estilo de prompt é muito simples, consiste em um único prompt. Esta técnica é provavelmente o que você está usando ao começar a aprender sobre LLMs. Aqui está um exemplo:

- Prompt: "O que é Álgebra?"
- Resposta: "Álgebra é um ramo da matemática que estuda símbolos matemáticos e as regras para manipulá-los."

### Prompt com poucos exemplos (Few-shot prompting)

Este estilo de prompt ajuda o modelo fornecendo alguns exemplos junto com a solicitação. Consiste em um único prompt com dados adicionais específicos da tarefa. Aqui está um exemplo:

- Prompt: "Escreva um poema no estilo de Shakespeare. Aqui estão alguns exemplos de sonetos de Shakespeare:
  Soneto 18: 'Devo comparar-te a um dia de verão? És mais belo e mais temperado...'
  Soneto 116: 'Não deixemos que a união de mentes verdadeiras Admita impedimentos. O amor não é amor Que muda quando encontra mudança...'
  Soneto 132: 'Teus olhos eu amo, e eles, como se tivessem pena de mim, Sabendo que teu coração me atormenta com desdém,...'
  Agora, escreva um soneto sobre a beleza da lua."
- Resposta: "No céu, a lua suavemente brilha, Em luz prateada que lança sua graça gentil,..."

Os exemplos fornecem ao LLM o contexto, formato ou estilo do resultado desejado. Eles ajudam o modelo a entender a tarefa específica e gerar respostas mais precisas e relevantes.

### Cadeia de raciocínio (Chain-of-thought)

Cadeia de raciocínio é uma técnica muito interessante, pois trata de levar o LLM por uma série de etapas. A ideia é instruir o LLM de forma que ele entenda como fazer algo. Considere o seguinte exemplo, com e sem cadeia de raciocínio:

    - Prompt: "Alice tem 5 maçãs, joga fora 3 maçãs, dá 2 para Bob e Bob devolve uma, quantas maçãs Alice tem?"
    - Resposta: 5

O LLM responde com 5, o que está incorreto. A resposta correta é 1 maçã, dado o cálculo (5 - 3 - 2 + 1 = 1).

Então, como podemos ensinar o LLM a fazer isso corretamente?

Vamos tentar a cadeia de raciocínio. Aplicar a cadeia de raciocínio significa:

1. Dar ao LLM um exemplo semelhante.
1. Mostrar o cálculo e como calculá-lo corretamente.
1. Fornecer o prompt original.

Veja como:

- Prompt: "Lisa tem 7 maçãs, joga fora 1 maçã, dá 4 maçãs para Bart e Bart devolve uma:
  7 - 1 = 6
  6 - 4 = 2
  2 + 1 = 3  
  Alice tem 5 maçãs, joga fora 3 maçãs, dá 2 para Bob e Bob devolve uma, quantas maçãs Alice tem?"
  Resposta: 1

Note como escrevemos prompts substancialmente mais longos com outro exemplo, um cálculo e depois o prompt original, e chegamos à resposta correta, 1.

Como pode ver, a cadeia de raciocínio é uma técnica muito poderosa.

### Conhecimento gerado

Muitas vezes, quando você quer construir um prompt, deseja fazê-lo usando os dados da sua própria empresa. Você quer que parte do prompt venha da empresa e a outra parte seja o prompt que realmente lhe interessa.

Como exemplo, este é o aspecto que seu prompt pode ter se você estiver no setor de seguros:

```text
{{company}}: {{company_name}}
{{products}}:
{{products_list}}
Please suggest an insurance given the following budget and requirements:
Budget: {{budget}}
Requirements: {{requirements}}
```

Acima, você vê como o prompt é construído usando um modelo. No modelo, há várias variáveis, denotadas por `{{variable}}`, que serão substituídas por valores reais de uma API da empresa.

Aqui está um exemplo de como o prompt pode parecer uma vez que as variáveis tenham sido substituídas por conteúdo da sua empresa:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- Car, cheap, 500 USD
- Car, expensive, 1100 USD
- Home, cheap, 600 USD
- Home, expensive, 1200 USD
- Life, cheap, 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000
Requirements: Car, Home, and Life insurance
```

Executar este prompt em um LLM produzirá uma resposta como esta:

```output
Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
- Car, cheap, 500 USD
- Home, cheap, 600 USD
- Life, cheap, 100 USD
Total cost: $1,200 USD
```

Como pode ver, ele também sugere o seguro de vida, o que não deveria. Este resultado é uma indicação de que precisamos otimizar o prompt, tornando-o mais claro sobre o que ele pode permitir. Após alguns _testes e ajustes_, chegamos ao seguinte prompt:

```text
Insurance company: ACME Insurance
Insurance products (cost per month):
- type: Car, cheap, cost: 500 USD
- type: Car, expensive, cost: 1100 USD
- type: Home, cheap, cost: 600 USD
- type: Home, expensive, cost: 1200 USD
- type: Life, cheap, cost: 100 USD

Please suggest an insurance given the following budget and requirements:
Budget: $1000 restrict choice to types: Car, Home
```

Note como adicionar _tipo_ e _custo_ e também usar a palavra-chave _restringir_ ajuda o LLM a entender o que queremos.

Agora obtemos a seguinte resposta:

```output
Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
```

O objetivo deste exemplo foi mostrar que, mesmo quando usamos uma técnica básica como _conhecimento gerado_, ainda precisamos otimizar o prompt na maioria dos casos para obter o resultado desejado.

### Do mais simples ao mais complexo (Least-to-most)

A ideia do prompt do mais simples ao mais complexo é dividir um problema maior em subproblemas. Dessa forma, você ajuda a guiar o LLM sobre como "conquistar" o problema maior. Um bom exemplo pode ser na ciência de dados, onde você pode pedir ao LLM para dividir um problema assim:

> Prompt: Como realizar ciência de dados em 5 etapas?

Com seu assistente de IA respondendo com:

1. Coletar dados
1. Limpar dados
1. Analisar dados
1. Plotar dados
1. Apresentar dados

### Auto-refinamento, criticar os resultados

Com IAs generativas e LLMs, você não pode confiar cegamente no resultado. É necessário verificar. Afinal, o LLM está apenas apresentando o que é mais provável dizer em seguida, não o que é correto. Portanto, uma boa ideia é pedir ao LLM para criticar a si mesmo, o que nos leva à técnica de auto-refinamento.

Como funciona é que você segue os seguintes passos:

1. Prompt inicial pedindo ao LLM para resolver um problema
1. O LLM responde
1. Você critica a resposta e pede à IA para melhorar
1. O LLM responde novamente, desta vez considerando a crítica e sugerindo soluções que ele elaborou

Você pode repetir este processo quantas vezes quiser.

Aqui está um exemplo usando esta técnica:

> Prompt: "Crie uma API Web em Python com rotas para produtos e clientes"

Resposta da IA:

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

> Prompt: sugira 3 melhorias para o código acima

Resposta da IA:

```text
Sure, here are three suggestions to improve the code:

Import the correct module: The first line should import Flask instead of flask. The correct import statement should be from flask import Flask.

Add a main function: Add a if __name__ == '__main__': block to the end of the file to run the application when the file is executed.

Use f-strings: Use f-strings to format the return statements in the route functions. For example, return 'Products' can be changed to return f'This is the {request.path} page'.
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

Como pode ver, a resposta acima da IA está melhorando o primeiro código sugerido graças à crítica feita à primeira resposta.

### Prompt maiêutico (Maieutic prompting)

O prompt maiêutico é uma técnica semelhante ao auto-refinamento, mas trata mais de pedir ao LLM para se explicar. O objetivo é reduzir inconsistências na saída do LLM para garantir que ele chegue à resposta correta. O fluxo de trabalho a seguir é:

1. Pedir ao LLM para responder a uma pergunta
1. Para cada parte da resposta, pedir ao LLM para explicá-la mais detalhadamente.
1. Se houver inconsistências, descartar as partes que são inconsistentes.

Repita os passos 2 e 3 até que tenha analisado todas as partes e esteja satisfeito com a resposta.

Aqui está um exemplo de prompt:

> Prompt: Como posso criar um plano de crise para mitigar uma pandemia em 5 etapas?
> Resposta do LLM:

```text
1. Identify the risks
1. Identify the stakeholders
1. Identify the resources
1. Identify the actions
1. Identify the communication channels
```

Ele identificou 5 etapas, mas podemos determinar se isso está correto? Vamos pedir ao LLM para explicar cada etapa:

> Prompt: Explique a primeira etapa em mais detalhes, quais são os riscos detalhados de uma pandemia?

```text
The risks are the following:

- Loss of life
- Loss of business
- Loss of reputation
- Loss of customers
- Loss of employees
```

Neste ponto, queremos ter certeza de que o LLM está correto, então pedimos que ele explique o primeiro risco em mais detalhes e esperamos que seja consistente com a resposta acima:

> Prompt: Em uma pandemia, qual é o maior risco e por quê?

```text
The biggest risk is loss of life because it's the most important thing to protect.
```

> Quais são os dois maiores riscos em uma pandemia?

```text
The two biggest risks are loss of life and loss of business.
```

Neste ponto, o LLM é consistente e menciona "vida" e "negócios" como os dois maiores riscos. Agora podemos continuar para a próxima etapa e nos sentir razoavelmente confiantes. No entanto, não devemos confiar cegamente no LLM, sempre devemos verificar o resultado.

## Variar o seu resultado

LLMs são naturalmente não determinísticos, o que significa que você obterá resultados diferentes cada vez que executar o mesmo prompt. Experimente o seguinte prompt, por exemplo:

> "Gere código para uma API Web em Python"

```python
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

Executar o mesmo prompt novamente gera uma resposta ligeiramente diferente:

```python
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

> Então, o resultado variado é um problema?

Depende do que você está tentando fazer. Se você quer uma resposta específica, então é um problema. Se você está bem com um resultado variado, como "Gere 3 perguntas sobre geografia", então não é um problema.

### Usando temperatura para variar o seu resultado

Ok, então decidimos que queremos limitar o resultado para ser mais previsível, ou seja, mais determinístico. Como fazemos isso?

Temperatura é um valor entre 0 e 1, onde 0 é o mais determinístico e 1 é o mais variado. O valor padrão é 0.7. Vamos ver o que acontece com duas execuções do mesmo prompt com a temperatura definida em 0.1:

> "Gere código para uma API Web em Python"

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

Há apenas uma pequena diferença entre esses dois resultados. Vamos fazer o oposto desta vez, definir a temperatura para 0.9:

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

e a segunda tentativa com o valor de temperatura definido em 0.9:

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

Como pode ver, os resultados não poderiam ser mais variados.

> Note que existem mais parâmetros que pode alterar para variar o resultado, como top-k, top-p, penalização de repetição, penalização de comprimento e penalização de diversidade, mas estes estão fora do âmbito deste currículo.

## Boas práticas

Existem muitas práticas que pode aplicar para tentar obter o que deseja. Vai encontrar o seu próprio estilo à medida que utiliza mais e mais o prompting.

Além das técnicas que abordámos, há algumas boas práticas a considerar ao criar prompts para um LLM.

Aqui estão algumas boas práticas a considerar:

- **Especificar o contexto**. O contexto é importante; quanto mais puder especificar, como domínio, tópico, etc., melhor.
- Limitar o resultado. Se quiser um número específico de itens ou um comprimento específico, especifique-o.
- **Especificar o quê e como**. Lembre-se de mencionar tanto o que quer como como quer, por exemplo, "Crie uma API Web em Python com rotas para produtos e clientes, dividida em 3 ficheiros".
- **Utilizar templates**. Muitas vezes, vai querer enriquecer os seus prompts com dados da sua empresa. Utilize templates para fazer isso. Os templates podem ter variáveis que substitui por dados reais.
- **Escrever corretamente**. Os LLMs podem fornecer-lhe uma resposta correta, mas se escrever corretamente, obterá uma resposta melhor.

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

Utilize um assistente de IA como o GitHub Copilot ou o ChatGPT e aplique a técnica de "auto-refinamento" para melhorar o código.

## Solução

Por favor, tente resolver o exercício adicionando prompts adequados ao código.

> [!TIP]
> Formule um prompt para pedir melhorias; é uma boa ideia limitar o número de melhorias. Também pode pedir para melhorar de uma forma específica, por exemplo, arquitetura, desempenho, segurança, etc.

[Solução](../../../05-advanced-prompts/python/aoai-solution.py)

## Verificação de conhecimento

Por que usaria o prompting de cadeia de pensamento? Mostre-me 1 resposta correta e 2 respostas incorretas.

1. Para ensinar o LLM a resolver um problema.
1. B, Para ensinar o LLM a encontrar erros no código.
1. C, Para instruir o LLM a propor diferentes soluções.

A: 1, porque o prompting de cadeia de pensamento consiste em mostrar ao LLM como resolver um problema fornecendo-lhe uma série de passos, e problemas semelhantes e como foram resolvidos.

## 🚀 Desafio

Acabou de utilizar a técnica de auto-refinamento no exercício. Pegue em qualquer programa que tenha criado e considere que melhorias gostaria de aplicar. Agora utilize a técnica de auto-refinamento para aplicar as alterações propostas. O que achou do resultado, melhor ou pior?

## Excelente trabalho! Continue a aprender

Depois de completar esta lição, consulte a nossa [coleção de aprendizagem de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprofundar os seus conhecimentos sobre IA generativa!

Avance para a Lição 6, onde aplicaremos os nossos conhecimentos de Engenharia de Prompts [criando aplicações de geração de texto](../06-text-generation-apps/README.md?WT.mc_id=academic-105485-koreyst)

---

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se uma tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.