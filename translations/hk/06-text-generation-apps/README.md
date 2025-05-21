<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-05-19T16:44:41+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hk"
}
-->
# 建立文本生成應用程式

[![建立文本生成應用程式](../../../translated_images/06-lesson-banner.90d8a665630e46b2990412d7c7d3d43c30f2441c95c0ee93e0763fb252734e83.hk.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(點擊上方圖片觀看本課程影片)_

到目前為止，透過這個課程，你已經看到一些核心概念，例如提示（prompts），甚至有一個名為「提示工程」的學科。許多工具，例如 ChatGPT、Office 365、Microsoft Power Platform 等，支持你使用提示來完成一些事情。

如果你想在應用程式中添加這樣的體驗，你需要了解提示、完成（completions）等概念，並選擇一個合適的庫來工作。這正是你在本章中將學習的內容。

## 介紹

在本章中，你將：

- 了解 openai 庫及其核心概念。
- 使用 openai 建立一個文本生成應用程式。
- 理解如何使用提示、溫度和令牌等概念來建立文本生成應用程式。

## 學習目標

在本課程結束時，你將能夠：

- 解釋什麼是文本生成應用程式。
- 使用 openai 建立一個文本生成應用程式。
- 配置你的應用程式以使用多或少的令牌，並改變溫度以獲得不同的輸出。

## 什麼是文本生成應用程式？

通常當你建立應用程式時，它會有一些界面，例如：

- 基於命令的。控制台應用程式是典型的應用程式，你輸入一個命令，它就執行一項任務。例如，`git` 是一個基於命令的應用程式。
- 用戶界面（UI）。一些應用程式有圖形用戶界面（GUI），你可以點擊按鈕、輸入文本、選擇選項等。

### 控制台和 UI 應用程式的局限性

與基於命令的應用程式相比，你輸入命令：

- **有限制**。你不能隨意輸入任何命令，只有應用程式支持的命令。
- **語言特定**。一些應用程式支持多種語言，但默認情況下，應用程式是為特定語言構建的，即使你可以添加更多語言支持。

### 文本生成應用程式的優勢

那麼文本生成應用程式有什麼不同呢？

在文本生成應用程式中，你有更多的靈活性，不受限於一組命令或特定的輸入語言。相反，你可以使用自然語言與應用程式互動。另一個好處是，由於你已經在與一個訓練過大量信息的數據源互動，而傳統應用程式可能僅限於數據庫中的內容。

### 我可以用文本生成應用程式建立什麼？

有很多東西可以建立。例如：

- **聊天機器人**。聊天機器人回答有關主題的問題，比如你的公司及其產品可能是一個不錯的選擇。
- **助手**。LLMs 在總結文本、從文本中獲取見解、生成文本如履歷等方面非常出色。
- **代碼助手**。根據你使用的語言模型，你可以建立一個幫助你編寫代碼的代碼助手。例如，你可以使用 GitHub Copilot 和 ChatGPT 等產品來幫助你編寫代碼。

## 我如何開始？

你需要找到一種方式與 LLM 集成，通常包括以下兩種方法：

- 使用 API。在這裡，你構建網絡請求並使用你的提示獲得生成的文本。
- 使用庫。庫幫助封裝 API 調用並使其更易於使用。

## 庫/SDK

有一些知名的庫可用於處理 LLM，例如：

- **openai**，這個庫使連接到你的模型並發送提示變得容易。

然後還有一些操作在更高層次的庫，例如：

- **Langchain**。Langchain 是眾所周知的並支持 Python。
- **Semantic Kernel**。Semantic Kernel 是 Microsoft 的庫，支持 C#、Python 和 Java 語言。

## 使用 openai 建立第一個應用程式

讓我們看看如何建立第一個應用程式，需要哪些庫，需要多少等。

### 安裝 openai

有很多庫可供與 OpenAI 或 Azure OpenAI 互動。可以使用多種編程語言，例如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` Python 庫，因此我們將使用 `pip` 來安裝它。

```bash
pip install openai
```

### 創建資源

你需要執行以下步驟：

- 在 Azure 上創建帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 獲得 Azure OpenAI 的訪問權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並請求訪問。

  > [!NOTE]
  > 在撰寫本文時，你需要申請 Azure OpenAI 的訪問權限。

- 安裝 Python <https://www.python.org/>
- 已創建 Azure OpenAI 服務資源。請參閱此指南了解如何 [創建資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰和端點

此時，你需要告訴你的 `openai` 庫使用哪個 API 金鑰。要找到你的 API 金鑰，請前往 Azure OpenAI 資源的「Keys and Endpoint」部分並複製「Key 1」的值。

![Azure Portal 中的 Keys and Endpoint 資源面板](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已經複製了這些信息，讓我們指導庫使用它。

> [!NOTE]
> 將你的 API 金鑰與代碼分開是值得的。你可以通過使用環境變量來做到這一點。
>
> - 設置環境變量 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### 設置 Azure 配置

如果你正在使用 Azure OpenAI，以下是設置配置的方法：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

上面我們設置了以下內容：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion` 類。以下是一個示例：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上述代碼中，我們創建了一個完成對象並傳入我們想使用的模型和提示。然後我們打印生成的文本。

### 聊天完成

到目前為止，你已經看到我們一直在使用 `Completion` to generate text. But there's another class called `ChatCompletion` 更適合聊天機器人。以下是使用它的示例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多關於此功能的內容將在接下來的章節中介紹。

## 練習 - 你的第一個文本生成應用程式

現在我們已經學習了如何設置和配置 openai，是時候建立你的第一個文本生成應用程式了。要建立你的應用程式，請遵循以下步驟：

1. 創建一個虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用 Windows，請輸入 `venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1` 的值。

1. 創建一個 _app.py_ 文件並給予以下代碼：

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
   > 如果你使用 Azure OpenAI，你需要設置 `api_type` to `azure` and set the `api_key` 為你的 Azure OpenAI 金鑰。

   你應該看到如下輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示，用於不同的事情

現在你已經看到如何使用提示生成文本。你甚至有一個運行中的程序，你可以修改和更改以生成不同類型的文本。

提示可以用於各種任務。例如：

- **生成某種類型的文本**。例如，你可以生成一首詩、測驗的問題等。
- **查詢信息**。你可以使用提示來查詢信息，例如以下示例「在網絡開發中 CORS 是什麼意思？」。
- **生成代碼**。你可以使用提示來生成代碼，例如開發用於驗證電子郵件的正則表達式，或者為什麼不生成整個程序，比如一個網絡應用程式？

## 一個更實際的使用案例：食譜生成器

想象一下你家裡有食材，你想做些什麼。為此，你需要一個食譜。一種查找食譜的方法是使用搜索引擎，或者你可以使用 LLM。

你可以寫一個提示如下：

> "顯示 5 個使用以下食材的菜餚食譜：雞肉、土豆和胡蘿蔔。每個食譜列出所有使用的食材"

根據上述提示，你可能會得到類似的回應：

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

這個結果很棒，我知道要做什麼菜了。此時，可能有用的改進是：

- 過濾掉我不喜歡或過敏的食材。
- 生成購物清單，以防我家裡沒有所有的食材。

針對上述情況，讓我們添加一個額外的提示：

> "請移除含有大蒜的食譜，因為我過敏，並用其他東西替代。此外，請根據我已經擁有的雞肉、土豆和胡蘿蔔，生成食譜的購物清單。"

現在你有了新的結果，即：

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

這就是你的五個食譜，沒有提到大蒜，並且你還有一個購物清單，考慮到你家裡已經有的食材。

## 練習 - 建立食譜生成器

現在我們已經演示了一個場景，讓我們編寫代碼來匹配演示的場景。為此，請遵循以下步驟：

1. 使用現有的 _app.py_ 文件作為起點
1. 找到 `prompt` 變量並將其代碼更改為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果你現在運行代碼，你應該看到類似的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > NOTE, 你的 LLM 是非確定性的，因此每次運行程序時，你可能會得到不同的結果。

   很好，讓我們看看如何改進。要改進，我們希望確保代碼是靈活的，因此食材和食譜數量可以改進和更改。

1. 讓我們以下列方式更改代碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   進行測試運行的代碼可能看起來像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通過添加過濾器和購物清單進行改進

我們現在有了一個可以生成食譜的工作應用程式，並且它是靈活的，因為它依賴於用戶的輸入，無論是食譜的數量還是使用的食材。

為了進一步改進，我們希望添加以下內容：

- **過濾掉食材**。我們希望能夠過濾掉我們不喜歡或過敏的食材。要完成此更改，我們可以編輯我們現有的提示並在末尾添加一個過濾條件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  在上面，我們在提示的末尾添加了 `{filter}`，並且我們還從用戶那裡獲取過濾器的值。

  運行程序的示例輸入現在可以看起來像這樣：

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

  如你所見，任何含有牛奶的食譜都已被過濾掉。但是，如果你對乳糖不耐受，你可能還想過濾掉含有奶酪的食譜，因此需要明確。

- **生成購物清單**。我們希望生成一個購物清單，考慮到我們家裡已經擁有的食材。

  對於此功能，我們可以嘗試在一個提示中解決所有問題，也可以將其分成兩個提示。讓我們嘗試後一種方法。在這裡，我們建議添加一個額外的提示，但要使其工作，我們需要將前一個提示的結果作為上下文添加到後一個提示中。

  找到代碼中打印第一個提示結果的部分，並在下面添加以下代碼：

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

  請注意以下內容：

  1. 我們通過將第一個提示的結果添加到新提示中來構建一個新提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們進行了一個新請求，但也考慮到我們在第一個提示中要求的令牌數量，因此這次我們說 `max_tokens` 是 1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     測試運行此代碼，我們現在得到以下輸出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善你的設置

到目前為止，我們有了可工作的代碼，但有一些調整我們應該做以進一步改善。我們應該做的一些事情是：

- **將秘密與代碼分開**，例如 API 金鑰。秘密不屬於代碼，應存儲在安全的位置。要將秘密與代碼分開，我們可以使用環境變量和庫，例如 `python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env` 文件，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Azure，你需要設置以下環境變量：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在代碼中，你可以像這樣加載環境變量：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **關於令牌長度的一個字**。我們應該考慮需要多少令牌來生成我們想要的文本。令牌是有成本的，因此在可能的情況下，我們應該嘗試節約使用的令牌數量。例如，我們能否重新措辭提示，以便使用更少的令牌？

  要更改使用的令牌數量，你可以使用 `max_tokens` 參數。例如，如果你想使用 100 個令牌，你可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **實驗溫度**。溫度是我們尚未提及的重要背景，對於我們的程序性能非常重要。溫度值越高，輸出越隨機。相反，溫度值越低，輸出越可預測。考慮你是否希望輸出有變化。

  要改變溫度，你可以使用 `temperature` 參數。例如，如果你想使用 0.5 的溫度，你可以這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，越接近 1.0，輸出越多樣化。

## 作業

對於這次作業，你可以選擇要建立什麼。

以下是一些建議：

- 調整食譜生成器應用程式以進一步改進。嘗試不同的溫度值，並查看你可以想出什麼樣的提示。
- 建立一個「學習助手」。這個應用程式應能回答有關主題的問題，例如 Python，你可以有類似「Python 中某個主題是什麼？」的提示，或者你可以有一個提示說，顯示某個主題的代碼等。
- 歷史機器人，讓歷史活起來，指導機器人扮演某個歷史角色，並詢問它有關其生活和時代的問題。

## 解決方案

### 學習助手

以下是一個起始提示，看看你如何使用並調整它以符合你的喜好。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

以下是一些你可以使用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢查

溫度概念是做什麼的？

1. 它控制輸出有多隨機。
1. 它控制回應的大小。
1. 它控制使用的令牌數量。

## 🚀 挑戰

**免責聲明**：  
本文件是使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。