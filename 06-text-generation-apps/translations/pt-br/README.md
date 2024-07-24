# Desenvolvendo Aplicativos de Geração de Texto

[![Building Text Generation Applications](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

Você viu até agora neste currículo que existem conceitos básicos como prompts e até mesmo uma disciplina inteira chamada "engenharia de prompts". Muitas ferramentas com as quais você pode interagir, como ChatGPT, Office 365, Microsoft Power Platform e muito mais, suportam o uso de prompts para realizar algo.

Para que você adicione tal experiência a um aplicação, você precisa entender conceitos como prompts, conclusões e escolher uma biblioteca para trabalhar. É exatamente isso que você aprenderá neste capítulo.

## Introdução

Nesse capítulo, você aprenderá:

- Aprender sobre a biblioteca openai e seus conceitos básicos.
- Criar uma aplicação de geração de texto usando openai.
- Entender como usar conceitos como prompt, temperatura e tokens para construir um aplicativo de geração de texto.

## Objetivos de aprendizagem

No final desta lição, você será capaz de:

- Explicar o que é uma aplicação de geração de texto.
- Criar uma aplicação de geração de texto usando openai.
- Configurar sua aplicação para usar mais ou menos tokens e também alterar a temperatura, para uma saída variada.

## O que é uma aplicação de geração de texto?

Normalmente quando você desenvolve uma aplicaçaõ, ele tem algum tipo de interface como a seguinte:

- Baseado em comando. Aplicações de console são aplicativos típicos onde você digita um comando e ele executa uma tarefa. Por exemplo, `git` é um aplicativo baseado em comando.
- Interface do usuário (UI). Alguns aplicativos têm interfaces gráficas do usuário (GUIs) onde você clica em botões, insere texto, seleciona opções e muito mais.

### Console e Aplições de UI são limitadas

Compare com um aplicativo baseado em comandos onde você digita um comando:

- **É limitado**: Você não pode simplesmente digitar qualquer comando, apenas aqueles que o aplicativo suporta.
- **Específico de idioma**: Alguns aplicativos suportam vários idiomas, mas por padrão, o aplicativo é construído para um idioma específico, mesmo que você possa adicionar mais suporte a idiomas.

### Benefícios de aplicativos de geração de texto

Então, como uma aplicativo de geração de texto é diferente?

Em um aplicativo de geração de texto, você tem mais flexibilidade, não está limitado a um conjunto de comandos ou a um idioma específico de entrada. Em vez disso, você pode usar linguagem natural para interagir com o aplicativo. Outro benefício é que, como você já está interagindo com uma fonte de dados que foi treinada em um vasto corpus de informações, ao contrário de um aplicativo tradicional que pode ser limitado ao que está em um banco de dados.

### O que posso criar com um aplicativo de geração de texto?

Existem muitas coisas que você pode construir. Por exemplo:

- **Um chatbot**: Um chatbot que responde a perguntas sobre tópicos, como sua empresa e seus produtos, pode ser uma boa opção.
- **Assistente**: Modelos de linguagem são ótimos para coisas como resumir texto, obter insights a partir de texto, produzir texto como currículos e mais.
- **Assistente de código**: Dependendo do modelo de linguagem que você usa, é possível construir um assistente de código que o ajuda a escrever código. Por exemplo, você pode usar um produto como o GitHub Copilot, bem como o ChatGPT, para ajudá-lo a escrever código.

## Como posso começar?

Bem, você precisa encontrar uma maneira de integrar um modelo de linguagem grande (LLM), o que geralmente envolve as seguintes duas abordagens:

- **Usar uma API**: Aqui, você está construindo solicitações web com seu prompt e obtendo texto gerado de volta.
- **Usar uma biblioteca**: As bibliotecas ajudam a encapsular as chamadas de API e facilitam o uso delas.

## Bibliotecas/SDKs

Existem algumas bibliotecas bem conhecidas para trabalhar com Grandes Modelos de Linguagem (LLMs), como:

- **openai**: Esta biblioteca facilita a conexão com seu modelo e o envio de prompts.

Em seguida, existem bibliotecas que operam em um nível mais alto, como:

- **Langchain**: Langchain é bem conhecida e oferece suporte ao Python.
- **Semantic Kernel**: Semantic Kernel é uma biblioteca da Microsoft que oferece suporte às linguagens C#, Python e Java.

## Primeiro aplicativo usando openai

Vamos ver como podemos criar nosso primeiro aplicativo, quais bibliotecas precisamos, quanto é necessário e etc.

### Instalando o openai

Existem muitas bibliotecas por aí para interagir com o OpenAI ou o Azure OpenAI. É possível usar várias linguagens de programação, como C#, Python, JavaScript, Java e outras. Optamos por usar a biblioteca `openai` em Python, então vamos usar o `pip` para instalá-la.

```bash
pip install openai
```

### Criando o Recurso

Você precisa realizar as seguintes etapas:

- Criar uma conta no Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obter acesso ao Azure Open AI. Vá para [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e solicite acesso.

  > [!OBSERVAÇÃO]
  > Até o presente momento, você precisa solicitar acesso ao Azure Open AI.

- Instale Python <https://www.python.org/>
- Ter criado um recurso de serviço Azure OpenAI. Consulte este guia para saber como [criar um recurso](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localize a chave da API e o endpoint

Neste ponto, você precisa informar à biblioteca `openai` qual chave de API usar. Para encontrar sua chave de API, vá para a seção "Chaves e Endpoint" de seu recurso Azure Open AI e copie o valor de "Chave 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Agora que você tem essas informações copiadas, vamos instruir as bibliotecas a usá-las.

> [!OBSERVAÇÃO]
> Vale a pena separar sua chave API do seu código. Você pode fazer isso usando variáveis de ambiente.
>
> - Defina a variável de ambiente em: `OPENAI_API_TYPE` para a chave da sua API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurando o recurso do Azure no código

If you're using Azure Open AI, here's how you setup configuration:

Se você estiver usando o Azure Open AI, veja como configurar:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Aqui estamos definindo o seguinte:

- `api_type` para `azure`. Isso diz à biblioteca para usar o Azure Open AI e não o OpenAI.
- `api_key`, esta é a sua chave API encontrada no Portal do Azure.
- `api_version`, esta é a versão da API que você deseja usar. No momento da escrita, a versão mais recente é `2023-05-15`.
- `api_base`, este é o endpoint da API. Você pode encontrá-lo no Portal do Azure ao lado de sua chave API.

> [!OBSERVAÇÃO] > `os.getenv` é uma função que lê variáveis de ambiente. Você pode usá-lo para ler variáveis de ambiente como `OPENAI_API_KEY` e `API_BASE`. Defina essas variáveis de ambiente em seu terminal ou usando uma biblioteca como `dotenv`.

## Gerando texto

Uma maneira de gerar texto é usar a classe `Completion`. Aqui está um exemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

No código acima, criamos um `completion object` e passamos o modelo que queremos usar e o prompt. Em seguida, imprimimos o texto gerado.

### Chat completions

Até agora, você viu como usamos `Completion` para gerar texto. Mas há outra classe chamada `ChatCompletion` que é mais adequada para chatbots. Aqui está um exemplo de uso:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Aprenderemos mais sobre essa funcionalidade em um capítulo futuro.

## Exercício - seu primeiro aplicativo de geração de texto

Agora que aprendemos a configurar o openai, é hora de criar o seu primeiro aplicativo de geração de texto. Para criar seu aplicativo, siga estas etapas:

1. Crie um ambiente virtual e instale o openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!OBSERVAÇÃO]
   > Se você estiver usando o Windows, digite `venv\Scripts\activate` em vez de `source venv/bin/activate`.

   > [!OBSERVAÇÃO]
   > Localize sua chave Azure Open AI acessando [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) e pesquise por `Open AI` e selecione o `recurso Open AI` e depois selecione `Chaves e Endpoint` e copie o valor `Chave 1`.

1. Crie um arquivo _app.py_ e dê a ele o seguinte código:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure Open AI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make completion
   completion = openai.Completion.create(engine= deployment_name, model="davinci-002", prompt=prompt)

   # print response
   print(completion.choices[0].text)
   ```

   > [!OBSERVAÇÃO]
   > Se você estiver usando o Azure Open AI, precisará definir o `api_type` como `azure` e definir o `api_key` como sua chave Azure Open AI.

   Você deve ver uma saída como a seguinte:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para diferentes coisas

Agora que você viu como gerar texto usando um prompt, você até tem um programa em execução que pode modificar e alterar para gerar diferentes tipos de texto.

Prompts podem ser usados para todas as formas de tarefas. Por exemplo:

- **Gerar um tipo de texto**: Por exemplo, você pode gerar um poema, perguntas para um quiz, etc.
- **Procurar informações**: Você pode usar prompts para procurar informações, como no exemplo a seguir: 'O que significa CORS no desenvolvimento web?'.
- **Gerar código**: Você pode usar prompts para gerar código, por exemplo, desenvolvendo uma expressão regular usada para validar e-mails ou até mesmo gerar um programa inteiro, como um aplicativo web?

## Um caso de uso mais prático: um gerador de receitas

Imagine que você tenha ingredientes em casa e quer cozinhar algo. Para isso, você precisa de uma receita. Uma maneira de encontrar receitas é usar um mecanismo de busca ou você poderia usar um LLM para fazer isso.

Você poderia escrever um prompt assim:

> "Me forneça 5 receitas para um prato com os seguintes ingredientes: frango, batatas e cenouras. Por receita, liste todos os ingredientes utilizados"

Dado o prompt acima, você pode obter uma resposta semelhante a:

```output
1. Frango Assado com Vegetais:
   - Ingredientes:
     - 4 coxas de frango
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 2 colheres de sopa de azeite de oliva
     - 2 dentes de alho, picados
     - 1 colher de chá de tomilho seco
     - 1 colher de chá de orégano seco
     - Sal e pimenta a gosto

2. Ensopado de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 1 cebola, picada
     - 2 dentes de alho, picados
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 1 xícara de caldo de galinha
     - Sal e pimenta a gosto

3. Assado de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 cebola, picada
     - 2 dentes de alho, picados
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 1 xícara de caldo de galinha
     - Sal e pimenta a gosto

4. Sopa de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 1 cebola, picada
     - 2 dentes de alho, picados
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 4 xícaras de caldo de galinha
     - Sal e pimenta a gosto

5. Hash de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 cebola, picada
     - 2 dentes de alho, picados
     - 1 colher de chá de orégano

```

Essa saída é ótima, eu sei o quê cozinhar. Neste ponto, o que poderia ser útil são melhorias:

- Filtre os ingredientes que não gosto ou sou alérgico.
- Me forneça uma lista de compras, caso eu não tenha todos os ingredientes em casa.

Para os casos acima, vamos adicionar um prompt adicional:

> "Por favor, remova receitas com alho, pois sou alérgico e substitua por outra coisa. Além disso, por favor, me forneça uma lista de compras para as receitas, considerando que já tenho frango, batatas e cenouras em casa."

Agora você tem um novo resultado, a saber:

```output
1. Frango Assado com Vegetais:
   - Ingredientes:
     - 4 coxas de frango
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 2 colheres de sopa de azeite de oliva
     - 1 colher de chá de tomilho seco
     - 1 colher de chá de orégano seco
     - Sal e pimenta a gosto

2. Ensopado de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 1 cebola, picada
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 1 xícara de caldo de galinha
     - Sal e pimenta a gosto

3. Frango e Batata Assados:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 cebola, picada
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 1 xícara de caldo de galinha
     - Sal e pimenta a gosto

4. Sopa de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 1 cebola, picada
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 colher de chá de orégano seco
     - 1 colher de chá de tomilho seco
     - 4 xícaras de caldo de galinha
     - Sal e pimenta a gosto

5. Hash de Frango e Batata:
   - Ingredientes:
     - 2 colheres de sopa de azeite de oliva
     - 2 peitos de frango, cortados em cubos
     - 2 batatas, cortadas em cubos
     - 2 cenouras, cortadas em cubos
     - 1 cebola, picada
     - 1 colher de chá de orégano

Lista de Compras:
- Azeite de oliva
- Cebola
- Tomilho
- Orégano
- Sal
- Pimenta
```

Aqui estão as cinco receitas, sem mencionar alho, e também uma lista de compras considerando o que você já tem em casa.

## Execírcio - crie um gerador de receitas

Agora que temos um cenário, vamos escrever o código para corresponder ao cenário demonstrado. Para fazer isso, siga estas etapas:

1. Use o arquivo _app.py_ existente como ponto de partida
1. Localize a variável `prompt` e altere seu código para o seguinte:

   ```python
   prompt = "Me forneça 5 receitas de um prato com os seguintes ingredientes: frango, batata e cenoura. Por receita, liste todos os ingredientes usados"
   ```

   Se você executar o código agora, deverá ver uma saída semelhante a:

   ```output
   - Ensopado de Frango com Batata e Cenoura: 3 colheres de sopa de azeite, 1 cebola picada, 2 dentes de alho picados, 1 cenoura descascada e picada, 1 batata descascada e picada, 1 folha de louro, 1 raminho de tomilho, 1/2 colher de chá de sal , 1/4 colher de chá de pimenta preta, 1 1/2 xícara de caldo de galinha, 1/2 xícara de vinho branco seco, 2 colheres de sopa de salsa fresca picada, 2 colheres de sopa de manteiga sem sal, 1 1/2 libra de coxas de frango desossadas e sem pele, cortadas em 1- pedaços de polegada

   - Frango Assado no Forno com Batata e Cenoura: 3 colheres de sopa de azeite extra-virgem, 1 colher de sopa de mostarda Dijon, 1 colher de sopa de alecrim fresco picado, 1 colher de sopa de tomilho fresco picado, 4 dentes de alho picados, 1 1/2 libra de batatas vermelhas pequenas, esquartejado, 1 1/2 libra de cenoura, cortada em quartos longitudinalmente, 1/2 colher de chá de sal, 1/4 colher de chá de pimenta preta, 1 (4 libras) de frango inteiro

   - Caçarola de frango, batata e cenoura: spray de cozinha, 1 cebola grande picada, 2 dentes de alho picados, 1 cenoura descascada e ralada, 1 batata descascada e ralada, 1/2 colher de chá de folhas secas de tomilho, 1/4 colher de chá sal, 1/4 colher de chá de pimenta preta, 2 xícaras de caldo de galinha desnatado e com baixo teor de sódio, 1 xícara de ervilhas congeladas, 1/4 xícara de farinha de trigo, 1 xícara de leite com baixo teor de gordura a 2%, 1/4 xícara de parmesão ralado queijo

   - Jantar de frango e batata em uma panela: 2 colheres de sopa de azeite, 1 quilo de coxas de frango desossadas e sem pele, cortadas em pedaços de 2,5 cm, 1 cebola grande picada, 3 dentes de alho picados, 1 cenoura descascada e picada, 1 batata, descascado e picado, 1 folha de louro, 1 raminho de tomilho, 1/2 colher de chá de sal, 1/4 colher de chá de pimenta preta, 2 xícaras de caldo de galinha, 1/2 xícara de vinho branco seco

   - Caril de Frango, Batata e Cenoura: 1 colher de sopa de óleo vegetal, 1 cebola grande picada, 2 dentes de alho picados, 1 cenoura descascada e picada, 1 batata descascada e picada, 1 colher de chá de coentro moído, 1 colher de chá de cominho moído, 1/2 colher de chá de açafrão em pó, 1/2 colher de chá de gengibre em pó, 1/4 colher de chá de pimenta caiena, 2 xícaras de caldo de galinha, 1/2 xícara de vinho branco seco, 1 lata (15 onças) de grão de bico, escorrido e enxaguado, 1/2 xícara de passas, 1/2 xícara de coentro fresco picado
   ```

   > [!OBSERVAÇÃO]
   > seu LLM é não determinístico, então você pode obter resultados diferentes sempre que executar o programa.

   Ótimo! Vamos ver como podemos melhorar as coisas. Para melhorar as coisas, queremos ter certeza de que o código é flexível, para que os ingredientes e o número de receitas possam ser melhorados e alterados.

1. Vamos alterar o código da seguinte maneira:

   ```python
   no_recipes = input("No of recipes (for example, 5: ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Execute o código e teste, e vejamos o resultado:

   ```output
   No of recipes (for example, 5: 3
   List of ingredients (for example, chicken, potatoes, and carrots: milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Melhore adicionando filtro e lista de compras

Agora nós temos um aplicativo funcionando capaz de produzir receitas e é flexível, pois depende de entradas do usuário, tanto no número de receitas quanto nos ingredientes usados.

Para melhorar ainda mais, queremos adicionar o seguinte:

- **Filtrar ingredientes**: Queremos ser capazes de filtrar ingredientes que não gostamos ou somos alérgicos. Para realizar essa alteração, podemos editar nosso prompt existente e adicionar uma condição de filtro ao final, assim:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Acima adicionamos `{filter}` ao final do prompt e também capturamos o valor do filtro do usuário.

  Um exemplo de entrada da execução do programa pode ser assim:

  ```output
  No of recipes (for example, 5: 3
  List of ingredients (for example, chicken, potatoes, and carrots: onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free: no milk

  1. French Onion Soup

  Ingredients:

  -1 large onion, sliced
  -3 cups beef broth
  -1 cup milk
  -6 slices french bread
  -1/4 cup shredded Parmesan cheese
  -1 tablespoon butter
  -1 teaspoon dried thyme
  -1/4 teaspoon salt
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Place french bread slices on soup bowls.
  5. Ladle soup over bread.
  6. Sprinkle with Parmesan cheese.

  2. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. Serve hot.

  3. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  1. In a large pot, sauté onions in butter until golden brown.
  2. Add vegetable broth, milk, and pepper. Bring to a boil.
  3. Reduce heat and simmer for 10 minutes.
  4. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  5. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  Como você pode ver, todas as receitas com leite foram filtradas. Mas, se você for intolerante à lactose, talvez queira filtrar também as receitas com queijo, então é preciso ser claro.

- **Produze uma lista de compras**. Queremos produzir uma lista de compras, considerando o que já temos em casa.

  Para esta funcionalidade, poderíamos tentar resolver tudo em um prompt ou poderíamos dividi-lo em dois prompts. Vamos tentar a última abordagem. Aqui estamos sugerindo adicionar um prompt adicional, mas para que isso funcione, precisamos adicionar o resultado do prompt anterior como contexto para o prompt posterior.

  ```python
  old_prompt_result = completion.choices[0].text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].text)
  ```

  Observe o seguinte:

  1. Nós estamos criando um novo prompt adicionando o resultado do primeiro prompt ao novo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Nós fizemos uma nova requisição, mas também considerando o número de tokens que solicitamos no primeiro prompt, então desta vez dizemos que `max_tokens` é 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Dando uma olhada neste código, chegamos agora à seguinte saída:

     ```output
     No of recipes (for example, 5: 2
     List of ingredients (for example, chicken, potatoes, and carrots: apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free: sugar


     - Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated

     - Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples

     Shopping list:
     - Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Melhorando a nossa configuração

O que temos até agora é um código que funciona, mas há algumas alterações que devemos fazer para melhorar ainda mais as coisas. Algumas coisas que devemos fazer são:

- **Separar `secrets` do código**, como a chave da API. Segredos não pertencem ao código e devem ser armazenados em um local seguro. Para separar segredos do código, podemos usar variáveis de ambiente e bibliotecas como `python-dotenv` para carregá-los de um arquivo. Veja como isso ficaria no código:

  1. Crie um arquivo `.env` com o seguinte conteúdo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Observação: para o Azure, você precisa definir as seguintes variáveis de ambiente:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     No código, você carregaria as variáveis de ambiente assim:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Uma palavra sobre o comprimento do token**. Devemos considerar quantos tokens precisamos para gerar o texto que queremos. Tokens custam dinheiro, então, sempre que possível, devemos tentar ser econômicos com o número de tokens que usamos. Por exemplo, podemos formular o prompt para que possamos usar menos tokens?

  Para alterar os tokens usados, você pode usar o parâmetro `max_tokens`. Por exemplo, se você quiser usar 100 tokens, você faria:

  ```python
  completion = openai.Completion.create(model="davinci-002", prompt=prompt, max_tokens=100)
  ```

- **Experimentando com a temperatura**. A temperatura é algo que não mencionamos até agora. Porém, é um contexto importante para o desempenho de nosso programa. Quanto maior o valor da temperatura, mais aleatório será o resultado. Por outro lado, quanto menor o valor da temperatura, mais previsível será o resultado. Considere se você deseja ou não variação na saída.

  Para alterar a temperatura, você pode usar o parâmetro `temperature`. Por exemplo, se você quiser usar uma temperatura de 0.5, você faria:

  ```python
  completion = openai.Completion.create(model="davinci-002", prompt=prompt, temperature=0.5)
  ```

  > Observação: quanto mais próximo de 1.0, mais variada será a saída.

## Tarefa

Para esta tarefa, você pode escolher o que criar para um aplicativo.

Aqui estão algumas sugestões:

- Ajuste o aplicativo gerador de receitas para melhorá-lo ainda mais. Brinque com os valores de temperatura e os prompts para ver o que você pode criar.
- Crie um "companheiro de estudos". Este aplicativo deve ser capaz de responder a perguntas sobre um tópico. Por exemplo: Python. Você poderia ter prompts como: "O que é um certo tópico em Python?" ou poderia ter um prompt que diz: "Me mostre o código para um certo tópico", etc.

- Bot de história, faça a história ganhar vida, instrua o bot a interpretar um certo personagem histórico e faça perguntas sobre sua vida e época.

## Solução

### Amigo de Estudo

Abaixo está um prompt inicial, veja como você pode usá-lo e ajustá-lo ao seu gosto.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de História

Aqui estão alguns prompts que você pode usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificação de Conhecimento

What does the concept temperature do?

O que o conceito de temperatura faz?

1. Ele controla o quão aleatória é a saída.
2. Ele controla o quão grande é a resposta.
3. Ele controla quantos tokens são usados.

Resposta: 1. Ele controla o quão aleatória é a saída.

## 🚀 Desafio

When working on the assignment, try to vary the temperature, try set it to 0, 0.5, and 1. Remember that 0 is the least varied and 1 is the most, what value works best for your app?

Quando estiver trabalhando na tarefa, tente variar a temperatura, tente definir para 0, 0.5 e 1. Lembre-se de que 0 é o menos variado e 1 é o mais, qual valor funciona melhor para o seu aplicativo?

## Excelente trabalho! Continue seu aprendizado

Após concluir esta lição, confira nossa [coleção de aprendizado de IA generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar seus conhecimentos sobre IA generativa!

Vamos prosseguir para a Lição 7, onde veremos como [criar aplicativos de chat](../../../07-building-chat-applications/translations/pt-br/README.md?WT.mc_id=academic-105485-koreyst)!
