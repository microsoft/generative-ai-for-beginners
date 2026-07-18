# 构建文本生成应用程序

[![构建文本生成应用程序](../../../translated_images/zh-CN/06-lesson-banner.a5c629f990a636c8.webp)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(点击上方图片观看本课视频)_

你已经通过本课程了解到，有核心概念如提示词（prompts）甚至有一整门学科叫做“提示词工程”。许多你可以交互使用的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你通过提示词来完成某些操作。

如果你想给一个应用程序添加这种体验，你需要理解提示词、补全等概念，并选择一个库来使用。这正是你将在本章学习的内容。

## 介绍

在本章中，你将：

- 了解 openai 库及其核心概念。
- 使用 openai 构建文本生成应用。
- 理解如何使用提示词、温度和令牌等概念来构建文本生成应用。

## 学习目标

本课结束后，你将能够：

- 解释什么是文本生成应用。
- 使用 openai 构建文本生成应用。
- 配置你的应用以使用更多或更少的令牌，并且调整温度参数，以获得不同风格的输出。

## 什么是文本生成应用？

通常，当你构建一个应用时，它会有某种界面，比如以下类型：

- 基于命令的。控制台应用是典型的基于命令的程序，你输入一个命令，它执行某个任务。例如，`git` 就是一个基于命令的应用。
- 用户界面（UI）。一些应用有图形用户界面（GUI），你可以点击按钮、输入文本、选择选项等。

### 控制台和 UI 应用是有限制的

比较你在基于命令的应用中输入命令时的情况：

- <strong>有限制</strong>。你不能随便输入任何命令，只能输入应用支持的命令。
- <strong>语言特定</strong>。一些应用支持多种语言，但默认是为某一种语言构建的，尽管你可以添加更多语言支持。

### 文本生成应用的优势

那么，文本生成应用有什么不同？

在文本生成应用中，你有更多灵活性，不受限于一套命令或特定输入语言。你可以使用自然语言与应用交互。另一个优点是，你实际上是在与一个在庞大语料库上训练过的数据源交互，而传统应用可能受限于数据库中的内容。

### 我可以用文本生成应用构建什么？

你可以构建许多东西。例如：

- <strong>聊天机器人</strong>。一个回答有关主题的问题的聊天机器人，比如你的公司及其产品，可能非常合适。
- <strong>辅助工具</strong>。大型语言模型（LLM）非常擅长诸如总结文本、从文本中获取洞察、生成简历等文本生成任务。
- <strong>代码助手</strong>。根据你使用的语言模型，你可以构建一个帮助编写代码的助手。例如，你可以使用 GitHub Copilot 或 ChatGPT 来帮助写代码。

## 如何开始？

你需要找到一种方式集成大型语言模型，通常有以下两种方法：

- 使用 API。在这里，你构造带有提示词的 Web 请求，并获取生成的文本。
- 使用库。库封装了 API 调用，让它们更易于使用。

## 库 / SDK

有几个知名的用于操作大型语言模型的库，例如：

- **openai**，该库让你轻松连接到模型并发送提示词。

还有一些在更高层次上操作的库，如：

- **Langchain**。Langchain 非常著名，支持 Python。
- **Semantic Kernel**。Semantic Kernel 是微软开发的库，支持 C#、Python 和 Java 语言。

## 使用 openai 构建第一个应用

让我们看看如何构建第一个应用，所需库、步骤等。

### 安装 openai

目前有很多与 OpenAI 或 Azure OpenAI 交互的库。你也可以使用多种编程语言，如 C#、Python、JavaScript、Java 等。我们选择使用 `openai` Python 库，因此使用 `pip` 安装它。

```bash
pip install openai
```

### 创建资源

你需要执行以下步骤：

- 在 Azure 上创建账户 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 获取 Azure OpenAI 访问权限。访问 [https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-foundry/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 并申请访问权限。

  > [!NOTE]
  > 撰写本文时，需要申请 Azure OpenAI 的访问权限。

- 安装 Python <https://www.python.org/>
- 已创建 Azure OpenAI 服务资源。参见本指南中如何[创建资源](https://learn.microsoft.com/azure/ai-foundry/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 密钥和端点

现在，你需要告诉 `openai` 库使用哪个 API 密钥。要找到你的 API 密钥，进入你的 Azure OpenAI 资源的“密钥和端点”部分，复制“Key 1”的值。

![Azure 门户中“密钥和端点”资源视图](https://learn.microsoft.com/azure/ai-foundry/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

有了这些信息后，让我们指示库去使用它。

> [!NOTE]
> 建议将 API 密钥与代码分离。可通过环境变量实现。
>
> - 将环境变量 `OPENAI_API_KEY` 设为你的 API 密钥。
>   `export OPENAI_API_KEY='sk-...'`

### Azure 配置设置

如果你使用 Azure OpenAI（现为 Microsoft Foundry 一部分），配置如下。我们使用标准 `OpenAI` 客户端，指向 Azure OpenAI 的 `/openai/v1/` 端点，它兼容 Responses API，无需 `api_version`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)
```

上面我们设置了：

- `api_key`，即你在 Azure 门户或 Microsoft Foundry 门户找到的 API 密钥。
- `base_url`，这是你的 Foundry 资源端点，后面追加 `/openai/v1/`。稳定的 v1 端点适用于 OpenAI 和 Azure OpenAI，无需管理 `api_version`。

> [!NOTE] > `os.environ` 读取环境变量。你可以用它读取如 `AZURE_OPENAI_API_KEY` 和 `AZURE_OPENAI_ENDPOINT` 等环境变量。在终端设置这些变量，或借助 `dotenv` 之类的库来设置。

## 生成文本

生成文本的方法是使用 Responses API 的 `responses.create` 方法。示例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

response = client.responses.create(
    model="gpt-5-mini",  # 这是您的模型部署名称
    input=prompt,
    store=False,
)
print(response.output_text)
```

在上面的代码中，我们创建了一个响应，传入想用的模型和提示词。然后通过 `response.output_text` 打印生成的文本。

### 多轮对话

Responses API 既适合单轮文本生成，也适合多轮聊天机器人——你通过在 `input` 中提供消息列表构建对话：

```python
from openai import OpenAI

client = OpenAI(api_key="sk-...")

response = client.responses.create(model="gpt-5-mini", input="Hello world", store=False)
print(response.output_text)
```

更多该功能详解将在后续章节介绍。

## 练习 - 你的第一个文本生成应用

现在我们学会了如何设置和配置 openai，是时候构建你的第一个文本生成应用。步骤如下：

1. 创建虚拟环境并安装 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你用的是 Windows，请输入 `venv\Scripts\activate`，而不是 `source venv/bin/activate`。

   > [!NOTE]
   > 访问 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst)，搜索 `Open AI`，选择 `Open AI 资源`，然后选择 `密钥和端点`，复制 `Key 1` 的值。

1. 创建一个 _app.py_ 文件，并写入以下代码：

   ```python
   import os
   from openai import OpenAI

   client = OpenAI(
       api_key="<replace this value with your Azure OpenAI key>",
       base_url="<endpoint found in Azure Portal>/openai/v1/",
   )
   deployment_name = "<deployment name>"

   # 添加你的完成代码
   prompt = "Complete the following: Once upon a time there was a"

   # 使用 Responses API 进行请求
   response = client.responses.create(model=deployment_name, input=prompt, store=False)

   # 打印响应
   print(response.output_text)
   ```

   > [!NOTE]
   > 如果你使用的是纯 OpenAI（非 Azure），请使用 `client = OpenAI(api_key="<用你的 OpenAI key 替换此值>")`（无 `base_url`），并传入模型名，如 `gpt-5-mini`，而非部署名称。

   你应该会看到如下输出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同类型的提示词，用于不同任务

现在你已经看到如何用提示词生成文本。你甚至有了一个运行中的程序，可以修改它来生成不同类型的文本。

提示词可以用于各种任务。例如：

- <strong>生成某种文本</strong>。例如，你可以生成诗歌、测验问题等。
- <strong>查询信息</strong>。你可以用提示词查找信息，比如示例中的“在网页开发中 CORS 是什么意思？”。
- <strong>生成代码</strong>。你可以用提示词生成代码，比如开发用于验证电子邮件的正则表达式，甚至生成整个程序，如 Web 应用。

## 更实用的用例：食谱生成器

假设你家里有一些食材，想做点菜。这个时候你需要菜谱。一种找菜谱的方式是用搜索引擎，当然你也可以用大型语言模型实现。

你可能写出如下的提示词：

> “请给我展示5个用以下食材做的菜谱：鸡肉、土豆和胡萝卜。每个菜谱列出所有所用食材。”

给出上面提示词，可能得到类似反馈：

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

这个结果很棒，我知道该做什么了。接下来，有几个可能的改进：

- 过滤掉我不喜欢或过敏的食材。
- 生成购物清单，以防我家里没有所有食材。

针对以上情况，让我们添加额外提示：

> “请移除含有大蒜的菜谱，我对大蒜过敏，替换成其它食材。另外，请考虑我家已有鸡肉、土豆和胡萝卜，帮我生成购物清单。”

现在你会得到一个新结果，就是：

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

这就是你的五个菜谱，没有提到大蒜，并且考虑你已有食材生成了购物清单。

## 练习 - 构建食谱生成器

既然我们演示了一个场景，接下来写代码实现匹配的功能。步骤如下：

1. 使用已有的 _app.py_ 文件作为起点
1. 找到 `prompt` 变量，修改它的代码为如下：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果现在运行代码，应该看到类似输出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 提示，你的 LLM 是非确定性的，可能每次运行结果不同。

   很好，现在看看怎么改进。我们希望代码更灵活，让食材和菜谱数量都可以调整。

1. 按如下方式修改代码：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # 将食谱数量插入到提示和配料中
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   测试用例代码示例如下：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 添加过滤和购物清单功能以改进

我们现在有了一个能做菜谱的应用，并且它灵活依赖用户输入，包括菜谱数量和使用的食材。

为进一步改进，我们想添加：

- <strong>过滤掉食材</strong>。我们希望能过滤掉不喜欢或过敏的食材。为此，我们可以编辑提示词，在末尾添加过滤条件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  以上，我们在提示词末尾加了 `{filter}`，同时从用户那里捕获过滤条件。

  运行程序的示例输入可能是：

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

  如你所见，带有牛奶的菜谱被过滤掉了。但如果你乳糖不耐，你可能还想过滤含奶酪的菜谱，因此需要明确。


- <strong>制作购物清单</strong>。我们想要制作一个购物清单，考虑到我们家里已经有什么。

  对于这个功能，我们可以尝试用一个提示解决所有问题，也可以把它分成两个提示。我们试试后一种方法。这里我们建议添加一个额外的提示，但要做到这一点，我们需要将前一个提示的结果作为上下文添加到后一个提示中。

  找到代码中打印第一个提示结果的部分，并在其下添加以下代码：

  ```python
  old_prompt_result = response.output_text
  prompt = "Produce a shopping list for the generated recipes and please don't include ingredients that I already have."

  new_prompt = f"{old_prompt_result} {prompt}"
  response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)

  # 打印响应
  print("Shopping list:")
  print(response.output_text)
  ```

  注意以下几点：

  1. 我们通过将第一个提示的结果添加到新提示中来构建一个新提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我们发起一个新的请求，同时考虑到我们在第一个提示中请求的令牌数，这次我们将 `max_output_tokens` 设置为 1200。

     ```python
     response = client.responses.create(model=deployment_name, input=new_prompt, max_output_tokens=1200, store=False)
     ```

     运行这段代码后，我们得到以下输出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改进您的设置

目前为止我们有的代码是可用的，但我们应该进行一些调整以进一步改进。有些事情我们应该做的是：

- <strong>将密钥与代码分离</strong>，比如 API 密钥。密钥不应该存放在代码中，应保存在安全的位置。为了将密钥与代码分离，我们可以使用环境变量和像 `python-dotenv` 这样的库从文件中加载密钥。代码示例如下：

  1. 创建一个内容如下的 `.env` 文件：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，对于 Microsoft Foundry 中的 Azure OpenAI，您需要设置以下环境变量：

     ```bash
     AZURE_OPENAI_API_KEY=<replace>
     AZURE_OPENAI_ENDPOINT=<replace>
     AZURE_OPENAI_API_VERSION=2024-10-21
     ```

     在代码中，您可以这样加载环境变量：

     ```python
     import os
     from dotenv import load_dotenv
     from openai import OpenAI

     load_dotenv()

     client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
     ```

- <strong>关于令牌长度的一句话</strong>。我们需要考虑生成所需文本需要多少令牌。令牌是收费的，因此尽量经济使用令牌。例如，是否能优化提示，以减少令牌数量？

  要更改使用的令牌数，可以使用 `max_output_tokens` 参数。例如，如果想用 100 个令牌，可以这样：

  ```python
  response = client.responses.create(model=deployment, input=prompt, max_output_tokens=100, store=False)
  ```

- **试验 temperature 参数**。temperature 是我们到目前为止还没提过但却是影响程序表现的重要参数。temperature 值越高，输出越随机；temperature 值越低，输出越可预测。考虑您是否需要输出多样性。

  要调整 temperature，可以使用 `temperature` 参数。例如，如果想用 0.5 的温度，可以这样：

  ```python
  response = client.responses.create(model=deployment, input=prompt, temperature=0.5, store=False)
  ```

  > 注意，越接近 1.0，输出越多样化。

- **推理模型不使用 `temperature`<strong>。这是 2026 年的重要转变。Microsoft Foundry 上当前未废弃的模型是</strong>推理模型<strong>（GPT-5 系列，o 系列），它们</strong>不支持 `temperature` 或 `top_p`**（也不支持 `max_tokens`；使用 `max_output_tokens`）。如果给 `gpt-5-mini` 发送 `temperature`，会收到“参数不支持”的错误。要尝试上面的 temperature 例子，请指向仍支持采样控制的模型——例如开源 **Llama** 模型，如来自 [Microsoft Foundry 模型目录](https://ai.azure.com/catalog/models?WT.mc_id=academic-105485-koreyst) 的 `Llama-3.3-70B-Instruct`，通过 Foundry Models / Azure AI Inference 端点调用（和 `githubmodels-*` 示例的调用方式相同）。对于 GPT-5 等推理模型，输出控制方式不同：
  - <strong>提示工程</strong> - 清晰的指令、示例和结构化输出（参见课程 [04 - Prompt Engineering](../04-prompt-engineering-fundamentals/README.md?WT.mc_id=academic-105485-koreyst)）取代了采样调节器的工作。
  - <strong>推理控制</strong> - 参数如推理努力/详细程度权衡推理深度与延迟和成本。

  总结：`temperature`/`top_p` 在很多模型（Llama、Mistral、Phi 和 GPT-4.x 系列——尽管 GPT-4.x 正在废弃）仍然有效，但趋势是在 GPT-5 这样的推理模型上使用提示工程和推理控制。

## 任务

在这个任务中，您可以自由选择要构建的内容。

这些是一些建议：

- 调整配方生成器应用以进一步改进。尝试不同的 temperature 值和提示，看看能做出什么新花样。
- 构建“学习伙伴”应用。该应用能够回答某个主题的问题，例如 Python，可以有类似“Python 中某个主题是什么？”的提示，也可以有“给我展示某个主题的代码”等提示。
- 历史机器人，让历史栩栩如生，指示机器人扮演某个历史人物，向它提问关于其生平和时代的问题。

## 解决方案

### 学习伙伴

下面是一个起始提示，看看您如何使用并调整它以适合您的需求。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 历史机器人

这些是您可以使用的一些提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知识检测

temperature 参数的作用是什么？

1. 它控制输出的随机程度。
1. 它控制响应的大小。
1. 它控制使用的令牌数量。

## 🚀 挑战

在完成任务时，尝试改变 temperature，尝试设置为 0、0.5 和 1。记住 0 表示变化最少，1 表示变化最多。什么值对您的应用效果最好？

## 做得好！继续学习

完成本课后，请查看我们的 [生成式 AI 学习集合](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式 AI 知识！

前往第七课，我们将学习如何[构建聊天应用](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免责声明**：
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译完成。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言版文件应视为权威来源。对于重要信息，建议使用专业人工翻译。我们对因使用本翻译而产生的任何误解或误释不承担责任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->