# 第六章：创建文本生成应用

[![Building Text Generation Applications](../../images/06-lesson-banner.png?WT.mc_id=academic-105485-koreyst)](https://learn.microsoft.com/_themes/docs.theme/master/en-us/_themes/global/video-embed.html?id=bf3f3528-9871-4628-8616-b4b03cb23dcd?WT.mc_id=academic-105485-koreyst)

> _(点击该图片看本章导学视频)_

到目前为止，您已经通过本系列课程看到了如提示之类的核心概念，甚至是称为“提示工程”的整个学科。 您可以与通过使用如 ChatGPT、Office 365、Microsoft Power Platform 等工具结合提示来完成某些工作任务。

为了将这样的体验添加到应用程序中，您需要了解提示、补全等概念并选择要使用的相关库。 这正是您将在本章中学到的内容。

## 本章概述

在本章中，您将学习到：

- 了解 openai 库及其核心概念。
- 使用 openai 构建文本生成应用程序。
- 了解如何使用提示、temperature 和 tokens 等概念来构建文本生成应用程序。

## 学习目标

在完成本章的学习，您将能够：

- 解释什么是文本生成应用程序。
- 使用 openai 构建文本生成应用程序。
- 配置您的应用程序以使用更多或更少的 tokens，并更改 temperature，以获得不同的输出。

## 什么是文本生成应用

一般来说当您构建应用程序时，它具有某种界面，如下所示：

- 基于命令。 控制台应用程序是典型的应用程序，您可以在其中键入命令并执行任务。 例如，“git”是一个基于命令的应用程序。
- 用户界面（UI）。 某些应用程序具有图形用户界面 (GUI)，您可以在其中单击按钮、输入文本、选择选项等。

### 传统控制台和 UI 应用程序的局限性

将其与输入命令的传统应用程序进行比较：

- **存在局限性**。 您不能输入任意命令，只能键入该应用程序支持的命令。
- **特定于某种语言**。 某些应用程序支持多种语言，但默认情况下，即使可以添加更多语言支持，该应用程序也是针对有限的语言构建的。

### 文本生成应用程序的优势

文本生成应用程序有何不同呢？

在文本生成应用程序中，您拥有更大的灵活性，不再局限于一组特定的命令或特定的输入语言。 相反，您可以使用自然语言与应用程序交互。 另一个好处是，因为您已经在与经过大量信息库训练的数据源进行交互，而传统应用程序可能仅限于在数据库中存储的有限内容。

### 使用文本生成应用程序构建什么？

您可以创建很多东西。 例如：

- **聊天机器人** 回答有关您的公司及其产品等主题的问题的聊天机器人可能是一个不错的选择。
- **协同助手** LLMs 擅长总结文本、从文本中获取见解、生成简历等文本等。
- **代码助手** 根据您使用的编程语言模型，您可以构建一个代码助手来帮助您编写代码。 例如，您可以使用 GitHub Copilot 和 ChatGPT 等产品来帮助您编写代码。

## 如何入门？

您需要找到一种与 LLMs 结合的方法，通常使用以下两种方法：

- API 在这里，您将根据提示构建 Web 请求并返回生成的文本。
- Libraries 库有助于封装 API 调用并使其更易于使用。

## Libraries/SDKs

有一些比较通用的与 LLMs 整合的 librarys，例如：

- **openai**，这个 librarys 可以轻松连接到您的模型并发送提示。

还有一些在更高级别的框架运行的 librarys，例如：

- **Langchain**。 Langchain 支持 Python 比较通用的 library
- **Semantic Kernel**。 Semantic Kernel 是 Microsoft 提供的一个 library，支持 C#、Python 和 Java 语言。

## 人生中第一个 openai 应用

Let's see how we can build our first app, what libraries we need, how much is required and so on.

让我们看看如何构建人生中第一个 openai 应用，我们需要哪些 libraries，需要多少技能等等。

### 安装 openai

There are many libraries out there for interacting with OpenAI or Azure OpenAI. It's possible to use numerous programming languages as well like C#, Python, JavaScript, Java and more. We've chosen to use the `openai` Python library, so we'll use `pip` to install it.

有许多 libraries 可用于与 OpenAI 或 Azure OpenAI 交互。 还可以使用不同的编程语言，如 C#、Python、JavaScript、Java 等。 我们选择使用 `openai` Python 库，通过 `pip` 来安装它。

```bash
pip install openai
```

### 创建资源

您需要执行以下步骤：

- 在 Azure [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst) 上创建帐户。
- 访问 Azure Open AI。 进入到 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 并请求访问权限。

  > [!注意]
  > 您需要申请访问 Azure Open AI Service 的访问。

- 安装 Python <https://www.python.org/>
- 已创建 Azure OpenAI 服务。 请参阅本指南，了解如何[创建资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst).

### 添加 API key and endpoint

您需要告诉“openai”库要使用什么 API key。 要查找 API key ，请转到创建好的 Azure Open AI Service 中的 "Keys and Endpoint"部分并复制 "Key 1" 值。

![Keys and Endpoint resource blade in Azure Portal](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

复制 Key 后，让我们调用 libraries 使用它。

> [!注意]
> 通过设置环境变量将 API Key 与代码分开是很重要的
>
> - 为您的 API key 中设置 `OPENAI_API_KEY`
> - `export OPENAI_API_KEY='sk-...'`

### 配置 Azure 环境

如果您使用 Azure OpenAI , 请按照以后步骤进行设置

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

设置相关的补充

- `api_type` 为 `azure`. 这告诉 librarys 使用 Azure Open AI 而不是 OpenAI。
- `api_key`, 对应 Azure Portal 中的 API Key
- `api_version`, 这是您要使用的 API 版本。 在撰写本文时，最新版本是'2023-05-15'。
- `api_base`, 这是 API 的 endpoint 。 您可以在 Azure Portal 中 API Key 下方找到它。

> [注意] > `os.getenv` 是一个读取环境变量的函数。 您可以使用它来读取“OPENAI_API_KEY”和“API_BASE”等环境变量。 在终端中或使用“dotenv”等库设置这些环境变量。

## 文字生成

生成文本的方法是使用“Completion”类。 这是一个例子：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上面的代码中，我们创建一个 completion 对象并传入我们要使用的模型和提示。 然后我们输出生成的文本。

### 聊天补全

到目前为止，您已经了解了我们如何使用“Completion”来生成文本。 但还有另一个更适合聊天机器人的类，称为“ChatCompletion”。 这是例子：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

下一章将详细介绍此功能。

## 练习 - 您的人生中首个文本生成应用

现在我们已经了解了如何设置和配置 openai，是时候构建您的第一个文本生成应用程序了。 请按照下列步骤操作：

1. 创建虚拟环境并安装 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!注意]
   > 如果您使用的是 Windows，请输入 `venv\Scripts\activate` 而不是 `source venv/bin/activate`。

   > [!注意]
   > 转至 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 找到您的 Azure Open AI Key ,在资源中搜索“Open AI” `并选择“打开 AI 资源”，然后选择`Keys and Endpoint`并复制`Key 1` 值。

2. 创建 _app.py_ 文件并添加以下代码:

   ```python
   import openai

   openai.api_key = "您的 openai key 或 Azure OpenAI key"

   openai.api_type = 'azure'
   openai.api_version = '2023-05-15'
   openai.api_base = "您的 Azure OpenAI Endpoint"
   deployment_name = "部署模型的名字"

   # add your completion code
   prompt = "Complete the following: Once upon a time there was a"

   # make completion
   completion = openai.Completion.create(engine= deployment_name, model="davinci-002", prompt=prompt)

   # print response
   print(completion.choices[0].text)
   ```

   > [!注意]
   > 如果您使用的是 Azure Open AI，则需要将 `api_type` 设置为 `azure`，并将 `api_key` 设置为您的 Azure Open AI Key

   您应该看到如下所示的输出结果：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同类型的提示，针对不同的事情

现在您已经了解了如何使用提示生成文本。 您甚至可以启动并运行一个程序，可以对其进行修改以生成不同类型的文本。

提示可用于各种任务。 例如：

- **生成一种类型的文本**。 例如，生成一首诗、测验题目等。
- **查找信息**。 您可以使用提示来查找信息，例如以下示例'What does CORS mean in web development?'。
- **生成代码**。 您可以使用提示来生成代码，例如开发用于验证电子邮件的正则表达式，或者为什么不生成整个程序，例如 web 应用？

## 进阶学习：菜谱生成器

象一下，你家里有食材，你想煮点东西。 为此，你需要一个食谱。 查找食谱的一种方法是使用搜索引擎，或者您可以使用 LLMs 来这样做。

你可以这样写一个提示：

> "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"

鉴于上述提示，您可能会得到类似于以下结果：

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

1. Chicken and Potato Stew:
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

1. Chicken and Potato Bake:
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

1. Chicken and Potato Soup:
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

1. Chicken and Potato Hash:
Ingredients:
- 2 tablespoons olive oil
- 2 chicken breasts, cut into cubes
- 2 potatoes, cut into cubes
- 2 carrots, cut into cubes
- 1 onion, diced
- 2 cloves garlic, minced
- 1 teaspoon dried oregano
```

结果很好，我知道该怎么做菜了。但希望有更进一步的改进是：

- 过滤掉我不喜欢或过敏的成分。
- 制作一份购物清单，以防我家里没有所有原料。

针对上述情况，我们添加一个额外的提示：

> "Please remove recipes with garlic as I'm allergic and replace it with something else. Also, please produce a shopping list for the recipes, considering I already have chicken, potatoes and carrots at home."

现在你有了一个新的结果，即：

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

1. Chicken and Potato Stew:
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

1. Chicken and Potato Bake:
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

1. Chicken and Potato Soup:
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

1. Chicken and Potato Hash:
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

That's your five recipes, with no garlic mentioned and you also have a shopping list considering what you already have at home.

这是根据您的购买清单生成你的食谱（不包含大蒜）

## 实战 - 打造一个菜谱生成器

根据场景，让我们编写代码来完整代码。为此，请按照下列步骤操作：

1. 使用现有的 _app.py_ 文件作为起点
2. 找到 `prompt` 变量并将其代码更改为以下内容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   运行代码，您应该会看到类似以下内容的输出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, your LLM is nondeterministic, so you might get different results every time you run the program.

   Great, let's see how we can improve things. To improve things, we want to make sure the code is flexible, so ingredients and number of recipes can be improved and changed.

3. 让我们按以下方式更改代码：

   ```python
   no_recipes = input("No of recipes (for example, 5: ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots: ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   Taking the code for a test run, could look like this:

   ```output
   No of recipes (for example, 5: 3
   List of ingredients (for example, chicken, potatoes, and carrots: milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通过添加过滤器和购物清单进行改进

我们现在有一个能够生成食谱的应用，并且它使用很方便，基于用户的输入和食谱的数量所使用的成分。

为了进一步改进它，添加以下内容：

- **过滤掉成分**。 我们希望能够过滤掉我们不喜欢或过敏的成分。 要完成此更改，我们可以编辑现有提示并在其末尾添加过滤条件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free: ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  Above, we add `{filter}` to the end of the prompt and we also capture the filter value from the user.

  An example input of running the program can now look like so:

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

  2. In a large pot, sauté onions in butter until golden brown.
  3. Add beef broth, milk, thyme, salt, and pepper. Bring to a boil.
  4. Reduce heat and simmer for 10 minutes.
  5. Place french bread slices on soup bowls.
  6. Ladle soup over bread.
  7. Sprinkle with Parmesan cheese.

  8. Onion and Potato Soup

  Ingredients:

  -1 large onion, chopped
  -2 cups potatoes, diced
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper

  Instructions:

  9. In a large pot, sauté onions in butter until golden brown.
  10. Add potatoes, vegetable broth, milk, and pepper. Bring to a boil.
  11. Reduce heat and simmer for 10 minutes.
  12. Serve hot.

  13. Creamy Onion Soup

  Ingredients:

  -1 large onion, chopped
  -3 cups vegetable broth
  -1 cup milk
  -1/4 teaspoon black pepper
  -1/4 cup all-purpose flour
  -1/2 cup shredded Parmesan cheese

  Instructions:

  14. In a large pot, sauté onions in butter until golden brown.
  15. Add vegetable broth, milk, and pepper. Bring to a boil.
  16. Reduce heat and simmer for 10 minutes.
  17. In a small bowl, whisk together flour and Parmesan cheese until smooth.
  18. Add to soup and simmer for an additional 5 minutes, or until soup has thickened.
  ```

  正如您所看到的，任何含有牛奶的食谱都已被过滤掉。 但是，如果您患有乳糖不耐症，您可能也想过滤掉含有奶酪的食谱，因此有必要明确一下。

  ```python

  ```

- **制作购物清单**。 我们想根据家里已有的物品制定一份购物清单。

  对于此功能，我们可以尝试在一个提示中解决所有问题，也可以将其分成两个提示。 让我们尝试一下后一种方法。 在这里，我们建议添加一个额外的提示，但为了使其起作用，我们需要将前一个提示的结果作为上下文添加到后一个提示中。

  找到代码中打印第一个提示结果的部分，并添加以下代码：

  ```python
  old_prompt_result = completion.choices[0].text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)

  # print response
  print("Shopping list:")
  print(completion.choices[0].text)
  ```

  请注意以下事项：

  1. 我们通过将第一个提示的结果添加到新提示来构造一个新提示

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  2. 我们提出一个新的请求，但也考虑到我们在第一个提示中请求的 token 数量，所以这次我们说 `max_tokens` 是 1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     运行代码，结果如下：

     ```output
     No of recipes (for example, 5: 2
     List of ingredients (for example, chicken, potatoes, and carrots: apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free: sugar
     Recipes:
      or milk.

     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
      -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改进您的设置

到目前为止，我们拥有的是可以运行的代码，但是我们应该做一些调整来进一步改进。 我们应该做的一些事情是：

- **将 Key 与代码分开**，例如 API Key。Key 不属于代码，应存储在安全的位置。 为了将 Key 与代码分开，我们可以使用环境变量和像`python-dotenv` 这样的 libraries 从文件中加载它们。 代码如下：

  1. 创建一个包含以下内容的 `.env` 文件：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > Note, for Azure, you need to set the following environment variables:

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     In code, you would load the environment variables like so:

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **关于 token 长度**。 我们应该考虑需要多少 token 来生成我们想要的文本。 token 需要花钱，因此在可能的情况下，我们应该尽量节约使用 token 的数量。 例如，我们可以对提示进行调整，以便我们可以使用更少的 token

  要更改使用的 token，您可以使用 `max_tokens` 参数。 例如，如果您想使用 100 个 token，您可以这样做：

  ```python
  completion = openai.Completion.create(model="davinci-002", prompt=prompt, max_tokens=100)
  ```

**进行 temperature 调整试验**。 temperature 是我们到目前为止还没有提到的东西，但它是我们的程序如何执行的重要元素。 temperature 值越高，输出就越随机。 相反， temperature 值越低，输出就越可预测。 考虑一下您是否希望输出有所变化。

    要改变 temperature ，您可以使用 `temperature` 参数。 例如，如果您想使用 0.5 的 temperature ，您可以这样做：

    ```python
    completion = openai.Completion.create(model="davinci-002", prompt=prompt, temperature=0.5)
    ```

> 请注意，越接近 1.0，输出的变化就越多。

## 作业

对于此作业，选择要构建的内容。

以下是一些建议：

- 调整食谱生成器应用程序以进一步改进它。 尝试一下温度值和提示，看看你能想出什么。
- 建立一个“学习伙伴”。 这个应用程序应该能够回答有关某个主题（例如 Python）的问题，您可能会收到诸如“Python 中的某个主题是什么？”之类的提示，或者您可能会收到一个提示，显示某个主题的代码等。
- 历史机器人，让历史变得生动起来，指导机器人扮演某个历史人物，并向其询问有关其生活和时代的问题。

## 解决方案

### 学习伙伴

下面是一个基础提示，看看如何使用它并根据自己的喜好进行调整。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 历史机器人

以下是您可能会使用的一些提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words:"
```

## 知识检查

temperature 有什么作用？

1. 它控制输出的随机程度。
2. 它控制响应的大小。
3. 它控制使用多少 tokens 。

A: 1

## 🚀 知识拓展

完成作业时，尝试改变 temperature ，尝试将其设置为 0、0.5 和 1。请记住，0 是变化最少的，1 是变化最多的，看看什么值最适合您的应用？

## 继续学习

想要了解有关创建文本生成应用的更多信息？ 转至[进阶学习的页面](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 查找有关此主章节的其他学习资源。

前往第七章，我们将学习[构建聊天应用程序](../../../07-building-chat-applications/translations/cn/README.md?WT.mc_id=academic-105485-koreyst)
