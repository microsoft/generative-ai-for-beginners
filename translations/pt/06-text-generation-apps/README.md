<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:54:41+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "pt"
}
-->
# Construir Aplicações de Geração de Texto

[![Construir Aplicações de Geração de Texto](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.pt.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para ver o vídeo desta lição)_

Até agora, neste currículo, já viu que existem conceitos fundamentais como prompts e até uma disciplina inteira chamada "engenharia de prompts". Muitas ferramentas com as quais pode interagir, como o ChatGPT, Office 365, Microsoft Power Platform e outras, suportam o uso de prompts para realizar tarefas.

Para adicionar essa experiência a uma aplicação, precisa de compreender conceitos como prompts, completions e escolher uma biblioteca para trabalhar. É exatamente isso que vai aprender neste capítulo.

## Introdução

Neste capítulo, irá:

- Aprender sobre a biblioteca openai e os seus conceitos principais.
- Construir uma aplicação de geração de texto usando openai.
- Compreender como usar conceitos como prompt, temperature e tokens para criar uma aplicação de geração de texto.

## Objetivos de aprendizagem

No final desta lição, será capaz de:

- Explicar o que é uma aplicação de geração de texto.
- Construir uma aplicação de geração de texto usando openai.
- Configurar a sua aplicação para usar mais ou menos tokens e também alterar a temperature, para obter resultados variados.

## O que é uma aplicação de geração de texto?

Normalmente, quando constrói uma aplicação, esta tem algum tipo de interface como as seguintes:

- Baseada em comandos. Aplicações de consola são típicas aplicações onde escreve um comando e este executa uma tarefa. Por exemplo, `git` é uma aplicação baseada em comandos.
- Interface de utilizador (UI). Algumas aplicações têm interfaces gráficas (GUIs) onde clica em botões, insere texto, seleciona opções e mais.

### Aplicações de consola e UI são limitadas

Compare com uma aplicação baseada em comandos onde escreve um comando:

- **É limitada**. Não pode simplesmente escrever qualquer comando, apenas os que a aplicação suporta.
- **Específica de linguagem**. Algumas aplicações suportam várias línguas, mas por padrão a aplicação é construída para uma língua específica, mesmo que possa adicionar suporte a mais línguas.

### Vantagens das aplicações de geração de texto

Então, como é que uma aplicação de geração de texto é diferente?

Numa aplicação de geração de texto, tem mais flexibilidade, não está limitado a um conjunto de comandos ou a uma língua específica de entrada. Em vez disso, pode usar linguagem natural para interagir com a aplicação. Outra vantagem é que, porque já está a interagir com uma fonte de dados treinada num vasto corpus de informação, enquanto uma aplicação tradicional pode estar limitada ao que está numa base de dados.

### O que posso construir com uma aplicação de geração de texto?

Há muitas coisas que pode construir. Por exemplo:

- **Um chatbot**. Um chatbot que responde a perguntas sobre temas, como a sua empresa e os seus produtos, pode ser uma boa opção.
- **Assistente**. Os LLMs são ótimos para coisas como resumir texto, obter insights de texto, produzir texto como currículos e mais.
- **Assistente de código**. Dependendo do modelo de linguagem que usar, pode construir um assistente de código que o ajuda a escrever código. Por exemplo, pode usar um produto como o GitHub Copilot assim como o ChatGPT para ajudar a escrever código.

## Como posso começar?

Bem, precisa de encontrar uma forma de integrar com um LLM, o que normalmente implica as seguintes duas abordagens:

- Usar uma API. Aqui está a construir pedidos web com o seu prompt e recebe texto gerado de volta.
- Usar uma biblioteca. As bibliotecas ajudam a encapsular as chamadas à API e tornam-nas mais fáceis de usar.

## Bibliotecas/SDKs

Existem algumas bibliotecas bem conhecidas para trabalhar com LLMs como:

- **openai**, esta biblioteca facilita a ligação ao seu modelo e o envio de prompts.

Depois, há bibliotecas que operam a um nível mais alto como:

- **Langchain**. Langchain é bem conhecido e suporta Python.
- **Semantic Kernel**. Semantic Kernel é uma biblioteca da Microsoft que suporta as linguagens C#, Python e Java.

## Primeira aplicação usando openai

Vamos ver como podemos construir a nossa primeira aplicação, que bibliotecas precisamos, quanto é necessário e assim por diante.

### Instalar openai

Existem muitas bibliotecas para interagir com OpenAI ou Azure OpenAI. É possível usar várias linguagens de programação como C#, Python, JavaScript, Java e mais. Escolhemos usar a biblioteca Python `openai`, por isso vamos usar o `pip` para a instalar.

```bash
pip install openai
```

### Criar um recurso

Precisa de realizar os seguintes passos:

- Criar uma conta no Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obter acesso ao Azure OpenAI. Vá a [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e solicite acesso.

  > [!NOTE]
  > No momento da escrita, precisa de solicitar acesso ao Azure OpenAI.

- Instalar Python <https://www.python.org/>
- Ter criado um recurso Azure OpenAI Service. Veja este guia para saber como [criar um recurso](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizar chave API e endpoint

Neste ponto, precisa de indicar à sua biblioteca `openai` qual chave API usar. Para encontrar a sua chave API, vá à secção "Keys and Endpoint" do seu recurso Azure OpenAI e copie o valor de "Key 1".

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Agora que tem esta informação copiada, vamos instruir as bibliotecas a usá-la.

> [!NOTE]
> Vale a pena separar a sua chave API do seu código. Pode fazê-lo usando variáveis de ambiente.
>
> - Defina a variável de ambiente `OPENAI_API_KEY` para a sua chave API.
>   `export OPENAI_API_KEY='sk-...'`

### Configurar Azure

Se estiver a usar Azure OpenAI, aqui está como configurar:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Acima estamos a definir o seguinte:

- `api_type` para `azure`. Isto indica à biblioteca para usar Azure OpenAI e não OpenAI.
- `api_key`, esta é a sua chave API encontrada no Portal Azure.
- `api_version`, esta é a versão da API que quer usar. No momento da escrita, a versão mais recente é `2023-05-15`.
- `api_base`, este é o endpoint da API. Pode encontrá-lo no Portal Azure ao lado da sua chave API.

> [!NOTE] > `os.getenv` é uma função que lê variáveis de ambiente. Pode usá-la para ler variáveis como `OPENAI_API_KEY` e `API_BASE`. Defina estas variáveis no seu terminal ou usando uma biblioteca como `dotenv`.

## Gerar texto

A forma de gerar texto é usar a classe `Completion`. Aqui está um exemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

No código acima, criamos um objeto completion e passamos o modelo que queremos usar e o prompt. Depois imprimimos o texto gerado.

### Completions de chat

Até agora, viu como temos usado `Completion` para gerar texto. Mas há outra classe chamada `ChatCompletion` que é mais adequada para chatbots. Aqui está um exemplo de como usá-la:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Mais sobre esta funcionalidade num capítulo futuro.

## Exercício - a sua primeira aplicação de geração de texto

Agora que aprendemos como configurar e usar openai, é hora de construir a sua primeira aplicação de geração de texto. Para construir a sua aplicação, siga estes passos:

1. Crie um ambiente virtual e instale openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Se estiver a usar Windows, escreva `venv\Scripts\activate` em vez de `source venv/bin/activate`.

   > [!NOTE]
   > Localize a sua chave Azure OpenAI indo a [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), pesquise por `Open AI`, selecione o `Open AI resource` e depois selecione `Keys and Endpoint` e copie o valor de `Key 1`.

1. Crie um ficheiro _app.py_ e coloque o seguinte código:

   ```python
   import openai

   openai.api_key = "<replace this value with your open ai key or Azure OpenAI key>"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "<endpoint found in Azure Portal where your API key is>"
   deployment_name = "<deployment name>"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"
   messages = [{"role": "user", "content": prompt}]

   # make completion
   completion = openai.chat.completions.create(model=deployment_name, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > Se estiver a usar Azure OpenAI, precisa de definir `api_type` para `azure` e definir `api_key` para a sua chave Azure OpenAI.

   Deve ver uma saída semelhante a esta:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para diferentes fins

Agora que viu como gerar texto usando um prompt, tem até um programa a funcionar que pode modificar para gerar diferentes tipos de texto.

Os prompts podem ser usados para todo o tipo de tarefas. Por exemplo:

- **Gerar um tipo de texto**. Por exemplo, pode gerar um poema, perguntas para um quiz, etc.
- **Pesquisar informação**. Pode usar prompts para procurar informação como no exemplo 'O que significa CORS no desenvolvimento web?'.
- **Gerar código**. Pode usar prompts para gerar código, por exemplo, desenvolver uma expressão regular para validar emails ou até gerar um programa completo, como uma aplicação web.

## Um caso de uso mais prático: um gerador de receitas

Imagine que tem ingredientes em casa e quer cozinhar algo. Para isso, precisa de uma receita. Uma forma de encontrar receitas é usar um motor de busca ou pode usar um LLM para isso.

Poderia escrever um prompt assim:

> "Mostra-me 5 receitas para um prato com os seguintes ingredientes: frango, batatas e cenouras. Por receita, lista todos os ingredientes usados"

Dado o prompt acima, poderá obter uma resposta semelhante a:

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

Este resultado é ótimo, já sei o que cozinhar. Neste ponto, melhorias úteis poderiam ser:

- Filtrar ingredientes que não gosto ou aos quais sou alérgico.
- Produzir uma lista de compras, caso não tenha todos os ingredientes em casa.

Para os casos acima, vamos adicionar um prompt adicional:

> "Por favor, remove receitas com alho pois sou alérgico e substitui por outro ingrediente. Além disso, por favor produz uma lista de compras para as receitas, considerando que já tenho frango, batatas e cenouras em casa."

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

Estas são as suas cinco receitas, sem alho mencionado, e também tem uma lista de compras considerando o que já tem em casa.

## Exercício - construir um gerador de receitas

Agora que encenámos um cenário, vamos escrever código para corresponder ao cenário demonstrado. Para isso, siga estes passos:

1. Use o ficheiro _app.py_ existente como ponto de partida
1. Localize a variável `prompt` e altere o seu código para o seguinte:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Se agora executar o código, deverá ver uma saída semelhante a:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, o seu LLM é não determinístico, por isso pode obter resultados diferentes cada vez que executar o programa.

   Ótimo, vamos ver como podemos melhorar as coisas. Para melhorar, queremos garantir que o código é flexível, para que os ingredientes e o número de receitas possam ser alterados e melhorados.

1. Vamos alterar o código da seguinte forma:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Um teste do código pode ficar assim:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Melhorar adicionando filtro e lista de compras

Agora temos uma aplicação funcional capaz de produzir receitas e é flexível pois depende de entradas do utilizador, tanto no número de receitas como nos ingredientes usados.

Para melhorar ainda mais, queremos adicionar o seguinte:

- **Filtrar ingredientes**. Queremos poder filtrar ingredientes que não gostamos ou aos quais somos alérgicos. Para isso, podemos editar o nosso prompt existente e adicionar uma condição de filtro no final, assim:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Acima, adicionamos `{filter}` no final do prompt e também capturamos o valor do filtro do utilizador.

  Um exemplo de entrada ao executar o programa pode agora ser assim:

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

  Como pode ver, quaisquer receitas com leite foram filtradas. Mas, se for intolerante à lactose, poderá querer filtrar também receitas com queijo, por isso é importante ser claro.

- **Produzir uma lista de compras**. Queremos produzir uma lista de compras, considerando o que já temos em casa.

  Para esta funcionalidade, poderíamos tentar resolver tudo num único prompt ou dividir em dois prompts. Vamos tentar a segunda abordagem. Aqui sugerimos adicionar um prompt adicional, mas para isso funcionar, precisamos de adicionar o resultado do primeiro prompt como contexto para o segundo prompt.

  Localize a parte do código que imprime o resultado do primeiro prompt e adicione o seguinte código abaixo:

  ```python
  old_prompt_result = completion.choices[0].message.content
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  messages = [{"role": "user", "content": new_prompt}]
  completion = openai.Completion.create(engine=deployment_name, messages=messages, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].message.content)
  ```

  Note o seguinte:

  1. Estamos a construir um novo prompt adicionando o resultado do primeiro prompt ao novo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
  1. Fazemos um novo pedido, mas também considerando o número de tokens que pedimos no primeiro prompt, por isso desta vez definimos `max_tokens` como 1200.

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     Testando este código, chegamos agora ao seguinte resultado:

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

O que temos até agora é um código que funciona, mas há alguns ajustes que devemos fazer para melhorar ainda mais. Algumas coisas que devemos fazer são:

- **Separar segredos do código**, como a chave da API. Segredos não devem estar no código e devem ser guardados num local seguro. Para separar segredos do código, podemos usar variáveis de ambiente e bibliotecas como `python-dotenv` para as carregar a partir de um ficheiro. Veja como isso ficaria no código:

  1. Crie um ficheiro `.env` com o seguinte conteúdo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Nota, para Azure, precisa de definir as seguintes variáveis de ambiente:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     No código, carregaria as variáveis de ambiente assim:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **Uma palavra sobre o comprimento dos tokens**. Devemos considerar quantos tokens precisamos para gerar o texto que queremos. Os tokens têm custo, por isso, sempre que possível, devemos tentar ser económicos com o número de tokens usados. Por exemplo, podemos reformular o prompt para usar menos tokens?

  Para alterar o número de tokens usados, pode usar o parâmetro `max_tokens`. Por exemplo, se quiser usar 100 tokens, faria:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentar com a temperatura**. A temperatura é algo que ainda não mencionámos, mas é um contexto importante para o desempenho do nosso programa. Quanto maior o valor da temperatura, mais aleatória será a saída. Por outro lado, quanto menor o valor da temperatura, mais previsível será a saída. Pense se quer variação na sua saída ou não.

  Para alterar a temperatura, pode usar o parâmetro `temperature`. Por exemplo, se quiser usar uma temperatura de 0.5, faria:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Nota, quanto mais próximo de 1.0, mais variada será a saída.

## Tarefa

Para esta tarefa, pode escolher o que construir.

Aqui ficam algumas sugestões:

- Ajuste a aplicação geradora de receitas para a melhorar ainda mais. Experimente valores de temperatura e os prompts para ver o que consegue criar.
- Crie um "companheiro de estudo". Esta aplicação deve ser capaz de responder a perguntas sobre um tema, por exemplo Python, pode ter prompts como "O que é determinado tema em Python?", ou um prompt que diga, mostra-me código para determinado tema, etc.
- Bot de história, faça a história ganhar vida, instrua o bot para interpretar uma certa personagem histórica e faça-lhe perguntas sobre a sua vida e época.

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

Aqui estão alguns prompts que pode usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificação de conhecimento

O que faz o conceito de temperatura?

1. Controla o quão aleatória é a saída.
1. Controla o tamanho da resposta.
1. Controla quantos tokens são usados.

## 🚀 Desafio

Ao trabalhar na tarefa, tente variar a temperatura, experimente defini-la para 0, 0.5 e 1. Lembre-se que 0 é o menos variado e 1 o mais. Qual valor funciona melhor para a sua aplicação?

## Excelente trabalho! Continue a aprender

Depois de completar esta lição, consulte a nossa [coleção de Aprendizagem de IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar a aprimorar os seus conhecimentos em IA Generativa!

Siga para a Lição 7 onde vamos ver como [construir aplicações de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.