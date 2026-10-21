# Construir Aplicações de Geração de Texto

[![Construir Aplicações de Geração de Texto](../../../translated_images/pt-PT/06-lesson-banner.a5c629f990a636c8.webp?WT.mc_id=academic-105485-koreyst)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Clique na imagem acima para ver o vídeo desta lição)_

Até agora, viu através deste currículo que existem conceitos fundamentais como prompts e até uma disciplina inteira chamada "engenharia de prompts". Muitas ferramentas com que pode interagir, como ChatGPT, Office 365, Microsoft Power Platform e mais, suportam o uso de prompts para realizar algo.

Para adicionar essa experiência a uma aplicação, precisa de compreender conceitos como prompts, compleções e escolher uma biblioteca para trabalhar. É exatamente isso que vai aprender neste capítulo.

## Introdução

Neste capítulo, irá:

- Aprender sobre a biblioteca openai e os seus conceitos principais.
- Construir uma aplicação de geração de texto usando openai.
- Compreender como utilizar conceitos como prompt, temperatura e tokens para construir uma aplicação de geração de texto.

## Objetivos de aprendizagem

No final desta lição, será capaz de:

- Explicar o que é uma aplicação de geração de texto.
- Construir uma aplicação de geração de texto usando openai.
- Configurar a sua aplicação para usar mais ou menos tokens e também alterar a temperatura, para uma saída variada.

## O que é uma aplicação de geração de texto?

Normalmente, quando constrói uma aplicação, esta tem algum tipo de interface como a seguinte:

- Baseada em comandos. Aplicações de consola são aplicações típicas onde digita um comando e ele executa uma tarefa. Por exemplo, `git` é uma aplicação baseada em comandos.
- Interface do utilizador (UI). Algumas aplicações têm interfaces gráficas do utilizador (GUIs) onde clica em botões, insere texto, seleciona opções e mais.

### Aplicações de consola e UI são limitadas

Compare com uma aplicação baseada em comandos onde digita um comando:

- **É limitado**. Não pode simplesmente digitar qualquer comando, apenas aqueles que a aplicação suporta.
- **Específico da língua**. Algumas aplicações suportam muitas línguas, mas por padrão a aplicação é construída para uma língua específica, mesmo que possa adicionar mais suporte linguístico.

### Benefícios das aplicações de geração de texto

Então, como é que uma aplicação de geração de texto é diferente?

Numa aplicação de geração de texto, tem mais flexibilidade, não está limitado a um conjunto de comandos ou a uma língua de entrada específica. Em vez disso, pode usar a linguagem natural para interagir com a aplicação. Outro benefício é que já está a interagir com uma fonte de dados que foi treinada num vasto corpus de informação, enquanto que uma aplicação tradicional pode estar limitada ao que está numa base de dados.

### O que posso construir com uma aplicação de geração de texto?

Existem muitas coisas que pode construir. Por exemplo:

- **Um chatbot**. Um chatbot a responder a perguntas sobre tópicos, como a sua empresa e os seus produtos, poderia ser uma boa opção.
- **Assistente**. LLMs são ótimos em tarefas como resumir texto, obter insights de texto, produzir texto como currículos e mais.
- **Assistente de código**. Dependendo do modelo de linguagem que usa, pode construir um assistente de código que ajuda a escrever código. Por exemplo, pode usar produtos como GitHub Copilot assim como o ChatGPT para ajudar a escrever código.

## Como posso começar?

Bem, precisa de encontrar uma forma de integrar com um LLM, o que geralmente implica as seguintes duas abordagens:

- Usar uma API. Aqui está a construir pedidos web com o seu prompt e obter texto gerado de volta.
- Usar uma biblioteca. As bibliotecas ajudam a encapsular as chamadas à API e a torná-las mais fáceis de usar.

## Bibliotecas/SDKs

Existem algumas bibliotecas bem conhecidas para trabalhar com LLMs, como:

- **openai**, esta biblioteca facilita a ligação ao seu modelo e o envio de prompts.

Depois, existem bibliotecas que operam a um nível mais elevado como:

- **Langchain**. Langchain é bem conhecido e suporta Python.
- **Semantic Kernel**. Semantic Kernel é uma biblioteca da Microsoft que suporta as linguagens C#, Python e Java.

## Primeira aplicação usando openai

Vamos ver como podemos construir a nossa primeira aplicação, que bibliotecas precisamos, o quanto é necessário e assim por diante.

### Instalar openai

Existem muitas bibliotecas para interagir com OpenAI ou Azure OpenAI. É possível usar várias linguagens de programação também como C#, Python, JavaScript, Java e mais. Escolhemos usar a biblioteca `openai` para Python, por isso vamos usar `pip` para a instalar.

```bash
pip install openai
```

### Criar um recurso

Precisa de realizar os seguintes passos:

- Criar uma conta no Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obter acesso ao Azure OpenAI. Vá a [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e solicite acesso.

  > [!NOTE]
  > No momento da escrita, precisa de solicitar acesso ao Azure OpenAI.

- Instalar Python <https://www.python.org/>
- Ter criado um recurso do Serviço Azure OpenAI. Veja este guia para como [criar um recurso](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizar a chave API e endpoint

Neste ponto, precisa de dizer à sua biblioteca `openai` qual chave API usar. Para encontrar a sua chave API, vá à secção "Chaves e Endpoint" do seu recurso Azure OpenAI e copie o valor "Chave 1".

![Lâmina de recurso Chaves e Endpoint no Portal Azure](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Agora que tem esta informação copiada, vamos indicar às bibliotecas para a usar.

> [!NOTE]
> Vale a pena separar a sua chave API do seu código. Pode fazê-lo usando variáveis de ambiente.
>
> - Defina a variável de ambiente `OPENAI_API_KEY` para a sua chave API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurar configuração Azure

Se estiver a usar Azure OpenAI (agora parte da Microsoft Foundry), aqui está como configurar. Usamos o cliente padrão `OpenAI` apontado ao endpoint `/openai/v1/` do Azure OpenAI, que funciona com a API Responses e não necessita de `api_version`:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

Acima estamos a definir o seguinte:

- `api_key`, esta é a sua chave API encontrada no Portal Azure ou no portal Microsoft Foundry.
- `base_url`, este é o endpoint do seu recurso Foundry com `/openai/v1/` anexado. O endpoint estável v1 funciona tanto para OpenAI como para Azure OpenAI sem gestão `api_version`.

> [!NOTE] > `os.environ` lê variáveis de ambiente. Pode usá-lo para ler variáveis de ambiente como `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`. Defina estas variáveis de ambiente no seu terminal ou usando uma biblioteca como `dotenv`.

## Gerar texto

A forma de gerar texto é usar a API Responses via o método `responses.create`. Aqui está um exemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # this is your model deployment name
    input=prompt,
    store=False,
)
print(response.output_text)
```

No código acima, criamos uma resposta e passamos o modelo que queremos usar e o prompt. Depois imprimimos o texto gerado via `response.output_text`.

### Conversas multi-turno

A API Responses é bem adequada tanto para geração de texto de turno único como para chatbots multi-turno - fornece uma lista de mensagens em `input` para construir uma conversa:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mais sobre esta funcionalidade num capítulo futuro.

## Exercício - a sua primeira aplicação de geração de texto

Agora que aprendemos como configurar e configurar openai, é tempo de construir a sua primeira aplicação de geração de texto. Para construir a sua aplicação, siga estes passos:

1. Crie um ambiente virtual e instale openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Se está a usar Windows, digite `venv\Scripts\activate` em vez de `source venv/bin/activate`.

   > [!NOTE]
   > Localize a sua chave Azure OpenAI indo a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), procure por `Open AI`, selecione `Open AI resource` e depois selecione `Keys and Endpoint` e copie o valor `Key 1`.

1. Crie um ficheiro _app.py_ e coloque o seguinte código:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make a request using the Responses API
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # print response
   print(response.output_text)
   ```

   > [!NOTE]
   > Se estiver a usar OpenAI simples (não Azure), use `client = OpenAI(api_key="<replace this value with your OpenAI key>")` (sem `base_url`) e passe um nome de modelo como `gpt-5-mini` em vez de um nome de deployment.

   Deve ver uma saída semelhante à seguinte:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para coisas diferentes

Agora já viu como gerar texto usando um prompt. Tem até um programa a funcionar que pode modificar e alterar para gerar diferentes tipos de texto.

Os prompts podem ser usados para todo o tipo de tarefas. Por exemplo:

- **Gerar um tipo de texto**. Por exemplo, pode gerar um poema, perguntas para um quiz, etc.
- **Procurar informação**. Pode usar prompts para procurar informação como no exemplo seguinte 'O que significa CORS no desenvolvimento web?'.
- **Gerar código**. Pode usar prompts para gerar código, por exemplo desenvolvendo uma expressão regular usada para validar emails ou até gerar um programa inteiro, como uma aplicação web?

## Um caso de uso mais prático: um gerador de receitas

Imagine que tem ingredientes em casa e quer cozinhar algo. Para isso, precisa de uma receita. Uma forma de encontrar receitas é usar um motor de busca ou pode usar um LLM para isso.

Pode escrever um prompt assim:

> "Mostra-me 5 receitas para um prato com os seguintes ingredientes: frango, batatas e cenouras. Por receita, liste todos os ingredientes usados"

Dado o prompt acima, pode receber uma resposta semelhante a:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 2 cloves garlic, minced
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 cloves garlic, minced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

Este resultado é ótimo, sei o que cozinhar. A partir daqui, o que poderia ser melhorias úteis são:

- Filtrar ingredientes que não gosto ou aos quais sou alérgico.
- Produzir uma lista de compras, caso não tenha todos os ingredientes em casa.

Para os casos acima, vamos adicionar um prompt adicional:

> "Por favor, remova receitas com alho pois sou alérgico e substitua por algo diferente. Também, por favor produza uma lista de compras para as receitas, considerando que já tenho frango, batatas e cenouras em casa."

Agora tem um novo resultado, concretamente:

```output
1. Roasted Chicken and Vegetables:
Ingredients:
- 4 chicken thighs
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 2 tablespoons olive oil
- 1 teaspoon dried thyme
- 1 teaspoon dried oregano
- Salt and pepper, to taste

2. Chicken and Potato Stew:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

3. Chicken and Potato Bake:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 1 cup chicken broth
- Salt and pepper, to taste

4. Chicken and Potato Soup:
Ingredients:
- 2 tablespoons olive oil
- 1 onion, diced
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 teaspoon dried oregano
- 1 teaspoon dried thyme
- 4 cups chicken broth
- Salt and pepper, to taste

5. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 1 teaspoon dried oregano

Shopping List:
- Olive oil
- Onion
- Thyme
- Oregano
- Salt
- Pepper
```

Essas são as suas cinco receitas, sem alho mencionado e também tem uma lista de compras considerando o que já tem em casa.

## Exercício - construir um gerador de receitas

Agora que encenámos um cenário, vamos escrever código para corresponder ao cenário demonstrado. Para isso, siga estes passos:

1. Use o ficheiro _app.py_ existente como ponto de partida
1. Localize a variável `prompt` e altere o seu código para o seguinte:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Se agora executar o código, deve ver uma saída semelhante a:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTA, o seu LLM é não determinístico, por isso pode obter resultados diferentes todas as vezes que executar o programa.

   Ótimo, vamos ver como podemos melhorar as coisas. Para melhorar as coisas, queremos garantir que o código é flexível, para que os ingredientes e o número de receitas possam ser aprimorados e alterados.

1. Vamos alterar o código da seguinte forma:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Testar o código pode parecer assim:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Melhorar adicionando filtro e lista de compras

Agora temos uma aplicação funcional capaz de produzir receitas e é flexível pois depende das entradas do utilizador, tanto no número de receitas como também nos ingredientes usados.

Para aprimorar ainda mais, queremos adicionar o seguinte:

- **Filtrar ingredientes**. Queremos poder filtrar ingredientes que não gostamos ou aos quais somos alérgicos. Para realizar esta alteração, podemos editar o nosso prompt existente e adicionar uma condição de filtro no final do mesmo assim:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Acima, adicionamos `{filter}` ao final do prompt e também capturamos o valor do filtro do utilizador.

  Um exemplo de entrada a executar o programa pode agora ser assim:

  ```output
  No of recipes (for example, 5): 3
  List of ingredients (for example, chicken, potatoes, and carrots): onion,milk
  Filter (for example, vegetarian, vegan, or gluten-free): no milk

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

  Como pode ver, quaisquer receitas com leite foram filtradas. Mas, se for intolerante à lactose, pode querer filtrar também receitas com queijo, por isso é necessário ser claro.

- **Produzir uma lista de compras**. Queremos produzir uma lista de compras, considerando o que já temos em casa.

  Para esta funcionalidade, poderíamos tentar resolver tudo num prompt ou poderíamos dividi-lo em dois prompts. Vamos tentar a última abordagem. Aqui estamos a sugerir adicionar um prompt adicional, mas para isso funcionar, precisamos de adicionar o resultado do primeiro prompt como contexto para o segundo prompt.

  Localize a parte do código que imprime o resultado do primeiro prompt e adicione o seguinte código abaixo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # print response
  print("Shopping list:")
  print(response.output_text)
  ```

  Note o seguinte:

  1. Estamos a construir um novo prompt adicionando o resultado do primeiro prompt ao novo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Fazemos um novo pedido, mas também considerando o número de tokens que pedimos no primeiro prompt, por isso desta vez dizemos que `max_output_tokens` é 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Testando este código, agora chegamos à seguinte saída:

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Melhore a sua configuração

O que temos até agora é um código que funciona, mas há alguns ajustes que devemos fazer para melhorar ainda mais as coisas. Algumas coisas que devemos fazer são:

- **Separar segredos do código**, como a chave da API. Segredos não pertencem ao código e devem ser armazenados num local seguro. Para separar segredos do código, podemos usar variáveis de ambiente e bibliotecas como `python-dotenv` para as carregar a partir de um ficheiro. É assim que isso ficaria no código:

  1. Crie um ficheiro `.env` com o seguinte conteúdo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, para Azure OpenAI na Microsoft Foundry, precisa de definir as seguintes variáveis de ambiente em vez disso:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     No código, carregaria as variáveis de ambiente assim:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Uma palavra sobre o comprimento dos tokens**. Devemos considerar quantos tokens precisamos para gerar o texto que queremos. Os tokens custam dinheiro, por isso, sempre que possível, devemos tentar ser económicos com o número de tokens que usamos. Por exemplo, podemos formular o prompt de forma a usar menos tokens?

  Para alterar os tokens usados, pode usar o parâmetro `max_output_tokens`. Por exemplo, se quiser usar 100 tokens, faria:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentar com a temperatura**. A temperatura é algo que ainda não mencionámos mas é um contexto importante para o desempenho do nosso programa. Quanto maior o valor da temperatura, mais aleatória será a saída. Por outro lado, quanto menor o valor da temperatura, mais previsível será a saída. Considere se quer variação na sua saída ou não.

  Para alterar a temperatura, pode usar o parâmetro `temperature`. Por exemplo, se quiser usar uma temperatura de 0,5, faria:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, quanto mais próximo de 1,0, mais variada é a saída.

- **Modelos de raciocínio não usam `temperature`**. Esta é uma mudança importante em 2026. Os modelos atuais, não obsoletos, na Microsoft Foundry são **modelos de raciocínio** (a família GPT-5, série o) - e eles **não suportam `temperature` ou `top_p`** (nem `max_tokens`; use `max_output_tokens`). Se enviar `temperature` para `gpt-5-mini` obterá um erro de "parâmetro não suportado". Para experimentar o exemplo da temperatura acima, aponte para um modelo que ainda suporte controlos de amostragem - por exemplo, um modelo aberto **Llama** como `Llama-3.3-70B-Instruct` do [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), chamado via o endpoint Foundry Models / Azure AI Inference (da mesma forma que as amostras `githubmodels-*`). Para modelos de raciocínio como o GPT-5, guia a saída de forma diferente:
  - **Engenharia de prompt** - instruções claras, exemplos e saída estruturada (veja a lição [04 - Engenharia de Prompt](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) fazem o trabalho que os controlos de amostragem costumavam fazer.
  - **Controlos de raciocínio** - parâmetros como esforço/verbosidade do raciocínio equilibram a profundidade do raciocínio com a latência e custo.

  Em resumo: `temperature`/`top_p` ainda são válidos em muitos modelos (Llama, Mistral, Phi e a família GPT-4.x - embora GPT-4.x esteja a ser descontinuado), mas a direção é engenharia de prompt + controlos de raciocínio em modelos de raciocínio como GPT-5.

## Tarefa

Para esta tarefa, pode escolher o que criar.

Aqui estão algumas sugestões:

- Ajuste a app geradora de receitas para a melhorar ainda mais. Experimente valores de temperatura e os prompts para ver o que consegue criar.
- Construa um "companheiro de estudo". Esta app deve ser capaz de responder a perguntas sobre um tema, por exemplo Python, pode ter prompts como "O que é determinado tópico em Python?", ou pode ter um prompt que diga, mostra-me código para determinado tópico, etc.
- Bot de história, faça a história ganhar vida, instrua o bot para interpretar uma certa personagem histórica e faça-lhe perguntas sobre a sua vida e época.

## Solução

### Companheiro de estudo

Abaixo está um prompt inicial, veja como o pode usar e ajustar ao seu gosto.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de história

Aqui estão alguns prompts que pode usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Teste de conhecimento

O que faz o conceito de temperatura?

1. Controla o quão aleatória é a saída.
1. Controla o tamanho da resposta.
1. Controla quantos tokens são usados.

## 🚀 Desafio

Ao trabalhar na tarefa, tente variar a temperatura, experimente definir para 0, 0,5 e 1. Lembre-se que 0 é o menos variado e 1 o mais. Que valor funciona melhor para a sua app?

## Excelente trabalho! Continue a sua aprendizagem

Após completar esta lição, confira a nossa [coleção de aprendizagem sobre IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar o seu conhecimento em IA Generativa!

Vá para a Lição 7 onde vamos ver como [construir aplicações de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->