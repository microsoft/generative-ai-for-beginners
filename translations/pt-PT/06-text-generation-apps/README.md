# Construir aplicações de geração de texto

[![Construir aplicações de geração de texto](../../../translated_images/pt-PT/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(Clique na imagem acima para ver o vídeo desta lição)_

Até agora, neste currículo, viu-se que existem conceitos fundamentais como prompts e até uma disciplina inteira chamada "engenharia de prompts". Muitas ferramentas com as quais pode interagir, como o ChatGPT, Office 365, Microsoft Power Platform e outras, suportam a utilização de prompts para realizar algo.

Para adicionar essa experiência a uma aplicação, precisa de compreender conceitos como prompts, completions e escolher uma biblioteca para trabalhar. É exatamente isso que vai aprender neste capítulo.

## Introdução

Neste capítulo, irá:

- Aprender sobre a biblioteca openai e os seus conceitos principais.
- Construir uma aplicação de geração de texto utilizando openai.
- Compreender como usar conceitos como prompt, temperature e tokens para construir uma aplicação de geração de texto.

## Objetivos de aprendizagem

No final desta lição, será capaz de:

- Explicar o que é uma aplicação de geração de texto.
- Construir uma aplicação de geração de texto utilizando openai.
- Configurar a sua aplicação para usar mais ou menos tokens e também alterar a temperature, para uma saída variada.

## O que é uma aplicação de geração de texto?

Normalmente, quando constrói uma aplicação, ela tem algum tipo de interface como o seguinte:

- Baseada em comandos. Aplicações de consola são aplicações típicas onde escreve um comando e esta executa uma tarefa. Por exemplo, o `git` é uma aplicação baseada em comandos.
- Interface de utilizador (UI). Algumas aplicações têm interfaces gráficas de utilizador (GUIs) onde clica em botões, insere texto, seleciona opções e mais.

### Aplicações de consola e UI são limitadas

Compare com uma aplicação baseada em comandos onde escreve um comando:

- **É limitada**. Não pode simplesmente escrever qualquer comando, apenas os que a aplicação suporta.
- **Específica de linguagem**. Algumas aplicações suportam muitas linguagens, mas por padrão a aplicação é construída para uma linguagem específica, mesmo que possa adicionar suporte a mais linguagens.

### Vantagens das aplicações de geração de texto

Então, como é que uma aplicação de geração de texto é diferente?

Numa aplicação de geração de texto, tem mais flexibilidade, não está limitado a um conjunto de comandos ou a uma linguagem de entrada específica. Em vez disso, pode usar linguagem natural para interagir com a aplicação. Outra vantagem é que já está a interagir com uma fonte de dados que foi treinada num vasto corpus de informação, enquanto uma aplicação tradicional pode estar limitada ao que está numa base de dados.

### O que posso construir com uma aplicação de geração de texto?

Há muitas coisas que pode construir. Por exemplo:

- **Um chatbot**. Um chatbot a responder a perguntas sobre temas, como a sua empresa e os seus produtos, pode ser uma boa solução.
- **Assistente**. LLMs são ótimos para coisas como resumir texto, obter insights de texto, produzir texto como currículos e mais.
- **Assistente de código**. Dependendo do modelo de linguagem que usa, pode construir um assistente de código que ajuda a escrever código. Por exemplo, pode usar produtos como o GitHub Copilot bem como o ChatGPT para ajudar a escrever código.

## Como posso começar?

Bem, precisa de encontrar uma forma de integrar com um LLM que geralmente envolve as seguintes duas abordagens:

- Usar uma API. Aqui está a construir pedidos web com o seu prompt e recebe o texto gerado de volta.
- Usar uma biblioteca. Bibliotecas ajudam a encapsular as chamadas da API e torná-las mais fáceis de usar.

## Bibliotecas/SDKs

Existem algumas bibliotecas bem conhecidas para trabalhar com LLMs como:

- **openai**, esta biblioteca facilita a ligação ao seu modelo e o envio de prompts.

Depois há bibliotecas que operam num nível mais alto como:

- **Langchain**. Langchain é bastante conhecido e suporta Python.
- **Semantic Kernel**. Semantic Kernel é uma biblioteca da Microsoft que suporta as linguagens C#, Python e Java.

## Primeira aplicação usando openai

Vamos ver como podemos construir a nossa primeira aplicação, que bibliotecas precisamos, quanto é necessário e assim por diante.

### Instalar openai

Existem muitas bibliotecas para interagir com OpenAI ou Azure OpenAI. Também é possível usar várias linguagens de programação como C#, Python, JavaScript, Java e mais. Escolhemos usar a biblioteca `openai` em Python, por isso vamos usar o `pip` para instalá-la.

```bash
pip install openai
```

### Criar um recurso

Precisa de seguir os seguintes passos:

- Criar uma conta no Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obter acesso ao Azure OpenAI. Vá a [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e solicite acesso.

  > [!NOTE]
  > No momento da escrita, precisa de candidatar-se para acesso ao Azure OpenAI.

- Instalar Python <https://www.python.org/>
- Ter criado um recurso Azure OpenAI Service. Veja este guia para saber como [criar um recurso](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizar chave API e endpoint

A esta altura, precisa de informar à sua biblioteca `openai` que chave API usar. Para encontrar a sua chave API, vá à secção "Keys and Endpoint" do seu recurso Azure OpenAI e copie o valor "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Agora que tem esta informação copiada, vamos instruir as bibliotecas para a usarem.

> [!NOTE]
> Vale a pena separar a sua chave API do seu código. Pode fazer isso usando variáveis de ambiente.
>
> - Defina a variável de ambiente `OPENAI_API_KEY` para a sua chave API.
>   `export OPENAI_API_KEY='sk-...'`

### Configuração para Azure

Se está a usar Azure OpenAI (agora parte do Microsoft Foundry), veja como configurar. Usamos o cliente padrão `OpenAI` apontado para o endpoint Azure OpenAI `/openai/v1/`, que funciona com a API de Responses e não precisa de `api_version`:

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
- `base_url`, este é o endpoint do seu recurso Foundry com `/openai/v1/` adicionado. O endpoint estável v1 funciona tanto para OpenAI como para Azure OpenAI sem necessidade de gestão do `api_version`.

> [!NOTE] > `os.environ` lê variáveis de ambiente. Pode usá-lo para ler variáveis de ambiente como `AZURE_OPENAI_API_KEY` e `AZURE_OPENAI_ENDPOINT`. Defina estas variáveis no seu terminal ou usando uma biblioteca como `dotenv`.

## Gerar texto

A forma de gerar texto é usando a API Responses via o método `responses.create`. Aqui está um exemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # este é o nome da sua implementação do modelo
    input=prompt,
    store=False,
)
print(response.output_text)
```

No código acima, criamos uma resposta e passamos o modelo que queremos usar e o prompt. Depois imprimimos o texto gerado via `response.output_text`.

### Conversas múltiplas (multi-turn)

A API Responses é adequada tanto para geração de texto de turno único como para chatbots de múltiplos turnos — fornece uma lista de mensagens em `input` para construir a conversa:

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

Mais informações sobre esta funcionalidade num capítulo futuro.

## Exercício - a sua primeira aplicação de geração de texto

Agora que aprendemos a configurar e configurar openai, é hora de construir a sua primeira aplicação de geração de texto. Para construir a sua aplicação siga estes passos:

1. Crie um ambiente virtual e instale openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Se usar Windows, escreva `venv\Scripts\activate` em vez de `source venv/bin/activate`.

   > [!NOTE]
   > Localize a sua chave Azure OpenAI indo a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) e pesquise por `Open AI` e selecione o `Open AI resource` e depois `Keys and Endpoint` e copie o valor `Key 1`.

1. Crie um ficheiro _app.py_ e coloque o seguinte código:

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # adicione o seu código de conclusão
   prompt = "Complete the following: Once upon a time there was a"

   # faça um pedido usando a API de Respostas
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # imprimir resposta
   print(response.output_text)
   ```

   > [!NOTE]
   > Se estiver a usar OpenAI simples (não Azure), use `client = OpenAI(api_key="<substitua este valor pela sua chave OpenAI>")` (sem `base_url`) e passe um nome de modelo como `gpt-5-mini` em vez de um nome de implantação.

   Deve ver uma saída como a seguinte:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para coisas diferentes

Agora viu como gerar texto usando um prompt. Tem até um programa em funcionamento que pode modificar para gerar diferentes tipos de texto.

Prompts podem ser usados para todo o tipo de tarefas. Por exemplo:

- **Gerar um tipo de texto**. Por exemplo, pode gerar um poema, perguntas para um quiz, etc.
- **Pesquisar informação**. Pode usar prompts para procurar informação como no exemplo 'O que significa CORS no desenvolvimento web?'.
- **Gerar código**. Pode usar prompts para gerar código, por exemplo desenvolver uma expressão regular para validar emails ou porque não gerar um programa inteiro, como uma aplicação web?

## Um caso de uso mais prático: um gerador de receitas

Imagine que tem ingredientes em casa e quer cozinhar algo. Para isso, precisa de uma receita. Uma forma de encontrar receitas é usar um motor de busca ou poderia usar um LLM para isso.

Poderia escrever um prompt assim:

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

Este resultado é ótimo, sei o que cozinhar. Neste ponto, melhorias úteis poderiam ser:

- Filtrar ingredientes que não gosto ou aos quais sou alérgico.
- Produzir uma lista de compras, caso não tenha todos os ingredientes em casa.

Para os casos acima, vamos adicionar um prompt adicional:

> "Por favor, remova receitas com alho pois sou alérgico e substitua por outra coisa. Além disso, por favor, produza uma lista de compras para as receitas, considerando que já tenho frango, batatas e cenouras em casa."

Agora tem um novo resultado, nomeadamente:

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

   > NOTA, o seu LLM é não determinístico, por isso pode obter resultados diferentes cada vez que executar o programa.

   Ótimo, vejamos como podemos melhorar as coisas. Para melhorar, queremos garantir que o código é flexível, para que os ingredientes e o número de receitas possam ser alterados e melhorados.

1. Vamos alterar o código da seguinte forma:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolar o número de receitas no prompt e nos ingredientes
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Usar o código numa execução de teste, pode ficar assim:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Melhorar adicionando filtro e lista de compras

Agora temos uma aplicação funcional capaz de produzir receitas e é flexível pois depende das entradas do utilizador, tanto no número de receitas como nos ingredientes usados.

Para melhorar ainda mais queremos adicionar o seguinte:

- **Filtrar ingredientes**. Queremos ser capazes de filtrar ingredientes que não gostamos ou aos quais somos alérgicos. Para realizar esta alteração, podemos editar o nosso prompt existente e adicionar uma condição de filtro no final, assim:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Acima, adicionamos `{filter}` no final do prompt e também capturamos o valor do filtro do utilizador.

  Um exemplo de execução do programa pode agora ser assim:

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

  Como pode ver, qualquer receita com leite foi filtrada. Mas, se for intolerante à lactose, poderá querer filtrar receitas com queijo também, por isso há necessidade de ser claro.


- **Produzir uma lista de compras**. Queremos produzir uma lista de compras, considerando o que já temos em casa.

  Para esta funcionalidade, poderíamos tentar resolver tudo num único prompt ou poderíamos dividir em dois prompts. Vamos tentar a segunda abordagem. Aqui estamos a sugerir adicionar um prompt adicional, mas para isso funcionar, precisamos de adicionar o resultado do primeiro prompt como contexto para o segundo prompt.

  Localize a parte do código que imprime o resultado do primeiro prompt e adicione o seguinte código abaixo:

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # imprimir resposta
  print("Shopping list:")
  print(response.output_text)
  ```

  Note o seguinte:

  1. Estamos a construir um novo prompt adicionando o resultado do primeiro prompt ao novo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. Fazemos um novo pedido, mas também considerando o número de tokens que solicitámos no primeiro prompt, por isso desta vez dizemos que `max_output_tokens` é 1200.

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     Experimentando com este código, chegamos agora à seguinte saída:

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

O que temos até agora é um código que funciona, mas há algumas melhorias que deveríamos fazer para melhorar ainda mais. Algumas coisas que devemos fazer são:

- **Separar segredos do código**, como a chave da API. Segredos não pertencem ao código e devem ser armazenados num local seguro. Para separar segredos do código, podemos usar variáveis de ambiente e bibliotecas como `python-dotenv` para as carregar a partir de um ficheiro. Aqui está como isso ficaria em código:

  1. Crie um ficheiro `.env` com o seguinte conteúdo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Nota, para Azure OpenAI no Microsoft Foundry, você precisa de definir as seguintes variáveis de ambiente em vez disso:

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     Em código, carregaria as variáveis de ambiente assim:

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- **Uma palavra sobre o comprimento dos tokens**. Devemos considerar quantos tokens precisamos para gerar o texto que queremos. Os tokens custam dinheiro, por isso, sempre que possível, devemos tentar ser económicos com o número de tokens que usamos. Por exemplo, podemos formular o prompt de forma a usar menos tokens?

  Para mudar os tokens usados, pode usar o parâmetro `max_output_tokens`. Por exemplo, se quiser usar 100 tokens, faria:

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **Experimentar com a temperatura**. A temperatura é algo que ainda não mencionámos até agora, mas é um contexto importante para o desempenho do nosso programa. Quanto maior o valor da temperatura, mais aleatória será a saída. Por outro lado, quanto mais baixa for a temperatura, mais previsível será a saída. Considere se quer variação na sua saída ou não.

  Para alterar a temperatura, pode usar o parâmetro `temperature`. Por exemplo, se quiser usar uma temperatura de 0,5, faria:

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > Nota, quanto mais próximo de 1.0, mais variada será a saída.

- **Modelos de raciocínio não usam `temperature`**. Esta é uma mudança importante para 2026. Os modelos atuais, não descontinuados, no Microsoft Foundry são **modelos de raciocínio** (a família GPT-5, série o) - e eles **não suportam `temperature` ou `top_p`** (nem `max_tokens`; use `max_output_tokens`). Se enviar `temperature` para `gpt-5-mini` receberá um erro "parameter not supported". Por isso, para tentar o exemplo da temperatura acima, aponte para um modelo que ainda suporte controles de amostragem - por exemplo um modelo open **Llama** como `Llama-3.3-70B-Instruct` do [catálogo de modelos Microsoft Foundry](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst), chamado via o endpoint Foundry Models / Azure AI Inference (da mesma forma que as amostras `githubmodels-*`). Para modelos de raciocínio como o GPT-5, controla-se a saída de forma diferente:
  - **Engenharia de prompts** - instruções claras, exemplos e saída estruturada (veja a aula [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)) fazem o trabalho que os botões de amostragem costumavam fazer.
  - **Controles de raciocínio** - parâmetros como esforço/verbosity do raciocínio valorizam a profundidade do raciocínio contra a latência e o custo.

  Em resumo: `temperature`/`top_p` ainda são válidos em muitos modelos (Llama, Mistral, Phi, e a família GPT-4.x - embora GPT-4.x esteja a descontinuar), mas a direção é engenharia de prompts + controles de raciocínio em modelos de raciocínio como GPT-5.

## Tarefa

Para esta tarefa, pode escolher o que construir.

Aqui estão algumas sugestões:

- Ajuste a aplicação de gerador de receitas para melhorá-la ainda mais. Experimente valores de temperatura e os prompts para ver o que consegue criar.
- Crie um "companheiro de estudo". Esta aplicação deve ser capaz de responder a perguntas sobre um tópico, por exemplo Python, poderia ter prompts como "O que é determinado tópico em Python?" ou poderia ter um prompt que pede, mostra-me código para um determinado tópico, etc.
- Bot de história, faça a história ganhar vida, instrua o bot para interpretar um certo personagem histórico e faça perguntas sobre a sua vida e época.

## Solução

### Companheiro de estudo

Abaixo está um prompt inicial, veja como pode usá-lo e ajustá-lo ao seu gosto.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de história

Aqui estão alguns prompts que poderia usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificação de conhecimento

O que faz o conceito de temperatura?

1. Controla quão aleatória é a saída.
1. Controla o tamanho da resposta.
1. Controla quantos tokens são usados.

## 🚀 Desafio

Quando estiver a trabalhar na tarefa, tente variar a temperatura, experimente definir para 0, 0.5 e 1. Lembre-se que 0 é o menos variado e 1 é o mais variado. Qual valor funciona melhor para a sua aplicação?

## Bom trabalho! Continue a sua aprendizagem

Depois de concluir esta lição, confira a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a elevar o seu conhecimento de IA Generativa!

Vá para a Lição 7 onde veremos como [construir aplicações de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->