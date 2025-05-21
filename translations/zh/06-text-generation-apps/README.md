<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T10:04:48+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "zh"
}
-->
# 构建文本生成应用程序

[![构建文本生成应用程序](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.zh.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(点击上方图片观看本课视频)_

在这门课程中，您已经看到了一些核心概念，比如提示以及一个被称为“提示工程”的学科。许多您可以与之互动的工具，如ChatGPT、Office 365、Microsoft Power Platform等，支持您使用提示来实现某些目标。

要将这种体验添加到应用程序中，您需要理解提示、完成等概念，并选择一个库进行工作。这正是您将在本章中学习的内容。

## 简介

在本章中，您将：

- 了解openai库及其核心概念。
- 使用openai构建一个文本生成应用程序。
- 理解如何使用提示、温度和令牌等概念来构建文本生成应用程序。

## 学习目标

在本课结束时，您将能够：

- 解释什么是文本生成应用程序。
- 使用openai构建文本生成应用程序。
- 配置您的应用程序以使用更多或更少的令牌，并改变温度，以获得不同的输出。

## 什么是文本生成应用程序？

通常，当您构建一个应用程序时，它具有某种界面，如下所示：

- 基于命令。控制台应用程序是典型的应用程序，您输入命令，它执行任务。例如，`git` 是一个基于命令的应用程序。
- 用户界面 (UI)。一些应用程序具有图形用户界面 (GUI)，您可以点击按钮、输入文本、选择选项等。

### 控制台和UI应用程序的局限性

与基于命令的应用程序相比，您输入命令：

- **有限制**。您不能随意输入任何命令，只能输入应用程序支持的命令。
- **语言特定**。一些应用程序支持多种语言，但默认情况下，应用程序是为特定语言构建的，即使您可以添加更多语言支持。

### 文本生成应用程序的优势

那么文本生成应用程序有什么不同呢？

在文本生成应用程序中，您有更多的灵活性，不受限于一组命令或特定的输入语言。相反，您可以使用自然语言与应用程序交互。另一个好处是，由于您已经在与一个经过大量信息训练的数据源交互，而传统应用程序可能仅限于数据库中的内容。

### 我可以用文本生成应用程序构建什么？

您可以构建很多东西。例如：

- **聊天机器人**。聊天机器人回答关于主题的问题，比如您的公司及其产品可能是一个很好的匹配。
- **助手**。LLMs在总结文本、从文本中获取洞察、生成简历等文本方面非常出色。
- **代码助手**。根据您使用的语言模型，您可以构建一个代码助手来帮助您编写代码。例如，您可以使用GitHub Copilot以及ChatGPT等产品来帮助您编写代码。

## 我如何开始？

您需要找到一种方法来集成LLM，这通常涉及以下两种方法：

- 使用API。在这里，您构建网络请求，带有您的提示，并获取生成的文本。
- 使用库。库帮助封装API调用，使其更易于使用。

## 库/SDK

有一些众所周知的库可以用于处理LLMs，比如：

- **openai**，这个库使您可以轻松连接到您的模型并发送提示。

然后还有一些操作在更高层次的库，比如：

- **Langchain**。Langchain非常知名，支持Python。
- **Semantic Kernel**。Semantic Kernel是Microsoft提供的一个库，支持C#、Python和Java语言。

## 使用openai构建第一个应用程序

让我们看看如何构建我们的第一个应用程序，我们需要哪些库，需要多少等。

### 安装openai

有很多库可以与OpenAI或Azure OpenAI进行交互。可以使用多种编程语言，比如C#、Python、JavaScript、Java等。我们选择使用`openai` Python库，因此我们将使用`pip`来安装它。

```bash
pip install openai
```

### 创建资源

您需要执行以下步骤：

- 在Azure上创建一个帐户 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 获取Azure OpenAI的访问权限。访问 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 并申请访问。

  > [!NOTE]
  > 在撰写本文时，您需要申请访问Azure OpenAI。

- 安装Python <https://www.python.org/>
- 创建一个Azure OpenAI服务资源。请参阅此指南了解如何[创建资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 查找API密钥和终端

此时，您需要告诉您的`openai`库使用哪个API密钥。要查找您的API密钥，请转到您的Azure OpenAI资源的“密钥和终端”部分，并复制“密钥1”的值。

![Azure门户中的密钥和终端资源面板](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

现在您已经复制了这些信息，让我们指示库使用它。

> [!NOTE]
> 将API密钥与代码分离是值得的。您可以通过使用环境变量来实现。
>
> - 设置环境变量 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### 设置Azure配置

如果您使用的是Azure OpenAI，以下是设置配置的方法：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上述代码中，我们设置了以下内容：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion`类。以下是一个示例：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上面的代码中，我们创建了一个完成对象，并传入我们想使用的模型和提示。然后我们打印生成的文本。

### 聊天完成

到目前为止，您已经看到我们一直在使用`Completion` to generate text. But there's another class called `ChatCompletion`，它更适合聊天机器人。以下是一个使用它的示例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多关于此功能的信息将在即将到来的章节中介绍。

## 练习 - 您的第一个文本生成应用程序

现在我们已经学习了如何设置和配置openai，是时候构建您的第一个文本生成应用程序了。要构建您的应用程序，请按照以下步骤：

1. 创建一个虚拟环境并安装openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果您使用的是Windows，请输入`venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1`值。

1. 创建一个_app.py_文件并给它以下代码：

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
   > 如果您使用的是Azure OpenAI，您需要将`api_type` to `azure` and set the `api_key`设置为您的Azure OpenAI密钥。

   您应该看到如下输出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同类型的提示，用于不同的事情

现在您已经看到如何使用提示生成文本。您甚至有一个程序正在运行，您可以修改和更改以生成不同类型的文本。

提示可以用于各种任务。例如：

- **生成一种类型的文本**。例如，您可以生成一首诗、测验问题等。
- **查找信息**。您可以使用提示来查找信息，比如以下示例“在网络开发中CORS是什么意思？”。
- **生成代码**。您可以使用提示生成代码，例如开发用于验证电子邮件的正则表达式，或者为什么不生成整个程序，比如一个网络应用程序？

## 更实用的用例：食谱生成器

想象一下，您在家里有一些食材，您想做点东西。为此，您需要一个食谱。找到食谱的方法是使用搜索引擎，或者您可以使用LLM来完成。

您可以编写一个这样的提示：

> “给我展示5个包含以下食材的菜肴食谱：鸡肉、土豆和胡萝卜。每个食谱列出所有使用的食材。”

根据上述提示，您可能会得到类似的响应：

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

这个结果很好，我知道该做什么。在这个时候，有用的改进可能是：

- 过滤掉我不喜欢或过敏的食材。
- 生成购物清单，以防我家里没有所有的食材。

对于上述情况，让我们添加一个额外的提示：

> “请移除含有大蒜的食谱，因为我过敏，并用其他东西代替。此外，请为这些食谱生成一个购物清单，考虑到我家里已经有鸡肉、土豆和胡萝卜。”

现在您有了新的结果，即：

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

这是您的五个食谱，没有提到大蒜，并且您还根据家里已有的食材生成了一个购物清单。

## 练习 - 构建食谱生成器

现在我们已经演示了一个场景，让我们编写代码来匹配演示的场景。为此，请按照以下步骤：

1. 使用现有的_app.py_文件作为起点
1. 找到`prompt`变量并将其代码更改为以下内容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果您现在运行代码，您应该看到类似的输出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，您的LLM是非确定性的，因此每次运行程序时可能会得到不同的结果。

   很好，让我们看看如何改进。为了改进，我们希望确保代码是灵活的，因此食材和食谱数量可以改进和更改。

1. 让我们以以下方式更改代码：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   测试代码可能看起来像这样：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通过添加过滤器和购物清单来改进

我们现在有一个能够生成食谱的工作应用程序，它是灵活的，因为它依赖于用户输入，无论是食谱数量还是使用的食材。

为了进一步改进，我们希望添加以下内容：

- **过滤掉食材**。我们希望能够过滤掉我们不喜欢或过敏的食材。要实现此更改，我们可以编辑现有的提示并在末尾添加一个过滤条件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面，我们在提示末尾添加了`{filter}`，并且我们还从用户那里获取过滤器值。

  现在运行程序的示例输入可能看起来像这样：

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

  如您所见，任何含有牛奶的食谱都被过滤掉了。但是，如果您对乳糖不耐受，您可能还希望过滤掉含有奶酪的食谱，因此需要明确说明。

- **生成购物清单**。我们希望生成购物清单，考虑到我们家里已经有的食材。

  对于此功能，我们可以尝试在一个提示中解决所有问题，也可以将其分为两个提示。让我们尝试后者方法。在这里，我们建议添加一个额外的提示，但为了使其工作，我们需要将第一个提示的结果作为上下文添加到第二个提示中。

  找到代码中打印第一个提示结果的部分，并在下面添加以下代码：

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

  请注意以下几点：

  1. 我们通过将第一个提示的结果添加到新提示中来构建一个新提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我们进行新的请求，但也考虑到我们在第一个提示中请求的令牌数量，因此这次我们说`max_tokens`是1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     运行此代码，我们现在得到以下输出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善您的设置

到目前为止，我们的代码是有效的，但有一些调整我们应该进行以进一步改进。一些我们应该做的事情是：

- **将秘密与代码分离**，例如API密钥。秘密不属于代码中，应该存储在安全的位置。要将秘密与代码分离，我们可以使用环境变量和库，比如`python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env`文件，内容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，对于Azure，您需要设置以下环境变量：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在代码中，您可以这样加载环境变量：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **关于令牌长度的说明**。我们应该考虑生成我们想要的文本需要多少令牌。令牌是有成本的，因此在可能的情况下，我们应该尝试节省使用的令牌数量。例如，我们可以重新措辞提示以便使用更少的令牌吗？

  要更改使用的令牌，您可以使用`max_tokens`参数。例如，如果您想使用100个令牌，您可以这样做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **尝试温度**。温度是我们到目前为止没有提到的，但对于我们的程序表现非常重要。温度值越高，输出越随机。相反，温度值越低，输出越可预测。考虑您是否希望输出有所变化。

  要改变温度，您可以使用`temperature`参数。例如，如果您想使用0.5的温度，您可以这样做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，越接近1.0，输出越多样化。

## 作业

对于这个作业，您可以选择构建什么。

以下是一些建议：

- 调整食谱生成器应用程序以进一步改进。尝试不同的温度值，和提示，看看您能做些什么。
- 构建一个“学习伙伴”。这个应用程序应该能够回答关于某个主题的问题，例如Python，您可以有这样的提示“Python中的某个主题是什么？”，或者您可以有一个提示，显示某个主题的代码等。
- 历史机器人，让历史变得生动，指示机器人扮演某个历史角色，并询问它关于其生活和时代的问题。

## 解决方案

### 学习伙伴

以下是一个起始提示，看看您如何使用它并根据自己的喜好进行调整。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 历史机器人

以下是一些您可以使用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知识检查

温度概念的作用是什么？

1. 它控制输出的随机性。
1. 它控制响应的大小。
1. 它控制使用的令牌数量。

## 🚀 挑战

在完成作业时，尝试改变温度，尝试设置为0、0.5和1。记住0是变化最小的，1是变化最大的，哪个值最适合您的应用程序？

## 很棒的工作！继续您的学习

完成本课后，请查看我们的[生成式AI学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升您的生成式AI知识！

前往第7课，我们将探讨如何[构建聊天应用程序](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：
本文档已使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文档视为权威来源。对于关键信息，建议进行专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们不承担责任。