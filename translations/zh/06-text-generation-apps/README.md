# 构建文本生成应用

[![构建文本生成应用](../../../translated_images/06-lesson-banner.png?WT.2cbccad4fdd538d4f7d47c475b058629b7b7fb1a010acde6e323370d82005b16.zh.mc_id=academic-105485-koreyst)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(点击上方图片查看本课视频)_

通过本课程，你已经了解了一些核心概念，比如提示词，甚至还有一个叫做“提示词工程”的学科。许多工具如 ChatGPT、Office 365、Microsoft Power Platform 等，支持使用提示词来完成任务。

要将这样的体验添加到应用中，你需要理解提示词、完成等概念，并选择一个库来使用。本章将教你如何做到这一点。

## 介绍

在本章中，你将会：

- 了解 openai 库及其核心概念。
- 使用 openai 构建一个文本生成应用。
- 理解如何使用提示词、温度和 tokens 等概念来构建文本生成应用。

## 学习目标

在本课结束时，你将能够：

- 解释什么是文本生成应用。
- 使用 openai 构建一个文本生成应用。
- 配置你的应用，以使用更多或更少的 tokens，并改变温度，以获得多样化的输出。

## 什么是文本生成应用？

通常，当你构建一个应用时，它会有如下某种接口：

- 基于命令的。控制台应用是典型的应用，你输入一个命令，它执行一个任务。例如，`git` 是一个基于命令的应用。
- 用户界面（UI）。有些应用有图形用户界面（GUI），你可以点击按钮、输入文本、选择选项等。

### 控制台和 UI 应用的限制

将其与基于命令的应用进行比较，你输入一个命令：

- **有限制**。你不能输入任何命令，只能输入应用支持的命令。
- **语言特定**。一些应用支持多种语言，但默认情况下，应用是为特定语言构建的，即使你可以添加更多语言支持。

### 文本生成应用的优势

那么，文本生成应用有什么不同？

在文本生成应用中，你有更多的灵活性，不受限于一组命令或特定的输入语言。相反，你可以使用自然语言与应用互动。另一个好处是，你已经在与一个经过大量信息训练的数据源互动，而传统应用可能仅限于数据库中的内容。

### 我可以用文本生成应用构建什么？

你可以构建很多东西。例如：

- **聊天机器人**。一个聊天机器人可以回答关于主题的问题，比如你的公司及其产品。
- **助手**。LLM 在总结文本、从文本中获取见解、生成简历等文本方面表现出色。
- **代码助手**。根据你使用的语言模型，你可以构建一个帮助你编写代码的代码助手。例如，你可以使用 GitHub Copilot 或 ChatGPT 帮助你编写代码。

## 我该如何开始？

好吧，你需要找到一种方式与 LLM 集成，通常涉及以下两种方法：

- 使用 API。在这里，你构建网络请求，带上你的提示词并获得生成的文本。
- 使用库。库帮助封装 API 调用，使其更易于使用。

## 库/SDK

有一些知名的库用于处理 LLM，例如：

- **openai**，这个库使得连接到你的模型并发送提示词变得容易。

然后还有一些在更高层次上操作的库，比如：

- **Langchain**。Langchain 以支持 Python 而闻名。
- **Semantic Kernel**。Semantic Kernel 是微软的一个库，支持 C#、Python 和 Java 语言。

## 使用 openai 构建第一个应用

让我们看看如何构建我们的第一个应用，所需的库有哪些，以及需要多少工作量。

### 安装 openai

市面上有很多库可以与 OpenAI 或 Azure OpenAI 交互。可以使用多种编程语言，如 C#、Python、JavaScript、Java 等。我们选择使用 `openai` Python 库，因此我们将使用 `pip` 来安装它。

```bash
pip install openai
```

### 创建资源

你需要执行以下步骤：

- 在 Azure 上创建一个账户 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 获取 Azure OpenAI 的访问权限。访问 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 并申请访问权限。

  > [!NOTE]
  > 在撰写本文时，你需要申请 Azure OpenAI 的访问权限。

- 安装 Python <https://www.python.org/>
- 创建一个 Azure OpenAI 服务资源。参见此指南以了解如何 [创建资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 密钥和端点

此时，你需要告诉 `openai` 库使用哪个 API 密钥。要找到你的 API 密钥，请转到 Azure OpenAI 资源的“密钥和端点”部分并复制“密钥 1”值。

![Azure 门户中的密钥和端点资源页面](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

现在你已经复制了这些信息，让我们指示库使用它。

> [!NOTE]
> 将 API 密钥与代码分离是值得的。你可以通过使用环境变量来实现。
>
> - 设置环境变量 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### 配置 Azure

如果你使用的是 Azure OpenAI，以下是设置配置的方法：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上面我们设置了以下内容：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` 类。以下是一个示例：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上面的代码中，我们创建了一个 completion 对象，并传入了我们想要使用的模型和提示词。然后我们打印生成的文本。

### 聊天完成

到目前为止，你已经看到了我们如何使用 `Completion` to generate text. But there's another class called `ChatCompletion` 更适合聊天机器人的方法。以下是使用它的示例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

关于此功能的更多内容将在后续章节中介绍。

## 练习 - 你的第一个文本生成应用

现在我们已经了解了如何设置和配置 openai，是时候构建你的第一个文本生成应用了。要构建你的应用，请按以下步骤操作：

1. 创建一个虚拟环境并安装 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用的是 Windows，请输入 `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` 值。

1. 创建一个 _app.py_ 文件，并给它如下代码：

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
   completion = client.chat.completions.create(model=deployment, messages=messages)

   # print response
   print(completion.choices[0].message.content)
   ```

   > [!NOTE]
   > 如果你使用的是 Azure OpenAI，你需要将 `api_type` to `azure` and set the `api_key` 设置为你的 Azure OpenAI 密钥。

   你应该会看到如下输出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同类型的提示词，用于不同的事情

现在你已经看到了如何使用提示词生成文本。你甚至已经有一个可以运行的程序，可以修改和更改以生成不同类型的文本。

提示词可以用于各种任务。例如：

- **生成某种类型的文本**。例如，你可以生成一首诗、一个测验的问题等。
- **查找信息**。你可以使用提示词查找信息，比如以下示例“在 web 开发中 CORS 是什么意思？”。
- **生成代码**。你可以使用提示词生成代码，例如开发用于验证电子邮件的正则表达式，或者为什么不生成一个完整的程序，比如一个 web 应用？

## 一个更实际的用例：食谱生成器

想象一下你家里有一些食材，你想做点什么。为此，你需要一个食谱。找到食谱的一种方法是使用搜索引擎，或者你可以使用 LLM 来做到这一点。

你可以这样写一个提示词：

> "展示 5 个包含以下食材的菜肴食谱：鸡肉、土豆和胡萝卜。每个食谱列出使用的所有食材"

给出上述提示词，你可能会得到类似这样的回应：

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

这个结果很棒，我知道该做什么菜了。此时，有用的改进可能是：

- 过滤掉我不喜欢或过敏的食材。
- 生成购物清单，以防我家里没有所有食材。

对于上述情况，让我们添加一个额外的提示词：

> "请去掉含有大蒜的食谱，因为我过敏，并用其他东西代替。另外，请根据我已经有的鸡肉、土豆和胡萝卜生成购物清单。"

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

这是你的五个食谱，没有提到大蒜，你还有一个购物清单，考虑到了你家里已经有的食材。

## 练习 - 构建一个食谱生成器

现在我们已经演示了一个场景，让我们编写代码来匹配这个场景。要做到这一点，请按以下步骤操作：

1. 使用现有的 _app.py_ 文件作为起点
1. 找到 `prompt` 变量并将其代码更改为以下内容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果你现在运行代码，你应该会看到类似的输出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非确定性的，因此每次运行程序时，你可能会得到不同的结果。

   很好，让我们看看如何改进。为了改进，我们希望确保代码是灵活的，以便食材和食谱数量可以改进和更改。

1. 让我们通过以下方式更改代码：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   运行代码的测试可能如下所示：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通过添加过滤器和购物清单进行改进

我们现在有一个可以生成食谱的工作应用，并且它是灵活的，因为它依赖于用户的输入，无论是食谱数量还是使用的食材。

为了进一步改进，我们希望添加以下内容：

- **过滤掉食材**。我们希望能够过滤掉我们不喜欢或过敏的食材。为了实现这一更改，我们可以编辑现有的提示词，并在其末尾添加一个过滤条件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面，我们在提示词末尾添加了 `{filter}`，我们还从用户那里获取了过滤值。

  运行程序的示例输入现在可能如下所示：

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

  如你所见，任何含有牛奶的食谱都被过滤掉了。但是，如果你对乳糖不耐受，你可能还想过滤掉含有奶酪的食谱，因此需要明确说明。

- **生成购物清单**。我们希望生成购物清单，考虑到我们家里已经有的东西。

  对于此功能，我们可以尝试在一个提示词中解决所有问题，也可以将其拆分为两个提示词。让我们尝试后者。在这里，我们建议添加一个额外的提示词，但为了使其工作，我们需要将第一个提示词的结果作为上下文添加到后一个提示词中。

  找到代码中打印第一个提示词结果的部分，并在其下方添加以下代码：

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

  1. 我们通过将第一个提示词的结果添加到新提示词中来构建一个新提示词：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我们发出一个新的请求，但也考虑到我们在第一个提示词中请求的 tokens 数量，因此这次我们说 `max_tokens` 是 1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     运行这段代码后，我们现在得到了以下输出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善你的设置

到目前为止，我们的代码是可以工作的，但我们应该进行一些调整以进一步改进。我们应该做的一些事情是：

- **将密钥与代码分开**，比如 API 密钥。密钥不应该存在于代码中，而应该存储在安全的位置。要将密钥与代码分开，我们可以使用环境变量和库，如 `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` 文件，内容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，对于 Azure，你需要设置以下环境变量：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在代码中，你可以这样加载环境变量：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **关于 token 长度的建议**。我们应该考虑生成所需文本的 token 数量。tokens 是有成本的，因此在可能的情况下，我们应该尝试节省 tokens 的使用。例如，我们可以重新措辞提示词，以便使用更少的 tokens 吗？

  要更改使用的 tokens，你可以使用 `max_tokens` 参数。例如，如果你想使用 100 个 tokens，你可以这样做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **尝试改变温度**。温度是我们尚未提到的重要概念，但对程序的表现很重要。温度值越高，输出就越随机。相反，温度值越低，输出就越可预测。考虑你是否希望输出有变化。

  要改变温度，你可以使用 `temperature` 参数。例如，如果你想使用 0.5 的温度，你可以这样做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，温度越接近 1.0，输出就越多样化。

## 作业

对于这次作业，你可以选择构建什么。

这里有一些建议：

- 调整食谱生成器应用以进一步改进。尝试不同的温度值和提示词，看看你能得到什么。
- 构建一个“学习伙伴”。这个应用应该能够回答关于某个主题的问题，例如 Python，你可以有类似“Python 中某个主题是什么？”的提示词，或者你可以有一个提示词，要求展示某个主题的代码等。
- 历史机器人，让历史变得生动，指示机器人扮演某个历史人物并询问其生活和时代的问题。

## 解决方案

### 学习伙伴

以下是一个初始提示词，看看你如何使用它并根据需要进行调整。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 历史机器人

以下是你可以使用的一些提示词：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知识检查

温度概念的作用是什么？

1. 它控制输出的随机性。
1. 它控制响应的大小。
1. 它控制使用的 tokens 数量。

## 🚀 挑战

在完成作业时，尝试改变温度，尝试将其设置为 0、0.5 和 1。记住，0 是变化最小的，1 是变化最大的，哪个值最适合你的应用？

## 出色的工作！继续学习

完成本课后，查看我们的 [生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst) 以继续提升你的生成式 AI 知识！

前往第 7 课，我们将研究如何 [构建聊天应用](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：
本文件是使用基于机器的人工智能翻译服务翻译的。尽管我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。应将原始语言的文件视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担责任。