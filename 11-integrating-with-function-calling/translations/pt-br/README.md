# Integrando com chamadas de função

[![Integrating with function calling](../../images/11-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson11-gh?WT.mc_id=academic-105485-koreyst)

Você aprendeu bastante até agora nas lições anteriores. No entanto, podemos melhorar ainda mais. Algumas coisas que podemos abordar são como podemos obter um formato de resposta mais consistente para facilitar o trabalho com a resposta a jusante. Além disso, podemos querer adicionar dados de outras fontes para enriquecer ainda mais nossa aplicação.

Os problemas mencionados acima são o que este capítulo pretende abordar.

## Introdução

Esta lição abordará:

- Explicará o que é a chamada de função e seus casos de uso.
- Criar uma chamada de função usando o Azure OpenAI.
- Como integrar uma chamada de função em um aplicativo.

## Metas de Aprendizado

Após concluir esta lição, você será capaz de:

- Explicar o propósito de usar chamadas de função.
- Configurar a Chamada de Função usando o Serviço Azure Open AI.
- Projetar chamadas de função eficazes para o caso de uso do seu aplicativo.

## Cenário: melhorando nosso chatbot com funções

Para esta lição, queremos criar um recurso para nossa startup de educação que permite aos usuários usar um chatbot para encontrar cursos técnicos. Vamos recomendar cursos que se encaixem no nível de habilidade deles, função atual e tecnologia de interesse.

Para completar este cenário, usaremos uma combinação de:

- `Azure Open AI` para criar uma experiência de chat para o usuário.
- `Microsoft Learn Catalog API` para ajudar os usuários a encontrar cursos com base na solicitação do usuário.
- `Chamada de Função` para pegar a consulta do usuário e enviá-la a uma função para fazer a solicitação à API.

Para começar, vamos ver por que queremos usar chamada de função em primeiro lugar:

## Por que a Chamada de Função

Antes da chamada de função, as respostas de um LLM eram desestruturadas e inconsistentes. Os desenvolvedores eram obrigados a escrever código de validação complexo para garantir que pudessem lidar com cada variação de uma resposta. Os usuários não podiam obter respostas como "Qual é a temperatura atual em Estocolmo?". Isso ocorre porque os modelos eram limitados ao tempo em que os dados foram treinados.

A Chamada de Função é um recurso do Serviço Azure Open AI para superar as seguintes limitações:

- **Formato de resposta consistente**. Se pudermos controlar melhor o formato da resposta, podemos integrar mais facilmente a resposta a jusante em outros sistemas.
- **Dados externos**. Capacidade de usar dados de outras fontes de um aplicativo em um contexto de chat.

## Ilustrando o problema por meio de um cenário

> Recomendamos que você crie um arquivo _Notebook.ipynb_ e cole o código abaixo em células de código separadas se quiser executar o cenário abaixo. Você também pode apenas ler enquanto tentamos ilustrar um problema em que as funções podem ajudar a resolver o problema.

Vamos dar uma olhada no exemplo que ilustra o problema do formato de resposta:

Digamos que queremos criar um banco de dados de dados de estudantes para que possamos sugerir o curso certo para eles. Abaixo temos duas descrições de estudantes que são muito semelhantes nos dados que contêm.

1. Crie uma conexão com nosso recurso Azure Open AI:

   ```python
   import os
   import openai
   import json
   openai.api_type = "azure"
   openai.api_base = "YOUR OPENAI API BASE URL"
   openai.api_version = "2023-07-01-preview"
   openai.api_key = os.getenv("OPENAI_API_KEY")
   ```

   Acima está algum código Python para configurar nossa conexão com o Azure Open AI, onde definimos `api_type`, `api_base`, `api_version` e `api_key`.

1. Crie duas descrições de estudantes usando as variáveis `student_1_description` e `student_2_description`.

   ```python
   student_1_description="Emily Johnson is a sophomore majoring in computer science at Duke University. She has a 3.7 GPA. Emily is an active member of the university's Chess Club and Debate Team. She hopes to pursue a career in software engineering after graduating."

   student_2_description = "Michael Lee is a sophomore majoring in computer science at Stanford University. He has a 3.8 GPA. Michael is known for his programming skills and is an active member of the university's Robotics Club. He hopes to pursue a career in artificial intelligence after finishing his studies."
   ```

   Nós queremos enviar as descrições de estudantes acima para um LLM para analisar os dados. Esses dados podem ser usados posteriormente em nosso aplicativo e enviados para uma API ou armazenados em um banco de dados.

1. Vamos criar duas solicitações idênticas nas quais instruímos o LLM sobre as informações que nos interessam:

   ```python
   prompt1 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_1_description}
   '''

   prompt2 = f'''
   Please extract the following information from the given text and return it as a JSON object:

   name
   major
   school
   grades
   club

   This is the body of text to extract the information from:
   {student_2_description}
   '''
   ```

   O prompt acima instrui o LLM a extrair informações e retornar a resposta no formato JSON.

1. Após configurar os prompts e a conexão com o Azure Open AI, agora enviaremos os prompts para o LLM usando `openai.ChatCompletion`. Armazenamos o prompt na variável `messages` e atribuímos a função `user`. Isso é para imitar uma mensagem de um usuário sendo escrita em um chatbot.

   ```python
   # response from prompt one
   openai_response1 = openai.ChatCompletion.create(
     engine="gpt-function",
     messages = [{'role': 'user', 'content': prompt1}]
   )
   openai_response1['choices'][0]['message']['content']

   # response from prompt two
   openai_response2 = openai.ChatCompletion.create(
     engine="gpt-function",
     messages = [{'role': 'user', 'content': prompt2 }]
   )
   openai_response2['choices'][0]['message']['content']
   ```

Agora nós podemos enviar ambas as solicitações para o LLM e examinar a resposta que recebemos encontrando-a assim `openai_response1['choices'][0]['message']['content']`.

1. Por fim, podemos converter a resposta para o formato JSON chamando `json.loads`:

   ```python
   # Loading the response as a JSON object
   json_response1 = json.loads(openai_response1['choices'][0]['message']['content'])
   json_response1
   ```

   Resposta 1:

   ```json
   {
     "name": "Emily Johnson",
     "major": "computer science",
     "school": "Duke University",
     "grades": "3.7",
     "club": "Chess Club"
   }
   ```

   Resposta 2:

   ```json
   {
     "name": "Michael Lee",
     "major": "computer science",
     "school": "Stanford University",
     "grades": "3.8 GPA",
     "club": "Robotics Club"
   }
   ```

   Embora os prompts sejam os mesmos e as descrições sejam semelhantes, vemos que os valores da propriedade `Grades` são formatados de maneira diferente, como `3.7` ou `3.7 GPA`, por exemplo.

   Isso ocorre porque o LLM recebe dados não estruturados na forma do prompt escrito e também retorna dados não estruturados. Precisamos ter um formato estruturado para saber o que esperar ao armazenar ou usar esses dados.

Então, como resolvemos o problema de formatação? Ao usar chamadas de função, podemos garantir que recebemos dados estruturados de volta. Ao usar chamadas de função, o LLM na verdade não chama ou executa funções. Em vez disso, criamos uma estrutura para o LLM seguir para suas respostas. Em seguida, usamos essas respostas estruturadas para saber qual função executar em nossos aplicativos.

![fluxo de função](../../images/Function-Flow.png?WT.mc_id=academic-105485-koreyst)

Podemos então pegar o que é retornado da função e enviar isso de volta ao LLM. O LLM responderá usando linguagem natural para responder à consulta do usuário.

## Casos de uso para chamadas de função

Existem muitos casos de uso diferentes em que chamadas de função podem aprimorar seu aplicativo, como:

- **Chamando Ferramentas Externas**. Chatbots são ótimos para fornecer respostas a perguntas dos usuários. Ao usar chamadas de função, os chatbots podem usar mensagens dos usuários para concluir determinadas tarefas. Por exemplo, um aluno pode pedir ao chatbot para "Enviar e-mail ao meu instrutor dizendo que preciso de mais ajuda com este assunto". Isso pode fazer uma chamada de função para `send_email(to: string, body: string)`.

- **Criando Consultas de API ou Banco de Dados**. Os usuários podem encontrar informações usando linguagem natural que é convertida em uma consulta ou solicitação de API formatada. Um exemplo disso pode ser um professor que solicita "Quais são os alunos que concluíram a última tarefa", o que poderia chamar uma função chamada `get_completed(student_name: string, assignment: int, current_status: string)`.

- **Criando Dados Estruturados**. Os usuários podem pegar um bloco de texto ou CSV e usar o LLM para extrair informações importantes. Por exemplo, um aluno pode converter um artigo da Wikipedia sobre acordos de paz para criar cartões de memória de IA. Isso pode ser feito usando uma função chamada `get_important_facts(agreement_name: string, date_signed: string, parties_involved: list)`.

## Criando Sua Primeira Chamada de Função

O processo de criar uma chamada de função inclui 3 etapas principais:

1. **Chamando** a API de Completions de Chat com uma lista de suas funções e uma mensagem do usuário.
2. **Lendo** a resposta do modelo para realizar uma ação, ou seja, executar uma função ou chamada de API.
3. **Fazendo** outra chamada para a API de Completions de Chat com a resposta de sua função para usar essas informações e criar uma resposta para o usuário.

![Fluxo LLM](../../images/LLM-Flow.png?WT.mc_id=academic-105485-koreyst)

### Etapa 1 - criando mensagens

A primeira etapa é criar uma mensagem do usuário. Isso pode ser atribuído dinamicamente, pegando o valor de uma entrada de texto, ou você pode atribuir um valor aqui. Se esta é a sua primeira vez trabalhando com a API de Completions de Chat, precisamos definir o `role` e o `content` da mensagem.

O `role` pode ser `system` (criando regras), `assistant` (o modelo) ou `user` (o usuário final). Para chamadas de função, vamos atribuir isso como `user` e uma pergunta de exemplo.

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Ao atribuir diferentes papéis, fica claro para o LLM se é o sistema dizendo algo ou o usuário, o que ajuda a criar um histórico de conversação no qual o LLM pode se basear.

### Etapa 2 - criando funções

Em seguida, definiremos uma função e os parâmetros dessa função. Usaremos apenas uma função aqui chamada `search_courses`, mas você pode criar várias funções.

> **Importante**: As funções são incluídas na mensagem do sistema para o LLM e serão contadas na quantidade de tokens disponíveis.

Abaixo, criamos as funções como uma matriz de itens. Cada item é uma função e tem propriedades `name`, `description` e `parameters`:

```python
functions = [
   {
      "name":"search_courses",
      "description":"Retrieves courses from the search index based on the parameters provided",
      "parameters":{
         "type":"object",
         "properties":{
            "role":{
               "type":"string",
               "description":"The role of the learner (i.e. developer, data scientist, student, etc.)"
            },
            "product":{
               "type":"string",
               "description":"The product that the lesson is covering (i.e. Azure, Power BI, etc.)"
            },
            "level":{
               "type":"string",
               "description":"The level of experience the learner has prior to taking the course (i.e. beginner, intermediate, advanced)"
            }
         },
         "required":[
            "role"
         ]
      }
   }
]
```

Vamos descrever cada instância de função mais detalhadamente abaixo:

- `name` - O nome da função que queremos que seja chamada.
- `description` - Esta é a descrição de como a função funciona. Aqui é importante ser específico e claro.
- `parameters` - Uma lista de valores e formatos que você deseja que o modelo produza em sua resposta. A matriz de parâmetros consiste em itens, onde cada item tem as seguintes propriedades:
  1.  `type` - O tipo de dados no qual as propriedades serão armazenadas.
  1.  `properties` - Lista dos valores específicos que o modelo usará para sua resposta
      1. `name` - A chave é o nome da propriedade que o modelo usará em sua resposta formatada, por exemplo, `product`.
      1. `type` - O tipo de dados desta propriedade, por exemplo, `string`.
      1. `description` - Descrição da propriedade específica.

Há também uma propriedade opcional `required` - propriedade necessária para que a chamada da função seja concluída.

### Etapa 3 - Fazendo a chamada da função

Depois de definir uma função, agora precisamos incluí-la na chamada à API de Completção de Bate-papo. Fazemos isso adicionando `functions` à solicitação. Neste caso, `functions=functions`.

Também há a opção de definir `function_call` como `auto`. Isso significa que vamos deixar o LLM decidir qual função deve ser chamada com base na mensagem do usuário, em vez de atribuirmos.

Aqui está algum código abaixo onde chamamos `ChatCompletion.create`, observe como definimos `functions=functions` e `function_call="auto"`, dando assim ao LLM a escolha de quando chamar as funções que fornecemos:

```python
response = openai.ChatCompletion.create( engine="gpt-function",
                                        messages=messages,
                                        functions=functions,
                                        function_call="auto", )

print(response['choices'][0]['message'])
```

The response coming back now looks like so:

```json
{
  "role": "assistant",
  "function_call": {
    "name": "search_courses",
    "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
  }
}
```

Aqui nós podemos ver como a função `search_courses` foi chamada e com quais argumentos, conforme listado na propriedade `arguments` na resposta JSON.

A conclusão de que o LLM foi capaz de encontrar os dados para se encaixar nos argumentos da função, pois estava extraindo-o do valor fornecido ao parâmetro `messages` na chamada de conclusão do chat. Abaixo está um lembrete do valor `messages`:

```python
messages= [ {"role": "user", "content": "Find me a good course for a beginner student to learn Azure."} ]
```

Como você pode ver, `student`, `Azure` e `beginner` foram extraídos de `messages` e definidos como entrada para a função. Usar funções dessa maneira é uma ótima maneira de extrair informações de um prompt, mas também de fornecer estrutura ao LLM e ter funcionalidade reutilizável.

Agora, precisamos ver como podemos usar isso em nosso aplicativo.

## Integrando Chamadas de Função em um Aplicativo

Após testarmos a resposta formatada do LLM, agora podemos integrá-la a um aplicativo.

### Gerenciando o fluxo

Para integrar isso ao nosso aplicativo, siga estas etapas:

1. First, let's make the call to the Open AI services and store the message in a variable called `response_message`.

1. Primeiro, vamos fazer a chamada aos serviços Open AI e armazenar a mensagem em uma variável chamada `response_message`.

   ```python
   response_message = response["choices"][0]["message"]
   ```

1. Agora vamos definir a função que chamará a API Microsoft Learn para obter uma lista de cursos:

   ```python
   import requests

   def search_courses(role, product, level):
     url = "https://learn.microsoft.com/api/catalog/"
     params = {
        "role": role,
        "product": product,
        "level": level
     }
     response = requests.get(url, params=params)
     modules = response.json()["modules"]
     results = []
     for module in modules[:5]:
        title = module["title"]
        url = module["url"]
        results.append({"title": title, "url": url})
     return str(results)
   ```

   Observe como agora criamos uma função Python real que mapeia para os nomes de função introduzidos na variável `functions`. Também estamos fazendo chamadas reais de API externa para buscar os dados de que precisamos. Neste caso, vamos contra a API Microsoft Learn para pesquisar módulos de treinamento.

Ok! Então criamos variáveis `functions` e uma função Python correspondente, como dizemos ao LLM como mapear essas duas coisas para que nossa função Python seja chamada?

1. Para ver se precisamos chamar uma função Python, precisamos olhar para a resposta LLM e ver se `function_call` faz parte dela e chamar a função apontada. Veja como você pode fazer a verificação mencionada abaixo:

   ```python
   # Check if the model wants to call a function
   if response_message.get("function_call"):
     print("Recommended Function call:")
     print(response_message.get("function_call"))
     print()

    # Call the function.
    function_name = response_message["function_call"]["name"]

    available_functions = {
            "search_courses": search_courses,
    }
    function_to_call = available_functions[function_name]

    function_args = json.loads(response_message["function_call"]["arguments"])
    function_response = function_to_call(**function_args)

    print("Output of function call:")
    print(function_response)
    print(type(function_response))


    # Add the assistant response and function response to the messages
    messages.append( # adding assistant response to messages
        {
            "role": response_message["role"],
            "function_call": {
                "name": function_name,
                "arguments": response_message["function_call"]["arguments"],
            },
            "content": None
        }
    )
    messages.append( # adding function response to messages
        {
            "role": "function",
            "name": function_name,
            "content":function_response,
        }
    )
   ```

   Essas três linhas garantem que extraímos o nome da função, os argumentos e fazemos a chamada:

   ```python
   function_to_call = available_functions[function_name]

   function_args = json.loads(response_message["function_call"]["arguments"])
   function_response = function_to_call(**function_args)
   ```

   Acima está a saída da execução do nosso código:

   **Saída**

   ```Recommended Function call:
   {
     "name": "search_courses",
     "arguments": "{\n  \"role\": \"student\",\n  \"product\": \"Azure\",\n  \"level\": \"beginner\"\n}"
   }

   Output of function call:
   [{'title': 'Describe concepts of cryptography', 'url': 'https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Introduction to audio classification with TensorFlow', 'url': 'https://learn.microsoft.com/en-
   us/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi'}, {'title': 'Design a Performant Data Model in Azure SQL
   Database with Azure Data Studio', 'url': 'https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?
   WT.mc_id=api_CatalogApi'}, {'title': 'Getting started with the Microsoft Cloud Adoption Framework for Azure', 'url':
   'https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi'}, {'title': 'Set up the
   Rust development environment', 'url': 'https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi'}]
   <class 'str'>
   ```

1. Agora enviaremos a mensagem atualizada, `messages` para o LLM para que possamos receber uma resposta em linguagem natural em vez de uma resposta formatada em JSON da API.

   ```python
   print("Messages in next request:")
   print(messages)
   print()

   second_response = openai.ChatCompletion.create(
     messages=messages,
     engine="gpt-function",
     function_call="auto",
     functions=functions,
     temperature=0
        )  # get a new response from GPT where it can see the function response


   print(second_response["choices"][0]["message"])
   ```

   **Saída**

   ```python
   {
     "role": "assistant",
     "content": "I found some good courses for beginner students to learn Azure:\n\n1. [Describe concepts of cryptography] (https://learn.microsoft.com/training/modules/describe-concepts-of-cryptography/?WT.mc_id=api_CatalogApi)\n2. [Introduction to audio classification with TensorFlow](https://learn.microsoft.com/training/modules/intro-audio-classification-tensorflow/?WT.mc_id=api_CatalogApi)\n3. [Design a Performant Data Model in Azure SQL Database with Azure Data Studio](https://learn.microsoft.com/training/modules/design-a-data-model-with-ads/?WT.mc_id=api_CatalogApi)\n4. [Getting started with the Microsoft Cloud Adoption Framework for Azure](https://learn.microsoft.com/training/modules/cloud-adoption-framework-getting-started/?WT.mc_id=api_CatalogApi)\n5. [Set up the Rust development environment](https://learn.microsoft.com/training/modules/rust-set-up-environment/?WT.mc_id=api_CatalogApi)\n\nYou can click on the links to access the courses."
   }

   ```

## Tarefa

Para continuar seu aprendizado sobre a Chamada de Função do Azure Open AI, você pode:

- Adicionar mais parâmetros à função que podem ajudar os aprendizes a encontrar mais cursos.
- Criar outra chamada de função que obtenha mais informações do aprendiz, como o idioma nativo.
- Implementar tratamento de erro quando a chamada de função e/ou a chamada da API não retornar cursos adequados.

Dica: Consulte a [documentação de referência da API Learn](https://learn.microsoft.com/training/support/catalog-api-developer-reference?WT.mc_id=academic-105485-koreyst) para ver como e onde esses dados estão disponíveis.

## Ótimo trabalho! Continue a jornada

Após completar esta lição, confira nossa [coleção de aprendizado sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos em IA Generativa!

Vá para a Lição 12, onde veremos como [Projetando UX para aplicativos de IA](../../../12-designing-ux-for-ai-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
