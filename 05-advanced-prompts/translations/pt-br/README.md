# Criando prompts avançados

[![Creating Advanced Prompts](../../images/05-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=f3615e46-dbca-477c-832d-21eef95cd9f3?WT.mc_id=academic-105485-koreyst)

Vamos recapitular algumas aprendizagens do capítulo anterior:

> A _engenharia_ de prompts é o processo pelo qual **guiamos o modelo em direção a respostas mais relevantes** fornecendo instruções ou contexto mais úteis.

Também existem duas etapas para escrever prompts: a construção do prompt, fornecendo contexto relevante, e a segunda parte é a _otimização_, como melhorar gradualmente o prompt.

Neste ponto, temos uma compreensão básica de como escrever prompts, mas precisamos aprofundar. Neste capítulo, você passará de experimentar vários prompts para entender por que um prompt é melhor que outro.

## Introdução

Neste capítulo, abordaremos os seguintes tópicos:

- Amplie seu conhecimento de engenharia de prompts aplicando diferentes técnicas aos seus prompts.
- Configure seus prompts para variar a saída.

## Metas de aprendizado

Após concluir esta lição, você será capaz de:

- Aplicar técnicas de engenharia de prompts que melhorem o resultado dos seus prompts.
- Realizar prompts que sejam variados ou determinísticos.

## Engenharia de prompts

A engenharia de prompts é o processo de criar prompts que produzirão o resultado desejado. Há mais na engenharia de prompts do que simplesmente escrever um prompt de texto. A engenharia de prompts não é uma disciplina de engenharia; é mais um conjunto de técnicas que você pode aplicar para obter o resultado desejado.

### Um exemplo de prompt

Vamos pegar um prompt básico como este:

> Generate 10 questions on geography.

Neste prompt, você está aplicando na verdade um conjunto de diferentes técnicas de prompt.

Vamos analisar isso.

- **Contexto**, você especifica que deve ser sobre "geografia".
- **Limitação da saída**, você não quer mais do que 10 perguntas.

### Limitações de prompts simples

Você pode ou não obter o resultado desejado. Você terá suas perguntas geradas, mas a geografia é um tópico amplo e você pode não obter o que deseja devido às seguintes razões:

- **Tópico amplo**, você não sabe se será sobre países, capitais, rios e assim por diante.
- **Formato**, e se você quisesse que as perguntas fossem formatadas de uma maneira específica?

Como você pode ver, há muito a considerar ao criar prompts.

Até agora, vimos um exemplo simples de prompt, mas a IA generativa é capaz de muito mais para ajudar pessoas em várias funções e indústrias. Vamos explorar algumas técnicas básicas a seguir.

### Técnicas de prompting

Primeiro, precisamos entender que o prompting é uma propriedade _emergente_ de um LLM, o que significa que não é uma característica incorporada ao modelo, mas sim algo que descobrimos conforme usamos o modelo.

Existem algumas técnicas básicas que podemos usar para fazer um prompt em um LLM. Vamos explorá-las.

- **Prompt de poucas tentativas**, esta é a forma mais básica de prompt. É um prompt único com alguns exemplos.
- **Corrente de pensamento**, este tipo de prompt diz ao LLM como dividir um problema em etapas.
- **Conhecimento gerado**, para melhorar a resposta de um prompt, você pode fornecer fatos ou conhecimentos gerados adicionalmente ao seu prompt.
- **Do menos para o mais**, assim como a corrente de pensamento, esta técnica consiste em dividir um problema em uma série de etapas e depois pedir que essas etapas sejam realizadas em ordem.
- **Auto-aperfeiçoamento**, esta técnica consiste em criticar a saída do LLM e depois pedir que ele melhore.
- **Prompt maieutico**. O que você deseja aqui é garantir que a resposta do LLM esteja correta e pedir que ele explique várias partes da resposta. Isso é uma forma de auto-aperfeiçoamento.

### Prompt de Poucas Tentativas

Este estilo de prompt é muito simples, pode consistir em um único prompt e possivelmente alguns exemplos. Essa técnica é provavelmente o que você está usando ao começar a aprender sobre LLMs. Aqui está um exemplo:

- Prompt: "O que é Álgebra?"
- Resposta: "Álgebra é uma ramificação da matemática que estuda símbolos matemáticos e as regras para manipular esses símbolos."

### Prompt - Corrente de Pensamento (chain-of-thought prompting)

O prompt corrente de pensamento é uma técnica muito interessante, pois envolve levar o LLM por uma série de etapas. A ideia é instruir o LLM de tal forma que ele entenda como fazer algo. Considere o seguinte exemplo, com e sem corrente de pensamento:

    - Prompt: "Alice tem 5 maçãs, joga 3 maçãs, dá 2 para Bob e Bob devolve uma, quantas maçãs Alice tem?"
    - Resposta: 5

O LLM responde com 5, o que está incorreto. A resposta correta é 1 maçã, dada a seguinte operação (5 -3 -2 + 1 = 1).

Então, como podemos ensinar o LLM a fazer isso corretamente?

Vamos tentar a corrente de pensamento. Aplicar a corrente de pensamento significa:

1. Dar ao LLM um exemplo semelhante.
1. Mostrar o cálculo e como calculá-lo corretamente.
1. Fornecer o prompt original.

Veja como:

- Prompt: "Lisa tem 7 maçãs, joga 1 maçã, dá 4 maçãs para Bart e Bart devolve uma:
  7 -1 = 6
  6 -4 = 2
  2 +1 = 3  
  Alice tem 5 maçãs, joga 3 maçãs, dá 2 para Bob e Bob devolve uma, quantas maçãs Alice tem?"
  Resposta: 1

Note como escrevemos prompts substancialmente mais longos com outro exemplo, um cálculo e, em seguida, o prompt original, e chegamos à resposta correta, que é 1.

Como você pode ver, a corrente de pensamento é uma técnica muito poderosa.

### Conhecimento Gerado

Muitas vezes, ao criar uma solicitação, você deseja fazê-lo usando os dados de sua própria empresa. Você quer que parte da solicitação seja da empresa e a outra parte seja a solicitação real que você está interessado.

Como exemplo, é assim que sua solicitação pode parecer se você estiver no ramo de seguros:

    ```text
    {{company}}: {{company_name}}
    {{products}}:
    {{products_list}}
    Please suggest an insurance given the following budget and requirements:
    Budget: {{budget}}
    Requirements: {{requirements}}
    ```

Acima, você vê como a solicitação é construída usando um modelo. No modelo, há várias variáveis, indicadas por `{{variável}}`, que serão substituídas por valores reais de uma API da empresa.

Aqui está um exemplo de como a solicitação pode parecer depois que as variáveis foram substituídas pelo conteúdo de sua empresa:

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
    Requirements: Car, Home
    ```

Executando esta solicitação em um Modelo de Linguagem com Aprendizado Profundo (LLM), o resultado será algo como:

    ```output
    , and Life insurance

    Given the budget and requirements, we suggest the following insurance package from ACME Insurance:
    - Car, cheap, 500 USD
    - Home, cheap, 600 USD
    - Life, cheap, 100 USD
    Total cost: $1,200 USD
    ```

Como você pode ver, também sugere o seguro de vida, o que não deveria acontecer. Este resultado é uma indicação de que precisamos otimizar a solicitação tornando-a mais clara sobre o que é permitido. Após alguma _tentativa e erro_, chegamos à seguinte solicitação:

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

Observe como adicionar _tipo_ e _custo_ e também usar a palavra-chave _restringir_ ajuda o LLM a entender o que queremos.

Agora obtemos a seguinte resposta:

    ```output
    Given the budget and requirements, we suggest the Car, Cheap insurance product which costs 500 USD per month.
    ```

O objetivo deste exemplo foi mostrar que, mesmo que estejamos usando uma técnica básica como _conhecimento gerado_, ainda precisamos otimizar o prompt na maioria dos casos para obter o resultado desejado.

### Least-to-most

The idea with Least-to-most prompting is to break down a bigger problem into subproblems. That way, you help guide the LLM on how to "conquer" the bigger problem. A good example could be for data science where you can ask the LLM to divide up a problem like so:

> Prompt: How to perform data science in 5 steps?

With your AI assistant answering with:

1. Collect data
1. Clean data
1. Analyze data
1. Plot data
1. Present data

### Self-refine, critique the results

With generative AIs and LLMs, you can't trust the output. You need to verify it. After all, the LLM is just presenting you what's the next most likely thing to say, not what's correct. Therefore, a good idea is to ask the LLM to critique itself, which leads us to the self-refine technique.

How it works is that you follow the following steps:

1. Initial prompt asking the LLM to solve a problem
1. LLM answers
1. You critique the answer and ask the AI to improve
1. LLM answers again, this time considering the critique and suggest solutions it came up with

You can repeat this process as many times as you want.

Here's an example using this technique:

### Menos para mais

A ideia com a técnica do prompt "Menos para mais" é decompor um problema maior em subproblemas. Dessa forma, você ajuda a orientar o LLM sobre como "conquistar" o problema maior. Um bom exemplo pode ser em ciência de dados, onde você pode pedir ao LLM para dividir um problema da seguinte maneira:

> Prompt: How to perform data science in 5 steps?

Com seu assistente de IA respondendo:

1. Coletar dados
1. Limpar dados
1. Analisar dados
1. Plotar dados
1. Apresentar dados

### Autoaperfeiçoamento, crítica dos resultados

Com AIs generativas e LLMs, você não pode confiar na saída. É preciso verificá-la. Afinal, o LLM está apenas apresentando o que é mais provável dizer a seguir, não o que está correto. Portanto, uma boa ideia é pedir ao LLM que faça uma autocrítica, o que nos leva à técnica de autoaperfeiçoamento.

Como funciona é como você segue os seguintes passos:

1. Prompt inicial pedindo ao LLM para resolver um problema
1. LLM responde
1. Você critica a resposta e pede à IA para melhorar
1. LLM responde novamente, desta vez considerando a crítica e sugerindo soluções que elaborou

Você pode repetir esse processo quantas vezes quiser.

Aqui está um exemplo usando essa técnica:

> Prompt: "Create a Python Web API with routes products and customers"

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

> Prompt: suggest 3 improvements of the above code

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

Como você pode ver, a resposta da IA acima está aprimorando o primeiro código sugerido, graças à crítica da primeira resposta.

### Maieutic prompting

Maieutic prompting is a technique that is similar to self-refine but it's more about asking the LLM to explain itself. The goal is to reduce inconsistencies in the LLM's output so to ensure it arrives at the correct answer. The workflow to follow is:

1. Ask the LLM to answer a question
1. For each part of the answer, ask the LLM to explain it more in depth.
1. If there are inconsistencies, discard the parts that are inconsistent.

Repeat 2 and 3 until you've gone through all the parts and you're satisfied with the answer.

Here's an example prompt:

### Prompt de Maiêutico

O prompt de maiêutico é uma técnica semelhante ao autoaperfeiçoamento, mas trata-se mais de pedir ao LLM para se explicar. O objetivo é reduzir inconsistências na saída do LLM para garantir que ele chegue à resposta correta. O fluxo de trabalho a ser seguido é:

1. Peça ao LLM para responder a uma pergunta.
1. Para cada parte da resposta, peça ao LLM para explicá-la mais detalhadamente.
1. Se houver inconsistências, descarte as partes inconsistentes.

Repita os passos 2 e 3 até passar por todas as partes e ficar satisfeito com a resposta.

Aqui está um exemplo de um prompt:

> prompt: How can I create a crisis plan to mitigate a pandemic in 5 steps?
> LLM answer:

    ```text
    1. Identify the risks
    1. Identify the stakeholders
    1. Identify the resources
    1. Identify the actions
    1. Identify the communication channels
    ```

São identificadas 5 etapas, mas podemos determinar se isso está correto? Vamos pedir ao LLM para explicar cada etapa:

> prompt: Explain the first step in more detail, what are the risks in detail with a pandemic?

    ```text
    The risks are the following:

    - Loss of life
    - Loss of business
    - Loss of reputation
    - Loss of customers
    - Loss of employees
    ```

Neste ponto, queremos ter certeza de que o LLM está correto, por isso pedimos que explique o primeiro risco com mais detalhes e esperamos que seja consistente com a resposta acima:

> prompt: In a Pandemic, which is the biggest risk and why?

    ```text
    The biggest risk is loss of life because it's the most important thing to protect.
    ```

> What are the two biggest risks in a pandemic?

    ```text
    The two biggest risks are loss of life and loss of business.
    ```

Neste ponto, o LLM é consistente e menciona "vida" e "negócios" como os dois principais riscos. Podemos agora prosseguir para o próximo passo e sentir confiança razoável. No entanto, não devemos confiar cegamente no LLM; sempre devemos verificar a saída.

## Varie sua saída

Os LLMs são, por natureza, não-determinísticos, o que significa que você obterá resultados diferentes cada vez que executar o mesmo prompt. Tente o seguinte prompt, por exemplo:

> "Generate code for a Python Web API"

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

Execute o mesmo prompt novamente e você observará que vai gerar uma resposta ligeiramente diferente:

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

> Então, a saída diferente é um problema?

Depende do que você está tentando fazer. Se você deseja uma resposta específica, é um problema. Se você está bem com uma saída variada como "Gerar 3 perguntas sobre geografia", então não é um problema.

### Usando a temperatura para variar sua saída

Ok! Então, decidimos que queremos limitar a saída para ser mais previsível, ou seja, mais determinística. Como fazemos isso?

Temperatura é um valor entre 0 e 1, onde 0 é o mais determinístico e 1 é o mais variado. O valor padrão é 0.7. Vamos ver o que acontece com duas execuções do mesmo prompt com temperatura definida como 0.1:

> "Generate code for a Python Web API"

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

Execute o prompt novamente e você verá este resultado:

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

Há apenas uma pequena diferença entre essas duas saídas. Vamos fazer o contrário desta vez, vamos definir a temperatura para 0.9:

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

e a segunda tentativa em 0,9 como valor de temperatura:

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

> Observe que, existem mais parâmetros que você pode alterar para variar a saída, como top-k, top-p, penalidade de repetição, penalidade de comprimento e penalidade de diversidade, mas estes estão fora do escopo deste currículo.

## Boas práticas

Há muitas práticas que você pode aplicar para tentar obter o que deseja. Você encontrará seu próprio estilo à medida que usar mais e mais prompts.

Além das técnicas que cobrimos, existem algumas boas práticas a serem consideradas ao solicitar um LLM.

Aqui estão algumas boas práticas a serem consideradas:

- **Especifique o contexto**: O contexto é importante. Quanto mais você puder especificar, como domínio, tópico, etc., será muito melhor.
- **Limite a saída**: Se você deseja um número específico de itens ou um comprimento específico, especifique.
- **Especifique tanto o que, quanto e como**: Lembre-se de mencionar tanto o que você deseja quanto como deseja. Por exemplo: _Crie uma API da Web em Python com rotas para produtos e clientes, dividindo-a em 3 arquivos_.
- **Use modelos**: Muitas vezes, você desejará enriquecer suas solicitações com dados da sua empresa. Use modelos para fazer isso. Os modelos podem ter variáveis que você substitui por dados reais.
- **Escreva corretamente**: Os LLMs podem fornecer uma resposta correta. Mas, se você escrever corretamente, obterá uma resposta melhor.

## Tarefa

Aqui está o código em Python que mostra como criar uma API simples usando o Flask:

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

Use um assistente de IA como o GitHub Copilot ou o ChatGPT e aplique a técnica de "auto-aperfeiçoamento" para melhorar o código.

## Solução

Por favor, tente resolver a tarefa adicionando prompts adequados ao código.

> [!DICA]
> Formule um prompt para pedir que ele melhor. É uma boa ideia limitar quantas melhorias devem ter. Você também pode pedir para melhorar de uma certa maneira, por exemplo, arquitetura, desempenho, segurança, etc.

[Solution](../../python/aoai-solution.py?WT.mc_id=academic-105485-koreyst)

## Verificação de conhecimento

Por que eu usaria a técnica de prompt de corrente de pensamento? Mostre-me 1 resposta correta e 2 respostas incorretas.

Para ensinar o LLM a resolver um problema.
B, Para ensinar o LLM a encontrar erros no código.
C, Para instruir o LLM a propor diferentes soluções.

Resposta correta: A, 1, porque o prompt de corrente de pensamento trata de mostrar ao LLM como resolver um problema, fornecendo uma série de passos e problemas semelhantes e como foram resolvidos.

## 🚀 Desafio

Você acabou de usar a técnica de auto-aperfeiçoamento na atribuição. Pegue qualquer programa que você criou e considere quais melhorias você gostaria de aplicar a ele. Agora, use a técnica de auto-aperfeiçoamento para aplicar as alterações propostas. O que você achou do resultado, melhor ou pior?

## Ótimo trabalho! Continue seu aprendizado

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos sobre IA generativa!

Agora, vamos para a Lição 6, onde aplicaremos nosso conhecimento de Engenharia de Prompt, [construindo aplicativos de geração de texto](../../../06-text-generation-apps/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)
