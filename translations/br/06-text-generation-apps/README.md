<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:55:13+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "br"
}
-->
# Construindo Aplicações de Geração de Texto

[![Construindo Aplicações de Geração de Texto](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.br.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(Clique na imagem acima para assistir ao vídeo desta lição)_

Até agora, você viu neste currículo que existem conceitos fundamentais como prompts e até uma disciplina inteira chamada "engenharia de prompts". Muitas ferramentas com as quais você pode interagir, como ChatGPT, Office 365, Microsoft Power Platform e outras, te ajudam usando prompts para realizar algo.

Para você adicionar essa experiência a um app, é preciso entender conceitos como prompts, completions e escolher uma biblioteca para trabalhar. É exatamente isso que você vai aprender neste capítulo.

## Introdução

Neste capítulo, você vai:

- Conhecer a biblioteca openai e seus conceitos principais.
- Construir um app de geração de texto usando openai.
- Entender como usar conceitos como prompt, temperatura e tokens para criar um app de geração de texto.

## Objetivos de aprendizado

Ao final desta lição, você será capaz de:

- Explicar o que é um app de geração de texto.
- Construir um app de geração de texto usando openai.
- Configurar seu app para usar mais ou menos tokens e também alterar a temperatura, para obter resultados variados.

## O que é um app de geração de texto?

Normalmente, quando você constrói um app, ele tem algum tipo de interface como as seguintes:

- Baseado em comandos. Apps de console são típicos apps onde você digita um comando e ele executa uma tarefa. Por exemplo, `git` é um app baseado em comandos.
- Interface de usuário (UI). Alguns apps têm interfaces gráficas (GUIs) onde você clica em botões, digita texto, seleciona opções e mais.

### Apps de console e UI são limitados

Compare com um app baseado em comandos onde você digita um comando:

- **É limitado**. Você não pode digitar qualquer comando, apenas os que o app suporta.
- **Idioma específico**. Alguns apps suportam vários idiomas, mas por padrão o app é construído para um idioma específico, mesmo que você possa adicionar suporte para mais idiomas.

### Benefícios dos apps de geração de texto

Então, como um app de geração de texto é diferente?

Em um app de geração de texto, você tem mais flexibilidade, não está limitado a um conjunto de comandos ou a um idioma específico de entrada. Em vez disso, você pode usar linguagem natural para interagir com o app. Outro benefício é que, como você já está interagindo com uma fonte de dados treinada em um vasto corpus de informações, enquanto um app tradicional pode ser limitado ao que está em um banco de dados.

### O que posso construir com um app de geração de texto?

Há muitas coisas que você pode construir. Por exemplo:

- **Um chatbot**. Um chatbot que responde perguntas sobre temas, como sua empresa e seus produtos, pode ser uma boa opção.
- **Assistente**. LLMs são ótimos para coisas como resumir textos, extrair insights de textos, produzir textos como currículos e mais.
- **Assistente de código**. Dependendo do modelo de linguagem que você usar, pode construir um assistente de código que te ajuda a escrever código. Por exemplo, você pode usar um produto como GitHub Copilot, assim como o ChatGPT, para ajudar a escrever código.

## Como posso começar?

Bem, você precisa encontrar uma forma de integrar com um LLM, o que geralmente envolve as duas abordagens a seguir:

- Usar uma API. Aqui você constrói requisições web com seu prompt e recebe o texto gerado de volta.
- Usar uma biblioteca. Bibliotecas ajudam a encapsular as chamadas da API e tornam o uso mais fácil.

## Bibliotecas/SDKs

Existem algumas bibliotecas bem conhecidas para trabalhar com LLMs, como:

- **openai**, essa biblioteca facilita a conexão com seu modelo e o envio de prompts.

Depois, há bibliotecas que operam em um nível mais alto, como:

- **Langchain**. Langchain é bem conhecida e suporta Python.
- **Semantic Kernel**. Semantic Kernel é uma biblioteca da Microsoft que suporta as linguagens C#, Python e Java.

## Primeiro app usando openai

Vamos ver como construir nosso primeiro app, quais bibliotecas precisamos, o que é necessário e assim por diante.

### Instalar openai

Existem muitas bibliotecas para interagir com OpenAI ou Azure OpenAI. É possível usar várias linguagens de programação também, como C#, Python, JavaScript, Java e outras. Escolhemos usar a biblioteca Python `openai`, então usaremos o `pip` para instalá-la.

```bash
pip install openai
```

### Criar um recurso

Você precisa seguir os seguintes passos:

- Crie uma conta no Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst).
- Obtenha acesso ao Azure OpenAI. Vá para [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) e solicite acesso.

  > [!NOTE]
  > No momento da escrita, é necessário solicitar acesso ao Azure OpenAI.

- Instale o Python <https://www.python.org/>
- Crie um recurso do Azure OpenAI Service. Veja este guia para saber como [criar um recurso](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### Localizar chave da API e endpoint

Neste ponto, você precisa informar à sua biblioteca `openai` qual chave da API usar. Para encontrar sua chave da API, vá para a seção "Keys and Endpoint" do seu recurso Azure OpenAI e copie o valor de "Key 1".

![Chaves e Endpoint no portal Azure](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

Agora que você copiou essa informação, vamos instruir as bibliotecas a usá-la.

> [!NOTE]
> Vale a pena separar sua chave da API do seu código. Você pode fazer isso usando variáveis de ambiente.
>
> - Defina a variável de ambiente `OPENAI_API_KEY` com sua chave da API.
>   `export OPENAI_API_KEY='sk-...'`

### Configuração para Azure

Se você estiver usando Azure OpenAI, veja como configurar:

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

Acima estamos definindo o seguinte:

- `api_type` para `azure`. Isso indica à biblioteca para usar Azure OpenAI e não OpenAI.
- `api_key`, essa é sua chave da API encontrada no portal Azure.
- `api_version`, essa é a versão da API que você quer usar. No momento da escrita, a versão mais recente é `2023-05-15`.
- `api_base`, esse é o endpoint da API. Você pode encontrá-lo no portal Azure ao lado da sua chave da API.

> [!NOTE] > `os.getenv` é uma função que lê variáveis de ambiente. Você pode usá-la para ler variáveis como `OPENAI_API_KEY` e `API_BASE`. Defina essas variáveis no seu terminal ou usando uma biblioteca como `dotenv`.

## Gerar texto

A forma de gerar texto é usar a classe `Completion`. Veja um exemplo:

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

No código acima, criamos um objeto completion e passamos o modelo que queremos usar e o prompt. Depois imprimimos o texto gerado.

### Completions de chat

Até agora, você viu como usamos `Completion` para gerar texto. Mas existe outra classe chamada `ChatCompletion` que é mais adequada para chatbots. Veja um exemplo de uso:

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

Mais sobre essa funcionalidade em um capítulo futuro.

## Exercício - seu primeiro app de geração de texto

Agora que aprendemos como configurar e usar openai, é hora de construir seu primeiro app de geração de texto. Para construir seu app, siga estes passos:

1. Crie um ambiente virtual e instale openai:

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > Se estiver usando Windows, digite `venv\Scripts\activate` em vez de `source venv/bin/activate`.

   > [!NOTE]
   > Localize sua chave Azure OpenAI acessando [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst), pesquise por `Open AI`, selecione o recurso `Open AI` e depois `Keys and Endpoint` e copie o valor de `Key 1`.

1. Crie um arquivo _app.py_ e coloque o seguinte código:

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
   > Se estiver usando Azure OpenAI, você precisa definir `api_type` como `azure` e configurar `api_key` com sua chave Azure OpenAI.

   Você deve ver uma saída parecida com esta:

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## Diferentes tipos de prompts, para diferentes propósitos

Agora você viu como gerar texto usando um prompt. Você até tem um programa funcionando que pode modificar para gerar diferentes tipos de texto.

Prompts podem ser usados para todo tipo de tarefa. Por exemplo:

- **Gerar um tipo de texto**. Por exemplo, você pode gerar um poema, perguntas para um quiz etc.
- **Buscar informações**. Você pode usar prompts para buscar informações, como no exemplo: 'O que significa CORS no desenvolvimento web?'.
- **Gerar código**. Você pode usar prompts para gerar código, por exemplo, desenvolver uma expressão regular para validar emails ou até gerar um programa inteiro, como um app web.

## Um caso de uso mais prático: um gerador de receitas

Imagine que você tem ingredientes em casa e quer cozinhar algo. Para isso, precisa de uma receita. Uma forma de encontrar receitas é usar um motor de busca ou você pode usar um LLM para isso.

Você poderia escrever um prompt assim:

> "Mostre 5 receitas para um prato com os seguintes ingredientes: frango, batatas e cenouras. Para cada receita, liste todos os ingredientes usados"

Dado o prompt acima, você pode receber uma resposta parecida com:

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

Esse resultado é ótimo, já sei o que cozinhar. Neste ponto, melhorias úteis poderiam ser:

- Filtrar ingredientes que não gosto ou sou alérgico.
- Produzir uma lista de compras, caso eu não tenha todos os ingredientes em casa.

Para esses casos, vamos adicionar um prompt adicional:

> "Por favor, remova receitas com alho pois sou alérgico e substitua por outro ingrediente. Além disso, por favor, produza uma lista de compras para as receitas, considerando que já tenho frango, batatas e cenouras em casa."

Agora você tem um novo resultado, a saber:

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

Essas são suas cinco receitas, sem alho mencionado, e você também tem uma lista de compras considerando o que já tem em casa.

## Exercício - construa um gerador de receitas

Agora que encenamos um cenário, vamos escrever código para corresponder ao cenário demonstrado. Para isso, siga estes passos:

1. Use o arquivo _app.py_ existente como ponto de partida
1. Localize a variável `prompt` e altere seu código para o seguinte:

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   Se você executar o código agora, deve ver uma saída parecida com:

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, seu LLM é não determinístico, então você pode obter resultados diferentes a cada execução.

   Ótimo, vamos ver como podemos melhorar as coisas. Para melhorar, queremos garantir que o código seja flexível, para que ingredientes e número de receitas possam ser alterados facilmente.

1. Vamos alterar o código da seguinte forma:

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Um teste rápido com o código poderia ser assim:

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### Melhorar adicionando filtro e lista de compras

Agora temos um app funcional capaz de produzir receitas e é flexível, pois depende de entradas do usuário, tanto no número de receitas quanto nos ingredientes usados.

Para melhorar ainda mais, queremos adicionar o seguinte:

- **Filtrar ingredientes**. Queremos poder filtrar ingredientes que não gostamos ou somos alérgicos. Para isso, podemos editar nosso prompt existente e adicionar uma condição de filtro no final, assim:

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Acima, adicionamos `{filter}` ao final do prompt e também capturamos o valor do filtro do usuário.

  Um exemplo de entrada ao rodar o programa pode ser assim:

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

  Como você pode ver, qualquer receita com leite foi filtrada. Mas, se você for intolerante à lactose, pode querer filtrar receitas com queijo também, então é importante ser claro.

- **Produzir uma lista de compras**. Queremos gerar uma lista de compras, considerando o que já temos em casa.

  Para essa funcionalidade, poderíamos tentar resolver tudo em um único prompt ou dividir em dois prompts. Vamos tentar a segunda abordagem. Aqui sugerimos adicionar um prompt adicional, mas para isso funcionar, precisamos adicionar o resultado do primeiro prompt como contexto para o segundo prompt.

  Localize a parte do código que imprime o resultado do primeiro prompt e adicione o seguinte código logo abaixo:

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

  1. Estamos construindo um novo prompt adicionando o resultado do primeiro prompt ao novo prompt:

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. Fazemos uma nova requisição, mas também considerando o número de tokens que pedimos no primeiro prompt, então desta vez definimos `max_tokens` como 1200.

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

Testando esse código, chegamos agora à seguinte saída:

```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## Melhore sua configuração

O que temos até agora é um código que funciona, mas há alguns ajustes que devemos fazer para melhorar ainda mais. Algumas coisas que devemos fazer são:

- **Separar segredos do código**, como a chave da API. Segredos não pertencem ao código e devem ser armazenados em um local seguro. Para separar segredos do código, podemos usar variáveis de ambiente e bibliotecas como `python-dotenv` para carregá-las a partir de um arquivo. Veja como isso ficaria no código:

  1. Crie um arquivo `.env` com o seguinte conteúdo:

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     
> Note que, para Azure, você precisa definir as seguintes variáveis de ambiente:

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

- **Uma palavra sobre o comprimento dos tokens**. Devemos considerar quantos tokens precisamos para gerar o texto desejado. Tokens custam dinheiro, então, sempre que possível, devemos tentar ser econômicos com a quantidade de tokens usados. Por exemplo, podemos reformular o prompt para usar menos tokens?

  Para alterar a quantidade de tokens usados, você pode usar o parâmetro `max_tokens`. Por exemplo, se quiser usar 100 tokens, você faria:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **Experimentando com a temperatura**. Temperatura é algo que ainda não mencionamos, mas é um contexto importante para o desempenho do nosso programa. Quanto maior o valor da temperatura, mais aleatória será a saída. Por outro lado, quanto menor o valor da temperatura, mais previsível será a saída. Considere se você quer variação na sua saída ou não.

  Para alterar a temperatura, você pode usar o parâmetro `temperature`. Por exemplo, se quiser usar uma temperatura de 0.5, você faria:

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > Note que, quanto mais próximo de 1.0, mais variada será a saída.

## Tarefa

Para esta tarefa, você pode escolher o que construir.

Aqui estão algumas sugestões:

- Ajuste o app gerador de receitas para melhorá-lo ainda mais. Brinque com os valores de temperatura e os prompts para ver o que consegue criar.
- Crie um "companheiro de estudos". Este app deve ser capaz de responder perguntas sobre um tema, por exemplo Python, você poderia ter prompts como "O que é determinado tópico em Python?", ou um prompt que diga, mostre-me código para determinado tópico, etc.
- Bot de história, faça a história ganhar vida, instrua o bot a interpretar um personagem histórico e faça perguntas sobre sua vida e época.

## Solução

### Companheiro de estudos

Abaixo está um prompt inicial, veja como você pode usá-lo e ajustá-lo ao seu gosto.

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### Bot de história

Aqui estão alguns prompts que você poderia usar:

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## Verificação de conhecimento

O que o conceito de temperatura faz?

1. Controla o quão aleatória é a saída.
1. Controla o tamanho da resposta.
1. Controla quantos tokens são usados.

## 🚀 Desafio

Ao trabalhar na tarefa, tente variar a temperatura, definindo-a como 0, 0.5 e 1. Lembre-se que 0 é o menos variado e 1 é o mais. Qual valor funciona melhor para seu app?

## Ótimo trabalho! Continue seu aprendizado

Após completar esta lição, confira nossa [coleção de Aprendizado em IA Generativa](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) para continuar aprimorando seu conhecimento em IA Generativa!

Siga para a Lição 7, onde veremos como [construir aplicações de chat](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)!

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.