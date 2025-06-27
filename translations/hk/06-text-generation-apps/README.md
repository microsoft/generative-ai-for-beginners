<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5ec6c92b629564538ef397c550adb73e",
  "translation_date": "2025-06-25T14:04:39+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "hk"
}
-->
# 構建文字生成應用程式

[![構建文字生成應用程式](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.hk.png)](https://aka.ms/gen-ai-lesson6-gh?WT.mc_id=academic-105485-koreyst)

> _(點擊上面的圖片觀看本課程的視頻)_

在這個課程中，你已經看到了一些核心概念，比如提示詞，甚至有一個整個學科叫做「提示詞工程」。許多你可以互動的工具，比如ChatGPT、Office 365、Microsoft Power Platform等，支持你使用提示詞來完成一些事情。

要將這樣的體驗添加到應用程式中，你需要理解提示詞、完成等概念，並選擇一個庫來使用。這正是你在本章中將學到的內容。

## 介紹

在本章中，你將：

- 了解openai庫及其核心概念。
- 使用openai構建文字生成應用程式。
- 理解如何使用提示詞、溫度和令牌等概念來構建文字生成應用程式。

## 學習目標

在本課程結束時，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用openai構建文字生成應用程式。
- 配置你的應用程式以使用更多或更少的令牌，並改變溫度，以獲得多樣化的輸出。

## 什麼是文字生成應用程式？

通常當你構建應用程式時，它會有某種界面，如下所示：

- 基於命令。控制台應用程式是典型的應用程式，你輸入一個命令，它就會執行一個任務。例如，`git` 是一個基於命令的應用程式。
- 用戶界面（UI）。有些應用程式有圖形用戶界面（GUI），你可以點擊按鈕、輸入文本、選擇選項等。

### 控制台和UI應用程式的限制

與基於命令的應用程式相比，你輸入命令：

- **有限制**。你不能隨便輸入任何命令，只能輸入應用程式支持的命令。
- **語言特定**。有些應用程式支持多種語言，但默認情況下應用程式是為特定語言構建的，即使你可以添加更多語言支持。

### 文字生成應用程式的好處

那麼文字生成應用程式有什麼不同呢？

在文字生成應用程式中，你有更多的靈活性，不受限於一組命令或特定的輸入語言。相反，你可以使用自然語言來與應用程式互動。另一個好處是，你已經在與一個已經訓練了大量信息的數據源互動，而傳統的應用程式可能受限於數據庫中的內容。

### 我可以用文字生成應用程式構建什麼？

你可以構建很多東西。例如：

- **聊天機器人**。一個回答問題的聊天機器人，關於你的公司及其產品等主題可能是一個不錯的選擇。
- **助手**。LLM在總結文本、從文本中獲取洞察、生成簡歷等方面非常出色。
- **代碼助手**。根據你使用的語言模型，你可以構建一個幫助你編寫代碼的助手。例如，你可以使用GitHub Copilot以及ChatGPT來幫助你編寫代碼。

## 我怎樣才能開始？

好吧，你需要找到一種方法來與LLM集成，通常涉及以下兩種方法：

- 使用API。在這裡，你構建帶有提示詞的網絡請求並獲得生成的文本。
- 使用庫。庫幫助封裝API調用，使其更易於使用。

## 庫/SDK

有一些知名的庫可以用於處理LLM，例如：

- **openai**，這個庫使得連接到你的模型並發送提示詞變得容易。

然後有一些在更高層次上運作的庫，例如：

- **Langchain**。Langchain廣為人知，支持Python。
- **Semantic Kernel**。Semantic Kernel是Microsoft的一個庫，支持C#、Python和Java語言。

## 使用openai的第一個應用程式

讓我們看看如何構建我們的第一個應用程式，需要哪些庫，需要多少等等。

### 安裝openai

有許多庫可以與OpenAI或Azure OpenAI互動。可以使用多種編程語言，如C#、Python、JavaScript、Java等。我們選擇使用`openai` Python庫，因此我們將使用`pip`來安裝它。

```bash
pip install openai
```

### 創建資源

你需要執行以下步驟：

- 在Azure上創建帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 獲得Azure OpenAI的訪問權限。前往[https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst)並申請訪問。

  > [!NOTE]
  > 在撰寫本文時，你需要申請訪問Azure OpenAI。

- 安裝Python <https://www.python.org/>
- 創建一個Azure OpenAI服務資源。查看此指南以了解如何[創建資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 查找API密鑰和端點

此時，你需要告訴你的`openai`庫使用哪個API密鑰。要找到你的API密鑰，請前往Azure OpenAI資源的「密鑰和端點」部分並複製「密鑰1」的值。

![Azure Portal中的密鑰和端點資源刀片](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已經複製了這些信息，讓我們指示庫使用它。

> [!NOTE]
> 將API密鑰與代碼分開是值得的。你可以通過使用環境變數來做到這一點。
>
> - 設置環境變數 `OPENAI_API_KEY` to your API key.
>   `export OPENAI_API_KEY='sk-...'`

### 設置Azure配置

如果你使用的是Azure OpenAI，這裡是如何設置配置：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

以上我們設置了以下內容：

- `api_type` to `azure`. This tells the library to use Azure OpenAI and not OpenAI.
- `api_key`, this is your API key found in the Azure Portal.
- `api_version`, this is the version of the API you want to use. At the time of writing, the latest version is `2023-05-15`.
- `api_base`, this is the endpoint of the API. You can find it in the Azure Portal next to your API key.

> [!NOTE] > `os.getenv` is a function that reads environment variables. You can use it to read environment variables like `OPENAI_API_KEY` and `API_BASE`. Set these environment variables in your terminal or by using a library like `dotenv`.

## Generate text

The way to generate text is to use the `Completion`類。這裡是一個例子：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上面的代碼中，我們創建了一個完成對象，並傳入我們想使用的模型和提示詞。然後我們打印生成的文本。

### 聊天完成

到目前為止，你已經看到我們一直在使用`Completion` to generate text. But there's another class called `ChatCompletion`，它更適合聊天機器人。這裡是使用它的一個例子：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多關於此功能的內容在接下來的章節中。

## 練習 - 你的第一個文字生成應用程式

現在我們學習了如何設置和配置openai，是時候構建你的第一個文字生成應用程式了。要構建你的應用程式，請按照以下步驟：

1. 創建虛擬環境並安裝openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用的是Windows，請輸入`venv\Scripts\activate` instead of `source venv/bin/activate`.

   > [!NOTE]
   > Locate your Azure OpenAI key by going to [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) and search for `Open AI` and select the `Open AI resource` and then select `Keys and Endpoint` and copy the `Key 1`值。

1. 創建一個_app.py_文件並給它以下代碼：

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
   > 如果你使用的是Azure OpenAI，你需要將`api_type` to `azure` and set the `api_key`設置為你的Azure OpenAI密鑰。

   你應該看到如下輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示詞，用於不同的事情

現在你已經看到如何使用提示詞生成文本。你甚至有一個正在運行的程序，你可以修改和更改以生成不同類型的文本。

提示詞可以用於各種任務。例如：

- **生成一種文本**。例如，你可以生成一首詩、測驗問題等。
- **查詢信息**。你可以使用提示詞查找信息，比如下面的例子「在網絡開發中CORS是什麼意思？」。
- **生成代碼**。你可以使用提示詞生成代碼，例如開發用於驗證電子郵件的正則表達式，或者為什麼不生成整個程序，比如一個網絡應用程式？

## 更實際的用例：食譜生成器

想像一下你家裡有食材，想做點什麼。為此，你需要一個食譜。一種找到食譜的方法是使用搜索引擎，或者你可以使用LLM來做到這一點。

你可以寫一個提示詞，如下所示：

> 「給我展示5個包含以下食材的菜餚食譜：雞肉、馬鈴薯和胡蘿蔔。每個食譜列出所有使用的食材」

根據上述提示詞，你可能會得到類似的響應：

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

這個結果很好，我知道該做什麼菜。此時，可能有用的改進是：

- 篩選掉我不喜歡或過敏的食材。
- 生成購物清單，以防我家裡沒有所有的食材。

對於上述情況，讓我們添加一個額外的提示詞：

> 「請移除含有大蒜的食譜，因為我過敏，並用其他東西替換它。另外，請為食譜生成購物清單，考慮到我已經有雞肉、馬鈴薯和胡蘿蔔。」

現在你有了一個新結果，即：

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

這就是你的五個食譜，沒有提到大蒜，你還有一個考慮到你家裡已有食材的購物清單。

## 練習 - 構建食譜生成器

現在我們已經演示了一個場景，讓我們編寫代碼來匹配演示的場景。要做到這一點，請按照以下步驟：

1. 使用現有的_app.py_文件作為起點
1. 找到`prompt`變量並將其代碼更改為以下內容：

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

   > 注意，你的LLM是非確定性的，因此每次運行程序可能會得到不同的結果。

   很好，讓我們看看如何改進。我們希望確保代碼是靈活的，因此食材和食譜數量可以改進和更改。

1. 讓我們以以下方式更改代碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試運行代碼，可能看起來像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通過添加篩選器和購物清單來改進

我們現在有一個能夠生成食譜的工作應用程式，它是靈活的，因為它依賴於用戶的輸入，不僅在食譜數量上，而且在使用的食材上。

為了進一步改進，我們希望添加以下內容：

- **篩選掉食材**。我們希望能夠篩選掉我們不喜歡或過敏的食材。要完成此更改，我們可以編輯我們現有的提示詞，並在其末尾添加一個篩選條件，如下所示：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上面，我們在提示詞的末尾添加了`{filter}`，我們還從用戶那裡捕獲了篩選值。

  運行程序的示例輸入現在可能看起來像這樣：

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

  如你所見，任何含有牛奶的食譜都已被篩選掉。但是，如果你乳糖不耐受，你可能還想篩選掉含有奶酪的食譜，因此需要明確。

- **生成購物清單**。我們希望生成購物清單，考慮到我們家裡已有的食材。

  對於此功能，我們可以嘗試在一個提示詞中解決所有問題，或者可以將其分成兩個提示詞。讓我們嘗試後者的方法。這裡我們建議添加一個額外的提示詞，但為了使其工作，我們需要將前一個提示詞的結果作為上下文添加到後一個提示詞中。

  找到代碼中打印出第一個提示詞結果的部分，並在其下添加以下代碼：

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

  注意以下事項：

  1. 我們通過將第一個提示詞的結果添加到新的提示詞中來構建一個新的提示詞：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

  1. 我們進行新的請求，但也考慮到我們在第一個提示詞中要求的令牌數量，因此這次我們說`max_tokens`是1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

     進行此代碼測試運行，我們現在得到了以下輸出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改進你的設置

到目前為止，我們的代碼是有效的，但有一些調整我們應該做以進一步改進。一些我們應該做的事情是：

- **將秘密與代碼分開**，例如API密鑰。秘密不屬於代碼，應存儲在安全位置。要將秘密與代碼分開，我們可以使用環境變數和庫，如`python-dotenv` to load them from a file. Here's how that would look like in code:

  1. Create a `.env`文件，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於Azure，你需要設置以下環境變數：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在代碼中，你會這樣加載環境變數：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **關於令牌長度的一句話**。我們應該考慮需要多少令牌來生成我們想要的文本。令牌是要花錢的，因此在可能的情況下，我們應該盡量節約使用令牌的數量。例如，我們能否以使用更少令牌的方式來措辭提示詞？

  要更改使用的令牌數量，你可以使用`max_tokens`參數。例如，如果你想使用100個令牌，你會這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **試驗溫度**。溫度是我們迄今為止未提及的內容，但它對我們程序的性能非常重要。溫度值越高，輸出就越隨機。相反，溫度值越低，輸出就越可預測。考慮你是否希望輸出有變化。

  要改變溫度，你可以使用`temperature`參數。例如，如果你想使用0.5的溫度，你會這樣做：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，越接近1.0，輸出就越多樣化。

## 作業

對於這個作業，你可以選擇構建什麼。

以下是一些建議：

- 調整食譜生成器應用程式以進一步改進。試試不同的溫度值和提示詞，看看你能做出什麼。
- 構建一個「學習夥伴」。這個應用程式應該能夠回答關於某個主題的問題，例如Python，你可以有類似「Python中的某個主題是什麼？」的提示詞，或者你可以有一個提示詞說，給我展示某個主題的代碼等。
- 歷史機器人，讓歷史活起來，指示機器人扮演某個歷史角色並詢問它關於其生活和時代的問題。

## 解決方案

### 學習夥伴

下面是一個起始提示詞，看看你如何使用它並根據你的喜好進行調整。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

以下是一些你可以使用的提示詞：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢查

溫度的概念是什麼？

1. 它控制輸出的隨機性。
1

**免責聲明**:  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們不對使用此翻譯所引起的任何誤解或誤釋承擔責任。