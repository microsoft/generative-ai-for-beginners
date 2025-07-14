<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "ce8224073b86b728ed52b19bed7932fd",
  "translation_date": "2025-07-09T11:46:58+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "zh"
}
-->
# 构建文本生成应用

[![Building Text Generation Applications](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.zh.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(点击上方图片观看本课视频)_

到目前为止，你已经通过本课程了解了核心概念，比如提示词（prompts），甚至还有一个完整的学科叫做“提示词工程”。许多你可以交互的工具，如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你通过提示词来完成任务。

如果你想在应用中添加这样的体验，就需要理解提示词、完成（completions）等概念，并选择一个合适的库来使用。这正是本章要教你的内容。

## 介绍

在本章中，你将：

- 了解 openai 库及其核心概念。
- 使用 openai 构建一个文本生成应用。
- 理解如何使用提示词、温度（temperature）和令牌（tokens）等概念来构建文本生成应用。

## 学习目标

本课结束后，你将能够：

- 解释什么是文本生成应用。
- 使用 openai 构建文本生成应用。
- 配置应用以使用更多或更少的令牌，并调整温度参数，以获得多样化的输出。

## 什么是文本生成应用？

通常，当你构建一个应用时，它会有某种界面，比如：

- 基于命令的。控制台应用是典型的基于命令的应用，你输入命令，应用执行任务。例如，`git` 就是一个基于命令的应用。
- 用户界面（UI）。有些应用有图形用户界面（GUI），你可以点击按钮、输入文本、选择选项等。

### 控制台和 UI 应用的局限性

与基于命令的应用相比，你只能输入特定的命令：

- **受限**。你不能随意输入任何命令，只能输入应用支持的命令。
- **语言特定**。有些应用支持多种语言，但默认情况下应用是为特定语言构建的，即使你可以添加更多语言支持。

### 文本生成应用的优势

那么，文本生成应用有什么不同？

文本生成应用更灵活，不受限于固定命令或特定输入语言。你可以使用自然语言与应用交互。另一个好处是，你正在与一个基于庞大语料库训练的数据源交互，而传统应用可能仅限于数据库中的内容。

### 我能用文本生成应用做什么？

你可以构建很多东西，例如：

- **聊天机器人**。一个回答关于公司及其产品问题的聊天机器人非常合适。
- **助手**。大型语言模型（LLM）擅长总结文本、提取信息、生成简历等文本内容。
- **代码助手**。根据你使用的语言模型，可以构建帮助你写代码的助手。例如，你可以使用 GitHub Copilot 或 ChatGPT 来辅助编程。

## 如何开始？

你需要找到一种方式与大型语言模型（LLM）集成，通常有以下两种方法：

- 使用 API。构造带有提示词的网络请求，获取生成的文本。
- 使用库。库封装了 API 调用，使其更易使用。

## 库/SDK

有几个知名的用于操作 LLM 的库：

- **openai**，这个库让你轻松连接模型并发送提示词。

还有一些更高层次的库：

- **Langchain**。Langchain 很有名，支持 Python。
- **Semantic Kernel**。Semantic Kernel 是微软的库，支持 C#、Python 和 Java。

## 使用 openai 构建第一个应用

让我们看看如何构建第一个应用，需要哪些库，具体步骤等。

### 安装 openai

有很多库可以与 OpenAI 或 Azure OpenAI 交互。支持多种编程语言，如 C#、Python、JavaScript、Java 等。我们选择使用 `openai` Python 库，使用 `pip` 安装。

```bash
pip install openai
```

### 创建资源

你需要完成以下步骤：

- 在 Azure 上创建账户 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 获取 Azure OpenAI 访问权限。访问 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 并申请访问。

  > [!NOTE]
  > 撰写本文时，你需要申请 Azure OpenAI 的访问权限。

- 安装 Python <https://www.python.org/>
- 创建 Azure OpenAI 服务资源。参考此指南了解如何[创建资源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 密钥和端点

此时，你需要告诉 `openai` 库使用哪个 API 密钥。登录 Azure OpenAI 资源的“密钥和端点”部分，复制“密钥 1”的值。

![Azure 门户中的密钥和端点资源页](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

复制好信息后，我们来配置库使用它。

> [!NOTE]
> 建议将 API 密钥与代码分离。可以通过环境变量实现。
>
> - 设置环境变量 `OPENAI_API_KEY` 为你的 API 密钥。
>   `export OPENAI_API_KEY='sk-...'`

### 配置 Azure

如果你使用 Azure OpenAI，配置方法如下：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上面设置了：

- `api_type` 为 `azure`，告诉库使用 Azure OpenAI 而非 OpenAI。
- `api_key`，即你在 Azure 门户找到的 API 密钥。
- `api_version`，你想使用的 API 版本。撰写时最新版本是 `2023-05-15`。
- `api_base`，API 的端点地址，可在 Azure 门户中与你的 API 密钥旁找到。

> [!NOTE] > `os.getenv` 是读取环境变量的函数。你可以用它读取 `OPENAI_API_KEY` 和 `API_BASE` 等环境变量。请在终端或使用类似 `dotenv` 的库设置这些环境变量。

## 生成文本

生成文本的方法是使用 `Completion` 类。示例如下：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

上面代码中，我们创建了一个 completion 对象，传入想用的模型和提示词，然后打印生成的文本。

### 聊天完成

到目前为止，你看到我们用 `Completion` 生成文本。但还有一个更适合聊天机器人的类叫 `ChatCompletion`。示例如下：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

关于此功能将在后续章节详细介绍。

## 练习 - 你的第一个文本生成应用

现在我们学会了如何设置和配置 openai，是时候构建你的第一个文本生成应用了。按以下步骤操作：

1. 创建虚拟环境并安装 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用 Windows，输入 `venv\Scripts\activate`，而不是 `source venv/bin/activate`。

   > [!NOTE]
   > 在 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 搜索 `Open AI`，选择 `Open AI resource`，然后进入 `Keys and Endpoint`，复制 `Key 1`。

1. 创建一个 _app.py_ 文件，写入以下代码：

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
   > 如果使用 Azure OpenAI，需要将 `api_type` 设置为 `azure`，并将 `api_key` 设置为你的 Azure OpenAI 密钥。

   你应该看到类似如下输出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同类型的提示词，适用于不同任务

现在你已经知道如何用提示词生成文本。你甚至有了一个运行中的程序，可以修改它来生成不同类型的文本。

提示词可以用于各种任务，例如：

- **生成某种类型的文本**。比如生成诗歌、测验题目等。
- **查询信息**。你可以用提示词查询信息，比如“CORS 在网页开发中是什么意思？”。
- **生成代码**。你可以用提示词生成代码，比如写一个用于验证邮箱的正则表达式，甚至生成一个完整的程序，如网页应用。

## 更实用的案例：食谱生成器

假设你家里有一些食材，想做点菜。你需要食谱。找食谱的方法可以用搜索引擎，也可以用大型语言模型。

你可以写一个提示词：

> “给我展示5个包含以下食材的菜谱：鸡肉、土豆和胡萝卜。每个菜谱列出所有用到的食材。”

根据这个提示词，你可能会得到类似的回答：

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

这个结果很棒，我知道该做什么了。此时，有些改进可能会很有用：

- 过滤掉我不喜欢或过敏的食材。
- 生成购物清单，以防我家里没有所有食材。

针对上述情况，我们可以添加一个额外的提示词：

> “请去掉含有大蒜的菜谱，因为我过敏，并用其他食材替代。同时，请根据我家已有的鸡肉、土豆和胡萝卜，生成购物清单。”

现在你会得到新的结果：

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

这就是五个不含大蒜的菜谱，同时还有考虑你已有食材的购物清单。

## 练习 - 构建食谱生成器

既然我们演示了一个场景，接下来写代码实现它。按以下步骤操作：

1. 以现有的 _app.py_ 文件为起点
1. 找到 `prompt` 变量，修改为以下内容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   现在运行代码，你应该看到类似输出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，你的 LLM 是非确定性的，每次运行程序可能得到不同结果。

很好，我们来看看如何改进。为了改进，我们希望代码更灵活，能调整食材和菜谱数量。

1. 按如下方式修改代码：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   运行测试代码可能如下：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通过添加过滤和购物清单来改进

我们现在有了一个能生成菜谱的工作应用，且它依赖用户输入，既能调整菜谱数量，也能调整食材。

为了进一步改进，我们想添加：

- **过滤食材**。能过滤掉不喜欢或过敏的食材。为此，我们可以修改现有提示词，在末尾添加过滤条件，如下：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面，我们在提示词末尾添加了 `{filter}`，并从用户处获取过滤条件。

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

  如你所见，含有牛奶的菜谱被过滤掉了。但如果你乳糖不耐受，可能还想过滤奶酪，所以需要明确说明。

- **生成购物清单**。根据已有食材生成购物清单。

  对此功能，我们可以尝试用一个提示词解决，也可以拆成两个提示词。这里我们尝试后者。建议添加一个额外提示词，但为此需要将第一个提示词的结果作为上下文传给第二个提示词。

  找到代码中打印第一个提示词结果的部分，下面添加：

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

  注意：

  1. 我们通过将第一个提示词的结果添加到新提示词中，构造了一个新的提示词：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```
1. 我们发起了一个新的请求，同时也考虑了第一次提示中请求的令牌数量，这次我们将 `max_tokens` 设置为1200。

```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

运行这段代码后，我们得到了以下输出：

```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改进你的设置

到目前为止，我们的代码是可用的，但还有一些调整可以进一步优化。我们应该做的一些事情包括：

- **将密钥与代码分离**，比如 API 密钥。密钥不应该写在代码里，应该存放在安全的位置。为了将密钥与代码分离，我们可以使用环境变量，并借助像 `python-dotenv` 这样的库从文件中加载它们。代码示例如下：

  1. 创建一个 `.env` 文件，内容如下：

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

- **关于令牌长度的说明**。我们需要考虑生成文本所需的令牌数量。令牌是有成本的，所以尽可能节省令牌的使用。例如，我们能否调整提示语，使得使用更少的令牌？

  要更改使用的令牌数，可以使用 `max_tokens` 参数。例如，如果你想使用100个令牌，可以这样写：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **尝试调整 temperature 参数**。temperature 是我们之前没提到但对程序表现很重要的参数。temperature 值越高，输出越随机；值越低，输出越可预测。你可以根据是否需要输出的多样性来决定。

  要调整 temperature，可以使用 `temperature` 参数。例如，如果你想设置 temperature 为0.5，可以这样写：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，越接近1.0，输出越多样化。

## 任务

这次任务你可以自由选择要做什么。

以下是一些建议：

- 调整配方生成器应用，进一步改进它。尝试不同的 temperature 值和提示语，看看能得到什么效果。
- 制作一个“学习伙伴”应用。这个应用可以回答某个主题的问题，比如 Python，你可以设计提示语如“Python 中某个主题是什么？”，或者“给我展示某个主题的代码”等。
- 历史机器人，让历史变得生动。让机器人扮演某个历史人物，向它提问关于其生平和时代的问题。

## 解决方案

### 学习伙伴

下面是一个起始提示，看看你如何使用并调整它以符合你的需求。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 历史机器人

以下是一些你可以使用的提示语：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知识检测

temperature 参数的作用是什么？

1. 它控制输出的随机程度。
1. 它控制响应的长度。
1. 它控制使用的令牌数量。

## 🚀 挑战

在完成任务时，尝试调整 temperature，分别设置为0、0.5和1。记住，0表示最不多样，1表示最多样。哪个值最适合你的应用？

## 干得好！继续学习

完成本课后，查看我们的[生成式 AI 学习合集](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，继续提升你的生成式 AI 知识！

接下来进入第7课，我们将学习如何[构建聊天应用](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。