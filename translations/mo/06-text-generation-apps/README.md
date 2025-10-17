<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "00e33cd3ff945511446ecda4a9f8a828",
  "translation_date": "2025-10-17T15:11:21+00:00",
  "source_file": "06-text-generation-apps/README.md",
  "language_code": "mo"
}
-->
# 建立文字生成應用程式

[![建立文字生成應用程式](../../../translated_images/06-lesson-banner.a5c629f990a636c852353c5533f1a6a218ece579005e91f96339d508d9cf8f47.mo.png)](https://youtu.be/0Y5Luf5sRQA?si=t_xVg0clnAI4oUFZ)

> _(點擊上方圖片觀看本課程的影片)_

在這份課程中，你已經了解了一些核心概念，例如提示（prompts），甚至還有一整個學科叫做「提示工程」（prompt engineering）。許多工具，例如 ChatGPT、Office 365、Microsoft Power Platform 等，都支持你使用提示來完成某些任務。

如果你想在應用程式中加入這樣的體驗，你需要了解提示、完成（completions）等概念，並選擇一個合適的庫來使用。本章節將教你如何做到這一點。

## 介紹

在本章節中，你將學到：

- 了解 openai 庫及其核心概念。
- 使用 openai 建立文字生成應用程式。
- 理解如何使用提示、溫度（temperature）和 tokens 等概念來建立文字生成應用程式。

## 學習目標

完成本課程後，你將能夠：

- 解釋什麼是文字生成應用程式。
- 使用 openai 建立文字生成應用程式。
- 配置你的應用程式以使用更多或更少的 tokens，並調整溫度以獲得多樣化的輸出。

## 什麼是文字生成應用程式？

通常在建立應用程式時，它會有某種介面，例如以下：

- 基於命令的介面。控制台應用程式是典型的應用程式，你輸入命令，它就執行任務。例如，`git` 是一個基於命令的應用程式。
- 使用者介面（UI）。一些應用程式有圖形使用者介面（GUI），你可以點擊按鈕、輸入文字、選擇選項等。

### 控制台和 UI 應用程式的限制

與基於命令的應用程式相比，限制如下：

- **有限性**。你不能隨意輸入任何命令，只能輸入應用程式支持的命令。
- **語言特定性**。有些應用程式支持多種語言，但通常應用程式是為特定語言設計的，即使可以添加更多語言支持。

### 文字生成應用程式的優勢

那麼文字生成應用程式有什麼不同呢？

在文字生成應用程式中，你有更多的靈活性，不受限於一組命令或特定的輸入語言。相反，你可以使用自然語言與應用程式互動。另一個優勢是，你正在與一個基於大量信息訓練的數據源互動，而傳統應用程式可能僅限於資料庫中的內容。

### 我可以用文字生成應用程式建立什麼？

你可以建立許多東西。例如：

- **聊天機器人**。一個回答有關公司及其產品問題的聊天機器人可能是一個不錯的選擇。
- **助手**。大型語言模型（LLM）在摘要文字、從文字中獲取洞察、生成簡歷等方面非常出色。
- **程式碼助手**。根據你使用的語言模型，你可以建立一個幫助你編寫程式碼的助手。例如，你可以使用 GitHub Copilot 或 ChatGPT 來幫助你編寫程式碼。

## 我該如何開始？

你需要找到與 LLM 整合的方法，通常有以下兩種方式：

- 使用 API。你可以構建包含提示的網路請求，並獲得生成的文字。
- 使用庫。庫可以封裝 API 調用，使其更易於使用。

## 庫/SDK

有一些知名的庫可以用來與 LLM 互動，例如：

- **openai**，這個庫使得連接到模型並發送提示變得非常簡單。

此外，還有一些操作層級更高的庫，例如：

- **Langchain**。Langchain 是一個知名的庫，支持 Python。
- **Semantic Kernel**。Semantic Kernel 是 Microsoft 的一個庫，支持 C#、Python 和 Java。

## 使用 openai 建立第一個應用程式

讓我們來看看如何建立第一個應用程式，所需的庫、步驟等。

### 安裝 openai

有許多庫可以用來與 OpenAI 或 Azure OpenAI 互動。可以使用多種程式語言，例如 C#、Python、JavaScript、Java 等。我們選擇使用 `openai` 的 Python 庫，因此我們將使用 `pip` 來安裝它。

```bash
pip install openai
```

### 建立資源

你需要完成以下步驟：

- 在 Azure 上建立帳戶 [https://azure.microsoft.com/free/](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
- 獲得 Azure OpenAI 的訪問權限。前往 [https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai](https://learn.microsoft.com/azure/ai-services/openai/overview#how-do-i-get-access-to-azure-openai?WT.mc_id=academic-105485-koreyst) 並申請訪問。

  > [!NOTE]
  > 在撰寫本文時，你需要申請訪問 Azure OpenAI。

- 安裝 Python <https://www.python.org/>
- 建立 Azure OpenAI Service 資源。請參閱此指南了解如何 [建立資源](https://learn.microsoft.com/azure/ai-services/openai/how-to/create-resource?pivots=web-portal?WT.mc_id=academic-105485-koreyst)。

### 找到 API 金鑰和端點

此時，你需要告訴 `openai` 庫使用哪個 API 金鑰。要找到你的 API 金鑰，請前往 Azure OpenAI 資源的「金鑰和端點」部分，並複製「金鑰 1」的值。

![Azure Portal 中的金鑰和端點資源頁面](https://learn.microsoft.com/azure/ai-services/openai/media/quickstarts/endpoint.png?WT.mc_id=academic-105485-koreyst)

現在你已經複製了這些信息，讓我們指導庫使用它。

> [!NOTE]
> 建議將 API 金鑰與程式碼分開。你可以使用環境變數來做到這一點。
>
> - 設置環境變數 `OPENAI_API_KEY` 為你的 API 金鑰。
>   `export OPENAI_API_KEY='sk-...'`

### 配置 Azure

如果你使用 Azure OpenAI，以下是配置方法：

```python
openai.api_type = 'azure'
openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_version = '2023-05-15'
openai.api_base = os.getenv("API_BASE")
```

以上我們設置了以下內容：

- `api_type` 設置為 `azure`。這告訴庫使用 Azure OpenAI 而不是 OpenAI。
- `api_key`，這是你在 Azure Portal 中找到的 API 金鑰。
- `api_version`，這是你想使用的 API 版本。在撰寫本文時，最新版本是 `2023-05-15`。
- `api_base`，這是 API 的端點。你可以在 Azure Portal 中的 API 金鑰旁邊找到它。

> [!NOTE] > `os.getenv` 是一個讀取環境變數的函數。你可以使用它來讀取像 `OPENAI_API_KEY` 和 `API_BASE` 這樣的環境變數。在終端中設置這些環境變數，或者使用像 `dotenv` 這樣的庫。

## 生成文字

生成文字的方法是使用 `Completion` 類。以下是一個範例：

```python
prompt = "Complete the following: Once upon a time there was a"

completion = openai.Completion.create(model="davinci-002", prompt=prompt)
print(completion.choices[0].text)
```

在上述程式碼中，我們建立了一個完成物件，並傳入我們想使用的模型和提示。然後我們打印出生成的文字。

### 聊天完成

到目前為止，你已經看到我們如何使用 `Completion` 來生成文字。但還有另一個更適合聊天機器人的類別，叫做 `ChatCompletion`。以下是一個使用範例：

```python
import openai

openai.api_key = "sk-..."

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
print(completion.choices[0].message.content)
```

更多相關功能將在後續章節中介紹。

## 練習 - 建立你的第一個文字生成應用程式

現在我們已經學會了如何設置和配置 openai，是時候建立你的第一個文字生成應用程式了。按照以下步驟來建立你的應用程式：

1. 建立虛擬環境並安裝 openai：

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install openai
   ```

   > [!NOTE]
   > 如果你使用 Windows，請輸入 `venv\Scripts\activate` 而不是 `source venv/bin/activate`。

   > [!NOTE]
   > 通過前往 [https://portal.azure.com/](https://portal.azure.com/?WT.mc_id=academic-105485-koreyst) 並搜索 `Open AI`，選擇 `Open AI 資源`，然後選擇 `金鑰和端點`，複製 `金鑰 1` 的值來找到你的 Azure OpenAI 金鑰。

1. 建立一個 _app.py_ 文件，並輸入以下程式碼：

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
   > 如果你使用 Azure OpenAI，你需要將 `api_type` 設置為 `azure`，並將 `api_key` 設置為你的 Azure OpenAI 金鑰。

   你應該會看到類似以下的輸出：

   ```output
    very unhappy _____.

   Once upon a time there was a very unhappy mermaid.
   ```

## 不同類型的提示，用於不同的用途

現在你已經看到如何使用提示生成文字。你甚至已經有一個可以運行的程式，並且可以修改和更改它來生成不同類型的文字。

提示可以用於各種任務。例如：

- **生成某種類型的文字**。例如，你可以生成詩歌、測驗問題等。
- **查詢信息**。你可以使用提示來查詢信息，例如「在網頁開發中，CORS 是什麼意思？」。
- **生成程式碼**。你可以使用提示來生成程式碼，例如開發用於驗證電子郵件的正則表達式，或者甚至生成整個程式，例如網頁應用程式。

## 更實用的案例：食譜生成器

想像一下，你家裡有一些食材，想要做些菜。為此，你需要一份食譜。一種找到食譜的方法是使用搜索引擎，或者你可以使用 LLM。

你可以寫一個像這樣的提示：

> 「列出使用以下食材的五道菜的食譜：雞肉、馬鈴薯和胡蘿蔔。每道食譜列出所有使用的食材。」

根據上述提示，你可能會得到類似以下的回應：

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

這個結果很棒，我知道該做什麼菜了。此時，可能有一些有用的改進：

- 過濾掉我不喜歡或過敏的食材。
- 生成購物清單，以防我家裡沒有所有的食材。

針對上述情況，我們可以添加一個額外的提示：

> 「請移除含有大蒜的食譜，因為我對大蒜過敏，並用其他東西替代。此外，請根據我家裡已有的雞肉、馬鈴薯和胡蘿蔔生成購物清單。」

現在你會得到一個新的結果，即：

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

這就是你的五道食譜，沒有提到大蒜，並且還有一份考慮到你家裡已有食材的購物清單。

## 練習 - 建立食譜生成器

現在我們已經模擬了一個場景，讓我們編寫程式碼來匹配展示的場景。按照以下步驟操作：

1. 使用現有的 _app.py_ 文件作為起點
1. 找到 `prompt` 變數並將其程式碼更改為以下內容：

   ```python
   prompt = "Show me 5 recipes for a dish with the following ingredients: chicken, potatoes, and carrots. Per recipe, list all the ingredients used"
   ```

   如果你現在運行程式碼，你應該會看到類似以下的輸出：

   ```output
   -Chicken Stew with Potatoes and Carrots: 3 tablespoons oil, 1 onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 1/2 cups chicken broth, 1/2 cup dry white wine, 2 tablespoons chopped fresh parsley, 2 tablespoons unsalted butter, 1 1/2 pounds boneless, skinless chicken thighs, cut into 1-inch pieces
   -Oven-Roasted Chicken with Potatoes and Carrots: 3 tablespoons extra-virgin olive oil, 1 tablespoon Dijon mustard, 1 tablespoon chopped fresh rosemary, 1 tablespoon chopped fresh thyme, 4 cloves garlic, minced, 1 1/2 pounds small red potatoes, quartered, 1 1/2 pounds carrots, quartered lengthwise, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 1 (4-pound) whole chicken
   -Chicken, Potato, and Carrot Casserole: cooking spray, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and shredded, 1 potato, peeled and shredded, 1/2 teaspoon dried thyme leaves, 1/4 teaspoon salt, 1/4 teaspoon black pepper, 2 cups fat-free, low-sodium chicken broth, 1 cup frozen peas, 1/4 cup all-purpose flour, 1 cup 2% reduced-fat milk, 1/4 cup grated Parmesan cheese

   -One Pot Chicken and Potato Dinner: 2 tablespoons olive oil, 1 pound boneless, skinless chicken thighs, cut into 1-inch pieces, 1 large onion, chopped, 3 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 bay leaf, 1 thyme sprig, 1/2 teaspoon salt, 1/4 teaspoon black pepper, 2 cups chicken broth, 1/2 cup dry white wine

   -Chicken, Potato, and Carrot Curry: 1 tablespoon vegetable oil, 1 large onion, chopped, 2 cloves garlic, minced, 1 carrot, peeled and chopped, 1 potato, peeled and chopped, 1 teaspoon ground coriander, 1 teaspoon ground cumin, 1/2 teaspoon ground turmeric, 1/2 teaspoon ground ginger, 1/4 teaspoon cayenne pepper, 2 cups chicken broth, 1/2 cup dry white wine, 1 (15-ounce) can chickpeas, drained and rinsed, 1/2 cup raisins, 1/2 cup chopped fresh cilantro
   ```

   > 注意，LLM 是非確定性的，因此每次運行程式時可能會得到不同的結果。

   很棒，讓我們看看如何改進。為了改進，我們希望確保程式碼是靈活的，因此食材和食譜數量可以改進和更改。

1. 讓我們以以下方式更改程式碼：

   ```python
   no_recipes = input("No of recipes (for example, 5): ")

   ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")

   # interpolate the number of recipes into the prompt an ingredients
   prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used"
   ```

   測試程式碼的運行可能看起來像這樣：

   ```output
   No of recipes (for example, 5): 3
   List of ingredients (for example, chicken, potatoes, and carrots): milk,strawberries

   -Strawberry milk shake: milk, strawberries, sugar, vanilla extract, ice cubes
   -Strawberry shortcake: milk, flour, baking powder, sugar, salt, unsalted butter, strawberries, whipped cream
   -Strawberry milk: milk, strawberries, sugar, vanilla extract
   ```

### 通過添加過濾器和購物清單進一步改進

我們現在有一個能夠生成食譜的應用程式，並且它是靈活的，因為它依賴於使用者的輸入，包括食譜數量和使用的食材。

為了進一步改進，我們希望添加以下功能：

- **過濾掉食材**。我們希望能夠過濾掉我們不喜歡或過敏的食材。為了實現這一改變，我們可以編輯現有的提示，並在其末尾添加過濾條件，例如：

  ```python
  filter = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

  prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter}"
  ```

  上述程式碼中，我們在提示末尾添加了 `{filter}`，並且還從使用者那裡獲取了過濾值。

  程式運行的示例輸入現在可能看起來像這樣：

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

  如你所見，任何含有牛奶的食譜都被過濾掉了。但是，如果你對乳糖不耐受，你可能還希望過濾掉含有奶酪的食譜，因此需要明確指出。

- **生成購物清單**。我們希望生成一份購物清單，考慮到我們家裡已有的食材。

  對於此功能，我們可以嘗試在一個提示中解決所有問題，或者將其分成兩個提示。讓我們嘗試後者方法。這裡建議添加一個額外的提示，但為了使其工作，我們需要將前一個提示的結果作為上下文添加到後一個提示中。
在程式碼中找到列印第一個提示結果的部分，並在其下方新增以下程式碼：

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

請注意以下事項：

1. 我們透過將第一個提示的結果加入新的提示來構建新的提示：

     ```python
     new_prompt = f"{old_prompt_result} {prompt}"
     ```

1. 我們進行新的請求，但也考慮到第一個提示中要求的 token 數量，因此這次我們將 `max_tokens` 設定為 1200。

     ```python
     completion = openai.Completion.create(engine=deployment_name, prompt=new_prompt, max_tokens=1200)
     ```

執行這段程式碼後，我們得到以下輸出：

     ```output
     No of recipes (for example, 5): 2
     List of ingredients (for example, chicken, potatoes, and carrots): apple,flour
     Filter (for example, vegetarian, vegan, or gluten-free): sugar


     -Apple and flour pancakes: 1 cup flour, 1/2 tsp baking powder, 1/2 tsp baking soda, 1/4 tsp salt, 1 tbsp sugar, 1 egg, 1 cup buttermilk or sour milk, 1/4 cup melted butter, 1 Granny Smith apple, peeled and grated
     -Apple fritters: 1-1/2 cups flour, 1 tsp baking powder, 1/4 tsp salt, 1/4 tsp baking soda, 1/4 tsp nutmeg, 1/4 tsp cinnamon, 1/4 tsp allspice, 1/4 cup sugar, 1/4 cup vegetable shortening, 1/4 cup milk, 1 egg, 2 cups shredded, peeled apples
     Shopping list:
     -Flour, baking powder, baking soda, salt, sugar, egg, buttermilk, butter, apple, nutmeg, cinnamon, allspice
     ```

## 改善您的設置

目前我們的程式碼可以運作，但仍有一些調整可以進一步改善。以下是一些建議：

- **將機密資訊與程式碼分離**，例如 API 金鑰。機密資訊不應該直接寫在程式碼中，應存放在安全的位置。為了將機密資訊與程式碼分離，我們可以使用環境變數以及像 `python-dotenv` 這樣的庫來從檔案中載入它們。以下是程式碼範例：

  1. 建立 `.env` 檔案，內容如下：

     ```bash
     OPENAI_API_KEY=sk-...
     ```

     > 注意，對於 Azure，您需要設定以下環境變數：

     ```bash
     OPENAI_API_TYPE=azure
     OPENAI_API_VERSION=2023-05-15
     OPENAI_API_BASE=<replace>
     ```

     在程式碼中，您可以這樣載入環境變數：

     ```python
     from dotenv import load_dotenv

     load_dotenv()

     openai.api_key = os.environ["OPENAI_API_KEY"]
     ```

- **關於 token 長度的建議**。我們應該考慮生成所需文字所需的 token 數量。token 是有成本的，因此我們應盡量節省使用的 token 數量。例如，我們是否可以重新措辭提示以使用更少的 token？

  若要更改使用的 token 數量，您可以使用 `max_tokens` 參數。例如，若您希望使用 100 個 token，您可以這樣設定：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=100)
  ```

- **嘗試調整溫度值**。溫度值是我們尚未提及但對程式表現非常重要的上下文。溫度值越高，輸出越隨機；溫度值越低，輸出越可預測。考慮您是否希望輸出具有變化性。

  若要調整溫度值，您可以使用 `temperature` 參數。例如，若您希望使用 0.5 的溫度值，您可以這樣設定：

  ```python
  completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.5)
  ```

  > 注意，溫度值越接近 1.0，輸出越多樣化。

## 作業

在這次作業中，您可以選擇要建構的內容。

以下是一些建議：

- 調整食譜生成器應用程式以進一步改善。嘗試不同的溫度值以及提示，看看能產生什麼結果。
- 建構一個「學習夥伴」。這個應用程式應能回答有關某個主題的問題，例如 Python，您可以使用提示如「Python 中某個主題是什麼？」或者「顯示某個主題的程式碼」等。
- 歷史機器人，讓歷史活起來，指示機器人扮演某個歷史人物並向它提問有關其生活和時代的問題。

## 解決方案

### 學習夥伴

以下是一個起始提示，看看您如何使用並調整它以符合您的需求。

```text
- "You're an expert on the Python language

    Suggest a beginner lesson for Python in the following format:

    Format:
    - concepts:
    - brief explanation of the lesson:
    - exercise in code with solutions"
```

### 歷史機器人

以下是一些您可以使用的提示：

```text
- "You are Abe Lincoln, tell me about yourself in 3 sentences, and respond using grammar and words like Abe would have used"
- "You are Abe Lincoln, respond using grammar and words like Abe would have used:

   Tell me about your greatest accomplishments, in 300 words"
```

## 知識檢查

溫度值的概念是什麼？

1. 它控制輸出的隨機性。
1. 它控制回應的大小。
1. 它控制使用的 token 數量。

## 🚀 挑戰

在完成作業時，嘗試調整溫度值，嘗試設定為 0、0.5 和 1。記住，0 是最不多樣化的，1 是最多樣化的。哪個值最適合您的應用程式？

## 很棒的工作！繼續學習

完成本課程後，請查看我們的 [生成式 AI 學習系列](https://aka.ms/genai-collection?WT.mc_id=academic-105485-koreyst)，繼續提升您的生成式 AI 知識！

前往第 7 課，我們將探討如何 [建構聊天應用程式](../07-building-chat-applications/README.md?WT.mc_id=academic-105485-koreyst)！

---

**免責聲明**：  
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。